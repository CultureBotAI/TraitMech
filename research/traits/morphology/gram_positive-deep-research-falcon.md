---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:35:36.029413'
end_time: '2026-08-04T08:44:41.283122'
duration_seconds: 545.25
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: gram positive
  trait_identifier: METPO:1000698
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: gram_positive
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A gram stain in which an organism retains crystal violet dye and appears
    purple under microscopy due to a thick peptidoglycan cell wall.
  parent_traits: METPO:1000697
  synonyms: G_positive, positive
  evidence_summary: 'DOI:10.3109/10520299609117151: retention of a crystal violet:iodine
    complex (Supports Gram-positive phenotype as retention of crystal violet-iodine
    complex.) | PMID:16950365: Staphylococcus aureus is a gram-positive bacterium
    (Organism example: Staphylococcus aureus is described as Gram-positive.)'
  causal_graph_summary: 'gram_positive_cell_wall_retention: 13 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gram positive
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000698
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A gram stain in which an organism retains crystal violet dye and appears purple under microscopy due to a thick peptidoglycan cell wall.
- **Parent traits:** METPO:1000697
- **Synonyms:** G_positive, positive
- **Existing evidence:** DOI:10.3109/10520299609117151: retention of a crystal violet:iodine complex (Supports Gram-positive phenotype as retention of crystal violet-iodine complex.) | PMID:16950365: Staphylococcus aureus is a gram-positive bacterium (Organism example: Staphylococcus aureus is described as Gram-positive.)
- **Existing causal graph summary:** gram_positive_cell_wall_retention: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **gram positive** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gram_positive.yaml`.

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
- **Trait label:** gram positive
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000698
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A gram stain in which an organism retains crystal violet dye and appears purple under microscopy due to a thick peptidoglycan cell wall.
- **Parent traits:** METPO:1000697
- **Synonyms:** G_positive, positive
- **Existing evidence:** DOI:10.3109/10520299609117151: retention of a crystal violet:iodine complex (Supports Gram-positive phenotype as retention of crystal violet-iodine complex.) | PMID:16950365: Staphylococcus aureus is a gram-positive bacterium (Organism example: Staphylococcus aureus is described as Gram-positive.)
- **Existing causal graph summary:** gram_positive_cell_wall_retention: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **gram positive** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gram_positive.yaml`.

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


# Curation report: Gram-positive stain phenotype

## Trait record and recommendation

- **Trait label:** gram positive
- **Trait identifier:** **`METPO:1000698`**
- **Category/kind/status:** MORPHOLOGY / CLASS / REVIEWED
- **Parent:** `METPO:1000697`
- **Recommended graph interpretation:** an **assay-observed dye-retention phenotype**, not a taxonomic clade and not a synonym for a one-membrane (“monoderm”) envelope.

The core phenotype is retention of the crystal-violet–iodine (CV–I) complex after decolorization, producing purple cells by bright-field microscopy. In the canonical procedure, crystal violet enters fixed cells, iodine forms a relatively insoluble complex, and the structurally intact peptidoglycan-rich wall of a typical Gram-positive cell prevents efficient extraction during ethanol or acetone treatment. Counterstain therefore does not replace the purple signal. Conversely, autolysis, lysozyme, penicillin-mediated wall injury, or excessive decolorization can permit CV–I loss and make genetically “Gram-positive” organisms appear Gram-variable or Gram-negative. (beveridge2014samplingandstaining pages 6-7, rohde2019thegrampositivebacterial pages 1-2)

The curation should therefore terminate in **CV–I retention → purple microscopic appearance → `METPO:1000698`**, while treating peptidoglycan synthesis genes as upstream contributors rather than universal, individually sufficient determinants.

## 1. Scope and boundary cases

### Included phenotype

The trait represents a result of the classical differential-staining assay under specified conditions: fixed cells remain violet/purple after crystal violet, iodine mordant, and alcohol/acetone decolorization. The mechanistic center is the integrity, thickness, organization, and permeability of the cell wall—not merely the presence of peptidoglycan, which is widespread among bacteria. (beveridge2014samplingandstaining pages 6-7, rohde2019thegrampositivebacterial pages 1-2)

### Nearby concepts that must remain distinct

1. **Monoderm envelope architecture.** A one-membrane cell is not necessarily Gram-positive by stain. A 2024 analysis of **366 representative complete Bacillota genomes** found deeply branching organisms that stain Gram-negative despite lacking canonical LPS/outer-membrane biosynthesis machinery; the authors associate this with a relatively thin peptidoglycan layer inherited from diderm ancestors. Thus Gram reaction is at most a proxy for wall properties, not definitive evidence of membrane number. (choi2024deeplybranchingbacillota pages 1-2)
2. **Gram-positive taxonomic groups.** Bacillota and Actinomycetota contain important Gram-positive organisms, but staining is a phenotype and may vary with species, growth state, and protocol.
3. **Gram-variable phenotype.** Aged, autolytic, antibiotic-damaged, or otherwise wall-compromised cells can contain both purple and counterstained cells. This should be represented as an assay/state qualifier, not silently assigned to `METPO:1000698`. (beveridge2014samplingandstaining pages 6-7)
4. **Acid-fastness.** Mycobacteria have unusual lipid-rich envelopes and stain indifferently with the conventional Gram method; acid-fast staining is a separate trait and assay. (rohde2019thegrampositivebacterial pages 1-2)
5. **Cell-wall-deficient bacteria.** Mycoplasmas and experimentally generated L-forms lack the canonical wall substrate needed for the standard retention mechanism and should not be inferred from taxonomy.
6. **False-positive staining.** Thick smears or incomplete decolorization may leave nominally Gram-negative cells purple. Recent clinical-image work also observed purple Gram-negative cells or peripheral purple rings and documented variation caused by staining duration and specimen background. (beveridge2014samplingandstaining pages 6-7, wang2024aclinicalbacterial pages 3-5)

## 2. Candidate nodes grouped by type

### Trait and assay readouts

- Gram-positive stain phenotype — **`METPO:1000698`**
- Purple appearance under bright-field microscopy — label-only candidate
- Gram-variable staining — label-only candidate
- Gram-negative stain phenotype — use the reviewed METPO term if available; do not infer an identifier

### Chemicals and complexes

- Crystal violet — **`CHEBI:41688`**
- Iodine — **`CHEBI:17606`**
- Ethanol — **`CHEBI:16236`**
- Crystal-violet–iodine complex — label-only candidate; do not ground to crystal violet alone
- Counterstain, usually safranin — label-only unless the exact ontology term is verified
- Lysozyme — enzyme/protein node; species-specific UniProt grounding should be used only when the reagent is known
- Penicillin / β-lactam antibiotic — ground to the exact compound used rather than a generic drug-class identifier

### Macromolecules and envelope structures

- Peptidoglycan — **`CHEBI:8005`**
- Bacterial-type cell wall — **`GO:0009274`**
- Plasma membrane — **`GO:0005886`**
- Thick/cross-linked peptidoglycan layer — label-only state node
- Wall teichoic acid and lipoteichoic acid — label-only candidates pending structure-specific ChEBI verification
- Pentaglycine cross-bridge — label-only candidate, **Staphylococcus-specific**

### Biological processes and functions

- Peptidoglycan biosynthetic process — **`GO:0009252`**
- Peptidoglycan catabolic/remodeling process — use a verified GO term during implementation; label-only here
- Transpeptidation / peptidoglycan cross-linking — label-only unless the exact GO molecular-function term is checked
- Autolysis — label-only process candidate
- Alcohol/acetone decolorization — experimental-process node
- CV–I retention/extraction — assay-process nodes

### Genes, proteins, and complexes

- **MurA–MurF** cytoplasmic precursor pathway; MurF is a strong candidate upstream node
- **MraY** and **MurG**, lipid-linked precursor synthesis
- **MurJ**, lipid II flippase
- **SEDS glycosyltransferases** and **penicillin-binding proteins (PBPs)**, polymerization/cross-linking
- **FemX/FemA/FemB**, pentaglycine bridge assembly in *Staphylococcus aureus*; taxon-specific
- **Atl, LytN**, and other peptidoglycan hydrolases; taxon-specific examples
- **TagO** and downstream Tag enzymes, wall-teichoic-acid synthesis; architectural modifiers, not established universal Gram-retention determinants

For gene/protein nodes, use organism-qualified identifiers—e.g., UniProt, NCBIGene, KEGG Orthology, or EC—only after the graph’s taxonomic scope is fixed. A bare `murF` node across all bacteria risks collapsing non-orthologous context and does not establish a direct stain phenotype.

## 3. Candidate causal graph

The following compact edge set is suitable as a starting point for `gram_positive.yaml`.

| subject | predicate | object | confidence/scope | evidence DOI |
|---|---|---|---|---|
| crystal violet | enters | heat-fixed bacterial cell | High; core Gram-stain assay step (beveridge2014samplingandstaining pages 6-7, rohde2019thegrampositivebacterial pages 1-2) | 10.1128/9781555817497.ch2; 10.1128/microbiolspec.gpp3-0044-2018 |
| iodine | forms complex with | crystal violet | High; core Gram-stain assay step (beveridge2014samplingandstaining pages 6-7, rohde2019thegrampositivebacterial pages 1-2) | 10.1128/9781555817497.ch2; 10.1128/microbiolspec.gpp3-0044-2018 |
| crystal violet-iodine complex | is retained by | intact peptidoglycan-rich Gram-positive cell wall | High; core phenotype-defining mechanism (beveridge2014samplingandstaining pages 6-7, rohde2019thegrampositivebacterial pages 1-2) | 10.1128/9781555817497.ch2; 10.1128/microbiolspec.gpp3-0044-2018 |
| intact thick/cross-linked peptidoglycan | limits extraction of | crystal violet-iodine complex during ethanol/acetone decolorization | High; core assay mechanism (beveridge2014samplingandstaining pages 6-7, rohde2019thegrampositivebacterial pages 1-2, wang2024aclinicalbacterial pages 3-5) | 10.1128/9781555817497.ch2; 10.1128/microbiolspec.gpp3-0044-2018; 10.1038/s41597-024-03370-5 |
| retained crystal violet-iodine complex | causes | purple Gram-positive microscopy phenotype | High; defining readout (beveridge2014samplingandstaining pages 6-7, rohde2019thegrampositivebacterial pages 1-2) | 10.1128/9781555817497.ch2; 10.1128/microbiolspec.gpp3-0044-2018 |
| autolysis / peptidoglycan self-degradation | increases extraction of | crystal violet-iodine complex | High for damaged/aged cells; negative perturbation (beveridge2014samplingandstaining pages 6-7) | 10.1128/9781555817497.ch2 |
| lysozyme exposure | increases extraction of | crystal violet-iodine complex | High for perturbation experiments; negative perturbation (beveridge2014samplingandstaining pages 6-7) | 10.1128/9781555817497.ch2 |
| penicillin or other cell-wall damaging treatment | increases extraction of | crystal violet-iodine complex | High for perturbation experiments; negative perturbation (beveridge2014samplingandstaining pages 6-7) | 10.1128/9781555817497.ch2 |
| improper or incomplete decolorization | can cause | false Gram-positive appearance / Gram variability | High; assay-artifact edge (beveridge2014samplingandstaining pages 6-7, wang2024aclinicalbacterial pages 3-5) | 10.1128/9781555817497.ch2; 10.1038/s41597-024-03370-5 |
| Mur ligases (Mur pathway) | contribute to biosynthesis of | peptidoglycan precursor / peptidoglycan layer | Medium; upstream indirect envelope-biology edge, not stain-specific (rohde2019thegrampositivebacterial pages 1-2) | 10.1128/microbiolspec.gpp3-0044-2018 |
| penicillin-binding proteins (PBPs) | catalyze cross-linking of | peptidoglycan | Medium; upstream indirect envelope-biology edge (benedetti2021bacterialcellwall pages 5-7) | 10.1201/9781003099277-20 |
| Fem factors (FemX/FemA/FemB) | build | pentaglycine cross-bridges in peptidoglycan | Medium; taxon-specific indirect edge, especially Staphylococcus aureus (benedetti2021bacterialcellwall pages 5-7) | 10.1201/9781003099277-20 |
| peptidoglycan hydrolases / murein hydrolases | remodel or cleave | peptidoglycan | Medium; indirect edge that can weaken retention if excessive or misregulated (benedetti2021bacterialcellwall pages 5-7) | 10.1201/9781003099277-20 |
| wall teichoic acids / lipoteichoic acids | modify architecture of | Gram-positive cell wall | Medium-Low; indirect architectural modifier, not proven universal determinant of stain outcome (rohde2019thegrampositivebacterial pages 1-2, benedetti2021bacterialcellwall pages 5-7) | 10.1128/microbiolspec.gpp3-0044-2018; 10.1201/9781003099277-20 |
| thin peptidoglycan monoderm Bacillota | can cause | Gram-negative staining despite lack of diderm outer membrane | High; boundary-case edge separating stain phenotype from envelope architecture (choi2024deeplybranchingbacillota pages 1-2) | 10.1128/spectrum.00732-24 |


*Table: This table lists concise, curation-ready candidate causal edges for the Gram-positive trait graph, emphasizing the core assay mechanism, key perturbations, indirect upstream cell-wall biology, and important boundary cases.*

### Evidence snippets and curation notes

| Proposed triple | Supporting snippet | Interpretation |
|---|---|---|
| crystal violet — **enters** → fixed bacterial cell | “crystal violet molecules are small enough to penetrate the wall interstices” | Direct assay step; high confidence. (beveridge2014samplingandstaining pages 6-7) |
| iodine — **forms complex with** → crystal violet | Iodine acts as mordant and “forms an insoluble complex” | Direct chemical step; high confidence. (rohde2019thegrampositivebacterial pages 1-2) |
| intact peptidoglycan-rich wall — **prevents extraction of** → CV–I complex | “the dye-iodine complex is too large to exit”; the wall “prevents extraction of the complex” | Core mechanistic edge. The size-exclusion description is a useful operational model but should not be over-specified as the only molecular mechanism. (beveridge2014samplingandstaining pages 6-7) |
| retained CV–I complex — **causes** → purple microscopy phenotype | Gram-positive cells “retain the purple stain” after ethanol washing | Defining readout and strongest terminal edge. (beveridge2014samplingandstaining pages 6-7) |
| autolysis — **increases** → CV–I extraction | Compromised integrity “resulting from autolysis…allows extraction of the complex” | Direct negative perturbation; high confidence. (beveridge2014samplingandstaining pages 6-7) |
| lysozyme exposure — **increases** → CV–I extraction | Compromised integrity from “lysozyme exposure…allows extraction” | Direct experimental perturbation; high confidence. (beveridge2014samplingandstaining pages 6-7) |
| penicillin-mediated wall injury — **increases** → CV–I extraction | Wall-targeting antibiotics “like penicillin” permit complex extraction | Direct perturbation but antibiotic, dose, and growth-state dependent. (beveridge2014samplingandstaining pages 6-7) |
| PBPs — **cross-link** → peptidoglycan | The source describes “PBP-mediated transpeptidation”; *S. aureus* cross-linking is reported as **74–92%**, versus **30–60%** in *E. coli* | Valid envelope-biology edge; the subsequent link to staining remains indirect. (benedetti2021bacterialcellwall pages 5-7) |
| FemX/FemA/FemB — **assemble** → pentaglycine bridges | Fem factors assemble bridges “essential for cell integrity in *S. aureus*” | Curate only in a *Staphylococcus*-scoped subgraph; not a universal Gram-positive mechanism. (benedetti2021bacterialcellwall pages 5-7) |
| thin-peptidoglycan monoderm Bacillota — **can yield** → Gram-negative staining | Organisms “stain Gram-negative” while lacking genes for LPS and outer-membrane proteins | High-value boundary edge showing that stain class and membrane architecture are separable. (choi2024deeplybranchingbacillota pages 1-2) |
| incomplete decolorization — **can cause** → false purple appearance | Thick film can prevent complete decolorization; recent images show atypical purple Gram-negative bacteria | Experimental-confounder edge; do not treat as a biological cause of the target trait. (beveridge2014samplingandstaining pages 6-7, wang2024aclinicalbacterial pages 3-5) |

## 4. Current understanding and expert analysis

Authoritative cell-envelope reviews identify thick peptidoglycan, wall teichoic acids, and lipoteichoic acids as major features of canonical Gram-positive walls, while emphasizing continuous peptidoglycan synthesis and turnover. These features explain why wall integrity is central to staining, but they do **not** show that teichoic acid abundance alone is necessary or sufficient for CV–I retention. (rohde2019thegrampositivebacterial pages 1-2)

The most defensible graph is consequently layered:

1. **Envelope construction:** precursor synthesis and translocation → peptidoglycan polymerization and cross-linking.
2. **Wall state:** intact, sufficiently thick/organized, low-extractability envelope.
3. **Assay chemistry:** crystal violet + iodine → intracellular CV–I complex; decolorizer challenges retention.
4. **Readout:** retained complex → purple cell → `METPO:1000698`.
5. **Modifiers/confounders:** growth phase, autolysis, lysozyme, β-lactams, smear thickness, timing, and unusual envelope composition.

This layered model avoids the common but unsupported shortcut **“Gram-positive gene → Gram-positive phenotype.”** Most Mur enzymes and PBPs occur in both Gram-positive and Gram-negative bacteria; what matters for this trait is the resulting envelope state under assay conditions.

## 5. Recent developments and implementations, 2023–2024

### Conceptual revision of the Gram divide

Choi et al. (October 2024) examined 366 representative complete Bacillota genomes and found multiple deeply branching lineages with atypical Gram-negative staining despite apparently monoderm architecture. The authors interpret Gram reaction as informative about peptidoglycan thickness but insufficient to establish outer-membrane presence. This is the most directly relevant recent evidence for defining TraitMech boundaries. (choi2024deeplybranchingbacillota pages 1-2)

### Clinical microscopy and machine learning

Wang et al. (June 2024) released a clinical dataset of **1,705 Gram-stained respiratory-specimen images**, each **4,912 × 3,684 pixels**, totaling **18.7 GB**. It contains **11,824 bacterial annotations**: 3,371 Gram-negative cocci, 1,462 Gram-positive cocci, 5,799 Gram-negative bacilli, and 1,192 Gram-positive bacilli. YOLOv5 detection and U-Net segmentation benchmarks used a 7:2:1 train/validation/test split; reported mAP@0.5 exceeded **0.73** in validation and test sets. (wang2024aclinicalbacterial pages 2-3, wang2024aclinicalbacterial pages 3-5, wang2024aclinicalbacterial pages 5-6)

The implementation targets microbiological rapid on-site evaluation of bronchoalveolar lavage fluid and endotracheal aspirates, with potential use in recognizing infection or colonization and informing antibiotic selection. Importantly for curation, the study documents errors caused by atypical staining, background interference, bacterial shrinkage, blurred edges, and protocol variation; automated classification therefore predicts image labels, not necessarily the underlying envelope mechanism. (wang2024aclinicalbacterial pages 2-3, wang2024aclinicalbacterial pages 3-5, wang2024aclinicalbacterial pages 5-6)

## 6. Recommended minimal YAML graph

A conservative first implementation should contain approximately the following core relations:

1. crystal violet → **enters** → fixed bacterial cell
2. iodine → **complexes_with** → crystal violet
3. CV–I complex → **located_in** → fixed bacterial cell
4. intact thick/cross-linked peptidoglycan wall → **decreases** → CV–I extraction during decolorization
5. ethanol/acetone decolorization → **promotes** → CV–I extraction
6. reduced CV–I extraction → **increases** → CV–I retention
7. CV–I retention → **causes** → purple microscopic appearance
8. purple microscopic appearance → **realizes** → `METPO:1000698`
9. autolysis → **decreases** → wall integrity
10. lysozyme exposure → **decreases** → wall integrity
11. wall-active β-lactam treatment → **decreases** → wall integrity
12. incomplete decolorization → **causes** → false-positive purple appearance
13. thin peptidoglycan in atypical monoderm Bacillota → **can cause** → Gram-negative staining

Mur/PBP/Tag/autolysin branches should be added only with organism-specific evidence and an explicit distinction between **direct stain evidence** and **indirect envelope evidence**.

## 7. Claims not yet ready for TraitMech curation

- **Do not curate “monoderm → Gram positive” as universal.** It is contradicted by 2024 Bacillota evidence. (choi2024deeplybranchingbacillota pages 1-2)
- **Do not curate “thick peptidoglycan alone is sufficient.”** Cross-linking, permeability, fixation, physiological state, and protocol affect retention.
- **Do not make wall or lipoteichoic acid a required determinant.** They are major canonical wall constituents, but the retrieved evidence does not directly demonstrate that their loss abolishes Gram-positive staining. (rohde2019thegrampositivebacterial pages 1-2)
- **Do not make MurF, PBPs, Fem factors, or TagO direct causes without a mutant Gram-stain experiment.** Their roles in wall synthesis are strong, but gene-to-stain edges are currently inferred; Fem factors are especially taxon-specific. (benedetti2021bacterialcellwall pages 5-7)
- **Do not treat purple color as organism identity.** Incomplete decolorization and atypical cells produce false or mixed reactions. (beveridge2014samplingandstaining pages 6-7, wang2024aclinicalbacterial pages 3-5)
- **Do not conflate acid-fast organisms with ordinary Gram-positive cells.** Mycobacterial envelope chemistry requires separate representation. (rohde2019thegrampositivebacterial pages 1-2)
- **Do not curate AI classification performance as mechanistic evidence.** It supports application and assay variability, not causal wall biology. (wang2024aclinicalbacterial pages 2-3, wang2024aclinicalbacterial pages 5-6)

## DOI-first bibliography

1. Beveridge TJ, Lawrence JR, Murray RGE. **Sampling and Staining for Light Microscopy.** Published April 2014. DOI: [10.1128/9781555817497.ch2](https://doi.org/10.1128/9781555817497.ch2). (beveridge2014samplingandstaining pages 6-7)
2. Rohde M. **The Gram-Positive Bacterial Cell Wall.** *Microbiology Spectrum*. Published May 2019. DOI: [10.1128/microbiolspec.GPP3-0044-2018](https://doi.org/10.1128/microbiolspec.GPP3-0044-2018). (rohde2019thegrampositivebacterial pages 1-2)
3. Choi JK, Poudel S, Yee N, Goff JL. **Deeply branching Bacillota species exhibit atypical Gram-negative staining.** *Microbiology Spectrum*. Published October 2024. DOI: [10.1128/spectrum.00732-24](https://doi.org/10.1128/spectrum.00732-24). (choi2024deeplybranchingbacillota pages 1-2)
4. Wang X, et al. **A Clinical Bacterial Dataset for Deep Learning in Microbiological Rapid On-Site Evaluation.** *Scientific Data*. Published June 2024. DOI: [10.1038/s41597-024-03370-5](https://doi.org/10.1038/s41597-024-03370-5). (wang2024aclinicalbacterial pages 2-3, wang2024aclinicalbacterial pages 3-5, wang2024aclinicalbacterial pages 5-6)
5. De Benedetti S, Fisher J, Mobashery S. **Bacterial Cell Wall: Morphology and Biochemistry.** DOI: [10.1201/9781003099277-20](https://doi.org/10.1201/9781003099277-20). Used only for indirect peptidoglycan-cross-linking evidence. (benedetti2021bacterialcellwall pages 5-7)

**Overall curation judgment:** the existing `gram_positive_cell_wall_retention` graph is directionally correct. Its highest-confidence backbone should remain assay-centered. Expansion beyond the current 13 nodes/11 edges should prioritize explicit decolorization, wall-integrity perturbations, false-positive/Gram-variable branches, and the 2024 monoderm boundary case before adding broad gene-level modules.

References

1. (beveridge2014samplingandstaining pages 6-7): Terry J. Beveridge, John R. Lawrence, and Robert G. E. Murray. Sampling and staining for light microscopy. ArXiv, pages 19-33, Apr 2014. URL: https://doi.org/10.1128/9781555817497.ch2, doi:10.1128/9781555817497.ch2. This article has 327 citations.

2. (rohde2019thegrampositivebacterial pages 1-2): Manfred Rohde. The gram-positive bacterial cell wall. Microbiology Spectrum, May 2019. URL: https://doi.org/10.1128/microbiolspec.gpp3-0044-2018, doi:10.1128/microbiolspec.gpp3-0044-2018. This article has 425 citations and is from a domain leading peer-reviewed journal.

3. (choi2024deeplybranchingbacillota pages 1-2): Jessica K. Choi, Saroj Poudel, Nathan Yee, and Jennifer L. Goff. Deeply branching <i>bacillota</i> species exhibit atypical gram-negative staining. Oct 2024. URL: https://doi.org/10.1128/spectrum.00732-24, doi:10.1128/spectrum.00732-24. This article has 13 citations and is from a domain leading peer-reviewed journal.

4. (wang2024aclinicalbacterial pages 3-5): Xiuli Wang, Yinghan Shi, Shasha Guo, Xuzhong Qu, Fei Xie, Zhimei Duan, Ye Hu, Han Fu, Xin Shi, Tingwei Quan, Kaifei Wang, and Lixin Xie. A clinical bacterial dataset for deep learning in microbiological rapid on-site evaluation. Scientific Data, Jun 2024. URL: https://doi.org/10.1038/s41597-024-03370-5, doi:10.1038/s41597-024-03370-5. This article has 18 citations and is from a peer-reviewed journal.

5. (benedetti2021bacterialcellwall pages 5-7): Stefania De Benedetti, J. Fisher, and S. Mobashery. Bacterial cell wall: morphology and biochemistry. 2008. URL: https://doi.org/10.1201/9781003099277-20, doi:10.1201/9781003099277-20. This article has 13 citations.

6. (wang2024aclinicalbacterial pages 2-3): Xiuli Wang, Yinghan Shi, Shasha Guo, Xuzhong Qu, Fei Xie, Zhimei Duan, Ye Hu, Han Fu, Xin Shi, Tingwei Quan, Kaifei Wang, and Lixin Xie. A clinical bacterial dataset for deep learning in microbiological rapid on-site evaluation. Scientific Data, Jun 2024. URL: https://doi.org/10.1038/s41597-024-03370-5, doi:10.1038/s41597-024-03370-5. This article has 18 citations and is from a peer-reviewed journal.

7. (wang2024aclinicalbacterial pages 5-6): Xiuli Wang, Yinghan Shi, Shasha Guo, Xuzhong Qu, Fei Xie, Zhimei Duan, Ye Hu, Han Fu, Xin Shi, Tingwei Quan, Kaifei Wang, and Lixin Xie. A clinical bacterial dataset for deep learning in microbiological rapid on-site evaluation. Scientific Data, Jun 2024. URL: https://doi.org/10.1038/s41597-024-03370-5, doi:10.1038/s41597-024-03370-5. This article has 18 citations and is from a peer-reviewed journal.