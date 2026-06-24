---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:18:46.389445'
end_time: '2026-06-18T07:35:09.617338'
duration_seconds: 983.23
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: coccus shaped
  trait_identifier: METPO:1000668
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: coccus_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a spherical or nearly spherical
    morphology, with roughly equal dimensions in all directions.
  parent_traits: METPO:1000666
  synonyms: coccus, coccus-shaped
  evidence_summary: 'DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan
    only at the division septum (Supports coccus shape as a spherical morphology with
    septal wall growth rather than lateral elongation.) | PMID:19747126: Staphylococcus
    aureus is a facultative, Gram-positive coccus (Organism example: Staphylococcus
    aureus is described as coccus-shaped.)'
  causal_graph_summary: 'coccus_shaped_septal_growth: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** coccus shaped
- **METPO identifier:** METPO:1000668
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spherical or nearly spherical morphology, with roughly equal dimensions in all directions.
- **Parent traits:** METPO:1000666
- **Synonyms:** coccus, coccus-shaped
- **Existing evidence:** DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan only at the division septum (Supports coccus shape as a spherical morphology with septal wall growth rather than lateral elongation.) | PMID:19747126: Staphylococcus aureus is a facultative, Gram-positive coccus (Organism example: Staphylococcus aureus is described as coccus-shaped.)
- **Existing causal graph summary:** coccus_shaped_septal_growth: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **coccus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/coccus_shaped.yaml`.

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
- **Trait label:** coccus shaped
- **METPO identifier:** METPO:1000668
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spherical or nearly spherical morphology, with roughly equal dimensions in all directions.
- **Parent traits:** METPO:1000666
- **Synonyms:** coccus, coccus-shaped
- **Existing evidence:** DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan only at the division septum (Supports coccus shape as a spherical morphology with septal wall growth rather than lateral elongation.) | PMID:19747126: Staphylococcus aureus is a facultative, Gram-positive coccus (Organism example: Staphylococcus aureus is described as coccus-shaped.)
- **Existing causal graph summary:** coccus_shaped_septal_growth: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **coccus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/coccus_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report
### Target trait
- **Trait label:** coccus shaped
- **METPO:** METPO:1000668
- **Category:** MORPHOLOGY (CLASS)
- **Working definition:** spherical or nearly spherical cells with roughly equal dimensions in all directions (consistent with coccoid bacteria being “round-shaped or spherical”). (pinho2013howtoget pages 1-2)

---
## 1) Trait scope (phenotype meaning, boundaries, and nearby traits)
### 1.1 What the trait represents
“Coccus-shaped” denotes a **single-cell morphology** whose defining geometric property is near-sphericity. Mechanistically, in many “true spherical” cocci, near-sphericity is maintained because **new peptidoglycan is synthesized at the division septum only** (rather than along a cylindrical lateral wall). (pinho2013howtoget pages 3-4)

### 1.2 Key boundary case: spherical cocci vs ovococci (ovoid/ellipsoid cocci)
A critical curation boundary is that **coccoid bacteria include both true spheres and elongated ellipsoids (ovococci)**. (pinho2013howtoget pages 2-3)

- **Spherical cocci (e.g., *Staphylococcus aureus*)**: “synthesize peptidoglycan at the septum only.” (pinho2013howtoget pages 3-4)
- **Ovococci (e.g., *Streptococcus pneumoniae*, *Lactococcus lactis*)**: perform **both septal and peripheral peptidoglycan synthesis**, with peripheral synthesis occurring at mid-cell between equatorial rings and producing a “broad band” that drives longitudinal elongation and an ovoid shape. (pinho2013howtoget pages 3-4)

This distinction is visually summarized in **Figure 1** of Pinho et al. (2013), contrasting septal-only synthesis in spherical cocci vs septal+peripheral in ovococci. (pinho2013howtoget media c13a885f, pinho2013howtoget media f7060298)

### 1.3 Nearby traits that should not be conflated with METPO:1000668
- **Ovococcal/ovoid morphology**: elongated ellipsoids with peripheral synthesis component; should be curated separately from strict “coccus shaped” if the ontology distinguishes them. (pinho2013howtoget pages 2-3, pinho2013howtoget pages 3-4)
- **Coccobacillus**: short rods/ovoid intermediates; not directly supported by the retrieved evidence set and should be treated as a separate trait.
- **Cell arrangements (not shapes)**: diplococci, chains (streptococci), clusters (staphylococci), packets (sarcinae) are **arrangements of cocci** rather than defining a single-cell shape; do not encode as “coccus-shaped” causal mechanisms. (murodov2024modernviewson pages 1-3)

---
## 2) Current understanding: mechanistic determinants of coccal shape
### 2.1 Core concept: spatial pattern of peptidoglycan insertion
For spherical cocci, the canonical growth mode is that peptidoglycan synthesis is localized to the **division septum** (septal wall synthesis), rather than distributed over a lateral sidewall. (pinho2013howtoget pages 3-4)

In contrast, ovococci combine septal synthesis with **peripheral synthesis near midcell**, which produces elongation and deviates from strict coccus shape. (pinho2013howtoget pages 3-4)

### 2.2 Divisome-centered control and frequent lack of MreB-based elongasome
A 2023 review emphasizes that cocci such as *S. aureus* often **lack MreB homologs and elongation machinery**, so cell division and shape are coordinated primarily by the **divisome**; peptidoglycan synthesis occurs “mostly” at the septum coordinated by FtsZ. (battaje2023modelsversuspathogens pages 3-4)

Curation note: “lack of MreB” is a useful *tendency* but is not universal across all coccoid lineages and should be marked as generalized if included as a causal node/edge. (battaje2023modelsversuspathogens pages 3-4)

---
## 3) Recent developments (prioritizing 2023–2024)
### 3.1 Septal peptidoglycan synthesis drives constriction in *Staphylococcus aureus* (2024)
Single-molecule imaging in *S. aureus* shows that septal constriction is driven by a processive septal PG synthase module, supporting a mechanistic view of coccal division where **active sPG synthesis is the proximate driver of constriction**:
- The septal synthase complex **FtsW/PBP1** and the divisome protein **DivIB** move processively with similar velocities around the division site.
- **Impairing FtsZ treadmilling** did **not** affect FtsW/DivIB velocities or constriction rate.
- **Inhibiting PG synthesis** decelerated or stopped FtsW/DivIB movement and septum constriction.
(doi:10.1038/s41564-024-01629-6; published Mar 2024; URL: https://doi.org/10.1038/s41564-024-01629-6) (schaper2024cellconstrictionrequires pages 1-2)

Interpretation: In this coccus, constriction is tightly linked to the activity/motion of septal synthases, while FtsZ treadmilling is not rate-limiting under the tested conditions. (schaper2024cellconstrictionrequires pages 1-2)

### 3.2 GpsB regulates morphogenesis by controlling PBP localization (2024)
A 2024 mBio study revises a long-standing oversimplification that *S. aureus* is purely spherical and lacks elongation, showing a **subtle elongation phase** and identifying determinants that tune roundness:
- *S. aureus* elongation requires the SEDS/PBP pair **RodA (glycosyltransferase)** and **PBP3 (transpeptidase)**.
- A transposon-library screen identified **GpsB, SsaA, and RodZ** as additional proteins involved in this elongation process.
- **GpsB deletion** caused partial delocalization of **PBP2 and PBP4** away from the septum toward the cell periphery, increasing peripheral peptidoglycan insertion/crosslinking, and cells became **more spherical**.
(doi:10.1128/mbio.03235-23; published Mar 2024; URL: https://doi.org/10.1128/mbio.03235-23) (costa2024theroleof pages 1-2)

Interpretation: Coccal “roundness” is not just the presence/absence of elongation genes, but also **spatiotemporal allocation of PBP activity between septum and periphery**. (costa2024theroleof pages 1-2)

### 3.3 Antibiotics that inhibit peptidoglycan synthesis rapidly arrest staphylococcal division (2023)
A 2023 Science Advances study links real-world antibacterial perturbations to coccal division mechanics:
- Antibiotics targeting peptidoglycan synthesis “arrest cell division within minutes.”
- The β-lactam **oxacillin** stops division by preventing recruitment of **PBP2** to the septum, implying PBP2 is crucial for septum closure.
(doi:10.1126/sciadv.ade9023; published Mar 2023; URL: https://doi.org/10.1126/sciadv.ade9023) (costa2023newapproachesto pages 248-252)

### 3.4 Quantitative dynamics of septal synthase states (context from 2024 single-molecule study)
Although measured in rod-shaped *Bacillus subtilis*, Whitley et al. (2024) provide quantitative single-molecule evidence consistent with a general principle: **septal synthase motion is driven by septal peptidoglycan synthesis**.
- PBP2B molecules spend ~**38.1±0.4%** immobile, **59.0±0.6%** processive, and **3.0±0.1%** fast-moving.
- Immobile-state lifetime: **48±3 s**.
(doi:10.1038/s41564-024-01650-9; published Mar 2024; URL: https://doi.org/10.1038/s41564-024-01650-9) (whitley2024peptidoglycansynthesisdrives pages 1-2)

Curation note: This is **cross-taxon contextual** evidence; do not treat as direct coccal evidence without additional cocci-specific validation. (whitley2024peptidoglycansynthesisdrives pages 1-2)

---
## 4) Current applications and real-world implementations
### 4.1 Antibacterial mechanism-of-action inference from morphology/division phenotypes
Because coccal growth depends strongly on septal PG synthesis, inhibitors of PG synthesis and divisome-linked enzymes generate rapid and diagnostic division defects. This is leveraged for:
- **Antibiotic target validation** and **MoA studies** (e.g., oxacillin preventing PBP2 septal recruitment and rapidly halting constriction). (costa2023newapproachesto pages 248-252)
- **Potential divisome/PG synthase drug discovery logic**, motivated by the centrality of FtsZ and septal synthase modules in cocci (review-level framing). (battaje2023modelsversuspathogens pages 3-4)

### 4.2 Imaging-based phenotyping for morphogenesis determinants
Recent coccal-shape work relies on high-resolution imaging (including single-molecule and super-resolution) to quantify septal synthesis dynamics and subtle elongation or rounding phenotypes (e.g., FtsW/PBP1 motion; PBP delocalization; septal vs peripheral insertion shifts). (schaper2024cellconstrictionrequires pages 1-2, costa2024theroleof pages 1-2)

---
## 5) Expert synthesis (authoritative analysis)
### 5.1 Consolidated mechanistic model for METPO:1000668
A curation-ready, mechanism-centered model consistent with authoritative sources is:
1. **Divisome assembly** (FtsZ-centered) organizes a midcell septal synthesis zone. (battaje2023modelsversuspathogens pages 3-4)
2. **Septal peptidoglycan synthesis** (SEDS/PBP complexes such as FtsW/PBP1 and PBPs such as PBP2 in *S. aureus*) drives constriction and thereby maintains/reinforces near-spherical geometry when peripheral/lateral synthesis is minimal. (schaper2024cellconstrictionrequires pages 1-2, costa2023newapproachesto pages 248-252, pinho2013howtoget pages 3-4)
3. **Regulators (e.g., GpsB)** tune the spatial distribution of PBP activity between septum and periphery; shifting activity to the periphery can alter mechanical properties and growth patterns, changing the degree of sphericity. (costa2024theroleof pages 1-2)

### 5.2 Boundary-aware interpretation
Pinho et al. (2013) emphasize that coccoid bacteria include both spherical cocci and ovococci, and that ovococci use a two-mode synthesis strategy (septal + peripheral) that yields elongation. Therefore, in TraitMech curation, “coccus shaped” should be **anchored to septal-dominant insertion** and **minimal peripheral elongation**, and edges involving peripheral synthesis should typically be modeled as boundary/contrast or as negative associations with strict coccus shape. (pinho2013howtoget pages 2-3, pinho2013howtoget pages 3-4, pinho2013howtoget media c13a885f)

---
## 6) Candidate causal-graph nodes (grouped) with ontology grounding suggestions
### 6.1 Trait node
- **coccus shaped** — METPO:1000668 (given)

### 6.2 Biological processes / cellular components (grounded)
- **peptidoglycan biosynthetic process** — GO:0009252 (suggested)
- **division septum assembly / cytokinesis-related** — (GO term needed; label acceptable if not resolved here)
- **septal peptidoglycan synthesis** — label node (no GO ID asserted from retrieved evidence)
- **peripheral peptidoglycan synthesis** — label node (used for boundary with ovococci) (pinho2013howtoget pages 3-4)

### 6.3 Protein/gene nodes (label-only unless taxa-specific UniProt is added during curation)
Divisome / septal synthesis module (coccus-relevant):
- FtsZ (tubulin homolog; Z-ring)
- FtsW (SEDS)
- PBP1 (septal bPBP; naming species-specific)
- PBP2 (major PG synthase in *S. aureus*) (costa2023newapproachesto pages 248-252)
- DivIB (divisome factor associated with FtsW/PBP1 motion) (schaper2024cellconstrictionrequires pages 1-2)

Morphogenesis regulators and elongation-associated components (boundary nodes):
- GpsB (controls PBP2/PBP4 localization; impacts sphericity) (costa2024theroleof pages 1-2)
- PBP4 (cross-linking; delocalizes in gpsB mutant) (costa2024theroleof pages 1-2)
- RodA + PBP3 (SEDS/bPBP elongation pair implicated in *S. aureus* elongation) (costa2024theroleof pages 1-2)
- RodZ, SsaA (identified as involved in *S. aureus* elongation phenotype screen) (costa2024theroleof pages 1-2)

### 6.4 Chemicals / inhibitors (application nodes)
- **β-lactam oxacillin** — CHEBI grounding recommended during curation (not assigned here)
- **vancomycin / telavancin** — CHEBI grounding recommended during curation (not assigned here)
These are linked to arrest of septum constriction and/or failure to recruit PBPs at septa in *S. aureus*. (costa2023newapproachesto pages 248-252)

---
## 7) Candidate evidence-backed causal edges (curation table)
The following table is formatted for direct TraitMech-style curation work and includes evidence snippets, notes on uncertainty/taxon specificity, and source metadata.

| Edge (subject–predicate–object) | Evidence (short snippet/quote) | Notes (mechanistic interpretation and whether taxon-specific/uncertain) | Source (first author year, journal) | DOI/URL | Pub date | Suggested CURIEs (subject; object) |
|---|---|---|---|---|---|---|
| septal peptidoglycan synthesis — contributes_to — coccus shaped | “Spherical cocci … synthesize peptidoglycan at the septum only” (pinho2013howtoget pages 3-4) | Strong foundational edge for true spherical cocci; supports that septum-focused wall insertion is a defining mechanism of spherical coccal morphology. General for spherical cocci, not all ovococci. | Pinho 2013, Nat Rev Microbiol | https://doi.org/10.1038/nrmicro3088 | Aug 2013 | GO:0009252 peptidoglycan biosynthetic process; METPO:1000668 |
| peripheral peptidoglycan synthesis — negatively_associated_with — coccus shaped | “ovococci … perform both septal and peripheral peptidoglycan synthesis” and peripheral synthesis “drives slight longitudinal elongation and the ovoid shape” (pinho2013howtoget pages 3-4) | Supports boundary: peripheral/mid-cell elongation shifts morphology toward ovococcal/ovoid rather than true coccus. Strong for distinguishing trait scope. | Pinho 2013, Nat Rev Microbiol | https://doi.org/10.1038/nrmicro3088 | Aug 2013 | GO:0009252; METPO:1000668 |
| lack of MreB/elongasome machinery — contributes_to — coccus shaped | “cocci such as Staphylococcus aureus lack the elongation machinery/MreB homologs and therefore have a single coordinator—the divisome complex” (battaje2023modelsversuspathogens pages 3-4) | Broad review-level claim; useful high-level edge, but some cocci/ovococci retain elongation-like functions. Mark as somewhat generalized. **Uncertain/generalized**. | Battaje 2023, Biosci Rep | https://doi.org/10.1042/BSR20221664 | Feb 2023 | UniProt:P0A9X4 (example MreB in E. coli, homolog reference only); GO:0000917 division septum assembly |
| divisome complex — mediates — septal peptidoglycan synthesis | “In cocci, peptidoglycan synthesis takes place mostly at the site of the division, i.e., the septum coordinated by FtsZ” (battaje2023modelsversuspathogens pages 3-4) | Strong review support that divisome-centered synthesis underlies coccal growth/division. Broad but appropriate. | Battaje 2023, Biosci Rep | https://doi.org/10.1042/BSR20221664 | Feb 2023 | GO:0000917 division septum assembly; GO:0009252 peptidoglycan biosynthetic process |
| FtsZ — coordinates — septal peptidoglycan synthesis | “peptidoglycan synthesis takes place mostly at … the septum coordinated by FtsZ” (battaje2023modelsversuspathogens pages 3-4) | Foundational edge linking cytoskeletal ring to coccal septal growth. Broad across bacteria, especially cocci in cited review. | Battaje 2023, Biosci Rep | https://doi.org/10.1042/BSR20221664 | Feb 2023 | UniProt:P0A9A6 (generic FtsZ reference protein example); GO:0007049 cell cycle |
| FtsW/PBP1 septal synthase complex — drives — septum constriction | “a single population of processively moving FtsW/PBP1 associated with DivIB drives cell constriction” (schaper2024cellconstrictionrequires pages 1-2) | Strong primary evidence in *S. aureus*; taxon-specific but mechanistically central for coccal constriction. | Schäper 2024, Nat Microbiol | https://doi.org/10.1038/s41564-024-01629-6 | Mar 2024 | UniProt candidate labels only: FtsW; PBP1; GO:0000917 |
| peptidoglycan synthesis inhibition — inhibits — septum constriction | “PG synthesis inhibition decelerated or stopped directional movement of FtsW and DivIB, and septum constriction” (schaper2024cellconstrictionrequires pages 1-2) | Strong causal evidence in *S. aureus* that active PG synthesis is required for coccal constriction. Suitable experimental-factor edge. | Schäper 2024, Nat Microbiol | https://doi.org/10.1038/s41564-024-01629-6 | Mar 2024 | GO:0009252; GO:1901990 negative regulation of cell division (label-level) |
| DivIB — associates_with — FtsW/PBP1 septal synthase complex | “the septal PG synthase complex FtsW/PBP1 and its putative activator protein, DivIB, move with similar velocity around the division site” (schaper2024cellconstrictionrequires pages 1-2) | Supports co-moving divisome module; direct mechanistic interaction is plausible but this excerpt mainly shows functional association. **Uncertain interaction granularity**. | Schäper 2024, Nat Microbiol | https://doi.org/10.1038/s41564-024-01629-6 | Mar 2024 | DivIB (label); FtsW/PBP1 complex (label) |
| GpsB — spatially_restricts — PBP2/PBP4 to septum | “GpsB… partial delocalization from the division septum of PBP2 and PBP4… In the absence of GpsB, S. aureus cells become more spherical” (costa2024theroleof pages 1-2) | Strong primary evidence in *S. aureus*; supports localization-control mechanism affecting shape. | Costa 2024, mBio | https://doi.org/10.1128/mbio.03235-23 | Mar 2024 | GpsB (label); PBP2/PBP4 (label) |
| loss of GpsB — increases — peripheral peptidoglycan insertion/crosslinking | “Increased levels of these PBPs at the cell periphery versus the septum result in higher levels of peptidoglycan insertion/crosslinking throughout the entire cell” (costa2024theroleof pages 1-2) | Strong *S. aureus*-specific edge; mechanistically explains shape change via altered wall growth distribution. | Costa 2024, mBio | https://doi.org/10.1128/mbio.03235-23 | Mar 2024 | GpsB (label); GO:0009252 |
| increased peripheral PBP2/PBP4 activity — causes — more spherical cells | “Consequently, in the absence of GpsB, S. aureus cells become more spherical” (costa2024theroleof pages 1-2) | Direct phenotype edge in *S. aureus*; useful but taxon-specific and reflects perturbation from normal slight elongation. | Costa 2024, mBio | https://doi.org/10.1128/mbio.03235-23 | Mar 2024 | PBP2/PBP4 (label); METPO:1000668 |
| RodA/PBP3-mediated peptidoglycan synthesis at septal sidewall — promotes — elongation / less spherical morphology | “This elongation… is driven by… RodA… and PBP3… synthesize peptidoglycan at the septal sidewall” (costa2024theroleof pages 1-2) | Important boundary edge: this pathway counteracts strict coccal roundness in *S. aureus*. Better for warning/nearby-trait distinction than core coccal graph. **Taxon-specific**. | Costa 2024, mBio | https://doi.org/10.1128/mbio.03235-23 | Mar 2024 | RodA (label); PBP3 (label) |
| PBP2 recruitment to septum — required_for — septum closure | “oxacillin stops division progress by preventing recruitment of the major peptidoglycan synthase PBP2 to the septum, revealing PBP2 as crucial for septum closure” (costa2023newapproachesto pages 248-252) | Strong antibiotic-perturbation evidence in *S. aureus*; good experimental support for role of septal PBP2 in coccal division. | Puls 2023, Sci Adv | https://doi.org/10.1126/sciadv.ade9023 | Mar 2023 | PBP2 (label); GO:0000917 |
| inhibition of peptidoglycan synthesis — arrests — staphylococcal cell division | “antibiotics targeting peptidoglycan synthesis arrest cell division within minutes” and “completely inhibit septum constriction” (costa2023newapproachesto pages 248-252) | Strong real-world/experimental edge linking cell-wall-targeting antibiotics to coccal division failure. Taxon-specific but robust. | Puls 2023, Sci Adv | https://doi.org/10.1126/sciadv.ade9023 | Mar 2023 | GO:0009252; GO:0051301 cell division |
| septal synthase processive movement — depends_on — active peptidoglycan synthesis | “a single population of processive synthases whose motion is driven by sPG synthesis” (whitley2024peptidoglycansynthesisdrives pages 1-2) | Strong mechanistic context from *B. subtilis* divisome; not coccal, but relevant for septal-growth logic. **Cross-taxon contextual edge**. | Whitley 2024, Nat Microbiol | https://doi.org/10.1038/s41564-024-01650-9 | Mar 2024 | GO:0009252; GO:0000917 |
| multimeric divisome synthesis complex — mediates — septal peptidoglycan synthesis | “the synthesis complex is multimeric and follows a single sPG-dependent track” (whitley2024peptidoglycansynthesisdrives pages 1-2) | Contextual edge from rod-shaped Gram-positive model; may transfer to cocci only by inference. **Uncertain for direct curation into coccal TraitMech**. | Whitley 2024, Nat Microbiol | https://doi.org/10.1038/s41564-024-01650-9 | Mar 2024 | divisome synthesis complex (label); GO:0009252 |
| FtsZ treadmilling impairment — does_not_necessarily_reduce — septum constriction rate in S. aureus | “Impairing FtsZ treadmilling did not affect FtsW or DivIB velocities or septum constriction rates” (schaper2024cellconstrictionrequires pages 1-2) | Negative-result edge refines mechanism: in *S. aureus*, constriction is not limited by FtsZ treadmilling. Useful as regulatory caveat, not a positive trait determinant. **Taxon-specific**. | Schäper 2024, Nat Microbiol | https://doi.org/10.1038/s41564-024-01629-6 | Mar 2024 | FtsZ (label); GO:0051301 |
| spherical coccus morphology — associated_with — orthogonal division planes | “spherical cocci can alternate division in two or three orthogonal planes” (pinho2013howtoget pages 1-2, pinho2013howtoget pages 2-3) | Useful morphology-associated edge, but arrangement/division-plane behavior is not itself the shape mechanism. **Phenomenological/secondary**. | Pinho 2013, Nat Rev Microbiol | https://doi.org/10.1038/nrmicro3088 | Aug 2013 | METPO:1000668; GO:0051301 |
| peripheral synthesis between equatorial rings — produces — ovococcal/ovoid shape | “peripheral synthesis occurring at mid-cell, between the equatorial rings… drives slight longitudinal elongation and the ovoid shape” (pinho2013howtoget pages 3-4) | Strong boundary edge to exclude from strict coccus-shaped graph except as contrast/warning. | Pinho 2013, Nat Rev Microbiol | https://doi.org/10.1038/nrmicro3088 | Aug 2013 | peripheral PG synthesis (label); ovococcal/ovoid shape (label) |


*Table: This table compiles evidence-backed candidate causal edges for curating the microbial trait 'coccus shaped' (METPO:1000668). It prioritizes mechanistic links among septal peptidoglycan synthesis, divisome components, and shape regulators, while explicitly flagging taxon-specific or uncertain edges.*

---
## 8) Warnings / claims not yet ready for TraitMech curation
1. **“Cocci lack elongation machinery/MreB”** is a useful generalization but not universal; some cocci exhibit mild elongation and may deploy peripheral synthesis mechanisms distinct from rods. Curate as **uncertain/generalized** unless tied to specific taxa/genomes. (battaje2023modelsversuspathogens pages 3-4, costa2024theroleof pages 1-2)
2. **Cross-taxon transfer of quantitative dynamics** (e.g., PBP2B state fractions in *B. subtilis*) should be treated as **context**, not direct coccal evidence, unless corroborated in cocci. (whitley2024peptidoglycansynthesisdrives pages 1-2)
3. **Protein identifiers** (UniProt accessions) are species- and strain-dependent; this report uses label-only nodes for many proteins and recommends grounding during curation to the relevant NCBITaxon (e.g., *Staphylococcus aureus*). (schaper2024cellconstrictionrequires pages 1-2, costa2024theroleof pages 1-2)

---
## 9) DOI-first bibliography (with URLs and publication dates when available)
1. **Pinho MG, Kjos M, Veening J-W.** *How to get (a)round: mechanisms controlling growth and division of coccoid bacteria.* **Nature Reviews Microbiology**. **Aug 2013**. DOI: **10.1038/nrmicro3088**. URL: https://doi.org/10.1038/nrmicro3088 (pinho2013howtoget pages 2-3, pinho2013howtoget pages 3-4, pinho2013howtoget pages 1-2, pinho2013howtoget media c13a885f)
2. **Schäper S, et al.** *Cell constriction requires processive septal peptidoglycan synthase movement independent of FtsZ treadmilling in Staphylococcus aureus.* **Nature Microbiology**. **Mar 2024**. DOI: **10.1038/s41564-024-01629-6**. URL: https://doi.org/10.1038/s41564-024-01629-6 (schaper2024cellconstrictionrequires pages 1-2)
3. **Costa SF, et al.** *The role of GpsB in Staphylococcus aureus cell morphogenesis.* **mBio**. **Mar 2024**. DOI: **10.1128/mbio.03235-23**. URL: https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2)
4. **Puls J-S, et al.** *Inhibition of peptidoglycan synthesis is sufficient for total arrest of staphylococcal cell division.* **Science Advances**. **Mar 2023**. DOI: **10.1126/sciadv.ade9023**. URL: https://doi.org/10.1126/sciadv.ade9023 (costa2023newapproachesto pages 248-252)
5. **Whitley KD, et al.** *Peptidoglycan synthesis drives a single population of septal cell wall synthases during division in Bacillus subtilis.* **Nature Microbiology**. **Mar 2024**. DOI: **10.1038/s41564-024-01650-9**. URL: https://doi.org/10.1038/s41564-024-01650-9 (whitley2024peptidoglycansynthesisdrives pages 1-2)
6. **Battaje RR, et al.** *Models versus pathogens: how conserved is the FtsZ in bacteria?* **Bioscience Reports**. **Feb 2023**. DOI: **10.1042/BSR20221664**. URL: https://doi.org/10.1042/BSR20221664 (battaje2023modelsversuspathogens pages 3-4)
7. **Massidda O, Nováková L, Vollmer W.** *From models to pathogens: how much have we learned about Streptococcus pneumoniae cell division?* **Environmental Microbiology**. **Dec 2013**. DOI: **10.1111/1462-2920.12189**. URL: https://doi.org/10.1111/1462-2920.12189 (massidda2013frommodelsto pages 1-2, massidda2013frommodelsto pages 2-3)

---
## Appendix: visual evidence
Pinho et al. (2013) Figure 1 provides a schematic comparison of **septal-only peptidoglycan synthesis in spherical cocci** versus **septal + peripheral synthesis in ovococci**, supporting the key trait boundary used in this report. (pinho2013howtoget media c13a885f, pinho2013howtoget media f7060298)


References

1. (pinho2013howtoget pages 1-2): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

2. (pinho2013howtoget pages 3-4): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

3. (pinho2013howtoget pages 2-3): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

4. (pinho2013howtoget media c13a885f): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

5. (pinho2013howtoget media f7060298): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

6. (murodov2024modernviewson pages 1-3): KB Murodov. Modern views on the morphological structure of bacterial species. Unknown journal, 2024.

7. (battaje2023modelsversuspathogens pages 3-4): Rachana Rao Battaje, Ravikant Piyush, Vidyadhar Pratap, and Dulal Panda. Models versus pathogens: how conserved is the ftsz in bacteria? Bioscience Reports, Feb 2023. URL: https://doi.org/10.1042/bsr20221664, doi:10.1042/bsr20221664. This article has 27 citations and is from a peer-reviewed journal.

8. (schaper2024cellconstrictionrequires pages 1-2): Simon Schäper, António D. Brito, Bruno M. Saraiva, Georgia R. Squyres, Matthew J. Holmes, Ethan C. Garner, Zach Hensel, Ricardo Henriques, and Mariana G. Pinho. Cell constriction requires processive septal peptidoglycan synthase movement independent of ftsz treadmilling in staphylococcus aureus. Nature Microbiology, 9:1049-1063, Mar 2024. URL: https://doi.org/10.1038/s41564-024-01629-6, doi:10.1038/s41564-024-01629-6. This article has 33 citations and is from a highest quality peer-reviewed journal.

9. (costa2024theroleof pages 1-2): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

10. (costa2023newapproachesto pages 248-252): S Francisco Da Costa. New approaches to study staphylococcus aureus elongation and division. Unknown journal, 2023.

11. (whitley2024peptidoglycansynthesisdrives pages 1-2): Kevin D. Whitley, James Grimshaw, David M. Roberts, Eleni Karinou, Phillip J. Stansfeld, and Séamus Holden. Peptidoglycan synthesis drives a single population of septal cell wall synthases during division in bacillus subtilis. Nature Microbiology, 9:1064-1074, Mar 2024. URL: https://doi.org/10.1038/s41564-024-01650-9, doi:10.1038/s41564-024-01650-9. This article has 26 citations and is from a highest quality peer-reviewed journal.

12. (massidda2013frommodelsto pages 1-2): Orietta Massidda, Linda Nováková, and Waldemar Vollmer. From models to pathogens: how much have we learned about streptococcus pneumoniae cell division? Environmental microbiology, 15 12:3133-57, Dec 2013. URL: https://doi.org/10.1111/1462-2920.12189, doi:10.1111/1462-2920.12189. This article has 170 citations and is from a domain leading peer-reviewed journal.

13. (massidda2013frommodelsto pages 2-3): Orietta Massidda, Linda Nováková, and Waldemar Vollmer. From models to pathogens: how much have we learned about streptococcus pneumoniae cell division? Environmental microbiology, 15 12:3133-57, Dec 2013. URL: https://doi.org/10.1111/1462-2920.12189, doi:10.1111/1462-2920.12189. This article has 170 citations and is from a domain leading peer-reviewed journal.