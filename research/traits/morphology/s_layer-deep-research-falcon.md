---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:22:34.068599'
end_time: '2026-06-18T09:41:57.755859'
duration_seconds: 1163.69
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
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
  causal_graph_summary: 's_layer_2d_protein_array: 3 nodes, 2 edges'
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
- **Trait label:** S-layer
- **METPO identifier:** traitmech:000064
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell surface is coated by a crystalline, two-dimensional array of self-assembling proteinaceous (glyco)protein subunits (a surface layer), found in many bacteria and most archaea.
- **Parent traits:** METPO:1000059
- **Synonyms:** surface layer
- **Existing evidence:** DOI:10.1038/nrmicro3213:  (Fagan & Fairweather describe the S-layer as a self-assembled, regularly spaced two-dimensional protein array coating the cell surface.) | DOI:10.1038/s41579-025-01258-8:  (Review of assembly, architecture and functional roles of microbial surface layers supports the S-layer as a defined cell-surface structure.)
- **Existing causal graph summary:** s_layer_2d_protein_array: 3 nodes, 2 edges

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
- **Existing causal graph summary:** s_layer_2d_protein_array: 3 nodes, 2 edges

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


## Microbial Trait Causal Graph Report: **S-layer** (METPO: traitmech:000064)

### 0. Scope summary (TraitMech curation)
An S-layer (surface layer) is a microbial morphology trait in which the cell surface is coated by a crystalline (para-/pseudo-crystalline), self-assembling two-dimensional lattice of proteinaceous subunits, often (glyco)proteins, forming the outermost envelope layer. Recent structural studies emphasize (i) broad taxonomic distribution (many bacteria; most archaea), (ii) frequent post-translational glycosylation and cation binding, and (iii) envelope-context-dependent attachment strategies (e.g., Gram-positive teichoic acids or SCWP; diderm OM/LPS-associated biogenesis). (gambelli2024structureofthe pages 1-2, sogues2023structureandfunction pages 1-2, sagmeister2024themoleculararchitecture pages 1-2)

**Boundary cases / nearby traits**
* Distinguish **S-layer** from capsules and generic extracellular polymeric substances (EPS): S-layers are ordered 2D lattices of repeating protein subunits; capsules/EPS are typically amorphous polysaccharide-rich matrices. However, an S-layer protein can appear as a transported matrix component in some systems (e.g., anammox biofilms), so “S-layer protein in matrix” should not be automatically equated with “cell-encasing S-layer lattice.” (wong2023surfacelayerproteinis pages 1-2)
* Envelope context: 
  * **Gram-positive** anchoring via teichoic acids (LTA/WTA) in lactobacilli, or via **SLH domains** binding secondary cell wall polysaccharide (SCWP) in *Bacillus anthracis*. (sagmeister2024themoleculararchitecture pages 6-9, sogues2023structureandfunction pages 1-2)
  * **Diderm bacteria** (e.g., *Caulobacter crescentus*) assemble S-layers on the outer membrane, with dependence on LPS and coordination with peptidoglycan turnover. (herdman2024cellcycledependent pages 8-9)
  * **Archaea** often rely on the S-layer as a principal/sole wall component; *Sulfolobus acidocaldarius* has a two-component S-layer with an outer glycoprotein (SlaA) and an inner membrane-bound component (SlaB). (gambelli2024structureofthe pages 1-2)

---

### 1. Key concepts and definitions (current understanding)

#### 1.1 Structural definition and common physical properties
* S-layers are resilient 2D lattices; pores can occupy up to ~70% of the S-layer surface, consistent with a porous molecular-sieve-like layer rather than a continuous barrier. (gambelli2024structureofthe pages 1-2)
* In *S. acidocaldarius*, pore dimensions were reported as **48 Å (hexagonal pores)** and **85 Å (trimeric pores)**; glycans project into pores and may reduce effective pore size. (gambelli2024structureofthe pages 12-13)

#### 1.2 Biogenesis and attachment strategies
* **Self-assembly:** S-layer proteins can self-polymerize into crystalline lattices; the *Lactobacillus* SlpA/SlpX system is explicitly described as self-assembling with defined assembly vs attachment regions. (sagmeister2024themoleculararchitecture pages 1-2)
* **Cation dependence:** In *C. crescentus*, purified RsaA plus calcium forms hexameric lattices in vitro (a direct mechanistic condition for ordered polymerization). (herdman2024cellcycledependent pages 8-9)
* **Gram-positive teichoic-acid anchoring:** Lactobacillus S-layer proteins attach non-covalently to (lipo)teichoic acids; ITC/NMR supported two GroP (glycerol phosphate repeat) binding sites within a teichoic-acid-binding (TAB) domain. (sagmeister2024themoleculararchitecture pages 6-9)
* **SLH domain anchoring to SCWP:** In *B. anthracis*, Sap and EA1 contain SLH domains that bind the ketal-pyruvylated N-acetylmannosamine unit in the SCWP to anchor the S-layer to the cell surface. (sogues2023structureandfunction pages 1-2)

#### 1.3 Post-translational modification (archaea emphasis)
* Archaeal S-layer proteins are frequently glycosylated. In *S. acidocaldarius*, SlaA was predicted to have **31 N-glycosylation sites**, with many glycan densities visible by cryo-EM. The oligosaccharyltransferase **AglB** is described as essential. (gambelli2024structureofthe pages 12-13)

---

### 2. Recent developments and latest research (prioritizing 2023–2024)

#### 2.1 Atomic/near-atomic architectures and assembly interfaces
* **Archaeal two-component S-layer:** Cryo-EM/cryoET-enabled atomic modeling of *S. acidocaldarius* SlaA/SlaB highlights how an outer flexible glycoprotein and an inner membrane-bound component form an interwoven lattice, expanding structural understanding of archaeal cell walls. (gambelli2024structureofthe pages 1-2)
* **Lactobacillus assembly + teichoic-acid attachment:** PNAS 2024 provides atomic-resolution SLP structures and a model for lattice self-assembly and TA attachment, including explicit binding sites. (sagmeister2024themoleculararchitecture pages 1-2, sagmeister2024themoleculararchitecture pages 6-9)

#### 2.2 Coordination with broader envelope biogenesis (diderm bacteria)
* **Cell-cycle coordinated insertion:** In *C. crescentus*, S-layer biogenesis localizes to growth/turnover regions; it follows new peptidoglycan synthesis and is disrupted upon dysregulation of MreB or LPS. This supports a multi-layer envelope coordination model rather than S-layer “static coating.” (herdman2024cellcycledependent pages 8-9)

#### 2.3 Domain-level functional mapping (phage receptors)
* **Phage receptor mapping in *C. difficile*:** SlpA loss renders cells resistant; complementation with distinct S-layer cassette types (SLCTs) changes susceptibility; deletion of a specific **D2 domain** in the low-molecular-weight (LMW) fragment abolishes infection by some phages but not others. (royer2023clostridioidesdifficileslayer pages 8-10, royer2023clostridioidesdifficileslayer pages 1-2)

#### 2.4 S-layers in secretion-system context (Bacteroidota)
* A 2023 review of the **type IX secretion system (T9SS)** explicitly describes secretion of glycoproteins that self-assemble into a 2D crystalline S-layer lattice in *Tannerella forsythia* (TfsA/TfsB) and links Gram-negative S-layers to LPS-associated attachment and mechanical protection. (paillat2023ajourneywith pages 7-8)

---

### 3. Current applications and real-world implementations

#### 3.1 Host–microbe interaction and immunomodulation (probiotics / mucosal health)
* In the lower female reproductive tract, *L. crispatus* S-layer proteins modulate innate immune responses, with reported mechanisms including **shielding of TLR ligands** and selective interaction with **DC-SIGN**, associated with lower pro-inflammatory cytokines. (decout2024lactobacilluscrispatusslayer pages 1-2)

#### 3.2 Phage therapy design (rational host-range engineering)
* Demonstration that SlpA is a general receptor for multiple *C. difficile* phages, and that SLCT isoforms and the D2 domain influence adsorption/infection, directly supports rational phage-cocktail design strategies that account for S-layer diversity. (royer2023clostridioidesdifficileslayer pages 4-6, royer2023clostridioidesdifficileslayer pages 8-10)

#### 3.3 Biofilm ecology and wastewater-relevant systems
* In environmental anammox granules, an extracellular S-layer glycoprotein (BROSI_A1236) behaves as a **“public-good” EPS** and adhesive scaffold facilitating organization of other taxa (e.g., filamentous Chloroflexi) into a biofilm lattice—an ecological implementation relevant to engineered wastewater systems. (wong2023surfacelayerproteinis pages 1-2)

#### 3.4 Biomimetic nanotechnology / biosensing
* A 2023 Science Advances implementation used **2D crystalline S-layer proteins as dense antifouling linkers** in a graphene FET array biosensor architecture. The work reports ligand-binding Kd values (e.g., ~20 nM range for CXCL12) and detection limits in human serum (e.g., **LOD 7.2 nM for CXCL12 and 26 pM for gp41–120**) plus device regeneration after immersion in pH 3 glycine buffer for ~1 hour. (qing2023scalablebiomimeticsensing pages 5-6)

---

### 4. Expert opinions / analysis grounded in authoritative sources
Across 2023–2024 sources, a convergent view is that S-layers are not merely passive coats but dynamic, mechanistically integrated envelope modules:
* **Mechanical stabilization / exoskeleton concept:** Direct perturbation of the *B. anthracis* EA1 lattice (nanobody-induced depolymerization) caused defects, membrane blebbing, and hypotonic lysis, supporting a mechanical-stability function beyond “adhesin/sieve.” (sogues2023structureandfunction pages 1-2)
* **Envelope systems coordination:** In *Caulobacter*, S-layer insertion follows peptidoglycan synthesis and depends on OM/LPS state, supporting a multi-layer envelope coordination paradigm. (herdman2024cellcycledependent pages 8-9)
* **Functional modularity via domains:** Diverse anchoring modules (TAB vs SLH) and receptor subdomains (SlpA D2) support a causal-graph view where “S-layer present” is downstream of multiple distinct biogenesis/attachment mechanisms rather than one conserved pathway. (sagmeister2024themoleculararchitecture pages 6-9, sogues2023structureandfunction pages 1-2, royer2023clostridioidesdifficileslayer pages 8-10)

---

### 5. Recent statistics and quantitative data (from cited studies)

* **Porosity:** S-layer pores can occupy up to **~70%** of the surface (general archaeal S-layer physical characterization). (gambelli2024structureofthe pages 1-2)
* **Pore sizes (archaea):** *S. acidocaldarius* pores **48 Å (hexagonal)** and **85 Å (trimeric)**; glycans reduce effective pore size. (gambelli2024structureofthe pages 12-13)
* **Glycosylation (archaea):** SlaA predicted **31 N-glycosylation sites**; multiple glycan densities visible in cryo-EM. (gambelli2024structureofthe pages 12-13)
* **Stress-dependent S-layer composition shift (Lactobacillus):** SlpX comprises **~10%** of the S-layer under physiological conditions and increases to **~40%** under environmental stress in *L. acidophilus* NCFM. (sagmeister2024themoleculararchitecture pages 1-2)
* **Phage adsorption dependence on SlpA (C. difficile):** WT adsorption levels reported at **92.9% ± 1.7%** (ϕCD38-2), **81.0% ± 6.7%** (ϕCD146), **65% ± 8.5%** (ϕCD111), dropping to near-zero/low adsorption in SlpA-deficient mutants, and domain-level deletion (D2) drastically reduced adsorption for specific phages. (royer2023clostridioidesdifficileslayer pages 4-6, royer2023clostridioidesdifficileslayer pages 8-10)
* **Biosensor metrics (engineered S-layer arrays):** device-estimated **Kd 20.1 ± 9.1 nM** (CXCL12), **LOD ~18 nM** in buffer, and in human serum **LOD 7.2 nM (CXCL12)** and **26 pM (gp41–120)**. (qing2023scalablebiomimeticsensing pages 5-6)

---

## 6. Candidate nodes for `data/traits/morphology/s_layer.yaml`

### 6.1 Proteins / complexes (label-first; add UniProt as available during curation)
* **SlpA** (Lactobacillus S-layer structural protein; also *C. difficile* receptor) (sagmeister2024themoleculararchitecture pages 1-2, royer2023clostridioidesdifficileslayer pages 8-10)
* **SlpX**, **SlpB** (Lactobacillus S-layer proteins; stress-responsive composition shift) (sagmeister2024themoleculararchitecture pages 1-2)
* **RsaA** (*Caulobacter crescentus* S-layer protein) (herdman2024cellcycledependent pages 8-9)
* **Sap**, **EA1** (*Bacillus anthracis* mutually exclusive S-layers) (sogues2023structureandfunction pages 1-2)
* **SlaA**, **SlaB** (*Sulfolobus acidocaldarius* two-component archaeal S-layer) (gambelli2024structureofthe pages 1-2)
* **AglB** (archaeal oligosaccharyltransferase mediating S-layer glycosylation) (gambelli2024structureofthe pages 12-13)
* **BROSI_A1236** (anammox S-layer glycoprotein acting as EPS) (wong2023surfacelayerproteinis pages 1-2)
* **DR_2577 (“SlpA”) / DR_0644** (*Deinococcus radiodurans* S-layer complex subunits; oxidative stress quenching) (farci2023thesdbcis pages 1-2)

### 6.2 Domains / motifs
* **TAB (teichoic-acid-binding) domain** (SlpA/SlpX) (sagmeister2024themoleculararchitecture pages 6-9, sagmeister2024themoleculararchitecture media ab0cf737)
* **SLH domains** (Sap/EA1 anchoring to SCWP) (sogues2023structureandfunction pages 1-2)
* **D2 domain** within LMW fragment of *C. difficile* SlpA (phage adsorption determinant) (royer2023clostridioidesdifficileslayer pages 8-10)
* **Assembly/crystallization domain** (e.g., EA1AD) (sogues2023structureandfunction pages 1-2)

### 6.3 Chemicals / polymers / envelope components
* **Ca2+** (CHEBI:29108) (herdman2024cellcycledependent pages 8-9, sogues2023structureandfunction pages 1-2)
* **Lipoteichoic acid (LTA)**, **wall teichoic acid (WTA)** (TAB binding) (sagmeister2024themoleculararchitecture pages 6-9)
* **Secondary cell wall polysaccharide (SCWP)** including ketal-pyruvylated N-acetylmannosamine (SLH binding) (sogues2023structureandfunction pages 1-2)
* **Lipopolysaccharide (LPS)** (S-layer insertion dependence in diderm bacteria) (herdman2024cellcycledependent pages 8-9)
* **Peptidoglycan** (turnover sites coordinating insertion) (herdman2024cellcycledependent pages 8-9)

### 6.4 Processes / functions (GO identifiers where unambiguous)
* **Protein N-linked glycosylation** (GO:0006487) (gambelli2024structureofthe pages 12-13)
* **Protein lattice assembly** (candidate GO term for S-layer assembly; may require GO mapping in curation) (herdman2024cellcycledependent pages 8-9)
* **Phage adsorption / receptor function** (label-only) (royer2023clostridioidesdifficileslayer pages 4-6)
* **Innate immune modulation via receptor binding (DC-SIGN) / TLR ligand shielding** (label-only) (decout2024lactobacilluscrispatusslayer pages 1-2)

---

## 7. Candidate causal edges (curation-ready table)
The following table is designed to be directly mined into TraitMech edges (subject–predicate–object) with evidence and notes.

| Edge (Subject—Predicate—Object) | Entity types (gene/protein/process/environment/chemical) | Suggested ontology grounding (CURIEs if available; otherwise label-only) | Evidence snippet (short quote or paraphrase tightly tied to text) | Reference (DOI + URL + year) | Certainty/notes (taxon-specific, inferred, requires review) |
|---|---|---|---|---|---|
| S-layer protein (SLP) — self-assembles into — 2D paracrystalline S-layer lattice | protein → process/structure | GO:0045006 protein-lattice assembly; label-only: S-layer lattice | “S-layers are self-assembling, crystalline surface proteins”; in *Lactobacillus*, the N-terminal region mediates self-assembly into the layer (sagmeister2024themoleculararchitecture pages 1-2) | DOI:10.1073/pnas.2401686121 · https://doi.org/10.1073/pnas.2401686121 · 2024 | Broad but not universal in mechanistic detail; curation-safe at class level, taxa-specific domains vary. |
| Ca2+ — promotes — RsaA/S-layer lattice polymerization | chemical/environment → process | CHEBI:29108 calcium(2+); UniProt/label-only: RsaA; GO:0045006 | In *C. crescentus*, “purified RsaA plus calcium spontaneously forms hexameric lattices,” indicating calcium requirement for ordered polymerization (herdman2024cellcycledependent pages 8-9) | DOI:10.1038/s41467-024-47529-5 · https://doi.org/10.1038/s41467-024-47529-5 · 2024 | Strong, but taxon-specific to *Caulobacter* for direct experiment. |
| Ca2+ binding sites in EA1 assembly domain — stabilize — assembly-competent conformation / S-layer stability | protein domain + chemical → process | CHEBI:29108; label-only: EA1 assembly domain; GO:0045006 | EA1 has “three calcium-binding sites [that] stabilize interdomain contacts and promote an assembly-competent conformation” (sogues2023structureandfunction pages 1-2) | DOI:10.1038/s41467-023-42826-x · https://doi.org/10.1038/s41467-023-42826-x · 2023 | Strong for *Bacillus anthracis* EA1; not necessarily general to all S-layers. |
| TAB domain of SlpA/SlpX — binds — lipoteichoic acid (LTA) / wall teichoic acid (WTA) | protein domain → polymer/cell-wall chemical | label-only: TAB domain; CHEBI:teichoic acid label-only; GO:0043169 cation binding not exact; label-only: LTA/WTA | ITC/NMR identified “two GroP binding sites” and support binding of SlpA TAB to both LTA and WTA via glycerol-phosphate repeats (sagmeister2024themoleculararchitecture pages 6-9, sagmeister2024themoleculararchitecture media ab0cf737) | DOI:10.1073/pnas.2401686121 · https://doi.org/10.1073/pnas.2401686121 · 2024 | Strong for lactobacilli; ontology grounding for TAB/LTA/WTA may remain label-only pending preferred CURIEs. |
| Teichoic acid length exceeding peptidoglycan thickness — enables — S-layer attachment to Gram-positive cell wall | cell-wall polymer/property → process | label-only: teichoic acid polymer length; GO:0071555 cell wall organization | “TA length must exceed the PG layer… to permit S-layer binding” in lactobacilli (sagmeister2024themoleculararchitecture pages 6-9) | DOI:10.1073/pnas.2401686121 · https://doi.org/10.1073/pnas.2401686121 · 2024 | Useful mechanistic constraint; likely taxon-specific geometry, curate as conditional edge with note. |
| SLH domains — bind — secondary cell wall polysaccharide bearing ketal-pyruvylated N-acetylmannosamine | protein domain → cell-wall polysaccharide | pfam/label-only: SLH domain; label-only: secondary cell wall polysaccharide (SCWP); CHEBI label-only: N-acetylmannosamine | Sap/EA1 contain “three S-layer homology (SLH) domains that anchor the protein… by binding the ketal-pyruvylated N-acetylmannosamine unit in the secondary cell wall polysaccharide” (sogues2023structureandfunction pages 1-2) | DOI:10.1038/s41467-023-42826-x · https://doi.org/10.1038/s41467-023-42826-x · 2023 | Strong for *B. anthracis* and related Gram-positives; not for archaeal/lactobacillal attachment systems. |
| AglB oligosaccharyltransferase — glycosylates — archaeal S-layer protein SlaA | enzyme → protein modification | UniProt/label-only: AglB; GO:0006487 protein N-linked glycosylation; label-only: SlaA | “Glycosylation is installed by the oligosaccharyl transferase AglB, which is essential in *S. acidocaldarius*” and SlaA has many N-glycosylation sites (gambelli2024structureofthe pages 12-13) | DOI:10.7554/eLife.84617 · https://doi.org/10.7554/eLife.84617 · 2024 | Strong for *Sulfolobus acidocaldarius*; direct link to S-layer trait is archaeal-specific. |
| S-layer glycosylation — contributes to — lattice stability / permeability regulation | protein modification → process/function | GO:0006487; GO:0045006; GO:0005215 transporter activity not exact; label-only: pore permeability | Cryo-EM shows glycans projecting into pores and authors suggest glycans “may regulate permeability”; thermophiles show more glycosylation, suggesting thermostability role (gambelli2024structureofthe pages 1-2, gambelli2024structureofthe pages 12-13) | DOI:10.7554/eLife.84617 · https://doi.org/10.7554/eLife.84617 · 2024 | Partly inferred/mechanistic hypothesis; mark uncertain until perturbation data directly tie glycosylation to permeability. |
| SlaA — assembles with — SlaB into two-component archaeal S-layer lattice | protein complex/structure | label-only: SlaA; label-only: SlaB; GO:0045006 | The *S. acidocaldarius* S-layer comprises “a flexible, highly glycosylated outer protein (SlaA) and an inner membrane-bound component (SlaB) that together form a porous interwoven lattice” (gambelli2024structureofthe pages 1-2) | DOI:10.7554/eLife.84617 · https://doi.org/10.7554/eLife.84617 · 2024 | Strong, archaeal and taxon-specific. |
| New peptidoglycan turnover sites — localize — new S-layer insertion | process → process | GO:0009252 peptidoglycan biosynthetic process / label-only: cell wall turnover; GO:0045006 | In *C. crescentus*, S-layer biogenesis “follows new peptidoglycan synthesis and localises to regions of high cell wall turnover” (herdman2024cellcycledependent pages 8-9) | DOI:10.1038/s41467-024-47529-5 · https://doi.org/10.1038/s41467-024-47529-5 · 2024 | Strong but species-specific; useful for biogenesis subgraph rather than trait presence per se. |
| LPS integrity/dynamics — is required for — localized S-layer insertion | cell-envelope component → process | label-only: lipopolysaccharide; GO:0045006 | Localized S-layer insertion in *C. crescentus* “is disrupted upon dysregulation of… lipopolysaccharide,” implicating OM/LPS context in assembly (herdman2024cellcycledependent pages 8-9) | DOI:10.1038/s41467-024-47529-5 · https://doi.org/10.1038/s41467-024-47529-5 · 2024 | Strong for *Caulobacter*; likely diderm-specific. |
| SlpA — serves as receptor for — multiple *C. difficile* phages | protein → virus interaction | label-only: SlpA; label-only: bacteriophage receptor activity; NCBITaxon:1496 *Clostridioides difficile* | “Absence of SlpA… led to complete resistance” and complementation restored susceptibility; many siphophages and myophages use SlpA as receptor (royer2023clostridioidesdifficileslayer pages 2-4, royer2023clostridioidesdifficileslayer pages 1-2) | DOI:10.1128/spectrum.03894-22 · https://doi.org/10.1128/spectrum.03894-22 · 2023 | Strong, species-specific; important ecological/host-range edge, not core biogenesis edge. |
| Loss of SlpA — causes — phage adsorption failure / phage resistance | protein absence → phenotype | label-only: SlpA loss-of-function; label-only: phage adsorption; label-only: phage resistance | FM2.5 showed adsorption dropping from high WT levels to near zero for several phages; “The absence of SlpA… led to complete resistance” (royer2023clostridioidesdifficileslayer pages 2-4, royer2023clostridioidesdifficileslayer pages 4-6) | DOI:10.1128/spectrum.03894-22 · https://doi.org/10.1128/spectrum.03894-22 · 2023 | Strong, species-specific genetic evidence. |
| SlpA D2 domain (LMW fragment) — mediates adsorption of — subset of phages (e.g., ϕCD38-2, ϕCD146) | protein domain → virus interaction | label-only: SlpA D2 domain; label-only: phage adsorption | Deletion of D2 “abolished infection by ϕCD38-2 and ϕCD146 but not ϕCD111,” indicating domain-specific receptor contacts (royer2023clostridioidesdifficileslayer pages 8-10, royer2023clostridioidesdifficileslayer pages 10-12) | DOI:10.1128/spectrum.03894-22 · https://doi.org/10.1128/spectrum.03894-22 · 2023 | Strong, narrow and phage-specific; curate with explicit scope note. |
| *Lactobacillus crispatus* S-layer proteins — shield — TLR ligands | protein → host-interaction process | label-only: L. crispatus S-layer proteins; label-only: TLR ligands; GO:0002224 toll-like receptor signaling pathway | Anti-inflammatory action was “regulated by surface layer protein (SLPs)-mediated shielding of TLR ligands” (decout2024lactobacilluscrispatusslayer pages 1-2) | DOI:10.1038/s41467-024-55233-7 · https://doi.org/10.1038/s41467-024-55233-7 · 2024 | Strong, host-interaction edge; not universal S-layer function. |
| *Lactobacillus crispatus* S-layer proteins — interact with — DC-SIGN | protein → receptor binding | label-only: S-layer proteins; label-only: DC-SIGN/CD209 | SLPs “selectively interact with the anti-inflammatory receptor, DC-SIGN” and correlate with lower pro-inflammatory cytokines (decout2024lactobacilluscrispatusslayer pages 1-2) | DOI:10.1038/s41467-024-55233-7 · https://doi.org/10.1038/s41467-024-55233-7 · 2024 | Strong, host-specific immunomodulatory edge. |
| Anammox S-layer protein BROSI_A1236 — functions as — extracellular matrix EPS / adhesive | protein → biofilm matrix role | label-only: BROSI_A1236; GO:0045226 extracellular matrix structural constituent not exact; label-only: EPS | Study shows S-layer protein appears beyond producer cells and “acts as an adhesive” / “public-good EPS” organizing Chloroflexi framework in biofilms (wong2023surfacelayerproteinis pages 1-2) | DOI:10.1038/s41396-023-01388-y · https://doi.org/10.1038/s41396-023-01388-y · 2023 | Strong for this environmental anammox system; unusual/noncanonical S-layer role, curate with taxon/ecosystem note. |
| BROSI_A1236-rich matrix — facilitates assembly of — 3D anammox biofilm lattice | protein/EPS → community structure process | label-only: BROSI_A1236; label-only: biofilm lattice assembly | Spatial distribution suggests the S-layer protein “facilitates the assembly of filamentous Chloroflexi into a three-dimensional biofilm lattice” (wong2023surfacelayerproteinis pages 1-2) | DOI:10.1038/s41396-023-01388-y · https://doi.org/10.1038/s41396-023-01388-y · 2023 | Strong for community-level effect; not a generic S-layer property. |
| Recombinant S-layer protein array — positions membrane receptors as — dense antifouling linker layer in biosensor | engineered protein scaffold → device function | label-only: rSbpA-ZZ; label-only: dual-monolayer probe; label-only: antifouling linker | The sensing construct uses “two-dimensional crystalline S-layer proteins as dense antifouling linkers guiding their orientations” (engineered application) (yuliawati2024potencyofsurface pages 2-4) | DOI:10.1126/sciadv.adf1402 · https://doi.org/10.1126/sciadv.adf1402 · 2023 | Application edge, not native microbial causality; useful for implementation section, likely exclude from core TraitMech graph. |


*Table: This table compiles evidence-backed candidate causal edges for curating the microbial S-layer trait into a TraitMech graph. It emphasizes experimentally supported mechanisms, taxon scope, ontology grounding suggestions, and cautions for edges that may be too taxon-specific or application-specific for direct curation.*

---

## 8. Warnings / items requiring caution before curation
1. **Generality vs taxon-specificity:** Attachment mechanisms differ strongly by lineage (TAB–teichoic acids vs SLH–SCWP vs OM/LPS contexts vs archaeal SlaA/SlaB). Curate these as alternative pathways or conditional edges rather than assuming a single universal anchoring mechanism. (sagmeister2024themoleculararchitecture pages 6-9, sogues2023structureandfunction pages 1-2, herdman2024cellcycledependent pages 8-9, gambelli2024structureofthe pages 1-2)
2. **Inferred roles of glycosylation in permeability:** The claim that glycans regulate effective pore size/permeability is plausible but partly interpretive; perturbation data are explicitly suggested as future work. Mark as **uncertain** unless supported by direct glycosylation mutants in the same system. (gambelli2024structureofthe pages 12-13)
3. **S-layer proteins in EPS:** The anammox example demonstrates an S-layer protein functioning as a transported EPS “public good,” which may not represent a canonical “cell-encasing crystalline coat” phenotype. Treat as a context-specific functional extension rather than redefining the trait. (wong2023surfacelayerproteinis pages 1-2)
4. **Engineered nanotechnology edges:** Biosensor scaffolding uses S-layer proteins as materials; these are real-world implementations but generally should not be curated as native microbial causal edges. (qing2023scalablebiomimeticsensing pages 5-6)

---

## 9. DOI-first bibliography (with dates and URLs)
* Sagmeister T. et al. **“The molecular architecture of Lactobacillus S-layer: Assembly and attachment to teichoic acids.”** *PNAS* (Jun 2024). DOI:10.1073/pnas.2401686121. https://doi.org/10.1073/pnas.2401686121 (sagmeister2024themoleculararchitecture pages 1-2, sagmeister2024themoleculararchitecture pages 6-9)
* Herdman M. et al. **“Cell cycle dependent coordination of surface layer biogenesis in Caulobacter crescentus.”** *Nature Communications* (Apr 2024). DOI:10.1038/s41467-024-47529-5. https://doi.org/10.1038/s41467-024-47529-5 (herdman2024cellcycledependent pages 8-9)
* Gambelli L. et al. **“Structure of the two-component S-layer of the archaeon Sulfolobus acidocaldarius.”** *eLife* (Jan 2024). DOI:10.7554/eLife.84617. https://doi.org/10.7554/elife.84617 (gambelli2024structureofthe pages 1-2, gambelli2024structureofthe pages 12-13)
* Sogues A. et al. **“Structure and function of the EA1 surface layer of Bacillus anthracis.”** *Nature Communications* (Nov 2023). DOI:10.1038/s41467-023-42826-x. https://doi.org/10.1038/s41467-023-42826-x (sogues2023structureandfunction pages 1-2)
* Royer A.L.M. et al. **“Clostridioides difficile S-layer protein A (SlpA) serves as a general phage receptor.”** *Microbiology Spectrum* (Apr 2023). DOI:10.1128/spectrum.03894-22. https://doi.org/10.1128/spectrum.03894-22 (royer2023clostridioidesdifficileslayer pages 4-6, royer2023clostridioidesdifficileslayer pages 8-10)
* Decout A. et al. **“Lactobacillus crispatus S-layer proteins modulate innate immune response and inflammation in the lower female reproductive tract.”** *Nature Communications* (Sep 2024). DOI:10.1038/s41467-024-55233-7. https://doi.org/10.1038/s41467-024-55233-7 (decout2024lactobacilluscrispatusslayer pages 1-2)
* Wong L.L. et al. **“Surface-layer protein is a public-good matrix exopolymer for microbial community organisation in environmental anammox biofilms.”** *ISME Journal* (Mar 2023). DOI:10.1038/s41396-023-01388-y. https://doi.org/10.1038/s41396-023-01388-y (wong2023surfacelayerproteinis pages 1-2)
* Qing R. et al. **“Scalable biomimetic sensing system with membrane receptor dual-monolayer probe and graphene transistor arrays.”** *Science Advances* (Jul 2023). DOI:10.1126/sciadv.adf1402. https://doi.org/10.1126/sciadv.adf1402 (qing2023scalablebiomimeticsensing pages 5-6)
* Paillat M. et al. **“A journey with type IX secretion system effectors: selection, transport, processing and activities.”** *Microbiology* (Apr 2023). DOI:10.1099/mic.0.001320. https://doi.org/10.1099/mic.0.001320 (paillat2023ajourneywith pages 7-8)
* Farci D. et al. **“The SDBC is active in quenching oxidative conditions and bridges the cell envelope layers in Deinococcus radiodurans.”** *Journal of Biological Chemistry* (Published online Dec 2022; issue Jan 2023). DOI:10.1016/j.jbc.2022.102784. https://doi.org/10.1016/j.jbc.2022.102784 (farci2023thesdbcis pages 1-2)


References

1. (gambelli2024structureofthe pages 1-2): Lavinia Gambelli, Mathew McLaren, Rebecca Conners, Kelly Sanders, Matthew C Gaines, Lewis Clark, Vicki AM Gold, Daniel Kattnig, Mateusz Sikora, Cyril Hanus, Michail N Isupov, and Bertram Daum. Structure of the two-component s-layer of the archaeon sulfolobus acidocaldarius. Jan 2024. URL: https://doi.org/10.7554/elife.84617, doi:10.7554/elife.84617. This article has 34 citations and is from a domain leading peer-reviewed journal.

2. (sogues2023structureandfunction pages 1-2): Adrià Sogues, Antonella Fioravanti, Wim Jonckheere, Els Pardon, Jan Steyaert, and Han Remaut. Structure and function of the ea1 surface layer of bacillus anthracis. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42826-x, doi:10.1038/s41467-023-42826-x. This article has 16 citations and is from a highest quality peer-reviewed journal.

3. (sagmeister2024themoleculararchitecture pages 1-2): Theo Sagmeister, Nina Gubensäk, Christoph Buhlheller, Christoph Grininger, Markus Eder, Anđela Ðordić, Claudia Millán, Ana Medina, Pedro Alejandro Sánchez Murcia, Francesca Berni, Ulla Hynönen, Djenana Vejzović, Elisabeth Damisch, Natalia Kulminskaya, Lukas Petrowitsch, Monika Oberer, Airi Palva, Nermina Malanović, Jeroen Codée, Walter Keller, Isabel Usón, and Tea Pavkov-Keller. The molecular architecture of lactobacillus s-layer: assembly and attachment to teichoic acids. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2401686121, doi:10.1073/pnas.2401686121. This article has 37 citations and is from a highest quality peer-reviewed journal.

4. (wong2023surfacelayerproteinis pages 1-2): Lan Li Wong, Yang Lu, James Chin Shing Ho, Sudarsan Mugunthan, Yingyu Law, Patricia Conway, Staffan Kjelleberg, and Thomas Seviour. Surface-layer protein is a public-good matrix exopolymer for microbial community organisation in environmental anammox biofilms. The ISME Journal, 17:803-812, Mar 2023. URL: https://doi.org/10.1038/s41396-023-01388-y, doi:10.1038/s41396-023-01388-y. This article has 79 citations.

5. (sagmeister2024themoleculararchitecture pages 6-9): Theo Sagmeister, Nina Gubensäk, Christoph Buhlheller, Christoph Grininger, Markus Eder, Anđela Ðordić, Claudia Millán, Ana Medina, Pedro Alejandro Sánchez Murcia, Francesca Berni, Ulla Hynönen, Djenana Vejzović, Elisabeth Damisch, Natalia Kulminskaya, Lukas Petrowitsch, Monika Oberer, Airi Palva, Nermina Malanović, Jeroen Codée, Walter Keller, Isabel Usón, and Tea Pavkov-Keller. The molecular architecture of lactobacillus s-layer: assembly and attachment to teichoic acids. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2401686121, doi:10.1073/pnas.2401686121. This article has 37 citations and is from a highest quality peer-reviewed journal.

6. (herdman2024cellcycledependent pages 8-9): Matthew Herdman, Buse Isbilir, Andriko von Kügelgen, Ulrike Schulze, Alan Wainman, and Tanmay A. M. Bharat. Cell cycle dependent coordination of surface layer biogenesis in caulobacter crescentus. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47529-5, doi:10.1038/s41467-024-47529-5. This article has 14 citations and is from a highest quality peer-reviewed journal.

7. (gambelli2024structureofthe pages 12-13): Lavinia Gambelli, Mathew McLaren, Rebecca Conners, Kelly Sanders, Matthew C Gaines, Lewis Clark, Vicki AM Gold, Daniel Kattnig, Mateusz Sikora, Cyril Hanus, Michail N Isupov, and Bertram Daum. Structure of the two-component s-layer of the archaeon sulfolobus acidocaldarius. Jan 2024. URL: https://doi.org/10.7554/elife.84617, doi:10.7554/elife.84617. This article has 34 citations and is from a domain leading peer-reviewed journal.

8. (royer2023clostridioidesdifficileslayer pages 8-10): Alexia L. M. Royer, Andrew A. Umansky, Marie-Maude Allen, Julian R. Garneau, Maicol Ospina-Bedoya, Joseph A. Kirk, Gregory Govoni, Robert P. Fagan, Olga Soutourina, and Louis-Charles Fortier. Clostridioides difficile s-layer protein a (slpa) serves as a general phage receptor. Apr 2023. URL: https://doi.org/10.1128/spectrum.03894-22, doi:10.1128/spectrum.03894-22. This article has 21 citations and is from a domain leading peer-reviewed journal.

9. (royer2023clostridioidesdifficileslayer pages 1-2): Alexia L. M. Royer, Andrew A. Umansky, Marie-Maude Allen, Julian R. Garneau, Maicol Ospina-Bedoya, Joseph A. Kirk, Gregory Govoni, Robert P. Fagan, Olga Soutourina, and Louis-Charles Fortier. Clostridioides difficile s-layer protein a (slpa) serves as a general phage receptor. Apr 2023. URL: https://doi.org/10.1128/spectrum.03894-22, doi:10.1128/spectrum.03894-22. This article has 21 citations and is from a domain leading peer-reviewed journal.

10. (paillat2023ajourneywith pages 7-8): Maëlle Paillat, Ignacio Lunar Silva, Eric Cascales, and Thierry Doan. A journey with type ix secretion system effectors: selection, transport, processing and activities. Apr 2023. URL: https://doi.org/10.1099/mic.0.001320, doi:10.1099/mic.0.001320. This article has 45 citations and is from a peer-reviewed journal.

11. (decout2024lactobacilluscrispatusslayer pages 1-2): Alexiane Decout, Ioannis Krasias, Lauren Roberts, Belen Gimeno Molina, Chloe Charenton, Daniel Brown Romero, Qiong Yu Tee, Julian R Marchesi, Sherrianne Ng, Lynne Sykes, Phillip R Bennett, and David Alan MacIntyre. Lactobacillus crispatus s-layer proteins modulate innate immune response and inflammation in the lower female reproductive tract. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-55233-7, doi:10.1038/s41467-024-55233-7. This article has 56 citations and is from a highest quality peer-reviewed journal.

12. (royer2023clostridioidesdifficileslayer pages 4-6): Alexia L. M. Royer, Andrew A. Umansky, Marie-Maude Allen, Julian R. Garneau, Maicol Ospina-Bedoya, Joseph A. Kirk, Gregory Govoni, Robert P. Fagan, Olga Soutourina, and Louis-Charles Fortier. Clostridioides difficile s-layer protein a (slpa) serves as a general phage receptor. Apr 2023. URL: https://doi.org/10.1128/spectrum.03894-22, doi:10.1128/spectrum.03894-22. This article has 21 citations and is from a domain leading peer-reviewed journal.

13. (qing2023scalablebiomimeticsensing pages 5-6): Rui Qing, Mantian Xue, Jiayuan Zhao, Lidong Wu, Andreas Breitwieser, Eva Smorodina, Thomas Schubert, Giovanni Azzellino, David Jin, Jing Kong, Tomás Palacios, Uwe B. Sleytr, and Shuguang Zhang. Scalable biomimetic sensing system with membrane receptor dual-monolayer probe and graphene transistor arrays. Science Advances, Jul 2023. URL: https://doi.org/10.1126/sciadv.adf1402, doi:10.1126/sciadv.adf1402. This article has 40 citations and is from a highest quality peer-reviewed journal.

14. (farci2023thesdbcis pages 1-2): Domenica Farci, André T. Graça, Luca Iesu, Daniele de Sanctis, and Dario Piano. The sdbc is active in quenching oxidative conditions and bridges the cell envelope layers in deinococcus radiodurans. Journal of Biological Chemistry, 299:102784, Jan 2023. URL: https://doi.org/10.1016/j.jbc.2022.102784, doi:10.1016/j.jbc.2022.102784. This article has 12 citations and is from a domain leading peer-reviewed journal.

15. (sagmeister2024themoleculararchitecture media ab0cf737): Theo Sagmeister, Nina Gubensäk, Christoph Buhlheller, Christoph Grininger, Markus Eder, Anđela Ðordić, Claudia Millán, Ana Medina, Pedro Alejandro Sánchez Murcia, Francesca Berni, Ulla Hynönen, Djenana Vejzović, Elisabeth Damisch, Natalia Kulminskaya, Lukas Petrowitsch, Monika Oberer, Airi Palva, Nermina Malanović, Jeroen Codée, Walter Keller, Isabel Usón, and Tea Pavkov-Keller. The molecular architecture of lactobacillus s-layer: assembly and attachment to teichoic acids. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2401686121, doi:10.1073/pnas.2401686121. This article has 37 citations and is from a highest quality peer-reviewed journal.

16. (royer2023clostridioidesdifficileslayer pages 2-4): Alexia L. M. Royer, Andrew A. Umansky, Marie-Maude Allen, Julian R. Garneau, Maicol Ospina-Bedoya, Joseph A. Kirk, Gregory Govoni, Robert P. Fagan, Olga Soutourina, and Louis-Charles Fortier. Clostridioides difficile s-layer protein a (slpa) serves as a general phage receptor. Apr 2023. URL: https://doi.org/10.1128/spectrum.03894-22, doi:10.1128/spectrum.03894-22. This article has 21 citations and is from a domain leading peer-reviewed journal.

17. (royer2023clostridioidesdifficileslayer pages 10-12): Alexia L. M. Royer, Andrew A. Umansky, Marie-Maude Allen, Julian R. Garneau, Maicol Ospina-Bedoya, Joseph A. Kirk, Gregory Govoni, Robert P. Fagan, Olga Soutourina, and Louis-Charles Fortier. Clostridioides difficile s-layer protein a (slpa) serves as a general phage receptor. Apr 2023. URL: https://doi.org/10.1128/spectrum.03894-22, doi:10.1128/spectrum.03894-22. This article has 21 citations and is from a domain leading peer-reviewed journal.

18. (yuliawati2024potencyofsurface pages 2-4): Yuliawati Yuliawati, Diah Anggraini Wulandari, Ni Wayan Sri Agustini, Asrul Muhamad Fuad, Trisanti Anindyawati, Mega Ferdina Warsito, and Riyona Desvy Pratiwi. Potency of surface layer protein from lactobacillus sp. as drug nanocarriers. Journal of Applied Pharmaceutical Science, Jan 2024. URL: https://doi.org/10.7324/japs.2024.199203, doi:10.7324/japs.2024.199203. This article has 1 citations.