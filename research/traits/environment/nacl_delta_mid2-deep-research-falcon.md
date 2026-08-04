---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:34:07.456233'
end_time: '2026-08-04T01:42:17.107709'
duration_seconds: 489.65
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl delta mid2
  trait_identifier: METPO:1000481
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_delta_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A NaCl delta phenotype with a growth-supporting NaCl breadth of approximately\
    \ 3\u20138% (w/v), characteristic of organisms with broad salinity tolerance."
  parent_traits: METPO:1000335
  synonyms: Nad_3_8
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports broad osmoadaptive breadths as the halotolerant / moderately euryhaline
    phenotype.)'
  causal_graph_summary: 'nacl_delta_mid2_broad_breadth: 13 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl delta mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000481
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth of approximately 3–8% (w/v), characteristic of organisms with broad salinity tolerance.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_3_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports broad osmoadaptive breadths as the halotolerant / moderately euryhaline phenotype.)
- **Existing causal graph summary:** nacl_delta_mid2_broad_breadth: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **NaCl delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_mid2.yaml`.

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
- **Trait label:** NaCl delta mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000481
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth of approximately 3–8% (w/v), characteristic of organisms with broad salinity tolerance.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_3_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports broad osmoadaptive breadths as the halotolerant / moderately euryhaline phenotype.)
- **Existing causal graph summary:** nacl_delta_mid2_broad_breadth: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **NaCl delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_mid2.yaml`.

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


# Curation report: NaCl delta mid2

## 1. Scope summary

**Target:** **“METPO:1000481”** (*NaCl delta mid2*; synonym *Nad_3_8*; parent **METPO:1000335**).

This trait should represent an **assay-observed breadth of growth-supporting NaCl concentrations of approximately 3–8 percentage points (w/v)**. It is a breadth/range phenotype, not an NaCl optimum, a single-point tolerance result, an absolute upper limit, or evidence that NaCl is required for growth. For example, *Spiribacter salinus* had no detectable growth below 0.4 M NaCl, optimum growth at 0.8 M, and impaired but detectable growth through 2.0 M; these are separate lower-bound, optimum, and upper-bound observations from which breadth may be calculated (leon2018compatiblesolutesynthesis pages 4-5).

A percentage-point interval should not be confused with the statement “grows at 3–8% NaCl.” The latter describes endpoints only if both were tested and growth was demonstrated throughout the interval. Every TraitMech assertion should therefore retain medium, temperature, incubation time, aeration, inoculum/acclimation, growth threshold, and NaCl units. Medium dependence is substantial: *Pseudomonas putida* KT2440 tolerated 5% NaCl in rich KB medium, whereas its engineering experiments used minimal salts medium (fan2024improvementinsalt pages 5-8). Acclimatization also altered high-salt growth of engineered *Halomonas elongata* (khanh2024metabolicpathwayengineering pages 9-12).

### Boundary cases

- **Below scope:** narrow intervals under approximately 3 percentage points, survival without growth, transient osmotic-shock survival, and single-concentration growth tests.
- **Within scope:** demonstrated continuous growth interval whose upper minus lower bound is approximately 3–8% (w/v), including a genetically expanded interval if both endpoints are measured comparably.
- **Above/adjacent scope:** breadth greater than approximately 8 percentage points, extreme halophily, and organisms such as wild-type *H. elongata* reported to grow from 0.3% to 21% NaCl (khanh2024metabolicpathwayengineering pages 1-2).
- **Not equivalent:** halophily or salt requirement. A halotolerant organism can have broad tolerance without requiring NaCl; a moderate halophile may have a broad range but fail at low salt.
- **Assay caveat:** 1 M NaCl is approximately 5.84% (w/v), but conversions should only be added when solution conventions are explicit.

Mechanistically, the best-supported architecture is a staged response: hyperosmotic exposure drives water loss and reduced turgor; early K⁺ uptake with counter-anion accumulation restores osmotic balance; longer-term compatible-solute synthesis/import and Na⁺ extrusion permit growth; and mechanosensitive channels protect against the reverse, hypoosmotic transition. This is a family of taxon- and context-dependent mechanisms rather than one universal pathway (godard2020metabolicrearrangementscausing pages 4-5, vandrich2020contributionofmechanosensitive pages 1-2, guo2024biohydrogenproductionfrom pages 16-18).

## 2. Candidate nodes

### Trait and assay/environment nodes

- **NaCl delta mid2 — “METPO:1000481”**.
- **NaCl concentration / salinity gradient** — label-only pending exact METPO/ENVO assay mapping.
- **Hyperosmotic stress**, **hypoosmotic downshock**, **cellular turgor**, **water efflux/influx**, **growth-supporting NaCl lower bound**, **growth-supporting NaCl upper bound**, and **NaCl growth breadth** — label-only candidates unless the repository already has preferred assay terms.
- Experimental qualifiers: medium composition, compatible-solute supplementation, temperature, aeration, incubation duration, inoculum acclimation, OD threshold, and NaCl unit.

### Chemicals and metabolites

- Sodium chloride — **CHEBI:26710**.
- Potassium ion — **CHEBI:29103**.
- Sodium ion — **CHEBI:29101**.
- L-glutamate — **CHEBI:29985**.
- L-proline — **CHEBI:17203**.
- Glycine betaine — **CHEBI:17750**.
- Ectoine — **CHEBI:143227**; curator should verify this release-specific mapping before insertion.
- Trehalose — **CHEBI:27082**.
- Hydroxyectoine, choline, γ-glutamyl phosphate, glutamate-5-semialdehyde, and pyrroline-5-carboxylate — retain as labels until identifier verification.

### Genes, proteins, and complexes

- **ectA–ectB–ectC / EctABC**: ectoine biosynthesis. In *H. elongata*, deletion removed the principal ectoine strategy and imposed a >4% NaCl growth defect in minimal medium; in *S. salinus*, genes occur as noncanonical separated `ectAC` and `ectB`, warning against requiring operon colocalization (leon2018compatiblesolutesynthesis pages 1-2, khanh2024metabolicpathwayengineering pages 1-2).
- **proB, proA, proC / ProBAC**: glutamate-to-proline biosynthesis. ProB is γ-glutamate kinase, ProA γ-glutamyl-phosphate reductase, and ProC pyrroline-5-carboxylate reductase (khanh2024metabolicpathwayengineering pages 1-2).
- **proBm1**: feedback-insensitive *H. elongata* ProB D118N/D119N allele; strain-specific label node.
- **putA / PutA**: bifunctional proline dehydrogenase/P5C dehydrogenase; deletion limits proline catabolism (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9).
- **betB / betaine-aldehyde dehydrogenase**: contributes to glycine-betaine synthesis in *P. putida* KT2440 (fan2024improvementinsalt pages 12-14).
- **EcnhaA / NhaA Na⁺:H⁺ antiporter** and endogenous `nhaA-II`: sodium-homeostasis candidates; retain strain/source prefixes because antiporter effects are paralog- and host-dependent (fan2024improvementinsalt pages 12-14).
- **KdpA/KdpB/KdpD** and **TrkH/Trk-type K⁺ uptake systems**: plausible early ion-homeostasis nodes, but Kdp overexpression did not improve KT2440 growth at 4% NaCl (fan2024improvementinsalt pages 12-14).
- **TeaABC**: osmoregulated ectoine uptake/recycling transporter in *H. elongata* (vandrich2020contributionofmechanosensitive pages 1-2).
- **MscS-family channels**: `mscK`, `mscS1`, `mscS2`, and `mscS3` in *H. elongata*; primarily supported for hypoosmotic protection, not as positive high-salt-growth determinants (vandrich2020contributionofmechanosensitive pages 1-2, vandrich2020contributionofmechanosensitive pages 8-9).
- **DnaJ and ClpB**: molecular-chaperone candidates with only slight improvement on overexpression; weak evidence for this trait (fan2024improvementinsalt pages 12-14).

Exact UniProt, KEGG, and EC mappings should be assigned only after selecting the taxon/strain-specific protein record. Gene symbols alone should not be assigned universal protein CURIEs.

### Pathways, processes, and localizations

- Compatible-solute biosynthesis and intracellular accumulation.
- Compatible-solute uptake/recycling.
- Ectoine biosynthetic process.
- Proline biosynthetic and catabolic processes.
- Glycine-betaine biosynthesis.
- Potassium import and glutamate counter-ion accumulation.
- Sodium-proton antiport / sodium extrusion.
- Osmotic-stress response — **GO:0006970**.
- Mechanosensitive-channel-mediated solute release during downshock.
- Cytoplasm — **GO:0005737**; plasma membrane — **GO:0005886**.

## 3. Evidence-backed candidate edges

The highest-confidence intervention and physiological edges are summarized below.

| subject | predicate | object | evidence strength | organism/assay | quantitative result | DOI |
|---|---|---|---|---|---|---|
| `putA` deletion + `ΔectABC::proBm1AC` engineering | increases | high-NaCl growth tolerance | direct genetic/intervention | *Halomonas elongata* HN6; minimal medium with graded NaCl | Ect-deficient KA1 "could not grow" at >4% NaCl, whereas HN6 "thrived" at 8% NaCl; IC50 6.1% NaCl and IC25 7.2% NaCl for HN6 vs IC50 4.2% and IC25 5.2% for HN1 (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9) | 10.1128/aem.01195-24 |
| feedback-insensitive `proBm1AC` + `putA` deletion | increases | intracellular L-proline accumulation | direct genetic/intervention | *Halomonas elongata* HN6; M63/LB high-salt culture | 353.1 ± 40.5 µmol/g cell fresh weight Pro at 8% NaCl; 115.9 ± 7.8 µmol/g CFW at 6% NaCl; >100-fold above wild type/controls in 15% NaCl LB (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9) | 10.1128/aem.01195-24 |
| `betB` overexpression + `EcnhaA` overexpression | increases | maximum NaCl tolerance | direct genetic/intervention | *Pseudomonas putida* KT2440; MSM/KB growth under NaCl stress | tolerance increased from 4% to 5% (w/v) NaCl; engineered strain grew at 4% NaCl and enabled pollutant degradation under 4% NaCl (fan2024improvementinsalt pages 12-14) | 10.3390/biology13060404 |
| exogenous betaine supplementation | increases | growth under salt stress | direct intervention | *Pseudomonas putida* KT2440; MSM with 4-5% NaCl | at 4% NaCl, biomass increased by 154.4% vs control; at 5% NaCl biomass reached 0.64, enabling tolerance at 5% NaCl (fan2024improvementinsalt pages 5-8) | 10.3390/biology13060404 |
| exogenous proline supplementation | increases | growth under salt stress | direct intervention | *Pseudomonas putida* KT2440; MSM with 4-5% NaCl | at 4% NaCl, biomass increased by 188.1% vs control; at 5% NaCl biomass reached 0.38 (fan2024improvementinsalt pages 5-8) | 10.3390/biology13060404 |
| deletion of all four `mscS`-family genes | decreases | survival after hypoosmotic shock | direct genetic/intervention | *Halomonas elongata* mutant MSC-1324; downshock from 1 M to 0.1 M NaCl | mutant was "unable to cope with hypoosmotic shock"; ~100-fold fewer cells survived than wild type after downshock (vandrich2020contributionofmechanosensitive pages 1-2, vandrich2020contributionofmechanosensitive pages 8-9) | 10.1007/s00792-020-01168-y |
| deletion of all four `mscS`-family genes | increases | growth at high salinity | direct genetic/intervention | *Halomonas elongata* mutant MSC-1324; high-salt growth | knockout mutant "grew significantly faster than the wildtype at high salinity of 2 M NaCl" (vandrich2020contributionofmechanosensitive pages 1-2) | 10.1007/s00792-020-01168-y |
| deletion of all four `mscS`-family genes | does not abolish | ectoine export | direct genetic/intervention | *Halomonas elongata* KB2.13-MSC; ectoine excretion assay at 0.7 M and 2 M NaCl | mutant still exported ~80% of ectoine relative to parental strain; export deficit only 19-21% (vandrich2020contributionofmechanosensitive pages 1-2, vandrich2020contributionofmechanosensitive pages 8-9) | 10.1007/s00792-020-01168-y |
| increasing external NaCl | increases | glutamate counterion pool during early osmoadaptation | physiological association | *Bacillus megaterium* DSM319; metabolome/flux analysis across 0-1.8 M NaCl | glutamate pool peaked at 0.6 M NaCl and then declined at 1.2 M NaCl; described as counterion to imported K+ at moderate salt (godard2020metabolicrearrangementscausing pages 4-5) | 10.3389/fbioe.2020.00047 |
| increasing salinity | increases | ectoine accumulation | physiological association | *Spiribacter salinus* M19-40; SMM medium with 0-2.0 M NaCl | intracellular ectoine rose from ~80 µM at 0.6 M NaCl to ~170 µM at 0.8 M NaCl, with little further increase at 1.3 M (leon2018compatiblesolutesynthesis pages 10-11) | 10.3389/fmicb.2018.00108 |
| glycine betaine uptake | suppresses | ectoine synthesis | physiological association | *Spiribacter salinus* M19-40; radiolabeled glycine betaine/osmostress assay | salinity-dependent glycine betaine accumulation was observed and reported to suppress ectoine synthesis (leon2018compatiblesolutesynthesis pages 1-2) | 10.3389/fmicb.2018.00108 |


*Table: This table compiles the strongest directly supported causal and near-causal edges relevant to broad NaCl growth breadth for METPO:1000481. It prioritizes intervention/genetic evidence and clearly separates it from physiological associations that are informative but less suitable for immediate causal curation.*

### Additional curation-ready triples with supporting snippets

| Subject | Predicate | Object | Reference and supporting snippet | Curation note |
|---|---|---|---|---|
| Hyperosmotic NaCl exposure | initiates | K⁺/glutamate osmoadaptation | Godard et al.: glutamate served as the “counterion to imported potassium” at ≤0.6 M NaCl and peaked at 0.6 M (godard2020metabolicrearrangementscausing pages 4-5). | **Moderate confidence; physiological association.** Taxon-specific to *B. megaterium* DSM319; do not infer that K⁺ accumulation expands every organism’s growth breadth. |
| `ectABC` loss | reduces | high-NaCl growth capacity | Khanh et al.: “Ect-deficient *H. elongata* KA1 could not grow in minimal media containing more than 4% NaCl” (khanh2024metabolicpathwayengineering pages 1-2). | **Strong direct genetic evidence**, but source excerpt does not isolate whether complementation by native `ectABC` alone restores the bound. Curate as taxon- and medium-specific. |
| `proBm1AC` expression plus `putA` deletion | increases | intracellular proline | HN6 accumulated “353.1 ± 40.5 µmol/g cell fresh weight” at 8% NaCl; at 15% NaCl LB, HN6 accumulated 123.03 µmol/g versus 1.19 in relevant controls (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9). | **Strong intervention evidence.** Use a genotype-composite node or separate edges joined through proline accumulation. |
| Intracellular proline accumulation | enables | growth at 8% NaCl in an ectoine-deficient background | HN6 “thrived in the medium containing 8% NaCl by accumulating Pro in the cell instead of Ect” (khanh2024metabolicpathwayengineering pages 1-2). | **Strong but genotype-specific.** This is functional osmolyte substitution, not proof that proline universally replaces ectoine. |
| `putA` deletion | increases | proline accumulation | At 15% NaCl, KA1/HN1/HN2 accumulated 1.19/1.19/4.09 µmol g⁻¹ CFW, while corresponding `putA`-deficient HN4/HN5/HN6 accumulated 10.86/64.76/123.03 (khanh2024metabolicpathwayengineering pages 6-9). | **Strong comparative genetic evidence.** |
| Feedback-insensitive `proBm1` | increases | salt-induced proline biosynthetic flux | HN2 grew better at 6% NaCl, and the effect was further enhanced by `putA` deletion; expression was controlled by the salt-inducible `ectA` promoter (khanh2024metabolicpathwayengineering pages 6-9). | **Strong but construct-specific.** Prefer “increases proline accumulation” over a direct universal trait edge. |
| `betB` plus `EcnhaA` overexpression | increases | maximum NaCl tolerance | Fan et al.: “maximum salinity tolerance…increased to 5% w/v”; the unengineered minimal-medium ceiling was 4% (fan2024improvementinsalt pages 12-14). | **Strong direct engineering evidence.** The combined construct does not resolve the individual contribution to breadth. |
| Exogenous betaine | increases | KT2440 biomass at 4–5% NaCl | Biomass increased 154.4% at 4% NaCl and reached OD/biomass value 0.64 at 5% (fan2024improvementinsalt pages 5-8). | **Direct supplementation evidence**, conditional on uptake and medium composition. |
| Exogenous proline | increases | KT2440 biomass at 4–5% NaCl | Biomass increased 188.1% at 4% and reached 0.38 at 5% NaCl (fan2024improvementinsalt pages 5-8). | **Direct supplementation evidence**, not proof of endogenous synthesis. |
| EcnhaA overexpression | increases | KT2440 growth at 4% NaCl | “Overexpression of EcnhaA…could significantly improve the growth” at 4% NaCl (fan2024improvementinsalt pages 12-14). | **Direct, heterologous and host-specific.** Do not generalize to every NhaA paralog. |
| Individual `kdpA`, `kdpB`, or `kdpD` overexpression | does not increase | KT2440 growth at 4% NaCl | Each “failed to improve the growth” despite transcriptional upregulation under hypertonic conditions (fan2024improvementinsalt pages 12-14). | Useful **negative edge/evidence**; demonstrates that differential expression alone is not causal evidence. |
| Increasing salinity | increases | ectoine accumulation | *S. salinus* ectoine increased from approximately 80 µM at 0.6 M to 170 µM at 0.8 M NaCl, with little further increase at 1.3 M (leon2018compatiblesolutesynthesis pages 10-11). | **Physiological association**, not a direct breadth-expansion experiment. |
| Glycine-betaine uptake | suppresses | ectoine synthesis | Radiolabeled uptake demonstrated salinity-dependent betaine accumulation in unmodified form and suppression of ectoine synthesis (leon2018compatiblesolutesynthesis pages 1-2). | **Moderate-to-strong physiological evidence** for osmolyte substitution/regulation. |
| TeaABC | imports/recycles | ectoine | *H. elongata* accumulates environmental ectoine through the osmoregulated TeaABC transporter; TeaABC disruption produces constitutive ectoine loss (vandrich2020contributionofmechanosensitive pages 1-2). | **Direct transporter evidence**, but the retrieved study focused on export/recycling rather than growth-breadth endpoints. |
| Hypoosmotic downshock | activates functional need for | MscS-family channels | Sudden salt decrease causes water influx and turgor increase; channels serve as “emergency valves” (vandrich2020contributionofmechanosensitive pages 1-2). | Mechanistically authoritative, but activation was not inferred from increased transcription. |
| Four-channel `mscS`-family deletion | decreases | downshock survival | After 1→0.1 M NaCl downshock, approximately 100-fold fewer mutant cells survived than wild type (vandrich2020contributionofmechanosensitive pages 8-9). | **Strong direct genetic evidence** for breadth across fluctuating salinity, but it measures survival after a transition rather than steady-state growth breadth. |
| Four-channel `mscS`-family deletion | increases | growth at 2 M NaCl | The deletion mutant “grew significantly faster” at 2 M NaCl (vandrich2020contributionofmechanosensitive pages 1-2). | **Direct but counterintuitive, taxon-specific evidence.** Do not model MscS simply as promoting high-salt growth. |
| MscS-family channels | contribute only partly to | ectoine export | The quadruple mutant retained ~80% of parental ectoine export at 0.7 and 2 M NaCl (vandrich2020contributionofmechanosensitive pages 8-9). | Curate as a minor contribution or negative finding; an unknown major export pathway remains. |

## 4. Recommended compact causal structure

A defensible core graph for `nacl_delta_mid2_broad_breadth` is:

1. **increased external NaCl → hyperosmotic stress**;
2. **hyperosmotic stress → early K⁺ uptake**;
3. **K⁺ uptake → glutamate counter-ion accumulation**;
4. **ectABC → ectoine biosynthesis → intracellular ectoine accumulation → increased high-NaCl growth capacity**;
5. **proBAC → proline biosynthesis → intracellular proline accumulation → increased high-NaCl growth capacity**;
6. **putA → proline catabolism ┤ intracellular proline accumulation**;
7. **betB → glycine-betaine biosynthesis → compatible-solute accumulation → increased high-NaCl growth capacity**;
8. **NhaA-type antiport → Na⁺ extrusion/homeostasis → increased high-NaCl growth capacity**;
9. **TeaABC → ectoine uptake/recycling → intracellular ectoine pool**;
10. **decreased external NaCl → hypoosmotic water influx → increased membrane tension/turgor → MscS-family opening → solute release → downshock survival**;
11. **combined maintenance of growth at lower and upper tested bounds → “METPO:1000481”**.

Edges 4–8 should be attached to organism/genotype and assay context. The final edge must be asserted only when an actual 3–8 percentage-point growth interval is documented; a mechanism that improves growth at one concentration is evidence toward, but not by itself proof of, the target trait.

## 5. Recent developments, applications, and quantitative data

### 2024 mechanism engineering

Khanh et al. provided the strongest recent functional-substitution experiment. Replacing `ectABC` with salt-inducible feedback-insensitive `proBm1AC` and deleting `putA` moved an ectoine-deficient *H. elongata* background from inability to grow above 4% NaCl to growth at 8%. HN6 had IC50 and IC25 values of 6.1% and 7.2% NaCl, versus 4.2% and 5.2% for HN1, and accumulated 353.1 ± 40.5 µmol proline g⁻¹ fresh cells under optimized 8% NaCl conditions (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9). Published online 19 August 2024; DOI URL: https://doi.org/10.1128/aem.01195-24.

Fan et al. combined compatible-solute synthesis and ion extrusion in *P. putida* KT2440. `betB` plus *E. coli* `nhaA` raised the minimal-medium tolerance ceiling to 5% NaCl; betaine and proline supplementation increased biomass at 4% by 154.4% and 188.1%, respectively (fan2024improvementinsalt pages 5-8, fan2024improvementinsalt pages 12-14). Published June 2024; DOI URL: https://doi.org/10.3390/biology13060404.

### Real-world implementations

The engineered KT2440 strain degraded 56.70% of benzoic acid and 95.64% of protocatechuic acid in 48 h at 4% NaCl, while parental KT2440 showed no degradation under those conditions. Catechol degradation nevertheless failed above 2% NaCl, illustrating that salt tolerance of the chassis does not guarantee salt-tolerant performance of every metabolic function (fan2024improvementinsalt pages 12-14).

*H. elongata* is already an industrial ectoine producer; ectoine is manufactured at ton scale for health-care and skin-care uses. The 2024 proline-engineering work proposes the same robust halophile as a cell factory for converting high-salinity biomass waste into proline-rich single-cell aquaculture feed (khanh2024metabolicpathwayengineering pages 1-2, vandrich2020contributionofmechanosensitive pages 1-2).

A 2023 multi-omics platform for *Halomonas bluephagenesis* TD1.0 integrates KEGG enrichment, gene-expression clusters, and a genome-scale metabolic model. Machine learning identified osmolarity-dependent energy expenditure on motility and flagella, validated by microscopy and fluorescent flagellar staining. This is a current implementation for engineering an industrial chassis, but it does not by itself establish flagella as a cause of NaCl breadth (park2023onlineomicsplatform pages 1-2). Published 2023; DOI URL: https://doi.org/10.1177/11779322231171779.

A 2024 saline-wastewater review identifies salt-in and compatible-solute strategies as relevant to biohydrogen systems. It reports Na⁺/H⁺ antiporters (NhaA/NhaD/NhaP/Mrp), Trk/Ktr K⁺ uptake, and compatible solutes as major modules, while noting the energetic cost of organic-osmolyte synthesis and the specialized salt dependence of salt-in proteins (guo2024biohydrogenproductionfrom pages 16-18). Published September 2024; DOI URL: https://doi.org/10.18686/cest.v2i3.210.

## 6. Expert interpretation

The most defensible expert conclusion is that **broad NaCl growth breadth is an emergent systems phenotype**, not a marker-gene trait. Osmolyte synthesis, uptake, catabolism, sodium extrusion, potassium homeostasis, macromolecular protection, and safe downshock release interact, and their importance changes with taxon and assay. Three results particularly constrain simplistic graph construction:

1. Kdp genes were transcriptionally induced in KT2440, but their individual overexpression did not improve high-salt growth (fan2024improvementinsalt pages 12-14).
2. Removing all four *H. elongata* MscS-family channels impaired downshock survival yet accelerated growth at 2 M NaCl (vandrich2020contributionofmechanosensitive pages 1-2, vandrich2020contributionofmechanosensitive pages 8-9).
3. Proline could functionally replace ectoine in an engineered background, showing that chemically distinct osmolyte modules can converge on the same growth phenotype (khanh2024metabolicpathwayengineering pages 1-2).

Accordingly, intervention evidence should outrank transcriptomic enrichment or gene presence. Graph edges should carry evidence strength, taxon, genotype, medium, salinity, and whether the endpoint was growth, biomass, survival, metabolite level, or industrial activity.

## 7. Claims not yet suitable for TraitMech curation

- **Do not curate “gene present → NaCl delta mid2.”** Genome annotation of Trk, Mrp, antiporters, osmolyte genes, or chaperones is only mechanistic potential.
- **Do not curate transcript upregulation as causation.** The Kdp negative result directly demonstrates this problem (fan2024improvementinsalt pages 12-14).
- **Do not treat 3–8% growth as automatically a 5% breadth** unless growth continuity and both bounds were tested under the same assay.
- **Do not conflate optimum, maximum, IC50/IC25, survival, and breadth.** These should remain different phenotype/measurement nodes.
- **Do not universalize MscS as increasing salt tolerance.** Its strongest role here is protection during downshock; deletion improved steady-state growth at 2 M NaCl (vandrich2020contributionofmechanosensitive pages 1-2).
- **Do not assert MscS is the principal ectoine exporter.** The quadruple mutant retained approximately 80% of export, implying an unidentified dominant route (vandrich2020contributionofmechanosensitive pages 8-9).
- **Do not generalize EcnhaA to all NhaA proteins.** Endogenous KT2440 `nhaA-II` overexpression had only a slight effect, whereas heterologous EcnhaA was stronger (fan2024improvementinsalt pages 12-14).
- **Do not curate flagellar remodeling, membrane-component enrichment, quorum sensing, or two-component systems as causal breadth mechanisms** from omics enrichment alone (park2023onlineomicsplatform pages 1-2, fan2024improvementinsalt pages 5-8).
- **Do not combine “salt-in” archaea/anaerobes with compatible-solute bacteria into one universal intracellular-ion mechanism.** These strategies entail different proteome adaptations and energetic trade-offs (guo2024biohydrogenproductionfrom pages 16-18).
- **Do not assign unverified CURIEs.** Strain-specific proteins, constructs, promoter alleles, and assay terms should remain label-only until database records are checked.

## 8. DOI-first bibliography

1. Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H. “Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient *Halomonas elongata*.” *Applied and Environmental Microbiology* 90(9). Published online **19 August 2024**. https://doi.org/10.1128/aem.01195-24 (khanh2024metabolicpathwayengineering pages 1-2)
2. Fan M, Tan S, Wang W, Zhang X. “Improvement in Salt Tolerance Ability of *Pseudomonas putida* KT2440.” *Biology* 13:404. **June 2024**. https://doi.org/10.3390/biology13060404 (fan2024improvementinsalt pages 12-14)
3. Park H, Faulkner M, Toogood HS, Chen G-Q, Scrutton N. “Online Omics Platform Expedites Industrial Application of *Halomonas bluephagenesis* TD1.0.” *Bioinformatics and Biology Insights* 17. **2023**; accepted 7 April 2023. https://doi.org/10.1177/11779322231171779 (park2023onlineomicsplatform pages 1-2)
4. Guo H, Teng Z, Han H, Li T. “Biohydrogen production from saline wastewater: An overview.” *Clean Energy Science and Technology* 2:210. **September 2024**. https://doi.org/10.18686/cest.v2i3.210 (guo2024biohydrogenproductionfrom pages 16-18)
5. Vandrich J, Pfeiffer F, Alfaro-Espinoza G, Kunte HJ. “Contribution of mechanosensitive channels to osmoadaptation and ectoine excretion in *Halomonas elongata*.” *Extremophiles* 24:421–432. Published online **7 April 2020**. https://doi.org/10.1007/s00792-020-01168-y (vandrich2020contributionofmechanosensitive pages 1-2)
6. Godard T et al. “Metabolic Rearrangements Causing Elevated Proline and Polyhydroxybutyrate Accumulation During the Osmotic Adaptation Response of *Bacillus megaterium*.” *Frontiers in Bioengineering and Biotechnology* 8:47. **February 2020**. https://doi.org/10.3389/fbioe.2020.00047 (godard2020metabolicrearrangementscausing pages 4-5)
7. León MJ et al. “Compatible Solute Synthesis and Import by the Moderate Halophile *Spiribacter salinus*: Physiology and Genomics.” *Frontiers in Microbiology* 9:108. **February 2018**. https://doi.org/10.3389/fmicb.2018.00108 (leon2018compatiblesolutesynthesis pages 10-11)
8. Czech L et al. “Role of the Extremolytes Ectoine and Hydroxyectoine as Stress Protectants and Nutrients.” *Genes* 9:177. **March 2018**. https://doi.org/10.3390/genes9040177.
9. Gunde-Cimerman N, Plemenitaš A, Oren A. “Strategies of adaptation of microorganisms of the three domains of life to high salt concentrations.” *FEMS Microbiology Reviews* 42:353–375. **2018**. https://doi.org/10.1093/femsre/fuy009.

References

1. (leon2018compatiblesolutesynthesis pages 4-5): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

2. (fan2024improvementinsalt pages 5-8): Min Fan, Shuyu Tan, Wei Wang, and Xuehong Zhang. Improvement in salt tolerance ability of pseudomonas putida kt2440. Biology, 13:404, Jun 2024. URL: https://doi.org/10.3390/biology13060404, doi:10.3390/biology13060404. This article has 24 citations.

3. (khanh2024metabolicpathwayengineering pages 9-12): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

4. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

5. (godard2020metabolicrearrangementscausing pages 4-5): Thibault Godard, Daniela Zühlke, Georg Richter, Melanie Wall, Manfred Rohde, Katharina Riedel, Ignacio Poblete-Castro, Rainer Krull, and Rebekka Biedendieck. Metabolic rearrangements causing elevated proline and polyhydroxybutyrate accumulation during the osmotic adaptation response of bacillus megaterium. Frontiers in Bioengineering and Biotechnology, Feb 2020. URL: https://doi.org/10.3389/fbioe.2020.00047, doi:10.3389/fbioe.2020.00047. This article has 36 citations.

6. (vandrich2020contributionofmechanosensitive pages 1-2): Jasmina Vandrich, Friedhelm Pfeiffer, Gabriela Alfaro-Espinoza, and Hans Jörg Kunte. Contribution of mechanosensitive channels to osmoadaptation and ectoine excretion in halomonas elongata. Extremophiles, 24:421-432, Apr 2020. URL: https://doi.org/10.1007/s00792-020-01168-y, doi:10.1007/s00792-020-01168-y. This article has 40 citations and is from a peer-reviewed journal.

7. (guo2024biohydrogenproductionfrom pages 16-18): Huiyuan Guo, Zedong Teng, Hexing Han, and Tinggang Li. Biohydrogen production from saline wastewater: an overview. Clean Energy Science and Technology, 2:210, Sep 2024. URL: https://doi.org/10.18686/cest.v2i3.210, doi:10.18686/cest.v2i3.210. This article has 5 citations.

8. (leon2018compatiblesolutesynthesis pages 1-2): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

9. (khanh2024metabolicpathwayengineering pages 6-9): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

10. (fan2024improvementinsalt pages 12-14): Min Fan, Shuyu Tan, Wei Wang, and Xuehong Zhang. Improvement in salt tolerance ability of pseudomonas putida kt2440. Biology, 13:404, Jun 2024. URL: https://doi.org/10.3390/biology13060404, doi:10.3390/biology13060404. This article has 24 citations.

11. (vandrich2020contributionofmechanosensitive pages 8-9): Jasmina Vandrich, Friedhelm Pfeiffer, Gabriela Alfaro-Espinoza, and Hans Jörg Kunte. Contribution of mechanosensitive channels to osmoadaptation and ectoine excretion in halomonas elongata. Extremophiles, 24:421-432, Apr 2020. URL: https://doi.org/10.1007/s00792-020-01168-y, doi:10.1007/s00792-020-01168-y. This article has 40 citations and is from a peer-reviewed journal.

12. (leon2018compatiblesolutesynthesis pages 10-11): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

13. (park2023onlineomicsplatform pages 1-2): Helen Park, Matthew Faulkner, Helen S Toogood, Guo-Qiang Chen, and Nigel Scrutton. Online omics platform expedites industrial application of halomonas bluephagenesis td1.0. Bioinformatics and Biology Insights, Jan 2023. URL: https://doi.org/10.1177/11779322231171779, doi:10.1177/11779322231171779. This article has 2 citations and is from a peer-reviewed journal.