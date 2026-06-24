---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:21:33.272004'
end_time: '2026-06-18T06:38:50.122744'
duration_seconds: 1036.85
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: branched shaped
  trait_identifier: METPO:1000687
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: branched_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism forms lateral branches from filamentous
    or hyphal cells.
  parent_traits: METPO:1000666
  synonyms: branced, branched
  evidence_summary: 'DOI:10.1016/j.mib.2012.10.012: Streptomyces grow by tip extension
    and through the initiation of new branches (Supports branched morphology as a
    Streptomyces hyphal growth phenotype.)'
  causal_graph_summary: 'branched_shaped_streptomyces_branching: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** branched shaped
- **METPO identifier:** METPO:1000687
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms lateral branches from filamentous or hyphal cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** branced, branched
- **Existing evidence:** DOI:10.1016/j.mib.2012.10.012: Streptomyces grow by tip extension and through the initiation of new branches (Supports branched morphology as a Streptomyces hyphal growth phenotype.)
- **Existing causal graph summary:** branched_shaped_streptomyces_branching: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **branched shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/branched_shaped.yaml`.

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
- **Trait label:** branched shaped
- **METPO identifier:** METPO:1000687
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms lateral branches from filamentous or hyphal cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** branced, branched
- **Existing evidence:** DOI:10.1016/j.mib.2012.10.012: Streptomyces grow by tip extension and through the initiation of new branches (Supports branched morphology as a Streptomyces hyphal growth phenotype.)
- **Existing causal graph summary:** branched_shaped_streptomyces_branching: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **branched shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/branched_shaped.yaml`.

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


## Research report: Microbial trait **branched shaped** (METPO:1000687) as a candidate TraitMech causal graph

### Scope summary (TraitMech-ready)
**Trait definition (METPO:1000687)**: “Branched shaped” refers to a **cell shape** where an organism forms **lateral branches from filamentous or hyphal cells**. Mechanistically, this implies repeated establishment of **new polarized growth sites** along an existing filament/hypha (lateral branching) and/or generation of additional apical growth axes (apical branching) during tip extension. This trait is most directly applicable to **filamentous Actinomycetota** (e.g., *Streptomyces*) and **filamentous fungi**, where branching frequency can be quantified by metrics such as **tip-to-proximal-branch distance** (bacteria) or **lateral/apical branch counts per hyphal length/time** (fungi). (bhowmick2023osmoticstressresponses pages 1-2, zhong2025thestomatinlikeprotein pages 4-5)

**Boundary cases / distinctions for curation**:
- Exclude **budding** (yeast-like single-cell proliferation), **pseudohyphae** (chains of elongated budding cells), and **biofilm/pellet macromorphology** unless branching is explicitly at the **single-filament/hypha level**.
- Distinguish **true lateral branches** (new growth sites along a pre-existing filament) from **septation/compartmentalization** (division-related cross-walls) and from **extrusion of wall-deficient cells** under stress (which may co-occur with branching). (bhowmick2024cellshapeand pages 1-2, zhong2025thestomatinlikeprotein pages 1-2)

---

## 1) Key concepts & current understanding (mechanistic framing)

### A. Filamentous bacteria (*Streptomyces* and related actinobacteria)
**Core concept: branch initiation is a polarity-replication event**. *Streptomyces* hyphae grow by **apical wall synthesis** at tips and initiate **lateral branches** by creating new polarity centers behind the tip.

**Polarisome / TIPOC**: Branching and tip extension are coordinated by a DivIVA-centered multiprotein polarity system (DivIVA with Scy and FilP) that organizes enzymes for cell-wall synthesis/remodeling at growth zones. (bhowmick2024cellshapeand pages 1-2, bhowmick2023osmoticstressresponses pages 1-2)

**Polarisome splitting model**: A recent synthesis of the field emphasizes that **splitting of tip polarisomes** yields “daughter polarisomes” that later drive **lateral branch emergence** once they reach a size threshold. This provides a concrete mechanistic edge from polarity-organelle dynamics to branching. (bhowmick2023osmoticstressresponses pages 1-2)

**Membrane organization and “microdomains” at tips**: Beyond protein scaffolds, **membrane physical properties** (e.g., local fluidity regions) can spatially confine wall synthesis at tips and thereby influence whether and where new branches initiate—particularly under stress. (zhong2025thestomatinlikeprotein pages 1-2, claessen2024thestomatinlikeprotein pages 7-9)

### B. Filamentous fungi
**Core concept: branching is controlled by conserved polarity, trafficking, cytoskeleton, and cell-cycle coordination**.

**Polarity GTPases and secretory organization**: Tip-localized polarity proteins (e.g., Cdc42 system) and cytoskeletal transport organize vesicle trafficking to the apex. Vesicles form the **Spitzenkörper**, which is described as actively regulating directional growth by steering secretory vesicles that deliver wall synthases/hydrolases for extension. (schyck2024harnessingfungisignaling pages 2-3)

**Exocyst complex**: The exocyst (GO:0000145) is an octameric tethering complex that positions vesicle fusion at sites of polarized growth. Reviews highlight regulatory inputs from Rho-family GTPases (including Cdc42) and phosphorylation of exocyst subunits that modulate polarized growth—mechanistically upstream of branching patterns. (zuriegat2024emergingrolesof pages 6-7, zuriegat2024emergingrolesof pages 23-24)

**Cell cycle linkage**: In *Aspergillus fumigatus*, branching is tightly coordinated with nuclear division; **blocking the cell cycle abolishes branching** (strong causal constraint for mechanistic curation). (cuesta2024discoveryandcharacterization pages 148-152)

---

## 2) Recent developments & latest research (prioritizing 2023–2024)

### A. 2024: Cell-wall glycopolymer ligation and morphology in *Streptomyces*
A 2024 *mBio* study identifies **CglA**, an LCP/LytR_C family **cell-wall glycopolymer ligase**, as necessary for cell-shape maintenance. Reduced glycopolymers in a *cglA* mutant cause enlarged vegetative hyphae and mispositioned division septa via FtsZ-ring defects; the work also reports a physiological link between wall glycopolymer decoration and **c-di-AMP** signaling under high salt. While this is not a direct “branch count” phenotype, it provides a tractable cell-envelope module that can be upstream of stable branched morphology (branch maintenance and mechanical integrity). (bhowmick2024cellshapeand pages 1-2)

### B. 2023: Osmotic stress, cell-wall stress, and a phosphorylation switch controlling branching
A 2023 review in *microLife* integrates osmotic-stress responses with Streptomyces developmental cell biology and highlights a **post-translational switch** on DivIVA: AfsK phosphorylates DivIVA in response to **cell-wall stress** (e.g., bacitracin, vancomycin), while SppA reverses it. High/constitutive AfsK activity and elevated DivIVA phosphorylation are linked to disassembly of the apical polarisome, production of multiple new polarity centers, and **hyperbranching**. This creates a curated stress→signaling→polarity→branching chain suitable for TraitMech edges (with “uncertain” tags where review-based). (bhowmick2023osmoticstressresponses pages 1-2)

### C. 2024: Exocyst as a central fungal node connecting signaling, cytoskeleton, and secretion
A 2024 *Journal of Fungi* review synthesizes recent understanding of the fungal **exocyst** and emphasizes (i) targeting by Rho-family GTPases including Cdc42, (ii) coordination with septins (diffusion barriers and exocyst interactions), and (iii) phosphorylation-based regulation of subunits that impacts hyphal extension. These mechanistic relationships provide candidate edges for a fungal branching subgraph where direct branching phenotypes may need additional primary studies for final curation. (zuriegat2024emergingrolesof pages 6-7, zuriegat2024emergingrolesof pages 23-24)

### D. 2024: Branching phenotypes from regulatory genes and ROS/cytoskeleton modules in fungi
Evidence in 2024 sources supports multiple causal levers for branching:
- **grn (granulin) deletion → increased branching** (lateral and apical) in *A. fumigatus*, with associated morphological changes (smaller diameter, increased septation). (cuesta2024discoveryandcharacterization pages 148-152)
- **Septin AspB marks future branch sites** prior to mitosis, linking septin localization to branch-site specification. (cuesta2024discoveryandcharacterization pages 148-152)
- **NADPH oxidases (Nox/ROS)** regulate hyphal formation, tip growth, and branching-related processes in *Pleurotus ostreatus* and cited fungi, connecting ROS production and cell-wall composition to morphology. (li2024contrastingeffectsof pages 9-10)

---

## 3) Current applications and real-world implementations

### A. Industrial/bioprocess relevance (filamentous bacteria)
*Streptomyces* branching is widely understood as a key determinant of **mycelial architecture**, which in turn affects **mass transfer, broth rheology, shear sensitivity, and productivity** in submerged culture. While the retrieved evidence here is largely mechanistic, it explicitly notes that manipulating branching rate can alter physical robustness and production outcomes in *Streptomyces* (review-level). This is consistent with common industrial practice of controlling morphology via medium composition and stress, and provides justification for including environmental/experimental nodes (osmolarity, salt, wall stress antibiotics) in TraitMech graphs. (lubbersUnknownyearaspersn.& pages 8-8)

### B. Fungal biomaterials and engineered living composites
A 2024 review on fungal signaling highlights that hyphal growth directionality (and by implication branching patterns) is controllable by polarity proteins, cytoskeleton, vesicle trafficking, and Ca2+ signaling, with emerging applications in **living composites** and engineered materials using fungal mycelia. This motivates TraitMech edges that connect environmental cues/ion signaling to branching-related polarized growth systems. (schyck2024harnessingfungisignaling pages 2-3)

---

## 4) Expert opinions and authoritative analyses

- **Branching as polarisome dynamics**: Authoritative synthesis emphasizes that branch emergence can be conceptualized as a consequence of **polarisome splitting/replication** and downstream establishment of new growth sites (a mechanistic framing that is both explanatory and curatable). (bhowmick2023osmoticstressresponses pages 1-2)
- **Exocyst-centered model of polarized growth**: Review consensus positions the exocyst as a central hub integrating small GTPases, actin-based trafficking, septin barriers, and phosphorylation control to achieve polarized growth—an upstream determinant of branching. (zuriegat2024emergingrolesof pages 6-7, zuriegat2024emergingrolesof pages 23-24)

---

## 5) Relevant recent statistics and quantitative data

### Quantitative branching metric (actinobacteria): tip-to-proximal-branch distance
A high-quality 2025 Nature Communications study (included here because it provides unusually explicit quantitative branching statistics and assay definitions) quantified branching by measuring **distance from hyphal tip to proximal branch point** after 16 h growth, with sample sizes n=188 (WT), n=282 (ΔstlP), n=192 (complement). In ΔstlP, **>60%** of hyphae branched within the first **5 µm** from the tip versus ~**15%** in parent/complemented strains, and no mutant hyphae branched beyond **35 µm**. This provides curation-grade quantitative thresholds and supports edges linking membrane microdomains and hyperosmotic stress to branching frequency. (zhong2025thestomatinlikeprotein pages 4-5, zhong2025thestomatinlikeprotein media f2a749fa)

### Additional quantitative growth/morphology metrics under stress
The same work reports colony diameter reductions on hyperosmotic medium (1.4 ± 0.3 mm mutant vs 3.8 ± 0.6 mm wild-type) and vesicle release from tips (2.5×10^5 vesicles/mL in mutant vs none in parent), suggesting envelope failure accompanies hyperbranching in the mutant. (zhong2025thestomatinlikeprotein pages 2-4)

---

# Curation-focused outputs

## Candidate nodes grouped by type (with suggested grounding)

### Trait node
- **Branched shaped** (METPO:1000687)

### Organisms / taxa (NCBITaxon)
- *Streptomyces coelicolor* (NCBITaxon:1902) (zhong2025thestomatinlikeprotein pages 1-2)
- *Streptomyces venezuelae* (NCBITaxon:54571) (bhowmick2024cellshapeand pages 1-2)
- *Aspergillus fumigatus* (NCBITaxon:746128) (cuesta2024discoveryandcharacterization pages 148-152)
- *Pleurotus ostreatus* (NCBITaxon:5326) (li2024contrastingeffectsof pages 9-10)
- *Fusarium graminearum* (NCBITaxon:5518) (yuan2024fgpfnparticipatesin pages 9-11)
- *Neurospora crassa* (NCBITaxon:5141) (li2024contrastingeffectsof pages 9-10)
- *Kitasatospora viridifaciens* (NCBITaxon: unresolved in retrieved evidence; label-only) (claessen2024thestomatinlikeprotein pages 7-9)

### Cellular processes / functions (GO suggestions)
- Polarized growth / cell polarity establishment (label-only GO term not resolved here)
- **Exocyst complex** (GO:0000145) (zuriegat2024emergingrolesof pages 6-7)
- **Exocytosis** (GO:0006887) (zuriegat2024emergingrolesof pages 23-24)
- **Protein transport** (GO:0015031) (zuriegat2024emergingrolesof pages 23-24)
- **Actin cytoskeleton organization** (e.g., GO:0030036) / regulation of actin polymerization (e.g., GO:0030833) (cuesta2024discoveryandcharacterization pages 29-34)
- **Microtubule-based movement** (GO:0007018) (cuesta2024discoveryandcharacterization pages 148-152)
- **Cell cycle** (GO:0007049) (cuesta2024discoveryandcharacterization pages 148-152)

### Genes/proteins/complexes (label-level nodes; UniProt accessions need follow-up)
**Actinobacteria (Streptomyces):**
- DivIVA (polarity determinant) (bhowmick2023osmoticstressresponses pages 1-2)
- Scy, FilP (polarisome components) (bhowmick2024cellshapeand pages 1-2)
- AfsK (Ser/Thr kinase) (bhowmick2023osmoticstressresponses pages 1-2)
- SppA (phosphatase) (bhowmick2023osmoticstressresponses pages 1-2)
- StlP (stomatin-like; membrane microdomains) (zhong2025thestomatinlikeprotein pages 1-2)
- CglA (LCP/LytR_C glycopolymer ligase) (bhowmick2024cellshapeand pages 1-2)
- DisA (c-di-AMP cyclase; signaling) (bhowmick2024cellshapeand pages 1-2)

**Fungi:**
- Cdc42 (Rho-family GTPase) (zuriegat2024emergingrolesof pages 6-7)
- Exocyst subunits (Sec3, Exo70, Sec6, Exo84, Sec15) (zuriegat2024emergingrolesof pages 6-7, zuriegat2024emergingrolesof pages 23-24)
- Septin AspB (branch-site marker) (cuesta2024discoveryandcharacterization pages 148-152)
- Dynein (motor; nuclear migration) (cuesta2024discoveryandcharacterization pages 148-152)
- NADPH oxidases (NoxA/NoxB; taxon-specific orthologs) (li2024contrastingeffectsof pages 9-10)
- Catalases (e.g., catalase-3 in *Neurospora*) (li2024contrastingeffectsof pages 9-10)
- grn (granulin; negative regulator of branching) (cuesta2024discoveryandcharacterization pages 148-152)

### Chemicals / environmental factors (CHEBI/condition nodes)
- **Hydrogen peroxide** (CHEBI:16240) / ROS (li2024contrastingeffectsof pages 9-10)
- **Calcium ion** (CHEBI:29108) and Ca2+ signaling (schyck2024harnessingfungisignaling pages 2-3)
- **Potassium ion** (CHEBI:29103); compatible solutes: proline (CHEBI:17203), ectoine (CHEBI:49574), trehalose (CHEBI:17792) as osmoadaptation factors (bhowmick2023osmoticstressresponses pages 1-2)
- **Hyperosmotic stress / high salt** (ENVO term unresolved; use label-level node) (zhong2025thestomatinlikeprotein pages 1-2, bhowmick2024cellshapeand pages 1-2)
- **Cell-wall stress antibiotics**: bacitracin, vancomycin (chemical IDs not resolved here; label-level nodes acceptable) (bhowmick2023osmoticstressresponses pages 1-2)

---

## Candidate causal edges (evidence-backed triples)
| Edge (S–P–O) | Mechanistic context/assay | Taxon/model system | Evidence snippet | Citation ID(s) |
|---|---|---|---|---|
| StlP membrane microdomain formation — enables — proper polar growth and normal branch spacing | Hyperosmotic-stress growth; tip membrane fluidity and branching phenotypes measured in *stlP* mutants/complemented strains | *Streptomyces coelicolor*; *Kitasatospora viridifaciens* | Loss of StlP “leads to branching of filaments”; constitutive *stlP* expression in *K. viridifaciens* “notably reduces lateral branching” and increases tip-to-branch distance | (zhong2025thestomatinlikeprotein pages 1-2, claessen2024thestomatinlikeprotein pages 7-9, zhong2025thestomatinlikeprotein media f2a749fa) |
| Hyperosmotic stress — increases dependence on — StlP-mediated membrane microdomains for branch control | LPMA/high-osmolarity growth conditions; comparison of WT vs *stlP* mutant branch frequency | *Streptomyces coelicolor* | Under hyperosmotic stress, *stlP* deletion causes hyperbranching; >60% of mutant hyphae branch within 5 μm of the tip | (zhong2025thestomatinlikeprotein pages 1-2, zhong2025thestomatinlikeprotein media f2a749fa) |
| DivIVA polarisome splitting — causes — emergence of new lateral branches | Polarisome dynamics during vegetative tip growth | *Streptomyces* spp. | “Splitting of polarisomes at growing tips generates daughter polarisomes that coordinate emergence of new lateral branches upon reaching a critical size” | (bhowmick2023osmoticstressresponses pages 1-2) |
| DivIVA/Scy/FilP polarisome — localizes — peptidoglycan synthases and hydrolases to the apex | Review of apical growth machinery and branch initiation | *Streptomyces* spp. | The polarisome composed of DivIVA with Scy and FilP localizes cell-wall enzymes to one pole, linking polarity establishment to branching | (bhowmick2024cellshapeand pages 1-2, bhowmick2023osmoticstressresponses pages 1-2) |
| AfsK-mediated DivIVA phosphorylation — stimulates — multiple new polarisomes and hyperbranching | Cell-wall stress response; kinase/phosphatase control of DivIVA | *Streptomyces* spp. | “Constitutive AfsK activity/high DivIVA phosphorylation disassembles the apical polarisome and stimulates multiple new polarisomes, producing a hyperbranching phenotype” | (bhowmick2023osmoticstressresponses pages 1-2) |
| SppA dephosphorylation of DivIVA — opposes — AfsK-driven hyperbranching | Post-translational regulation of DivIVA under cell-wall stress | *Streptomyces* spp. | AfsK phosphorylates DivIVA in response to bacitracin/vancomycin stress, while SppA dephosphorylates DivIVA, defining a reversible branching-control circuit | (bhowmick2023osmoticstressresponses pages 1-2) |
| Cell-wall stress (bacitracin/vancomycin) — activates — AfsK-dependent DivIVA phosphorylation | Antibiotic-induced cell-wall stress signaling | *Streptomyces* spp. | AfsK “phosphorylates [DivIVA] in response to cell-wall stress (e.g., bacitracin, vancomycin)” | (bhowmick2023osmoticstressresponses pages 1-2) |
| CglA glycopolymer ligase activity — maintains — normal hyphal cell shape | *cglA* mutant morphology and cell-wall glycopolymer defect analysis | *Streptomyces venezuelae* | Reduced glycopolymers in the *cglA* mutant cause “enlarged vegetative hyphae” and loss of normal cell shape | (bhowmick2024cellshapeand pages 1-2) |
| Loss of CglA — causes — aberrant septation and misshapen compartments/spores | Cell-wall biogenesis defect; septa positioning assay | *Streptomyces venezuelae* | *cglA* mutants show “failures in FtsZ-rings formation and positioning,” “misplaced septa,” and “misshaped spores” | (bhowmick2024cellshapeand pages 1-2) |
| c-di-AMP signaling — is physiologically linked to — cell-wall glycopolymer decoration | Genetic interaction between *disA* and *cglA*; salt-growth phenotypes | *Streptomyces venezuelae* | The study reports a “physiological link” between c-di-AMP signaling and cell-wall glycopolymer decoration; deleting *cglA* restores growth of a *disA* mutant at high salt | (bhowmick2024cellshapeand pages 1-2) |
| DisA/c-di-AMP system — supports — osmotic-stress adaptation affecting morphology | Review of osmotic stress and differentiation | *Streptomyces* spp. | c-di-AMP is linked to “cell differentiation and osmotic stress responses” in *Streptomyces* models | (bhowmick2023osmoticstressresponses pages 1-2) |
| Cdc42/Rho GTPase signaling — targets — exocyst to sites of polarized growth | Exocyst review; polarity and vesicle-tethering mechanisms | Filamentous fungi | Rho-family GTPases including Cdc42 interact with Sec3/Exo70 to target the exocyst to active growth sites, supporting polarized growth underlying branching | (zuriegat2024emergingrolesof pages 6-7, zuriegat2024emergingrolesof pages 9-10) |
| Exocyst-mediated vesicle tethering/fusion — enables — polarized hyphal growth | Exocyst assembly, phosphoregulation, membrane trafficking | Filamentous fungi | Exocyst dynamics and phosphorylation “ensure accurate vesicle tethering/fusion for polarized growth”; Cdc42 acts at a late exocytosis step during polarized growth | (zuriegat2024emergingrolesof pages 23-24, zuriegat2024emergingrolesof pages 6-7, zuriegat2024emergingrolesof pages 9-10) |
| Spitzenkörper-guided vesicle traffic — drives — directional hyphal growth | Fungal polarity/cytoskeleton review | Filamentous fungi | The Spitzenkörper “actively regulates directional hyphal growth by guiding the path of secretory vesicles” that deliver wall-building enzymes | (schyck2024harnessingfungisignaling pages 2-3) |
| NADPH oxidase/ROS signaling — regulates — hyphal tip growth and branching | Nox mutant/overexpression phenotypes | *Pleurotus ostreatus*; cited comparisons to other fungi | PoNoxA positively regulates tip growth, and Nox proteins are described as responsible for hyphal tip growth and branching; related fungi require NoxA/B for ROS generation and hyphal branching | (li2024contrastingeffectsof pages 9-10) |
| Catalase-mediated ROS detoxification — modulates — hyphal morphology and aerial growth | ROS metabolism perturbation | Fungi including *Neurospora crassa* | Catalase-3 inactivation yields increased hyphal adhesion, aerial hyphae, and conidia, supporting ROS balance as a morphology regulator | (li2024contrastingeffectsof pages 9-10) |
| grn deletion — increases — lateral and apical branching | Gene deletion phenotype during germination/hyphal growth | *Aspergillus fumigatus* | Deletion of fungal *grn* causes a “marked increase in both lateral and apical branching,” with reduced hyphal diameter and increased septation | (cuesta2024discoveryandcharacterization pages 148-152) |
| Septin AspB localization — marks — future branching sites | Microscopy-based temporal localization prior to mitosis | *Aspergillus fumigatus* | “AspB localizes to future branching sites prior to mitosis” | (cuesta2024discoveryandcharacterization pages 148-152) |
| Cell-cycle progression/nuclear division — is required for — branch emergence | Branching observed under cell-cycle perturbation | *Aspergillus fumigatus* | “Blocking the cell cycle abolishes branching,” linking branch emergence to nuclear division timing | (cuesta2024discoveryandcharacterization pages 148-152) |
| Dynein- and microtubule-dependent nuclear movement — supports — branching | Cytoskeletal transport linked to branch emergence | *Aspergillus fumigatus* | Nuclear movement depends on dynein and microtubules, and this movement is linked to branching control | (cuesta2024discoveryandcharacterization pages 148-152) |
| Actin-based vesicle transport — supplies — materials for tip growth and branch maintenance | Polarity/cytoskeleton review; myosin-mediated secretion | Filamentous fungi | Actin filaments drive myosin-mediated vesicle transport to the tip, where vesicles aggregate into the Spitzenkörper to support elongation and branching-related polarity | (cuesta2024discoveryandcharacterization pages 29-34, schyck2024harnessingfungisignaling pages 2-3) |
| RacA disruption/mislocalized ROS — causes — multiple polarity axes | Polarity mutant phenotype | *Aspergillus fumigatus* | RacA deletion produced “multiple polarity axes,” attributed to ROS mislocalization, implicating ROS in branch/polarity control | (cuesta2024discoveryandcharacterization pages 29-34) |


*Table: This table compiles curation-ready subject–predicate–object edges for the microbial trait 'branched shaped' (METPO:1000687), emphasizing experimentally supported regulators of branching in Streptomyces and filamentous fungi. It is useful as a starting artifact for building a TraitMech causal graph with evidence-linked nodes and edges.*

---

## Warnings / curation caveats (do not yet curate as “high-confidence” without follow-up)
1. **Review-derived edges** (especially fungal exocyst/Cdc42 → branching) often support polarized growth but may not provide a direct branching phenotype; mark as **inferred/indirect** unless complemented by primary mutant branching assays. (zuriegat2024emergingrolesof pages 6-7, zuriegat2024emergingrolesof pages 23-24)
2. **Preprint evidence**: some branching-modulating factors (e.g., certain Streptomyces chemical/ROS cross-talk studies retrieved as preprints) should be tagged **uncertain** until peer-reviewed versions are used. (zhong2025thestomatinlikeprotein pages 1-2)
3. **UniProt/EC identifiers** for gene products are not extractable from current snippets; curation should map organism-specific proteins to stable accessions during YAML population.
4. **Trait granularity**: Some cell-envelope genes (e.g., *cglA*) cause hyphal widening/shape defects and viability effects; these may influence the persistence of branched morphology rather than **branch initiation rate**. Consider separate nodes for “branch initiation frequency” vs “branch maintenance/mechanical integrity” if TraitMech schema allows. (bhowmick2024cellshapeand pages 1-2)

---

# DOI-first bibliography (with URLs and publication dates)

1. Bhowmick S, Viveros RP, Latoscha A, et al. **Cell shape and division septa positioning in filamentous Streptomyces require a functional cell wall glycopolymer ligase CglA.** *mBio*. **2024-10**. DOI: **10.1128/mbio.01492-24**. https://doi.org/10.1128/mbio.01492-24 (bhowmick2024cellshapeand pages 1-2)

2. Bhowmick S, Shenouda ML, Tschowri N. **Osmotic stress responses and the biology of the second messenger c-di-AMP in Streptomyces.** *microLife*. **2023-04**. DOI: **10.1093/femsml/uqad020**. https://doi.org/10.1093/femsml/uqad020 (bhowmick2023osmoticstressresponses pages 1-2)

3. Zuriegat Q, Abubakar YS, Wang Z, Chen M, Zhang J. **Emerging Roles of Exocyst Complex in Fungi: A Review.** *Journal of Fungi*. **2024-08**. DOI: **10.3390/jof10090614**. https://doi.org/10.3390/jof10090614 (zuriegat2024emergingrolesof pages 6-7, zuriegat2024emergingrolesof pages 23-24)

4. Li H, Zhu J, Li Z, et al. **Contrasting effects of NADPH oxidases on the fungal hyphae growth and immune responses in Pleurotus ostreatus.** *Frontiers in Microbiology*. **2024-06**. DOI: **10.3389/fmicb.2024.1387643**. https://doi.org/10.3389/fmicb.2024.1387643 (li2024contrastingeffectsof pages 9-10)

5. Schyck S, Marchese P, Amani M, et al. **Harnessing Fungi Signaling in Living Composites.** *Global Challenges*. **2024-07**. DOI: **10.1002/gch2.202400104**. https://doi.org/10.1002/gch2.202400104 (schyck2024harnessingfungisignaling pages 2-3)

6. Yuan Z, Li P, Yang X, et al. **FgPfn participates in vegetative growth, sexual reproduction, pathogenicity, and fungicides sensitivity via affecting both microtubules and actin in the filamentous fungus Fusarium graminearum.** *PLOS Pathogens*. **2024-05**. DOI: **10.1371/journal.ppat.1012215**. https://doi.org/10.1371/journal.ppat.1012215 (yuan2024fgpfnparticipatesin pages 9-11)

7. Zhong X, Baur SSM, Ongenae VMA, et al. **The stomatin-like protein StlP organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress.** *Nature Communications*. **2025-03**. DOI: **10.1038/s41467-025-58093-x**. https://doi.org/10.1038/s41467-025-58093-x (zhong2025thestomatinlikeprotein pages 1-2, zhong2025thestomatinlikeprotein pages 4-5, zhong2025thestomatinlikeprotein media f2a749fa)

8. Claessen D, Zhong X, Baur S, et al. **The stomatin-like protein StlP organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress (preprint).** *Research Square*. **2024-01**. DOI: **10.21203/rs.3.rs-3811693/v1**. https://doi.org/10.21203/rs.3.rs-3811693/v1 (claessen2024thestomatinlikeprotein pages 7-9, claessen2024thestomatinlikeprotein pages 20-27)

9. Cuesta UP. **Discovery and characterization of the first fungal granulin among the genes overexpressed during germination of Aspergillus fumigatus.** **2024**. (Bibliographic metadata incomplete in retrieved text; use with caution; prioritize peer-reviewed version during final curation.) (cuesta2024discoveryandcharacterization pages 148-152)


References

1. (bhowmick2023osmoticstressresponses pages 1-2): Sukanya Bhowmick, Mary L. Shenouda, and Natalia Tschowri. Osmotic stress responses and the biology of the second messenger c-di-amp in streptomyces. microLife, Apr 2023. URL: https://doi.org/10.1093/femsml/uqad020, doi:10.1093/femsml/uqad020. This article has 17 citations and is from a peer-reviewed journal.

2. (zhong2025thestomatinlikeprotein pages 4-5): Xiaobo Zhong, Sarah S. M. Baur, Veronique M. A. Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles P. van Wezel, Victor Carrion Bravo, Ariane Briegel, Marc Bramkamp, and Dennis Claessen. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Nature Communications, Mar 2025. URL: https://doi.org/10.1038/s41467-025-58093-x, doi:10.1038/s41467-025-58093-x. This article has 4 citations and is from a highest quality peer-reviewed journal.

3. (bhowmick2024cellshapeand pages 1-2): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

4. (zhong2025thestomatinlikeprotein pages 1-2): Xiaobo Zhong, Sarah S. M. Baur, Veronique M. A. Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles P. van Wezel, Victor Carrion Bravo, Ariane Briegel, Marc Bramkamp, and Dennis Claessen. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Nature Communications, Mar 2025. URL: https://doi.org/10.1038/s41467-025-58093-x, doi:10.1038/s41467-025-58093-x. This article has 4 citations and is from a highest quality peer-reviewed journal.

5. (claessen2024thestomatinlikeprotein pages 7-9): Dennis Claessen, Xiaobo Zhong, Sarah Baur, Veronique Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles van Wezel, Victor Carrion Brava, Ariane Briegel, and Marc Bramkamp. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Unknown journal, Jan 2024. URL: https://doi.org/10.21203/rs.3.rs-3811693/v1, doi:10.21203/rs.3.rs-3811693/v1.

6. (schyck2024harnessingfungisignaling pages 2-3): Sarah Schyck, Pietro Marchese, Muhamad Amani, Mark Ablonczy, Linde Spoelstra, Mitchell Jones, Yaren Bathaei, Alexander Bismarck, and Kunal Masania. Harnessing fungi signaling in living composites. Global Challenges, Jul 2024. URL: https://doi.org/10.1002/gch2.202400104, doi:10.1002/gch2.202400104. This article has 13 citations and is from a peer-reviewed journal.

7. (zuriegat2024emergingrolesof pages 6-7): Qussai Zuriegat, Yakubu Saddeeq Abubakar, Zonghua Wang, Meilian Chen, and Jun Zhang. Emerging roles of exocyst complex in fungi: a review. Journal of Fungi, 10:614, Aug 2024. URL: https://doi.org/10.3390/jof10090614, doi:10.3390/jof10090614. This article has 11 citations.

8. (zuriegat2024emergingrolesof pages 23-24): Qussai Zuriegat, Yakubu Saddeeq Abubakar, Zonghua Wang, Meilian Chen, and Jun Zhang. Emerging roles of exocyst complex in fungi: a review. Journal of Fungi, 10:614, Aug 2024. URL: https://doi.org/10.3390/jof10090614, doi:10.3390/jof10090614. This article has 11 citations.

9. (cuesta2024discoveryandcharacterization pages 148-152): U Pérez Cuesta. Discovery and characterization of the first fungal granulin among the genes overexpressed during germination of aspergillus fumigatus. Unknown journal, 2024.

10. (li2024contrastingeffectsof pages 9-10): Huiping Li, Jiachun Zhu, Zihao Li, Ping Xu, Lin Ma, Yajie Zou, Shaoxuan Qu, and Xiaoqin Wu. Contrasting effects of nadph oxidases on the fungal hyphae growth and immune responses in pleurotus ostreatus. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1387643, doi:10.3389/fmicb.2024.1387643. This article has 3 citations and is from a peer-reviewed journal.

11. (lubbersUnknownyearaspersn.& pages 8-8): M Lubbers. Aspers, n., & claessen, d.(2025). Unknown journal, Unknown year.

12. (zhong2025thestomatinlikeprotein media f2a749fa): Xiaobo Zhong, Sarah S. M. Baur, Veronique M. A. Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles P. van Wezel, Victor Carrion Bravo, Ariane Briegel, Marc Bramkamp, and Dennis Claessen. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Nature Communications, Mar 2025. URL: https://doi.org/10.1038/s41467-025-58093-x, doi:10.1038/s41467-025-58093-x. This article has 4 citations and is from a highest quality peer-reviewed journal.

13. (zhong2025thestomatinlikeprotein pages 2-4): Xiaobo Zhong, Sarah S. M. Baur, Veronique M. A. Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles P. van Wezel, Victor Carrion Bravo, Ariane Briegel, Marc Bramkamp, and Dennis Claessen. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Nature Communications, Mar 2025. URL: https://doi.org/10.1038/s41467-025-58093-x, doi:10.1038/s41467-025-58093-x. This article has 4 citations and is from a highest quality peer-reviewed journal.

14. (yuan2024fgpfnparticipatesin pages 9-11): Zhili Yuan, Pengfei Li, Xin Yang, Xiaowei Cai, Luoyu Wu, Feifei Zhao, Weidong Wen, Mingguo Zhou, and Yiping Hou. Fgpfn participates in vegetative growth, sexual reproduction, pathogenicity, and fungicides sensitivity via affecting both microtubules and actin in the filamentous fungus fusarium graminearum. PLOS Pathogens, 20:e1012215, May 2024. URL: https://doi.org/10.1371/journal.ppat.1012215, doi:10.1371/journal.ppat.1012215. This article has 8 citations and is from a highest quality peer-reviewed journal.

15. (cuesta2024discoveryandcharacterization pages 29-34): U Pérez Cuesta. Discovery and characterization of the first fungal granulin among the genes overexpressed during germination of aspergillus fumigatus. Unknown journal, 2024.

16. (zuriegat2024emergingrolesof pages 9-10): Qussai Zuriegat, Yakubu Saddeeq Abubakar, Zonghua Wang, Meilian Chen, and Jun Zhang. Emerging roles of exocyst complex in fungi: a review. Journal of Fungi, 10:614, Aug 2024. URL: https://doi.org/10.3390/jof10090614, doi:10.3390/jof10090614. This article has 11 citations.

17. (claessen2024thestomatinlikeprotein pages 20-27): Dennis Claessen, Xiaobo Zhong, Sarah Baur, Veronique Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles van Wezel, Victor Carrion Brava, Ariane Briegel, and Marc Bramkamp. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Unknown journal, Jan 2024. URL: https://doi.org/10.21203/rs.3.rs-3811693/v1, doi:10.21203/rs.3.rs-3811693/v1.