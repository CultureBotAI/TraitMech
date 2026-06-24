---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:46:15.471173'
end_time: '2026-06-18T02:03:31.221194'
duration_seconds: 1035.75
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature delta mid1
  trait_identifier: METPO:1000485
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_delta_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature delta phenotype with a growth-supporting temperature\
    \ breadth of approximately 10\u201320 \xB0C, characteristic of organisms with\
    \ moderate thermal-tolerance breadth."
  parent_traits: METPO:1000303
  synonyms: Td_10_20
  evidence_summary: 'DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty
    acids (Membrane-adaptation review supports moderate homoviscous remodeling capacity
    as common among generalist mesophiles.)'
  causal_graph_summary: 'temperature_delta_mid1_moderate_breadth: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta mid1
- **METPO identifier:** METPO:1000485
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 10–20 °C, characteristic of organisms with moderate thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_10_20
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports moderate homoviscous remodeling capacity as common among generalist mesophiles.)
- **Existing causal graph summary:** temperature_delta_mid1_moderate_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_mid1.yaml`.

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
- **Trait label:** temperature delta mid1
- **METPO identifier:** METPO:1000485
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 10–20 °C, characteristic of organisms with moderate thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_10_20
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports moderate homoviscous remodeling capacity as common among generalist mesophiles.)
- **Existing causal graph summary:** temperature_delta_mid1_moderate_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_mid1.yaml`.

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


## Research report: Microbial trait **temperature delta mid1** (Td_10_20; METPO:1000485)

### Scope summary (trait semantics)
**temperature delta mid1** represents a *moderate growth-supporting temperature breadth* phenotype: organisms whose growth is supported across an intermediate temperature span (approximately **10–20 °C**) rather than being strict specialists (narrow span) or broad generalists (wide span). Operationally, temperature-breadth phenotypes are quantified from **thermal performance (growth) curves** using *cardinal temperatures* **Tmin**, **Topt**, and **Tmax**, where **Tmin and Tmax bound the growth-permissive interval** (the organism’s “thermal tolerance/thermal niche”). (noll2020modelingandexploiting pages 6-8)

A common quantitative descriptor is **Trange = Tmax − Tmin** (chaloner2020geometryandevolution pages 1-2). For Td_10_20 curation, Trange should be interpreted as **growth in culture under defined medium and assay conditions**, because different biological processes can yield different apparent temperature ranges (e.g., axenic growth vs host-associated processes), meaning realized thermal ranges can be narrower than fundamental (axenic) ranges. (chaloner2020geometryandevolution pages 1-2)

**Boundary cases / nearby traits.**
* **Narrow-breadth specialists:** psychrophiles and some thermophiles with limited permissive windows; e.g., psychrophiles can grow at 0 °C and have optima around ~15 °C but do not grow at 20 °C (review definition). (ramon2023ageneraloverview pages 1-2)
* **Broad-breadth generalists:** taxa with very wide Tmin–Tmax spans; e.g., some thermophiles show spans >>20 °C (review examples; useful as contrast but outside Td_10_20). (lehmann2023adaptivelaboratoryevolution pages 1-2)
* **Assay dependence:** “growth/no-growth across temperatures” is the most direct proxy of breadth; example of narrow breadth: *Pseudarthrobacter psychrotolerans* YJ56 shows “superior growth at 13 °C” and “could not grow at 30 °C,” illustrating narrow growth breadth. (son2023morphologicalandphysiological pages 1-2)

### Key concepts & definitions (current understanding)
1. **Thermal performance curve (TPC):** growth rate µ as a function of temperature. Thermal performance is often quantified by **specific growth rate µ** (“reciprocal of generation time”) and summarized by cardinal temperatures. (noll2020modelingandexploiting pages 6-8)
2. **Thermal tolerance / niche / breadth:** the growth-permissive interval bracketed by **Tmin** and **Tmax** (“mark the thermal tolerance or thermal niche of an organism”). (noll2020modelingandexploiting pages 6-8)
3. **Temperature range (Trange):** **Tmax − Tmin** used as a breadth descriptor. (chaloner2020geometryandevolution pages 1-2)
4. **Mechanistic interpretation for moderate breadth:** Td_10_20 can be conceptualized as requiring **sufficient physiological plasticity** to maintain critical cellular functions across moderate temperature swings—especially membrane biophysics and proteostasis.

### Candidate causal-graph entities (nodes) for TraitMech curation
Below are candidate nodes likely to recur across taxa that fall into moderate temperature breadth classes.

#### A) Phenotype / assay nodes
- Growth-supporting temperature breadth / Trange (label node; METPO:1000485 as trait)
- Tmin, Topt, Tmax (cardinal temperature nodes; label-only unless ontology used)
- Growth rate µ (label-only; often measured as specific growth rate) (noll2020modelingandexploiting pages 6-8)
- Temperature shift (environmental perturbation; ENVO:01000340 “temperature” is typically used, but not grounded here)

#### B) Environmental & experimental factor nodes
- Low temperature / cold shock (treatment)
- Mild temperature shock vs harsh cold shock (important for DesK function in vivo) (sidarta2024lipidphaseseparation pages 1-2)
- Media composition / growth condition (boundary-case modifier; label-only)

#### C) Membrane & lipid adaptation nodes (homeoviscous adaptation)
**Processes / functions (suggest GO nodes; exact IDs should be looked up during YAML curation):**
- Homeoviscous adaptation (label; GO grounding TBD)
- Fatty acid biosynthesis (GO:0006633)
- Fatty acid desaturation (GO:0033988)

**Genes/proteins (labels; UniProt grounding deferred to strain/species):**
- **Bacillus** DesK/DesR/Des system: **DesK** (histidine kinase/phosphatase), **DesR** (response regulator), **Des** (acyl lipid Δ5 desaturase) (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation media fa0513c8)
- **E. coli-type anaerobic UFA synthesis:** **FabA**, **FabB**, **FabF**, **FabH**, regulator **FabR** (ramon2023ageneraloverview pages 2-4)
- **E. coli UFA regulator:** **FadR** (regulator controlling UFA synthesis; perturbation used to reduce UFAs) (lehmann2023adaptivelaboratoryevolution pages 6-7)

**Chemicals/metabolites (CHEBI grounding recommended during curation):**
- cis-unsaturated fatty acids (category)
- **cis-vaccenic acid (18:1)** (ramon2023ageneraloverview pages 2-4)
- **palmitoleic acid (C16:1)** (dessenne2024lipidomicanalysesreveal pages 1-2)
- **oleic acid (C18:1)** (dessenne2024lipidomicanalysesreveal pages 1-2)

#### D) Stress response / proteostasis nodes
- Chaperones (general)
- **GroEL** (chaperonin), stress-induced (son2023morphologicalandphysiological pages 1-2)
- **KatE** catalase (oxidative stress defense; heat-stress associated) (son2023morphologicalandphysiological pages 1-2)

#### E) Stringent response / growth-division coupling nodes
- (p)ppGpp (alarmone; CHEBI grounding recommended)
- Cell division genes **ftsQ**, **ftsA**, **ftsZ** (rescue of growth defect from low membrane fluidity) (lehmann2023adaptivelaboratoryevolution pages 6-7)

#### F) Compatible solutes / cryoprotectants
- Compatible solutes (process node)
- **betaine**, **trehalose**, **glycerol**, **sucrose**, **mannitol**, **sorbitol** (review-level list) (purwar2024adaptationsofpsychrophilic pages 10-11)

### Evidence-backed candidate causal edges (triples)
The table below is designed to be directly translatable into `temperature_delta_mid1.yaml` edges (with taxon/assay qualifiers). It prioritizes 2023–2024 evidence where available.

| Edge (subject—predicate—object) | Mechanistic rationale (1 sentence) | Evidence snippet (short quote) | Source (first author year, journal) | DOI URL | Pub date (month/year if known) | Confidence (high/med/low) | Notes for curation (assay/taxon specificity, boundary cases) |
|---|---|---|---|---|---|---|---|
| decrease in temperature — causes — membrane rigidification/thickening | Cooling can thicken/rigidify bacterial membranes, creating the proximal physical signal for homeoviscous adaptation. | “Upon temperature decrease the membrane rigidifies and thickens” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta 2024, Microbiology Spectrum | https://doi.org/10.1128/spectrum.03925-23 | 06/2024 | high | Directly supported in *Bacillus subtilis* des system; physical membrane state is a broadly relevant intermediate rather than a trait-defining node by itself. |
| membrane rigidification/thickening — activates kinase activity of — DesK | DesK is a membrane physical-state sensor that switches to kinase mode when the bilayer thickens under cold conditions. | “activating DesK’s kinase state” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta 2024, Microbiology Spectrum | https://doi.org/10.1128/spectrum.03925-23 | 06/2024 | high | Strong mechanistic edge, but taxon-specific to organisms carrying DesK/DesR; not universal across mesophiles. |
| DesK kinase activity — phosphorylates — DesR | In the canonical des pathway, activated DesK transfers phosphate to the response regulator DesR. | “leading to phosphorylation of DesR” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta 2024, Microbiology Spectrum | https://doi.org/10.1128/spectrum.03925-23 | 06/2024 | high | Good curation candidate as part of a pathway subgraph for *B. subtilis*-like systems. |
| phosphorylated DesR — induces expression of — des (lipid desaturase) | Phosphorylated DesR binds the promoter and induces the desaturase gene that remodels membrane lipids. | “binding to Pdes, and induction of des expression” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta 2024, Microbiology Spectrum | https://doi.org/10.1128/spectrum.03925-23 | 06/2024 | high | Strong mechanistic support; assay involves promoter activation and current model of des system. |
| des (lipid desaturase) activity — increases — membrane unsaturated fatty acids | Des-mediated desaturation adds double bonds to existing lipids, increasing unsaturation. | “The acyl lipid Δ5 desaturase Des is central to the rapid response” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta 2024, Microbiology Spectrum | https://doi.org/10.1128/spectrum.03925-23 | 06/2024 | med | The excerpt implies rather than explicitly quantifies UFA increase; still a standard, well-supported interpretation within the cited model. |
| increased membrane unsaturated fatty acids — increases — membrane fluidity | More unsaturated acyl chains counteract cold-induced rigidification and restore fluidity. | “Des-mediated desaturation fluidizes membranes” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta 2024, Microbiology Spectrum | https://doi.org/10.1128/spectrum.03925-23 | 06/2024 | high | Central homeoviscous-adaptation edge; likely generalizable beyond *B. subtilis*. |
| decrease in temperature — increases — cis-unsaturated fatty acid biosynthesis | In many bacteria, colder temperature shifts fatty-acid synthesis toward cis-unsaturated products to preserve membrane function. | “increased unsaturation (especially cis-MUFA)” (ramon2023ageneraloverview pages 2-4) | Ramón 2023, Brazilian Journal of Microbiology | https://doi.org/10.1007/s42770-023-01057-4 | 07/2023 | high | Broad review support; appropriate as a higher-level edge for moderate temperature breadth phenotypes. |
| FabA — participates in — cis-unsaturated fatty acid biosynthesis | FabA introduces cis double bonds during anaerobic UFA synthesis, contributing to colder-temperature adaptation. | “FabA (introduces cis double bonds)” (ramon2023ageneraloverview pages 2-4) | Ramón 2023, Brazilian Journal of Microbiology | https://doi.org/10.1007/s42770-023-01057-4 | 07/2023 | high | Gene-level edge from review; mechanistically grounded in *E. coli*-type pathway. |
| FabB — elongates — cis-unsaturated fatty acid intermediate | FabB extends the cis-unsaturated intermediate produced by FabA in the UFA synthesis pathway. | “FabB (elongates the cis-10-carbon intermediate)” (ramon2023ageneraloverview pages 2-4) | Ramón 2023, Brazilian Journal of Microbiology | https://doi.org/10.1007/s42770-023-01057-4 | 07/2023 | high | Good pathway-detail node if TraitMech captures enzyme chain logic. |
| FabR — regulates — fabA/fabB expression | FabR links fatty-acid status to transcriptional control of unsaturated-fatty-acid biosynthesis genes. | “FabR which binds UFA/SFA-CoA or -ACP and the promoters of fabA/fabB” (ramon2023ageneraloverview pages 2-4) | Ramón 2023, Brazilian Journal of Microbiology | https://doi.org/10.1007/s42770-023-01057-4 | 07/2023 | high | Regulatory edge is strong, but mainly grounded in *E. coli* and close relatives. |
| decrease in temperature — increases — cis-vaccenic acid | In *E. coli*, one documented rapid cold-response output is increased cis-vaccenic acid in the membrane. | “cis-vaccenic acid increases rapidly when temperature drops” (ramon2023ageneraloverview pages 2-4) | Ramón 2023, Brazilian Journal of Microbiology | https://doi.org/10.1007/s42770-023-01057-4 | 07/2023 | high | Very useful chemical-level edge; taxon-specific but canonical. |
| lower temperature (18°C vs 37°C) — increases — palmitoleic acid (C16:1) in GPLs | In *A. baumannii*, moderate cooling within a 19°C shift drives higher monounsaturated GPL acyl chains consistent with homeoviscous adaptation. | “At 18°C, five strains increased palmitoleic acid (C16:1)” (dessenne2024lipidomicanalysesreveal pages 1-2) | Dessenne 2024, Microbiology Spectrum | https://doi.org/10.1128/spectrum.00757-24 | 10/2024 | high | Especially relevant to Td_10_20 because the experiment compares 18°C and 37°C; strain-level variation should be noted. |
| lower temperature (18°C vs 37°C) — increases — oleic acid (C18:1) in GPLs | Some *A. baumannii* strains use C18:1 enrichment rather than C16:1 enrichment at lower temperature. | “ABVal2 uniquely shows an increase in oleic acid (C18:1)” (dessenne2024lipidomicanalysesreveal pages 1-2) | Dessenne 2024, Microbiology Spectrum | https://doi.org/10.1128/spectrum.00757-24 | 10/2024 | high | Strain-specific branch; curate as conditional or uncertain across species/strains. |
| FabA presence — supports — unsaturated fatty acid synthesis at lower temperature | Presence of FabA in some *A. baumannii* strains is consistent with capacity for expanded UFA remodeling under cooling. | “this enzyme was found in both ABVal2 and ABVal3” (dessenne2024lipidomicanalysesreveal pages 1-2) | Dessenne 2024, Microbiology Spectrum | https://doi.org/10.1128/spectrum.00757-24 | 10/2024 | med | Correlative genomic support rather than direct genetic perturbation; keep as weaker mechanistic edge. |
| candidate desaturases — may contribute to — low-temperature lipid remodeling | Additional desaturases may underlie strain-specific C18:1/C16:1 remodeling at 18°C. | “ABVal2 contains five candidate desaturases that may contribute to its lipid profile” (dessenne2024lipidomicanalysesreveal pages 1-2) | Dessenne 2024, Microbiology Spectrum | https://doi.org/10.1128/spectrum.00757-24 | 10/2024 | low | Explicitly tentative (“candidate”, “may contribute”); useful hypothesis node but weak for direct curation. |
| FadR inactivation — reduces — membrane unsaturated fatty acids | Lowering UFA synthesis through FadR inactivation shifts the membrane toward lower fluidity. | “Lowering unsaturated fatty acid synthesis by inactivation of FadR reduced the proportion of unsaturated fatty acids in the membrane” (lehmann2023adaptivelaboratoryevolution pages 6-7) | Singh 2024, Molecular Microbiology | https://doi.org/10.1111/mmi.15323 | 10/2024 | high | Strong perturbation evidence in *E. coli*; mechanistic but not directly a breadth phenotype assay. |
| reduced membrane unsaturated fatty acids — decreases — membrane fluidity | Loss of UFA content causes fluidity loss, creating a downstream cell-division stress. | “changes in membrane fatty acid composition lead to fluidity loss” (lehmann2023adaptivelaboratoryevolution pages 6-7) | Singh 2024, Molecular Microbiology | https://doi.org/10.1111/mmi.15323 | 10/2024 | high | Useful general edge linking membrane composition to physiology. |
| decreased membrane fluidity — requires — (p)ppGpp for cell division | When fluidity drops, *E. coli* relies on stringent-response alarmone signaling to maintain division. | “cell division was dependent on the guanine nucleotide analogous (p)ppGpp” (lehmann2023adaptivelaboratoryevolution pages 6-7) | Singh 2024, Molecular Microbiology | https://doi.org/10.1111/mmi.15323 | 10/2024 | high | Important conditional edge; relevant as a buffering mechanism rather than a primary breadth determinant. |
| ftsQ/ftsA/ftsZ overexpression — rescues — growth defect from membrane fluidity loss | Increasing core division machinery can bypass the division defect associated with reduced membrane fluidity. | “Combined expression of cell division genes ftsQ, ftsA and ftsZ from plasmid rescued the growth defect” (lehmann2023adaptivelaboratoryevolution pages 6-7) | Singh 2024, Molecular Microbiology | https://doi.org/10.1111/mmi.15323 | 10/2024 | high | Rescue assay is strong but highly specific to *E. coli* experimental setup. |
| temperature stress at 25°C in *Pseudarthrobacter psychrotolerans* YJ56 — upregulates — GroEL | Chaperone induction under supra-optimal temperature helps proteostasis when a cold-adapted organism experiences heat stress. | “showing the upregulation of chaperone proteins, GroEL” (son2023morphologicalandphysiological pages 1-2) | Son 2023, Scientific Reports | https://doi.org/10.1038/s41598-023-42179-x | 09/2023 | high | Important stress-response edge, but from a psychrophile exposed to stressful 25°C rather than a general mesophile breadth assay. |
| temperature stress at 25°C in *Pseudarthrobacter psychrotolerans* YJ56 — upregulates — KatE catalase | Heat stress in this psychrophile also induces oxidative-stress defense, linking thermal stress to ROS management. | “showing the upregulation of chaperone proteins, GroEL and catalase, KatE” (son2023morphologicalandphysiological pages 1-2) | Son 2023, Scientific Reports | https://doi.org/10.1038/s41598-023-42179-x | 09/2023 | high | Good mechanistic support for oxidative-stress/proteostasis subgraph; likely not specific to Td_10_20 alone. |
| compatible solutes (e.g., betaine, trehalose, sucrose, mannitol, sorbitol) — promote — cryoprotection/cold tolerance | Accumulation of compatible solutes is a recurring cold-adaptation strategy that protects cells under low-temperature stress. | “Compatible solutes explicitly listed include glycine, betaine, glycerol, trehalose, sucrose, mannitol, sorbitol” (purwar2024adaptationsofpsychrophilic pages 10-11) | Purwar 2024, Applied Microbiology: Theory ＆ Technology | https://doi.org/10.37256/amtt.5220244537 | 10/2024 | med | Review-level support and broad generalization; no single causal test for Td_10_20, so keep as higher-level/uncertain edge. |
| membrane state change at low temperature — activates — two-component cold signaling | Membrane physical-state changes can act as the upstream sensor event for cold adaptation responses. | “Cold sensing occurs via changes in the liquid-crystalline state of membranes that activate two-component signalling” (ramon2023ageneraloverview pages 1-2) | Ramón 2023, Brazilian Journal of Microbiology | https://doi.org/10.1007/s42770-023-01057-4 | 07/2023 | med | Broad review statement; informative, but specific sensor identities vary by taxon. |
| Tmin and Tmax — define — thermal niche/breadth | Thermal breadth is operationally measured as the span bounded by growth-supporting minimum and maximum temperatures. | “The minimum and maximum temperatures (Tmin and Tmax, respectively) for growth flank the asymmetric function and mark the thermal tolerance or thermal niche of an organism” (noll2020modelingandexploiting pages 6-8) | Noll 2020, Processes | https://doi.org/10.3390/pr8010121 | 01/2020 | high | Essential scope/definition edge for curating phenotype boundaries; not mechanistic but should anchor trait semantics. |
| temperature range (Trange) — equals — Tmax − Tmin | Trange is the standard quantitative descriptor for breadth-like temperature phenotypes. | “temperature range (Trange) is defined as Tmax–Tmin” (chaloner2020geometryandevolution pages 1-2) | Chaloner 2020, Nature Communications | https://doi.org/10.1038/s41467-020-16778-5 | 06/2020 | high | Best used in trait metadata or assay-definition section rather than mechanistic subgraph. |


*Table: This table compiles evidence-backed candidate causal edges relevant to the moderate microbial temperature-breadth trait Td_10_20. It emphasizes experimentally supported membrane-remodeling, stress-response, and trait-definition edges, while flagging taxon specificity and weaker inference for curation.*

### Central mechanistic model (with figure evidence)
A well-characterized, curation-ready subgraph for temperature-driven membrane adaptation is the **Bacillus subtilis DesK/DesR/des** system. Figure evidence shows a **cold-to-membrane-thickening-to-DesK kinase-to-DesR-to-des-to-membrane-fluidization** feedback loop, and the opposite behavior in warmer conditions. (sidarta2024lipidphaseseparation media fa0513c8)

### Recent developments and latest research (2023–2024 emphasis)
1. **In vivo limitations of canonical membrane sensors:** Sidarta et al. (2024) report that **des expression is activated only by mild temperature shocks** and that **lipid phase separation can impair DesK thickness sensing** by partitioning DesK into fluid domains, raising cautions about extrapolating simplified in vitro sensing models to in vivo conditions. (sidarta2024lipidphaseseparation pages 1-2)
2. **Strain-to-strain diversity in homeoviscous adaptation:** Dessenne et al. (2024) used lipidomics to show that at **18 °C vs 37 °C**, most *A. baumannii* strains increased **C16:1**, whereas one strain increased **C18:1**, and some strains carried **FabA** and additional candidate desaturases—highlighting heterogeneity in the genetic basis of membrane remodeling at moderate temperature differences. (dessenne2024lipidomicanalysesreveal pages 1-2)
3. **Coupling of membrane physics to cell-cycle control:** Singh & Harinarayanan (2024) connect membrane fluidity loss (via reduced UFA content after **FadR inactivation**) to a requirement for **(p)ppGpp** and show that overexpressing **ftsQ/ftsA/ftsZ** can rescue growth defects, offering a mechanistic route by which membrane constraints could translate into temperature-breadth constraints. (lehmann2023adaptivelaboratoryevolution pages 6-7)
4. **Cold-adaptation synthesis with gene-level detail:** Ramón et al. (2023) provide a mechanistically explicit review of cold membrane adaptation, naming **FabA/FabB/FabR** and detailing how microbes increase cis-unsaturation and remodel chain length/branching to preserve function. (ramon2023ageneraloverview pages 2-4)

### Current applications and real-world implementations
Temperature-breadth phenotypes directly affect:
- **Bioprocess robustness:** Thermal growth models and cardinal temperature concepts are used in industrial microbiology to describe and optimize microbial growth conditions and to interpret temperature control strategies. (noll2020modelingandexploiting pages 6-8)
- **Food and built-environment microbiology:** Moderate breadth organisms can persist across modest temperature fluctuations typical of processing/storage environments; mechanistic insights into cross-protection and membrane remodeling inform risk assessment and process design (conceptual linkage; mechanistic evidence here centers on membrane and stress systems). (lehmann2023adaptivelaboratoryevolution pages 6-7, sidarta2024lipidphaseseparation pages 1-2)

### Expert opinions / authoritative synthesis points (from reviews)
- A central theme in cold adaptation is that **membranes serve as both the temperature sensor and the adaptation target**, with two-component signaling frequently linked to membrane physical-state changes. (ramon2023ageneraloverview pages 1-2)
- Temperature tolerance breadth is best treated as a **cardinal-temperature bounded niche property** (Tmin/Tmax) rather than a single optimum-temperature metric. (noll2020modelingandexploiting pages 6-8, chaloner2020geometryandevolution pages 1-2)

### Relevant statistics and recent data points
- **Moderate experimental temperature deltas aligning with Td_10_20:** *A. baumannii* lipid remodeling was profiled at **18 °C vs 37 °C** (Δ=19 °C), showing consistent increases in monounsaturated fatty acids in most strains—an experimentally relevant temperature window for curating Td_10_20 mechanisms. (dessenne2024lipidomicanalysesreveal pages 1-2)
- **Cold adaptation temperature benchmarks (definitions):** psychrophiles can grow at **0 °C** and have optima around **~15 °C** but do not grow at **20 °C** (definition-level data useful for boundary cases). (ramon2023ageneraloverview pages 1-2)

### Warnings / claims not yet ready for strong curation
- **Candidate desaturases in *A. baumannii*:** the study explicitly frames these as “candidate” enzymes that “may contribute,” so edges linking these desaturases to lipid remodeling should be curated as **low confidence** or **hypothesis** unless validated genetically/biochemically. (dessenne2024lipidomicanalysesreveal pages 1-2)
- **Compatible solutes → temperature breadth:** evidence here is **review-level** listing of solutes associated with cold tolerance, without direct causal tests tied to breadth; treat as **high-level, uncertain** edges until organism-specific perturbation evidence is added. (purwar2024adaptationsofpsychrophilic pages 10-11)
- **Generalizing DesK/DesR/des:** DesKR is a strong mechanistic model but **taxon-specific**; other bacteria rely on different sensors/regulators.

---

## DOI-first bibliography (with URLs and publication dates)

1. Sidarta M, et al. *Lipid phase separation impairs membrane thickness sensing by the Bacillus subtilis sensor kinase DesK.* **Microbiology Spectrum**. **Jun 2024**. DOI: 10.1128/spectrum.03925-23. https://doi.org/10.1128/spectrum.03925-23 (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation media fa0513c8)
2. Dessenne C, et al. *Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of Acinetobacter baumannii.* **Microbiology Spectrum**. **Oct 2024**. DOI: 10.1128/spectrum.00757-24. https://doi.org/10.1128/spectrum.00757-24 (dessenne2024lipidomicanalysesreveal pages 1-2)
3. Singh V, Harinarayanan R. *(p)ppGpp Buffers Cell Division When Membrane Fluidity Decreases in Escherichia coli.* **Molecular Microbiology**. **Oct 2024**. DOI: 10.1111/mmi.15323. https://doi.org/10.1111/mmi.15323 (lehmann2023adaptivelaboratoryevolution pages 6-7)
4. Ramón A, et al. *A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.* **Brazilian Journal of Microbiology**. **Jul 2023**. DOI: 10.1007/s42770-023-01057-4. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 2-4)
5. Son Y, et al. *Morphological and physiological adaptations of psychrophilic Pseudarthrobacter psychrotolerans YJ56 under temperature stress.* **Scientific Reports**. **Sep 2023**. DOI: 10.1038/s41598-023-42179-x. https://doi.org/10.1038/s41598-023-42179-x (son2023morphologicalandphysiological pages 1-2)
6. Purwar S, Srivastava S. *Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.* **Applied Microbiology: Theory & Technology**. **Oct 2024**. DOI: 10.37256/amtt.5220244537. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 10-11)
7. Noll P, et al. *Modeling and Exploiting Microbial Temperature Response.* **Processes**. **Jan 2020**. DOI: 10.3390/pr8010121. https://doi.org/10.3390/pr8010121 (noll2020modelingandexploiting pages 6-8)
8. Chaloner TM, et al. *Geometry and evolution of the ecological niche in plant-associated microbes.* **Nature Communications**. **Jun 2020**. DOI: 10.1038/s41467-020-16778-5. https://doi.org/10.1038/s41467-020-16778-5 (chaloner2020geometryandevolution pages 1-2)


References

1. (noll2020modelingandexploiting pages 6-8): Philipp Noll, Lars Lilge, Rudolf Hausmann, and Marius Henkel. Modeling and exploiting microbial temperature response. ArXiv, 8:121, Jan 2020. URL: https://doi.org/10.3390/pr8010121, doi:10.3390/pr8010121. This article has 69 citations.

2. (chaloner2020geometryandevolution pages 1-2): Thomas M. Chaloner, Sarah J. Gurr, and Daniel P. Bebber. Geometry and evolution of the ecological niche in plant-associated microbes. Nature Communications, Jun 2020. URL: https://doi.org/10.1038/s41467-020-16778-5, doi:10.1038/s41467-020-16778-5. This article has 92 citations and is from a highest quality peer-reviewed journal.

3. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

4. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

5. (son2023morphologicalandphysiological pages 1-2): Yongjun Son, Jihyeon Min, Yoonjae Shin, and Woojun Park. Morphological and physiological adaptations of psychrophilic pseudarthrobacter psychrotolerans yj56 under temperature stress. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42179-x, doi:10.1038/s41598-023-42179-x. This article has 17 citations and is from a peer-reviewed journal.

6. (sidarta2024lipidphaseseparation pages 1-2): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

7. (sidarta2024lipidphaseseparation media fa0513c8): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

8. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

9. (lehmann2023adaptivelaboratoryevolution pages 6-7): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

10. (dessenne2024lipidomicanalysesreveal pages 1-2): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

11. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.