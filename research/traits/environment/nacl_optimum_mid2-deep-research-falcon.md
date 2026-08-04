---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:42:36.644420'
end_time: '2026-08-04T01:49:21.725329'
duration_seconds: 405.08
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl optimum mid2
  trait_identifier: METPO:1000467
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_optimum_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl optimum phenotype with the best-growth NaCl concentration approximately
    between 3 and 8% (w/v), corresponding to moderate-halophile or halotolerant physiology.
  parent_traits: METPO:1000333
  synonyms: Halotolerant, Moderate halophile, NaO_3_to_8
  evidence_summary: "DOI:10.1093/femsre/fuy009: moderate halophile (Osmoadaptation\
    \ review supports the 3\u20138% NaCl optimum range as the moderate-halophile category.)"
  causal_graph_summary: 'nacl_optimum_mid2_moderate_halophile: 9 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl optimum mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000467
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration approximately between 3 and 8% (w/v), corresponding to moderate-halophile or halotolerant physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Halotolerant, Moderate halophile, NaO_3_to_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: moderate halophile (Osmoadaptation review supports the 3–8% NaCl optimum range as the moderate-halophile category.)
- **Existing causal graph summary:** nacl_optimum_mid2_moderate_halophile: 9 nodes, 10 edges

## Research Objective

Research the microbial trait **NaCl optimum mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_mid2.yaml`.

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
- **Trait label:** NaCl optimum mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000467
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration approximately between 3 and 8% (w/v), corresponding to moderate-halophile or halotolerant physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Halotolerant, Moderate halophile, NaO_3_to_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: moderate halophile (Osmoadaptation review supports the 3–8% NaCl optimum range as the moderate-halophile category.)
- **Existing causal graph summary:** nacl_optimum_mid2_moderate_halophile: 9 nodes, 10 edges

## Research Objective

Research the microbial trait **NaCl optimum mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_mid2.yaml`.

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


# Curation report: NaCl optimum mid2

## 1. Scope summary

**Target:** **NaCl optimum mid2**  
**Trait identifier:** **METPO:1000467**  
**Parent:** METPO:1000333  
**Category/kind/status:** ENVIRONMENT / CLASS / REVIEWED

This trait should represent an **organism-level growth optimum**, operationally defined as best growth at approximately **3–8% (w/v) NaCl**. It is not equivalent to survival, maximum tolerated salinity, broad halotolerance, growth range, or induction of a salt-stress response. The preferred evidence is a growth-rate or biomass-yield curve measured across several NaCl concentrations under otherwise fixed conditions.

A useful physiological anchor is *Spiribacter salinus* M19-40: no growth was detected through 0.4 M NaCl, growth was strongly stimulated up to an optimum near 0.8 M, and progressively impaired from 1.0 to 2.0 M. Because 0.8 M NaCl is approximately 4.7% (w/v), this is a direct example inside the target interval. Its viable range extended well beyond its optimum, illustrating why optimum and tolerance must remain separate graph concepts (leon2018compatiblesolutesynthesis pages 4-5).

### Boundary cases

- **Lower boundary:** organisms growing best below approximately 3% NaCl should not receive this trait merely because they tolerate 3–8%.
- **Upper boundary:** an optimum reported as exactly 8% is within the supplied approximate definition, but should retain the measured value and assay conditions. Optima above 8% should normally map to a higher-salinity class.
- **Halotolerant versus halophilic:** “halotolerant” is not always synonymous with a 3–8% optimum; many halotolerant organisms grow optimally without added salt. The synonym should therefore be treated as a search term, not an independently sufficient annotation.
- **NaCl versus total salts or Na⁺:** results stated in total dissolved salts, molar Na⁺, seawater salinity, or another chloride salt are not automatically equivalent to % (w/v) NaCl.
- **Assay dependence:** medium composition, compatible solutes, carbon source, temperature, pH, oxygen status, inoculum history, and whether optimum means growth rate or final yield can move the apparent optimum.

## 2. Current mechanistic interpretation

Moderately halophilic and halotolerant bacteria usually employ a predominantly **“salt-out” strategy**: rapid K⁺ uptake and ion-homeostasis responses are followed by accumulation of compatible organic solutes, allowing cytoplasmic osmotic balance without maintaining extremely high concentrations of disruptive inorganic salts. The strongest trait-proximal evidence currently supports **ectoine and proline accumulation** as alternative sufficient osmolyte solutions in *Halomonas elongata*.

In a 2024 genetic-engineering experiment, an ectoine-deficient *H. elongata* strain could not grow above 4% NaCl. Replacing `ectABC` with an engineered `proBm1AC` cluster and deleting the proline-catabolic gene `putA` generated intracellular proline accumulation of **353.1 ± 40.5 µmol g⁻¹ fresh cells** and restored robust growth at **8% NaCl**. This provides unusually strong perturbational evidence that intracellular compatible-solute accumulation causally supports growth at the upper boundary of METPO:1000467, while also showing that the specific osmolyte is partly substitutable (khanh2024metabolicpathwayengineering pages 1-2).

In *S. salinus*, intracellular ectoine increased from approximately **80 µM at 0.6 M NaCl** to **170 µM at the 0.8 M optimum**. Trehalose was much less abundant and was interpreted as a minor contributor. Exogenous compatible-solute assays found glycine betaine and arsenobetaine among the strongest osmoprotectants, supporting import as an alternative to de novo synthesis (leon2018compatiblesolutesynthesis pages 10-11).

## 3. Candidate nodes

### Trait and environmental nodes

- **NaCl optimum mid2 — METPO:1000467**
- **NaCl optimum phenotype** — parent supplied as METPO:1000333
- Sodium chloride — use a verified ChEBI record during implementation; do not assign an unchecked CURIE
- NaCl concentration, 3–8% (w/v)
- Extracellular osmolarity / hyperosmotic stress
- Growth rate, biomass yield, and growth optimum
- Medium composition, temperature, pH, oxygen regime, incubation time

### Chemicals and metabolites

- Sodium ion — **CHEBI:29101**
- Potassium ion — **CHEBI:29103**
- Chloride — **CHEBI:17996**
- L-proline — **CHEBI:17203**
- L-glutamate — **CHEBI:29985**
- Glycine betaine — candidate ChEBI grounding should be registry-verified before YAML insertion
- Ectoine — candidate ChEBI grounding should be registry-verified
- 5-hydroxyectoine — label-only until verified
- Trehalose — **CHEBI:27082**
- Glutathione — **CHEBI:16856**
- Water

### Genes, proteins, and complexes

- `ectA`, `ectB`, `ectC`; **EctABC ectoine-biosynthesis module**
- `proB`, `proA`, `proC`; proline-biosynthesis module
- Engineered feedback-insensitive `proBm1AC`
- `putA`; bifunctional proline utilization enzyme
- `otsA`, `otsB`; trehalose-biosynthesis module
- TrkG/TrkH/TrkA-type K⁺ uptake system; COG0168 is a useful comparative annotation
- Mrp multisubunit Na⁺-extrusion system
- TeaABC TRAP-type ectoine/5-hydroxyectoine transporter
- ProU/Opu-family ABC osmoprotectant transporters
- BetT-family choline/glycine-betaine transporter
- MscS mechanosensitive channel
- O-antigen, lipid-A, LPS-transport, and membrane-remodeling machinery—association-only candidates

Gene symbols should generally remain **taxon-qualified labels** unless the YAML schema supports orthology-level identifiers. A bacterial gene symbol does not denote one universal molecular entity across all taxa.

### Pathways and biological processes

- Compatible-solute biosynthesis
- Compatible-solute uptake and recycling
- Ectoine biosynthesis from L-aspartate-β-semialdehyde
- Proline biosynthesis from L-glutamate
- Proline degradation
- Trehalose biosynthesis through OtsAB
- Potassium-ion uptake and homeostasis
- Sodium-ion export and monovalent-cation homeostasis
- Osmotic adjustment / response to osmotic stress
- Maintenance of cytoplasmic water activity
- Cell-envelope and membrane remodeling
- Protein-folding and oxidative-damage responses

### Cellular locations

- Extracellular medium
- Cytoplasm
- Cytoplasmic membrane
- Periplasm and outer membrane for Gram-negative taxa
- Membrane transporter complex

## 4. Candidate causal edges

The following table separates experimentally manipulated edges from physiological associations and cross-taxon hypotheses.

| subject | predicate | object | evidence strength | key supporting result/snippet | DOI/date | curation qualifier |
|---|---|---|---|---|---|---|
| NaCl 3–8% (w/v) exposure | causes | osmotic/salt stress requiring osmoadaptation | Moderate | Moderate halophiles are defined by best growth at ~3–8% NaCl; in *S. salinus*, growth required salt and increased up to 0.8 M NaCl, then declined at higher salinity (leon2018compatiblesolutesynthesis pages 4-5) | 10.3389/fmicb.2018.00108; Feb 2018 | Trait-scope edge; phenotype-level, not a gene mechanism |
| ectABC (native ectoine biosynthetic operon) | enables | ectoine accumulation | High | *H. elongata* is described as accumulating ectoine; replacing the Ect biosynthetic operon with proBm1AC removed ectoine-based osmolyte production and forced proline substitution (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/aem.01195-24; Published 19 Aug 2024 | Direct genetic perturbation, but ectoine amount in wild type summarized from paper context |
| ectoine accumulation | supports growth at | 8% NaCl | High | “the Ect-deficient *H. elongata* KA1 could not grow in minimal media containing more than 4% NaCl,” whereas osmolyte replacement restored 8% growth (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/aem.01195-24; Published 19 Aug 2024 | Inferred from deletion phenotype; direct negative evidence for loss of ectoine system |
| engineered proBm1AC + putA deletion | increases | intracellular proline accumulation | High | “*H. elongata* HN6 thrived in the medium containing 8% NaCl by accumulating Pro… reaching 353.1 ± 40.5 µmol/g cell fresh weight” (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/aem.01195-24; Published 19 Aug 2024 | Direct engineering evidence |
| intracellular proline accumulation | restores/supports growth at | 8% NaCl | High | Engineered HN6 used Pro “instead of Ect” and “thrived… containing 8% NaCl,” unlike ectoine-deficient KA1 (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/aem.01195-24; Published 19 Aug 2024 | Direct causal chain within *H. elongata*; taxon-specific |
| exogenous proline | improves growth under | 300 mM NaCl stress in *Acidithiobacillus caldus* | High | “the strain with exogenous addition of proline had a significant growth advantage”; final sulfate was “3.41 mM/L higher than the control” (li2023studyonthe pages 12-15) | 10.1186/s12934-023-02232-w; Oct 2023 | Direct supplementation, but assay is salt-stress tolerance not NaCl optimum 3–8% |
| TeaABC / ProU / Opu compatible-solute transporters | may mediate uptake of | ectoine / glycine betaine osmoprotectants | Moderate | *S. salinus* has TeaABC; in *H. elongata* TeaABC imports ectoine/5-hydroxyectoine as osmostress protectants; ProU/Opu systems are broad osmoprotectant importers (leon2018compatiblesolutesynthesis pages 7-8, xing2024thepolyextremophilenatranaerobius pages 14-17) | 10.3389/fmicb.2018.00108; Feb 2018; 10.1128/aem.00145-24; May 2024 | Candidate mechanism; mixed direct analogy and omics evidence; curate cautiously |
| Trk-type K+ uptake system | contributes to | K+ homeostasis during salinity adaptation | Moderate | *S. salinus* “possesses two copies of Trk-type potassium uptake systems”; K+ fluxes “play key roles” in osmotic/salt stress response (leon2018compatiblesolutesynthesis pages 4-5) | 10.3389/fmicb.2018.00108; Feb 2018 | Mechanistic plausibility from genome/physiology discussion; not direct knockout evidence |
| COG0168 / Trk-type K+ transport | is positively associated with | increasing environmental salinity | Low | In estuary MAGs, COG0168 was top-ranked and its relative abundance increased with salinity, “R2 = 0.7778” (wu2024metagenomicinsightsinto pages 9-11) | 10.1186/s40168-024-01817-w; Jun 2024 | Association only; metagenomic feature selection, not causal proof |
| Mrp sodium extrusion system | contributes to | Na+ homeostasis in high salinity | Moderate | *S. salinus* contains an Mrp system; authors note Mrp exporters “play key roles in monovalent inorganic cation homeostasis” and are important for growth in high salinity (leon2018compatiblesolutesynthesis pages 4-5) | 10.3389/fmicb.2018.00108; Feb 2018 | Genome-based inference plus literature analogy; no species-specific perturbation |
| otsA/otsB trehalose synthesis pathway | produces | trehalose with minor osmoprotective contribution | Moderate | *S. salinus* possesses “otsB and otsA”; study summary reports trehalose “seems to make only a minor contribution to the cytoplasmic solute pool under osmotic stress” (leon2018compatiblesolutesynthesis pages 7-8, leon2018compatiblesolutesynthesis pages 10-11) | 10.3389/fmicb.2018.00108; Feb 2018 | Direct physiology/genomics in a moderate halophile; contribution is minor |
| high NaCl stress | is associated with | envelope/LPS remodeling | Low | In *A. caldus*, high salt up-regulated LPS and membrane genes; “upregulation of these genes suggests alterations of LPS assembly under high salt stress” (li2023studyonthe pages 10-12) | 10.1186/s12934-023-02232-w; Oct 2023 | Transcriptomic association, not direct mechanism for 3–8% optimum |
| compatible-solute accumulation plus K+ accumulation | forms | hybrid osmoadaptation strategy | Low | *N. thermophilus* “simultaneously accumulating compatible solutes and K+”; glycine betaine rose 52.7–893.1 mM across 2.5–4.3 M Na+ (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19) | 10.1128/aem.00145-24; May 2024 | Non-transferable/extreme-halophile evidence; useful hypothesis only for METPO:1000467 |


*Table: This table summarizes candidate causal edges for curating the NaCl optimum mid2 trait, emphasizing direct perturbation evidence where available and clearly separating associations, genomic inferences, and non-transferable extreme-halophile evidence.*

### Recommended minimal graph core

For a conservative first revision of `nacl_optimum_mid2.yaml`, the most defensible chain is:

1. **3–8% NaCl exposure → increases extracellular osmotic pressure**.
2. **Increased extracellular osmotic pressure → promotes cellular water loss / osmotic stress**.
3. **`ectABC` activity → produces ectoine**.
4. **Ectoine accumulation → supports osmotic balance and growth in the 3–8% NaCl interval**.
5. **Engineered `proBAC` activity plus reduced `putA` catabolism → increases intracellular proline**.
6. **Intracellular proline accumulation → can substitute for ectoine and restore growth at 8% NaCl in *H. elongata***.
7. **Compatible-solute transport → increases intracellular osmoprotectant pools**, retained as taxon- and substrate-qualified.

Edges involving Trk and Mrp may be included with lower evidence codes or an `uncertain` qualifier until direct perturbation evidence is attached. In *S. salinus*, two Trk-type systems and a ten-gene Mrp locus were found, but the reported evidence is mainly genome-based and supported by functional analogy rather than strain-specific knockout experiments (leon2018compatiblesolutesynthesis pages 4-5).

## 5. Recent developments, 2023–2024

### Direct pathway substitution at 8% NaCl

The 2024 *H. elongata* study is the clearest recent causal result. The ectoine-deficient control failed above 4% NaCl, whereas feedback-resistant proline synthesis combined with `putA` deletion restored growth at 8% and generated 353.1 ± 40.5 µmol proline g⁻¹ fresh weight. The result demonstrates **functional replacement of one compatible solute by another**, arguing that TraitMech should model an abstract compatible-solute/osmotic-balance module in addition to molecule-specific branches (khanh2024metabolicpathwayengineering pages 1-2).

### Natural-community evidence for K⁺ transport

A 2024 estuarine metagenomic study reconstructed **127 MAGs** and selected 40 salinity-associated features from **12,612 COGs**. COG0168, a Trk-type K⁺ transport component, ranked first; its abundance increased with salinity with reported **R² = 0.7778**. The salinity-category comparisons included 33 low-, 36 intermediate-, and 44 high-salinity stenohaline MAGs. This is strong ecological association but not causal perturbation evidence (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 9-11).

### Multi-omics evidence for hybrid strategies

In 2024, *Natranaerobius thermophilus* accumulated both K⁺ and compatible solutes. Glycine betaine rose from **52.7 to 893.1 mM** across 2.5–4.3 M Na⁺, while proline reached 130 mM at the highest condition; transport and biosynthetic proteins were also induced (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19). This supports the current expert view that “salt-in” and “salt-out” are not invariably exclusive. However, the organism is an extreme polyextremophile operating far above the target interval, so these edges should not be asserted as mechanisms of METPO:1000467 without moderate-halophile confirmation.

### Stress-protection experiments outside the exact trait scope

At 300 mM NaCl, 0.5 mM exogenous proline gave *Acidithiobacillus caldus* a significant growth advantage and raised final sulfate by 3.41 mM L⁻¹ relative to the unsupplemented control. Proline outperformed glutamate, betaine, ectoine, and trehalose in that assay. Overexpression of individual proline-pathway genes produced mixed and generally modest effects, illustrating that pathway context and metabolic burden matter (li2023studyonthe pages 12-15). The same study associated salt exposure with altered LPS, lipid-A, outer-membrane, glucan, repair, and chaperone gene expression, but these transcript changes do not demonstrate that envelope remodeling causes a 3–8% optimum (li2023studyonthe pages 10-12).

## 6. Applications and real-world relevance

1. **Compatible-solute production.** Moderately halophilic *Halomonas* strains are industrial hosts for ectoine, while the 2024 proline-engineered strain provides a proposed route for converting saline biomass waste into proline-rich single-cell aquaculture feed (khanh2024metabolicpathwayengineering pages 1-2).
2. **Low-sterility saline fermentation.** Growth at elevated NaCl suppresses many contaminants, making halophiles attractive chassis for open or reduced-sterility production. The trait optimum is therefore an important design parameter rather than merely a stress-tolerance annotation.
3. **Biomining and saline bioprocessing.** Proline and glutathione supplementation improved the performance of a bioleaching acidophile under chloride stress, suggesting routes to chloride-compatible mineral processing, although 300 mM NaCl lies below the target optimum interval and should not be used to assign METPO:1000467 (li2023studyonthe pages 12-15).
4. **Ecological prediction.** Trk-type K⁺ transport and osmolyte modules may help predict habitat salinity preference from genomes or MAGs, but current feature-selection results classify association, not an organism’s measured NaCl optimum (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 9-11).

## 7. Expert assessment for curation

The evidence supports a **many-to-one causal architecture**. Ectoine, proline, glycine betaine, and—in some taxa—trehalose can feed into a shared state of intracellular osmotic balance. Their importance depends on biosynthetic capacity, environmental availability, transporters, and energetic cost. Thus, no single gene should be treated as universally necessary or sufficient for METPO:1000467.

The strongest available evidence is **taxon-specific genetic perturbation** in *H. elongata*. Physiological measurements in *S. salinus* establish that ectoine abundance rises around a moderate-halophile optimum, but do not independently show that each transporter or K⁺ system determines that optimum. Metagenomic enrichment of Trk genes is valuable corroboration, not proof that Trk causes the phenotype.

## 8. Warnings: claims not yet ready for TraitMech

- Do not curate **“presence of `ectABC` causes METPO:1000467”** universally. Ectoine synthesis occurs across organisms with different optima, and alternative osmolytes can substitute for it.
- Do not infer the trait from a **maximum growth salinity**. *H. elongata*, for example, has a reported broad growth range, while the causal experiment concerns growth restoration at 8%, not a newly measured wild-type optimum (khanh2024metabolicpathwayengineering pages 1-2).
- Do not treat **COG0168 abundance → moderate-halophile optimum** as causal. The 2024 evidence is ecological and correlative (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 9-11).
- Do not transfer the *N. thermophilus* hybrid strategy directly to this trait. Its experimental conditions of 2.5–4.3 M Na⁺ are far beyond 3–8% NaCl (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19).
- Do not curate transcript up-regulation of LPS, chaperone, repair, or transporter genes as beneficial causal edges without perturbation or growth-rescue evidence (li2023studyonthe pages 10-12).
- Do not equate osmoprotection in an assay at 300 mM NaCl with a best-growth optimum in the target interval (li2023studyonthe pages 12-15).
- Verify every ChEBI, GO, KEGG, EC, Rhea, and UniProt identifier against its primary registry before YAML insertion. Label-only nodes are safer than guessed CURIEs.
- Preserve strain, medium, NaCl units, temperature, pH, oxygen regime, growth metric, and exposure duration as evidence qualifiers.

## 9. DOI-first bibliography

1. **Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H.** “Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient *Halomonas elongata*.” *Applied and Environmental Microbiology* 90(9). Published online **19 August 2024**; issue September 2024. DOI: [10.1128/aem.01195-24](https://doi.org/10.1128/aem.01195-24). (khanh2024metabolicpathwayengineering pages 1-2)
2. **Wu Z, Li M, Qu L, Zhang C, Xie W.** “Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary.” *Microbiome* 12:115. **June 2024**. DOI: [10.1186/s40168-024-01817-w](https://doi.org/10.1186/s40168-024-01817-w). (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 9-11)
3. **Xing Q, Zhang S, Tao X, et al.** “The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K⁺.” *Applied and Environmental Microbiology* 90(5). **May 2024**. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19)
4. **Li M, Wen J.** “Study on the intracellular adaptative mechanism of *Acidithiobacillus caldus* MTH-04 to NaCl stress.” *Microbial Cell Factories* 22:218. **October 2023**. DOI: [10.1186/s12934-023-02232-w](https://doi.org/10.1186/s12934-023-02232-w). (li2023studyonthe pages 10-12, li2023studyonthe pages 12-15)
5. **León MJ, Hoffmann T, Sánchez-Porro C, Heider J, Ventosa A, Bremer E.** “Compatible solute synthesis and import by the moderate halophile *Spiribacter salinus*: physiology and genomics.” *Frontiers in Microbiology* 9:108. **February 2018**. DOI: [10.3389/fmicb.2018.00108](https://doi.org/10.3389/fmicb.2018.00108). (leon2018compatiblesolutesynthesis pages 10-11, leon2018compatiblesolutesynthesis pages 7-8, leon2018compatiblesolutesynthesis pages 4-5)
6. **Gunde-Cimerman N, Plemenitaš A, Oren A.** “Strategies of adaptation of microorganisms of the three domains of life to high salt concentrations.” *FEMS Microbiology Reviews* 42:353–375. **May 2018**. DOI: [10.1093/femsre/fuy009](https://doi.org/10.1093/femsre/fuy009). This is the supplied existing evidence and remains an appropriate review-level source for terminology and broad osmoadaptation context.

References

1. (leon2018compatiblesolutesynthesis pages 4-5): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

2. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

3. (leon2018compatiblesolutesynthesis pages 10-11): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

4. (li2023studyonthe pages 12-15): Min Li and Jianping Wen. Study on the intracellular adaptative mechanism of acidithiobacillus caldus mth-04 to nacl stress. Microbial Cell Factories, Oct 2023. URL: https://doi.org/10.1186/s12934-023-02232-w, doi:10.1186/s12934-023-02232-w. This article has 4 citations and is from a peer-reviewed journal.

5. (leon2018compatiblesolutesynthesis pages 7-8): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

6. (xing2024thepolyextremophilenatranaerobius pages 14-17): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

7. (wu2024metagenomicinsightsinto pages 9-11): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 69 citations and is from a highest quality peer-reviewed journal.

8. (li2023studyonthe pages 10-12): Min Li and Jianping Wen. Study on the intracellular adaptative mechanism of acidithiobacillus caldus mth-04 to nacl stress. Microbial Cell Factories, Oct 2023. URL: https://doi.org/10.1186/s12934-023-02232-w, doi:10.1186/s12934-023-02232-w. This article has 4 citations and is from a peer-reviewed journal.

9. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

10. (wu2024metagenomicinsightsinto pages 1-2): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 69 citations and is from a highest quality peer-reviewed journal.