---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:55:11.128346'
end_time: '2026-08-04T03:03:26.837981'
duration_seconds: 495.71
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range mid2
  trait_identifier: METPO:1000462
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH range phenotype in which the growth-supporting external pH range\
    \ spans approximately 7\u20138, characteristic of neutrophile or mild-alkaliphile\
    \ physiology."
  parent_traits: METPO:1000332
  synonyms: Alkali Tolerant, Alkaliphile, Facultative acidophile, Neutrophile, pHR_7_to_8
  evidence_summary: "DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review\
    \ supports modest alkaline-tolerance physiology as the basis of growth across\
    \ pH 7\u20138.)"
  causal_graph_summary: 'ph_range_mid2_mild_alkaline_tolerance: 15 nodes, 9 edges'
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
- **Trait label:** pH range mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000462
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 7–8, characteristic of neutrophile or mild-alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Facultative acidophile, Neutrophile, pHR_7_to_8
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports modest alkaline-tolerance physiology as the basis of growth across pH 7–8.)
- **Existing causal graph summary:** ph_range_mid2_mild_alkaline_tolerance: 15 nodes, 9 edges

## Research Objective

Research the microbial trait **pH range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid2.yaml`.

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
- **Trait label:** pH range mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000462
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 7–8, characteristic of neutrophile or mild-alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Facultative acidophile, Neutrophile, pHR_7_to_8
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports modest alkaline-tolerance physiology as the basis of growth across pH 7–8.)
- **Existing causal graph summary:** ph_range_mid2_mild_alkaline_tolerance: 15 nodes, 9 edges

## Research Objective

Research the microbial trait **pH range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid2.yaml`.

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


# Curation-focused research report: microbial **pH range mid2**

## 1. Scope and current interpretation

**Target trait:** **“METPO:1000462”** (`pH range mid2`; category `ENVIRONMENT`; kind `CLASS`; parent `METPO:1000332`).

For TraitMech purposes, this trait should mean **reproducible growth across an external-pH interval approximately spanning pH 7–8**, rather than survival after a short alkaline shock, a single optimum near pH 7–8, or growth exclusively above pH 9. Its mechanistic core is the ability to keep cytoplasmic physicochemistry growth-compatible while external proton activity changes modestly. Most bacteria keep cytoplasmic pH near 7–7.5; the relevant phenotype therefore combines proton/ion homeostasis, energy transduction, and maintenance of envelope synthesis rather than requiring the specialized machinery of an obligate alkaliphile. The literature emphasizes that external-pH tolerance can extend beyond the narrower cytoplasmic-pH range that supports growth. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14, poolman2023physicochemicalhomeostasisin pages 2-4)

### Boundaries

- **Include:** strains demonstrably growing at both approximately pH 7 and pH 8 under controlled, buffered conditions.
- **Do not equate with “neutrophile”:** neutral optimum and breadth of growth range are different observations.
- **Do not equate with “alkaliphile”:** organisms whose minimum or optimum is around pH 9–10 represent a neighboring, more alkaline phenotype.
- **Do not infer from acid tolerance:** acid-resistance pathways can overlap pH homeostasis but do not establish growth through pH 7–8.
- **Do not infer from shock survival alone:** for example, *Bacillus subtilis* was 100% viable after a 30-minute pH-8.5 shock, yet this does not itself establish sustained growth across a buffered 7–8 range. (mitchell2024penicillinbindingproteinredundancy pages 8-10)
- **Treat synonyms cautiously:** “Alkali Tolerant,” “Alkaliphile,” “Facultative acidophile,” and “Neutrophile” are not exact biological equivalents. `pHR_7_to_8` is the least ambiguous synonym.

The observed range is conditional on buffer identity and capacity, Na⁺/K⁺ concentration, osmolarity, carbon and energy source, oxygen, temperature, inoculum history, and endpoint. Unbuffered media are particularly unsuitable: *B. subtilis*, for example, partially neutralized LB initially set to pH 9.4 down to pH 8.0 overnight. (mitchell2024penicillinbindingproteinredundancy pages 8-10)

## 2. Mechanistic model

The best-supported generic model is:

**external pH 7→8 shift → altered ΔpH and proton availability → respiratory/metabolic proton extrusion plus cation/H⁺ exchange preserve PMF and membrane potential → near-neutral cytoplasmic pH is maintained → ATP generation, solute transport, macromolecular function, and envelope biogenesis continue → growth across pH 7–8.**

A 2024 single-cell/modeling study of *Escherichia coli* sharpened this model. It found that lowering PMF impaired intracellular-pH maintenance and that collapsing PMF depolarized cells. Its energetic model predicts NhaB-like exchange as the minimum-cost strategy over approximately pH 5–9, directly encompassing the target interval, whereas NhaA-like exchange dominates only at approximately pH 9–12. The transporter assignment is model-based, but the PMF–pH-homeostasis relation was experimentally tested. (terradot2024escherichiacolimaintains pages 4-5, terradot2024escherichiacolimaintains pages 8-9)

The strongest recent pH-8 genetic evidence concerns envelope biogenesis. In *Vibrio cholerae*, deletion of **vca0040**, encoding a DUF368 protein, caused growth and shape defects at pH 8 but not at pH 6 or 7. The mutant contained 1.5–2-fold less peptidoglycan, accumulated the precursor UDP-M5, and showed alkaline-dependent C55-P abnormalities. Thus, mild alkaline tolerance can require conditionally robust lipid-carrier recycling and peptidoglycan production, not only cytoplasmic proton control. (sit2023undecaprenylphosphatetranslocases pages 5-8)

## 3. Candidate nodes grouped by type

### Trait and environmental/experimental nodes

- **pH range mid2:** **METPO:1000462**.
- **External pH 7–8 / mildly alkaline extracellular environment:** retain label-only unless an existing METPO/ENVO term is verified.
- **Buffered growth assay**, **growth rate**, **lag time**, **biomass yield**, and **viability after alkaline shock**: assay nodes; do not merge these outcomes.
- **Na⁺ concentration**, **K⁺ concentration**, oxygen availability, carbon/energy source, osmolarity, temperature, and buffer capacity: contextual modifiers.

### Chemicals and energetic quantities

- Proton: **CHEBI:15378**.
- Sodium ion: **CHEBI:29101**.
- Potassium ion: **CHEBI:29103**.
- ATP: **CHEBI:15422**.
- Proton-motive force, membrane potential, transmembrane pH gradient, cytoplasmic pH, and ion-motive force: label-only unless project-approved ontology mappings are verified.
- Undecaprenyl phosphate/C55-P, undecaprenyl pyrophosphate/C55-PP, UDP-N-acetylmuramyl pentapeptide/UDP-M5, and peptidoglycan: verify exact ChEBI accessions before YAML entry.

K⁺ is a major bacterial cytoplasmic cation, but concentration is highly taxon-dependent: reported values are approximately 0.2 M in *E. coli*, 0.8 M in *Lactococcus lactis*, and 2.1 M in *Haloferax volcanii*. This supports including ionic-strength context, not a universal potassium threshold. (poolman2023physicochemicalhomeostasisin pages 2-4, poolman2023physicochemicalhomeostasisin pages 4-5)

### Cellular structures and processes

- Plasma membrane: **GO:0005886**.
- Cytoplasm: **GO:0005737**.
- Cell wall, peptidoglycan layer, and extracellular/periplasmic enzyme activity: verify taxon-appropriate GO terms.
- Cytoplasmic pH homeostasis, monovalent-cation/proton antiport, oxidative phosphorylation, ATP synthesis coupled proton transport, peptidoglycan biosynthesis, C55-P recycling/translocation, cell-shape maintenance, and growth under mildly alkaline conditions: candidate process nodes; verify exact GO/Rhea mappings before curation.

### Transporters and complexes

- **NhaA** Na⁺/H⁺ antiporter; review evidence gives a 2 H⁺:1 Na⁺ stoichiometry and a major role under alkaline conditions. (krulwich2011molecularaspectsof pages 5-6)
- **NhaB** Na⁺/H⁺ antiporter; recent modeling assigns NhaB-like transport to approximately pH 5–9. (terradot2024escherichiacolimaintains pages 8-9)
- **K⁺/H⁺ antiporters:** conditional substitutes under low-Na⁺ conditions; family identity is taxon-specific. (krulwich2011molecularaspectsof pages 5-6)
- **MrpABCDEFG/MrpA:** strong alkaliphile mechanism, but evidence retrieved here is chiefly from *Bacillus* at substantially higher pH; it is not automatically a core pH-7–8 node. (krulwich2011molecularaspectsof pages 12-14)
- **F1Fo ATP synthase:** proton capture/ATP synthesis; high-pH sequence adaptations are well established in obligate alkaliphiles but are boundary evidence for this trait. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 27-28)
- Proton-pumping respiratory complexes and **cytochrome bd**: respiratory remodeling described in *E. coli* during alkaline stress. (krulwich2011molecularaspectsof pages 5-6)
- **VCA0040/DUF368**, **SAOUHSC_00846**, and **DedA/YghB-family proteins:** candidate C55-P translocases with pH-dependent requirements. Direct transport activity remains provisional. (sit2023undecaprenylphosphatetranslocases pages 5-8, sit2023undecaprenylphosphatetranslocases pages 11-15)
- **PBPH/ykuA, PBP2a/pbpA, PBP3/pbpC, PBP4/pbpD, PBP5/dacA, and PBP1a/PBP1b/ponA:** alkaline-conditioned peptidoglycan enzymes in *B. subtilis*; mostly pH ≥8.5–10.5 evidence. (mitchell2024penicillinbindingproteinredundancy pages 8-10, mitchell2024penicillinbindingproteinredundancy pages 4-6)

## 4. Candidate causal edges

The following table is the curation shortlist; the report text below supplies source snippets and interpretation.

| subject | predicate | object | candidate grounding | evidence strength/context | DOI |
|---|---|---|---|---|---|
| external alkaline pH (~8) | increases requirement for | VCA0040 / DUF368-containing protein | subject: external alkaline pH; object: VCA0040 / DUF368-containing protein | Direct, taxon-specific: *Vibrio cholerae* Δvca0040 showed a growth defect at pH 8 but not pH 6 or 7; buffered LB defects at pH ≥8, not ≤7 (sit2023undecaprenylphosphatetranslocases pages 5-8, sit2023undecaprenylphosphatetranslocases pages 18-21) | 10.1038/s41586-022-05569-1 |
| VCA0040 / DUF368-containing protein | positively regulates | cell shape integrity in alkaline conditions | subject: VCA0040 / DUF368-containing protein; object: cell shape integrity | Direct, taxon-specific: Δvca0040 cells became large spheres under alkaline conditions; acidification of spent supernatant abolished sphere induction (sit2023undecaprenylphosphatetranslocases pages 5-8, sit2023undecaprenylphosphatetranslocases pages 11-15) | 10.1038/s41586-022-05569-1 |
| VCA0040 / DUF368-containing protein | positively regulates | growth in alkaline conditions | subject: VCA0040 / DUF368-containing protein; object: growth in alkaline conditions | Direct, taxon-specific and in vivo-relevant: alkaline growth defect in *V. cholerae* and strong intestinal colonization defect in alkaline cecal fluid pH 8.5–9 (sit2023undecaprenylphosphatetranslocases pages 5-8, sit2023undecaprenylphosphatetranslocases pages 11-15) | 10.1038/s41586-022-05569-1 |
| VCA0040 / DUF368-containing protein | positively regulates | peptidoglycan production/composition | subject: VCA0040 / DUF368-containing protein; object: peptidoglycan biosynthesis/maintenance | Direct, taxon-specific: Δvca0040 had 1.5–2× less PG and UDP-M5 accumulation; defects present at neutral pH and exacerbated at alkaline pH (sit2023undecaprenylphosphatetranslocases pages 5-8, sit2023undecaprenylphosphatetranslocases pages 18-21) | 10.1038/s41586-022-05569-1 |
| DUF368-containing protein loss | causes accumulation of | undecaprenyl phosphate (C55-P) | subject: DUF368-containing protein loss; object: undecaprenyl phosphate | Direct, taxon-specific: alkaline-dependent increases in C55-P in ΔSAOUHSC_00846 *S. aureus* and Δvca0040 *V. cholerae* support impaired recycling/translocation (sit2023undecaprenylphosphatetranslocases pages 5-8, sit2023undecaprenylphosphatetranslocases pages 18-21) | 10.1038/s41586-022-05569-1 |
| candidate C55-P translocase activity (DUF368 / DedA) | positively regulates | C55-P recycling | subject: DUF368/DedA candidate C55-P translocase activity; object: C55-P recycling | Strong but partly provisional: authors propose DUF368 and DedA families as C55-P translocases; genetic/phenotypic evidence strong, biochemical proof still pending (sit2023undecaprenylphosphatetranslocases pages 18-21, sit2023undecaprenylphosphatetranslocases pages 11-15) | 10.1038/s41586-022-05569-1 |
| proton motive force | positively regulates | maintenance of near-neutral cytoplasmic pH | subject: proton motive force; object: cytoplasmic pH homeostasis | Direct in *E. coli*: lowering PMF impaired pHi maintenance; modeled/mechanistic framing shows PMF determines pHe range supporting pHi ≈7 (terradot2024escherichiacolimaintains pages 4-5, terradot2024escherichiacolimaintains pages 8-9) | 10.1103/PRXLife.2.043015 |
| proton motive force collapse | causes decrease of | membrane potential | subject: proton motive force collapse; object: membrane potential | Direct in *E. coli*: authors state collapsing PMF depolarized cells; recent single-cell study (terradot2024escherichiacolimaintains pages 8-9) | 10.1103/PRXLife.2.043015 |
| proton-ion antiporters | positively regulate | membrane potential generation | subject: proton-ion antiporters; object: membrane potential | Modeled + experimental support in *E. coli*: antiporters predicted to generate ψ by exporting other ions while importing H+; PMF dependence confirmed experimentally, transporter-specific contribution inferred/model-based (terradot2024escherichiacolimaintains pages 4-5, terradot2024escherichiacolimaintains pages 8-9) | 10.1103/PRXLife.2.043015 |
| NhaB-like antiporter | supports pHi maintenance over | intermediate external pH range (~5–9) | subject: NhaB-like antiporter; object: pHi maintenance over external pH range | Modeled in *E. coli*: minimal-cost antiporter across pHe ~5–9; relevant to pH 7–8 trait but not direct growth assay (terradot2024escherichiacolimaintains pages 8-9) | 10.1103/PRXLife.2.043015 |
| NhaA-like antiporter | supports pHi maintenance over | alkaline external pH range (~9–12) | subject: NhaA-like antiporter; object: pHi maintenance over external pH range | Modeled in *E. coli* with review support; boundary/nearby-trait evidence, more extreme than pH 7–8 (terradot2024escherichiacolimaintains pages 8-9, krulwich2011molecularaspectsof pages 5-6) | 10.1103/PRXLife.2.043015; 10.1038/nrmicro2549 |
| Na+/H+ antiporters | positively regulate | cytoplasmic pH homeostasis | subject: Na+/H+ antiporter; object: cytoplasmic pH homeostasis | Review-derived, broad bacterial mechanism: key regulators of bacterial pH homeostasis; strong background but not specific to one pH-7–8 assay (krulwich2011molecularaspectsof pages 5-6) | 10.1038/nrmicro2549 |
| K+/H+ antiporters | positively regulate | cytoplasmic pH homeostasis under Na+-poor conditions | subject: K+/H+ antiporter; object: cytoplasmic pH homeostasis | Review-derived, conditional mechanism: dominance can shift to K+/H+ antiporters when Na+ is limiting; useful conditional edge, not trait-core alone (krulwich2011molecularaspectsof pages 5-6) | 10.1038/nrmicro2549 |
| respiratory proton extrusion | positively regulates | proton motive force | subject: respiratory proton extrusion; object: proton motive force | Review-derived and foundational: central metabolism/respiration exports protons to build PMF, which underpins pH homeostasis (krulwich2011molecularaspectsof pages 5-6, terradot2024escherichiacolimaintains pages 2-3) | 10.1038/nrmicro2549; 10.1103/PRXLife.2.043015 |
| increased cytochrome bd usage / reduced proton-pumping respiratory complexes | helps maintain | cytoplasmic pH during alkaline stress | subject: respiratory chain remodeling; object: cytoplasmic pH homeostasis | Review-derived, taxon-focused (*E. coli*): described as minimizing proton loss and supporting alkaline pH homeostasis; not directly tested here at pH 7–8 growth (krulwich2011molecularaspectsof pages 5-6) | 10.1038/nrmicro2549 |
| F1Fo-ATP synthase | positively regulates | proton capture / cytoplasmic pH homeostasis | subject: ATP synthase; object: proton capture / cytoplasmic pH homeostasis | Review-derived and partly mutational in alkaliphiles: increased expression in alkaline stress in review; high-pH motifs contribute in *Bacillus* alkaliphiles, mostly extreme-pH evidence (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 27-28) | 10.1038/nrmicro2549 |
| alkaline shock (~pH 10–10.5) | inactivates | PBPH | subject: alkaline shock; object: PBPH | Direct but extreme-pH and taxon-specific: *B. subtilis* PBPH activity lost by pH 8.5–10 range; viability still 100% at pH 8.5 after 30 min, indicating shock-specific envelope response rather than trait-defining growth edge (mitchell2024penicillinbindingproteinredundancy pages 8-10, mitchell2024penicillinbindingproteinredundancy pages 4-6) | 10.1128/AEM.00548-23 |
| alkaline shock (~pH 10) | inactivates | PBP4 (pbpD) | subject: alkaline shock; object: PBP4/pbpD | Direct but extreme-pH and taxon-specific: inactivation begins around pH ~10; biochemical effect likely independent of intact-cell regulation (mitchell2024penicillinbindingproteinredundancy pages 4-6) | 10.1128/AEM.00548-23 |
| alkaline shock (~pH 10.5) | shifts activity from | PBP1a to PBP1b | subject: alkaline shock; object: PBP1a/PBP1b isoforms from ponA | Direct but extreme-pH and taxon-specific: intact cells required for PBP1b activation, implying processing or pH-sensing machinery (mitchell2024penicillinbindingproteinredundancy pages 4-6) | 10.1128/AEM.00548-23 |
| PBP2a (pbpA) | positively regulates | growth under alkaline conditions | subject: PBP2a/pbpA; object: growth under alkaline conditions | Direct but taxon-specific and above target range: PBP2a remains active under alkaline conditions; mutants more base-sensitive, suggesting alkaline-stable envelope synthesis role (mitchell2024penicillinbindingproteinredundancy pages 8-10, mitchell2024penicillinbindingproteinredundancy pages 4-6) | 10.1128/AEM.00548-23 |
| potassium ion (K+) | is a major contributor to | bacterial internal ionic strength | subject: potassium ion; object: ionic strength homeostasis | Review-derived context: K+ among most abundant cations and central to physicochemical homeostasis; supportive background node, not a direct pH 7–8 causal edge (poolman2023physicochemicalhomeostasisin pages 2-4, poolman2023physicochemicalhomeostasisin pages 4-5) | 10.1093/femsre/fuad033 |


*Table: This table summarizes the strongest candidate causal edges for the pH range mid2 trait, emphasizing direct 2023–2024 evidence where available and clearly marking review-derived, modeled, taxon-specific, and extreme-pH findings. It is designed to support TraitMech curation by separating broadly relevant mechanisms from claims that are conditional or not yet ready for direct trait-level curation.*

### Priority edges with supporting snippets

1. **External pH ~8 — increases requirement for → VCA0040/DUF368 protein.**  
   **Snippet:** “a growth defect at pH 8, but not pH 6 or 7” and defects “at pH ≥ 8, but not at pH ≤ 7.”  
   **Evidence:** Direct deletion phenotype in buffered media, *V. cholerae*. This is the strongest edge aligned with the upper boundary of **METPO:1000462**. (sit2023undecaprenylphosphatetranslocases pages 5-8)

2. **VCA0040/DUF368 — positively regulates → alkaline growth and cell-shape integrity.**  
   **Snippet:** “VCA0040 is required for *V. cholerae* cell shape integrity and growth in alkaline conditions.”  
   **Evidence:** Direct growth, morphology, complementation, and pH-manipulation evidence; taxon-specific. Acidifying spent supernatant abolished sphere induction. (sit2023undecaprenylphosphatetranslocases pages 5-8)

3. **VCA0040/DUF368 — supports → peptidoglycan production/composition.**  
   **Snippet:** the mutant had “1.5–2x less PG,” accumulated UDP-M5, and these phenotypes were “exacerbated by exposure to alkaline conditions.”  
   **Evidence:** Direct biochemical phenotype in *V. cholerae*, with a related phenotype in *S. aureus*. (sit2023undecaprenylphosphatetranslocases pages 5-8)

4. **DUF368 protein — supports → C55-P recycling/translocation — supports → peptidoglycan biogenesis.**  
   **Snippet:** alkaline-grown DUF368 mutants accumulated C55-P; the authors describe “direct evidence that C55-P homeostasis is linked to SAOUHSC_00846.”  
   **Evidence:** Strong lipidomic, genetic, antibiotic-sensitivity, and complementation evidence. However, the authors explicitly state that transport-independent activities are not definitively excluded; curate the molecular function as **candidate/uncertain**. (sit2023undecaprenylphosphatetranslocases pages 5-8, sit2023undecaprenylphosphatetranslocases pages 11-15)

5. **PMF — positively regulates → near-neutral cytoplasmic-pH maintenance.**  
   **Snippet:** “a lower magnitude PMF impaired their maintenance of pHi.”  
   **Evidence:** Recent single-cell experimental support in *E. coli* plus an integrated energetic model. This is a strong generic mechanism, although the experiments used selected external pH values rather than a full growth-range assay. (terradot2024escherichiacolimaintains pages 8-9)

6. **PMF collapse — causes → membrane depolarization.**  
   **Snippet:** “collapsing the PMF depolarised *E. coli* cells.”  
   **Evidence:** Direct physiological perturbation. (terradot2024escherichiacolimaintains pages 8-9)

7. **NhaB-like cation/H⁺ antiport — supports → pHi maintenance at external pH ~5–9.**  
   **Snippet:** the modeled minimum-cost antiporter is “NhaB-like … between 5 and 9.”  
   **Evidence:** Mechanistically relevant to pH 7–8 but **modeled**, not a knockout-based demonstration of the target trait. Curate with an inference qualifier or retain as supporting evidence. (terradot2024escherichiacolimaintains pages 8-9)

8. **Na⁺/H⁺ and K⁺/H⁺ antiport — increases proton uptake during alkaline stress → supports cytoplasmic-pH homeostasis.**  
   **Snippet:** the authoritative review describes increased cation/proton antiporter expression for active proton uptake; K⁺/H⁺ exchange can dominate when Na⁺ is scarce.  
   **Evidence:** Broad review synthesis. The edge is biologically strong, but transporter family and dominant coupling ion must be instantiated per taxon. (krulwich2011molecularaspectsof pages 5-6)

9. **Respiratory/metabolic proton extrusion — generates → PMF.**  
   **Snippet:** the 2024 model states, “metabolism powers the export of protons.”  
   **Evidence:** Foundational bioenergetic relation integrated with current electrophysiology. (terradot2024escherichiacolimaintains pages 4-5, terradot2024escherichiacolimaintains pages 2-3)

10. **Alkaline respiratory-chain remodeling — reduces proton loss → supports pHi homeostasis.**  
    **Snippet:** *E. coli* decreases proton-pumping respiratory complexes and increases non-proton-pumping cytochrome bd during alkaline stress.  
    **Evidence:** Review-derived and taxon-specific; useful as a downstream implementation, not a universal node. (krulwich2011molecularaspectsof pages 5-6)

11. **F1Fo ATP synthase — captures protons/produces ATP → supports alkaline pH homeostasis.**  
    **Snippet:** the review reports increased ATP-synthase expression under alkaline stress; high-pH mutations in alkaliphile subunits disproportionately impair activity at pH 10.5 and pH homeostasis after alkaline shifts.  
    **Evidence:** The generic energy-transduction edge is strong, but high-pH-specific motifs are extreme-alkaliphile adaptations and should not define pH 7–8 growth. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14)

12. **Alkaline-stable PBP activity — supports → growth under alkaline conditions.**  
    **Snippet:** *B. subtilis* ΔpbpA, ΔpbpC, and ΔdacA strains were more base-sensitive, while PBP2a, PBP3, and PBP5 remained active during alkaline shock.  
    **Evidence:** Direct activity labeling and mutant growth evidence, but principally at pH values above the target interval. Use as taxon-specific envelope-resilience evidence. (mitchell2024penicillinbindingproteinredundancy pages 8-10)

## 5. Recent developments, applications, and quantitative evidence

### 2023–2024 developments

- **Energetic integration:** Terradot and colleagues reframed proton-ion antiporters as generators/regulators of membrane potential, not merely proton-import devices. Their model assigns NhaB-like exchange to approximately pH 5–9 and NhaA-like exchange to approximately pH 9–12; experimentally reducing PMF impaired pHi control. This makes PMF magnitude a candidate determinant of the *breadth* of external pH compatible with homeostasis. (terradot2024escherichiacolimaintains pages 4-5, terradot2024escherichiacolimaintains pages 8-9)
- **Conditional envelope lipid-carrier recycling:** Sit and colleagues found that loss of VCA0040 produces a growth defect at pH 8 but not 6 or 7, 1.5–2-fold less peptidoglycan, and pH-dependent C55-P accumulation. In infant rabbits, Δvca0040 showed approximately 100–1,000-fold competitive impairment and approximately 1,000-fold colonization defects in intestinal fluid at pH 8.5–9, connecting mild alkaline envelope fitness to a real host environment. (sit2023undecaprenylphosphatetranslocases pages 5-8, sit2023undecaprenylphosphatetranslocases pages 11-15)
- **PBP functional specialization:** During *B. subtilis* alkaline shock, PBPH activity was lost, PBP4 inactivation began near pH 10, and activity shifted from PBP1a to PBP1b near pH 10.5. At pH 8.5, 30-minute viability was 100%; at pH 10.5 it was 40%. Alkaline conditions delayed peak exponential growth by approximately 3–7 hours. These results demonstrate envelope-enzyme specialization but mostly characterize a neighboring, more severe phenotype. (mitchell2024penicillinbindingproteinredundancy pages 8-10, mitchell2024penicillinbindingproteinredundancy pages 4-6)
- **Physicochemical-homeostasis framework:** Poolman’s 2023 review emphasizes that pH, PMF, ionic strength, osmotic pressure, crowding, and energy state are interdependent. This argues against curating pH range as an isolated linear pathway. (poolman2023physicochemicalhomeostasisin pages 2-4, poolman2023physicochemicalhomeostasisin pages 4-5)

### Current and potential applications

1. **Pathogen fitness and antimicrobial targeting.** C55-P recycling was required for *V. cholerae* shape and fitness in the alkaline intestine. The *S. aureus* DUF368 mutant was more than 64-fold more sensitive to amphomycin under alkaline conditions, suggesting conditional vulnerabilities in cell-wall lipid-carrier recycling. (sit2023undecaprenylphosphatetranslocases pages 5-8, sit2023undecaprenylphosphatetranslocases pages 11-15)
2. **Industrial strain engineering.** Antiporter stoichiometry/expression, respiratory-chain choice, ATP-synthase capacity, and envelope robustness are candidate engineering levers for bioprocesses that drift from neutral toward mildly alkaline pH. The present evidence supports these as design hypotheses, not a universal engineering recipe. (krulwich2011molecularaspectsof pages 5-6, terradot2024escherichiacolimaintains pages 8-9)
3. **Phenotype prediction and annotation.** Presence of Nha/Mrp, DUF368, DedA, or multiple PBPs cannot alone predict **METPO:1000462**. Their effects depend on redundancy, expression, coupling ions, membrane energetics, and assay conditions. Functional growth assays remain necessary. (mitchell2024penicillinbindingproteinredundancy pages 8-10, sit2023undecaprenylphosphatetranslocases pages 11-15)
4. **Single-cell diagnostics.** pHluorin and membrane-potential/flagellar-motor measurements permit direct testing of the proposed PMF→pHi edges and can distinguish population growth effects from failure of pH homeostasis. (terradot2024escherichiacolimaintains pages 8-9)

## 6. Recommended graph architecture

A conservative initial TraitMech graph should prioritize the following backbone:

1. **external pH approximately 7–8** → alters → **transmembrane ΔpH/proton availability**;
2. **respiratory/metabolic proton extrusion** → generates → **PMF**;
3. **PMF** → drives → **cation/H⁺ antiport**;
4. **cation/H⁺ antiport** → supports → **near-neutral cytoplasmic pH**;
5. **near-neutral cytoplasmic pH** → supports → **macromolecular and metabolic function**;
6. **VCA0040/DUF368-dependent C55-P homeostasis** → supports → **peptidoglycan biogenesis**;
7. **peptidoglycan biogenesis** → supports → **cell-shape integrity and growth at pH 8**;
8. **cytoplasmic and envelope homeostasis together** → enables → **“METPO:1000462”**.

Edges 1 and 5 are physiologically compelling but broad; attach them to review evidence and avoid implying a single-gene mechanism. Edges 6–7 provide the cleanest direct pH-8 genetic branch. NhaB, VCA0040, PBPs, and Mrp should be represented as taxon-specific implementations rather than universal children of the trait.

## 7. Warnings: claims not yet ready for unqualified curation

- **Do not curate DUF368 or DedA as definitively proven C55-P translocases.** The 2023 authors explicitly state that transport-independent activities remain possible and call for biochemical/structural confirmation. (sit2023undecaprenylphosphatetranslocases pages 11-15)
- **Do not make NhaB universally causal for pH 7–8 growth.** The approximately pH 5–9 assignment is an *E. coli* energetic-model prediction. (terradot2024escherichiacolimaintains pages 8-9)
- **Do not import obligate-alkaliphile adaptations wholesale.** Mrp dependence, specialized ATP-synthase motifs, S-layer proton capture, and extreme membrane potentials largely derive from growth above pH 9. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 27-28)
- **Do not use pH-shock PBP responses as direct evidence for the target growth range.** Most transitions occurred around pH 10–10.5 and after short exposure. (mitchell2024penicillinbindingproteinredundancy pages 8-10, mitchell2024penicillinbindingproteinredundancy pages 4-6)
- **Do not infer the trait from gene presence, transcript induction, or metagenomic abundance alone.** Demonstrated growth at controlled pH endpoints is required.
- **Do not merge pH with salinity.** Na⁺ is both a coupling ion and an osmotic variable; sodium-dependent effects require factorial pH × Na⁺ experiments.
- **Do not curate unverified ontology identifiers.** Label-only nodes are preferable to guessed GO, ChEBI, KEGG, Rhea, or UniProt accessions.
- **Do not treat “facultative acidophile,” “neutrophile,” and “alkaliphile” as exact synonyms for the interval phenotype.** They encode preference or broader lifestyle concepts rather than the same observed range.

## 8. DOI-first bibliography

1. Terradot G, Krasnopeeva E, Swain PS, Pilizota T. **Escherichia coli Maintains pH via the Membrane Potential.** *PRX Life*. Published November 2024;2:043015. DOI: [10.1103/PRXLife.2.043015](https://doi.org/10.1103/PRXLife.2.043015). (terradot2024escherichiacolimaintains pages 4-5, terradot2024escherichiacolimaintains pages 8-9)
2. Mitchell SL, Kearns DB, Carlson EE. **Penicillin-binding protein redundancy in Bacillus subtilis enables growth during alkaline shock.** *Applied and Environmental Microbiology*. Published January 2024;90(1). DOI: [10.1128/AEM.00548-23](https://doi.org/10.1128/AEM.00548-23). (mitchell2024penicillinbindingproteinredundancy pages 8-10, mitchell2024penicillinbindingproteinredundancy pages 4-6)
3. Poolman B. **Physicochemical homeostasis in bacteria.** *FEMS Microbiology Reviews*. Published June 2023;47(4). DOI: [10.1093/femsre/fuad033](https://doi.org/10.1093/femsre/fuad033). (poolman2023physicochemicalhomeostasisin pages 2-4, poolman2023physicochemicalhomeostasisin pages 4-5)
4. Sit B, Srisuknimit V, Bueno E, et al. **Undecaprenyl phosphate translocases confer conditional microbial fitness.** *Nature*. Published online November 2022; volume issue published January 2023;613:721–728. DOI: [10.1038/s41586-022-05569-1](https://doi.org/10.1038/s41586-022-05569-1). (sit2023undecaprenylphosphatetranslocases pages 5-8, sit2023undecaprenylphosphatetranslocases pages 11-15)
5. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology*. Published May 2011;9:330–343. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). Foundational review and the supplied existing evidence. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 27-28)

## Curation conclusion

The most defensible expansion beyond the existing 15-node/9-edge graph is a two-branch mechanism: **(i) PMF-dependent cation/proton exchange maintaining near-neutral cytoplasmic pH, and (ii) pH-conditioned C55-P recycling and peptidoglycan synthesis maintaining envelope integrity.** The VCA0040→C55-P-homeostasis→peptidoglycan→growth branch has direct pH-8 genetic and biochemical support; transporter-specific antiporter edges should carry modeled, review-derived, or taxon-specific qualifiers. Extreme-alkaliphile ATP-synthase/Mrp and pH-10 PBP findings are valuable boundary evidence but should not be represented as universal causes of **“METPO:1000462.”**

References

1. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

3. (poolman2023physicochemicalhomeostasisin pages 2-4): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 46 citations and is from a domain leading peer-reviewed journal.

4. (mitchell2024penicillinbindingproteinredundancy pages 8-10): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

5. (terradot2024escherichiacolimaintains pages 4-5): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.

6. (terradot2024escherichiacolimaintains pages 8-9): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.

7. (sit2023undecaprenylphosphatetranslocases pages 5-8): Brandon Sit, Veerasak Srisuknimit, Emilio Bueno, Franz G. Zingl, Karthik Hullahalli, Felipe Cava, and Matthew K. Waldor. Undecaprenyl phosphate translocases confer conditional microbial fitness. Nature, 613:721-728, Nov 2023. URL: https://doi.org/10.1038/s41586-022-05569-1, doi:10.1038/s41586-022-05569-1. This article has 65 citations and is from a highest quality peer-reviewed journal.

8. (poolman2023physicochemicalhomeostasisin pages 4-5): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 46 citations and is from a domain leading peer-reviewed journal.

9. (krulwich2011molecularaspectsof pages 27-28): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

10. (sit2023undecaprenylphosphatetranslocases pages 11-15): Brandon Sit, Veerasak Srisuknimit, Emilio Bueno, Franz G. Zingl, Karthik Hullahalli, Felipe Cava, and Matthew K. Waldor. Undecaprenyl phosphate translocases confer conditional microbial fitness. Nature, 613:721-728, Nov 2023. URL: https://doi.org/10.1038/s41586-022-05569-1, doi:10.1038/s41586-022-05569-1. This article has 65 citations and is from a highest quality peer-reviewed journal.

11. (mitchell2024penicillinbindingproteinredundancy pages 4-6): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

12. (sit2023undecaprenylphosphatetranslocases pages 18-21): Brandon Sit, Veerasak Srisuknimit, Emilio Bueno, Franz G. Zingl, Karthik Hullahalli, Felipe Cava, and Matthew K. Waldor. Undecaprenyl phosphate translocases confer conditional microbial fitness. Nature, 613:721-728, Nov 2023. URL: https://doi.org/10.1038/s41586-022-05569-1, doi:10.1038/s41586-022-05569-1. This article has 65 citations and is from a highest quality peer-reviewed journal.

13. (terradot2024escherichiacolimaintains pages 2-3): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.