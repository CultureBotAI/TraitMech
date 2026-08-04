---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T00:04:09.666005'
end_time: '2026-06-30T00:34:18.320241'
duration_seconds: 1808.65
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: spindle shaped
  trait_identifier: METPO:1000692
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: spindle_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape that is widest at the middle and tapers symmetrically toward
    pointed poles.
  parent_traits: METPO:1000666
  synonyms: spindle
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically
    determined (Cell-shape review supports symmetric tapered shapes as a genetically
    determined outcome of polar wall patterning.)'
  causal_graph_summary: 'spindle_shaped_symmetric_taper: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spindle shaped
- **METPO identifier:** METPO:1000692
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape that is widest at the middle and tapers symmetrically toward pointed poles.
- **Parent traits:** METPO:1000666
- **Synonyms:** spindle
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports symmetric tapered shapes as a genetically determined outcome of polar wall patterning.)
- **Existing causal graph summary:** spindle_shaped_symmetric_taper: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **spindle shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spindle_shaped.yaml`.

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
- **Trait label:** spindle shaped
- **METPO identifier:** METPO:1000692
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape that is widest at the middle and tapers symmetrically toward pointed poles.
- **Parent traits:** METPO:1000666
- **Synonyms:** spindle
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports symmetric tapered shapes as a genetically determined outcome of polar wall patterning.)
- **Existing causal graph summary:** spindle_shaped_symmetric_taper: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **spindle shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spindle_shaped.yaml`.

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


# Microbial Trait Causal Graph Research Report: Spindle-Shaped (METPO:1000692)

## 1. Trait Scope Summary

The **spindle-shaped** (fusiform) trait describes a cell morphology that is widest at the middle and tapers symmetrically toward pointed poles. This distinguishes it from standard rod-shaped bacteria (which have hemispherical pole caps of uniform width) and from ovoid/coccoid shapes. The canonical example of a spindle-shaped microorganism is *Fusobacterium nucleatum*, a Gram-negative anaerobe described as "a fusiform or spindle-shaped gram-negative anaerobe" (wang2025mrebunravelingthe pages 11-12). The spindle shape is genetically determined and results from the spatial patterning of peptidoglycan (PG) synthesis at cell poles, producing symmetric tapering rather than the blunt, hemispherical caps seen in typical rod-shaped bacteria.

**Boundary cases:** The trait should be distinguished from (i) standard rod shape (blunt poles, uniform width along the cylindrical body), (ii) lanceolate/lancet-shaped cells (asymmetric tapering), and (iii) lemon-shaped cells (wider mid-body but with rounded rather than pointed poles). Archaeal spindle-shaped viruses (e.g., fuselloviruses like SSV1) represent a non-cellular context where spindle morphology arises from capsid protein self-assembly rather than PG-based mechanisms.

## 2. Mechanistic Framework

### 2.1 Peptidoglycan as the Shape-Determining Layer

Peptidoglycan is the primary shape-determining structure of the bacterial cell wall. As established in comprehensive reviews, PG synthesis requires "spatio-temporal regulation for successful assembly of a robust sacculus to protect the cell from turgor and determine cell shape" (billini2019aspecializedmrebdependent pages 1-2). The spatial patterning of PG insertion—whether lateral (elongasome-mediated), septal (divisome-mediated), or polar (DivIVA/GPR-mediated)—directly determines the resulting cell geometry. For spindle-shaped cells, the key mechanistic question is how PG synthesis is directed to produce pointed, tapered poles rather than the hemispherical caps characteristic of rod-shaped bacteria.

### 2.2 The Elongasome: Lateral Wall Synthesis and Rod Maintenance

The elongasome (Rod complex) is the central machinery for maintaining cylindrical (rod) morphology in many bacteria. It consists of the actin-like protein MreB, the membrane-associated regulators MreC, MreD, and RodZ, and the PG synthase pair RodA–PBP2 (wang2025mrebunravelingthe pages 11-12, jain2023understandingelongasomeunit pages 2-4). MreB forms antiparallel protofilament doublets on the inner membrane that organize circumferential PG insertion, maintaining constant cell width during elongation (wang2025mrebunravelingthe pages 11-12). RodZ activates the elongasome through dual signaling cascades: one in the periplasm via MreCD and another in the cytoplasm through MreB (zhan2026rodzactsthrough pages 1-5, zhan2026rodzactsthrough pages 19-22). Disruption of MreB causes cells to transition from rod-shaped to spherical morphology, demonstrating that MreB is "absolutely essential for rod shape determination" (maharjan2026alaninescanningmutagenesislibrary pages 11-14).

For spindle-shaped cells, the elongasome provides the mid-body cylindrical geometry. The distinguishing feature—tapered poles—requires additional or modified polar growth mechanisms that deviate from standard rod morphogenesis.

### 2.3 Polar Growth Mechanisms

Three distinct polar growth systems are relevant to understanding spindle/fusiform morphology:

**a) DivIVA-mediated polar growth (Actinobacteria):** DivIVA is "essential for polar growth in Actinomycetota" and "focuses cell wall synthesis activity to cell poles" (sen2024adispensablesepiva pages 1-2, sen2024adispensablesepiva pages 10-12). In *Streptomyces* and *Corynebacterium*, DivIVA assembles a polarisome complex with coiled-coil proteins Scy and FilP and the cellulose synthase-like protein CslA, which coordinates apical cell wall material insertion (lubbers2025definingtheminimal pages 12-14, lubbers2025definingtheminimal pages 10-12). DivIVA senses negative membrane curvature, causing it to preferentially localize at cell poles (meyer2024understandingthegrowth pages 35-38). Post-translational modifications (phosphorylation by AfsK kinase) regulate DivIVA function and polarisome dynamics (lubbers2025definingtheminimal pages 12-14).

**b) GPR-mediated polar growth (Hyphomicrobiales):** In *Agrobacterium tumefaciens*, the growth pole ring (GPR) protein forms a distinctive hexameric ring structure approximately 200 nm in diameter at the growth pole and "serves as an organizing center for membrane and peptidoglycan synthesis during polar growth" (zupan2021agrobacteriumtumefaciensgrowth pages 1-2, zupan2021agrobacteriumtumefaciensgrowth pages 11-13). Loss of GPR causes PG synthesis to become "distributed around the cell periphery rather than concentrated at discrete polar locations, resulting in spherical cell morphology" (zupan2021agrobacteriumtumefaciensgrowth pages 10-11). LD-transpeptidases are essential for polar growth in these organisms, with A. tumefaciens possessing 14 putative LDTs, 7 of which are Hyphomicrobiales-specific and localize to polar or subpolar regions (aliashkevich2024essentialityofldtranspeptidation pages 4-7).

**c) Bactofilin-mediated polar PG remodeling:** Bactofilins are widespread cytoskeletal proteins that "polymerize into static filamentous structures and assemble at confined cellular positions" (richter2023interactingbactofilinsimpact pages 2-4). They interact with PG synthases and lytic enzymes to "locally alter PG synthesis and composition, enabling cell shape modifications such as bending, helicity, and stalk growth" (richter2023interactingbactofilinsimpact pages 2-4). In *Caulobacter crescentus*, BacA and BacB recruit penicillin-binding protein PbpC to the stalked cell pole (liu2022comprehensiveanalysisof pages 24-28). In *Rhodomicrobium vannielii*, BacA localizes to hyphal tips and regulates LD-transpeptidase activity for proper hyphal morphology (richter2023interactingbactofilinsimpact pages 13-15, richter2023interactingbactofilinsimpact pages 15-16).

### 2.4 Specialized Polar PG Composition

The *Caulobacter crescentus* stalk provides direct evidence that polar structures can have distinct PG composition. Stalk PG contains "a significantly higher proportion of 3–3 crosslinked peptides and non-crosslinked tripeptides compared to cell body PG" (billini2019aspecializedmrebdependent pages 7-8). These 3–3 crosslinks, generated by LD-transpeptidases, are "mechanically stiffer and more extended than 3–4 crosslinks, making them better suited to support stressed PG" (billini2019aspecializedmrebdependent pages 21-22). The stalk biosynthetic complex is a hybrid that "incorporat[es] factors from both the elongasome (MreB, RodZ, RodA, PBP2) and divisome (DipM, SdpA, SdpB, CrbA)" (billini2019aspecializedmrebdependent pages 18-19). Stalk elongation occurs through "expansion of the stalk-proximal polar cap and its simultaneous remodeling into new stalk segments" (billini2019aspecializedmrebdependent pages 18-19, billini2019aspecializedmrebdependent pages 19-21).

### 2.5 Mechanochemical Feedback

The MreB-RodZ complex "senses membrane curvature changes induced by peptidoglycan synthesis and adaptively adjusts filament trajectories through mechanochemical feedback" (wang2025mrebunravelingthe pages 9-11). This curvature-sensing mechanism is critical for maintaining uniform cell width and could, in principle, be modulated to produce gradual tapering rather than an abrupt transition between cylindrical body and hemispherical cap. Post-translational modifications including "acetylation [which] reduces the peptidoglycan synthesis zone to fine-tune cell diameter" further regulate shape (wang2025mrebunravelingthe pages 9-11).

## 3. Candidate Causal Graph Nodes

The following table presents candidate nodes grouped by type for the spindle-shaped trait causal graph:

| Node Name | Node Type | Suggested CURIE (if available) | Taxon Scope | Notes |
|---|---|---|---|---|
| MreB | Gene/Protein | GO:0000902 | Broad bacterial; especially rod-shaped bacteria | Actin-like cytoskeletal protein that organizes elongasome activity and rod-shape maintenance; loss commonly causes rounding/spherical morphology (wang2025mrebunravelingthe pages 11-12, maharjan2026alaninescanningmutagenesislibrary pages 11-14) |
| MreC | Gene/Protein | label only | Broad bacterial | Periplasmic elongasome component; helps spatially arrange PG synthases and supports elongasome activation (wang2025mrebunravelingthe pages 11-12, zhan2026rodzactsthrough pages 1-5) |
| MreD | Gene/Protein | label only | Broad bacterial | Transmembrane elongasome regulator acting with MreC and RodZ in elongasome control (wang2025mrebunravelingthe pages 11-12, zhan2026rodzactsthrough pages 1-5) |
| RodZ | Gene/Protein | label only | Broad bacterial | Bridge between MreB and PG synthesis machinery; required for proper elongasome assembly and robust rod morphology (wang2025mrebunravelingthe pages 11-12, zhan2026rodzactsthrough pages 19-22) |
| RodA | Gene/Protein | label only | Broad bacterial | SEDS-family PG glycosyltransferase in the elongasome; pairs with PBP2/MrdA for lateral wall synthesis (jain2023understandingelongasomeunit pages 2-4, billini2019aspecializedmrebdependent pages 18-19) |
| PBP2/MrdA | Gene/Protein | label only | Broad bacterial | Elongasome DD-transpeptidase; required for rod-like elongation and shape maintenance (jain2023understandingelongasomeunit pages 2-4, billini2019aspecializedmrebdependent pages 18-19) |
| FtsZ | Gene/Protein | label only | Broad bacterial | Tubulin-like divisome scaffold defining septal PG synthesis zone; relevant as nearby/contrast mechanism to elongasome and polar growth (wang2025mrebunravelingthe pages 11-12, zupan2021agrobacteriumtumefaciensgrowth pages 2-4) |
| FtsW | Gene/Protein | label only | Broad bacterial | SEDS-family divisome glycosyltransferase for septal PG synthesis; contrasts with elongasome-driven shape maintenance (billini2019aspecializedmrebdependent pages 18-19) |
| FtsI/PBP3 | Gene/Protein | label only | Broad bacterial | Divisome DD-transpeptidase for septation; contributes to pole formation after division (billini2019aspecializedmrebdependent pages 18-19) |
| DivIVA/Wag31 | Gene/Protein | label only | Actinobacteria | Polar growth determinant focusing cell wall synthesis at poles; core organizer of actinobacterial polarisome/tip growth (sen2024adispensablesepiva pages 1-2, sen2024adispensablesepiva pages 10-12) |
| GPR (growth pole ring protein) | Gene/Protein | label only | Hyphomicrobiales; Agrobacterium tumefaciens | Hexameric ring-like scaffold at growth pole; organizes polar PG and membrane synthesis; loss mislocalizes PG synthesis and causes spherical cells (zupan2021agrobacteriumtumefaciensgrowth pages 1-2, zupan2021agrobacteriumtumefaciensgrowth pages 10-11) |
| BacA/BacB | Gene/Protein | label only | Alphaproteobacteria; broader bactofilin-bearing bacteria | Bactofilin scaffolds that localize to poles/growth zones and recruit or constrain morphogenetic factors; implicated in stalk/hypha shape (liu2022comprehensiveanalysisof pages 24-28, richter2023interactingbactofilinsimpact pages 13-15) |
| PBP1a | Gene/Protein | label only | Hyphomicrobiales; Actinobacteria | Bifunctional PG synthase important for polar growth in Agrobacterium and related systems (aliashkevich2024ldtranspeptidationiscrucial pages 22-23) |
| LD-transpeptidases (LDTs) | Gene/Protein/Enzyme class | EC:3.4.-.- | Especially Hyphomicrobiales; also stalk PG in Caulobacter | Create 3-3 PG crosslinks; major contributors to polar growth, wall integrity, and specialized mechanical properties (aliashkevich2024essentialityofldtranspeptidation pages 4-7, billini2019aspecializedmrebdependent pages 7-8) |
| PopZ | Gene/Protein | label only | Caulobacter/alphaproteobacteria | Polar scaffold protein contributing to pole identity and organization of polar development (zupan2021agrobacteriumtumefaciensgrowth pages 2-4) |
| CslA | Gene/Protein | label only | Filamentous actinobacteria | Cellulose synthase-like polarisome component associated with apical growth zones (lubbers2025definingtheminimal pages 10-12) |
| Scy | Gene/Protein | label only | Filamentous actinobacteria | Coiled-coil polarisome component interacting with DivIVA to shape tip growth zones (lubbers2025definingtheminimal pages 12-14, lubbers2025definingtheminimal pages 10-12) |
| FilP | Gene/Protein | label only | Filamentous actinobacteria | Coiled-coil cytoskeletal/polar scaffold supporting tip growth and morphogenesis (lubbers2025definingtheminimal pages 10-12, richter2023interactingbactofilinsimpact pages 15-16) |
| Peptidoglycan synthesis | Biological Process | GO:0009252 | Broad bacterial | Core morphogenetic process; spatial patterning of PG insertion underlies rod, polar, and specialized tapered morphologies (billini2019aspecializedmrebdependent pages 1-2, billini2019aspecializedmrebdependent pages 18-19) |
| Polar cell wall growth | Biological Process | label only | Polar-growing bacteria | Growth mode in which new wall material is inserted at one or both poles; mechanistically relevant to symmetric tapering candidates (zupan2021agrobacteriumtumefaciensgrowth pages 1-2, sen2024adispensablesepiva pages 1-2) |
| Cell elongation | Biological Process | GO:0009826 | Broad bacterial | Expansion of cylindrical or polar cell body by PG insertion; controlled by elongasome or tip-growth apparatus (jain2023understandingelongasomeunit pages 2-4, wang2025mrebunravelingthe pages 11-12) |
| Elongasome assembly | Biological Process | label only | Broad bacterial | Assembly/activation of MreB–RodZ–MreCD–RodA/PBP2 machinery for lateral elongation (wang2025mrebunravelingthe pages 11-12, zhan2026rodzactsthrough pages 1-5) |
| Divisome-mediated septation | Biological Process | label only | Broad bacterial | Midcell PG synthesis and cytokinesis; creates new poles and can be repurposed in specialized morphogenesis (billini2019aspecializedmrebdependent pages 18-19) |
| Cell shape determination | Biological Process | GO:0008360 | Broad bacterial/archaeal | High-level process encompassing cytoskeletal patterning, PG synthesis, and polar scaffolding (wang2025mrebunravelingthe pages 11-12, richter2023interactingbactofilinsimpact pages 2-4) |
| Peptidoglycan | Chemical/Metabolic | CHEBI:8005 | Broad bacterial | Structural wall polymer whose local synthesis and remodeling directly determine shape (billini2019aspecializedmrebdependent pages 1-2, billini2019aspecializedmrebdependent pages 7-8) |
| Lipid II | Chemical/Metabolic | CHEBI:16902 | Broad bacterial | Universal PG precursor used by elongasome/divisome synthases; useful upstream substrate node for cell-wall-growth edges (jain2023understandingelongasomeunit pages 2-4) |
| UDP-MurNAc-pentapeptide | Chemical/Metabolic | label only | Broad bacterial | Cytoplasmic PG precursor upstream of Lipid II; candidate precursor node for wall biogenesis graph (jain2023understandingelongasomeunit pages 2-4) |
| 3-3 crosslinks (LD-crosslinks) | Chemical/Metabolic | label only | Especially Caulobacter stalks and Hyphomicrobiales | LDT-generated PG crosslinks enriched in specialized polar structures and associated with altered mechanical properties (billini2019aspecializedmrebdependent pages 7-8, billini2019aspecializedmrebdependent pages 21-22) |
| 4-3 crosslinks (DD-crosslinks) | Chemical/Metabolic | label only | Broad bacterial | Canonical PBP-generated PG crosslinks dominating typical cell-body PG (billini2019aspecializedmrebdependent pages 21-22) |
| Elongasome complex | Cellular Structure/Complex | label only | Broad bacterial | Morphogenetic complex for lateral PG insertion and rod-shape maintenance (jain2023understandingelongasomeunit pages 2-4, zhan2026rodzactsthrough pages 1-5) |
| Divisome complex | Cellular Structure/Complex | label only | Broad bacterial | Septal PG synthesis machinery centered on FtsZ/FtsW/FtsI (billini2019aspecializedmrebdependent pages 18-19) |
| Polarisome (actinobacterial tip complex) | Cellular Structure/Complex | label only | Filamentous actinobacteria | DivIVA-centered tip growth complex including coiled-coil and wall-synthesis factors (sen2024adispensablesepiva pages 1-2, lubbers2025definingtheminimal pages 10-12) |
| Turgor pressure | Environmental/Physical | label only | Broad bacterial | Physical force resisted by PG; relevant as a background biophysical driver but not specific enough alone to curate as spindle determinant (billini2019aspecializedmrebdependent pages 1-2) |
| Membrane curvature | Environmental/Physical | label only | Broad bacterial | Geometric cue sensed by MreB/RodZ and DivIVA-like systems to bias morphogenetic localization (wang2025mrebunravelingthe pages 11-12, meyer2024understandingthegrowth pages 35-38) |


*Table: This table lists candidate causal-graph nodes for the spindle-shaped microbial trait, grouped by entity type and annotated with suggested identifiers, taxonomic scope, and curation notes. It is useful for assembling a TraitMech graph centered on cytoskeletal control, polar growth, and peptidoglycan remodeling.*

## 4. Candidate Causal Edges

The following table presents evidence-backed subject-predicate-object triples for curation into the TraitMech graph:

| Subject | Predicate | Object | Reference (DOI) | Supporting Quote/Snippet | Notes/Confidence |
|---|---|---|---|---|---|
| MreB | organizes | Elongasome complex | 10.1186/s12964-025-02373-y | “MreB binds to membrane proteins MreC and MreD, which regulate peptidoglycan synthases including RodA and penicillin-binding proteins (PBPs)… RodZ bridges the cytoskeleton and cell wall synthesis” (wang2025mrebunravelingthe pages 11-12) | Strong general mechanism for rod morphogenesis; supports MreB-centered elongasome organization. High confidence. |
| RodZ | activates | Elongasome complex | 10.64898/2026.01.05.697639 | “RodZ activates the elongasome through two signaling pathways: one in the periplasm via MreCD and another in the cytoplasm through MreB” (zhan2026rodzactsthrough pages 1-5, zhan2026rodzactsthrough pages 19-22) | Direct support for activation relationship. High confidence. |
| Elongasome complex | mediates | Lateral peptidoglycan synthesis | 10.33696/signaling.4.101 | “The elongasome's primary function is cell elongation during division” and it “regulate[s] peptidoglycan (PG) synthesis and maintain[s] bacterial cell shape” (jain2023understandingelongasomeunit pages 2-4) | Well-supported general elongasome function. High confidence. |
| MreB | determines | Rod cell shape | 10.1101/2024.04.02.587816 | “MreB is absolutely essential for rod shape determination… cells transition from rod-shaped to spherical morphology” (maharjan2026alaninescanningmutagenesislibrary pages 11-14) | One of the strongest shape-determination edges. High confidence. |
| RodA-PBP2 | catalyzes | Peptidoglycan polymerization and crosslinking | 10.1186/s12964-025-02373-y | “RodA and PBP2 are critical for rod-shaped cell morphology” and “RodA-PBP2 coordinate peptidoglycan polymerization and crosslinking” (wang2025mrebunravelingthe pages 11-12, jain2023understandingelongasomeunit pages 2-4) | Direct enzymatic/morphogenetic role in elongasome. High confidence. |
| DivIVA | localizes | Polar peptidoglycan synthesis | 10.1186/s12866-024-03625-6 | “DivIVA is essential for polar growth in Actinomycetota” and in mycobacteria “focuses cell wall synthesis activity to cell poles” (sen2024adispensablesepiva pages 1-2, sen2024adispensablesepiva pages 10-12) | Actinobacteria-specific; strong support for pole-focused PG insertion. High confidence. |
| GPR | organizes | Polar growth | 10.1128/mbio.00764-21 | “GPR… serves as an organizing center for membrane and peptidoglycan synthesis during polar growth” (zupan2021agrobacteriumtumefaciensgrowth pages 1-2) | Agrobacterium-specific growth-pole scaffold. High confidence. |
| GPR loss | mislocalizes | PG synthesis (circumferential) | 10.1128/mbio.00764-21 | “Without GPR, PG synthesis becomes distributed around the cell periphery rather than concentrated at discrete polar locations, resulting in spherical cell morphology” (zupan2021agrobacteriumtumefaciensgrowth pages 10-11, zupan2021agrobacteriumtumefaciensgrowth pages 11-13) | Strong loss-of-function evidence linking polarity to shape. High confidence. |
| BacA | recruits | PbpC to stalk pole | 10.17192/z2023.0041 | “In C. crescentus, BacA and BacB form sheet-like structures at the stalked cell pole and recruit the penicillin-binding protein PbpC” (liu2022comprehensiveanalysisof pages 24-28) | Caulobacter-specific; useful for specialized polar morphogenesis. High confidence. |
| Bactofilins | regulate | Polar PG modification | 10.1371/journal.pgen.1010788 | “Bactofilins… interact directly or indirectly with peptidoglycan (PG) synthases and lytic enzymes… locally alter PG synthesis and composition” (richter2023interactingbactofilinsimpact pages 2-4) | Strong general role for accessory cytoskeleton in local wall remodeling. High confidence. |
| LD-transpeptidases | generate | 3-3 crosslinks in PG | 10.1371/journal.pgen.1011449 | “LDTs… are essential for maintaining cell shape and wall integrity” and mediate “LD crosslinks” in A. tumefaciens (aliashkevich2024essentialityofldtranspeptidation pages 4-7) | Strong biochemical role in Hyphomicrobiales polar growth. High confidence. |
| 3-3 crosslinks | confer | Enhanced stalk mechanical properties | 10.1371/journal.pgen.1007897 | “The 3–3 crosslinks are mechanically stiffer and more extended than 3–4 crosslinks, making them better suited to support stressed PG” (billini2019aspecializedmrebdependent pages 21-22) | Caulobacter stalk-specific mechanical inference is explicit. High confidence. |
| Stalk PG complex | combines | Elongasome + divisome components | 10.1371/journal.pgen.1007897 | “This complex is hybrid in composition, incorporating factors from both the elongasome (MreB, RodZ, RodA, PBP2) and divisome (DipM, SdpA, SdpB, CrbA)” (billini2019aspecializedmrebdependent pages 18-19) | Strong evidence for repurposed hybrid morphogenetic machinery. High confidence. |
| Polar PG synthesis | produces | Tapered pole morphology | Inferred from multiple sources | Polar growth factors “focus cell wall synthesis activity to cell poles” (sen2024adispensablesepiva pages 1-2); GPR localizes PG synthesis to the growth pole (zupan2021agrobacteriumtumefaciensgrowth pages 1-2, zupan2021agrobacteriumtumefaciensgrowth pages 10-11); stalk growth occurs by polar remodeling (billini2019aspecializedmrebdependent pages 18-19, billini2019aspecializedmrebdependent pages 19-21) | Mechanistically plausible for spindle/taper formation, but not directly demonstrated for fusiform bacteria. UNCERTAIN. |
| Membrane curvature | sensed by | MreB-RodZ complex | 10.1186/s12964-025-02373-y | “The MreB-RodZ complex senses membrane curvature changes induced by peptidoglycan synthesis and adaptively adjusts filament trajectories” (wang2025mrebunravelingthe pages 9-11) | Directly supported mechanochemical feedback edge. High confidence. |
| Polarisome (DivIVA-Scy-FilP) | coordinates | Apical cell wall synthesis | 10.1101/2025.06.24.661030 | “DivIVA functions as a core component of a dynamic complex at hyphal tips that coordinates cell wall material insertion” and interacts with “Scy and FilP” (lubbers2025definingtheminimal pages 10-12, lubbers2025definingtheminimal pages 12-14) | Streptomyces/filamentous actinobacteria-specific. High confidence. |
| Peptidoglycan sacculus | determines | Cell shape | 10.1128/ecosalplus.esp-0010-2020 | “These processes require spatio-temporal regulation for successful assembly of a robust sacculus to protect the cell from turgor and determine cell shape” (billini2019aspecializedmrebdependent pages 1-2) | Foundational, broad bacterial principle. High confidence. |
| Turgor pressure | resisted by | Peptidoglycan sacculus | 10.1128/ecosalplus.esp-0010-2020 | Peptidoglycan assembly forms “a robust sacculus to protect the cell from turgor” (billini2019aspecializedmrebdependent pages 1-2) | General biophysical principle relevant to shape maintenance. High confidence. |


*Table: This table lists evidence-backed subject-predicate-object edges relevant to curating a spindle-shaped microbial trait causal graph. It emphasizes experimentally supported links among cytoskeletal proteins, peptidoglycan synthesis, polar growth machinery, and morphology, while clearly flagging inferred edges.*

## 5. Ontology Grounding

| Term | Suggested CURIE | Source |
|---|---|---|
| spindle_shaped | METPO:1000692 | METPO ontology |
| cell morphogenesis | GO:0000902 | Gene Ontology |
| cell shape determination | GO:0008360 | Gene Ontology |
| peptidoglycan biosynthetic process | GO:0009252 | Gene Ontology |
| peptidoglycan | CHEBI:8005 | ChEBI |
| lipid II | CHEBI:16902 | ChEBI |
| *Fusobacterium nucleatum* | NCBITaxon:851 | NCBI Taxonomy |
| *Caulobacter crescentus* | NCBITaxon:155892 | NCBI Taxonomy |
| *Agrobacterium tumefaciens* | NCBITaxon:358 | NCBI Taxonomy |
| *Rhodomicrobium vannielii* | NCBITaxon:1069 | NCBI Taxonomy |
| *Streptomyces venezuelae* | NCBITaxon:54571 | NCBI Taxonomy |
| *Corynebacterium glutamicum* | NCBITaxon:1718 | NCBI Taxonomy |

Note: CURIEs for MreB, RodZ, MreC, MreD, RodA, PBP2, DivIVA, GPR, BacA, and LDTs vary by organism and are best assigned to specific UniProt entries per taxon. Label-only identifiers are used here where no single stable cross-taxon identifier exists.

## 6. DOI-First Bibliography

1. Wang Y, Jiang Y, Song Z, et al. (2025). MreB: unraveling the molecular mechanisms of bacterial shape, division, and environmental adaptation. *Cell Communication and Signaling* 23. DOI: 10.1186/s12964-025-02373-y (wang2025mrebunravelingthe pages 11-12, wang2025mrebunravelingthe pages 7-9, wang2025mrebunravelingthe pages 9-11)

2. Maharjan S, Sloan R, Lusk J, et al. (2024). Alanine-scanning mutagenesis library of MreB reveals distinct roles for regulating cell shape and viability. *bioRxiv*. DOI: 10.1101/2024.04.02.587816 (maharjan2026alaninescanningmutagenesislibrary pages 21-24, maharjan2026alaninescanningmutagenesislibrary pages 11-14, maharjan2026alaninescanningmutagenesislibrary pages 24-26)

3. Zhan R, Gong H, Li Y, et al. (2026). RodZ acts through MreBCD to activate the elongasome in *Escherichia coli*. *bioRxiv*. DOI: 10.64898/2026.01.05.697639 (zhan2026rodzactsthrough pages 1-5, zhan2026rodzactsthrough pages 19-22)

4. Jain P (2023). Understanding elongasome unit of Mycobacterium and its comparative analysis with other model organisms. *J Cellular Signaling* 4:142–150. DOI: 10.33696/signaling.4.101 (jain2023understandingelongasomeunit pages 2-4, jain2023understandingelongasomeunit pages 7-8)

5. Richter P, Melzer B, Müller FD (2023). Interacting bactofilins impact cell shape of the MreB-less multicellular *Rhodomicrobium vannielii*. *PLOS Genetics* 19. DOI: 10.1371/journal.pgen.1010788 (richter2023interactingbactofilinsimpact pages 15-16, richter2023interactingbactofilinsimpact pages 26-27, richter2023interactingbactofilinsimpact pages 2-4, richter2023interactingbactofilinsimpact pages 13-15)

6. Zupan J, Guo Z, Biddle T, Zambryski P (2021). *Agrobacterium tumefaciens* growth pole ring protein: C terminus and internal apolipoprotein homologous domains are essential for function and subcellular localization. *mBio* 12. DOI: 10.1128/mbio.00764-21 (zupan2021agrobacteriumtumefaciensgrowth pages 1-2, zupan2021agrobacteriumtumefaciensgrowth pages 10-11, zupan2021agrobacteriumtumefaciensgrowth pages 11-13, zupan2021agrobacteriumtumefaciensgrowth pages 2-4)

7. Aliashkevich A, Guest T, Alvarez L, et al. (2024). LD-transpeptidation is crucial for fitness and polar growth in *Agrobacterium tumefaciens*. *PLOS Genetics* 20:e1011449. DOI: 10.1371/journal.pgen.1011449 (aliashkevich2024essentialityofldtranspeptidation pages 4-7, aliashkevich2024ldtranspeptidationiscrucial pages 22-23)

8. Billini M, Biboy J, Kühn J, Vollmer W, Thanbichler M (2019). A specialized MreB-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in *Caulobacter crescentus*. *PLoS Genetics* 15:e1007897. DOI: 10.1371/journal.pgen.1007897 (billini2019aspecializedmrebdependent pages 1-2, billini2019aspecializedmrebdependent pages 7-8, billini2019aspecializedmrebdependent pages 21-22, billini2019aspecializedmrebdependent pages 16-18, billini2019aspecializedmrebdependent pages 18-19, billini2019aspecializedmrebdependent pages 14-16, billini2019aspecializedmrebdependent pages 19-21)

9. Sen BC, Mavi PS, Irazoki O, et al. (2024). A dispensable SepIVA orthologue in *Streptomyces venezuelae* is associated with polar growth and not cell division. *BMC Microbiology* 24. DOI: 10.1186/s12866-024-03625-6 (sen2024adispensablesepiva pages 1-2, sen2024adispensablesepiva pages 10-12)

10. Lubbers M, Bajramović B, Ongenae V, et al. (2025). Defining the minimal structural requirements of DivIVA in filamentous Actinomycetota. *bioRxiv*. DOI: 10.1101/2025.06.24.661030 (lubbers2025definingtheminimal pages 12-14, lubbers2025definingtheminimal pages 10-12)

11. Meyer FM (2024). Understanding the growth of *Corynebacterium glutamicum*. Dissertation, LMU Munich. DOI: 10.5282/edoc.33534 (meyer2024understandingthegrowth pages 35-38)

12. Liu Y (2022). Comprehensive analysis of the cytoskeletal protein bactofilin in *Caulobacter crescentus*. Philipps-Universität Marburg. DOI: 10.17192/z2023.0041 (liu2022comprehensiveanalysisof pages 24-28)

13. Cameron TA, Margolin W (2024). Insights into the assembly and regulation of the bacterial divisome. *Nature Reviews Microbiology* 22:33–45. DOI: 10.1038/s41579-023-00942-x

14. Garde S, Chodisetti PK, Reddy M (2021). Peptidoglycan: Structure, Synthesis, and Regulation. *EcoSal Plus* 9. DOI: 10.1128/ecosalplus.esp-0010-2020

## 7. Warnings and Curation Notes

1. **UNCERTAIN EDGE — Polar PG synthesis → Tapered pole morphology:** While polar PG synthesis is well-documented in multiple bacterial lineages, the specific molecular mechanism that produces pointed (tapered) poles rather than hemispherical poles has not been directly demonstrated for fusiform bacteria such as *Fusobacterium nucleatum*. This edge should be flagged as inferred and awaiting direct experimental validation.

2. **Taxon-specific mechanisms:** Many of the identified molecular determinants (DivIVA in Actinobacteria, GPR in Agrobacterium, bactofilins in Caulobacter) are lineage-specific. The existing 6-node causal graph for spindle_shaped_symmetric_taper should remain general, and taxon-specific nodes should be annotated accordingly.

3. **Fusobacterium nucleatum cell shape determinants:** Despite being the canonical fusiform bacterium, the specific genetic determinants of fusiform morphology in *F. nucleatum* remain poorly characterized at the molecular level. No direct studies were found that identify specific shape-determining genes in this organism. The Fusobacteriota phylum is phylogenetically distant from model organisms, and its cell wall synthesis machinery may involve unique components. This represents a significant knowledge gap.

4. **Archaeal spindle-shaped viruses:** The spindle-shaped morphology of fuselloviruses (e.g., SSV1) arises from capsid protein self-assembly mechanisms entirely distinct from bacterial PG-based morphogenesis. These should not be curated into the same causal graph without explicit separation.

5. **Elongasome-absent bacteria:** Some organisms that display polar growth (e.g., Hyphomicrobiales, Actinobacteria) lack a canonical MreB-dependent elongasome. Their shape mechanisms rely on alternative polar growth determinants (DivIVA, GPR, bactofilins). The causal graph should accommodate both elongasome-dependent and elongasome-independent paths to spindle morphology.

6. **Mechanical/biophysical nodes:** Turgor pressure and membrane curvature are important biophysical parameters but function as background constraints rather than specific genetic determinants. They should be included as contextual nodes but not as primary causal drivers of the spindle-shaped trait.


References

1. (wang2025mrebunravelingthe pages 11-12): Yaqi Wang, Yalan Jiang, Zhixuan Song, Chengbin Zhu, Yujun Tang, Jiaofeng Peng, and Peng Liu. Mreb: unraveling the molecular mechanisms of bacterial shape, division, and environmental adaptation. Cell Communication and Signaling, Aug 2025. URL: https://doi.org/10.1186/s12964-025-02373-y, doi:10.1186/s12964-025-02373-y. This article has 12 citations and is from a peer-reviewed journal.

2. (billini2019aspecializedmrebdependent pages 1-2): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

3. (jain2023understandingelongasomeunit pages 2-4): Preeti Jain. Understanding elongasome unit of mycobacterium and its comparative analysis with other model organisms. Journal of Cellular Signaling, 4:142-150, Sep 2023. URL: https://doi.org/10.33696/signaling.4.101, doi:10.33696/signaling.4.101. This article has 0 citations.

4. (zhan2026rodzactsthrough pages 1-5): Rui Zhan, Han Gong, Ying Li, Yuanyuan Cui, Xiangdong Chen, Joe Lutkenhaus, and Shishen Du. Rodz acts through mrebcd to activate the elongasome in <i>escherichia coli</i>. bioRxiv, Jan 2026. URL: https://doi.org/10.64898/2026.01.05.697639, doi:10.64898/2026.01.05.697639. This article has 1 citations.

5. (zhan2026rodzactsthrough pages 19-22): Rui Zhan, Han Gong, Ying Li, Yuanyuan Cui, Xiangdong Chen, Joe Lutkenhaus, and Shishen Du. Rodz acts through mrebcd to activate the elongasome in <i>escherichia coli</i>. bioRxiv, Jan 2026. URL: https://doi.org/10.64898/2026.01.05.697639, doi:10.64898/2026.01.05.697639. This article has 1 citations.

6. (maharjan2026alaninescanningmutagenesislibrary pages 11-14): Suman Maharjan, Ryan Sloan, Jada Lusk, Rose Bevienguevarr, Jacob Surber, and Randy M. Morgenstein. Alanine-scanning mutagenesis library of mreb reveals distinct roles for regulating cell shape and viability. BioRxiv, Apr 2026. URL: https://doi.org/10.1101/2024.04.02.587816, doi:10.1101/2024.04.02.587816. This article has 2 citations.

7. (sen2024adispensablesepiva pages 1-2): Beer Chakra Sen, Parminder Singh Mavi, Oihane Irazoki, Susmita Datta, Sebastian Kaiser, Felipe Cava, and Klas Flärdh. A dispensable sepiva orthologue in streptomyces venezuelae is associated with polar growth and not cell division. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03625-6, doi:10.1186/s12866-024-03625-6. This article has 5 citations and is from a peer-reviewed journal.

8. (sen2024adispensablesepiva pages 10-12): Beer Chakra Sen, Parminder Singh Mavi, Oihane Irazoki, Susmita Datta, Sebastian Kaiser, Felipe Cava, and Klas Flärdh. A dispensable sepiva orthologue in streptomyces venezuelae is associated with polar growth and not cell division. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03625-6, doi:10.1186/s12866-024-03625-6. This article has 5 citations and is from a peer-reviewed journal.

9. (lubbers2025definingtheminimal pages 12-14): Maarten Lubbers, Belmin Bajramović, Véronique Ongenae, Joost Willemse, Dieuwertje de Bruin, Niels Mulder, Bastienne Vriesendorp, Francisco Barona-Gómez, Ariane Briegel, Gilles P. van Wezel, Klas Flärdh, and Dennis Claessen. Defining the minimal structural requirements of diviva in filamentous actinomycetota. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2025.06.24.661030, doi:10.1101/2025.06.24.661030. This article has 0 citations.

10. (lubbers2025definingtheminimal pages 10-12): Maarten Lubbers, Belmin Bajramović, Véronique Ongenae, Joost Willemse, Dieuwertje de Bruin, Niels Mulder, Bastienne Vriesendorp, Francisco Barona-Gómez, Ariane Briegel, Gilles P. van Wezel, Klas Flärdh, and Dennis Claessen. Defining the minimal structural requirements of diviva in filamentous actinomycetota. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2025.06.24.661030, doi:10.1101/2025.06.24.661030. This article has 0 citations.

11. (meyer2024understandingthegrowth pages 35-38): Fabian Mark Meyer. Understanding the growth of corynebacterium glutamicum. Dissertation, Jan 2024. URL: https://doi.org/10.5282/edoc.33534, doi:10.5282/edoc.33534. This article has 0 citations.

12. (zupan2021agrobacteriumtumefaciensgrowth pages 1-2): John Zupan, Zisheng Guo, Trevor Biddle, and Patricia Zambryski. Agrobacterium tumefaciens growth pole ring protein: c terminus and internal apolipoprotein homologous domains are essential for function and subcellular localization. Jun 2021. URL: https://doi.org/10.1128/mbio.00764-21, doi:10.1128/mbio.00764-21. This article has 15 citations and is from a domain leading peer-reviewed journal.

13. (zupan2021agrobacteriumtumefaciensgrowth pages 11-13): John Zupan, Zisheng Guo, Trevor Biddle, and Patricia Zambryski. Agrobacterium tumefaciens growth pole ring protein: c terminus and internal apolipoprotein homologous domains are essential for function and subcellular localization. Jun 2021. URL: https://doi.org/10.1128/mbio.00764-21, doi:10.1128/mbio.00764-21. This article has 15 citations and is from a domain leading peer-reviewed journal.

14. (zupan2021agrobacteriumtumefaciensgrowth pages 10-11): John Zupan, Zisheng Guo, Trevor Biddle, and Patricia Zambryski. Agrobacterium tumefaciens growth pole ring protein: c terminus and internal apolipoprotein homologous domains are essential for function and subcellular localization. Jun 2021. URL: https://doi.org/10.1128/mbio.00764-21, doi:10.1128/mbio.00764-21. This article has 15 citations and is from a domain leading peer-reviewed journal.

15. (aliashkevich2024essentialityofldtranspeptidation pages 4-7): Alena Aliashkevich, Thomas Guest, Laura Alvarez, Michael C. Gilmore, Jennifer Amstutz, André Mateus, Bastian Schiffthaler, Iñigo Ruiz, Athanasios Typas, Mikhail M. Savitski, Pamela J. B. Brown, and Felipe Cava. Essentiality of ld-transpeptidation in<i>agrobacterium tumefaciens</i>. BioRxiv, Jun 2024. URL: https://doi.org/10.1101/2024.06.21.600065, doi:10.1101/2024.06.21.600065. This article has 1 citations.

16. (richter2023interactingbactofilinsimpact pages 2-4): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

17. (liu2022comprehensiveanalysisof pages 24-28): Ying Liu. Comprehensive analysis of the cytoskeletal protein bactofilin in caulobacter crescentus. Text, Sep 2022. URL: https://doi.org/10.17192/z2023.0041, doi:10.17192/z2023.0041. This article has 0 citations and is from a peer-reviewed journal.

18. (richter2023interactingbactofilinsimpact pages 13-15): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

19. (richter2023interactingbactofilinsimpact pages 15-16): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

20. (billini2019aspecializedmrebdependent pages 7-8): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

21. (billini2019aspecializedmrebdependent pages 21-22): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

22. (billini2019aspecializedmrebdependent pages 18-19): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

23. (billini2019aspecializedmrebdependent pages 19-21): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

24. (wang2025mrebunravelingthe pages 9-11): Yaqi Wang, Yalan Jiang, Zhixuan Song, Chengbin Zhu, Yujun Tang, Jiaofeng Peng, and Peng Liu. Mreb: unraveling the molecular mechanisms of bacterial shape, division, and environmental adaptation. Cell Communication and Signaling, Aug 2025. URL: https://doi.org/10.1186/s12964-025-02373-y, doi:10.1186/s12964-025-02373-y. This article has 12 citations and is from a peer-reviewed journal.

25. (zupan2021agrobacteriumtumefaciensgrowth pages 2-4): John Zupan, Zisheng Guo, Trevor Biddle, and Patricia Zambryski. Agrobacterium tumefaciens growth pole ring protein: c terminus and internal apolipoprotein homologous domains are essential for function and subcellular localization. Jun 2021. URL: https://doi.org/10.1128/mbio.00764-21, doi:10.1128/mbio.00764-21. This article has 15 citations and is from a domain leading peer-reviewed journal.

26. (aliashkevich2024ldtranspeptidationiscrucial pages 22-23): Alena Aliashkevich, Thomas Guest, Laura Alvarez, Michael C. Gilmore, Daniel Rea, Jennifer Amstutz, André Mateus, Bastian Schiffthaler, Iñigo Ruiz, Athanasios Typas, Mikhail M. Savitski, Pamela J. B. Brown, and Felipe Cava. Ld-transpeptidation is crucial for fitness and polar growth in agrobacterium tumefaciens. Oct 2024. URL: https://doi.org/10.1371/journal.pgen.1011449, doi:10.1371/journal.pgen.1011449. This article has 12 citations and is from a domain leading peer-reviewed journal.

27. (wang2025mrebunravelingthe pages 7-9): Yaqi Wang, Yalan Jiang, Zhixuan Song, Chengbin Zhu, Yujun Tang, Jiaofeng Peng, and Peng Liu. Mreb: unraveling the molecular mechanisms of bacterial shape, division, and environmental adaptation. Cell Communication and Signaling, Aug 2025. URL: https://doi.org/10.1186/s12964-025-02373-y, doi:10.1186/s12964-025-02373-y. This article has 12 citations and is from a peer-reviewed journal.

28. (maharjan2026alaninescanningmutagenesislibrary pages 21-24): Suman Maharjan, Ryan Sloan, Jada Lusk, Rose Bevienguevarr, Jacob Surber, and Randy M. Morgenstein. Alanine-scanning mutagenesis library of mreb reveals distinct roles for regulating cell shape and viability. BioRxiv, Apr 2026. URL: https://doi.org/10.1101/2024.04.02.587816, doi:10.1101/2024.04.02.587816. This article has 2 citations.

29. (maharjan2026alaninescanningmutagenesislibrary pages 24-26): Suman Maharjan, Ryan Sloan, Jada Lusk, Rose Bevienguevarr, Jacob Surber, and Randy M. Morgenstein. Alanine-scanning mutagenesis library of mreb reveals distinct roles for regulating cell shape and viability. BioRxiv, Apr 2026. URL: https://doi.org/10.1101/2024.04.02.587816, doi:10.1101/2024.04.02.587816. This article has 2 citations.

30. (jain2023understandingelongasomeunit pages 7-8): Preeti Jain. Understanding elongasome unit of mycobacterium and its comparative analysis with other model organisms. Journal of Cellular Signaling, 4:142-150, Sep 2023. URL: https://doi.org/10.33696/signaling.4.101, doi:10.33696/signaling.4.101. This article has 0 citations.

31. (richter2023interactingbactofilinsimpact pages 26-27): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

32. (billini2019aspecializedmrebdependent pages 16-18): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

33. (billini2019aspecializedmrebdependent pages 14-16): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.