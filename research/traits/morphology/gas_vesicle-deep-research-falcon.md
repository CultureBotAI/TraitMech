---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:51:40.751759'
end_time: '2026-06-18T08:03:47.583739'
duration_seconds: 726.83
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: gas vesicle
  trait_identifier: traitmech:000070
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: gas_vesicle
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An intracellular gas-filled proteinaceous inclusion that provides buoyancy,
    allowing planktonic bacteria and archaea to position themselves in the water column.
  parent_traits: traitmech:000066
  synonyms: gas vacuole
  evidence_summary: 'DOI:10.1038/nrmicro2834:  (Pfeifer describes gas vesicles as
    intracellular gas-filled proteinaceous flotation structures in bacteria and archaea.)
    | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include gas vesicles among
    bacterial intracellular organelles.)'
  causal_graph_summary: 'gas_vesicle_buoyancy: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gas vesicle
- **METPO identifier:** traitmech:000070
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular gas-filled proteinaceous inclusion that provides buoyancy, allowing planktonic bacteria and archaea to position themselves in the water column.
- **Parent traits:** traitmech:000066
- **Synonyms:** gas vacuole
- **Existing evidence:** DOI:10.1038/nrmicro2834:  (Pfeifer describes gas vesicles as intracellular gas-filled proteinaceous flotation structures in bacteria and archaea.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include gas vesicles among bacterial intracellular organelles.)
- **Existing causal graph summary:** gas_vesicle_buoyancy: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **gas vesicle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gas_vesicle.yaml`.

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
- **Trait label:** gas vesicle
- **METPO identifier:** traitmech:000070
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular gas-filled proteinaceous inclusion that provides buoyancy, allowing planktonic bacteria and archaea to position themselves in the water column.
- **Parent traits:** traitmech:000066
- **Synonyms:** gas vacuole
- **Existing evidence:** DOI:10.1038/nrmicro2834:  (Pfeifer describes gas vesicles as intracellular gas-filled proteinaceous flotation structures in bacteria and archaea.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include gas vesicles among bacterial intracellular organelles.)
- **Existing causal graph summary:** gas_vesicle_buoyancy: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **gas vesicle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gas_vesicle.yaml`.

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


## Microbial TraitMech Curation Report: Gas Vesicle (gas vacuole)

**Target trait:** gas vesicle (METPO:traitmech:000070; MORPHOLOGY; CLASS)

### 1) Scope summary (trait meaning, boundaries, and nearby traits)

**Current understanding / definition.** Gas vesicles (GVs; “gas vacuoles”) are intracellular, gas-filled, proteinaceous organelles/nanostructures produced by diverse microbes. They function primarily as flotation/buoyancy devices that allow aquatic microbes to control vertical position to access light and/or oxygen (iburg2024elucidatingtheassembly pages 1-2, feng2024advancesinthe pages 2-4). In engineered contexts, the same gas-filled architecture yields strong ultrasound scattering, enabling use as genetically encodable ultrasound contrast agents (“acoustic reporter genes,” ARGs) (hurt2024directedevolutionof pages 1-3).

**Phenotype represented by the TraitMech node.** For TraitMech, *gas vesicle* is best treated as the **presence/biogenesis of intracellular gas-filled protein compartments** (organelles), leading to:
- **Physiological capacity:** buoyancy / flotation and vertical migration (especially in water columns) (iburg2024elucidatingtheassembly pages 1-2, feng2024advancesinthe pages 2-4).
- **Assay-observed property:** flotation/floatation in laboratory flotation assays; presence of intracellular/cytoplasmic gas-filled inclusions observable by EM/phase contrast (jazbec2024proteingasvesicles pages 1-3, jazbec2024proteingasvesicles media 312076f3).

**Boundary cases / distinctions.**
- Distinguish **intracellular gas vesicles** from **extracellular microbubbles/nanobubbles** used clinically as contrast agents; microbubbles are not genetically encoded microbial organelles and have short circulation lifetime (feng2024advancesinthe pages 4-5).
- Distinguish **GV-mediated buoyancy** from **non-GV rapid flotation** driven by extracellular oxygen microbubbles trapped in aggregates (e.g., Microcystis scum via EPS + micro-bubbles), which is *not* gas vesicle biogenesis (yang2024rapidflotationof pages 1-2).
- GVs are *proteinaceous compartments* and part of the broader set of proteinaceous bacterial organelles/microcompartments (chen2013thebacterialcarbonfixing pages 1-2, jr.2013microcompartmentsandprotein pages 1-2).

### 2) Key concepts and mechanistic entities for a causal graph

#### A. Core structural concepts
- **Gas vesicle shell:** extremely thin protein shell; review summarizes cryo-EM work describing shells “only one or two peptide layers thick,” hydrophobic inner surface, and pore-based gas diffusion (feng2024advancesinthe pages 2-4).
- **Hydrophobic inner surface:** supports stable gas compartment by preventing heterogeneous condensation of water into liquid in the lumen (iburg2024elucidatingtheassembly pages 1-2).
- **Mechanical collapse / critical pressure:** GVs irreversibly collapse above a critical pressure; critical collapse pressure spans ~0.09–1 MPa across taxa per review (feng2024advancesinthe pages 2-4).

#### B. Genes and proteins (Gvp)
**Candidate gene/protein nodes (label-only grounding unless taxon-specific UniProt IDs are selected during curation):**
- Structural proteins: **GvpA/GvpA2 (often called GvpB in B. megaterium)**, **GvpC** (feng2024advancesinthe pages 2-4, iburg2024elucidatingtheassembly pages 2-4).
- Transcriptional regulation: **GvpE** (activator), **GvpD** (inhibitor) (feng2024advancesinthe pages 4-5).
- Assembly/accessory: **GvpF, GvpL, GvpN (AAA+/ATPase), GvpJ, GvpM** and others (feng2024advancesinthe pages 4-5, jazbec2024proteingasvesicles pages 5-6).

#### C. Environmental / experimental factors
Evidence in this retrieved set is strongest for ecological “light/oxygen seeking” framing rather than detailed environmental regulatory circuits:
- **Light availability:** buoyancy enables upward movement to “get enough light for photosynthesis” (feng2024advancesinthe pages 2-4).
- **Oxygen availability:** halophilic archaea buoy upward to reach higher oxygen levels (feng2024advancesinthe pages 2-4).
- **Pressure/acoustic pressure:** ultrasound and physical pressure can collapse GVs (conceptual; collapse threshold described) (feng2024advancesinthe pages 2-4, hurt2024directedevolutionof pages 1-3).

*Note:* Specific environmental regulation edges (e.g., nitrogen limitation → gvp expression; depth → narrower GVs) are mentioned as review summaries but often as citations to older primary literature (feng2024advancesinthe pages 9-10) and should be curated cautiously unless the primary sources are obtained.

#### D. Application nodes (real-world implementations)
- **Acoustic reporter genes (ARGs):** gene clusters encoding gas vesicles expressed heterologously for ultrasound imaging (hurt2024directedevolutionof pages 1-3, feng2024advancesinthe pages 4-5).
- **Mammalian acoustic reporter genes (mARG):** inducible, drug-selectable constructs enabling robust GV expression in mammalian cells for ultrasound imaging (howells2024adrug‐selectableacoustic pages 1-2).
- **Ultrasound contrast agents / targeted imaging:** purified/isolated or engineered GVs used for in vivo imaging in mice (liu2024characterizationandcomparison pages 1-2).

### 3) Evidence-backed candidate causal edges (triples)

The following table is designed for direct translation into `gas_vesicle.yaml` as subject–predicate–object edges with notes on uncertainty and grounding.

| Subject node (label + suggested CURIE) | Predicate | Object node (label + CURIE) | Evidence snippet (verbatim quote) | Source (authors/year/journal) | DOI | URL | Publication date | Notes/uncertainty |
|---|---|---|---|---|---|---|---|---|
| gas vesicle (METPO:traitmech:000070) | enables | buoyancy / flotation in aquatic microbes (GO:000? candidate; label-only if ungrounded) | "Gas vesicles (GVs) are a class of gas-filled protein organelles evolved in photosynthetic microbes, which use them as flotation devices to compete for the surface of the water and maximize photosynthesis" (iburg2024elucidatingtheassembly pages 1-2) | Iburg et al. 2024, The EMBO Journal | 10.1038/s44318-024-00178-2 | https://doi.org/10.1038/s44318-024-00178-2 | 2024-09-03 | Strong scope statement; photosynthetic microbe framing may not cover all taxa. |
| gas vesicle (METPO:traitmech:000070) | enables | access to light for photosynthesis (ENVO:water column surface, label-only for process) | "The GVs produced by PSB give them the buoyancy to move upward so that they can get enough light for photosynthesis to produce nutrients" (feng2024advancesinthe pages 2-4) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Good ecological-function edge; review summarizes prior primary literature. |
| gas vesicle (METPO:traitmech:000070) | enables | access to higher oxygen concentrations (CHEBI:15379 oxygen) | "GVs can lift these halophilic archaea from the bottom of low-oxygen waters to an appropriate oxygen concentration level by increasing upward buoyancy" (feng2024advancesinthe pages 2-4) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Halophilic-archaea specific ecological edge. |
| GvpA (label-only; UniProt taxon-specific) | forms | gas vesicle shell (METPO:traitmech:000070) | "The most important of these is the structural protein GvpA, which is a small hydrophobic protein that forms the hollow protein structure of GV" (feng2024advancesinthe pages 2-4) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Strong review statement; exact protein accession depends on taxon. |
| GvpA (label-only) | self_assembles_into | helical half-shells / helical filaments (label-only) | "Their study also found that GvpA can self-assemble into two helical half-shells and close at the cone apex, after which the two half-shells are joined by the characteristic arrangement of GvpA monomers to form the GV structure of a hollow helical cylinder" (feng2024advancesinthe pages 2-4) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Structural-mechanistic edge from review of 2023 cryo-EM work. |
| GvpA α1 helix region (label-only) | allows_diffusion_of | gas molecules into gas vesicle lumen (label-only) | "the pores in the GV shell are large, and these pores are caused by α1 helix of the GvpA, which can allow the external gas to diffuse freely into the vesicle" (feng2024advancesinthe pages 2-4) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Region-specific molecular mechanism; grounding unclear. |
| hydrophobic inner shell surface (label-only) | prevents | water condensation into lumen (label-only) | "the protein shell is permeable to individual molecules of both gas and water, and GVs maintain an inner gas compartment by having a hydrophobic inner surface that prevents heterogeneous condensation of water molecules into liquid" (iburg2024elucidatingtheassembly pages 1-2) | Iburg et al. 2024, The EMBO Journal | 10.1038/s44318-024-00178-2 | https://doi.org/10.1038/s44318-024-00178-2 | 2024-09-03 | Strong physical-mechanistic edge; object is conceptual/label-only. |
| GvpC (label-only) | strengthens | gas vesicle shell (METPO:traitmech:000070) | "GvpC is another coat protein. It is the second structural protein involved in the formation of GV... it was found that GvpC has the function of strengthening the GV shell" (feng2024advancesinthe pages 2-4) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Strong but review-derived. |
| GvpC (Anabaena flos-aquae; label-only) | increases | hydrostatic pressure resistance of gas vesicles (label-only) | "coexpress a structural protein known as GvpC, which adheres to the outer surface of gas vesicles, reinforcing their structure and rendering them 3 times more resistant to hydrostatic pressure in the case of A. flos-aquae" (jazbec2024proteingasvesicles pages 5-6) | Jazbec et al. 2024, ACS Nano | 10.1021/acsnano.4c01498 | https://doi.org/10.1021/acsnano.4c01498 | 2024-06-19 | Taxon-specific quantitative edge; very useful. |
| pressure (PATO/physical factor label-only) | collapses_under / irreversibly_collapses | gas vesicle (METPO:traitmech:000070) | "However, when GVs are under pressure, there is a critical point at which the GV irreversibly collapses" (feng2024advancesinthe pages 2-4) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Strong physical-property edge. |
| gas vesicle width (label-only) | inversely_correlates_with | gas vesicle strength / critical collapse pressure (label-only) | "The inverse correlation between width and strength of gas vesicles" and "The relationship between critical pressure and width" (feng2024advancesinthe pages 9-10) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Citation is bibliographic snippet in review rather than full quote from primary data; curate cautiously. |
| critical collapse pressure (label-only) | has_range | 0.09–1 MPa (UO:0000095 megapascal) | "The critical collapse pressure of GV in different microorganisms ranges from 0.09 MPa to 1 MPa" (feng2024advancesinthe pages 2-4) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Range spans taxa; suitable as annotation/statistic more than edge. |
| GvpE (label-only) | activates_transcription_of | gas vesicle synthesis genes / core proteins (label-only) | "GvpE is responsible for activating transcription" and "GvpE can activate transcription and thus promote the expression of core proteins" (feng2024advancesinthe pages 4-5) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Regulatory edge from review; taxon dependence likely. |
| GvpD (label-only) | inhibits | gas vesicle formation (METPO:traitmech:000070) | "GvpD has an inhibitory effect on GV formation" (feng2024advancesinthe pages 4-5) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Strong review-derived regulatory edge. |
| GvpF (label-only) | binds | GvpA (label-only) | "GvpF is an important accessory protein because it is the only protein that binds to GvpA" (feng2024advancesinthe pages 4-5) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Binding relation; likely species-context dependent. |
| GvpL (label-only) | binds | all GV proteins except GvpA (label-only set) | "GvpL is homologous to GvpF but has the opposite function, binding to all GV proteins except GvpA" (feng2024advancesinthe pages 4-5) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Complex set-valued object; may need decomposition if curated. |
| GvpN (label-only) | hydrolyzes / provides_energy_for | gas vesicle assembly / maturation (label-only) | "there is another energy-providing GV protein, GvpN, which can hydrolyze adenosine triphosphate (ATP) to release energy due to its nucleoside triphosphate (NTP) binding/AAA+ domain" (feng2024advancesinthe pages 4-5) | Feng et al. 2024, Journal of Biological Engineering | 10.1186/s13036-024-00426-3 | https://doi.org/10.1186/s13036-024-00426-3 | 2024-07 | Mechanistic but still somewhat inferred to assembly energy role. |
| N-terminus of GvpN (label-only) | required_for | mature gas vesicle formation (METPO:traitmech:000070) | "the N-terminus of GvpN was observed to play an important role in the formation of mature GVs" (jazbec2024proteingasvesicles pages 1-3) | Jazbec et al. 2024, ACS Nano | 10.1021/acsnano.4c01498 | https://doi.org/10.1021/acsnano.4c01498 | 2024-06-19 | Primary experimental evidence, B. megaterium system. |
| GvpN deletion/perturbation (label-only) | results_in | spindle-shaped gas vesicles (label-only) | "GvpN N-terminus tagging resulted in the formation of spindle-shaped GVs, lacking an elongated cylindrical part" (jazbec2024proteingasvesicles pages 5-6) | Jazbec et al. 2024, ACS Nano | 10.1021/acsnano.4c01498 | https://doi.org/10.1021/acsnano.4c01498 | 2024-06-19 | Assay-specific perturbation phenotype. |
| GvpJ (label-only) | tightly_bound_to | cylindrical part of gas vesicle (label-only) | "GvpJ was nevertheless found to be tightly bound to the cylindrical part of GVs in this study" (jazbec2024proteingasvesicles pages 1-3) | Jazbec et al. 2024, ACS Nano | 10.1021/acsnano.4c01498 | https://doi.org/10.1021/acsnano.4c01498 | 2024-06-19 | Strong primary evidence in B. megaterium-derived GVs. |
| GvpJ (label-only) | involved_in | gas vesicle elongation (label-only) | "Based on the location of GvpJ around the polarity inversal point, it indicates its involvement in elongation likely adding GvpB units into the growing GV" (jazbec2024proteingasvesicles pages 5-6) | Jazbec et al. 2024, ACS Nano | 10.1021/acsnano.4c01498 | https://doi.org/10.1021/acsnano.4c01498 | 2024-06-19 | Inferred from localization; mark uncertain. |
| GvpR (label-only) | dispensable_for | functional gas vesicle formation (METPO:traitmech:000070) | "Three (GvpR, GvpT, and GvpU) out of 11 genes in the cluster were found to be dispensable for functional GV formation" (jazbec2024proteingasvesicles pages 1-3) | Jazbec et al. 2024, ACS Nano | 10.1021/acsnano.4c01498 | https://doi.org/10.1021/acsnano.4c01498 | 2024-06-19 | B. megaterium cluster-specific. |
| GvpT (label-only) | dispensable_for | functional gas vesicle formation (METPO:traitmech:000070) | "Three (GvpR, GvpT, and GvpU) out of 11 genes in the cluster were found to be dispensable for functional GV formation" (jazbec2024proteingasvesicles pages 1-3) | Jazbec et al. 2024, ACS Nano | 10.1021/acsnano.4c01498 | https://doi.org/10.1021/acsnano.4c01498 | 2024-06-19 | B. megaterium cluster-specific. |
| GvpU (label-only) | dispensable_for | functional gas vesicle formation (METPO:traitmech:000070) | "Three (GvpR, GvpT, and GvpU) out of 11 genes in the cluster were found to be dispensable for functional GV formation" (jazbec2024proteingasvesicles pages 1-3) | Jazbec et al. 2024, ACS Nano | 10.1021/acsnano.4c01498 | https://doi.org/10.1021/acsnano.4c01498 | 2024-06-19 | B. megaterium cluster-specific. |
| deletion of GvpR/T/U (label-only) | results_in | narrower gas vesicles (label-only) | "their omission resulted in narrower GVs" (jazbec2024proteingasvesicles pages 1-3) | Jazbec et al. 2024, ACS Nano | 10.1021/acsnano.4c01498 | https://doi.org/10.1021/acsnano.4c01498 | 2024-06-19 | Strong phenotype edge, taxon-specific. |
| gas vesicle shell (METPO:traitmech:000070) | scatters | ultrasound waves (label-only) | "GVs scatter US due to the difference in the density and compressibility of their gaseous interior relative to a surrounding aqueous medium" (hurt2024directedevolutionof pages 1-3) | Hurt et al. 2024, ACS Synthetic Biology | 10.1021/acssynbio.4c00283 | https://doi.org/10.1021/acssynbio.4c00283 | 2024-07-09 | Strong mechanistic basis for engineered applications. |
| acoustic reporter genes (ARGs; label-only) | are_based_on | gas vesicles (METPO:traitmech:000070) | "These acoustic reporter genes (ARGs) represent a novel class of genetically encoded US contrast agent, and are based on air-filled protein nanostructures called gas vesicles (GVs)" (hurt2024directedevolutionof pages 1-3) | Hurt et al. 2024, ACS Synthetic Biology | 10.1021/acssynbio.4c00283 | https://doi.org/10.1021/acssynbio.4c00283 | 2024-07-09 | Strong application edge. |
| directed evolution of GvpA/B homologues (label-only) | increases | nonlinear ultrasound signal 5-fold and 14-fold (label-only) | "two rounds of evolution resulted in GV variants with 5- and 14-fold stronger acoustic signals than the parent proteins" (hurt2024directedevolutionof pages 1-3) | Hurt et al. 2024, ACS Synthetic Biology | 10.1021/acssynbio.4c00283 | https://doi.org/10.1021/acssynbio.4c00283 | 2024-07-09 | Engineering-performance edge; not native biology but useful for applications. |
| gas vesicles expressed in mammalian cells (mARGds; label-only) | increases | ultrasound signal-to-noise ratio (label-only) | "cells expressing gas vesicles exhibiting an 80% greater signal-to-noise ratio compared to negative controls and a 500% greater signal-to-noise ratio compared to wild-type HEK293T cells" (howells2024adrug‐selectableacoustic pages 1-2) | Howells et al. 2024, Bioengineering & Translational Medicine | 10.1002/btm2.10584 | https://doi.org/10.1002/btm2.10584 | 2024-08 | Mammalian engineered implementation; assay-specific. |
| gas vesicles (engineered or isolated) (METPO:traitmech:000070) | can_produce | stable ultrasound contrast in vivo (label-only) | "naturally isolated GVs could produce stable ultrasound contrast signals in murine livers and tumors using clinical diagnostic ultrasound equipment. Additionally, heterologously expressed GVs from gene-engineered bacteria also exhibited good ultrasound contrast performance" (liu2024characterizationandcomparison pages 1-2) | Liu et al. 2024, Pharmaceuticals | 10.3390/ph17060755 | https://doi.org/10.3390/ph17060755 | 2024-06-07 | Real-world preclinical implementation. |
| gas vesicles (METPO:traitmech:000070) | remain_stable_for | months (UO:0000036 month; label-only if unavailable) | "GVs can be made with diameters smaller than 100 nm and stable for months" (iburg2024elucidatingtheassembly pages 1-2) | Iburg et al. 2024, The EMBO Journal | 10.1038/s44318-024-00178-2 | https://doi.org/10.1038/s44318-024-00178-2 | 2024-09-03 | Comparative physical-performance statement. |
| synthetic nanobubbles (label-only comparator) | remain_stable_for | minutes (UO:0000031 minute; label-only if unavailable) | "nanobubbles have only recently reached <200 nm in diameter and a lifetime of minutes" (iburg2024elucidatingtheassembly pages 1-2) | Iburg et al. 2024, The EMBO Journal | 10.1038/s44318-024-00178-2 | https://doi.org/10.1038/s44318-024-00178-2 | 2024-09-03 | Comparator rather than gas-vesicle trait edge; include with caution. |


*Table: This table compiles candidate causal edges for TraitMech curation of the microbial gas vesicle trait, spanning native structure, assembly, regulation, physical properties, ecology, and engineered applications. It emphasizes direct evidence snippets and flags taxon-specific, inferred, or assay-specific claims for cautious curation.*

**Figure-level support (visual evidence).**
- Jazbec et al. show a **B. megaterium GV gene cluster schematic**, flotation assay (buoyancy proxy), and EM images supporting that **GvpR/T/U are dispensable** and that deletion yields **narrower GVs** (jazbec2024proteingasvesicles media 312076f3).
- Hurt et al. show figures describing **ARG directed evolution workflow** and **optimization of gene clusters** with ultrasound signal readouts (hurt2024directedevolutionof media 720b427e, hurt2024directedevolutionof media 82d8c825, hurt2024directedevolutionof media 9d8d0096).

### 4) Recent developments (prioritizing 2023–2024)

#### 4.1 Assembly mechanism: interaction networks and essentiality mapping
A 2024 EMBO Journal study frames the major knowledge gap as the limited functional definition of most Gvp “assembly factor” proteins beyond GvpA (major shell) and GvpC (minor/coat) and uses high-throughput interaction assays across all 11 proteins in a B. megaterium-derived operon (pNL29) (iburg2024elucidatingtheassembly pages 1-2, iburg2024elucidatingtheassembly pages 2-4). This provides a mechanistic foundation for adding intermediate nodes such as “protein complexes” and “assembly interdependence” into TraitMech graphs (iburg2024elucidatingtheassembly pages 2-4).

#### 4.2 Protein-level functional evidence from 2024 ACS Nano (B. megaterium operon)
Jazbec et al. experimentally establish accessory-protein roles relevant to curation:
- Dispensability of **GvpR/T/U** for functional GV formation; deletions yield **narrower vesicles** (jazbec2024proteingasvesicles pages 1-3, jazbec2024proteingasvesicles media 312076f3).
- **GvpJ** binds tightly to the cylindrical GV portion and is implicated in elongation based on localization around a polarity inversion region (the elongation claim is partially inferential and should be marked uncertain) (jazbec2024proteingasvesicles pages 1-3, jazbec2024proteingasvesicles pages 5-6).
- **GvpC** from Anabaena can be used as a modular surface functionalization scaffold and is described as strengthening GVs, with a quantitative claim of ~3× increased hydrostatic pressure resistance in A. flos-aquae (jazbec2024proteingasvesicles pages 5-6).

#### 4.3 Engineering acceleration (2023–2024): ARG evolution and mammalian integration
- Directed evolution of the primary structural protein homologues (GvpA/B) produced **5- and 14-fold stronger acoustic signals** than parent proteins, enabled by high-throughput acoustic screening (Hurt et al., 2024) (hurt2024directedevolutionof pages 1-3).
- A drug-selectable mammalian ARG system reports **80% higher SNR vs negative controls** and **500% higher SNR vs wild-type HEK293T**, supporting feasibility for cell therapy tracking and cellular reporting applications (Howells et al., accepted 2023; published 2024) (howells2024adrug‐selectableacoustic pages 1-2).

### 5) Current applications and real-world implementations (with data)

**In vivo ultrasound contrast in mice (preclinical).** Naturally isolated and heterologously expressed GVs produced “stable ultrasound contrast signals in murine livers and tumors using clinical diagnostic ultrasound equipment” (Liu et al., 2024) (liu2024characterizationandcomparison pages 1-2). Reported physical/particle statistics include particle sizes by DLS of **164.53 ± 1.47 nm** and **147.5 ± 2.10 nm**, and EM-based counts of **25–58 GVs per Serratia cell** vs **35–290 per engineered E. coli cell** in their system (liu2024characterizationandcomparison pages 1-2).

**Ultrasound-driven cell control / sonogenetics adjunct.** GVs can act as acoustic force enhancers when bound to mammalian cells through engineered GvpC, increasing ultrasound-driven Ca2+ influx and downstream transcriptional activation in engineered pathways (jazbec2024proteingasvesicles pages 1-3, jazbec2024proteingasvesicles pages 5-6).

**Why GVs are attractive vs synthetic bubbles.** GVs are described as genetically encodable nanostructures with stable gas compartments; the EMBO Journal review contrasts synthetic nanobubbles (minutes lifetime) with GVs “stable for months” and “diameters smaller than 100 nm” (iburg2024elucidatingtheassembly pages 1-2). This is a key expert framing for application-driven curation.

### 6) Expert opinions / authoritative analysis

- Iburg et al. (EMBO J 2024) emphasize that the “rapidly growing” application space (imaging, delivery, sensing) “has now demanded a deeper understanding of the biology of GV formation to facilitate their molecular engineering” (iburg2024elucidatingtheassembly pages 1-2). This supports inclusion of “assembly mechanism unknown/active research” as a curation note.
- Feng et al. (J Biol Eng 2024 review) synthesize consensus structural understanding: GvpA forms the “rib”-like shell and GvpC reinforces the exterior; GVs are stable yet exhibit irreversible collapse above a critical pressure (feng2024advancesinthe pages 2-4).

### 7) Candidate node inventory (grouped) with suggested ontology grounding

**Trait / structure**
- Gas vesicle (METPO:traitmech:000070)
- Gas vesicle shell (label-only)
- “Buoyancy” (GO term likely exists; not grounded here)

**Genes / proteins (taxon-specific UniProt IDs to be assigned during curation)**
- gvpA / GvpA; gvpA2 (aka GvpB in B. megaterium literature) (iburg2024elucidatingtheassembly pages 2-4)
- gvpC / GvpC (feng2024advancesinthe pages 2-4)
- Regulatory: gvpE, gvpD (feng2024advancesinthe pages 4-5)
- Assembly/accessory: gvpF, gvpL, gvpN (AAA+/ATPase), gvpJ, gvpM; and other operon members depending on taxon (feng2024advancesinthe pages 4-5, jazbec2024proteingasvesicles pages 5-6)

**Processes / functions**
- Protein self-assembly (GO process exists; not grounded here)
- Ultrasound scattering / contrast (label-only; physics process)

**Environmental / experimental factors**
- Light (ENVO/physical factor; label-only)
- Oxygen availability (CHEBI:15379 oxygen)
- Hydrostatic pressure / acoustic pressure (PATO/physical factor label-only)

**Applications**
- Acoustic reporter gene (ARG; label-only) (hurt2024directedevolutionof pages 1-3)
- Mammalian acoustic reporter gene (mARG / mARGds; label-only) (howells2024adrug‐selectableacoustic pages 1-2)

### 8) Warnings / curation cautions

1. **Do not conflate GV-dependent buoyancy with aggregation + extracellular oxygen microbubble-driven flotation** (distinct mechanism in Microcystis scum formation literature) (yang2024rapidflotationof pages 1-2).
2. **Environmental regulation edges (nutrients/depth/zooplankton) in the 2024 JBE review often refer to older primary sources.** For high-confidence TraitMech edges, obtain and quote the primary studies before curating strong regulatory claims (feng2024advancesinthe pages 9-10).
3. **Some mechanistic interpretations are inferential**, e.g., “GvpJ involved in elongation” based on localization; curate as *uncertain* unless additional direct functional assays are retrieved (jazbec2024proteingasvesicles pages 5-6).
4. **Taxon dependence of gvp operon composition and essential genes is high.** Edges about dispensability (e.g., GvpR/T/U) should be explicitly annotated as *B. megaterium operon-specific* (jazbec2024proteingasvesicles pages 1-3).

---

## DOI-first bibliography (2023–2024 prioritized)

1. Iburg M, Anderson AP, Wong VT, Anton ED, He A, Lu GJ. **Elucidating the assembly of gas vesicles by systematic protein-protein interaction analysis.** *The EMBO Journal.* Published online 3 Sep 2024. DOI: **10.1038/s44318-024-00178-2**. URL: https://doi.org/10.1038/s44318-024-00178-2 (iburg2024elucidatingtheassembly pages 1-2, iburg2024elucidatingtheassembly pages 2-4)
2. Jazbec V, Varda N, Šprager E, et al. **Protein Gas Vesicles of Bacillus megaterium as Enhancers of Ultrasound-Induced Transcriptional Regulation.** *ACS Nano.* Published 19 Jun 2024. DOI: **10.1021/acsnano.4c01498**. URL: https://doi.org/10.1021/acsnano.4c01498 (jazbec2024proteingasvesicles pages 1-3, jazbec2024proteingasvesicles pages 5-6, jazbec2024proteingasvesicles media 312076f3)
3. Hurt RC, Jin Z, Soufi M, et al. **Directed Evolution of Acoustic Reporter Genes Using High-Throughput Acoustic Screening.** *ACS Synthetic Biology.* Published 9 Jul 2024. DOI: **10.1021/acssynbio.4c00283**. URL: https://doi.org/10.1021/acssynbio.4c00283 (hurt2024directedevolutionof pages 1-3, hurt2024directedevolutionof media 720b427e, hurt2024directedevolutionof media 82d8c825, hurt2024directedevolutionof media 9d8d0096)
4. Feng R, Lan J, Goh MC, Du M, Chen Z. **Advances in the application of gas vesicles in medical imaging and disease treatment.** *Journal of Biological Engineering.* July 2024. DOI: **10.1186/s13036-024-00426-3**. URL: https://doi.org/10.1186/s13036-024-00426-3 (feng2024advancesinthe pages 2-4, feng2024advancesinthe pages 4-5, feng2024advancesinthe pages 9-10)
5. Liu T, Wang J, Liu C, Wang Y, Li Z, Yan F. **Characterization and Comparison of Contrast Imaging Properties of Naturally Isolated and Heterologously Expressed Gas Vesicles.** *Pharmaceuticals.* Published 7 Jun 2024. DOI: **10.3390/ph17060755**. URL: https://doi.org/10.3390/ph17060755 (liu2024characterizationandcomparison pages 1-2)
6. Howells AR, Welch PJ, Kim J, Forest CR, Shi C, Lian XL. **A drug-selectable acoustic reporter gene system for human cell ultrasound imaging.** *Bioengineering & Translational Medicine.* Accepted 10 Jul 2023; journal issue 2024. DOI: **10.1002/btm2.10584**. URL: https://doi.org/10.1002/btm2.10584 (howells2024adrug‐selectableacoustic pages 1-2)

**Contextual (older) sources used for compartmentalization framing**
- Chen AH, Robinson-Mosher A, Savage DF, Silver PA, Polka JK. *PLoS ONE.* 2013. DOI: **10.1371/journal.pone.0076127**. URL: https://doi.org/10.1371/journal.pone.0076127 (chen2013thebacterialcarbonfixing pages 1-2)
- Saier MH Jr. *J Mol Microbiol Biotechnol.* 2013. DOI: **10.1159/000351625**. URL: https://doi.org/10.1159/000351625 (jr.2013microcompartmentsandprotein pages 1-2)


References

1. (iburg2024elucidatingtheassembly pages 1-2): Manuel Iburg, Andrew P. Anderson, Vivian T. Wong, Erica D. Anton, Art He, and George J. Lu. Elucidating the assembly of gas vesicles by systematic protein-protein interaction analysis. The EMBO Journal, 43:4156-4172, Jul 2024. URL: https://doi.org/10.1038/s44318-024-00178-2, doi:10.1038/s44318-024-00178-2. This article has 8 citations.

2. (feng2024advancesinthe pages 2-4): Renjie Feng, Jie Lan, Meei Chyn Goh, Meng Du, and Zhiyi Chen. Advances in the application of gas vesicles in medical imaging and disease treatment. Journal of Biological Engineering, Jul 2024. URL: https://doi.org/10.1186/s13036-024-00426-3, doi:10.1186/s13036-024-00426-3. This article has 15 citations and is from a peer-reviewed journal.

3. (hurt2024directedevolutionof pages 1-3): Robert C. Hurt, Zhiyang Jin, Mohamed Soufi, Katie K. Wong, Daniel P. Sawyer, Hao K. Shen, Przemysław Dutka, Ramya Deshpande, Ruby Zhang, David R. Mittelstein, and Mikhail G. Shapiro. Directed evolution of acoustic reporter genes using high-throughput acoustic screening. ACS Synthetic Biology, 13:2215-2226, Jul 2024. URL: https://doi.org/10.1021/acssynbio.4c00283, doi:10.1021/acssynbio.4c00283. This article has 11 citations and is from a domain leading peer-reviewed journal.

4. (jazbec2024proteingasvesicles pages 1-3): Vid Jazbec, Nina Varda, Ernest Šprager, Maja Meško, Sara Vidmar, Rok Romih, Marjetka Podobnik, Andreja Kežar, Roman Jerala, and Mojca Benčina. Protein gas vesicles of <i>bacillus megaterium</i> as enhancers of ultrasound-induced transcriptional regulation. ACS Nano, 18:16692-16700, Jun 2024. URL: https://doi.org/10.1021/acsnano.4c01498, doi:10.1021/acsnano.4c01498. This article has 9 citations and is from a highest quality peer-reviewed journal.

5. (jazbec2024proteingasvesicles media 312076f3): Vid Jazbec, Nina Varda, Ernest Šprager, Maja Meško, Sara Vidmar, Rok Romih, Marjetka Podobnik, Andreja Kežar, Roman Jerala, and Mojca Benčina. Protein gas vesicles of <i>bacillus megaterium</i> as enhancers of ultrasound-induced transcriptional regulation. ACS Nano, 18:16692-16700, Jun 2024. URL: https://doi.org/10.1021/acsnano.4c01498, doi:10.1021/acsnano.4c01498. This article has 9 citations and is from a highest quality peer-reviewed journal.

6. (feng2024advancesinthe pages 4-5): Renjie Feng, Jie Lan, Meei Chyn Goh, Meng Du, and Zhiyi Chen. Advances in the application of gas vesicles in medical imaging and disease treatment. Journal of Biological Engineering, Jul 2024. URL: https://doi.org/10.1186/s13036-024-00426-3, doi:10.1186/s13036-024-00426-3. This article has 15 citations and is from a peer-reviewed journal.

7. (yang2024rapidflotationof pages 1-2): Tiantian Yang, Jiaxin Pan, Huaming Wu, Cuicui Tian, Chunbo Wang, Bangding Xiao, Min Pan, and Xingqiang Wu. Rapid flotation of microcystis wesenbergii mediated by high light exposure: implications for surface scum formation and cyanobacterial species succession. Frontiers in Plant Science, Apr 2024. URL: https://doi.org/10.3389/fpls.2024.1367680, doi:10.3389/fpls.2024.1367680. This article has 14 citations.

8. (chen2013thebacterialcarbonfixing pages 1-2): Anna H. Chen, Avi Robinson-Mosher, David F. Savage, Pamela A. Silver, and Jessica K. Polka. The bacterial carbon-fixing organelle is formed by shell envelopment of preassembled cargo. PLoS ONE, 8:e76127, Sep 2013. URL: https://doi.org/10.1371/journal.pone.0076127, doi:10.1371/journal.pone.0076127. This article has 161 citations and is from a peer-reviewed journal.

9. (jr.2013microcompartmentsandprotein pages 1-2): Milton H. Saier Jr. Microcompartments and protein machines in prokaryotes. Journal of Molecular Microbiology and Biotechnology, 23:243-269, Aug 2013. URL: https://doi.org/10.1159/000351625, doi:10.1159/000351625. This article has 42 citations and is from a peer-reviewed journal.

10. (iburg2024elucidatingtheassembly pages 2-4): Manuel Iburg, Andrew P. Anderson, Vivian T. Wong, Erica D. Anton, Art He, and George J. Lu. Elucidating the assembly of gas vesicles by systematic protein-protein interaction analysis. The EMBO Journal, 43:4156-4172, Jul 2024. URL: https://doi.org/10.1038/s44318-024-00178-2, doi:10.1038/s44318-024-00178-2. This article has 8 citations.

11. (jazbec2024proteingasvesicles pages 5-6): Vid Jazbec, Nina Varda, Ernest Šprager, Maja Meško, Sara Vidmar, Rok Romih, Marjetka Podobnik, Andreja Kežar, Roman Jerala, and Mojca Benčina. Protein gas vesicles of <i>bacillus megaterium</i> as enhancers of ultrasound-induced transcriptional regulation. ACS Nano, 18:16692-16700, Jun 2024. URL: https://doi.org/10.1021/acsnano.4c01498, doi:10.1021/acsnano.4c01498. This article has 9 citations and is from a highest quality peer-reviewed journal.

12. (feng2024advancesinthe pages 9-10): Renjie Feng, Jie Lan, Meei Chyn Goh, Meng Du, and Zhiyi Chen. Advances in the application of gas vesicles in medical imaging and disease treatment. Journal of Biological Engineering, Jul 2024. URL: https://doi.org/10.1186/s13036-024-00426-3, doi:10.1186/s13036-024-00426-3. This article has 15 citations and is from a peer-reviewed journal.

13. (howells2024adrug‐selectableacoustic pages 1-2): Alessandro R. Howells, Phoebe J. Welch, John Kim, Craig R. Forest, Chengzhi Shi, and Xiaojun Lance Lian. A drug‐selectable acoustic reporter gene system for human cell ultrasound imaging. Bioengineering & Translational Medicine, Aug 2024. URL: https://doi.org/10.1002/btm2.10584, doi:10.1002/btm2.10584. This article has 4 citations.

14. (liu2024characterizationandcomparison pages 1-2): Tingting Liu, Jieqiong Wang, Chenxing Liu, Yuanyuan Wang, Zhenzhou Li, and Fei Yan. Characterization and comparison of contrast imaging properties of naturally isolated and heterologously expressed gas vesicles. Pharmaceuticals, 17:755, Jun 2024. URL: https://doi.org/10.3390/ph17060755, doi:10.3390/ph17060755. This article has 3 citations.

15. (hurt2024directedevolutionof media 720b427e): Robert C. Hurt, Zhiyang Jin, Mohamed Soufi, Katie K. Wong, Daniel P. Sawyer, Hao K. Shen, Przemysław Dutka, Ramya Deshpande, Ruby Zhang, David R. Mittelstein, and Mikhail G. Shapiro. Directed evolution of acoustic reporter genes using high-throughput acoustic screening. ACS Synthetic Biology, 13:2215-2226, Jul 2024. URL: https://doi.org/10.1021/acssynbio.4c00283, doi:10.1021/acssynbio.4c00283. This article has 11 citations and is from a domain leading peer-reviewed journal.

16. (hurt2024directedevolutionof media 82d8c825): Robert C. Hurt, Zhiyang Jin, Mohamed Soufi, Katie K. Wong, Daniel P. Sawyer, Hao K. Shen, Przemysław Dutka, Ramya Deshpande, Ruby Zhang, David R. Mittelstein, and Mikhail G. Shapiro. Directed evolution of acoustic reporter genes using high-throughput acoustic screening. ACS Synthetic Biology, 13:2215-2226, Jul 2024. URL: https://doi.org/10.1021/acssynbio.4c00283, doi:10.1021/acssynbio.4c00283. This article has 11 citations and is from a domain leading peer-reviewed journal.

17. (hurt2024directedevolutionof media 9d8d0096): Robert C. Hurt, Zhiyang Jin, Mohamed Soufi, Katie K. Wong, Daniel P. Sawyer, Hao K. Shen, Przemysław Dutka, Ramya Deshpande, Ruby Zhang, David R. Mittelstein, and Mikhail G. Shapiro. Directed evolution of acoustic reporter genes using high-throughput acoustic screening. ACS Synthetic Biology, 13:2215-2226, Jul 2024. URL: https://doi.org/10.1021/acssynbio.4c00283, doi:10.1021/acssynbio.4c00283. This article has 11 citations and is from a domain leading peer-reviewed journal.