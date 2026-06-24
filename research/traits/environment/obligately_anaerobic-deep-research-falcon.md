---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:47:58.988591'
end_time: '2026-06-18T00:04:37.011940'
duration_seconds: 998.02
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: obligately anaerobic
  trait_identifier: METPO:1000607
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: obligately_anaerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference in which molecular oxygen (O\u2082) inhibits or\
    \ prevents growth."
  parent_traits: METPO:1000601
  synonyms: obligate anaerobe, obligate anaerobic
  evidence_summary: 'https://www.ncbi.nlm.nih.gov/books/NBK482349/: Oxygen is toxic
    to anaerobes (Supports oxygen inhibition/toxicity for obligately anaerobic organisms.)
    | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides
    fragilis is described as an obligate anaerobe.)'
  causal_graph_summary: 'obligate_anaerobe_oxygen_toxicity: 5 nodes, 4 edges'
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
- **Trait label:** obligately anaerobic
- **METPO identifier:** METPO:1000607
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which molecular oxygen (O₂) inhibits or prevents growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** obligate anaerobe, obligate anaerobic
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: Oxygen is toxic to anaerobes (Supports oxygen inhibition/toxicity for obligately anaerobic organisms.) | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides fragilis is described as an obligate anaerobe.)
- **Existing causal graph summary:** obligate_anaerobe_oxygen_toxicity: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **obligately anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_anaerobic.yaml`.

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
- **Trait label:** obligately anaerobic
- **METPO identifier:** METPO:1000607
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which molecular oxygen (O₂) inhibits or prevents growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** obligate anaerobe, obligate anaerobic
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: Oxygen is toxic to anaerobes (Supports oxygen inhibition/toxicity for obligately anaerobic organisms.) | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides fragilis is described as an obligate anaerobe.)
- **Existing causal graph summary:** obligate_anaerobe_oxygen_toxicity: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **obligately anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_anaerobic.yaml`.

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


# Research Report: Microbial Trait Causal Graph for **obligately anaerobic** (METPO:1000607)

## Scope summary (TraitMech curation view)

**Trait definition (curation-ready):** The defining property of obligate anaerobes is that **oxygen blocks their growth** (i.e., exposure to O2 at levels used in laboratory tests prevents growth), even though many organisms labeled obligate anaerobes can sometimes transiently tolerate low O2 and resume growth after returning to anoxia. (lu2021whenanaerobesencounter pages 1-3, lu2021whenanaerobesencounter pages 3-4)

**Trait boundaries and boundary cases:** Oxygen sensitivity is **graded rather than binary**. Some taxa classified as anaerobes harbor O2-consuming systems (e.g., cytochrome bd, rubredoxin:oxygen oxidoreductase) and may survive or even grow better at *low* O2, but typically fail to thrive at air-equilibrated O2 because O2 inactivates a limited set of key anaerobic enzymes. (lu2021whenanaerobesencounter pages 4-6, lu2021whenanaerobesencounter pages 3-4, lu2021whenanaerobesencounter pages 22-27)

**Operational phenotyping:** The trait is most cleanly measured as **growth/no-growth (or severe growth impairment) under defined O2 tensions** relative to anoxic controls, plus survival/CFU after timed O2 exposures. In *Clostridioides difficile* (an obligate anaerobe), tolerance was assayed across 0.1–4% O2 and short exposures to air (21% O2), and gene-specific phenotypes depend strongly on the O2 tension. (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 5-7)

## Key concepts and current mechanistic understanding

### 1) Why oxygen inhibits obligate anaerobes: targets and damage cascades

Mechanistically, obligate anaerobiosis is increasingly understood less as “missing antioxidant enzymes” and more as **chemical incompatibility between O2 and core anaerobic metabolism** (low-potential electron flow; radical enzymes; metal-centered catalysis). (lu2021whenanaerobesencounter pages 13-15, lu2021whenanaerobesencounter pages 4-6)

**Primary causal motif:**
- **O2 exposure → ROS formation → oxidation of metal centers and macromolecular damage**. Oxygenation causes endogenous formation of ROS (superoxide, peroxides, hydroxyl radical) and oxidative stress with damage to proteins and nucleic acids. (dyksma2024growthofsulfatereducing pages 1-2)

**Central vulnerable enzyme classes (examples):**
- **Glycyl-radical enzymes:** Pyruvate formate-lyase (PFL) is a canonical target; even low O2 can inactivate PFL rapidly, creating a metabolic block sufficient to “prohibit growth” (growth arrest without immediate lethality). (lu2021whenanaerobesencounter pages 4-6, lu2021whenanaerobesencounter pages 22-27)
- **Low-potential metalloenzymes:** O2 directly inactivates enzymes such as pyruvate:ferredoxin oxidoreductase (PFOR) and hydrogenases; these blocks can arrest growth until repaired under anoxia. (lu2021whenanaerobesencounter pages 22-27)
- **Fe–S cluster enzymes:** Superoxide can oxidize Fe–S clusters and mononuclear iron centers, yielding inactive enzymes; downstream H2O2 and Fenton chemistry can generate hydroxyl radicals that damage DNA. (bystrom2024couplingbutyrylcoenzymea pages 17-21, lu2021whenanaerobesencounter pages 11-13)

### 2) Oxygen tolerance in obligate anaerobes: detoxification, O2 scavenging, and repair

Contrary to older assumptions, anaerobes can “wield most of the same defences that aerobes possess” and activate peroxide stress responses upon aeration; however, the degree and deployment differs across taxa and conditions. (lu2021whenanaerobesencounter pages 1-3, lu2021whenanaerobesencounter pages 11-13)

Key defense categories that are directly useful for graph nodes/edges:

**(A) O2-reducing / O2-consuming enzymes (oxygen scavenging):**
- In *C. difficile*, four O2-reducing enzymes provide **tension-partitioned protection**: two flavodiiron proteins (FdpA, FdpF) and two reverse rubrerythrins (revRbr1, revRbr2), all with in vitro O2-reductase activity. Mutant phenotypes show that each enzyme dominates in a different O2 window (e.g., revRbr2 at <0.4%; FdpA at 0.4–1%; revRbr1 across 0.1–4%; FdpF at >4% and air). (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5)
- In sulfate-reducing bacteria (SRB), oxygen consumption defenses include cytoplasmic **rubredoxin:oxygen oxidoreductase (Roo/NorV)** and membrane-bound oxidases including **bd-type oxidase (CydAB)**, which is described as widely distributed and important in oxygen consumption as a defense. (dyksma2024growthofsulfatereducing pages 1-2)

**(B) ROS detoxification enzymes:**
- SRB oxygen-defense repertoires include catalase-peroxidase (KatG), alkyl hydroperoxide reductase (Ahp), and rubrerythrin/revRbr-type enzymes. (dyksma2024growthofsulfatereducing pages 1-2)

**(C) Repair of oxidized proteins / recovery:**
- Oxidative damage repair is highlighted as crucial; examples include **TrxA/TrxB** and **MsrA** for repair of oxidized proteins. (dyksma2024growthofsulfatereducing pages 1-2)

## Recent developments and latest research (emphasis 2023–2024)

### 1) 2024: Quantitative, multi-enzyme O2-scavenging architecture in an obligate anaerobic pathogen

Caulat et al. (mBio, Oct 2024) provide a recent, mechanistically detailed example of how an obligate anaerobe can exhibit **stratified O2 tolerance** via multiple O2-reductases with **overlapping activity spectra** and complex regulation, enabling survival in physiological gut O2 gradients and transient air exposure. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5)

Notable quantitative details for curation:
- Growth/survival assays across **0.1–4% O2**, plus **air exposure (21% O2)** and defined timings (e.g., 24–48 h at 1% O2; 24 h at 4% O2; hours in air) (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 5-7)
- Evidence that specific O2-defense genes are regulated by **σB**, **σA**, **Rex**, and the oxygen-sensing repressor **OseR** (repression in anaerobiosis, relief upon O2 exposure). (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 15-17)

### 2) 2024: In situ-relevant oxygen stress regimes for “strict anaerobes” in ecosystems

Dyksma & Pester (Microbiome, Oct 2024) used a peat-soil bioreactor cycled between oxic (1 week) and anoxic (4 weeks) phases for >200 days, showing that SRB populations established growth despite periodic O2 exposures of **133 µM O2 (50% air saturation)** and reached **up to 2.9% relative abundance**. This is valuable for curating **environmental exposure nodes** and indicating that “strict anaerobe” labels can mask community-level oxygen buffering and adaptive expression programs. (dyksma2024growthofsulfatereducing pages 1-2)

## Current applications and real-world implementations

### A) Cultivation/assay infrastructure for obligate anaerobes (clinical and research labs)

Practical implementation hinges on preventing oxygen intrusion and verifying low redox potential.

- For *Bacteroides thetaiotaomicron* (anaerobic gut symbiont), “they do not grow significantly in the presence of molecular oxygen,” so it is essential to remove oxygen from culture media; common infrastructure includes an anaerobic glove box, GasPak sealed canisters, and Hungate tubes; resazurin is used as a redox indicator and L-cysteine as a reducing agent. (silva2024methodsforcultivation pages 1-3)
- Anaerobic glovebox operation can include repeated flush/evacuation cycles and a palladium catalyst with H2 to remove residual O2, achieving very low O2 (reported as <2 ppm in one protocol context). (silva2024methodsforcultivation pages 3-5)

### B) High-throughput anaerobic screening (2024 protocol-level implementation)

Müller et al. (Nature Protocols, Dec 2024) describe chamber-integrated automation (plate stacker + plate reader, small liquid-handling robot) for **high-throughput anaerobic screening** of gut anaerobes in monocultures/communities, highlighting the practical constraints of chamber space and the need for temperature stability and pre-reduced consumables. (muller2024highthroughputanaerobicscreening pages 2-4, muller2024highthroughputanaerobicscreening pages 15-18)

### C) Anaerobic digestion and micro-aeration: oxygen as an engineered control knob and inhibitor

- Morais et al. (Applied Microbiology and Biotechnology, Feb 2024) quantified inhibition of methanogenic activity under headspace micro-aeration. At **0.5% O2**, methane production rate (MPR) from acetate or H2/CO2 was inhibited **~30–40%**, and at **5% O2** inhibition was **close to 100%** (near-complete). (morais2024effectofmicroaeration pages 1-2)
- A 2024 review (Li et al., Methane) summarizes microaeration as an emerging strategy, while emphasizing that oxygen inhibits methanogens (obligate anaerobes) and giving typical dosing ranges (e.g., 0.005–5 L O2 per Lreactor per day). (li2024acomprehensivereview pages 11-13, li2024acomprehensivereview pages 1-2)

## Candidate nodes grouped by type (for YAML curation)

| Node label | Node type | Suggested ontology grounding | Notes (brief) |
|---|---|---|---|
| molecular oxygen (O2) | environmental factor | CHEBI:15379 | Defining inhibitory factor for obligate anaerobiosis; experimental O2 ranges include 0.1–4%, air/21%, and dissolved 133 µM in recent studies (lu2021whenanaerobesencounter pages 1-3, caulat2024physiologicalroleand pages 2-5, dyksma2024growthofsulfatereducing pages 1-2, morais2024effectofmicroaeration pages 1-2) |
| superoxide | metabolite-chemical | CHEBI:18421 | ROS formed during O2 exposure; implicated in damage to metal centers and anaerobic enzymes (bystrom2024couplingbutyrylcoenzymea pages 17-21, dyksma2024growthofsulfatereducing pages 1-2) |
| hydrogen peroxide | metabolite-chemical | CHEBI:16240 | ROS and substrate for peroxidase defenses; activates stress responses in anaerobes (lu2021whenanaerobesencounter pages 11-13, caulat2024physiologicalroleand pages 1-2) |
| hydroxyl radical | metabolite-chemical | CHEBI:16243 | Highly damaging ROS produced via Fenton chemistry (bystrom2024couplingbutyrylcoenzymea pages 17-21, dyksma2024growthofsulfatereducing pages 1-2) |
| Fenton reaction | process | GO:0055114 | Chemical process linking Fe(II) and H2O2 to hydroxyl-radical generation and macromolecular damage; label-level grounding only (bystrom2024couplingbutyrylcoenzymea pages 17-21, lu2021whenanaerobesencounter pages 11-13) |
| oxygen exposure | process | GO:0070482 | Broad stress condition causing growth arrest or inhibition in obligate anaerobes (lu2021whenanaerobesencounter pages 1-3, dyksma2024growthofsulfatereducing pages 1-2) |
| reactive oxygen species detoxification | process | GO:0006801 | Defense program induced/transcribed during oxic phases in anaerobes (dyksma2024growthofsulfatereducing pages 1-2) |
| repair of oxidized proteins | process | GO:0030091 | Important secondary defense module after oxidative damage (dyksma2024growthofsulfatereducing pages 1-2) |
| oxygen consumption / oxygen reduction defense | process | GO:0016491 | Defensive O2 reduction by dedicated enzymes can support transient tolerance (dyksma2024growthofsulfatereducing pages 1-2, caulat2024physiologicalroleand pages 1-2) |
| Fe-S cluster | metabolite-chemical | label-only | Oxygen-sensitive cofactor/target damaged by ROS and O2 in anaerobic enzymes (bystrom2024couplingbutyrylcoenzymea pages 17-21, lu2021whenanaerobesencounter pages 13-15) |
| pyruvate formate-lyase (PFL) | gene-protein-complex | label-only | Glycyl-radical enzyme rapidly inactivated by O2; central example of fragile anaerobic metabolism (lu2021whenanaerobesencounter pages 4-6, lu2021whenanaerobesencounter pages 22-27) |
| pyruvate:ferredoxin oxidoreductase (PFOR) | gene-protein-complex | label-only | O2-sensitive anaerobic enzyme cited as a key target of oxygen poisoning (lu2021whenanaerobesencounter pages 22-27) |
| [FeFe]-hydrogenase | gene-protein-complex | label-only | Oxygen-sensitive hydrogenase representative of low-potential anaerobic redox enzymes (lu2021whenanaerobesencounter pages 22-27) |
| flavodiiron protein FdpA | gene-protein-complex | label-only | C. difficile O2-reductase active mainly at low/intermediate O2; contributes to survival around 0.4–1% O2 (caulat2024physiologicalroleand pages 2-5) |
| flavodiiron protein FdpF | gene-protein-complex | label-only | Class F O2-reductase receiving electrons directly from NADH; important at >4% O2 and air (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 5-7) |
| reverse rubrerythrin revRbr1 | gene-protein-complex | label-only | Major contributor to C. difficile tolerance at 1% O2 and active across wider low-O2 range (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 5-7) |
| reverse rubrerythrin revRbr2 | gene-protein-complex | label-only | Supports very low O2 tolerance, especially <0.4% O2 (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 15-17) |
| rubredoxin:oxygen oxidoreductase / Roo / NorV | gene-protein-complex | label-only | Cytoplasmic O2-reducing defense enzyme reported in anaerobes and SRB (dyksma2024growthofsulfatereducing pages 1-2, lu2021whenanaerobesencounter pages 3-4) |
| cytochrome bd-type oxidase / CydAB | gene-protein-complex | label-only | Membrane O2-consuming defense enzyme widely distributed in SRB and anaerobes (dyksma2024growthofsulfatereducing pages 1-2) |
| catalase-peroxidase / KatG | gene-protein-complex | label-only | ROS-detoxifying enzyme in oxygen defense repertoires of anaerobes/SRB (dyksma2024growthofsulfatereducing pages 1-2) |
| alkyl hydroperoxide reductase / Ahp | gene-protein-complex | label-only | Peroxide detoxification enzyme induced/used during oxygen stress (dyksma2024growthofsulfatereducing pages 1-2, lu2021whenanaerobesencounter pages 11-13) |
| thioredoxin / TrxA | gene-protein-complex | label-only | Protein redox repair component for oxidized proteins (dyksma2024growthofsulfatereducing pages 1-2) |
| thioredoxin reductase / TrxB | gene-protein-complex | label-only | Works with thioredoxin in redox maintenance/repair after oxidative stress (dyksma2024growthofsulfatereducing pages 1-2) |
| methionine sulfoxide reductase / MsrA | gene-protein-complex | label-only | Repairs oxidized methionine residues in proteins (dyksma2024growthofsulfatereducing pages 1-2) |
| general stress sigma factor σB | gene-protein-complex | label-only | Controls C. difficile O2-reductase genes and broader oxygen-stress response (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 15-17) |
| housekeeping sigma factor σA | gene-protein-complex | label-only | Provides basal transcription for some O2-defense genes such as fdpA/revrbr2 (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 15-17) |
| Rex regulator | gene-protein-complex | label-only | NADH/NAD+ sensing regulator linked to fdpF control and redox-dependent oxygen defense (caulat2024physiologicalroleand pages 15-17, dyksma2024growthofsulfatereducing pages 5-6) |
| OseR regulator | gene-protein-complex | label-only | Oxygen-sensing repressor of C. difficile O2-reductase genes under anaerobiosis (caulat2024physiologicalroleand pages 15-17) |
| Spx-family regulator | gene-protein-complex | label-only | Induces fdp/revrbr genes upon O2 exposure in C. difficile (caulat2024physiologicalroleand pages 1-2) |
| O2-reductase module (Fdp/revRbr system) | pathway-module | label-only | Multi-enzyme oxygen-scavenging module covering overlapping O2 ranges in obligate anaerobe tolerance (caulat2024physiologicalroleand pages 1-2) |
| ROS detoxification module | pathway-module | label-only | Includes KatG, Ahp, rubrerythrins and related enzymes (dyksma2024growthofsulfatereducing pages 1-2, lu2021whenanaerobesencounter pages 11-13) |
| protein repair module | pathway-module | label-only | Includes TrxA/TrxB, MsrA, chaperones; supports recovery after O2 stress (dyksma2024growthofsulfatereducing pages 1-2, lu2021whenanaerobesencounter pages 13-15) |
| anaerobic energy metabolism with radical/metallocofactor enzymes | pathway-module | label-only | Core metabolic architecture that is intrinsically O2-labile in obligate anaerobes (lu2021whenanaerobesencounter pages 13-15, lu2021whenanaerobesencounter pages 4-6) |
| resazurin | assay-factor | CHEBI:50373 | Redox indicator used to verify anaerobic conditions in media/cultures (silva2024methodsforcultivation pages 1-3, silva2024methodsforcultivation pages 5-6) |
| L-cysteine | assay-factor | CHEBI:17561 | Reducing agent added to lower redox potential in anaerobic media (silva2024methodsforcultivation pages 1-3, silva2024methodsforcultivation pages 5-6) |
| anaerobic glove box | assay-factor | label-only | Core cultivation infrastructure for oxygen-free handling of obligate anaerobes (silva2024methodsforcultivation pages 1-3, silva2024methodsforcultivation pages 3-5, muller2024highthroughputanaerobicscreening pages 2-4) |
| GasPak system | assay-factor | label-only | Sealed canister/jar method generating H2/CO2 for O2 removal with catalyst (silva2024methodsforcultivation pages 1-3, silva2024methodsforcultivation pages 5-6) |
| Hungate tubes | assay-factor | label-only | Sealed glass vessels for anaerobic culture and transfers (silva2024methodsforcultivation pages 1-3, silva2024methodsforcultivation pages 3-5) |
| headspace O2 percent | assay-factor | label-only | Quantitative assay variable in micro-aeration and tolerance tests; e.g., 0%, 0.5%, 1%, 2.5%, 5%, 21% air (morais2024effectofmicroaeration pages 1-2, morais2024effectofmicroaeration pages 2-4, caulat2024physiologicalroleand pages 15-17) |
| dissolved O2 (µM) | assay-factor | label-only | Quantitative assay/environment variable; e.g., 133 µM equals 50% air saturation in SRB bioreactor study (dyksma2024growthofsulfatereducing pages 1-2, dyksma2024growthofsulfatereducing pages 5-6) |


*Table: This table inventories candidate causal-graph nodes relevant to the trait 'obligately anaerobic,' grouped by node type and grounded where possible. It is useful for translating literature-supported mechanisms, defense systems, and assay variables into TraitMech curation targets.*

## Candidate evidence-backed causal edges (triples)

| Edge (S–P–O) | Predicate type | Evidence snippet (short quote) | Source (first author year, journal) | Identifier (DOI or URL) | Notes/curation confidence | Ontology grounding hints |
|---|---|---|---|---|---|---|
| molecular oxygen (O2) → inhibits → growth of obligate anaerobes | inhibits | “The defining trait of obligate anaerobes is that oxygen blocks their growth.” (lu2021whenanaerobesencounter pages 1-3) | Lu 2021, Nature Reviews Microbiology | https://doi.org/10.1038/s41579-021-00583-y | High; core trait-defining edge | CHEBI:15379 → METPO:1000607 |
| oxygenation/O2 exposure → causes → reactive oxygen species (ROS) formation | causes | “As a consequence of oxygenation, reactive oxygen species like superoxide, peroxides, and hydroxyl radicals are produced” (dyksma2024growthofsulfatereducing pages 1-2) | Dyksma 2024, Microbiome | https://doi.org/10.1186/s40168-024-01909-7 | High; general mechanism across anaerobes | GO:0070482, CHEBI:26523 |
| O2 exposure → causes → oxidative damage to biomolecules | causes | “ROS cause oxidative stress due to damage to biomolecules like proteins and nucleic acids” (dyksma2024growthofsulfatereducing pages 1-2) | Dyksma 2024, Microbiome | https://doi.org/10.1186/s40168-024-01909-7 | High | GO:0006979 |
| superoxide → damages/inactivates → Fe-S cluster enzymes | causes | “can react with iron-sulfur clusters and mononuclear iron centers… yielding inactive enzyme” (bystrom2024couplingbutyrylcoenzymea pages 17-21) | Bystrom 2024, Text | https://doi.org/10.14288/1.0447284 | Medium; mechanistically strong but source is thesis text | CHEBI:18421; Fe-S cluster label-only |
| H2O2 + Fe(II) → causes → hydroxyl radical formation | causes | “Fe(II)+H2O2 produces hydroxyl radicals” (lu2021whenanaerobesencounter pages 11-13) | Lu 2021, Nature Reviews Microbiology | https://doi.org/10.1038/s41579-021-00583-y | High | CHEBI:16240 + Fe(II) label-only + CHEBI:16243 |
| hydroxyl radical → causes → DNA damage | causes | “hydroxyl radicals… create irreparable lesions and block replication” (lu2021whenanaerobesencounter pages 11-13) | Lu 2021, Nature Reviews Microbiology | https://doi.org/10.1038/s41579-021-00583-y | High | CHEBI:16243; GO:0006974 |
| molecular oxygen (O2) → inactivates → pyruvate formate-lyase (PFL) | inhibits | “PFL is rapidly inactivated by O2” and “even low O2 levels can inactivate PFL within seconds” (lu2021whenanaerobesencounter pages 4-6) | Lu 2021, Nature Reviews Microbiology | https://doi.org/10.1038/s41579-021-00583-y | High | PFL label-only |
| molecular oxygen (O2) → inactivates → pyruvate:ferredoxin oxidoreductase (PFOR) | inhibits | “O2 directly inactivates diverse metalloenzymes… (e.g., PFOR… )” (lu2021whenanaerobesencounter pages 22-27) | Lu 2021, Nature Reviews Microbiology | https://doi.org/10.1038/s41579-021-00583-y | High | PFOR label-only |
| molecular oxygen (O2) → inactivates → [FeFe]-hydrogenases | inhibits | “O2 directly inactivates diverse metalloenzymes… hydrogenases” (lu2021whenanaerobesencounter pages 22-27) | Lu 2021, Nature Reviews Microbiology | https://doi.org/10.1038/s41579-021-00583-y | High | [FeFe]-hydrogenase label-only |
| FdpA → increases → tolerance to 0.4–1% O2 in C. difficile | increases | “fdpA mutant has a reduced growth at 0.4% O2” and shows “almost complete loss of survival… after 48 h of exposure to 1% O2” (caulat2024physiologicalroleand pages 2-5) | Caulat 2024, mBio | https://doi.org/10.1128/mbio.01591-24 | High; taxon-specific | FdpA label-only; NCBITaxon:C. difficile label-only |
| revRbr1 → increases → tolerance to ~1% O2 in C. difficile | increases | “revRbr1 seems to play a more important role in the tolerance to 1% O2” (caulat2024physiologicalroleand pages 2-5) | Caulat 2024, mBio | https://doi.org/10.1128/mbio.01591-24 | High; taxon-specific | revRbr1 label-only |
| revRbr2 → increases → tolerance to <0.4% O2 in C. difficile | increases | “revRbr2 (<0.4%)” and double revrbr mutant is “almost unable to grow at 0.1 or 0.4% O2” (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5) | Caulat 2024, mBio | https://doi.org/10.1128/mbio.01591-24 | High; taxon-specific | revRbr2 label-only |
| FdpF → increases → tolerance to >4% O2 and air in C. difficile | increases | “FdpF is more specific to tensions > 4% and air” and “FdpF is reported as the main O2-reductase for air (21%)” (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 5-7) | Caulat 2024, mBio | https://doi.org/10.1128/mbio.01591-24 | High; taxon-specific | FdpF label-only |
| O2-reductase activity (Fdp/revRbr module) → increases → O2 tolerance across overlapping O2 ranges | increases | “the four O2-reductases have different yet overlapping spectra of activity” (caulat2024physiologicalroleand pages 2-5) | Caulat 2024, mBio | https://doi.org/10.1128/mbio.01591-24 | High; useful module-level edge | pathway-module label-only |
| σB → regulates → fdpA/fdpF/revRbr1/revRbr2 expression | regulates | “the genes encoding the four O2-reductases are controlled by the alternative sigma factor σB” (caulat2024physiologicalroleand pages 2-5) | Caulat 2024, mBio | https://doi.org/10.1128/mbio.01591-24 | High | σB label-only |
| σA → regulates → basal transcription of fdpA and revrbr2 | regulates | “revrbr2 and fdpA are also transcribed by σA” (caulat2024physiologicalroleand pages 2-5) | Caulat 2024, mBio | https://doi.org/10.1128/mbio.01591-24 | High; taxon-specific | σA label-only |
| OseR → represses → O2-reductase genes in anaerobiosis | represses | “All four O2-reductase genes are repressed in anaerobiosis by OseR” (caulat2024physiologicalroleand pages 15-17) | Caulat 2024, mBio | https://doi.org/10.1128/mbio.01591-24 | High | OseR label-only |
| O2 exposure → relieves repression by → OseR | induces | “repression released upon O2 exposure” (caulat2024physiologicalroleand pages 15-17) | Caulat 2024, mBio | https://doi.org/10.1128/mbio.01591-24 | High | O2 CHEBI:15379; OseR label-only |
| Rex → regulates → fdpF | regulates | “fdpF is additionally regulated by Rex” (caulat2024physiologicalroleand pages 15-17) | Caulat 2024, mBio | https://doi.org/10.1128/mbio.01591-24 | High | Rex label-only |
| Spx-family regulator → induces → fdp and revrbr genes upon O2 exposure | induces | “an Spx-family regulator induces fdp and revrbr genes upon O2 exposure” (caulat2024physiologicalroleand pages 1-2) | Caulat 2024, mBio | https://doi.org/10.1128/mbio.01591-24 | Medium; regulator name unresolved here | Spx-family regulator label-only |
| Roo/NorV → increases → oxygen defense in SRB/anaerobes | increases | “Oxygen reduction can be facilitated in the cytoplasm by the bifunctional rubredoxin:oxygen oxidoreductase/nitric oxide reductase (Roo/NorV)” (dyksma2024growthofsulfatereducing pages 1-2) | Dyksma 2024, Microbiome | https://doi.org/10.1186/s40168-024-01909-7 | High | Roo/NorV label-only |
| CydAB (bd-type oxidase) → increases → oxygen consumption defense | increases | “bd-type oxidase (CydAB)… known to play an important role in oxygen consumption as a defense mechanism” (dyksma2024growthofsulfatereducing pages 1-2) | Dyksma 2024, Microbiome | https://doi.org/10.1186/s40168-024-01909-7 | High | CydAB label-only |
| KatG/Ahp/rubrerythrin → detoxify → ROS/peroxides | decreases | “ROS-detoxifying enzymes (catalase-peroxidase KatG, alkyl hydroperoxide reductase Ahp, and rubrerythrin/revRbr)” (dyksma2024growthofsulfatereducing pages 1-2) | Dyksma 2024, Microbiome | https://doi.org/10.1186/s40168-024-01909-7 | High; module-level edge may be split in curation | KatG, Ahp, rubrerythrin label-only |
| TrxA/TrxB/MsrA → repair → oxidized proteins | required_for | “Thioredoxin (TrxA) and thioredoxin reductase (TrxB)… together with… MsrA is also key for the repair of oxidized proteins” (dyksma2024growthofsulfatereducing pages 1-2) | Dyksma 2024, Microbiome | https://doi.org/10.1186/s40168-024-01909-7 | High | TrxA, TrxB, MsrA label-only |
| oxygen removal from culture media → required_for → cultivation of B. thetaiotaomicron | required_for | “it is essential to supply it with heme and remove oxygen from the culture media” (silva2024methodsforcultivation pages 1-3) | Silva 2024, Methods in Molecular Biology | https://doi.org/10.1007/978-1-0716-4043-2_7 | High; cultivation/assay edge | assay-factor |
| anaerobic glove box / GasPak / sealed vessels → required_for → anaerobic cultivation | required_for | “Equipment for anaerobically cultivating this species include anaerobic glove box… GasPak™ sealed canisters… Hungate tubes” (silva2024methodsforcultivation pages 1-3) | Silva 2024, Methods in Molecular Biology | https://doi.org/10.1007/978-1-0716-4043-2_7 | High; assay-specific | glove box, GasPak, Hungate tube label-only |
| resazurin → indicates → anaerobic/redox status of media | indicates | “resazurin is recommended as a non-toxic redox indicator” (silva2024methodsforcultivation pages 5-6) | Silva 2024, Methods in Molecular Biology | https://doi.org/10.1007/978-1-0716-4043-2_7 | High; assay-specific | CHEBI:50373 |
| micro-aeration at 0.5% O2 → inhibits → methane production rate by ~30–40% | inhibits | “at 0.5% O2 methane production rate (MPR) was inhibited by ~30–40%” (morais2024effectofmicroaeration pages 1-2) | Morais 2024, Applied Microbiology and Biotechnology | https://doi.org/10.1007/s00253-023-12969-4 | High; process-level application evidence | headspace O2 assay variable |
| micro-aeration at 5% O2 → strongly inhibits → methane production rate (~100%) | inhibits | “close to 100% at 5% O2” (morais2024effectofmicroaeration pages 1-2) | Morais 2024, Applied Microbiology and Biotechnology | https://doi.org/10.1007/s00253-023-12969-4 | High | headspace O2 assay variable |
| periodic exposure to 133 µM O2 (50% air saturation) → permits growth of → peatland SRB populations | permits | “growing populations… despite weekly periods of oxygen exposures at 133 µM (50% air saturation)” (dyksma2024growthofsulfatereducing pages 1-2) | Dyksma 2024, Microbiome | https://doi.org/10.1186/s40168-024-01909-7 | Medium; community/bioreactor context rather than pure culture trait | dissolved O2 assay variable; SRB community |
| persistent transcription of oxygen-defense genes under anoxic conditions → increases → periodic O2 stress tolerance in SRB | increases | “maintained high transcript levels of genes encoding oxygen defense proteins even under anoxic conditions” (dyksma2024growthofsulfatereducing pages 1-2) | Dyksma 2024, Microbiome | https://doi.org/10.1186/s40168-024-01909-7 | Medium; ecological adaptation edge | oxygen-defense module label-only |


*Table: This table lists evidence-backed subject–predicate–object triples relevant to curating the obligately anaerobic trait, spanning core oxygen toxicity mechanisms, defense systems, regulatory control, and assay/application conditions. It is designed to support direct translation into a TraitMech-style causal graph with confidence notes and grounding hints.*

## Ontology grounding notes (what is safe to curate now)

- **Chemicals:** O2 (CHEBI:15379), superoxide (CHEBI:18421), H2O2 (CHEBI:16240), hydroxyl radical (CHEBI:16243), resazurin (CHEBI:50373), L-cysteine (CHEBI:17561) have stable identifiers and are suitable for curation. (dyksma2024growthofsulfatereducing pages 1-2, lu2021whenanaerobesencounter pages 11-13, silva2024methodsforcultivation pages 5-6)
- **Genes/proteins:** For many defense enzymes (Fdp*, revRbr*, Roo/NorV, CydAB, KatG, Ahp, TrxA/B, MsrA) and regulators (σB, σA, Rex, OseR, Spx-family regulator), grounding should ideally be done at the **gene family / function** level (GO molecular function, EC, UniProt, KEGG ortholog, or MetaCyc reactions) in the final YAML; this report therefore provides label-level nodes with mechanistic evidence. (caulat2024physiologicalroleand pages 15-17, dyksma2024growthofsulfatereducing pages 1-2, caulat2024physiologicalroleand pages 2-5)

## Expert opinions and authoritative synthesis

Authoritative synthesis from a highly cited review emphasizes: (i) obligate anaerobiosis is defined by **growth blocked by O2**; (ii) oxygen sensitivity is frequently due to inactivation of a small set of essential enzymes (often radical or metal-centered), rather than wholesale absence of defenses; and (iii) many “obligate anaerobes” do possess defenses and can tolerate episodic oxygenation. (lu2021whenanaerobesencounter pages 1-3, lu2021whenanaerobesencounter pages 22-27)

## Relevant quantitative statistics/data extracted from recent studies

- *C. difficile* O2-defense enzymes have distinct O2 ranges (revRbr2 <0.4%; FdpA 0.4–1%; revRbr1 0.1–4%; FdpF >4% and air) and were tested across 0.1–4% O2 and air exposure assays. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5)
- SRB bioreactor oxygen regime: **133 µM O2 (50% air saturation)** during weekly oxic phases; SRB established populations **up to 2.9% relative abundance**. (dyksma2024growthofsulfatereducing pages 1-2)
- Methanogenic inhibition by O2 (headspace): **0.5% O2 → 30–40% MPR inhibition**; **5% O2 → ~100% inhibition** for acetate or H2/CO2 methanogenesis. (morais2024effectofmicroaeration pages 1-2)

## Warnings / non-curation notes (claims needing care)

1. **Taxon specificity:** The multi-enzyme O2-reductase partitioning described for *C. difficile* (FdpA/FdpF/revRbr1/2 and their regulatory wiring) should be curated as **species- or clade-specific** unless corroborated in other obligate anaerobes. (caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 15-17)
2. **Community vs isolate:** SRB tolerance to 133 µM O2 was shown in a **peat-soil bioreactor community**; do not generalize directly to pure culture tolerance thresholds without supporting isolate data. (dyksma2024growthofsulfatereducing pages 1-2)
3. **Source strength:** Some mechanistic descriptions of ROS damage to Fe–S enzymes are supported here by a thesis-text source; the same mechanisms are consistent with authoritative review synthesis, but curations relying on this text alone should be flagged as medium confidence. (bystrom2024couplingbutyrylcoenzymea pages 17-21, lu2021whenanaerobesencounter pages 22-27)

## DOI-first bibliography (with publication dates and URLs)

- Caulat LC et al. **Physiological role and complex regulation of O2-reducing enzymes in the obligate anaerobe *Clostridioides difficile*.** *mBio* (Oct 2024). DOI: 10.1128/mbio.01591-24. URL: https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 2-5)
- Dyksma S, Pester M. **Growth of sulfate-reducing Desulfobacterota and Bacillota at periodic oxygen stress of 50% air-O2 saturation.** *Microbiome* (Oct 2024). DOI: 10.1186/s40168-024-01909-7. URL: https://doi.org/10.1186/s40168-024-01909-7 (dyksma2024growthofsulfatereducing pages 1-2)
- da Silva RR, Adedoyin V, DuBois JL. **Methods for cultivation of *Bacteroides thetaiotaomicron* and analysis of heme metabolism…** *Methods in Molecular Biology* (Jan 2024). DOI: 10.1007/978-1-0716-4043-2_7. URL: https://doi.org/10.1007/978-1-0716-4043-2_7 (silva2024methodsforcultivation pages 1-3)
- Müller P et al. **High-throughput anaerobic screening for identifying compounds acting against gut bacteria in monocultures or communities.** *Nature Protocols* (Dec 2024). DOI: 10.1038/s41596-023-00926-4. URL: https://doi.org/10.1038/s41596-023-00926-4 (muller2024highthroughputanaerobicscreening pages 2-4)
- Morais BP et al. **Effect of micro-aeration on syntrophic and methanogenic activity in anaerobic sludge.** *Applied Microbiology and Biotechnology* (Feb 2024). DOI: 10.1007/s00253-023-12969-4. URL: https://doi.org/10.1007/s00253-023-12969-4 (morais2024effectofmicroaeration pages 1-2)
- Li X et al. **A Comprehensive Review of the Strategies to Improve Anaerobic Digestion…** *Methane* (Apr 2024). DOI: 10.3390/methane3020014. URL: https://doi.org/10.3390/methane3020014 (li2024acomprehensivereview pages 11-13)
- Lu Z, Imlay JA. **When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence.** *Nature Reviews Microbiology* (Jun 2021). DOI: 10.1038/s41579-021-00583-y. URL: https://doi.org/10.1038/s41579-021-00583-y (lu2021whenanaerobesencounter pages 1-3)
- Bystrom L. **Coupling butyryl-coenzyme A oxidation to oxygen reduction in *Fusobacterium nucleatum*.** (Jan 2024). DOI: 10.14288/1.0447284. URL: https://doi.org/10.14288/1.0447284 (bystrom2024couplingbutyrylcoenzymea pages 17-21)


References

1. (lu2021whenanaerobesencounter pages 1-3): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

2. (lu2021whenanaerobesencounter pages 3-4): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

3. (lu2021whenanaerobesencounter pages 4-6): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

4. (lu2021whenanaerobesencounter pages 22-27): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

5. (caulat2024physiologicalroleand pages 2-5): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

6. (caulat2024physiologicalroleand pages 5-7): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

7. (lu2021whenanaerobesencounter pages 13-15): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

8. (dyksma2024growthofsulfatereducing pages 1-2): Stefan Dyksma and Michael Pester. Growth of sulfate-reducing desulfobacterota and bacillota at periodic oxygen stress of 50% air-o2 saturation. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01909-7, doi:10.1186/s40168-024-01909-7. This article has 49 citations and is from a highest quality peer-reviewed journal.

9. (bystrom2024couplingbutyrylcoenzymea pages 17-21): Liam Bystrom. Coupling butyryl-coenzyme a oxidation to oxygen reduction in fusobacterium nucleatum. Text, Jan 2024. URL: https://doi.org/10.14288/1.0447284, doi:10.14288/1.0447284. This article has 0 citations and is from a peer-reviewed journal.

10. (lu2021whenanaerobesencounter pages 11-13): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

11. (caulat2024physiologicalroleand pages 1-2): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

12. (caulat2024physiologicalroleand pages 15-17): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

13. (silva2024methodsforcultivation pages 1-3): Ronivaldo Rodrigues da Silva, Victoria Adedoyin, and Jennifer L. DuBois. Methods for cultivation of bacteroides thetaiotaomicron and analysis of heme metabolism by mass spectrometry and spectroscopic approaches. Methods in molecular biology, 2839:113-130, Jan 2024. URL: https://doi.org/10.1007/978-1-0716-4043-2\_7, doi:10.1007/978-1-0716-4043-2\_7. This article has 3 citations and is from a peer-reviewed journal.

14. (silva2024methodsforcultivation pages 3-5): Ronivaldo Rodrigues da Silva, Victoria Adedoyin, and Jennifer L. DuBois. Methods for cultivation of bacteroides thetaiotaomicron and analysis of heme metabolism by mass spectrometry and spectroscopic approaches. Methods in molecular biology, 2839:113-130, Jan 2024. URL: https://doi.org/10.1007/978-1-0716-4043-2\_7, doi:10.1007/978-1-0716-4043-2\_7. This article has 3 citations and is from a peer-reviewed journal.

15. (muller2024highthroughputanaerobicscreening pages 2-4): Patrick Müller, Jacobo de la Cuesta-Zuluaga, Michael Kuhn, Maral Baghai Arassi, Tim Treis, Sonja Blasche, Michael Zimmermann, Peer Bork, Kiran Raosaheb Patil, Athanasios Typas, Sarela Garcia-Santamarina, and Lisa Maier. High-throughput anaerobic screening for identifying compounds acting against gut bacteria in monocultures or communities. Nature protocols, 19:668-699, Dec 2024. URL: https://doi.org/10.1038/s41596-023-00926-4, doi:10.1038/s41596-023-00926-4. This article has 38 citations and is from a peer-reviewed journal.

16. (muller2024highthroughputanaerobicscreening pages 15-18): Patrick Müller, Jacobo de la Cuesta-Zuluaga, Michael Kuhn, Maral Baghai Arassi, Tim Treis, Sonja Blasche, Michael Zimmermann, Peer Bork, Kiran Raosaheb Patil, Athanasios Typas, Sarela Garcia-Santamarina, and Lisa Maier. High-throughput anaerobic screening for identifying compounds acting against gut bacteria in monocultures or communities. Nature protocols, 19:668-699, Dec 2024. URL: https://doi.org/10.1038/s41596-023-00926-4, doi:10.1038/s41596-023-00926-4. This article has 38 citations and is from a peer-reviewed journal.

17. (morais2024effectofmicroaeration pages 1-2): Bruno P. Morais, Carla P. Magalhães, Gilberto Martins, Maria Alcina Pereira, and Ana J. Cavaleiro. Effect of micro-aeration on syntrophic and methanogenic activity in anaerobic sludge. Applied Microbiology and Biotechnology, Feb 2024. URL: https://doi.org/10.1007/s00253-023-12969-4, doi:10.1007/s00253-023-12969-4. This article has 16 citations and is from a domain leading peer-reviewed journal.

18. (li2024acomprehensivereview pages 11-13): Xiaoyong Li, Zhi Wang, Yun He, Yuzhong Wang, Shilei Wang, Zehui Zheng, Songtao Wang, Jingliang Xu, Yafan Cai, and Hanjie Ying. A comprehensive review of the strategies to improve anaerobic digestion: their mechanism and digestion performance. Methane, 3:227-256, Apr 2024. URL: https://doi.org/10.3390/methane3020014, doi:10.3390/methane3020014. This article has 47 citations.

19. (li2024acomprehensivereview pages 1-2): Xiaoyong Li, Zhi Wang, Yun He, Yuzhong Wang, Shilei Wang, Zehui Zheng, Songtao Wang, Jingliang Xu, Yafan Cai, and Hanjie Ying. A comprehensive review of the strategies to improve anaerobic digestion: their mechanism and digestion performance. Methane, 3:227-256, Apr 2024. URL: https://doi.org/10.3390/methane3020014, doi:10.3390/methane3020014. This article has 47 citations.

20. (dyksma2024growthofsulfatereducing pages 5-6): Stefan Dyksma and Michael Pester. Growth of sulfate-reducing desulfobacterota and bacillota at periodic oxygen stress of 50% air-o2 saturation. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01909-7, doi:10.1186/s40168-024-01909-7. This article has 49 citations and is from a highest quality peer-reviewed journal.

21. (silva2024methodsforcultivation pages 5-6): Ronivaldo Rodrigues da Silva, Victoria Adedoyin, and Jennifer L. DuBois. Methods for cultivation of bacteroides thetaiotaomicron and analysis of heme metabolism by mass spectrometry and spectroscopic approaches. Methods in molecular biology, 2839:113-130, Jan 2024. URL: https://doi.org/10.1007/978-1-0716-4043-2\_7, doi:10.1007/978-1-0716-4043-2\_7. This article has 3 citations and is from a peer-reviewed journal.

22. (morais2024effectofmicroaeration pages 2-4): Bruno P. Morais, Carla P. Magalhães, Gilberto Martins, Maria Alcina Pereira, and Ana J. Cavaleiro. Effect of micro-aeration on syntrophic and methanogenic activity in anaerobic sludge. Applied Microbiology and Biotechnology, Feb 2024. URL: https://doi.org/10.1007/s00253-023-12969-4, doi:10.1007/s00253-023-12969-4. This article has 16 citations and is from a domain leading peer-reviewed journal.