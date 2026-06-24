---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:18:21.894322'
end_time: '2026-06-18T10:33:52.780788'
duration_seconds: 930.89
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: twitching motility
  trait_identifier: traitmech:000061
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: twitching_motility
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A flagella-independent surface motility driven by the extension, attachment,
    and retraction of type IV pili, producing intermittent, jerky translocation of
    cells across moist surfaces.
  parent_traits: METPO:1000702
  synonyms: twitching
  evidence_summary: 'DOI:10.1146/annurev.micro.56.012302.160938:  (Mattick, "Type
    IV pili and twitching motility", describes twitching as type-IV-pilus-driven surface
    translocation operating like a grappling hook.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey,
    "Bacterial motility on a surface", places twitching among the distinct surface-translocation
    strategies of bacteria.)'
  causal_graph_summary: 'twitching_type_iv_pilus_retraction: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** twitching motility
- **METPO identifier:** traitmech:000061
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagella-independent surface motility driven by the extension, attachment, and retraction of type IV pili, producing intermittent, jerky translocation of cells across moist surfaces.
- **Parent traits:** METPO:1000702
- **Synonyms:** twitching
- **Existing evidence:** DOI:10.1146/annurev.micro.56.012302.160938:  (Mattick, "Type IV pili and twitching motility", describes twitching as type-IV-pilus-driven surface translocation operating like a grappling hook.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey, "Bacterial motility on a surface", places twitching among the distinct surface-translocation strategies of bacteria.)
- **Existing causal graph summary:** twitching_type_iv_pilus_retraction: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **twitching motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/twitching_motility.yaml`.

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
- **Trait label:** twitching motility
- **METPO identifier:** traitmech:000061
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagella-independent surface motility driven by the extension, attachment, and retraction of type IV pili, producing intermittent, jerky translocation of cells across moist surfaces.
- **Parent traits:** METPO:1000702
- **Synonyms:** twitching
- **Existing evidence:** DOI:10.1146/annurev.micro.56.012302.160938:  (Mattick, "Type IV pili and twitching motility", describes twitching as type-IV-pilus-driven surface translocation operating like a grappling hook.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey, "Bacterial motility on a surface", places twitching among the distinct surface-translocation strategies of bacteria.)
- **Existing causal graph summary:** twitching_type_iv_pilus_retraction: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **twitching motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/twitching_motility.yaml`.

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


# Twitching motility (METPO: traitmech:000061) — Curation-focused research report

## 0. Scope summary (trait definition and boundaries)

**Trait meaning.** Twitching motility is a **surface-associated, flagella-independent translocation** driven by **type IV pili (T4P)** that “effectively [pull] the cell across a surface through a complex process of cooperative binding, pulling, and unbinding” (Pseudomonas aeruginosa PA14 model). (geiger2024abacterialsense pages 1-3)

**Observable phenotype (assay-level).** In P. aeruginosa PA14, twitching is typically slow on average (~0.3 µm/s) with intermittent faster bursts (~1 µm/s), consistent with step-like pilus retraction events. (geiger2024abacterialsense pages 3-5)

**Boundary cases / near-neighbor traits.**
- **Not flagellar swimming/swarming:** twitching is **T4P-based** rather than flagellar rotation; surface context can shift signaling and behavior between a **T4P/cAMP program** and a **flagellum/c-di-GMP program**. (zheng2024thesurfaceinterface pages 1-2)
- **Not other “gliding” systems:** twitching is a “pulling” mechanism (T4P extension–attachment–retraction cycles), unlike secretion-driven or focal-adhesion-like gliding. (costin2023themovementbehaviour pages 23-27)
- **Archaea boundary expansion:** twitching-like, saltatory surface motion can occur in archaea via retractable **adhesion pili** even without canonical PilT homologs, indicating twitching is best scoped as **retractile type-IV-filament-like** surface translocation rather than strictly PilT-dependent. (charlesorszag2024adhesionpilusretraction pages 1-2)

## 1. Key concepts and definitions (current understanding)

### 1.1 Core mechanical cycle
A minimal mechanistic definition supported across recent sources is:
1) **Pilus extension** (polymerization of pilin subunits) → 2) **surface attachment** → 3) **retraction** (depolymerization) that generates pulling force → 4) net surface displacement (“twitching”). (geiger2024abacterialsense pages 1-3, costin2023themovementbehaviour pages 23-27)

### 1.2 Type IV pilus machine architecture (curatable components)
High-resolution in situ structural work in P. aeruginosa places twitching in the context of a multi-layer envelope-spanning nanomachine:
- **Outer membrane secretin:** PilQ forms the outer-membrane channel; in Pelicic’s synthesis, PilQ is required for **surface exposure** (pilQ pilT mutants assemble filaments trapped in the periplasm). (pelicic2023mechanismofassembly pages 3-5)
- **Alignment subcomplex:** PilP/PilO/PilN/PilM explicitly constitute the alignment complex connecting outer-membrane and inner-membrane components. (guo2024pily1regulatesthe pages 1-2)
- **Inner membrane platform:** PilC coordinates with ATPase motors to drive pilin assembly/disassembly. (guo2024pily1regulatesthe pages 1-2)
- **Priming/tip machinery:** assembly is “primed by the minor pilin proteins (FimU, PilV, PilW, PilX and PilE) and a non-pilin protein, PilY1.” (guo2024pily1regulatesthe pages 1-2)

A schematic model depicting these labeled parts (PilQ; PilM/N/O/P; PilC; PilY1/minor pilins) was retrieved for curator reference. (guo2024pily1regulatesthe media 2c9d0e01)

### 1.3 Force generation and physical magnitude (statistics)
T4P retraction is among the strongest known microbial motors:
- In the P. aeruginosa-focused surface-sensing review, typical forces are summarized as **~30 pN per pilus on average** in P. aeruginosa; “single pili…can reach **>100 pN**,” bundles can reach **~1 nN**, and single-pilus adhesive forces up to **750 pN** have been measured (AFM). (geiger2024abacterialsense pages 3-5)
- A 2024 archaeal twitching study reiterates PilT-mediated bacterial retraction can reach **~100 pN** and speeds up to **~1 µm s−1** (as background context), then demonstrates twitching under extreme conditions in Sulfolobus. (charlesorszag2024adhesionpilusretraction pages 1-2)

## 2. Recent developments and latest research (prioritizing 2023–2024)

### 2.1 In situ architecture and a “gate-keeping” model (2024)
Cryo-electron tomography and integrative modeling provide a 2024 in situ view of the P. aeruginosa T4P machine, including PilQ secretin, alignment complex, PilC platform, and a PilY1 structure that can occlude the secretin channel (“champagne-cork-shaped”), motivating a gate-keeping concept for controlling dynamic pilus states. (guo2024pily1regulatesthe pages 1-2)

### 2.2 Surface sensing and signaling integration via retraction motors (2024)
A 2024 Journal of Bacteriology review frames twitching as part of a **surface-sensing** lifecycle: P. aeruginosa surface engagement increases **cAMP** over multiple generations via Pil-Chp, with downstream activation through the cAMP-binding transcription factor Vfr. (geiger2024abacterialsense pages 1-3)

### 2.3 Regulatory logic linking Pil-Chp → cAMP and PilB control (2024)
A 2024 minireview on PilB regulation provides a mechanistic signaling chain suited for curation:
- PilB docks with PilM and interfaces with PilC; PilT competes/exchanges stochastically with PilB at the same socket. (roberge2024buildingpermits—controlof pages 1-3)
- PilJ senses signals from pilus dynamics and routes through ChpA to PilG/PilH; phosphorylated PilG stimulates adenylate cyclase CyaB to increase cAMP, which with Vfr upregulates T4P genes. (roberge2024buildingpermits—controlof pages 1-3)
- The same source connects c-di-GMP microcircuits to PilB positioning (FimX/PilZ, EAL/DGC modules), supporting a multi-messenger control architecture. (roberge2024buildingpermits—controlof pages 1-3)

### 2.4 Environmental context flips between cAMP/twitching and c-di-GMP/biofilm modes (2024)
A 2024 PNAS study reports that **interface conditions** determine which surface program dominates:
- Agarose–**air** interface: activates **cAMP** via T4P and Pil-Chp, aligning with twitching-associated behaviors. (zheng2024thesurfaceinterface pages 1-2)
- **Aqueous** phase over surface (liquid–agarose): favors **c-di-GMP** signaling dependent on the **flagellar apparatus**, consistent with matrix/biofilm programs. (zheng2024thesurfaceinterface pages 1-2)

### 2.5 Material mechanics and mesh size as an upstream environmental control (2023)
A 2023 mBio study directly links substrate physical properties to twitching and clinically relevant outcomes:
- Twitching speed correlates more strongly with **hydrogel mesh size** (r = −0.81) than Young’s modulus (r = 0.69), and twitching increases for mesh sizes **below ~5 nm** (comparable to pilus diameter). (cont2023materialsubstratephysical pages 4-6)
- Biofilm tolerance to colistin after 46 h growth + 1 h colistin exposure increases with mesh size (reported survival up to ~80% on large-mesh hydrogels vs ~25% on glass). (cont2023materialsubstratephysical pages 6-8)
- Importantly, cAMP and c-di-GMP reporter intensities showed **no detectable differences across gel compositions on the twitching timescale**, supporting a model where attachment probability/geometry can dominate over second-messenger changes under these conditions. (cont2023materialsubstratephysical pages 4-6)

### 2.6 Twitching beyond bacteria: archaeal retractile pili (2024)
A 2024 Nature Communications paper demonstrates twitching motility in **Sulfolobus acidocaldarius** at **75 °C, pH 2**, driven by retractable **Aap adhesion pili**. Deleting the assembly protein **AapF** abolishes twitching, with strong quantitative reductions in displacement/persistence compared with WT-like controls. (charlesorszag2024adhesionpilusretraction pages 1-2)

## 3. Current applications and real-world implementations

### 3.1 Biofilm initiation, architecture control, and antibiotic tolerance (applied microbiology / infection)
Twitching is frequently treated as a **surface exploration** mode that primes biofilm development; the 2023 hydrogel study provides a clear applied link: **twitching-regulated biofilm architecture** changes **colistin susceptibility**, producing protected cores in denser architectures and more uniform killing in flatter architectures. (cont2023materialsubstratephysical pages 6-8)

### 3.2 Surfaces and interfaces relevant to medical and environmental settings
The interface-dependence identified in 2024 (air-exposed vs aqueous-over-surface) provides a mechanistic basis to interpret why P. aeruginosa may exhibit different colonization programs on **air-exposed mucosal/medical-device microenvironments** vs fully submerged surfaces, with implications for controlling early attachment and biofilm transitions. (zheng2024thesurfaceinterface pages 1-2)

### 3.3 Antivirulence targeting opportunities (mechanism-informed)
Recent reviews emphasize that because T4P are important virulence factors, disrupting **extension motor regulation** (PilB and cofactors) and its messenger-controlled logic may be a rational strategy to disable T4P-dependent physiology, including surface motility. (roberge2024buildingpermits—controlof pages 1-3)

## 4. Expert synthesis and analysis (authoritative viewpoints)

### 4.1 “Sense of touch” model for PilT-mediated surface sensing
Geiger et al. (2024) emphasize that twitching is not just locomotion but is integrated into surface sensing and adaptation: surface engagement triggers increased cAMP via Pil-Chp and Vfr-regulated pathways, and the authors propose an integrated model where the retraction motor PilT relays surface engagement signals via PilJ to Pil-Chp. (geiger2024abacterialsense pages 1-3)

### 4.2 Architecture as a control point for dynamics
Guo et al. (2024) interpret the PilQ–PilY1 relationship as a potential gating mechanism that may optimize conformations of the T4P machine and regulate pilus dynamics, a perspective supported by in situ structural data. (guo2024pily1regulatesthe pages 1-2)

### 4.3 Environment-first controls on twitching speed
Cont et al. (2023) argue that mesh-size–dependent attachment probability can govern twitching speed and downstream biofilm architecture without requiring detectable cAMP/c-di-GMP differences on the twitching timescale, illustrating how physical environment can dominate short-timescale phenotype expression. (cont2023materialsubstratephysical pages 4-6)

## 5. Candidate nodes (grouped by type) for `twitching_motility.yaml`

### 5.1 Phenotype/process nodes
- Twitching motility (METPO:traitmech:000061)
- Type IV pilus extension (GO candidate; verify exact term) (roberge2024buildingpermits—controlof pages 1-3)
- Type IV pilus retraction (GO candidate; verify exact term) (roberge2024buildingpermits—controlof pages 1-3)
- Surface adhesion (GO:0007155) (guo2024pily1regulatesthe pages 1-2)
- Surface sensing / mechanosensing (label-only candidate process) (geiger2024abacterialsense pages 1-3)

### 5.2 Molecular machine components (proteins/complexes; grounding often taxon-specific)
- PilQ secretin (label-only; OM secretin) (pelicic2023mechanismofassembly pages 3-5, guo2024pily1regulatesthe pages 1-2)
- Alignment complex PilM/PilN/PilO/PilP (label-only complex) (guo2024pily1regulatesthe pages 1-2)
- PilC inner-membrane platform (label-only) (guo2024pily1regulatesthe pages 1-2)
- PilB extension ATPase (label-only) (roberge2024buildingpermits—controlof pages 1-3)
- PilT retraction ATPase (label-only) (roberge2024buildingpermits—controlof pages 1-3)
- PilU accessory retraction ATPase (label-only; Pseudomonas-centric) (geiger2024abacterialsense pages 3-5, costin2023themovementbehaviour pages 23-27)
- Minor pilins: FimU/PilV/PilW/PilX/PilE (label-only set/complex) (guo2024pily1regulatesthe pages 1-2)
- PilY1 (adhesin/mechanosensor; calcium-dependent effects suggested) (guo2024pily1regulatesthe pages 1-2)

### 5.3 Regulatory pathway nodes
- Pil-Chp chemosensory-like system (label-only pathway) (roberge2024buildingpermits—controlof pages 1-3)
- PilJ chemoreceptor (label-only) (roberge2024buildingpermits—controlof pages 1-3)
- ChpA kinase; PilG/PilH response regulators (label-only) (roberge2024buildingpermits—controlof pages 1-3)
- Adenylate cyclase CyaB (label-only) → cAMP (roberge2024buildingpermits—controlof pages 1-3)
- Vfr (cAMP-binding transcription factor; label-only) (geiger2024abacterialsense pages 1-3)
- FimX, PilZ (c-di-GMP-linked regulators; label-only) (roberge2024buildingpermits—controlof pages 1-3)

### 5.4 Chemicals / second messengers
- cAMP (CHEBI:17489) (geiger2024abacterialsense pages 1-3, roberge2024buildingpermits—controlof pages 1-3)
- c-di-GMP (CHEBI:17237; referenced as cdGMP) (roberge2024buildingpermits—controlof pages 1-3, zheng2024thesurfaceinterface pages 1-2)
- ATP (CHEBI:15422; implicit motor fuel) (geiger2024abacterialsense pages 1-3)

### 5.5 Environmental / experimental factor nodes
- Surface engagement / surface contact (ENVO candidate) (geiger2024abacterialsense pages 1-3)
- Air–surface interface vs aqueous-over-surface interface (ENVO candidates; grounding TBD) (zheng2024thesurfaceinterface pages 1-2)
- Substrate mesh size (material property node) and Young’s modulus (material property node) (cont2023materialsubstratephysical pages 4-6)
- Hydrogel precursor composition (PEGDA molecular weight, % wt/vol) (cont2023materialsubstratephysical pages 2-4)
- Physiological extremes: 75 °C, pH 2 (ENVO/NCBITaxon context) (charlesorszag2024adhesionpilusretraction pages 1-2)

## 6. Candidate causal edges (evidence-backed triples)

The table below is formatted for direct curation into a TraitMech-style causal graph.

| Subject node (label + suggested CURIE) | Predicate (causal) | Object node (label + suggested CURIE) | Evidence snippet/quote | Source (DOI + URL + publication date) | Notes (taxon/assay specificity, uncertainty) |
|---|---|---|---|---|---|
| PilB extension ATPase (label-only candidate; often PilB/PilF family) | drives | type IV pilus extension (GO:0044781 candidate) | “T4P are dynamic, undergoing rapid cycles of filament extension and retraction facilitated by a complex protein nanomachine powered by cytoplasmic motor ATPases.” Also: “Extension is driven by PilB bound to PilC.” (roberge2024buildingpermits—controlof pages 1-3, costin2023themovementbehaviour pages 23-27) | Roberge & Burrows 2024, DOI:10.1128/jb.00359-24, https://doi.org/10.1128/jb.00359-24, Dec 2024; Costin 2023 excerpt | Strong mechanistic consensus; GO term should be verified before curation. Costin excerpt is secondary synthesis. |
| PilT retraction ATPase (label-only candidate) | drives | type IV pilus retraction (GO:1904890 candidate) | “Retraction is driven by PilT, which engages with PilC within the same cytoplasmic socket.” (roberge2024buildingpermits—controlof pages 1-3) | Roberge & Burrows 2024, DOI:10.1128/jb.00359-24, https://doi.org/10.1128/jb.00359-24, Dec 2024 | Strong for bacterial T4aP systems; ontology grounding for retraction process may require manual check. |
| PilU accessory retraction ATPase (label-only candidate) | contributes to | type IV pilus retraction (GO:1904890 candidate) | “Retraction occurs when PilB decouples and PilT or PilU bind to depolymerize PilA.” (costin2023themovementbehaviour pages 23-27) | Costin 2023 excerpt | Useful but based on a mechanistic synthesis excerpt; curate as supporting/less direct than PilT. |
| type IV pilus retraction (GO:1904890 candidate) | enables | twitching motility (METPO:traitmech:000061) | Twitching is described as movement that “effectively [pulls] the cell across a surface through a complex process of cooperative binding, pulling, and unbinding.” (geiger2024abacterialsense pages 1-3) | Geiger et al. 2024, DOI:10.1128/jb.00442-23, https://doi.org/10.1128/jb.00442-23, Jul 2024 | Core trait-defining edge; strong. |
| PilC inner-membrane platform protein (label-only candidate) | coordinates with | PilB/PilT motor switching (label-only candidate) | “PilC is identified as the inner-membrane platform that ‘coordinates with ATPase motors to drive assembly and disassembly’ of pilin subunits.” (guo2024pily1regulatesthe pages 1-2) | Guo et al. 2024, DOI:10.1038/s41467-024-53638-y, https://doi.org/10.1038/s41467-024-53638-y, Oct 2024 | Structural/mechanistic edge; object may be better modeled as T4P assembly-disassembly rather than specific motor switching. |
| PilQ secretin (label-only candidate) | enables surface exposure of | type IV pilus filament (GO:0009289 candidate) | “pilQ pilT mutants assemble filaments that are trapped in the periplasm, indicating PilQ is required for surface exposure though not strictly for filament assembly.” (pelicic2023mechanismofassembly pages 3-5) | Pelicic 2023, DOI:10.1099/mic.0.001311, https://doi.org/10.1099/mic.0.001311, Mar 2023 | Strong architectural edge; trait-relevant but indirect. |
| PilM/N/O/P alignment complex (label-only candidate complex) | forms part of | type IV pilus machine (GO:0044780 candidate) | The T4P machine includes an alignment subcomplex “consisting of PilP, PilO, PilN, and PilM.” (guo2024pily1regulatesthe pages 1-2) | Guo et al. 2024, DOI:10.1038/s41467-024-53638-y, https://doi.org/10.1038/s41467-024-53638-y, Oct 2024 | Structural node; indirect for phenotype but useful for graph completeness. |
| minor pilin complex (FimU/PilV/PilW/PilX/PilE; label-only candidate complex) | primes | type IV pilus assembly (GO:0044780 candidate) | “The assembly is ‘primed by the minor pilin proteins (FimU, PilV, PilW, PilX and PilE) and a non-pilin protein, PilY1.’” (guo2024pily1regulatesthe pages 1-2) | Guo et al. 2024, DOI:10.1038/s41467-024-53638-y, https://doi.org/10.1038/s41467-024-53638-y, Oct 2024 | Good candidate edge; taxon-specific to P. aeruginosa architecture but broadly plausible in T4aP. |
| PilY1 adhesin/mechanosensor (label-only candidate) | promotes | surface adhesion (GO:0007155) | PilY1 “acts as an adhesion protein that binds bacteria to diverse substrates.” (guo2024pily1regulatesthe pages 1-2) | Guo et al. 2024, DOI:10.1038/s41467-024-53638-y, https://doi.org/10.1038/s41467-024-53638-y, Oct 2024 | Strong for adhesion; links to twitching likely indirect unless combined with retraction/attachment cycle. |
| PilY1 (label-only candidate) | regulates | twitching motility (METPO:traitmech:000061) | PilY1 “has been suggested to play key roles as a calcium-dependent regulator of twitching motility.” (guo2024pily1regulatesthe pages 1-2) | Guo et al. 2024, DOI:10.1038/s41467-024-53638-y, https://doi.org/10.1038/s41467-024-53638-y, Oct 2024 | Mark uncertain: review of prior work and wording “suggested”; calcium dependence may be taxon/assay specific. |
| PilJ chemoreceptor (label-only candidate) | activates | Pil-Chp signaling system (label-only candidate pathway) | “PilJ senses a signal from pilus dynamics, activating ChpA and response regulators PilG/PilH.” (roberge2024buildingpermits—controlof pages 1-3) | Roberge & Burrows 2024, DOI:10.1128/jb.00359-24, https://doi.org/10.1128/jb.00359-24, Dec 2024 | Strong regulatory edge in P. aeruginosa; likely species-focused. |
| Pil-Chp signaling system (label-only candidate pathway) | increases | cAMP (CHEBI:17489) | “Phosphorylated PilG stimulates…the adenylate cyclase CyaB” producing cAMP. (roberge2024buildingpermits—controlof pages 1-3) | Roberge & Burrows 2024, DOI:10.1128/jb.00359-24, https://doi.org/10.1128/jb.00359-24, Dec 2024 | Strong for P. aeruginosa surface-sensing branch. |
| cAMP (CHEBI:17489) | promotes transcription of | type IV pilus genes (label-only candidate gene set) | “CyaB raises intracellular cAMP that, with Vfr, upregulates T4P gene transcription.” (roberge2024buildingpermits—controlof pages 3-5) | Roberge & Burrows 2024, DOI:10.1128/jb.00359-24, https://doi.org/10.1128/jb.00359-24, Dec 2024 | Strong regulatory edge; likely mediated via Vfr, which could be inserted as an intermediate node. |
| cAMP (CHEBI:17489) | promotes | surface adaptation/virulence program (label-only candidate process) | “This rise in cAMP allows cells and their progeny to become better adapted for surface attachment and activates virulence pathways through the cAMP-binding transcription factor Vfr.” (geiger2024abacterialsense pages 1-3) | Geiger et al. 2024, DOI:10.1128/jb.00442-23, https://doi.org/10.1128/jb.00442-23, Jul 2024 | Strong but broader than twitching; useful contextual edge. |
| air–surface interface (ENVO candidate: air-liquid/air-solid interface, exact CURIE TBD) | activates | cAMP signaling (CHEBI:17489-associated process) | “An agarose–air interface activates cAMP signaling via type IV pili and the Pil-Chp system.” (zheng2024thesurfaceinterface pages 1-2) | Zheng et al. 2024, DOI:10.1073/pnas.2411981121, https://doi.org/10.1073/pnas.2411981121, Sep 2024 | Environmental edge; exact ENVO grounding needs verification. |
| aqueous-over-surface interface (ENVO candidate; exact CURIE TBD) | favors | c-di-GMP signaling (CHEBI:17237-associated process) | “a liquid–agarose (aqueous-over-surface) interface favors c-di-GMP signaling, a response that is dependent on the flagellar apparatus” (zheng2024thesurfaceinterface pages 1-2) | Zheng et al. 2024, DOI:10.1073/pnas.2411981121, https://doi.org/10.1073/pnas.2411981121, Sep 2024 | Important boundary-context edge; may distinguish when twitching-dominant vs biofilm-dominant surface responses occur. |
| cAMP signaling (CHEBI:17489-associated process) | promotes | twitching motility (METPO:traitmech:000061) | Zheng et al. note cAMP signaling at the air interface supports “surface-associated twitching”; Geiger notes cAMP is linked to T4P-dependent surface adaptation. (zheng2024thesurfaceinterface pages 1-2, geiger2024abacterialsense pages 1-3) | Zheng et al. 2024, DOI:10.1073/pnas.2411981121, https://doi.org/10.1073/pnas.2411981121, Sep 2024; Geiger et al. 2024, DOI:10.1128/jb.00442-23, https://doi.org/10.1128/jb.00442-23, Jul 2024 | Supportive but somewhat indirect; consider as regulatory/context edge rather than minimal core mechanism. |
| hydrogel mesh size <~5 nm (material property; label-only candidate) | increases | twitching motility speed (label-only candidate assay phenotype) | “Twitching speeds increase on hydrogels with mesh sizes below ~5 nm.” (cont2023materialsubstratephysical pages 4-6) | Cont et al. 2023, DOI:10.1128/mbio.03518-22, https://doi.org/10.1128/mbio.03518-22, Apr 2023 | Strong experimental environmental edge in P. aeruginosa on PEGDA hydrogels. |
| larger hydrogel mesh size (material property; label-only candidate) | decreases | twitching motility speed (label-only candidate assay phenotype) | Population mean twitching speed showed a “stronger negative correlation with hydrogel mesh size (reported as r = -0.81).” (cont2023materialsubstratephysical pages 4-6) | Cont et al. 2023, DOI:10.1128/mbio.03518-22, https://doi.org/10.1128/mbio.03518-22, Apr 2023 | Quantitative edge; assay/material specific. |
| increased twitching motility (label-only candidate assay phenotype) | produces | flatter / monolayer-favoring biofilm architecture (label-only candidate phenotype) | On short-chain gels cells were “much more motile” and produced uniform coverage; monolayer-like architecture was observed under high-twitching conditions. (cont2023materialsubstratephysical pages 2-4) | Cont et al. 2023, DOI:10.1128/mbio.03518-22, https://doi.org/10.1128/mbio.03518-22, Apr 2023 | Strong within this assay system; phenotype object may need controlled vocabulary later. |
| reduced twitching motility (label-only candidate assay phenotype) | produces | tall dome-like biofilm architecture (label-only candidate phenotype) | Cells “barely migrated” on dome-favoring gels; large-mesh-size hydrogels inhibited motility and produced dense, low surface-to-volume ratio biofilms. (cont2023materialsubstratephysical pages 2-4, cont2023materialsubstratephysical pages 6-8) | Cont et al. 2023, DOI:10.1128/mbio.03518-22, https://doi.org/10.1128/mbio.03518-22, Apr 2023 | Strong assay-specific edge. |
| tall dome-like / dense low-SV biofilm architecture (label-only candidate phenotype) | increases | colistin tolerance (CHEBI:5291) | “Survival after treatment rose…up to ~80% on larger-mesh-size hydrogels,” and dense architectures had protected cores, whereas glass biofilms showed only “~25% survival.” (cont2023materialsubstratephysical pages 6-8) | Cont et al. 2023, DOI:10.1128/mbio.03518-22, https://doi.org/10.1128/mbio.03518-22, Apr 2023 | Strong experimental outcome edge; mediated by architecture rather than twitching directly. |
| small-mesh hydrogel / high-twitching condition (label-only candidate environmental state) | increases | clonal lineage mixing (label-only candidate population phenotype) | Mean first-nearest-neighbor distance decreased “from 20 mm on large-mesh hydrogels to 3 mm on the smallest-mesh hydrogels,” indicating increased mixing. (cont2023materialsubstratephysical pages 8-10) | Cont et al. 2023, DOI:10.1128/mbio.03518-22, https://doi.org/10.1128/mbio.03518-22, Apr 2023 | Useful ecological/application edge; likely downstream, not core trait mechanism. |
| AapF adhesion-pilus assembly protein (label-only candidate; archaeal) | required for | Aap pilus assembly/function (label-only candidate process) | “Deletion of the adhesion-pilus assembly protein AapF (ΔaapF) abolished twitching.” (charlesorszag2024adhesionpilusretraction pages 1-2) | Charles-Orszag et al. 2024, DOI:10.1038/s41467-024-49101-7, https://doi.org/10.1038/s41467-024-49101-7, Jun 2024 | Archaeal-specific branch; AapF likely upstream of Aap pilus function. |
| Aap pili (archaeal adhesion pili; label-only candidate) | drive | twitching motility (METPO:traitmech:000061) | “Sulfolobus acidocaldarius exhibits bona fide twitching…driven specifically by Aap (adhesion) pili.” (charlesorszag2024adhesionpilusretraction pages 1-2) | Charles-Orszag et al. 2024, DOI:10.1038/s41467-024-49101-7, https://doi.org/10.1038/s41467-024-49101-7, Jun 2024 | Important boundary-expanding edge: shows twitching-like trait in archaea without canonical PilT homolog. |
| PilT-independent pilus retraction (label-only candidate; archaeal inference) | can enable | twitching motility (METPO:traitmech:000061) | Aap pili are “capable of retraction in the absence of a PilT homolog,” and this retraction powers twitching in S. acidocaldarius. (charlesorszag2024adhesionpilusretraction pages 1-2) | Charles-Orszag et al. 2024, DOI:10.1038/s41467-024-49101-7, https://doi.org/10.1038/s41467-024-49101-7, Jun 2024 | Important but should be flagged uncertain/generalized beyond this archaeal system; do not overextend to bacteria. |


*Table: This table lists candidate subject–predicate–object edges for curating a TraitMech causal graph of twitching motility, with supporting quotes, source metadata, and notes on scope or uncertainty. It prioritizes experimentally supported mechanistic, regulatory, and environmental relationships from recent authoritative sources.*

## 7. Warnings / curation notes (do-not-curate-yet or mark uncertain)

1. **PilY1 “calcium-dependent regulator of twitching”:** Guo et al. phrase this as “has been suggested,” so treat as **weaker/secondary** unless the primary calcium-dependence source is also curated. (guo2024pily1regulatesthe pages 1-2)
2. **PilT-independent retraction as a general mechanism:** strong for Sulfolobus Aap pili, but should be scoped as **archaeal/taxon-specific** and not generalized to bacterial PilT systems without additional evidence. (charlesorszag2024adhesionpilusretraction pages 1-2)
3. **ENVO grounding for “air–surface interface” and “aqueous-over-surface interface”:** the biological distinction is well supported, but precise CURIEs should be confirmed before final YAML grounding. (zheng2024thesurfaceinterface pages 1-2)
4. **Some node groundings are label-only:** proteins (PilB/PilT/PilQ/PilC, etc.) can be grounded to UniProt/NCBI Gene IDs in a taxon-specific curation step; current evidence supports inclusion as **mechanistic entities** but not their universal identifiers. (roberge2024buildingpermits—controlof pages 1-3, guo2024pily1regulatesthe pages 1-2)

## 8. DOI-first bibliography (with URLs and publication dates)

- **Geiger CJ, Wong GCL, O’Toole GA.** “A bacterial sense of touch: T4P retraction motor as a means of surface sensing by *Pseudomonas aeruginosa* PA14.” *Journal of Bacteriology* (Jul 2024). DOI: **10.1128/jb.00442-23**. https://doi.org/10.1128/jb.00442-23 (geiger2024abacterialsense pages 1-3, geiger2024abacterialsense pages 3-5)
- **Roberge NA, Burrows LL.** “Building permits—control of type IV pilus assembly by PilB and its cofactors.” *Journal of Bacteriology* (Dec 2024). DOI: **10.1128/jb.00359-24**. https://doi.org/10.1128/jb.00359-24 (roberge2024buildingpermits—controlof pages 1-3, roberge2024buildingpermits—controlof pages 3-5)
- **Guo S, Chang Y, Brun YV, Howell PL, Burrows LL, Liu J.** “PilY1 regulates the dynamic architecture of the type IV pilus machine in *Pseudomonas aeruginosa*.” *Nature Communications* (Oct 2024). DOI: **10.1038/s41467-024-53638-y**. https://doi.org/10.1038/s41467-024-53638-y (guo2024pily1regulatesthe pages 1-2, guo2024pily1regulatesthe media 2c9d0e01)
- **Zheng X, Gomez-Rivas EJ, Lamont SI, et al.** “The surface interface and swimming motility influence surface-sensing responses in *Pseudomonas aeruginosa*.” *PNAS* (Sep 2024). DOI: **10.1073/pnas.2411981121**. https://doi.org/10.1073/pnas.2411981121 (zheng2024thesurfaceinterface pages 1-2, zheng2024thesurfaceinterface pages 10-11)
- **Charles-Orszag A, van Wolferen M, Lord SJ, Albers S-V, Mullins RD.** “Adhesion pilus retraction powers twitching motility in the thermoacidophilic crenarchaeon *Sulfolobus acidocaldarius*.” *Nature Communications* (Jun 2024). DOI: **10.1038/s41467-024-49101-7**. https://doi.org/10.1038/s41467-024-49101-7 (charlesorszag2024adhesionpilusretraction pages 1-2)
- **Cont A, Vermeil J, Persat A.** “Material Substrate Physical Properties Control *Pseudomonas aeruginosa* Biofilm Architecture.” *mBio* (Apr 2023). DOI: **10.1128/mbio.03518-22**. https://doi.org/10.1128/mbio.03518-22 (cont2023materialsubstratephysical pages 2-4, cont2023materialsubstratephysical pages 4-6, cont2023materialsubstratephysical pages 6-8)
- **Pelicic V.** “Mechanism of assembly of type 4 filaments: everything you always wanted to know (but were afraid to ask).” *Microbiology* (Mar 2023). DOI: **10.1099/mic.0.001311**. https://doi.org/10.1099/mic.0.001311 (pelicic2023mechanismofassembly pages 3-5)



References

1. (geiger2024abacterialsense pages 1-3): C. J. Geiger, G. C. L. Wong, and G. A. O'Toole. A bacterial sense of touch: t4p retraction motor as a means of surface sensing by <i>pseudomonas aeruginosa</i> pa14. Journal of Bacteriology, Jul 2024. URL: https://doi.org/10.1128/jb.00442-23, doi:10.1128/jb.00442-23. This article has 21 citations and is from a peer-reviewed journal.

2. (geiger2024abacterialsense pages 3-5): C. J. Geiger, G. C. L. Wong, and G. A. O'Toole. A bacterial sense of touch: t4p retraction motor as a means of surface sensing by <i>pseudomonas aeruginosa</i> pa14. Journal of Bacteriology, Jul 2024. URL: https://doi.org/10.1128/jb.00442-23, doi:10.1128/jb.00442-23. This article has 21 citations and is from a peer-reviewed journal.

3. (zheng2024thesurfaceinterface pages 1-2): Xuhui Zheng, Emma J. Gomez-Rivas, Sabrina I. Lamont, Katayoun Daneshjoo, Angeli Shieh, Daniel J. Wozniak, and Matthew R. Parsek. The surface interface and swimming motility influence surface-sensing responses in pseudomonas aeruginosa. Proceedings of the National Academy of Sciences of the United States of America, Sep 2024. URL: https://doi.org/10.1073/pnas.2411981121, doi:10.1073/pnas.2411981121. This article has 20 citations and is from a highest quality peer-reviewed journal.

4. (costin2023themovementbehaviour pages 23-27): NA Costin. The movement behaviour of solitary and collectively twitching pseudomonas aeruginosa cells on surfaces. Unknown journal, 2023.

5. (charlesorszag2024adhesionpilusretraction pages 1-2): Arthur Charles-Orszag, Marleen van Wolferen, Samuel J. Lord, Sonja-Verena Albers, and R. Dyche Mullins. Adhesion pilus retraction powers twitching motility in the thermoacidophilic crenarchaeon sulfolobus acidocaldarius. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49101-7, doi:10.1038/s41467-024-49101-7. This article has 13 citations and is from a highest quality peer-reviewed journal.

6. (pelicic2023mechanismofassembly pages 3-5): Vladimir Pelicic. Mechanism of assembly of type 4 filaments: everything you always wanted to know (but were afraid to ask). Mar 2023. URL: https://doi.org/10.1099/mic.0.001311, doi:10.1099/mic.0.001311. This article has 49 citations and is from a peer-reviewed journal.

7. (guo2024pily1regulatesthe pages 1-2): Shuaiqi Guo, Yunjie Chang, Yves V. Brun, P. L. Howell, Lori L. Burrows, and Jun Liu. Pily1 regulates the dynamic architecture of the type iv pilus machine in pseudomonas aeruginosa. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53638-y, doi:10.1038/s41467-024-53638-y. This article has 45 citations and is from a highest quality peer-reviewed journal.

8. (guo2024pily1regulatesthe media 2c9d0e01): Shuaiqi Guo, Yunjie Chang, Yves V. Brun, P. L. Howell, Lori L. Burrows, and Jun Liu. Pily1 regulates the dynamic architecture of the type iv pilus machine in pseudomonas aeruginosa. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53638-y, doi:10.1038/s41467-024-53638-y. This article has 45 citations and is from a highest quality peer-reviewed journal.

9. (roberge2024buildingpermits—controlof pages 1-3): Nathan A. Roberge and Lori L. Burrows. Building permits—control of type iv pilus assembly by pilb and its cofactors. Dec 2024. URL: https://doi.org/10.1128/jb.00359-24, doi:10.1128/jb.00359-24. This article has 16 citations and is from a peer-reviewed journal.

10. (cont2023materialsubstratephysical pages 4-6): Alice Cont, Joseph Vermeil, and Alexandre Persat. Material substrate physical properties control pseudomonas aeruginosa biofilm architecture. Apr 2023. URL: https://doi.org/10.1128/mbio.03518-22, doi:10.1128/mbio.03518-22. This article has 23 citations and is from a domain leading peer-reviewed journal.

11. (cont2023materialsubstratephysical pages 6-8): Alice Cont, Joseph Vermeil, and Alexandre Persat. Material substrate physical properties control pseudomonas aeruginosa biofilm architecture. Apr 2023. URL: https://doi.org/10.1128/mbio.03518-22, doi:10.1128/mbio.03518-22. This article has 23 citations and is from a domain leading peer-reviewed journal.

12. (cont2023materialsubstratephysical pages 2-4): Alice Cont, Joseph Vermeil, and Alexandre Persat. Material substrate physical properties control pseudomonas aeruginosa biofilm architecture. Apr 2023. URL: https://doi.org/10.1128/mbio.03518-22, doi:10.1128/mbio.03518-22. This article has 23 citations and is from a domain leading peer-reviewed journal.

13. (roberge2024buildingpermits—controlof pages 3-5): Nathan A. Roberge and Lori L. Burrows. Building permits—control of type iv pilus assembly by pilb and its cofactors. Dec 2024. URL: https://doi.org/10.1128/jb.00359-24, doi:10.1128/jb.00359-24. This article has 16 citations and is from a peer-reviewed journal.

14. (cont2023materialsubstratephysical pages 8-10): Alice Cont, Joseph Vermeil, and Alexandre Persat. Material substrate physical properties control pseudomonas aeruginosa biofilm architecture. Apr 2023. URL: https://doi.org/10.1128/mbio.03518-22, doi:10.1128/mbio.03518-22. This article has 23 citations and is from a domain leading peer-reviewed journal.

15. (zheng2024thesurfaceinterface pages 10-11): Xuhui Zheng, Emma J. Gomez-Rivas, Sabrina I. Lamont, Katayoun Daneshjoo, Angeli Shieh, Daniel J. Wozniak, and Matthew R. Parsek. The surface interface and swimming motility influence surface-sensing responses in pseudomonas aeruginosa. Proceedings of the National Academy of Sciences of the United States of America, Sep 2024. URL: https://doi.org/10.1073/pnas.2411981121, doi:10.1073/pnas.2411981121. This article has 20 citations and is from a highest quality peer-reviewed journal.