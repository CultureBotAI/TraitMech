---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T00:04:09.666011'
end_time: '2026-06-30T00:31:12.639109'
duration_seconds: 1622.97
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: S-layer
  trait_identifier: traitmech:000064
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: s_layer
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A morphology trait in which the cell surface is coated by a crystalline,
    two-dimensional array of self-assembling proteinaceous (glyco)protein subunits
    (a surface layer), found in many bacteria and most archaea.
  parent_traits: METPO:1000059
  synonyms: surface layer
  evidence_summary: 'DOI:10.1038/nrmicro3213:  (Fagan & Fairweather describe the S-layer
    as a self-assembled, regularly spaced two-dimensional protein array coating the
    cell surface.) | DOI:10.1038/s41579-025-01258-8:  (Review of assembly, architecture
    and functional roles of microbial surface layers supports the S-layer as a defined
    cell-surface structure.)'
  causal_graph_summary: 's_layer_2d_protein_array: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** S-layer
- **METPO identifier:** traitmech:000064
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell surface is coated by a crystalline, two-dimensional array of self-assembling proteinaceous (glyco)protein subunits (a surface layer), found in many bacteria and most archaea.
- **Parent traits:** METPO:1000059
- **Synonyms:** surface layer
- **Existing evidence:** DOI:10.1038/nrmicro3213:  (Fagan & Fairweather describe the S-layer as a self-assembled, regularly spaced two-dimensional protein array coating the cell surface.) | DOI:10.1038/s41579-025-01258-8:  (Review of assembly, architecture and functional roles of microbial surface layers supports the S-layer as a defined cell-surface structure.)
- **Existing causal graph summary:** s_layer_2d_protein_array: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **S-layer** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/s_layer.yaml`.

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
- **Trait label:** S-layer
- **METPO identifier:** traitmech:000064
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell surface is coated by a crystalline, two-dimensional array of self-assembling proteinaceous (glyco)protein subunits (a surface layer), found in many bacteria and most archaea.
- **Parent traits:** METPO:1000059
- **Synonyms:** surface layer
- **Existing evidence:** DOI:10.1038/nrmicro3213:  (Fagan & Fairweather describe the S-layer as a self-assembled, regularly spaced two-dimensional protein array coating the cell surface.) | DOI:10.1038/s41579-025-01258-8:  (Review of assembly, architecture and functional roles of microbial surface layers supports the S-layer as a defined cell-surface structure.)
- **Existing causal graph summary:** s_layer_2d_protein_array: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **S-layer** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/s_layer.yaml`.

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


# S-layer Trait Causal Graph: Curation-Focused Research Report

## 1. Trait Scope Summary

The S-layer (surface layer) is a morphology trait defined as a crystalline, two-dimensional array of self-assembling proteinaceous (glyco)protein subunits coating the cell surface of many bacteria and most archaea (METPO identifier: traitmech:000064) (pum2013slayerproteinselfassembly pages 1-4, sleytr2025slayersfroma pages 2-4). S-layers represent one of the most abundant cellular protein structures on Earth and the simplest biological membrane developed during evolution (sleytr2025slayersfroma pages 2-4). They exhibit oblique (p1, p2), square (p4), or hexagonal (p3, p6) lattice symmetries with unit cell dimensions of 3–30 nm, thicknesses of 5–20 nm in bacteria (up to ~70 nm in archaea), and 30–70% porosity with uniform pores of 2–8 nm (pum2013slayerproteinselfassembly pages 1-4, sleytr2025slayersfroma pages 2-4). Hexagonal symmetry predominates among archaea while varied symmetries are found in bacteria (sleytr2025slayersfroma pages 2-4, pum2021patternsinnature—slayer pages 6-8).

**Boundary cases and distinctions from nearby traits:**
- S-layers are distinct from sheaths (e.g., *Methanospirillum hungatei*), which are non-crystalline amyloid-like protein assemblies, though both are cell-surface proteinaceous structures.
- S-layers differ from peptidoglycan cell walls, outer membranes, and capsules in being exclusively composed of (glyco)protein subunits arranged in a periodic lattice. In archaea that possess S-layers as the sole cell wall component, they functionally replace peptidoglycan (grillwalcher2025anewage pages 1-2).
- The trait is defined at the CLASS level and encompasses diverse S-layer protein families (SLH-domain containing, CWB2-domain containing, non-SLH lactobacilli types, two-component archaeal types) that converge on the same cell-surface phenotype.

---

## 2. Candidate Causal Graph Nodes

The following table organizes all candidate nodes by type, with ontology groundings where available:

| Node Name | Node Type | Suggested CURIE | Description |
|---|---|---|---|
| **PROTEINS/GENES** ||||
| SlpA | protein/gene | label-only candidate | *Clostridioides difficile* S-layer precursor protein; exported via accessory Sec, proteolytically cleaved into HMW/LMW SLPs, then assembled into the mature S-layer (kirk2017characteristicsofthe pages 4-5) |
| SlaA | protein/gene | label-only candidate | Outer extracellular S-layer glycoprotein of *Sulfolobus acidocaldarius*; highly glycosylated and forms the main porous lattice (gambelli2024structureofthe pages 10-12, gambelli2024structureofthe pages 2-3) |
| SlaB | protein/gene | label-only candidate | Inner/membrane-bound S-layer component of *S. acidocaldarius*; trimeric anchor linking SlaA lattice to the membrane (gambelli2024structureofthe pages 10-12, gambelli2024structureofthe pages 2-3) |
| EA1 | protein/gene | label-only candidate | *Bacillus anthracis* stationary-phase S-layer protein; calcium-dependent assembly protein with N-terminal SLH domains and six Ig-like assembly domains (sogues2023structureandfunction pages 1-2, sogues2023structureandfunction pages 2-3) |
| Sap | protein/gene | label-only candidate | *B. anthracis* exponential-phase S-layer protein; mutually exclusive with EA1 and anchored to SCWP through SLH domains (sogues2023structureandfunction pages 1-2, sogues2023structureandfunction pages 7-8) |
| Cwp84 | protein/gene | label-only candidate | Cell wall-localized cysteine protease that cleaves SlpA precursor into mature HMW and LMW S-layer proteins in *C. difficile* (kirk2017characteristicsofthe pages 4-5) |
| Cwp66 | protein/gene | label-only candidate | *C. difficile* cell wall protein and adhesin contributing to adhesion, stress tolerance, and antibiotic resistance (chandra2023hostimmuneresponses pages 4-6) |
| Cwp2 | protein/gene | label-only candidate | Major *C. difficile* cell wall protein associated with the S-layer and implicated in adhesion/colonization (chandra2023hostimmuneresponses pages 4-6) |
| RsaA | protein/gene | label-only candidate | Major *Caulobacter crescentus* S-layer protein inserted at poles and mid-cell during cell-cycle-coordinated S-layer biogenesis (herdman2023cellcycledependent pages 8-11, herdman2023cellcycledependent pages 11-15) |
| SlpB | protein/gene | label-only candidate | Lactobacillus S-layer protein paralog/accessory component; present in S-layer loci but often silenced in studied strains (sagmeister2024themoleculararchitecture pages 1-2, hynonen2013lactobacillussurfacelayer pages 7-8) |
| SlpX | protein/gene | label-only candidate | Lactobacillus accessory S-layer protein incorporated into the lattice, especially under environmental stress; linked to cell integrity (sagmeister2024themoleculararchitecture pages 1-2, sagmeister2024themoleculararchitecture pages 9-9) |
| SecA2 | protein/gene | label-only candidate | Accessory Sec ATPase in the *C. difficile* S-layer locus required for export of SlpA and related S-layer proteins (kirk2017characteristicsofthe pages 4-5, barwinskasendra2025evolutionaryplasticityof pages 21-21) |
| MreB | protein/gene | UniProtKB:P0A9X4 | Bacterial actin homolog; required for spatial coordination of S-layer insertion with elongation zones in *C. crescentus* (herdman2023cellcycledependent pages 5-8, herdman2024cellcycledependent pages 4-5) |
| Saci1846 | protein/gene | label-only candidate | Thermopsin-like protease implicated with SlaB in anchoring/assembly of the *Sulfolobus* S-layer; taxon-specific and still emerging evidence (foo2025themechanicsof pages 23-26) |
| TfsA | protein/gene | label-only candidate | *Tannerella forsythia* O-glycosylated S-layer protein secreted by T9SS and assembled into the cell-surface lattice (paillat2023ajourneywith pages 8-9) |
| TfsB | protein/gene | label-only candidate | *T. forsythia* O-glycosylated S-layer protein secreted by T9SS and assembled with TfsA into the S-layer (paillat2023ajourneywith pages 8-9) |
| AglB | protein/gene | label-only candidate | Archaeal oligosaccharyltransferase catalyzing the final step of N-glycosylation; essential in *S. acidocaldarius* (gambelli2024structureofthe pages 12-13) |
| **DOMAINS/MOTIFS** ||||
| SLH domain | domain/motif | pfam:PF00395 | S-layer homology domain mediating non-covalent anchoring of Bacillaceae S-layer proteins to secondary cell wall polysaccharides (pum2013slayerproteinselfassembly pages 1-4, sogues2023structureandfunction pages 1-2) |
| CWB2 domain | domain/motif | pfam:PF04122 | Cell wall binding 2 motif in *C. difficile* HMW SLP region; mediates anchoring to PS-II (kirk2017characteristicsofthe pages 4-5) |
| signal peptide | domain/motif | GO:0005048 | N-terminal secretion signal directing S-layer proteins into export pathways such as Sec or accessory SecA2 (kirk2017characteristicsofthe pages 4-5, paillat2023ajourneywith pages 1-3) |
| Ig-like domain | domain/motif | label-only candidate | Immunoglobulin-like assembly domain forming the tile-like assembly regions of EA1 and Sap (sogues2023structureandfunction pages 1-2, sogues2023structureandfunction pages 7-8) |
| TAB domain | domain/motif | label-only candidate | Teichoic-acid-binding domain of Lactobacillus SlpA proteins implicated in LTA/WTA attachment (sagmeister2024themoleculararchitecture pages 9-9, sagmeister2024themoleculararchitecture pages 1-2) |
| **CHEMICALS/METABOLITES** ||||
| Ca2+ ions | chemical | CHEBI:29108 | Divalent cation commonly required for S-layer reassembly and, in EA1 and archaeal systems, structural stabilization/assembly control (sleytr2025slayersfroma pages 19-20, sogues2023structureandfunction pages 2-3) |
| secondary cell wall polymer (SCWP) | chemical/polymer | label-only candidate | Bacillaceae wall polymer recognized by SLH domains to anchor S-layer proteins such as EA1 and Sap (sogues2023structureandfunction pages 1-2, sogues2023structureandfunction pages 7-8) |
| polysaccharide II (PS-II) | chemical/polymer | label-only candidate | *C. difficile* anionic wall polymer bound by CWB2 motifs to attach SlpA-derived heterodimers to the cell wall (kirk2017characteristicsofthe pages 4-5) |
| lipoteichoic acid (LTA) | chemical/polymer | CHEBI:24402 | Lactobacillus cell wall polymer serving as S-layer attachment ligand for TAB-containing SlpA proteins (sagmeister2024themoleculararchitecture pages 1-2, sagmeister2024themoleculararchitecture pages 9-9) |
| wall teichoic acid (WTA) | chemical/polymer | CHEBI:7744 | Cell wall polymer implicated in Lactobacillus S-layer attachment alongside LTA (sagmeister2024themoleculararchitecture pages 1-2) |
| N-glycans | chemical/glycan | CHEBI:50699 | N-linked glycans decorating archaeal S-layer proteins such as SlaA/SlaB; associated with thermostability and surface properties (gambelli2024structureofthe pages 1-2, gambelli2024structureofthe pages 12-13) |
| O-glycans | chemical/glycan | label-only candidate | O-linked glycans decorating some bacterial S-layer proteins, including *T. forsythia* TfsA/TfsB (paillat2023ajourneywith pages 8-9) |
| peptidoglycan | chemical/polymer | CHEBI:52722 | Structural cell wall polymer beneath many bacterial S-layers; S-layer insertion coordinates with zones of peptidoglycan turnover (herdman2024cellcycledependent pages 1-2, herdman2023cellcycledependent pages 8-11) |
| **SECRETION SYSTEMS** ||||
| Sec pathway | secretion system | GO:0015031 | General secretion pathway exporting signal-peptide-containing proteins across the cytoplasmic membrane; used upstream of several S-layer systems (kirk2017characteristicsofthe pages 4-5, paillat2023ajourneywith pages 1-3) |
| accessory Sec (SecA2) | secretion system | label-only candidate | Specialized Sec branch in *C. difficile* associated with S-layer protein export, especially SlpA secretion (kirk2017characteristicsofthe pages 4-5) |
| Type IX secretion system (T9SS) | secretion system | label-only candidate | Bacteroidota secretion machine exporting S-layer glycoproteins such as TfsA/TfsB after Sec-dependent periplasmic transit (paillat2023ajourneywith pages 8-9, paillat2023ajourneywith pages 1-3) |
| signal peptide-dependent export | secretion process | GO:0006614 | Protein export logic in which N-terminal signal peptides target S-layer precursors to translocation pathways (kirk2017characteristicsofthe pages 4-5, paillat2023ajourneywith pages 1-3) |
| **BIOLOGICAL PROCESSES** ||||
| self-assembly | biological process | GO:0043934 | Intrinsic spontaneous assembly of S-layer proteins into ordered arrays on cell surfaces or in vitro (pum2021patternsinnature—slayer pages 2-4, pum2013slayerproteinselfassembly pages 4-6) |
| 2D crystalline lattice formation | biological process | label-only candidate | Formation of porous para/crystalline monolayers characteristic of S-layers (pum2013slayerproteinselfassembly pages 1-4, gambelli2024structureofthe pages 2-3) |
| entropy-driven assembly | biological process | label-only candidate | In vitro S-layer reassembly process described as largely entropy-driven and modulated by ionic conditions (sleytr2025slayersfroma pages 18-19) |
| cell wall anchoring | biological process | GO:0046813 | Attachment of assembled S-layer proteins to wall polymers via SLH, CWB2, or TAB-mediated interactions (kirk2017characteristicsofthe pages 4-5, sagmeister2024themoleculararchitecture pages 9-9) |
| post-translational cleavage | biological process | GO:0016485 | Maturation step in which proteases such as Cwp84 process S-layer precursors after export (kirk2017characteristicsofthe pages 4-5) |
| N-glycosylation | biological process | GO:0018279 | Common archaeal S-layer protein modification; in *Sulfolobus* mediated by AglB and extensive on SlaA/SlaB (gambelli2024structureofthe pages 12-13, gambelli2024structureofthe pages 1-2) |
| O-glycosylation | biological process | GO:0006493 | Modification of certain bacterial S-layer proteins, notably TfsA/TfsB in *T. forsythia* (paillat2023ajourneywith pages 8-9) |
| cell cycle coordination | biological process | GO:0007049 | Spatial and temporal coordination of S-layer insertion with growth and division, especially in *C. crescentus* (herdman2024cellcycledependent pages 4-5, herdman2024cellcycledependent pages 1-2) |
| peptidoglycan turnover coordination | biological process | label-only candidate | Coupling of new S-layer insertion to regions of active peptidoglycan synthesis/turnover (herdman2023cellcycledependent pages 8-11, herdman2024cellcycledependent pages 8-9) |
| **CELLULAR LOCALIZATIONS** ||||
| cell surface | cellular localization | GO:0009986 | Principal location of mature S-layer lattices as the outermost coat of many bacteria and most archaea (gambelli2024structureofthe pages 2-3, sleytr2025slayersfroma pages 2-4) |
| outer membrane | cellular localization | GO:0019867 | Relevant location for diderm S-layers such as *Caulobacter* and for T9SS-mediated delivery across the outer membrane (paillat2023ajourneywith pages 1-3, herdman2024cellcycledependent pages 4-5) |
| periplasm | cellular localization | GO:0042597 | Intermediate compartment for Sec-exported/T9SS-targeted proteins in diderm bacteria; TfsA/TfsB remain here in T9SS mutants (paillat2023ajourneywith pages 8-9, paillat2023ajourneywith pages 1-3) |
| cell wall | cellular localization | GO:0005618 | Anchoring substrate for many bacterial S-layers via SCWP, PS-II, or teichoic acids (kirk2017characteristicsofthe pages 4-5, sogues2023structureandfunction pages 1-2) |
| **FUNCTIONS** ||||
| molecular sieve | functional role | GO:0016491 | Porous S-layer lattice acts as an isoporous molecular sieve controlling passage of molecules (hynonen2013lactobacillussurfacelayer pages 1-2, grillwalcher2025anewage pages 1-2) |
| mechanical stabilization/exoskeleton | functional role | label-only candidate | S-layer provides mechanical and osmotic support to the envelope; disruption causes defects, blebbing, or lysis (sogues2023structureandfunction pages 1-2, barwinskasendra2025evolutionaryplasticityof pages 33-35) |
| cell shape determination | functional role | GO:0008360 | Especially in archaea lacking peptidoglycan, S-layers help determine and maintain cell morphology (hynonen2013lactobacillussurfacelayer pages 1-2, grillwalcher2025anewage pages 1-2) |
| virulence factor | functional role | GO:0009405 | In pathogens such as *C. difficile* and *B. anthracis*, S-layer components contribute to host interaction and pathogenicity (grillwalcher2025anewage pages 1-2, chandra2023hostimmuneresponses pages 4-6) |
| adhesion | functional role | GO:0022610 | S-layer proteins and associated CWPs mediate binding to host cells, extracellular matrix, or abiotic surfaces (hynonen2013lactobacillussurfacelayer pages 1-2, chandra2023hostimmuneresponses pages 4-6) |
| immune evasion | functional role | GO:0050776 | S-layers can protect against complement/phagocytosis and contribute to serum resistance or antigenic variation (hynonen2013lactobacillussurfacelayer pages 1-2, barwinskasendra2025evolutionaryplasticityof pages 33-35) |
| protection from environmental stress | functional role | GO:0006950 | S-layers protect cells from osmotic, pH, oxidative, radiation, predatory, and phage-associated stresses (hynonen2013lactobacillussurfacelayer pages 1-2, grillwalcher2025anewage pages 1-2) |


*Table: This table compiles candidate causal graph nodes for the S-layer trait, grouped by entity type and grounded where possible to stable identifiers. It is useful as a starting inventory for TraitMech curation of mechanistic components, processes, localizations, and functions.*

---

## 3. Mechanistic Summary and Causal Pathways

### 3.1 S-Layer Protein Synthesis and Export

S-layer proteins are among the most highly expressed proteins in prokaryotes, with approximately 590,000 subunits per cell in *C. difficile* (kirk2017characteristicsofthe pages 4-5). The biogenesis pathway begins with transcription and translation of S-layer protein genes. In *C. difficile*, the *slpA* gene encodes a precursor protein containing an N-terminal signal peptide, a variable low-molecular-weight (LMW) region, and a high-molecular-weight (HMW) region with three tandem CWB2 motifs (kirk2017characteristicsofthe pages 4-5). The signal peptide directs the pre-protein across the cytoplasmic membrane via the accessory Sec system, with SecA2 serving as the dedicated S-layer secretion ATPase (kirk2017characteristicsofthe pages 4-5).

In Bacteroidota species such as *Tannerella forsythia*, S-layer glycoproteins TfsA and TfsB are first exported to the periplasm via the general Sec pathway using their signal peptides, then translocated across the outer membrane by the Type IX secretion system (T9SS) (paillat2023ajourneywith pages 8-9, paillat2023ajourneywith pages 1-3). Notably, O-glycosylation of TfsA/TfsB occurs independently of T9SS function, as T9SS mutants retain glycosylated proteins in the periplasm (paillat2023ajourneywith pages 8-9).

### 3.2 Post-Translational Processing and Modification

A critical maturation step in *C. difficile* is the proteolytic cleavage of the SlpA precursor by the cell wall-localized cysteine protease Cwp84, generating HMW and LMW SLPs that form a stable heterodimeric complex (kirk2017characteristicsofthe pages 4-5).

Glycosylation is a major post-translational modification of S-layer proteins. In the archaeon *Sulfolobus acidocaldarius*, SlaA contains 31 predicted N-glycosylation sites, with 19 confirmed by cryo-EM density corresponding to complete hexasaccharides and glycan intermediates (gambelli2024structureofthe pages 12-13). The oligosaccharyltransferase AglB catalyzes the final step of N-glycosylation and is essential for viability in *S. acidocaldarius* (gambelli2024structureofthe pages 12-13). Thermophilic archaea generally display more glycosylation sites than mesophilic archaea, suggesting glycans support thermostability (gambelli2024structureofthe pages 2-3, gambelli2024structureofthe pages 1-2).

### 3.3 Cell Wall Anchoring

Three major anchoring mechanisms have been characterized:

1. **SLH–SCWP system** (Bacillaceae): EA1 and Sap of *B. anthracis* contain three N-terminal SLH domains (~180 amino acids) that bind non-covalently to the secondary cell wall polysaccharide (SCWP) decorating peptidoglycan (sogues2023structureandfunction pages 1-2, sogues2023structureandfunction pages 2-3).

2. **CWB2–PS-II system** (*C. difficile*): Three tandem CWB2 motifs in the HMW SLP anchor the H/L complex to polysaccharide II (PS-II), an anionic polymer in the cell wall (kirk2017characteristicsofthe pages 4-5).

3. **TAB–teichoic acid system** (Lactobacillaceae): The TAB domain at the N-terminus of SlpA binds lipoteichoic acid (LTA) or wall teichoic acid (WTA) through electrostatic interactions (sagmeister2024themoleculararchitecture pages 1-2, sagmeister2024themoleculararchitecture pages 9-9).

In the archaeon *S. acidocaldarius*, the membrane-spanning SlaB protein anchors the outer SlaA lattice via a C-terminal transmembrane helix, with SlaB trimers interacting with SlaA dimers through charged domain interactions (gambelli2024structureofthe pages 10-12, foo2025themechanicsof pages 23-26).

### 3.4 Self-Assembly and Lattice Formation

S-layer self-assembly is an intrinsic property of the protein subunits, fundamentally determined by their amino acid sequence and tertiary structure (pum2013slayerproteinselfassembly pages 4-6). The process is primarily entropy-driven and modulated by environmental conditions (sleytr2025slayersfroma pages 18-19). Key factors include:

- **Ca²⁺ ions**: Essential for reassembly of most S-layer proteins, including SbpA and EA1, where calcium controls crystal morphology from fractal-like structures to micrometer-sized monocrystalline patches (sleytr2025slayersfroma pages 19-20, sleytr2025slayersfroma pages 4-5). In EA1, three calcium-binding sites structure interdomain contacts, enabling monomers to adopt assembly-competent conformations (sogues2023structureandfunction pages 1-2, sogues2023structureandfunction pages 2-3).

- **pH, temperature, and ionic strength**: These parameters collectively determine self-assembly outcomes—flat sheets, ribbons, tubes, or vesicles (pum2021patternsinnature—slayer pages 2-4, pum2013slayerproteinselfassembly pages 6-10, sleytr2025slayersfroma pages 18-19).

- **Divalent cation interactions**: Ca²⁺ and other divalent cations stabilize S-layers by interacting with acidic amino acid residues and participating in ionic bonding (pum2013slayerproteinselfassembly pages 6-10, pum2013slayerproteinselfassembly pages 4-6).

### 3.5 Biogenesis Coordination with Cell Cycle

S-layer biogenesis in *Caulobacter crescentus* is tightly coordinated with the cell cycle. New S-layer (RsaA) insertion localizes to cell poles in swarmer cells and to the mid-cell during division, consistent with regions of active cell growth (herdman2024cellcycledependent pages 4-5, herdman2024cellcycledependent pages 1-2). The bacterial actin homolog MreB is crucial for this spatial organization; disruption of MreB dramatically delocalizes S-layer insertion (herdman2023cellcycledependent pages 5-8, herdman2024cellcycledependent pages 4-5). Peptidoglycan turnover precedes S-layer expansion, indicating a coordinated temporal sequence where cell wall synthesis creates membrane surfaces that are then coated by available S-layer monomers filling lattice gaps (herdman2023cellcycledependent pages 8-11, herdman2024cellcycledependent pages 8-9). This pattern of localized, cell-cycle-dependent insertion at growth regions is conserved across diverse prokaryotes including *C. difficile* (SlpA at cell wall turnover regions) and *Haloferax volcanii* (S-layer machinery colocalizing with FtsZ) (herdman2024cellcycledependent pages 8-9).

### 3.6 Functional Roles

The S-layer lattice provides multiple functional outputs:

- **Molecular sieve**: Uniform pores with precise exclusion limits regulate nutrient uptake and enzyme secretion (grillwalcher2025anewage pages 1-2).
- **Mechanical stabilization/exoskeleton**: Provides osmotic and mechanical support; disruption of the *B. anthracis* EA1 S-layer causes membrane blebbing and cell lysis under hypotonic conditions (sogues2023structureandfunction pages 1-2, sogues2023structureandfunction pages 7-8).
- **Cell shape determination**: Especially in archaea lacking peptidoglycan, S-layers serve as shape-determining scaffolds (grillwalcher2025anewage pages 1-2, gambelli2024structureofthe pages 2-3).
- **Virulence factor**: In *C. difficile*, SLPs mediate adhesion to intestinal epithelial cells via TLR4 and modulate immune responses including Th1/Th2 and humoral immunity (chandra2023hostimmuneresponses pages 4-6).
- **Adhesion**: S-layer proteins and associated cell wall proteins (Cwp66, Cwp2) mediate binding to host cells, extracellular matrix proteins, and abiotic surfaces (hynonen2013lactobacillussurfacelayer pages 1-2, chandra2023hostimmuneresponses pages 4-6).
- **Immune evasion**: S-layers protect against complement, phagocytosis, and provide serum resistance (hynonen2013lactobacillussurfacelayer pages 1-2, barwinskasendra2025evolutionaryplasticityof pages 33-35).
- **Protection from environmental stress**: S-layers shield cells from osmotic, pH, oxidative, radiation, predatory, and bacteriophage-associated stresses (hynonen2013lactobacillussurfacelayer pages 1-2, grillwalcher2025anewage pages 1-2).

---

## 4. Candidate Causal Edges

The following table presents 30 evidence-backed causal edges as subject–predicate–object triples suitable for TraitMech curation:

| Edge ID | Subject | Predicate | Object | Reference (DOI) | Snippet | Notes |
|---|---|---|---|---|---|---|
| E1 | slpA gene | encodes | SlpA precursor protein | 10.1111/1751-7915.12372 | “The C. difficile S-layer is composed of two proteins (HMW and LMW SLPs) generated by post-translational cleavage of a pre-protein encoded by the slpA gene.” (kirk2017characteristicsofthe pages 4-5) | Strong evidence in *C. difficile*; taxon-specific but canonical for this lineage. |
| E2 | signal peptide | directs | Sec-dependent export of S-layer protein | 10.1111/1751-7915.12372 | “The signal peptide directs the pre-protein across the cell membrane via the accessory Sec system.” (kirk2017characteristicsofthe pages 4-5) | Strong evidence for SlpA export; applies to signal-peptide-bearing S-layer precursors in this system. |
| E3 | SecA2 | mediates | SlpA translocation across membrane | 10.1111/1751-7915.12372 | “The S-layer locus encodes SecA2, identified as the S-layer secretion ATPase.” (kirk2017characteristicsofthe pages 4-5) | Strong evidence for accessory Sec involvement in *C. difficile* S-layer biogenesis. |
| E4 | Cwp84 | cleaves | SlpA precursor into HMW + LMW SLPs | 10.1111/1751-7915.12372 | “The cysteine protease Cwp84 cleaves the pre-protein to generate the two SLPs.” (kirk2017characteristicsofthe pages 4-5) | Strong evidence; direct maturation step. |
| E5 | HMW/LMW SLP complex | self-assembles | S-layer lattice | 10.1111/1751-7915.12372 | “The two SLPs form a stable heterodimeric complex (H/L complex) that self-assembles into the mature S-layer.” (kirk2017characteristicsofthe pages 4-5) | Strong evidence for *C. difficile*. |
| E6 | CWB2 domain | anchors | HMW SLP to PS-II | 10.1111/1751-7915.12372 | “The CWB2 motifs anchor the H/L complex to the cell wall through interaction with PS-II (polysaccharide II).” (kirk2017characteristicsofthe pages 4-5) | Strong evidence; anchor chemistry is lineage-specific. |
| E7 | slaA gene | encodes | SlaA outer S-layer protein | 10.1101/2025.02.04.636414 | “slaA (saci2355) and slaB (saci2354) genes encode major S-layer proteins.” (foo2025themechanicsof pages 23-26) | Evidence is from 2025 preprint, not Gambelli 2024; curate as probable/needs confirmation in primary genomic annotation. |
| E8 | slaB gene | encodes | SlaB membrane anchor | 10.1101/2025.02.04.636414 | “slaA (saci2355) and slaB (saci2354) genes encode major S-layer proteins.” (foo2025themechanicsof pages 23-26) | As above; SlaB membrane-anchor role additionally supported structurally elsewhere. |
| E9 | SlaB trimer | anchors | SlaA lattice to membrane | 10.7554/eLife.84617 | “SlaB trimers occupy alternating triangular pores with their long axis perpendicular to the membrane plane, functioning as membrane anchors.” (gambelli2024structureofthe pages 10-12) | Strong structural evidence in *Sulfolobus acidocaldarius*. |
| E10 | AglB | catalyzes | N-glycosylation of SlaA | 10.7554/eLife.84617 | “The oligosaccharyl transferase AglB catalyzes the final step of protein glycosylation in archaea.” (gambelli2024structureofthe pages 12-13) | Indirect for SlaA specifically; strong for archaeal S-layer glycoproteins in *Sulfolobus*. Mark as moderately inferred. |
| E11 | N-glycosylation | promotes | thermostability of archaeal S-layer | 10.7554/eLife.84617 | “Thermophilic and hyperthermophilic archaea show higher numbers of glycosylation sites on S-layer proteins… suggesting glycans support thermostability.” (gambelli2024structureofthe pages 2-3) | Suggestive rather than direct causal proof; mark uncertain/inferred. |
| E12 | SLH domain | binds | SCWP for cell wall anchoring | 10.1038/s41467-023-42826-x | “Three S-layer homology (SLH) domains… anchor them to the cell surface through non-covalent interactions with the secondary cell wall polysaccharide.” (sogues2023structureandfunction pages 1-2) | Strong evidence for Bacillaceae S-layers. |
| E13 | Ca2+ ions | facilitate | EA1 assembly-competent conformation | 10.1038/s41467-023-42826-x | “Three calcium-binding sites structure interdomain contacts that allow monomers to adopt their assembly-competent conformation.” (sogues2023structureandfunction pages 1-2) | Strong evidence for EA1 specifically. |
| E14 | Ig-like domains | mediate | inter-protomer contacts in lattice | 10.1038/s41467-023-42826-x | “The assembly domains of both proteins consist of six immunoglobulin-like domains.” / “The S-layer encompasses four intermolecular contact zones between adjacent EA1 protomers.” (sogues2023structureandfunction pages 1-2, sogues2023structureandfunction pages 3-4) | Supported by combined structural statements; moderate-to-strong. |
| E15 | TAB domain | binds | teichoic acids for S-layer anchoring | 10.1073/pnas.2401686121 | “The TAB domain located at the N-terminus of SlpA proteins… plays a role in teichoic acid (LTA) binding.” (sagmeister2024themoleculararchitecture pages 9-9) | Strong evidence in Lactobacillus system. |
| E16 | SlpX | integrates | into S-layer under stress | 10.1073/pnas.2401686121 | “Under normal conditions, SlpX comprises ~10% of the S-layer, increasing to ~40% under environmental stress.” (sagmeister2024themoleculararchitecture pages 1-2) | Strong quantitative evidence for stress-associated incorporation. |
| E17 | T9SS | secretes | TfsA/TfsB S-layer proteins | 10.1099/mic.0.001320 | “The T9SS secretes two glycoproteins, TfsA and TfsB, which self-assemble into a two-dimensional crystalline S-layer lattice.” (paillat2023ajourneywith pages 8-9) | Strong evidence in *Tannerella forsythia*. |
| E18 | Sec pathway | exports | T9SS substrates to periplasm | 10.1099/mic.0.001320 | “Proteins destined for secretion possess a signal peptide… for export to the periplasm via the Sec machinery.” (paillat2023ajourneywith pages 1-3) | Strong evidence for upstream export step before T9SS. |
| E19 | Ca2+ concentration | controls | S-layer crystal morphology | 10.1017/S0033583524000106 | “Calcium concentration directly controlling crystal morphology and lattice formation.” (sleytr2025slayersfroma pages 19-20) | Strong in vitro assembly evidence; assay-context specific. |
| E20 | pH | modulates | S-layer self-assembly pathway | 10.3390/ijms14022484 | “Environmental conditions including pH… significantly influence assembly outcomes.” (pum2013slayerproteinselfassembly pages 6-10) | Strong but general/in vitro-heavy evidence. |
| E21 | ionic strength | influences | lattice formation outcome | 10.3390/ijms14022484 | “Environmental conditions including… ionic strength… significantly influence assembly outcomes.” (pum2013slayerproteinselfassembly pages 6-10) | Strong but largely derived from reassembly experiments. |
| E22 | MreB | coordinates | localized S-layer insertion | 10.1038/s41467-024-47529-5 | “When MreB is disrupted… S-layer integration becomes delocalized.” (herdman2024cellcycledependent pages 4-5) | Strong evidence in *Caulobacter crescentus*. |
| E23 | peptidoglycan turnover | precedes | S-layer insertion | 10.1038/s41467-024-47529-5 | “Cell wall turnover precedes S-layer expansion.” (herdman2024cellcycledependent pages 8-9) | Strong evidence in *C. crescentus*. |
| E24 | cell cycle | regulates | S-layer biogenesis spatiotemporal pattern | 10.1038/s41467-024-47529-5 | “S-layer insertion is temporally coupled… at cell poles and mid-cell.” (herdman2024cellcycledependent pages 1-2) | Strong evidence in *C. crescentus*; extrapolation to all taxa should be cautious. |
| E25 | S-layer lattice | provides | molecular sieve function | 10.1016/j.jbc.2025.110205 | “The pores formed in S-layer lattices function as molecular sieves with precise exclusion limits.” (grillwalcher2025anewage pages 1-2) | Strong review-level synthesis; broad across taxa. |
| E26 | S-layer lattice | provides | mechanical stabilization/exoskeleton | 10.1038/s41467-023-42826-x | “S-layers function as mechanical supports for the cell wall; depolymerization results in surface defects, membrane blebbing and cell lysis.” (sogues2023structureandfunction pages 1-2) | Strong direct experimental evidence in *B. anthracis*. |
| E27 | S-layer lattice | mediates | host cell adhesion | 10.3390/microorganisms11020380 | “SLPs mediate adhesion… disrupt tight junctions of intestinal epithelial cells.” (chandra2023hostimmuneresponses pages 4-6) | Strong for *C. difficile* SLPs; likely taxon-specific functional role. |
| E28 | S-layer lattice | confers | immune evasion | 10.1101/2025.04.02.646754 | “The surface layer of Tannerella forsythia provides serum resistance, indicating immune evasion capabilities.” (barwinskasendra2025evolutionaryplasticityof pages 33-35) | Preprint evidence and lineage-specific example; mark uncertain/broad generalization. |
| E29 | S-layer lattice | determines | cell shape in archaea | 10.1016/j.jbc.2025.110205 | “They provide structural support and maintain cell shape, particularly important in archaea lacking complex cell walls.” (grillwalcher2025anewage pages 1-2) | Strong review-level support, especially for archaeal systems. |
| E30 | S-layer lattice | protects | against environmental stress | 10.1007/s00253-013-4962-2 | “S-layer proteins protect bacterial cells from various environmental stresses including mechanical and osmotic stress, antimicrobial peptides, radiation, pH changes, bacteriophages…” (hynonen2013lactobacillussurfacelayer pages 1-2) | Strong review-level support; broad functional generalization across taxa. |


*Table: This table summarizes candidate subject-predicate-object edges for TraitMech curation of the S-layer trait, with DOI-linked references, evidence snippets, and notes on scope or uncertainty. It is designed to support direct translation into a curated causal graph while flagging lineage-specific or inferred claims.*

---

## 5. DOI-First Bibliography

1. Kirk JA, Banerji O, Fagan RP (2017) Characteristics of the *Clostridium difficile* cell envelope and its importance in therapeutics. *Microbial Biotechnology* 10:76–90. DOI: 10.1111/1751-7915.12372
2. Gambelli L et al. (2024) Structure of the two-component S-layer of the archaeon *Sulfolobus acidocaldarius*. *eLife* 13. DOI: 10.7554/eLife.84617
3. Sogues A et al. (2023) Structure and function of the EA1 surface layer of *Bacillus anthracis*. *Nature Communications* 14. DOI: 10.1038/s41467-023-42826-x
4. Sagmeister T et al. (2024) The molecular architecture of Lactobacillus S-layer: Assembly and attachment to teichoic acids. *PNAS* 121. DOI: 10.1073/pnas.2401686121
5. Herdman M et al. (2024) Cell cycle dependent coordination of surface layer biogenesis in *Caulobacter crescentus*. *Nature Communications* 15. DOI: 10.1038/s41467-024-47529-5
6. Sleytr UB, Pum D (2025) S-layers: from a serendipitous discovery to a toolkit for nanobiotechnology. *Quarterly Reviews of Biophysics* 58. DOI: 10.1017/S0033583524000106
7. Grill-Walcher S, Schäffer C (2025) A new age in structural S-layer biology: Experimental and in silico milestones. *Journal of Biological Chemistry* 301:110205. DOI: 10.1016/j.jbc.2025.110205
8. Paillat M et al. (2023) A journey with type IX secretion system effectors. *Microbiology* 169. DOI: 10.1099/mic.0.001320
9. Chandra H et al. (2023) Host immune responses to surface S-layer proteins (SLPs) of *Clostridioides difficile*. *Microorganisms* 11:380. DOI: 10.3390/microorganisms11020380
10. Barwinska-Sendra A et al. (2025) Evolutionary plasticity of bacterial surface layer protein exoskeletons. *bioRxiv*. DOI: 10.1101/2025.04.02.646754
11. Pum D et al. (2013) S-Layer protein self-assembly. *Int J Mol Sci* 14:2484–2501. DOI: 10.3390/ijms14022484
12. Pum D et al. (2021) Patterns in nature—S-layer lattices of bacterial and archaeal cells. *Crystals* 11:869. DOI: 10.3390/cryst11080869
13. Hynönen U, Palva A (2013) *Lactobacillus* surface layer proteins: structure, function and applications. *Appl Microbiol Biotechnol* 97:5225–5243. DOI: 10.1007/s00253-013-4962-2
14. Foo S et al. (2025) The mechanics of a continuous self-assembling surface-layer aids cell division in an archaeon. *bioRxiv*. DOI: 10.1101/2025.02.04.636414
15. Buhlheller C et al. (2024) SymProFold: Structural prediction of symmetrical biological assemblies. *Nature Communications* 15. DOI: 10.1038/s41467-024-52138-3
16. Yuliawati Y et al. (2024) Potency of surface layer protein from *Lactobacillus* sp. as drug nanocarriers. *J Appl Pharm Sci*. DOI: 10.7324/japs.2024.199203
17. Fagan RP, Fairweather NF (2014) Biogenesis and functions of bacterial S-layers. *Nature Reviews Microbiology* 12:211–222. DOI: 10.1038/nrmicro3213 (existing evidence)
18. Isbilir B et al. (2025) Assembly, architecture and functional roles of microbial surface layers. *Nature Reviews Microbiology* 24:344–358. DOI: 10.1038/s41579-025-01258-8 (existing evidence)

---

## 6. Warnings and Curation Notes

1. **Taxon-specific claims**: Many mechanistic edges are documented in specific model organisms. The *C. difficile* SlpA/CWB2/PS-II system, the *Sulfolobus* SlaA/SlaB system, the Bacillaceae SLH/SCWP system, and the *Lactobacillus* TAB/teichoic acid system represent distinct lineage-specific architectures converging on the same S-layer phenotype. Causal edges derived from one system should be flagged when generalized.

2. **Preprint evidence**: Edges E7, E8 (Foo et al. 2025) and E28 (Barwinska-Sendra et al. 2025) are from preprints and should be confirmed upon peer-reviewed publication before full curation.

3. **Inferred causation**: Edge E11 (N-glycosylation → thermostability) is correlative—higher glycosylation correlates with thermophily—but a direct causal mechanism has not been fully established (gambelli2024structureofthe pages 2-3).

4. **Emerging components**: Saci1846 (thermopsin-like protease in *Sulfolobus*) is newly implicated in S-layer anchoring and requires further validation before full curation (foo2025themechanicsof pages 23-26).

5. **Existing causal graph expansion**: The existing graph "s_layer_2d_protein_array" contains 4 nodes and 3 edges. This report proposes expanding to ~50 nodes and 30 edges, which represents a substantial increase in mechanistic resolution. Curators should consider a layered approach: (a) a core universal sub-graph (S-layer protein → self-assembly → 2D lattice → cell surface coating), and (b) lineage-specific elaboration modules.

6. **Missing data**: Regulatory elements controlling S-layer gene expression remain poorly characterized across most taxa (hynonen2013lactobacillussurfacelayer pages 7-8). Transcriptional and translational regulation mechanisms are largely unexplored for most S-layer systems, limiting the ability to curate regulatory edges.

7. **Application nodes not for TraitMech**: Nanobiotechnology applications (liposome coating, vaccine delivery, biosensors) documented in Sleytr 2025 and Yuliawati 2024 reflect applied exploitation of S-layer properties and should not be curated as mechanistic trait edges unless they illuminate biological function.

References

1. (pum2013slayerproteinselfassembly pages 1-4): Dietmar Pum, Jose Toca-Herrera, and Uwe Sleytr. S-layer protein self-assembly. International Journal of Molecular Sciences, 14:2484-2501, Jan 2013. URL: https://doi.org/10.3390/ijms14022484, doi:10.3390/ijms14022484. This article has 159 citations.

2. (sleytr2025slayersfroma pages 2-4): Uwe B. Sleytr and Dietmar Pum. S-layers: from a serendipitous discovery to a toolkit for nanobiotechnology. Quarterly Reviews of Biophysics, Jan 2025. URL: https://doi.org/10.1017/s0033583524000106, doi:10.1017/s0033583524000106. This article has 7 citations and is from a peer-reviewed journal.

3. (pum2021patternsinnature—slayer pages 6-8): Dietmar Pum, Andreas Breitwieser, and Uwe B. Sleytr. Patterns in nature—s-layer lattices of bacterial and archaeal cells. Crystals, 11:869, Jul 2021. URL: https://doi.org/10.3390/cryst11080869, doi:10.3390/cryst11080869. This article has 27 citations.

4. (grillwalcher2025anewage pages 1-2): Stephanie Grill-Walcher and Christina Schäffer. A new age in structural s-layer biology: experimental and in silico milestones. Journal of Biological Chemistry, 301:110205, Jun 2025. URL: https://doi.org/10.1016/j.jbc.2025.110205, doi:10.1016/j.jbc.2025.110205. This article has 5 citations and is from a domain leading peer-reviewed journal.

5. (kirk2017characteristicsofthe pages 4-5): Joseph A. Kirk, Oishik Banerji, and Robert P. Fagan. Characteristics of the clostridium difficile cell envelope and its importance in therapeutics. Microbial Biotechnology, 10:76-90, Jun 2017. URL: https://doi.org/10.1111/1751-7915.12372, doi:10.1111/1751-7915.12372. This article has 92 citations and is from a peer-reviewed journal.

6. (gambelli2024structureofthe pages 10-12): Lavinia Gambelli, Mathew McLaren, Rebecca Conners, Kelly Sanders, Matthew C Gaines, Lewis Clark, Vicki AM Gold, Daniel Kattnig, Mateusz Sikora, Cyril Hanus, Michail N Isupov, and Bertram Daum. Structure of the two-component s-layer of the archaeon sulfolobus acidocaldarius. Jan 2024. URL: https://doi.org/10.7554/elife.84617, doi:10.7554/elife.84617. This article has 34 citations and is from a domain leading peer-reviewed journal.

7. (gambelli2024structureofthe pages 2-3): Lavinia Gambelli, Mathew McLaren, Rebecca Conners, Kelly Sanders, Matthew C Gaines, Lewis Clark, Vicki AM Gold, Daniel Kattnig, Mateusz Sikora, Cyril Hanus, Michail N Isupov, and Bertram Daum. Structure of the two-component s-layer of the archaeon sulfolobus acidocaldarius. Jan 2024. URL: https://doi.org/10.7554/elife.84617, doi:10.7554/elife.84617. This article has 34 citations and is from a domain leading peer-reviewed journal.

8. (sogues2023structureandfunction pages 1-2): Adrià Sogues, Antonella Fioravanti, Wim Jonckheere, Els Pardon, Jan Steyaert, and Han Remaut. Structure and function of the ea1 surface layer of bacillus anthracis. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42826-x, doi:10.1038/s41467-023-42826-x. This article has 16 citations and is from a highest quality peer-reviewed journal.

9. (sogues2023structureandfunction pages 2-3): Adrià Sogues, Antonella Fioravanti, Wim Jonckheere, Els Pardon, Jan Steyaert, and Han Remaut. Structure and function of the ea1 surface layer of bacillus anthracis. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42826-x, doi:10.1038/s41467-023-42826-x. This article has 16 citations and is from a highest quality peer-reviewed journal.

10. (sogues2023structureandfunction pages 7-8): Adrià Sogues, Antonella Fioravanti, Wim Jonckheere, Els Pardon, Jan Steyaert, and Han Remaut. Structure and function of the ea1 surface layer of bacillus anthracis. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42826-x, doi:10.1038/s41467-023-42826-x. This article has 16 citations and is from a highest quality peer-reviewed journal.

11. (chandra2023hostimmuneresponses pages 4-6): Harish Chandra, Rhett A. Kovall, Jagjit S. Yadav, and Xingmin Sun. Host immune responses to surface s-layer proteins (slps) of clostridioides difficile. Microorganisms, 11:380, Feb 2023. URL: https://doi.org/10.3390/microorganisms11020380, doi:10.3390/microorganisms11020380. This article has 9 citations.

12. (herdman2023cellcycledependent pages 8-11): Matthew Herdman, Andriko von Kügelgen, Ulrike Schulze, Alan Wainman, and Tanmay A.M. Bharat. Cell cycle dependent orchestration of surface layer biogenesis in caulobacter crescentus. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.14.544926, doi:10.1101/2023.06.14.544926. This article has 0 citations.

13. (herdman2023cellcycledependent pages 11-15): Matthew Herdman, Andriko von Kügelgen, Ulrike Schulze, Alan Wainman, and Tanmay A.M. Bharat. Cell cycle dependent orchestration of surface layer biogenesis in caulobacter crescentus. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.14.544926, doi:10.1101/2023.06.14.544926. This article has 0 citations.

14. (sagmeister2024themoleculararchitecture pages 1-2): Theo Sagmeister, Nina Gubensäk, Christoph Buhlheller, Christoph Grininger, Markus Eder, Anđela Ðordić, Claudia Millán, Ana Medina, Pedro Alejandro Sánchez Murcia, Francesca Berni, Ulla Hynönen, Djenana Vejzović, Elisabeth Damisch, Natalia Kulminskaya, Lukas Petrowitsch, Monika Oberer, Airi Palva, Nermina Malanović, Jeroen Codée, Walter Keller, Isabel Usón, and Tea Pavkov-Keller. The molecular architecture of lactobacillus s-layer: assembly and attachment to teichoic acids. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2401686121, doi:10.1073/pnas.2401686121. This article has 37 citations and is from a highest quality peer-reviewed journal.

15. (hynonen2013lactobacillussurfacelayer pages 7-8): Ulla Hynönen and Airi Palva. Lactobacillus surface layer proteins: structure, function and applications. Applied Microbiology and Biotechnology, 97:5225-5243, May 2013. URL: https://doi.org/10.1007/s00253-013-4962-2, doi:10.1007/s00253-013-4962-2. This article has 342 citations and is from a domain leading peer-reviewed journal.

16. (sagmeister2024themoleculararchitecture pages 9-9): Theo Sagmeister, Nina Gubensäk, Christoph Buhlheller, Christoph Grininger, Markus Eder, Anđela Ðordić, Claudia Millán, Ana Medina, Pedro Alejandro Sánchez Murcia, Francesca Berni, Ulla Hynönen, Djenana Vejzović, Elisabeth Damisch, Natalia Kulminskaya, Lukas Petrowitsch, Monika Oberer, Airi Palva, Nermina Malanović, Jeroen Codée, Walter Keller, Isabel Usón, and Tea Pavkov-Keller. The molecular architecture of lactobacillus s-layer: assembly and attachment to teichoic acids. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2401686121, doi:10.1073/pnas.2401686121. This article has 37 citations and is from a highest quality peer-reviewed journal.

17. (barwinskasendra2025evolutionaryplasticityof pages 21-21): Anna Barwinska-Sendra, Paula S. Salgado, and Kacper M. Sendra. Evolutionary plasticity of bacterial surface layer protein exoskeletons. bioRxiv, Apr 2025. URL: https://doi.org/10.1101/2025.04.02.646754, doi:10.1101/2025.04.02.646754. This article has 3 citations.

18. (herdman2023cellcycledependent pages 5-8): Matthew Herdman, Andriko von Kügelgen, Ulrike Schulze, Alan Wainman, and Tanmay A.M. Bharat. Cell cycle dependent orchestration of surface layer biogenesis in caulobacter crescentus. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.14.544926, doi:10.1101/2023.06.14.544926. This article has 0 citations.

19. (herdman2024cellcycledependent pages 4-5): Matthew Herdman, Buse Isbilir, Andriko von Kügelgen, Ulrike Schulze, Alan Wainman, and Tanmay A. M. Bharat. Cell cycle dependent coordination of surface layer biogenesis in caulobacter crescentus. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47529-5, doi:10.1038/s41467-024-47529-5. This article has 14 citations and is from a highest quality peer-reviewed journal.

20. (foo2025themechanicsof pages 23-26): Sherman Foo, Ido Caspy, Alice Cezanne, Tanmay A.M. Bharat, and Buzz Baum. The mechanics of a continuous self-assembling surface-layer aids cell division in an archaeon. bioRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.04.636414, doi:10.1101/2025.02.04.636414. This article has 1 citations.

21. (paillat2023ajourneywith pages 8-9): Maëlle Paillat, Ignacio Lunar Silva, Eric Cascales, and Thierry Doan. A journey with type ix secretion system effectors: selection, transport, processing and activities. Apr 2023. URL: https://doi.org/10.1099/mic.0.001320, doi:10.1099/mic.0.001320. This article has 46 citations and is from a peer-reviewed journal.

22. (gambelli2024structureofthe pages 12-13): Lavinia Gambelli, Mathew McLaren, Rebecca Conners, Kelly Sanders, Matthew C Gaines, Lewis Clark, Vicki AM Gold, Daniel Kattnig, Mateusz Sikora, Cyril Hanus, Michail N Isupov, and Bertram Daum. Structure of the two-component s-layer of the archaeon sulfolobus acidocaldarius. Jan 2024. URL: https://doi.org/10.7554/elife.84617, doi:10.7554/elife.84617. This article has 34 citations and is from a domain leading peer-reviewed journal.

23. (paillat2023ajourneywith pages 1-3): Maëlle Paillat, Ignacio Lunar Silva, Eric Cascales, and Thierry Doan. A journey with type ix secretion system effectors: selection, transport, processing and activities. Apr 2023. URL: https://doi.org/10.1099/mic.0.001320, doi:10.1099/mic.0.001320. This article has 46 citations and is from a peer-reviewed journal.

24. (sleytr2025slayersfroma pages 19-20): Uwe B. Sleytr and Dietmar Pum. S-layers: from a serendipitous discovery to a toolkit for nanobiotechnology. Quarterly Reviews of Biophysics, Jan 2025. URL: https://doi.org/10.1017/s0033583524000106, doi:10.1017/s0033583524000106. This article has 7 citations and is from a peer-reviewed journal.

25. (gambelli2024structureofthe pages 1-2): Lavinia Gambelli, Mathew McLaren, Rebecca Conners, Kelly Sanders, Matthew C Gaines, Lewis Clark, Vicki AM Gold, Daniel Kattnig, Mateusz Sikora, Cyril Hanus, Michail N Isupov, and Bertram Daum. Structure of the two-component s-layer of the archaeon sulfolobus acidocaldarius. Jan 2024. URL: https://doi.org/10.7554/elife.84617, doi:10.7554/elife.84617. This article has 34 citations and is from a domain leading peer-reviewed journal.

26. (herdman2024cellcycledependent pages 1-2): Matthew Herdman, Buse Isbilir, Andriko von Kügelgen, Ulrike Schulze, Alan Wainman, and Tanmay A. M. Bharat. Cell cycle dependent coordination of surface layer biogenesis in caulobacter crescentus. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47529-5, doi:10.1038/s41467-024-47529-5. This article has 14 citations and is from a highest quality peer-reviewed journal.

27. (pum2021patternsinnature—slayer pages 2-4): Dietmar Pum, Andreas Breitwieser, and Uwe B. Sleytr. Patterns in nature—s-layer lattices of bacterial and archaeal cells. Crystals, 11:869, Jul 2021. URL: https://doi.org/10.3390/cryst11080869, doi:10.3390/cryst11080869. This article has 27 citations.

28. (pum2013slayerproteinselfassembly pages 4-6): Dietmar Pum, Jose Toca-Herrera, and Uwe Sleytr. S-layer protein self-assembly. International Journal of Molecular Sciences, 14:2484-2501, Jan 2013. URL: https://doi.org/10.3390/ijms14022484, doi:10.3390/ijms14022484. This article has 159 citations.

29. (sleytr2025slayersfroma pages 18-19): Uwe B. Sleytr and Dietmar Pum. S-layers: from a serendipitous discovery to a toolkit for nanobiotechnology. Quarterly Reviews of Biophysics, Jan 2025. URL: https://doi.org/10.1017/s0033583524000106, doi:10.1017/s0033583524000106. This article has 7 citations and is from a peer-reviewed journal.

30. (herdman2024cellcycledependent pages 8-9): Matthew Herdman, Buse Isbilir, Andriko von Kügelgen, Ulrike Schulze, Alan Wainman, and Tanmay A. M. Bharat. Cell cycle dependent coordination of surface layer biogenesis in caulobacter crescentus. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47529-5, doi:10.1038/s41467-024-47529-5. This article has 14 citations and is from a highest quality peer-reviewed journal.

31. (hynonen2013lactobacillussurfacelayer pages 1-2): Ulla Hynönen and Airi Palva. Lactobacillus surface layer proteins: structure, function and applications. Applied Microbiology and Biotechnology, 97:5225-5243, May 2013. URL: https://doi.org/10.1007/s00253-013-4962-2, doi:10.1007/s00253-013-4962-2. This article has 342 citations and is from a domain leading peer-reviewed journal.

32. (barwinskasendra2025evolutionaryplasticityof pages 33-35): Anna Barwinska-Sendra, Paula S. Salgado, and Kacper M. Sendra. Evolutionary plasticity of bacterial surface layer protein exoskeletons. bioRxiv, Apr 2025. URL: https://doi.org/10.1101/2025.04.02.646754, doi:10.1101/2025.04.02.646754. This article has 3 citations.

33. (sleytr2025slayersfroma pages 4-5): Uwe B. Sleytr and Dietmar Pum. S-layers: from a serendipitous discovery to a toolkit for nanobiotechnology. Quarterly Reviews of Biophysics, Jan 2025. URL: https://doi.org/10.1017/s0033583524000106, doi:10.1017/s0033583524000106. This article has 7 citations and is from a peer-reviewed journal.

34. (pum2013slayerproteinselfassembly pages 6-10): Dietmar Pum, Jose Toca-Herrera, and Uwe Sleytr. S-layer protein self-assembly. International Journal of Molecular Sciences, 14:2484-2501, Jan 2013. URL: https://doi.org/10.3390/ijms14022484, doi:10.3390/ijms14022484. This article has 159 citations.

35. (sogues2023structureandfunction pages 3-4): Adrià Sogues, Antonella Fioravanti, Wim Jonckheere, Els Pardon, Jan Steyaert, and Han Remaut. Structure and function of the ea1 surface layer of bacillus anthracis. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42826-x, doi:10.1038/s41467-023-42826-x. This article has 16 citations and is from a highest quality peer-reviewed journal.