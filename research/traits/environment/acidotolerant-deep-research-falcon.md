---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:02:26.305742'
end_time: '2026-06-17T21:15:25.578818'
duration_seconds: 779.27
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: acidotolerant
  trait_identifier: METPO:1003008
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: acidotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference characterized by the ability to tolerate acidic
    environments (typically pH below 5.5) while maintaining optimal growth near neutral
    pH.
  parent_traits: METPO:1003000
  synonyms: aciduric
  evidence_summary: 'DOI:10.1038/nrmicro2549: tolerate and grow at external pH values
    (Supports acidotolerance as growth or survival under otherwise stressful external
    pH conditions.)'
  causal_graph_summary: 'acidotolerant_acid_stress_homeostasis: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** acidotolerant
- **METPO identifier:** METPO:1003008
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by the ability to tolerate acidic environments (typically pH below 5.5) while maintaining optimal growth near neutral pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** aciduric
- **Existing evidence:** DOI:10.1038/nrmicro2549: tolerate and grow at external pH values (Supports acidotolerance as growth or survival under otherwise stressful external pH conditions.)
- **Existing causal graph summary:** acidotolerant_acid_stress_homeostasis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **acidotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/acidotolerant.yaml`.

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
- **Trait label:** acidotolerant
- **METPO identifier:** METPO:1003008
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by the ability to tolerate acidic environments (typically pH below 5.5) while maintaining optimal growth near neutral pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** aciduric
- **Existing evidence:** DOI:10.1038/nrmicro2549: tolerate and grow at external pH values (Supports acidotolerance as growth or survival under otherwise stressful external pH conditions.)
- **Existing causal graph summary:** acidotolerant_acid_stress_homeostasis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **acidotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/acidotolerant.yaml`.

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


## Microbial trait causal graph curation report: **acidotolerant** (METPO:1003008)

### Scope summary (TraitMech curation intent)
**Acidotolerant (aciduric)** organisms tolerate acidic environments (typically <pH 5.5) while retaining an optimum near neutral pH (as in the provided METPO definition). Mechanistically, the common unifying feature is **maintenance of cytoplasmic pH homeostasis** under external acid stress, via (i) proton-consuming reactions, (ii) reduced proton influx/controlled ion transport, and (iii) protection/repair of macromolecules damaged by acid stress. (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 6-8)

**Boundary cases / nearby traits**
- **Acidophilic** microbes are adapted to grow optimally at low external pH; “extremely acidophilic” bacteria can grow at external pH <3 (often pH 1–3). This should be separated from acidotolerance in neutralophiles. (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 14-15)
- **Extreme-acid resistance** (survival at pH ~2–3) is often discussed for enterics (e.g., stomach transit) and can share mechanisms (e.g., amino-acid decarboxylases), but trait curation for “acidotolerant” should focus on **tolerance/growth under acidic conditions** rather than only survival after extreme acid shock. (li2024responseofescherichia pages 2-4, krulwich2011molecularaspectsof pages 5-6)
- **Acid acclimation** (as defined for Gram-negative neutralophiles) is specifically the ability to keep **periplasmic pH near neutral** in highly acidic media, permitting survival and growth—related but not identical to general acidotolerance. (krulwich2011molecularaspectsof pages 14-15)

### Key concepts and current understanding (mechanistic framing)
Across taxa, acidotolerance can be decomposed into several mechanism classes:
1. **Proton-consuming metabolic cycles** (e.g., amino-acid decarboxylation and associated antiport) that directly consume intracellular H+ and export products to sustain flux. (li2024responseofescherichia pages 2-4, li2024responseofescherichia pages 4-5)
2. **Bioenergetic and transport solutions** including ATPase reversal/ATP-driven proton extrusion, respiratory-chain modulation, and cation/H+ antiporters to stabilize cytoplasmic pH. (li2024responseofescherichia pages 2-4, krulwich2011molecularaspectsof pages 6-8)
3. **Envelope/membrane remodeling** to limit proton influx and maintain membrane integrity at low pH (fatty-acid composition shifts, cyclopropane fatty acids, porin tuning). (li2024responseofescherichia pages 5-7, krulwich2011molecularaspectsof pages 6-8)
4. **Proteostasis and damage control**: acid-activated chaperones (e.g., periplasmic HdeA/HdeB in Gram-negatives) and DNA repair, plus oxidative-stress defenses that become important because acid stress can increase damage and disrupt metabolism. (li2024responseofescherichia pages 5-7, qin2024characterizationofmild pages 1-2)

### Recent developments and latest research (prioritizing 2023–2024)
#### 1) Engineering acidotolerance modules in *E. coli* (2024)
A 2024 study characterized a **synthetic “acid-tolerance module”** in an engineered *E. coli* strain comprising a proton-consuming acid resistance regulator **gadE**, periplasmic chaperone **hdeB**, and ROS scavengers **sodB** and **katE**, and used transcriptomics to connect mild-acid growth with energy and transport remodeling. (qin2024characterizationofmild pages 1-2)

#### 2) Multi-omics models of acid-stress response in an acid-adapted juice spoilage bacterium (2023)
In *Alicyclobacillus acidoterrestris* DSM 3922T, integrative transcriptomics+metabolomics under acid stress (pH 3.0, 1 h) supported a model centered on **pHi homeostasis** via enhanced **amino-acid decarboxylation**, **urea hydrolysis**, and **energy supply**, with additional roles for **two-component systems**, **ABC transporters**, and **unsaturated fatty-acid synthesis**. (xu2023transcriptomicandmetabolomic pages 1-2)

#### 3) Community/biofilm-level modulation of pH stress by polyamines (2024)
In activated-sludge biofilms, **exogenous putrescine** acted as a “switch-like” regulator across defined pH regimes (acid pH 3–4; pI pH 5–6; alkali pH 8–9). Under acidic conditions, putrescine protonation/uptake was linked to **intracellular H+ decreases** and stimulation of **glutamate–GABA acid resistance** and bioenergetics. (jiang2024exogenousputrescineplays pages 6-9, jiang2024exogenousputrescineplays pages 9-12)

#### 4) Cross-protection strategies in probiotic/food LAB (2024)
In *Limosilactobacillus reuteri*, transcriptomics and overexpression experiments implicated stress-response proteins (including GatD/OsmC/CsbD in the text) in **improved survival under artificial gastric juice (pH 2.5)**, bile salts, and freeze-drying; survival phenotypes are shown in the paper’s Figure 5. (liu2024expressionofstress pages 4-6, liu2024expressionofstress media e571b46d)

### Current applications and real-world implementations
- **Industrial fermentation robustness:** Acid accumulation during fermentation can push pH below 5.0; engineering acid-tolerant chassis strains (e.g., *E. coli*) is used to improve growth and productivity under acidic process conditions. (li2024responseofescherichia pages 7-9, qin2024characterizationofmild pages 1-2)
- **Food fermentation and probiotic viability:** Acid/bile tolerance is essential for strains that must survive acidic foods and gastric transit; overexpression/cross-protection strategies in LAB target these properties and can also improve survival through processing stressors (e.g., freeze-drying). (liu2024expressionofstress pages 4-6, liu2024expressionofstress media e571b46d)
- **Environmental/engineering biofilms:** Manipulating polyamines (putrescine) provides a potential control lever to promote biofilm formation under acidic conditions or restrain it under alkaline conditions, relevant to wastewater and engineered biofilm systems. (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12)

### Relevant statistics and quantitative assay data (recent studies)
- **Growth inhibition by low pH (A. acidoterrestris, 2023):** maximum growth rate (mmax) decreased from **0.209 at pH 4.0** to **0.068 at pH 3.0** and **0.050 at pH 2.5**; **pH 2.0 fully inhibited growth** (no biomass increase within 20 h). (xu2023transcriptomicandmetabolomic pages 2-5)
- **Engineered mild-acid growth advantage (*E. coli*, 2024):** final OD600 at pH 6.0 for engineered strain SC3124 was **131% of MG1655 at pH 6.8** and **124% of MG1655 at pH 6.0**. (qin2024characterizationofmild pages 1-2)
- **Putrescine and intracellular acid burden in biofilms (2024):** intracellular H+ decreased by **~74% (acid), 68% (pI), 32% (alkali)** with putrescine; ATP and ADP increased by **58% and 26%** under acidic conditions in the presence of putrescine (used as a proxy for oxidative phosphorylation activity). (jiang2024exogenousputrescineplays pages 6-9, jiang2024exogenousputrescineplays pages 9-12)
- **LAB survival under strong acid (2024):** *L. reuteri* survival under **artificial gastric juice pH 2.5** is reported and plotted for gene-overexpression strains in Figure 5 (A–C). (liu2024expressionofstress pages 3-4, liu2024expressionofstress media e571b46d)

### Candidate causal-graph nodes (grouped by type)

#### A) Environmental / experimental factors
- **Low external pH / acidic environment** (candidate: ENVO “acidic environment”; label-only if exact ENVO term not selected) (krulwich2011molecularaspectsof pages 3-5)
- **Artificial gastric juice (pH 2.5)** as assay condition (liu2024expressionofstress media e571b46d)
- **Organic acids / fermentation acidification leading to pH <5.0** (process context) (li2024responseofescherichia pages 7-9)
- **Bile salts** (co-stressor commonly coupled with acid challenge in probiotic viability assays) (liu2024expressionofstress pages 3-4)

#### B) Pathways / modules
- **Glutamate-dependent acid resistance (Gad system; AR2)**: GadA/GadB + GadC antiporter; augmented by glutaminase YbaS. (li2024responseofescherichia pages 2-4)
- **Arginine-dependent decarboxylase system (AdiA/AdiC; AR3)** (li2024responseofescherichia pages 4-5)
- **Lysine-dependent decarboxylase system (CadA/CadB; AR4)** (li2024responseofescherichia pages 4-5)
- **Ornithine-dependent system (SpeF/PotE; AR5)** (li2024responseofescherichia pages 4-5)
- **Urea hydrolysis / urease-linked buffering** (inferred in *A. acidoterrestris* acid stress model) (xu2023transcriptomicandmetabolomic pages 1-2)
- **Oxidative phosphorylation / energy supply remodeling under acid stress** (association/role in mild-acid tolerance and putrescine effects) (qin2024characterizationofmild pages 1-2, jiang2024exogenousputrescineplays pages 9-12)

#### C) Genes / proteins / complexes
- **F0F1-ATPase** (F-type ATPase complex; reverses to hydrolyze ATP and consume intracellular H+) (li2024responseofescherichia pages 2-4)
- **GadA/GadB (glutamate decarboxylases), GadC (GABA/glutamate antiporter), GadE regulator, YbaS** (li2024responseofescherichia pages 2-4)
- **AdiA/AdiC; CadA/CadB; SpeF/PotE** (li2024responseofescherichia pages 4-5)
- **HdeA/HdeB periplasmic chaperones** (active at defined pH ranges) (li2024responseofescherichia pages 5-7)
- **SodB, KatE (ROS defenses)** as acid tolerance module components in engineered *E. coli* (qin2024characterizationofmild pages 1-2)
- **OsmC, CsbD, GatD** as stress proteins implicated in LAB cross-protection (note: verify gene naming consistency before final node grounding) (liu2024expressionofstress pages 4-6, liu2024expressionofstress pages 6-7)

#### D) Chemicals/metabolites
- **H+** (proton burden)
- **L-glutamate / glutamine**; **GABA**; **CO2**; **NH3/NH4+** (acid-neutralizing/consuming cycle components) (li2024responseofescherichia pages 2-4, jiang2024exogenousputrescineplays pages 6-9)
- **Putrescine** (polyamine modulating acid stress adaptability in biofilms) (jiang2024exogenousputrescineplays pages 6-9)
- **Urea** (substrate for buffering via urea hydrolysis) (xu2023transcriptomicandmetabolomic pages 1-2)

#### E) Cellular processes / phenotypes
- **Intracellular pH homeostasis / cytoplasmic buffering capacity** (krulwich2011molecularaspectsof pages 14-15, krulwich2011molecularaspectsof pages 1-3)
- **Membrane integrity / proton permeability control** (krulwich2011molecularaspectsof pages 6-8, li2024responseofescherichia pages 5-7)
- **Protein folding / anti-aggregation under acid** (HdeA/HdeB) (li2024responseofescherichia pages 5-7)

### Candidate causal edges (evidence-backed)
The following edge list is presented in a curation-ready table with direct snippets, DOI links, and uncertainty notes:

| Edge (subject–predicate–object) | Node type(s) | Evidence & mechanism summary | Source (DOI, year, URL) | Direct quote/snippet | Notes/uncertainty |
|---|---|---|---|---|---|
| low external pH → increases need for → cytoplasmic pH homeostasis | environmental factor → biological process | Acidotolerance is best framed as the capacity of mostly neutralophilic microbes to survive/grow under acidic external pH by maintaining intracellular pH near the physiological range rather than being obligate acidophiles. Neutralophiles generally grow over ~pH 5.5–9.0, while extreme acidophiles grow below pH 3. | 10.1038/nrmicro2549 (2011), https://doi.org/10.1038/nrmicro2549 | “neutralophiles (grow at external pH ~5.5–9.0 while keeping cytoplasmic pH ~7.5–7.7)”; “Extremely acidophilic bacteria grow at external pH < 3” (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 14-15) | Scope edge; useful to distinguish acidotolerant from acidophilic. Not a gene-level mechanism. |
| acidotolerant phenotype → distinct from → acidophilic lifestyle | trait → trait | Acidotolerance should not be conflated with acidophily: acidophiles have constitutive adaptations for growth at very low pH, whereas acidotolerant neutralophiles maintain near-neutral cytoplasm and survive/grow under acid stress. | 10.1038/nrmicro2549 (2011), https://doi.org/10.1038/nrmicro2549 | “bacteria use diverse mechanisms to tolerate or grow at external pH outside their cytoplasmic range”; “Extremely acidophilic ... grow, respectively, at pH 1–3” (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5) | Boundary/ontology note rather than mechanistic edge. Recommended as annotation note, not necessarily TraitMech edge. |
| F0F1-ATPase activity → consumes → intracellular H+ | protein complex → chemical | In E. coli AR1, F0F1-ATPase can reverse to hydrolyze ATP and remove intracellular proton burden, directly supporting pH homeostasis under acid stress. | 10.3390/microorganisms12091774 (2024), https://doi.org/10.3390/microorganisms12091774 | “under acid stress it ‘rapidly shifts its mechanism to consume intracellular H+ by hydrolyzing ATP to maintain intracellular homeostasis’” (li2024responseofescherichia pages 2-4) | Strong mechanistic edge; mostly evidenced in E. coli/enterics. Grounding candidate: GO:F-type ATPase complex. |
| glutamate decarboxylase system (GadA/GadB/GadC) → maintains → intracellular pH homeostasis | pathway/module → biological process | AR2 is a canonical proton-consuming system: GadA/B decarboxylate glutamate to GABA + CO2 while consuming H+, and GadC exchanges GABA for extracellular glutamate, sustaining the cycle. | 10.3390/microorganisms12091774 (2024), https://doi.org/10.3390/microorganisms12091774 | “GadA/B decarboxylate glutamate to GABA + CO2 while consuming intracellular H+, and GadC exports GABA in exchange for extracellular glutamate” (li2024responseofescherichia pages 2-4) | Strong, broadly reusable edge for many bacteria/LAB; taxon-general but not universal. |
| gadA/gadB/gadC deletion → decreases → survival at pH 2–3 | genes → phenotype | Review summarizes loss-of-function evidence: deleting gadA/gadB/gadC impairs survival under extreme acid, showing causal necessity of the Gad system. | 10.3390/microorganisms12091774 (2024), https://doi.org/10.3390/microorganisms12091774 | “Deletion of gadA/gadB/gadC impairs survival at pH 2–3; one decarboxylase suffices for survival at pH 2.5, while survival at pH 2 requires both” (li2024responseofescherichia pages 2-4) | Strong but E. coli-centric; good for mechanistic support notes. |
| glutaminase YbaS → produces → ammonia | enzyme → chemical | YbaS hydrolyzes glutamine below pH 6.0, generating NH3 that neutralizes protons and augments Gad-based acid defense. | 10.3390/microorganisms12091774 (2024), https://doi.org/10.3390/microorganisms12091774 | “The Gad system is also augmented by glutaminase YbaS under ambient pH <6.0, producing ammonia to neutralize protons” (li2024responseofescherichia pages 2-4) | Strong in E. coli; candidate edge may be more specific than trait core. |
| arginine decarboxylase system (AdiA/AdiC) → consumes → intracellular H+ | pathway/module → chemical | AR3 decarboxylates arginine and exchanges products through AdiC, supporting survival at very low pH. | 10.3390/microorganisms12091774 (2024), https://doi.org/10.3390/microorganisms12091774 | “The arginine-dependent Adi (AR3) system (AdiA/AdiC) decarboxylates arginine to consume intracellular H+ and functions effectively down to pH 2.5” (li2024responseofescherichia pages 4-5) | Strong but primarily enteric-bacteria evidence. |
| lysine decarboxylase system (CadA/CadB) → consumes → intracellular H+ | pathway/module → chemical | AR4 consumes protons via lysine decarboxylation; CadB exchanges products/substrates to support pH control around moderately acidic pH. | 10.3390/microorganisms12091774 (2024), https://doi.org/10.3390/microorganisms12091774 | “The lysine-dependent Cad (AR4) system (CadA/CadB) decarboxylates lysine to consume H+ and normally functions around pH 5.8” (li2024responseofescherichia pages 4-5) | Good candidate edge; narrower pH range than Gad/Adi. |
| ornithine decarboxylase system (SpeF/PotE) → contributes to → acid resistance | pathway/module → phenotype | AR5 consumes H+ anaerobically around pH 5.0 through ornithine decarboxylation/export cycles. | 10.3390/microorganisms12091774 (2024), https://doi.org/10.3390/microorganisms12091774 | “The ornithine system (AR5; SpeF/PotE) is active anaerobically around pH 5.0 and consumes H+ via decarboxylation” (li2024responseofescherichia pages 4-5) | Weaker as a general trait edge because condition-specific (anaerobic). Mark uncertain/generalizability-limited. |
| periplasmic chaperone HdeA → prevents → protein aggregation at low pH | protein → biological process | HdeA is acid-activated and protects periplasmic proteins from aggregation under severe acid. | 10.3390/microorganisms12091774 (2024), https://doi.org/10.3390/microorganisms12091774 | “HdeA: pH 1–3 ... convert[s] from inactive dimers to monomers in severe acid to prevent aggregation without ATP” (li2024responseofescherichia pages 5-7) | Strong, but mostly Gram-negative/periplasmic context. |
| periplasmic chaperone HdeB → prevents → protein aggregation at moderately low pH | protein → biological process | HdeB complements HdeA at somewhat higher acidic pH, broadening periplasmic proteostasis under acid stress. | 10.3390/microorganisms12091774 (2024), https://doi.org/10.3390/microorganisms12091774 | “HdeB: pH 3–5” and acts to “prevent aggregation without ATP” (li2024responseofescherichia pages 5-7) | Strong, but taxon/cell-envelope specific. |
| cyclopropane fatty acid synthetase activity → increases → membrane acid resistance | enzyme/process → phenotype | Conversion of unsaturated fatty acids into cyclopropane fatty acids is linked to reduced proton permeability and improved membrane robustness in acid. | 10.3390/microorganisms12091774 (2024), https://doi.org/10.3390/microorganisms12091774 | “membrane lipids can enhance acid resistance by altering saturated/unsaturated ratios or converting unsaturated fatty acids to cyclopropane fatty acids via cyclopropane fatty acid synthetase” (li2024responseofescherichia pages 5-7) | Good generic membrane-mechanism edge. Specific enzyme grounding may vary by taxon. |
| altered membrane lipid composition → reduces → inward proton leakage | cellular component/process → process | Krulwich review generalizes passive pH-homeostasis mechanisms: membrane lipid/porin changes can limit proton entry in acidic environments. | 10.1038/nrmicro2549 (2011), https://doi.org/10.1038/nrmicro2549 | “changes in membrane lipids and porins to minimize inward proton leakage” (krulwich2011molecularaspectsof pages 6-8) | Broad, cross-taxon homeostasis edge; mechanism may remain label-level if specific lipid chemistry unclear. |
| cation/H+ antiporters → contribute to → cytoplasmic pH control | transporter family → biological process | Core pH-homeostasis mechanism across bacteria: Na+/H+ and K+/H+ antiporters exchange cations and protons to stabilize intracellular pH. | 10.1038/nrmicro2549 (2011), https://doi.org/10.1038/nrmicro2549 | “Na+/H+ and K+/H+ antiporters ... support cytoplasmic pH control” (krulwich2011molecularaspectsof pages 6-8) | Useful generic node/edge for acidotolerance graphs; not acid-specific only. |
| amino acid decarboxylation → maintains → pHi homeostasis in Alicyclobacillus acidoterrestris | pathway/module → biological process | Multi-omics study in an acidophile found enhanced amino-acid decarboxylation under acid stress, coupled to pHi measurements and growth inhibition metrics. | 10.1128/spectrum.00022-23 (2023), https://doi.org/10.1128/spectrum.00022-23 | “maintains intracellular pH (pHi) homeostasis by enhancing amino acids decarboxylation, urea hydrolysis, and energy supply” (xu2023transcriptomicandmetabolomic pages 1-2) | Strong but from acidophile A. acidoterrestris; may represent both acidophile and acidotolerance stress logic. |
| urea hydrolysis/urease activity → contributes to → pHi homeostasis under acid stress | pathway/enzyme → biological process | Xu et al. infer urease/urea-hydrolysis support for acid-stress response in A. acidoterrestris, likely via ammonia generation and buffering. | 10.1128/spectrum.00022-23 (2023), https://doi.org/10.1128/spectrum.00022-23 | “maintains intracellular pH (pHi) homeostasis by enhancing amino acids decarboxylation, urea hydrolysis, and energy supply” (xu2023transcriptomicandmetabolomic pages 1-2) | Strong in this taxon; curatable as a candidate but mark taxon-specific until broader support added. |
| ABC transporters → contribute to → acid stress resistance | transporter family → phenotype | A. acidoterrestris omics implicated ABC transporters in resisting acid stress; engineered E. coli mild-acid data also associated ABC transporters with tolerance modules. | 10.1128/spectrum.00022-23 (2023), https://doi.org/10.1128/spectrum.00022-23; 10.3390/microorganisms12081565 (2024), https://doi.org/10.3390/microorganisms12081565 | “ABC transporters ... play crucial roles in resisting acid stress”; “ABC transporters ... were highly positively associated with mild acid stress responses” (xu2023transcriptomicandmetabolomic pages 1-2, qin2024characterizationofmild pages 1-2) | Moderate-strength edge because transporter identities are broad/unspecified. |
| unsaturated fatty acid synthesis → contributes to → acid stress resistance | lipid metabolic process → phenotype | A. acidoterrestris upregulated unsaturated fatty acid synthesis under acid stress, consistent with membrane remodeling as an acid adaptation mechanism. | 10.1128/spectrum.00022-23 (2023), https://doi.org/10.1128/spectrum.00022-23 | “unsaturated fatty acid synthesis also play[s] crucial roles in resisting acid stress” (xu2023transcriptomicandmetabolomic pages 1-2) | Good membrane-adaptation edge; taxon support from acidophile study. |
| two-component systems → regulate response to → acid stress | signaling pathway → environmental factor | A. acidoterrestris multi-omics implicated TCS in acid-stress response coordination. | 10.1128/spectrum.00022-23 (2023), https://doi.org/10.1128/spectrum.00022-23 | “two-component systems ... play crucial roles in resisting acid stress” (xu2023transcriptomicandmetabolomic pages 1-2) | Regulatory edge is plausible and useful, but precise TCS nodes were not specified in excerpt. |
| decreasing external pH → decreases → growth rate of A. acidoterrestris | environmental factor → phenotype | Quantitative assay context: maximum growth rate dropped from 0.209 at pH 4.0 to 0.068 at pH 3.0 and 0.050 at pH 2.5; pH 2.0 fully inhibited growth. | 10.1128/spectrum.00022-23 (2023), https://doi.org/10.1128/spectrum.00022-23 | “mmax at pH 4.0 = 0.209, pH 3.0 = 0.068, pH 2.5 = 0.050 ... pH 2.0 fully inhibited growth” (xu2023transcriptomicandmetabolomic pages 2-5) | Assay/phenotype edge; important for trait boundary and evidence context, not mechanism node. |
| synthetic module gadE + hdeB + sodB + katE overexpression → increases → mild-acid growth robustness | gene set/module → phenotype | Engineered E. coli with proton-consuming regulator, periplasmic chaperone, and ROS scavengers showed improved growth at pH 6.0. | 10.3390/microorganisms12081565 (2024), https://doi.org/10.3390/microorganisms12081565 | “synthetic acid-tolerance module genes consisting of ... gadE, ... hdeB, and ROS scavengers (sodB, katE)”; final “OD600 at pH 6.0 was 131% ... and 124%...” (qin2024characterizationofmild pages 1-2) | Strong engineering evidence; composite edge may be better kept as module-level rather than single-gene causal certainty. |
| oxidative phosphorylation upregulation → associates with → mild acid tolerance | pathway → phenotype | Transcriptomics of engineered acid-tolerant E. coli identified oxidative phosphorylation as a major positively associated response to pH 6.0. | 10.3390/microorganisms12081565 (2024), https://doi.org/10.3390/microorganisms12081565 | “genes involved in oxidative phosphorylation ... were highly positively associated with mild acid stress responses” (qin2024characterizationofmild pages 1-2) | Association stronger than direct causation; curate with uncertainty. |
| protonated putrescine → enhances → glutamate-based acid resistance/GABA pathway | chemical → pathway | In mixed biofilms, low-pH protonation of putrescine promoted uptake and stimulated glutamate/GABA acid-resistance metabolism, lowering intracellular H+. | 10.1128/aem.00569-24 (2024), https://doi.org/10.1128/aem.00569-24 | “Inside cells, putrescine promotes intracellular H+ consumption by enhancing the glutamate-based acid resistance strategy and the γ-aminobutyric acid (GABA) metabolic pathway” (jiang2024exogenousputrescineplays pages 1-2) | Strong in mixed-community biofilm; environmental/consortium-specific. |
| exogenous putrescine → decreases → intracellular H+ | chemical → chemical/process | Jiang et al. reported intracellular H+ decreases of 74%, 68%, and 32% in acid, pI, and alkaline regimes, respectively, with linked increases in GABA and glutamate use. | 10.1128/aem.00569-24 (2024), https://doi.org/10.1128/aem.00569-24 | “putrescine reduced intracellular H+ (reported decreases of 74%, 68%, and 32% in acid, pI, and alkali, respectively)” (jiang2024exogenousputrescineplays pages 6-9) | Quantitative and useful, but from activated-sludge biofilm rather than isolate-level microbe. |
| exogenous putrescine → increases → ATPase expression/oxidative phosphorylation under acidic conditions | chemical → pathway/process | Putrescine stimulated ATPase-linked proton transport and increased ATP/ADP under acid, indicating bioenergetic support for acid adaptation. | 10.1128/aem.00569-24 (2024), https://doi.org/10.1128/aem.00569-24 | “Putrescine also stimulates ATPase expression ... and enhancing oxidative phosphorylation”; “ATP and ADP concentrations are significantly increased by 58% and 26%” (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12) | Moderate-strength due to community context; ATPase identity unspecified. |
| GatD overexpression → increases → survival under acid stress (pH 2.5 gastric juice) | gene/protein → phenotype | In L. reuteri Z204, overexpression of GatD improved survival in artificial gastric juice and under bile/freeze-drying, supporting a causal acid-stress role for glutamate-related metabolism. | 10.3389/fmicb.2024.1437803 (2024), https://doi.org/10.3389/fmicb.2024.1437803 | “overexpression of three stress-response proteins — glutamate decarboxylase GatD ... significantly increased the survival rate ... under acid/bile salts stress”; Fig. 5A used “artificial gastric juice (pH 2.5)” (liu2024expressionofstress pages 1-2, liu2024expressionofstress media e571b46d) | Strong phenotype edge; protein naming in excerpts is slightly inconsistent across pages, so verify exact annotation before curation. |
| OsmC overexpression → increases → survival under acid stress | gene/protein → phenotype | OsmC, an oxidative stress/peroxide-related protein, improved acid/bile/freeze-drying survival when overexpressed in L. reuteri. | 10.3389/fmicb.2024.1437803 (2024), https://doi.org/10.3389/fmicb.2024.1437803 | “overexpression of the OsmC, CsbD, and GatD proteins also enhanced the survival of L. reuteri after freeze-drying” and “significantly increased the survival rate ... under acid/bile salts stress” (liu2024expressionofstress pages 1-2, liu2024expressionofstress pages 6-7) | Strong phenotype edge; mechanism for acid specifically may be partly indirect via oxidative-stress defense. |
| CsbD overexpression → increases → survival under acid stress | gene/protein → phenotype | CsbD overexpression improved acid, bile, and freeze-drying tolerance in L. reuteri, potentially via membrane/global stress regulation. | 10.3389/fmicb.2024.1437803 (2024), https://doi.org/10.3389/fmicb.2024.1437803 | “strains overexpressing CsbD ... showed significantly enhanced resistance to acid”; Fig. 5A compares survival after treatment in artificial gastric juice (pH 2.5) (liu2024expressionofstress pages 4-6, liu2024expressionofstress media e571b46d) | Strong phenotype edge; precise biochemical mechanism remains less defined than Gad/Hde systems. |


*Table: This table lists evidence-backed candidate subject–predicate–object edges for curating microbial acidotolerance into TraitMech. It prioritizes mechanistic links, quantitative assay context, and flags where claims are taxon-specific, community-level, or more associative than directly causal.*

### Visual evidence (figure)
Figure 5 (A–C) from Liu et al. (2024) provides plotted survival outcomes for *L. reuteri* overexpression strains under **artificial gastric juice pH 2.5**, bile salts, and freeze-drying, supporting edges that link specific stress-response genes to improved acid survival phenotypes. (liu2024expressionofstress media e571b46d)

### Expert synthesis / analysis (authoritative sources)
A convergent view from authoritative reviews and 2023–2024 primary work is that acidotolerance is not a single pathway but a **systems property** combining proton economy (consumption/export), envelope physics (proton leakage limitation), and stress response networks (proteostasis, transport and energy metabolism). This is consistent with (i) a high-level pH-homeostasis framing across bacteria, and (ii) specific, experimentally dissected acid-resistance modules (e.g., Gad system, F0F1-ATPase reversal, chaperones) in model organisms that can be abstracted into a TraitMech causal graph. (krulwich2011molecularaspectsof pages 1-3, li2024responseofescherichia pages 2-4, li2024responseofescherichia pages 5-7)

### Warnings / claims not yet ready for curation
- **Community-level biofilm results** (activated sludge) may not transfer to single-species trait mechanisms without additional isolate-level evidence; treat putrescine-related edges as context-specific unless validated in defined taxa. (jiang2024exogenousputrescineplays pages 6-9, jiang2024exogenousputrescineplays pages 9-12)
- **Broad categories (e.g., “ABC transporters”, “two-component systems”)** are often too nonspecific to curate as stable mechanistic nodes without identifying specific transporters/sensors. Keep as label-only candidates unless primary sources specify identities and causal evidence. (xu2023transcriptomicandmetabolomic pages 1-2)
- **Gene naming inconsistencies** in the *L. reuteri* excerpts (e.g., gatD vs cobQ mention in methods excerpt) should be resolved by checking the full text and gene annotations prior to ontology grounding. (liu2024expressionofstress pages 2-3, liu2024expressionofstress pages 4-6)

---

## DOI-first bibliography (with dates and URLs)
1. **Krulwich TA, Sachs G, Padan E.** Molecular aspects of bacterial pH sensing and homeostasis. *Nature Reviews Microbiology*. **2011-05**. DOI: **10.1038/nrmicro2549**. URL: https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 5-6)
2. **Xu J, Zhao N, Meng X, et al.** Transcriptomic and metabolomic profiling uncovers response mechanisms of *Alicyclobacillus acidoterrestris* DSM 3922T to acid stress. *Microbiology Spectrum*. **2023-08**. DOI: **10.1128/spectrum.00022-23**. URL: https://doi.org/10.1128/spectrum.00022-23 (xu2023transcriptomicandmetabolomic pages 2-5, xu2023transcriptomicandmetabolomic pages 1-2, xu2023transcriptomicandmetabolomic pages 10-11)
3. **Jiang G, Wang C, Wang Y, et al.** Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge. *Applied and Environmental Microbiology*. **2024-07**. DOI: **10.1128/aem.00569-24**. URL: https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 6-9, jiang2024exogenousputrescineplays pages 9-12)
4. **Qin J, Guo H, Wu X, et al.** Characterization of mild acid stress response in an engineered acid-tolerant *Escherichia coli* strain. *Microorganisms*. **2024-07**. DOI: **10.3390/microorganisms12081565**. URL: https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2)
5. **Li Z, Huang Z, Gu P.** Response of *Escherichia coli* to Acid Stress: Mechanisms and Applications—A Narrative Review. *Microorganisms*. **2024-08**. DOI: **10.3390/microorganisms12091774**. URL: https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4, li2024responseofescherichia pages 4-5, li2024responseofescherichia pages 5-7)
6. **Liu Z, Zhao X, Bangash HI.** Expression of stress responsive genes enables *Limosilactobacillus reuteri* to cross-protection against acid, bile salt, and freeze-drying. *Frontiers in Microbiology*. **2024-09**. DOI: **10.3389/fmicb.2024.1437803**. URL: https://doi.org/10.3389/fmicb.2024.1437803 (liu2024expressionofstress pages 4-6, liu2024expressionofstress media e571b46d, liu2024expressionofstress pages 3-4)



References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 6-8): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

3. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 14-15): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

5. (li2024responseofescherichia pages 2-4): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

6. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

7. (li2024responseofescherichia pages 4-5): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

8. (li2024responseofescherichia pages 5-7): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

9. (qin2024characterizationofmild pages 1-2): Jingliang Qin, Han Guo, Xiaoxue Wu, Shuai Ma, Xin Zhang, Xiaofeng Yang, Bin Liu, Lu Feng, Huanhuan Liu, and Di Huang. Characterization of mild acid stress response in an engineered acid-tolerant escherichia coli strain. Microorganisms, 12:1565, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081565, doi:10.3390/microorganisms12081565. This article has 2 citations.

10. (xu2023transcriptomicandmetabolomic pages 1-2): Junnan Xu, Ning Zhao, Xuemei Meng, Jun Li, Tong Zhang, Ruoyun Xu, Xinyuan Wei, and Mingtao Fan. Transcriptomic and metabolomic profiling uncovers response mechanisms of alicyclobacillus acidoterrestris dsm 3922 <sup>t</sup> to acid stress. Microbiology Spectrum, Aug 2023. URL: https://doi.org/10.1128/spectrum.00022-23, doi:10.1128/spectrum.00022-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

11. (jiang2024exogenousputrescineplays pages 6-9): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

12. (jiang2024exogenousputrescineplays pages 9-12): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

13. (liu2024expressionofstress pages 4-6): Zhenzhen Liu, Xiao Zhao, and Hina Iqbal Bangash. Expression of stress responsive genes enables limosilactobacillus reuteri to cross-protection against acid, bile salt, and freeze-drying. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1437803, doi:10.3389/fmicb.2024.1437803. This article has 9 citations and is from a peer-reviewed journal.

14. (liu2024expressionofstress media e571b46d): Zhenzhen Liu, Xiao Zhao, and Hina Iqbal Bangash. Expression of stress responsive genes enables limosilactobacillus reuteri to cross-protection against acid, bile salt, and freeze-drying. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1437803, doi:10.3389/fmicb.2024.1437803. This article has 9 citations and is from a peer-reviewed journal.

15. (li2024responseofescherichia pages 7-9): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

16. (jiang2024exogenousputrescineplays pages 1-2): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

17. (xu2023transcriptomicandmetabolomic pages 2-5): Junnan Xu, Ning Zhao, Xuemei Meng, Jun Li, Tong Zhang, Ruoyun Xu, Xinyuan Wei, and Mingtao Fan. Transcriptomic and metabolomic profiling uncovers response mechanisms of alicyclobacillus acidoterrestris dsm 3922 <sup>t</sup> to acid stress. Microbiology Spectrum, Aug 2023. URL: https://doi.org/10.1128/spectrum.00022-23, doi:10.1128/spectrum.00022-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

18. (liu2024expressionofstress pages 3-4): Zhenzhen Liu, Xiao Zhao, and Hina Iqbal Bangash. Expression of stress responsive genes enables limosilactobacillus reuteri to cross-protection against acid, bile salt, and freeze-drying. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1437803, doi:10.3389/fmicb.2024.1437803. This article has 9 citations and is from a peer-reviewed journal.

19. (liu2024expressionofstress pages 6-7): Zhenzhen Liu, Xiao Zhao, and Hina Iqbal Bangash. Expression of stress responsive genes enables limosilactobacillus reuteri to cross-protection against acid, bile salt, and freeze-drying. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1437803, doi:10.3389/fmicb.2024.1437803. This article has 9 citations and is from a peer-reviewed journal.

20. (liu2024expressionofstress pages 1-2): Zhenzhen Liu, Xiao Zhao, and Hina Iqbal Bangash. Expression of stress responsive genes enables limosilactobacillus reuteri to cross-protection against acid, bile salt, and freeze-drying. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1437803, doi:10.3389/fmicb.2024.1437803. This article has 9 citations and is from a peer-reviewed journal.

21. (liu2024expressionofstress pages 2-3): Zhenzhen Liu, Xiao Zhao, and Hina Iqbal Bangash. Expression of stress responsive genes enables limosilactobacillus reuteri to cross-protection against acid, bile salt, and freeze-drying. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1437803, doi:10.3389/fmicb.2024.1437803. This article has 9 citations and is from a peer-reviewed journal.

22. (xu2023transcriptomicandmetabolomic pages 10-11): Junnan Xu, Ning Zhao, Xuemei Meng, Jun Li, Tong Zhang, Ruoyun Xu, Xinyuan Wei, and Mingtao Fan. Transcriptomic and metabolomic profiling uncovers response mechanisms of alicyclobacillus acidoterrestris dsm 3922 <sup>t</sup> to acid stress. Microbiology Spectrum, Aug 2023. URL: https://doi.org/10.1128/spectrum.00022-23, doi:10.1128/spectrum.00022-23. This article has 14 citations and is from a domain leading peer-reviewed journal.