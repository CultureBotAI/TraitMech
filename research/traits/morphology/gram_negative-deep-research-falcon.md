---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:35:08.864050'
end_time: '2026-08-04T08:45:44.014485'
duration_seconds: 635.15
template_file: templates/trait_causal_graph_research.md
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
  causal_graph_summary: 'gram_negative_outer_membrane_dye_loss: 17 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 58
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gram negative
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000699
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A gram stain in which bacteria do not retain crystal violet dye and appear pink or red after staining, indicating a thin peptidoglycan layer and presence of an outer membrane.
- **Parent traits:** METPO:1000697
- **Synonyms:** G_negative, negative
- **Existing evidence:** DOI:10.1038/s41579-019-0201-x: defining feature of the Gram-negative cell envelope (Supports the outer membrane as a defining Gram-negative envelope feature.) | PMID:27564552: Gram-Negative Bacterium Escherichia coli (Organism example: Escherichia coli is described as Gram-negative.)
- **Existing causal graph summary:** gram_negative_outer_membrane_dye_loss: 17 nodes, 12 edges

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
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000699
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A gram stain in which bacteria do not retain crystal violet dye and appear pink or red after staining, indicating a thin peptidoglycan layer and presence of an outer membrane.
- **Parent traits:** METPO:1000697
- **Synonyms:** G_negative, negative
- **Existing evidence:** DOI:10.1038/s41579-019-0201-x: defining feature of the Gram-negative cell envelope (Supports the outer membrane as a defining Gram-negative envelope feature.) | PMID:27564552: Gram-Negative Bacterium Escherichia coli (Organism example: Escherichia coli is described as Gram-negative.)
- **Existing causal graph summary:** gram_negative_outer_membrane_dye_loss: 17 nodes, 12 edges

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


# Curation report: Gram-negative trait

**Trait:** gram negative  
**Identifier:** `METPO:1000699`  
**Category / kind:** MORPHOLOGY / CLASS  
**Recommended interpretation:** an **assay-observed Gram-stain phenotype**, not a taxonomic clade and not an exact synonym of “diderm,” “outer-membrane-bearing,” or “LPS-producing.”

## 1. Scope summary

`METPO:1000699` should represent cells that fail to retain the crystal-violet–iodine primary stain after the decolorization step and consequently appear pink/red after counterstaining. The classical sequence is gentian/crystal violet, iodine, alcohol decolorization, and safranin counterstaining. Typical Gram-negative Proteobacteria have a thin peptidoglycan layer between inner and outer membranes; disruption of the outer membrane by decolorizer permits ready removal of the limited retained primary-dye complex. Safranin then supplies the observed pink/red endpoint. (megrian2020oneortwo pages 1-3, zerbib2025bacterialcellenvelopes pages 4-6)

The mechanistic graph should therefore distinguish:

1. **proximal assay mechanism:** staining → mordanting → envelope disruption/dehydration → primary-dye loss → counterstain uptake → pink/red observation;
2. **cell-envelope determinants:** relatively thin peptidoglycan, outer membrane, periplasm and envelope organization;
3. **upstream biogenesis machinery:** Lpt, BAM, Lol and related systems that construct a typical diderm envelope; and
4. **correlated consequences:** permeability, antimicrobial resistance and innate immune recognition, which are biologically important but do not themselves cause the Gram-stain readout.

### Boundary cases

The Gram reaction and membrane count correlate but are not equivalent. “Diderm” means two cellular membranes regardless of staining or membrane lipid composition. Some monoderm Firmicutes stain Gram-negative or Gram-variable, some diderms can stain Gram-positive, and diderms lacking LPS exist. Consequently, neither `outer membrane → gram negative` nor `LPS → gram negative` should be asserted as an exception-free universal rule. (megrian2020oneortwo pages 1-3, leonard2022wasthelast pages 1-2, zerbib2025bacterialcellenvelopes pages 4-6)

Other assay boundaries requiring explicit metadata include culture age, cell-envelope damage, fixation, decolorization time and reagent formulation. These can produce Gram-variable or false reactions and should be modeled as experimental modifiers unless directly supported for a specified organism and protocol.

## 2. Candidate nodes

### Trait and observed phenotype

- **gram negative:** `METPO:1000699`
- **parent trait:** `METPO:1000697`
- Primary-dye retention/loss — label-only candidate
- Pink/red Gram-stain appearance — label-only candidate
- Gram-variable staining — label-only candidate

### Cellular structures and localizations

- **Outer membrane:** `GO:0019867`
- **Periplasmic space:** `GO:0042597`
- **Peptidoglycan-based cell wall:** `GO:0009274`
- Inner/cytoplasmic membrane — use the verified organism-appropriate GO cellular-component term during implementation
- Outer-membrane outer leaflet — label-only candidate
- Outer-membrane inner leaflet — label-only candidate
- Diderm cell envelope — label-only candidate; do not equate automatically with the target trait

A typical diderm-LPS envelope has an asymmetric outer membrane—LPS in the surface leaflet and phospholipid in the periplasmic leaflet—with a thin but mechanically strong peptidoglycan layer in the periplasm. Reported peptidoglycan thicknesses include approximately 6 nm in *E. coli* and 2.4 nm in *Pseudomonas aeruginosa*; these are examples, not universal thresholds for Gram negativity. (zerbib2025bacterialcellenvelopes pages 4-6)

### Chemicals and assay factors

- Crystal violet — preferably ground to a verified ChEBI record at implementation
- Iodine / iodide mordant — verify exact chemical-form CURIE
- Crystal-violet–iodine complex — label-only candidate
- Ethanol — `CHEBI:16236`
- Acetone — `CHEBI:15347`
- Safranin counterstain — verify exact dye record; label-only if formulation is ambiguous
- Lipopolysaccharide — `CHEBI:16412`
- Lipid A — verify exact ChEBI class before YAML insertion
- Peptidoglycan — `CHEBI:8005`
- Phospholipid — `CHEBI:16247`
- Mg²⁺ — `CHEBI:18420`
- Ca²⁺ — `CHEBI:29108`
- Polymyxin B — verify exact ChEBI record
- 4-amino-4-deoxy-L-arabinose modification — label-only pending exact molecular grounding

### Complexes, pathways and proteins

- LPS biosynthesis module: Lpx/Kds enzymes — gene/protein nodes should be organism-specific
- MsbA LPS flippase — organism-specific protein/ABC transporter node
- **Lpt system:** LptB₂FGC–LptA–LptDE; label-level complex plus organism-specific protein nodes
- **BAM complex:** BamA and accessory BamB/C/D/E or phylum-specific alternatives
- **Lol pathway:** LolCDE, LolA and LolB where present
- **Mla/AsmA-like lipid-homeostasis systems:** include only with edge-specific evidence
- Braun’s lipoprotein Lpp — *E. coli*/Enterobacterales-scoped protein node
- Porins / β-barrel outer-membrane proteins — class node plus organism-specific proteins where needed
- Envelope-stress systems, including σE and taxon-specific two-component systems — label-level module unless individual regulators are directly evidenced
- PhoPQ–PmrD–PmrAB lipid-A-remodeling response — *Klebsiella*/Enterobacterales-scoped module
- Outer-membrane vesicles — `GO:0031909` may be considered after confirming ontology fit

### Processes and functions

- Gram staining — assay/process label
- Decolorization and counterstaining — assay-step labels
- LPS transport to outer membrane
- β-barrel outer-membrane-protein folding/insertion
- Lipoprotein trafficking to outer membrane
- Outer-membrane lipid asymmetry maintenance
- Envelope stress response/homeostasis
- Selective permeability and nutrient uptake
- Polymyxin-mediated outer-membrane disruption

## 3. Candidate causal edges

The following compact set captures the recommended priority edges.

| subject | predicate | object | confidence/scope | DOI |
|---|---|---|---|---|
| Gram staining decolorization step | disrupts | outer membrane | High; general Gram-negative staining mechanism in typical diderms (zerbib2025bacterialcellenvelopes pages 4-6) | 10.1007/978-3-319-26779-1_28-2 |
| Thin peptidoglycan layer protected by outer membrane | permits rapid loss of | crystal-violet–iodine dye complex during decolorization | High; typical Proteobacteria/diderm explanation, not universal to all taxa (zerbib2025bacterialcellenvelopes pages 4-6) | 10.1007/978-3-319-26779-1_28-2 |
| Loss of primary dye after decolorization | enables | pink/red counterstain outcome | Medium; operational assay logic from Gram-stain procedure and Gram-negative readout (megrian2020oneortwo pages 1-3) | 10.1111/mmi.14469 |
| LptB2FGCADE complex | transports | lipopolysaccharide to the outer membrane outer leaflet | High; conserved Gram-negative OM biogenesis pathway, mechanism best resolved in E. coli and related diderms (yoon2024structuralinsightsinto pages 1-3, lundstedt2020assemblyandmaintenance pages 1-2, okuda2016lipopolysaccharidetransportand pages 9-11) | 10.1007/s12275-024-00137-w |
| BAM complex | inserts/folds | β-barrel outer membrane proteins into outer membrane | High; conserved diderm pathway with phylum-level accessory variation (george2024atp‐independentassemblymachinery pages 1-2, smith2023teasingapartthe pages 1-2) | 10.1002/pro.4896 |
| Lol pathway (LolCDE–LolA–LolB or bifunctional LolA) | traffics | outer-membrane lipoproteins | High for pathway; final insertion step varies by taxon, so scope should be annotated (smith2023teasingapartthe pages 1-2) | 10.1073/pnas.2218473120 |
| Lpp (Braun’s lipoprotein) | covalently tethers | outer membrane to peptidoglycan | High; demonstrated in E. coli, taxon-specific and should not be universalized to all Gram-negatives (mathelieguinlet2020lipoproteinlppregulates pages 1-3) | 10.1038/s41467-020-15489-1 |
| Lipopolysaccharide-rich asymmetric outer membrane | confers | permeability barrier to toxic compounds and many antibiotics | High; defining feature of typical Gram-negative outer membrane (simpson2019pushingtheenvelope pages 1-2, lundstedt2020assemblyandmaintenance pages 1-2, bisht2024breakingbarriersexploiting pages 1-2) | 10.1038/s41579-019-0201-x |
| Outer-membrane porins | permit uptake of | nutrients/small molecules across outer membrane | High; typical diderm outer-membrane function (zerbib2025bacterialcellenvelopes pages 4-6, george2024atp‐independentassemblymachinery pages 1-2) | 10.1007/978-3-319-26779-1_28-2 |
| Lipid A modification (e.g., 4-amino-4-deoxy-L-arabinose addition) | increases resistance to | polymyxin | High; strong mechanistic support in Klebsiella/polymyxin literature, taxon and stress-condition dependent (hussein2023comparativeproteomicsof pages 1-2) | 10.1128/msphere.00537-22 |
| Envelope stress response systems | maintain/restore | outer-membrane integrity and homeostasis | High; broad Gram-negative review evidence, specific regulators vary by species (bisht2024breakingbarriersexploiting pages 1-2) | 10.3390/pathogens13100889 |


*Table: This table lists compact, high-priority candidate causal edges for curating the Gram-negative trait (METPO:1000699). It emphasizes mechanisms directly tied to staining phenotype and the diderm envelope systems most strongly supported by the retrieved literature.*

More detailed curation notes and supporting snippets follow.

| Subject | Predicate | Object | Supporting snippet | Reference | Curation note |
|---|---|---|---|---|---|
| Gram-stain decolorizer | disrupts | outer membrane | “the decoloring agent…disrupts the OM” | [Zerbib 2025](https://doi.org/10.1007/978-3-319-26779-1_28-2) | **Strong for the typical diderm mechanism**, but this is a 2025 secondary source summarizing earlier work. Represent ethanol/acetone formulation explicitly. (zerbib2025bacterialcellenvelopes pages 4-6) |
| Thin peptidoglycan plus outer-membrane organization | enables | easy removal of limited bound primary dye | Thin PG “binds only very few dye molecules which are easily removed” | [Zerbib 2025](https://doi.org/10.1007/978-3-319-26779-1_28-2) | Strong but simplified. Avoid making peptidoglycan thickness alone sufficient. (zerbib2025bacterialcellenvelopes pages 4-6) |
| Primary-dye complex loss | enables | safranin-determined pink appearance | Classical method ends with “counterstaining with safranin (pink color in gram-negative bacteria)” | [Megrian et al. 2020](https://doi.org/10.1111/mmi.14469) | Strong operational assay edge. Safranin uptake is not a unique Gram-negative biological capacity. (megrian2020oneortwo pages 1-3) |
| Lpx/Kds synthesis, MsbA flipping and Lpt transport | builds | classical LPS-containing outer membrane | Review lists “Lpx and Kds enzymes,” “MsbA,” and “transport to the OM (Lpt system)” | [Megrian et al. 2020](https://doi.org/10.1111/mmi.14469) | Curate as upstream envelope-biogenesis branches, not direct stain edges. Taxonomic architecture varies. (megrian2020oneortwo pages 1-3) |
| LptB₂FG | ATP-dependently extracts | mature LPS from inner membrane | LptB₂FG is described as the ABC transporter that extracts LPS using ATP | [Yoon & Song 2024](https://doi.org/10.1007/s12275-024-00137-w) | High confidence; best characterized in *E. coli*. (yoon2024structuralinsightsinto pages 1-3) |
| LptC/LptA bridge | transfers | LPS across periplasm | LPS passes from LptC to bridge protein LptA | [Yoon & Song 2024](https://doi.org/10.1007/s12275-024-00137-w) | High confidence for canonical Lpt systems. (yoon2024structuralinsightsinto pages 1-3) |
| LptDE | inserts | LPS into outer leaflet | LptDE “inserts LPS into the outer leaflet” | [Yoon & Song 2024](https://doi.org/10.1007/s12275-024-00137-w) | High confidence; essentiality differs, e.g. LPS can be non-essential in *Neisseria meningitidis*. (yoon2024structuralinsightsinto pages 1-3, okuda2016lipopolysaccharidetransportand pages 9-11) |
| LPS-rich asymmetric outer membrane | confers | permeability barrier | LPS surface layer contributes to “stringent permeability properties” and resistance to toxic compounds including antibiotics | [Simpson & Trent 2019](https://doi.org/10.1038/s41579-019-0201-x) | Strong envelope-function edge; **not a direct staining edge**. (simpson2019pushingtheenvelope pages 1-2) |
| BAM complex | folds and inserts | β-barrel outer-membrane proteins | BAM recognizes/folds β-barrels and executes membrane insertion without electrochemical energy | [George et al. 2024](https://doi.org/10.1002/pro.4896) | Strong diderm-envelope edge; accessory components vary across phyla. (george2024atp‐independentassemblymachinery pages 1-2) |
| LolCDE | extracts from inner membrane and transfers to | LolA-bound lipoproteins | LolCDE “extracts lipoproteins from the IM and delivers them to LolA” | [Smith et al. 2023](https://doi.org/10.1073/pnas.2218473120) | Strong for Proteobacteria; do not require LolB universally. (smith2023teasingapartthe pages 1-2) |
| LolA | carries through | aqueous periplasm | LolA shields hydrophobic acyl chains and delivers lipoproteins onward | [Smith et al. 2023](https://doi.org/10.1073/pnas.2218473120) | Strong; in *Caulobacter vibrioides*, LolA also performs LolB-like insertion. (smith2023teasingapartthe pages 1-2) |
| LolB or bifunctional LolA | inserts | lipoproteins into outer membrane | *C. vibrioides* LolA has both chaperone and insertion activities | [Smith et al. 2023](https://doi.org/10.1073/pnas.2218473120) | Taxon-dependent alternatives should be represented as separate edges. (smith2023teasingapartthe pages 1-2) |
| Lpp | covalently connects | outer membrane and peptidoglycan | Lpp provides the “only covalent crosslink” in *E. coli* | [Mathelié-Guinlet et al. 2020](https://doi.org/10.1038/s41467-020-15489-1) | High confidence but **strictly *E. coli*-scoped**. (mathelieguinlet2020lipoproteinlppregulates pages 1-3) |
| Lpp-mediated tethering | increases/controls | envelope stiffness and periplasm width | Lpp contributes by covalent connection and control of periplasmic width | [Mathelié-Guinlet et al. 2020](https://doi.org/10.1038/s41467-020-15489-1) | Strong organism-specific structural edge; indirect relative to staining. (mathelieguinlet2020lipoproteinlppregulates pages 1-3) |
| Porins | permit | selective small-solute/nutrient passage | OM restricts harmful substances while permitting nutrient uptake through porins | [Zerbib 2025](https://doi.org/10.1007/978-3-319-26779-1_28-2) | Use a general edge; the cited <700-Da statement is an approximation and should not be a universal cutoff. (zerbib2025bacterialcellenvelopes pages 4-6) |
| Envelope-stress responses | detect and repair | envelope damage | ESRs ensure assembly fidelity and “detect and repair envelope damage” | [Bisht et al. 2024](https://doi.org/10.3390/pathogens13100889) | Strong module-level relation; individual ESR circuitry is species-specific. (bisht2024breakingbarriersexploiting pages 1-2) |
| Polymyxin binding to lipid A | disrupts | outer-membrane permeability barrier | Polymyxin interacts with lipid A, inserts into the acyl layer, causes leakage and death | [Hussein et al. 2023](https://doi.org/10.1128/msphere.00537-22) | Strong for polymyxin-susceptible *K. pneumoniae*; an inhibitor/application branch, not core trait causation. (hussein2023comparativeproteomicsof pages 1-2) |
| L-Ara4N or phosphoethanolamine addition to lipid A | reduces susceptibility to | polymyxins | Resistance “primarily involves modification of lipid A” with these groups | [Hussein et al. 2023](https://doi.org/10.1128/msphere.00537-22) | Strong but taxon/condition-specific. (hussein2023comparativeproteomicsof pages 1-2) |
| Low Mg²⁺, low pH, high iron or cationic peptides | activates | PhoPQ–PmrD–PmrAB remodeling | These conditions activate regulatory systems controlling L-Ara4N addition | [Hussein et al. 2023](https://doi.org/10.1128/msphere.00537-22) | Curate only in a *K. pneumoniae*/supported-taxon context. (hussein2023comparativeproteomicsof pages 1-2) |

### Minimal recommended phenotype path

For `gram_negative_outer_membrane_dye_loss`, the most defensible core is:

1. thin periplasmic peptidoglycan + outer-membrane envelope organization;
2. crystal-violet staining;
3. iodine-mediated primary-dye complex formation;
4. ethanol/acetone decolorization;
5. outer-membrane disruption and limited retention of primary dye;
6. loss of the crystal-violet–iodine complex;
7. safranin counterstaining;
8. pink/red microscopic observation;
9. classification as `METPO:1000699`.

Lpt/BAM/Lol/Lpp should be attached as upstream explanatory branches with taxon qualifiers, not placed on a single mandatory path shared by every Gram-negative-staining bacterium.

## 4. Recent developments and applications

### Envelope biogenesis as an antibiotic target

Two 2024 reviews emphasize BAM and Lpt as high-value outer-membrane targets. BAM inserts β-barrel proteins without ATP or a transmembrane electrochemical energy source; darobactin selectively inhibits BamA. Lpt uses ATP-driven extraction and a trans-envelope bridge to move LPS. These mechanisms are promising because disrupting envelope assembly compromises bacterial survival and permeability. (yoon2024structuralinsightsinto pages 1-3, george2024atp‐independentassemblymachinery pages 1-2)

A July 2024 pipeline review reported 51 antibacterial candidates in phase 1/2 development at the end of 2022, compared with 34 in 2011. It also listed inhaled murepavadin, an LptD inhibitor for pseudomonal infection, and intravenous zosurabalpin, an LptB₂FGC inhibitor in phase 1 for *Acinetobacter baumannii*. These drug-development states are time-sensitive metadata and should not be encoded as timeless trait edges. (butler2024areviewof pages 3-4, butler2024areviewof pages 1-3)

### Revised understanding of Lol-pathway diversity

A 2023 PNAS study resolved why many Gram-negative taxa lack LolB: *C. vibrioides* LolA is bifunctional, combining periplasmic chaperone and outer-membrane insertion activities. This is an important warning against treating the *E. coli* LolCDE→LolA→LolB sequence as universal. (smith2023teasingapartthe pages 1-2)

### Rapid and stain-free classification

Single-cell Raman spectroscopy with machine learning classified seven common clinical pathogens; the reported SVM accuracy was 98.1% in the study’s small database. In the supplementary clinical-sample table, SVM overall accuracy was 0.959 across the shown *E. coli*, *K. pneumoniae* and *Enterococcus faecalis* samples. The authors identified peptidoglycan and teichoic-acid Raman peaks as important discriminatory features. This supports an **alternative diagnostic-classification application**, not a causal edge in the conventional Gram-stain graph. (hu2022stainfreegramstaining pages 1-2)

FTIR is also being applied to microbial identification, cell-wall analysis, biofilm examination, stress monitoring and environmental surveillance. A 2023 review identifies standardized spectral libraries, high-throughput/single-cell measurements and portable real-time monitoring as development priorities, while noting sample complexity and interpretation challenges. (kassem2023applicationsoffourier pages 1-2)

### Outer-membrane vesicles and resistance

A 2023 *K. pneumoniae* study compared a polymyxin-susceptible strain (MIC 0.5 mg/L) with an extremely resistant derivative (MIC ≥128 mg/L) after 2 mg/L polymyxin-B exposure. OMVs were described as approximately 20–200 nm particles that can carry resistance and repair factors and may act as polymyxin decoys. The study is compelling but organism- and treatment-specific; “OMVs cause Gram negativity” would be unsupported. (hussein2023comparativeproteomicsof pages 1-2)

### Clinical and public-health significance

A 2024 envelope review cites more than 1.25 million deaths linked to bacterial AMR in 2019 and discusses a projection of 10 million annual deaths by 2050 without intervention. The same source emphasizes that Gram-negative envelope permeability and envelope-stress responses contribute to intrinsic resistance. These burden estimates motivate research but are contextual statistics, not graph edges. (bisht2024breakingbarriersexploiting pages 1-2)

## 5. Expert synthesis

The strongest expert consensus is that the **outer membrane is a hallmark of the typical Gram-negative envelope**, but modern envelope biology prefers the structural terms **monoderm** and **diderm** because staining and architecture are not perfectly congruent. The typical Gram-negative phenotype emerges from the entire envelope’s behavior during a specific assay, not from a single “Gram-negative gene.” (simpson2019pushingtheenvelope pages 1-2, megrian2020oneortwo pages 1-3, zerbib2025bacterialcellenvelopes pages 4-6)

For TraitMech, the graph should consequently use a layered model:

- **direct phenotype edges:** reagents, envelope disruption, dye retention/loss and observed color;
- **architecture edges:** membrane count, PG localization/thickness and OM composition;
- **biogenesis edges:** Lpt/BAM/Lol and taxon-specific tethers or homeostasis systems;
- **consequence/application edges:** permeability, antibiotic action, immune recognition and diagnostics.

This design avoids converting common textbook correlations into universal causal assertions.

## 6. Claims not yet suitable for unqualified curation

1. **“All Gram-negative organisms have LPS.”** False as a universal statement; some diderms lack LPS, and the relationship between diderm architecture and Gram reaction has exceptions. (zerbib2025bacterialcellenvelopes pages 4-6)
2. **“All diderms stain Gram-negative.”** Do not curate without qualification. Staining and membrane architecture can disagree. (megrian2020oneortwo pages 1-3, zerbib2025bacterialcellenvelopes pages 4-6)
3. **“Thin peptidoglycan alone causes Gram negativity.”** Too reductive. Decolorizer chemistry, outer-membrane behavior and protocol conditions are also involved.
4. **“Lpt/BAM/Lol are direct causes of pink staining.”** These systems build the envelope and are upstream contributors; direct evidence generally concerns envelope biogenesis, not stain color.
5. **Universal *E. coli* machinery composition.** LolB is absent from many species; BAM accessory subunits vary; Lpp’s unique covalent tethering is specifically demonstrated in *E. coli*. (mathelieguinlet2020lipoproteinlppregulates pages 1-3, george2024atp‐independentassemblymachinery pages 1-2, smith2023teasingapartthe pages 1-2)
6. **Universal porin cutoff of 700 Da.** Treat as an approximate example; permeability depends on porin identity, solute chemistry and organism. (zerbib2025bacterialcellenvelopes pages 4-6)
7. **AMR as part of the trait definition.** Gram-negative envelopes often contribute to intrinsic resistance, but resistance is not required for the staining phenotype.
8. **Gram reaction inferred solely from genome content.** Genome-based envelope predictions require phenotypic validation, especially for atypical taxa and incomplete assemblies. (leonard2022wasthelast pages 1-2)
9. **OMVs or lipid-A remodeling as core stain causes.** These are useful application/resistance branches only.
10. **Unverified CURIEs.** Exact identifiers for dye formulations, protein complexes, lipid-A variants and organism-specific proteins should be validated against the target ontology release rather than guessed.

## 7. DOI-first bibliography

- Yoon Y, Song S. **Structural Insights into the Lipopolysaccharide Transport (Lpt) System as a Novel Antibiotic Target.** *Journal of Microbiology*. Published May 2024. https://doi.org/10.1007/s12275-024-00137-w (yoon2024structuralinsightsinto pages 1-3)
- George A, Patil AG, Mahalakshmi R. **ATP-independent assembly machinery of bacterial outer membranes: BAM complex structure and function set the stage for next-generation therapeutics.** *Protein Science*. Published 2024; accepted December 31, 2023. https://doi.org/10.1002/pro.4896 (george2024atp‐independentassemblymachinery pages 1-2)
- Bisht R, Charlesworth PD, Sperandeo P, Polissi A. **Breaking Barriers: Exploiting Envelope Biogenesis and Stress Responses to Develop Novel Antimicrobial Strategies in Gram-Negative Bacteria.** *Pathogens*. Published October 11, 2024. https://doi.org/10.3390/pathogens13100889 (bisht2024breakingbarriersexploiting pages 1-2)
- Butler MS et al. **A Review of Antibacterial Candidates with New Modes of Action.** *ACS Infectious Diseases*. Published July 17, 2024. https://doi.org/10.1021/acsinfecdis.4c00218 (butler2024areviewof pages 3-4, butler2024areviewof pages 1-3)
- Smith HC, May KL, Grabowicz M. **Teasing apart the evolution of lipoprotein trafficking in gram-negative bacteria reveals a bifunctional LolA.** *PNAS*. Published January 30, 2023. https://doi.org/10.1073/pnas.2218473120 (smith2023teasingapartthe pages 1-2)
- Hussein M et al. **Comparative Proteomics of Outer Membrane Vesicles from Polymyxin-Susceptible and Extremely Drug-Resistant Klebsiella pneumoniae.** *mSphere*. Published January 9, 2023. https://doi.org/10.1128/msphere.00537-22 (hussein2023comparativeproteomicsof pages 1-2)
- Kassem A et al. **Applications of Fourier Transform-Infrared spectroscopy in microbial cell biology and environmental microbiology.** *Frontiers in Microbiology*. Published November 21, 2023. https://doi.org/10.3389/fmicb.2023.1304081 (kassem2023applicationsoffourier pages 1-2)
- Hu H et al. **Stain-free Gram staining classification of pathogens via single-cell Raman spectroscopy combined with machine learning.** *Analytical Methods*. Published October 2022. https://doi.org/10.1039/D2AY01056A (hu2022stainfreegramstaining pages 1-2)
- Léonard RR et al. **Was the Last Bacterial Common Ancestor a Monoderm after All?** *Genes*. Published February 18, 2022. https://doi.org/10.3390/genes13020376 (leonard2022wasthelast pages 1-2)
- Valvano MA. **Remodelling of the Gram-negative bacterial Kdo₂-lipid A and its functional implications.** *Microbiology*. Published April 2022. https://doi.org/10.1099/mic.0.001159 (valvano2022remodellingofthe pages 1-3)
- Lundstedt E, Kahne D, Ruiz N. **Assembly and Maintenance of Lipids at the Bacterial Outer Membrane.** *Chemical Reviews*. Published September 2020. https://doi.org/10.1021/acs.chemrev.0c00587 (lundstedt2020assemblyandmaintenance pages 1-2, lundstedt2020assemblyandmaintenance pages 3-4)
- Megrian D et al. **One or two membranes? Diderm Firmicutes challenge the Gram-positive/Gram-negative divide.** *Molecular Microbiology*. Published 2020. https://doi.org/10.1111/mmi.14469 (megrian2020oneortwo pages 1-3)
- Mathelié-Guinlet M et al. **Lipoprotein Lpp regulates the mechanical properties of the E. coli cell envelope.** *Nature Communications*. Published April 2020. https://doi.org/10.1038/s41467-020-15489-1 (mathelieguinlet2020lipoproteinlppregulates pages 1-3)
- Simpson BW, Trent MS. **Pushing the envelope: LPS modifications and their consequences.** *Nature Reviews Microbiology*. Published May 2019. https://doi.org/10.1038/s41579-019-0201-x (simpson2019pushingtheenvelope pages 1-2)
- Okuda S et al. **Lipopolysaccharide transport and assembly at the outer membrane: the PEZ model.** *Nature Reviews Microbiology*. Published March 2016. https://doi.org/10.1038/nrmicro.2016.25 (okuda2016lipopolysaccharidetransportand pages 9-11)

**Recommended curation decision:** retain the current trait definition, but make the graph’s terminal phenotype explicitly assay-based. Curate the decolorization/dye-loss/counterstain chain as the core mechanism, and attach canonical diderm-envelope biogenesis as qualified upstream branches rather than necessary-and-sufficient universal determinants.

References

1. (megrian2020oneortwo pages 1-3): Daniela Megrian, Najwa Taib, Jerzy Witwinowski, Christophe Beloin, and Simonetta Gribaldo. One or two membranes? diderm firmicutes challenge the gram‐positive/gram‐negative divide. Molecular Microbiology, 113:659-671, Mar 2020. URL: https://doi.org/10.1111/mmi.14469, doi:10.1111/mmi.14469. This article has 140 citations and is from a domain leading peer-reviewed journal.

2. (zerbib2025bacterialcellenvelopes pages 4-6): Didier Zerbib. Bacterial cell envelopes from monoderms to diderms: composition, architecture, and origin. Handbook of Electroporation, pages 1-27, Jan 2025. URL: https://doi.org/10.1007/978-3-319-26779-1\_28-2, doi:10.1007/978-3-319-26779-1\_28-2. This article has 1 citations.

3. (leonard2022wasthelast pages 1-2): Raphaël R. Léonard, Eric Sauvage, Valérian Lupo, Amandine Perrin, Damien Sirjacobs, Paulette Charlier, Frédéric Kerff, and Denis Baurain. Was the last bacterial common ancestor a monoderm after all? Genes, 13:376, Feb 2022. URL: https://doi.org/10.3390/genes13020376, doi:10.3390/genes13020376. This article has 21 citations.

4. (yoon2024structuralinsightsinto pages 1-3): Yurim Yoon and Saemee Song. Structural insights into the lipopolysaccharide transport (lpt) system as a novel antibiotic target. Journal of microbiology, 62:261-275, May 2024. URL: https://doi.org/10.1007/s12275-024-00137-w, doi:10.1007/s12275-024-00137-w. This article has 14 citations and is from a peer-reviewed journal.

5. (lundstedt2020assemblyandmaintenance pages 1-2): Emily Lundstedt, Daniel Kahne, and Natividad Ruiz. Assembly and maintenance of lipids at the bacterial outer membrane. Chemical reviews, 121:5098-5123, Sep 2020. URL: https://doi.org/10.1021/acs.chemrev.0c00587, doi:10.1021/acs.chemrev.0c00587. This article has 182 citations and is from a highest quality peer-reviewed journal.

6. (okuda2016lipopolysaccharidetransportand pages 9-11): Suguru Okuda, David J. Sherman, Thomas J. Silhavy, Natividad Ruiz, and Daniel Kahne. Lipopolysaccharide transport and assembly at the outer membrane: the pez model. Nature Reviews Microbiology, 14:337-345, Mar 2016. URL: https://doi.org/10.1038/nrmicro.2016.25, doi:10.1038/nrmicro.2016.25. This article has 481 citations and is from a highest quality peer-reviewed journal.

7. (george2024atp‐independentassemblymachinery pages 1-2): Anjana George, Akanksha Gajanan Patil, and Radhakrishnan Mahalakshmi. Atp‐independent assembly machinery of bacterial outer membranes: bam complex structure and function set the stage for next‐generation therapeutics. Protein Science, Jan 2024. URL: https://doi.org/10.1002/pro.4896, doi:10.1002/pro.4896. This article has 16 citations and is from a peer-reviewed journal.

8. (smith2023teasingapartthe pages 1-2): Hannah C. Smith, Kerrie L. May, and Marcin Grabowicz. Teasing apart the evolution of lipoprotein trafficking in gram-negative bacteria reveals a bifunctional lola. Proceedings of the National Academy of Sciences of the United States of America, Jan 2023. URL: https://doi.org/10.1073/pnas.2218473120, doi:10.1073/pnas.2218473120. This article has 30 citations and is from a highest quality peer-reviewed journal.

9. (mathelieguinlet2020lipoproteinlppregulates pages 1-3): Marion Mathelié-Guinlet, Abir T. Asmar, Jean-François Collet, and Yves F. Dufrêne. Lipoprotein lpp regulates the mechanical properties of the e. coli cell envelope. Nature Communications, Apr 2020. URL: https://doi.org/10.1038/s41467-020-15489-1, doi:10.1038/s41467-020-15489-1. This article has 192 citations and is from a highest quality peer-reviewed journal.

10. (simpson2019pushingtheenvelope pages 1-2): Brent W. Simpson and M. Stephen Trent. Pushing the envelope: lps modifications and their consequences. Nature Reviews Microbiology, 17:403-416, May 2019. URL: https://doi.org/10.1038/s41579-019-0201-x, doi:10.1038/s41579-019-0201-x. This article has 600 citations and is from a highest quality peer-reviewed journal.

11. (bisht2024breakingbarriersexploiting pages 1-2): Renu Bisht, Pierre D. Charlesworth, Paola Sperandeo, and Alessandra Polissi. Breaking barriers: exploiting envelope biogenesis and stress responses to develop novel antimicrobial strategies in gram-negative bacteria. Pathogens, 13:889, Oct 2024. URL: https://doi.org/10.3390/pathogens13100889, doi:10.3390/pathogens13100889. This article has 15 citations.

12. (hussein2023comparativeproteomicsof pages 1-2): Maytham Hussein, Raad Jasim, Hakan Gocol, Mark Baker, Varsha J. Thombare, James Ziogas, Aayush Purohit, Gauri G. Rao, Jian Li, and Tony Velkov. Comparative proteomics of outer membrane vesicles from polymyxin-susceptible and extremely drug-resistant klebsiella pneumoniae. mSphere, Feb 2023. URL: https://doi.org/10.1128/msphere.00537-22, doi:10.1128/msphere.00537-22. This article has 36 citations and is from a peer-reviewed journal.

13. (butler2024areviewof pages 3-4): Mark S. Butler, Waldemar Vollmer, Emily C. A. Goodall, Robert J. Capon, Ian R. Henderson, and Mark A. T. Blaskovich. A review of antibacterial candidates with new modes of action. ACS Infectious Diseases, 10:3440-3474, Jul 2024. URL: https://doi.org/10.1021/acsinfecdis.4c00218, doi:10.1021/acsinfecdis.4c00218. This article has 112 citations and is from a peer-reviewed journal.

14. (butler2024areviewof pages 1-3): Mark S. Butler, Waldemar Vollmer, Emily C. A. Goodall, Robert J. Capon, Ian R. Henderson, and Mark A. T. Blaskovich. A review of antibacterial candidates with new modes of action. ACS Infectious Diseases, 10:3440-3474, Jul 2024. URL: https://doi.org/10.1021/acsinfecdis.4c00218, doi:10.1021/acsinfecdis.4c00218. This article has 112 citations and is from a peer-reviewed journal.

15. (hu2022stainfreegramstaining pages 1-2): Huijie Hu, Jingkai Wang, Xiaofei Yi, Kaicheng Lin, Siyu Meng, Xin Zhang, Chenyu Jiang, Yuguo Tang, Minggui Wang, Jianxing He, Xiaogang Xu, and Yizhi Song. Stain-free gram staining classification of pathogens via single-cell raman spectroscopy combined with machine learning. Analytical methods : advancing methods and applications, 14:4014-4020, Oct 2022. URL: https://doi.org/10.1039/d2ay01056a, doi:10.1039/d2ay01056a. This article has 19 citations.

16. (kassem2023applicationsoffourier pages 1-2): Amin Kassem, Lana Abbas, Oliver Coutinho, Somie Opara, Hawraa Najaf, Diana Kasperek, Keshav Pokhrel, Xiaohua Li, and Sonia Tiquia-Arashiro. Applications of fourier transform-infrared spectroscopy in microbial cell biology and environmental microbiology: advances, challenges, and future perspectives. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1304081, doi:10.3389/fmicb.2023.1304081. This article has 349 citations and is from a peer-reviewed journal.

17. (valvano2022remodellingofthe pages 1-3): Miguel A. Valvano. Remodelling of the gram-negative bacterial kdo2-lipid a and its functional implications. Apr 2022. URL: https://doi.org/10.1099/mic.0.001159, doi:10.1099/mic.0.001159. This article has 25 citations and is from a peer-reviewed journal.

18. (lundstedt2020assemblyandmaintenance pages 3-4): Emily Lundstedt, Daniel Kahne, and Natividad Ruiz. Assembly and maintenance of lipids at the bacterial outer membrane. Chemical reviews, 121:5098-5123, Sep 2020. URL: https://doi.org/10.1021/acs.chemrev.0c00587, doi:10.1021/acs.chemrev.0c00587. This article has 182 citations and is from a highest quality peer-reviewed journal.