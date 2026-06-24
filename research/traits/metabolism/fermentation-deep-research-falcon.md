---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:57:47.993468'
end_time: '2026-06-18T05:18:45.149511'
duration_seconds: 1257.16
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
  causal_graph_summary: 'fermentation_redox_energy: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Fermentation
- **METPO identifier:** METPO:1002005
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration that generates energy through the oxidation of organic compounds without using an external electron acceptor, using organic molecules as both electron donors and final electron acceptors.
- **Parent traits:** METPO:1000800
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525: substrate of a fermentation has to serve as electron donor as well as acceptor (Supports donor/acceptor definition of anaerobic bacterial fermentation.) | DOI:10.1111/1751-7915.13746: Substrate-level phosphorylation is one of the main sources of energy (Supports substrate-level phosphorylation as a major fermentative energy-conservation mechanism.)
- **Existing causal graph summary:** fermentation_redox_energy: 6 nodes, 5 edges

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
- **METPO identifier:** METPO:1002005
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration that generates energy through the oxidation of organic compounds without using an external electron acceptor, using organic molecules as both electron donors and final electron acceptors.
- **Parent traits:** METPO:1000800
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525: substrate of a fermentation has to serve as electron donor as well as acceptor (Supports donor/acceptor definition of anaerobic bacterial fermentation.) | DOI:10.1111/1751-7915.13746: Substrate-level phosphorylation is one of the main sources of energy (Supports substrate-level phosphorylation as a major fermentative energy-conservation mechanism.)
- **Existing causal graph summary:** fermentation_redox_energy: 6 nodes, 5 edges

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


## Microbial Trait Causal Graph Curation Report: Fermentation (METPO:1002005)

### Scope summary (TraitMech curation target)
**Fermentation (METPO:1002005)** is best curated as an **anaerobic metabolic capacity** in which cells conserve energy by coupling oxidation of an organic substrate to reduction of **internally generated electron acceptors** (typically organic intermediates), with ATP produced canonically by **substrate-level phosphorylation (SLP)** rather than by using an external terminal electron acceptor. A modern synthesis emphasizes “organic compounds serve as both electron donors and acceptors” and uses this to distinguish fermentation from anaerobic respiration using acceptors such as nitrate or sulfur compounds. (hackmann2024thevastlandscape pages 1-2)

**Boundary cases:** contemporary reviews stress that strict “no inorganic acceptor” rules break down in some fermentations because **protons can act as electron acceptors** (yielding H2) and **H2 can be co-used as an electron donor** in some secondary fermentations; handling these cases is left to curator discretion. (hackmann2024thevastlandscape pages 2-3)

**Practical curation decision:** for METPO:1002005, treat fermentation as a **class-level trait** that is true when organisms can perform internally balanced anaerobic catabolism (often SLP-centered), while allowing optional submodules (e.g., Rnf/Ech, electron bifurcation, hydrogenogenesis) as mechanistic nodes that modify energy yield/product spectrum rather than redefining fermentation itself. (hackmann2024thevastlandscape pages 5-6, hackmann2024thevastlandscape pages 2-3)

---

## 1) Key concepts and definitions (current understanding)

### Definition anchors
Multiple modern definitions converge on fermentation as anaerobic catabolism where redox balance is achieved without an external terminal electron acceptor, because reduced cofactors (e.g., NADH) are reoxidized by pathway intermediates/end products; SLP is a defining ATP source. (hackmann2024thevastlandscape pages 1-2)

### Distinguishing from nearby traits
- **Anaerobic respiration:** uses **external** terminal acceptors such as nitrate/sulfur compounds; these processes are explicitly excluded from fermentation in the reviewed definition set. (hackmann2024thevastlandscape pages 1-2)
- **Homoacetogenesis/methanogenesis:** often treated as outside “fermentation” in strict definitions; however, the boundary becomes ambiguous when fermentation uses protons/H2/CO2 as part of electron disposal or secondary fermentation. (hackmann2024thevastlandscape pages 2-3, hackmann2024thevastlandscape pages 1-2)
- **Mixed-acid fermentation:** a subtype/product-spectrum pattern rather than a different fundamental energy logic; it is best modeled as a branch module under fermentation. (moon2023anewmetabolic pages 1-2, taggar2024hydrogenproductionvia pages 5-7)

### Edge-case rule of thumb for curation
- If ATP conservation relies mainly on SLP and internal redox balancing (including H2 evolution), curate as fermentation.
- If growth depends on externally supplied electron acceptors (nitrate, electrodes) or sustained electron transport chain use, mark as **edge/conditional** or consider a different trait linkage (anaerobic respiration / EET). (tejedorsanz2023extracellularelectronuptake pages 2-3, tejedorsanz2023extracellularelectronuptake pages 1-2, hackmann2024thevastlandscape pages 1-2)

---

## 2) Recent developments and latest research (prioritize 2023–2024)

### A. Large-scale synthesis of fermentation diversity and pathway complexity (2024)
A 2024 FEMS Microbiology Reviews synthesis compiled a cross-organism view of fermentation with several quantitative “state-of-the-field” results:
- **>1/4 of ~8,300** prokaryotes examined were capable of fermentation. (hackmann2024thevastlandscape pages 2-3)
- Reported diversity includes **46 substrates**, **55 end products**, and nearly **300 end-product combinations**. (hackmann2024thevastlandscape pages 2-3)
- A detailed map of glucose fermentation spans **123 reactions, 127 enzymes, and 97 metabolites**, underscoring pathway modularity (multiple routes to the same end product). (hackmann2024thevastlandscape pages 5-6)

Figure evidence (diversity and stoichiometry/ATP accounting) was extracted from this review (phylogenetic diversity and ATP/yield summary). (hackmann2024thevastlandscape media ac3846af, hackmann2024thevastlandscape media 15f20e7e)

### B. Fermentation bioenergetics beyond SLP: electron bifurcation + ion-gradient modules
A recurring 2023–2024 theme is that fermenters can achieve additional energy conservation or redox flexibility via:
- **Flavin-based electron bifurcation (FBEB):** defined as coupling an exergonic and endergonic redox reaction within one enzyme complex; flavins enable sequential one-electron transfers via an anionic semiquinone intermediate. (kumar2023moleculararchitectureand pages 1-2)
- **Rnf/Ech modules:** membrane-associated complexes that couple ferredoxin-linked redox reactions to **ion translocation**, enabling ATP synthesis via ATP synthases; these can increase ATP yield in some fermentations (e.g., butyrate formation). (hackmann2024thevastlandscape pages 7-9, hackmann2024thevastlandscape pages 5-6)

### C. Environmental control of fermentation via hydrogen (gut + dark fermentation)
Recent data-driven work in gut microbiology emphasizes H2 as a thermodynamic regulator:
- Colonic H2 can range from “undetectable to **over 40% v/v**.” (campbell2023h2generatedby pages 1-2)
- In butyrate producers, **high H2** favors reduced organic products (butyrate/lactate/formate) over acetate/H2/CO2; adding an H2-consuming methanogen reduced H2 and decreased butyrate in a synthetic community. (campbell2023h2generatedby pages 1-2)

For engineered/dark fermentation hydrogen production, a 2024 review reports quantitative constraints:
- NADH-derived H2 formation requires **very low H2 partial pressure (<60 Pa)**. (taggar2024hydrogenproductionvia pages 5-7)
- Stoichiometry/yields depend on end-product pattern: acetate-associated routes are higher theoretical H2 yield than butyrate routes; practical mixed yields often **~1–2.5 mol H2/mol glucose**. (taggar2024hydrogenproductionvia pages 5-7)

### D. Fermentation boundary expansion: electrofermentation/EET in “primarily fermentative” taxa
A 2023 study showed a lactic acid bacterium (typically fermentative) can uptake electrons from a cathode and couple them to reduction of pyruvate and an **external inorganic acceptor (nitrate)**, rerouting glucose fermentation and increasing viability after sugar exhaustion. (tejedorsanz2023extracellularelectronuptake pages 1-2)
Quantitatively, nitrate reduction increased under EET compared with open-circuit conditions (8.98 ± 2.29 mM/day vs 1.19 ± 1.16 mM/day), and current uptake depended on nitrate presence. (tejedorsanz2023extracellularelectronuptake pages 2-3)

This should be curated as an **edge-case mechanism** (“fermentation + conditional external acceptor/EET module”), not as the core definition. (tejedorsanz2023extracellularelectronuptake pages 2-3, tejedorsanz2023extracellularelectronuptake pages 1-2)

---

## 3) Current applications and real-world implementations

### Industrial and food applications (broad)
A recent synthesis highlights applications spanning fermented foods, agriculture, and industrial bioproducts, with active manipulation strategies including **genetic engineering** and **electrofermentation**. (hackmann2024thevastlandscape pages 1-2)

### Chain elongation (waste-to-chemicals; medium-chain carboxylates)
A 2023 study quantified ethanol-based chain elongation (a fermentation-linked process) and provided a thermodynamic/stoichiometric anchor usable as a mechanistic constraint in curation:
- Overall stoichiometry: **3 ethanol → hexanoate + H+ + 2 H2 + H2O** with ΔG°′ = **−67.9 kJ/mol**. (allaart2023physiologicalandstoichiometric pages 2-3)
- Under electron-acceptor limitation, energy conservation was reported to occur via **SLP rather than Rnf-driven chemiosmosis** in the described condition. (allaart2023physiologicalandstoichiometric pages 2-3)

### Gut microbiome and health
Hydrogen cycling and fermentation end products (e.g., butyrate) are implicated in ecosystem function and host-relevant metabolite outputs; high H2 and hydrogenase inhibition shifted product distributions in butyrate producers, and methanogen addition decreased butyrate in communities. (campbell2023h2generatedby pages 1-2)

---

## 4) Expert opinions and authoritative analysis (mechanistic framing)

### Mechanistic consensus from authoritative reviews
- **Hackmann 2024 (FEMS Microbiol Rev)** argues for a broadened, practical fermentation definition (organic donor/acceptor logic) while explicitly acknowledging edge cases where protons/H2/CO2 complicate strict boundaries, and emphasizes that pathway maps show unexpected complexity and multiple ATP-conserving strategies including ATP synthase contributions. (hackmann2024thevastlandscape pages 2-3)
- **Kumar et al. 2023 (Nat Commun)** frames FBEB as a key anaerobic strategy that allows coupling redox reactions at the thermodynamic limit and connects NAD(H)/NADP(H) pools via bifurcating transhydrogenases (Nfn/Stn). (kumar2023moleculararchitectureand pages 1-2)

---

## 5) Recent statistics and data points (curation-relevant)

### Diversity/coverage statistics
- **>1/4 of prokaryotes fermentative** (analysis of ~8,300 descriptions). (hackmann2024thevastlandscape pages 2-3)
- Documented: **46 substrates**, **55 end products**, ~**300 product combinations**. (hackmann2024thevastlandscape pages 2-3)
- Glucose fermentation map: **123 reactions**, **127 enzymes**, **97 metabolites**. (hackmann2024thevastlandscape pages 5-6)

### Bioenergetic/pathway accounting
- Fermentation may be augmented by **Rnf/Ech** and electron bifurcation/confurcation; Rnf/Ech can increase ATP yield (reported up to ~50% for butyrate formation in the synthesis). (hackmann2024thevastlandscape pages 7-9)
- Figures summarizing ATP yields and cofactor stoichiometries for glucose fermentation end products were extracted for reference. (hackmann2024thevastlandscape media 15f20e7e)

### Environmental measurements and constraints
- Colonic H2: “undetectable to **over 40% v/v**.” (campbell2023h2generatedby pages 1-2)
- Dark fermentation: NADH-derived H2 formation requires **<60 Pa** H2 partial pressure; typical yields **~1–2.5 mol H2/mol glucose** in practice. (taggar2024hydrogenproductionvia pages 5-7)

### Electrofermentation/EET quantitative results
- Cathode EET + nitrate: nitrate reduction rate **8.98 ± 2.29 mM/day** with EET vs **1.19 ± 1.16 mM/day** open-circuit; current uptake required nitrate. (tejedorsanz2023extracellularelectronuptake pages 2-3)

---

## Candidate nodes for `fermentation.yaml` (grouped by type)

### Trait / processes
- Fermentation (METPO:1002005; GO:0006113 fermentation) (hackmann2024thevastlandscape pages 1-2)
- Substrate-level phosphorylation (GO term needed) (hackmann2024thevastlandscape pages 1-2)
- Electron bifurcation / flavin-based electron bifurcation (GO term needed) (kumar2023moleculararchitectureand pages 1-2)
- Hydrogen production / hydrogenogenesis (GO term needed) (taggar2024hydrogenproductionvia pages 5-7)

### Pathways / modules
- Glycolysis (Embden–Meyerhof–Parnas; GO glycolytic process) (hackmann2024thevastlandscape pages 4-5)
- Pentose phosphate pathway (GO pentose-phosphate shunt) (hackmann2024thevastlandscape pages 4-5)
- Pyruvate metabolism; branch modules to acetate/lactate/ethanol/butyrate/propionate/succinate (hackmann2024thevastlandscape pages 10-11)
- Mixed-acid fermentation module (moon2023anewmetabolic pages 1-2)
- Reverse β-oxidation / chain elongation (hexanoate formation) (allaart2023physiologicalandstoichiometric pages 2-3)

### Enzymes / complexes (EC-grounded where available)
- Pyruvate:ferredoxin oxidoreductase (PFOR; **EC 1.2.7.1**) (hackmann2024thevastlandscape pages 5-6)
- Rnf complex (ferredoxin—NAD oxidoreductase; **EC 7.2.1.2**) (hackmann2024thevastlandscape pages 5-6)
- Ech (energy-converting hydrogenase; **EC 7.1.1.-**) (hackmann2024thevastlandscape pages 5-6)
- Ferredoxin—NAD+ reductase (**EC 1.18.1.3**) (hackmann2024thevastlandscape pages 6-7)
- Nfn transhydrogenase (**EC 1.6.1.4**) and Stn family transhydrogenase (structure/mechanism) (kumar2023moleculararchitectureand pages 1-2)
- Butyryl-CoA dehydrogenase (**EC 1.3.8.1**) (hackmann2024thevastlandscape pages 5-6)
- Electron-transferring flavoprotein:methylmenaquinone oxidoreductase (EMO; **EC 1.5.5.1**) (hackmann2024thevastlandscape pages 11-12)
- Lactate dehydrogenase (NAD+, ferredoxin) (**EC 1.1.1.436**) (hackmann2024thevastlandscape pages 11-12)
- Formate dehydrogenases (**EC 1.17.1.11 / 1.17.5.3 / 1.17.1.9**) (hackmann2024thevastlandscape pages 11-12)

### Metabolites / electron carriers (CHEBI grounding recommended)
- Glucose; fructose; pyruvate; acetyl-CoA; crotonyl-CoA; NAD+/NADH; NADP+/NADPH; ferredoxin (Fdox/Fdred); H+/H2; CO2; acetate; lactate; ethanol; formate; butyrate; propionate; succinate. (hackmann2024thevastlandscape pages 5-6, hackmann2024thevastlandscape pages 10-11)

### Environmental / experimental factors (ENVO grounding recommended)
- Anoxic/oxygen-free conditions; oxygen presence (inhibits H2 production) (taggar2024hydrogenproductionvia pages 5-7)
- Hydrogen partial pressure / hydrogen atmosphere (campbell2023h2generatedby pages 1-2, taggar2024hydrogenproductionvia pages 5-7)
- External electron acceptors (e.g., nitrate) and electrodes/cathodes (electrofermentation/EET edge case) (tejedorsanz2023extracellularelectronuptake pages 2-3, tejedorsanz2023extracellularelectronuptake pages 1-2)

---

## Candidate causal edges (evidence-backed)
The following table is formatted for direct review and translation into TraitMech edge assertions.

| Edge (S–P–O) | Node types | Suggested IDs/grounding (EC/GO/CHEBI/ENVO where available) | Evidence snippet (short quote) | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| Fermentation — has defining feature — organic substrate serves as electron donor and acceptor | trait → definition | METPO:1002005; GO:0006113 fermentation; candidate CHEBI organic substrate | “organic compounds serve as both electron donors and acceptors” (hackmann2024thevastlandscape pages 1-2) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Strong, broad definition-level edge. |
| Fermentation — excludes — external inorganic terminal electron acceptor use | trait → boundary condition | GO:0006113; CHEBI:nitrate candidate; CHEBI:sulfur compounds candidate | “excludes processes that use external inorganic terminal acceptors, explicitly naming nitrate respiration, sulfur respiration” (hackmann2024thevastlandscape pages 1-2) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Strong boundary edge; useful to distinguish from anaerobic respiration. |
| Fermentation — primarily conserves energy by — substrate-level phosphorylation | trait → process | GO:0006757 ATP generation from ADP; candidate GO substrate-level phosphorylation | “ATP is made by substrate-level phosphorylation” (hackmann2024thevastlandscape pages 1-2, moon2023anewmetabolic pages 1-2) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016; 10.1111/1758-2229.13160, 2023, https://doi.org/10.1111/1758-2229.13160 | Strong canonical edge; some fermenters also use ion-gradient systems. |
| Glycolysis/EMP — feeds into — pyruvate fermentation branches | pathway → metabolite/process | GO:glycolytic process candidate; CHEBI:17234 glucose; CHEBI:15361 pyruvate | “glycolysis (EMP) and the pentose phosphate pathway feed to pyruvate” (hackmann2024thevastlandscape pages 4-5) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Broad pathway scaffold edge. |
| Pentose phosphate pathway — feeds into — pyruvate fermentation branches | pathway → metabolite/process | GO:pentose-phosphate shunt candidate; CHEBI:15361 pyruvate | “the pentose phosphate pathway feed to pyruvate” (hackmann2024thevastlandscape pages 4-5) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Useful alternate entry route. |
| Pyruvate:ferredoxin oxidoreductase — produces — reduced ferredoxin | enzyme → electron carrier | EC:1.2.7.1; CHEBI:15361 pyruvate; CHEBI:23357 ferredoxin | “pyruvate:ferredoxin oxidoreductase… produces reduced ferredoxin” (hackmann2024thevastlandscape pages 5-6, taggar2024hydrogenproductionvia pages 5-7) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016; 10.35812/cellulosechemtechnol.2024.58.90, 2024, https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Strong mechanistic edge central to redox balancing. |
| Reduced ferredoxin — requires reoxidation by — ferredoxin:NAD+ oxidoreductase / Rnf / hydrogenase systems | electron carrier → enzyme/process | EC:1.18.1.3; EC:7.2.1.2; candidate [FeFe]-hydrogenase | “without Rnf, fermentation would become unbalanced” and enzymes “prevent buildup of reduced ferredoxin” (hackmann2024thevastlandscape pages 5-6, hackmann2024thevastlandscape pages 4-5) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Causal relation is strong, but exact enzyme used varies by taxon. |
| Ferredoxin:NAD+ oxidoreductase — transfers electrons from — reduced ferredoxin to NAD+ | enzyme → cofactors | EC:1.18.1.3; CHEBI:NAD+ candidate; CHEBI:23357 ferredoxin | “ferredoxin—NAD+ reductase… transfers electrons from reduced ferredoxin to NAD+” (hackmann2024thevastlandscape pages 4-5) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Strong redox-balancing edge. |
| Flavin-based electron bifurcation — couples — exergonic and endergonic redox reactions | process → process | candidate GO electron bifurcation; flavin cofactor candidate CHEBI:FAD/FMNs | “couples an exergonic and an endergonic redox reaction within a single soluble enzyme complex” (kumar2023moleculararchitectureand pages 1-2) | 10.1038/s41467-023-41212-x, 2023, https://doi.org/10.1038/s41467-023-41212-x | Strong mechanistic concept edge. |
| Flavin-based electron bifurcation — reduces — low-potential ferredoxin | process → electron carrier | CHEBI:23357 ferredoxin | “typically including low-potential ferredoxin” (kumar2023moleculararchitectureand pages 1-2, britton2024thernfcomplex pages 27-31) | 10.1038/s41467-023-41212-x, 2023, https://doi.org/10.1038/s41467-023-41212-x | Strong; central to anaerobic redox economy. |
| Butyryl-CoA dehydrogenase/EtfAB — bifurcates electrons from — NADH to crotonyl-CoA and ferredoxin | enzyme complex → metabolites/cofactors | EC:1.3.8.1; CHEBI:NADH candidate; CHEBI:crotonyl-CoA candidate; CHEBI:23357 ferredoxin | “EtfAB paired with Bcd catalyzes bifurcation of electrons from NADH… reduce crotonyl-CoA and ferredoxin” (britton2024thernfcomplex pages 39-42, britton2024thernfcomplex pages 31-35) | Britton 2024 Rnf complex excerpt | Strong, but source is excerpt-derived rather than full citable DOI in context. Curate with note. |
| Nfn/Stn transhydrogenase — connects — NAD(H) and NADP(H) pools for redox balancing | enzyme complex → cofactors/process | EC:1.6.1.4 (Nfn); Stn family candidate | “anaerobes… use FBEB transhydrogenases (e.g., Nfn, Stn) to connect NAD(H) and NADP(H) pools for redox balancing” (kumar2023moleculararchitectureand pages 1-2) | 10.1038/s41467-023-41212-x, 2023, https://doi.org/10.1038/s41467-023-41212-x | Strong for specific enzyme families; not universal to all fermenters. |
| Rnf complex — oxidizes — reduced ferredoxin while reducing NAD+ | complex → cofactors | EC:7.2.1.2; CHEBI:23357 ferredoxin; CHEBI:NAD+ candidate | “Rnf accepts Fd2- and couples ferredoxin oxidation to NAD+ reduction” (britton2024thernfcomplex pages 31-35) | Britton 2024 Rnf complex excerpt | Strong mechanistic edge; excerpt source. |
| Rnf complex — pumps — ions to generate ion-motive force | complex → process | EC:7.2.1.2; CHEBI:Na+ candidate; CHEBI:H+ candidate | “while pumping ions (H+/Na+), generating an ion-motive force” (britton2024thernfcomplex pages 31-35); “Rnf… expel ions (Na+)” (hackmann2024thevastlandscape pages 5-6) | Britton 2024 excerpt; 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Strong, but ion specificity can vary by organism. |
| Ion-motive force — drives — ATP synthase-mediated ATP formation | process → enzyme/process | EC:7.2.2.1; EC:7.1.2.2; GO:0015986 ATP synthesis coupled proton transport candidate | “generating ion gradients that drive ATP synthesis via two different ATP synthases” (hackmann2024thevastlandscape pages 5-6) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Strong; links fermentation to chemiosmotic ATP conservation. |
| Ech hydrogenase — couples — ferredoxin oxidation to H2 production and ion translocation | complex → metabolite/process | EC:7.1.1.-; CHEBI:23357 ferredoxin; CHEBI:18276 hydrogen molecular entity | “Ech… oxidizes ferredoxin to produce H2 while translocating cations” (britton2024thernfcomplex pages 27-31) | Britton 2024 Rnf complex excerpt | Strong general mechanistic edge; excerpt source. |
| Rnf/Ech complexes — increase — ATP yield in some fermentations | complexes → phenotype | EC:7.2.1.2; EC:7.1.1.- | “Rnf and Ech complexes increase ATP yield (up to ~50% during butyrate formation)” (hackmann2024thevastlandscape pages 7-9) | 10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 | Quantitative but pathway/taxon-dependent; mark moderate confidence. |
| High H2 partial pressure — shifts fermentation toward — butyrate/lactate/formate over acetate/H2/CO2 | environmental factor → product profile | CHEBI:18276 hydrogen molecular entity; CHEBI:17968 butyrate; CHEBI:24996 lactate; CHEBI:15740 formate; CHEBI:30089 acetate | “high H2 favors formation of butyrate, lactate, and formate over acetate, H2, and CO2” (campbell2023h2generatedby pages 1-2) | 10.1186/s40168-023-01565-3, 2023, https://doi.org/10.1186/s40168-023-01565-3 | Strong for gut butyrogens; taxon-specific. |
| H2-consuming methanogen activity — decreases — butyrate production in synthetic gut communities | community member/process → metabolite output | NCBITaxon:Methanobrevibacter smithii candidate; CHEBI:17968 butyrate | “addition of the H2-consuming methanogen… lowered H2 and decreased butyrate production” (campbell2023h2generatedby pages 1-2) | 10.1186/s40168-023-01565-3, 2023, https://doi.org/10.1186/s40168-023-01565-3 | Strong but community-context specific; useful environmental edge rather than core universal trait edge. |
| Low H2 partial pressure (<60 Pa) — enables — NADH-derived fermentative H2 formation | environmental factor → process | CHEBI:18276 hydrogen molecular entity; candidate GO hydrogen production | “NADH-derived H2 formation requires very low H2 partial pressure (‘less than 60 Pa’)” (taggar2024hydrogenproductionvia pages 5-7) | 10.35812/cellulosechemtechnol.2024.58.90, 2024, https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Strong for dark-fermentation hydrogen branch; not all fermentation types. |
| Oxygen presence — inhibits — fermentative H2 production | environmental factor → process | CHEBI:15379 dioxygen; candidate GO hydrogen production | “The presence of oxygen prevents the generation of hydrogen” (taggar2024hydrogenproductionvia pages 5-7) | 10.35812/cellulosechemtechnol.2024.58.90, 2024, https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Strong branch-specific edge; also helps define anaerobic scope. |
| External electron sink (glycine betaine + CO2 or caffeate) — restores growth of — A. woodii redox-impaired mutant | environmental factor → phenotype | candidate CHEBI:glycine betaine; CHEBI:16526 carbon dioxide; candidate CHEBI:caffeate | “growth was restored by addition of an external electron sink, glycine betaine + CO2 or caffeate” (moon2023anewmetabolic pages 1-2) | 10.1111/1758-2229.13160, 2023, https://doi.org/10.1111/1758-2229.13160 | Taxon-specific; useful as external electron sink edge case, not universal fermentation rule. |
| Cathode electron uptake — coupled with nitrate reduction — reroutes glucose fermentation in Lactiplantibacillus plantarum | external factor/process → process | candidate cathode node; CHEBI:nitrate candidate; CHEBI:15361 pyruvate; GO:0006113 fermentation | “couple that oxidation to reduction of… pyruvate and… nitrate” and “reroutes glucose fermentation” (tejedorsanz2023extracellularelectronuptake pages 1-2) | 10.3389/fmicb.2023.1298023, 2023, https://doi.org/10.3389/fmicb.2023.1298023 | Important boundary/edge-case; should likely be marked non-core or conditional. |
| Nitrate availability during cathodic EET — increases — current consumption and nitrate reduction rate | environmental factor → phenotype/process | CHEBI:nitrate candidate | “maximum current consumption… with nitrate” and “8.98 ± 2.29 mM/day with EET vs 1.19 ± 1.16 mM/day under open-circuit” (tejedorsanz2023extracellularelectronuptake pages 2-3) | 10.3389/fmicb.2023.1298023, 2023, https://doi.org/10.3389/fmicb.2023.1298023 | Quantitative edge case; more electrorespiratory than core fermentation. |
| Ethanol oxidation + reverse β-oxidation — enables — ethanol-to-hexanoate chain elongation without external acetate | pathway coupling → product formation | reverse β-oxidation candidate; CHEBI:16236 ethanol; CHEBI:hexanoate candidate | “3 ethanol → hexanoate + H+ + 2 H2 + H2O” (allaart2023physiologicalandstoichiometric pages 2-3) | 10.1038/s41598-023-43682-x, 2023, https://doi.org/10.1038/s41598-023-43682-x | Strong for chain elongation subtrait; useful optional branch node set. |
| Ethanol-only chain elongation — conserves energy via — substrate-level phosphorylation | pathway → process | candidate reverse β-oxidation node; GO ATP generation candidate | “Energy conservation is reported to occur via substrate-level phosphorylation rather than… Rnf” (allaart2023physiologicalandstoichiometric pages 2-3) | 10.1038/s41598-023-43682-x, 2023, https://doi.org/10.1038/s41598-023-43682-x | Strong but specific to described condition. |
| Fermentative glucose metabolism in A. woodii mutant — induces — mixed-acid fermentation enzymes | substrate/process → pathway induction | candidate mixed-acid fermentation node | “growth on fructose alone induced enzymes for mixed acid fermentation (MAF)” (moon2023anewmetabolic pages 1-2) | 10.1111/1758-2229.13160, 2023, https://doi.org/10.1111/1758-2229.13160 | Taxon- and genotype-specific; not universal. |
| Hydrogenogenic fermentation — converts — fructose to acetate + H2 in A. woodii under external acceptor pre-growth | substrate/process → products | CHEBI:15824 fructose; CHEBI:30089 acetate; CHEBI:18276 hydrogen molecular entity | “fermented fructose to two acetate and four hydrogen” (moon2023anewmetabolic pages 1-2) | 10.1111/1758-2229.13160, 2023, https://doi.org/10.1111/1758-2229.13160 | Specific phenotype in mutant/condition; useful as branch example. |


*Table: This table lists evidence-backed subject–predicate–object edges for curating a TraitMech causal graph of microbial fermentation. It emphasizes scope boundaries, central redox and ATP-conservation mechanisms, environmental modulators, and important edge cases that may need uncertainty flags.*

---

## Warnings / claims that should not yet be curated as strong universal edges
1. **“No external electron acceptor” is not absolute.** Some fermentations use protons (→H2) and secondary fermentations can use H2/CO2, blurring boundaries; handle as curator-defined edge cases. (hackmann2024thevastlandscape pages 2-3)
2. **Rnf/Ech prevalence and directionality are taxon- and condition-dependent.** Reviews note that Rnf is sometimes inferred from genomes without biochemical validation; treat presence→function edges as uncertain unless supported in the specific taxon. (hackmann2024thevastlandscape pages 7-9)
3. **Electrofermentation/EET in fermenters is conditional.** Cathode uptake required nitrate and specific potentials in L. plantarum; curate as conditional on external acceptor/electrode settings. (tejedorsanz2023extracellularelectronuptake pages 2-3, tejedorsanz2023extracellularelectronuptake pages 1-2)
4. **Excerpt-only evidence:** some detailed electron-bifurcation/Rnf mechanism statements are from an extracted text chunk without a clearly provided DOI in this workspace; curate those edges with “needs primary DOI confirmation” unless you can retrieve/verify the exact publication metadata in your curation workflow. (britton2024thernfcomplex pages 27-31, britton2024thernfcomplex pages 39-42, britton2024thernfcomplex pages 31-35)

---

## DOI-first bibliography (with dates/URLs where available)
1. Hackmann TJ. *The vast landscape of carbohydrate fermentation in prokaryotes.* **FEMS Microbiology Reviews** (May 2024). https://doi.org/10.1093/femsre/fuae016 (hackmann2024thevastlandscape pages 1-2)
2. Campbell A, Gdanetz K, Schmidt AW, Schmidt TM. *H2 generated by fermentation in the human gut microbiome influences metabolism and competitive fitness of gut butyrate producers.* **Microbiome** (Jun 2023). https://doi.org/10.1186/s40168-023-01565-3 (campbell2023h2generatedby pages 1-2)
3. Tejedor-Sanz S, Li S, Kundu BB, Ajo-Franklin CM. *Extracellular electron uptake from a cathode by the lactic acid bacterium Lactiplantibacillus plantarum.* **Frontiers in Microbiology** (Nov 2023). https://doi.org/10.3389/fmicb.2023.1298023 (tejedorsanz2023extracellularelectronuptake pages 1-2)
4. Taggar MS, Kaur A, Jain C, Kalia A, Sooch SS. *Hydrogen production via dark fermentation: A review of influential factors.* **Cellulose Chemistry and Technology** (Nov 2024). https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 (taggar2024hydrogenproductionvia pages 5-7)
5. Kumar A, Kremp F, Roth J, et al. *Molecular architecture and electron transfer pathway of the Stn family transhydrogenase.* **Nature Communications** (Sep 2023). https://doi.org/10.1038/s41467-023-41212-x (kumar2023moleculararchitectureand pages 1-2)
6. Allaart MTT, Fox BB, Nettersheim IHMS, et al. *Physiological and stoichiometric characterization of ethanol-based chain elongation in the absence of short-chain carboxylic acids.* **Scientific Reports** (Oct 2023). https://doi.org/10.1038/s41598-023-43682-x (allaart2023physiologicalandstoichiometric pages 2-3)
7. Moon J, Schubert A, Poehlein A, Daniel R, Müller V. *A new metabolic trait in an acetogen: Mixed acid fermentation of fructose in a methylene-tetrahydrofolate reductase mutant of Acetobacterium woodii.* **Environmental Microbiology Reports** (May 2023). https://doi.org/10.1111/1758-2229.13160 (moon2023anewmetabolic pages 1-2)
8. Davin ME, Thompson RA, Giannone RJ, et al. *Clostridium autoethanogenum alters cofactor synthesis, redox metabolism, and lysine-acetylation in response to elevated H2:CO feedstock ratios for enhancing carbon capture efficiency.* **Biotechnology for Biofuels and Bioproducts** (Sep 2024). https://doi.org/10.1186/s13068-024-02554-w (davin2024clostridiumautoethanogenumalters pages 7-8)

References

1. (hackmann2024thevastlandscape pages 1-2): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

2. (hackmann2024thevastlandscape pages 2-3): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

3. (hackmann2024thevastlandscape pages 5-6): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

4. (moon2023anewmetabolic pages 1-2): Jimyung Moon, Anja Schubert, Anja Poehlein, Rolf Daniel, and Volker Müller. A new metabolic trait in an acetogen: mixed acid fermentation of fructose in a methylene‐tetrahydrofolate reductase mutant of acetobacterium woodii. Environmental Microbiology Reports, 15:339-351, May 2023. URL: https://doi.org/10.1111/1758-2229.13160, doi:10.1111/1758-2229.13160. This article has 7 citations and is from a peer-reviewed journal.

5. (taggar2024hydrogenproductionvia pages 5-7): Monica SACHDEVA TAGGAR, Amanpreet Kaur, Chahak Jain, Anu Kalia, and Sarbjit SINGH SOOCH. Hydrogen production via dark fermentation: a review of influential factors. Cellulose Chemistry and Technology, 58:1051-1063, Nov 2024. URL: https://doi.org/10.35812/cellulosechemtechnol.2024.58.90, doi:10.35812/cellulosechemtechnol.2024.58.90. This article has 11 citations and is from a peer-reviewed journal.

6. (tejedorsanz2023extracellularelectronuptake pages 2-3): Sara Tejedor-Sanz, Siliang Li, Biki Bapi Kundu, and Caroline M. Ajo-Franklin. Extracellular electron uptake from a cathode by the lactic acid bacterium lactiplantibacillus plantarum. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1298023, doi:10.3389/fmicb.2023.1298023. This article has 20 citations and is from a peer-reviewed journal.

7. (tejedorsanz2023extracellularelectronuptake pages 1-2): Sara Tejedor-Sanz, Siliang Li, Biki Bapi Kundu, and Caroline M. Ajo-Franklin. Extracellular electron uptake from a cathode by the lactic acid bacterium lactiplantibacillus plantarum. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1298023, doi:10.3389/fmicb.2023.1298023. This article has 20 citations and is from a peer-reviewed journal.

8. (hackmann2024thevastlandscape media ac3846af): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

9. (hackmann2024thevastlandscape media 15f20e7e): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

10. (kumar2023moleculararchitectureand pages 1-2): Anuj Kumar, Florian Kremp, Jennifer Roth, Sven A. Freibert, Volker Müller, and Jan M. Schuller. Molecular architecture and electron transfer pathway of the stn family transhydrogenase. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41212-x, doi:10.1038/s41467-023-41212-x. This article has 22 citations and is from a highest quality peer-reviewed journal.

11. (hackmann2024thevastlandscape pages 7-9): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

12. (campbell2023h2generatedby pages 1-2): Austin Campbell, Kristi Gdanetz, Alexander W. Schmidt, and Thomas M. Schmidt. H2 generated by fermentation in the human gut microbiome influences metabolism and competitive fitness of gut butyrate producers. Microbiome, Jun 2023. URL: https://doi.org/10.1186/s40168-023-01565-3, doi:10.1186/s40168-023-01565-3. This article has 76 citations and is from a highest quality peer-reviewed journal.

13. (allaart2023physiologicalandstoichiometric pages 2-3): Maximilienne Toetie Allaart, Bartholomeus B. Fox, Ingo H. M. S. Nettersheim, Martin Pabst, Diana Z. Sousa, and Robbert Kleerebezem. Physiological and stoichiometric characterization of ethanol-based chain elongation in the absence of short-chain carboxylic acids. Scientific Reports, Oct 2023. URL: https://doi.org/10.1038/s41598-023-43682-x, doi:10.1038/s41598-023-43682-x. This article has 16 citations and is from a peer-reviewed journal.

14. (hackmann2024thevastlandscape pages 4-5): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

15. (hackmann2024thevastlandscape pages 10-11): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

16. (hackmann2024thevastlandscape pages 6-7): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

17. (hackmann2024thevastlandscape pages 11-12): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

18. (britton2024thernfcomplex pages 27-31): TA Britton. The rnf complex is vital for metabolic adaptation and virulence in the oral pathogen fusobacterium nucleatum. Unknown journal, 2024.

19. (britton2024thernfcomplex pages 39-42): TA Britton. The rnf complex is vital for metabolic adaptation and virulence in the oral pathogen fusobacterium nucleatum. Unknown journal, 2024.

20. (britton2024thernfcomplex pages 31-35): TA Britton. The rnf complex is vital for metabolic adaptation and virulence in the oral pathogen fusobacterium nucleatum. Unknown journal, 2024.

21. (davin2024clostridiumautoethanogenumalters pages 7-8): Megan E. Davin, R. Adam Thompson, Richard J. Giannone, Lucas W. Mendelson, Dana L. Carper, Madhavi Z. Martin, Michael E. Martin, Nancy L. Engle, Timothy J. Tschaplinski, Steven D. Brown, and Robert L. Hettich. Clostridium autoethanogenum alters cofactor synthesis, redox metabolism, and lysine-acetylation in response to elevated h2:co feedstock ratios for enhancing carbon capture efficiency. Biotechnology for Biofuels and Bioproducts, Sep 2024. URL: https://doi.org/10.1186/s13068-024-02554-w, doi:10.1186/s13068-024-02554-w. This article has 18 citations and is from a domain leading peer-reviewed journal.