---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:56:13.303407'
end_time: '2026-06-18T08:16:09.175563'
duration_seconds: 1195.87
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: gram negative
  trait_identifier: METPO:1000699
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: gram_negative
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A gram stain in which bacteria do not retain crystal violet dye and
    appear pink or red after staining, indicating a thin peptidoglycan layer and presence
    of an outer membrane.
  parent_traits: METPO:1000697
  synonyms: G_negative, negative
  evidence_summary: 'DOI:10.1038/s41579-019-0201-x: defining feature of the Gram-negative
    cell envelope (Supports the outer membrane as a defining Gram-negative envelope
    feature.) | PMID:27564552: Gram-Negative Bacterium Escherichia coli (Organism
    example: Escherichia coli is described as Gram-negative.)'
  causal_graph_summary: 'gram_negative_outer_membrane_dye_loss: 7 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gram negative
- **METPO identifier:** METPO:1000699
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A gram stain in which bacteria do not retain crystal violet dye and appear pink or red after staining, indicating a thin peptidoglycan layer and presence of an outer membrane.
- **Parent traits:** METPO:1000697
- **Synonyms:** G_negative, negative
- **Existing evidence:** DOI:10.1038/s41579-019-0201-x: defining feature of the Gram-negative cell envelope (Supports the outer membrane as a defining Gram-negative envelope feature.) | PMID:27564552: Gram-Negative Bacterium Escherichia coli (Organism example: Escherichia coli is described as Gram-negative.)
- **Existing causal graph summary:** gram_negative_outer_membrane_dye_loss: 7 nodes, 5 edges

## Research Objective

Research the microbial trait **gram negative** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gram_negative.yaml`.

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
- **Trait label:** gram negative
- **METPO identifier:** METPO:1000699
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A gram stain in which bacteria do not retain crystal violet dye and appear pink or red after staining, indicating a thin peptidoglycan layer and presence of an outer membrane.
- **Parent traits:** METPO:1000697
- **Synonyms:** G_negative, negative
- **Existing evidence:** DOI:10.1038/s41579-019-0201-x: defining feature of the Gram-negative cell envelope (Supports the outer membrane as a defining Gram-negative envelope feature.) | PMID:27564552: Gram-Negative Bacterium Escherichia coli (Organism example: Escherichia coli is described as Gram-negative.)
- **Existing causal graph summary:** gram_negative_outer_membrane_dye_loss: 7 nodes, 5 edges

## Research Objective

Research the microbial trait **gram negative** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gram_negative.yaml`.

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


## Microbial Trait Causal Graph Research Report: **gram negative** (METPO:1000699)

### 1) Scope summary (trait meaning, boundaries, and assay context)
The METPO trait **gram negative** (METPO:1000699) is best treated as an **assay-observed staining phenotype**: in a standard Gram stain, cells **do not retain the crystal violet–iodine complex after decolorization** and therefore appear **pink/red** after counterstaining. Mechanistically, this outcome is commonly linked to a **diderm (two-membrane) envelope architecture** in which a **thin peptidoglycan layer** in the periplasm is insufficient to retain the crystal violet–iodine complex during the ethanol/solvent step. The decolorizer can also disrupt the outer lipid layer, further promoting dye-complex loss. (meister2024gramstaining pages 1-6, meister2024gramstaining pages 6-9)

In modern cell-envelope biology, the **outer membrane (OM)** is viewed as a defining structural feature: “**The outer membrane (OM) is the hallmark of the gram-negative bacterial cell envelope**.” (tan2024howbacteriaestablish pages 1-3)

**Boundary/nearby phenotypes and curation cautions:**
- **Gram-variable / technical variability:** Gram-stain outcome can be affected by smear thickness, fixation, and especially decolorization; over- or under-decolorization can cause misinterpretation. Older cultures may show ruptured walls and stain inconsistently. (meister2024gramstaining pages 6-9, meister2024gramstaining pages 1-6)
- **Diderms without canonical LPS:** Not all diderm bacteria have canonical LPS; ~25% of diderm phyla may lack LPS biosynthesis genes (boundary case; do not equate “diderm” with “LPS-positive” universally). (machin2023theroleof pages 34-37)
- **LOS vs LPS:** Some Gram-negative pathogens (e.g., A. baumannii) can produce **lipooligosaccharide (LOS)** lacking O-antigen rather than full LPS. (bisht2024breakingbarriersexploiting pages 2-3)

### 2) Key concepts and definitions (current understanding)
**Gram stain chemistry and outcome:** A classical Gram stain applies **crystal violet** (primary stain) followed by **iodine/Lugol’s** (mordant) to form a crystal violet–iodine complex, then **ethanol/solvent decolorization**, then a **counterstain** (e.g., safranin/fuchsin). Cells that cannot retain the complex are decolorized and become visible as **pink** with counterstain. (meister2024gramstaining pages 1-6)

**Procedural parameters matter:** One stepwise protocol specifies ~1 min crystal violet, ~1 min Lugol iodine, ~15 s decolorization, and 30–60 s counterstain; it emphasizes decolorization as “the most consequential step” and warns that both over- and under-decolorization can misclassify results. (meister2024gramstaining pages 6-9, meister2024gramstaining media cd894c1e)

**Envelope architecture link:** A Gram-negative (diderm) envelope is typically described as **inner membrane + periplasm containing thin peptidoglycan + outer membrane**, with the OM often being asymmetric and protein-rich. (machin2023theroleof pages 34-37, tan2024howbacteriaestablish pages 1-3)

### 3) Recent developments and latest research (prioritizing 2023–2024)
**3.1 Outer membrane as a “hallmark” and mechanistic focus on lipid asymmetry (2024 Annual Review)**
A key 2024 synthesis frames OM lipid asymmetry (LPS outer leaflet; phospholipids inner leaflet) as central to the barrier properties of Gram-negative bacteria and intrinsic antibiotic resistance, explicitly calling the OM the hallmark of the Gram-negative envelope. (tan2024howbacteriaestablish pages 1-3)

**3.2 Cell-envelope diversity across Bacteria (2024 Nature Microbiology)**
A 2024 Nature Microbiology review highlights envelope diversity across the bacterial tree and reinforces that many diderms use conserved OM components (e.g., β-barrel OMPs assembled by BAM; Lpt components broadly conserved even when LPS varies), while also emphasizing that OM composition differs across lineages. (hashimi2024cellenvelopediversity pages 1-2)

**3.3 OM biogenesis as an antimicrobial strategy space (2024 Pathogens; 2024 J Microbiology; 2024 npj Antimicrobials and Resistance)**
Recent reviews emphasize that OM construction and maintenance depend on **specialized trans-envelope machines**—and that disrupting them can destabilize the OM and sensitize bacteria:
- **Lpt** (LPS transport): transports LPS across the periplasm to the OM, and disruption of LPS biosynthesis/transport leads to **membrane instability** and **increased antibiotic susceptibility**. (yoon2024structuralinsightsinto pages 1-3)
- **BAM** (β-barrel OMP insertion): folds and inserts β-barrel OMPs into the OM; OMP biogenesis defects provoke envelope stress responses (σE). (bisht2024breakingbarriersexploiting pages 3-5)
- **Lol** (lipoprotein trafficking): delivers OM lipoproteins including key OM biogenesis factors (e.g., BamD, LptE). (bisht2024breakingbarriersexploiting pages 5-7)
- **Mla** (retrograde phospholipid transport): removes mislocalized phospholipids to preserve OM asymmetry. (bisht2024breakingbarriersexploiting pages 2-3)
- **Tol–Pal** (envelope connectivity): disruption increases OM permeability and sensitizes cells to a broad range of antibiotics. (szczepaniak2024thetolpal pages 5-6)

### 4) Current applications and real-world implementations
**4.1 Clinical microbiology and rapid decision support**
Gram staining remains a front-line diagnostic categorization. A 2024 Scientific Data report released a clinical Gram-stain microscopy dataset for Microbiological Rapid On-Site Evaluation (M-ROSE): **1,705 images** (4,912×3,684 px) from lower-respiratory samples; **4,833 cocci** and **6,991 bacilli** were manually labeled and classified as Gram-negative vs Gram-positive, supporting automated interpretation and rapid treatment guidance. (wang2024aclinicalbacterial pages 1-2, wang2024aclinicalbacterial pages 2-3)

**4.2 Antimicrobial discovery/optimization and barrier-aware strategies**
Mechanistic research on Gram-negative envelopes directly informs antibiotic development because OM impermeability is a central barrier to compound entry and efficacy. Reviews emphasize that LPS in the outer leaflet is a major determinant of OM impermeability and that Lpt-mediated LPS transport is a druggable vulnerability (disruption → instability and antibiotic sensitization). (yoon2024structuralinsightsinto pages 1-3, tan2024howbacteriaestablish pages 1-3)

### 5) Relevant statistics and data from recent studies
**5.1 Sepsis prognosis and biomarker differences (2023 meta-analysis)**
A 2023 Critical Care systematic review and meta-analysis screened **6,949** records and included **45** observational studies with **5,586** subjects. It found:
- **No significant survival difference** between Gram-negative and Gram-positive sepsis (OR **0.95**, 95% CI 0.70–1.28). (tang2023prognosticdifferencesin pages 1-2)
- **Higher incidence of septic shock/severe sepsis** in Gram-negative infections (OR **1.73**, 95% CI 1.09–2.76). (tang2023prognosticdifferencesin pages 2-4)
- Higher inflammatory markers in Gram-negative infections: CRP SMD **0.39** (95% CI 0.02–0.76), PCT SMD **1.95** (95% CI 1.32–2.59), TNF-α MD **0.31** (95% CI 0.25–0.38). (tang2023prognosticdifferencesin pages 1-2)

**5.2 Diagnostic AI dataset statistics (2024)**
The M-ROSE dataset includes **1,705** Gram-stained images and thousands of labeled bacteria (4,833 cocci; 6,991 bacilli), providing a real-world resource for automated Gram-status inference from clinical specimens. (wang2024aclinicalbacterial pages 1-2, wang2024aclinicalbacterial pages 2-3)

---

## Candidate nodes (grouped, with suggested grounding)
| Node label | Node type (assay factor / cellular structure / macromolecule / pathway-system / gene-protein complex / chemical) | Suggested ontology grounding (CURIE or label-only) | Notes (1 line) |
|---|---|---|---|
| crystal violet | chemical | CHEBI:58090 | Primary Gram-stain dye applied before mordanting; part of the assay mechanism distinguishing Gram-negative from Gram-positive cells (meister2024gramstaining pages 1-6, meister2024gramstaining pages 6-9) |
| Lugol's solution / iodine | chemical | CHEBI:17632 | Mordant that stabilizes crystal violet in a crystal violet–iodine complex during Gram staining (meister2024gramstaining pages 1-6, meister2024gramstaining pages 6-9) |
| ethanol decolorizer | chemical | CHEBI:16236 | Decolorizing solvent; in Gram-negative cells it removes outer lipid material and promotes dye-complex loss if not retained (meister2024gramstaining pages 1-6, meister2024gramstaining pages 6-9) |
| safranin | chemical | CHEBI:52648 | Counterstain that colors decolorized Gram-negative cells pink/red after ethanol treatment (meister2024gramstaining pages 1-6, meister2024gramstaining pages 6-9) |
| basic fuchsin / fuchsin | chemical | CHEBI:8764 | Alternative counterstain for cells that lose the primary stain during decolorization (meister2024gramstaining pages 6-9) |
| crystal violet–iodine complex retention | assay factor | label-only | Positive retention outcome associated with thick peptidoglycan/monoderm architecture rather than Gram-negative cells (useful contrast node) (meister2024gramstaining pages 1-6, ranjani2024studyonisolation pages 7-10) |
| crystal violet–iodine complex loss | assay factor | label-only | Immediate assay outcome underlying Gram-negative staining after decolorization (meister2024gramstaining pages 1-6, ranjani2024studyonisolation pages 7-10) |
| outer membrane | cellular structure | GO:0019867 | Hallmark structure of the Gram-negative envelope and key determinant of permeability/barrier properties (tan2024howbacteriaestablish pages 1-3, machin2023theroleof pages 34-37) |
| inner membrane | cellular structure | GO:0005886 | Cytoplasmic membrane underlying the periplasm and source membrane for envelope biogenesis pathways (machin2023theroleof pages 34-37, yoon2024structuralinsightsinto pages 1-3) |
| periplasm | cellular structure | GO:0042597 | Aqueous compartment between membranes containing thin peptidoglycan and multiple envelope biogenesis factors (machin2023theroleof pages 34-37, bisht2024breakingbarriersexploiting pages 2-3) |
| thin peptidoglycan layer | cellular structure | GO:0009273 | Characteristic thin wall in diderms/Gram-negatives; insufficient alone to retain dye complex after decolorization (meister2024gramstaining pages 1-6, machin2023theroleof pages 34-37) |
| lipopolysaccharide (LPS) | macromolecule | CHEBI:16412 | Major outer-leaflet glycolipid creating the strong outer-membrane barrier in many Gram-negative bacteria (yoon2024structuralinsightsinto pages 1-3, machin2023theroleof pages 37-41) |
| lipooligosaccharide (LOS) | macromolecule | label-only | LPS-related outer-membrane glycolipid lacking O-antigen in some Gram-negatives such as A. baumannii (bisht2024breakingbarriersexploiting pages 2-3, fivenson2024coordinatedassemblyof pages 6-7) |
| lipid A | macromolecule | CHEBI:16412 | Conserved membrane-anchor portion of LPS inserted into the OM outer leaflet (machin2023theroleof pages 37-41, yoon2024structuralinsightsinto pages 1-3) |
| O-antigen | macromolecule | label-only | Distal polysaccharide part of many LPS molecules; absent in LOS-producing taxa (bisht2024breakingbarriersexploiting pages 2-3, machin2023theroleof pages 37-41) |
| outer membrane porins | macromolecule | GO:0015288 | β-barrel channels such as OmpF/OmpC/PhoE that regulate small-molecule influx across the OM (bisht2024breakingbarriersexploiting pages 2-3, szczepaniak2024thetolpal pages 1-2) |
| β-barrel outer membrane proteins (OMPs) | macromolecule | GO:0140318 | Major OM protein class assembled by BAM and important for membrane integrity/permeability (hashimi2024cellenvelopediversity pages 1-2, bisht2024breakingbarriersexploiting pages 3-5) |
| Lpt pathway | pathway-system | label-only | Trans-envelope machinery that transports LPS from IM to OM and is essential for OM impermeability (yoon2024structuralinsightsinto pages 1-3, bisht2024breakingbarriersexploiting pages 3-5) |
| BAM complex | gene-protein complex | label-only | β-barrel assembly machinery that folds/inserts OMPs into the OM; BamA/BamD are core essential components (bisht2024breakingbarriersexploiting pages 3-5) |
| Lol pathway | pathway-system | label-only | Lipoprotein trafficking pathway delivering mature lipoproteins such as LptE and BamD to the OM (bisht2024breakingbarriersexploiting pages 5-7, bisht2024breakingbarriersexploiting pages 2-3) |
| Mla pathway | pathway-system | label-only | Retrograde phospholipid transport system that removes mislocalized phospholipids and helps preserve OM asymmetry (bisht2024breakingbarriersexploiting pages 2-3, tan2024howbacteriaestablish pages 1-3) |
| Tol-Pal system | gene-protein complex | label-only | Envelope-spanning complex that safeguards connectivity of the three-layer Gram-negative envelope and affects permeability when disrupted (szczepaniak2024thetolpal pages 1-2, szczepaniak2024thetolpal pages 5-6) |
| SecYEG translocon | gene-protein complex | label-only | Inner-membrane translocon exporting unfolded OMP precursors into the periplasm before OM assembly (bisht2024breakingbarriersexploiting pages 3-5) |
| SurA chaperone | gene-protein complex | UniProtKB: label-only | Periplasmic chaperone that delivers unfolded OMPs to BAM for OM insertion (bisht2024breakingbarriersexploiting pages 3-5) |
| Skp chaperone | gene-protein complex | UniProtKB: label-only | Alternative periplasmic OMP chaperone involved in escorting unfolded substrates to BAM (bisht2024breakingbarriersexploiting pages 3-5) |
| σE envelope stress response | pathway-system | GO:0035963 | Stress-signaling system activated by unfolded OMP accumulation and OM biogenesis defects (bisht2024breakingbarriersexploiting pages 3-5, bisht2024breakingbarriersexploiting pages 2-3) |
| Rcs envelope stress response | pathway-system | label-only | Stress system induced by LPS perturbation that promotes protective envelope responses such as colanic acid production (bisht2024breakingbarriersexploiting pages 3-5) |
| Cpx envelope stress response | pathway-system | label-only | Stress system activated by mislocalized lipoproteins such as NlpE during envelope damage (bisht2024breakingbarriersexploiting pages 3-5) |
| magnesium ion (Mg2+) | chemical | CHEBI:18420 | Divalent cation that stabilizes LPS packing in the outer leaflet and supports OM barrier integrity (bisht2024breakingbarriersexploiting pages 2-3, machin2023theroleof pages 37-41) |
| calcium ion (Ca2+) | chemical | CHEBI:29108 | Divalent cation that stabilizes LPS-LPS interactions in the OM outer leaflet (bisht2024breakingbarriersexploiting pages 2-3) |


*Table: This table lists evidence-supported candidate entities for a Gram-negative TraitMech graph, spanning assay reagents, envelope structures, macromolecular components, and biogenesis/maintenance systems. It is useful as a node inventory for converting literature evidence into ontology-grounded causal graph curation.*

---

## Candidate causal edges (evidence-backed triples)
| Subject (node) | Predicate | Object (node) | Evidence snippet (short quote) | Reference (DOI + URL + year) | Notes/curation flags |
|---|---|---|---|---|---|
| ethanol decolorization | causes | crystal violet–iodine complex loss | "When ethanol is added, diderm/Gram-negative organisms lose their outer lipid layer and lose most of the stain" (meister2024gramstaining pages 1-6) | 2024, Meister et al., Gram staining, journal unavailable via context | Assay-mechanism edge; protocol source, not high-authority review |
| crystal violet–iodine complex loss | enables | safranin uptake / pink-red staining | "A counterstain (e.g., safranin or fuchsin) is applied to stain cells that were decolorized, making them visible as pink" (meister2024gramstaining pages 1-6) | 2024, Meister et al., Gram staining, journal unavailable via context | Assay-mechanism edge |
| thin peptidoglycan layer | insufficient_to_retain | crystal violet–iodine complex during decolorization | "their thin peptidoglycan layer cannot retain the crystal violet–iodide complexes" (meister2024gramstaining pages 1-6) | 2024, Meister et al., Gram staining, journal unavailable via context | Central phenotype mechanism; assay-specific wording |
| outer membrane | is_hallmark_of | Gram-negative cell envelope | "The outer membrane (OM) is the hallmark of the gram-negative bacterial cell envelope" (tan2024howbacteriaestablish pages 1-3) | 10.1146/annurev-micro-032521-014507 · https://doi.org/10.1146/annurev-micro-032521-014507 · 2024 | Strong scope-defining edge |
| Gram-negative / diderm envelope | has_part | thin peptidoglycan layer in periplasm | "diderm bacteria possess an inner membrane (IM) and an outer membrane (OM) that enclose a thin (2–4 nm) peptidoglycan" (machin2023theroleof pages 34-37) | 2023, Machin thesis/journal unavailable via context | Use cautiously; supported by broader reviews too |
| LPS | occupies | outer membrane outer leaflet | "LPS occupies the outer leaflet while phospholipids occupy the inner leaflet" (tan2024howbacteriaestablish pages 1-3) | 10.1146/annurev-micro-032521-014507 · https://doi.org/10.1146/annurev-micro-032521-014507 · 2024 | Strong OM-asymmetry edge |
| Mg2+/Ca2+ | stabilizes | LPS packing | "Divalent cations (Mg2+/Ca2+) stabilize LPS packing" (bisht2024breakingbarriersexploiting pages 2-3) | 10.3390/pathogens13100889 · https://doi.org/10.3390/pathogens13100889 · 2024 | Good chemical-to-structure edge |
| tight LPS packing | contributes_to | outer membrane impermeability / barrier function | "the tight packing of LPS and OM proteins creates an impermeable barrier" (tan2024howbacteriaestablish pages 1-3) | 10.1146/annurev-micro-032521-014507 · https://doi.org/10.1146/annurev-micro-032521-014507 · 2024 | Strong functional edge |
| Lpt pathway | transports | LPS to outer membrane outer leaflet | "transported to the OM by the ATP-driven Lpt machinery"; "moves LPS across the periplasm for insertion into the OM" (yoon2024structuralinsightsinto pages 1-3) | 10.1007/s12275-024-00137-w · https://doi.org/10.1007/s12275-024-00137-w · 2024 | Core biogenesis edge |
| LPS transport disruption | causes | membrane instability | "disruption of LPS biosynthesis or transport to membrane instability" (yoon2024structuralinsightsinto pages 1-3) | 10.1007/s12275-024-00137-w · https://doi.org/10.1007/s12275-024-00137-w · 2024 | Strong perturbation edge |
| LPS transport disruption | increases | antibiotic susceptibility | "disruption of LPS biosynthesis or transport [leads] to... increased antibiotic susceptibility" (yoon2024structuralinsightsinto pages 1-3) | 10.1007/s12275-024-00137-w · https://doi.org/10.1007/s12275-024-00137-w · 2024 | Strong perturbation edge; application-relevant |
| BAM complex | inserts/folds | β-barrel outer membrane proteins | "The Bam complex (BamA-E) folds uOMPs into β-barrels" (bisht2024breakingbarriersexploiting pages 3-5) | 10.3390/pathogens13100889 · https://doi.org/10.3390/pathogens13100889 · 2024 | Core OM biogenesis edge |
| Lol pathway | delivers | outer-membrane lipoproteins (e.g., BamD, LptE) | "The Lol system... delivers mature lipoproteins to the OM. Lipoproteins include... BamD, LptE" (bisht2024breakingbarriersexploiting pages 5-7) | 10.3390/pathogens13100889 · https://doi.org/10.3390/pathogens13100889 · 2024 | Good pathway-to-component edge |
| Mla pathway | removes | mislocalized phospholipids from outer membrane | "The Mla system performs retrograde transport of mislocalized phospholipids" (bisht2024breakingbarriersexploiting pages 2-3) | 10.3390/pathogens13100889 · https://doi.org/10.3390/pathogens13100889 · 2024 | Good OM-homeostasis edge |
| Mla pathway | maintains | outer membrane lipid asymmetry | "to counteract PL flipping to the outer leaflet" (bisht2024breakingbarriersexploiting pages 2-3) | 10.3390/pathogens13100889 · https://doi.org/10.3390/pathogens13100889 · 2024 | Slightly inferred from explicit function; curate with note |
| Tol-Pal system | safeguards | connectivity of outer membrane, peptidoglycan, and inner membrane | "Tol-Pal 'safeguard[s] connectivity between the three layers of the Gram-negative cell envelope'" (szczepaniak2024thetolpal pages 5-6) | 10.1038/s44259-024-00065-0 · https://doi.org/10.1038/s44259-024-00065-0 · 2024 | Strong envelope-maintenance edge |
| Tol-Pal disruption / tol mutants | increases | outer membrane permeability | "Disruption (tol mutants) increases OM permeability" (szczepaniak2024thetolpal pages 5-6) | 10.1038/s44259-024-00065-0 · https://doi.org/10.1038/s44259-024-00065-0 · 2024 | Strong perturbation edge |
| Tol-Pal disruption / tol mutants | sensitizes_to | antibiotics and detergents | "sensitises cells to detergents and a broad range of antibiotics" (szczepaniak2024thetolpal pages 5-6) | 10.1038/s44259-024-00065-0 · https://doi.org/10.1038/s44259-024-00065-0 · 2024 | Strong perturbation edge; application-relevant |
| some diderm bacteria | may_lack | LPS biosynthesis / canonical LPS-containing OM | "~25% of diderm phyla lack LPS biosynthesis genes" (machin2023theroleof pages 34-37) | 2023, Machin thesis/journal unavailable via context | Boundary case; uncertain for direct TraitMech generalization |
| LOS | lacks | O-antigen | "some species... produce LOS lacking O-antigen" (bisht2024breakingbarriersexploiting pages 2-3) | 10.3390/pathogens13100889 · https://doi.org/10.3390/pathogens13100889 · 2024 | Boundary-case chemistry edge; taxon-specific |
| diderm/Gram-negative architecture | tends_to_cause | crystal violet–iodine complex loss after ethanol step | "diderm/Gram-negative organisms lose their outer lipid layer and lose most of the stain" (meister2024gramstaining pages 1-6) | 2024, Meister et al., Gram staining, journal unavailable via context | Integrative phenotype edge; assay-specific and somewhat inferred across taxa |


*Table: This table compiles curation-ready causal edges for the Gram-negative trait, spanning Gram-stain assay chemistry, defining envelope structures, outer-membrane biogenesis systems, and perturbation effects. It is useful for translating literature evidence into a TraitMech-style graph while flagging uncertain or boundary-case claims.*

---

## Warnings / claims not yet suitable for strong curation
1. **Equating Gram-negative with “LPS-containing OM” is not universally valid.** Some diderm lineages may lack LPS biosynthesis genes; treat “outer membrane presence” as the primary defining feature, and LPS as a common (but not universal) OM component. (machin2023theroleof pages 34-37, hashimi2024cellenvelopediversity pages 1-2)
2. **Assay sensitivity:** Gram-negative classification is operationally defined by the Gram stain. Edges from “outer membrane” or “thin peptidoglycan” to “dye loss” are assay-dependent and can be confounded by protocol variation (decolorization time, smear thickness) and physiological state (older cultures). (meister2024gramstaining pages 6-9, meister2024gramstaining pages 1-6)
3. **Some sources in the evidence set are nonstandard (protocol/thesis) and should be treated as supporting but not definitive.** Prefer curating mechanistic/biogenesis edges from peer-reviewed reviews and primary literature (e.g., Lpt, Tol–Pal) and keep protocol-derived chemistry edges as assay-process nodes. (yoon2024structuralinsightsinto pages 1-3, szczepaniak2024thetolpal pages 5-6, meister2024gramstaining pages 1-6)

---

## DOI-first bibliography (with URLs and publication dates)
1. **Tan WB, Chng S-S.** *How Bacteria Establish and Maintain Outer Membrane Lipid Asymmetry.* **Annual Review of Microbiology** (Nov **2024**). DOI: **10.1146/annurev-micro-032521-014507**. URL: https://doi.org/10.1146/annurev-micro-032521-014507 (tan2024howbacteriaestablish pages 1-3)
2. **Hashimi A, Tocheva EI.** *Cell envelope diversity and evolution across the bacterial tree of life.* **Nature Microbiology** (Sep **2024**). DOI: **10.1038/s41564-024-01812-9**. URL: https://doi.org/10.1038/s41564-024-01812-9 (hashimi2024cellenvelopediversity pages 1-2)
3. **Bisht R, Charlesworth PD, Sperandeo P, Polissi A.** *Breaking Barriers: Exploiting Envelope Biogenesis and Stress Responses to Develop Novel Antimicrobial Strategies in Gram-Negative Bacteria.* **Pathogens** (Oct **2024**). DOI: **10.3390/pathogens13100889**. URL: https://doi.org/10.3390/pathogens13100889 (bisht2024breakingbarriersexploiting pages 3-5)
4. **Yoon Y, Song S.** *Structural Insights into the Lipopolysaccharide Transport (Lpt) System as a Novel Antibiotic Target.* **Journal of Microbiology** (May **2024**). DOI: **10.1007/s12275-024-00137-w**. URL: https://doi.org/10.1007/s12275-024-00137-w (yoon2024structuralinsightsinto pages 1-3)
5. **Szczepaniak J, Webby MN.** *The Tol Pal system integrates maintenance of the three layered cell envelope.* **npj Antimicrobials and Resistance** (Dec **2024**). DOI: **10.1038/s44259-024-00065-0**. URL: https://doi.org/10.1038/s44259-024-00065-0 (szczepaniak2024thetolpal pages 5-6)
6. **Wang X, Shi Y, Guo S, et al.** *A Clinical Bacterial Dataset for Deep Learning in Microbiological Rapid On-Site Evaluation.* **Scientific Data** (Jun **2024**). DOI: **10.1038/s41597-024-03370-5**. URL: https://doi.org/10.1038/s41597-024-03370-5 (wang2024aclinicalbacterial pages 1-2)
7. **Tang A, Shi Y, Dong Q, et al.** *Prognostic differences in sepsis caused by gram-negative bacteria and gram-positive bacteria: a systematic review and meta-analysis.* **Critical Care** (Nov **2023**). DOI: **10.1186/s13054-023-04750-w**. URL: https://doi.org/10.1186/s13054-023-04750-w (tang2023prognosticdifferencesin pages 1-2)

### Non-DOI/secondary protocol sources used for assay detail (use cautiously in curation)
- **Meister C, Bernhart L, Jimenez-Soto LF.** *Gram staining.* (2024; journal metadata not available in retrieved text). Provides stepwise staining timing and interpretation cautions. (meister2024gramstaining pages 1-6, meister2024gramstaining pages 6-9, meister2024gramstaining media cd894c1e)

---

## Figures (retrieved from sources)
- Gram staining procedural list (timings and steps) from Meister et al. 2024. (meister2024gramstaining media cd894c1e)

References

1. (meister2024gramstaining pages 1-6): C Meister, L Bernhart, and LF Jimenez-Soto. Gram staining. Unknown journal, 2024.

2. (meister2024gramstaining pages 6-9): C Meister, L Bernhart, and LF Jimenez-Soto. Gram staining. Unknown journal, 2024.

3. (tan2024howbacteriaestablish pages 1-3): Wee Boon Tan and Shu-Sin Chng. How bacteria establish and maintain outer membrane lipid asymmetry. Nov 2024. URL: https://doi.org/10.1146/annurev-micro-032521-014507, doi:10.1146/annurev-micro-032521-014507. This article has 19 citations and is from a peer-reviewed journal.

4. (machin2023theroleof pages 34-37): JM Machin. The role of native outer membrane features in the folding and function of omps. Unknown journal, 2023.

5. (bisht2024breakingbarriersexploiting pages 2-3): Renu Bisht, Pierre D. Charlesworth, Paola Sperandeo, and Alessandra Polissi. Breaking barriers: exploiting envelope biogenesis and stress responses to develop novel antimicrobial strategies in gram-negative bacteria. Pathogens, 13:889, Oct 2024. URL: https://doi.org/10.3390/pathogens13100889, doi:10.3390/pathogens13100889. This article has 12 citations.

6. (meister2024gramstaining media cd894c1e): C Meister, L Bernhart, and LF Jimenez-Soto. Gram staining. Unknown journal, 2024.

7. (hashimi2024cellenvelopediversity pages 1-2): Ameena Hashimi and Elitza I. Tocheva. Cell envelope diversity and evolution across the bacterial tree of life. Nature microbiology, 9:2475-2487, Sep 2024. URL: https://doi.org/10.1038/s41564-024-01812-9, doi:10.1038/s41564-024-01812-9. This article has 27 citations and is from a highest quality peer-reviewed journal.

8. (yoon2024structuralinsightsinto pages 1-3): Yurim Yoon and Saemee Song. Structural insights into the lipopolysaccharide transport (lpt) system as a novel antibiotic target. Journal of microbiology, 62:261-275, May 2024. URL: https://doi.org/10.1007/s12275-024-00137-w, doi:10.1007/s12275-024-00137-w. This article has 11 citations and is from a peer-reviewed journal.

9. (bisht2024breakingbarriersexploiting pages 3-5): Renu Bisht, Pierre D. Charlesworth, Paola Sperandeo, and Alessandra Polissi. Breaking barriers: exploiting envelope biogenesis and stress responses to develop novel antimicrobial strategies in gram-negative bacteria. Pathogens, 13:889, Oct 2024. URL: https://doi.org/10.3390/pathogens13100889, doi:10.3390/pathogens13100889. This article has 12 citations.

10. (bisht2024breakingbarriersexploiting pages 5-7): Renu Bisht, Pierre D. Charlesworth, Paola Sperandeo, and Alessandra Polissi. Breaking barriers: exploiting envelope biogenesis and stress responses to develop novel antimicrobial strategies in gram-negative bacteria. Pathogens, 13:889, Oct 2024. URL: https://doi.org/10.3390/pathogens13100889, doi:10.3390/pathogens13100889. This article has 12 citations.

11. (szczepaniak2024thetolpal pages 5-6): Joanna Szczepaniak and Melissa N. Webby. The tol pal system integrates maintenance of the three layered cell envelope. npj Antimicrobials and Resistance, Dec 2024. URL: https://doi.org/10.1038/s44259-024-00065-0, doi:10.1038/s44259-024-00065-0. This article has 12 citations and is from a peer-reviewed journal.

12. (wang2024aclinicalbacterial pages 1-2): Xiuli Wang, Yinghan Shi, Shasha Guo, Xuzhong Qu, Fei Xie, Zhimei Duan, Ye Hu, Han Fu, Xin Shi, Tingwei Quan, Kaifei Wang, and Lixin Xie. A clinical bacterial dataset for deep learning in microbiological rapid on-site evaluation. Scientific Data, Jun 2024. URL: https://doi.org/10.1038/s41597-024-03370-5, doi:10.1038/s41597-024-03370-5. This article has 18 citations and is from a peer-reviewed journal.

13. (wang2024aclinicalbacterial pages 2-3): Xiuli Wang, Yinghan Shi, Shasha Guo, Xuzhong Qu, Fei Xie, Zhimei Duan, Ye Hu, Han Fu, Xin Shi, Tingwei Quan, Kaifei Wang, and Lixin Xie. A clinical bacterial dataset for deep learning in microbiological rapid on-site evaluation. Scientific Data, Jun 2024. URL: https://doi.org/10.1038/s41597-024-03370-5, doi:10.1038/s41597-024-03370-5. This article has 18 citations and is from a peer-reviewed journal.

14. (tang2023prognosticdifferencesin pages 1-2): Aling Tang, Yi Shi, Qingqing Dong, Sihui Wang, Yao Ge, Chenyan Wang, Zhimin Gong, Weizhen Zhang, and Wei Chen. Prognostic differences in sepsis caused by gram-negative bacteria and gram-positive bacteria: a systematic review and meta-analysis. Critical Care, Nov 2023. URL: https://doi.org/10.1186/s13054-023-04750-w, doi:10.1186/s13054-023-04750-w. This article has 91 citations and is from a highest quality peer-reviewed journal.

15. (tang2023prognosticdifferencesin pages 2-4): Aling Tang, Yi Shi, Qingqing Dong, Sihui Wang, Yao Ge, Chenyan Wang, Zhimin Gong, Weizhen Zhang, and Wei Chen. Prognostic differences in sepsis caused by gram-negative bacteria and gram-positive bacteria: a systematic review and meta-analysis. Critical Care, Nov 2023. URL: https://doi.org/10.1186/s13054-023-04750-w, doi:10.1186/s13054-023-04750-w. This article has 91 citations and is from a highest quality peer-reviewed journal.

16. (ranjani2024studyonisolation pages 7-10): VA Ranjani, GT Rani, B Jithendar, K Serafina, and KJ Sri. Study on isolation and characterization of bacteria from soil samples of fuel station. Unknown journal, 2024.

17. (machin2023theroleof pages 37-41): JM Machin. The role of native outer membrane features in the folding and function of omps. Unknown journal, 2023.

18. (fivenson2024coordinatedassemblyof pages 6-7): Elayne M Fivenson, Laurent Dubois, and Thomas G Bernhardt. Co-ordinated assembly of the multilayered cell envelope of gram-negative bacteria. Jun 2024. URL: https://doi.org/10.1016/j.mib.2024.102479, doi:10.1016/j.mib.2024.102479. This article has 24 citations and is from a peer-reviewed journal.

19. (szczepaniak2024thetolpal pages 1-2): Joanna Szczepaniak and Melissa N. Webby. The tol pal system integrates maintenance of the three layered cell envelope. npj Antimicrobials and Resistance, Dec 2024. URL: https://doi.org/10.1038/s44259-024-00065-0, doi:10.1038/s44259-024-00065-0. This article has 12 citations and is from a peer-reviewed journal.