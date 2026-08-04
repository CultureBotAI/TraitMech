---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:36:03.450503'
end_time: '2026-08-04T10:45:07.811982'
duration_seconds: 544.36
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: autotrophic
  trait_identifier: METPO:1000632
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: autotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism produces organic compounds from
    inorganic carbon sources (primarily carbon dioxide or bicarbonate) using energy
    from light (photoautotrophy) or from the oxidation of inorganic compounds (chemoautotrophy).
  parent_traits: METPO:1000631
  synonyms: TT_autotroph, autotroph, autotrophy
  evidence_summary: 'DOI:10.1038/nrmicro.2016.130: require only CO2 as a carbon source
    (Review defines autotrophic organisms by CO2 use as carbon source for growth.)
    | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports Calvin-Benson
    and other microbial CO2-fixation pathways.) | PMID:8590279: Synechocystis sp.
    strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model autotrophic
    cyanobacterium that fixes CO2 via the Calvin-Benson cycle (Kaneko et al. 1996,
    DNA Res, full genome).)'
  causal_graph_summary: 'autotrophic_inorganic_carbon_fixation: 18 nodes, 17 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** autotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000632
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism produces organic compounds from inorganic carbon sources (primarily carbon dioxide or bicarbonate) using energy from light (photoautotrophy) or from the oxidation of inorganic compounds (chemoautotrophy).
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_autotroph, autotroph, autotrophy
- **Existing evidence:** DOI:10.1038/nrmicro.2016.130: require only CO2 as a carbon source (Review defines autotrophic organisms by CO2 use as carbon source for growth.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports Calvin-Benson and other microbial CO2-fixation pathways.) | PMID:8590279: Synechocystis sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model autotrophic cyanobacterium that fixes CO2 via the Calvin-Benson cycle (Kaneko et al. 1996, DNA Res, full genome).)
- **Existing causal graph summary:** autotrophic_inorganic_carbon_fixation: 18 nodes, 17 edges

## Research Objective

Research the microbial trait **autotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/autotrophic.yaml`.

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
- **Trait label:** autotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000632
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism produces organic compounds from inorganic carbon sources (primarily carbon dioxide or bicarbonate) using energy from light (photoautotrophy) or from the oxidation of inorganic compounds (chemoautotrophy).
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_autotroph, autotroph, autotrophy
- **Existing evidence:** DOI:10.1038/nrmicro.2016.130: require only CO2 as a carbon source (Review defines autotrophic organisms by CO2 use as carbon source for growth.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports Calvin-Benson and other microbial CO2-fixation pathways.) | PMID:8590279: Synechocystis sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model autotrophic cyanobacterium that fixes CO2 via the Calvin-Benson cycle (Kaneko et al. 1996, DNA Res, full genome).)
- **Existing causal graph summary:** autotrophic_inorganic_carbon_fixation: 18 nodes, 17 edges

## Research Objective

Research the microbial trait **autotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/autotrophic.yaml`.

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


# Curation report: microbial trait **autotrophic**

## 1. Trait record and scope

- **Trait label:** autotrophic
- **Trait identifier:** **METPO:1000632**
- **Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED
- **Parent:** METPO:1000631
- **Synonyms:** TT_autotroph; autotroph; autotrophy

### Operational definition

For TraitMech, **autotrophic** should denote an organism-level physiological capacity to grow while obtaining biomass carbon from inorganic carbon—principally CO₂ or HCO₃⁻—with energy and reducing power supplied by either light (**photoautotrophy**) or oxidation/uptake of inorganic electron donors (**chemolithoautotrophy**). Claassens et al. explicitly define autotrophs as organisms requiring “only CO₂ as a carbon source for growth” and state that microbial autotrophs derive energy from light or inorganic electron donors. Thus, the terminal phenotype should be **growth/biomass production from inorganic carbon**, not merely expression of a carboxylase or detectable CO₂ incorporation. (claassens2016harnessingthepower pages 1-2)

The supplied definition is therefore current and suitable, with one practical refinement: assays may provide HCO₃⁻ rather than gaseous CO₂, and a valid demonstration should show that inorganic carbon supplies essentially all net biomass carbon under the tested condition.

### Boundary cases

1. **Carbon fixation is not equivalent to autotrophy.** Heterotrophs routinely incorporate inorganic carbon through anaplerotic and biosynthetic carboxylation. Estimated inorganic-carbon contributions are commonly 1–8% of heterotrophic microbial biomass; the broader review estimates at least 1–5%, and as much as 50% in methanotrophs. Such incorporation must not be curated as autotrophy without inorganic-carbon-supported growth. (braun2021reviewsandsyntheses pages 1-2)
2. **Mixotrophy is distinct.** Concurrent use of organic and inorganic carbon is mixotrophy, even when an autotrophic fixation pathway operates. A strain capable of both modes may receive the autotrophic trait only when growth is demonstrated under an inorganic-carbon-only condition. (claassens2016harnessingthepower pages 1-2)
3. **Photoautotrophy and chemolithoautotrophy are child mechanisms, not synonyms for the entire trait.** Phototrophy describes energy acquisition and does not by itself establish the carbon source; similarly, oxidation of H₂, sulfur, Fe²⁺, NH₃, or extracellular minerals does not establish autotrophy unless coupled to net inorganic-carbon assimilation.
4. **Genomic potential is weaker than phenotype.** A MAG containing Rubisco, CODH/ACS, or another pathway should support a candidate mechanism or “autotrophic potential,” not a definitive organismal trait, unless expression, isotope incorporation, or growth data are available. The 2024 deep-aquifer study, for example, reports genes for autotrophic pathways in 60% of MAGs but properly interprets these as chemosynthetic capacity. (atencio2024metabolicadaptationsunderpin pages 1-2)
5. **Methanotrophy and methylotrophy are generally not autotrophy.** CH₄ and methanol are organic C₁ carbon sources. Auxiliary CO₂ assimilation does not change that classification.
6. **Carbon-concentrating mechanisms are enabling modules, not universal requirements.** Carboxysomes are central to cyanobacterial and some bacterial CBB systems, but autotrophs using Wood–Ljungdahl, rTCA, 3HP, or archaeal cycles need not possess them. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2)

## 2. Candidate graph nodes

Only identifiers that can be stated confidently are proposed. Label-only nodes should remain ungrounded until checked against the project’s preferred ontology release.

### A. Trait and biological-process nodes

| Candidate node | Suggested grounding | Curation role |
|---|---|---|
| autotrophic | **METPO:1000632** | Terminal phenotype |
| carbon fixation | GO:0015977 | General inorganic-carbon assimilation process |
| Calvin–Benson–Bassham cycle | label-only; verify MetaCyc/KEGG pathway identifier | Dominant cyclic fixation module |
| Wood–Ljungdahl pathway / reductive acetyl-CoA pathway | label-only; verify MetaCyc identifier | Linear anaerobic fixation module |
| reductive TCA cycle | label-only | Fixation module |
| 3-hydroxypropionate bicycle | label-only | Fixation module |
| 3-hydroxypropionate/4-hydroxybutyrate cycle | label-only | Archaeal fixation module |
| dicarboxylate/4-hydroxybutyrate cycle | label-only | Archaeal fixation module |
| reductive glycine pathway | label-only | Natural/synthetic C₁ assimilation candidate |
| cyanobacterial carbon-concentrating mechanism (CCM) | label-only | Carbon acquisition and concentration module |
| oxygenic photosynthesis | GO term should be release-verified | Light-energy module |
| extracellular electron uptake | label-only | Alternative electron-acquisition module |

A recent review lists CBB, Wood–Ljungdahl, rTCA, 3HP, 3HP/4HB, DC/4HB, reductive glycine, and reverse oxidative TCA mechanisms, but pathway counts and whether the last two qualify as established natural *autotrophic growth* cycles vary among reviews. The safest core graph should begin with the six canonical pathways and add newer routes only with organism-level growth evidence. (li2024processstudyon pages 1-2, li2024productionofsuccinate pages 1-2)

### B. Chemicals, energy sources, and environmental nodes

| Candidate node | Suggested grounding | Role |
|---|---|---|
| carbon dioxide | CHEBI:16526 | Inorganic carbon substrate |
| hydrogencarbonate/bicarbonate | CHEBI:17544 | Inorganic carbon substrate and CCM pool |
| dioxygen | CHEBI:15379 | Photosynthetic product, Rubisco competitor, electron acceptor, and pathway constraint |
| water | CHEBI:15377 | Oxygenic photosynthesis/CA substrate |
| ATP | CHEBI:15422 | Energy currency for fixation and transport |
| NADPH | CHEBI:16474 | Reducing power for CBB and biosynthesis |
| molecular hydrogen | CHEBI identifier should be release-verified | Common chemolithotrophic electron donor |
| reduced sulfur compounds; Fe²⁺; ammonia; nitrite; phosphite | label-only pending exact species | Taxon-specific inorganic electron donors |
| light | ENVO or ontology term to be verified | Photoautotrophic energy input |
| low inorganic carbon | label-only environmental state | Inducer of cyanobacterial CCM |
| anoxia / microoxia | ENVO terms to be verified | Selects oxygen-sensitive pathways |
| hypersaline sediment | ENVO term to be verified | Environment favoring low-energy anaerobic fixation |
| poised electrode / redox-active mineral | label-only | Insoluble electron donor for electrosynthesis/EEU |
| 2-phosphoglycolate | CHEBI identifier to be verified | Low-Ci/photorespiration signal |
| 2-oxoglutarate | CHEBI identifier to be verified | Cellular C/N-status signal |
| ribulose 1,5-bisphosphate (RuBP) | CHEBI identifier to be verified | Rubisco substrate and CsoSCA activator |
| 3-phosphoglycerate | CHEBI identifier to be verified | Initial CBB product |

### C. Genes, proteins, enzymes, transporters, and complexes

| Candidate node | Grounding | Function/scope |
|---|---|---|
| Rubisco, RbcL/RbcS | EC:4.1.1.39; GO molecular-function term should be verified | CO₂ carboxylation in CBB |
| carbonic anhydrase | EC:4.2.1.1; GO:0004089 | Reversible CO₂/HCO₃⁻ interconversion |
| CsoSCA | taxon-specific protein; UniProt per strain | α-carboxysomal CA |
| SbtA | UniProt per strain | High-affinity Na⁺/HCO₃⁻ transporter |
| BicA | UniProt per strain | Na⁺/HCO₃⁻ symporter |
| BCT1/CmpABCD | UniProt per strain | ATP-driven HCO₃⁻ uptake system |
| NDH-1₃/CupA and NDH-1₄/CupB | UniProt per strain | Energy-coupled CO₂ uptake/hydration complexes |
| SbtB | UniProt per strain | PII-family regulator of SbtA |
| CcmR/NdhR, CyAbrB2, CmpR, RbcR | UniProt per strain | CCM transcriptional regulators |
| CODH/ACS complex | EC and UniProt components require pathway-specific verification | Central Wood–Ljungdahl CO₂/CO-to-acetyl-CoA machinery |
| ATP citrate lyase or alternative citrate-cleavage enzymes | verify per taxon | Key rTCA module |
| acetyl-CoA carboxylase and propionyl-CoA carboxylase | EC identifiers should be verified | 3HP-cycle carboxylation reactions |
| formate dehydrogenase | enzyme family requires reaction-specific grounding | CO₂/formate interconversion in reductive routes |
| multiheme c-type cytochrome conduit | protein-specific grounding required | Direct extracellular electron uptake |

### D. Cellular-location nodes

| Candidate node | Suggested grounding | Role |
|---|---|---|
| carboxysome | GO:0031470 | Protein microcompartment containing Rubisco and CA |
| carboxysome lumen | label-only | Local high-CO₂ reaction space |
| cytoplasm | GO:0005737 | HCO₃⁻ pool and most CBB regeneration reactions |
| cytoplasmic membrane | GO:0005886 | Ci transporters |
| thylakoid membrane | GO identifier should be verified | Photosynthetic electron transport and NDH complexes |
| periplasm / outer membrane | GO terms should be verified | Ci passage and possible electron-transfer interfaces |

Kurkela and Tyystjärvi’s 2024 CCM figures directly show BCT1, BicA, SbtA, NDH-1₃/CupA, NDH-1₄/CupB, carboxysomal CA/Rubisco, the CBB cycle, photosystems, NADPH formation, and ATP synthase in their relevant compartments. (kurkela2024inorganiccarbonsensing media d31d5ffa, kurkela2024inorganiccarbonsensing media 73d706c5)

## 3. Candidate causal edges

The following table uses curation-oriented predicates. “High” means that the cited source directly states or experimentally demonstrates the relation; “conditional” indicates taxonomic or environmental restriction.

| # | Subject–predicate–object triple | Reference | Supporting snippet | Curation note |
|---:|---|---|---|---|
| 1 | **CO₂ + light or inorganic electron donor —supports→ autotrophic biomass production** | 10.1038/nrmicro.2016.130 | “Autotrophic microorganisms convert CO₂ into biomass by deriving energy from light or inorganic electron donors.” | **High; defining edge.** Make this the graph’s terminal mechanistic convergence. (claassens2016harnessingthepower pages 1-2)
| 2 | **organic carbon required for growth —contradicts→ strict autotrophic assay state** | 10.1038/nrmicro.2016.130 | “Heterotrophs…require organic substrates as a carbon source for growth.” | High as a boundary, but facultative autotrophs may switch modes. (claassens2016harnessingthepower pages 1-2)
| 3 | **heterotrophic CO₂ fixation —does-not-entail→ autotrophic** | 10.5194/bg-18-3689-2021 | “All heterotrophs…take up CO₂ and incorporate it into their biomass.” | **High; essential negative curation rule.** CO₂ labeling alone is inadequate. (braun2021reviewsandsyntheses pages 1-2)
| 4 | **SbtA/BicA/BCT1 —imports→ HCO₃⁻ into cyanobacterial cytoplasm** | 10.1111/ppl.14140 | “The CCM includes bicarbonate transporters SbtA, BicA and BCT1.” | High, **cyanobacteria-specific**; individual species may lack one or more systems. (kurkela2024inorganiccarbonsensing pages 1-2)
| 5 | **NDH-1₃/CupA and NDH-1₄/CupB —convert→ CO₂ to cytoplasmic HCO₃⁻** | 10.1111/ppl.14140 | Specialized NDH complexes “convert CO₂ to HCO₃⁻ in the cytoplasm.” | High, cyanobacterial CCM. (kurkela2024inorganiccarbonsensing pages 1-2)
| 6 | **CCM transporters —establish→ concentrated cytosolic HCO₃⁻ pool** | 10.1126/sciadv.adk7283 | “Energy-coupled inorganic carbon…transporters actively establish a concentrated pool of HCO₃⁻.” | High; links uptake to compartmentalized fixation. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2)
| 7 | **cytosolic HCO₃⁻ —diffuses-into→ carboxysome** | 10.1126/sciadv.adk7283 | “This HCO₃⁻ then diffuses into…carboxysomes.” | High; cyanobacteria and bacterial CCM-containing autotrophs. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2)
| 8 | **carboxysomal carbonic anhydrase —converts→ HCO₃⁻ to CO₂** | 10.1126/sciadv.adk7283 | “Here, the CA converts HCO₃⁻ to CO₂ to elevate luminal CO₂.” | **High and curation-ready.** Use EC:4.2.1.1 for generic CA, protein-specific IDs for isoforms. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2)
| 9 | **carboxysome —increases-local-concentration-of→ CO₂ near Rubisco** | 10.1111/1462-2920.16283 | CCMs produce “an increased concentration of CO₂ and reduced concentration of O₂ around RuBisCO.” | High; causal enabling edge, not universal to all autotrophs. (huffine2023roleofcarboxysomes pages 1-2)
| 10 | **elevated CO₂ near Rubisco —increases→ Rubisco substrate turnover** | 10.1126/sciadv.adk7283 | CCMs increase local CO₂ near Rubisco, “thereby increasing its substrate turnover.” | High; mechanistic effect. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2)
| 11 | **elevated CO₂ near Rubisco —competitively inhibits→ Rubisco oxygenation** | 10.1126/sciadv.adk7283 | Elevated CO₂ “competitively inhibit[s] competing oxygenation reactions.” | High; represents suppression of photorespiratory loss. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2)
| 12 | **Rubisco —catalyzes→ first CBB carbon-fixation reaction** | 10.1111/ppl.14140 | Carboxysomes contain Rubisco and CA, “bodies in which the first reaction of carbon fixation occurs.” | High. More chemically explicit reaction edges should use a reaction database after stoichiometric verification. (kurkela2024inorganiccarbonsensing pages 1-2)
| 13 | **RuBP —allosterically activates→ Cyanobium CsoSCA** | 10.1126/sciadv.adk7283 | “Cyanobium CsoSCA is allosterically activated by…ribulose-1,5-bisphosphate.” | **High but taxon-specific.** Do not generalize beyond α-cyanobacterial carboxysome CAs. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2)
| 14 | **low inorganic carbon —activates/acclimates→ cyanobacterial CCM** | 10.1111/ppl.14140 | “In low Ci…cyanobacteria efficiently collect Ci using a carbon concentrating mechanism.” | High at system level; regulator-specific edges require the finer statements below. (kurkela2024inorganiccarbonsensing pages 1-2)
| 15 | **2-phosphoglycolate accumulation —signals→ low inorganic carbon** | 10.1111/ppl.14140 | 2-phosphoglycolate accumulation “indicates low Ci.” | High in reviewed cyanobacterial regulation. (kurkela2024inorganiccarbonsensing pages 1-2)
| 16 | **2-phosphoglycolate + RuBP —activate→ CmpR** | 10.1111/ppl.14140 | “2-phosphoglycolate and ribulose-1,5-bisphosphate activate transcription activator CmpR.” | High, cyanobacterial regulatory edge. (kurkela2024inorganiccarbonsensing pages 1-2)
| 17 | **CcmR/NdhR, CyAbrB2, CmpR, RbcR —regulate→ CCM genes** | 10.1111/ppl.14140 | These proteins “act as transcription factors regulating CCM genes.” | High, but direction and target operons should be represented in taxon-specific subgraphs. (kurkela2024inorganiccarbonsensing pages 1-2)
| 18 | **CCM transporter/NDH loss —prevents→ ambient-air growth** | 10.1111/ppl.14140 | Inactivation of two NDH complexes and three bicarbonate systems yields cells that “cannot grow in ambient air but grow in high CO₂.” | High experimental genotype-to-phenotype edge; exact source experiment should be attached when available. (kurkela2024inorganiccarbonsensing pages 1-2)
| 19 | **CODH/ACS oxygen sensitivity —restricts→ Wood–Ljungdahl activity to anoxia** | 10.1186/s12934-024-02470-6 | WLP is “limited to absolutely anaerobic settings because of the high sensitivity of the CO dehydrogenase/acetyl-CoA synthase to oxygen.” | High review-supported pathway constraint. (li2024productionofsuccinate pages 1-2)
| 20 | **oxygen-sensitive enzymes —restrict→ rTCA and DC/4HB cycles to anaerobic/microaerobic conditions** | 10.1186/s12934-024-02470-6 | Oxygen-sensitive enzymes cause these cycles “to operate under conditions of anaerobic and microaerobic.” | Moderate-to-high; annotate as pathway-level and verify organism-specific exceptions. (li2024productionofsuccinate pages 1-2)
| 21 | **anoxic + hypersaline conditions —select-for→ Wood–Ljungdahl autotrophy** | 10.1093/femsec/fiae105 | The authors infer selection for “the lowest energy requiring CO₂-fixation pathway known, the Wood–Ljungdahl pathway,” under anoxic hypersaline conditions. | **Conditional ecological edge.** It is a field-supported selection hypothesis, not a universal deterministic rule. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)
| 22 | **H₂ + CO₂ —supports→ autotrophic acetogenesis** | 10.1093/femsec/fiae105 | The sediment study identifies “novel hydrogenotrophic acetogens” and discusses acetate generation from H₂ and CO₂. | Conditional and taxon-specific; H₂ is electron donor, CO₂ is carbon source/electron acceptor in acetogenesis. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)
| 23 | **redox-active mineral/electrode electron uptake —supplies-electrons-for→ autotrophic CO₂ fixation** | 10.1007/s10295-020-02309-0 | EEU uses electrons from “redox-active minerals, poised electrodes, or other microbial cells”; direct transfer can involve multiheme c-type cytochromes. | Moderate-to-high; create organism-specific edges only when EEU and fixation are experimentally coupled. (gupta2020extracellularelectronuptake pages 1-2)
| 24 | **CBB/Wood–Ljungdahl genes in MAGs —supports-inference-of→ autotrophic potential** | 10.1038/s41598-024-68868-9 | “60% of MAGs harbored genes for autotrophic pathways.” | Evidence edge only; **not sufficient for confirmed phenotype**. (atencio2024metabolicadaptationsunderpin pages 1-2)
| 25 | **ATP/NADPH optimization —increases→ engineered CO₂-fixing succinate production** | 10.1186/s12934-024-02470-6 | Optimization included “ATP and NADPH supply,” and the strain produced 3.6 g L⁻¹ succinate. | Application edge, but **mixotrophic/heterotrophic engineering**, not proof of strict autotrophy. (li2024productionofsuccinate pages 1-2)

The strongest core edges are summarized here:

| subject | predicate | object | scope/taxon | confidence | primary DOI |
|---|---|---|---|---|---|
| Inorganic carbon (CO2/HCO3-) + light or inorganic electron donor | supports growth of | autotrophic biomass | microbial autotrophs, general definition | High (definition) (claassens2016harnessingthepower pages 1-2) | 10.1038/nrmicro.2016.130 |
| SbtA/BicA/BCT1 bicarbonate transporters | contribute to | cytoplasmic HCO3- accumulation for CCM | cyanobacteria | High (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing media d31d5ffa) | 10.1111/ppl.14140 |
| NDH-1_3 / NDH-1_4 specialized complexes | convert | CO2 to HCO3- in the cytoplasm | cyanobacteria | High (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing media d31d5ffa) | 10.1111/ppl.14140 |
| Carboxysome-localized carbonic anhydrase | converts | HCO3- to CO2 in carboxysome lumen | cyanobacteria and some autotrophic bacteria | High (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2, huffine2023roleofcarboxysomes pages 1-2) | 10.1126/sciadv.adk7283 |
| Carboxysome | elevates local CO2 near | Rubisco | bacterial CCM, especially cyanobacteria | High (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2, huffine2023roleofcarboxysomes pages 1-2) | 10.1111/1462-2920.16283 |
| Rubisco | catalyzes first step of | Calvin-Benson carbon fixation | cyanobacteria / CBB autotrophs | High (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2, kurkela2024inorganiccarbonsensing pages 1-2) | 10.1111/ppl.14140 |
| RuBP | allosterically activates | CsoSCA carbonic anhydrase | α-cyanobacterial carboxysome | High, taxon-specific (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2) | 10.1126/sciadv.adk7283 |
| Low inorganic carbon | induces/regulates | CCM genes and transport functions | cyanobacteria | High (kurkela2024inorganiccarbonsensing pages 1-2) | 10.1111/ppl.14140 |
| Wood-Ljungdahl pathway | is favored in | anoxic hypersaline conditions | dark hypersaline sediments | High, environment-specific (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2) | 10.1093/femsec/fiae105 |
| Oxygen sensitivity of CODH/ACS | restricts | Wood-Ljungdahl pathway to anaerobic settings | microbes using WL pathway | High (li2024productionofsuccinate pages 1-2) | 10.1186/s12934-024-02470-6 |
| Oxygen-sensitive enzymes | restrict | rTCA and DC/4HB cycles to anaerobic/microaerobic conditions | pathway-level, general | Moderate (review summary) (li2024productionofsuccinate pages 1-2) | 10.1186/s12934-024-02470-6 |
| Heterotrophic CO2 fixation | does not imply | autotrophy | boundary warning, all heterotrophs | High (braun2021reviewsandsyntheses pages 1-2) | 10.5194/bg-18-3689-2021 |


*Table: This table summarizes strong, curation-ready causal edges for microbial autotrophy, emphasizing core definition, cyanobacterial CCM mechanisms, and environmental constraints on major carbon-fixation pathways. It also includes a key boundary warning to prevent over-curation of heterotrophic CO2 incorporation as autotrophy.*

## 4. Recommended initial TraitMech graph architecture

A conservative graph can retain the existing `autotrophic_inorganic_carbon_fixation` structure while separating five layers:

1. **Inputs:** CO₂/HCO₃⁻ plus light or a defined inorganic electron donor.
2. **Energy conservation:** photosynthetic electron transport or donor oxidation → proton motive force → ATP; electron transfer → NAD(P)H/reduced ferredoxin.
3. **Carbon acquisition:** diffusion/transport; in cyanobacteria, SbtA/BicA/BCT1 and NDH-1₃/NDH-1₄ → cytosolic HCO₃⁻.
4. **Carbon fixation:** CCM/carboxysome → CA → CO₂ near Rubisco → CBB, or an alternative pathway-specific module such as CODH/ACS → acetyl-CoA.
5. **Phenotypic outcome:** inorganic carbon incorporated into central metabolites → biosynthesis → **growth/biomass with inorganic carbon as sole or predominant biomass-carbon source** → METPO:1000632.

This modular design prevents a cyanobacteria-specific CCM from being represented as universal and allows pathway alternatives to converge on the same physiological endpoint.

## 5. Recent developments, applications, and quantitative evidence

### 5.1 Mechanistic advances, 2023–2024

- **Regulatory coupling inside α-carboxysomes:** Pulsford et al. showed structurally and biochemically that CsoSCA from *Cyanobium* sp. PCC7001 forms a hexameric trimer of dimers and is allosterically activated by RuBP. The sequence evidence suggests this regulation is specific to cyanobacterial α-carboxysome CAs, providing a new feedback edge between the CBB substrate pool and local CO₂ generation. Published **10 May 2024**. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2)
- **Current cyanobacterial CCM model:** the 2024 synthesis identifies SbtA, BicA, BCT1, NDH-1₃, NDH-1₄, carboxysomes, and the CcmR/CmpR/RbcR regulatory network, while emphasizing that mechanisms controlling carboxysome dynamics and coordination of cell division with Ci remain incompletely known. Published in **January 2024**. (kurkela2024inorganiccarbonsensing pages 1-2)
- **Carboxysome importance:** all free-living cyanobacteria possess carboxysomes, and these structures are required for survival at present ambient CO₂; the CCM raises CO₂ and lowers O₂ around Rubisco, reducing photorespiration. Published in the 2023 journal volume. (huffine2023roleofcarboxysomes pages 1-2)

### 5.2 Environmental implementation

- In deep Negev aquifers extending to **1.5 km**, measured chemosynthetic productivity was **0.55 ± 0.06 to 0.82 ± 0.07 µg C L⁻¹ d⁻¹**, and **60% of MAGs** encoded predicted autotrophic pathways, mainly CBB and Wood–Ljungdahl. These data support active dark primary production and identify deep aquifers as potentially underestimated carbon sinks. Published **August 2024**. (atencio2024metabolicadaptationsunderpin pages 1-2)
- In a **30-cm Great Salt Lake sediment core**, 36 MAG-based OTUs shifted from aerobic/heterotrophic near the surface to anaerobic/autotrophic at depth. Dark fixation was detected and WLP was predicted as the dominant mode. The authors interpret this as energetic selection for WLP in combined anoxia and salt stress. Published **25 July 2024**. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)

### 5.3 Biotechnology and real-world relevance

- **Engineered carbon conversion:** a *Cupriavidus necator* H16 process used two partial 3HP-cycle carboxylations per succinate. Isotope labeling showed that **50% of succinate carbon** came from CO₂; the optimized strain reached **3.6 g L⁻¹**, a **159% increase** over the starting strain. This is a valuable carbon-fixation application but uses fatty acid as an organic carbon/energy source and therefore should not be curated as strict autotrophy. Published **July 2024**. (li2024productionofsuccinate pages 1-2)
- **Carbon removal:** a 2024 expert review estimates current anthropogenic emissions at approximately **40 billion tonnes CO₂ yr⁻¹** and the carbon removal needed for a 1.5 °C pathway at roughly **10 billion tonnes yr⁻¹**. It reports that cyanobacteria/microalgae may yield approximately fourfold more biomass than terrestrial plants and can be cultivated on non-arable land, but stresses thermodynamic, land, water, reactor, and permanence constraints. Published **17 June 2024**. (kim2024recentadvancesin pages 1-2)
- **Microbial electrosynthesis:** autotrophs can receive electrons from electrodes or redox-active minerals through direct cytochrome conduits or indirect shuttles, providing a mechanistic basis for electricity-to-chemical systems. Evidence remains organism- and reactor-specific. (gupta2020extracellularelectronuptake pages 1-2)

The expert consensus is that microbial autotrophy offers important routes to sustainable chemicals, fuels, carbon capture, primary production, and wastewater/resource-recovery systems, but industrial performance remains constrained by carbon-transfer rates, energy/reductant supply, pathway oxygen sensitivity, slow growth, product recovery, and the need to prove durable net carbon removal rather than transient fixation. (claassens2016harnessingthepower pages 1-2, kim2024recentadvancesin pages 1-2)

## 6. Warnings: claims not yet suitable for TraitMech curation

1. **Do not infer METPO:1000632 from a single fixation gene, pathway-completeness score, or MAG annotation.** Record these as predicted potential.
2. **Do not infer autotrophy from ¹³CO₂ incorporation alone** unless organic-carbon carryover and anaplerotic fixation are excluded and growth/biomass yield is demonstrated.
3. **Do not treat all eight recently enumerated fixation mechanisms as equally established natural autotrophic pathways.** The reductive glycine pathway and “reverse oxidative TCA” classification require strain-level growth evidence and nomenclature reconciliation. (li2024processstudyon pages 1-2, li2024productionofsuccinate pages 1-2)
4. **Do not universalize CsoSCA activation by RuBP.** Current evidence is specific to α-cyanobacterial CsoSCA and absent from the examined chemoautotrophic homolog. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2)
5. **Do not make carboxysomes obligatory for autotrophy.** They belong only to CCM-containing CBB implementations.
6. **Do not encode anoxia as universally causing WLP autotrophy.** The Great Salt Lake result is an ecological selection interpretation under combined hypersalinity, anoxia, and energy limitation. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)
7. **Do not classify the engineered succinate process as autotrophic.** Fatty acids supply organic carbon and reducing power even though two CO₂-fixing reactions contribute half the product carbon. (li2024productionofsuccinate pages 1-2)
8. **Avoid unverified CURIEs.** Transporters, operons, pathway records, and environmental states should be resolved against the exact ontology/database releases used by TraitMech before YAML insertion.
9. **Separate capacity from expression and activity.** `has_gene`, `expresses_gene`, `catalyzes_reaction`, `supports_growth`, and `has_trait` should remain distinct predicates.

## 7. DOI-first bibliography

1. Pulsford, S. B. et al. “Cyanobacterial α-carboxysome carbonic anhydrase is allosterically regulated by the Rubisco substrate RuBP.” *Science Advances* 10 (2024). Published **10 May 2024**. DOI: [10.1126/sciadv.adk7283](https://doi.org/10.1126/sciadv.adk7283). (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2)
2. Kurkela, J. & Tyystjärvi, T. “Inorganic carbon sensing and signalling in cyanobacteria.” *Physiologia Plantarum* 176 (2024). Published **January 2024**; accepted 12 December 2023. DOI: [10.1111/ppl.14140](https://doi.org/10.1111/ppl.14140). (kurkela2024inorganiccarbonsensing pages 1-2)
3. Atencio, B. et al. “Metabolic adaptations underpin high productivity rates in relict subsurface water.” *Scientific Reports* 14, 18126 (2024). Published **August 2024**. DOI: [10.1038/s41598-024-68868-9](https://doi.org/10.1038/s41598-024-68868-9). (atencio2024metabolicadaptationsunderpin pages 1-2)
4. Shoemaker, A. et al. “Wood–Ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at Great Salt Lake, Utah.” *FEMS Microbiology Ecology* 100 (2024). Published **25 July 2024**. DOI: [10.1093/femsec/fiae105](https://doi.org/10.1093/femsec/fiae105). (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)
5. Li, L. et al. “Production of succinate with two CO₂ fixation reactions from fatty acids in *Cupriavidus necator* H16.” *Microbial Cell Factories* 23, 194 (2024). Published **July 2024**. DOI: [10.1186/s12934-024-02470-6](https://doi.org/10.1186/s12934-024-02470-6). (li2024productionofsuccinate pages 1-2)
6. Kim, D. S. et al. “Recent advances in engineering fast-growing cyanobacterial species for enhanced CO₂ fixation.” *Frontiers in Climate* 6, 1412232 (2024). Published **17 June 2024**. DOI: [10.3389/fclim.2024.1412232](https://doi.org/10.3389/fclim.2024.1412232). (kim2024recentadvancesin pages 1-2)
7. Huffine, C. A. et al. “Role of carboxysomes in cyanobacterial CO₂ assimilation.” *Environmental Microbiology* 25, 219–228 (2023 volume; online 2022). DOI: [10.1111/1462-2920.16283](https://doi.org/10.1111/1462-2920.16283). (huffine2023roleofcarboxysomes pages 1-2)
8. Braun, A. et al. “Heterotrophic fixation of inorganic carbon—significant but invisible flux in environmental carbon cycling.” *Biogeosciences* 18, 3689–3700 (2021). Published **21 June 2021**. DOI: [10.5194/bg-18-3689-2021](https://doi.org/10.5194/bg-18-3689-2021). (braun2021reviewsandsyntheses pages 1-2)
9. Gupta, D., Guzman, M. S. & Bose, A. “Extracellular electron uptake by autotrophic microbes.” *Journal of Industrial Microbiology and Biotechnology* 47, 863–876 (2020). Published **October 2020**. DOI: [10.1007/s10295-020-02309-0](https://doi.org/10.1007/s10295-020-02309-0). (gupta2020extracellularelectronuptake pages 1-2)
10. Claassens, N. J. et al. “Harnessing the power of microbial autotrophy.” *Nature Reviews Microbiology* 14, 692–706 (2016). Published online **26 September 2016**. DOI: [10.1038/nrmicro.2016.130](https://doi.org/10.1038/nrmicro.2016.130). (claassens2016harnessingthepower pages 1-2)
11. Berg, I. A. et al. “Autotrophic carbon fixation in archaea.” *Nature Reviews Microbiology* 8, 447–460 (2010). Published **May 2010**. DOI: [10.1038/nrmicro2365](https://doi.org/10.1038/nrmicro2365). (berg2010autotrophiccarbonfixation pages 9-10, berg2010autotrophiccarbonfixation pages 10-11)

**Curation recommendation:** retain **METPO:1000632** as an organism-level growth phenotype and build alternative mechanistic branches beneath it. The cyanobacterial CCM/CBB branch is currently the most evidence-dense and curation-ready; WLP and other fixation branches should retain explicit oxygen, taxonomic, electron-donor, and assay-context qualifiers.

References

1. (claassens2016harnessingthepower pages 1-2): Nico J. Claassens, Diana Z. Sousa, Vitor A. P. Martins dos Santos, Willem M. de Vos, and John van der Oost. Harnessing the power of microbial autotrophy. Nature Reviews Microbiology, 14:692-706, Sep 2016. URL: https://doi.org/10.1038/nrmicro.2016.130, doi:10.1038/nrmicro.2016.130. This article has 333 citations and is from a highest quality peer-reviewed journal.

2. (braun2021reviewsandsyntheses pages 1-2): Alexander Braun, Marina Spona-Friedl, Maria Avramov, Martin Elsner, Federico Baltar, Thomas Reinthaler, Gerhard J. Herndl, and Christian Griebler. Reviews and syntheses: heterotrophic fixation of inorganic carbon – significant but invisible flux in environmental carbon cycling. Biogeosciences, 18:3689-3700, Jun 2021. URL: https://doi.org/10.5194/bg-18-3689-2021, doi:10.5194/bg-18-3689-2021. This article has 104 citations and is from a domain leading peer-reviewed journal.

3. (atencio2024metabolicadaptationsunderpin pages 1-2): Betzabe Atencio, Eyal Geisler, Maxim Rubin-Blum, Edo Bar-Zeev, Eilon M. Adar, Roi Ram, and Zeev Ronen. Metabolic adaptations underpin high productivity rates in relict subsurface water. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-68868-9, doi:10.1038/s41598-024-68868-9. This article has 3 citations and is from a peer-reviewed journal.

4. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2): Sacha B. Pulsford, Megan A. Outram, Britta Förster, Timothy Rhodes, Simon J. Williams, Murray R. Badger, G. Dean Price, Colin J. Jackson, and Benedict M. Long. Cyanobacterial α-carboxysome carbonic anhydrase is allosterically regulated by the rubisco substrate rubp. Science Advances, May 2024. URL: https://doi.org/10.1126/sciadv.adk7283, doi:10.1126/sciadv.adk7283. This article has 27 citations and is from a highest quality peer-reviewed journal.

5. (li2024processstudyon pages 1-2): Manman Li. Process study on microbial fixation of co&lt;sub&gt;2&lt;/sub&gt; and its conversion into organic acids. Biological Evidence, Jan 2024. URL: https://doi.org/10.5376/be.2024.14.0016, doi:10.5376/be.2024.14.0016. This article has 1 citations.

6. (li2024productionofsuccinate pages 1-2): Linqing Li, Xiuyuan Zhou, Zhuoao Gao, Peng Xiong, and Xiutao Liu. Production of succinate with two co2 fixation reactions from fatty acids in cupriavidus necator h16. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02470-6, doi:10.1186/s12934-024-02470-6. This article has 13 citations and is from a peer-reviewed journal.

7. (kurkela2024inorganiccarbonsensing media d31d5ffa): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 24 citations and is from a peer-reviewed journal.

8. (kurkela2024inorganiccarbonsensing media 73d706c5): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 24 citations and is from a peer-reviewed journal.

9. (kurkela2024inorganiccarbonsensing pages 1-2): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 24 citations and is from a peer-reviewed journal.

10. (huffine2023roleofcarboxysomes pages 1-2): Clair A. Huffine, Runyu Zhao, Yinjie J. Tang, and Jeffrey C. Cameron. Role of carboxysomes in cyanobacterial <scp>co<sub>2</sub></scp> assimilation: <scp>co<sub>2</sub></scp> concentrating mechanisms and metabolon implications. Environmental Microbiology, 25:219-228, Nov 2023. URL: https://doi.org/10.1111/1462-2920.16283, doi:10.1111/1462-2920.16283. This article has 43 citations and is from a domain leading peer-reviewed journal.

11. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2): Anna Shoemaker, Andrew Maritan, Su Cosar, Sylvia Nupp, Ana Menchaca, Thomas Jackson, Aria Dang, Bonnie K Baxter, Daniel R Colman, Eric C Dunham, and Eric S Boyd. Wood–ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at great salt lake, utah. FEMS Microbiology Ecology, Jul 2024. URL: https://doi.org/10.1093/femsec/fiae105, doi:10.1093/femsec/fiae105. This article has 15 citations and is from a peer-reviewed journal.

12. (gupta2020extracellularelectronuptake pages 1-2): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.

13. (kim2024recentadvancesin pages 1-2): David S. Kim, José Ángel Moreno-Cabezuelo, Eduardo Nicolas Schulz, David J. Lea-Smith, and Uma Shankar Sagaram. Recent advances in engineering fast-growing cyanobacterial species for enhanced co2 fixation. Frontiers in Climate, Jun 2024. URL: https://doi.org/10.3389/fclim.2024.1412232, doi:10.3389/fclim.2024.1412232. This article has 29 citations and is from a peer-reviewed journal.

14. (berg2010autotrophiccarbonfixation pages 9-10): Ivan A. Berg, Daniel Kockelkorn, W. Hugo Ramos-Vera, Rafael F. Say, Jan Zarzycki, Michael Hügler, Birgit E. Alber, and Georg Fuchs. Autotrophic carbon fixation in archaea. Nature Reviews Microbiology, 8:447-460, May 2010. URL: https://doi.org/10.1038/nrmicro2365, doi:10.1038/nrmicro2365. This article has 1063 citations and is from a highest quality peer-reviewed journal.

15. (berg2010autotrophiccarbonfixation pages 10-11): Ivan A. Berg, Daniel Kockelkorn, W. Hugo Ramos-Vera, Rafael F. Say, Jan Zarzycki, Michael Hügler, Birgit E. Alber, and Georg Fuchs. Autotrophic carbon fixation in archaea. Nature Reviews Microbiology, 8:447-460, May 2010. URL: https://doi.org/10.1038/nrmicro2365, doi:10.1038/nrmicro2365. This article has 1063 citations and is from a highest quality peer-reviewed journal.