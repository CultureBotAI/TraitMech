---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:48:14.335869'
end_time: '2026-06-17T23:07:35.432460'
duration_seconds: 1161.1
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: moderately halophilic
  trait_identifier: METPO:1000623
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: moderately_halophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A halophily preference where growth and proliferation requires high
    levels of sodium chloride, usually above or about 0.2 M.
  parent_traits: METPO:1000629
  synonyms: moderate-halophilic
  evidence_summary: 'PMID:9758852: moderately halophilic bacterium Halomonas elongata
    (Organism example: Halomonas elongata is described as moderately halophilic.)'
  causal_graph_summary: 'moderate_halophile_compatible_solutes: 5 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** moderately halophilic
- **METPO identifier:** METPO:1000623
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference where growth and proliferation requires high levels of sodium chloride, usually above or about 0.2 M.
- **Parent traits:** METPO:1000629
- **Synonyms:** moderate-halophilic
- **Existing evidence:** PMID:9758852: moderately halophilic bacterium Halomonas elongata (Organism example: Halomonas elongata is described as moderately halophilic.)
- **Existing causal graph summary:** moderate_halophile_compatible_solutes: 5 nodes, 5 edges

## Research Objective

Research the microbial trait **moderately halophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/moderately_halophilic.yaml`.

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
- **Trait label:** moderately halophilic
- **METPO identifier:** METPO:1000623
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference where growth and proliferation requires high levels of sodium chloride, usually above or about 0.2 M.
- **Parent traits:** METPO:1000629
- **Synonyms:** moderate-halophilic
- **Existing evidence:** PMID:9758852: moderately halophilic bacterium Halomonas elongata (Organism example: Halomonas elongata is described as moderately halophilic.)
- **Existing causal graph summary:** moderate_halophile_compatible_solutes: 5 nodes, 5 edges

## Research Objective

Research the microbial trait **moderately halophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/moderately_halophilic.yaml`.

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


## Research report: Moderately halophilic (METPO:1000623) — TraitMech causal-graph evidence

### 0) Scope summary (trait definition, boundaries, and assay considerations)

**Trait meaning.** The microbial trait *moderately halophilic* describes organisms whose growth is favored by (and often requires) elevated salt, typically NaCl, with widely used operational definitions tying *optimal growth* to **~0.5–2.5 M total salt** (often expressed as ~3–15% NaCl). This category is commonly credited to Kushner’s classification as summarized in a highly cited MMBR review. (ventosa1998biologyofmoderately pages 2-3)

**Boundary with nearby traits.**
- **Halotolerant** organisms can grow without added salt, but tolerate relatively high salinity; “extremely halotolerant” is sometimes used when growth extends above ~2.5 M salt. (ventosa1998biologyofmoderately pages 2-3)
- **Borderline/extreme halophiles** may require ≥2 M salt and have optima above the moderate range (example given: *Actinopolyspora halophila* with optimal growth at ~3.4 M). (ventosa1998biologyofmoderately pages 2-3)

**Assay dependence.** Salt range can vary with temperature and medium composition; e.g., the *same organism* may grow at lower NaCl at cooler temperatures, so curated trait evidence should include assay conditions (temperature, medium) when possible. (ventosa1998biologyofmoderately pages 2-3)

**Representative moderately halophilic taxa used as mechanistic models in the curated evidence here.**
- *Halomonas elongata* (Gammaproteobacteria) — industrial ectoine producer, often used as a model for “salt-out/compatible-solute” strategies. (yu2024temporaldynamicsof pages 1-2, khanh2024metabolicpathwayengineering pages 2-6)
- *Halobacillus halophilus* (Firmicutes) — model for **chloride-dependent** osmoadaptation and osmolyte strategy switching. (saum2008regulationofosmoadaptation pages 1-2, saum2008regulationofosmoadaptation pages 2-3)


### 1) Key concepts and current mechanistic understanding

#### 1.1 Osmoregulation strategies relevant to moderate halophily
Two broad strategies are used by halophiles:
- **“Salt-in” strategy:** intracellular accumulation of inorganic ions (typically KCl) and concomitant evolution of an “acidic proteome” that functions in high ionic strength.
- **“Salt-out/compatible-solute” strategy:** maintain relatively low cytosolic salt and instead accumulate small organic osmolytes (“compatible solutes”).

For many moderate halophiles, the salt-out strategy is frequently emphasized; however, hybrid or scalable strategies can occur under fluctuating salinity. (ionescu2024extremefluctuationsin pages 2-4)

#### 1.2 Compatible solutes central to moderately halophilic physiology
Core compatible solutes repeatedly supported in the provided evidence include:
- **Ectoine** and **5-hydroxyectoine** (major in *Halomonas*; widely distributed). (ventosa1998biologyofmoderately pages 19-20, liu2021microbialproductionof pages 2-4)
- **Glycine betaine** (often imported rather than synthesized). (ventosa1998biologyofmoderately pages 19-20, lichty2024compatiblesolutesare pages 19-23)
- **Proline**, **glutamate**, **glutamine** (taxon- and condition-dependent). (ventosa1998biologyofmoderately pages 19-20, saum2008regulationofosmoadaptation pages 1-2, yu2024temporaldynamicsof pages 1-2)

Mechanistically, uptake is often favored when environmental osmoprotectants are available because it can be less energetically costly than de novo synthesis. (ventosa1998biologyofmoderately pages 19-20)

#### 1.3 Ion homeostasis as an early-phase response
In salt shock, early osmotic balance may involve rapid **Na+ and K+ uptake**, followed by a shift toward compatible solutes as longer-term osmoprotectants. This has direct experimental support from multi-omics salt shock analysis in *H. elongata*. (yu2024temporaldynamicsof pages 1-2)

#### 1.4 Oxidative stress coupling
A notable current insight from 2024 multi-omics work is that **NaCl shock can simultaneously induce oxidative stress** (not only osmotic stress) in a moderately halophilic bacterium, linking salt adaptation to antioxidant defenses and sulfur/cysteine metabolism regulation. (yu2024temporaldynamicsof pages 1-2)


### 2) Recent developments and latest research (prioritizing 2023–2024)

#### 2.1 Multi-omics time-resolved salt-shock physiology in *Halomonas elongata* (2024)
A 2024 study in *Microbial Cell Factories* quantified stress dynamics after NaCl shock and identified a two-stress model:
- **Osmotic stress (early):** within the tolerable range (reported 1–8% NaCl shock), cells rapidly take up **Na+ and K+** and increase **glutamate/glutamine** pools. (yu2024temporaldynamicsof pages 1-2)
- **Ectoine dominance (delayed):** ectoine increased only after ~**20 min** post-shock but then became the dominant osmoprotectant; the study reported **maximum ectoine productivity 1450 ± 99 mg/L/h** and a specific ectoine production rate **qp = 66.54 mg ectoine/g DCW/h** at 8% NaCl shock. (yu2024temporaldynamicsof pages 2-5, yu2024temporaldynamicsof pages 1-2)
- **Oxidative stress module:** cysB upregulation linked to sulfur metabolism and cysteine biosynthesis; a peroxidase gene (HELO_RS18165) and increased peroxidase/catalase activities were part of antioxidant defense. (yu2024temporaldynamicsof pages 1-2)
- **Energy crisis threshold:** exceeding tolerance (reported up to 1–13% NaCl shock) inhibited respiratory chain/ATP synthase and correlated with stalled growth and ectoine biosynthesis. (yu2024temporaldynamicsof pages 1-2)

These results are directly usable for trait-mechanism edges (NaCl shock → ions/amino acids → ectoine; NaCl shock → oxidative stress → antioxidant response). (yu2024temporaldynamicsof pages 1-2)

#### 2.2 Engineering alternative osmolyte strategies in an ectoine-centric moderate halophile (2024)
A 2024 paper in *Applied and Environmental Microbiology* used *H. elongata* as a chassis to demonstrate that changing osmolyte pathways can alter salt tolerance:
- The authors state *H. elongata* accumulates ectoine due to a **salt-inducible ectABC operon**, encoding EctB/EctA/EctC. (khanh2024metabolicpathwayengineering pages 2-6)
- Replacing ectABC with a salt-inducible proline biosynthesis cassette and deleting **putA** (proline catabolism) increased proline accumulation and improved high-salinity tolerance in engineered strains. (khanh2024metabolicpathwayengineering pages 2-6)
- A schematic of the ectoine/proline/putA network provides an interpretable mechanistic map for curation. (khanh2024metabolicpathwayengineering media 3e1e8c19)

This is highly informative mechanistically but should be curated as **engineered evidence** rather than a universal native mechanism. (khanh2024metabolicpathwayengineering pages 2-6)

#### 2.3 Ecosystem-scale view: fluctuating salinity selects for scalable/hybrid osmoregulation (2024)
A 2024 *Frontiers in Microbiomes* study on Dead Sea spring biofilms emphasizes that fluctuating salinity can select for microbes possessing gene repertoires spanning both salt-in and salt-out strategies, challenging overly rigid phylogeny-based assumptions. (ionescu2024extremefluctuationsin pages 2-4)

#### 2.4 Expert synthesis (2023 editorial)
A 2023 editorial in *Frontiers in Microbiology* highlights halophile adaptations spanning compatible solutes, salt-in adaptation, and macromolecular/membrane stabilization, and notes broad application domains (industry, agriculture, wastewater). (martinezespinosa2023editorialadaptationof pages 1-2)


### 3) Current applications and real-world implementations (with quantitative data)

#### 3.1 Industrial ectoine production (Halomonas-based processes)
A peer-reviewed 2021 review (still widely used for industrial benchmarks) describes *Halomonas elongata* “bacterial milking” ectoine production:
- **7.4 g/L ectoine** after repeated milking cycles at **2.57 M** salinity, **productivity 0.22 g/L/h** (reported for *H. elongata* DSM142). (liu2021microbialproductionof pages 2-4)

The same review summarizes multiple production hosts and titers, including engineered low-salt chassis (not trait-defining, but relevant for applications):
- *Corynebacterium glutamicum* engineered: **65 g/L ectoine** at ~0.03 M salinity (illustrates industrial push away from high-salt corrosion/wastewater constraints). (liu2021microbialproductionof pages 2-4)

#### 3.2 High-salt fermentation performance and process optimization via salt shock (2024)
The 2024 *H. elongata* NaCl-shock study reports process-relevant productivity metrics:
- Maximum ectoine productivity during the 4 h after shock up to **1450 ± 99 mg/L/h** (8% NaCl shock) and **1230 ± 112 mg/L/h** (5% shock). (yu2024temporaldynamicsof pages 2-5)

These are directly actionable for bioprocess control strategies (e.g., dynamic salinity shifting). (yu2024temporaldynamicsof pages 2-5)

#### 3.3 Engineering “super-leaky” ectoine producers to simplify downstream processing
A mechanistic production strategy described in the ectoine production review: deleting the ectoine uptake transporter **TeaABC** and disrupting the **Doe ectoine degradation pathway** yielded a *H. elongata* mutant that exports ectoine **without hypoosmotic shock** (“super-leaky”). (liu2021microbialproductionof pages 2-4)

#### 3.4 Enzyme discovery / lignocellulose and polysaccharide degradation under polyextreme conditions
The 2023 editorial notes functional metagenomics efforts recovering **378 glycoside hydrolase genes** (predominantly linked to *Halomonas*), with enzymes active at high salt plus other extremes (temperature/pH), relevant to biorefinery and biodegradation. (martinezespinosa2023editorialadaptationof pages 1-2)


### 4) Candidate nodes for the TraitMech causal graph (ontology grounding)

The following node inventory is intended for curation into `data/traits/environment/moderately_halophilic.yaml`.

| Node label | Node type | Suggested ontology grounding | Notes |
|---|---|---|---|
| moderately halophilic | phenotype | METPO:1000623 | Trait node; moderate halophily usually defined by optimal growth around 0.5–2.5 M salt, but assay conditions can shift observed range (ventosa1998biologyofmoderately pages 2-3, ventosa1998biologyofmoderately pages 3-4) |
| NaCl salinity | environmental factor | CHEBI:26710 | Core external driver of the trait; salinity changes trigger osmoadaptation and ectoine accumulation in Halomonas spp. (yu2024temporaldynamicsof pages 2-5, ventosa1998biologyofmoderately pages 2-3) |
| osmotic stress | environmental factor | GO:0006970 | Immediate stress imposed by high external salinity; central experimental factor in NaCl-shock studies (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5) |
| chloride | environmental factor | CHEBI:17996 | Particularly important in Halobacillus halophilus, where Cl− is required for growth and regulates osmoadaptation-related functions; likely taxon-specific for curation (saum2008regulationofosmoadaptation pages 1-2, saum2008regulationofosmoadaptation pages 2-3) |
| Na+ | environmental factor | CHEBI:29101 | Intracellular/extracellular sodium participates in early salt-shock balancing and ion homeostasis (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5) |
| K+ | environmental factor | CHEBI:29103 | Rapidly accumulated during salt shock as part of ion-based osmotic adjustment before/alongside compatible-solute accumulation (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5) |
| oxidative stress | process | GO:0006979 | NaCl shock in H. elongata induces oxidative stress in addition to osmotic stress (yu2024temporaldynamicsof pages 1-2) |
| ion homeostasis | process | GO:0050801 | Broad process covering Na+/K+ balancing under salt stress; useful higher-level node for multiple transporter edges (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5) |
| K+ uptake | process | GO:0098655 | Early osmoadaptive response in several halophiles; generic process node preferred over ungrounded taxon-specific transporter proteins unless directly evidenced (yu2024temporaldynamicsof pages 1-2, saum2008regulationofosmoadaptation pages 1-2) |
| Na+ uptake | process | GO:1902476 | H. elongata shows sodium uptake after NaCl shock; likely early-stage response rather than sole determinant of trait (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5) |
| compatible solute accumulation | process | GO:0015696 | Central moderate-halophile strategy; broad node linking salinity to osmoprotection (ventosa1998biologyofmoderately pages 19-20, saum2008regulationofosmoadaptation pages 1-2, ionescu2024extremefluctuationsin pages 2-4) |
| ectoine biosynthetic process | process | GO:1902235 | Strong candidate mechanism; salinity-inducible in Halomonas elongata and widely associated with moderate halophily (liu2021microbialproductionof pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) |
| hydroxyectoine biosynthetic process | process | unmapped | Process mediated by EctD; label-only if specific GO grounding is uncertain (liu2021microbialproductionof pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) |
| proline biosynthetic process | process | GO:0006561 | Compatible-solute pathway used naturally or by engineering in H. elongata; may be major or auxiliary depending on taxon (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) |
| glycine betaine biosynthetic process from choline | process | GO:0031423 | Common osmoprotectant pathway via BetA/BetB; widely distributed but not always native in every moderate halophile (lichty2024compatiblesolutesare pages 19-23) |
| ectoine degradation (Doe pathway) | process | unmapped | Supported in H. elongata genome-based pathway descriptions; likely important for net ectoine retention/export phenotypes (liu2021microbialproductionof pages 1-2, liu2021microbialproductionof pages 2-4) |
| sulfur metabolism | process | GO:0006790 | Upregulated through cysB in salt-shocked H. elongata as part of oxidative-stress defense (yu2024temporaldynamicsof pages 1-2) |
| cysteine biosynthetic process | process | GO:0019344 | Downstream of cysB-linked response in H. elongata under NaCl shock (yu2024temporaldynamicsof pages 1-2) |
| mechanosensitive channel activity | process | GO:0008381 | Relevant to ectoine/solute release during hypoosmotic shock and bacterial milking; not the dominant ectoine export route in H. elongata (liu2021microbialproductionof pages 1-2, liu2021microbialproductionof pages 2-4) |
| ectoine | metabolite | CHEBI:22396 | Major compatible solute in many moderate halophiles, especially Halomonas/Chromohalobacter; strong core node (ventosa1998biologyofmoderately pages 19-20, liu2021microbialproductionof pages 1-2) |
| 5-hydroxyectoine | metabolite | CHEBI:60135 | Hydroxylated ectoine derivative with osmoprotective role; often secondary to ectoine (lichty2024compatiblesolutesare pages 19-23, liu2021microbialproductionof pages 1-2) |
| glycine betaine | metabolite | CHEBI:17750 | Widely used osmoprotectant; often imported rather than synthesized de novo (ventosa1998biologyofmoderately pages 19-20, lichty2024compatiblesolutesare pages 19-23) |
| proline | metabolite | CHEBI:17203 | Compatible solute in some moderate halophiles and engineered H. elongata strains (khanh2024metabolicpathwayengineering pages 1-2, saum2008regulationofosmoadaptation pages 1-2) |
| glutamate | metabolite | CHEBI:29991 | Early osmolyte and precursor node linking primary metabolism to multiple osmoprotectants (yu2024temporaldynamicsof pages 1-2, ventosa1998biologyofmoderately pages 19-20, saum2008regulationofosmoadaptation pages 1-2) |
| glutamine | metabolite | CHEBI:28300 | Important osmolyte in H. halophilus and elevated during salt shock in H. elongata (yu2024temporaldynamicsof pages 1-2, saum2008regulationofosmoadaptation pages 1-2) |
| trehalose | metabolite | CHEBI:16551 | General compatible solute mentioned across osmoadaptation literature; weaker direct evidence for this specific trait set than ectoine/betaine/proline (lichty2024compatiblesolutesare pages 19-23, ionescu2024extremefluctuationsin pages 2-4) |
| GABA | metabolite | CHEBI:16865 | Engineered alternative osmolyte in ectoine-deficient H. elongata; valuable but should be flagged as engineered/taxon-specific (khanh2024metabolicpathwayengineering pages 1-2) |
| choline | metabolite | CHEBI:15354 | Precursor for glycine betaine biosynthesis (BetA/BetB pathway) (lichty2024compatiblesolutesare pages 19-23) |
| aspartate | metabolite | CHEBI:22660 | Precursor entering ectoine biosynthesis via Ask/Asd and ectABC route (liu2021microbialproductionof pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) |
| aspartate-semialdehyde | metabolite | CHEBI:15740 | Intermediate in ectoine biosynthesis from aspartate (liu2021microbialproductionof pages 1-2, qiao2024expressionofabc pages 2-5) |
| ectA (DABA acetyltransferase) | gene-protein | uniprotkb:unmapped | Core ectoine biosynthesis gene; strong mechanistic relevance in Halomonas and related taxa (liu2021microbialproductionof pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) |
| ectB (DABA transaminase) | gene-protein | uniprotkb:unmapped | Core ectoine biosynthesis gene (liu2021microbialproductionof pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) |
| ectC (ectoine synthase) | gene-protein | uniprotkb:unmapped | Core ectoine biosynthesis gene; often used as marker for ectoine-producing moderate halophiles (liu2021microbialproductionof pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) |
| ectD (ectoine hydroxylase) | gene-protein | uniprotkb:unmapped | Converts ectoine to hydroxyectoine (liu2021microbialproductionof pages 1-2, qiao2024expressionofabc pages 2-5) |
| ask (aspartokinase) | gene-protein | EC:2.7.2.4 | Upstream precursor-supplying enzyme for ectoine biosynthesis (liu2021microbialproductionof pages 1-2, qiao2024expressionofabc pages 2-5) |
| asd (aspartate-semialdehyde dehydrogenase) | gene-protein | EC:1.2.1.11 | Upstream precursor-supplying enzyme for ectoine biosynthesis (liu2021microbialproductionof pages 1-2, qiao2024expressionofabc pages 2-5) |
| betA (choline dehydrogenase) | gene-protein | EC:1.1.99.1 | Part of betaine-from-choline pathway; broadly relevant compatible-solute gene (lichty2024compatiblesolutesare pages 19-23) |
| betB (betaine aldehyde dehydrogenase) | gene-protein | EC:1.2.1.8 | Converts betaine aldehyde to glycine betaine (lichty2024compatiblesolutesare pages 19-23) |
| proB (gamma-glutamyl kinase) | gene-protein | EC:2.7.2.11 | First committed step in proline biosynthesis; feedback-sensitive control point in H. elongata engineering (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) |
| proA (glutamate-5-semialdehyde dehydrogenase) | gene-protein | EC:1.2.1.41 | Proline biosynthesis enzyme (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) |
| proC (pyrroline-5-carboxylate reductase) | gene-protein | EC:1.5.1.2 | Proline biosynthesis enzyme (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) |
| putA | gene-protein | uniprotkb:unmapped | Proline catabolic enzyme; deletion increases proline accumulation and salt tolerance in engineered H. elongata (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) |
| gadB / glutamate decarboxylase | gene-protein | EC:4.1.1.15 | Converts glutamate to GABA; evidence here is from metabolic engineering rather than native universal mechanism (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) |
| glnA2 (glutamine synthetase) | gene-protein | EC:6.3.1.2 | Chloride-dependent expression/activity in H. halophilus; likely taxon-specific regulation node (saum2008regulationofosmoadaptation pages 1-2) |
| cysB | gene-protein | uniprotkb:unmapped | Salt-shock-upregulated transcription factor positively linked to sulfur metabolism/cysteine biosynthesis in H. elongata (yu2024temporaldynamicsof pages 1-2) |
| HELO_RS18165 peroxidase | gene-protein | uniprotkb:unmapped | Specific H. elongata peroxidase locus upregulated after NaCl shock; taxon/locus-specific node (yu2024temporaldynamicsof pages 1-2) |
| catalase | gene-protein | EC:1.11.1.6 | Antioxidant defense enzyme activity increased after NaCl shock in H. elongata (yu2024temporaldynamicsof pages 1-2) |
| peroxidase | gene-protein | EC:1.11.1.7 | Antioxidant defense enzyme activity increased after NaCl shock in H. elongata (yu2024temporaldynamicsof pages 1-2) |
| DoeA (ectoine hydrolase) | gene-protein | uniprotkb:unmapped | Ectoine degradation enzyme in Doe pathway (liu2021microbialproductionof pages 1-2, liu2021microbialproductionof pages 2-4) |
| DoeB (N-alpha-acetyl-L-2,4-diaminobutyric acid deacetylase) | gene-protein | uniprotkb:unmapped | Ectoine degradation enzyme in Doe pathway (liu2021microbialproductionof pages 1-2, liu2021microbialproductionof pages 2-4) |
| DoeC (aspartate-semialdehyde dehydrogenase, catabolic) | gene-protein | uniprotkb:unmapped | Part of proposed ectoine degradation pathway; exact grounding may vary by annotation (liu2021microbialproductionof pages 2-4) |
| DoeD (diaminobutyrate transaminase, catabolic) | gene-protein | uniprotkb:unmapped | Part of proposed ectoine degradation pathway (liu2021microbialproductionof pages 2-4) |
| ProU ABC transporter | transporter | GO:0015419 | High-affinity compatible-solute importer family for glycine betaine/proline-type solutes; family-level node (lichty2024compatiblesolutesare pages 19-23) |
| BCCT transporter family | transporter | GO:0015658 | Family including BetT/BetP/OpuD-type transporters for osmoprotectant uptake; family-level node (lichty2024compatiblesolutesare pages 19-23) |
| TeaABC TRAP transporter | transporter | GO:0043190 | Ectoine/5-hydroxyectoine uptake system; deletion used to create super-leaky H. elongata ectoine exporter phenotype (lichty2024compatiblesolutesare pages 19-23, liu2021microbialproductionof pages 2-4) |
| mechanosensitive channels (MSC) | transporter | GO:0008381 | Contribute to compatible-solute release during hypoosmotic shock, but only minor contribution to ectoine excretion in H. elongata (liu2021microbialproductionof pages 1-2, liu2021microbialproductionof pages 2-4) |
| Na+/H+ antiporter | transporter | unmapped | Generic ion-homeostasis node supported conceptually in halophiles, but specific antiporter gene evidence for moderate halophiles in provided sources is weak; keep generic (lee2018naclsaturatedbrinesare pages 15-17) |
| Na+ and K+ uptake system | transporter | unmapped | Generic node for early ionic balancing after salt shock in H. elongata; precise molecular identity not established in cited sources (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5) |


*Table: This table lists curation-ready candidate nodes for a TraitMech causal graph of the microbial trait 'moderately halophilic'. It groups environmental drivers, processes, metabolites, genes/proteins, transporters, and phenotype-level nodes, with suggested ontology grounding and notes about taxon specificity or curation uncertainty.*


### 5) Evidence-backed candidate edges (subject–predicate–object triples)

The following candidate edges are curated with DOI-first references, supporting snippets, and uncertainty notes.

| Edge (S–P–O) | Evidence (paper; year; DOI; URL) | Supporting snippet (short quote) | Notes/uncertainty & suggested grounding |
|---|---|---|---|
| NaCl salinity / osmotic stress → induces → compatible solute accumulation | Ventosa et al.; 1998; 10.1128/MMBR.62.2.504-544.1998; https://doi.org/10.1128/mmbr.62.2.504-544.1998 | “Organic compatible solutes predominate: glycine betaine… ectoine and hydroxyectoine… amino acids (Glu, Gln, Asp), and proline in some Gram-positives” (ventosa1998biologyofmoderately pages 19-20) | Broad, well-supported trait-level edge for moderate halophiles. Grounding: NaCl CHEBI:26710; osmotic stress GO:0006970; compatible solute accumulation GO:0015696. |
| NaCl shock → induces → Na+ uptake | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “H. elongata urgently balanced the surging osmotic pressure by uptaking sodium and potassium ions” (yu2024temporaldynamicsof pages 1-2) | Strong but taxon-specific to H. elongata shock experiments. Grounding: sodium ion CHEBI:29101; sodium ion transport process candidate GO term, generic if uncertain. |
| NaCl shock → induces → K+ uptake | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “H. elongata urgently balanced the surging osmotic pressure by uptaking sodium and potassium ions” (yu2024temporaldynamicsof pages 1-2) | Strong H. elongata evidence; broadly consistent with halophile adaptation models. Grounding: potassium ion CHEBI:29103; potassium ion transport/uptake GO:0098655. |
| NaCl shock → increases → intracellular glutamate | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “augmenting intracellular amino acid pools, particularly glutamate and glutamine” (yu2024temporaldynamicsof pages 1-2) | Strong in H. elongata under salt shock. Grounding: glutamate CHEBI:29991. |
| NaCl shock → increases → intracellular glutamine | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “augmenting intracellular amino acid pools, particularly glutamate and glutamine” (yu2024temporaldynamicsof pages 1-2) | Strong in H. elongata under salt shock. Grounding: glutamine CHEBI:28300. |
| K+ uptake → provides initial osmotic balance before → compatible solute dominance | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “many microbes rapidly uptake K+ after salt shock and later substitute it with compatible solutes… H. elongata primarily accumulates ectoine” (yu2024temporaldynamicsof pages 1-2) | Good mechanistic edge for early-vs-late adaptation; somewhat generalized from review framing plus H. elongata data. Grounding: potassium uptake GO candidate; compatible solute accumulation GO:0015696. |
| NaCl shock → delays then induces → ectoine accumulation | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “ectoine content started to increase until 20 min post-shock, rapidly becoming the dominant osmoprotectant” (yu2024temporaldynamicsof pages 1-2) | Strong temporal edge in H. elongata; useful assay-specific kinetics note. Grounding: ectoine CHEBI:22396. |
| NaCl shock → induces → oxidative stress | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “NaCl shock induced two major stresses, namely osmotic stress and oxidative stress” (yu2024temporaldynamicsof pages 1-2) | Strong H. elongata evidence. Grounding: oxidative stress GO:0006979. |
| NaCl shock → upregulates → cysB | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “transcription factor cys B was significantly upregulated” (yu2024temporaldynamicsof pages 1-2) | Strong locus-specific edge in H. elongata. Grounding: cysB unmapped/gene label. |
| cysB → positively regulates → sulfur metabolism | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “cys B was significantly upregulated, positively regulating the sulfur metabolism” (yu2024temporaldynamicsof pages 1-2) | Strong H. elongata regulatory edge. Grounding: sulfur metabolism GO:0006790. |
| cysB → positively regulates → cysteine biosynthesis | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “cys B was significantly upregulated, positively regulating… cysteine biosynthesis” (yu2024temporaldynamicsof pages 1-2) | Strong H. elongata regulatory edge. Grounding: cysteine biosynthetic process GO:0019344. |
| NaCl shock → upregulates → HELO_RS18165 peroxidase | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “the upregulation of the crucial peroxidase gene (HELO_RS18165)” (yu2024temporaldynamicsof pages 1-2) | Strong but strain/locus-specific. Grounding: peroxidase gene label only. |
| NaCl shock → increases → peroxidase activity | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “the simultaneous enhancement of peroxidase (POD) and catalase (CAT) activities” (yu2024temporaldynamicsof pages 1-2) | Strong H. elongata edge. Grounding: peroxidase EC:1.11.1.7. |
| NaCl shock → increases → catalase activity | Yu et al.; 2024; 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5 | “the simultaneous enhancement of peroxidase (POD) and catalase (CAT) activities” (yu2024temporaldynamicsof pages 1-2) | Strong H. elongata edge. Grounding: catalase EC:1.11.1.6. |
| salt-inducible ectABC operon → encodes → EctB/EctA/EctC | Khanh et al.; 2024; 10.1128/AEM.01195-24; https://doi.org/10.1128/aem.01195-24 | “salt-inducible ectABC operon… contains genes that encode… ectB… ectA… ectC” (khanh2024metabolicpathwayengineering pages 2-6) | Strong H. elongata gene-pathway edge. Grounding: ectB/ectA/ectC gene labels. |
| EctB/EctA/EctC → catalyze → ectoine biosynthesis | Khanh et al.; 2024; 10.1128/AEM.01195-24; https://doi.org/10.1128/aem.01195-24 | “the three enzymes of the ectoine biosynthetic pathway” (khanh2024metabolicpathwayengineering pages 2-6) | Strong pathway edge. Grounding: ectoine biosynthetic process GO:1902235; ectoine CHEBI:22396. |
| EctD → converts → ectoine to hydroxyectoine | Liu et al.; 2021; 10.1186/s12934-021-01567-6; https://doi.org/10.1186/s12934-021-01567-6 | “EctD is the ectoine hydroxylase converting ectoine to hydroxyectoine” (liu2021microbialproductionof pages 1-2) | Strong generic ectoine-pathway edge across halophiles. Grounding: hydroxyectoine CHEBI:60135. |
| BetA → converts → choline to betaine aldehyde | Lichty dissertation; 2024; 10.58088/07hg-r941; https://doi.org/10.58088/07hg-r941 | “GB is typically produced from choline via betA (choline dehydrogenase)” (lichty2024compatiblesolutesare pages 19-23) | First half of GB biosynthesis; dissertation source but specific and mechanistically standard. Grounding: choline CHEBI:15354; betA EC:1.1.99.1. |
| BetB → converts → betaine aldehyde to glycine betaine | Lichty dissertation; 2024; 10.58088/07hg-r941; https://doi.org/10.58088/07hg-r941 | “and betB (betaine-aldehyde dehydrogenase)” (lichty2024compatiblesolutesare pages 19-23) | Second half of GB biosynthesis. Grounding: glycine betaine CHEBI:17750; betB EC:1.2.1.8. |
| ProU ABC transporters → import → compatible solutes | Lichty dissertation; 2024; 10.58088/07hg-r941; https://doi.org/10.58088/07hg-r941 | “ABC transporters (e.g., ProU) requiring proV/proW/proX” (lichty2024compatiblesolutesare pages 19-23) | Good family-level transporter edge; substrate class includes glycine betaine/proline-type osmolytes. Grounding: ProU ABC transporter family. |
| BCCT transporters → import → compatible solutes | Lichty dissertation; 2024; 10.58088/07hg-r941; https://doi.org/10.58088/07hg-r941 | “BCCT carriers (e.g., BetT, BetP, OpuD)” (lichty2024compatiblesolutesare pages 19-23) | Good family-level edge for osmoprotectant uptake. Grounding: BCCT family, compatible-solute transport. |
| TeaABC TRAP transporter → imports → ectoine / hydroxyectoine | Lichty dissertation; 2024; 10.58088/07hg-r941; https://doi.org/10.58088/07hg-r941 | “TRAP systems (e.g., TeaABC, UehABC) that import ectoine and 5-hydroxyectoine” (lichty2024compatiblesolutesare pages 19-23) | Strong transporter-substrate edge. Grounding: TeaABC transporter; ectoine CHEBI:22396; hydroxyectoine CHEBI:60135. |
| TeaABC deletion + Doe pathway disruption → increases → ectoine export | Liu et al.; 2021; 10.1186/s12934-021-01567-6; https://doi.org/10.1186/s12934-021-01567-6 | “By deleting the Trap-TeaABC transporter for ectoine uptake and disrupting the Doe pathway… developed a ‘super-leaky’ H. elongata mutant” (liu2021microbialproductionof pages 2-4) | Strong but engineered strain edge; curate with engineered/biotech flag. |
| DoeA/DoeB/DoeD/DoeC pathway → degrades → ectoine to aspartate | Liu et al.; 2021; 10.1186/s12934-021-01567-6; https://doi.org/10.1186/s12934-021-01567-6 | “Doe pathway converts ectoine back to aspartate via DoeA, DoeB, DoeD and DoeC” (liu2021microbialproductionof pages 2-4) | Strong catabolic pathway edge from genome/pathway analysis. Grounding: Doe gene labels; aspartate CHEBI:22660. |
| putA deletion → increases → proline accumulation | Khanh et al.; 2024; 10.1128/AEM.01195-24; https://doi.org/10.1128/aem.01195-24 | “Genomic deletion of a putA gene… enhanced Pro accumulation” (khanh2024metabolicpathwayengineering pages 2-6) | Strong but engineered edge in ectoine-deficient H. elongata. Grounding: putA gene label; proline CHEBI:17203. |
| putA deletion → increases → high-salinity stress tolerance | Khanh et al.; 2024; 10.1128/AEM.01195-24; https://doi.org/10.1128/aem.01195-24 | “Genomic deletion of a putA gene… increased high-salinity stress tolerance” (khanh2024metabolicpathwayengineering pages 2-6) | Strong but engineered; should be flagged not as native universal trait mechanism. |
| chloride → required for → Halobacillus halophilus growth | Saum & Müller; 2008; 10.1186/1746-1448-4-4; https://doi.org/10.1186/1746-1448-4-4 | “a minimal Cl− concentration of 0.2 M is needed to support cell growth” (saum2008regulationofosmoadaptation pages 2-3) | Strong but taxon-specific to H. halophilus; do not overgeneralize to all moderate halophiles. Grounding: chloride CHEBI:17996; NCBITaxon candidate for H. halophilus if used. |
| chloride → increases expression/activity of → glnA2 | Saum & Müller; 2008; 10.1186/1746-1448-4-4; https://doi.org/10.1186/s1746-1448-4-4 | “The transcription of glnA2… as well as the glutamine synthetase activity were identified as chloride dependent steps” (saum2008regulationofosmoadaptation pages 1-2) | Strong taxon-specific regulation in H. halophilus. Grounding: glnA2; glutamine synthetase EC:6.3.1.2. |
| moderate salinity → favors accumulation of → glutamine and glutamate | Saum & Müller; 2008; 10.1186/1746-1448-4-4; https://doi.org/10.1186/s1746-1448-4-4 | “In the presence of moderate salinities Halobacillus halophilus mainly accumulates glutamine and glutamate” (saum2008regulationofosmoadaptation pages 1-2) | Strong H. halophilus osmolyte-strategy edge. Grounding: glutamine CHEBI:28300; glutamate CHEBI:29991. |
| high salinity → favors accumulation of → proline | Saum & Müller; 2008; 10.1186/1746-1448-4-4; https://doi.org/10.1186/s1746-1448-4-4 | “Halobacillus halophilus switches its osmolyte strategy and produces proline as the main compatible solute at high salinities” (saum2008regulationofosmoadaptation pages 1-2) | Strong H. halophilus edge; taxon-specific regulatory program. |
| stationary phase → favors accumulation of → ectoine | Saum & Müller; 2008; 10.1186/1746-1448-4-4; https://doi.org/10.1186/s1746-1448-4-4 | “at the transition from the exponential to the stationary phase… proline is exchanged by ectoine” (saum2008regulationofosmoadaptation pages 1-2) | Strong H. halophilus growth-phase edge; not universal. |
| salt-out strategy / compatible-solute accumulation → predominates in → moderate halophiles | Ionescu et al.; 2024; 10.3389/frmbi.2023.1329925; https://doi.org/10.3389/frmbi.2023.1329925 | “‘salt-out’, is more common among moderate halophiles… and relies on the accumulation of small organic compounds” (ionescu2024extremefluctuationsin pages 2-4) | Good higher-level ecological edge for the trait, but not universal in every lineage. Grounding: salt-out/compatible-solute strategy label node. |
| osmoadaptation in halophiles → involves → genes for osmolyte synthesis, ion transport, membrane permeability control | Martínez-Espinosa et al.; 2023; 10.3389/fmicb.2023.1252921; https://doi.org/10.3389/fmicb.2023.1252921 | “Genomic analyses link halotolerance to genes for osmolyte synthesis, membrane permeability control, ion transport” (martinezespinosa2023editorialadaptationof pages 1-2) | Broad review-level support for including these node classes; indirect for any single edge, so use cautiously for curation. |


*Table: This table lists curation-oriented subject–predicate–object edges for the moderately halophilic trait, with source-backed snippets, DOI-first citations, and notes on taxon specificity or engineering context. It is useful as a starting point for selecting high-confidence TraitMech edges and flagging uncertain ones.*


### 6) Statistics and data highlights (recent studies emphasized)

- **Ectoine productivity under dynamic salinity (2024):** 8% NaCl shock in *H. elongata* reached **1450 ± 99 mg/L/h**; specific ectoine production **66.54 mg/g DCW/h**. (yu2024temporaldynamicsof pages 2-5)
- **Ectoine accumulation kinetics (2024):** ectoine increase begins ~**20 min post-shock** and becomes dominant osmoprotectant. (yu2024temporaldynamicsof pages 1-2)
- **Industrial benchmark (2021 review of milking):** *H. elongata* DSM142: **7.4 g/L** ectoine at **2.57 M** salinity, **0.22 g/L/h**. (liu2021microbialproductionof pages 2-4)
- **Engineered osmolyte substitution (2024):** engineered *H. elongata* strains can increase proline accumulation and salt tolerance via **salt-inducible proline pathway** and **putA deletion**. (khanh2024metabolicpathwayengineering pages 2-6)


### 7) Expert interpretation and curation warnings (what to curate vs flag)

1. **High-confidence, broadly curation-ready mechanisms:**
   - NaCl/osmotic stress → compatible-solute accumulation (ectoine/betaine/proline/amino acids). (ventosa1998biologyofmoderately pages 19-20, yu2024temporaldynamicsof pages 1-2)
   - Ectoine biosynthesis via ectABC and conversion to hydroxyectoine via ectD. (khanh2024metabolicpathwayengineering pages 2-6, liu2021microbialproductionof pages 1-2)
   - Transport-mediated osmoprotectant uptake (BCCT/ProU/TeaABC families). (lichty2024compatiblesolutesare pages 19-23)

2. **Taxon-specific regulation (curate with organism qualifiers or mark uncertain):**
   - Chloride requirement and chloride-dependent regulation (e.g., glnA2) in *Halobacillus halophilus*. This is a compelling mechanism for that lineage but should not be generalized to all moderate halophiles. (saum2008regulationofosmoadaptation pages 1-2, saum2008regulationofosmoadaptation pages 2-3)

3. **Engineered edges (flag as engineered; may still be useful for mechanism hypotheses):**
   - putA deletion → proline accumulation → improved salt tolerance in ectoine-deficient *H. elongata*. (khanh2024metabolicpathwayengineering pages 2-6)
   - TeaABC deletion + Doe disruption → “super-leaky” ectoine exporter phenotype. (liu2021microbialproductionof pages 2-4)

4. **Incomplete grounding in provided evidence (do not curate yet without additional sources):**
   - Specific Na+/H+ antiporter gene-level edges (e.g., nhaA/mrp) for moderate halophiles were not directly evidenced in the retrieved text excerpts; keep ion transport at a process/family level unless additional primary sources are added. (lee2018naclsaturatedbrinesare pages 15-17, yu2024temporaldynamicsof pages 1-2)


### 8) DOI-first bibliography (with dates and URLs)

- Yu J, et al. **Temporal dynamics of stress response in *Halomonas elongata* to NaCl shock: physiological, metabolomic, and transcriptomic insights.** *Microbial Cell Factories* (Mar 2024). DOI: **10.1186/s12934-024-02358-5**. URL: https://doi.org/10.1186/s12934-024-02358-5 (yu2024temporaldynamicsof pages 2-5, yu2024temporaldynamicsof pages 1-2)
- Khanh HC, et al. **Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient *Halomonas elongata*.** *Applied and Environmental Microbiology* (Sep 2024). DOI: **10.1128/aem.01195-24**. URL: https://doi.org/10.1128/aem.01195-24 (khanh2024metabolicpathwayengineering pages 2-6, khanh2024metabolicpathwayengineering media 3e1e8c19)
- Ionescu D, et al. **Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy.** *Frontiers in Microbiomes* (Jan 2024). DOI: **10.3389/frmbi.2023.1329925**. URL: https://doi.org/10.3389/frmbi.2023.1329925 (ionescu2024extremefluctuationsin pages 2-4)
- Martínez-Espinosa RM, et al. **Editorial: Adaptation of halophilic/halotolerant microorganisms and their applications.** *Frontiers in Microbiology* (Aug 2023). DOI: **10.3389/fmicb.2023.1252921**. URL: https://doi.org/10.3389/fmicb.2023.1252921 (martinezespinosa2023editorialadaptationof pages 1-2)
- Liu M, et al. **Microbial production of ectoine and hydroxyectoine as high-value chemicals.** *Microbial Cell Factories* (Mar 2021). DOI: **10.1186/s12934-021-01567-6**. URL: https://doi.org/10.1186/s12934-021-01567-6 (liu2021microbialproductionof pages 2-4)
- Saum SH, Müller V. **Regulation of osmoadaptation in the moderate halophile *Halobacillus halophilus*: chloride, glutamate and switching osmolyte strategies.** *Saline Systems* (Apr 2008). DOI: **10.1186/1746-1448-4-4**. URL: https://doi.org/10.1186/1746-1448-4-4 (saum2008regulationofosmoadaptation pages 1-2, saum2008regulationofosmoadaptation pages 2-3)
- Ventosa A, Nieto JJ, Oren A. **Biology of moderately halophilic aerobic bacteria.** *Microbiology and Molecular Biology Reviews* (Jun 1998). DOI: **10.1128/mmbr.62.2.504-544.1998**. URL: https://doi.org/10.1128/mmbr.62.2.504-544.1998 (ventosa1998biologyofmoderately pages 2-3, ventosa1998biologyofmoderately pages 19-20)
- Lichty KE Boas. **Compatible Solutes Are Accumulated in Response to Osmotic Stress and Are Used as an Abundant Nutrient Source in Marine Bacteria.** Dissertation (2024). DOI: **10.58088/07hg-r941**. URL: https://doi.org/10.58088/07hg-r941 (lichty2024compatiblesolutesare pages 19-23)


References

1. (ventosa1998biologyofmoderately pages 2-3): Antonio Ventosa, Joaquín J. Nieto, and Aharon Oren. Biology of moderately halophilic aerobic bacteria. Microbiology and Molecular Biology Reviews, 62:504-544, Jun 1998. URL: https://doi.org/10.1128/mmbr.62.2.504-544.1998, doi:10.1128/mmbr.62.2.504-544.1998. This article has 1999 citations and is from a domain leading peer-reviewed journal.

2. (yu2024temporaldynamicsof pages 1-2): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.

3. (khanh2024metabolicpathwayengineering pages 2-6): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

4. (saum2008regulationofosmoadaptation pages 1-2): Stephan H Saum and Volker Müller. Regulation of osmoadaptation in the moderate halophile halobacillus halophilus: chloride, glutamate and switching osmolyte strategies. Saline Systems, 4:4-4, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-4, doi:10.1186/1746-1448-4-4. This article has 160 citations.

5. (saum2008regulationofosmoadaptation pages 2-3): Stephan H Saum and Volker Müller. Regulation of osmoadaptation in the moderate halophile halobacillus halophilus: chloride, glutamate and switching osmolyte strategies. Saline Systems, 4:4-4, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-4, doi:10.1186/1746-1448-4-4. This article has 160 citations.

6. (ionescu2024extremefluctuationsin pages 2-4): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 11 citations.

7. (ventosa1998biologyofmoderately pages 19-20): Antonio Ventosa, Joaquín J. Nieto, and Aharon Oren. Biology of moderately halophilic aerobic bacteria. Microbiology and Molecular Biology Reviews, 62:504-544, Jun 1998. URL: https://doi.org/10.1128/mmbr.62.2.504-544.1998, doi:10.1128/mmbr.62.2.504-544.1998. This article has 1999 citations and is from a domain leading peer-reviewed journal.

8. (liu2021microbialproductionof pages 2-4): Mengshuang Liu, Hui Liu, Meng Shi, Mingyue Jiang, Lingling Li, and Yanning Zheng. Microbial production of ectoine and hydroxyectoine as high-value chemicals. Microbial Cell Factories, Mar 2021. URL: https://doi.org/10.1186/s12934-021-01567-6, doi:10.1186/s12934-021-01567-6. This article has 153 citations and is from a peer-reviewed journal.

9. (lichty2024compatiblesolutesare pages 19-23): Compatible Solutes Are Accumulated in Response to Osmotic Stress and Are Used as an Abundant Nutrient Source in Marine Bacteria This article has 0 citations.

10. (yu2024temporaldynamicsof pages 2-5): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.

11. (khanh2024metabolicpathwayengineering media 3e1e8c19): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

12. (martinezespinosa2023editorialadaptationof pages 1-2): Rosa María Martínez-Espinosa, Sumit Kumar, Sudhir K. Upadhyay, and Furkan Orhan. Editorial: adaptation of halophilic/halotolerant microorganisms and their applications. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1252921, doi:10.3389/fmicb.2023.1252921. This article has 14 citations and is from a peer-reviewed journal.

13. (ventosa1998biologyofmoderately pages 3-4): Antonio Ventosa, Joaquín J. Nieto, and Aharon Oren. Biology of moderately halophilic aerobic bacteria. Microbiology and Molecular Biology Reviews, 62:504-544, Jun 1998. URL: https://doi.org/10.1128/mmbr.62.2.504-544.1998, doi:10.1128/mmbr.62.2.504-544.1998. This article has 1999 citations and is from a domain leading peer-reviewed journal.

14. (liu2021microbialproductionof pages 1-2): Mengshuang Liu, Hui Liu, Meng Shi, Mingyue Jiang, Lingling Li, and Yanning Zheng. Microbial production of ectoine and hydroxyectoine as high-value chemicals. Microbial Cell Factories, Mar 2021. URL: https://doi.org/10.1186/s12934-021-01567-6, doi:10.1186/s12934-021-01567-6. This article has 153 citations and is from a peer-reviewed journal.

15. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

16. (qiao2024expressionofabc pages 2-5): Lijuan Qiao, Guoping Shen, Rui Han, Rong Wang, Xiang Gao, Jiangwa Xing, Yanbing Lin, and Derui Zhu. Expression of abc transporters negatively correlates with ectoine biosynthesis in halomonas campaniensis under nacl and ultraviolet mutagenesis treatments revealed by transcriptomic and proteomics combined analysis. BMC Genomics, Nov 2024. URL: https://doi.org/10.1186/s12864-024-11003-9, doi:10.1186/s12864-024-11003-9. This article has 1 citations and is from a peer-reviewed journal.

17. (lee2018naclsaturatedbrinesare pages 15-17): Callum J D Lee, Phillip E McMullan, Callum J O’Kane, Andrew Stevenson, Inês C Santos, Chayan Roy, Wriddhiman Ghosh, Rocco L Mancinelli, Melanie R Mormile, Geoffrey McMullan, Horia L Banciu, Mario A Fares, Kathleen C Benison, Aharon Oren, Mike L Dyall-Smith, and John E Hallsworth. Nacl-saturated brines are thermodynamically moderate, rather than extreme, microbial habitats. FEMS microbiology reviews, 42 5:672-693, Jun 2018. URL: https://doi.org/10.1093/femsre/fuy026, doi:10.1093/femsre/fuy026. This article has 90 citations and is from a domain leading peer-reviewed journal.