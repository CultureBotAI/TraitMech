---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:56:44.939562'
end_time: '2026-06-18T07:20:42.480783'
duration_seconds: 1437.54
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell width large
  trait_identifier: METPO:1000890
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_width_large
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-width phenotype in which the shorter cell dimension exceeds approximately
    0.9 micrometers.
  parent_traits: METPO:1000882
  synonyms: W_>0.9
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan
    synthesis (Supports MreB/Rod-complex activity as the control point governing wide
    rod radii.) | DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent
    size law supports widening of cells at fast growth rates or under nutrient-rich
    conditions.)'
  causal_graph_summary: 'cell_width_large_setpoint_increase: 4 nodes, 3 edges'
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
- **Trait label:** cell width large
- **METPO identifier:** METPO:1000890
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension exceeds approximately 0.9 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_>0.9
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports MreB/Rod-complex activity as the control point governing wide rod radii.) | DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports widening of cells at fast growth rates or under nutrient-rich conditions.)
- **Existing causal graph summary:** cell_width_large_setpoint_increase: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell width large** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_large.yaml`.

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
- **Trait label:** cell width large
- **METPO identifier:** METPO:1000890
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension exceeds approximately 0.9 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_>0.9
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports MreB/Rod-complex activity as the control point governing wide rod radii.) | DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports widening of cells at fast growth rates or under nutrient-rich conditions.)
- **Existing causal graph summary:** cell_width_large_setpoint_increase: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell width large** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_large.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **cell width large** (METPO:1000890)

### 1) Scope summary (trait meaning, boundary cases)
**Trait definition:** *cell width large* refers to a morphology phenotype in which the **shorter cell dimension (diameter/minor axis) exceeds ~0.9 µm** (METPO:1000890). In rod-shaped bacteria, this corresponds to an increased **rod radius/diameter**; in cocci/ovals it corresponds to increased **cell diameter or short-axis length**. The most curation-relevant biological interpretation is **an increased width setpoint** caused by changes in cell-envelope synthesis mechanics (especially elongasome/Rod-complex function), but the trait may also capture **rod-to-sphere transitions** where width increases because rod elongation fails (common under elongasome inhibition or severe envelope stress). (micelli2023aconservedzincbinding pages 1-2)

**Boundary cases to distinguish during curation:**
- **Filamentation (length-only increase)**: division defects (divisome perturbation) can yield very long cells without increased width; do not conflate with width-large unless minor axis increases. (cameron2024insightsintothe pages 1-3)
- **Transient swelling/spheroplasting** under acute antibiotic stress can produce large widths but may be assay- and time-dependent; curate as **treatment-induced morphology** rather than stable setpoint where appropriate. (kals2024antibioticschangethe pages 5-7)
- **Taxon/program differences**: some organisms (e.g., staphylococci) lack MreB and use different morphogenetic logic; “large width” may occur via septal/peripheral PBP redistribution rather than Rod-complex geometry. (costa2024theroleof pages 1-2)

### 2) Key concepts and current mechanistic understanding (2023–2024 emphasis)
#### 2.1 Peptidoglycan (PG) synthesis systems that determine width
Bacterial width is primarily determined by **how and where peptidoglycan is inserted and crosslinked** in the envelope.
- PG synthesis requires coordinated **glycan polymerization** and **peptide crosslinking**, typically executed by either **class A PBPs (aPBPs)** or **SEDS–class B PBP pairs**. (shlosman2023allostericactivationof pages 1-2, galinier2023recentadvancesin pages 1-3)
- The **Rod complex (elongasome)** is the canonical rod-shape/width system, containing a core **RodA–PBP2** synthase pair plus accessory factors and cytoskeletal guidance. (fivenson2023arolefor pages 1-2, micelli2023aconservedzincbinding pages 1-2, ago2023relationshipbetweenthe pages 1-3)

#### 2.2 Allosteric activation of RodA–PBP2 (a mechanistic “control point”)
A 2023 mechanistic advance is evidence that **RodA–PBP2 activity is controlled by conformational switching**: RodA–PBP2 exchanges between **closed and open states**, and **structural opening couples activation of polymerization and crosslinking** and is essential in vivo. (shlosman2023allostericactivationof pages 1-2)

The paper provides schematic mechanistic models (Figure 1 and Figure 7) showing the ON/OFF activation logic of RodA–PBP2 via interfaces and conformational transitions, supporting the idea that “activation state of the core synthase” is a causal control node upstream of width. (shlosman2023allostericactivationof media d3995263, shlosman2023allostericactivationof media 78b544e9)

#### 2.3 MreB-guided geometry: why circumferential insertion impacts width
For rod-shaped bacteria, **MreB** forms short filaments that guide PG insertion in a **circumferential direction** (perpendicular to the long axis). This geometry reinforces the sidewall and supports rod morphology. (fivenson2023arolefor pages 1-2, middlemiss2024molecularmotortugofwar pages 1-2)

#### 2.4 Accessory regulators: MreC/MreD/RodZ tune the synthase
The Rod complex includes accessory membrane proteins MreC, MreD, and RodZ.
- The Rod complex in *E. coli* is described as including **MreB, PBP2, RodA, RodZ, MreC, MreD**. (ago2023relationshipbetweenthe pages 1-3)
- A key regulatory statement is that **“the balance between MreC and MreD determines the activity of PBP2”**, supporting a tunable activation mechanism influencing elongation and thus width. (ago2023relationshipbetweenthe pages 1-3)
- RodZ **physically and genetically interacts** with multiple Rod components, supporting its role as a structural organizer node in a causal graph. (ago2023relationshipbetweenthe pages 1-3)

### 3) Recent developments and latest research highlights (prioritizing 2023–2024)
#### 3.1 Elongasome dynamics and “RodA-level tuning” of width (2024)
Single-molecule work in *Bacillus subtilis* (Nature Communications, 2024) quantifies elongasome/MreB dynamics and explicitly connects synthase abundance to morphology:
- The elongasome is **highly processive**, with prior estimates of processivity **~400–600 nm**. (middlemiss2024molecularmotortugofwar pages 1-2)
- The authors report that **cellular levels of RodA regulate elongasome processivity, reversal and pausing**, and that extreme synthase levels are associated with **abnormally wide cells** versus intermediate levels yielding “narrower, wild-type-like” morphology. (middlemiss2024molecularmotortugofwar pages 1-2, middlemiss2024molecularmotortugofwar pages 6-7)

These observations motivate a causal edge from **RodA abundance → elongasome processivity/density dynamics → width setpoint increase**.

#### 3.2 Metal–enzyme coupling: Zn-dependent PBP2 integrity and width increase (2023)
In *Acinetobacter baumannii* (PNAS, 2023), PBP2 contains a **Zn coordination site** required for stability.
- The study directly links mutation to width: **“mutation of PBP2 zinc-coordinating residues causes loss of the short-rod shape and an increase in cell width.”** (micelli2023aconservedzincbinding pages 6-7)
- It also states that **zinc-deprived growth conditions** and **carbapenem exposure** cause a **rod-to-sphere morphological transition**, resembling deficiency of the RodA–PBP2 complex. (micelli2023aconservedzincbinding pages 1-2)

This provides a rare, high-confidence edge for environmental metal limitation → elongasome impairment → width increase.

#### 3.3 Envelope mechanics beyond PG: outer membrane/LPS can modulate shape (2023–2024)
A 2023 PNAS study argues that Gram-negative **outer membrane (OM)** mechanics contribute to shape determination.
- It reports that **changes in LPS synthesis/modification predicted to strengthen the OM** can **suppress growth and shape defects** of *E. coli* mutants with reduced Rod-complex activity and restore proper MreB orientation. (fivenson2023arolefor pages 1-2)

This supports inclusion of an OM/LPS “envelope mechanics” branch in a width causal graph, including suppressor/compensation edges.

#### 3.4 Environmental switching between elongasomes (pH/nutrients) (2023)
In *Salmonella* (Communications Biology, 2023), two elongasomes are described that respond to different environmental cues:
- The canonical PBP2 elongasome responds to neutral pH, while PBP2SAL assembles in acidic conditions. (castanheira2023evidenceoftwo pages 1-2)
- Under acidic minimal medium (PCN pH 4.6), **ΔmrdA cells can exhibit genuine rod shape**, consistent with an adaptive elongasome switch. (castanheira2023evidenceoftwo pages 2-3)
- Under neutral pH, **ΔmrdA cells appear as “giant spherical cells with larger size”**. (castanheira2023evidenceoftwo pages 2-3)

This provides a condition-dependent context for when width-large phenotypes emerge (e.g., when the “wrong” elongasome program is active for a given environment).

### 4) Current applications and real-world implementations
1. **Antibiotic mechanism and susceptibility phenotyping:** Because elongasome/divisome PG synthases are prime antibiotic targets, width changes (including rounding) are used as phenotypic readouts of PBP inhibition. Carbapenems preferentially acylate PBP2 in *A. baumannii*, blocking RodA–PBP2 function and producing rod-to-sphere transitions. (micelli2023aconservedzincbinding pages 1-2)
2. **Microbial physiology / cell-envelope systems biology:** The 2024 single-molecule elongasome tracking approach provides a platform for quantifying how changes in synthase levels alter processivity and morphology, supporting rational perturbation experiments targeting width. (middlemiss2024molecularmotortugofwar pages 1-2)
3. **Host-associated niche adaptation:** *Salmonella* encodes alternative PBPs and switches elongation programs in acidic conditions, suggesting in-host conditions can be associated with distinct cell-shape control regimes. (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 2-3)

### 5) Expert opinions / authoritative synthesis
- Reviews emphasize that PG is a central, dynamic structure constantly synthesized/remodeled/repaired, with synthases and hydrolases organized in regulated complexes (supporting a graph architecture with “assembly/regulation” nodes). (galinier2023recentadvancesin pages 1-3)
- A divisome-focused Nature Reviews Microbiology review highlights coordination demands in fast growth (e.g., ~20 min division cycles in fast-growing *E. coli*) and positions septal PG synthases (FtsW/FtsI) as mechanistically related to elongation synthases, supporting cross-talk edges when interpreting width phenotypes under division stress. (cameron2024insightsintothe pages 1-3)

### 6) Candidate nodes grouped by type (ontology grounding)
A node inventory for curation is provided here:

| Node label | Group | Type | Description | Suggested grounding CURIE | Key supporting sources (DOI + year) |
|---|---|---|---|---|---|
| cell width large | Phenotype nodes | phenotype | Minor cell axis / diameter exceeds ~0.9 µm; includes widened rods and some rod-to-sphere/ovoid outcomes when width increases substantially (costa2024theroleof pages 1-2, micelli2023aconservedzincbinding pages 6-7) | METPO:1000890 | 10.1128/mbio.03235-23 (2024); 10.1073/pnas.2215237120 (2023) |
| rod-to-sphere morphological transition | Phenotype nodes | phenotype | Severe widening-associated loss of rod morphology seen after RodA–PBP2 inhibition or Zn deprivation (micelli2023aconservedzincbinding pages 1-2) | label-only | 10.1073/pnas.2215237120 (2023) |
| giant spherical cells | Phenotype nodes | phenotype | Large rounded cells observed when canonical PBP2 elongasome function is absent under non-permissive conditions (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 2-3) | label-only | 10.1038/s42003-023-05308-w (2023) |
| abnormal wide-cell morphology | Phenotype nodes | phenotype | Width-abnormal state produced by extreme RodA/synthase levels in Bacillus subtilis (middlemiss2024molecularmotortugofwar pages 6-7) | label-only | 10.1038/s41467-024-49785-x (2024) |
| MreB | Gene/protein nodes | protein | Bacterial actin homolog that forms filaments guiding circumferential peptidoglycan insertion and rod-shape maintenance (middlemiss2024molecularmotortugofwar pages 1-2, fivenson2023arolefor pages 1-2, ago2023relationshipbetweenthe pages 1-3) | label-only | 10.1038/s41467-024-49785-x (2024); 10.1073/pnas.2301987120 (2023); 10.1002/mbo3.1385 (2023) |
| RodA | Gene/protein nodes | protein | SEDS-family glycosyltransferase core elongasome synthase; abundance modulates processivity and shape outcomes (middlemiss2024molecularmotortugofwar pages 1-2, shlosman2023allostericactivationof pages 1-2) | label-only | 10.1038/s41467-024-49785-x (2024); 10.1038/s41467-023-39037-9 (2023) |
| PBP2 (MrdA) | Gene/protein nodes | protein | Class B penicillin-binding protein transpeptidase partnering with RodA for elongation and width control (micelli2023aconservedzincbinding pages 1-2, ago2023relationshipbetweenthe pages 1-3) | label-only | 10.1073/pnas.2215237120 (2023); 10.1002/mbo3.1385 (2023) |
| MreC | Gene/protein nodes | protein | Rod-complex accessory factor that interacts with PBP2 and contributes to activation/regulation of elongation synthesis (ago2023relationshipbetweenthe pages 1-3, shlosman2023allostericactivationof pages 1-2) | label-only | 10.1002/mbo3.1385 (2023); 10.1038/s41467-023-39037-9 (2023) |
| MreD | Gene/protein nodes | protein | Rod-complex accessory factor that balances MreC-dependent activation of PBP2 (ago2023relationshipbetweenthe pages 1-3) | label-only | 10.1002/mbo3.1385 (2023) |
| RodZ | Gene/protein nodes | protein | Transmembrane organizer linking major Rod-complex components; required for proper Rod-complex localization and shape maintenance (ago2023relationshipbetweenthe pages 1-3, costa2024theroleof pages 1-2) | label-only | 10.1002/mbo3.1385 (2023); 10.1128/mbio.03235-23 (2024) |
| PBP2SAL | Gene/protein nodes | protein | Alternative Salmonella elongasome bPBP used under acidic host-like conditions to maintain rod shape (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 2-3) | label-only | 10.1038/s42003-023-05308-w (2023) |
| PBP3SAL | Gene/protein nodes | protein | Alternative divisome-associated bPBP co-produced with PBP2SAL under acidic conditions in Salmonella (castanheira2023evidenceoftwo pages 2-3) | label-only | 10.1038/s42003-023-05308-w (2023) |
| FtsZ | Gene/protein nodes | protein | Tubulin homolog organizing division; indirectly relevant where mislocalization perturbs envelope growth and morphology (cameron2024insightsintothe pages 1-3, lakey2023theroleof pages 1-2) | label-only | 10.1038/s41579-023-00942-x (2024); 10.1128/mbio.00631-23 (2023) |
| FtsW | Gene/protein nodes | protein | SEDS-family divisome glycosyltransferase; homologous septal PG synthase related to RodA (cameron2024insightsintothe pages 1-3, shlosman2023allostericactivationof pages 1-2) | label-only | 10.1038/s41579-023-00942-x (2024); 10.1038/s41467-023-39037-9 (2023) |
| FtsI (PBP3) | Gene/protein nodes | protein | Divisome class B PBP transpeptidase; related synthase system to RodA-PBP2 (cameron2024insightsintothe pages 1-3, shlosman2023allostericactivationof pages 1-2) | label-only | 10.1038/s41579-023-00942-x (2024); 10.1038/s41467-023-39037-9 (2023) |
| GpsB | Gene/protein nodes | protein | Staphylococcal morphogenesis factor controlling septal vs peripheral PBP localization; loss causes more spherical cells (costa2024theroleof pages 1-2) | label-only | 10.1128/mbio.03235-23 (2024) |
| PBP4 | Gene/protein nodes | protein | Staphylococcal PBP whose peripheral delocalization contributes to altered cell shape (costa2024theroleof pages 1-2) | label-only | 10.1128/mbio.03235-23 (2024) |
| LpxC | Gene/protein nodes | protein | LPS-biosynthesis enzyme used as indicator of OM/LPS state in suppression of Rod-complex defects (fivenson2023arolefor pages 1-2) | label-only | 10.1073/pnas.2301987120 (2023) |
| Pal | Gene/protein nodes | protein | Tol-Pal outer-membrane-associated factor whose mobility links envelope constriction and morphogenesis (lakey2023theroleof pages 1-2) | label-only | 10.1128/mbio.00631-23 (2023) |
| Rod complex / elongasome | Complex/machinery nodes | protein complex | Multiprotein elongation machinery that inserts sidewall peptidoglycan and controls rod shape/width (micelli2023aconservedzincbinding pages 1-2, fivenson2023arolefor pages 1-2, ago2023relationshipbetweenthe pages 1-3) | label-only | 10.1073/pnas.2215237120 (2023); 10.1073/pnas.2301987120 (2023); 10.1002/mbo3.1385 (2023) |
| RodA–PBP2 complex | Complex/machinery nodes | protein complex | Core elongasome PG synthase whose open/closed conformational states regulate synthesis activation (shlosman2023allostericactivationof pages 1-2, micelli2023aconservedzincbinding pages 1-2) | label-only | 10.1038/s41467-023-39037-9 (2023); 10.1073/pnas.2215237120 (2023) |
| MreB filament / antiparallel double filament | Complex/machinery nodes | cytoskeletal structure | Dynamic scaffold for circumferential elongasome motion and insertion geometry (middlemiss2024molecularmotortugofwar pages 1-2) | label-only | 10.1038/s41467-024-49785-x (2024) |
| divisome | Complex/machinery nodes | protein complex | Septal cell-wall synthesis machinery; interacts conceptually and functionally with elongation programs (cameron2024insightsintothe pages 1-3, shlosman2023allostericactivationof pages 1-2) | label-only | 10.1038/s41579-023-00942-x (2024); 10.1038/s41467-023-39037-9 (2023) |
| FtsW–FtsI complex | Complex/machinery nodes | protein complex | Core divisome septal PG synthase, evolutionarily related to RodA–PBP2 (shlosman2023allostericactivationof pages 1-2, cameron2024insightsintothe pages 1-3) | label-only | 10.1038/s41467-023-39037-9 (2023); 10.1038/s41579-023-00942-x (2024) |
| outer membrane | Complex/machinery nodes | cellular component | Load-bearing Gram-negative envelope layer that can modulate MreB orientation and suppress shape defects (fivenson2023arolefor pages 1-2) | GO:0019867 | 10.1073/pnas.2301987120 (2023) |
| peptidoglycan cell wall / sacculus | Complex/machinery nodes | cellular structure | Major load-bearing wall polymer whose architecture and insertion pattern determine shape and width (galinier2023recentadvancesin pages 1-3, shlosman2023allostericactivationof pages 1-2) | CHEBI:24636 | 10.3390/biom13050720 (2023); 10.1038/s41467-023-39037-9 (2023) |
| RodA–PBP2 allosteric activation | Processes/GO nodes | biological process | Structural opening of the elongation synthase complex couples polymerization and crosslinking (shlosman2023allostericactivationof pages 1-2, shlosman2023allostericactivationof media d3995263) | label-only | 10.1038/s41467-023-39037-9 (2023) |
| peptidoglycan biosynthetic process | Processes/GO nodes | biological process | Synthesis of cell-wall PG from lipid II during elongation/division (galinier2023recentadvancesin pages 1-3, shlosman2023allostericactivationof pages 1-2) | GO:0009252 | 10.3390/biom13050720 (2023); 10.1038/s41467-023-39037-9 (2023) |
| transpeptidase activity | Processes/GO nodes | molecular function | Crosslinking of nascent glycan strands by PBPs such as PBP2/FtsI (micelli2023aconservedzincbinding pages 1-2, shlosman2023allostericactivationof pages 1-2) | label-only | 10.1073/pnas.2215237120 (2023); 10.1038/s41467-023-39037-9 (2023) |
| glycosyltransferase activity in PG synthesis | Processes/GO nodes | molecular function | Polymerization of glycan chains by RodA/FtsW and related synthases (micelli2023aconservedzincbinding pages 1-2, shlosman2023allostericactivationof pages 1-2) | label-only | 10.1073/pnas.2215237120 (2023); 10.1038/s41467-023-39037-9 (2023) |
| circumferential peptidoglycan insertion | Processes/GO nodes | biological process | Sidewall insertion pattern oriented perpendicular to the long axis and linked to width control (middlemiss2024molecularmotortugofwar pages 1-2, ago2023relationshipbetweenthe pages 1-3) | label-only | 10.1038/s41467-024-49785-x (2024); 10.1002/mbo3.1385 (2023) |
| elongasome processivity / reversal / pausing | Processes/GO nodes | process attribute | Dynamic parameters of elongasome motion modulated by RodA abundance and linked to shape outcomes (middlemiss2024molecularmotortugofwar pages 1-2, middlemiss2024molecularmotortugofwar pages 6-7) | label-only | 10.1038/s41467-024-49785-x (2024) |
| MreB filament orientation | Processes/GO nodes | process attribute | Orientation of MreB filaments relative to cell axis; restored by OM fortification in Rod mutants (fivenson2023arolefor pages 1-2) | label-only | 10.1073/pnas.2301987120 (2023) |
| cell-wall fortification / repair | Processes/GO nodes | biological process | Complementary aPBP-associated reinforcement/repair branch relevant when elongasome function is compromised (shlosman2023allostericactivationof pages 1-2) | label-only | 10.1038/s41467-023-39037-9 (2023) |
| peptidoglycan crosslinking | Processes/GO nodes | biological process | Mechanical-strength-generating reaction coordinated with glycan polymerization (shlosman2023allostericactivationof pages 1-2) | label-only | 10.1038/s41467-023-39037-9 (2023) |
| lipid II | Chemicals/metabolites (CHEBI) | metabolite | Universal disaccharide-pentapeptide precursor used as substrate for PG polymerization (galinier2023recentadvancesin pages 1-3, shlosman2023allostericactivationof pages 1-2) | label-only | 10.3390/biom13050720 (2023); 10.1038/s41467-023-39037-9 (2023) |
| UDP-N-acetylglucosamine | Chemicals/metabolites (CHEBI) | metabolite | Shared precursor for PG and lipid A/LPS biosynthesis (galinier2023recentadvancesin pages 1-3, fivenson2024coordinatedassemblyof pages 1-2) | label-only | 10.3390/biom13050720 (2023); 10.1016/j.mib.2024.102479 (2024) |
| N-acetylmuramic acid (MurNAc) | Chemicals/metabolites (CHEBI) | metabolite | PG sugar component assembled into lipid II and glycan chains (galinier2023recentadvancesin pages 1-3, micelli2023aconservedzincbinding pages 1-2) | label-only | 10.3390/biom13050720 (2023); 10.1073/pnas.2215237120 (2023) |
| undecaprenyl phosphate (UndP) | Chemicals/metabolites (CHEBI) | lipid carrier | Membrane carrier used in lipid I / lipid II synthesis (galinier2023recentadvancesin pages 1-3) | label-only | 10.3390/biom13050720 (2023) |
| zinc ion | Chemicals/metabolites (CHEBI) | metal ion | Essential cofactor bound in A. baumannii PBP2 transpeptidase domain; loss increases width (micelli2023aconservedzincbinding pages 1-2, micelli2023aconservedzincbinding pages 6-7) | CHEBI:29105 | 10.1073/pnas.2215237120 (2023) |
| lipopolysaccharide (LPS) | Chemicals/metabolites (CHEBI) | glycolipid | OM outer-leaflet component whose altered synthesis/modification can suppress Rod shape defects (fivenson2024coordinatedassemblyof pages 1-2, fivenson2023arolefor pages 1-2) | CHEBI:16412 | 10.1016/j.mib.2024.102479 (2024); 10.1073/pnas.2301987120 (2023) |
| carbapenem | Chemicals/metabolites (CHEBI) | antibiotic class | Preferentially acylates PBP2 in A. baumannii and drives rod-to-sphere transition (micelli2023aconservedzincbinding pages 1-2) | label-only | 10.1073/pnas.2215237120 (2023) |
| beta-lactam antibiotic | Chemicals/metabolites (CHEBI) | antibiotic class | Inhibits PBPs and can cause rounded giant cells when elongasome function is blocked (micelli2023aconservedzincbinding pages 1-2, castanheira2023evidenceoftwo pages 2-3) | CHEBI:35627 | 10.1073/pnas.2215237120 (2023); 10.1038/s42003-023-05308-w (2023) |
| mecillinam | Chemicals/metabolites (CHEBI) | antibiotic | PBP2-targeting beta-lactam used as sensitivity readout for RodA–PBP2 functional state (shlosman2023allostericactivationof pages 7-8) | label-only | 10.1038/s41467-023-39037-9 (2023) |
| nutrient-rich medium | Environmental/experimental factors | growth condition | Rich medium can expose stronger shape defects in PBP2-deficient cells and is associated with larger spherical forms in Salmonella experiments (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 2-3) | label-only | 10.1038/s42003-023-05308-w (2023) |
| minimal medium (PCN) | Environmental/experimental factors | growth condition | Minimal acidic medium supports alternative elongasome usage and restoration of rod shape in Salmonella ΔmrdA (castanheira2023evidenceoftwo pages 2-3) | label-only | 10.1038/s42003-023-05308-w (2023) |
| acidic pH | Environmental/experimental factors | environmental condition | Host-like cue that induces PBP2SAL/PBP3SAL morphogenetic program in Salmonella (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 2-3) | label-only | 10.1038/s42003-023-05308-w (2023) |
| neutral pH | Environmental/experimental factors | environmental condition | Condition under which Salmonella lacking canonical PBP2 forms giant spherical cells (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 2-3) | label-only | 10.1038/s42003-023-05308-w (2023) |
| Zn-deprived growth conditions | Environmental/experimental factors | environmental condition | Zinc limitation impairs PBP2-dependent elongation and promotes rod-to-sphere morphology (micelli2023aconservedzincbinding pages 1-2, micelli2023aconservedzincbinding pages 6-7) | label-only | 10.1073/pnas.2215237120 (2023) |
| carbapenem exposure | Environmental/experimental factors | treatment | Pharmacologic inhibition of PBP2 transpeptidase activity leading to widened spherical morphology (micelli2023aconservedzincbinding pages 1-2) | label-only | 10.1073/pnas.2215237120 (2023) |
| altered LPS synthesis/modification | Environmental/experimental factors | perturbation | OM-strengthening perturbations that suppress Rod-complex-related shape defects (fivenson2023arolefor pages 1-2) | label-only | 10.1073/pnas.2301987120 (2023) |
| RodA overexpression / depletion | Environmental/experimental factors | experimental perturbation | Changing RodA abundance shifts elongasome dynamics and can yield abnormally wide cells (middlemiss2024molecularmotortugofwar pages 6-7, middlemiss2023moleculartugofwarregulatesa pages 100-103) | label-only | 10.1038/s41467-024-49785-x (2024) |
| Escherichia coli | Taxon context | taxon | Canonical Gram-negative rod model for Rod-complex, MreB, and OM-shape coordination studies (fivenson2023arolefor pages 1-2, ago2023relationshipbetweenthe pages 1-3, cameron2024insightsintothe pages 1-3) | NCBITaxon:562 | 10.1073/pnas.2301987120 (2023); 10.1002/mbo3.1385 (2023); 10.1038/s41579-023-00942-x (2024) |
| Bacillus subtilis | Taxon context | taxon | Gram-positive rod model for elongasome processivity and RodA-level effects on cell shape (middlemiss2024molecularmotortugofwar pages 1-2) | NCBITaxon:1423 | 10.1038/s41467-024-49785-x (2024) |
| Acinetobacter baumannii | Taxon context | taxon | Pathogen where PBP2 Zn-binding integrity directly controls width and rod shape (micelli2023aconservedzincbinding pages 1-2, micelli2023aconservedzincbinding pages 6-7) | NCBITaxon:470 | 10.1073/pnas.2215237120 (2023) |
| Salmonella enterica serovar Typhimurium | Taxon context | taxon | Pathogen with alternative elongasomes responding to pH/nutrient cues (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 2-3) | NCBITaxon:90371 | 10.1038/s42003-023-05308-w (2023) |
| Staphylococcus aureus | Taxon context | taxon | Coccoid pathogen with elongation-associated shape regulation via GpsB/PBP localization despite lacking MreB (costa2024theroleof pages 1-2) | NCBITaxon:1280 | 10.1128/mbio.03235-23 (2024) |
| Rhodobacter sphaeroides | Taxon context | taxon | Alphaproteobacterium where envelope/division regulation perturbs MreB/FtsZ localization and morphology (lakey2023theroleof pages 1-2) | NCBITaxon:1063 | 10.1128/mbio.00631-23 (2023) |


*Table: This table lists candidate causal-graph nodes for the microbial trait 'cell width large', organized by phenotype, mechanism, chemistry, environment, and taxon. It is designed to support TraitMech curation by highlighting citable entities and tentative ontology grounding from the current evidence base.*

### 7) Candidate causal edges (curation-ready triples with snippets)
The evidence-backed edge table below is designed for direct translation into a TraitMech YAML graph.

| Edge (subject–predicate–object) | Entity type(s) | Suggested ontology grounding | Evidence (paper, year, DOI, URL) | Supporting snippet (verbatim short quote from provided excerpts) | Notes/curation confidence |
|---|---|---|---|---|---|
| RodA protein level increase/decrease → causally influences → cell width large / abnormal wide-cell morphology | protein abundance → phenotype | RodA: label-only candidate (SEDS glycosyltransferase); phenotype: METPO:1000890 | Middlemiss et al., 2024, Nature Communications, DOI:10.1038/s41467-024-49785-x, https://doi.org/10.1038/s41467-024-49785-x (middlemiss2024molecularmotortugofwar pages 1-2, middlemiss2024molecularmotortugofwar pages 6-7) | “We found that cellular levels of RodA regulate elongasome processivity, reversal and pausing.” / “extreme synthase levels produce ‘abnormally wide cells,’ whereas intermediate synthase/RodA levels produce ‘narrower, wild-type-like cell morphology.’” | Strong for RodA-levels→shape link; medium for direct curation to METPO large-width because excerpt gives qualitative, not numeric, width thresholds. Likely best modeled as RodA abundance modulates width setpoint in rod-shaped Bacillus. |
| RodA–PBP2 complex structural opening/activation → positively regulates → peptidoglycan polymerization and crosslinking during elongation | protein complex → biological process | RodA-PBP2 complex: label-only candidate; GO:0009252 peptidoglycan biosynthetic process | Shlosman et al., 2023, Nature Communications, DOI:10.1038/s41467-023-39037-9, https://doi.org/10.1038/s41467-023-39037-9 (shlosman2023allostericactivationof pages 1-2) | “Structural opening couples the activation of polymerization and crosslinking and is essential in vivo.” | Strong mechanistic edge for elongasome activation; width effect is indirect/inferred via elongation PG synthesis, so this edge should be curated upstream of width. |
| Activated RodA–PBP2 elongasome → positively regulates → rod-like sidewall peptidoglycan insertion | protein complex → biological process | RodA-PBP2 complex: label-only candidate; GO:0009252; peptidoglycan sidewall insertion: label-only candidate | Micelli et al., 2023, PNAS, DOI:10.1073/pnas.2215237120, https://doi.org/10.1073/pnas.2215237120 (micelli2023aconservedzincbinding pages 1-2) | “The elongasome… synthesizing and inserting new PG material at dispersed sites in the lateral cell wall.” | Strong for elongasome function in lateral wall growth; indirect for large-width phenotype. Suitable upstream node for width control graph. |
| PBP2 zinc-binding-site disruption → causes → loss of rod shape / increased cell width | protein site mutation → phenotype | PBP2: label-only candidate; zinc ion: CHEBI:29105; phenotype: METPO:1000890 | Micelli et al., 2023, PNAS, DOI:10.1073/pnas.2215237120, https://doi.org/10.1073/pnas.2215237120 (micelli2023aconservedzincbinding pages 6-7) | “mutation of PBP2 zinc-coordinating residues causes loss of the short-rod shape and an increase in cell width” | Strong and directly relevant to width increase, but taxon-specific (Acinetobacter baumannii) and mutation-specific. Good candidate positive edge to width-large phenotype. |
| Zinc-deprived growth conditions → cause → rod-to-sphere transition / widened cells | environmental factor → phenotype | zinc deprivation: low-zinc condition (label-only); zinc ion: CHEBI:29105; phenotype: METPO:1000890 | Micelli et al., 2023, PNAS, DOI:10.1073/pnas.2215237120, https://doi.org/10.1073/pnas.2215237120 (micelli2023aconservedzincbinding pages 1-2) | “Exposure to carbapenems or zinc (Zn)-deprived growth conditions leads to a rod-to-sphere morphological transition” | Strong for condition-induced widening via elongasome impairment in A. baumannii; assay/context-specific and may reflect severe morphogenesis failure rather than stable width setpoint. |
| Carbapenem exposure → inhibits → PBP2 transpeptidase function | chemical → molecular function | carbapenem antibiotic: CHEBI class label-only candidate; PBP2: label-only candidate; transpeptidase activity: GO:0009253 or label-only TP activity | Micelli et al., 2023, PNAS, DOI:10.1073/pnas.2215237120, https://doi.org/10.1073/pnas.2215237120 (micelli2023aconservedzincbinding pages 1-2) | “carbapenems preferentially acylate PBP2 and therefore block the transpeptidase function of the RodA–PBP2 system” | Strong upstream inhibitory edge. Width-large consequence is indirect but well supported in same study. |
| Carbapenem exposure → causes → rod-to-sphere transition / width increase | chemical → phenotype | carbapenem antibiotic: CHEBI class label-only candidate; phenotype: METPO:1000890 | Micelli et al., 2023, PNAS, DOI:10.1073/pnas.2215237120, https://doi.org/10.1073/pnas.2215237120 (micelli2023aconservedzincbinding pages 1-2) | “Exposure to carbapenems… leads to a rod-to-sphere morphological transition” | Strong, but phenotype may be broader than large width alone; curate with note that widening accompanies rod-shape loss. |
| MreB filaments → orient → circumferential peptidoglycan insertion | cytoskeletal protein → biological process | MreB: label-only candidate; GO:0009252 peptidoglycan biosynthetic process | Fivenson et al., 2023, PNAS, DOI:10.1073/pnas.2301987120, https://doi.org/10.1073/pnas.2301987120 (fivenson2023arolefor pages 1-2); Middlemiss et al., 2024, Nat Commun, DOI:10.1038/s41467-024-49785-x, https://doi.org/10.1038/s41467-024-49785-x (middlemiss2024molecularmotortugofwar pages 1-2) | “MreB filaments are thought to orient it orthogonally to the long cell axis” / “These cytoskeletal structures guide peptidoglycan insertion perpendicular to the long axis of the cell” | Strong foundational edge. Width effect is indirect via orientation of wall insertion and rod radius control. |
| Rod complex rotation around cell circumference → enables → even peptidoglycan distribution | protein complex behavior → cell wall architecture | Rod complex: label-only candidate; GO:0009252 | Ago et al., 2023, MicrobiologyOpen, DOI:10.1002/mbo3.1385, https://doi.org/10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 1-3) | “the Rod complex rotates perpendicularly to the long axis of the cell… allowing the insertion of peptidoglycan in the cell surface layer in an evenly distributed manner.” | Strong for cell-wall architecture; indirect for width. Useful intermediate edge in width-setpoint mechanism. |
| MreC–MreD balance → regulates → PBP2 activity | proteins → protein activity | MreC: label-only candidate; MreD: label-only candidate; PBP2: label-only candidate | Ago et al., 2023, MicrobiologyOpen, DOI:10.1002/mbo3.1385, https://doi.org/10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 1-3) | “the balance between MreC and MreD determines the activity of PBP2” | Strong mechanistic edge; indirect for width-large phenotype. Candidate upstream regulatory control point. |
| RodZ → physically/genetically interacts with → MreB/MreC/MreD/PBP2/RodA | protein → protein complex assembly | RodZ, MreB, MreC, MreD, PBP2, RodA: label-only candidates | Ago et al., 2023, MicrobiologyOpen, DOI:10.1002/mbo3.1385, https://doi.org/10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 1-3) | “RodZ physically and genetically interacts with itself, MreB, MreC, MreD, PBP2, and RodA” | Strong for complex assembly/context; width consequence indirect. Good structural edge for graph completeness. |
| RodZ transmembrane-domain perturbation (RMR) → causes → abnormal morphology and porous peptidoglycan | mutant protein → phenotype / cell wall architecture | RodZ mutant RMR: label-only candidate; peptidoglycan: CHEBI:24636 | Ago et al., 2023, MicrobiologyOpen, DOI:10.1002/mbo3.1385, https://doi.org/10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 1-3) | “Cells producing RMR grew slower than WT cells and showed an abnormal shape.” / “the peptidoglycan purified from RMR cells had many large holes” | Medium: direct morphology defect but not explicitly widened cells in excerpt. Keep as upstream evidence for RodZ-dependent wall organization, not direct width-large edge. |
| Increased peripheral PBP2/PBP4 localization → increases → peripheral peptidoglycan insertion/crosslinking | protein localization → biological process | PBP2/PBP4 in S. aureus: label-only candidates; GO:0009252 | Costa et al., 2024, mBio, DOI:10.1128/mbio.03235-23, https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2) | “Increased levels of these PBPs at the cell periphery versus the septum result in higher levels of peptidoglycan insertion/crosslinking throughout the entire cell” | Strong within S. aureus morphogenesis; however species lacks MreB and phenotype is spherical/elongation defect rather than classic rod-width control. |
| Loss of GpsB → causes → more spherical cells (increased short-axis dominance) | protein loss-of-function → phenotype | GpsB: label-only candidate; phenotype: broader morphology label, possible mapping to large width if minor axis >0.9 µm | Costa et al., 2024, mBio, DOI:10.1128/mbio.03235-23, https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2) | “Consequently, in the absence of GpsB, S. aureus cells become more spherical.” | Medium. Relevant as width-increase-like morphology, but in coccoid/ovoid context and may not cleanly map to METPO width-large without direct minor-axis measurement. |
| Strengthened outer membrane / altered LPS synthesis-modification → suppresses → Rod-complex shape defects | envelope layer / pathway → phenotype modulation | outer membrane: GO:0019867; LPS biosynthetic/modification pathway: label-only candidate; Rod complex: label-only candidate | Fivenson et al., 2023, PNAS, DOI:10.1073/pnas.2301987120, https://doi.org/10.1073/pnas.2301987120 (fivenson2023arolefor pages 1-2) | “changes in LPS synthesis or modification predicted to strengthen the OM can suppress the growth and shape defects of Escherichia coli mutants with reduced activity in a conserved PG synthesis machine called the Rod complex” | Strong for rescue/suppression edge. This is a negative regulator of width-abnormality rather than a direct cause of large width. Important envelope-mechanics branch. |
| Strengthened outer membrane / altered LPS synthesis-modification → restores → proper MreB filament orientation | envelope property → cytoskeletal organization | outer membrane: GO:0019867; LPS: CHEBI:16412; MreB: label-only candidate | Fivenson et al., 2023, PNAS, DOI:10.1073/pnas.2301987120, https://doi.org/10.1073/pnas.2301987120 (fivenson2023arolefor pages 1-2) | “OM fortification in the shape mutants restores the ability of MreB cytoskeletal filaments to properly orient the synthesis of new cell wall material” | Strong mechanistic rescue edge; indirect for width-large. |
| Acidic pH + minimal medium (PCN pH 4.6) → enables → PBP2SAL-directed rod shape in ΔmrdA Salmonella | environmental condition → morphogenetic program | acidic pH: label-only / ENVO candidate unavailable; minimal medium PCN: label-only; PBP2SAL: label-only candidate | Castanheira & García-del Portillo, 2023, Communications Biology, DOI:10.1038/s42003-023-05308-w, https://doi.org/10.1038/s42003-023-05308-w (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 2-3) | “growth in minimal PCN pH 4.6 medium yielded ΔmrdA cells exhibiting a genuine rod shape with convex polar caps” | Medium. Environmental control of alternative elongasome is strong, but this edge decreases width abnormality rather than increasing width. Include as context-specific branch. |
| Neutral pH in PBP2-deficient Salmonella → causes → giant spherical cells / increased width | environmental condition + gene loss → phenotype | neutral pH: label-only; PBP2/MrdA: label-only candidate; phenotype: METPO:1000890 candidate with caution | Castanheira & García-del Portillo, 2023, Communications Biology, DOI:10.1038/s42003-023-05308-w, https://doi.org/10.1038/s42003-023-05308-w (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 2-3) | “ΔmrdA cells appear at neutral pH as giant spherical cells with larger size” | Medium to strong for widened/spherical phenotype, but highly taxon- and genotype-specific. Good conditional edge if graph allows conjunction of PBP2 loss and neutral pH. |
| β-lactam inhibition of PBP2 → causes → giant rounded non-dividing cells | chemical inhibition → phenotype | beta-lactam antibiotic: CHEBI:35627; PBP2: label-only candidate; phenotype: METPO:1000890 candidate with caution | Castanheira & García-del Portillo, 2023, Communications Biology, DOI:10.1038/s42003-023-05308-w, https://doi.org/10.1038/s42003-023-05308-w (castanheira2023evidenceoftwo pages 2-3) | “inhibition of PBP2 by beta-lactams in E. coli causes giant rounded, non-dividing cells” | Medium because this is background statement in retrieved excerpt rather than focal experiment here; still useful as corroborating upstream pharmacologic edge. |
| Lipid II availability → required for → Rod/elongasome peptidoglycan synthesis | metabolite → biological process | Lipid II: label-only candidate; MurJ: label-only candidate; GO:0009252 | Galinier et al., 2023, Biomolecules, DOI:10.3390/biom13050720, https://doi.org/10.3390/biom13050720 (galinier2023recentadvancesin pages 1-3) | “GTases and TPases utilize the disaccharide pentapeptide of Lipid-II as a substrate for PG polymerization and synthesis of the PG layer” | Strong biochemical prerequisite, but far upstream and not width-specific. Include only if broader TraitMech graph needs metabolic precursor branch. |


*Table: This table compiles curation-ready candidate causal edges for the microbial morphology trait 'cell width large' using only retrieved context IDs. It emphasizes mechanistic links from elongasome/Rod-complex activity, PBP2/RodA regulation, envelope mechanics, and environmental perturbations to widened or spherical cell phenotypes.*

### 8) Visual evidence (figures/tables)
Shlosman et al. provide structural and schematic figures supporting the core mechanistic control point (RodA–PBP2 allosteric activation), including:
- Figure 1 (structure and open/closed schematic) and Figure 7 (summary OFF/ON model). (shlosman2023allostericactivationof media d3995263, shlosman2023allostericactivationof media 78b544e9)

### 9) Statistics and quantitative data extractable from current evidence
From the retrieved 2024 Nature Communications elongasome study:
- **MreB antiparallel double filaments** are described as **~170 nm long**, and monomers are **~5 nm**, implying **~68 subunits per filament** (estimate stated in text). (middlemiss2024molecularmotortugofwar pages 1-2)
- Prior estimates of elongasome processivity are reported as **~400–600 nm**. (middlemiss2024molecularmotortugofwar pages 1-2)

From *S. aureus* morphology context:
- Cells are described as **~1 µm in diameter**, meaning they can trivially meet a >0.9 µm width threshold; however, this is a coccoid context without MreB. (costa2024theroleof pages 1-2)

### 10) Warnings / claims not ready for curation
- **“Growth-rate-dependent widening”** is mentioned in the user’s prior evidence list (Science 2015 size law), but **no direct 2023–2024 quantitative growth-rate→width evidence** was retrieved in the current tool context; avoid curating growth-rate edges without additional primary evidence.
- Several width-relevant statements in the *Middlemiss 2023 thesis* are qualitative (e.g., diameter increases under RodA depletion/overexpression) and lack numeric thresholds in extracted pages; curate thesis-derived width edges as **weaker** unless corroborated by peer-reviewed quantitative sections. (middlemiss2023moleculartugofwarregulatesa pages 100-103, middlemiss2023moleculartugofwarregulates pages 100-103)
- Antibiotic-induced morphological changes can be **time- and concentration-dependent**, potentially reflecting transient stress morphologies rather than stable width setpoints; model these as treatment-response edges and annotate assay conditions. (kals2024antibioticschangethe pages 5-7)

---

## DOI-first bibliography (with URLs and publication dates where available)
1. Middlemiss S, Blandenet M, Roberts DM, et al. **Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in *Bacillus subtilis*.** *Nature Communications* (Accepted 18 Jun 2024). DOI: **10.1038/s41467-024-49785-x**. URL: https://doi.org/10.1038/s41467-024-49785-x (middlemiss2024molecularmotortugofwar pages 1-2, middlemiss2024molecularmotortugofwar pages 6-7)
2. Shlosman I, Fivenson EM, Gilman MSA, et al. **Allosteric activation of cell wall synthesis during bacterial growth.** *Nature Communications* (Accepted 25 May 2023; published Jun 2023). DOI: **10.1038/s41467-023-39037-9**. URL: https://doi.org/10.1038/s41467-023-39037-9 (shlosman2023allostericactivationof pages 1-2, shlosman2023allostericactivationof media d3995263, shlosman2023allostericactivationof media 78b544e9)
3. Micelli C, Dai Y, Raustad N, et al. **A conserved zinc-binding site in *Acinetobacter baumannii* PBP2 required for elongasome-directed bacterial cell shape.** *PNAS* (Published 14 Feb 2023). DOI: **10.1073/pnas.2215237120**. URL: https://doi.org/10.1073/pnas.2215237120 (micelli2023aconservedzincbinding pages 1-2, micelli2023aconservedzincbinding pages 6-7)
4. Fivenson EM, Rohs PDA, Vettiger A, et al. **A role for the Gram-negative outer membrane in bacterial shape determination.** *PNAS* (Published 22 Aug 2023). DOI: **10.1073/pnas.2301987120**. URL: https://doi.org/10.1073/pnas.2301987120 (fivenson2023arolefor pages 1-2)
5. Castanheira S, García-del Portillo F. **Evidence of two differentially regulated elongasomes in *Salmonella*.** *Communications Biology* (Published Sep 2023). DOI: **10.1038/s42003-023-05308-w**. URL: https://doi.org/10.1038/s42003-023-05308-w (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 2-3)
6. Costa SF, Saraiva BM, Veiga H, et al. **The role of GpsB in *Staphylococcus aureus* cell morphogenesis.** *mBio* (Published 6 Feb 2024; article header shows Mar 2024 volume/issue). DOI: **10.1128/mbio.03235-23**. URL: https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2)
7. Ago R, Tahara YO, Yamaguchi H, et al. **Relationship between the Rod complex and peptidoglycan structure in *Escherichia coli*.** *MicrobiologyOpen* (Accepted 25 Sep 2023; published Oct 2023). DOI: **10.1002/mbo3.1385**. URL: https://doi.org/10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 1-3)
8. Galinier A, Delan-Forino C, Foulquier E, Lakhal H, Pompeo F. **Recent Advances in Peptidoglycan Synthesis and Regulation in Bacteria.** *Biomolecules* (Published 22 Apr 2023). DOI: **10.3390/biom13050720**. URL: https://doi.org/10.3390/biom13050720 (galinier2023recentadvancesin pages 1-3)
9. Cameron TA, Margolin W. **New insights into the assembly and regulation of the bacterial divisome.** *Nature Reviews Microbiology* (Published in final form Jan 2024; PMC note). DOI: **10.1038/s41579-023-00942-x**. URL: https://doi.org/10.1038/s41579-023-00942-x (cameron2024insightsintothe pages 1-3)
10. Fivenson EM, Dubois L, Bernhardt TG. **Co-ordinated assembly of the multilayered cell envelope of Gram-negative bacteria.** *Current Opinion in Microbiology* (Published Jun 2024). DOI: **10.1016/j.mib.2024.102479**. URL: https://doi.org/10.1016/j.mib.2024.102479 (fivenson2024coordinatedassemblyof pages 1-2)



References

1. (micelli2023aconservedzincbinding pages 1-2): Carmina Micelli, Yunfei Dai, Nicole Raustad, Ralph R. Isberg, Christopher G. Dowson, Adrian J. Lloyd, Edward Geisinger, Allister Crow, and David I. Roper. A conserved zinc-binding site in acinetobacter baumannii pbp2 required for elongasome-directed bacterial cell shape. Proceedings of the National Academy of Sciences of the United States of America, Feb 2023. URL: https://doi.org/10.1073/pnas.2215237120, doi:10.1073/pnas.2215237120. This article has 21 citations and is from a highest quality peer-reviewed journal.

2. (cameron2024insightsintothe pages 1-3): Todd A. Cameron and William Margolin. Insights into the assembly and regulation of the bacterial divisome. Nature Reviews Microbiology, 22:33-45, Jul 2024. URL: https://doi.org/10.1038/s41579-023-00942-x, doi:10.1038/s41579-023-00942-x. This article has 134 citations and is from a highest quality peer-reviewed journal.

3. (kals2024antibioticschangethe pages 5-7): Morten Kals, Emma Kals, Jurij Kotar, Allen Donald, Leonardo Mancini, and Pietro Cicuta. Antibiotics change the growth rate heterogeneity and morphology of bacteria. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.27.609914, doi:10.1101/2024.08.27.609914. This article has 1 citations.

4. (costa2024theroleof pages 1-2): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

5. (shlosman2023allostericactivationof pages 1-2): Irina Shlosman, Elayne M. Fivenson, Morgan S. A. Gilman, Tyler A. Sisley, Suzanne Walker, Thomas G. Bernhardt, Andrew C. Kruse, and Joseph J. Loparo. Allosteric activation of cell wall synthesis during bacterial growth. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9, doi:10.1038/s41467-023-39037-9. This article has 44 citations and is from a highest quality peer-reviewed journal.

6. (galinier2023recentadvancesin pages 1-3): Anne Galinier, Clémentine Delan-Forino, Elodie Foulquier, Hakima Lakhal, and Frédérique Pompeo. Recent advances in peptidoglycan synthesis and regulation in bacteria. Biomolecules, 13:720, Apr 2023. URL: https://doi.org/10.3390/biom13050720, doi:10.3390/biom13050720. This article has 68 citations.

7. (fivenson2023arolefor pages 1-2): Elayne M. Fivenson, Patricia D. A. Rohs, Andrea Vettiger, Marios F. Sardis, Grasiela Torres, Alison Forchoh, and Thomas G. Bernhardt. A role for the gram-negative outer membrane in bacterial shape determination. Proceedings of the National Academy of Sciences of the United States of America, Aug 2023. URL: https://doi.org/10.1073/pnas.2301987120, doi:10.1073/pnas.2301987120. This article has 92 citations and is from a highest quality peer-reviewed journal.

8. (ago2023relationshipbetweenthe pages 1-3): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 15 citations and is from a peer-reviewed journal.

9. (shlosman2023allostericactivationof media d3995263): Irina Shlosman, Elayne M. Fivenson, Morgan S. A. Gilman, Tyler A. Sisley, Suzanne Walker, Thomas G. Bernhardt, Andrew C. Kruse, and Joseph J. Loparo. Allosteric activation of cell wall synthesis during bacterial growth. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9, doi:10.1038/s41467-023-39037-9. This article has 44 citations and is from a highest quality peer-reviewed journal.

10. (shlosman2023allostericactivationof media 78b544e9): Irina Shlosman, Elayne M. Fivenson, Morgan S. A. Gilman, Tyler A. Sisley, Suzanne Walker, Thomas G. Bernhardt, Andrew C. Kruse, and Joseph J. Loparo. Allosteric activation of cell wall synthesis during bacterial growth. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9, doi:10.1038/s41467-023-39037-9. This article has 44 citations and is from a highest quality peer-reviewed journal.

11. (middlemiss2024molecularmotortugofwar pages 1-2): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 20 citations and is from a highest quality peer-reviewed journal.

12. (middlemiss2024molecularmotortugofwar pages 6-7): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 20 citations and is from a highest quality peer-reviewed journal.

13. (micelli2023aconservedzincbinding pages 6-7): Carmina Micelli, Yunfei Dai, Nicole Raustad, Ralph R. Isberg, Christopher G. Dowson, Adrian J. Lloyd, Edward Geisinger, Allister Crow, and David I. Roper. A conserved zinc-binding site in acinetobacter baumannii pbp2 required for elongasome-directed bacterial cell shape. Proceedings of the National Academy of Sciences of the United States of America, Feb 2023. URL: https://doi.org/10.1073/pnas.2215237120, doi:10.1073/pnas.2215237120. This article has 21 citations and is from a highest quality peer-reviewed journal.

14. (castanheira2023evidenceoftwo pages 1-2): Sónia Castanheira and Francisco García-del Portillo. Evidence of two differentially regulated elongasomes in salmonella. Communications Biology, Sep 2023. URL: https://doi.org/10.1038/s42003-023-05308-w, doi:10.1038/s42003-023-05308-w. This article has 15 citations and is from a peer-reviewed journal.

15. (castanheira2023evidenceoftwo pages 2-3): Sónia Castanheira and Francisco García-del Portillo. Evidence of two differentially regulated elongasomes in salmonella. Communications Biology, Sep 2023. URL: https://doi.org/10.1038/s42003-023-05308-w, doi:10.1038/s42003-023-05308-w. This article has 15 citations and is from a peer-reviewed journal.

16. (lakey2023theroleof pages 1-2): Bryan D. Lakey, François Alberge, Daniel Parrell, Elizabeth R. Wright, Daniel R. Noguera, and Timothy J. Donohue. The role of cenkr in the coordination of rhodobacter sphaeroides cell elongation and division. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.00631-23, doi:10.1128/mbio.00631-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

17. (fivenson2024coordinatedassemblyof pages 1-2): Elayne M Fivenson, Laurent Dubois, and Thomas G Bernhardt. Co-ordinated assembly of the multilayered cell envelope of gram-negative bacteria. Current Opinion in Microbiology, 79:102479, Jun 2024. URL: https://doi.org/10.1016/j.mib.2024.102479, doi:10.1016/j.mib.2024.102479. This article has 24 citations and is from a peer-reviewed journal.

18. (shlosman2023allostericactivationof pages 7-8): Irina Shlosman, Elayne M. Fivenson, Morgan S. A. Gilman, Tyler A. Sisley, Suzanne Walker, Thomas G. Bernhardt, Andrew C. Kruse, and Joseph J. Loparo. Allosteric activation of cell wall synthesis during bacterial growth. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9, doi:10.1038/s41467-023-39037-9. This article has 44 citations and is from a highest quality peer-reviewed journal.

19. (middlemiss2023moleculartugofwarregulatesa pages 100-103): SA Middlemiss. Molecular tug-of-war regulates bacillus subtilis elongasome dynamics and bacterial cell shape. Unknown journal, 2023.

20. (middlemiss2023moleculartugofwarregulates pages 100-103): SA Middlemiss. Molecular tug-of-war regulates bacillus subtilis elongasome dynamics and bacterial cell shape. Unknown journal, 2023.