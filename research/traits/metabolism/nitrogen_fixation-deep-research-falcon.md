---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:21:15.418444'
end_time: '2026-06-18T05:49:47.620208'
duration_seconds: 1712.2
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: nitrogen fixation
  trait_identifier: traitmech:000103
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: nitrogen_fixation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which an organism reduces atmospheric dinitrogen (N2)
    to ammonia using the nitrogenase enzyme complex, making fixed nitrogen biologically
    available (diazotrophy).
  parent_traits: METPO:1000060
  synonyms: diazotrophy
  evidence_summary: 'DOI:10.1038/nrmicro.2018.9:  (Kuypers, Marchant & Kartal place
    nitrogen fixation as the reductive entry point of the microbial nitrogen-cycling
    network.) | DOI:10.1038/nrmicro954:  (Dixon & Kahn review the genetic regulation
    of biological nitrogen fixation and nitrogenase.)'
  causal_graph_summary: 'nitrogen_fixation_nitrogenase: 5 nodes, 4 edges'
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
- **Trait label:** nitrogen fixation
- **METPO identifier:** traitmech:000103
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism reduces atmospheric dinitrogen (N2) to ammonia using the nitrogenase enzyme complex, making fixed nitrogen biologically available (diazotrophy).
- **Parent traits:** METPO:1000060
- **Synonyms:** diazotrophy
- **Existing evidence:** DOI:10.1038/nrmicro.2018.9:  (Kuypers, Marchant & Kartal place nitrogen fixation as the reductive entry point of the microbial nitrogen-cycling network.) | DOI:10.1038/nrmicro954:  (Dixon & Kahn review the genetic regulation of biological nitrogen fixation and nitrogenase.)
- **Existing causal graph summary:** nitrogen_fixation_nitrogenase: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **nitrogen fixation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/nitrogen_fixation.yaml`.

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
- **Trait label:** nitrogen fixation
- **METPO identifier:** traitmech:000103
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism reduces atmospheric dinitrogen (N2) to ammonia using the nitrogenase enzyme complex, making fixed nitrogen biologically available (diazotrophy).
- **Parent traits:** METPO:1000060
- **Synonyms:** diazotrophy
- **Existing evidence:** DOI:10.1038/nrmicro.2018.9:  (Kuypers, Marchant & Kartal place nitrogen fixation as the reductive entry point of the microbial nitrogen-cycling network.) | DOI:10.1038/nrmicro954:  (Dixon & Kahn review the genetic regulation of biological nitrogen fixation and nitrogenase.)
- **Existing causal graph summary:** nitrogen_fixation_nitrogenase: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **nitrogen fixation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/nitrogen_fixation.yaml`.

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


## Microbial trait causal-graph report: Nitrogen fixation (diazotrophy; METPO traitmech:000103)

### Scope summary (TraitMech curation)
Nitrogen fixation (diazotrophy) is the **metabolic capability to reduce atmospheric dinitrogen (N2) to ammonia (NH3)**, and is **restricted to microorganisms that carry nitrogenase**. (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4) It is a reductive entry point into the microbial nitrogen network: fixed NH3 can be assimilated into biomass, while other processes (nitrification, denitrification, anammox) transform nitrogen at different redox states and should be treated as distinct traits. (kuypers2018themicrobialnitrogencycling pages 1-4)

**Boundary cases / exclusions for the trait definition**
- Include: organisms or engineered systems with demonstrable nitrogenase-dependent N2→NH3 conversion (e.g., Mo-, V-, Fe-only nitrogenases) measured by biochemical, isotopic, or growth phenotypes. (kuypers2018themicrobialnitrogencycling pages 1-4, bennett2023engineeringnitrogenasesfor pages 1-2)
- Exclude: mere ammonia assimilation (NH4+ uptake/GS-GOGAT), nitrification (NH4+→NO2−→NO3−), denitrification (NO3−→N2), and anammox (NO2− + NH4+ → N2) unless explicitly linked to nitrogenase-mediated N2 reduction. (kuypers2018themicrobialnitrogencycling pages 1-4)

**Operational/assay readouts (how the trait is observed)**
- **Acetylene reduction assay (ARA)**: nitrogenase reduces C2H2→C2H4 as a proxy for activity; used widely in pure culture and engineered systems. (perez2026nonnodulatingrhizobiumlikeaco34a pages 5-7, dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11)
- **15N2 incorporation / nanoSIMS**: direct evidence of N2 reduction into biomass in engineered E. coli and other systems. (solomon2024ammoniasynthesisvia pages 9-10, solomon2024ammoniasynthesisvia pages 7-9)
- **Growth under N2 with limiting fixed N**: engineered nitrogenase systems can produce a post-induction growth advantage under N2 relative to inert gas controls. (solomon2024ammoniasynthesisvia pages 7-9)
- **Marker-gene surveys**: **nifH is widely used as a molecular marker** to profile diazotrophic communities, but marker detection alone is not sufficient to assert activity without complementary assays. (li2024mechanismofmicrobial pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4)

---

## 1) Key concepts & current mechanistic understanding (2023–2024 emphasis)

### 1.1 Core enzymatic mechanism (nitrogenase)
Across diazotroph diversity, nitrogenase catalysis is mechanistically conserved and energetically demanding. Diazotrophs are described as phylogenetically diverse but **all use nitrogenase to reduce N2**, and nitrogenase is **O2-sensitive** and requires **ATP plus low-potential electrons**. (alleman2023mechanismsforgenerating pages 1-3)

**Canonical Mo-nitrogenase reaction stoichiometry**
The net reaction commonly cited for Mo-nitrogenase is:
N2 + 8H+ + 8e− + 16 MgATP → 2 NH3 + H2 + 16 MgADP + 16 Pi. (bennett2023engineeringnitrogenasesfor pages 1-2)
This implies ~**2 ATP per electron transfer** to the catalytic component, and a minimum of **16 ATP per N2** reduced (excluding upstream costs of generating reductant and maintaining protective physiology). (bennett2023engineeringnitrogenasesfor pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4)

**Two-component architecture and electron flow**
Mo-nitrogenase comprises:
- **NifH (Fe protein; dinitrogenase reductase)**: homodimer with a [4Fe–4S] cluster and ATP binding sites; it receives electrons from reduced carriers and delivers them in an ATP-dependent cycle. (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, bennett2023engineeringnitrogenasesfor pages 1-2)
- **NifDK (MoFe protein; dinitrogenase)**: α2β2 component containing the **P-cluster** (electron relay) and **FeMo-cofactor/M-cluster** (substrate reduction site). (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, alleman2023mechanismsforgenerating pages 1-3)

Mechanistically, **Fd/Fld donate electrons to NifH**, and NifH transfers electrons to the **P-cluster**, which relays electrons to **FeMo-co** for N2 reduction. (bennett2023engineeringnitrogenasesfor pages 1-2, alleman2023mechanismsforgenerating pages 1-3)

A key visual summary of this electron-transfer logic (including ATP dependence) is shown in Fig. 1 of Alleman & Peters (2023). (alleman2023mechanismsforgenerating media 6f3977b8)

### 1.2 Oxygen sensitivity and protection
Nitrogenase metal clusters are **oxygen-labile**; both reviews and foundational syntheses emphasize that O2 exposure deactivates nitrogenase, motivating spatial/temporal separation (heterocysts), high respiration, and ROS detox strategies. (alleman2023mechanismsforgenerating pages 1-3, kuypers2018themicrobialnitrogencycling pages 1-4)

For engineering contexts, organellar targeting (e.g., mitochondria) is discussed as a strategy to address oxygen sensitivity of Nif components and intermediates. (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2)

### 1.3 FeMo-cofactor (M-cluster) assembly as a mechanistic subgraph
Nitrogen fixation is not only a catalytic reaction; it depends on a specialized **metallocluster biosynthetic pathway**.

A concise, explicitly described assembly route in a 2024 Nature Catalysis paper includes:
- Delivery of [Fe4S4] pairs to NifDK (P-cluster) and to NifB (M-cluster pathway). (solomon2024ammoniasynthesisvia pages 4-5)
- **NifB converts the K-cluster (a [Fe4S4] pair) into the L-cluster ([Fe8S9C])** via radical SAM chemistry, incorporating a “ninth belt sulfur.” (solomon2024ammoniasynthesisvia pages 4-5)
- **L-cluster transfer to NifEN**, where it is matured into the M-cluster via **NifH-mediated substitution of terminal Fe with Mo/homocitrate**, followed by transfer to apo-NifDK to form holo-NifDK. (solomon2024ammoniasynthesisvia pages 4-5)

This assembly chain provides multiple curatable edges: NifS/NifU→[Fe4S4] modules; NifB→L-cluster; L→NifEN; NifH+Mo/homocitrate→M-cluster; M→apo-NifDK→holo-NifDK. (solomon2024ammoniasynthesisvia pages 4-5)

---

## 2) Recent developments and latest research (prioritizing 2023–2024)

### 2.1 Heterologous nitrogenase assembly and measurable N2 fixation in E. coli (Nature Catalysis, 2024)
A major 2024 advance is demonstration of an **engineered nitrogenase assembly pathway in E. coli** with in vivo evidence of N2 reduction and ammonia handling.

**Mechanistic assembly and “minimal essential gene set” concept**
The study describes heterologous co-expression of nif genes (including nifS,U,H,M,Z,D,K,E,N,B,V and an electron donor such as fdxN) to assemble active Mo-nitrogenase in a non-diazotrophic host. (solomon2024ammoniasynthesisvia pages 4-5)

**Quantitative/traceable outputs (statistics)**
- Heterologously expressed AvNifDK in E. coli shows partial cofactor occupancy: **~34% M-cluster occupancy and ~58% P-cluster occupancy**, aligning with **38–48% of native activity** for N2/H+/C2H2 reduction in vitro. (solomon2024ammoniasynthesisvia pages 7-9)
- In vivo nitrogen fixation evidence via nanoSIMS: **15N2-grown nitrogenase-expressing E. coli (YM538EE) reached 15N/14N = 3.1% ± 0.1% (8.4-fold above natural abundance)**, while controls remained at background. (solomon2024ammoniasynthesisvia pages 9-10)
- Oxygen sensitivity quantified: increasing O2 to **0.1% and 0.2% lowered 15N enrichment by 29% and 46%**. (solomon2024ammoniasynthesisvia pages 9-10)

**Engineering ammonia release as an output phenotype**
Deletion of the ammonia transporter **amtB** allowed **extracellular 15NH4+ accumulation** detected by NMR, and supernatants transferred 15N enrichment to a nitrogenase-free recipient strain. (solomon2024ammoniasynthesisvia pages 9-10)

### 2.2 FeMo-co biosynthesis using proteins produced in yeast mitochondria (mBio, 2024)
A 2024 mBio study advances eukaryotic engineering by demonstrating that **FeMo-co biosynthesis can be recapitulated in vitro using NifB/NifEN/NifH proteins produced in Saccharomyces cerevisiae mitochondria**. (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11, dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2)

**Quantitative/assay readout (ARA units)**
FeMo-co formation was evaluated via apo-NifDK activation and acetylene reduction (ethylene production). Reported activities include **873 ± 124 and 653 ± 91** (nmol ethylene·min−1·mg NifDK−1) for different yeast-produced NifB variants in reconstitution. (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11)

A key caution is that **in vivo nitrogen fixation in a eukaryote is not yet achieved**, in part because a FeMo-co-activatable apo-NifDK has not yet been produced in a eukaryotic host. (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11)

### 2.3 Modern views of regulation: environmental signal integration and RNA-level control (2024)
**NifL/NifA signal integration (oxygen, energy, fixed N)**
A 2024 review using Azotobacter vinelandii as a model explains mechanistic sensing:
- NifA is a σ54-dependent transcriptional activator; NifL modulates NifA by binding/releasing it in response to oxygen/energy/fixed-N cues. (barron2024nitrogenfixinggammaproteobacteria pages 7-8)
- Oxygen sensing via PAS1-FAD oxidation promotes NifL–NifA binding (inhibitory state). (barron2024nitrogenfixinggammaproteobacteria pages 7-8)
- Energy sensing via ADP/ATP binding (ADP favored) biases toward the inhibitory state. (barron2024nitrogenfixinggammaproteobacteria pages 7-8)
- Fixed nitrogen information is transmitted via PII protein GlnK uridylylation state (GlnD-dependent), controlling NifL interaction and repression logic. (barron2024nitrogenfixinggammaproteobacteria pages 7-8)

**Hfq-mediated post-transcriptional regulation (mSphere, 2024)**
In root-associated Pseudomonas stutzeri A1501, eCLIP-seq and transcriptomics identify Hfq-binding to multiple nitrogen-fixation-relevant RNAs, including **nifM** and **amtB**, and interactions with **NifA** mRNA, linking RNA regulation to the nitrogen fixation network. (lv2024integratedhfqinteractingrnaome pages 1-2)

---

## 3) Current applications and real-world implementations

### 3.1 Agricultural inoculants and microbiome manipulation
A 2024 rice pot experiment inoculating a nitrogen-fixing Herbaspirillum strain reports changes in soil nutrients and yield metrics:
- Rhizosphere nitrate nitrogen +**14.77%**, ammonium nitrogen +**27.83%**, available phosphorus +**22.67%** vs control. (li2024mechanismofmicrobial pages 1-2)
- Theoretical rice yield +**8.81%**, linked to +**10.24%** effective panicles and +**4.14%** seed setting rate. (li2024mechanismofmicrobial pages 1-2)

This is an application-level study: it supports edges from “inoculation with diazotroph” to “soil inorganic N pools” and “plant yield components,” but it does not directly prove nitrogenase-driven N2 fixation rates without isotopic assays. (li2024mechanismofmicrobial pages 1-2)

### 3.2 Synthetic biology and heterologous systems
- **E. coli heterologous nitrogenase**: engineered assembly yields measurable 15N incorporation and tunable ammonia release phenotypes (amtB deletion). (solomon2024ammoniasynthesisvia pages 9-10, solomon2024ammoniasynthesisvia pages 4-5)
- **Yeast mitochondria expression**: in vitro FeMo-co assembly using only yeast-produced components is a milestone toward transgenic nitrogen fixation, but remains pre-in vivo. (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11)

---

## 4) Expert opinions / analysis (authoritative synthesis)

- Nitrogenase is repeatedly described as uniquely capable of catalyzing N2 reduction and as **one of the most energy-intensive biochemical reactions**, requiring extensive physiological integration (ATP generation, low-potential electron supply, oxygen protection). (alleman2023mechanismsforgenerating pages 1-3)
- Engineering reviews stress that Mo-nitrogenase is often preferred as a scaffold due to higher activity relative to alternative nitrogenases, and that oxygen tolerance and proper stoichiometry/assembly are major constraints in heterologous contexts. (bennett2023engineeringnitrogenasesfor pages 1-2, dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2)
- A network view of nitrogen cycling cautions that microbes can be metabolically versatile (e.g., combining fixation with denitrification), so trait assignment should be grounded in mechanism/evidence rather than simple ecological labels. (kuypers2018themicrobialnitrogencycling pages 1-4)

---

## 5) Candidate nodes and causal edges for `nitrogen_fixation.yaml`

### 5.1 Candidate nodes (grouped) with grounding
| Node type | Label | Suggested ontology CURIE(s) | Key supporting citation IDs |
|---|---|---|---|
| Trait/process | nitrogen fixation | METPO:traitmech:000103; GO:0009399 | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Trait/process | diazotrophy |  | (alleman2023mechanismsforgenerating pages 1-3, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Trait/process | biological nitrogen fixation | GO:0009399 | (alleman2023mechanismsforgenerating pages 1-3, dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2) |
| Trait/process | dinitrogen reduction to ammonia |  | (alleman2023mechanismsforgenerating pages 1-3, dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2) |
| Trait/process | FeMo-co biosynthesis |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, solomon2024ammoniasynthesisvia pages 4-5) |
| Trait/process | electron transfer to nitrogenase | GO:1990123 | (alleman2023mechanismsforgenerating pages 1-3, bennett2023engineeringnitrogenasesfor pages 1-2) |
| Trait/process | nitrogenase-dependent acetylene reduction |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11, solomon2024ammoniasynthesisvia pages 7-9) |
| Enzymes/complexes | nitrogenase | EC:1.18.6.1 | (alleman2023mechanismsforgenerating pages 1-3, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Enzymes/complexes | Mo-dependent nitrogenase | EC:1.18.6.1 | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, bennett2023engineeringnitrogenasesfor pages 1-2) |
| Enzymes/complexes | NifH (Fe protein; dinitrogenase reductase) |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, bennett2023engineeringnitrogenasesfor pages 1-2) |
| Enzymes/complexes | NifDK (MoFe protein; dinitrogenase) |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, bennett2023engineeringnitrogenasesfor pages 1-2) |
| Enzymes/complexes | NifEN scaffold complex |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, liu2025heterologoussynthesisof pages 1-2) |
| Enzymes/complexes | Fe-only nitrogenase (AnfHDGK) |  | (bennett2023engineeringnitrogenasesfor pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Enzymes/complexes | V-dependent nitrogenase (VnfHDGK) |  | (bennett2023engineeringnitrogenasesfor pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Assembly factors | NifB |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, liu2025heterologoussynthesisof pages 1-2) |
| Assembly factors | NifE |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, solomon2024ammoniasynthesisvia pages 4-5) |
| Assembly factors | NifN |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, solomon2024ammoniasynthesisvia pages 4-5) |
| Assembly factors | NifS |  | (liu2025heterologoussynthesisof pages 1-2, solomon2024ammoniasynthesisvia pages 1-4) |
| Assembly factors | NifU |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, solomon2024ammoniasynthesisvia pages 1-4) |
| Assembly factors | NifV (homocitrate synthase) | EC:2.3.3.14 | (usman2024nitrogenfixationby pages 4-6, solomon2024ammoniasynthesisvia pages 4-5) |
| Assembly factors | NifM |  | (bennett2023engineeringnitrogenasesfor pages 1-2, lv2024integratedhfqinteractingrnaome pages 1-2) |
| Assembly factors | NifQ |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11, dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2) |
| Assembly factors | NifX |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11, dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2) |
| Assembly factors | NafY |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11) |
| Electron donors & redox partners | ferredoxin (Fd) |  | (alleman2023mechanismsforgenerating pages 1-3, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Electron donors & redox partners | flavodoxin (Fld) |  | (alleman2023mechanismsforgenerating pages 1-3, bennett2023engineeringnitrogenasesfor pages 1-2) |
| Electron donors & redox partners | FdxN |  | (usman2024nitrogenfixationby pages 4-6, solomon2024ammoniasynthesisvia pages 4-5) |
| Electron donors & redox partners | pyruvate:flavodoxin/ferredoxin oxidoreductase (NifJ/PFOR) | EC:1.2.7.1 | (usman2024nitrogenfixationby pages 4-6) |
| Electron donors & redox partners | FixABCX electron-bifurcating complex |  | (alleman2023mechanismsforgenerating pages 1-3, barron2024nitrogenfixinggammaproteobacteria pages 7-8) |
| Electron donors & redox partners | Rnf complex |  | (alleman2023mechanismsforgenerating pages 1-3, barron2024nitrogenfixinggammaproteobacteria pages 7-8) |
| Electron donors & redox partners | Fd:NAD(P)H oxidoreductase |  | (alleman2023mechanismsforgenerating pages 1-3) |
| Electron donors & redox partners | hydrogenase | EC:1.12.-.- | (alleman2023mechanismsforgenerating pages 1-3) |
| Electron donors & redox partners | photosystem I |  | (alleman2023mechanismsforgenerating pages 1-3) |
| Metalloclusters/cofactors | FeMo-cofactor (FeMo-co; M-cluster) |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, liu2025heterologoussynthesisof pages 1-2) |
| Metalloclusters/cofactors | P-cluster |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, alleman2023mechanismsforgenerating pages 1-3) |
| Metalloclusters/cofactors | NifB-co |  | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2) |
| Metalloclusters/cofactors | L-cluster |  | (liu2025heterologoussynthesisof pages 1-2, solomon2024ammoniasynthesisvia pages 4-5) |
| Metalloclusters/cofactors | K-cluster |  | (liu2025heterologoussynthesisof pages 1-2, solomon2024ammoniasynthesisvia pages 4-5) |
| Metalloclusters/cofactors | O-cluster |  | (liu2025heterologoussynthesisof pages 1-2, lee2024cofactormaturasenifen pages 1-2) |
| Metalloclusters/cofactors | [4Fe-4S] cluster | CHEBI:30413 | (alleman2023mechanismsforgenerating pages 1-3, dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2) |
| Small molecules/metabolites | dinitrogen (N2) | CHEBI:17997 | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Small molecules/metabolites | ammonia (NH3) | CHEBI:16134 | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Small molecules/metabolites | ammonium | CHEBI:28938 | (kuypers2018themicrobialnitrogencycling pages 1-4, solomon2024ammoniasynthesisvia pages 9-10) |
| Small molecules/metabolites | ATP | CHEBI:15422 | (alleman2023mechanismsforgenerating pages 1-3, bennett2023engineeringnitrogenasesfor pages 1-2) |
| Small molecules/metabolites | ADP | CHEBI:16761 | (alleman2023mechanismsforgenerating pages 1-3, barron2024nitrogenfixinggammaproteobacteria pages 7-8) |
| Small molecules/metabolites | inorganic phosphate | CHEBI:43474 | (alleman2023mechanismsforgenerating pages 1-3, bennett2023engineeringnitrogenasesfor pages 1-2) |
| Small molecules/metabolites | proton (H+) | CHEBI:15378 | (bennett2023engineeringnitrogenasesfor pages 1-2, alleman2023mechanismsforgenerating pages 1-3) |
| Small molecules/metabolites | dihydrogen (H2) | CHEBI:18276 | (bennett2023engineeringnitrogenasesfor pages 1-2, alleman2023mechanismsforgenerating pages 1-3) |
| Small molecules/metabolites | molybdenum | CHEBI:33363 | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Small molecules/metabolites | vanadium | CHEBI:33340 | (bennett2023engineeringnitrogenasesfor pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Small molecules/metabolites | iron | CHEBI:18248 | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Small molecules/metabolites | homocitrate | CHEBI:50347 | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, liu2025heterologoussynthesisof pages 1-2) |
| Small molecules/metabolites | FMN | CHEBI:17621 | (alleman2023mechanismsforgenerating pages 1-3) |
| Small molecules/metabolites | acetylene (C2H2) | CHEBI:25979 | (solomon2024ammoniasynthesisvia pages 7-9, dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11) |
| Small molecules/metabolites | ethylene (C2H4) | CHEBI:18153 | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11, perez2026nonnodulatingrhizobiumlikeaco34a pages 5-7) |
| Small molecules/metabolites | azide (N3−) | CHEBI:29128 | (liu2025heterologoussynthesisof pages 1-2) |
| Small molecules/metabolites | α-ketoglutarate / 2-oxoglutarate | CHEBI:16810 | (barron2024nitrogenfixinggammaproteobacteria pages 7-8) |
| Environmental factors | oxygen | CHEBI:15379; ENVO:01000324 | (alleman2023mechanismsforgenerating pages 1-3, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Environmental factors | microaerobic conditions | ENVO:01000741 | (alleman2023mechanismsforgenerating pages 13-14, perez2026nonnodulatingrhizobiumlikeaco34a pages 5-7) |
| Environmental factors | nitrogen limitation / low fixed nitrogen | ENVO:01000277 | (kuypers2018themicrobialnitrogencycling pages 1-4, barron2024nitrogenfixinggammaproteobacteria pages 7-8) |
| Environmental factors | ammonium excess / fixed nitrogen availability |  | (barron2024nitrogenfixinggammaproteobacteria pages 7-8, bennett2023engineeringnitrogenasesfor pages 1-2) |
| Environmental factors | molybdenum limitation |  | (bennett2023engineeringnitrogenasesfor pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Environmental factors | heterocyst spatial separation | GO:0009416 | (kuypers2018themicrobialnitrogencycling pages 1-4, barron2024nitrogenfixinggammaproteobacteria pages 1-2) |
| Environmental factors | enhanced respiration / respiratory protection |  | (kuypers2018themicrobialnitrogencycling pages 1-4, barron2024nitrogenfixinggammaproteobacteria pages 1-2) |
| Environmental factors | mitochondrial targeting for O2 protection | GO:0005739 | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11, dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2) |
| Experimental/assay readouts | nifH gene marker |  | (li2024mechanismofmicrobial pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4) |
| Experimental/assay readouts | acetylene reduction assay (ARA) |  | (perez2026nonnodulatingrhizobiumlikeaco34a pages 5-7, solomon2024ammoniasynthesisvia pages 7-9) |
| Experimental/assay readouts | 15N2 incorporation assay |  | (solomon2024ammoniasynthesisvia pages 9-10, solomon2024ammoniasynthesisvia pages 7-9) |
| Experimental/assay readouts | nanoSIMS |  | (solomon2024ammoniasynthesisvia pages 9-10, solomon2024ammoniasynthesisvia pages 7-9) |
| Experimental/assay readouts | diazotrophic growth on N2 / under N2 with limited NH4+ |  | (solomon2024ammoniasynthesisvia pages 9-10, solomon2024ammoniasynthesisvia pages 7-9) |
| Experimental/assay readouts | EPR detection of M-cluster/P-cluster occupancy |  | (solomon2024ammoniasynthesisvia pages 7-9, solomon2024ammoniasynthesisvia pages 4-5) |
| Experimental/assay readouts | extracellular 15NH4+ detection by NMR |  | (solomon2024ammoniasynthesisvia pages 9-10) |
| Regulatory proteins/complexes | NifA |  | (barron2024nitrogenfixinggammaproteobacteria pages 7-8, lv2024integratedhfqinteractingrnaome pages 1-2) |
| Regulatory proteins/complexes | NifL |  | (barron2024nitrogenfixinggammaproteobacteria pages 7-8, lv2024integratedhfqinteractingrnaome pages 1-2) |
| Regulatory proteins/complexes | NifLA regulatory system |  | (lv2024integratedhfqinteractingrnaome pages 1-2, usman2024nitrogenfixationby pages 10-12) |
| Regulatory proteins/complexes | RpoN / sigma-54 |  | (lv2024integratedhfqinteractingrnaome pages 1-2, bennett2023engineeringnitrogenasesfor pages 1-2) |
| Regulatory proteins/complexes | NtrB |  | (bennett2023engineeringnitrogenasesfor pages 1-2, lv2024integratedhfqinteractingrnaome pages 1-2) |
| Regulatory proteins/complexes | NtrC |  | (bennett2023engineeringnitrogenasesfor pages 1-2, lv2024integratedhfqinteractingrnaome pages 1-2) |
| Regulatory proteins/complexes | GlnB (PII protein) |  | (barron2024nitrogenfixinggammaproteobacteria pages 7-8, lv2024integratedhfqinteractingrnaome pages 1-2) |
| Regulatory proteins/complexes | GlnK (PII protein) |  | (barron2024nitrogenfixinggammaproteobacteria pages 7-8, lv2024integratedhfqinteractingrnaome pages 1-2) |
| Regulatory proteins/complexes | GlnD |  | (barron2024nitrogenfixinggammaproteobacteria pages 7-8) |
| Regulatory proteins/complexes | AmtB ammonium transporter |  | (lv2024integratedhfqinteractingrnaome pages 1-2, solomon2024ammoniasynthesisvia pages 9-10) |
| Regulatory proteins/complexes | Hfq |  | (lv2024integratedhfqinteractingrnaome pages 1-2) |
| Regulatory proteins/complexes | NifM |  | (lv2024integratedhfqinteractingrnaome pages 1-2, bennett2023engineeringnitrogenasesfor pages 1-2) |


*Table: This table lists candidate nodes for a microbial nitrogen-fixation causal graph, grouped by biological type and annotated with suggested ontology identifiers where available. It is useful for transferring evidence-backed entities into a TraitMech YAML curation workflow.*

### 5.2 Evidence-backed candidate edges (triples + snippets)
| Subject node | Predicate | Object node | Evidence snippet (short quote) | Citation IDs | Notes/uncertainty and taxon/assay specificity |
|---|---|---|---|---|---|
| ferredoxin (Fd) / flavodoxin (Fld) | transfers_electron_to | NifH | "Reduced electron carriers donate electrons to the [4Fe-4S] cluster at the interface of the NifH homodimer" | (bennett2023engineeringnitrogenasesfor pages 1-2, alleman2023mechanismsforgenerating pages 1-3) | Core Mo-nitrogenase mechanism; Fd/Fld donor identity varies by organism. |
| NifH | transfers_electron_to | P-cluster | "The Fe-protein contains 1 FeS cluster that accepts electrons from Fd or Fld and reduces the P-cluster in the MoFe protein in an ATP-dependent electron transfer" | (alleman2023mechanismsforgenerating pages 1-3, alleman2023mechanismsforgenerating media 6f3977b8) | Strong direct support from review figure/text. |
| P-cluster | transfers_electron_to | FeMo-cofactor (M-cluster) | "The P-cluster delivers electrons to the MoFe cofactor allowing electrons to be loaded for the reduction of N2" | (alleman2023mechanismsforgenerating pages 1-3, alleman2023mechanismsforgenerating media 6f3977b8) | Core electron relay. |
| FeMo-cofactor (M-cluster) | enables | N2 reduction to NH3 | "FeMo-co ... binds and reduces N2 to form NH3 and H2" | (bennett2023engineeringnitrogenasesfor pages 1-2) | For canonical Mo-dependent nitrogenase. |
| NifH | requires | ATP | "NifH transiently binds and then dissociates from the NifDK complex, hydrolyzing 2 molecules of Mg-ATP per electron transfer" | (bennett2023engineeringnitrogenasesfor pages 1-2) | Supports per-electron ATP cost. |
| nitrogen fixation | requires | 16 MgATP per N2 | "N2 + 8H+ + 8e- + 16MgATP ➔ 2NH3 + H2 + 16MgADP + 16Pi" | (bennett2023engineeringnitrogenasesfor pages 1-2) | Canonical stoichiometry for Mo nitrogenase. |
| nitrogen fixation | requires | 8 electrons per N2 | "N2 + 8H+ + 8e- + 16MgATP ➔ 2NH3 + H2 + 16MgADP + 16Pi" | (bennett2023engineeringnitrogenasesfor pages 1-2) | Canonical stoichiometry for Mo nitrogenase. |
| oxygen | inhibits | nitrogenase | "Nitrogenase is an O2-sensitive enzyme" | (alleman2023mechanismsforgenerating pages 1-3, dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2) | Broad, well-supported claim across diazotrophs. |
| oxygen exposure | deactivates | nitrogenase | "Because oxygen exposure deactivates nitrogenases" | (kuypers2018themicrobialnitrogencycling pages 1-4) | Foundational review; broad ecological generalization. |
| heterocysts | protects_from | oxygen inhibition of nitrogenase | "separate N2 fixation from photosynthesis, either spatially (for example in heterocysts" | (kuypers2018themicrobialnitrogencycling pages 1-4) | Cyanobacteria-specific protection strategy. |
| enhanced respiration | protects_from | oxygen inhibition of nitrogenase | "Even non-photosynthetic organisms living in oxic environments require mechanisms, such as enhanced oxygen respiration" | (kuypers2018themicrobialnitrogencycling pages 1-4) | Protection mechanism in aerobic diazotrophs; taxon-specific implementation. |
| mitochondrial targeting | protects_from | oxidative inactivation of Nif proteins / cofactors | "the oxygen sensitivity issue can be resolved by subcellular targeting" | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11) | Engineering/eukaryotic context; not native microbial physiology. |
| NifS/NifU | assembles | [Fe4S4] units/modules | "NifS/NifU mobilize Fe/S to form [Fe4S4] units" | (liu2025heterologoussynthesisof pages 1-2, solomon2024ammoniasynthesisvia pages 1-4) | Strong support from 2025/2024 engineering pathway summaries. |
| [Fe4S4] units/modules | assembles | K-cluster on NifB | "transfer of a pair of [Fe4S4] clusters to NifB ... transforms the [Fe4S4] cluster pair (termed K-cluster)" | (liu2025heterologoussynthesisof pages 1-2) | Biosynthesis pathway step. |
| NifB | assembles | L-cluster | "the K-cluster ... are coupled/rearranged into a [Fe8S9C] cluster (designated the L-cluster) via radical chemistry on NifB" | (solomon2024ammoniasynthesisvia pages 4-5) | Strong direct support. |
| L-cluster | transfers_to | NifEN | "the L-cluster is transferred to NifEN" | (solomon2024ammoniasynthesisvia pages 4-5) | Core FeMo-co assembly step. |
| NifEN | matures | FeMo-cofactor (M-cluster) | "NifEN matures the NifB cofactor producing the FeMo-cofactor" | (bennett2023engineeringnitrogenasesfor pages 1-2) | Figure/text level support; intermediate chemistry elaborated elsewhere. |
| NifH | assembles | FeMo-cofactor (M-cluster) | "NifH-mediated substitution of one terminal Fe of the L-cluster with Mo/homocitrate" | (solomon2024ammoniasynthesisvia pages 4-5) | Directly supports NifH role in late FeMo-co maturation. |
| molybdenum + homocitrate | enables | M-cluster maturation on NifEN | "converted into a mature M-cluster upon NifH-mediated substitution of one terminal Fe of the L-cluster with Mo/homocitrate" | (solomon2024ammoniasynthesisvia pages 4-5) | Specific to Mo-dependent nitrogenase. |
| M-cluster (FeMo-co) | transfers_to | apo-NifDK | "transfer of the M-cluster to its target binding site within the α-subunit of apo NifDK" | (solomon2024ammoniasynthesisvia pages 4-5) | Direct late assembly step. |
| apo-NifDK + M-cluster | causes | holo-NifDK | "resulting in a P- and M-cluster-replete, holo NifDK" | (solomon2024ammoniasynthesisvia pages 4-5) | Strong direct support. |
| NifL | inhibits | NifA | "NifL modulates NifA by binding/releasing it in response to oxygen, energy, and fixed-nitrogen cues" | (barron2024nitrogenfixinggammaproteobacteria pages 7-8) | Strong recent review support. |
| oxygen / oxidized PAS1-FAD state | promotes | NifL-NifA binding | "oxidation of PAS1 FAD ... promote[s] NifL–NifA binding" | (barron2024nitrogenfixinggammaproteobacteria pages 7-8) | Mechanistic oxygen-sensing edge in A. vinelandii review context. |
| low cellular energy / ADP | promotes | NifL inhibitory state | "binds ADP/ATP and has ~10-fold higher affinity for ADP, favoring the NifA-binding (inhibitory) state" | (barron2024nitrogenfixinggammaproteobacteria pages 7-8) | Regulatory edge from recent review; especially A. vinelandii. |
| deuridylylated GlnK (high fixed N) | promotes | NifL-NifA complex formation | "deuridylylated GlnK in high N binds NifL and promotes NifLA complex formation, repressing nif expression" | (barron2024nitrogenfixinggammaproteobacteria pages 7-8) | Strong recent regulatory support. |
| uridylylated GlnK (low N) | inhibits | NifL interaction | "uridylylation by GlnD ... prevents NifL interaction in low N" | (barron2024nitrogenfixinggammaproteobacteria pages 7-8) | Regulatory state edge; taxon/model review context. |
| sigma-54 (RpoN) | enables | nif gene transcription | "expression depends on the alternative sigma factor, σ54" | (bennett2023engineeringnitrogenasesfor pages 1-2, lv2024integratedhfqinteractingrnaome pages 1-2) | Broad proteobacterial regulation; not universal across all diazotrophs. |
| Hfq | binds | nifA mRNA | "Hfq directly interacts with the mRNA of regulatory proteins ... and NifA" | (lv2024integratedhfqinteractingrnaome pages 1-2) | Post-transcriptional regulation in Pseudomonas stutzeri A1501. |
| Hfq | binds | nifM mRNA | "Notable among these is nifM" | (lv2024integratedhfqinteractingrnaome pages 1-2) | Root-associated P. stutzeri A1501 specific. |
| Hfq | binds | amtB mRNA | "Notable among these is ... amtB" | (lv2024integratedhfqinteractingrnaome pages 1-2) | Root-associated P. stutzeri A1501 specific. |
| amtB deletion | causes | extracellular 15NH4+ accumulation | "deletion of amtB ... permitted accumulation of extracellular 15NH4+" | (solomon2024ammoniasynthesisvia pages 9-10) | Engineered E. coli Mo-nitrogenase context. |
| heterologous nitrogenase expression in E. coli | causes | 15N incorporation into biomass | "15N2-grown YM538EE showed an average 15N/14N of 3.1%±0.1%" | (solomon2024ammoniasynthesisvia pages 9-10, solomon2024ammoniasynthesisvia pages 1-4) | Strong engineering evidence for in vivo activity. |
| heterologous expression of nif components in E. coli | causes | active Mo-nitrogenase assembly | "we report the heterologous formation of an active Mo-nitrogenase ... in E. coli" | (solomon2024ammoniasynthesisvia pages 4-5, solomon2024ammoniasynthesisvia pages 1-4) | Engineering edge; host-specific. |
| yeast mitochondrial expression of NifB/NifEN/NifH | enables | in vitro FeMo-co biosynthesis | "the entire in vitro FeMo-co biosynthetic pathway can be recapitulated using only purified components produced in S. cerevisiae" | (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11, dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2) | Eukaryotic engineering context; in vitro, not full in vivo nitrogen fixation. |


*Table: This table lists candidate subject-predicate-object edges for a TraitMech nitrogen fixation graph, with concise evidence snippets and context-ID citations. It covers core catalysis, FeMo-co assembly, oxygen sensitivity and protection, regulation, and recent engineering demonstrations.*

---

## Warnings / curation cautions (do-not-curate-yet or mark uncertain)
1. **Marker-only inference**: nifH presence is strong evidence of genetic potential but **not proof of nitrogen fixation activity** without assay support (ARA/15N2/growth). (li2024mechanismofmicrobial pages 1-2, kuypers2018themicrobialnitrogencycling pages 1-4)
2. **Engineering vs native physiology**: mitochondria targeting and in vitro FeMo-co synthesis from yeast-derived proteins are engineering strategies; treat edges about these contexts as **engineering/experimental-factor nodes** rather than universal physiology. (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11, dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2)
3. **Taxon-specific protection/regulation**: heterocysts apply to cyanobacteria, respiratory protection is prominent in aerobes, and NifL/NifA details are best supported in Proteobacteria model systems; annotate these edges as potentially taxon-scoped. (kuypers2018themicrobialnitrogencycling pages 1-4, barron2024nitrogenfixinggammaproteobacteria pages 7-8)
4. **Partial assembly states**: engineered hosts frequently produce mixed holo/apo nitrogenase populations (e.g., P-cluster replete but M-cluster deficient), so edges that assume full functionality should specify maturation state. (solomon2024ammoniasynthesisvia pages 7-9)

---

## DOI-first bibliography (with URLs and publication dates when available)

1. Solomon JB, Lee CC, Liu YA, et al. **Ammonia synthesis via an engineered nitrogenase assembly pathway in Escherichia coli.** *Nature Catalysis*. Published Sep 2024. DOI: **10.1038/s41929-024-01229-x**. URL: https://doi.org/10.1038/s41929-024-01229-x (solomon2024ammoniasynthesisvia pages 4-5, solomon2024ammoniasynthesisvia pages 9-10)
2. Dobrzyńska K, Pérez-González A, Echavarri-Erasun C, et al. **Nitrogenase cofactor biosynthesis using proteins produced in mitochondria of Saccharomyces cerevisiae.** *mBio*. Published 21 Dec 2023 (issue Feb 2024). DOI: **10.1128/mbio.03088-23**. URL: https://doi.org/10.1128/mbio.03088-23 (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2, dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11)
3. Barron S, Mus F, Peters JW. **Nitrogen-Fixing Gamma Proteobacteria Azotobacter vinelandii—A Blueprint for Nitrogen-Fixing Plants?** *Microorganisms*. Published Oct 2024. DOI: **10.3390/microorganisms12102087**. URL: https://doi.org/10.3390/microorganisms12102087 (barron2024nitrogenfixinggammaproteobacteria pages 7-8)
4. Lv F, Zhan Y, Feng H, et al. **Integrated Hfq-interacting RNAome and transcriptomic analysis reveals complex regulatory networks of nitrogen fixation in root-associated Pseudomonas stutzeri A1501.** *mSphere*. Published Jun 2024. DOI: **10.1128/msphere.00762-23**. URL: https://doi.org/10.1128/msphere.00762-23 (lv2024integratedhfqinteractingrnaome pages 1-2)
5. Li P, Tian Y, Yang K, et al. **Mechanism of microbial action of the inoculated nitrogen-fixing bacterium for growth promotion and yield enhancement in rice (Oryza sativa L.).** *Advanced Biotechnology*. Published Sep 2024. DOI: **10.1007/s44307-024-00038-4**. URL: https://doi.org/10.1007/s44307-024-00038-4 (li2024mechanismofmicrobial pages 1-2)
6. Alleman AB, Peters JW. **Mechanisms for generating low potential electrons across the metabolic diversity of nitrogen-fixing bacteria.** *Applied and Environmental Microbiology*. Published 8 May 2023. DOI: **10.1128/aem.00378-23**. URL: https://doi.org/10.1128/aem.00378-23 (alleman2023mechanismsforgenerating pages 1-3, alleman2023mechanismsforgenerating media 6f3977b8)
7. Bennett EM, Murray JW, Isalan M. **Engineering Nitrogenases for Synthetic Nitrogen Fixation: From Pathway Engineering to Directed Evolution.** *Biodesign Research*. Published 7 Feb 2023. DOI: **10.34133/bdr.0005**. URL: https://doi.org/10.34133/bdr.0005 (bennett2023engineeringnitrogenasesfor pages 1-2)
8. Kuypers MMM, Marchant HK, Kartal B. **The microbial nitrogen-cycling network.** *Nature Reviews Microbiology*. Published Feb 2018. DOI: **10.1038/nrmicro.2018.9**. URL: https://doi.org/10.1038/nrmicro.2018.9 (kuypers2018themicrobialnitrogencycling pages 1-4)
9. Lee CC, Górecki K, Stang M, Ribbe MW, Hu Y. **Cofactor maturase NifEN: A prototype ancient nitrogenase?** *Science Advances*. Published 12 Jun 2024. DOI: **10.1126/sciadv.ado6169**. URL: https://doi.org/10.1126/sciadv.ado6169 (lee2024cofactormaturasenifen pages 1-2)

---

## Appendix: Figure (mechanism support)
Alleman & Peters (2023) Figure 1 provides a compact depiction of the nitrogenase electron-transfer chain **Fd/Fld → NifH → P-cluster → FeMo-co**, and the associated ATP dependence (2 ATP per electron transfer), suitable for mechanistic grounding in the causal graph. (alleman2023mechanismsforgenerating media 6f3977b8)

References

1. (dobrzynska2024nitrogenasecofactorbiosynthesis pages 1-2): Katarzyna Dobrzyńska, Ana Pérez-González, Carlos Echavarri-Erasun, Diana Coroian, Alvaro Salinero-Lanzarote, Marcel Veldhuizen, Dennis R. Dean, Stefan Burén, and Luis M. Rubio. Nitrogenase cofactor biosynthesis using proteins produced in mitochondria of <i>saccharomyces cerevisiae</i>. Feb 2024. URL: https://doi.org/10.1128/mbio.03088-23, doi:10.1128/mbio.03088-23. This article has 10 citations and is from a domain leading peer-reviewed journal.

2. (kuypers2018themicrobialnitrogencycling pages 1-4): Marcel M. M. Kuypers, Hannah K. Marchant, and Boran Kartal. The microbial nitrogen-cycling network. Nature Reviews Microbiology, 16:263-276, Feb 2018. URL: https://doi.org/10.1038/nrmicro.2018.9, doi:10.1038/nrmicro.2018.9. This article has 4784 citations and is from a highest quality peer-reviewed journal.

3. (bennett2023engineeringnitrogenasesfor pages 1-2): Emily M. Bennett, James W. Murray, and Mark Isalan. Engineering nitrogenases for synthetic nitrogen fixation: from pathway engineering to directed evolution. Biodesign Research, 5:0005, Jan 2023. URL: https://doi.org/10.34133/bdr.0005, doi:10.34133/bdr.0005. This article has 83 citations.

4. (perez2026nonnodulatingrhizobiumlikeaco34a pages 5-7): Luis Galdino García Pérez, Julio Cesar Martínez Romero, Marco A. Rogel, Gustavo Cuaxinque-Flores, María Gabriela Guerrero Ruiz, Marisa Rodríguez-Padilla, Lourdes Girard, Ronal Pacheco, Jesús Montiel González, Clara Ivette Rincón Molina, José David Flores-Félix, Reiner Rincón Rosales, and Esperanza Martínez-Romero. Non-nodulating rhizobium-like aco-34a fixes nitrogen in pure cultures and has a nif plasmid. Unknown journal, Feb 2026. URL: https://doi.org/10.21203/rs.3.rs-8833836/v1, doi:10.21203/rs.3.rs-8833836/v1.

5. (dobrzynska2024nitrogenasecofactorbiosynthesis pages 9-11): Katarzyna Dobrzyńska, Ana Pérez-González, Carlos Echavarri-Erasun, Diana Coroian, Alvaro Salinero-Lanzarote, Marcel Veldhuizen, Dennis R. Dean, Stefan Burén, and Luis M. Rubio. Nitrogenase cofactor biosynthesis using proteins produced in mitochondria of <i>saccharomyces cerevisiae</i>. Feb 2024. URL: https://doi.org/10.1128/mbio.03088-23, doi:10.1128/mbio.03088-23. This article has 10 citations and is from a domain leading peer-reviewed journal.

6. (solomon2024ammoniasynthesisvia pages 9-10): Joseph B. Solomon, Chi Chung Lee, Yiling A. Liu, Calder Duffin, Markus W. Ribbe, and Yilin Hu. Ammonia synthesis via an engineered nitrogenase assembly pathway in escherichia coli. Nature catalysis, 7 10:1130-1141, Sep 2024. URL: https://doi.org/10.1038/s41929-024-01229-x, doi:10.1038/s41929-024-01229-x. This article has 35 citations and is from a domain leading peer-reviewed journal.

7. (solomon2024ammoniasynthesisvia pages 7-9): Joseph B. Solomon, Chi Chung Lee, Yiling A. Liu, Calder Duffin, Markus W. Ribbe, and Yilin Hu. Ammonia synthesis via an engineered nitrogenase assembly pathway in escherichia coli. Nature catalysis, 7 10:1130-1141, Sep 2024. URL: https://doi.org/10.1038/s41929-024-01229-x, doi:10.1038/s41929-024-01229-x. This article has 35 citations and is from a domain leading peer-reviewed journal.

8. (li2024mechanismofmicrobial pages 1-2): Peng Li, Yunhe Tian, Kun Yang, Meijie Tian, Yi Zhu, Xinyu Chen, Ruiwen Hu, Tian Qin, Yongjun Liu, Shuguang Peng, Zhenxie Yi, Zhixuan Liu, He-jun Ao, and Juan Li. Mechanism of microbial action of the inoculated nitrogen-fixing bacterium for growth promotion and yield enhancement in rice (oryza sativa l.). Advanced Biotechnology, Sep 2024. URL: https://doi.org/10.1007/s44307-024-00038-4, doi:10.1007/s44307-024-00038-4. This article has 28 citations.

9. (alleman2023mechanismsforgenerating pages 1-3): Alexander B. Alleman and John W. Peters. Mechanisms for generating low potential electrons across the metabolic diversity of nitrogen-fixing bacteria. Applied and Environmental Microbiology, May 2023. URL: https://doi.org/10.1128/aem.00378-23, doi:10.1128/aem.00378-23. This article has 54 citations and is from a peer-reviewed journal.

10. (alleman2023mechanismsforgenerating media 6f3977b8): Alexander B. Alleman and John W. Peters. Mechanisms for generating low potential electrons across the metabolic diversity of nitrogen-fixing bacteria. Applied and Environmental Microbiology, May 2023. URL: https://doi.org/10.1128/aem.00378-23, doi:10.1128/aem.00378-23. This article has 54 citations and is from a peer-reviewed journal.

11. (solomon2024ammoniasynthesisvia pages 4-5): Joseph B. Solomon, Chi Chung Lee, Yiling A. Liu, Calder Duffin, Markus W. Ribbe, and Yilin Hu. Ammonia synthesis via an engineered nitrogenase assembly pathway in escherichia coli. Nature catalysis, 7 10:1130-1141, Sep 2024. URL: https://doi.org/10.1038/s41929-024-01229-x, doi:10.1038/s41929-024-01229-x. This article has 35 citations and is from a domain leading peer-reviewed journal.

12. (barron2024nitrogenfixinggammaproteobacteria pages 7-8): Sayre Barron, Florence Mus, and John W. Peters. Nitrogen-fixing gamma proteobacteria azotobacter vinelandii—a blueprint for nitrogen-fixing plants? Microorganisms, 12:2087, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102087, doi:10.3390/microorganisms12102087. This article has 12 citations.

13. (lv2024integratedhfqinteractingrnaome pages 1-2): Fanyang Lv, Yuhua Zhan, Haichao Feng, Wenyue Sun, Changyan Yin, Yueyue Han, Yahui Shao, Wei Xue, Shanshan Jiang, Yiyuan Ma, Haonan Hu, Jinfeng Wei, Yongliang Yan, and Min Lin. Integrated hfq-interacting rnaome and transcriptomic analysis reveals complex regulatory networks of nitrogen fixation in root-associated <i>pseudomonas stutzeri</i> a1501. Jun 2024. URL: https://doi.org/10.1128/msphere.00762-23, doi:10.1128/msphere.00762-23. This article has 5 citations and is from a peer-reviewed journal.

14. (liu2025heterologoussynthesisof pages 1-2): Yiling A. Liu, Chi Chung Lee, Kamil Górecki, Martin T. Stiebritz, Calder Duffin, Joseph B. Solomon, Markus W. Ribbe, and Yilin Hu. Heterologous synthesis of a simplified nitrogenase analog in escherichia coli. Science Advances, May 2025. URL: https://doi.org/10.1126/sciadv.adw6785, doi:10.1126/sciadv.adw6785. This article has 8 citations and is from a highest quality peer-reviewed journal.

15. (solomon2024ammoniasynthesisvia pages 1-4): Joseph B. Solomon, Chi Chung Lee, Yiling A. Liu, Calder Duffin, Markus W. Ribbe, and Yilin Hu. Ammonia synthesis via an engineered nitrogenase assembly pathway in escherichia coli. Nature catalysis, 7 10:1130-1141, Sep 2024. URL: https://doi.org/10.1038/s41929-024-01229-x, doi:10.1038/s41929-024-01229-x. This article has 35 citations and is from a domain leading peer-reviewed journal.

16. (usman2024nitrogenfixationby pages 4-6): Nazeef Idris Usman and Muazzam Muazu Wali. Nitrogen fixation by rhizobacterial nif mechanism: an advanced genetic perspective. Updates on Rhizobacteria, Jan 2024. URL: https://doi.org/10.5772/intechopen.1004087, doi:10.5772/intechopen.1004087. This article has 11 citations.

17. (lee2024cofactormaturasenifen pages 1-2): Chi Chung Lee, Kamil Górecki, Martin Stang, Markus W. Ribbe, and Yilin Hu. Cofactor maturase nifen: a prototype ancient nitrogenase? Science Advances, Jun 2024. URL: https://doi.org/10.1126/sciadv.ado6169, doi:10.1126/sciadv.ado6169. This article has 16 citations and is from a highest quality peer-reviewed journal.

18. (alleman2023mechanismsforgenerating pages 13-14): Alexander B. Alleman and John W. Peters. Mechanisms for generating low potential electrons across the metabolic diversity of nitrogen-fixing bacteria. Applied and Environmental Microbiology, May 2023. URL: https://doi.org/10.1128/aem.00378-23, doi:10.1128/aem.00378-23. This article has 54 citations and is from a peer-reviewed journal.

19. (barron2024nitrogenfixinggammaproteobacteria pages 1-2): Sayre Barron, Florence Mus, and John W. Peters. Nitrogen-fixing gamma proteobacteria azotobacter vinelandii—a blueprint for nitrogen-fixing plants? Microorganisms, 12:2087, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102087, doi:10.3390/microorganisms12102087. This article has 12 citations.

20. (usman2024nitrogenfixationby pages 10-12): Nazeef Idris Usman and Muazzam Muazu Wali. Nitrogen fixation by rhizobacterial nif mechanism: an advanced genetic perspective. Updates on Rhizobacteria, Jan 2024. URL: https://doi.org/10.5772/intechopen.1004087, doi:10.5772/intechopen.1004087. This article has 11 citations.