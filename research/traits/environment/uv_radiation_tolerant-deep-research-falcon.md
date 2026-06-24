---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:51:25.399895'
end_time: '2026-06-18T02:59:19.016024'
duration_seconds: 473.62
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: UV radiation tolerant
  trait_identifier: traitmech:000009
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: uv_radiation_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An environmental tolerance in which an organism survives high doses
    of ultraviolet radiation, typically via photoreactivation and nucleotide-excision
    repair of cyclobutane pyrimidine dimers and 6-4 photoproducts.
  parent_traits: traitmech:000007
  synonyms: UV resistant
  evidence_summary: "DOI:10.3390/genes14091803: Deinococcus radiodurans R1 demonstrates\
    \ a significantly higher radiation resistance with D10 values exceeding 12 kGy\
    \ for gamma radiation and 700 J/m2 for UV-C radiation (Organism example: Deinococcus\
    \ radiodurans tolerates UV-C radiation D10 doses of 700 J/m2.) | DOI:10.1101/cshperspect.a012765:\
    \ The bacterium Deinococcus radiodurans is a champion of extreme radiation resistance\
    \ (Review support \u2014 Deinococcus radiodurans is the reference organism for\
    \ extreme UV and ionizing radiation resistance.)"
  causal_graph_summary: 'uv_tolerance_excision_repair: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** UV radiation tolerant
- **METPO identifier:** traitmech:000009
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives high doses of ultraviolet radiation, typically via photoreactivation and nucleotide-excision repair of cyclobutane pyrimidine dimers and 6-4 photoproducts.
- **Parent traits:** traitmech:000007
- **Synonyms:** UV resistant
- **Existing evidence:** DOI:10.3390/genes14091803: Deinococcus radiodurans R1 demonstrates a significantly higher radiation resistance with D10 values exceeding 12 kGy for gamma radiation and 700 J/m2 for UV-C radiation (Organism example: Deinococcus radiodurans tolerates UV-C radiation D10 doses of 700 J/m2.) | DOI:10.1101/cshperspect.a012765: The bacterium Deinococcus radiodurans is a champion of extreme radiation resistance (Review support — Deinococcus radiodurans is the reference organism for extreme UV and ionizing radiation resistance.)
- **Existing causal graph summary:** uv_tolerance_excision_repair: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **UV radiation tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/uv_radiation_tolerant.yaml`.

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
- **Trait label:** UV radiation tolerant
- **METPO identifier:** traitmech:000009
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives high doses of ultraviolet radiation, typically via photoreactivation and nucleotide-excision repair of cyclobutane pyrimidine dimers and 6-4 photoproducts.
- **Parent traits:** traitmech:000007
- **Synonyms:** UV resistant
- **Existing evidence:** DOI:10.3390/genes14091803: Deinococcus radiodurans R1 demonstrates a significantly higher radiation resistance with D10 values exceeding 12 kGy for gamma radiation and 700 J/m2 for UV-C radiation (Organism example: Deinococcus radiodurans tolerates UV-C radiation D10 doses of 700 J/m2.) | DOI:10.1101/cshperspect.a012765: The bacterium Deinococcus radiodurans is a champion of extreme radiation resistance (Review support — Deinococcus radiodurans is the reference organism for extreme UV and ionizing radiation resistance.)
- **Existing causal graph summary:** uv_tolerance_excision_repair: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **UV radiation tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/uv_radiation_tolerant.yaml`.

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


## Research Report: Microbial Trait “UV radiation tolerant” (METPO: traitmech:000009)

### 1) Trait scope (phenotype definition and boundaries)
**Trait definition (curation scope).** *UV radiation tolerant* denotes the capacity of a microorganism to **survive exposure to high doses of ultraviolet radiation** (typically UV-B/UV-C in laboratory assays, and UV-A/UV-B in environmental contexts) via a combination of (i) **DNA damage repair** (notably photoreactivation/photolyase and nucleotide excision repair), (ii) **UV screening/avoidance** (e.g., extracellular pigments that attenuate UV penetration), and (iii) **management of UV-induced oxidative stress** (ROS detoxification). Core UV-induced DNA lesions implicated in this trait are **cyclobutane pyrimidine dimers (CPDs)** and **(6-4) photoproducts (6-4PPs)**. (garciamouronte2024understandingactivephotoprotection pages 2-4, ellington2025thegeneticdeterminants pages 19-20)

**Key boundary conditions.** UV tolerance is frequently **assay-conditional**, because **post-UV exposure to photoreactivating light** (near-UV/blue/visible light) can substantially increase survival by enabling photolyase-mediated direct repair; therefore, *UV tolerance* measured in “light” vs “dark” recovery conditions can reflect different causal mechanisms. (nag2023genomicanalysisof pages 4-6)

**Distinguishing from nearby traits.**
- **Ionizing radiation tolerance** (gamma/X-ray) overlaps mechanistically (oxidative damage, DNA repair) but is distinct in damage spectrum and is not the primary focus of this trait definition; UV damage is dominated by CPDs/6-4PPs. (garciamouronte2024understandingactivephotoprotection pages 2-4, ellington2025thegeneticdeterminants pages 19-20)
- **Oxidative-stress tolerance** is a contributing component because UV also generates ROS, but UV tolerance specifically includes UV photolesions and UV screening mechanisms. (ellington2025thegeneticdeterminants pages 1-2)
- **Desiccation tolerance** can co-occur (e.g., stratosphere/endolithic contexts), and dry DNA conditions can shift lesion types (e.g., spore photoproduct), but desiccation is not required for UV tolerance. (ellington2025thegeneticdeterminants pages 19-20, ellington2025thegeneticdeterminants pages 29-30)

### 2) Key concepts and mechanistic definitions (current understanding)
#### 2.1 UV-induced DNA lesion types
- **Cyclobutane pyrimidine dimers (CPDs):** described as a principal UV-induced DNA photoproduct and commonly the majority lesion type under UV exposure. (ellington2025thegeneticdeterminants pages 19-20, garciamouronte2024understandingactivephotoprotection pages 2-4)
- **Pyrimidine (6-4) pyrimidone photoproducts (6-4PPs):** another principal UV-induced lesion type. (garciamouronte2024understandingactivephotoprotection pages 2-4, tunca2026dnarepairmechanisms pages 1-2)

Both CPDs and 6-4PPs can **impede transcription and replication**, increasing mutagenesis risk if unrepaired. (laughery2025illuminatinggenomerepair pages 1-3, ellington2025thegeneticdeterminants pages 1-2)

#### 2.2 Primary DNA repair routes supporting UV tolerance
- **Photoreactivation (photolyase-dependent direct repair):** photolyases are flavoprotein enzymes that use **near-UV/blue light** to directly reverse UV photoproducts; photolyases are **substrate-specific** (CPD photolyase vs 6-4 photolyase). (garciamouronte2024understandingactivephotoprotection pages 2-4, singh2023resilienceandmitigation pages 11-13)
- **Nucleotide excision repair (NER):** a conserved multi-protein pathway that removes bulky helix-distorting lesions; NER is described as efficient for 6-4PPs but less effective for CPDs relative to photolyase-based repair. (garciamouronte2024understandingactivephotoprotection pages 2-4)

#### 2.3 UV-associated oxidative stress
UV can generate **reactive oxygen species (ROS)**, which can drive **strand breaks and oxidative base damage**, adding an oxidative-stress axis to UV tolerance. (ellington2025thegeneticdeterminants pages 1-2)

### 3) Recent developments and latest research (prioritizing 2023–2024)
#### 3.1 Haloarchaea: genotype–phenotype links for UV-C tolerance (2023)
A 2023 comparative study of diverse haloarchaea quantified survival after **254 nm UV-C doses (0–144 J/m²)** under **photoreactivating light vs dark** recovery. Multiple strains showed **complete survival up to 144 J/m² with photoreactivation**, whereas most strains showed **3–4 log killing at 144 J/m² without photoreactivation**, indicating strong dependence of tolerance on light-enabled repair. (nag2023genomicanalysisof pages 4-6)

This work also explicitly connects UV tolerance variation to **photolyase gene functionality/variants** and documents that haloarchaeal genomes include both **photorepair (photolyase)** and **dark repair via NER components (uvrABC/uvrD)**; deletion of **uvrA** or **uvrC** strongly diminishes dark repair in the haloarchaeal model. (nag2023genomicanalysisof pages 2-4)

#### 3.2 Halophilic archaeon UV-C tolerance and DNA repair gene repertoire (2023)
A 2023 study on *Natrinema altunense* 4.1R reported survival up to **180 J/m² UV-C**, and identified repair determinants including **UvrA/UvrB/UvrC excinucleases (NER)** and **photolyase**, alongside oxidative-stress defense systems (e.g., SOD). (najjari2023physiologicalandgenomic pages 1-2)

#### 3.3 Cyanobacteria: integrated model of UV stress responses (2023)
A 2023 cyanobacterial UV-stress synthesis emphasizes **photoreactivation as a dominant DNA repair pathway** in cyanobacteria and provides mechanistic detail for photolyase cofactors and electron-transfer-based monomerization of CPDs/6-4PPs. It also reports UV-associated upregulation of DNA-repair genes including **phrA (photolyase)** and **uvrC (NER)** during recovery in specific cyanobacterial contexts. (singh2023resilienceandmitigation pages 11-13)

#### 3.4 Scytonemin as an extracellular UV screen with production optimization data (2024)
A 2024 study on endolithic Atacama cyanobacteria provides quantitative production data for **scytonemin**, a **lipid-soluble, EPS-sheath-localized UV-screening pigment** that can reduce **~90% of incident radiation reaching cell interiors**. (casero2024effectofsalinity pages 1-2)

The same work reports strong regulation by salinity: at **20 g/L NaCl**, scytonemin content reached **3.17 mg/g dry weight after 14 days**, described as a **53-fold increase**, with productivity **57.4 µg/L/day** (vs 1.2 µg/L/day at 0 NaCl). (casero2024effectofsalinity pages 2-3)

A key mechanistic development relevant to curation is that the scytonemin biosynthetic cluster comprises ~18 genes and that a **minimal set (scyA/scyB/scyC)** was sufficient for **heterologous scytonemin production in *E. coli***. (casero2024effectofsalinity pages 1-2)

#### 3.5 A 2024 mechanistic synthesis of UV lesions and repair pathway roles
A 2024 review summarises the lesion spectrum (CPDs and 6-4PPs) and clarifies functional differences between NER and photolyase-based repair (e.g., NER more efficient for 6-4PPs and less effective for CPDs). (garciamouronte2024understandingactivephotoprotection pages 2-4)

### 4) Current applications and real-world implementations
#### 4.1 UV-screening pigments as bioproducts (cosmetics/materials)
Endolithic desert cyanobacteria are presented as candidates for **pilot-scale cultivation** for **scytonemin production** for biotechnological applications (including cosmetics), supported by controllable yield increases under salt stress. (casero2024effectofsalinity pages 1-2, casero2024effectofsalinity pages 2-3)

#### 4.2 Astrobiology/extreme-environment survival models
Haloarchaeal UV survival diversity is framed as reflective of natural UV exposure and is explicitly discussed in the context of survival in ancient halite deposits and potential extraterrestrial surface environments. (nag2023genomicanalysisof pages 1-2)

### 5) Expert opinions and analysis (authoritative, source-grounded)
**Photoreactivation as a major determinant of apparent UV tolerance.** Quantitative haloarchaeal survival differences between light and dark recovery strongly indicate that assay conditions can switch the dominant mechanism from photolyase-driven direct repair to dark repair pathways (e.g., NER), and thus can change whether an organism is labeled “UV tolerant” in practice. (nag2023genomicanalysisof pages 4-6, nag2023genomicanalysisof pages 2-4)

**UV tolerance is multi-component (“resistome” framing).** Mechanistic framing in extremophile-focused work emphasizes that UV tolerance is not solely DNA repair; it includes shielding and detoxification components (e.g., pigments, catalases) in addition to repair and tolerance strategies. (ellington2025thegeneticdeterminants pages 1-2)

### Candidate nodes for TraitMech causal graph (grouped)
#### A) Environmental and experimental factors
- UV radiation (UV-B/UV-C; plus photoreactivating light exposure during recovery) (nag2023genomicanalysisof pages 4-6)
- Salinity/NaCl stress (modulates scytonemin yield; conditional) (casero2024effectofsalinity pages 2-3)

#### B) DNA lesions and damage classes
- Cyclobutane pyrimidine dimer (CPD) (ellington2025thegeneticdeterminants pages 19-20, garciamouronte2024understandingactivephotoprotection pages 2-4)
- (6-4) photoproduct (6-4PP) (garciamouronte2024understandingactivephotoprotection pages 2-4)
- ROS-mediated DNA damage (strand breaks, oxidative base damage; optional auxiliary node) (ellington2025thegeneticdeterminants pages 1-2)

#### C) Pathways / biological processes
- Photoreactivation (photolyase-mediated direct reversal) (singh2023resilienceandmitigation pages 11-13)
- Nucleotide excision repair (NER) (GO:0006289) (garciamouronte2024understandingactivephotoprotection pages 2-4)
- Oxidative stress detoxification / antioxidant defenses (ellington2025thegeneticdeterminants pages 1-2)

#### D) Genes/proteins (examples that support generalizable nodes)
- Photolyase (CPD photolyase; 6-4 photolyase) (garciamouronte2024understandingactivephotoprotection pages 2-4, singh2023resilienceandmitigation pages 11-13)
- NER proteins: uvrA, uvrB, uvrC, uvrD (nag2023genomicanalysisof pages 2-4, najjari2023physiologicalandgenomic pages 1-2)
- Antioxidant enzymes: catalase, superoxide dismutase (SOD) (ellington2025thegeneticdeterminants pages 1-2, najjari2023physiologicalandgenomic pages 1-2)

#### E) Protective metabolites/pigments
- Scytonemin (extracellular UV screen) (casero2024effectofsalinity pages 1-2)
- Mycosporine-like amino acids (MAAs; UV absorbance + ROS quenching) (singh2023resilienceandmitigation pages 9-11)

### Candidate causal edges (evidence-backed; curation-ready)
| Edge (subject–predicate–object) | Node types | Suggested ontology grounding (CURIEs where possible) | Evidence snippet (short quote/paraphrase) | Reference (DOI, year, URL) | Evidence strength/notes |
|---|---|---|---|---|---|
| UV radiation exposure → causes → cyclobutane pyrimidine dimers (CPDs) | environmental factor → DNA lesion | ENVO:ultraviolet radiation; CHEBI:cyclobutane pyrimidine dimer (candidate label) | UV produces “two primary pyrimidine photoproducts — cyclobutane pyrimidine dimers (CPDs) and … 6-4PPs”; CPDs are the majority lesion. (ellington2025thegeneticdeterminants pages 19-20, garciamouronte2024understandingactivephotoprotection pages 2-4) | 10.3390/life14070822 (2024) https://doi.org/10.3390/life14070822; 10.3390/microorganisms13040756 (2025) https://doi.org/10.3390/microorganisms13040756 | Strong, general across taxa; central trait-defining lesion. |
| UV radiation exposure → causes → pyrimidine (6-4) pyrimidone photoproducts (6-4PPs) | environmental factor → DNA lesion | ENVO:ultraviolet radiation; label-only candidate: 6-4 photoproduct | Principal UV lesions include CPDs and “pyrimidine (6-4) pyrimidone photoproducts (6-4PPs).” (garciamouronte2024understandingactivephotoprotection pages 2-4, tunca2026dnarepairmechanisms pages 1-2) | 10.3390/life14070822 (2024) https://doi.org/10.3390/life14070822; 10.17216/limnofish.1792319 (2026) https://doi.org/10.17216/limnofish.1792319 | Strong, general; 2026 source used only as supporting background. |
| CPDs → inhibit → transcription/replication | DNA lesion → biological process | GO:0006351 transcription, DNA-templated; GO:0006260 DNA replication | Pyrimidine dimers “inhibit transcription and replication”; CPDs and 6-4PPs impede these processes if unrepaired. (ellington2025thegeneticdeterminants pages 1-2, laughery2025illuminatinggenomerepair pages 1-3) | 10.3390/microorganisms13040756 (2025) https://doi.org/10.3390/microorganisms13040756; 10.1111/php.70047 (2025) https://doi.org/10.1111/php.70047 | Strong, mechanistically general. |
| 6-4PPs → inhibit → transcription/replication | DNA lesion → biological process | GO:0006351; GO:0006260 | 6-4PPs are major UV photoproducts that impede transcription and replication and lead to mutations if unrepaired. (laughery2025illuminatinggenomerepair pages 1-3, garciamouronte2024understandingactivephotoprotection pages 2-4) | 10.1111/php.70047 (2025) https://doi.org/10.1111/php.70047; 10.3390/life14070822 (2024) https://doi.org/10.3390/life14070822 | Strong, mechanistically general. |
| CPD photolyase → repairs → CPDs | protein/enzyme → DNA lesion | GO:0003904 photolyase activity; UniProt/EC candidate if taxon-specific protein curated later | Photolyases directly reverse UV photoproducts; CPD photolyase uses light-driven electron transfer to monomerize CPD dimers. (singh2023resilienceandmitigation pages 11-13, garciamouronte2024understandingactivephotoprotection pages 2-4) | 10.3390/ijms241512381 (2023) https://doi.org/10.3390/ijms241512381; 10.3390/life14070822 (2024) https://doi.org/10.3390/life14070822 | Strong, general; canonical edge for UV tolerance. |
| 6-4 photolyase → repairs → 6-4PPs | protein/enzyme → DNA lesion | GO:0003904 photolyase activity (broad); label-only candidate: 6-4 photolyase | Separate substrate-specific photolyases repair 6-4PPs; 6-4 photolyase activity is described across taxa. (garciamouronte2024understandingactivephotoprotection pages 2-4, tunca2026dnarepairmechanisms pages 1-2) | 10.3390/life14070822 (2024) https://doi.org/10.3390/life14070822; 10.17216/limnofish.1792319 (2026) https://doi.org/10.17216/limnofish.1792319 | Strong but enzyme subtype grounding may remain label-only. |
| photoreactivating light (UV-A/blue light) → activates → photolyase-mediated DNA repair | experimental factor/light condition → biological process | ENVO:blue light (candidate); GO:0019555 photoreactivation | Light-harvesting cofactors absorb UV-A/blue light and transfer energy to catalytic FADH, enabling direct reversal of dimers. (singh2023resilienceandmitigation pages 11-13) | 10.3390/ijms241512381 (2023) https://doi.org/10.3390/ijms241512381 | Strong, assay-relevant; important boundary condition because tolerance can depend on post-UV light exposure. |
| nucleotide excision repair (NER) → repairs → CPDs | pathway/process → DNA lesion | GO:0006289 nucleotide-excision repair | NER is a conserved pathway removing UV photolesions; it repairs CPDs, though often less efficiently than photolyase. (garciamouronte2024understandingactivephotoprotection pages 2-4, laughery2025illuminatinggenomerepair pages 1-3) | 10.3390/life14070822 (2024) https://doi.org/10.3390/life14070822; 10.1111/php.70047 (2025) https://doi.org/10.1111/php.70047 | Strong, general; note relative efficiency is context-dependent. |
| nucleotide excision repair (NER) → repairs → 6-4PPs | pathway/process → DNA lesion | GO:0006289 nucleotide-excision repair | NER “corrects 6-4PPs efficiently” and removes bulky UV photolesions. (garciamouronte2024understandingactivephotoprotection pages 2-4) | 10.3390/life14070822 (2024) https://doi.org/10.3390/life14070822 | Strong, general. |
| uvrA/uvrB/uvrC excinuclease system → enables → nucleotide excision repair of UV damage | genes/proteins → pathway/process | KEGG/UniProt label candidates: uvrA, uvrB, uvrC; GO:0006289 | Haloarchaea and other microbes encode uvrABC; deletion of uvrA or uvrC greatly diminishes dark repair. (nag2023genomicanalysisof pages 2-4, najjari2023physiologicalandgenomic pages 1-2) | 10.3390/microorganisms11030607 (2023) https://doi.org/10.3390/microorganisms11030607; 10.1007/s10709-023-00182-0 (2023) https://doi.org/10.1007/s10709-023-00182-0 | Strong for NER role; knockout evidence especially strong in haloarchaea, but taxon-specific details should be noted. |
| uvrD helicase → participates_in → dark repair / NER | gene/protein → pathway/process | KEGG/UniProt label candidate: uvrD; GO:0006289 | Dark repair in haloarchaea is mediated by UvrABCD excinuclease activity; UvrD is part of the encoded NER toolkit. (nag2023genomicanalysisof pages 2-4) | 10.3390/microorganisms11030607 (2023) https://doi.org/10.3390/microorganisms11030607 | Moderate; pathway membership strong, direct causal phenotype support in provided context is less explicit than for uvrA/uvrC. |
| UV radiation exposure → generates → reactive oxygen species (ROS) | environmental factor → chemical/process | ENVO:ultraviolet radiation; CHEBI:reactive oxygen species | Indirect UV effects via photolysis of water generate ROS that damage DNA, proteins and lipids. (ellington2025thegeneticdeterminants pages 1-2) | 10.3390/microorganisms13040756 (2025) https://doi.org/10.3390/microorganisms13040756 | Strong, general; captures non-lesion-mediated component of tolerance. |
| ROS → causes → DNA strand breaks and oxidative base damage | chemical/process → DNA damage process | CHEBI:reactive oxygen species; GO:0006974 response to DNA damage stimulus (broad) | ROS induce single- and double-strand breaks, apurinic sites and base damage. (ellington2025thegeneticdeterminants pages 1-2) | 10.3390/microorganisms13040756 (2025) https://doi.org/10.3390/microorganisms13040756 | Strong, general. |
| catalase → detoxifies → ROS | enzyme/protein → chemical/process | EC:1.11.1.6; GO:0004096 catalase activity | Genomic analyses implicated catalases in UV resistance; ROS-scavengers/catalases detoxify ROS and prevent oxidative damage. (ellington2025thegeneticdeterminants pages 1-2, najjari2023physiologicalandgenomic pages 1-2) | 10.3390/microorganisms13040756 (2025) https://doi.org/10.3390/microorganisms13040756; 10.1007/s10709-023-00182-0 (2023) https://doi.org/10.1007/s10709-023-00182-0 | Moderate-to-strong; general antioxidant edge, but specific causal magnitude may be taxon-specific. |
| superoxide dismutase (SOD) → detoxifies → ROS | enzyme/protein → chemical/process | EC:1.15.1.1; GO:0004784 superoxide dismutase activity | Haloarchaeal genomes encode SOD among UV/oxidative stress defenses; antioxidant systems are part of UV tolerance. (najjari2023physiologicalandgenomic pages 1-2) | 10.1007/s10709-023-00182-0 (2023) https://doi.org/10.1007/s10709-023-00182-0 | Moderate; good support for stress-defense node, but direct UV-specific knockout evidence not provided here. |
| scytonemin → reduces exposure_to → intracellular UV radiation | pigment/metabolite → environmental factor | CHEBI candidate: scytonemin (label-only if CURIE unavailable); GO candidate: sunscreening pigment process not established | Scytonemin is an EPS-sheath UV-screening pigment that can reduce “~90% of the radiation reaching cell interiors.” (casero2024effectofsalinity pages 1-2) | 10.1038/s41598-024-60499-4 (2024) https://doi.org/10.1038/s41598-024-60499-4 | Strong for cyanobacteria; taxon-specific, extracellular shielding mechanism. |
| UV radiation exposure → induces → scytonemin biosynthesis | environmental factor → biosynthetic process/metabolite | ENVO:ultraviolet radiation; label-only candidate: scytonemin biosynthetic process | Scytonemin production is inducible and triggered by UV radiation, oxidative stress, nutrient deficit, desiccation, and salt stress. (casero2024effectofsalinity pages 1-2) | 10.1038/s41598-024-60499-4 (2024) https://doi.org/10.1038/s41598-024-60499-4 | Strong for cyanobacteria; induction may be multifactorial, not UV-exclusive. |
| scyA/scyB/scyC → enable → scytonemin biosynthesis | genes → metabolite/biosynthetic process | label-only candidates: scyA, scyB, scyC | Scytonemin cluster contains ~18 genes; “a minimal set (scyA, scyB, scyC) was sufficient for heterologous production in E. coli.” (casero2024effectofsalinity pages 1-2) | 10.1038/s41598-024-60499-4 (2024) https://doi.org/10.1038/s41598-024-60499-4 | Strong for biosynthesis; taxon-specific gene cluster edge suitable for curated subgraph. |
| NaCl stress (20 g/L) → increases → scytonemin accumulation in Chroococcidiopsis sp. UAM571 | environmental/experimental factor → metabolite abundance | CHEBI:NaCl; NCBITaxon:Chroococcidiopsis (genus-level candidate); scytonemin label | In Atacama strain UAM571, 20 g/L NaCl produced a “53-fold increase” in scytonemin; 3.17 mg gDW−1 after 14 d and 57.4 µg L−1 d−1 productivity. (casero2024effectofsalinity pages 2-3) | 10.1038/s41598-024-60499-4 (2024) https://doi.org/10.1038/s41598-024-60499-4 | Strong but assay-specific and not a universal UV-tolerance edge; useful for conditional regulation subgraph. |
| mycosporine-like amino acids (MAAs) → absorb/dissipate → UV-A/UV-B radiation | metabolite class → environmental factor | CHEBI candidate: mycosporine-like amino acid; label-only class node | MAAs absorb ~309–362 nm with high extinction coefficients and release absorbed UV as harmless heat. (singh2023resilienceandmitigation pages 9-11) | 10.3390/ijms241512381 (2023) https://doi.org/10.3390/ijms241512381 | Strong, general especially for cyanobacteria/algae. |
| MAAs → quench → reactive oxygen species | metabolite class → chemical/process | CHEBI candidate: mycosporine-like amino acid; CHEBI:reactive oxygen species | MAAs act as antioxidants/free-radical scavengers and quench ROS induced by PAR, UV-A, and UV-B. (singh2023resilienceandmitigation pages 9-11) | 10.3390/ijms241512381 (2023) https://doi.org/10.3390/ijms241512381 | Strong, but mechanism/class-level rather than single-gene level. |
| UV-B exposure → induces → MAA synthesis | environmental factor → biosynthetic process/metabolite | ENVO:UV-B radiation; label-only candidate: MAA biosynthetic process | UV-B is reported as the strongest inducer of MAA synthesis; a UV-B photoreceptor in Chlorogloeopsis PCC6912 induces MAA production. (singh2023resilienceandmitigation pages 9-11) | 10.3390/ijms241512381 (2023) https://doi.org/10.3390/ijms241512381 | Moderate-to-strong; taxon examples support broader pattern. |
| mysA/mysB/mysC/mysD gene cluster → enables → MAA biosynthesis | genes → metabolite class/biosynthetic process | label-only candidates: mysA, mysB, mysC, mysD | A defined “mysABC-D” biosynthetic cluster is reported; heterologous expression produced MAA analogues such as palythine and mycosporine-glycine. (wang2025naturalantioxidantsderived pages 5-7) | 10.1186/s44315-025-00050-w (2025) https://doi.org/10.1186/s44315-025-00050-w | Moderate; useful biosynthesis edge, but 2025 source and broader taxonomic coverage mean curation should note source recency and class-level inference. |
| photoreactivation-permissive light exposure → increases survival_after UV-C → haloarchaea | experimental factor → phenotype | ENVO:visible light (candidate); METPO:traitmech:000009 | In haloarchaea, several strains showed complete survival up to 144 J/m2 with photoreactivation, while most had 3–4 log killing at 144 J/m2 in the dark. (nag2023genomicanalysisof pages 4-6) | 10.3390/microorganisms11030607 (2023) https://doi.org/10.3390/microorganisms11030607 | Strong, assay-specific phenotype edge; highlights dependence of observed tolerance on post-irradiation lighting. |
| functional photolyase gene variants → associated_with_higher → UV-C survival in haloarchaea | gene/protein variant → phenotype | label-only candidate: photolyase (phr2) | Natural UV tolerance in haloarchaea correlated with photolyase gene functionality; strains lacking/altering photolyase were less tolerant. (nag2023genomicanalysisof pages 1-2, nag2023genomicanalysisof pages 2-4) | 10.3390/microorganisms11030607 (2023) https://doi.org/10.3390/microorganisms11030607 | Moderate-to-strong; association is compelling, though comparative and partly inferred from natural variation. |
| photolyase + uvrABC repair capacity → contributes_to → UV-C survival up to 180 J/m2 in Natrinema altunense 4.1R | genes/pathways → phenotype | label-only: photolyase, uvrA, uvrB, uvrC; NCBITaxon:Natrinema altunense (candidate) | N. altunense 4.1R survived UV-C doses up to 180 J/m2 and encodes photolyase plus UvrA/UvrB/UvrC repair proteins. (najjari2023physiologicalandgenomic pages 1-2) | 10.1007/s10709-023-00182-0 (2023) https://doi.org/10.1007/s10709-023-00182-0 | Moderate; phenotype and mechanism co-occur, but direct genetic causality was not experimentally dissected in provided context. |


*Table: This table compiles curation-ready subject–predicate–object edges for the microbial trait UV radiation tolerant, grounded where possible to stable ontology terms and supported by recent evidence. It emphasizes DNA lesion formation and repair, antioxidant defenses, UV-screening pigments, and assay-dependent quantitative phenotype data relevant for TraitMech curation.*

### Relevant statistics and quantitative data (recent studies)
- **Haloarchaea (UV-C 254 nm):** doses 0–144 J/m²; with photoreactivation some strains show complete survival up to 144 J/m²; without photoreactivation many strains show ~3–4 log killing at 144 J/m². (nag2023genomicanalysisof pages 4-6)
- **Halophilic archaeon *Natrinema altunense* 4.1R:** survival up to **180 J/m² UV-C**. (najjari2023physiologicalandgenomic pages 1-2)
- **Atacama endolithic cyanobacterium (*Chroococcidiopsis* sp. UAM571):** scytonemin content up to **3.17 mg/g DW** at 20 g/L NaCl after 14 days; **53-fold increase** vs control; productivity **57.4 µg/L/day** at 20 g/L NaCl. (casero2024effectofsalinity pages 2-3)

### Warnings / curation caveats (do not yet curate as high-confidence general edges)
1. **Assay dependence:** UV tolerance phenotypes can be dominated by **photoreactivation conditions**; record whether recovery was in light or dark when curating trait evidence. (nag2023genomicanalysisof pages 4-6)
2. **Taxon specificity of shielding pigments:** scytonemin is emphasized as an extracellular EPS-sheath pigment in cyanobacteria; its protective role should not be generalized to non-scytonemin-producing taxa without evidence. (casero2024effectofsalinity pages 1-2)
3. **Conditional regulation edges:** NaCl → scytonemin yield is a strong, quantitative edge but is primarily a **production/bioprocess regulation** relationship and may not generalize across cyanobacteria or environmental contexts. (casero2024effectofsalinity pages 2-3)
4. **Incomplete ontology grounding:** several chemical entities (e.g., scytonemin, CPD/6-4PP) may require confirmation of CHEBI identifiers during curation; label-only nodes are recommended until grounded.

---

## DOI-first bibliography (with publication dates and URLs)
- **Najjari A, et al. (Feb 2023).** Physiological and genomic insights into abiotic stress of halophilic archaeon *Natrinema altunense* 4.1R… *Genetica* 151:133–152. DOI: **10.1007/s10709-023-00182-0**. https://doi.org/10.1007/s10709-023-00182-0 (najjari2023physiologicalandgenomic pages 1-2)
- **Nag S, et al. (Feb 2023).** Genomic Analysis of Haloarchaea… Reveals Diversity of Ultraviolet Radiation Survival and DNA Photolyase Gene Variants. *Microorganisms* 11:607. DOI: **10.3390/microorganisms11030607**. https://doi.org/10.3390/microorganisms11030607 (nag2023genomicanalysisof pages 4-6)
- **Singh VK, et al. (Aug 2023).** Resilience and Mitigation Strategies of Cyanobacteria under Ultraviolet Radiation Stress. *Int J Mol Sci* 24:12381. DOI: **10.3390/ijms241512381**. https://doi.org/10.3390/ijms241512381 (singh2023resilienceandmitigation pages 11-13)
- **Casero MC, et al. (Apr 2024).** Effect of salinity on scytonemin yield in endolithic cyanobacteria from the Atacama Desert. *Scientific Reports* 14. DOI: **10.1038/s41598-024-60499-4**. https://doi.org/10.1038/s41598-024-60499-4 (casero2024effectofsalinity pages 2-3)
- **Garcia-Mouronte E, et al. (Jun 2024).** Understanding Active Photoprotection: DNA-Repair Enzymes and Antioxidants. *Life* 14:822. DOI: **10.3390/life14070822**. https://doi.org/10.3390/life14070822 (garciamouronte2024understandingactivephotoprotection pages 2-4)

(Additional supporting but non-priority years used for mechanistic context: Ellington et al. 2025, 10.3390/microorganisms13040756; Laughery & Wyrick 2025, 10.1111/php.70047.) (ellington2025thegeneticdeterminants pages 1-2, laughery2025illuminatinggenomerepair pages 1-3)

References

1. (garciamouronte2024understandingactivephotoprotection pages 2-4): Emilio Garcia-Mouronte, Luis Alfonso Pérez-González, Jorge Naharro-Rodriguez, and Montserrat Fernández Guarino. Understanding active photoprotection: dna-repair enzymes and antioxidants. Life, 14:822, Jun 2024. URL: https://doi.org/10.3390/life14070822, doi:10.3390/life14070822. This article has 16 citations.

2. (ellington2025thegeneticdeterminants pages 19-20): Adam J. Ellington, Tyler J. Schult, Christopher R. Reisch, and Brent C. Christner. The genetic determinants of extreme uv radiation and desiccation tolerance in a bacterium recovered from the stratosphere. Microorganisms, 13:756, Mar 2025. URL: https://doi.org/10.3390/microorganisms13040756, doi:10.3390/microorganisms13040756. This article has 5 citations.

3. (nag2023genomicanalysisof pages 4-6): Sagorika Nag, Priya DasSarma, David J. Crowley, Rafael Hamawi, Samantha Tepper, Brian P. Anton, Daniel Guzmán, and Shiladitya DasSarma. Genomic analysis of haloarchaea from diverse environments, including permian halite, reveals diversity of ultraviolet radiation survival and dna photolyase gene variants. Microorganisms, 11:607, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030607, doi:10.3390/microorganisms11030607. This article has 9 citations.

4. (ellington2025thegeneticdeterminants pages 1-2): Adam J. Ellington, Tyler J. Schult, Christopher R. Reisch, and Brent C. Christner. The genetic determinants of extreme uv radiation and desiccation tolerance in a bacterium recovered from the stratosphere. Microorganisms, 13:756, Mar 2025. URL: https://doi.org/10.3390/microorganisms13040756, doi:10.3390/microorganisms13040756. This article has 5 citations.

5. (ellington2025thegeneticdeterminants pages 29-30): Adam J. Ellington, Tyler J. Schult, Christopher R. Reisch, and Brent C. Christner. The genetic determinants of extreme uv radiation and desiccation tolerance in a bacterium recovered from the stratosphere. Microorganisms, 13:756, Mar 2025. URL: https://doi.org/10.3390/microorganisms13040756, doi:10.3390/microorganisms13040756. This article has 5 citations.

6. (tunca2026dnarepairmechanisms pages 1-2): Hatice Tunca and Rümeysa Özkılıç. Dna repair mechanisms in algae. Journal of Limnology and Freshwater Fisheries Research, 12:13-21, Apr 2026. URL: https://doi.org/10.17216/limnofish.1792319, doi:10.17216/limnofish.1792319. This article has 0 citations.

7. (laughery2025illuminatinggenomerepair pages 1-3): Marian F. Laughery and John J. Wyrick. Illuminating genome repair by photolyase. Photochemistry and Photobiology, 102(2):362-369, Oct 2025. URL: https://doi.org/10.1111/php.70047, doi:10.1111/php.70047. This article has 2 citations and is from a peer-reviewed journal.

8. (singh2023resilienceandmitigation pages 11-13): Varsha K. Singh, Sapana Jha, Palak Rana, Sonal Mishra, Neha Kumari, Suresh C. Singh, Shekhar Anand, Vijay Upadhye, and Rajeshwar P. Sinha. Resilience and mitigation strategies of cyanobacteria under ultraviolet radiation stress. International Journal of Molecular Sciences, 24:12381, Aug 2023. URL: https://doi.org/10.3390/ijms241512381, doi:10.3390/ijms241512381. This article has 55 citations.

9. (nag2023genomicanalysisof pages 2-4): Sagorika Nag, Priya DasSarma, David J. Crowley, Rafael Hamawi, Samantha Tepper, Brian P. Anton, Daniel Guzmán, and Shiladitya DasSarma. Genomic analysis of haloarchaea from diverse environments, including permian halite, reveals diversity of ultraviolet radiation survival and dna photolyase gene variants. Microorganisms, 11:607, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030607, doi:10.3390/microorganisms11030607. This article has 9 citations.

10. (najjari2023physiologicalandgenomic pages 1-2): Afef Najjari, Ayoub Boussetta, Noha Youssef, Javier A. Linares-Pastén, Mouna Mahjoubi, Rahma Belloum, Haitham Sghaier, Ameur Cherif, and Hadda Imene Ouzari. Physiological and genomic insights into abiotic stress of halophilic archaeon natrinema altunense 4.1r isolated from a saline ecosystem of tunisian desert. Genetica, 151:133-152, Feb 2023. URL: https://doi.org/10.1007/s10709-023-00182-0, doi:10.1007/s10709-023-00182-0. This article has 5 citations and is from a peer-reviewed journal.

11. (casero2024effectofsalinity pages 1-2): María Cristina Casero, María Ángeles Herrero, Juan Pablo De la Roche, Antonio Quesada, David Velázquez, and Samuel Cirés. Effect of salinity on scytonemin yield in endolithic cyanobacteria from the atacama desert. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-60499-4, doi:10.1038/s41598-024-60499-4. This article has 13 citations and is from a peer-reviewed journal.

12. (casero2024effectofsalinity pages 2-3): María Cristina Casero, María Ángeles Herrero, Juan Pablo De la Roche, Antonio Quesada, David Velázquez, and Samuel Cirés. Effect of salinity on scytonemin yield in endolithic cyanobacteria from the atacama desert. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-60499-4, doi:10.1038/s41598-024-60499-4. This article has 13 citations and is from a peer-reviewed journal.

13. (nag2023genomicanalysisof pages 1-2): Sagorika Nag, Priya DasSarma, David J. Crowley, Rafael Hamawi, Samantha Tepper, Brian P. Anton, Daniel Guzmán, and Shiladitya DasSarma. Genomic analysis of haloarchaea from diverse environments, including permian halite, reveals diversity of ultraviolet radiation survival and dna photolyase gene variants. Microorganisms, 11:607, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030607, doi:10.3390/microorganisms11030607. This article has 9 citations.

14. (singh2023resilienceandmitigation pages 9-11): Varsha K. Singh, Sapana Jha, Palak Rana, Sonal Mishra, Neha Kumari, Suresh C. Singh, Shekhar Anand, Vijay Upadhye, and Rajeshwar P. Sinha. Resilience and mitigation strategies of cyanobacteria under ultraviolet radiation stress. International Journal of Molecular Sciences, 24:12381, Aug 2023. URL: https://doi.org/10.3390/ijms241512381, doi:10.3390/ijms241512381. This article has 55 citations.

15. (wang2025naturalantioxidantsderived pages 5-7): Yushu Wang and Gang Ma. Natural antioxidants derived from microalgae and cyanobacteria and their applications in skincare. Blue Biotechnology, Dec 2025. URL: https://doi.org/10.1186/s44315-025-00050-w, doi:10.1186/s44315-025-00050-w. This article has 0 citations.