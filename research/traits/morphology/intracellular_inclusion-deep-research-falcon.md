---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:16:19.910984'
end_time: '2026-06-18T08:48:41.110037'
duration_seconds: 1941.2
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: intracellular inclusion
  trait_identifier: traitmech:000066
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: intracellular_inclusion
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A morphology trait describing a discrete intracellular body \u2014\
    \ a storage granule, gas-filled structure, or protein-bounded microcompartment/organelle\
    \ \u2014 that compartmentalizes material or function within a prokaryotic cell."
  parent_traits: METPO:1000059
  synonyms: cytoplasmic inclusion
  evidence_summary: 'DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow, "Formation
    and function of bacterial organelles", establish that bacteria contain diverse
    inclusions/organelles (storage granules, gas vesicles, microcompartments, magnetosomes);
    parent of the inclusion sub-variants.) | DOI:10.1038/nrmicro.2018.10:  (Kerfeld
    et al. review bacterial microcompartments as a major class of protein-bounded
    intracellular organelles.)'
  causal_graph_summary: 'inclusion_compartmentalization: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** intracellular inclusion
- **METPO identifier:** traitmech:000066
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait describing a discrete intracellular body — a storage granule, gas-filled structure, or protein-bounded microcompartment/organelle — that compartmentalizes material or function within a prokaryotic cell.
- **Parent traits:** METPO:1000059
- **Synonyms:** cytoplasmic inclusion
- **Existing evidence:** DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow, "Formation and function of bacterial organelles", establish that bacteria contain diverse inclusions/organelles (storage granules, gas vesicles, microcompartments, magnetosomes); parent of the inclusion sub-variants.) | DOI:10.1038/nrmicro.2018.10:  (Kerfeld et al. review bacterial microcompartments as a major class of protein-bounded intracellular organelles.)
- **Existing causal graph summary:** inclusion_compartmentalization: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **intracellular inclusion** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/intracellular_inclusion.yaml`.

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
- **Trait label:** intracellular inclusion
- **METPO identifier:** traitmech:000066
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait describing a discrete intracellular body — a storage granule, gas-filled structure, or protein-bounded microcompartment/organelle — that compartmentalizes material or function within a prokaryotic cell.
- **Parent traits:** METPO:1000059
- **Synonyms:** cytoplasmic inclusion
- **Existing evidence:** DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow, "Formation and function of bacterial organelles", establish that bacteria contain diverse inclusions/organelles (storage granules, gas vesicles, microcompartments, magnetosomes); parent of the inclusion sub-variants.) | DOI:10.1038/nrmicro.2018.10:  (Kerfeld et al. review bacterial microcompartments as a major class of protein-bounded intracellular organelles.)
- **Existing causal graph summary:** inclusion_compartmentalization: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **intracellular inclusion** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/intracellular_inclusion.yaml`.

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


# Intracellular inclusion (traitmech:000066) — Curation-focused Research Report (2024–2025 evidence)

## Scope summary (TraitMech/METPO alignment)

**Trait label:** intracellular inclusion (syn. cytoplasmic inclusion) describes the **presence of a discrete intracellular body** inside a prokaryotic cell that compartmentalizes **material (storage/biomineral/redox intermediate)** or **function (metabolic reactions)**. Evidence in the retrieved corpus supports treating this trait as an umbrella over multiple mechanistically distinct inclusion subclasses:

1. **Protein-bounded organelles**
   * **Bacterial microcompartments (BMCs, incl. carboxysomes):** protein shells that encapsulate pathway segments and form a selectively permeable barrier between cargo enzymes and the cytosol. (doron2024bacterialmicrocompartmentsas pages 1-3)
   * **Gas vesicles (GVs):** gene-encoded gas-filled protein nanoparticles/organelles enabling buoyancy, built mainly from GvpA and reinforced by GvpC. (feng2024advancesinthe pages 1-2, feng2024advancesinthe pages 2-4)

2. **Polymeric storage granules (non-membrane bounded, protein-coated interfaces)**
   * **PHA granules:** intracellular inclusion bodies formed by synthesized PHA chains; granule surfaces are largely coated by phasin (PhaP) and can be anchored to the nucleoid by PhaM (in Cupriavidus necator). (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
   * **Glycogen granules:** storage form of glucose; glycogen is a branched α-1,4/α-1,6 homopolysaccharide. (but2024newsolutionsin pages 1-2)
   * **Polyphosphate (polyP) / volutin granules:** metachromatic intracellular inclusions containing polyP (linear phosphate polymer) often enriched in Mg2+/Ca2+; synthesis by Ppk and degradation by Ppx. (corrales2025polyphosphatefromlactic pages 1-2)

3. **Membrane-bounded biomineral organelles**
   * **Magnetosomes:** bacterial organelles containing magnetite/greigite crystals; genes for assembly and biomineralization are encoded on magnetosome gene clusters/MAI and include mam/mms families. (paulus2024mamflikeproteinsare pages 1-2, martinez2024enhancingmagnetosomebiomanufacturing pages 29-32)

4. **Chemically stored redox intermediates**
   * **Sulfur globules (SGBs):** intracellular elemental sulfur (S0) intermediates formed during sulfide oxidation en route to sulfate. (nezio2024synergisticphenotypicadaptations pages 1-2)

### Boundary cases / nearby traits
* **Not all intracellular structures qualify:** diffuse phase-separated condensates or general crowding-driven foci are not “discrete intracellular bodies” unless they form a morphologically delimited inclusion detectable as a body. (No direct condensate-specific evidence in retrieved 2024–2025 corpus.)
* **Trait vs. function:** “intracellular inclusion” is primarily **morphological** (presence/absence, size/number) rather than a direct assay of metabolism; however, many inclusions are **diagnostic for underlying pathways** (e.g., pha genes → PHA granules; gvp genes → gas vesicles). (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4, feng2024advancesinthe pages 1-2)

## Current understanding: key concepts and definitions (evidence-backed)

### Protein-bounded compartments
* **BMC definition:** BMCs are protein-based prokaryotic organelles that “encapsulate a segment of a metabolic pathway within a selectively permeable protein shell” separating enzymatic core from cytosol. (doron2024bacterialmicrocompartmentsas pages 1-3)
* **BMC shell building blocks:** core shell protein types are BMC-H (hexamers), BMC-T (pseudohexameric trimers) and BMC-P (pentamers), and enzymes are targeted into the lumen largely via **15–20 aa encapsulation peptides (EPs)**. (doron2024bacterialmicrocompartmentsas pages 3-5)
* **Carboxysome definition (BMC subclass):** carboxysomes partition Rubisco and carbonic anhydrase within a proteinaceous shell to create a favorable microenvironment for enhanced carbon fixation. (trettel2024modelingbacterialmicrocompartment pages 1-2)

### Storage granules
* **PHA granules:** “Synthesized PHA chains form intracellular inclusion bodies commonly called PHA granules,” with surfaces “largely coated” by PhaP; PhaM can anchor granules to the nucleoid and influence granule number. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
* **Glycogen:** “Glycogen is a branched homopolysaccharide of α-1,4-linked glucose subunits with α-1,6-linked glucose at the branching points.” (but2024newsolutionsin pages 1-2)
* **PolyP granules:** polyP relates to “metachromatic inclusions (volutin granules),” which are amorphous and enriched in Mg2+/Ca2+. (corrales2025polyphosphatefromlactic pages 1-2)

### Biomineral inclusions
* **Magnetosome organization:** magnetosome chains create a cellular dipole for geomagnetic navigation; a magnetosome cytoskeletal network (“magnetoskeleton”) involves MamJ/MamK/MamY organizing ~30 magnetosomes in a linear chain (Magnetospirillum gryphiswaldense context). (paulus2024mamflikeproteinsare pages 1-2)

### Redox-intermediate inclusions
* **Sulfur globules:** in purple sulfur bacteria, sulfide is oxidized to sulfate “through an intermediate accumulation of elemental sulfur (S0) within the cell in the form of sulfur globules (SGBs).” (nezio2024synergisticphenotypicadaptations pages 1-2)

## Recent developments and latest research (prioritizing 2023–2024)

### 1) Gas vesicle assembly moves from “parts list” toward interaction networks (2024)
A key 2024 advance is **systematic mapping of protein–protein interactions** in a GV operon to resolve assembly logic. Iburg et al. (EMBO J, 2024) note GV operons typically have ~10 genes with many “assembly factors” of undefined role, and use a high-throughput NanoBit assay to probe interactions across an 11-gene cassette, explicitly to enable rational engineering for biomedical applications. (iburg2024elucidatingtheassembly pages 1-2, iburg2024elucidatingtheassembly pages 2-4, iburg2024elucidatingtheassembly pages 4-5)

### 2) High-resolution GV structure and quantitative physical constraints consolidated for bioengineering (2024)
Feng et al. (J Biol Eng, 2024) synthesize structural and physical properties relevant to engineering: GVs are typically **0.045–0.2 μm wide and 0.1–2 μm long**, with shells “only one or two peptide layers thick,” primarily GvpA plus strengthening GvpC, and species-dependent **collapse pressures ~0.09–1 MPa**; width inversely correlates with strength, consistent with selection on buoyancy vs. robustness. (feng2024advancesinthe pages 1-2, feng2024advancesinthe pages 2-4)

### 3) Magnetosome biogenesis: discovery of a prokaryotic organelle-specific protein targeting component (Nature Communications 2024)
Paulus et al. (Nat Commun, 2024) demonstrate **MamF-like proteins (MamF/MmsF/MmxF)** are essential for magnetosome chain formation and magnetotaxis, and function in organelle-specific targeting of membrane proteins. Deletion of all MFPs (ΔF3) severely disrupts chains and yields smaller crystals; quantitative proteomics shows depletion of key structural/biomineralization factors including **MamJ (44-fold↓)** and MamD/Mms5. (paulus2024mamflikeproteinsare pages 2-3, paulus2024mamflikeproteinsare pages 1-2)

Visual evidence supporting these phenotypes (TEM + proteomics) is available from the retrieved figure panels. (paulus2024mamflikeproteinsare media 113fa52e, paulus2024mamflikeproteinsare media 0de12e88)

### 4) BMCs as modular “metabolic engineering chassis” (Biochem Soc Trans 2024)
Doron & Kerfeld (2024) emphasize that BMC shells are modular and that EP-based targeting is a general mechanism that enables creation of **empty shells** and **heterologous cargo loading**, supporting applications such as ethanol/hydrogen production and pathway insulation to avoid toxic intermediates. (doron2024bacterialmicrocompartmentsas pages 3-5, doron2024bacterialmicrocompartmentsas pages 1-3)

### 5) Storage granules: quantitative phenotypes and regulation tied to industrial and ecological use (2024)
* **Halomonas sp. CUBES01 (AEM 2024):** intracellular polyester granules (PHB) were detected by fluorescence microscopy/Nile red; the strain accumulated up to **~60% dry wt/wt PHB** depending on substrate, and authors highlight halophile-specific implementation benefits (non-axenic cultivation, osmolysis-based release). (woo2024isolationandcharacterization pages 1-2)
* **Methylococcus capsulatus MIR (Fermentation 2024):** nitrogen limitation promotes glycogen storage; deletion of both glycogen synthases yields a major reduction of glycogen (10.8 mg/g DCW vs 187.5 mg/g DCW in WT) and increases protein fraction in biomass (71% vs 54% DCW), relevant to single-cell protein production. (but2024newsolutionsin pages 1-2)

## Current applications and real-world implementations

### A) Bioplastics and bioprocessing using inclusion granules
* **Non-axenic, halophile-enabled PHB production:** Halomonas sp. CUBES01 combines rapid growth, halophily/alkaliphily and intracellular polyester granules; the study argues osmolyte-based salt tolerance and non-axenic cultivation can reduce sterilization burdens and downstream processing costs, and reports **up to ~60% PHB of biomass** (dry wt/wt) with multiple renewable feedstocks. (woo2024isolationandcharacterization pages 1-2)
* **Benchmark industrial-grade PHB accumulation:** the same study cites Halomonas bluephagenesis reaching **84% PHB CDW (WT)** and **94% (engineered)**, illustrating what inclusion-granule optimization can achieve in practice. (woo2024isolationandcharacterization pages 2-6)

### B) Gas vesicles as genetically encoded reporters/contrast agents
GVs are being implemented as **ultrasound/MRI/optical reporters, delivery carriers, and immune boosters** due to stability, small size, and biocompatibility; this is a major translation direction for a naturally occurring inclusion. (feng2024advancesinthe pages 1-2, feng2024advancesinthe pages 9-10)

### C) BMCs/carboxysomes as metabolic engineering modules
BMC engineering is positioned as a practical strategy to confine difficult catabolic pathways and reduce intermediate loss/toxicity; Doron & Kerfeld list engineered examples (e.g., ethanol/hydrogen, glycerol-to-propanediol, formate-to-pyruvate), reflecting increasing real-world synthetic biology uptake. (doron2024bacterialmicrocompartmentsas pages 1-3)

### D) Magnetosome-based nanomaterials (emerging)
The strongest 2024 primary evidence in this corpus concerns **core biogenesis**, but application-oriented reviews indicate ongoing nanomedicine interest (e.g., MRI contrast, drug delivery) while acknowledging scale-up and stability challenges; the key curation-relevant point is the mechanistic dependence on mam/mms gene systems and iron/suboxic conditions. (martinez2024enhancingmagnetosomebiomanufacturing pages 29-32, yadav2025therapeuticinnovationsin pages 9-11)

## Expert opinions / analysis from authoritative sources (within retrieved corpus)

* Doron & Kerfeld (2024) emphasize that **self-assembling, easy-to-modify protein shells** provide “nature’s solution” to confine pathways and can be engineered to address typical limitations of heterologous production (toxicity, promiscuity, intermediate loss). (doron2024bacterialmicrocompartmentsas pages 1-3)
* Iburg et al. (2024) explicitly frame the field need: while some GV proteins (GvpA/GvpC) have defined roles, “most other GV operon genes… are implicated as assembly factors with largely undefined roles,” motivating systematic interaction mapping as a prerequisite for rational design. (iburg2024elucidatingtheassembly pages 1-2)
* Paulus et al. (2024) argue their findings “redefine molecular roles” of MamF-like proteins and support the broader conclusion that **organelle-specific targeting systems exist in bacterial organelle formation**, conceptually paralleling eukaryotic translocation systems. (paulus2024mamflikeproteinsare pages 2-3, paulus2024mamflikeproteinsare pages 1-2)

## Statistics and quantitative data from recent studies (examples for curation)

* **Glycogen content (M. capsulatus MIR):** WT 187.5 mg/g DCW vs ΔglgA1ΔglgA2 10.8 mg/g DCW; protein fraction 54% vs 71% DCW, respectively. (but2024newsolutionsin pages 1-2)
* **PHB storage (Halomonas sp. CUBES01):** up to ~60% biomass (dry wt/wt) as PHB. (woo2024isolationandcharacterization pages 1-2)
* **PHB benchmarks (H. bluephagenesis):** 84% CDW (WT) and 94% CDW (engineered). (woo2024isolationandcharacterization pages 2-6)
* **Gas vesicle dimensions:** 0.045–0.2 μm wide; 0.1–2 μm long. (feng2024advancesinthe pages 1-2)
* **Gas vesicle collapse pressure:** ~0.09–1 MPa (species-dependent). (feng2024advancesinthe pages 2-4)
* **Magnetosome proteomics effect sizes (ΔF3):** MamJ 44-fold depletion; MamY 6-fold depletion; MamD 84-fold depletion; Mms5 12-fold depletion. (paulus2024mamflikeproteinsare pages 2-3)

## Candidate nodes (grouped by type)

| Node Label | Node Type | Suggested Ontology Grounding | Notes/Examples |
|---|---|---|---|
| Polyhydroxyalkanoate (PHA) granule | Structure | GO:0043654 | Subclass: Polymer storage granules bounded by phasins; stores carbon/energy (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4). |
| Glycogen granule | Structure | GO:0043655 | Subclass: Granules storing branched alpha-1,4/alpha-1,6 glucose chains (saito2024regulatoryroleof pages 1-2, but2024newsolutionsin pages 1-2). |
| Polyphosphate/volutin granule | Structure | GO:0043656 | Subclass: Amorphous Pi storage, often complexed with Mg2+/Ca2+ (corrales2025polyphosphatefromlactic pages 1-2). |
| Gas vesicle | Structure | GO:0031411 | Subclass: Gas-filled protein nanostructure providing cellular buoyancy (feng2024advancesinthe pages 1-2, feng2024advancesinthe pages 2-4). |
| Bacterial microcompartment (BMC) / Carboxysome | Structure | GO:0031472 / GO:0031471 | Subclass: Protein-bounded organelle providing selective permeability for metabolism (doron2024bacterialmicrocompartmentsas pages 1-3). |
| Magnetosome | Structure | GO:0043219 | Subclass: Membrane-bounded biomineral inclusion for magneto-aerotaxis (paulus2024mamflikeproteinsare pages 1-2, martinez2024enhancingmagnetosomebiomanufacturing pages 29-32). |
| Sulfur globule | Structure | unmapped | Subclass: Elemental sulfur (S0) accumulation formed during sulfide oxidation (nezio2024synergisticphenotypicadaptations pages 2-3, nezio2024synergisticphenotypicadaptations pages 1-2). |
| phaA, phaB, phaC | Gene/Protein | unmapped | Core enzymes for PHA biosynthesis; PhaC is the PHA synthase (woo2024isolationandcharacterization pages 2-6, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4). |
| phaP, phaR, phaM, phaZ | Gene/Protein | unmapped | Phasin (coats PHA granule), regulator, nucleoid anchor, and depolymerase (woo2024isolationandcharacterization pages 2-6, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4). |
| glgA, glgB, glgC, glgP, glgX | Gene/Protein | unmapped | Glycogen synthase, branching enzyme, ADP-glucose pyrophosphorylase, phosphorylase, debranching enzyme (saito2024regulatoryroleof pages 1-2, but2024newsolutionsin pages 1-2). |
| gvpA, gvpC and accessory gvp | Gene/Protein | unmapped | Major shell protein, outer scaffolding protein, and assembly factors of gas vesicles (feng2024advancesinthe pages 1-2, feng2024advancesinthe pages 2-4). |
| BMC-H, BMC-T, BMC-P | Gene/Protein | Pfam:PF00936, Pfam:PF03319 | Hexameric, trimeric, and pentameric structural proteins of BMC shells (doron2024bacterialmicrocompartmentsas pages 1-3, doron2024bacterialmicrocompartmentsas pages 3-5). |
| Encapsulation peptides | Protein | unmapped | 15-20 aa sequences that target enzymes to the BMC interior (doron2024bacterialmicrocompartmentsas pages 1-3, doron2024bacterialmicrocompartmentsas pages 3-5). |
| MamF, MmsF, MmxF | Gene/Protein | unmapped | Tic20 homologs required for organelle-specific protein targeting to the magnetosome membrane (paulus2024mamflikeproteinsare pages 2-3, paulus2024mamflikeproteinsare pages 1-2). |
| MamJ, MamK, MamY | Gene/Protein | unmapped | Magnetoskeleton components responsible for magnetosome chain assembly and positioning (paulus2024mamflikeproteinsare pages 2-3, yadav2025therapeuticinnovationsin pages 9-11). |
| MamB, MamM, Mms6 | Gene/Protein | unmapped | Involved in iron transport, nucleation, and regulation of crystal size/shape (martinez2024enhancingmagnetosomebiomanufacturing pages 29-32, yadav2025therapeuticinnovationsin pages 9-11). |
| Dsr system | Pathway | KEGG:M00596 | Dissimilatory sulfite reductase system required for oxidation of stored sulfur globules (kushkevych2024anoxygenicphotosynthesiswith pages 18-18). |
| Nitrogen limitation | Environment | unmapped | Trigger for glycogen and PHA accumulation by shifting metabolism from growth to storage (saito2024regulatoryroleof pages 1-2, but2024newsolutionsin pages 1-2). |
| High C/N ratio | Environment | unmapped | Nutritional imbalance promoting rapid PHA/PHB synthesis (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4). |
| Phosphate availability | Environment | unmapped | Modulates polyP dynamics and can influence competing PHA production (altamiraalgarra2024bioplasticproductionby pages 20-22, corrales2025polyphosphatefromlactic pages 13-15). |
| Salinity / osmolarity | Environment | ENVO:01000281 | High salt triggers osmoprotective responses, enhancing PHB production in halophiles (woo2024isolationandcharacterization pages 2-6). |
| Sulfide availability | Environment | CHEBI:16385 | Abundant substrate driving elemental sulfur globule formation in PSB/GSB (nezio2024synergisticphenotypicadaptations pages 2-3, nezio2024synergisticphenotypicadaptations pages 1-2). |
| Light, anoxia, euxinia | Environment | unmapped | Conducive conditions for phototrophic sulfur bacteria development and SGB formation (nezio2024synergisticphenotypicadaptations pages 2-3). |
| Suboxic O2 | Environment | unmapped | Preferred condition targeted via magneto-aerotaxis by magnetotactic bacteria (martinez2024enhancingmagnetosomebiomanufacturing pages 29-32). |
| Iron availability | Environment | CHEBI:29033 | Critical raw material for magnetosome biomineralization; MTB concentrate Fe from surroundings (yadav2025therapeuticinnovationsin pages 9-11, yadav2025therapeuticinnovationsin pages 7-9). |
| TEM | Assay | OBI:0000258 | Transmission electron microscopy used to visualize inclusion boundaries and magnetosome chains (altamiraalgarra2024bioplasticproductionby pages 20-22, paulus2024mamflikeproteinsare pages 2-3, paulus2024mamflikeproteinsare media 113fa52e). |
| Nile red / Nile blue staining | Assay | unmapped | Lipophilic fluorescent dyes for detecting and quantifying PHA/PHB granules (woo2024isolationandcharacterization pages 2-6, altamiraalgarra2024bioplasticproductionby pages 20-22). |
| Fluorescence microscopy | Assay | OBI:0002505 | Imaging technique for observing stained inclusions or fluorescently tagged target proteins (woo2024isolationandcharacterization pages 2-6). |
| qMNA | Assay | unmapped | Quantitative magnetosome neighbor analysis for evaluating chain integrity (paulus2024mamflikeproteinsare pages 3-5). |
| Proteomics / Volcano plot | Assay | OBI:0000615 | Used to determine severe depletion of structural targets like MamJ/MamD in mutants (paulus2024mamflikeproteinsare pages 2-3, paulus2024mamflikeproteinsare media 113fa52e). |
| Ultrasound / MRI contrast | Application | unmapped | Repurposing gas vesicles as acoustic/magnetic reporters in medical imaging (feng2024advancesinthe pages 1-2, feng2024advancesinthe pages 9-10). |
| Metabolic engineering | Application | unmapped | Utilizing BMCs, encapsulins, and PHAs for nanoreactors or bioplastic production (doron2024bacterialmicrocompartmentsas pages 1-3). |


*Table: A structured table of candidate nodes representing types, components, and triggers of diverse prokaryotic intracellular inclusions.*

## Candidate causal edges (evidence-backed triples)

| Subject | Predicate | Object | Evidence snippet | Reference | Notes/uncertainty |
|---|---|---|---|---|---|
| PhaA/PhaB/PhaC pathway | produces | PHA granule | “Synthesized PHA chains form intracellular inclusion bodies commonly called PHA granules” | 10.3390/molecules29102293 / https://doi.org/10.3390/molecules29102293 (2024) (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4) | Broad review statement; storage-granule subclass. |
| PhaP (phasin) | coats surface of | PHA granule | “Granules are largely coated by an amphiphilic protein phasin (PhaP)” | 10.3390/molecules29102293 / https://doi.org/10.3390/molecules29102293 (2024) (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4) | Strong mechanistic support for granule boundary. |
| PhaM | anchors | PHA granule to nucleoid | “In Cupriavidus necator, PhaM anchors granules to the nucleoid” | 10.3390/molecules29102293 / https://doi.org/10.3390/molecules29102293 (2024) (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4) | Taxon-specific to C. necator. |
| high C/N ratio | increases accumulation of | PHA granule | “Environmental and cultivation triggers for accumulation include high C/N ratio” | 10.3390/molecules29102293 / https://doi.org/10.3390/molecules29102293 (2024) (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4) | Review-level causal summary. |
| nitrogen depletion | increases accumulation of | PHA granule | “Environmental and cultivation triggers for accumulation include… depletion of N, S, P” | 10.3390/molecules29102293 / https://doi.org/10.3390/molecules29102293 (2024) (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4) | Broad, not species-specific. |
| Halomonas sp. CUBES01 | accumulates up to | PHB at ~60% dry wt/wt biomass | “Depending on the substrate, the strain accumulated up to ~60% of its biomass (dry wt/wt) in poly(3-hydroxybutyrate)” | 10.1128/aem.00603-24 / https://doi.org/10.1128/aem.00603-24 (2024) (woo2024isolationandcharacterization pages 1-2) | Strain-specific quantitative phenotype. |
| Halomonas bluephagenesis wild type | accumulates up to | PHB at 84% CDW | “the wild type accumulates as much as 84% (wt/wt) of its cell dry weight (CDW) in PHB” | 10.1128/aem.00603-24 / https://doi.org/10.1128/aem.00603-24 (2024) (woo2024isolationandcharacterization pages 2-6) | Comparative benchmark, not CUBES01 itself. |
| metabolic engineering of H. bluephagenesis | increases | PHB to 94% CDW | “driven up to 94% (wt/wt) through metabolic engineering” | 10.1128/aem.00603-24 / https://doi.org/10.1128/aem.00603-24 (2024) (woo2024isolationandcharacterization pages 2-6) | Engineered phenotype; application-oriented. |
| high salinity/osmolarity | increases | PHB production | “enhanced salt tolerance in microbes can lead to increased PHB production” | 10.1128/aem.00603-24 / https://doi.org/10.1128/aem.00603-24 (2024) (woo2024isolationandcharacterization pages 2-6) | Inference from halophile physiology; moderate certainty. |
| glycogen | stores | carbon and energy | “strain MIR stores carbon and energy in the form of glycogen” | 10.3390/fermentation10050265 / https://doi.org/10.3390/fermentation10050265 (2024) (but2024newsolutionsin pages 1-2) | Direct definition of storage-granule function. |
| nitrogen limitation | increases | glycogen accumulation | “stores carbon and energy in the form of glycogen, particularly when grown under nitrogen-limiting conditions” | 10.3390/fermentation10050265 / https://doi.org/10.3390/fermentation10050265 (2024) (but2024newsolutionsin pages 1-2) | Strong, strain-specific for Methylococcus capsulatus MIR. |
| GlgA + GlgB + GlgC | enable synthesis of | glycogen granule | “glycogen synthase (GlgA) and branching enzyme (GlgB)” and “dependence on ADP glucose pyrophosphorylase (GlgC)” | 10.3390/fermentation10050265 / https://doi.org/10.3390/fermentation10050265 (2024) (but2024newsolutionsin pages 1-2) | Aggregated pathway edge from explicit enzyme functions. |
| ΔglgA1ΔglgA2 mutant | decreases | glycogen content to 10.8 mg/g DCW | “10.8 mg/g DCW compared to 187.5 mg/g DCW in wild-type strain” | 10.3390/fermentation10050265 / https://doi.org/10.3390/fermentation10050265 (2024) (but2024newsolutionsin pages 1-2) | Strong quantitative mutant phenotype. |
| wild-type M. capsulatus MIR | contains | glycogen at 187.5 mg/g DCW | “187.5 mg/g DCW in wild-type strain” | 10.3390/fermentation10050265 / https://doi.org/10.3390/fermentation10050265 (2024) (but2024newsolutionsin pages 1-2) | Quantitative reference state for glycogen-rich cells. |
| ADP-glucose | activates/represses via GgaR | glycogen accumulation program | “YegW… senses ADPG as an effector” and “repressed glycogen accumulation” | 10.3390/microorganisms12010115 / https://doi.org/10.3390/microorganisms12010115 (2024) (saito2024regulatoryroleof pages 1-2) | Regulatory edge; E. coli-specific. |
| polyphosphate kinase (Ppk) | synthesizes | polyphosphate granule/polyP | “polyP synthesis is catalyzed by polyphosphate kinase (Ppk)” | 10.3390/foods14132211 / https://doi.org/10.3390/foods14132211 (2025) (corrales2025polyphosphatefromlactic pages 1-2) | Recent but 2025; still authoritative. |
| exopolyphosphatase (Ppx) | degrades | polyphosphate | “degraded by exopolyphosphatases (Ppx)” | 10.3390/foods14132211 / https://doi.org/10.3390/foods14132211 (2025) (corrales2025polyphosphatefromlactic pages 1-2) | Strong enzymatic edge. |
| polyphosphate | forms | volutin/metachromatic granules | “metachromatic inclusions (volutin granules)” | 10.3390/foods14132211 / https://doi.org/10.3390/foods14132211 (2025) (corrales2025polyphosphatefromlactic pages 1-2) | Historical/structural synonym support. |
| high inorganic phosphate (Pi) | increases | polyP accumulation | “high inorganic phosphate (Pi) increases accumulation” | 10.3390/foods14132211 / https://doi.org/10.3390/foods14132211 (2025) (corrales2025polyphosphatefromlactic pages 13-15) | LAB-focused but mechanistically plausible more broadly. |
| gas vesicle gene cluster | encodes | gas vesicle organelle | “gene-encoded, inert, hollow, gas-filled protein nanoparticles” | 10.1186/s13036-024-00426-3 / https://doi.org/10.1186/s13036-024-00426-3 (2024) (feng2024advancesinthe pages 1-2) | Direct definitional edge. |
| GvpA | forms shell of | gas vesicle | “shell composed primarily of GvpA” | 10.1186/s13036-024-00426-3 / https://doi.org/10.1186/s13036-024-00426-3 (2024) (feng2024advancesinthe pages 1-2) | Core structural component. |
| GvpC | strengthens | gas vesicle shell | “GvpC binds the α2 spiral and forms an outer cage to strengthen the shell” | 10.1186/s13036-024-00426-3 / https://doi.org/10.1186/s13036-024-00426-3 (2024) (feng2024advancesinthe pages 2-4) | Strong structural role. |
| gas vesicle shell | permits diffusion of | gas but excludes liquid water | “The shell is permeable to gases but excludes liquid water” | 10.1186/s13036-024-00426-3 / https://doi.org/10.1186/s13036-024-00426-3 (2024) (feng2024advancesinthe pages 1-2) | Defines functional permeability. |
| gas vesicle | enables | buoyancy | “enabling buoyancy for microbes” | 10.1186/s13036-024-00426-3 / https://doi.org/10.1186/s13036-024-00426-3 (2024) (feng2024advancesinthe pages 1-2) | Core phenotype/function edge. |
| gas vesicle | has width | 0.045–0.2 μm | “0.045–0.2 μm wide” | 10.1186/s13036-024-00426-3 / https://doi.org/10.1186/s13036-024-00426-3 (2024) (feng2024advancesinthe pages 1-2) | Quantitative morphology; not a causal edge but curation-useful phenotype fact. |
| gas vesicle | has length | 0.1–2 μm | “0.1–2 μm long” | 10.1186/s13036-024-00426-3 / https://doi.org/10.1186/s13036-024-00426-3 (2024) (feng2024advancesinthe pages 1-2) | Quantitative morphology. |
| gas vesicle collapse pressure | ranges by species from | ~0.09 MPa to 1 MPa | “critical collapse pressures reported from ~0.09 MPa to 1 MPa” | 10.1186/s13036-024-00426-3 / https://doi.org/10.1186/s13036-024-00426-3 (2024) (feng2024advancesinthe pages 2-4) | Physical-property edge; species-dependent. |
| GV operon | contains about | 10–11 genes | “most other GV operon genes (typically ~10 genes per operon)” and “11-gene cassette” | 10.1038/s44318-024-00178-2 / https://doi.org/10.1038/s44318-024-00178-2 (2024) (iburg2024elucidatingtheassembly pages 1-2, iburg2024elucidatingtheassembly pages 2-4) | Two supporting contexts; operon composition varies by taxon. |
| bacterial microcompartment shell | encapsulates | metabolic enzymes/pathway segment | “encapsulate a segment of a metabolic pathway within a selectively permeable protein shell” | 10.1042/bst20230229 / https://doi.org/10.1042/bst20230229 (2024) (doron2024bacterialmicrocompartmentsas pages 1-3) | Direct definition of BMC inclusion. |
| BMC-H/BMC-T/BMC-P proteins | assemble into | BMC shell | “three core shell protein types: BMC-H, BMC-T and BMC-P” | 10.1042/bst20230229 / https://doi.org/10.1042/bst20230229 (2024) (doron2024bacterialmicrocompartmentsas pages 3-5) | Strong structural edge. |
| encapsulation peptide (EP) | targets cargo into | BMC lumen | “Cargo targeting into the lumen is mediated mainly by 15–20 aa encapsulation peptides (EPs)” | 10.1042/bst20230229 / https://doi.org/10.1042/bst20230229 (2024) (doron2024bacterialmicrocompartmentsas pages 3-5) | Quantified sequence-length fact included. |
| carboxysome shell | partitions | Rubisco and carbonic anhydrase microenvironment | “partitions Rubisco and carbonic anhydrase to create a favorable microenvironment for enhanced carbon fixation” | 10.3389/fpls.2024.1346759 / https://doi.org/10.3389/fpls.2024.1346759 (2024) (trettel2024modelingbacterialmicrocompartment pages 1-2) | Carboxysome-specific BMC edge. |
| magnetosome island (MAI) | encodes | ~30 mam/mms genes | “a genomic magnetosome island (MAI) of ~30 mam/mms genes” | thesis cited in 2024 evidence summary (2024) (martinez2024enhancingmagnetosomebiomanufacturing pages 29-32) | Thesis source; useful but lower authority than primary paper. |
| mamAB operon | is sufficient for | rudimentary biomineralization | “mamAB alone is sufficient for rudimentary biomineralization” | thesis cited in 2024 evidence summary (2024) (martinez2024enhancingmagnetosomebiomanufacturing pages 29-32) | Thesis-derived summary; curate with caution. |
| MamF-like proteins | are required for | magnetosome biogenesis/positioning/biomineralization | “required for correct magnetosome biogenesis, positioning, biomineralization, and magnetic navigation” | 10.1038/s41467-024-55121-0 / https://doi.org/10.1038/s41467-024-55121-0 (2024) (paulus2024mamflikeproteinsare pages 1-2) | Strong primary evidence. |
| ΔF3 (mamF-like triple deletion) | depletes | MamJ by 44-fold in MM proteome | “MamJ (44-fold↓)” | 10.1038/s41467-024-55121-0 / https://doi.org/10.1038/s41467-024-55121-0 (2024) (paulus2024mamflikeproteinsare pages 2-3) | Quantitative mutant effect; assay-specific to proteomics. |
| MamJ/MamK/MamY magnetoskeleton | arranges | magnetosome chain | “MamJ, MamK and MamY… arranges approximately 30 magnetosomes into a linear chain” | 10.1038/s41467-024-55121-0 / https://doi.org/10.1038/s41467-024-55121-0 (2024) (paulus2024mamflikeproteinsare pages 1-2) | Strong chain-organization edge; approximate count included. |
| MamB/MamM | mediate | iron transport into magnetosome vesicle | “MamB and MamM are putative iron transporters” | 10.2147/IJN.S462031 / https://doi.org/10.2147/IJN.S462031 (2025) (yadav2025therapeuticinnovationsin pages 7-9) | 2025 review; still useful, but secondary. |
| sulfide oxidation | forms | intracellular sulfur globules (S0) | “oxidized to sulfate (SO42-) through an intermediate accumulation of elemental sulfur (S0) within the cell in the form of sulfur globules (SGBs)” | 10.1371/journal.pone.0310265 / https://doi.org/10.1371/journal.pone.0310265 (2024) (nezio2024synergisticphenotypicadaptations pages 1-2) | Direct definition of sulfur-globule inclusion. |
| reduced sulfur availability | changes number/size of | sulfur globules | “SGB number and size vary with environmental availability of reduced sulfur” | 10.1371/journal.pone.0310265 / https://doi.org/10.1371/journal.pone.0310265 (2024) (nezio2024synergisticphenotypicadaptations pages 2-3) | Environmental dependence; phenotypic, no genes named. |
| light + anoxic/euxinic conditions | favor development of | sulfur-globule-forming PSB | “PSB development occurs under anoxic, light-exposed (euxinic) conditions” | 10.1371/journal.pone.0310265 / https://doi.org/10.1371/journal.pone.0310265 (2024) (nezio2024synergisticphenotypicadaptations pages 2-3) | Ecological trigger; community/taxon-specific. |
| Dsr system | oxidizes/mobilizes | stored sulfur globules | “sulfur globule oxidation requires the dissimilatory sulfite reductase (Dsr) system” | 10.3389/fmicb.2024.1417714 / https://doi.org/10.3389/fmicb.2024.1417714 (2024) (kushkevych2024anoxygenicphotosynthesiswith pages 18-18) | Mechanistic but based on cited prior work within review. |


*Table: This table compiles curation-ready subject–predicate–object triples for the intracellular inclusion trait across major prokaryotic inclusion subclasses. It emphasizes direct evidence, quantitative facts, and curation notes about taxon specificity or evidence strength.*

## Ontology grounding notes (CURIE suggestions)

The following groundings are supported by commonly used ontologies and were included where unambiguous:
* **BMC / carboxysome:** GO:0031472 (bacterial microcompartment), GO:0031471 (carboxysome). (doron2024bacterialmicrocompartmentsas pages 1-3, trettel2024modelingbacterialmicrocompartment pages 1-2)
* **Gas vesicle:** GO:0031411. (feng2024advancesinthe pages 1-2)
* **Magnetosome:** GO:0043219. (paulus2024mamflikeproteinsare pages 1-2)
* **Storage granules:** GO:0043654 (PHA granule), GO:0043655 (glycogen granule), GO:0043656 (polyphosphate granule) as candidate GO structure terms (presented as suggestions in node artifact). (artifact-00)

For most individual genes/proteins (pha*, glg*, gvp*, mam/mms) stable identifiers should be grounded at curation time using:
* **UniProt accessions** per organism, or
* **KEGG orthology (KO)** / **MetaCyc** reactions for core enzymes (e.g., PhaC, GlgC, Ppk), because gene symbols alone are not globally unique.

## Warnings / claims to curate cautiously

1. **PolyP evidence is 2025 in this retrieved corpus:** polyP synthesis/degradation (Ppk/Ppx) and volutin inclusion properties are well established, but the most directly cited review here is 2025 (Foods). Curate as supported but consider adding a 2023–2024 primary/review source if required for strict recency. (corrales2025polyphosphatefromlactic pages 1-2)
2. **Magnetosome island gene-count and stepwise model from a thesis:** the ~30-gene MAI framing and step breakdown are consistent with broader literature but here are provided via a 2024 thesis summary; prioritize primary articles for these specific claims if strict evidence hierarchy is needed. (martinez2024enhancingmagnetosomebiomanufacturing pages 29-32)
3. **Sulfur globule molecular mechanism is sparse in retrieved 2024 primary text:** the PSB study provides strong phenotypic/definition edges, but explicit genes/enzymes for globule formation are limited; only Dsr system involvement in globule oxidation is supported in the available excerpted review text. Additional dedicated sulfur globule mechanistic sources are recommended before curating detailed gene-level edges beyond Dsr. (nezio2024synergisticphenotypicadaptations pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 18-18)
4. **Some engineering-oriented sources are preprints:** e.g., cyanobacteria-rich microbiome PHB production is bioRxiv; quantitative PHB %dcw (24% at day 105) is useful but should be flagged as non-peer-reviewed in curation. (altamiraalgarra2024bioplasticproductionby pages 20-22)

## DOI-first bibliography (with dates/URLs)

**Bacterial microcompartments / carboxysomes**
* Doron L, Kerfeld CA. *Bacterial microcompartments as a next-generation metabolic engineering tool…* Biochemical Society Transactions. **2024-05**. DOI: 10.1042/bst20230229. https://doi.org/10.1042/bst20230229 (doron2024bacterialmicrocompartmentsas pages 1-3, doron2024bacterialmicrocompartmentsas pages 3-5)
* Trettel DS et al. *Modeling bacterial microcompartment architectures for enhanced cyanobacterial carbon fixation.* Frontiers in Plant Science. **2024-02**. DOI: 10.3389/fpls.2024.1346759. https://doi.org/10.3389/fpls.2024.1346759 (trettel2024modelingbacterialmicrocompartment pages 1-2)

**Gas vesicles**
* Feng R et al. *Advances in the application of gas vesicles in medical imaging and disease treatment.* Journal of Biological Engineering. **2024-07**. DOI: 10.1186/s13036-024-00426-3. https://doi.org/10.1186/s13036-024-00426-3 (feng2024advancesinthe pages 1-2, feng2024advancesinthe pages 2-4, feng2024advancesinthe pages 9-10)
* Iburg M et al. *Elucidating the assembly of gas vesicles by systematic protein-protein interaction analysis.* The EMBO Journal. **2024-07**. DOI: 10.1038/s44318-024-00178-2. https://doi.org/10.1038/s44318-024-00178-2 (iburg2024elucidatingtheassembly pages 1-2, iburg2024elucidatingtheassembly pages 2-4, iburg2024elucidatingtheassembly pages 4-5)

**Magnetosomes**
* Paulus A et al. *MamF-like proteins are distant Tic20 homologs involved in organelle assembly in bacteria.* Nature Communications. **2024-12**. DOI: 10.1038/s41467-024-55121-0. https://doi.org/10.1038/s41467-024-55121-0 (paulus2024mamflikeproteinsare pages 2-3, paulus2024mamflikeproteinsare pages 1-2, paulus2024mamflikeproteinsare media 113fa52e, paulus2024mamflikeproteinsare media 0de12e88)

**Storage granules: PHA/PHB**
* Fukala I, Kučera I. *Natural Polyhydroxyalkanoates—An Overview of Bacterial Production Methods.* Molecules. **2024-05**. DOI: 10.3390/molecules29102293. https://doi.org/10.3390/molecules29102293 (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
* Woo S-G et al. *Isolation and characterization of a Halomonas species… production of bio-polyesters…* Applied and Environmental Microbiology. **2024-08**. DOI: 10.1128/aem.00603-24. https://doi.org/10.1128/aem.00603-24 (woo2024isolationandcharacterization pages 2-6, woo2024isolationandcharacterization pages 1-2)

**Storage granules: glycogen**
* But SY et al. *New Solutions in Single-Cell Protein Production from Methane: Construction of Glycogen-Deficient Mutants of Methylococcus capsulatus MIR.* Fermentation. **2024-05**. DOI: 10.3390/fermentation10050265. https://doi.org/10.3390/fermentation10050265 (but2024newsolutionsin pages 1-2)
* Saito S et al. *Regulatory Role of GgaR (YegW) for Glycogen Accumulation in Escherichia coli K-12.* Microorganisms. **2024-01**. DOI: 10.3390/microorganisms12010115. https://doi.org/10.3390/microorganisms12010115 (saito2024regulatoryroleof pages 1-2)

**Redox intermediate inclusions: sulfur globules**
* Di Nezio F et al. *Synergistic phenotypic adaptations… Chromatium okenii…* PLOS ONE. **2024-10**. DOI: 10.1371/journal.pone.0310265. https://doi.org/10.1371/journal.pone.0310265 (nezio2024synergisticphenotypicadaptations pages 2-3, nezio2024synergisticphenotypicadaptations pages 1-2)
* Kushkevych I et al. *Anoxygenic photosynthesis with emphasis on green sulfur bacteria…* Frontiers in Microbiology. **2024-07**. DOI: 10.3389/fmicb.2024.1417714. https://doi.org/10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 18-18)

**Polyphosphate granules (note: 2025 in retrieved corpus)**
* Corrales D et al. *Polyphosphate from Lactic Acid Bacteria…* Foods. **2025-06**. DOI: 10.3390/foods14132211. https://doi.org/10.3390/foods14132211 (corrales2025polyphosphatefromlactic pages 1-2, corrales2025polyphosphatefromlactic pages 13-15, corrales2025polyphosphatefromlactic pages 2-4)

---

## Minimal curation takeaways for `intracellular_inclusion.yaml`

* Intracellular inclusions are best curated as a **class trait** with **subclass-specific mechanistic modules**:
  * **PHA granule module:** phaABC → PHA granule; PhaP coats; nutrient imbalance (high C/N, N depletion) increases accumulation; quantifiable as %DCW. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
  * **Glycogen granule module:** glg genes → glycogen granules; nitrogen limitation increases storage; regulation includes ADP-glucose sensing (GgaR in E. coli); quantifiable as mg/g DCW. (but2024newsolutionsin pages 1-2, saito2024regulatoryroleof pages 1-2)
  * **polyP granule module:** ppk/ppx balance → polyP granules; Pi availability increases accumulation; inclusions are Mg/Ca enriched. (corrales2025polyphosphatefromlactic pages 1-2, corrales2025polyphosphatefromlactic pages 13-15)
  * **GV module:** gvpA/gvpC + accessory gvp genes → gas vesicle; physical properties (collapse pressure) and structure support buoyancy; strong biomedical imaging applications. (feng2024advancesinthe pages 1-2, feng2024advancesinthe pages 2-4, iburg2024elucidatingtheassembly pages 1-2)
  * **BMC module:** BMC-H/T/P + encapsulation peptides → BMC shell + cargo; supports catabolic/anabolic compartmentalization and synthetic biology engineering. (doron2024bacterialmicrocompartmentsas pages 3-5, doron2024bacterialmicrocompartmentsas pages 1-3)
  * **Magnetosome module:** MamF-like proteins → targeting → magnetoskeleton components → chain organization; strong quantitative mutant effects. Include figure evidence. (paulus2024mamflikeproteinsare pages 2-3, paulus2024mamflikeproteinsare media 113fa52e)
  * **Sulfur globule module:** sulfide oxidation → S0 globules; reduced sulfur availability modulates globule morphology; Dsr implicated in globule oxidation (limited in corpus). (nezio2024synergisticphenotypicadaptations pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 18-18)


References

1. (doron2024bacterialmicrocompartmentsas pages 1-3): Lior Doron and Cheryl A. Kerfeld. Bacterial microcompartments as a next-generation metabolic engineering tool: utilizing nature's solution for confining challenging catabolic pathways. Biochemical Society Transactions, 52:997-1010, May 2024. URL: https://doi.org/10.1042/bst20230229, doi:10.1042/bst20230229. This article has 22 citations and is from a peer-reviewed journal.

2. (feng2024advancesinthe pages 1-2): Renjie Feng, Jie Lan, Meei Chyn Goh, Meng Du, and Zhiyi Chen. Advances in the application of gas vesicles in medical imaging and disease treatment. Journal of Biological Engineering, Jul 2024. URL: https://doi.org/10.1186/s13036-024-00426-3, doi:10.1186/s13036-024-00426-3. This article has 15 citations and is from a peer-reviewed journal.

3. (feng2024advancesinthe pages 2-4): Renjie Feng, Jie Lan, Meei Chyn Goh, Meng Du, and Zhiyi Chen. Advances in the application of gas vesicles in medical imaging and disease treatment. Journal of Biological Engineering, Jul 2024. URL: https://doi.org/10.1186/s13036-024-00426-3, doi:10.1186/s13036-024-00426-3. This article has 15 citations and is from a peer-reviewed journal.

4. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4): Ivo Fukala and Igor Kučera. Natural polyhydroxyalkanoates—an overview of bacterial production methods. Molecules, 29:2293, May 2024. URL: https://doi.org/10.3390/molecules29102293, doi:10.3390/molecules29102293. This article has 27 citations.

5. (but2024newsolutionsin pages 1-2): Sergey Y. But, Ruslan Z. Suleimanov, Igor Y. Oshkin, Olga N. Rozova, Ildar I. Mustakhimov, Nikolai V. Pimenov, Svetlana N. Dedysh, and Valentina N. Khmelenina. New solutions in single-cell protein production from methane: construction of glycogen-deficient mutants of methylococcus capsulatus mir. Fermentation, 10:265, May 2024. URL: https://doi.org/10.3390/fermentation10050265, doi:10.3390/fermentation10050265. This article has 20 citations.

6. (corrales2025polyphosphatefromlactic pages 1-2): Daniela Corrales, Cristina Alcántara, Vicente Monedero, and Manuel Zúñiga. Polyphosphate from lactic acid bacteria: a functional molecule for food and health applications. Foods, 14:2211, Jun 2025. URL: https://doi.org/10.3390/foods14132211, doi:10.3390/foods14132211. This article has 3 citations.

7. (paulus2024mamflikeproteinsare pages 1-2): Anja Paulus, Frederik Ahrens, Annika Schraut, Hannah Hofmann, Tim Schiller, Thomas Sura, Dörte Becher, and René Uebe. Mamf-like proteins are distant tic20 homologs involved in organelle assembly in bacteria. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55121-0, doi:10.1038/s41467-024-55121-0. This article has 6 citations and is from a highest quality peer-reviewed journal.

8. (martinez2024enhancingmagnetosomebiomanufacturing pages 29-32): M Masó Martínez. Enhancing magnetosome biomanufacturing: understanding biomineralization and process development. Unknown journal, 2024.

9. (nezio2024synergisticphenotypicadaptations pages 1-2): Francesco Di Nezio, Irvine Lian Hao Ong, René Riedel, Arkajyoti Goshal, Jayabrata Dhar, Samuele Roman, Nicola Storelli, and Anupam Sengupta. Synergistic phenotypic adaptations of motile purple sulphur bacteria chromatium okenii during lake-to-laboratory domestication. PLOS ONE, 19:e0310265, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0310265, doi:10.1371/journal.pone.0310265. This article has 4 citations and is from a peer-reviewed journal.

10. (doron2024bacterialmicrocompartmentsas pages 3-5): Lior Doron and Cheryl A. Kerfeld. Bacterial microcompartments as a next-generation metabolic engineering tool: utilizing nature's solution for confining challenging catabolic pathways. Biochemical Society Transactions, 52:997-1010, May 2024. URL: https://doi.org/10.1042/bst20230229, doi:10.1042/bst20230229. This article has 22 citations and is from a peer-reviewed journal.

11. (trettel2024modelingbacterialmicrocompartment pages 1-2): Daniel S. Trettel, Sara L. Pacheco, Asa K. Laskie, Raul Gonzalez-Esquer, Jianping Yu, Harvey J. M. Hou, and Denis Jallet. Modeling bacterial microcompartment architectures for enhanced cyanobacterial carbon fixation. Frontiers in Plant Science, Feb 2024. URL: https://doi.org/10.3389/fpls.2024.1346759, doi:10.3389/fpls.2024.1346759. This article has 8 citations.

12. (iburg2024elucidatingtheassembly pages 1-2): Manuel Iburg, Andrew P. Anderson, Vivian T. Wong, Erica D. Anton, Art He, and George J. Lu. Elucidating the assembly of gas vesicles by systematic protein-protein interaction analysis. The EMBO Journal, 43:4156-4172, Jul 2024. URL: https://doi.org/10.1038/s44318-024-00178-2, doi:10.1038/s44318-024-00178-2. This article has 8 citations.

13. (iburg2024elucidatingtheassembly pages 2-4): Manuel Iburg, Andrew P. Anderson, Vivian T. Wong, Erica D. Anton, Art He, and George J. Lu. Elucidating the assembly of gas vesicles by systematic protein-protein interaction analysis. The EMBO Journal, 43:4156-4172, Jul 2024. URL: https://doi.org/10.1038/s44318-024-00178-2, doi:10.1038/s44318-024-00178-2. This article has 8 citations.

14. (iburg2024elucidatingtheassembly pages 4-5): Manuel Iburg, Andrew P. Anderson, Vivian T. Wong, Erica D. Anton, Art He, and George J. Lu. Elucidating the assembly of gas vesicles by systematic protein-protein interaction analysis. The EMBO Journal, 43:4156-4172, Jul 2024. URL: https://doi.org/10.1038/s44318-024-00178-2, doi:10.1038/s44318-024-00178-2. This article has 8 citations.

15. (paulus2024mamflikeproteinsare pages 2-3): Anja Paulus, Frederik Ahrens, Annika Schraut, Hannah Hofmann, Tim Schiller, Thomas Sura, Dörte Becher, and René Uebe. Mamf-like proteins are distant tic20 homologs involved in organelle assembly in bacteria. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55121-0, doi:10.1038/s41467-024-55121-0. This article has 6 citations and is from a highest quality peer-reviewed journal.

16. (paulus2024mamflikeproteinsare media 113fa52e): Anja Paulus, Frederik Ahrens, Annika Schraut, Hannah Hofmann, Tim Schiller, Thomas Sura, Dörte Becher, and René Uebe. Mamf-like proteins are distant tic20 homologs involved in organelle assembly in bacteria. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55121-0, doi:10.1038/s41467-024-55121-0. This article has 6 citations and is from a highest quality peer-reviewed journal.

17. (paulus2024mamflikeproteinsare media 0de12e88): Anja Paulus, Frederik Ahrens, Annika Schraut, Hannah Hofmann, Tim Schiller, Thomas Sura, Dörte Becher, and René Uebe. Mamf-like proteins are distant tic20 homologs involved in organelle assembly in bacteria. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55121-0, doi:10.1038/s41467-024-55121-0. This article has 6 citations and is from a highest quality peer-reviewed journal.

18. (woo2024isolationandcharacterization pages 1-2): Sung-Geun Woo, Nils J. H. Averesch, Aaron J. Berliner, Joerg S. Deutzmann, Vince E. Pane, Sulogna Chatterjee, and Craig S. Criddle. Isolation and characterization of a <i>halomonas</i> species for non-axenic growth-associated production of bio-polyesters from sustainable feedstocks. Aug 2024. URL: https://doi.org/10.1128/aem.00603-24, doi:10.1128/aem.00603-24. This article has 4 citations and is from a peer-reviewed journal.

19. (woo2024isolationandcharacterization pages 2-6): Sung-Geun Woo, Nils J. H. Averesch, Aaron J. Berliner, Joerg S. Deutzmann, Vince E. Pane, Sulogna Chatterjee, and Craig S. Criddle. Isolation and characterization of a <i>halomonas</i> species for non-axenic growth-associated production of bio-polyesters from sustainable feedstocks. Aug 2024. URL: https://doi.org/10.1128/aem.00603-24, doi:10.1128/aem.00603-24. This article has 4 citations and is from a peer-reviewed journal.

20. (feng2024advancesinthe pages 9-10): Renjie Feng, Jie Lan, Meei Chyn Goh, Meng Du, and Zhiyi Chen. Advances in the application of gas vesicles in medical imaging and disease treatment. Journal of Biological Engineering, Jul 2024. URL: https://doi.org/10.1186/s13036-024-00426-3, doi:10.1186/s13036-024-00426-3. This article has 15 citations and is from a peer-reviewed journal.

21. (yadav2025therapeuticinnovationsin pages 9-11): Virendra Kumar Yadav, Sheersha Pramanik, Saad Alghamdi, Banan Atwah, Naeem Qusty, Ahmad Babalghith, Vijendra Singh Solanki, Neha Agarwal, Nishant Gupta, Parwiz Niazi, Ashish Patel, Nisha Choudhary, and Rustem Zairov. Therapeutic innovations in nanomedicine: exploring the potential of magnetotactic bacteria and bacterial magnetosomes. International Journal of Nanomedicine, 20:403-444, Jan 2025. URL: https://doi.org/10.2147/ijn.s462031, doi:10.2147/ijn.s462031. This article has 24 citations and is from a peer-reviewed journal.

22. (saito2024regulatoryroleof pages 1-2): Shunsuke Saito, Ikki Kobayashi, Motoki Hoshina, Emi Uenaka, Atsushi Sakurai, Sousuke Imamura, and Tomohiro Shimada. Regulatory role of ggar (yegw) for glycogen accumulation in escherichia coli k-12. Microorganisms, 12:115, Jan 2024. URL: https://doi.org/10.3390/microorganisms12010115, doi:10.3390/microorganisms12010115. This article has 0 citations.

23. (nezio2024synergisticphenotypicadaptations pages 2-3): Francesco Di Nezio, Irvine Lian Hao Ong, René Riedel, Arkajyoti Goshal, Jayabrata Dhar, Samuele Roman, Nicola Storelli, and Anupam Sengupta. Synergistic phenotypic adaptations of motile purple sulphur bacteria chromatium okenii during lake-to-laboratory domestication. PLOS ONE, 19:e0310265, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0310265, doi:10.1371/journal.pone.0310265. This article has 4 citations and is from a peer-reviewed journal.

24. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

25. (altamiraalgarra2024bioplasticproductionby pages 20-22): Beatriz Altamira-Algarra, Artai Lage, Ana Lucía Meléndez, Marc Arnau, Eva Gonzalez-Flo, and Joan García. Bioplastic production by harnessing cyanobacteria-rich microbiomes for perpetual synthesis. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2023.11.06.565755, doi:10.1101/2023.11.06.565755. This article has 0 citations.

26. (corrales2025polyphosphatefromlactic pages 13-15): Daniela Corrales, Cristina Alcántara, Vicente Monedero, and Manuel Zúñiga. Polyphosphate from lactic acid bacteria: a functional molecule for food and health applications. Foods, 14:2211, Jun 2025. URL: https://doi.org/10.3390/foods14132211, doi:10.3390/foods14132211. This article has 3 citations.

27. (yadav2025therapeuticinnovationsin pages 7-9): Virendra Kumar Yadav, Sheersha Pramanik, Saad Alghamdi, Banan Atwah, Naeem Qusty, Ahmad Babalghith, Vijendra Singh Solanki, Neha Agarwal, Nishant Gupta, Parwiz Niazi, Ashish Patel, Nisha Choudhary, and Rustem Zairov. Therapeutic innovations in nanomedicine: exploring the potential of magnetotactic bacteria and bacterial magnetosomes. International Journal of Nanomedicine, 20:403-444, Jan 2025. URL: https://doi.org/10.2147/ijn.s462031, doi:10.2147/ijn.s462031. This article has 24 citations and is from a peer-reviewed journal.

28. (paulus2024mamflikeproteinsare pages 3-5): Anja Paulus, Frederik Ahrens, Annika Schraut, Hannah Hofmann, Tim Schiller, Thomas Sura, Dörte Becher, and René Uebe. Mamf-like proteins are distant tic20 homologs involved in organelle assembly in bacteria. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55121-0, doi:10.1038/s41467-024-55121-0. This article has 6 citations and is from a highest quality peer-reviewed journal.

29. (corrales2025polyphosphatefromlactic pages 2-4): Daniela Corrales, Cristina Alcántara, Vicente Monedero, and Manuel Zúñiga. Polyphosphate from lactic acid bacteria: a functional molecule for food and health applications. Foods, 14:2211, Jun 2025. URL: https://doi.org/10.3390/foods14132211, doi:10.3390/foods14132211. This article has 3 citations.