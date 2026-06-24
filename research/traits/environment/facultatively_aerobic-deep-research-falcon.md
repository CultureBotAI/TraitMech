---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:03:57.453185'
end_time: '2026-06-17T22:33:25.477461'
duration_seconds: 1768.02
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: facultatively aerobic
  trait_identifier: METPO:1000608
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: facultatively_aerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An oxygen preference in which growth can occur without oxygen but is
    capable of aerobic growth.
  parent_traits: METPO:1000601
  synonyms: facultative, facultative aerobe
  evidence_summary: 'PMID:21413255: preferentially utilize oxygen as a terminal electron
    acceptor (Supports facultative aerobic growth when oxygen is available.) | PMID:16142505:
    A facultative aerobic, moderately thermophilic, spore forming bacterium (Organism
    example: Anoxybacillus kamchatkensis strain JW/VK-KG4 is described as facultatively
    aerobic.)'
  causal_graph_summary: 'facultative_aerobe_oxygen_flexible_growth: 5 nodes, 4 edges'
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
- **Trait label:** facultatively aerobic
- **METPO identifier:** METPO:1000608
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth can occur without oxygen but is capable of aerobic growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** facultative, facultative aerobe
- **Existing evidence:** PMID:21413255: preferentially utilize oxygen as a terminal electron acceptor (Supports facultative aerobic growth when oxygen is available.) | PMID:16142505: A facultative aerobic, moderately thermophilic, spore forming bacterium (Organism example: Anoxybacillus kamchatkensis strain JW/VK-KG4 is described as facultatively aerobic.)
- **Existing causal graph summary:** facultative_aerobe_oxygen_flexible_growth: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **facultatively aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_aerobic.yaml`.

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
- **Trait label:** facultatively aerobic
- **METPO identifier:** METPO:1000608
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth can occur without oxygen but is capable of aerobic growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** facultative, facultative aerobe
- **Existing evidence:** PMID:21413255: preferentially utilize oxygen as a terminal electron acceptor (Supports facultative aerobic growth when oxygen is available.) | PMID:16142505: A facultative aerobic, moderately thermophilic, spore forming bacterium (Organism example: Anoxybacillus kamchatkensis strain JW/VK-KG4 is described as facultatively aerobic.)
- **Existing causal graph summary:** facultative_aerobe_oxygen_flexible_growth: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **facultatively aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_aerobic.yaml`.

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


# Microbial Trait Causal Graph Research Report: **facultatively aerobic** (METPO:1000608)

## 1) Scope summary (trait meaning, boundaries, assays)

**Trait definition (operational):** *Facultatively aerobic* describes an oxygen preference in which an organism **can grow without oxygen**, but is **capable of aerobic growth/respiration when O\₂ is available**. Mechanistically, this requires at least one energy-conserving anoxic mode (anaerobic respiration and/or fermentation) plus an oxygen-respiring branch (aerobic or microaerobic/nanaerobic respiration). This aligns with recent mechanistic case studies where organisms retain both anaerobic and O\₂-respiring modules and switch terminal electron acceptors depending on availability. (butler2023bacteroidesfragilismaintains pages 1-2, dyksma2023oxygenrespirationand pages 1-2)

**Trait boundary cases that should be distinguished during curation:**

- **Facultatively aerobic vs. “facultative anaerobe”:** In practice, literature often uses *facultative anaerobe* for the same physiological capacity (growth with or without O\₂). For TraitMech, *facultatively aerobic* can be curated as “**anoxic growth possible + oxygen-respiring capability**,” regardless of which label a paper uses. (lamoureux2023amultiscaleexpression pages 10-12)
- **Aerotolerant (non-respiring) vs. facultatively aerobic:** Aerotolerant organisms can survive O\₂ but may not gain energy by O\₂ respiration. A key discriminator is **measurable O\₂ respiration and/or requirement of terminal oxidases for aerobic growth**. In *Zymomonas mobilis*, deletion of the bd-type oxidase (cydAB) nearly abolishes O\₂ consumption and collapses aerobic growth, supporting true functional oxygen respiration (and thus oxygen-capable growth), not mere tolerance. (felczak2023respirationisessential pages 2-4)
- **Microaerophilic/nanaerobic vs. facultatively aerobic:** Some organisms are viable only at very low O\₂. “Nanaerobic” respiration has been used for extremely low O\₂ niches (e.g., gut epithelium-adjacent oxygen), where cytochrome bd supports oxygen reduction at low concentration. This regime is a *context* that often selects for facultative-like flexibility, but it is not identical to “facultatively aerobic” unless growth without O\₂ is demonstrably supported by anaerobic processes. (butler2023bacteroidesfragilismaintains pages 1-2)

**Assay/observation types seen in the 2023–2024 literature relevant to this trait:**

- Growth curves under oxic vs anoxic conditions, often with different terminal electron acceptors (e.g., fumarate vs O\₂). (butler2023bacteroidesfragilismaintains pages 2-5)
- Oxygen consumption rates and mutant phenotyping of terminal oxidases (genetic proof). (felczak2023respirationisessential pages 2-4)
- Omics-based switching in redox-cycled bioreactors (evidence for switching pathways with O\₂). (dyksma2023oxygenrespirationand pages 1-2)
- Regulators/response systems that sense O\₂ or redox proxies (FNR, ArcAB). (brown2023conservedmetabolicregulator pages 12-14, lamoureux2023amultiscaleexpression pages 10-12)

## 2) Current understanding: mechanistic basis of facultatively aerobic growth

### 2.1 A core mechanistic motif: **branched respiratory chain + alternative terminal acceptors**

A clear mechanistic template comes from *Bacteroides fragilis*, which maintains **concurrent anaerobic respiration on fumarate** and **nanaerobic respiration on oxygen**. Electrons from NADH are fed into a **menaquinone pool** via NADH:quinone oxidoreductases (NQR and NDH2), then flow to either **fumarate reductase** (when fumarate is available) or **cytochrome bd oxidase** (when oxygen is available). A schematic pathway diagram supporting this branch architecture is shown in Fig. 5 of the paper (butler2023bacteroidesfragilismaintains media 83284cef), and the accompanying text emphasizes that the terminal branch used depends on electron acceptor availability. (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains media 83284cef)

Key quantitative observations in this system include:

- NQR and NDH2 contributions in nanaerobiosis ~77% and 23%, respectively, similar to anaerobic conditions, and core gene expression is largely unchanged across 0–1500 ppm oxygen—suggesting flexibility can be mediated by **terminal acceptor availability** and post-transcriptional/biochemical regulation rather than large-scale transcriptional remodeling. (butler2023bacteroidesfragilismaintains pages 2-5)
- Cytochrome bd activity (oxygen-dependent NADH consumption) is ~5-fold higher in nanaerobic cultures compared with anaerobic cultures under certain supplement conditions, indicating increased oxidase activity despite limited transcriptional changes. (butler2023bacteroidesfragilismaintains pages 5-7)

### 2.2 Regulatory switching: **FNR** (direct O\₂ sensing) and **ArcAB** (quinone redox proxy)

Facultative oxygen flexibility is frequently coordinated by global regulators that tune gene expression to oxygen/redox state.

- **FNR**: A canonical regulator for anaerobic/aerobic transitions. In *E. coli* regulatory summaries, FNR is **activated by assembly of a 4Fe–4S cluster and dimerization**, and **oxygen directly inactivates FNR by oxidizing the iron–sulfur cluster**; when active, FNR **activates anaerobic genes and represses aerobic genes**. This provides a direct mechanistic link between O\₂ presence and transcriptional state. (lamoureux2023amultiscaleexpression pages 10-12)

- **ArcAB**: A two-component system widely used by facultative anaerobes to regulate metabolism in response to oxygen utilization and ETC redox state. In a 2023 infection-relevant analysis of Gram-negative pathogens, ArcAB is described as **“repress[ing] aerobic respiration”** and mediating metabolic adaptation when oxygen utilization decreases. The mechanistic statement that ArcAB senses **ETC redox state via the quinone pool** (electrons routing to ArcB vs to O\₂ leading to ArcB→ArcA phosphorylation and a transcriptional shift) connects respiratory flux with regulatory outputs promoting fermentation and suppressing aerobic processes. (brown2023conservedmetabolicregulator pages 12-14, brown2023conservedmetabolicregulator pages 1-3)

### 2.3 Terminal oxidase diversity supports oxygen flexibility (cytochrome bd vs bo\₃, etc.)

A common mechanism enabling oxygen-capable growth across fluctuating O\₂ is the presence of multiple terminal oxidases with different oxygen affinity and inhibitor tolerance.

- In *E. coli* terminal oxidase mutants, cytochrome bd-I shows **minimal CO inhibition** compared with bd-II or bo\₃ under defined oxygen levels (e.g., at 100 µM O\₂, 96.3 µM CO inhibits bd-I-only respiration by 11.6 ± 1.1%, versus ~43–44% inhibition for bd-II-only and bo\₃-only strains). (nastasi2024membraneboundredoxenzyme pages 4-7)
- Reported oxygen affinity parameters used in that study include **Km(O\₂) ≈ 2 µM for cytochrome bd-II** and **Km(O\₂) ≈ 6 µM for cytochrome bo\₃**, consistent with bd-type oxidases being better suited for lower oxygen regimes. (nastasi2024membraneboundredoxenzyme pages 13-15)

In *Pseudomonas aeruginosa*, a bd-type “cyanide-insensitive oxidase” (CIO) can support growth under microaerobic conditions (2% O\₂) in strains lacking cbb\₃ oxidases, and has a measured **Km(O\₂) = 4.0 ± 2.1 µM** in a CIO-only strain, along with tolerance properties relevant to infection environments (e.g., H\₂S/NO contexts). (nastasi2024cyanideinsensitiveoxidase pages 2-3)

## 3) Recent developments (prioritizing 2023–2024)

### 3.1 2023: Nanaerobic respiration and “concurrent capability” paradigm in gut-associated bacteria

A 2023 *Journal of Bacteriology* study dissected nanaerobic respiration in *Bacteroides fragilis*, demonstrating it maintains capabilities for **anaerobic fumarate respiration and nanaerobic oxygen respiration simultaneously**, with shared upstream NADH→quinone machinery and a stable menaquinone pool composition across conditions. This supports a modern view that switching may be governed by terminal acceptor availability and modular respiratory architecture, rather than being strictly exclusive “aerobic vs anaerobic” states. (butler2023bacteroidesfragilismaintains pages 2-5)

### 3.2 2023: Quantitative genetic proof that oxygen respiration machinery can be required for aerobic growth even in “fermentative” chassis

A 2023 *mBio* study resolved a long-standing question in *Zymomonas mobilis*: deleting **cydAB** (bd-type oxidase) reduces O\₂ respiration to **0.6% of WT** and drops aerobic growth (final OD\₆₀₀ **0.29 ± 0.01 vs WT 4.54 ± 0.06**), while WT consumes oxygen at **0.941 ± 0.017 mg/L/min**. This provides strong, curation-friendly causal evidence linking a specific terminal oxidase to aerobic growth capability—a key requirement for labeling the trait as facultatively aerobic in a causal graph. (felczak2023respirationisessential pages 2-4)

### 3.3 2023: Infection physiology integrates oxygen availability, iron limitation, and membrane stress through ArcA

A 2023 *mBio* study in bacteremia models shows ArcA-dependent metabolic rewiring in multiple Enterobacterales. Quantitatively, average population doubling times in murine spleens were **66 min (Citrobacter freundii), 39 min (Klebsiella pneumoniae), 61 min (Serratia marcescens)**, and the paper highlights physiological oxygen gradients (ambient ~21.1% vs tissue values such as ~5.4% in liver) as constraints shaping bacterial respiratory strategy. This strengthens the application case: facultatively oxygen-flexible pathogens use regulators like ArcA to remain fit across host oxygen gradients. (brown2023conservedmetabolicregulator pages 12-14)

### 3.4 2024: Quantitative oxidase-level properties under inhibitors and stressors

A 2024 *IJMS* study quantitatively compared CO inhibition across E. coli terminal oxidases and derived oxygen-dependent inhibition curves and IC50/Ki estimates for bd-II and bo\₃ (bd-I too resistant for a standard IC50 fit in that work). Such studies expand practical “trait mechanism” nodes/edges to include inhibitor tolerance as a modulatory factor for oxygen respiration functionality. (nastasi2024membraneboundredoxenzyme pages 4-7)

A 2024 *Antioxidants* study on P. aeruginosa CIO extends this to infection-relevant stressors (NO/H\₂S) and microaerobic growth capacity (2% O\₂), supporting the notion that oxygen-flexible growth often co-evolves with tolerance to host-derived respiratory inhibitors. (nastasi2024cyanideinsensitiveoxidase pages 2-3)

## 4) Candidate nodes for TraitMech curation (grouped, with grounding suggestions)

Candidate node inventory is summarized in the table below.

| Node type | Label | Suggested CURIE(s) | Example evidence/source (author year DOI) | Notes (scope/taxon) |
|---|---|---|---|---|
| Environment | oxic conditions | ENVO:01000627 | Dyksma 2023, 10.1038/s41467-023-42074-z (dyksma2023oxygenrespirationand pages 1-2) | Environmental state that induces oxygen reduction in redox-cycling cultures; useful context node. |
| Environment | anoxic conditions | ENVO:01000311 | Dyksma 2023, 10.1038/s41467-023-42074-z (dyksma2023oxygenrespirationand pages 1-2) | Environmental state associated with sulfate reduction or other anaerobic respiration branches. |
| Environment | nanaerobic / low-oxygen conditions | label-only candidate | Butler 2023, 10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 1-2) | Important boundary-case oxygen regime in gut-associated bacteria; keep label-only unless ontology term is chosen later. |
| Environment | oxygen concentration 1,000-1,500 ppm | label-only candidate | Butler 2023, 10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains pages 1-2) | Assay/environmental measurement node for nanaerobic gut-like conditions in *Bacteroides fragilis*. |
| Chemical / electron acceptor | molecular oxygen | CHEBI:15379 | Butler 2023, 10.1128/jb.00389-22; Felczak 2023, 10.1128/mbio.02043-23 (butler2023bacteroidesfragilismaintains pages 1-2, felczak2023respirationisessential pages 2-4) | Core terminal electron acceptor for the aerobic branch of the trait. |
| Chemical / electron acceptor | fumarate | CHEBI:18012 | Butler 2023, 10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains pages 1-2) | Alternative terminal electron acceptor in anaerobic branch; direct evidence in *B. fragilis*. |
| Chemical / electron acceptor | sulfate | CHEBI:16189 | Dyksma 2023, 10.1038/s41467-023-42074-z (dyksma2023oxygenrespirationand pages 1-2) | Electron acceptor for sulfate-reducing branch in Acidobacteriota example; taxon-specific. |
| Chemical / electron donor | NADH | CHEBI:16908 | Butler 2023, 10.1128/jb.00389-22; Felczak 2023, 10.1128/mbio.02043-23 (butler2023bacteroidesfragilismaintains media 83284cef, felczak2023respirationisessential pages 2-4) | Common reductant feeding respiratory chain; useful as a generic donor node. |
| Chemical / carrier | menaquinone pool | CHEBI:18064 | Butler 2023, 10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains media 83284cef) | Central quinone carrier in *B. fragilis*; redox-pool node connects dehydrogenases to terminal reductases/oxidases. |
| Chemical / carrier | quinone pool redox state | label-only candidate | Brown 2023, 10.1128/mbio.01448-23; Lamoureux 2023, 10.1093/nar/gkad750 (brown2023conservedmetabolicregulator pages 12-14, lamoureux2023amultiscaleexpression pages 10-12) | Sensed variable for ArcAB-like regulation in facultative respiratory switching. |
| Pathway / module | aerobic respiration | GO:0009060 | Felczak 2023, 10.1128/mbio.02043-23; Brown 2023, 10.1128/mbio.01448-23 (felczak2023respirationisessential pages 2-4, brown2023conservedmetabolicregulator pages 1-3) | High-level process node for oxygen-dependent growth branch. |
| Pathway / module | fermentation | GO:0006113 | Brown 2023, 10.1128/mbio.01448-23 (brown2023conservedmetabolicregulator pages 12-14, brown2023conservedmetabolicregulator pages 1-3) | Alternative energy-conservation branch promoted when aerobic respiration is repressed. |
| Pathway / module | sulfate reduction pathway | label-only candidate | Dyksma 2023, 10.1038/s41467-023-42074-z (dyksma2023oxygenrespirationand pages 1-2) | Anaerobic branch example showing switching with oxygen reduction in one organism. |
| Pathway / module | oxygen reduction pathway | label-only candidate | Dyksma 2023, 10.1038/s41467-023-42074-z (dyksma2023oxygenrespirationand pages 1-2) | High-level pathway branch complementary to sulfate reduction in fluctuating redox conditions. |
| Pathway / module | electron transport chain | GO:0022900 | Felczak 2023, 10.1128/mbio.02043-23 (felczak2023respirationisessential pages 1-2, felczak2023respirationisessential pages 2-4) | Broad mechanistic node covering oxygen removal, redox balance, and PMF-linked processes. |
| Protein / complex | fumarate reductase complex | label-only candidate | Butler 2023, 10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains pages 1-2) | Anaerobic terminal reductase; strong evidence in *B. fragilis*. |
| Protein / complex | cytochrome bd oxidase | GO:0015002 | Butler 2023, 10.1128/jb.00389-22; Grund 2023, 10.3389/fchem.2022.1085463 (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains pages 5-7) | Key high-affinity terminal oxidase repeatedly linked to low-O2 respiration and facultative aerobiosis. |
| Protein / complex | cytochrome bd-I oxidase | label-only candidate | Nastasi 2024, 10.3390/ijms25021277 (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024membraneboundredoxenzyme pages 2-4) | *E. coli* subtype with strong CO resistance; useful subtype if modeling oxidase diversity. |
| Protein / complex | cytochrome bd-II oxidase | label-only candidate | Nastasi 2024, 10.3390/ijms25021277 (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024membraneboundredoxenzyme pages 13-15) | *E. coli* subtype with reported Km(O2) ~2 µM; strong low-O2 specialization evidence. |
| Protein / complex | cytochrome bo3 oxidase | label-only candidate | Nastasi 2024, 10.3390/ijms25021277 (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024membraneboundredoxenzyme pages 13-15) | Lower-affinity aerobic terminal oxidase favored at higher aeration; include for branch competition. |
| Protein / complex | cytochrome cbb3 oxidase | label-only candidate | Alleman 2023, 10.1128/aem.00378-23 (alleman2023mechanismsforgenerating pages 7-9) | High-affinity oxidase functioning under low O2 in diazotroph/symbiosis examples; broader facultative relevance. |
| Protein / complex | cytochrome caa3 oxidase | label-only candidate | Alleman 2023, 10.1128/aem.00378-23 (alleman2023mechanismsforgenerating pages 7-9) | Aerobic-condition oxidase contrasted with cbb3 in review evidence; likely optional node. |
| Protein / complex | cyanide-insensitive oxidase (CIO) | label-only candidate | Nastasi 2024, 10.3390/antiox13030383 (nastasi2024cyanideinsensitiveoxidase pages 2-3) | bd-type oxidase in *Pseudomonas aeruginosa* supporting stress-tolerant microaerobic respiration. |
| Protein / enzyme | NQR (Na+-translocating NADH:quinone oxidoreductase) | label-only candidate | Butler 2023, 10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains media 83284cef) | Major NADH dehydrogenase branch in *B. fragilis*; 77% contribution in cited assay. |
| Protein / enzyme | NDH2 (type II NADH dehydrogenase) | label-only candidate | Butler 2023, 10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains media 83284cef) | Secondary NADH dehydrogenase branch in *B. fragilis*; 23% contribution in cited assay. |
| Protein / enzyme | NDHII-cytochrome bd respiratory protection branch | label-only candidate | Alleman 2023, 10.1128/aem.00378-23 (alleman2023mechanismsforgenerating pages 7-9) | Review-derived module for rapid O2 consumption under diazotrophic/low-O2 protection scenarios. |
| Regulator | ArcA response regulator | label-only candidate | Brown 2023, 10.1128/mbio.01448-23; Lamoureux 2023, 10.1093/nar/gkad750 (brown2023conservedmetabolicregulator pages 12-14, brown2023conservedmetabolicregulator pages 1-3, lamoureux2023amultiscaleexpression pages 10-12) | Core regulatory node for quinone/redox-linked repression of aerobic functions and promotion of fermentation. |
| Regulator | ArcB sensor kinase | label-only candidate | Brown 2023, 10.1128/mbio.01448-23 (brown2023conservedmetabolicregulator pages 12-14) | Sensor component of ArcAB; senses ETC/quinone redox state. |
| Regulator | ArcAB two-component system | label-only candidate | Brown 2023, 10.1128/mbio.01448-23 (brown2023conservedmetabolicregulator pages 12-14, brown2023conservedmetabolicregulator pages 1-3) | Good high-level regulator node if graph need not split ArcA and ArcB. |
| Regulator | FNR transcription factor | label-only candidate | Lamoureux 2023, 10.1093/nar/gkad750 (lamoureux2023amultiscaleexpression pages 10-12) | Canonical oxygen-sensitive regulator via [4Fe-4S] cluster oxidation; broadly relevant to facultative switching. |
| Cofactor / sensing module | [4Fe-4S] cluster of FNR | label-only candidate | Lamoureux 2023, 10.1093/nar/gkad750 (lamoureux2023amultiscaleexpression pages 10-12) | Optional mechanistic node if modeling direct oxygen sensing chemistry. |
| Regulator | Crp | label-only candidate | Liu 2025, 10.1128/spectrum.03324-24 (liu2025crpandarc pages 1-2) | Relevant to respiratory remodeling in *Shewanella*; weaker for immediate 2023-2024 core graph, use with caution. |
| Phenotype | facultatively aerobic | METPO:1000608 | Trait definition supported by Butler 2023; Felczak 2023; Dyksma 2023 (butler2023bacteroidesfragilismaintains pages 1-2, felczak2023respirationisessential pages 2-4, dyksma2023oxygenrespirationand pages 1-2) | Target trait node; growth without O2 but capable of aerobic growth. |


*Table: This table lists candidate nodes for a TraitMech-style causal graph of the facultatively aerobic phenotype, grouped across environments, chemicals, pathways, respiratory complexes, and regulators. It is designed to support node selection and grounding before edge curation.*

## 5) Evidence-backed candidate causal edges (triples)

The following table proposes candidate edges for the causal graph, each backed by specific evidence snippets and DOI-first references.

| Edge ID | Subject node (label + CURIE if known) | Predicate | Object node (label + CURIE if known) | Evidence snippet (short quote) | Source (first author year, DOI, URL, publication date) | Notes (taxon-specific? uncertain? assay-specific?) |
|---|---|---|---|---|---|---|
| FAER-01 | molecular oxygen; CHEBI:15379 | enables | aerobic growth; GO:0009060 | “can grow without oxygen yet can respire using oxygen at low (nanaerobic) levels” (butler2023bacteroidesfragilismaintains pages 1-2) | Butler 2023; doi:10.1128/jb.00389-22; https://doi.org/10.1128/jb.00389-22; 2023-01 | Core trait-defining edge; shown in *Bacteroides fragilis*; low-O2/nanaerobic assay context. |
| FAER-02 | fumarate reductase complex; label-only candidate | enables | growth in absence of oxygen; label-only candidate | “Anaerobic respiration (NADH to fumarate) uses… fumarate reductase” and “which terminal enzyme is active depends on availability of the final electron acceptor” (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains media 83284cef) | Butler 2023; doi:10.1128/jb.00389-22; https://doi.org/10.1128/jb.00389-22; 2023-01 | Taxon-specific direct evidence in *B. fragilis*; good mechanistic template for facultative aerobiosis. |
| FAER-03 | cytochrome bd oxidase; GO:0015002 | uses_as_terminal_electron_acceptor | molecular oxygen; CHEBI:15379 | “Nanaerobic respiration uses cytochrome bd… to reduce oxygen” (butler2023bacteroidesfragilismaintains pages 1-2) | Butler 2023; doi:10.1128/jb.00389-22; https://doi.org/10.1128/jb.00389-22; 2023-01 | Strong edge; low-oxygen/nanaerobic context; applicable beyond *Bacteroides* but demonstrated here in one taxon. |
| FAER-04 | fumarate reductase complex; label-only candidate | uses_as_terminal_electron_acceptor | fumarate; CHEBI:18012 | “Fumarate reductase and cytochrome bd are both present, and which of these terminal enzymes is active… depends on… fumarate or oxygen” (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains media 83284cef) | Butler 2023; doi:10.1128/jb.00389-22; https://doi.org/10.1128/jb.00389-22; 2023-01 | Strong but pathway-specific; useful for alternative-respiration branch. |
| FAER-05 | terminal electron acceptor availability; label-only candidate | determines | terminal respiratory branch choice; label-only candidate | “which terminal enzyme is active depends on the availability of the final electron acceptor: fumarate or oxygen” (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains media 83284cef) | Butler 2023; doi:10.1128/jb.00389-22; https://doi.org/10.1128/jb.00389-22; 2023-01 | High-value abstract edge for causal graph; based on model schematic plus text. |
| FAER-06 | NQR; label-only candidate | feeds_electrons_to | menaquinone pool; CHEBI:18064 | “starting from NADH, which passes electrons to the menaquinone pool (MK 8-11) through either NQR or NDH2” (butler2023bacteroidesfragilismaintains media 83284cef) | Butler 2023; doi:10.1128/jb.00389-22; https://doi.org/10.1128/jb.00389-22; 2023-01 | Figure-model derived; curated as mechanistic ETC edge; assay/model synthesis. |
| FAER-07 | NDH2; label-only candidate | feeds_electrons_to | menaquinone pool; CHEBI:18064 | “electrons to the menaquinone pool… through either NQR or NDH2” (butler2023bacteroidesfragilismaintains media 83284cef) | Butler 2023; doi:10.1128/jb.00389-22; https://doi.org/10.1128/jb.00389-22; 2023-01 | Figure-model derived; taxon-specific but mechanistically standard. |
| FAER-08 | cytochrome bd oxidase; GO:0015002 | increases | oxygen-dependent NADH consumption | “cytochrome bd activity is assayed as oxygen-dependent NADH consumption… ~5-fold higher in nanaerobic versus anaerobic cultures” (butler2023bacteroidesfragilismaintains pages 5-7) | Butler 2023; doi:10.1128/jb.00389-22; https://doi.org/10.1128/jb.00389-22; 2023-01 | Strong quantitative support; assay-specific biochemical readout. |
| FAER-09 | molecular oxygen; CHEBI:15379 | increases | cytochrome bd activity; GO:0015002 | “Under nanaerobic conditions cytochrome bd activity and CydA protein increase” (butler2023bacteroidesfragilismaintains pages 1-2) | Butler 2023; doi:10.1128/jb.00389-22; https://doi.org/10.1128/jb.00389-22; 2023-01 | Direct but low-O2 specific; use as conditional edge if ontology supports context. |
| FAER-10 | cytochrome bd oxidase subunit CydA; label-only candidate | part_of | cytochrome bd oxidase; GO:0015002 | “the CydA subunit is produced under both anaerobic and nanaerobic conditions” (butler2023bacteroidesfragilismaintains pages 5-7) | Butler 2023; doi:10.1128/jb.00389-22; https://doi.org/10.1128/jb.00389-22; 2023-01 | Structural/composition edge; may be too generic unless graph needs protein-to-complex links. |
| FAER-11 | cytochrome bd quinol oxidase (cydAB); label-only candidate | enables | oxygen respiration | “deletion of cydAB completely inhibited O2 respiration” (felczak2023respirationisessential pages 2-4) | Felczak 2023; doi:10.1128/mbio.02043-23; https://doi.org/10.1128/mbio.02043-23; 2023-12 | Strong experimental genetics in *Zymomonas mobilis*; good facultative-aerobic support. |
| FAER-12 | cytochrome bd quinol oxidase (cydAB); label-only candidate | enables | aerobic growth; GO:0009060 | “loss of cydAB… strongly impairs aerobic growth” and final OD600 “0.29 ± 0.01 versus WT 4.54 ± 0.06” (felczak2023respirationisessential pages 2-4) | Felczak 2023; doi:10.1128/mbio.02043-23; https://doi.org/10.1128/mbio.02043-23; 2023-12 | Very strong but species-specific; aerobic-growth branch of facultative trait. |
| FAER-13 | water-forming NADH oxidase NoxE; label-only candidate | restores | aerobic growth; GO:0009060 | “a rescue experiment with water-forming NADH oxidase (NoxE)… suggest[s] that one key ETC role is oxygen removal” (felczak2023respirationisessential pages 2-4) | Felczak 2023; doi:10.1128/mbio.02043-23; https://doi.org/10.1128/mbio.02043-23; 2023-12 | Useful but heterologous complementation; curate as assay-specific/engineered. |
| FAER-14 | electron transport chain; GO:0022900 | decreases | intracellular molecular oxygen; CHEBI:15379 | “The authors propose the primary physiological role of the ETC… is lowering intracellular molecular oxygen” (felczak2023respirationisessential pages 1-2) | Felczak 2023; doi:10.1128/mbio.02043-23; https://doi.org/10.1128/mbio.02043-23; 2023-12 | Mechanistic interpretation; may be species-specific and partly inferential. |
| FAER-15 | ArcAB two-component system; label-only candidate | represses | aerobic respiration; GO:0009060 | “ArcAB, a two-component regulatory system that represses aerobic respiration” (brown2023conservedmetabolicregulator pages 1-3) | Brown 2023; doi:10.1128/mbio.01448-23; https://doi.org/10.1128/mbio.01448-23; 2023-10 | Strong regulator edge in Enterobacterales; relevant general switch mechanism. |
| FAER-16 | ArcB sensor kinase; label-only candidate | senses | quinone-pool redox state; label-only candidate | “ArcAB senses ETC redox state via the quinone pool” and “when electrons route to ArcB rather than to oxygen…” (brown2023conservedmetabolicregulator pages 12-14) | Brown 2023; doi:10.1128/mbio.01448-23; https://doi.org/10.1128/mbio.01448-23; 2023-10 | Mechanistic sensing edge; broad facultative Enterobacterales relevance. |
| FAER-17 | ArcA response regulator; label-only candidate | promotes | fermentation; GO:0006113 | “ArcA-mediated shift to fermentation independent of oxygen availability” (brown2023conservedmetabolicregulator pages 12-14) | Brown 2023; doi:10.1128/mbio.01448-23; https://doi.org/10.1128/mbio.01448-23; 2023-10 | Strong in infection/stress assays; useful for anaerobic branch. |
| FAER-18 | ArcA response regulator; label-only candidate | represses | respiratory operons nuo/shd; label-only candidate | “repressing respiratory operons (nuo, shd) and shifting metabolism toward lactate/acetate production” (brown2023conservedmetabolicregulator pages 12-14) | Brown 2023; doi:10.1128/mbio.01448-23; https://doi.org/10.1128/mbio.01448-23; 2023-10 | Specific operon edge; taxon-specific; may be too detailed for high-level trait graph. |
| FAER-19 | FNR transcription factor; label-only candidate | activated_by | [4Fe-4S] cluster assembly; label-only candidate | “Fnr is activated by assembly of a 4Fe–4S iron–sulfur cluster and dimerization” (lamoureux2023amultiscaleexpression pages 10-12) | Lamoureux 2023; doi:10.1093/nar/gkad750; https://doi.org/10.1093/nar/gkad750; 2023-09 | Canonical regulatory mechanism; strong for facultative anaerobe/aerobe switching. |
| FAER-20 | molecular oxygen; CHEBI:15379 | inactivates | FNR transcription factor; label-only candidate | “oxygen directly inactivates Fnr by oxidizing that iron–sulfur cluster” (lamoureux2023amultiscaleexpression pages 10-12) | Lamoureux 2023; doi:10.1093/nar/gkad750; https://doi.org/10.1093/nar/gkad750; 2023-09 | Core oxygen-sensing edge; strong and widely generalizable. |
| FAER-21 | active FNR transcription factor; label-only candidate | activates | anaerobic metabolism genes; label-only candidate | “when active, Fnr activates anaerobic metabolism genes and represses aerobic genes” (lamoureux2023amultiscaleexpression pages 10-12) | Lamoureux 2023; doi:10.1093/nar/gkad750; https://doi.org/10.1093/nar/gkad750; 2023-09 | High-level regulatory edge; broad relevance. |
| FAER-22 | active FNR transcription factor; label-only candidate | represses | aerobic metabolism genes; label-only candidate | “Fnr activates anaerobic metabolism genes and represses aerobic genes” (lamoureux2023amultiscaleexpression pages 10-12) | Lamoureux 2023; doi:10.1093/nar/gkad750; https://doi.org/10.1093/nar/gkad750; 2023-09 | High-level regulatory edge; broad relevance. |
| FAER-23 | sulfate reduction pathway; label-only candidate | enables | growth in absence of oxygen; label-only candidate | “switches between sulfate reduction under anoxic conditions and oxygen reduction under oxic conditions” (dyksma2023oxygenrespirationand pages 1-2) | Dyksma 2023; doi:10.1038/s41467-023-42074-z; https://doi.org/10.1038/s41467-023-42074-z; 2023-10 | Strong but from Acidobacteriota enrichment/metatranscriptomics, not isolate-only genetics. |
| FAER-24 | oxygen reduction pathway; label-only candidate | enables | growth in presence of oxygen; label-only candidate | “differential gene expression show it switches between sulfate reduction under anoxic conditions and oxygen reduction under oxic conditions” (dyksma2023oxygenrespirationand pages 1-2) | Dyksma 2023; doi:10.1038/s41467-023-42074-z; https://doi.org/10.1038/s41467-023-42074-z; 2023-10 | Strong phenotype-to-pathway edge; community/enrichment setting. |
| FAER-25 | oxic conditions; ENVO:01000627 | induces | oxygen reduction pathway; label-only candidate | “switch from sulfate to oxygen reduction when shifting from anoxic to oxic conditions” (dyksma2023oxygenrespirationand pages 1-2) | Dyksma 2023; doi:10.1038/s41467-023-42074-z; https://doi.org/10.1038/s41467-023-42074-z; 2023-10 | Environmental-condition edge; useful for causal context node. |
| FAER-26 | cytochrome bd oxidase; GO:0015002 | has_high_affinity_for | molecular oxygen; CHEBI:15379 | “cytochrome bd accumulates during high aeration… and is required for diazotrophic growth”; “high O2 consumption rate at the cell surface” in respiratory protection branch (alleman2023mechanismsforgenerating pages 7-9) | Alleman 2023; doi:10.1128/aem.00378-23; https://doi.org/10.1128/aem.00378-23; 2023-05 | Review-derived mechanistic generalization; not direct trait assay but strong supporting concept. |
| FAER-27 | NDHII–cytochrome bd respiratory protection branch; label-only candidate | enables | rapid oxygen consumption; label-only candidate | “uses a decoupled branch of the ETC (NDHII and cytochrome bd)… to enable a high O2 consumption rate at the cell surface” (alleman2023mechanismsforgenerating pages 7-9) | Alleman 2023; doi:10.1128/aem.00378-23; https://doi.org/10.1128/aem.00378-23; 2023-05 | Strong mechanistic concept; mostly from diazotroph literature; broad but not universal. |
| FAER-28 | cytochrome cbb3 oxidase; label-only candidate | enables | respiration under low oxygen; label-only candidate | “The high-affinity cbb3 oxidase functions under low O2, whereas caa3 predominates in aerobic conditions” (alleman2023mechanismsforgenerating pages 7-9) | Alleman 2023; doi:10.1128/aem.00378-23; https://doi.org/10.1128/aem.00378-23; 2023-05 | Important alternative oxidase edge; not specific to all facultative aerobes. |
| FAER-29 | cytochrome caa3 oxidase; label-only candidate | enables | respiration under aerobic conditions; label-only candidate | “caa3 predominates in aerobic conditions” (alleman2023mechanismsforgenerating pages 7-9) | Alleman 2023; doi:10.1128/aem.00378-23; https://doi.org/10.1128/aem.00378-23; 2023-05 | Complementary branch edge; review-based. |
| FAER-30 | microaerobic conditions; ENVO:01000632 | activates | bd-type oxidase expression; label-only candidate | “microaerobic shifts activate bd-type oxidases” (nastasi2024membraneboundredoxenzyme pages 2-4) | Nastasi 2024; doi:10.3390/ijms25021277; https://doi.org/10.3390/ijms25021277; 2024-01 | Strong and concise; *E. coli* expression-context edge. |
| FAER-31 | cytochrome bd-I oxidase; label-only candidate | confers_resistance_to | carbon monoxide; CHEBI:17245 | “96.3 µM CO inhibited bd-I-only respiration by only 11.6 ± 1.1%” while other oxidases were much more inhibited (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024membraneboundredoxenzyme pages 2-4) | Nastasi 2024; doi:10.3390/ijms25021277; https://doi.org/10.3390/ijms25021277; 2024-01 | Useful robustness edge, but not central to trait definition; assay-specific. |
| FAER-32 | cytochrome bd-II oxidase; label-only candidate | has_high_affinity_for | molecular oxygen; CHEBI:15379 | “Km(O2) values used were 2 µM for cytochrome bd-II and 6 µM for cytochrome bo3” (nastasi2024membraneboundredoxenzyme pages 13-15, nastasi2024membraneboundredoxenzyme pages 4-7) | Nastasi 2024; doi:10.3390/ijms25021277; https://doi.org/10.3390/ijms25021277; 2024-01 | Strong quantitative support for low-O2 respiration; specific to oxidase subtype. |
| FAER-33 | cyanide-insensitive oxidase (CIO, bd-type); label-only candidate | enables | growth under microaerobic conditions; ENVO:01000632 | “A cco1/cco2 double mutant grew under microaerobic conditions (2% O2), while a cco1/cco2/cio triple mutant did not” (nastasi2024cyanideinsensitiveoxidase pages 2-3) | Nastasi 2024; doi:10.3390/antiox13030383; https://doi.org/10.3390/antiox13030383; 2024-03 | Strong genetics in *Pseudomonas aeruginosa*; species-specific. |
| FAER-34 | cyanide-insensitive oxidase (CIO, bd-type); label-only candidate | confers_resistance_to | hydrogen sulfide; CHEBI:16136 | “O2 consumption by CIO is unaltered even in the presence of high levels of H2S” (nastasi2024cyanideinsensitiveoxidase pages 2-3) | Nastasi 2024; doi:10.3390/antiox13030383; https://doi.org/10.3390/antiox13030383; 2024-03 | Stress-tolerance edge; useful for low-O2/host niches but secondary to trait core. |
| FAER-35 | cyanide-insensitive oxidase (CIO, bd-type); label-only candidate | confers_resistance_to | nitric oxide; CHEBI:16480 | “CIO is reversibly inhibited by NO, while activity recovery after NO exhaustion is full and fast” (nastasi2024cyanideinsensitiveoxidase pages 2-3) | Nastasi 2024; doi:10.3390/antiox13030383; https://doi.org/10.3390/antiox13030383; 2024-03 | Stress/host-response edge; likely niche-specific. |


*Table: This table lists evidence-backed causal triples for the facultatively aerobic trait, emphasizing oxygen-responsive regulation, alternate terminal electron acceptors, and respiratory-chain components that support switching between oxic and anoxic growth modes.*

### Visual evidence (pathway schematic)

A key schematic supporting the branched architecture (NADH → menaquinone pool → cytochrome bd oxidase vs fumarate reductase) is captured from Butler et al. 2023 (Fig. 5). (butler2023bacteroidesfragilismaintains media 83284cef)

## 6) Current applications and real-world implementations

### 6.1 Host-associated niches (gut and infection)

- **Gut epithelium oxygen gradients (“nanaerobiosis”):** *B. fragilis* is described as capable of oxygen respiration at gut-adjacent “nanaerobic” oxygen levels, quantified as **1,000–1,500 ppm O\₂**. Mechanistically, this can be implemented by cytochrome bd using O\₂ as terminal acceptor while maintaining anaerobic fumarate reductase machinery concurrently. This is directly relevant to real-world colonization where O\₂ diffuses from epithelial cells. (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains media 83284cef)

- **Bloodstream infection (bacteremia):** Gram-negative facultative anaerobes in vivo face tissue oxygen limitation and stresses; ArcA-dependent regulation links ETC/redox state to fermentation shifts and fitness. The spleen doubling time measurements (39–66 min range depending on species) provide recent quantitative evidence that such oxygen-flexible regulation has measurable impacts on pathogen population dynamics. (brown2023conservedmetabolicregulator pages 12-14)

- **Microaerobic/hypoxic infection stresses:** In P. aeruginosa, bd-type CIO supports growth under 2% O\₂ in specific mutant backgrounds and is linked to tolerance against H\₂S/NO, both abundant in chronic infection contexts such as cystic fibrosis. (nastasi2024cyanideinsensitiveoxidase pages 2-3)

### 6.2 Industrial/bioprocessing contexts

- **Biofuel fermentation chassis robustness to oxygen:** *Zymomonas mobilis* is a platform organism for ethanol production. The 2023 findings that cydAB is essential for aerobic growth, and that WT oxygen consumption is ~0.941 mg/L/min, are directly actionable for bioprocess design (oxygen ingress, aeration control, and chassis engineering constraints). (felczak2023respirationisessential pages 2-4)

- **Engineered redox-cycling bioreactors:** A 2023 Nature Communications study enriched an Acidobacteriota population in a bioreactor alternated between oxic (50% air-O\₂ saturation for one week) and anoxic conditions, with pectin 0.5 g/L and sulfate 1 mM at pH 4.5 (dilution rate 0.025 d⁻¹). The organism switched between sulfate reduction and oxygen respiration, demonstrating real-world relevance to fluctuating redox environments in engineered systems. (dyksma2023oxygenrespirationand pages 1-2)

## 7) Expert synthesis and curation guidance

### 7.1 High-confidence mechanistic “backbone” for a TraitMech graph

Based on 2023–2024 evidence, a curation-ready backbone for **facultatively aerobic** can be:

1. **O\₂ availability** → enables **cytochrome bd oxidase activity** → enables **aerobic (or nanaerobic) respiration** → supports aerobic growth (supported in *B. fragilis* and *Z. mobilis*). (butler2023bacteroidesfragilismaintains pages 1-2, felczak2023respirationisessential pages 2-4)
2. **Anoxic conditions / alternative electron acceptor availability** (e.g., fumarate, sulfate) → enables **anaerobic respiration pathways** (fumarate reductase; sulfate reduction) → supports growth without oxygen. (butler2023bacteroidesfragilismaintains pages 2-5, dyksma2023oxygenrespirationand pages 1-2)
3. **O\₂ sensing and redox regulation**: FNR (direct [4Fe–4S] O\₂ inactivation) and ArcAB (quinone-pool redox proxy) regulate the shift between aerobic/anaerobic programs and fermentation. (brown2023conservedmetabolicregulator pages 12-14, lamoureux2023amultiscaleexpression pages 10-12)

### 7.2 Key statistics to preserve in curation notes

- *Z. mobilis* WT oxygen consumption: **0.941 ± 0.017 mg/L/min**; ΔcydAB: **0.6% of WT**; aerobic growth endpoint OD\₆₀₀ WT **4.54 ± 0.06** vs ΔcydAB **0.29 ± 0.01**. (felczak2023respirationisessential pages 2-4)
- *E. coli* oxidase inhibition example: at 100 µM O\₂, 96.3 µM CO inhibits bd-I-only respiration **11.6 ± 1.1%** vs bd-II-only **43.3 ± 7.6%** and bo\₃-only **44.3 ± 1.5%**. (nastasi2024membraneboundredoxenzyme pages 4-7)
- *P. aeruginosa* CIO O\₂ affinity: **Km(O\₂) = 4.0 ± 2.1 µM**; growth supported at **2% O\₂** in specific oxidase mutant backgrounds. (nastasi2024cyanideinsensitiveoxidase pages 2-3)
- Bacteremia population doubling times: **39–66 min** across species in mouse spleen context. (brown2023conservedmetabolicregulator pages 12-14)

## 8) Warnings / non-curatable or uncertain claims

1. **“Nanaerobic” oxygen level conversion ambiguity:** The *B. fragilis* paper reports 1,000–1,500 ppm O\₂ and also gives an approximate molar concentration; because ppm↔µM conversions depend on temperature, pressure, medium, and gas/liquid partitioning, **curate oxygen ranges as reported (ppm) unless the original paper provides a validated dissolved O\₂ measurement**. (butler2023bacteroidesfragilismaintains pages 1-2)
2. **Review-derived oxidase generalizations:** Edges such as “cytochrome bd has high O\₂ affinity” or “respiratory protection branch enables high O\₂ consumption” are strongly plausible and widely accepted, but where supported primarily by review synthesis (e.g., nitrogen fixation respiratory protection framing), they should be flagged as **general but not universal**. (alleman2023mechanismsforgenerating pages 7-9)
3. **Taxon specificity of anaerobic branches:** Fumarate respiration (as curated here) is strongly supported in *B. fragilis* but will not apply to all facultatively aerobic taxa; similarly sulfate reduction switching is taxon-specific. These should be curated as **optional branch modules** or with taxon constraints if your schema supports it. (butler2023bacteroidesfragilismaintains pages 2-5, dyksma2023oxygenrespirationand pages 1-2)
4. **Engineered/heterologous complementation edges:** Rescue by heterologous water-forming NADH oxidase (NoxE) in *Z. mobilis* is highly informative but should be marked **assay-specific/engineered** rather than natural physiology. (felczak2023respirationisessential pages 2-4)

## 9) DOI-first bibliography (with URLs and publication dates)

- Butler NL, Ito T, Foreman S, et al. *Bacteroides fragilis Maintains Concurrent Capability for Anaerobic and Nanaerobic Respiration.* **Journal of Bacteriology** (2023-01). DOI: **10.1128/jb.00389-22**. URL: https://doi.org/10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains media 83284cef)
- Felczak MM, Bernard MP, TerAvest MA. *Respiration is essential for aerobic growth of Zymomonas mobilis ZM4.* **mBio** (2023-12). DOI: **10.1128/mbio.02043-23**. URL: https://doi.org/10.1128/mbio.02043-23 (felczak2023respirationisessential pages 2-4)
- Brown AN, Anderson MT, Smith SN, et al. *Conserved metabolic regulator ArcA responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia.* **mBio** (2023-10). DOI: **10.1128/mbio.01448-23**. URL: https://doi.org/10.1128/mbio.01448-23 (brown2023conservedmetabolicregulator pages 12-14)
- Lamoureux CR, Decker KT, Sastry AV, et al. *A multi-scale expression and regulation knowledge base for Escherichia coli.* **Nucleic Acids Research** (2023-09). DOI: **10.1093/nar/gkad750**. URL: https://doi.org/10.1093/nar/gkad750 (lamoureux2023amultiscaleexpression pages 10-12)
- Dyksma S, Pester M. *Oxygen respiration and polysaccharide degradation by a sulfate-reducing acidobacterium.* **Nature Communications** (2023-10). DOI: **10.1038/s41467-023-42074-z**. URL: https://doi.org/10.1038/s41467-023-42074-z (dyksma2023oxygenrespirationand pages 1-2)
- Alleman AB, Peters JW. *Mechanisms for Generating Low Potential Electrons across the Metabolic Diversity of Nitrogen-Fixing Bacteria.* **Applied and Environmental Microbiology** (2023-05). DOI: **10.1128/aem.00378-23**. URL: https://doi.org/10.1128/aem.00378-23 (alleman2023mechanismsforgenerating pages 7-9)
- Nastasi MR, Borisov VB, Forte E. *Membrane-Bound Redox Enzyme Cytochrome bd-I Promotes Carbon Monoxide-Resistant Escherichia coli Growth and Respiration.* **International Journal of Molecular Sciences** (2024-01). DOI: **10.3390/ijms25021277**. URL: https://doi.org/10.3390/ijms25021277 (nastasi2024membraneboundredoxenzyme pages 4-7)
- Nastasi MR, Caruso L, Giordano F, et al. *Cyanide Insensitive Oxidase Confers Hydrogen Sulfide and Nitric Oxide Tolerance to Pseudomonas aeruginosa Aerobic Respiration.* **Antioxidants** (2024-03). DOI: **10.3390/antiox13030383**. URL: https://doi.org/10.3390/antiox13030383 (nastasi2024cyanideinsensitiveoxidase pages 2-3)

---

**Deliverable readiness for `data/traits/environment/facultatively_aerobic.yaml`:** The node list (artifact-01) and edge list (artifact-00), plus the branched ETC schematic (butler2023bacteroidesfragilismaintains media 83284cef), together provide a source-backed foundation for curating a TraitMech causal graph of facultatively aerobic growth, with multiple 2023–2024 primary sources and quantitative values for key edges.


References

1. (butler2023bacteroidesfragilismaintains pages 1-2): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

2. (dyksma2023oxygenrespirationand pages 1-2): Stefan Dyksma and Michael Pester. Oxygen respiration and polysaccharide degradation by a sulfate-reducing acidobacterium. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42074-z, doi:10.1038/s41467-023-42074-z. This article has 65 citations and is from a highest quality peer-reviewed journal.

3. (lamoureux2023amultiscaleexpression pages 10-12): Cameron R Lamoureux, Katherine T Decker, Anand V Sastry, Kevin Rychel, Ye Gao, John Luke McConn, Daniel C Zielinski, and Bernhard O Palsson. A multi-scale expression and regulation knowledge base for escherichia coli. Nucleic Acids Research, 51:10176-10193, Sep 2023. URL: https://doi.org/10.1093/nar/gkad750, doi:10.1093/nar/gkad750. This article has 56 citations and is from a highest quality peer-reviewed journal.

4. (felczak2023respirationisessential pages 2-4): Magdalena M. Felczak, Matthew P. Bernard, and Michaela A. TerAvest. Respiration is essential for aerobic growth of <i>zymomonas mobilis</i> zm4. Dec 2023. URL: https://doi.org/10.1128/mbio.02043-23, doi:10.1128/mbio.02043-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

5. (butler2023bacteroidesfragilismaintains pages 2-5): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

6. (brown2023conservedmetabolicregulator pages 12-14): Aric N. Brown, Mark T. Anderson, Sara N. Smith, Michael A. Bachman, and Harry L. T. Mobley. Conserved metabolic regulator arca responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia. Oct 2023. URL: https://doi.org/10.1128/mbio.01448-23, doi:10.1128/mbio.01448-23. This article has 11 citations and is from a domain leading peer-reviewed journal.

7. (butler2023bacteroidesfragilismaintains media 83284cef): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

8. (butler2023bacteroidesfragilismaintains pages 5-7): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

9. (brown2023conservedmetabolicregulator pages 1-3): Aric N. Brown, Mark T. Anderson, Sara N. Smith, Michael A. Bachman, and Harry L. T. Mobley. Conserved metabolic regulator arca responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia. Oct 2023. URL: https://doi.org/10.1128/mbio.01448-23, doi:10.1128/mbio.01448-23. This article has 11 citations and is from a domain leading peer-reviewed journal.

10. (nastasi2024membraneboundredoxenzyme pages 4-7): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

11. (nastasi2024membraneboundredoxenzyme pages 13-15): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

12. (nastasi2024cyanideinsensitiveoxidase pages 2-3): Martina R. Nastasi, Lorenzo Caruso, Francesca Giordano, Marta Mellini, Giordano Rampioni, Alessandro Giuffrè, and Elena Forte. Cyanide insensitive oxidase confers hydrogen sulfide and nitric oxide tolerance to pseudomonas aeruginosa aerobic respiration. Antioxidants, 13:383, Mar 2024. URL: https://doi.org/10.3390/antiox13030383, doi:10.3390/antiox13030383. This article has 8 citations.

13. (felczak2023respirationisessential pages 1-2): Magdalena M. Felczak, Matthew P. Bernard, and Michaela A. TerAvest. Respiration is essential for aerobic growth of <i>zymomonas mobilis</i> zm4. Dec 2023. URL: https://doi.org/10.1128/mbio.02043-23, doi:10.1128/mbio.02043-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

14. (nastasi2024membraneboundredoxenzyme pages 2-4): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

15. (alleman2023mechanismsforgenerating pages 7-9): Alexander B. Alleman and John W. Peters. Mechanisms for generating low potential electrons across the metabolic diversity of nitrogen-fixing bacteria. Applied and Environmental Microbiology, May 2023. URL: https://doi.org/10.1128/aem.00378-23, doi:10.1128/aem.00378-23. This article has 54 citations and is from a peer-reviewed journal.

16. (liu2025crpandarc pages 1-2): Jia-Rong Liu, Zhi-Qing Wang, Fei-Fei Li, Zhen-Kun Li, Ming-Chen Wang, Na Wang, Yu An, Xiu-Lan Chen, Yu-Zhong Zhang, and Hui-Hui Fu. Crp and arc system directly regulate the transcription of nadh dehydrogenase genes in <i>shewanella oneidensis</i> nitrate and nitrite respiration. Jul 2025. URL: https://doi.org/10.1128/spectrum.03324-24, doi:10.1128/spectrum.03324-24. This article has 1 citations and is from a domain leading peer-reviewed journal.