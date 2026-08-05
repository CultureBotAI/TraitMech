---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:59:53.611714'
end_time: '2026-08-04T05:14:49.065041'
duration_seconds: 895.45
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: genomic island
  trait_identifier: traitmech:000093
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: genomic_island
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A genomics trait describing possession of a genomic island \u2014 a\
    \ horizontally acquired chromosomal region (e.g. a pathogenicity, symbiosis, or\
    \ metabolic island) that often retains mobility signatures such as flanking repeats\
    \ and atypical nucleotide composition."
  parent_traits: traitmech:000089
  synonyms: pathogenicity island
  evidence_summary: 'DOI:10.1038/nrmicro884:  (Dobrindt et al. review genomic islands
    in pathogenic and environmental microorganisms.) | DOI:10.1111/j.1574-6976.2008.00136.x:  (Juhas
    et al. review genomic islands as tools of bacterial horizontal gene transfer and
    evolution.)'
  causal_graph_summary: 'gi_hgt_accessory_function: 8 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** genomic island
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000093
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of a genomic island — a horizontally acquired chromosomal region (e.g. a pathogenicity, symbiosis, or metabolic island) that often retains mobility signatures such as flanking repeats and atypical nucleotide composition.
- **Parent traits:** traitmech:000089
- **Synonyms:** pathogenicity island
- **Existing evidence:** DOI:10.1038/nrmicro884:  (Dobrindt et al. review genomic islands in pathogenic and environmental microorganisms.) | DOI:10.1111/j.1574-6976.2008.00136.x:  (Juhas et al. review genomic islands as tools of bacterial horizontal gene transfer and evolution.)
- **Existing causal graph summary:** gi_hgt_accessory_function: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **genomic island** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/genomic_island.yaml`.

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
- **Trait label:** genomic island
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000093
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of a genomic island — a horizontally acquired chromosomal region (e.g. a pathogenicity, symbiosis, or metabolic island) that often retains mobility signatures such as flanking repeats and atypical nucleotide composition.
- **Parent traits:** traitmech:000089
- **Synonyms:** pathogenicity island
- **Existing evidence:** DOI:10.1038/nrmicro884:  (Dobrindt et al. review genomic islands in pathogenic and environmental microorganisms.) | DOI:10.1111/j.1574-6976.2008.00136.x:  (Juhas et al. review genomic islands as tools of bacterial horizontal gene transfer and evolution.)
- **Existing causal graph summary:** gi_hgt_accessory_function: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **genomic island** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/genomic_island.yaml`.

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


# Microbial Trait Causal Graph Curation Report
## Genomic Island (traitmech:000093)

---

## 1. Trait Scope and Definition

### 1.1 Core Phenotype

Possession of a **genomic island** represents the microbial capacity to harbor a horizontally acquired chromosomal segment—typically 10–200 kb in size—characterized by atypical nucleotide composition (e.g., divergent GC content) and flanked by mobility signatures such as direct repeats, integrase genes, and insertion near tRNA loci (watanabe2025theroleof pages 1-2). Genomic islands (GIs) confer accessory functions including virulence, antimicrobial/metal resistance, metabolic degradation capacity, symbiosis, or defense against phages and other genetic parasites (watanabe2025theroleof pages 1-2, watanabe2025theroleof pages 11-12, watanabe2025theroleof pages 12-13, watanabe2025theroleof pages 13-15).

### 1.2 Mechanistic Subclasses and Boundary Cases

- **Integrative and Conjugative Elements (ICEs)** are self-transmissible GIs encoding a complete suite of excision, conjugation, and integration machinery, enabling horizontal transfer between bacterial cells (watanabe2025theroleof pages 1-2, chai2025comprehensiveprofilingof pages 10-13, matsumoto2024evolutionofthe pages 1-3, matsumoto2024evolutionofthe pages 9-13). ICEs share features with conjugative plasmids but differ by chromosomal integration (watanabe2025theroleof pages 1-2).
  
- **Integrative and Mobilizable Elements (IMEs)** are similar but require co-resident transfer machinery (chai2025comprehensiveprofilingof pages 10-13). In Mollicutes, ICEs/IMEs account for 83.9% of genomes exhibiting horizontal gene transfer (HGT) signatures (chai2025comprehensiveprofilingof pages 10-13).

- **Pathogenicity Islands (PAIs)** are GIs whose cargo genes encode virulence factors such as type III secretion systems (T3SS), toxins (e.g., coronafacic acid, tabtoxin), adhesins, and invasion determinants (watanabe2025theroleof pages 11-12, watanabe2025theroleof pages 12-13, lyu2024theintricaterelationship pages 4-6, benevides2024genomicfeaturesand pages 1-2). All Salmonella Mbandaka ST413 strains carry 7 canonical Salmonella pathogenicity islands (SPIs 1–5, 9, and C63PI) conferring intracellular survival and virulence (benevides2024genomicfeaturesand pages 1-2).

- **Prophages** are integrated phage genomes that may be intact (capable of excision), incomplete, or questionable (vladimirova2024hotspotsof pages 1-2, vladimirova2024hotspotsof pages 20-21). In *Sinorhizobium meliloti*, 314 phage-related sequences (PRSs) ranging from 3.24 kb to 88.98 kb collectively represent 6.30 Mb of foreign DNA, with more than 53% of this integrated into tRNA genes on chromosomes (vladimirova2024hotspotsof pages 1-2).

- **Defense Islands** cluster anti-phage/anti-MGE systems. Analysis of 7,759 bacterial metagenome-assembled genomes (MAGs) from soil, marine, and human gut environments identified 43,263 complete defense systems and 764,507 defense genes across 70 families, with highly variable genetic mobility and frequent clustering in defense islands (beavogui2024thedefensomeof pages 8-9, beavogui2024thedefensomeof pages 1-2).

**Boundary clarification**: A GI is *functionally* defined by its horizontally acquired nature and chromosomal integration, rather than by a specific size threshold or GC skew. Atypical nucleotide composition, direct repeats, integrase genes, and tRNA insertion sites are *diagnostic evidence* of HGT origin but are not individually necessary or sufficient (watanabe2025theroleof pages 1-2, mageeney2020newcandidatesfor pages 12-13).

### 1.3 Diagnostic Molecular Signatures

- **Integrase and excisionase genes** (tyrosine recombinases or serine integrases) mediate site-specific recombination (watanabe2025theroleof pages 1-2, vladimirova2024hotspotsof pages 1-2, vladimirova2024hotspotsof pages 20-21).
- **attL and attR sites** flank integrated elements; excision regenerates attP (on circular element) and attB (on chromosome) (watanabe2025theroleof pages 1-2, matsumoto2024evolutionofthe pages 1-3, matsumoto2024evolutionofthe pages 9-13).
- **Direct repeats (DRs)** of 9–23 bp typically mark integration boundaries (chai2025comprehensiveprofilingof pages 10-13, matsumoto2024evolutionofthe pages 1-3).
- **tRNA gene insertion hotspots**: In *S. meliloti*, 28% of PRSs integrated into tRNA genes, with tRNA^Thr(GGU), tRNA^Asn(GUU), and tRNA^Lys(CUU) as recurrent "hot spots"; integrated elements often encode a replacement tRNA isoacceptor (vladimirova2024hotspotsof pages 1-2, vladimirova2024hotspotsof pages 20-21).
- **Origin of transfer (oriT)** and **relaxase genes (traI)** mark conjugative capacity (chai2025comprehensiveprofilingof pages 10-13, matsumoto2024evolutionofthe pages 1-3, matsumoto2024evolutionofthe pages 9-13).

---

## 2. Candidate Causal Graph Entities

### 2.1 Molecular Machinery (Proteins and Complexes)

| Entity Label | Suggested CURIE (if stable) | Function |
|---|---|---|
| Integrase (Int) | GO:0015074 (DNA integration) | Catalyzes site-specific recombination at attL/attR or attP/attB |
| Excisionase (Xis) | — | Accessory factor for ICE excision; upregulated 80-fold by TraR in Tn4371 ICE (matsumoto2024evolutionofthe pages 9-13) |
| Relaxase (TraI) | GO:0003918 (DNA topoisomerase type I activity) | Nicks DNA at oriT, forms relaxosome |
| Coupling protein (TraG) | — | Delivers relaxase-ssDNA complex to T4SS |
| Type IV secretion system (T4SS / MPF) | GO:0030254 (protein secretion by the type IV secretion system) | Exports ssDNA-relaxase complex into recipient cell |
| TraR regulator | — | LysR-type transcriptional regulator; activates xis expression and ICE transfer (matsumoto2024evolutionofthe pages 1-3, matsumoto2024evolutionofthe pages 9-13) |
| CopR, CusR, CzcR response regulators | — | Copper/zinc two-component regulators; cross-regulate ICE-encoded pcoA2 operon (elsen2024crossregulationandcrosstalk pages 1-2, elsen2024crossregulationandcrosstalk pages 13-14) |
| CadX repressor | — | ArsR-family Cd²⁺-responsive regulator; binds cadDX promoter (zhu2024thecaddxoperon pages 1-2, zhu2024thecaddxoperon pages 9-13) |
| Topoisomerase IIIb (PbTopo IIIb) | — | Regulates GI stability and maintenance; inactivation causes hyper-excision (watanabe2025theroleof pages 12-13) |

### 2.2 Genetic Loci and Recombination Sites

| Entity | CURIE candidate | Notes |
|---|---|---|
| attL, attR | — | Flanking sites on integrated ICE |
| attP | — | Attachment site on circular ICE |
| attB | — | Chromosomal target site (often in tRNA genes) |
| oriT (origin of transfer) | — | 132 bp in Mollicutes ICE-3 (chai2025comprehensiveprofilingof pages 10-13); 463 bp in Tn4371 (matsumoto2024evolutionofthe pages 9-13) |
| Direct repeats (DR) | — | 9–23 bp flanking ICE (chai2025comprehensiveprofilingof pages 10-13, matsumoto2024evolutionofthe pages 1-3) |

### 2.3 Cargo Genes and Phenotypes

| Cargo gene / operon | Function | CURIE candidate |
|---|---|---|
| cadDX | Cadmium efflux (P-type ATPase CadD) + transcriptional repressor (CadX) | — |
| cusRS-pcoA2 | Copper homeostasis: CusRS two-component system, pcoA2 nine-gene operon | — |
| bph operon | Biphenyl/PCB degradation pathway | — |
| Type III secretion system (T3SS) effectors | Virulence: avrPphB, hopF1, hopT1, hopO1, hopQ, hopD, hopAR1 | GO:0030254? |
| Tabtoxin biosynthetic cluster | Phytotoxin biosynthesis | — |
| DctT transporter | Dicarboxylate transport | — |
| FeoAB system | Ferrous iron transport | GO:0015093 (ferrous iron transmembrane transporter activity) |
| tet(M), tetACDR | Tetracycline resistance | — |
| mer operon | Mercury resistance | — |
| Defense systems (CRISPR-Cas, R-M, Gabija, CBASS, etc.) | Anti-phage/anti-MGE immunity | various GO / specific tools |

### 2.4 Environmental and Regulatory Factors

| Factor | Role |
|---|---|
| Copper ion (Cu²⁺) | Induces CusRS and CopRS regulons; stimulates pcoA2 operon expression (elsen2024crossregulationandcrosstalk pages 1-2, elsen2024crossregulationandcrosstalk pages 13-14) |
| Cadmium ion (Cd²⁺) | De-represses cadDX; confers resistance (MIC increase ~1000-fold in *S. aureus*) (zhu2024thecaddxoperon pages 1-2) |
| Hydrogen peroxide (H₂O₂) | Oxidative stress; cadX responds via additional promoter (zhu2024thecaddxoperon pages 1-2, zhu2024thecaddxoperon pages 9-13) |
| UV light, mitomycin C | Induce prophage excision (watanabe2025theroleof pages 13-15) |
| Host immune factors | In planta stress increases GI excision frequency (watanabe2025theroleof pages 11-12) |
| Aromatic compounds (biphenyl, PCB) | Induce bph operon; TraR co-transcribed with bph genes (matsumoto2024evolutionofthe pages 1-3, matsumoto2024evolutionofthe pages 9-13) |

---

## 3. Evidence-Backed Causal Edges

| Subject | Predicate | Object | Evidence strength/context | DOI |
|---|---|---|---|---|
| Integrase + excisionase (xis) | mediates recombination between | attL and attR sites | Strong, mechanistic ICE transfer model; general ICE mechanism described from validated systems (matsumoto2024evolutionofthe pages 1-3) | 10.1128/spectrum.00607-24 |
| attL/attR recombination | generates | attP on circular ICE and attB on chromosome | Strong, mechanistic consequence of excision; general ICE model (matsumoto2024evolutionofthe pages 1-3) | 10.1128/spectrum.00607-24 |
| Relaxase (TraI) bound at oriT | nicks and forms relaxosome on | ICE DNA for transfer initiation | Strong, mechanistic ICE conjugation step; general transfer model (matsumoto2024evolutionofthe pages 1-3) | 10.1128/spectrum.00607-24 |
| TraG coupling protein + MPF/T4SS | transfers | relaxase-bound ssDNA to recipient cell | Strong, mechanistic ICE conjugation step; general transfer model (matsumoto2024evolutionofthe pages 1-3) | 10.1128/spectrum.00607-24 |
| Integrase | integrates | circular ICE DNA into recipient chromosome | Strong, mechanistic ICE lifecycle step; general transfer model (matsumoto2024evolutionofthe pages 1-3) | 10.1128/spectrum.00607-24 |
| TraR | upregulates | xis expression | Strong, perturbation-backed in Tn4371-family ICE: xis increased 80-fold after traR induction; taxon-specific assay in Acidovorax sp. KKS102 (matsumoto2024evolutionofthe pages 1-3, matsumoto2024evolutionofthe pages 9-13) | 10.1128/spectrum.00607-24 |
| TraR overexpression | increases | ICE excision and transfer frequency | Strong, perturbation-backed; qPCR/mating assays in Tn4371-family ICE; taxon-specific (matsumoto2024evolutionofthe pages 1-3, matsumoto2024evolutionofthe pages 9-13) | 10.1128/spectrum.00607-24 |
| cadDX operon | contributes to | cadmium resistance | Strong, gene-function study in Streptococcus suis and transfer into S. agalactiae; cargo phenotype on mobilizable element; taxon-specific (zhu2024thecaddxoperon pages 1-2, zhu2024thecaddxoperon pages 9-13) | 10.1186/s13567-024-01371-1 |
| cadDX operon | contributes to | oxidative-stress resistance and virulence | Strong, mutant/complementation and heterologous-transfer evidence in zoonotic streptococci; taxon-specific (zhu2024thecaddxoperon pages 1-2, zhu2024thecaddxoperon pages 9-13) | 10.1186/s13567-024-01371-1 |
| cusRS-pcoA2 locus on an ICE | provides resistance to | elevated extracellular copper | Strong, mutagenesis/transcriptional fusion/copper phenotype study in Pseudomonas paraeruginosa clinical isolate; ICE-encoded accessory copper response; taxon-specific (elsen2024crossregulationandcrosstalk pages 1-2, elsen2024crossregulationandcrosstalk pages 13-14) | 10.1371/journal.pgen.1011325 |
| Genomic-island accessory metabolic genes | enables degradation of | aromatic compounds / toxic chemicals | Strong for Bordetella petrii genomic islands, including clc-like ICEs encoding accessory metabolic functions; phenotype/genome correlation, partly taxon-specific (lechner2009genomicislandexcisions pages 1-2) | 10.1186/1471-2180-9-141 |


*Table: This table compiles the strongest candidate causal edges for the genomic-island trait, emphasizing core ICE lifecycle mechanisms and experimentally supported cargo-gene phenotypes. It is useful as a compact curation artifact for selecting high-confidence edges for TraitMech.*

### 3.1 Core Mechanistic Edges (General ICE/IME Lifecycle)

**Edge 1**: `integrase + excisionase (xis)` → `mediates recombination` → `attL/attR sites`  
**Reference**: DOI:10.1128/spectrum.00607-24 (Matsumoto et al., *Microbiology Spectrum*, Oct 2024)  
**Snippet**: "Integrase (encoded by the int gene) with the aid of excisionase (encoded by the xis gene) mediates excision by catalyzing site-specific recombination between attL and attR, which are located at the left and right boundaries of ICE." (matsumoto2024evolutionofthe pages 1-3)  
**Notes**: General ICE mechanism; tyrosine or serine integrases described in SXT/R391, Tn4371, ICEclc families.  
**Certainty**: High; mechanistic model validated in multiple taxa.

**Edge 2**: `attL/attR recombination` → `generates` → `attP (on circular ICE) + attB (on chromosome)`  
**Reference**: DOI:10.1128/spectrum.00607-24  
**Snippet**: "A set of two sites, attP and attB, are generated by the recombination: attP is on a plasmid-like circular molecule, and attB is on a chromosome." (matsumoto2024evolutionofthe pages 1-3)  
**Notes**: Canonical outcome of ICE excision; circular intermediates detected by PCR for all but GI5 in *Bordetella petrii* (lechner2009genomicislandexcisions pages 1-2).  
**Certainty**: High.

**Edge 3**: `relaxase (TraI) at oriT` → `nicks DNA and forms relaxosome` → `ssDNA–relaxase complex`  
**Reference**: DOI:10.1128/spectrum.00607-24  
**Snippet**: "oriT (origin of transfer) is recognized and nicked by relaxase (encoded by the traI gene) to form relaxosome, in which relaxase is covalently bound to the 5' end of DNA." (matsumoto2024evolutionofthe pages 1-3)  
**Notes**: Rolling-circle replication generates ssDNA substrate for transfer. Validated across conjugative plasmids and ICEs.  
**Certainty**: High.

**Edge 4**: `TraG coupling protein + T4SS (MPF)` → `exports` → `ssDNA–relaxase complex into recipient cell`  
**Reference**: DOI:10.1128/spectrum.00607-24  
**Snippet**: "The DNA-relaxase complex is passed to the MPF system by the function of the coupling protein (encoded by traG)." (matsumoto2024evolutionofthe pages 1-3)  
**Notes**: General conjugation mechanism; T4SS components are conserved in ICE families including Tn4371 and SXT/R391.  
**Certainty**: High.

**Edge 5**: `integrase in recipient cell` → `integrates` → `circular ICE DNA into chromosome`  
**Reference**: DOI:10.1128/spectrum.00607-24  
**Snippet**: "In the recipient cell, the imported DNA is recircularized, reverts back to double-stranded DNA, and is then integrated into the chromosome by the integrase." (matsumoto2024evolutionofthe pages 1-3)  
**Notes**: Site-specific integration commonly targets tRNA genes (attB sites). In *S. meliloti*, integration occurred at 28% of tRNA genes, with tRNA^Thr, tRNA^Asn, tRNA^Lys as hot spots (vladimirova2024hotspotsof pages 1-2, vladimirova2024hotspotsof pages 20-21).  
**Certainty**: High.

### 3.2 Regulatory and Induction Edges

**Edge 6**: `TraR (LysR-type regulator)` → `upregulates` → `xis expression`  
**Reference**: DOI:10.1128/spectrum.00607-24 (Matsumoto et al., Oct 2024)  
**Snippet**: "its overexpression on solid medium resulted in modest upregulation of traG (threefold), marked upregulation of xis (80-fold), enhanced ICE excision and, most notably, ICE transfer frequency." (matsumoto2024evolutionofthe pages 1-3); "the transcription level of xis showed the greatest increase, i.e., 80-fold, by traR induction." (matsumoto2024evolutionofthe pages 9-13)  
**Notes**: Taxon-specific (Tn4371-family ICE in Acidovorax sp. KKS102); TraR is conserved across Tn4371 βγ-type ICEs. Experimentally validated by qRT-PCR and mating assays.  
**Certainty**: High (perturbation evidence); taxon = Tn4371 family, primarily β/γ-proteobacteria.

**Edge 7**: `TraR overexpression` → `increases` → `ICE excision frequency + ICE transfer frequency`  
**Reference**: DOI:10.1128/spectrum.00607-24  
**Snippet**: "traR overexpression... enhanced ICE excision... ICE transfer frequency"; transfer frequency from SA10 = 1.9 × 10⁻³ under traR induction (matsumoto2024evolutionofthe pages 9-13)  
**Notes**: Baseline ICE transfer in KKS102 is ~10⁻¹⁰ per donor; TraR induction raises it >10⁶-fold. Perturbation assay; Tn4371-specific.  
**Certainty**: High (experimental); limited to Tn4371-like ICEs.

**Edge 8**: `In planta stress from host resistance factors` → `increases` → `GI excision frequency`  
**Reference**: DOI:10.3390/microorganisms13081803 (Watanabe et al., Aug 2025)  
**Snippet**: "Excision frequency increases under in planta stress from host resistance factors." (watanabe2025theroleof pages 11-12)  
**Notes**: Observed in plant-pathogenic *Pseudomonas syringae* GIs. Mechanism unclear; stress-responsive regulation hypothesized.  
**Certainty**: Moderate (association documented; molecular mechanism incomplete); taxon-specific (plant pathogens).

### 3.3 Cargo-Gene to Phenotype Edges

**Edge 9**: `cadDX operon` → `confers` → `cadmium resistance`  
**Reference**: DOI:10.1186/s13567-024-01371-1 (Zhu et al., *Veterinary Research*, Sep 2024)  
**Snippet**: "cadDX contributes to cadmium resistance"; MIC increase ~1000-fold in *S. aureus* (zhu2024thecaddxoperon pages 1-2); "the growth of S. agalactiae-cadD and S. agalactiae-cadDX were notably greater than those of S. agalactiae-pSET2 and S. agalactiae-cadX" under 15 µM CdCl₂ (zhu2024thecaddxoperon pages 9-13)  
**Notes**: cadDX within 11 kb integrative mobilizable element in *Streptococcus suis*; confirmed by heterologous transfer into *S. agalactiae*; wide distribution across gram-positive bacteria. CadD = P-type ATPase efflux pump; CadX = ArsR-family repressor.  
**Certainty**: High (mutant/complementation + heterologous expression); taxon-validated in streptococci.

**Edge 10**: `cadDX operon` → `confers` → `oxidative-stress resistance + increased virulence`  
**Reference**: DOI:10.1186/s13567-024-01371-1  
**Snippet**: "cadDX contributes to... oxidative stress resistance, and virulence"; "the survival rates of S. agalactiae-cadX and S. agalactiae-cadDX increased under H₂O₂ conditions" (zhu2024thecaddxoperon pages 9-13); bacterial load in blood/brain/kidney/liver significantly greater in ΔCRISPRS.a-cadDX vs. ΔCRISPRS.a-pSET2 infection (zhu2024thecaddxoperon pages 9-13)  
**Notes**: CadX responds to H₂O₂ via additional promoter within cadDX operon; FeoA downregulation implicated in oxidative-stress protection. Mouse infection model demonstrates increased bacterial persistence.  
**Certainty**: High (genetic and infection assays); taxon = zoonotic streptococci.

**Edge 11**: `cusRS-pcoA2 locus on ICE` → `confers` → `resistance to elevated extracellular copper`  
**Reference**: DOI:10.1371/journal.pgen.1011325 (Elsen et al., *PLOS Genetics*, Jun 2024)  
**Snippet**: "the accessory CusRS two-component system (TCS) responds to copper and activates both its own expression and that of the adjacent nine-gene operon (the pcoA2 operon) to provide resistance to elevated levels of extracellular copper." (elsen2024crossregulationandcrosstalk pages 1-2)  
**Notes**: The cusRS-pcoA2 locus is part of an ICE in *Pseudomonas paraeruginosa* clinical isolate. Cross-regulation by core-genome CopRS and CzcRS systems demonstrates integration of horizontally acquired regulon into endogenous network. Validated by mutagenesis, transcriptional fusions, and copper-sensitivity phenotyping.  
**Certainty**: High (perturbation + phenotype assays); taxon = *Pseudomonas paraeruginosa*.

**Edge 12**: `GI accessory metabolic genes (e.g., clc-like ICEs)` → `enable` → `degradation of aromatic compounds (e.g., 3-chlorobenzoate, PCB, biphenyl)`  
**Reference**: DOI:10.1186/1471-2180-9-141 (Lechner et al., *BMC Microbiology*, Jul 2009)  
**Snippet**: "These elements mainly encode accessory metabolic factors enabling this bacterium to grow on a large repertoire of aromatic compounds." (lechner2009genomicislandexcisions pages 1-2)  
**Notes**: GI1-GI3 in *Bordetella petrii* homologous to ICEclc; cargo genes include degradation pathways for xenobiotics. GI3 self-transmissible and lost within ~100 generations post-tetracycline-cassette insertion, indicating instability. Bph operon in Tn4371 ICE confers biphenyl degradation (matsumoto2024evolutionofthe pages 1-3).  
**Certainty**: High (genome annotation + phenotype correlation); environmental/non-pathogenic bacteria.

**Edge 13**: `Pathogenicity island cargo (T3SS, toxins, adhesins)` → `confers` → `intracellular survival + virulence`  
**Reference**: DOI:10.3390/microorganisms13081803 (Watanabe et al., Aug 2025); DOI:10.3390/microorganisms12020312 (Benevides et al., Feb 2024)  
**Snippet**: Plant-pathogenic GIs carry "secretion systems, toxins, and invasion enzymes" (watanabe2025theroleof pages 1-2); "HAI2 in P. atrosepticum synthesizes coronafacic acid (CFA) virulence factor; HAI8 associates with type III secretion systems" (watanabe2025theroleof pages 12-13); Salmonella Mbandaka carries "SPIs 1-5, 9, and C63PI... involved in intracellular survival and virulence" (benevides2024genomicfeaturesand pages 1-2)  
**Notes**: Broadly observed across pathogenic bacteria; mechanistic details vary by pathogen. Cargo-gene composition is taxon-specific, but functional category (virulence) is conserved.  
**Certainty**: High (well-established across multiple pathogens).

---

## 4. Ontology Grounding Suggestions

**Conservatively mapped CURIEs** (only where stable and widely accepted):

- **GO:0015074** (DNA integration) – integrase activity
- **GO:0003918** (DNA topoisomerase type I activity) – relaxase
- **GO:0030254** (protein secretion by the type IV secretion system) – T4SS/MPF
- **GO:0015093** (ferrous iron transmembrane transporter activity) – FeoAB

**Label-only candidates** (stable identifiers not yet established or ambiguous):

- Excisionase (Xis), TraR, CopR, CusR, CzcR, CadX, cadDX operon, cusRS-pcoA2 locus, bph operon, attL, attR, attP, attB, oriT, direct repeats, tabtoxin biosynthetic cluster, topoisomerase IIIb, defense islands

**Recommendations**:

- Query GO, CHEBI, KEGG, MetaCyc, UniProt for specific gene products once TraitMech curators determine grounding precision requirements.
- For ICE-specific entities (e.g., TraR, Xis), consider minting custom TraitMech identifiers if no broadly accepted stable URI exists.

---

## 5. Recent Developments and Quantitative Data (2023–2024)

### 5.1 Mollicutes ICE/IME Profiling (2025)

Comprehensive screening of 1,433 Mollicutes genomes revealed 263 ICEs/IMEs, showing strong correlation (r = 0.573, p = 0.002) with HGT frequency (chai2025comprehensiveprofilingof pages 10-13). ICEs/IMEs are intact or fragmented and drive gene shuttling; Ureaplasma ICE facilitates tet(M) spread to human pathogens (*Streptococcus pneumoniae*, *Staphylococcus aureus*, *Enterococcus faecium*) with >99.8% identity.

### 5.2 Tn4371-Family ICE Regulation (2024)

TraR (LysR-type regulator) induces xis expression 80-fold, traG expression 3-fold, and elevates ICE excision/transfer frequency by orders of magnitude in Acidovorax sp. KKS102 (matsumoto2024evolutionofthe pages 1-3, matsumoto2024evolutionofthe pages 9-13). Baseline transfer = ~10⁻¹⁰; TraR-induced transfer = 1.9 × 10⁻³.

### 5.3 Bacterial Defensome in Environmental MAGs (2024)

Analysis of 7,759 high-quality MAGs from soil, marine, and human gut environments identified 43,263 complete defense systems and 764,507 defense genes across 70 families (beavogui2024thedefensomeof pages 8-9, beavogui2024thedefensomeof pages 1-2). Defensomes vary by phylum, lifestyle, genome size, habitat, and geography. Defense islands (DIs) cluster multiple systems; genetic mobility and variability are system-specific and shaped by environment.

### 5.4 Sinorhizobium meliloti tRNA Integration Hot Spots (2024)

Among 314 PRSs (3.24–88.98 kb) in 27 *S. meliloti* strains, 28% integrated into tRNA genes, representing 53.5% of total foreign DNA (6.30 Mb cumulative). tRNA^Thr(GGU), tRNA^Asn(GUU), and tRNA^Lys(CUU) are preferential integration hot spots; integrated elements often carry replacement tRNA isoacceptor genes homologous to distant taxa (vladimirova2024hotspotsof pages 1-2, vladimirova2024hotspotsof pages 20-21).

### 5.5 cadDX Cargo Distribution (2024)

The cadDX operon resides in diverse MGEs across gram-positive bacteria, especially pathogenic streptococci (*S. suis*, *S. agalactiae*); detected in plasmids, ICEs, IMEs, and prophages (zhu2024thecaddxoperon pages 1-2, zhu2024thecaddxoperon pages 9-13). Transfer of cadDX into *S. agalactiae* conferred cadmium/oxidative-stress resistance and increased bacterial load in blood, brain, kidney, liver in murine infection.

### 5.6 Salmonella Mbandaka ST413 Epidemiology (2024)

Brazilian *S. Mbandaka* ST413 strains carry 7 SPIs (1–5, 9, C63PI), Salmonella genomic island 1 (SGI1) in 4/6 strains, and an IncHI2A plasmid (112,960 bp) harboring tet and mer genes (benevides2024genomicfeaturesand pages 1-2). Phylogenetic clustering with European outbreak strains indicates global dissemination potential.

---

## 6. Current Applications and Real-World Implementations

### 6.1 Epidemiological Surveillance and Source Attribution

Whole-genome sequencing identifies GI-driven transmission routes in foodborne and zoonotic pathogens. *S. Mbandaka* ST413 multi-country outbreak in EU/EEA linked to poultry meat (196 cases, 19 hospitalizations, 1 death, 2023–2024 outbreak) demonstrates GI-based virulence persistence (benevides2024genomicfeaturesand pages 1-2).

### 6.2 Environmental Bioremediation

ICE-encoded aromatic-degradation pathways (e.g., clc-like elements in *Bordetella petrii*, bph operons in Tn4371 ICE) enable microbial degradation of PCBs, biphenyl, and chlorinated aromatics (lechner2009genomicislandexcisions pages 1-2, matsumoto2024evolutionofthe pages 1-3). Transfer of catabolic GIs expands host metabolic repertoire for environmental cleanup.

### 6.3 Agricultural Microbiology and Symbiosis

*Sinorhizobium meliloti* GIs and prophages contribute to symbiotic nitrogen fixation and stress adaptation (vladimirova2024hotspotsof pages 1-2, vladimirova2024hotspotsof pages 20-21). tRNA-replacement by phage-encoded isoacceptors may enhance translation efficiency under specific environmental stresses.

### 6.4 Antimicrobial Resistance Management

ICE-mediated transfer of tet(M) among Mollicutes and to *Staphylococcus*, *Streptococcus*, *Enterococcus* pathogens (chai2025comprehensiveprofilingof pages 10-13) and IncHI2A plasmid-borne tet/mer genes in Salmonella (benevides2024genomicfeaturesand pages 1-2) highlight GI/ICE roles in resistance dissemination. Targeting ICE transfer machinery (e.g., TraR, T4SS) represents a potential intervention strategy.

### 6.5 Phage Therapy and Anti-Defense Strategies

Defense-island mapping informs phage-therapy design by predicting bacterial immune barriers (beavogui2024thedefensomeof pages 8-9, beavogui2024thedefensomeof pages 1-2). Solitary defense genes (incomplete systems) may retain activity, complicating treatment.

### 6.6 Bioinformatic Prediction and Validation

- **IslandViewer 4**: Predicts GIs by composition, comparative genomics, and integrase markers (benevides2024genomicfeaturesand pages 1-2, ramesh2024genomesequencingand pages 1-2).
- **TIGER**: Maps integrative genetic elements with precision, recovering regulated gene integrity (RGI) cases and identifying site-promiscuous integrases (mageeney2020newcandidatesfor pages 12-13). **Limitation**: Misses non-tyrosine/serine integrases (e.g., phage Mu), integrases deleted from multi-int elements, and scaffolded genomes (mageeney2020newcandidatesfor pages 12-13).
- **PHASTER / PHASTEST**: Annotate prophages; used in *S. meliloti* PRS survey (vladimirova2024hotspotsof pages 1-2).
- **DefenseFinder**: Identifies complete/incomplete defense systems in MAGs (beavogui2024thedefensomeof pages 8-9).

---

## 7. Expert Opinions and Analytical Interpretation

### 7.1 Evolutionary Plasticity and Adaptive Advantage

**Watanabe et al. (2025)**: "GIs function by transferring clusters of functionally linked genes—including toxins, secretion systems, resistance determinants, and metabolic pathways—enabling rapid phenotypic changes associated with host specialization and immune evasion." (watanabe2025theroleof pages 15-17).

**Matsumoto et al. (2024)**: "This property of ICE, i.e., undergoing transfer under environmental conditions that lead to cargo gene activation, would instantly confer fitness advantages to bacteria newly acquiring this ICE, thereby resulting in efficient dissemination of the Tn4371 family ICEs." (matsumoto2024evolutionofthe pages 1-3).

### 7.2 Integration of Acquired Regulons into Endogenous Networks

**Elsen et al. (2024)**: "The results presented here illustrate how acquired genetic elements can become part of endogenous regulatory networks, providing a physiological advantage. They also highlight the potential for broader effects of accessory regulatory proteins through interference with core regulatory proteins." Cross-talk between ICE-encoded CusRS and chromosomal CopRS ensures copper homeostasis despite distinct signaling mechanisms (elsen2024crossregulationandcrosstalk pages 1-2, elsen2024crossregulationandcrosstalk pages 13-14).

### 7.3 Prophage "Grounding" and GI Evolution

**Vladimirova et al. (2024)**: "The data are consistent with the previously proposed theory of the 'life cycle' of GIs, as well as with the theory of the 'grounding' of prophages in the bacterial genome. However, the presented data also demonstrate an active 'washout' of phage genes from bacterial genomes, which is apparently associated with the action of host bacterial defense systems." Prophage-to-GI transition reflects erosion of mobility genes while retaining cargo (vladimirova2024hotspotsof pages 1-2, vladimirova2024hotspotsof pages 20-21).

### 7.4 Defense-Island Co-evolution

**Beavogui et al. (2024)**: "The defensome's genetic mobility, its clustering in defense islands, and genetic variability was found to be system-specific and shaped by the bacterial environment." (beavogui2024thedefensomeof pages 8-9). High SNP + indel density in defense genes (dolB, mzaA, sspH) reflects ongoing arms race with phages/MGEs.

### 7.5 Computational Prediction Caveats

**Mageeney et al. (2020)**: "Certain IGE categories are missed, including those encoding integrases from other protein families (e.g., phage Mu); integrases may be deleted from multi-int IGEs, preventing accurate site-specificity mapping; and missing IGEs occur when elements are split across genome scaffolds." (mageeney2020newcandidatesfor pages 12-13). Manual curation and experimental validation remain essential.

---

## 8. Curation Warnings and Uncertain Claims

### 8.1 Do Not Curate as Universal Edges

- **Computational co-localization** of virulence/AMR genes in predicted GIs (e.g., IslandViewer results) establishes **association**, not causation. Experimental validation is required before asserting cargo-to-phenotype edges (benevides2024genomicfeaturesand pages 1-2, ramesh2024genomesequencingand pages 1-2).
  
- **G-quadruplex (G4) structures** in PAIs show non-random distribution and correlation with GC content (lyu2024theintricaterelationship pages 4-6), but mechanistic role in integration, expression, or mobility is speculative. Reserve for future investigation.

- **Tandem ICE integration** may incorporate core-genome DNA into composite islands (lechner2009genomicislandexcisions pages 1-2). Boundaries of such chimeric elements are difficult to define; mark as uncertain.

### 8.2 Taxon- or Assay-Specific Evidence (Mark Explicitly)

- **TraR-xis-transfer regulation**: Validated only for Tn4371-family ICEs in β/γ-proteobacteria; not confirmed in SXT/R391, ICEclc, or other ICE families (matsumoto2024evolutionofthe pages 1-3, matsumoto2024evolutionofthe pages 9-13).
  
- **cadDX phenotypes**: Demonstrated in zoonotic streptococci (*S. suis*, *S. agalactiae*); cadDX in *S. salivarius* and *S. lugdunensis* shows similar Cd²⁺ resistance but oxidative-stress/virulence roles not tested in those hosts (zhu2024thecaddxoperon pages 1-2, zhu2024thecaddxoperon pages 9-13).

- **tRNA isoacceptor replacement**: Observed in *S. meliloti* and *Mycobacterium* but generalization to other taxa requires validation (vladimirova2024hotspotsof pages 1-2, vladimirova2024hotspotsof pages 20-21).

### 8.3 Incomplete Mechanistic Understanding

- **In planta stress → GI excision**: Documented in *P. syringae* but molecular sensor/regulator unidentified (watanabe2025theroleof pages 11-12).
  
- **Topoisomerase IIIb stability regulation**: PbTopo IIIb knockout → hyper-excision in *Pectobacterium atrosepticum* (watanabe2025theroleof pages 12-13), but direct substrates and mechanism unclear.

- **Defense-island genetic variability**: High SNP/indel density suggests diversifying selection, but specific phage counter-defenses or evolutionary drivers remain hypothetical (beavogui2024thedefensomeof pages 8-9).

### 8.4 Boundary Ambiguities

- **Prophage vs. GI**: Prophages with extensive bacterial gene acquisition may lack canonical phage structural genes; conversely, GIs may retain defunct integrase/excisionase genes. Functional classification (mobility capacity) preferred over compositional thresholds (vladimirova2024hotspotsof pages 1-2).

- **ICE vs. IME**: Distinction based on conjugative autonomy; IMEs require trans-acting transfer machinery, but mosaic ICEs (e.g., Mollicutes bifurcated ICE-3) blur this boundary (chai2025comprehensiveprofilingof pages 10-13).

---

## 9. DOI-First Bibliography

1. **Watanabe Y, Ishiga Y, Sakata N** (Aug 2025). The Role of Genomic Islands in the Pathogenicity and Evolution of Plant-Pathogenic Gammaproteobacteria. *Microorganisms* 13(8):1803. DOI:10.3390/microorganisms13081803  
2. **Chai Z, Guo Z, Chen X, Yang Z, Wang X, Zhang F, Kang F, Liu W, Liang S, Ren H, Yue J, Jin Y** (Mar 2025). Comprehensive profiling of integrative conjugative elements (ICEs) in Mollicutes: distinct catalysts of gene flow and genome shaping. *NAR Genomics and Bioinformatics* 7(2):lqaf083. DOI:10.1093/nargab/lqaf083  
3. **Matsumoto S, Kishida K, Nonoyama S, Sakai K, Tsuda M, Nagata Y, Ohtsubo Y** (Oct 2024). Evolution of the Tn4371 ICE family: traR-mediated coordination of cargo gene upregulation and horizontal transfer. *Microbiology Spectrum* 12(10):e00607-24. DOI:10.1128/spectrum.00607-24  
4. **Zhu X, Liang Z, Ma J, Huang J, Wang L, Yao H, Wu Z** (Sep 2024). The cadDX operon contributes to cadmium resistance, oxidative stress resistance, and virulence in zoonotic streptococci. *Veterinary Research* 55:119. DOI:10.1186/s13567-024-01371-1  
5. **Vladimirova ME, Roumiantseva ML, Saksaganskaia AS, Muntyan VS, Gaponov SP, Mengoni A** (Sep 2024). Hot Spots of Site-Specific Integration into the Sinorhizobium meliloti Chromosome. *International Journal of Molecular Sciences* 25(19):10421. DOI:10.3390/ijms251910421  
6. **Elsen S, Simon V, Attrée I** (Jun 2024). Cross-regulation and cross-talk of conserved and accessory two-component regulatory systems orchestrate Pseudomonas copper resistance. *PLOS Genetics* 20(6):e1011325. DOI:10.1371/journal.pgen.1011325  
7. **Beavogui A, Lacroix A, Wiart N, Poulain J, Delmont TO, Paoli L, Wincker P, Oliveira PH** (Mar 2024). The defensome of complex bacterial communities. *Nature Communications* 15:2146. DOI:10.1038/s41467-024-46489-0  
8. **Lyu B, Song Q** (Feb 2024). The intricate relationship of G-Quadruplexes and bacterial pathogenicity islands. *eLife* 12:e91985.3. DOI:10.7554/elife.91985.3  
9. **Benevides VP, Saraiva MMS, Nascimento CF, Delgado-Suárez EJ, Oliveira CJB, Silva SR, Miranda VFO, Christensen H, Olsen JE, Berchieri Junior A** (Feb 2024). Genomic Features and Phylogenetic Analysis of Antimicrobial-Resistant Salmonella Mbandaka ST413 Strains. *Microorganisms* 12(2):312. DOI:10.3390/microorganisms12020312  
10. **Ramesh V, Sivakumar R, Annamanedi M, Chandrapriya S, Isloor S, Rajendhran J, Hegde NR** (Nov 2024). Genome sequencing and comparative genomic analysis of bovine mastitis-associated non-aureus staphylococci and mammaliicocci (NASM) strains from India. *Scientific Reports* 14:29019. DOI:10.1038/s41598-024-80533-9  
11. **Mageeney CM, Lau BY, Wagner JM, Hudson CM, Schoeniger JS, Krishnakumar R, Williams KP** (Mar 2020). New candidates for regulated gene integrity revealed through precise mapping of integrative genetic elements. *Nucleic Acids Research* 48(8):4052–4065. DOI:10.1093/nar/gkaa156  
12. **Lechner M, Schmitt K, Bauer S, Hot D, Hubans C, Levillain E, Locht C, Lemoine Y, Gross R** (Jul 2009). Genomic island excisions in Bordetella petrii. *BMC Microbiology* 9:141. DOI:10.1186/1471-2180-9-141

---

## 10. Summary and Recommendations for TraitMech Curation

**Trait scope**: Possession of a genomic island (traitmech:000093) is defined by chromosomal integration of horizontally acquired DNA segments encoding accessory functions. Mechanistic subclasses (ICE, IME, prophage, PAI) share recombinase-mediated integration but differ in transfer capacity and cargo specialization.

**High-confidence edges**: Integrase/excisionase-mediated excision → circular intermediate → relaxase/oriT processing → T4SS transfer → recipient integration are universally conserved across ICE families. Cargo-to-phenotype edges (cadDX → Cd²⁺/oxidative resistance, cusRS-pcoA2 → Cu resistance, T3SS → virulence) are experimentally validated but taxon-specific.

**2024 quantitative benchmarks**: 7,759 MAGs, 43,263 defense systems, 314 *S. meliloti* PRSs (53.5% foreign DNA in tRNA insertions), 80-fold TraR-xis induction, 263 Mollicutes ICEs, 83.9% HGT prevalence.

**Curation priorities**: Label ICE-lifecycle edges as general; mark cargo-phenotype edges with taxa. Reserve computational GI predictions for association evidence only. Avoid asserting G4, tandem-ICE, or topoisomerase mechanisms until validated.

References

1. (watanabe2025theroleof pages 1-2): Yuta Watanabe, Y. Ishiga, and Nanami Sakata. The role of genomic islands in the pathogenicity and evolution of plant-pathogenic gammaproteobacteria. Microorganisms, Aug 2025. URL: https://doi.org/10.3390/microorganisms13081803, doi:10.3390/microorganisms13081803. This article has 6 citations.

2. (watanabe2025theroleof pages 11-12): Yuta Watanabe, Y. Ishiga, and Nanami Sakata. The role of genomic islands in the pathogenicity and evolution of plant-pathogenic gammaproteobacteria. Microorganisms, Aug 2025. URL: https://doi.org/10.3390/microorganisms13081803, doi:10.3390/microorganisms13081803. This article has 6 citations.

3. (watanabe2025theroleof pages 12-13): Yuta Watanabe, Y. Ishiga, and Nanami Sakata. The role of genomic islands in the pathogenicity and evolution of plant-pathogenic gammaproteobacteria. Microorganisms, Aug 2025. URL: https://doi.org/10.3390/microorganisms13081803, doi:10.3390/microorganisms13081803. This article has 6 citations.

4. (watanabe2025theroleof pages 13-15): Yuta Watanabe, Y. Ishiga, and Nanami Sakata. The role of genomic islands in the pathogenicity and evolution of plant-pathogenic gammaproteobacteria. Microorganisms, Aug 2025. URL: https://doi.org/10.3390/microorganisms13081803, doi:10.3390/microorganisms13081803. This article has 6 citations.

5. (chai2025comprehensiveprofilingof pages 10-13): Zili Chai, Zhiyun Guo, Xinxin Chen, Zilong Yang, Xia Wang, Fengwei Zhang, Fuqiang Kang, Wenting Liu, Shuang Liang, Hongguang Ren, Junjie Yue, and Yuan Jin. Comprehensive profiling of integrative conjugative elements (ices) in mollicutes: distinct catalysts of gene flow and genome shaping. NAR Genomics and Bioinformatics, Mar 2025. URL: https://doi.org/10.1093/nargab/lqaf083, doi:10.1093/nargab/lqaf083. This article has 2 citations and is from a peer-reviewed journal.

6. (matsumoto2024evolutionofthe pages 1-3): Satoshi Matsumoto, Kouhei Kishida, Shouta Nonoyama, Keiichiro Sakai, Masataka Tsuda, Yuji Nagata, and Yoshiyuki Ohtsubo. Evolution of the tn <i>4371</i> ice family: <i>trar</i> -mediated coordination of cargo gene upregulation and horizontal transfer. Oct 2024. URL: https://doi.org/10.1128/spectrum.00607-24, doi:10.1128/spectrum.00607-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

7. (matsumoto2024evolutionofthe pages 9-13): Satoshi Matsumoto, Kouhei Kishida, Shouta Nonoyama, Keiichiro Sakai, Masataka Tsuda, Yuji Nagata, and Yoshiyuki Ohtsubo. Evolution of the tn <i>4371</i> ice family: <i>trar</i> -mediated coordination of cargo gene upregulation and horizontal transfer. Oct 2024. URL: https://doi.org/10.1128/spectrum.00607-24, doi:10.1128/spectrum.00607-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

8. (lyu2024theintricaterelationship pages 4-6): Bo Lyu and Qisheng Song. The intricate relationship of g-quadruplexes and bacterial pathogenicity islands. eLife, Feb 2024. URL: https://doi.org/10.7554/elife.91985.3, doi:10.7554/elife.91985.3. This article has 10 citations and is from a domain leading peer-reviewed journal.

9. (benevides2024genomicfeaturesand pages 1-2): Valdinete P. Benevides, Mauro M. S. Saraiva, Camila F. Nascimento, Enrique J. Delgado-Suárez, Celso J. B. Oliveira, Saura R. Silva, Vitor F. O. Miranda, Henrik Christensen, John E. Olsen, and Angelo Berchieri Junior. Genomic features and phylogenetic analysis of antimicrobial-resistant salmonella mbandaka st413 strains. Microorganisms, 12:312, Feb 2024. URL: https://doi.org/10.3390/microorganisms12020312, doi:10.3390/microorganisms12020312. This article has 15 citations.

10. (vladimirova2024hotspotsof pages 1-2): Maria E. Vladimirova, Marina L. Roumiantseva, Alla S. Saksaganskaia, Victoria S. Muntyan, Sergey P. Gaponov, and Alessio Mengoni. Hot spots of site-specific integration into the sinorhizobium meliloti chromosome. International Journal of Molecular Sciences, 25:10421, Sep 2024. URL: https://doi.org/10.3390/ijms251910421, doi:10.3390/ijms251910421. This article has 2 citations.

11. (vladimirova2024hotspotsof pages 20-21): Maria E. Vladimirova, Marina L. Roumiantseva, Alla S. Saksaganskaia, Victoria S. Muntyan, Sergey P. Gaponov, and Alessio Mengoni. Hot spots of site-specific integration into the sinorhizobium meliloti chromosome. International Journal of Molecular Sciences, 25:10421, Sep 2024. URL: https://doi.org/10.3390/ijms251910421, doi:10.3390/ijms251910421. This article has 2 citations.

12. (beavogui2024thedefensomeof pages 8-9): Angelina Beavogui, Auriane Lacroix, Nicolas Wiart, Julie Poulain, Tom O. Delmont, Lucas Paoli, Patrick Wincker, and Pedro H. Oliveira. The defensome of complex bacterial communities. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46489-0, doi:10.1038/s41467-024-46489-0. This article has 77 citations and is from a highest quality peer-reviewed journal.

13. (beavogui2024thedefensomeof pages 1-2): Angelina Beavogui, Auriane Lacroix, Nicolas Wiart, Julie Poulain, Tom O. Delmont, Lucas Paoli, Patrick Wincker, and Pedro H. Oliveira. The defensome of complex bacterial communities. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46489-0, doi:10.1038/s41467-024-46489-0. This article has 77 citations and is from a highest quality peer-reviewed journal.

14. (mageeney2020newcandidatesfor pages 12-13): Catherine M Mageeney, Britney Y Lau, Julian M Wagner, Corey M Hudson, Joseph S Schoeniger, Raga Krishnakumar, and Kelly P Williams. New candidates for regulated gene integrity revealed through precise mapping of integrative genetic elements. Nucleic Acids Research, 48:4052-4065, Mar 2020. URL: https://doi.org/10.1093/nar/gkaa156, doi:10.1093/nar/gkaa156. This article has 48 citations and is from a highest quality peer-reviewed journal.

15. (elsen2024crossregulationandcrosstalk pages 1-2): Sylvie Elsen, Victor Simon, and Ina Attrée. Cross-regulation and cross-talk of conserved and accessory two-component regulatory systems orchestrate pseudomonas copper resistance. PLOS Genetics, 20:e1011325, Jun 2024. URL: https://doi.org/10.1371/journal.pgen.1011325, doi:10.1371/journal.pgen.1011325. This article has 11 citations and is from a domain leading peer-reviewed journal.

16. (elsen2024crossregulationandcrosstalk pages 13-14): Sylvie Elsen, Victor Simon, and Ina Attrée. Cross-regulation and cross-talk of conserved and accessory two-component regulatory systems orchestrate pseudomonas copper resistance. PLOS Genetics, 20:e1011325, Jun 2024. URL: https://doi.org/10.1371/journal.pgen.1011325, doi:10.1371/journal.pgen.1011325. This article has 11 citations and is from a domain leading peer-reviewed journal.

17. (zhu2024thecaddxoperon pages 1-2): Xinchi Zhu, Zijing Liang, Jiale Ma, Jinhu Huang, Liping Wang, Huochun Yao, and Zongfu Wu. The caddx operon contributes to cadmium resistance, oxidative stress resistance, and virulence in zoonotic streptococci. Veterinary Research, Sep 2024. URL: https://doi.org/10.1186/s13567-024-01371-1, doi:10.1186/s13567-024-01371-1. This article has 4 citations and is from a highest quality peer-reviewed journal.

18. (zhu2024thecaddxoperon pages 9-13): Xinchi Zhu, Zijing Liang, Jiale Ma, Jinhu Huang, Liping Wang, Huochun Yao, and Zongfu Wu. The caddx operon contributes to cadmium resistance, oxidative stress resistance, and virulence in zoonotic streptococci. Veterinary Research, Sep 2024. URL: https://doi.org/10.1186/s13567-024-01371-1, doi:10.1186/s13567-024-01371-1. This article has 4 citations and is from a highest quality peer-reviewed journal.

19. (lechner2009genomicislandexcisions pages 1-2): Melanie Lechner, Karin Schmitt, Susanne Bauer, David Hot, Christine Hubans, Erwan Levillain, Camille Locht, Yves Lemoine, and Roy Gross. Genomic island excisions in bordetella petrii. BMC Microbiology, 9:141-141, Jul 2009. URL: https://doi.org/10.1186/1471-2180-9-141, doi:10.1186/1471-2180-9-141. This article has 50 citations and is from a peer-reviewed journal.

20. (ramesh2024genomesequencingand pages 1-2): Vishnukumar Ramesh, Ramamoorthy Sivakumar, Madhavi Annamanedi, S. Chandrapriya, Shrikrishna Isloor, Jeyaprakash Rajendhran, and Nagendra R. Hegde. Genome sequencing and comparative genomic analysis of bovine mastitis-associated non-aureus staphylococci and mammaliicocci (nasm) strains from india. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-80533-9, doi:10.1038/s41598-024-80533-9. This article has 6 citations and is from a peer-reviewed journal.

21. (watanabe2025theroleof pages 15-17): Yuta Watanabe, Y. Ishiga, and Nanami Sakata. The role of genomic islands in the pathogenicity and evolution of plant-pathogenic gammaproteobacteria. Microorganisms, Aug 2025. URL: https://doi.org/10.3390/microorganisms13081803, doi:10.3390/microorganisms13081803. This article has 6 citations.