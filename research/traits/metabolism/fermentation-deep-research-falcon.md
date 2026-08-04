---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:09:09.939259'
end_time: '2026-08-04T06:17:02.360068'
duration_seconds: 472.42
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Fermentation
  trait_identifier: METPO:1002005
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: fermentation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A respiration that generates energy through the oxidation of organic
    compounds without using an external electron acceptor, using organic molecules
    as both electron donors and final electron acceptors.
  parent_traits: METPO:1000800
  synonyms: ''
  evidence_summary: 'DOI:10.3389/fmicb.2021.703525: substrate of a fermentation has
    to serve as electron donor as well as acceptor (Supports donor/acceptor definition
    of anaerobic bacterial fermentation.) | DOI:10.1111/1751-7915.13746: Substrate-level
    phosphorylation is one of the main sources of energy (Supports substrate-level
    phosphorylation as a major fermentative energy-conservation mechanism.)'
  causal_graph_summary: 'fermentation_redox_energy: 16 nodes, 12 edges'
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
- **Trait label:** Fermentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1002005
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration that generates energy through the oxidation of organic compounds without using an external electron acceptor, using organic molecules as both electron donors and final electron acceptors.
- **Parent traits:** METPO:1000800
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525: substrate of a fermentation has to serve as electron donor as well as acceptor (Supports donor/acceptor definition of anaerobic bacterial fermentation.) | DOI:10.1111/1751-7915.13746: Substrate-level phosphorylation is one of the main sources of energy (Supports substrate-level phosphorylation as a major fermentative energy-conservation mechanism.)
- **Existing causal graph summary:** fermentation_redox_energy: 16 nodes, 12 edges

## Research Objective

Research the microbial trait **Fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/fermentation.yaml`.

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
- **Trait label:** Fermentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1002005
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration that generates energy through the oxidation of organic compounds without using an external electron acceptor, using organic molecules as both electron donors and final electron acceptors.
- **Parent traits:** METPO:1000800
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525: substrate of a fermentation has to serve as electron donor as well as acceptor (Supports donor/acceptor definition of anaerobic bacterial fermentation.) | DOI:10.1111/1751-7915.13746: Substrate-level phosphorylation is one of the main sources of energy (Supports substrate-level phosphorylation as a major fermentative energy-conservation mechanism.)
- **Existing causal graph summary:** fermentation_redox_energy: 16 nodes, 12 edges

## Research Objective

Research the microbial trait **Fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/fermentation.yaml`.

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


# Curation report: microbial fermentation

## Executive scope

**Target trait:** Fermentation  
**Identifier:** **“METPO:1002005”**  
**Category/kind/status:** METABOLISM / CLASS / REVIEWED  
**Parent:** METPO:1000800

For TraitMech, the defensible core meaning is a **bioenergetic phenotype**: an organism can conserve energy by oxidizing an organic substrate without an external terminal electron acceptor, while reducing substrate-derived organic intermediates/products to close redox balance. Buckel states that, because oxygen and other inorganic acceptors are absent, the substrate must serve as both electron donor and acceptor; nitrate, sulfate, or Fe(III) use would instead make the process respiration. A 2023 microbiology reference similarly says that no terminal acceptor is available and electrons are relocated to organic catabolic products. (weissbrodt2023basicmicrobiologyand pages 16-18, buckel2021energyconservationin pages 1-2)

This scope is narrower than the bioprocess use of *fermentation*. In biotechnology, “fermentation” may mean any microbial cultivation used to manufacture a product, including aerobic lysine production or recombinant-protein production. Precision fermentation likewise denotes optimized engineered cell factories and may be fully aerobic; it is therefore an application/process descriptor, not sufficient evidence for the phenotype **“METPO:1002005”**. (knychala2024precisionfermentationas pages 1-2, buckel2021energyconservationin pages 1-2)

## 1. Trait boundaries

### Include

- Anaerobic redox conversion of carbohydrates, amino acids, or other organic substrates into incompletely oxidized products.
- Internal redox balancing in which substrate-derived intermediates receive reducing equivalents.
- ATP conservation through substrate-level phosphorylation (SLP).
- In taxa that possess them, additional energy conservation through Rnf-linked ion gradients, biotin-dependent ion-pumping decarboxylases, ATP synthase, or flavin-based electron bifurcation. These are important extensions to the older view that fermentation conserves energy exclusively through SLP. (buckel2021energyconservationin pages 1-2)
- Product branches including lactate, ethanol, acetate, butyrate, volatile fatty acids, CO₂, and H₂, provided the complete reaction is redox-balanced. (weissbrodt2023basicmicrobiologyand pages 16-18, buckel2021energyconservationin pages 1-2)

### Exclude or model separately

1. **Anaerobic respiration.** Nitrate, sulfate, Fe(III), fumarate, DMSO, or another externally supplied terminal acceptor indicates respiration, even when oxygen is absent. “Anaerobic” alone is therefore not diagnostic. (weissbrodt2023basicmicrobiologyand pages 16-18, buckel2021energyconservationin pages 1-2)
2. **Aerobic overflow metabolism.** Ethanol or lactate formation in oxygenated cultures can resemble fermentation biochemically, but oxygen availability and respiratory activity must be recorded; do not infer the strict trait solely from product detection.
3. **Methanogenesis.** Methane production uses specialized archaeal energy metabolism and should not automatically be treated as fermentation. Fermenters can instead supply acetate, H₂, and CO₂ to methanogens.
4. **Malolactic conversion.** Malate-to-lactate/CO₂ may alter acidity but does not necessarily provide the core ATP-generating fermentation phenotype; curate as a separate module unless growth/energy conservation is demonstrated.
5. **Industrial or precision fermentation.** Recombinant proteins, enzymes, lipids, and metabolites can be produced in aerated bioreactors. The term describes manufacturing, not necessarily the strict causal trait. (knychala2024precisionfermentationas pages 1-2)
6. **Genomic prediction alone.** Presence of enzymes or an incomplete pathway supports potential, not demonstrated phenotype. Growth, substrate consumption, redox-balanced products, ATP conservation, or flux evidence is preferable.

## 2. Candidate graph nodes

### Trait and process nodes

- Fermentation — **“METPO:1002005”**
- Glycolysis — **GO:0006096**
- Substrate-level phosphorylation — **GO:0006757**
- NAD⁺ regeneration / cellular redox balancing — label-only pending ontology verification
- Alcoholic fermentation — label-only or a verified GO/MetaCyc pathway identifier
- Homolactic fermentation — label-only or verified pathway identifier
- Mixed-acid fermentation — label-only
- Glutamate fermentation through the 3-methylaspartate pathway — label-only; Firmicutes-specific
- Glutamate fermentation through the 2-hydroxyglutarate pathway — label-only; strict-anaerobe-specific
- Flavin-based electron bifurcation — label-only pending verified GO term
- Rnf-dependent ion-gradient generation — label-only

### Chemicals and redox carriers

- Glucose — **CHEBI:17234**
- Pyruvate — **CHEBI:15361**
- ATP — **CHEBI:15422**
- ADP — **CHEBI:16761**
- NAD⁺ — **CHEBI:57540**
- NADH — **CHEBI:57945**
- Ethanol — **CHEBI:16236**
- Acetaldehyde — **CHEBI:15343**
- Carbon dioxide — **CHEBI:16526**
- Lactate — **CHEBI:24996**
- Dihydrogen — **CHEBI:18276** or **CHEBI:16240**, subject to repository convention and validation
- Acetate, butyrate, ferredoxin, reduced ferredoxin, H⁺, and Na⁺ — use only after identifier validation in the target ontology release
- External terminal electron acceptor — label-only superclass
- Nitrate, sulfate, and Fe(III) — verify exact ChEBI protonation/charge forms before YAML insertion

### Enzymes, proteins, genes, and complexes

- Lactate dehydrogenase — **EC:1.1.1.27**; genes are taxon-dependent, commonly *ldh/ldhA*
- Pyruvate decarboxylase — **EC:4.1.1.1**; yeast *PDC1/PDC5/PDC6*
- Alcohol dehydrogenase — **EC:1.1.1.1**; yeast *ADH1/ADH2* have different physiological roles
- Rnf ferredoxin:NAD⁺ oxidoreductase complex — label-only; individual *rnf* genes vary by taxon
- Flavin-based electron-bifurcating ETF/Bcd system — label-only; pathway-specific
- 2-hydroxyglutaryl-CoA dehydratase — label-only; oxygen-sensitive, pathway-specific
- Glutamate mutase — label-only; B₁₂-dependent, pathway-specific
- ATP synthase — verified GO/EC complex identifier should be selected according to taxon and ion specificity
- Acetaldehyde dehydrogenase ALD4 — yeast gene-specific node; relevant to the PDH bypass rather than universal fermentation
- Monocarboxylate transporters JEN1, ADY2, ESBP6 — yeast engineering/application nodes, not universal trait requirements

### Cellular locations

- Cytosol: glycolysis, yeast PDC/ADH ethanol branch, and many SLP reactions.
- Cytoplasmic membrane: Rnf and ATP synthase ion-gradient coupling in applicable bacteria.
- Mitochondrion: taxon- and condition-specific yeast redox/acetaldehyde pathways; not part of the universal core.

### Environmental and assay nodes

- Absence of supplied terminal electron acceptor
- Anoxic/anaerobic incubation
- Organic substrate availability and identity
- pH, temperature, substrate concentration, and product concentration
- Acid stress, ethanol stress, and lignocellulosic inhibitors such as acetate, formate, and furfural
- Product panel, substrate depletion, growth, gas evolution, redox balance, ATP yield, and isotope/metabolic flux

## 3. Candidate causal edges

The strongest curation-ready and conditional edges are summarized below. The table deliberately separates universal definitional relations from yeast- or anaerobic-bacterium-specific mechanisms.

| subject | predicate | object | suggested grounding | evidence DOI and short quote | confidence/scope |
|---|---|---|---|---|---|
| Fermentation | lacks terminal electron acceptor | external terminal electron acceptor | METPO:1002005; label-only: external terminal electron acceptor | 10.2166/9781789062304_0009 — “In fermentation, no terminal e-acceptor is available” (weissbrodt2023basicmicrobiologyand pages 16-18) | High; general definition |
| Fermentation substrate | serves as electron donor and electron acceptor in | fermentation | label-only: fermentation substrate | 10.3389/fmicb.2021.703525 — “the substrate of a fermentation has to serve as electron donor as well as acceptor” (buckel2021energyconservationin pages 1-2) | High; strict bioenergetic definition |
| Presence of inorganic electron acceptor (e.g., nitrate, sulfate, Fe(III)) | excludes classification as | fermentation | CHEBI:nitrate; CHEBI:sulfate; CHEBI:iron(3+) where applicable; label-only: anaerobic respiration | 10.3389/fmicb.2021.703525 — “Inorganic electron acceptors such as nitrate, sulfate or Fe(III) are not involved; otherwise the process would be called respiration rather than fermentation” (buckel2021energyconservationin pages 1-2) | High; boundary with anaerobic respiration |
| Glycolysis | produces | pyruvate + ATP + NADH | GO:0006096; CHEBI:15361 pyruvate; CHEBI:15422 ATP; CHEBI:57945 NADH | 10.5376/be.2024.14.0025 — “Glycolysis (EMP pathway) converts glucose to two pyruvate molecules with net gain of 2 ATP and 2 NADH” (yan2024thebiochemicalbasis pages 1-2) | Moderate; ethanol-focused review but canonical biochemistry |
| Pyruvate | is electron source for reduced fermentation end products | ethanol, lactate, VFAs, H2 | CHEBI:15361 pyruvate; CHEBI:16236 ethanol; CHEBI:24996 lactate; CHEBI:16240 hydrogen | 10.2166/9781789062304_0009 — “electrons are relocated from pyruvate to end up in organic compounds such as ethanol, lactate, and VFAs, as well as dihydrogen” (weissbrodt2023basicmicrobiologyand pages 16-18) | High; general fermentation summary |
| NADH reoxidation | regenerates | NAD+ | CHEBI:57945 NADH; CHEBI:57540 NAD+ | 10.1017/gmb.2022.3 — “the reduced NADH needs to be regenerated” (louis2022microbiallactateutilisation pages 4-6) | High; general redox balancing principle |
| Lactate dehydrogenase (LDH) | redirects carbon flux from pyruvate to | lactate | EC:1.1.1.27; CHEBI:15361 pyruvate; CHEBI:24996 lactate | 10.1128/spectrum.02277-22 — “introduce heterologous lactate dehydrogenase (LDH) genes to redirect carbon flux from pyruvate to LA” (zhu2022metabolicengineeringand pages 1-2) | High; strong but based on engineered yeast context |
| Pyruvate decarboxylase (PDC) | converts | pyruvate to acetaldehyde + CO2 | EC:4.1.1.1; CHEBI:15361 pyruvate; CHEBI:15343 acetaldehyde; CHEBI:16526 CO2 | 10.46991/PYSU:B/2023.57.2.141 — “pyruvate decarboxylase conversion to carbon dioxide and acetaldehyde” (shirvanyan2023evaluationofethanol pages 1-3) | High; canonical yeast ethanol branch |
| Alcohol dehydrogenase (ADH) | reduces | acetaldehyde to ethanol | EC:1.1.1.1; CHEBI:15343 acetaldehyde; CHEBI:16236 ethanol | 10.46991/PYSU:B/2023.57.2.141 — “which is then reduced to ethanol by alcohol dehydrogenase” (shirvanyan2023evaluationofethanol pages 1-3) | High; canonical yeast ethanol branch |
| Ethanol branch (ADH step) | regenerates | NAD+ from NADH | CHEBI:57945 NADH; CHEBI:57540 NAD+ | 10.46991/PYSU:B/2023.57.2.141 — “reduced to ethanol by alcohol dehydrogenase while simultaneously releasing NAD+” (shirvanyan2023evaluationofethanol pages 1-3) | High; yeast-specific wording but general ethanol-branch logic |
| Substrate-level phosphorylation | conserves energy as | ATP in fermentation | GO:0006757; CHEBI:15422 ATP | 10.3389/fmicb.2021.703525 — “substrate level phosphorylation (SLP), by which only part of the available energy could be conserved” (buckel2021energyconservationin pages 1-2) | High; general fermentation energetics |
| Rnf (ferredoxin:NAD+ oxidoreductase) | generates | Na+/H+ motive force | label-only: Rnf complex; GO:1902600 proton motive force or label-only: Na+/H+ motive force | 10.3389/fmicb.2021.703525 — “anaerobes have enzymes which are able to generate a Na+/H+ motive force… the NAD:ferredoxin oxidoreductase (Rnf)” (buckel2021energyconservationin pages 1-2) | Moderate-High; anaerobic bacterial fermentation, not universal |
| Flavin-based electron bifurcation | provides | reduced ferredoxin | label-only: flavin-based electron bifurcation; CHEBI:64708 ferredoxin(reduced) | 10.3389/fmicb.2021.703525 — “Reduced ferredoxin is provided by… the recently discovered flavin based electron bifurcation (FBEB)” (buckel2021energyconservationin pages 1-2) | Moderate-High; anaerobic bacterial fermentation, not universal |
| Strict anaerobic environment / oxygen sensitivity | constrains occurrence of | oxygen-sensitive fermentation enzymes/pathways | ENVO:00002009 anaerobic environment; label-only: oxygen-sensitive radical enzyme | 10.3389/fmicb.2021.703525 — “2-hydroxyglutaryl-CoA dehydratase is extremely oxygen-sensitive and can only survive in the gut” (buckel2021energyconservationin pages 1-2) | Moderate; pathway-specific, not universal to all fermentation |
| External pH 5 and 30°C | increases | ethanol production / biomass relative to tested alternatives | label-only: pH 5; label-only: 30°C; CHEBI:16236 ethanol | 10.46991/PYSU:B/2023.57.2.141 — “at 25℃ and 30℃ pH 5 is optimal for yeast biomass production… At 30℃ ethanol concentration… reached ~117 mM” (shirvanyan2023evaluationofethanol pages 1-3) | Moderate; assay- and strain-specific (S. cerevisiae ATCC 9804/13007) |


*Table: This table summarizes strong, curation-ready causal edges for the microbial trait fermentation, emphasizing strict definitional boundaries, core redox and energy-conservation steps, major product branches, and selected environmental effects. It is useful as a compact starting point for TraitMech graph curation because each edge includes a grounding suggestion, source quote, and scope/confidence note.*

### Additional application-specific edges

| Subject | Predicate | Object | Evidence and snippet | Curation note |
|---|---|---|---|---|
| Heterologous LDH expression | redirects | pyruvate flux toward L-lactate | Zhu et al.: “introduce heterologous lactate dehydrogenase…to redirect carbon flux from pyruvate to LA.” (zhu2022metabolicengineeringand pages 1-2) | Strong intervention evidence, but engineered *S. cerevisiae*, not universal. |
| *PDC1/ADH1* deletion | decreases competing ethanol branch and increases | L-lactate yield | Deletion raised reported LA yield to 0.75 g/g in the reviewed engineering history. (zhu2022metabolicengineeringand pages 1-2) | Strong taxon/engineering-specific edge. |
| Monocarboxylate-transporter engineering | increases | extracellular lactate/export | Transporter screening and strengthened export produced up to 51.4 g/L LA. (zhu2022metabolicengineeringand pages 1-2) | Application edge; transporter identity and host must be retained. |
| Adaptive evolution under increasing lactate | increases | acid tolerance and LA production | Twelve serial subcultures increased production by 17.5%, to 60.4 g/L. (zhu2022metabolicengineeringand pages 1-2) | Assay-specific; do not treat adaptation as a universal mechanism. |
| ALD4 overexpression | increases | lipid production | A 2024 multi-omics study measured a 20.1% increase in *S. cerevisiae*. (lei2024regulatingthemetabolic pages 1-2) | Fully fermentative yeast PDH-bypass application; not evidence that ALD4 is required for fermentation. |
| Lower temperature at pH 5 | increases | ethanol production in tested strains | Ethanol increased as temperature decreased at pH 5; at 30°C, ATCC 13007 reached approximately 117 mM. (shirvanyan2023evaluationofethanol pages 1-3) | Two-strain assay only; direction was not reproduced at pH 6.5. |

## 4. Current understanding and expert analysis

The modern mechanistic picture is broader than “glycolysis plus SLP.” SLP remains a major and often essential source of ATP, but some anaerobic bacteria also conserve energy through electrochemical Na⁺/H⁺ gradients. Buckel identifies biotin-dependent decarboxylases and Rnf as gradient-generating systems and flavin-based electron bifurcation as a route to reduced ferredoxin. These mechanisms should be represented as optional modules beneath fermentation rather than mandatory nodes. (buckel2021energyconservationin pages 1-2)

Redox balance is the unifying causal constraint. Glycolysis generates pyruvate, ATP, and NADH; with no external acceptor, NADH must be reoxidized by reducing endogenous intermediates. In gut fermenters, reducing equivalents are transferred to products such as lactate, propionate, and butyrate, while Rnf/electron-bifurcation systems can redistribute reducing power and improve energy capture. (louis2022microbiallactateutilisation pages 4-6, yan2024thebiochemicalbasis pages 1-2)

The ethanol branch illustrates this clearly. In *S. cerevisiae*, PDC converts pyruvate to acetaldehyde plus CO₂, and ADH reduces acetaldehyde to ethanol while regenerating NAD⁺. The 2023 strain study emphasizes that Adh1 is associated with high-sugar fermentation, whereas Adh2 is more associated with ethanol utilization during respiration and biomass formation; enzyme family membership alone therefore does not establish edge direction in vivo. (shirvanyan2023evaluationofethanol pages 1-3)

Fermentative pathway choice is conditional rather than a fixed species property. Microorganisms can switch among fermentation, aerobic respiration, and anaerobic respiration depending on electron acceptors and substrate conditions. Graph implementations should consequently represent environmental context as causal input rather than encoding “fermenter” as an unconditional organism label. (weissbrodt2023basicmicrobiologyand pages 16-18)

## 5. Recent developments, applications, and statistics

### Metabolic engineering

An engineered *S. cerevisiae* strain produced **121.5 g/L L-lactic acid at up to 0.81 g/g in a 5-L batch bioreactor** after pathway rewiring, transporter engineering, and adaptive evolution. Intermediate interventions included transporter engineering to 51.4 g/L and 12 serial adaptive-evolution passages that increased production by 17.5% to 60.4 g/L. These data demonstrate direct manipulability of the pyruvate branch, export, and acid tolerance. (zhu2022metabolicengineeringand pages 1-2)

A 2024 study used transcriptomics and lipidomics to redirect the yeast pyruvate-dehydrogenase bypass. Overexpressing mitochondrial acetaldehyde dehydrogenase **ALD4 increased lipid production by 20.1%**, illustrating how fermentative central-carbon flux can feed acetyl-CoA-derived commercial products. (lei2024regulatingthemetabolic pages 1-2)

### Process control

In two *S. cerevisiae* strains tested during 2023, pH and temperature altered biomass and product partitioning. Biomass was highest at **30°C and pH 5**; extracellular ethanol reached approximately **117 mM** for ATCC 13007 at 30°C, whereas ATCC 9804 was 1.4-fold lower. Glycerol reached **6.1 mM** for ATCC 9804 after 32 h at 25°C/pH 5. These are useful causal-assay edges but should remain strain-, medium-, and experiment-specific. (shirvanyan2023evaluationofethanol pages 1-3)

### Bioenergy and circular biorefineries

A 2023 review of macroalgal microbial-fuel-cell systems reported power densities ranging from several µW/m² to **8160 mW/m²**, while identifying slow microbial kinetics and high bioproduct cost as commercialization constraints. Such electrofermentation/bioelectrochemical systems can combine L-lactate production with electricity generation, but electrode-mediated electron transfer introduces an external electron sink and should not automatically be curated as strict fermentation. (tong2023sustainablecircularbiorefinery pages 1-2)

### Precision fermentation

A 2024 review describes commercial-scale production of recombinant milk, egg-white, structural, flavor, and nutraceutical proteins in engineered bacterial or yeast cell factories. It identifies scale-up, process optimization, regulation, food safety, and GMO-related concerns as continuing implementation barriers. Because these processes can be aerobic, they belong in an application graph connected to microbial biomanufacturing, not directly as evidence for **“METPO:1002005.”** (knychala2024precisionfermentationas pages 1-2)

## 6. Recommended minimal graph architecture

A robust first revision of `fermentation.yaml` should have a universal backbone and optional branches:

1. **Environmental gate:** no external terminal electron acceptor.
2. **Substrate gate:** fermentable organic substrate is available.
3. **Core catabolism:** substrate → glycolysis/other catabolism → pyruvate or another central intermediate + reducing equivalents.
4. **Energy conservation:** catabolic intermediate → SLP → ATP.
5. **Redox closure:** NADH/reduced ferredoxin → reduction of endogenous intermediate → NAD⁺/oxidized carrier regeneration.
6. **Product alternatives:** lactate; ethanol + CO₂; acetate/butyrate; H₂; other taxon-specific products.
7. **Optional energy modules:** electron bifurcation → reduced ferredoxin; Rnf/decarboxylase → ion gradient → ATP synthase.
8. **Context modifiers:** oxygen/electron acceptors, pH, temperature, inhibitors, and product toxicity.
9. **Evidence outputs:** growth, substrate loss, product stoichiometry, gas formation, ATP or membrane-potential evidence, and redox/flux balance.

Avoid one edge asserting that oxygen absence alone causes fermentation. The stronger relation is: **absence of an external terminal acceptor permits/selects fermentative redox balancing when a suitable organic substrate and pathway machinery are present**.

## 7. Warnings: claims not yet suitable for unconditional curation

- Do not make Rnf, electron bifurcation, hydrogenase, PDC, ADH, or LDH universally required; each occurs only in subsets of fermentative pathways.
- Do not identify every anaerobic growth phenotype as fermentation; alternative acceptors must be excluded experimentally.
- Do not use ethanol, lactate, acetate, or H₂ detection alone. These compounds can arise from overflow metabolism, respiration-linked pathways, cross-feeding, or abiotic reactions.
- Do not treat precision fermentation, aerobic industrial cultivation, microbial fuel cells, or electrofermentation as synonyms of the strict trait.
- Do not curate the 3-methylaspartate and 2-hydroxyglutarate pathways outside their demonstrated taxonomic and oxygen-sensitivity contexts. Buckel’s examples concern particular anaerobic Firmicutes. (buckel2021energyconservationin pages 1-2)
- Do not generalize the pH 5/30°C optimum beyond the two tested *S. cerevisiae* strains and medium. (shirvanyan2023evaluationofethanol pages 1-3)
- Verify every CHEBI, GO, Rhea, KEGG, MetaCyc, UniProt, and NCBITaxon CURIE against the project’s pinned ontology versions before committing YAML. Label-only nodes are safer than guessed identifiers.
- The supplied existing citation DOI:10.1111/1751-7915.13746 was not available in the retrieved full-text evidence set; retain it as existing evidence but independently verify its exact wording before using it for a new edge.

## DOI-first bibliography

1. Buckel W. **Energy Conservation in Fermentations of Anaerobic Bacteria.** *Frontiers in Microbiology.* Published 13 September 2021. https://doi.org/10.3389/fmicb.2021.703525. (buckel2021energyconservationin pages 1-2)
2. Weissbrodt DG, Laureni M, van Loosdrecht MCM, Comeau Y. **Basic microbiology and metabolism.** In *Biological Wastewater Treatment.* Published May 2023. https://doi.org/10.2166/9781789062304_0009. (weissbrodt2023basicmicrobiologyand pages 16-18)
3. Louis P, Duncan SH, Sheridan PO, Walker AW, Flint HJ. **Microbial lactate utilisation and the stability of the gut microbiome.** *Gut Microbiome.* Published May 2022. https://doi.org/10.1017/gmb.2022.3. (louis2022microbiallactateutilisation pages 4-6)
4. Zhu P, Luo R, Li Y, Chen X. **Metabolic Engineering and Adaptive Evolution for Efficient Production of L-Lactic Acid in Saccharomyces cerevisiae.** *Microbiology Spectrum.* Published 10 November 2022. https://doi.org/10.1128/spectrum.02277-22. (zhu2022metabolicengineeringand pages 1-2)
5. Shirvanyan AH. **Evaluation of ethanol and biomass production rate by different Saccharomyces cerevisiae strains depending on external pH and temperature.** *Proceedings of the YSU B: Chemical and Biological Sciences.* Published July 2023. https://doi.org/10.46991/PYSU:B/2023.57.2.141. (shirvanyan2023evaluationofethanol pages 1-3)
6. Lei C et al. **Regulating the metabolic flux of pyruvate dehydrogenase bypass to enhance lipid production in Saccharomyces cerevisiae.** *Communications Biology.* Published October 2024. https://doi.org/10.1038/s42003-024-07103-7. (lei2024regulatingthemetabolic pages 1-2)
7. Tong KTX et al. **Sustainable circular biorefinery approach for novel building blocks and bioenergy production from algae using microbial fuel cell.** *Bioengineered.* Accepted 11 July 2023. https://doi.org/10.1080/21655979.2023.2236842. (tong2023sustainablecircularbiorefinery pages 1-2)
8. Knychala MM et al. **Precision Fermentation as an Alternative to Animal Protein, a Review.** *Fermentation.* Published 14 June 2024. https://doi.org/10.3390/fermentation10060315. (knychala2024precisionfermentationas pages 1-2)
9. Luo Q et al. **Metabolic Engineering of Microorganisms to Produce Pyruvate and Derived Compounds.** *Molecules.* Published February 2023. https://doi.org/10.3390/molecules28031418. (luo2023metabolicengineeringof pages 2-3)
10. Ferreira AM, Mendes-Faia A. **The Role of Yeasts and Lactic Acid Bacteria on the Metabolism of Organic Acids during Winemaking.** *Foods.* Published September 2020. https://doi.org/10.3390/foods9091231. (ferreira2020theroleof pages 3-4)
11. Yan S. **The Biochemical Basis of Ethanol Fermentation and Its Industrial Applications.** *Biological Evidence.* Published January 2024. https://doi.org/10.5376/be.2024.14.0025. (yan2024thebiochemicalbasis pages 1-2)

References

1. (weissbrodt2023basicmicrobiologyand pages 16-18): David G. Weissbrodt, Michele Laureni, Mark C.M. van Loosdrecht, and Yves Comeau. Basic microbiology and metabolism. Biological Wastewater Treatment, pages 9-74, May 2023. URL: https://doi.org/10.2166/9781789062304\_0009, doi:10.2166/9781789062304\_0009. This article has 21 citations.

2. (buckel2021energyconservationin pages 1-2): Wolfgang Buckel. Energy conservation in fermentations of anaerobic bacteria. Frontiers in Microbiology, Sep 2021. URL: https://doi.org/10.3389/fmicb.2021.703525, doi:10.3389/fmicb.2021.703525. This article has 139 citations and is from a peer-reviewed journal.

3. (knychala2024precisionfermentationas pages 1-2): Marilia M. Knychala, Larissa A. Boing, Jaciane L. Ienczak, Débora Trichez, and Boris U. Stambuk. Precision fermentation as an alternative to animal protein, a review. Fermentation, 10:315, Jun 2024. URL: https://doi.org/10.3390/fermentation10060315, doi:10.3390/fermentation10060315. This article has 119 citations.

4. (yan2024thebiochemicalbasis pages 1-2): Shudan Yan. The biochemical basis of ethanol fermentation and its industrial applications. Biological Evidence, Jan 2024. URL: https://doi.org/10.5376/be.2024.14.0025, doi:10.5376/be.2024.14.0025. This article has 2 citations.

5. (louis2022microbiallactateutilisation pages 4-6): Petra Louis, Sylvia Helen Duncan, Paul Owen Sheridan, Alan William Walker, and Harry James Flint. Microbial lactate utilisation and the stability of the gut microbiome. Gut Microbiome, May 2022. URL: https://doi.org/10.1017/gmb.2022.3, doi:10.1017/gmb.2022.3. This article has 224 citations.

6. (zhu2022metabolicengineeringand pages 1-2): Pan Zhu, Rui Luo, Yize Li, and Xiulai Chen. Metabolic engineering and adaptive evolution for efficient production of <scp>l</scp> -lactic acid in saccharomyces cerevisiae. Dec 2022. URL: https://doi.org/10.1128/spectrum.02277-22, doi:10.1128/spectrum.02277-22. This article has 37 citations and is from a domain leading peer-reviewed journal.

7. (shirvanyan2023evaluationofethanol pages 1-3): Anahit H. Shirvanyan. Evaluation of ethanol and biomass production rate by different $saccharomyces~cerevisiae$ strains depending on external ph and temperature. Proceedings of the YSU B: Chemical and Biological Sciences, 57:141-153, Jul 2023. URL: https://doi.org/10.46991/pysu:b/2023.57.2.141, doi:10.46991/pysu:b/2023.57.2.141. This article has 10 citations.

8. (lei2024regulatingthemetabolic pages 1-2): Cairong Lei, Xiaopeng Guo, Miaomiao Zhang, Xiang Zhou, Nan Ding, Junle Ren, Meihan Liu, Chenglin Jia, Yajuan Wang, Jingru Zhao, Ziyi Dong, and Dong Lu. Regulating the metabolic flux of pyruvate dehydrogenase bypass to enhance lipid production in saccharomyces cerevisiae. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-07103-7, doi:10.1038/s42003-024-07103-7. This article has 28 citations and is from a peer-reviewed journal.

9. (tong2023sustainablecircularbiorefinery pages 1-2): Kevin Tian Xiang Tong, Inn Shi Tan, Henry Chee Yew Foo, Pau Loke Show, Man Kee Lam, and Mee Kee Wong. Sustainable circular biorefinery approach for novel building blocks and bioenergy production from algae using microbial fuel cell. Bioengineered, 14:246-289, Jul 2023. URL: https://doi.org/10.1080/21655979.2023.2236842, doi:10.1080/21655979.2023.2236842. This article has 38 citations.

10. (luo2023metabolicengineeringof pages 2-3): Qian Luo, Nana Ding, Yunfeng Liu, Hailing Zhang, Yu Fang, and Lianghong Yin. Metabolic engineering of microorganisms to produce pyruvate and derived compounds. Molecules, 28:1418, Feb 2023. URL: https://doi.org/10.3390/molecules28031418, doi:10.3390/molecules28031418. This article has 71 citations.

11. (ferreira2020theroleof pages 3-4): Ana Mendes Ferreira and Arlete Mendes-Faia. The role of yeasts and lactic acid bacteria on the metabolism of organic acids during winemaking. Foods, 9:1231, Sep 2020. URL: https://doi.org/10.3390/foods9091231, doi:10.3390/foods9091231. This article has 284 citations.