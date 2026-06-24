---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:15:20.099563'
end_time: '2026-06-17T23:23:43.799193'
duration_seconds: 503.7
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl optimum mid1
  trait_identifier: METPO:1000466
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_optimum_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl optimum phenotype with the best-growth NaCl concentration approximately
    between 1 and 3% (w/v), corresponding to slight-halophile or halotolerant physiology.
  parent_traits: METPO:1000333
  synonyms: Halotolerant, Slight halophile, NaO_1_to_3
  evidence_summary: "DOI:10.1093/femsre/fuy009: slight halophile (Osmoadaptation review\
    \ supports the 1\u20133% NaCl optimum range as the slight-halophile category.)"
  causal_graph_summary: 'nacl_optimum_mid1_slight_halophile: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl optimum mid1
- **METPO identifier:** METPO:1000466
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration approximately between 1 and 3% (w/v), corresponding to slight-halophile or halotolerant physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Halotolerant, Slight halophile, NaO_1_to_3
- **Existing evidence:** DOI:10.1093/femsre/fuy009: slight halophile (Osmoadaptation review supports the 1–3% NaCl optimum range as the slight-halophile category.)
- **Existing causal graph summary:** nacl_optimum_mid1_slight_halophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **NaCl optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_mid1.yaml`.

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
- **Trait label:** NaCl optimum mid1
- **METPO identifier:** METPO:1000466
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration approximately between 1 and 3% (w/v), corresponding to slight-halophile or halotolerant physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Halotolerant, Slight halophile, NaO_1_to_3
- **Existing evidence:** DOI:10.1093/femsre/fuy009: slight halophile (Osmoadaptation review supports the 1–3% NaCl optimum range as the slight-halophile category.)
- **Existing causal graph summary:** nacl_optimum_mid1_slight_halophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **NaCl optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_mid1.yaml`.

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


## Curation-Focused Research Report: NaCl optimum mid1 (METPO:1000466)

### 1) Scope summary (trait meaning, boundaries, and assay context)

**Trait definition (operational):** *NaCl optimum mid1* represents a **growth optimum** at approximately **1–3% (w/v) NaCl**, corresponding to the **slight-halophile** category and often overlapping with **halotolerant** physiology depending on whether salt is required. A recent synthesis explicitly defines “slight halophiles” as **0.2–0.5 M or 1–3% NaCl**, separating them from moderate (3–15%) and extreme (15–30%) halophiles. (neagu2025novelhalotolerantbacteria pages 1-2)

**Key boundary cases to curate carefully:**
- **Optimum vs tolerance:** Many microbes *tolerate* higher NaCl than their *optimum*; the trait is about **best growth**, not survival or growth range. (neagu2025novelhalotolerantbacteria pages 1-2)
- **Slight halophile vs halotolerant:** “Halotolerant” organisms **do not require salt** but can tolerate it; slight halophiles often show improved growth in low salt. Do not equate halotolerance assays with an “optimum.” (neagu2025novelhalotolerantbacteria pages 1-2)
- **NaCl (%) vs molarity:** Literature commonly reports NaCl as **M** or **% w/v**; converting matters for curation.

### 2) Key concepts and current mechanistic understanding

#### 2.1 Two canonical osmoadaptation strategies relevant to the 1–3% NaCl optimum window
**(A) Salt-in strategy:** Maintain high intracellular inorganic ion concentrations (mainly **K+**) with protein adaptations such as increased acidic amino acids to preserve protein solubility/stability at high ionic strength. (ionescu2024extremefluctuationsin pages 1-2, neagu2025novelhalotolerantbacteria pages 1-2)

**(B) Salt-out / compatible-solute strategy:** Avoid high cytoplasmic salt by accumulating **compatible solutes** (organic osmolytes). These can be imported (transporters) or synthesized de novo; common osmolytes include **glycine betaine**, **trehalose**, **proline**, **ectoine**, and **glutamate**. (ionescu2024extremefluctuationsin pages 1-2, neagu2025novelhalotolerantbacteria pages 1-2, khanh2024metabolicpathwayengineering pages 1-2)

**Interpretation for NaCl optimum mid1:** In the slight-halophile/halotolerant range (1–3% NaCl), the trait likely reflects **energetically manageable osmotic balancing**, frequently via **compatible solutes** and/or mild **K+ homeostasis**, rather than the extreme proteome specialization typical of obligate high-salt “salt-in” specialists.

#### 2.2 Compatible solutes as causal mediators of salt-dependent growth
Evidence across recent studies supports a causal role for compatible solutes in enabling growth under elevated salinity.
- **Ectoine:** In halophilic/halotolerant bacterial isolates, ectoine production was quantified (reported range **0.01–3.17 mg/L**) and PCR evidence indicated presence of an **ectoine synthase gene**. (reang2024extremozymesandcompatible pages 1-2)
- **Glycine betaine / glutamate / proline:** In a detailed 2024 mechanistic study of a polyextremophilic bacterium, intracellular levels of **glycine betaine, glutamate, and proline** increased with salinity, with reported intracellular concentrations spanning (for that organism’s higher salinity regime) **glycine betaine 52.7–893.1 mM** and **L-glutamate 11.0–221.3 mM**, supporting osmolytes as direct effectors of osmotic balance. (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 1-2)

**Curation caution:** These quantitative intracellular concentrations were measured in an **extreme halophile** (salinities far above 1–3% NaCl), so the mechanistic principle is strong, but direct numeric transfer to the NaCl-optimum-mid1 range is **inferred**. (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 1-2)

#### 2.3 Transport and pathway entities that plausibly mediate NaCl optimum mid1
Mechanistically relevant gene/protein/pathway entities supported by recent evidence include:
- **PutP (Na+/proline symporter):** Reported to facilitate **sodium ion-dependent uptake of proline**, linking external Na+ to osmoprotectant uptake. (xing2024thepolyextremophilenatranaerobius pages 17-19)
- **Glycine betaine transport (ABC families Opu/ProU):** Implicated as part of compatible-solute uptake systems supporting salinity adaptation in bacteria. (xing2024thepolyextremophilenatranaerobius pages 1-2)
- **Proline biosynthesis from glutamate:** Engineering evidence emphasizes **proB/proA/proC** (γ-glutamate kinase; γ-glutamyl phosphate reductase; pyrroline-5-carboxylate reductase) and allosteric control of γ-glutamate kinase; catabolism via **putA** was manipulated to drive osmolyte accumulation. (khanh2024metabolicpathwayengineering pages 1-2)

### 3) Recent developments (prioritizing 2023–2024)

#### 3.1 Mechanistic engineering demonstrates causal sufficiency of osmolyte substitution (2024)
A 2024 Applied and Environmental Microbiology study provides strong causal evidence that **switching the dominant osmolyte** can restore high-salt growth:
- An ectoine-deficient Halomonas elongata strain could not grow above **4% NaCl**, but an engineered strain replacing the ectoine biosynthetic operon with a proline-biosynthesis cluster and deleting **putA** (blocking proline catabolism) **thrived at 8% NaCl**. (khanh2024metabolicpathwayengineering pages 1-2)
- The engineered strain accumulated intracellular proline at **353.1 ± 40.5 µmol/g cell fresh weight**. (khanh2024metabolicpathwayengineering pages 1-2)

**Relevance to NaCl optimum mid1:** While the experimental salinity (4–8%) is above the 1–3% optimum window, the work provides strong mechanistic support that **compatible solute identity and accumulation capacity** are causally linked to salt-dependent growth. (khanh2024metabolicpathwayengineering pages 1-2)

#### 3.2 Hybrid “salt-in/salt-out” repertoires under fluctuating salinity (2024)
Metagenomic evidence from biofilms experiencing large salinity swings supports the idea that fluctuating systems select for organisms encoding both **salt-in** and **compatible-solute** mechanisms, with attention drawn to mechanosensitive channels as part of osmoregulation. (ionescu2024extremefluctuationsin pages 1-2)

**Relevance to NaCl optimum mid1:** This supports curating nodes/edges for both strategies as potential contributors (or contingency mechanisms) around modest salinity optima, especially in environments where salinity varies.

#### 3.3 Mechanosensitive channels as experimentally manipulable determinants of osmotic downshock outcomes (2023)
A 2023 Microbial Cell Factories study provides direct quantitative evidence that mechanosensitive channels modulate outcomes of osmotic transitions:
- Adaptive laboratory evolution increased Cupriavidus necator halotolerance from **1.5% to 3.25% (w/v) NaCl**; after growth in **3% NaCl**, the evolved strain achieved **47% osmolytic efficiency** upon resuspension in distilled water. (adams2023engineeringosmolysissusceptibility pages 1-2)
- Deleting **mscL** increased lysis susceptibility and, when combined with halotolerance evolution, yielded **>90% osmolytic efficiency**. (adams2023engineeringosmolysissusceptibility pages 1-2)
- In E. coli BL21, deletion of **mscL and mscS** produced **75% cell lysis** after growth in **4% NaCl** and downshock to distilled water. (adams2023engineeringosmolysissusceptibility pages 1-2)

**Relevance to NaCl optimum mid1:** These data support adding mechanosensitive channels (MscL/MscS) to the causal graph when modeling **salinity fluctuations** rather than steady-state growth optima; the phenotype measured is lysis/downshock survival, not growth optimum per se. (adams2023engineeringosmolysissusceptibility pages 1-2)

### 4) Current applications and real-world implementations

#### 4.1 Saline bioprocessing and biomolecule production
Halotolerant/halophilic bacteria are used or proposed for bioprocessing in saline media, where compatible solutes can stabilize cellular functions and enzymes.
- A 2024 Scientific Reports study quantifies ectoine production in isolates and links compatible-solute production with enzyme (extremozyme) function under saline conditions, suggesting compatibility between salt-adapted physiology and industrially relevant enzyme stability. (reang2024extremozymesandcompatible pages 1-2)
- A 2024 engineering study demonstrates feasibility of developing a Pro-rich Halomonas strain for sustainable feed additive applications while maintaining growth at high salinity via osmolyte substitution. (khanh2024metabolicpathwayengineering pages 1-2)

#### 4.2 Downstream processing via osmolysis enabled by engineered osmoregulation
The 2023 mechanosensitive channel/halotolerance work provides a practical downstream concept: grow cells at elevated salt then trigger **hypoosmotic lysis** for intracellular product recovery, reducing reliance on mechanical/reagent lysis. (adams2023engineeringosmolysissusceptibility pages 1-2)

#### 4.3 Biohydrogen from saline wastewater at salinities overlapping the slight-halophile window
A 2024 overview reports multiple H2-producing microbes operating at moderate salinities in the neighborhood of the slight-halophile range; examples include organisms producing H2 around **0.4–0.5 M NaCl**, with yields such as **Bacillus sp. B2: 1.65 ± 0.4 mol H2/mol glucose at 0.5 M** and **Rhodovulum sulfidophilum: 2.06 ± 0.08 mol H2/mol acetate at 0.5 M**. (guo2024biohydrogenproductionfrom pages 14-16)

**Curation caution:** This source provides organism-level performance vs salinity, but limited gene/pathway details for the 1–3% optimum trait; treat as application context rather than direct mechanistic edge support. (guo2024biohydrogenproductionfrom pages 14-16)

### 5) Candidate nodes for TraitMech curation (grouped)

#### 5.1 Environmental / experimental factor nodes
- **NaCl concentration in growth medium** (label; could map to ENVO saline water terms depending on context)
- **Osmotic upshift / salt stress** (process context)
- **Hypoosmotic downshock** (for fluctuation/transition edges)

#### 5.2 Chemical / metabolite nodes (CHEBI grounded)
- **Glycine betaine** (CHEBI:17750) (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 1-2)
- **Ectoine** (CHEBI:30913) (reang2024extremozymesandcompatible pages 1-2)
- **L-proline** (CHEBI:17203) (khanh2024metabolicpathwayengineering pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 1-2)
- **L-glutamate** (CHEBI:29991) (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 1-2)

#### 5.3 Gene/protein/complex nodes (label-level unless curated to UniProt/KEGG)
- **PutP** (Na+/proline symporter; label node) (xing2024thepolyextremophilenatranaerobius pages 17-19)
- **Opu/ProU family glycine betaine ABC transporters** (label node family) (xing2024thepolyextremophilenatranaerobius pages 1-2)
- **proB, proA, proC** (proline biosynthesis enzymes; label nodes) (khanh2024metabolicpathwayengineering pages 1-2)
- **putA** (proline catabolism; label node) (khanh2024metabolicpathwayengineering pages 1-2)
- **Ectoine synthase gene (likely ectC)** (label node; excerpt does not specify symbol) (reang2024extremozymesandcompatible pages 1-2)
- **MscL, MscS mechanosensitive channels** (label nodes) (adams2023engineeringosmolysissusceptibility pages 1-2)

#### 5.4 Biological process nodes (GO candidates)
- **Response to osmotic stress** (GO:0006970; broad) (concept supported by multiple sources) (ionescu2024extremefluctuationsin pages 1-2, neagu2025novelhalotolerantbacteria pages 1-2)
- **Response to salt stress / osmoadaptation** (label node; map to GO term during curation if needed)

### 6) Candidate causal edges (evidence-backed)

The following artifact contains a curation-ready table of candidate edges (triples) with evidence snippets, DOI-first sources, and uncertainty notes.

| Edge (subject–predicate–object) | Candidate subject CURIE | Candidate object CURIE | Evidence snippet (verbatim/near-verbatim) | Source (DOI, year, URL) | Notes/uncertainty (taxon/assay/strength) |
|---|---|---|---|---|---|
| NaCl optimum 1–3% (w/v) — defines — slight halophile physiology | METPO:1000466 | label:slight_halophile | “slight halophiles (0.2–0.5 M or 1–3% NaCl)” (neagu2025novelhalotolerantbacteria pages 1-2) | 10.3390/biotech14020049, 2025, https://doi.org/10.3390/biotech14020049 | Strong for scope/definition; source is 2025 review-style primary paper, not a formal ontology source. Useful for trait boundary. |
| slight halophile / halotolerant physiology — associated_with — salt-in osmoregulation strategy | label:slight_halophile_or_halotolerant_physiology | label:salt-in_strategy | “The ‘salt-in’ strategy involves maintaining a high intracellular concentration of inorganic salts, mainly potassium” (ionescu2024extremefluctuationsin pages 1-2); “salt-in strategy (accumulation of inorganic ions, particularly K+, exclusion of Na+...)” (neagu2025novelhalotolerantbacteria pages 1-2) | 10.3389/frmbi.2023.1329925, 2024, https://doi.org/10.3389/frmbi.2023.1329925; 10.3390/biotech14020049, 2025, https://doi.org/10.3390/biotech14020049 | General mechanism across halotolerant/halophilic microbes; not specific to all slight halophiles. Curate as broad association, not deterministic edge. |
| slight halophile / halotolerant physiology — associated_with — compatible-solute osmoregulation strategy | label:slight_halophile_or_halotolerant_physiology | GO:0006970 | “The ‘salt-out’ strategy relies on biosynthesis or uptake of compatible solutes” (ionescu2024extremefluctuationsin pages 1-2); “compatible solute strategy (accumulation of small organic osmolytes)” (neagu2025novelhalotolerantbacteria pages 1-2) | 10.3389/frmbi.2023.1329925, 2024, https://doi.org/10.3389/frmbi.2023.1329925; 10.3390/biotech14020049, 2025, https://doi.org/10.3390/biotech14020049 | GO:0006970 is generic response to osmotic stress, not a perfect match for compatible-solute accumulation. Good candidate but grounding may need refinement. |
| elevated external NaCl — induces_accumulation_of — glycine betaine | CHEBI:26710 | CHEBI:17750 | “The intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2); “glycine betaine of 52.7–893.1 mM” across increasing salinity (xing2024thepolyextremophilenatranaerobius pages 17-19) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | Strong mechanistic evidence, but from extreme halophile Natranaerobius thermophilus rather than a 1–3% optimum organism; transfer to trait is inferred. |
| elevated external NaCl — induces_accumulation_of — L-glutamate | CHEBI:26710 | CHEBI:29991 | “The intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2); “L-glutamate of 11.0–221.3 mM” (xing2024thepolyextremophilenatranaerobius pages 17-19) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | Strong but taxon-specific to extreme halophile; likely relevant to many halotolerant/slight-halophile bacteria as a general osmolyte. |
| elevated external NaCl — induces_accumulation_of — L-proline | CHEBI:26710 | CHEBI:17203 | “The intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2); engineered H. elongata “thrived in the medium containing 8% NaCl by accumulating Pro ... reaching a concentration of 353.1 ± 40.5 µmol/g cell fresh weight” (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24; 10.1128/aem.01195-24, 2024, https://doi.org/10.1128/aem.01195-24 | Strong for proline as osmolyte; direct causality supported in engineered system. Natural relevance to NaCl-optimum-mid1 is plausible but not universal. |
| ectoine biosynthetic gene — enables_production_of — ectoine | label:ectoine_biosynthetic_gene | CHEBI:30913 | “the ectoine synthase gene responsible for its biosynthesis” and “production of ectoine-compatible solute ranged from 0.01 to 3.17 mg l−1” (reang2024extremozymesandcompatible pages 1-2) | 10.1038/s41598-024-63581-z, 2024, https://doi.org/10.1038/s41598-024-63581-z | Good gene→product edge, but exact gene symbol not given in excerpt; likely ectC/ectoine synthase. Keep node label-level unless full paper confirms symbol. |
| elevated external NaCl — selects_for_or_induces — ectoine production | CHEBI:26710 | CHEBI:30913 | “The compatible solute production by these isolates may be linked to their ability to produce extremozymes under saline conditions” and ectoine production was measured in halophilic/halotolerant isolates (reang2024extremozymesandcompatible pages 1-2) | 10.1038/s41598-024-63581-z, 2024, https://doi.org/10.1038/s41598-024-63581-z | Weaker than direct induction claim because excerpt ties ectoine production to saline isolates/conditions but not a controlled salinity gradient response. Mark uncertain. |
| replacement of ectABC operon with proBm1AC and deletion of putA — enables — proline accumulation | label:ΔectABC::proBm1AC_ΔputA | CHEBI:17203 | “replaced the coding region of H. elongata OUT30018’s Ect biosynthetic operon with the artificial self-cloned proBm1AC gene cluster” and “the putA gene ... was deleted”; strain HN6 accumulated Pro “353.1 ± 40.5 µmol/g cell fresh weight” (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/aem.01195-24, 2024, https://doi.org/10.1128/aem.01195-24 | Strong causal engineering evidence in Halomonas elongata; taxon-specific and synthetic genotype. Useful as mechanistic support for osmolyte substitution. |
| replacement of ectABC operon with proBm1AC and deletion of putA — enables_growth_at — 8% NaCl | label:ΔectABC::proBm1AC_ΔputA | ENVO:01000311 | “H. elongata HN6 thrived in the medium containing 8% NaCl by accumulating Pro in the cell instead of Ect” (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/aem.01195-24, 2024, https://doi.org/10.1128/aem.01195-24 | Strong direct assay evidence, but 8% NaCl is above NaCl optimum mid1 range; relevant as extrapolative mechanism, not direct trait-defining optimum evidence. |
| ectoine deficiency — decreases_growth_above — 4% NaCl | label:ectoine_deficient_Halomonas_elongata | ENVO:01000311 | “the Ect-deficient H. elongata KA1 could not grow in minimal media containing more than 4% NaCl” (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/aem.01195-24, 2024, https://doi.org/10.1128/aem.01195-24 | Strong negative evidence that ectoine can be growth-supporting at elevated salt; threshold is above trait range. |
| PutP — mediates — Na+-dependent proline uptake | label:PutP | CHEBI:17203 | “the Na+/proline symporter PutP ... facilitates the sodium ion-dependent uptake of proline into the cells” (xing2024thepolyextremophilenatranaerobius pages 17-19) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | Strong transporter-function edge, but source is extreme halophile and excerpt does not provide accession/CURIE. Label-level node recommended unless curated from genome annotation. |
| MscL — mediates_survival_during — hypoosmotic downshock | label:MscL | GO:0009268 | Deletions were “intended to limit osmolyte efflux during hypotonic shock and raise susceptibility to osmotic lysis” (adams2023engineeringosmolysissusceptibility pages 2-4); “deleting mechanosensitive channels plus adapting cells to higher salinity ... is an effective strategy to engineer osmolytic susceptibility” (adams2023engineeringosmolysissusceptibility pages 8-11) | 10.1186/s12934-023-02064-8, 2023, https://doi.org/10.1186/s12934-023-02064-8 | Inference from loss-of-function phenotype; strong for role in downshock survival/release. GO term is broad. |
| deletion of mscL — increases — hypoosmotic lysis after growth at elevated NaCl | label:ΔmscL | label:hypoosmotic_lysis | “the mscL knockout showed 62% lysis vs 19% for wild-type” and combining ALE with mscL deletion produced “>90% osmolysis efficiency” after growth in 3% NaCl (adams2023engineeringosmolysissusceptibility pages 8-11, adams2023engineeringosmolysissusceptibility pages 1-2) | 10.1186/s12934-023-02064-8, 2023, https://doi.org/10.1186/s12934-023-02064-8 | Strong direct assay evidence in Cupriavidus necator. Phenotype is lysis susceptibility, not growth optimum; should be curated only if graph includes downshock adaptation branch. |
| deletion of mscL and mscS — increases — hypoosmotic lysis after growth at 4% NaCl | label:ΔmscL_ΔmscS | label:hypoosmotic_lysis | “deleting mscL and mscS ... produced 75% cell lysis when cells were grown in medium with 4% NaCl and then resuspended in distilled water” (adams2023engineeringosmolysissusceptibility pages 1-2) | 10.1186/s12934-023-02064-8, 2023, https://doi.org/10.1186/s12934-023-02064-8 | Strong direct evidence in E. coli BL21; about osmotic downshock survival, not NaCl optimum. Useful supporting edge for response to salinity fluctuation, not core optimum mechanism. |


*Table: This table compiles candidate causal edges for the NaCl optimum mid1 trait, linking slight-halophile scope, osmoadaptation mechanisms, key osmolytes, transporter/gene functions, and mechanosensitive-channel evidence. It is designed for TraitMech curation, with concise evidence snippets, DOI-first sources, and uncertainty notes.*

### 7) Expert synthesis (authoritative interpretation anchored to evidence)

**Working mechanistic hypothesis for NaCl optimum mid1:** Microbes with best growth at ~1–3% NaCl likely occupy a regime where **ionic homeostasis (notably K+)** and **compatible-solute accumulation** efficiently offset moderate osmotic stress without requiring extreme proteome specialization. This aligns with definitions that place 1–3% NaCl in “slight halophile” range and with broad mechanistic descriptions of salt-in vs salt-out strategies. (neagu2025novelhalotolerantbacteria pages 1-2, ionescu2024extremefluctuationsin pages 1-2)

**Graph design recommendation:** Use a core module of **NaCl concentration → osmotic stress → compatible solute uptake/synthesis → restored turgor/protein stability → growth rate** and optionally include a side module for **salinity fluctuation → mechanosensitive channel gating → downshock survival/lysis**. Mechanosensitive-channel edges are strongly supported experimentally but represent a distinct phenotype from optimum growth. (adams2023engineeringosmolysissusceptibility pages 1-2)

### 8) Warnings / items not ready to curate as high-confidence TraitMech edges

1. **Avoid curating extreme-halophile quantitative solute concentrations as if they apply at 1–3% NaCl.** The intracellular mM values for glycine betaine/glutamate/proline were measured at much higher salinities and in a specialized organism. Curate the *directional causal relationship* (salinity increases compatible solutes) but mark numeric ranges as taxon- and regime-specific. (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 1-2)
2. **Do not equate growth at 4–8% NaCl with NaCl optimum mid1.** The Halomonas engineering paper is best used to support a mechanistic edge (osmolyte substitution enables growth under salt stress), not to define the trait’s optimum range. (khanh2024metabolicpathwayengineering pages 1-2)
3. **Mechanosensitive channels (MscL/MscS) are best curated under ‘salinity transitions/downshock’ rather than optimum growth.** Evidence is strong for downshock/lysis phenotype; relevance to steady-state optimum is indirect. (adams2023engineeringosmolysissusceptibility pages 1-2)
4. **Ectoine gene symbol grounding:** The Scientific Reports excerpt indicates an “ectoine synthase gene,” but does not provide the explicit gene symbol; confirm (e.g., ectC) in full text before grounding to specific identifiers. (reang2024extremozymesandcompatible pages 1-2)

---

## DOI-first bibliography (with dates and URLs)

1. **Neagu S, Stancu MM.** *Novel Halotolerant Bacteria from Saline Environments: Isolation and Biomolecule Production.* **BioTech**. **2025-06**. DOI: **10.3390/biotech14020049**. https://doi.org/10.3390/biotech14020049 (neagu2025novelhalotolerantbacteria pages 1-2, neagu2025novelhalotolerantbacteria pages 9-10, neagu2025novelhalotolerantbacteria pages 10-12)

2. **Ionescu D, Zoccarato L, Cabello-Yeves PJ, Tikochinski Y.** *Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy.* **Frontiers in Microbiomes**. **2024-01**. DOI: **10.3389/frmbi.2023.1329925**. https://doi.org/10.3389/frmbi.2023.1329925 (ionescu2024extremefluctuationsin pages 1-2)

3. **Reang L, et al.** *Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of Southwest Saurashtra Gujarat.* **Scientific Reports**. **2024-07**. DOI: **10.1038/s41598-024-63581-z**. https://doi.org/10.1038/s41598-024-63581-z (reang2024extremozymesandcompatible pages 1-2)

4. **Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H.** *Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient Halomonas elongata.* **Applied and Environmental Microbiology**. **2024-09**. DOI: **10.1128/aem.01195-24**. https://doi.org/10.1128/aem.01195-24 (khanh2024metabolicpathwayengineering pages 1-2)

5. **Xing Q, et al.** *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.* **Applied and Environmental Microbiology**. **2024-05**. DOI: **10.1128/aem.00145-24**. https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19)

6. **Adams JD, Sander KB, Criddle CS, Arkin AP, Clark DS.** *Engineering osmolysis susceptibility in Cupriavidus necator and Escherichia coli for recovery of intracellular products.* **Microbial Cell Factories**. **2023-04**. DOI: **10.1186/s12934-023-02064-8**. https://doi.org/10.1186/s12934-023-02064-8 (adams2023engineeringosmolysissusceptibility pages 1-2, adams2023engineeringosmolysissusceptibility pages 12-14, adams2023engineeringosmolysissusceptibility pages 8-11)

7. **Guo H, Teng Z, Han H, Li T.** *Biohydrogen production from saline wastewater: An overview.* **Clean Energy Science and Technology**. **2024-09**. DOI: **10.18686/cest.v2i3.210**. https://doi.org/10.18686/cest.v2i3.210 (guo2024biohydrogenproductionfrom pages 14-16, guo2024biohydrogenproductionfrom pages 11-14)


References

1. (neagu2025novelhalotolerantbacteria pages 1-2): Simona Neagu and Mihaela Marilena Stancu. Novel halotolerant bacteria from saline environments: isolation and biomolecule production. BioTech, 14:49, Jun 2025. URL: https://doi.org/10.3390/biotech14020049, doi:10.3390/biotech14020049. This article has 11 citations.

2. (ionescu2024extremefluctuationsin pages 1-2): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 11 citations.

3. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

4. (reang2024extremozymesandcompatible pages 1-2): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, Hiren Bhalani, JasminKumar Kheni, U. M. Vyas, and M. V. Parakhia. Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of southwest saurashtra gujarat. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-63581-z, doi:10.1038/s41598-024-63581-z. This article has 16 citations and is from a peer-reviewed journal.

5. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

6. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

7. (adams2023engineeringosmolysissusceptibility pages 1-2): Jeremy David Adams, Kyle B. Sander, Craig S. Criddle, Adam P. Arkin, and Douglas S. Clark. Engineering osmolysis susceptibility in cupriavidus necator and escherichia coli for recovery of intracellular products. Microbial Cell Factories, Apr 2023. URL: https://doi.org/10.1186/s12934-023-02064-8, doi:10.1186/s12934-023-02064-8. This article has 16 citations and is from a peer-reviewed journal.

8. (guo2024biohydrogenproductionfrom pages 14-16): Huiyuan Guo, Zedong Teng, Hexing Han, and Tinggang Li. Biohydrogen production from saline wastewater: an overview. Clean Energy Science and Technology, 2:210, Sep 2024. URL: https://doi.org/10.18686/cest.v2i3.210, doi:10.18686/cest.v2i3.210. This article has 5 citations.

9. (adams2023engineeringosmolysissusceptibility pages 2-4): Jeremy David Adams, Kyle B. Sander, Craig S. Criddle, Adam P. Arkin, and Douglas S. Clark. Engineering osmolysis susceptibility in cupriavidus necator and escherichia coli for recovery of intracellular products. Microbial Cell Factories, Apr 2023. URL: https://doi.org/10.1186/s12934-023-02064-8, doi:10.1186/s12934-023-02064-8. This article has 16 citations and is from a peer-reviewed journal.

10. (adams2023engineeringosmolysissusceptibility pages 8-11): Jeremy David Adams, Kyle B. Sander, Craig S. Criddle, Adam P. Arkin, and Douglas S. Clark. Engineering osmolysis susceptibility in cupriavidus necator and escherichia coli for recovery of intracellular products. Microbial Cell Factories, Apr 2023. URL: https://doi.org/10.1186/s12934-023-02064-8, doi:10.1186/s12934-023-02064-8. This article has 16 citations and is from a peer-reviewed journal.

11. (neagu2025novelhalotolerantbacteria pages 9-10): Simona Neagu and Mihaela Marilena Stancu. Novel halotolerant bacteria from saline environments: isolation and biomolecule production. BioTech, 14:49, Jun 2025. URL: https://doi.org/10.3390/biotech14020049, doi:10.3390/biotech14020049. This article has 11 citations.

12. (neagu2025novelhalotolerantbacteria pages 10-12): Simona Neagu and Mihaela Marilena Stancu. Novel halotolerant bacteria from saline environments: isolation and biomolecule production. BioTech, 14:49, Jun 2025. URL: https://doi.org/10.3390/biotech14020049, doi:10.3390/biotech14020049. This article has 11 citations.

13. (adams2023engineeringosmolysissusceptibility pages 12-14): Jeremy David Adams, Kyle B. Sander, Craig S. Criddle, Adam P. Arkin, and Douglas S. Clark. Engineering osmolysis susceptibility in cupriavidus necator and escherichia coli for recovery of intracellular products. Microbial Cell Factories, Apr 2023. URL: https://doi.org/10.1186/s12934-023-02064-8, doi:10.1186/s12934-023-02064-8. This article has 16 citations and is from a peer-reviewed journal.

14. (guo2024biohydrogenproductionfrom pages 11-14): Huiyuan Guo, Zedong Teng, Hexing Han, and Tinggang Li. Biohydrogen production from saline wastewater: an overview. Clean Energy Science and Technology, 2:210, Sep 2024. URL: https://doi.org/10.18686/cest.v2i3.210, doi:10.18686/cest.v2i3.210. This article has 5 citations.