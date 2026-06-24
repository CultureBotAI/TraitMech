---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:05:15.426679'
end_time: '2026-06-18T09:20:25.034557'
duration_seconds: 909.61
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: polyhydroxyalkanoate granule
  trait_identifier: traitmech:000067
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: polyhydroxyalkanoate_granule
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An intracellular storage inclusion composed of polyhydroxyalkanoate
    (e.g. polyhydroxybutyrate, PHB), a carbon and energy reserve accumulated as cytoplasmic
    granules.
  parent_traits: traitmech:000066
  synonyms: PHB granule, polyhydroxybutyrate inclusion
  evidence_summary: 'DOI:10.1128/mr.54.4.450-472.1990:  (Anderson & Dawes describe
    polyhydroxyalkanoates (chiefly PHB) as carbon/energy reserves stored as cytoplasmic
    granules.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include storage
    granules such as PHA bodies among bacterial intracellular organelles.)'
  causal_graph_summary: 'pha_granule_carbon_energy_storage: 3 nodes, 2 edges'
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
- **Trait label:** polyhydroxyalkanoate granule
- **METPO identifier:** traitmech:000067
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular storage inclusion composed of polyhydroxyalkanoate (e.g. polyhydroxybutyrate, PHB), a carbon and energy reserve accumulated as cytoplasmic granules.
- **Parent traits:** traitmech:000066
- **Synonyms:** PHB granule, polyhydroxybutyrate inclusion
- **Existing evidence:** DOI:10.1128/mr.54.4.450-472.1990:  (Anderson & Dawes describe polyhydroxyalkanoates (chiefly PHB) as carbon/energy reserves stored as cytoplasmic granules.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include storage granules such as PHA bodies among bacterial intracellular organelles.)
- **Existing causal graph summary:** pha_granule_carbon_energy_storage: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **polyhydroxyalkanoate granule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/polyhydroxyalkanoate_granule.yaml`.

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
- **Trait label:** polyhydroxyalkanoate granule
- **METPO identifier:** traitmech:000067
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular storage inclusion composed of polyhydroxyalkanoate (e.g. polyhydroxybutyrate, PHB), a carbon and energy reserve accumulated as cytoplasmic granules.
- **Parent traits:** traitmech:000066
- **Synonyms:** PHB granule, polyhydroxybutyrate inclusion
- **Existing evidence:** DOI:10.1128/mr.54.4.450-472.1990:  (Anderson & Dawes describe polyhydroxyalkanoates (chiefly PHB) as carbon/energy reserves stored as cytoplasmic granules.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include storage granules such as PHA bodies among bacterial intracellular organelles.)
- **Existing causal graph summary:** pha_granule_carbon_energy_storage: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **polyhydroxyalkanoate granule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/polyhydroxyalkanoate_granule.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Polyhydroxyalkanoate Granule (METPO: traitmech:000067)

### 1) Scope summary (trait meaning, boundaries, and definitions)

**Trait definition (curation-ready):** A polyhydroxyalkanoate (PHA) granule (often PHB granule) is a **discrete, intracellular, membraneless inclusion** comprising a **hydrophobic PHA/PHB polymer core** and a **proteinaceous boundary/coat enriched in granule-associated proteins (GAPs)** (e.g., PhaP phasins, PhaC synthase, PhaZ depolymerase, regulators), functioning primarily as a **carbon and energy reserve** that can be mobilized during starvation or carbon limitation. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4, koning2023thephbgranule pages 1-4, martinez2023polyhydroxybutyratemetabolismin pages 2-5)

**Composition and architecture:** Recent reviews and mechanistic work converge on a model where granules are primarily polymer, with a smaller fraction of GAPs; one review cites a typical PHB granule as ~**98% polymer and ~2% GAPs**, with growing PHB chains in the core surrounded by GAPs (including phasins that stabilize/coats PHB chains and control granule size). (martinez2023polyhydroxybutyratemetabolismin pages 2-5)

**Membraneless boundary:** PHB granules are widely treated as **lipid-free/membrane-free** organelles; cryo-EM/tomographic evidence in Caulobacter supports a **discontinuous, likely proteinaceous boundary** rather than a phospholipid bilayer. (koning2023thephbgranule pages 1-4, koning2023thephbgranule media 969dc70e, koning2023thephbgranule media 993d0652)

**Boundary cases / nearby traits that should not be conflated:**
- **Other intracellular storage inclusions**: glycogen granules, polyphosphate granules, sulfur globules, etc. (not directly evidenced in retrieved texts, so treat as conceptual boundary; do not curate cross-claims without sources).
- **Non-granule PHB forms**: Reusch distinguishes high-molecular-mass PHB in **discrete cytoplasmic granules** from a low-molecular-mass **complexed PHB (cPHB)** found associated with membranes and other macromolecular complexes; this supports a boundary between “PHB granule” vs “PHB complex in membranes.” (reusch1992biologicalcomplexesof pages 1-3)

**Assay/observation scope:** Granules are commonly observed by **transmission electron microscopy** and can be stained with **lipophilic dyes** such as **Nile Red** (useful for visualization but not necessarily quantitative). (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 4-6)

---

### 2) Key concepts and current mechanistic understanding

#### 2.1 Core metabolic pathway concept: storage polymer synthesis and mobilization
- **Biosynthesis (canonical scl-PHB):** acetyl-CoA-derived pathway catalyzed by **PhaA (β-ketothiolase; EC 2.3.1.9)** → **PhaB (acetoacetyl-CoA reductase; EC 1.1.1.36)** → **PhaC (PHA/PHB synthase/polymerase)** producing PHB from β-hydroxybutyryl-CoA. (martinez2023polyhydroxybutyratemetabolismin pages 2-5)
- **Mobilization/turnover:** mobilization proceeds via **PhaZ (PHB depolymerase)** releasing β-hydroxybutyrate that is metabolized back into central metabolism (e.g., acetyl-CoA). (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 4-6, martinez2023polyhydroxybutyratemetabolismin pages 2-5)

#### 2.2 Granule as a protein-decorated organelle (“carbonosome” framing)
Recent sources describe PHA/PHB granules as “membraneless organelles” in which amphiphilic surface proteins create a **functional boundary** between hydrophobic polymer and aqueous cytosol, and coordinate synthesis/mobilization. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4, koning2023thephbgranule pages 1-4)

#### 2.3 Granule-associated proteins: coat, regulation, anchoring, and stage-specific recruitment
- **PhaP (phasin):** amphiphilic granule surface protein that forms a boundary between hydrophobic polymer and cytosol and stabilizes/coats PHB chains; also influences granule morphology/size/number. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4, martinez2023polyhydroxybutyratemetabolismin pages 2-5)
- **PhaR:** transcriptional repressor regulating phasin genes; repression can be relieved by PhaR binding to nascent granules (a “sensor”/switch behavior). (santolin2024elucidatingregulationof pages 1-2)
- **PhaM (in Cupriavidus/C. necator models):** anchors granules to the nucleoid and affects granule number; also described forming an initiation complex with PhaC1 and supporting equal partitioning to daughter cells. (santolin2024elucidatingregulationof pages 1-2, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
- **PhaZ (depolymerase):** recruited to mature granules in the Caulobacter biogenesis model and depolymerizes amorphous PHB. (koning2023thephbgranule pages 1-4)

---

### 3) Recent developments and latest research (prioritizing 2023–2024)

#### 3.1 2024: Transcriptional regulation tied to granule association (Cupriavidus/Ralstonia model)
A 2024 *Journal of Biological Chemistry* paper synthesizes evidence for a regulatory architecture where **PhaR represses phaP promoters**, but **this repression is released when PhaR binds nascent granules**, and where **PhaM forms an initiation complex with PhaC1**, links granules to nucleoids, and supports partitioning. This supports graph edges linking **regulators and structural proteins directly to the granule state** rather than only to transcription. (santolin2024elucidatingregulationof pages 1-2)

#### 3.2 2024: Granule surface ecology (phasins + enzymes) and environmental drivers
A 2024 *Molecules* review states that PHA accumulation is stimulated by **high C/N** and limitation of **N/S/P**, and that granule surfaces are coated predominantly by **PhaP** forming a boundary between hydrophobic polymer and hydrophilic cytosol; the remaining surface is covered by polymerases and depolymerases; it also describes **PhaM anchoring** and granule-number effects in C. necator. This provides recent, curation-friendly summaries for environment→accumulation and protein-coat edges. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)

#### 3.3 2023: Mechanistic biogenesis pathway in Caulobacter (preprint; image-backed)
A 2023 bioRxiv study proposes and supports a stepwise model: **PhaC forms foci to initiate granule formation**, followed by recruitment/condensation of **PhaP** via direct interaction; during maturation, **PhaC dissociates** and **PhaZ is recruited** to mature granules. This work also reports a **discontinuous, likely proteinaceous boundary** in cryo-EM/tomography. While preprint status requires caution, it provides unusually explicit mechanistic edges and visual schematics. (koning2023thephbgranule pages 1-4, koning2023thephbgranule media 969dc70e, koning2023thephbgranule media 993d0652)

#### 3.4 2023: Physiological triggers and quantitative composition (Azospirillum review)
A 2023 *Polymers* review describes PHB granules (“carbonosomes”) with a typical **~98% polymer / ~2% granule-associated proteins** composition, and links accumulation to **high C/N and microaerophilic conditions**, with mobilization during **starvation/exogenous carbon depletion** via **PhaZ**. (martinez2023polyhydroxybutyratemetabolismin pages 2-5)

---

### 4) Current applications and real-world implementations

Although TraitMech focuses on **morphology**, PHA granules are also the intracellular basis for **bioplastic production pipelines**.

- **Industrial/bioprocess relevance:** PHA is accumulated intracellularly as granules and later extracted/processed. The 2024 *Molecules* review emphasizes engineering strains (including autotroph/methylotroph strategies) and highlights high intracellular PHA content as a key goal. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
- **Feedstock/waste bioconversion to PHA:** A 2024 paper demonstrates a microbial platform for converting **waste cooking oil** into medium-chain-length PHA (mcl-PHA), illustrating real-world feedstock integration (though the mechanistic granule details were not extracted here). DOI:10.1007/s13205-024-04048-w (Aug 2024) https://doi.org/10.1007/s13205-024-04048-w (retrieved but not deeply evidentiary-scanned for granule mechanistic edges).

**Graph-relevant link:** Applications often motivate genetic strategies that alter granule morphology (e.g., phasin manipulation generating single large granules), which may be important when curating morphology edges, but should be curated only when mechanistically supported and taxon-scoped. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 6-8)

---

### 5) Candidate causal-graph nodes (grouped by type)

#### Trait node
- **polyhydroxyalkanoate granule** — METPO: **traitmech:000067**

#### Cellular structures / localizations
- cytosol (label)
- nucleoid (label) (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
- “granule surface / boundary layer” (label) (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)

#### Pathways / processes
- PHA/PHB biosynthesis (label) (martinez2023polyhydroxybutyratemetabolismin pages 2-5)
- PHA/PHB mobilization/degradation (label) (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 4-6, martinez2023polyhydroxybutyratemetabolismin pages 2-5)
- granule biogenesis / initiation (label) (koning2023thephbgranule pages 1-4)
- partitioning/segregation to daughter cells (label) (santolin2024elucidatingregulationof pages 1-2)

#### Genes / proteins (granule-associated)
- **PhaA / PhbA** (β-ketothiolase; EC 2.3.1.9) (martinez2023polyhydroxybutyratemetabolismin pages 2-5)
- **PhaB / PhbB** (acetoacetyl-CoA reductase; EC 1.1.1.36) (martinez2023polyhydroxybutyratemetabolismin pages 2-5)
- **PhaC / PhbC** (PHA synthase / polymerase; EC ambiguous across classes) (martinez2023polyhydroxybutyratemetabolismin pages 2-5)
- **PhaP** (phasin family proteins; amphiphilic coat) (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4, martinez2023polyhydroxybutyratemetabolismin pages 2-5)
- **PhaR** (transcriptional repressor; phasin regulation; granule-binding switch) (santolin2024elucidatingregulationof pages 1-2, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
- **PhaM** (granule–nucleoid anchoring, granule number and partitioning; C. necator/Cupriavidus context) (santolin2024elucidatingregulationof pages 1-2, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
- **PhaZ / PhbZ** (PHA depolymerase; mobilization; recruited to mature granules in Caulobacter model) (koning2023thephbgranule pages 1-4, martinez2023polyhydroxybutyratemetabolismin pages 2-5)

#### Chemicals / metabolites (suggest CHEBI grounding where available)
- polyhydroxyalkanoate (PHA) (CHEBI label)
- poly(3-hydroxybutyrate) (PHB) (CHEBI label) (koning2023thephbgranule pages 1-4)
- acetyl-CoA (CHEBI label)
- β-hydroxybutyrate (CHEBI label) (martinez2023polyhydroxybutyratemetabolismin pages 2-5)

#### Environmental / experimental factors (suggest ENVO labels)
- high carbon-to-nitrogen ratio (high C/N) (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
- nitrogen limitation; phosphorus limitation; sulfur limitation (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
- microaerophilic/low oxygen conditions (martinez2023polyhydroxybutyratemetabolismin pages 2-5)
- carbon starvation / exogenous carbon depletion (koning2023thephbgranule pages 1-4, martinez2023polyhydroxybutyratemetabolismin pages 2-5)

---

### 6) Evidence-backed candidate causal edges (table)

The table below is intended to be directly reusable during YAML authoring (with taxon- and evidence-strength caveats noted).

| Edge (subject–predicate–object) | Evidence snippet (quoted) | Source (DOI + year + URL) | Notes/uncertainty | Suggested ontology grounding (CURIEs where plausible) |
|---|---|---|---|---|
| high C/N ratio or N/S/P limitation → increases → polyhydroxyalkanoate accumulation / polyhydroxyalkanoate granule | “PHA accumulation is stimulated by a high C/N ratio, depletion of N, S, and P, or a low rate of respiration.” (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4) | doi:10.3390/molecules29102293 (2024) https://doi.org/10.3390/molecules29102293 | Broad review claim across bacteria; suitable as environment→process edge rather than direct morphology edge. | subject: ENVO:high carbon-to-nitrogen ratio [label], ENVO:nitrogen limitation [label], ENVO:phosphorus limitation [label], ENVO:sulfur limitation [label]; predicate: increases; object: CHEBI:polyhydroxyalkanoate [label], METPO:traitmech:000067 |
| nutrient limitation + excess carbon → induces → PHA accumulation | “Environmental triggers include nutrient limitation and excess carbon that induce PHA accumulation…” (santolin2024elucidatingregulationof pages 1-2) | doi:10.1016/j.jbc.2024.107523 (2024) https://doi.org/10.1016/j.jbc.2024.107523 | Generalized from review/introduction in a mechanistic paper; curate as supportive, not sole evidence. | subject: ENVO:nutrient limitation [label], CHEBI:carbon [label]; object: CHEBI:polyhydroxyalkanoate [label], METPO:traitmech:000067 |
| microaerobic / low-oxygen conditions → increases → PHB accumulation | “PHB accumulates under high C/N and microaerophilic conditions…” (martinez2023polyhydroxybutyratemetabolismin pages 2-5) | doi:10.3390/polym15143027 (2023) https://doi.org/10.3390/polym15143027 | Species-focused review with broader relevance; oxygen effect can be taxon- and condition-dependent. | subject: ENVO:microaerobic environment [label]; object: CHEBI:poly(3-hydroxybutyrate) [label], METPO:traitmech:000067 |
| PhaA (β-ketothiolase) → participates_in → PHB biosynthetic pathway | “PHB biosynthesis is performed by PhbA (β-ketothiolase), PhbB (acetoacetyl-CoA reductase), and PhbC (PHB synthase/polymerase)…” (martinez2023polyhydroxybutyratemetabolismin pages 2-5) | doi:10.3390/polym15143027 (2023) https://doi.org/10.3390/polym15143027 | Canonical pathway; PhbA/PhaA naming varies by taxon. | subject: EC:2.3.1.9; predicate: participates_in; object: PHB biosynthetic pathway [label], CHEBI:acetyl-CoA |
| PhaB (acetoacetyl-CoA reductase) → participates_in → PHB biosynthetic pathway | “PHB biosynthesis is performed by PhbA (β-ketothiolase), PhbB (acetoacetyl-CoA reductase), and PhbC…” (martinez2023polyhydroxybutyratemetabolismin pages 2-5) | doi:10.3390/polym15143027 (2023) https://doi.org/10.3390/polym15143027 | Canonical pathway; reductant usage may vary (NADH/NADPH). | subject: EC:1.1.1.36; predicate: participates_in; object: PHB biosynthetic pathway [label] |
| PhaC (PHB synthase/polymerase) → catalyzes → PHB polymerization | “PhbC polymerizing β-hydroxybutyryl-CoA into PHB.” (martinez2023polyhydroxybutyratemetabolismin pages 2-5) | doi:10.3390/polym15143027 (2023) https://doi.org/10.3390/polym15143027 | Strong canonical edge for pathway core. | subject: EC:2.3.1.- [PHA synthase label]; predicate: catalyzes; object: CHEBI:poly(3-hydroxybutyrate) [label] |
| PhaC activity → required_for → PHB granule biogenesis | “Granule biogenesis requires an active PhaC and accumulation of PHB…” (koning2023thephbgranule pages 1-4) | doi:10.1101/2023.07.06.548030 (2023) https://doi.org/10.1101/2023.07.06.548030 | Strong mechanistic evidence but from bioRxiv and Caulobacter; mark taxon-specific/uncertain until peer-reviewed confirmation. | subject: PhaC [label]; predicate: required_for; object: METPO:traitmech:000067 |
| PhaC condensation into foci → initiates → granule formation | “PhaC condensation into foci initiates granule formation…” (koning2023thephbgranule pages 1-4) | doi:10.1101/2023.07.06.548030 (2023) https://doi.org/10.1101/2023.07.06.548030 | Mechanistic and useful for graph, but currently Caulobacter-specific and preprint-based. | subject: PhaC focus/condensate [label]; predicate: initiates; object: METPO:traitmech:000067 |
| PhaC → directly_binds → PhaP | “PhaC directly binds PhaP via an intrinsically disordered N-terminal domain…” (koning2023thephbgranule pages 1-4) | doi:10.1101/2023.07.06.548030 (2023) https://doi.org/10.1101/2023.07.06.548030 | Direct interaction shown in Caulobacter; taxon-specific/uncertain for broad curation. | subject: PhaC [label]; predicate: directly_binds; object: PhaP [label] |
| PhaC → recruits → PhaP to nascent granule | “…granule formation and is closely followed by recruitment/condensation of phasin (PhaP).” (koning2023thephbgranule pages 1-4) | doi:10.1101/2023.07.06.548030 (2023) https://doi.org/10.1101/2023.07.06.548030 | Recruitment sequence inferred from temporal imaging; useful but preprint/taxon-specific. | subject: PhaC [label]; predicate: recruits; object: PhaP [label] |
| PhaP (phasin) → forms_boundary_between → hydrophobic PHA and cytosol | “PhaP… ‘forms a boundary between the hydrophobic PHA chains and hydrophilic cytosol.’” (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4) | doi:10.3390/molecules29102293 (2024) https://doi.org/10.3390/molecules29102293 | Strong structural edge from recent review. | subject: PhaP [label]; predicate: forms_boundary_between; object: CHEBI:polyhydroxyalkanoate [label] / cytosol [label] |
| PhaP (phasin) → stabilizes → PHB chains / granule boundary | “Phasins are GAPs that ‘coat and stabilize PHB chains’…” (martinez2023polyhydroxybutyratemetabolismin pages 2-5) | doi:10.3390/polym15143027 (2023) https://doi.org/10.3390/polym15143027 | Strong and broadly applicable for granule coat function. | subject: PhaP [label]; predicate: stabilizes; object: CHEBI:poly(3-hydroxybutyrate) [label], METPO:traitmech:000067 |
| PhaP (phasin) → controls → granule size/number | “…and ‘control the size of the PHB granules’…” (martinez2023polyhydroxybutyratemetabolismin pages 2-5) | doi:10.3390/polym15143027 (2023) https://doi.org/10.3390/polym15143027 | Good high-level edge; exact phenotype can vary by phasin paralog and taxon. | subject: PhaP [label]; predicate: controls; object: PHB granule size/number [label] |
| phaP1 deletion → causes → fewer but larger granules | “deletion of phaP1 yields fewer but larger granules…” (martinez2023polyhydroxybutyratemetabolismin pages 5-6) | doi:10.3390/polym15143027 (2023) https://doi.org/10.3390/polym15143027 | Mutant phenotype; taxon-specific (Azospirillum) and gene-paralog-specific. | subject: phaP1 loss-of-function [label]; predicate: causes; object: fewer/larger PHB granules [label] |
| PhaR → represses_transcription_of → phaP | “PhaR is a transcriptional repressor that binds phaP promoters and represses their transcription…” (santolin2024elucidatingregulationof pages 1-2) | doi:10.1016/j.jbc.2024.107523 (2024) https://doi.org/10.1016/j.jbc.2024.107523 | Strong regulatory edge. | subject: PhaR [label]; predicate: represses_transcription_of; object: phaP [label] |
| PhaR binding to nascent granules → relieves → phaP repression | “this repression is released when PhaR binds nascent PHA granules…” (santolin2024elucidatingregulationof pages 1-2) | doi:10.1016/j.jbc.2024.107523 (2024) https://doi.org/10.1016/j.jbc.2024.107523 | Strong causal regulatory switch; wording may differ by organism. | subject: PhaR–granule binding [label]; predicate: relieves; object: phaP repression [label] |
| PhaR displaced by PhaP on granule surface → enables → upstream phaP repression | “phasin has higher affinity and displaces PhaR, which then binds upstream of phaP and represses its expression.” (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4) | doi:10.3390/molecules29102293 (2024) https://doi.org/10.3390/molecules29102293 | Supports dynamic competition model; may be best represented as two edges in final graph. | subject: PhaP [label]; predicate: displaces_from; object: PhaR on granule surface [label] |
| PhaM → anchors → PHA granule to nucleoid | “In C. necator, PhaM anchors granules to the nucleoid…” (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4) | doi:10.3390/molecules29102293 (2024) https://doi.org/10.3390/molecules29102293 | Useful but explicitly organism-specific (Cupriavidus necator). | subject: PhaM [label]; predicate: anchors; object: PHA granule [label] / nucleoid [label] |
| PhaM → affects → granule number | “PhaM anchors the granule to the nucleoid and affects the total number of granules in the cell.” (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4) | doi:10.3390/molecules29102293 (2024) https://doi.org/10.3390/molecules29102293 | Organism-specific (C. necator); acceptable as uncertain edge. | subject: PhaM [label]; predicate: affects; object: granule number [label] |
| PhaM–PhaC1 initiation complex → contributes_to → equal partitioning among daughter cells | “PhaM forms an initiation complex with PhaC1 and links granules to the nucleoid, contributing to equal partitioning among daughter cells.” (santolin2024elucidatingregulationof pages 1-2) | doi:10.1016/j.jbc.2024.107523 (2024) https://doi.org/10.1016/j.jbc.2024.107523 | Strong but taxon-specific to Ralstonia/Cupriavidus models. | subject: PhaM–PhaC1 complex [label]; predicate: contributes_to; object: granule partitioning to daughter cells [label] |
| PhaZ → is_recruited_to → mature granules | “As granules mature, PhaC dissociates and the PHB depolymerase PhaZ is recruited…” (koning2023thephbgranule pages 1-4) | doi:10.1101/2023.07.06.548030 (2023) https://doi.org/10.1101/2023.07.06.548030 | Mechanistic recruitment sequence from Caulobacter preprint; taxon-specific/uncertain. | subject: PhaZ [label]; predicate: is_recruited_to; object: mature PHB granule [label] |
| PhaZ → depolymerizes → amorphous PHB | “PhaZ specifically degrades amorphous PHB…” (koning2023thephbgranule pages 1-4) | doi:10.1101/2023.07.06.548030 (2023) https://doi.org/10.1101/2023.07.06.548030 | Strong mechanistic claim but from preprint for this granule-stage specificity. | subject: PhaZ [label]; predicate: depolymerizes; object: CHEBI:poly(3-hydroxybutyrate) [label] |
| PhaZ / PhbZ depolymerase → mediates → PHB mobilization | “PHB mobilization involves a PHB depolymerase (PhbZ/PhaZ) that cleaves PHB to β-hydroxybutyrate…” (martinez2023polyhydroxybutyratemetabolismin pages 2-5) | doi:10.3390/polym15143027 (2023) https://doi.org/10.3390/polym15143027 | Strong canonical mobilization edge. | subject: PhaZ [label]; predicate: mediates; object: PHB mobilization [label] |
| carbon starvation / external carbon depletion → increases → PHB consumption / mobilization | “PHB consumption increases during carbon starvation…” (koning2023thephbgranule pages 1-4) | doi:10.1101/2023.07.06.548030 (2023) https://doi.org/10.1101/2023.07.06.548030 | Supported also by review wording on starvation/exogenous carbon depletion; useful environment→mobilization edge. | subject: carbon starvation [label]; predicate: increases; object: PHB mobilization [label] |
| starvation or exogenous carbon depletion → triggers → PHB degradation | “PHB… is degraded during starvation/exogenous carbon depletion or stationary phase…” (martinez2023polyhydroxybutyratemetabolismin pages 2-5) | doi:10.3390/polym15143027 (2023) https://doi.org/10.3390/polym15143027 | Broad physiological edge; less direct to morphology but important for reserve turnover. | subject: starvation [label], exogenous carbon depletion [label]; predicate: triggers; object: PHB degradation [label] |
| polyhydroxyalkanoate granule → serves_as → intracellular carbon and energy reserve | “These serve as carbon and energy storage for the cell.” (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4) | doi:10.3390/molecules29102293 (2024) https://doi.org/10.3390/molecules29102293 | Core trait-defining edge; good anchor edge for graph. | subject: METPO:traitmech:000067; predicate: serves_as; object: carbon and energy reserve [label] |


*Table: This table lists candidate causal edges for curation of the polyhydroxyalkanoate granule TraitMech graph, with quoted evidence, source metadata, uncertainty notes, and suggested ontology grounding. It emphasizes mechanistic links among environmental triggers, biosynthetic enzymes, granule-associated proteins, regulators, and mobilization processes.*

**Image-based mechanistic support (granule biogenesis):** The Caulobacter preprint includes a schematic of a stepwise biogenesis pathway (PhaC focus initiation → PhaP recruitment → PhaZ recruitment) and cryo-CLEM/tomography illustrating immature vs mature granule architecture and boundary features. (koning2023thephbgranule media 969dc70e, koning2023thephbgranule media 993d0652)

---

### 7) Statistics and data points (recent studies/reviews)

- **Granule composition estimate:** PHB granules reported as ~**98% polymer** and ~**2% granule-associated proteins** (GAPs) in a 2023 review. (martinez2023polyhydroxybutyratemetabolismin pages 2-5)
- **Environmental enrichment condition:** High C/N ratio and depletion of N/S/P are repeatedly cited as conditions that stimulate PHA accumulation. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)

*Note:* Many industrial performance statistics (titers/productivities, kg-scale) are outside the current evidence excerpts; they should be added only after extracting explicit numeric values from bioprocess papers.

---

### 8) Expert opinions / analysis (authoritative synthesis)

**Convergent expert view:** Across modern reviews and mechanistic studies, PHA granules are increasingly treated not as passive “blobs” of polymer but as **organized, protein-decorated organelles** whose formation, morphology, and inheritance depend on specific proteins (phasins, synthases, anchoring factors) and regulatory switches that sense the presence of polymer/granules. (santolin2024elucidatingregulationof pages 1-2, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4, koning2023thephbgranule pages 1-4)

**Curation implication:** It is appropriate to represent granule morphology as a causal outcome of (i) polymer synthesis capacity (PhaA/B/C), (ii) surface-coat assembly (PhaP), (iii) regulatory feedback (PhaR), and (iv) spatial organization/partitioning (PhaM) where supported and taxon-scoped. (santolin2024elucidatingregulationof pages 1-2, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4, koning2023thephbgranule pages 1-4)

---

### 9) Warnings / claims not yet ready for broad curation

1. **Preprint-derived edges (Caulobacter biogenesis pathway):** Edges such as “PhaC condensation into foci initiates granule formation” and “PhaZ is recruited to mature granules” are mechanistically compelling but are supported here by a **bioRxiv preprint** and may be **taxon-specific**; curate as **uncertain** or scope explicitly to *Caulobacter* until peer-reviewed replication/generalization. (koning2023thephbgranule pages 1-4, koning2023thephbgranule media 969dc70e, koning2023thephbgranule media 993d0652)
2. **Organism-specific anchoring factor (PhaM):** PhaM anchoring to the nucleoid and effects on granule number/partitioning are described in the **C. necator/Cupriavidus/Ralstonia** context; do not generalize to all PHA producers without additional sources. (santolin2024elucidatingregulationof pages 1-2, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
3. **Boundary vs membrane terminology:** Older literature sometimes describes a “granule-bounding membrane,” but newer cryo-EM-informed sources emphasize a **proteinaceous boundary** and lipid-free granules; curate the “no phospholipid membrane” claim with modern evidence. (koning2023thephbgranule pages 1-4, koning2023thephbgranule pages 15-18)

---

## DOI-first bibliography (with publication dates and URLs)

1. **Santolin L, et al.** *Elucidating regulation of polyhydroxyalkanoate metabolism in Ralstonia eutropha: Identification of transcriptional regulators from phasin and depolymerase genes.* **Journal of Biological Chemistry** (Aug **2024**). DOI: **10.1016/j.jbc.2024.107523**. https://doi.org/10.1016/j.jbc.2024.107523 (santolin2024elucidatingregulationof pages 1-2)
2. **Fukala I, Kučera I.** *Natural Polyhydroxyalkanoates—An Overview of Bacterial Production Methods.* **Molecules** (May **2024**). DOI: **10.3390/molecules29102293**. https://doi.org/10.3390/molecules29102293 (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4)
3. **Martínez Martínez MdLA, et al.** *Polyhydroxybutyrate Metabolism in Azospirillum brasilense and Its Applications, a Review.* **Polymers** (Jul **2023**). DOI: **10.3390/polym15143027**. https://doi.org/10.3390/polym15143027 (martinez2023polyhydroxybutyratemetabolismin pages 2-5)
4. **de Koning EA, et al.** *The PHB Granule Biogenesis Pathway in Caulobacter.* **bioRxiv** (Jul **2023**). DOI: **10.1101/2023.07.06.548030**. https://doi.org/10.1101/2023.07.06.548030 (koning2023thephbgranule pages 1-4, koning2023thephbgranule media 969dc70e, koning2023thephbgranule media 993d0652)
5. **Reusch RN.** *Biological complexes of poly-β-hydroxybutyrate.* **FEMS Microbiology Letters** (Dec **1992**). DOI: **10.1111/j.1574-6968.1992.tb05829.x**. https://doi.org/10.1111/j.1574-6968.1992.tb05829.x (reusch1992biologicalcomplexesof pages 1-3)
6. **Anderson AJ, Dawes EA.** *Occurrence, metabolism, metabolic role, and industrial uses of bacterial polyhydroxyalkanoates.* **Microbiological Reviews** (Dec **1990**). DOI: **10.1128/mr.54.4.450-472.1990**. https://doi.org/10.1128/mr.54.4.450-472.1990 (anderson1990occurrencemetabolismmetabolic pages 15-16)

---

### Appendix: Suggested YAML curation notes (high-level)

- Treat **traitmech:000067** as a morphological trait node with a mechanistic definition tied to **polymer biosynthesis + protein coat assembly**. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4, martinez2023polyhydroxybutyratemetabolismin pages 2-5)
- Prefer edges supported by **peer-reviewed 2023–2024** sources for general assertions; scope preprint/taxon-specific edges explicitly (e.g., NCBITaxon: for Caulobacter) when curating. (santolin2024elucidatingregulationof pages 1-2, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4, koning2023thephbgranule pages 1-4)


References

1. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 2-4): Ivo Fukala and Igor Kučera. Natural polyhydroxyalkanoates—an overview of bacterial production methods. Molecules, 29:2293, May 2024. URL: https://doi.org/10.3390/molecules29102293, doi:10.3390/molecules29102293. This article has 27 citations.

2. (koning2023thephbgranule pages 1-4): Edward A. de Koning, Mayura Panjalingam, Jessica Tran, Michael R. Eckhart, Peter D. Dahlberg, and Lucy Shapiro. The phb granule biogenesis pathway in caulobacter. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.06.548030, doi:10.1101/2023.07.06.548030. This article has 1 citations.

3. (martinez2023polyhydroxybutyratemetabolismin pages 2-5): María de los Ángeles Martínez Martínez, Lucía Soto Urzúa, Yovani Aguilar Carrillo, Mirian Becerril Ramírez, and Luis Javier Martínez Morales. Polyhydroxybutyrate metabolism in azospirillum brasilense and its applications, a review. Polymers, 15:3027, Jul 2023. URL: https://doi.org/10.3390/polym15143027, doi:10.3390/polym15143027. This article has 21 citations.

4. (koning2023thephbgranule media 969dc70e): Edward A. de Koning, Mayura Panjalingam, Jessica Tran, Michael R. Eckhart, Peter D. Dahlberg, and Lucy Shapiro. The phb granule biogenesis pathway in caulobacter. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.06.548030, doi:10.1101/2023.07.06.548030. This article has 1 citations.

5. (koning2023thephbgranule media 993d0652): Edward A. de Koning, Mayura Panjalingam, Jessica Tran, Michael R. Eckhart, Peter D. Dahlberg, and Lucy Shapiro. The phb granule biogenesis pathway in caulobacter. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.06.548030, doi:10.1101/2023.07.06.548030. This article has 1 citations.

6. (reusch1992biologicalcomplexesof pages 1-3): RN Reusch. Biological complexes of poly-β-hydroxybutyrate. Fems Microbiology Letters, 103:119-129, Dec 1992. URL: https://doi.org/10.1111/j.1574-6968.1992.tb05829.x, doi:10.1111/j.1574-6968.1992.tb05829.x. This article has 172 citations and is from a peer-reviewed journal.

7. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 4-6): Ivo Fukala and Igor Kučera. Natural polyhydroxyalkanoates—an overview of bacterial production methods. Molecules, 29:2293, May 2024. URL: https://doi.org/10.3390/molecules29102293, doi:10.3390/molecules29102293. This article has 27 citations.

8. (santolin2024elucidatingregulationof pages 1-2): Lara Santolin, Rosalie Sandra Josianne Eichenroth, Paul Cornehl, Henrike Wortmann, Christian Forbrig, Anne Schulze, Inam Ul Haq, Sabine Brantl, Juri Rappsilber, Sebastian Lothar Riedel, Peter Neubauer, and Matthias Gimpel. Elucidating regulation of polyhydroxyalkanoate metabolism in ralstonia eutropha: identification of transcriptional regulators from phasin and depolymerase genes. Journal of Biological Chemistry, 300:107523, Aug 2024. URL: https://doi.org/10.1016/j.jbc.2024.107523, doi:10.1016/j.jbc.2024.107523. This article has 9 citations and is from a domain leading peer-reviewed journal.

9. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 6-8): Ivo Fukala and Igor Kučera. Natural polyhydroxyalkanoates—an overview of bacterial production methods. Molecules, 29:2293, May 2024. URL: https://doi.org/10.3390/molecules29102293, doi:10.3390/molecules29102293. This article has 27 citations.

10. (martinez2023polyhydroxybutyratemetabolismin pages 5-6): María de los Ángeles Martínez Martínez, Lucía Soto Urzúa, Yovani Aguilar Carrillo, Mirian Becerril Ramírez, and Luis Javier Martínez Morales. Polyhydroxybutyrate metabolism in azospirillum brasilense and its applications, a review. Polymers, 15:3027, Jul 2023. URL: https://doi.org/10.3390/polym15143027, doi:10.3390/polym15143027. This article has 21 citations.

11. (koning2023thephbgranule pages 15-18): Edward A. de Koning, Mayura Panjalingam, Jessica Tran, Michael R. Eckhart, Peter D. Dahlberg, and Lucy Shapiro. The phb granule biogenesis pathway in caulobacter. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.06.548030, doi:10.1101/2023.07.06.548030. This article has 1 citations.

12. (anderson1990occurrencemetabolismmetabolic pages 15-16): A J Anderson and E A Dawes. Occurrence, metabolism, metabolic role, and industrial uses of bacterial polyhydroxyalkanoates. Microbiological Reviews, 54:450-472, Dec 1990. URL: https://doi.org/10.1128/mr.54.4.450-472.1990, doi:10.1128/mr.54.4.450-472.1990. This article has 4202 citations.