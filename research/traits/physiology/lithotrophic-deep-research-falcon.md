---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:40:44.144586'
end_time: '2026-06-18T12:01:25.731806'
duration_seconds: 1241.59
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: lithotrophic
  trait_identifier: METPO:1000649
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: lithotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism uses inorganic compounds as electron
    donors for energy generation.
  parent_traits: METPO:1000631
  synonyms: TT_lithotroph, lithotroph
  evidence_summary: 'DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms
    or molecules (Encyclopedia review supports inorganic compounds as growth-supporting
    reductants and energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: generation
    of an electrochemical ion gradient (Review supports respiratory energy conservation
    through ion gradients and ATP synthesis.)'
  causal_graph_summary: 'lithotrophic_inorganic_donor_energy: 7 nodes, 6 edges'
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
- **Trait label:** lithotrophic
- **METPO identifier:** METPO:1000649
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses inorganic compounds as electron donors for energy generation.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_lithotroph, lithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Encyclopedia review supports inorganic compounds as growth-supporting reductants and energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: generation of an electrochemical ion gradient (Review supports respiratory energy conservation through ion gradients and ATP synthesis.)
- **Existing causal graph summary:** lithotrophic_inorganic_donor_energy: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **lithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithotrophic.yaml`.

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
- **Trait label:** lithotrophic
- **METPO identifier:** METPO:1000649
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses inorganic compounds as electron donors for energy generation.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_lithotroph, lithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Encyclopedia review supports inorganic compounds as growth-supporting reductants and energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: generation of an electrochemical ion gradient (Review supports respiratory energy conservation through ion gradients and ATP synthesis.)
- **Existing causal graph summary:** lithotrophic_inorganic_donor_energy: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **lithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithotrophic.yaml`.

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


## Microbial trait causal graph curation report: **lithotrophic** (METPO:1000649)

### 1) Scope summary (TraitMech curation)
**Trait definition (METPO:1000649):** lithotrophic organisms use **inorganic compounds as electron donors** to generate energy. In practice, lithotrophy is best curated as a **physiological energy strategy**: oxidation of inorganic electron donors supplies electrons into an electron-transfer chain (often quinone-linked), enabling **energy conservation** (commonly via chemiosmotic proton motive force and ATP synthesis). Lithotrophy can pair with **autotrophy** (CO2 fixation; “chemolithoautotrophy”) or with uptake/assimilation of organic carbon (“chemolithoheterotrophy”), and many taxa show **mixotrophy** or conditional switching. For example, *Acidithiobacillus ferrooxidans* is a chemolithoautotroph using Fe(II) and reduced inorganic sulfur compounds (RISCs) as energy sources while fixing CO2 via the CBB cycle (wang2024characterizethegrowth pages 1-2). Likewise, *Sideroxydans* sp. CL21 can grow on organics yet also oxidize inorganic substrates (Fe(II), magnetite, thiosulfate, S(0)), illustrating boundary cases where “lithotrophic capacity” and “lithotrophic activity” must be distinguished (hoover2025anorganotrophicsideroxydans pages 1-2).

**Boundary distinctions important for curation**
- **Lithotrophy vs organotrophy:** electron donors are inorganic vs organic; however, strains can be facultative/mixotrophic, so assays/transcriptomics may be needed to distinguish activity (hoover2025anorganotrophicsideroxydans pages 1-2).
- **Chemolithotrophy vs photolithotrophy:** photolithotrophy uses inorganic donors but light-driven energy conservation; the METPO term here targets **inorganic donor use for energy generation** rather than light capture.
- **Lithotrophy vs electrotrophy/electroautotrophy:** electrode-derived electrons can substitute for soluble inorganic donors; *A. ferrooxidans* shows electroautotrophy with altered expression of transmembrane proteins/pili/EPS compared to Fe(II)-based chemolithoautotrophy (wang2024characterizethegrowth pages 1-2).

### 2) Key concepts and current mechanistic understanding
#### 2.1 Conceptual mechanism (general)
A curation-useful abstraction is:
1) **Inorganic electron donor oxidation** (e.g., H2, Fe(II), sulfide/thiosulfate, NH3)
2) **Electron transfer to carriers** (often to a quinone pool or cytochromes)
3) **Terminal electron acceptor reduction** (commonly O2; also nitrate, Mn(IV), Fe(III) in some sulfur oxidizers)
4) **Energy conservation** by generating a transmembrane electrochemical gradient (pmf) that drives **ATP synthesis**.

This sequence is explicitly demonstrated for atmospheric H2 oxidation in a minimal reconstituted respiratory chain: H2 oxidation by hydrogenase → quinone reduction → terminal oxidase → pmf → ATP synthase → ATP (soom2025hydrogenasedrivenatpsynthesis pages 1-4, soom2025hydrogenasedrivenatpsynthesis pages 7-11, soom2025hydrogenasedrivenatpsynthesis pages 4-7).

#### 2.2 Hydrogen lithotrophy (high-affinity/trace-gas “aerotrophy”)
A major 2023 advance is the structural mechanism for **atmospheric H2 oxidation** in *Mycobacterium smegmatis*. The high-affinity [NiFe]-hydrogenase **Huc** “couples oxidation of atmospheric H2 to the hydrogenation of the respiratory electron carrier menaquinone” (grinter2023structuralbasisfor pages 1-2). The associated figure provides a mechanistic model of electron transfer from H2 oxidation through Fe–S clusters to menaquinone, including quinone extraction/transport via a membrane-associated stalk (grinter2023structuralbasisfor media c56ed0f4, grinter2023structuralbasisfor media 7212eac1).

A 2025 study (preprint) further provides a direct **energy-conservation** demonstration: Huc-driven quinone reduction can be coupled to a terminal oxidase to generate a **pmf** and drive **ATP synthesis**, including ATP formation even from open-air (atmospheric) H2 (soom2025hydrogenasedrivenatpsynthesis pages 7-11, soom2025hydrogenasedrivenatpsynthesis pages 4-7). This provides unusually direct support for core “lithotrophic donor → respiratory chain → ATP” edges.

#### 2.3 Sulfur lithotrophy
Sulfur-oxidizing lithotrophy uses reduced inorganic sulfur compounds (RISCs) as donors and spans multiple pathways.
- The **Sox multienzyme system** performs periplasmic thiosulfate oxidation via SoxXA, SoxYZ, SoxB, and Sox(CD)2 (nosalova2023coldsulfursprings—neglected pages 5-6). A mechanistically relevant regulatory concept is that “Transcription of sox genes is induced by reduced sulfur compounds” (nosalova2023coldsulfursprings—neglected pages 3-5).
- Sulfide oxidation can proceed via **SQR** (sulfide:quinone oxidoreductase) and/or **FccAB** (flavocytochrome c), providing multiple alternative entry points into electron transport (nosalova2023coldsulfursprings—neglected pages 5-6).
- When **SoxCD is absent**, sulfur globules can form; such globules can later be oxidized through the **reverse Dsr (rDsr)** system (nosalova2023coldsulfursprings—neglected pages 5-6, zhou2025diversityandecology pages 5-7).
- Sulfite oxidation to sulfate can proceed via **SoeABC** or via APS reductase plus ATP sulfurylase (nosalova2023coldsulfursprings—neglected pages 5-6).
- Environmental electron acceptors strongly shape sulfur lithotrophic edges; authoritative synthesis notes oxidation can be driven using acceptors such as **NO3−, MnO2, and Fe(III)** in addition to O2 (zhou2025diversityandecology pages 32-34).

#### 2.4 Iron lithotrophy (Fe(II) oxidation)
For acidophilic Fe(II)-oxidizers, *A. ferrooxidans* provides a curated chain: “Fe2+ is oxidized at the outer membrane by Cyc2” and electrons flow “Fe2+ → Cyc2 → Rus → Cyc1 → Cox” for a dominant downhill channel used for energy conservation (wang2024characterizethegrowth pages 1-2). This supports nodes for outer-membrane oxidase (Cyc2), periplasmic carriers (rusticyanin), and terminal oxidase.

For neutrophilic FeOB (Gallionellaceae), transcriptomics highlight a key curation pitfall: genes that indicate **capacity** (e.g., cyc2, mtoA) may not track **activity**. In *Sideroxydans* sp. CL21, cyc2 and mtoA were highly expressed regardless of whether the culture oxidized iron, while periplasmic/inner-membrane components (mtoD, cymA/imoA, ircABCD) were significantly upregulated when iron oxidation occurred (hoover2025anorganotrophicsideroxydans pages 1-2, hoover2025anorganotrophicsideroxydans pages 9-10). Thus, edges connecting “Fe(II) oxidation activity → upregulation of periplasmic shuttles/inner membrane carriers” are supported and may be valuable for assay-aware curation.

#### 2.5 Nitrifier lithotrophy (ammonia and nitrite oxidation)
Ammonia oxidation and nitrite oxidation underpin nitrification and represent globally important chemolithotrophic guilds.
- In an Arctic seasonal time series, **Nitrososphaeria** archaea “actively expressed genes associated with ammonia oxidation to nitrite (amt, amo, nirK)” (lasoperez2025nitrogencyclingduring pages 1-2). The resulting nitrite was “presumably further oxidized to nitrate” by a Nitrospinota bacterium that highly expressed **nxr** (lasoperez2025nitrogencyclingduring pages 1-2). These provide ecology-grounded gene→process associations.
- In oxic marine sediments, nitrifiers are “typically >10% of microbial taxa,” and nitrite rarely accumulates due to rapid oxidation to nitrate by NOB (zhao2024anabundantbacterial pages 1-3). This supports environmental prevalence claims relevant for trait importance.

### 3) Candidate mechanistic entities (nodes) grouped by type
Below are candidate nodes appropriate for `data/traits/physiology/lithotrophic.yaml` curation. CURIEs are suggested when stable.

#### 3.1 Electron donors / substrates (CHEBI)
- H2 (CHEBI:18276) (grinter2023structuralbasisfor pages 1-2)
- Fe2+ (CHEBI:29033) (wang2024characterizethegrowth pages 1-2)
- Sulfide (CHEBI:16134) (nosalova2023coldsulfursprings—neglected pages 5-6)
- Thiosulfate (CHEBI:30087) (nosalova2023coldsulfursprings—neglected pages 5-6)
- Sulfite (CHEBI:17980) (nosalova2023coldsulfursprings—neglected pages 5-6)
- Ammonia / ammonium (CHEBI:16134 / CHEBI:28938) (kong2026overlookedsiderophoreproducers pages 1-2)
- Nitrite (CHEBI:16301) (lasoperez2025nitrogencyclingduring pages 1-2)

#### 3.2 Electron acceptors / redox partners (CHEBI; label-only where needed)
- O2 (CHEBI:15379) (zhou2025diversityandecology pages 32-34)
- Nitrate (CHEBI:17632) (zhou2025diversityandecology pages 32-34)
- MnO2 (CHEBI:32595; label-only acceptable) (zhou2025diversityandecology pages 32-34)
- Fe(III) minerals / Fe3+ (CHEBI:29034; plus mineral ENVO label-only) (zhou2025diversityandecology pages 32-34)
- Respiratory quinones: menaquinone (CHEBI:18009) and reduced menaquinone/menaquinol (CHEBI:61717) (grinter2023structuralbasisfor pages 1-2, soom2025hydrogenasedrivenatpsynthesis pages 11-13)

#### 3.3 Pathways / modules (GO/label-only)
- Sulfur oxidation via Sox system (label-only; GO process label: sulfur oxidation) (nosalova2023coldsulfursprings—neglected pages 5-6)
- Reverse dissimilatory sulfite reductase (rDsr) sulfur oxidation (label-only) (nosalova2023coldsulfursprings—neglected pages 5-6)
- Fe(II) oxidation electron transfer chain (label-only) (wang2024characterizethegrowth pages 1-2)
- Ammonia oxidation to nitrite (label-only nitrification substep) (lasoperez2025nitrogencyclingduring pages 1-2)
- Nitrite oxidation to nitrate (label-only nitrification substep) (lasoperez2025nitrogencyclingduring pages 1-2)
- Proton motive force generation (GO:0015986) and ATP synthesis (GO:0006754) (soom2025hydrogenasedrivenatpsynthesis pages 1-4)

#### 3.4 Genes / proteins / complexes (EC/GO/label-only)
Hydrogen
- [NiFe]-hydrogenase Huc (group 2a; label-only) (grinter2023structuralbasisfor pages 1-2)

Sulfur
- SoxXA, SoxYZ, SoxB, Sox(CD)2 (label-only) (nosalova2023coldsulfursprings—neglected pages 5-6)
- SQR (EC 1.8.5.4) (nosalova2023coldsulfursprings—neglected pages 5-6)
- FccAB (label-only) (nosalova2023coldsulfursprings—neglected pages 5-6)
- SoeABC (label-only) (nosalova2023coldsulfursprings—neglected pages 5-6)

Iron
- Cyc2 (label-only) (wang2024characterizethegrowth pages 1-2)
- Rusticyanin (Rus; label-only) (wang2024characterizethegrowth pages 1-2)
- MtoAB; periplasmic mtoD; cymA/imoA; ircABCD (label-only) (hoover2025anorganotrophicsideroxydans pages 1-2)

Nitrogen
- AMO (EC 1.14.99.39) and HAO (EC 1.7.2.6) (kong2026overlookedsiderophoreproducers pages 1-2)
- amt, amo, nirK; nxr (gene labels) (lasoperez2025nitrogencyclingduring pages 1-2)

#### 3.5 Environmental / experimental factors (ENVO/label-only)
- pH/acidity (important for tetrathionate stability and acidophilic sulfur oxidizers) (nosalova2023coldsulfursprings—neglected pages 5-6)
- Redox/oxygen gradients (shape acceptor availability and sulfur oxidation regimes) (zhou2025diversityandecology pages 32-34)
- Iron limitation and siderophore availability in WWTP aerobic tanks (kong2026overlookedsiderophoreproducers pages 1-2)
- Electrode as electron donor (electroautotrophy experimental condition) (wang2024characterizethegrowth pages 1-2)

### 4) Evidence-backed candidate causal edges (curation table)
The following table compiles proposed edges as subject–predicate–object triples with supporting snippets and curation notes.

| Edge ID | Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet (short quote) | Source (author, year, title) | DOI/URL | Notes on strength/uncertainty | Suggested edge type |
|---|---|---|---|---|---|---|---|---|
| LITH-01 | Atmospheric H2 (CHEBI:18276) | oxidized_by | Huc hydrogenase, group 2a [NiFe]-hydrogenase (label-only candidate) | “Huc is a highly efficient oxygen-insensitive enzyme that couples oxidation of atmospheric H2” (grinter2023structuralbasisfor pages 1-2) | Grinter et al., 2023, *Structural basis for bacterial energy extraction from atmospheric hydrogen* | https://doi.org/10.1038/s41586-023-05781-7 | Strong, but taxon-specific to *Mycobacterium smegmatis* Huc | mechanistic |
| LITH-02 | Huc hydrogenase (label-only candidate) | reduces | menaquinone (CHEBI:18009) | “couples oxidation of atmospheric H2 to the hydrogenation of the respiratory electron carrier menaquinone” (grinter2023structuralbasisfor pages 1-2) | Grinter et al., 2023, *Structural basis for bacterial energy extraction from atmospheric hydrogen* | https://doi.org/10.1038/s41586-023-05781-7 | Strong structural/biochemical support; Huc-specific | mechanistic |
| LITH-03 | Menaquinol / reduced menaquinone (CHEBI:61717) | oxidized_by | terminal oxidase, e.g. cytochrome bd-I / bcc-aa3 (GO:0015002 label-only for terminal oxidase activity) | “the reduced quinone is oxidized by downstream terminal oxidases” (soom2025hydrogenasedrivenatpsynthesis pages 11-13) | Soom et al., 2025, *Hydrogenase-driven ATP synthesis from air* | https://doi.org/10.1101/2025.03.14.643271 | Strong in reconstituted system; preprint; terminal oxidase identity depends on chain | mechanistic |
| LITH-04 | Terminal oxidase (label-only candidate) | generates | proton motive force (GO:0015986) | “quinol oxidation by terminal oxidase generates a proton-motive force (pmf)” (soom2025hydrogenasedrivenatpsynthesis pages 1-4) | Soom et al., 2025, *Hydrogenase-driven ATP synthesis from air* | https://doi.org/10.1101/2025.03.14.643271 | Strong in liposome system; preprint | mechanistic |
| LITH-05 | Proton motive force (GO:0015986) | drives | F-type ATP synthase (GO:0046933) | “pmf generation required to accumulate ATP” and “F1Fo-ATP synthase regenerates ATP” (soom2025hydrogenasedrivenatpsynthesis pages 1-4, soom2025hydrogenasedrivenatpsynthesis pages 7-11) | Soom et al., 2025, *Hydrogenase-driven ATP synthesis from air* | https://doi.org/10.1101/2025.03.14.643271 | Strong for chemiosmotic coupling; preprint | mechanistic |
| LITH-06 | F-type ATP synthase (GO:0046933) | produces | ATP (CHEBI:15422) | “drives ATP synthesis” (soom2025hydrogenasedrivenatpsynthesis pages 4-7) | Soom et al., 2025, *Hydrogenase-driven ATP synthesis from air* | https://doi.org/10.1101/2025.03.14.643271 | Canonical respiratory inference directly demonstrated in reconstituted system | mechanistic |
| LITH-07 | Thiosulfate (CHEBI:30087) | oxidized_by | Sox multienzyme system (label-only candidate; soxXA/soxYZ/soxB/soxCD) | “The Sox multienzyme system… performs periplasmic thiosulfate oxidation” (nosalova2023coldsulfursprings—neglected pages 5-6) | Nosalova et al., 2023, *Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria* | https://doi.org/10.3390/microorganisms11061436 | Strong review support; pathway diversity across taxa | mechanistic |
| LITH-08 | Reduced sulfur compounds (CHEBI:26873 label-only grouping) | induce_expression_of | sox genes / sox cluster (label-only candidate) | “Transcription of sox genes is induced by reduced sulfur compounds” (nosalova2023coldsulfursprings—neglected pages 3-5) | Nosalova et al., 2023, *Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria* | https://doi.org/10.3390/microorganisms11061436 | Strong review support; regulatory specifics vary by taxon | regulatory |
| LITH-09 | Sulfide (CHEBI:16134) | oxidized_by | sulfide:quinone oxidoreductase SQR (EC 1.8.5.4) | “Sulfide oxidation employs… sulfide:quinone oxidoreductases (SqrD, SqrF)” (nosalova2023coldsulfursprings—neglected pages 5-6) | Nosalova et al., 2023, *Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria* | https://doi.org/10.3390/microorganisms11061436 | Strong review support; isoform usage taxon-specific | mechanistic |
| LITH-10 | Sulfide (CHEBI:16134) | oxidized_by | flavocytochrome c FccAB (label-only candidate) | “Sulfide oxidation employs flavocytochrome c (FccAB)” (nosalova2023coldsulfursprings—neglected pages 5-6) | Nosalova et al., 2023, *Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria* | https://doi.org/10.3390/microorganisms11061436 | Strong review support; route not universal | mechanistic |
| LITH-11 | Absence of SoxCD (label-only candidate condition) | leads_to | sulfur globule formation (label-only candidate) | “absence of SoxCD (Type IV) yields sulfate plus elemental sulfur and deposition of sulfur globules” (zhou2025diversityandecology pages 5-7) | Zhou et al., 2025, *Diversity and ecology of microbial sulfur metabolism* | https://doi.org/10.1038/s41579-024-01104-3 | Strong review support; 2025 publication from 2024 DOI; beyond requested 2024 but authoritative | mechanistic |
| LITH-12 | Sulfur globules / protein-bound sulfur (label-only candidate) | oxidized_by | reverse dissimilatory sulfite reductase rDsr (label-only candidate; dsrAB/dsrC/dsrMKJOP) | “globules are stored… and later oxidized via the dsr gene cluster including reverse dissimilatory sulfite reductase (rDsr)” (nosalova2023coldsulfursprings—neglected pages 5-6) | Nosalova et al., 2023, *Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria* | https://doi.org/10.3390/microorganisms11061436 | Strong review support; common in SoxCD-lacking sulfur oxidizers | mechanistic |
| LITH-13 | Sulfite (CHEBI:17980) | oxidized_by | SoeABC sulfite dehydrogenase (label-only candidate) | “Sulfite produced is oxidized to sulfate by membrane-bound SoeABC” (nosalova2023coldsulfursprings—neglected pages 5-6) | Nosalova et al., 2023, *Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria* | https://doi.org/10.3390/microorganisms11061436 | Strong review support | mechanistic |
| LITH-14 | Sulfite (CHEBI:17980) | converted_via | APS reductase + ATP sulfurylase / Sat route (label-only candidate) | “or via APS reductase plus ATP sulfurylase” (nosalova2023coldsulfursprings—neglected pages 5-6) | Nosalova et al., 2023, *Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria* | https://doi.org/10.3390/microorganisms11061436 | Strong review support; route varies by lineage | mechanistic |
| LITH-15 | Thiosulfate (CHEBI:30087) | oxidation_coupled_to | quinone pool reduction (label-only candidate) | “Membrane-bound thiosulfate:quinone oxidoreductase couples thiosulfate oxidation to the quinone pool” (nosalova2023coldsulfursprings—neglected pages 11-12) | Nosalova et al., 2023, *Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria* | https://doi.org/10.3390/microorganisms11061436 | Strong review support; especially polythionate pathway taxa | mechanistic |
| LITH-16 | Fe2+ (CHEBI:29033) | oxidized_by | Cyc2 outer-membrane cytochrome (label-only candidate) | “Fe2+ is oxidized at the outer membrane by Cyc2” (wang2024characterizethegrowth pages 1-2) | Wang et al., 2024, *Characterize the Growth and Metabolism of Acidithiobacillus ferrooxidans under Electroautotrophic and Chemoautotrophic Conditions* | https://doi.org/10.3390/microorganisms12030590 | Strong, but specific to *Acidithiobacillus ferrooxidans* | mechanistic |
| LITH-17 | Cyc2 (label-only candidate) | transfers_electrons_to | rusticyanin Rus (label-only candidate) | “Fe2+ → Cyc2 → Rus” (wang2024characterizethegrowth pages 1-2) | Wang et al., 2024, *Characterize the Growth and Metabolism of Acidithiobacillus ferrooxidans under Electroautotrophic and Chemoautotrophic Conditions* | https://doi.org/10.3390/microorganisms12030590 | Strong, A. ferrooxidans-specific chain | mechanistic |
| LITH-18 | Rusticyanin Rus (label-only candidate) | transfers_electrons_to | Cyc1 then Cox terminal oxidase (label-only candidate) | “~95% enter a downhill channel (Fe2+ →Cyc2 →Rus →Cyc1 →Cox)” (wang2024characterizethegrowth pages 1-2) | Wang et al., 2024, *Characterize the Growth and Metabolism of Acidithiobacillus ferrooxidans under Electroautotrophic and Chemoautotrophic Conditions* | https://doi.org/10.3390/microorganisms12030590 | Strong, A. ferrooxidans-specific respiratory branch | mechanistic |
| LITH-19 | Fe(II) oxidation electron transport (label-only candidate) | supports | ATP synthesis (GO:0006754) | “used for energy conservation (ATP synthesis implied via electron transport)” (wang2024characterizethegrowth pages 1-2) | Wang et al., 2024, *Characterize the Growth and Metabolism of Acidithiobacillus ferrooxidans under Electroautotrophic and Chemoautotrophic Conditions* | https://doi.org/10.3390/microorganisms12030590 | Moderate; ATP step inferred from characterized ETC context | mechanistic |
| LITH-20 | Fe2+ (CHEBI:29033) | donates_electrons_via | MtoAB porin-cytochrome complex (label-only candidate) | “MtoA, a decaheme cytochrome C, and MtoB, a porin-like structure” in the Fe oxidation pathway (burton2025studiesonthe pages 22-26) | Burton, 2025, *Studies on the G. sulfurreducens PCA Porin Cytochrome Complex ExtABCD* | no stable URL in context | Moderate; source is secondary/thesis-like and 2025; useful but should be curated cautiously | mechanistic |
| LITH-21 | Active Fe oxidation (label-only candidate state) | upregulates | mtoD (label-only candidate) | “mtoD significantly upregulated… when iron oxidation occurred” (hoover2025anorganotrophicsideroxydans pages 9-10) | Hoover et al., 2025, *An organotrophic Sideroxydans reveals potential iron oxidation marker genes* | https://doi.org/10.1128/aem.00395-25 | Strong transcriptomic correlation; marker of activity rather than universal mechanism | regulatory |
| LITH-22 | Active Fe oxidation (label-only candidate state) | upregulates | cymA/imoA (label-only candidate) | “periplasmic and inner membrane electron carrier genes (including mtoD, cymA/imoA)… are significantly upregulated only when cells oxidize iron” (hoover2025anorganotrophicsideroxydans pages 1-2) | Hoover et al., 2025, *An organotrophic Sideroxydans reveals potential iron oxidation marker genes* | https://doi.org/10.1128/aem.00395-25 | Strong transcriptomic correlation; 2025 | regulatory |
| LITH-23 | Active Fe oxidation (label-only candidate state) | upregulates | ircABCD cluster (label-only candidate) | “ircABCD… were significantly upregulated only when cells oxidize iron” (hoover2025anorganotrophicsideroxydans pages 1-2) | Hoover et al., 2025, *An organotrophic Sideroxydans reveals potential iron oxidation marker genes* | https://doi.org/10.1128/aem.00395-25 | Strong transcriptomic correlation; likely Gallionellaceae-enriched marker set | regulatory |
| LITH-24 | Ammonia / NH3 or NH4+ (CHEBI:16134 ammonia; CHEBI:28938 ammonium) | oxidized_by | ammonia monooxygenase AMO (EC 1.14.99.39) | “Key NH4+ oxidation enzymes including ammonia monooxygenase (AMO)” (kong2026overlookedsiderophoreproducers pages 1-2) | Kong et al., 2026, *Overlooked siderophore producers favor ammonium oxidation in global wastewater treatment plants* | https://doi.org/10.1186/s40168-025-02290-9 | Strong, but 2026 source; enzyme role canonical | mechanistic |
| LITH-25 | Hydroxylamine oxidation step (label-only candidate) | catalyzed_by | hydroxylamine oxidoreductase HAO (EC 1.7.2.6) | “Key NH4+ oxidation enzymes including… hydroxylamine oxidoreductase (HAO)” (kong2026overlookedsiderophoreproducers pages 1-2) | Kong et al., 2026, *Overlooked siderophore producers favor ammonium oxidation in global wastewater treatment plants* | https://doi.org/10.1186/s40168-025-02290-9 | Strong, but 2026 source; included because requested | mechanistic |
| LITH-26 | Ammonia-oxidizing archaea (NCBITaxon: label-only AOA) | expresses | amt, amo, nirK (label-only gene set) | “Nitrososphaeria archaea actively expressed genes associated with ammonia oxidation to nitrite (amt, amo, nirK)” (lasoperez2025nitrogencyclingduring pages 1-2) | Laso-Pérez et al., 2025, *Nitrogen cycling during an Arctic bloom: from chemolithotrophy to nitrogen assimilation* | https://doi.org/10.1128/mbio.00749-25 | Strong field transcriptomic evidence; archaeal/taxon-specific | regulatory |
| LITH-27 | Nitrite (CHEBI:16301) | oxidized_by | nitrite oxidoreductase NXR / nxr (EC 1.7.5.1) | “The resulting nitrite was presumably further oxidized to nitrate by a Nitrospinota bacterium that highly expressed a nitrite oxidoreductase gene (nxr)” (lasoperez2025nitrogencyclingduring pages 1-2) | Laso-Pérez et al., 2025, *Nitrogen cycling during an Arctic bloom: from chemolithotrophy to nitrogen assimilation* | https://doi.org/10.1128/mbio.00749-25 | Strong ecological evidence; organism assignment inferred from metatranscriptomics | mechanistic |
| LITH-28 | Iron limitation / low Fe3+ solubility in aerobic tanks (ENVO:00002006 wastewater treatment context, label-only) | constrains | ammonium oxidation (label-only process) | “Iron bioavailability is low in aerobic tanks because Fe is largely present as insoluble ferric (Fe3+, dissolved level ~10−11 M)” (kong2026overlookedsiderophoreproducers pages 1-2) | Kong et al., 2026, *Overlooked siderophore producers favor ammonium oxidation in global wastewater treatment plants* | https://doi.org/10.1186/s40168-025-02290-9 | Strong in WWTP context; environmental/engineering specific | environmental |
| LITH-29 | Exogenous siderophore / pyochelin (CHEBI:22999 label-only for siderophore; pyochelin label-only) | increases | ammonium oxidation rate (label-only process) | “addition of an exogenous siderophore (20 µM pyochelin) increased ammonium oxidation rates by 28.2%” (kong2026overlookedsiderophoreproducers pages 1-2) | Kong et al., 2026, *Overlooked siderophore producers favor ammonium oxidation in global wastewater treatment plants* | https://doi.org/10.1186/s40168-025-02290-9 | Strong application-relevant evidence; WWTP-specific and 2026 | environmental |
| LITH-30 | Oxygen (CHEBI:15379) | serves_as_terminal_acceptor_for | sulfur oxidation (GO:0009066 label-only sulfur oxidation process) | “sulfur’s lower redox potential makes it susceptible to oxidation by electron acceptors such as NO3-, MnO2/MnO(OH), and Fe3+/FeO(OH)” and aerobic sulfur oxidation contexts (zhou2025diversityandecology pages 32-34, nosalova2023coldsulfursprings—neglected pages 3-5) | Zhou et al., 2025, *Diversity and ecology of microbial sulfur metabolism*; Nosalova et al., 2023, *Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria* | https://doi.org/10.1038/s41579-024-01104-3 ; https://doi.org/10.3390/microorganisms11061436 | Strong, though generalized across sulfur oxidizers | environmental |
| LITH-31 | Nitrate (CHEBI:17632) | serves_as_terminal_acceptor_for | sulfur oxidation (GO:0009066 label-only sulfur oxidation process) | “denitrification-dependent sulfide oxidation” and “complete denitrification coupled to sulfur/sulfide oxidation” (zhou2025diversityandecology pages 32-34) | Zhou et al., 2025, *Diversity and ecology of microbial sulfur metabolism* | https://doi.org/10.1038/s41579-024-01104-3 | Strong review support; lineage-specific examples | environmental |
| LITH-32 | MnO2 / Mn(IV) oxide (CHEBI:32595 label-only) | serves_as_terminal_acceptor_for | sulfur oxidation (GO:0009066 label-only sulfur oxidation process) | “Sulfurimonas marisnigri oxidizes H2S and thiosulfate to sulfate while reducing MnO2 to Mn2+” (zhou2025diversityandecology pages 32-34) | Zhou et al., 2025, *Diversity and ecology of microbial sulfur metabolism* | https://doi.org/10.1038/s41579-024-01104-3 | Strong review support; taxon/example-specific | environmental |
| LITH-33 | Fe(III) / FeO(OH) (CHEBI:29034 label-only Fe3+) | serves_as_terminal_acceptor_for | sulfur oxidation (GO:0009066 label-only sulfur oxidation process) | “sulfur’s lower redox potential makes it susceptible to oxidation by electron acceptors such as… Fe3+/FeO(OH)” (zhou2025diversityandecology pages 32-34) | Zhou et al., 2025, *Diversity and ecology of microbial sulfur metabolism* | https://doi.org/10.1038/s41579-024-01104-3 | Moderate; broad geochemical review statement, direct microbial catalysts remain incompletely identified | environmental |


*Table: This table compiles curation-ready candidate causal edges for the lithotrophic trait, spanning hydrogen, sulfur, iron, and nitrogen-based lithotrophy plus environmental electron acceptors. It highlights suggested node grounding, short evidence snippets, source provenance, and uncertainty notes to support TraitMech graph curation.*

### 5) Recent developments (emphasis 2023–2024)
1) **Mechanistic structural resolution of atmospheric H2 oxidation:** Cryo-EM and biochemical evidence show Huc couples atmospheric H2 oxidation to menaquinone reduction and involves long-range quinone transport (Nature, 2023) (grinter2023structuralbasisfor pages 1-2, grinter2023structuralbasisfor media c56ed0f4).
2) **Expanded mechanistic evidence for energy conservation from trace-gas oxidation:** A reconstituted minimal respiratory chain demonstrates pmf generation and ATP synthesis driven by Huc-mediated quinone reduction (preprint; mechanistically strong though not yet peer-reviewed) (soom2025hydrogenasedrivenatpsynthesis pages 7-11, soom2025hydrogenasedrivenatpsynthesis pages 4-7).
3) **Updated multi-pathway view of sulfur lithotrophy:** 2023 reviews synthesize Sox, SQR/FccAB, rDsr, SoeABC, and polythionate routes and highlight regulation (sox induction) and environment-dependence (pH, oxygen gradients) (nosalova2023coldsulfursprings—neglected pages 5-6, nosalova2023coldsulfursprings—neglected pages 3-5).
4) **Activity-aware gene markers for Fe(II) lithotrophy:** Transcriptomic contrasts between non-oxidizing and oxidizing states indicate periplasmic/inner-membrane carriers (mtoD, cymA/imoA, ircABCD) better track iron oxidation activity than cyc2/mtoA alone in at least one Gallionellaceae isolate (hoover2025anorganotrophicsideroxydans pages 1-2, hoover2025anorganotrophicsideroxydans pages 9-10).
5) **Discovery of abundant, previously unrecognized nitrite oxidizer lineages:** In oligotrophic sediments, candidate nitrite-oxidizing lineages may help reconcile AOA:NOB abundance imbalances, reinforcing that lithotrophic roles are distributed across more phylogenetic diversity than classical cultured representatives (zhao2024anabundantbacterial pages 1-3).

### 6) Current applications and real-world implementations
- **Biomining/bioleaching and acid mine drainage contexts:** Acidophilic chemolithotrophs (e.g., *Acidithiobacillus* spp.) oxidize RISCs and Fe(II), producing sulfuric acid and mobilizing metals; mechanistic sulfur metabolism repertoires (Sox/TetH/TQO/SQR etc.) are directly linked to bioleaching utility (ibanez2023fromgenesto pages 1-2, wang2024characterizethegrowth pages 1-2).
- **Wastewater treatment nitrification:** Ammonium oxidation is described as the “initial and rate-limiting step” of nitrogen removal and is catalyzed by slow-growing chemolithoautotrophic AOB; the key enzymes AMO and HAO are iron-requiring, motivating engineering controls on Fe bioavailability (kong2026overlookedsiderophoreproducers pages 1-2).
- **Engineered manipulation of micronutrient accessibility:** Addition of an exogenous siderophore (pyochelin) increased ammonium oxidation rates by **28.2%** in a study of wastewater contexts, linking an environmental/experimental factor to a lithotroph-driven process rate (kong2026overlookedsiderophoreproducers pages 1-2).
- **Energy-limited ecosystem persistence (“maintenance lithotrophy”):** High-affinity hydrogenases enabling atmospheric H2 oxidation support persistence/growth under resource deprivation, with direct mechanistic coupling to respiratory quinones (grinter2023structuralbasisfor pages 1-2).
- **Electroautotrophy as an extension of lithotrophic electron sourcing:** *A. ferrooxidans* can grow with electrons supplied by solid electrodes, with differential expression of pili/porins/EPS relative to Fe(II)-based chemoautotrophy, suggesting a potential TraitMech adjacency between lithotrophy and extracellular electron uptake traits (wang2024characterizethegrowth pages 1-2).

### 7) Relevant statistics and quantitative data (recent studies)
- **Arctic seasonal nitrifier abundance:** Archaea reached “up to **25%** of metagenomic abundance in early spring” when nitrification-related chemolithotrophic activity was high (lasoperez2025nitrogencyclingduring pages 1-2).
- **Nitrifier prevalence in oxic sediments:** Nitrifiers are “typically **>10%** of microbial taxa” in oxic marine sediments (zhao2024anabundantbacterial pages 1-3).
- **WWTP microbial functional capacity distribution:** In a global WWTP metagenomic analysis, among 1,328 MAGs, **6.2%** were siderophore producers and **79.3%** could utilize siderophores (kong2026overlookedsiderophoreproducers pages 1-2).
- **Engineered intervention effect size:** Adding **20 µM pyochelin** increased ammonium oxidation rates by **28.2%** (kong2026overlookedsiderophoreproducers pages 1-2).
- **Energy coupling claims (preprint):** Atmospheric H2 oxidation via Huc was analyzed as sufficient for maintenance energy, including a reported estimate of “two ATP molecules per H2 oxidised” under certain coupling assumptions (soom2025hydrogenasedrivenatpsynthesis pages 1-4).

### 8) Expert analysis and curation guidance
**Key curation insight:** lithotrophy is a *functional trait* best captured by a causal graph anchored on (i) inorganic donor oxidation enzymes, (ii) electron carrier modules (quinone pool, cytochromes), and (iii) energy conservation nodes (pmf, ATP synthase). The strongest direct mechanistic chain in the current evidence base is **H2 → Huc → menaquinone → terminal oxidase → pmf → ATP** (grinter2023structuralbasisfor pages 1-2, soom2025hydrogenasedrivenatpsynthesis pages 7-11).

**Capacity vs activity:** For traits inferred from genomes/transcriptomes, separate “has pathway genes” from “is performing lithotrophy” edges. For Fe(II) oxidation, cyc2/mtoA may indicate capability, whereas mtoD/ircABCD and inner-membrane carriers correlate with active oxidation in at least one system (hoover2025anorganotrophicsideroxydans pages 1-2).

**Environmental acceptor dependence:** Sulfur lithotrophy often depends on available terminal electron acceptors (O2, nitrate, MnO2, Fe(III)), so ENVO/chemical acceptor nodes should be included and edges flagged as context-dependent (zhou2025diversityandecology pages 32-34).

### 9) Warnings / claims not yet ready for strong curation
- **Preprint-only edges:** The direct ATP synthesis-from-air system is mechanistically compelling but currently preprint; edges derived from this should be marked as *provisional* until peer-reviewed (soom2025hydrogenasedrivenatpsynthesis pages 7-11, soom2025hydrogenasedrivenatpsynthesis pages 4-7).
- **Secondary/unclear provenance documents:** Some supporting iron-oxidation mechanistic descriptions appear in non-standard/uncertain-source documents; use them only to guide node hypotheses, prioritizing peer-reviewed sources for edges (burton2025studiesonthe pages 22-26).
- **Generalized geochemical acceptor statements:** Claims that Fe(III) is an acceptor for sulfur oxidation may be broad; microbial catalysts may still be unresolved for some regimes—mark as uncertain where the review itself indicates unknown organisms (zhou2025diversityandecology pages 32-34).

---

## DOI-first bibliography (with dates and URLs)
1. **Grinter R, et al. (Mar 2023).** *Structural basis for bacterial energy extraction from atmospheric hydrogen.* **Nature** 615:541–547. DOI: **10.1038/s41586-023-05781-7**. URL: https://doi.org/10.1038/s41586-023-05781-7 (grinter2023structuralbasisfor pages 1-2, grinter2023structuralbasisfor media c56ed0f4)
2. **Wang Q, et al. (Mar 2024).** *Characterize the Growth and Metabolism of Acidithiobacillus ferrooxidans under Electroautotrophic and Chemoautotrophic Conditions.* **Microorganisms** 12:590. DOI: **10.3390/microorganisms12030590**. URL: https://doi.org/10.3390/microorganisms12030590 (wang2024characterizethegrowth pages 1-2)
3. **Nosalova L, et al. (May 2023).** *Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria.* **Microorganisms** 11:1436. DOI: **10.3390/microorganisms11061436**. URL: https://doi.org/10.3390/microorganisms11061436 (nosalova2023coldsulfursprings—neglected pages 3-5, nosalova2023coldsulfursprings—neglected pages 5-6, nosalova2023coldsulfursprings—neglected pages 11-12)
4. **Ibáñez A, et al. (Sep 2023).** *From Genes to Bioleaching: Unraveling Sulfur Metabolism in Acidithiobacillus Genus.* **Genes** 14:1772. DOI: **10.3390/genes14091772**. URL: https://doi.org/10.3390/genes14091772 (ibanez2023fromgenesto pages 1-2)
5. **Zhao R, et al. (Apr 2024).** *An abundant bacterial phylum with nitrite-oxidizing potential in oligotrophic marine sediments.* **Communications Biology** 7. DOI: **10.1038/s42003-024-06136-2**. URL: https://doi.org/10.1038/s42003-024-06136-2 (zhao2024anabundantbacterial pages 1-3)
6. **Laso-Pérez R, et al. (Jun 2025).** *Nitrogen cycling during an Arctic bloom: from chemolithotrophy to nitrogen assimilation.* **mBio** 16. DOI: **10.1128/mbio.00749-25**. URL: https://doi.org/10.1128/mbio.00749-25 (lasoperez2025nitrogencyclingduring pages 1-2)
7. **Hoover RL, et al. (Sep 2025).** *An organotrophic Sideroxydans reveals potential iron oxidation marker genes.* **Applied and Environmental Microbiology** 91. DOI: **10.1128/aem.00395-25**. URL: https://doi.org/10.1128/aem.00395-25 (hoover2025anorganotrophicsideroxydans pages 1-2, hoover2025anorganotrophicsideroxydans pages 9-10)
8. **Kong L, et al. (Dec 2026).** *Overlooked siderophore producers favor ammonium oxidation in global wastewater treatment plants.* **Microbiome** 14. DOI: **10.1186/s40168-025-02290-9**. URL: https://doi.org/10.1186/s40168-025-02290-9 (kong2026overlookedsiderophoreproducers pages 1-2)
9. **Zhou Z, et al. (Oct 2025; DOI indicates 2024 online).** *Diversity and ecology of microbial sulfur metabolism.* **Nature Reviews Microbiology** 23:122–140. DOI: **10.1038/s41579-024-01104-3**. URL: https://doi.org/10.1038/s41579-024-01104-3 (zhou2025diversityandecology pages 5-7, zhou2025diversityandecology pages 32-34)
10. **Soom S, et al. (Mar 2025; preprint).** *Hydrogenase-driven ATP synthesis from air.* **bioRxiv**. DOI: **10.1101/2025.03.14.643271**. URL: https://doi.org/10.1101/2025.03.14.643271 (soom2025hydrogenasedrivenatpsynthesis pages 1-4, soom2025hydrogenasedrivenatpsynthesis pages 7-11, soom2025hydrogenasedrivenatpsynthesis pages 4-7)



References

1. (wang2024characterizethegrowth pages 1-2): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 9 citations.

2. (hoover2025anorganotrophicsideroxydans pages 1-2): Rene L. Hoover, Kirsten Küsel, and Clara S. Chan. An organotrophic <i>sideroxydans</i> reveals potential iron oxidation marker genes. Sep 2025. URL: https://doi.org/10.1128/aem.00395-25, doi:10.1128/aem.00395-25. This article has 1 citations and is from a peer-reviewed journal.

3. (soom2025hydrogenasedrivenatpsynthesis pages 1-4): Sarah Soom, Stefan Urs Moning, Gregory M Cook, James P Lingford, Ashleigh Kropp, Sieu Tran, Rhys Grinter, Chris Greening, and Christoph von Ballmoos. Hydrogenase-driven atp synthesis from air. bioRxiv, Mar 2025. URL: https://doi.org/10.1101/2025.03.14.643271, doi:10.1101/2025.03.14.643271. This article has 0 citations.

4. (soom2025hydrogenasedrivenatpsynthesis pages 7-11): Sarah Soom, Stefan Urs Moning, Gregory M Cook, James P Lingford, Ashleigh Kropp, Sieu Tran, Rhys Grinter, Chris Greening, and Christoph von Ballmoos. Hydrogenase-driven atp synthesis from air. bioRxiv, Mar 2025. URL: https://doi.org/10.1101/2025.03.14.643271, doi:10.1101/2025.03.14.643271. This article has 0 citations.

5. (soom2025hydrogenasedrivenatpsynthesis pages 4-7): Sarah Soom, Stefan Urs Moning, Gregory M Cook, James P Lingford, Ashleigh Kropp, Sieu Tran, Rhys Grinter, Chris Greening, and Christoph von Ballmoos. Hydrogenase-driven atp synthesis from air. bioRxiv, Mar 2025. URL: https://doi.org/10.1101/2025.03.14.643271, doi:10.1101/2025.03.14.643271. This article has 0 citations.

6. (grinter2023structuralbasisfor pages 1-2): Rhys Grinter, Ashleigh Kropp, Hari Venugopal, Moritz Senger, Jack Badley, Princess R. Cabotaje, Ruyu Jia, Zehui Duan, Ping Huang, Sven T. Stripp, Christopher K. Barlow, Matthew Belousoff, Hannah S. Shafaat, Gregory M. Cook, Ralf B. Schittenhelm, Kylie A. Vincent, Syma Khalid, Gustav Berggren, and Chris Greening. Structural basis for bacterial energy extraction from atmospheric hydrogen. Nature, 615:541-547, Mar 2023. URL: https://doi.org/10.1038/s41586-023-05781-7, doi:10.1038/s41586-023-05781-7. This article has 93 citations and is from a highest quality peer-reviewed journal.

7. (grinter2023structuralbasisfor media c56ed0f4): Rhys Grinter, Ashleigh Kropp, Hari Venugopal, Moritz Senger, Jack Badley, Princess R. Cabotaje, Ruyu Jia, Zehui Duan, Ping Huang, Sven T. Stripp, Christopher K. Barlow, Matthew Belousoff, Hannah S. Shafaat, Gregory M. Cook, Ralf B. Schittenhelm, Kylie A. Vincent, Syma Khalid, Gustav Berggren, and Chris Greening. Structural basis for bacterial energy extraction from atmospheric hydrogen. Nature, 615:541-547, Mar 2023. URL: https://doi.org/10.1038/s41586-023-05781-7, doi:10.1038/s41586-023-05781-7. This article has 93 citations and is from a highest quality peer-reviewed journal.

8. (grinter2023structuralbasisfor media 7212eac1): Rhys Grinter, Ashleigh Kropp, Hari Venugopal, Moritz Senger, Jack Badley, Princess R. Cabotaje, Ruyu Jia, Zehui Duan, Ping Huang, Sven T. Stripp, Christopher K. Barlow, Matthew Belousoff, Hannah S. Shafaat, Gregory M. Cook, Ralf B. Schittenhelm, Kylie A. Vincent, Syma Khalid, Gustav Berggren, and Chris Greening. Structural basis for bacterial energy extraction from atmospheric hydrogen. Nature, 615:541-547, Mar 2023. URL: https://doi.org/10.1038/s41586-023-05781-7, doi:10.1038/s41586-023-05781-7. This article has 93 citations and is from a highest quality peer-reviewed journal.

9. (nosalova2023coldsulfursprings—neglected pages 5-6): Lea Nosalova, Maria Piknova, Mariana Kolesarova, and Peter Pristas. Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria. Microorganisms, 11:1436, May 2023. URL: https://doi.org/10.3390/microorganisms11061436, doi:10.3390/microorganisms11061436. This article has 16 citations.

10. (nosalova2023coldsulfursprings—neglected pages 3-5): Lea Nosalova, Maria Piknova, Mariana Kolesarova, and Peter Pristas. Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria. Microorganisms, 11:1436, May 2023. URL: https://doi.org/10.3390/microorganisms11061436, doi:10.3390/microorganisms11061436. This article has 16 citations.

11. (zhou2025diversityandecology pages 5-7): Zhichao Zhou, Patricia Q. Tran, Elise S. Cowley, Elizabeth Trembath-Reichert, and Karthik Anantharaman. Diversity and ecology of microbial sulfur metabolism. Nature reviews. Microbiology, 23:122-140, Oct 2025. URL: https://doi.org/10.1038/s41579-024-01104-3, doi:10.1038/s41579-024-01104-3. This article has 207 citations.

12. (zhou2025diversityandecology pages 32-34): Zhichao Zhou, Patricia Q. Tran, Elise S. Cowley, Elizabeth Trembath-Reichert, and Karthik Anantharaman. Diversity and ecology of microbial sulfur metabolism. Nature reviews. Microbiology, 23:122-140, Oct 2025. URL: https://doi.org/10.1038/s41579-024-01104-3, doi:10.1038/s41579-024-01104-3. This article has 207 citations.

13. (hoover2025anorganotrophicsideroxydans pages 9-10): Rene L. Hoover, Kirsten Küsel, and Clara S. Chan. An organotrophic <i>sideroxydans</i> reveals potential iron oxidation marker genes. Sep 2025. URL: https://doi.org/10.1128/aem.00395-25, doi:10.1128/aem.00395-25. This article has 1 citations and is from a peer-reviewed journal.

14. (lasoperez2025nitrogencyclingduring pages 1-2): Rafael Laso-Pérez, Juan Rivas-Santisteban, Nuria Fernandez-Gonzalez, Christopher J. Mundy, Javier Tamames, and Carlos Pedrós-Alió. Nitrogen cycling during an arctic bloom: from chemolithotrophy to nitrogen assimilation. mBio, Jun 2025. URL: https://doi.org/10.1128/mbio.00749-25, doi:10.1128/mbio.00749-25. This article has 5 citations and is from a domain leading peer-reviewed journal.

15. (zhao2024anabundantbacterial pages 1-3): Rui Zhao, Steffen L. Jørgensen, and Andrew R. Babbin. An abundant bacterial phylum with nitrite-oxidizing potential in oligotrophic marine sediments. Communications Biology, Apr 2024. URL: https://doi.org/10.1038/s42003-024-06136-2, doi:10.1038/s42003-024-06136-2. This article has 10 citations and is from a peer-reviewed journal.

16. (kong2026overlookedsiderophoreproducers pages 1-2): Lingrui Kong, Yimin Mao, Ru Zheng, Yiming Feng, Baiyizhuo Chen, Xiaogang Wu, Qile Zhu, Jinnan Feng, and Sitong Liu. Overlooked siderophore producers favor ammonium oxidation in global wastewater treatment plants. Microbiome, Dec 2026. URL: https://doi.org/10.1186/s40168-025-02290-9, doi:10.1186/s40168-025-02290-9. This article has 1 citations and is from a highest quality peer-reviewed journal.

17. (soom2025hydrogenasedrivenatpsynthesis pages 11-13): Sarah Soom, Stefan Urs Moning, Gregory M Cook, James P Lingford, Ashleigh Kropp, Sieu Tran, Rhys Grinter, Chris Greening, and Christoph von Ballmoos. Hydrogenase-driven atp synthesis from air. bioRxiv, Mar 2025. URL: https://doi.org/10.1101/2025.03.14.643271, doi:10.1101/2025.03.14.643271. This article has 0 citations.

18. (nosalova2023coldsulfursprings—neglected pages 11-12): Lea Nosalova, Maria Piknova, Mariana Kolesarova, and Peter Pristas. Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria. Microorganisms, 11:1436, May 2023. URL: https://doi.org/10.3390/microorganisms11061436, doi:10.3390/microorganisms11061436. This article has 16 citations.

19. (burton2025studiesonthe pages 22-26): JAJ Burton. Studies on the g. sulfurreducens pca porin cytochrome complex extabcd. Unknown journal, 2025.

20. (ibanez2023fromgenesto pages 1-2): Ana Ibáñez, Sonia Garrido-Chamorro, Juan J. R. Coque, and Carlos Barreiro. From genes to bioleaching: unraveling sulfur metabolism in acidithiobacillus genus. Genes, 14:1772, Sep 2023. URL: https://doi.org/10.3390/genes14091772, doi:10.3390/genes14091772. This article has 35 citations.