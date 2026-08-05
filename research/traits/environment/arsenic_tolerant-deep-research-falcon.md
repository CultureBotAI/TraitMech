---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:08:09.130920'
end_time: '2026-08-04T00:14:22.848801'
duration_seconds: 373.72
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: arsenic tolerant
  trait_identifier: traitmech:000017
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: arsenic_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metalloid tolerance in which an organism grows in the presence of
    elevated arsenic (arsenite/arsenate) concentrations, typically via the ars operon,
    whose ArsB pump extrudes arsenite from the cytoplasm.
  parent_traits: traitmech:000012
  synonyms: arsenic resistant
  evidence_summary: 'DOI:10.3389/fmicb.2018.02473: ArsB is an integral membrane protein
    able to extrude arsenite from the cell cytoplasm, thus diminishing arsenite accumulation
    (Review supports the ars operon as a near-ubiquitous arsenic-resistance determinant,
    "more common than genes for tryptophan biosynthesis".) | DOI:10.3389/fmicb.2020.00047:
    C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+
    (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and
    Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates arsenite
    (As3+) to a MIC of 3.5 mM.)'
  causal_graph_summary: 'arsenic_tolerance_ars_efflux: 13 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 51
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** arsenic tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000017
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metalloid tolerance in which an organism grows in the presence of elevated arsenic (arsenite/arsenate) concentrations, typically via the ars operon, whose ArsB pump extrudes arsenite from the cytoplasm.
- **Parent traits:** traitmech:000012
- **Synonyms:** arsenic resistant
- **Existing evidence:** DOI:10.3389/fmicb.2018.02473: ArsB is an integral membrane protein able to extrude arsenite from the cell cytoplasm, thus diminishing arsenite accumulation (Review supports the ars operon as a near-ubiquitous arsenic-resistance determinant, "more common than genes for tryptophan biosynthesis".) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates arsenite (As3+) to a MIC of 3.5 mM.)
- **Existing causal graph summary:** arsenic_tolerance_ars_efflux: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **arsenic tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/arsenic_tolerant.yaml`.

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
- **Trait label:** arsenic tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000017
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metalloid tolerance in which an organism grows in the presence of elevated arsenic (arsenite/arsenate) concentrations, typically via the ars operon, whose ArsB pump extrudes arsenite from the cytoplasm.
- **Parent traits:** traitmech:000012
- **Synonyms:** arsenic resistant
- **Existing evidence:** DOI:10.3389/fmicb.2018.02473: ArsB is an integral membrane protein able to extrude arsenite from the cell cytoplasm, thus diminishing arsenite accumulation (Review supports the ars operon as a near-ubiquitous arsenic-resistance determinant, "more common than genes for tryptophan biosynthesis".) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates arsenite (As3+) to a MIC of 3.5 mM.)
- **Existing causal graph summary:** arsenic_tolerance_ars_efflux: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **arsenic tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/arsenic_tolerant.yaml`.

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


# Curation-focused research report: microbial arsenic tolerance

## Trait record and scope

- **Trait label:** arsenic tolerant
- **Trait identifier:** `traitmech:000017`
- **Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED
- **Parent:** `traitmech:000012`
- **Synonym:** arsenic resistant

### Recommended operational definition

`traitmech:000017` should represent **the capacity of a living microorganism to grow, maintain viability, or sustain measurable physiological activity at an explicitly elevated concentration of a specified arsenic species**, relative to an appropriate arsenic-free or arsenic-sensitive control. The canonical mechanism is intracellular detoxification by an **ars** system: As(V) is reduced by ArsC to As(III), and As(III) is exported by ArsB or Acr3; ArsA and ArsD can increase the capacity of ArsB-based efflux. The ars operon protects the cell but does not necessarily remove or detoxify arsenic in the surrounding environment. (william2023arsenicandmicroorganisms pages 4-6, dunivin2019aglobalsurvey pages 1-2, yan2019geneticmechanismsof pages 2-4)

The supplied definition is therefore substantially correct but too ArsB-specific. **Acr3 is a major alternative arsenite exporter**, and some organisms tolerate arsenic through methylation, oxidation, sequestration, or combinations of pathways. A revised definition could read:

> A metalloid-tolerance phenotype in which a microorganism grows or remains physiologically active at an elevated, assay-specified concentration of arsenite, arsenate, or an organoarsenical. Canonical inorganic-arsenic tolerance is mediated by ars-regulated cytoplasmic arsenate reduction and arsenite efflux through ArsB or Acr3, sometimes enhanced by ArsA and ArsD.

### Boundary cases

1. **Resistance versus arsenic metabolism.** The ars system is a cellular-protection system. AioAB/ArxAB oxidation and ArrAB respiratory reduction alter environmental arsenic speciation and may support energy metabolism, but they are not equivalent to tolerance. ArrAB-mediated use of As(V) as a terminal electron acceptor is best represented as an arsenotrophic respiration trait with a possible supporting edge to tolerance. (hoque2024arsenotrophicachromobacteraegrifaciens pages 1-2, rueangmongkolrat2024theroleof pages 1-2, dunivin2019aglobalsurvey pages 1-2)
2. **Gene presence versus phenotype.** Detection of `arsB`, `acr3`, or `arsC` predicts capacity but does not establish growth at elevated arsenic. Expression, functional genetics, or a growth/MIC/MTC assay is needed to assert the trait. A global analysis of 922 soil genomes and 38 metagenomes found arsenic-related genes common but not universal. (dunivin2019aglobalsurvey pages 1-2)
3. **Biosorption versus tolerance.** Binding arsenic to living or dead biomass can remove arsenic without demonstrating that cells tolerate it. Dead-cell sorption should be excluded from this trait.
4. **Bioaccumulation versus tolerance.** Intracellular accumulation can coexist with tolerance, but disabling Acr3 and arsenate reductase increased arsenic accumulation in engineered *Corynebacterium glutamicum* by 28–30-fold—illustrating that accumulation may increase when canonical tolerance functions are removed. (naiel2024thearsenicbioremediation pages 6-7)
5. **As(V), As(III), and organoarsenicals are separate assay dimensions.** Their uptake, toxicity, and detoxification differ. MTCs must not be pooled across species, media, pH, or exposure duration.
6. **“Arsenic removal” is not necessarily detoxification.** ArsC followed by efflux can protect the cell while releasing the generally more mobile As(III). Environmental remediation therefore often requires a second immobilization, oxidation, adsorption, or precipitation step. (dunivin2019aglobalsurvey pages 1-2, haghi2023arsenicpollutionand pages 1-2)

## Current mechanistic model

Environmental As(V), a phosphate analogue, enters incidentally through Pst or Pit phosphate-transport systems. Cytoplasmic ArsC reduces As(V) to As(III), using either glutaredoxin- or thioredoxin-dependent reducing systems. As(III) is then exported through ArsB or Acr3, lowering the intracellular arsenic burden. Environmental As(III) itself can enter through aquaglyceroporins such as GlpF. (yang2016newmechanismsof pages 1-2, preetha2023biotechnologyadvancesin pages 2-4, yan2019geneticmechanismsof pages 2-4)

ArsR is an As(III)-responsive repressor. As(III) binding causes ArsR to dissociate from the operator, permitting transcription of other ars genes. In extended `arsRDABC` systems, ArsD transfers As(III) to the ArsA ATPase; ArsA couples ATP hydrolysis to ArsB transport, increasing efflux effectiveness at lower intracellular As(III). (william2023arsenicandmicroorganisms pages 4-6, yan2019geneticmechanismsof pages 2-4)

Organoarsenical-defense modules broaden—but should not automatically replace—the core inorganic-arsenic graph. ArsM methylates As(III); ArsP exports MAs(III); ArsH oxidizes MAs(III) to less-toxic MAs(V); and ArsI cleaves carbon–arsenic bonds. Because trivalent methylarsenicals can be highly toxic, “methylation causes detoxification” is only valid when downstream export, oxidation, or volatilization is demonstrated. (li2016theorganoarsenicalbiocycle pages 1-3, garbinski2020bacterialmechanismsof pages 32-35, dunivin2019aglobalsurvey pages 1-2, yan2019geneticmechanismsof pages 2-4)

## Candidate nodes grouped by type

### Trait and assay nodes

- arsenic-tolerant growth — `traitmech:000017`
- growth in elevated arsenite
- growth in elevated arsenate
- growth in elevated organoarsenical
- minimum inhibitory concentration (MIC)
- maximum tolerated concentration (MTC)
- exposure duration, growth medium, pH, phosphate concentration, redox state, oxygen availability, temperature, and salinity

These experimental variables should be retained as evidence qualifiers rather than collapsed into the trait node.

### Chemicals and environmental factors

- arsenic; arsenite/As(III); arsenate/As(V)
- phosphate
- methylarsenite/MAs(III); methylarsenate/MAs(V)
- dimethylarsenite; trimethylarsine
- ATP, ADP, phosphate
- S-adenosyl-L-methionine
- glutaredoxin and thioredoxin reducing equivalents
- molecular oxygen for AioBA/ArsH-dependent oxidation
- iron oxide and sulfide as downstream arsenic-immobilization agents

**Grounding recommendation:** use ChEBI records only after checking the exact protonation and oxidation-state entity required by the YAML. Retain label-only nodes rather than assigning a generic arsenic CURIE to a specific oxyanion.

### Genes, proteins, and complexes

- `arsR` / ArsR — As(III)-responsive transcriptional repressor
- `arsC` / ArsC — cytoplasmic arsenate reductase; distinguish glutaredoxin- and thioredoxin-coupled families
- `arsB` / ArsB — membrane As(III)/Sb(III) exporter
- `acr3` / Acr3 — alternative As(III) exporter/H⁺ antiporter
- `arsA` / ArsA — As(III)-stimulated ATPase coupled to ArsB
- `arsD` / ArsD — As(III) metallochaperone delivering substrate to ArsA
- ArsAB efflux complex
- `pst` / Pst and `pit` / Pit — phosphate uptake systems
- `glpF` / GlpF — aquaglyceroporin capable of As(III) entry
- `arsM`, `arsP`, `arsH`, and `arsI` — organoarsenical-defense extension
- `aioA`/`aioB` and AioBA — arsenite oxidase; context-specific extension
- `arxA`/`arxB` and ArxAB — alternative arsenite oxidation/reduction module; not a default tolerance node
- `arrA`/`arrB` and ArrAB — respiratory arsenate reductase; boundary pathway

Gene/protein identifiers should be assigned at the taxon or protein-record level. A single UniProt CURIE cannot safely represent every ArsB, ArsC, or Acr3 ortholog.

### Cellular locations and functions

- cytoplasm — `GO:0005737`
- plasma membrane — `GO:0005886`
- transmembrane transporter activity — `GO:0022857`
- ATP hydrolysis activity — candidate parent `GO:0016887`
- transcriptional repression and metal-responsive regulation
- arsenate reduction, arsenite export, arsenite oxidation, arsenic methylation, and organoarsenical oxidation

Gene-specific GO terms and EC/Rhea reaction identifiers should be added only after confirming that the record distinguishes detoxification ArsC from respiratory ArrA and distinguishes ArsB from Acr3.

## Candidate causal edges

The following table separates high-confidence core edges from organoarsenical extensions and arsenotrophic boundary processes.

| subject | predicate | object | confidence/scope | DOI reference | short exact supporting snippet |
|---|---|---|---|---|---|
| environmental arsenate [As(V)] | enters through | phosphate transporters Pst/Pit | high; core uptake step for inorganic As(V) tolerance background | 10.1007/s00294-018-0894-9 | “it can be incidentally taken up by bacteria through phosphate transporters such as Pst and Pit” (yan2019geneticmechanismsof pages 2-4) |
| environmental arsenite [As(III)] | enters through | aquaglyceroporin GlpF / AQP family transporter | high; core uptake step for inorganic As(III) tolerance background | 10.1016/j.bj.2015.08.003 | “Arsenite enters via aquaglyceroporin (AQP) family transporters like GlpF” (yang2016newmechanismsof pages 1-2) |
| As(III) | binds and derepresses | ArsR, permitting ars operon transcription | high; core transcriptional control | 10.1007/s00294-018-0894-9 | “Binding of As(III) to ArsR is proposed to cause a conformational change… and dissociate it from the promoters… to permit the transcription” (yan2019geneticmechanismsof pages 2-4) |
| ArsC | reduces | As(V) to As(III) | high; core detoxification chemistry | 10.1007/s00294-018-0894-9 | “ArsC… is a small cytoplasmic arsenate reductase that catalyzes the transformation of inorganic As(V) to As(III)” (yan2019geneticmechanismsof pages 2-4) |
| glutaredoxin-coupled ArsC | uses electron donor | glutaredoxin | high; enzyme-family-specific | 10.1007/s00294-018-0894-9 | “ArsCec family (glutaredoxin-coupled ArsCs)… uses glutaredoxin as an electron source” (yan2019geneticmechanismsof pages 2-4) |
| thioredoxin-coupled ArsC | uses electron donor | thioredoxin | high; enzyme-family-specific | 10.1007/s00294-018-0894-9 | “ArsCsa family (thioredoxin-coupled ArsCs)… uses thioredoxin as an electron source” (yan2019geneticmechanismsof pages 2-4) |
| ArsB / Acr3 | exports | cytoplasmic As(III) | high; core tolerance efflux | 10.1186/s12915-019-0661-5 | “This operon includes arsenite efflux (ArsB, Acr3)” (dunivin2019aglobalsurvey pages 1-2) |
| ArsA ATP hydrolysis | energizes | ArsB-mediated As(III) efflux | high; core in ArsAB systems only | 10.1007/s00294-018-0894-9 | “ArsA is allosterically activated…”, and “the evolution of ArsA and ArsD enhanced the ability of ArsB to extrude As(III)” (yan2019geneticmechanismsof pages 2-4) |
| ArsD | transfers | As(III) to ArsA | high; core enhancer in ArsD/A-containing systems | 10.1007/s00294-018-0894-9 | “ArsD is to act as an As(III) metallochaperone that transfers As(III) to the metal-binding site of ArsA” (yan2019geneticmechanismsof pages 2-4) |
| ArsB-mediated arsenite extrusion | diminishes | arsenite accumulation in the cytoplasm | high; direct trait-supporting edge | 10.3389/fmicb.2018.02473 | “ArsB is an integral membrane protein able to extrude arsenite from the cell cytoplasm, thus diminishing arsenite accumulation” (fekih2018distributionofarsenic pages 3-4) |
| diminished intracellular arsenic burden | enables | arsenic growth/tolerance phenotype | medium; mechanistic inference from detoxification definition | 10.1186/s12915-019-0661-5 | “The ars operon protects the cell from arsenic” (dunivin2019aglobalsurvey pages 1-2) |
| ArsM | methylates | As(III) | high; organoarsenical extension, not universal core | 10.1007/s00294-018-0894-9 | “The methylation of As(III) is catalyzed by ArsM” (yan2019geneticmechanismsof pages 2-4) |
| ArsP | exports | MAs(III) | high; organoarsenical extension | 10.1039/c6mt00168h | “ArsP is an efflux system that confers resistance to MAs(III)” (li2016theorganoarsenicalbiocycle pages 1-3) |
| ArsH | oxidizes | MAs(III) to MAs(V) | high; organoarsenical extension | 10.1007/s00294-018-0894-9 | “MAs(III) can be oxidized to less-toxic MAs(V) by ArsH” (yan2019geneticmechanismsof pages 2-4) |
| AioBA | oxidizes | As(III) to As(V) | medium; taxon/context extension, metabolism not core ars tolerance | 10.7717/peerj.18383 | “The aio operon is composed of the aioA and aioB genes… encode the large and small subunits of arsenite oxidase” (rueangmongkolrat2024theroleof pages 1-2) |
| ArrAB | enables respiratory reduction of | As(V) coupled to growth | medium; not core tolerance, arsenotrophic metabolism boundary | 10.7717/peerj.18383 | “Various bacterial taxa have the ability to utilize arsenate as a final electron acceptor to support their growth” (rueangmongkolrat2024theroleof pages 1-2) |


*Table: This table compiles the strongest mechanistic causal edges for curating traitmech:000017, emphasizing core ars-based detoxification while separating organoarsenical extensions and arsenotrophic metabolism boundary cases.*

### Minimal recommended core graph

For a conservative successor to the existing 13-node/12-edge graph, the highest-confidence chain is:

1. elevated environmental As(V) → uptake through Pst/Pit → cytoplasmic As(V);
2. cytoplasmic As(V) → ArsC-dependent reduction → cytoplasmic As(III);
3. environmental As(III) → entry through GlpF-like aquaglyceroporins → cytoplasmic As(III);
4. cytoplasmic As(III) → binding to ArsR → ars-operon derepression;
5. cytoplasmic As(III) → ArsB- or Acr3-mediated export → extracellular As(III);
6. export → decreased intracellular As(III) burden → increased growth/survival under arsenic exposure. (yang2016newmechanismsof pages 1-2, dunivin2019aglobalsurvey pages 1-2, yan2019geneticmechanismsof pages 2-4)

ArsA and ArsD should be optional enhancing branches, not universal requirements. ArsM/P/H/I should form a separately labeled organoarsenical extension. AioBA and ArrAB should not be placed in the universal core.

## Recent developments and quantitative evidence

### 2023–2024 phenotype and environmental studies

- Six arsenic-resistant isolates from drying Urmia Salt Lake, assigned to *Shouchella*, *Salipaludibacillus*, and *Evansella*, reached reported MTCs of up to **320 mM As(V)** and **16 mM As(III)**. All contained `arsC`, whereas `arsB` was absent from three strains; `arrB` and `arxA` were not detected. This is useful evidence that As(V) and As(III) tolerance must be represented separately and that `arsC` presence does not imply a uniform exporter genotype. Published 30 June 2023; DOI: [10.3389/fenvs.2023.1195643](https://doi.org/10.3389/fenvs.2023.1195643). (haghi2023arsenicpollutionand pages 1-2)
- A 2024 agricultural-soil study found `arsC` most abundant among four focal arsenic genes, followed by `arsM`, `aioA`, and `arrA`, in soils containing **7.60–10.28 mg As/kg**. Arsenic-functional genes constituted only about **0.3%** of PICRUSt2-predicted genes, and their predicted abundance did not differ significantly between wet and dry seasons. The study supports community-level coexistence of detoxification and metabolism, but predictions from 16S profiles should not be curated as organism-level causal proof. Published 30 October 2024; DOI: [10.7717/peerj.18383](https://doi.org/10.7717/peerj.18383). (rueangmongkolrat2024theroleof pages 1-2, rueangmongkolrat2024theroleof pages 8-10)
- Two *Achromobacter aegrifaciens* isolates from Bangladeshi tubewell water and soil oxidized As(III) in a KMnO₄ assay and contained `aioA` and `arsB`; their genomes also carried predicted `aioBA`, `arsRCDAB`, and `arsHCsO` clusters. This is a useful taxon-specific example of combined oxidation and resistance, but most gene-cluster functions remain genomic predictions rather than individually validated edges. Published December 2024; DOI: [10.1186/s12866-024-03676-9](https://doi.org/10.1186/s12866-024-03676-9). (hoque2024arsenotrophicachromobacteraegrifaciens pages 1-2)
- The same study reports that approximately **75 million of 170 million people in Bangladesh** are exposed to drinking-water arsenic above **50 µg/L**, versus the WHO guideline of **10 µg/L**. These figures establish application relevance but are not nodes in the cellular causal graph. (hoque2024arsenotrophicachromobacteraegrifaciens pages 1-2)

### Distribution and evolution

A global survey examined **922 soil genomes and 38 metagenomes**. Arsenic genes were widespread but not universal; particular `acr3` sequence variants were geographically endemic, and `arsM` had a median metagenomic abundance of **48%** under that study’s gene-detection framework. These findings argue against making any single ars gene necessary for the trait and highlight horizontal transfer, ecological filtering, and functional redundancy. DOI: [10.1186/s12915-019-0661-5](https://doi.org/10.1186/s12915-019-0661-5), published May 2019. (dunivin2019aglobalsurvey pages 1-2)

Chromosomal, plasmid, transposon, and genomic-island locations are all documented for ars determinants. Redundant operons and later acquisition of ArsA/ArsD are associated with higher resistance in some taxa, but genomic redundancy alone is not proof of a quantitative phenotype. DOI: [10.3389/fmicb.2018.02473](https://doi.org/10.3389/fmicb.2018.02473), published October 2018. (fekih2018distributionofarsenic pages 3-4)

## Applications and real-world implementation

### Water and mine-drainage treatment

Current implementations typically use arsenic-tolerant organisms as catalysts for a separable treatment step rather than relying on tolerance alone. A 2023 review reports that sulfate-reducing consortia achieved **80% arsenic removal at pH 3.5** in acid mine drainage and approximately **90% total-arsenic removal over six months** through biogenic pyrite formation. Coarse-sand biofilters carrying As(III)-oxidizing microorganisms achieved up to **85% oxidation at 140 mL/min**, treating approximately **400 L/day** from water initially containing 100 µg/L arsenic. Coupling biological As(III) oxidation to electrocoagulation reportedly brought treated water to the WHO guideline of ≤10 µg/L. These are process-level outcomes, not direct measures of the TraitMech growth phenotype. DOI: [10.3390/microorganisms12010074](https://doi.org/10.3390/microorganisms12010074), published December 2023. (william2023arsenicandmicroorganisms pages 8-9, william2023arsenicandmicroorganisms pages 11-12)

### Biosorption and engineered accumulation

A 2024 review reports *Pseudomonas aeruginosa* biosorption of **90.72%** from an initial 10,000 ppb in 30 minutes and **97.92%** after two hours, although the residual concentrations—928 and 208 ppb—remained above drinking-water standards. Reported biomass capacities included **62.99 mg As(V)/g** for polyethylenimine-coated fermented *C. glutamicum* waste and **17.58–19.66 mg/g** for *Pseudomonas* and *Exiguobacterium*. These observations concern material performance and must not be converted directly into cellular tolerance edges. DOI: [10.1016/j.heliyon.2024.e36314](https://doi.org/10.1016/j.heliyon.2024.e36314), published September 2024. (naiel2024thearsenicbioremediation pages 6-7)

Synthetic-biology strategies include overexpressing `arsM` to increase methylation/volatilization and removing efflux or reduction functions to increase intracellular accumulation. These designs illustrate an engineering trade-off: **maximizing organismal tolerance and maximizing arsenic capture are often opposing objectives**. (naiel2024thearsenicbioremediation pages 6-7)

## Expert analysis and curation interpretation

The strongest consensus is that arsenic tolerance is a **modular phenotype**, not an arsB-only binary property. ArsB and Acr3 are functionally redundant at the graph level, ArsC families use different reducing systems, and ArsA/ArsD are optional capacity-enhancing components. Environmental surveys further show that arsenic genes are common but not universal and that sequence variants can be endemic. (fekih2018distributionofarsenic pages 3-4, dunivin2019aglobalsurvey pages 1-2, yan2019geneticmechanismsof pages 2-4)

The mechanistic graph should distinguish three levels of evidence:

- **High confidence:** purified-protein biochemistry, genetic complementation/knockout, direct transport measurements, or phenotype-linked expression.
- **Moderate confidence:** isolate genome plus a directly corresponding arsenic phenotype.
- **Uncertain:** metagenomic detection, 16S-based functional prediction, operon adjacency, or removal performance without evidence of cellular growth.

A second important interpretation is that cellular detoxification may worsen environmental mobility. ArsC converts As(V) to As(III) before efflux, while As(III) is generally more mobile and toxic. A bioremediation graph must therefore continue from extracellular As(III) to oxidation, adsorption to iron oxide, sulfide precipitation, or another capture process rather than treating efflux as environmental remediation. (dunivin2019aglobalsurvey pages 1-2, haghi2023arsenicpollutionand pages 1-2)

## Warnings: claims not ready for TraitMech curation

1. **Do not curate `arsB` as universally necessary.** Acr3 and other exporters provide alternatives.
2. **Do not infer tolerance from an ars gene alone.** Require phenotype or functional evidence.
3. **Do not equate MTC, MIC, growth yield, and removal percentage.** They are different measurements.
4. **Do not combine As(V) and As(III) thresholds.** Record arsenic species, salt, medium, pH, temperature, oxygen, inoculum, and exposure time.
5. **Do not encode AioBA or ArrAB as universal causes of tolerance.** AioBA may support detoxification in particular taxa; ArrAB principally supports respiration.
6. **Do not encode methylation as unconditionally detoxifying.** MAs(III) and other trivalent intermediates may be more toxic unless exported, oxidized, or volatilized.
7. **Do not use dead-biomass biosorption as evidence for a living-cell tolerance trait.**
8. **Do not generalize a gene-cluster prediction from the two *A. aegrifaciens* genomes to the species or genus.** (hoque2024arsenotrophicachromobacteraegrifaciens pages 1-2)
9. **Treat the soil “cooperative detoxification” model as a community-level hypothesis.** Much of the taxonomic assignment was based on uncultured sequences or functional prediction. (rueangmongkolrat2024theroleof pages 1-2, rueangmongkolrat2024theroleof pages 8-10)
10. **Validate ontology mappings before YAML insertion.** Exact ChEBI protonation states, gene-specific GO terms, EC reactions, and UniProt accessions are organism- and reaction-dependent.

## DOI-first bibliography

1. Rueangmongkolrat N, et al. “The role of microbiomes in cooperative detoxification mechanisms of arsenate reduction and arsenic methylation in surface agricultural soil.” *PeerJ* 12:e18383. Published 30 October 2024. DOI: [10.7717/peerj.18383](https://doi.org/10.7717/peerj.18383). (rueangmongkolrat2024theroleof pages 1-2)
2. Hoque MN, et al. “Arsenotrophic *Achromobacter aegrifaciens* strains isolated from arsenic contaminated tubewell water and soil sources shared similar genomic potentials.” *BMC Microbiology* 24:518. Published December 2024. DOI: [10.1186/s12866-024-03676-9](https://doi.org/10.1186/s12866-024-03676-9). (hoque2024arsenotrophicachromobacteraegrifaciens pages 1-2)
3. Naiel MAE, et al. “The arsenic bioremediation using genetically engineered microbial strains on aquatic environments: An updated overview.” *Heliyon* 10:e36314. Published September 2024. DOI: [10.1016/j.heliyon.2024.e36314](https://doi.org/10.1016/j.heliyon.2024.e36314). (naiel2024thearsenicbioremediation pages 6-7)
4. William VU, Magpantay HD. “Arsenic and Microorganisms: Genes, Molecular Mechanisms, and Recent Advances in Microbial Arsenic Bioremediation.” *Microorganisms* 12:74. Published December 2023. DOI: [10.3390/microorganisms12010074](https://doi.org/10.3390/microorganisms12010074). (william2023arsenicandmicroorganisms pages 8-9, william2023arsenicandmicroorganisms pages 11-12)
5. Haghi M, et al. “Arsenic pollution and arsenic-resistant bacteria of drying Urmia Salt Lake.” *Frontiers in Environmental Science* 11:1195643. Published 30 June 2023. DOI: [10.3389/fenvs.2023.1195643](https://doi.org/10.3389/fenvs.2023.1195643). (haghi2023arsenicpollutionand pages 1-2)
6. Preetha JSY, et al. “Biotechnology Advances in Bioremediation of Arsenic: A Review.” *Molecules* 28:1474. Published February 2023. DOI: [10.3390/molecules28031474](https://doi.org/10.3390/molecules28031474). (preetha2023biotechnologyadvancesin pages 2-4)
7. Yan G, et al. “Genetic mechanisms of arsenic detoxification and metabolism in bacteria.” *Current Genetics* 65:329–338. Published 2019. DOI: [10.1007/s00294-018-0894-9](https://doi.org/10.1007/s00294-018-0894-9). (yan2019geneticmechanismsof pages 2-4)
8. Dunivin TK, Yeh SY, Shade A. “A global survey of arsenic-related genes in soil microbiomes.” *BMC Biology* 17:45. Published May 2019. DOI: [10.1186/s12915-019-0661-5](https://doi.org/10.1186/s12915-019-0661-5). (dunivin2019aglobalsurvey pages 1-2)
9. Ben Fekih I, et al. “Distribution of Arsenic Resistance Genes in Prokaryotes.” *Frontiers in Microbiology* 9:2473. Published October 2018. DOI: [10.3389/fmicb.2018.02473](https://doi.org/10.3389/fmicb.2018.02473). (fekih2018distributionofarsenic pages 3-4)
10. Li J, Pawitwar SS, Rosen BP. “The organoarsenical biocycle and the primordial antibiotic methylarsenite.” *Metallomics* 8:1047–1055. Published October 2016. DOI: [10.1039/C6MT00168H](https://doi.org/10.1039/C6MT00168H). (li2016theorganoarsenicalbiocycle pages 1-3)
11. Yang H-C, Rosen BP. “New mechanisms of bacterial arsenic resistance.” *Biomedical Journal* 39:5–13. Published February 2016. DOI: [10.1016/j.bj.2015.08.003](https://doi.org/10.1016/j.bj.2015.08.003). (yang2016newmechanismsof pages 1-2)

References

1. (william2023arsenicandmicroorganisms pages 4-6): Vladimir U. William and Hilbert D. Magpantay. Arsenic and microorganisms: genes, molecular mechanisms, and recent advances in microbial arsenic bioremediation. Microorganisms, 12:74, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010074, doi:10.3390/microorganisms12010074. This article has 59 citations.

2. (dunivin2019aglobalsurvey pages 1-2): Taylor K. Dunivin, Susanna Y. Yeh, and Ashley Shade. A global survey of arsenic-related genes in soil microbiomes. BMC Biology, May 2019. URL: https://doi.org/10.1186/s12915-019-0661-5, doi:10.1186/s12915-019-0661-5. This article has 131 citations and is from a domain leading peer-reviewed journal.

3. (yan2019geneticmechanismsof pages 2-4): Ge Yan, Xingxiang Chen, Shiming Du, Zixin Deng, Lianrong Wang, and Shi Chen. Genetic mechanisms of arsenic detoxification and metabolism in bacteria. Current Genetics, 65:329-338, Oct 2019. URL: https://doi.org/10.1007/s00294-018-0894-9, doi:10.1007/s00294-018-0894-9. This article has 142 citations and is from a peer-reviewed journal.

4. (hoque2024arsenotrophicachromobacteraegrifaciens pages 1-2): M. Nazmul Hoque, Ayman Bin Abdul Mannan, Anamica Hossian, Golam Mahbub Faisal, M. Anwar Hossain, and Munawar Sultana. Arsenotrophic achromobacter aegrifaciens strains isolated from arsenic contaminated tubewell water and soil sources shared similar genomic potentials. BMC Microbiology, Dec 2024. URL: https://doi.org/10.1186/s12866-024-03676-9, doi:10.1186/s12866-024-03676-9. This article has 9 citations and is from a peer-reviewed journal.

5. (rueangmongkolrat2024theroleof pages 1-2): Nattanan Rueangmongkolrat, Pichahpuk Uthaipaisanwong, Kanthida Kusonmano, Sasipa Pruksangkul, and Prinpida Sonthiphand. The role of microbiomes in cooperative detoxification mechanisms of arsenate reduction and arsenic methylation in surface agricultural soil. PeerJ, 12:e18383, Oct 2024. URL: https://doi.org/10.7717/peerj.18383, doi:10.7717/peerj.18383. This article has 3 citations and is from a peer-reviewed journal.

6. (naiel2024thearsenicbioremediation pages 6-7): Mohammed A.E. Naiel, Ehab S. Taher, Fatema Rashed, Shakira Ghazanfar, Abdelrazeq M. Shehata, Nourelhuda A. Mohammed, Raul Pascalau, Laura Smuleac, Ateya Megahed Ibrahim, Ahmed Abdeen, and Mustafa Shukry. The arsenic bioremediation using genetically engineered microbial strains on aquatic environments: an updated overview. Sep 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e36314, doi:10.1016/j.heliyon.2024.e36314. This article has 24 citations.

7. (haghi2023arsenicpollutionand pages 1-2): Morteza Haghi, Salar H. Diznabi, Ismail Karaboz, and Esra Ersoy Omeroglu. Arsenic pollution and arsenic-resistant bacteria of drying urmia salt lake. Frontiers in Environmental Science, Jun 2023. URL: https://doi.org/10.3389/fenvs.2023.1195643, doi:10.3389/fenvs.2023.1195643. This article has 10 citations and is from a peer-reviewed journal.

8. (yang2016newmechanismsof pages 1-2): Hung-Chi Yang and Barry P. Rosen. New mechanisms of bacterial arsenic resistance. Biomedical Journal, 39:5-13, Feb 2016. URL: https://doi.org/10.1016/j.bj.2015.08.003, doi:10.1016/j.bj.2015.08.003. This article has 240 citations.

9. (preetha2023biotechnologyadvancesin pages 2-4): Jaganathan Sakthi Yazhini Preetha, Muthukrishnan Arun, Nandakumar Vidya, Kumaresan Kowsalya, Jayachandran Halka, and Gabrijel Ondrasek. Biotechnology advances in bioremediation of arsenic: a review. Molecules, 28:1474, Feb 2023. URL: https://doi.org/10.3390/molecules28031474, doi:10.3390/molecules28031474. This article has 65 citations.

10. (li2016theorganoarsenicalbiocycle pages 1-3): Jiaojiao Li, Shashank S. Pawitwar, and Barry P. Rosen. The organoarsenical biocycle and the primordial antibiotic methylarsenite. Metallomics : integrated biometal science, 8 10:1047-1055, Oct 2016. URL: https://doi.org/10.1039/c6mt00168h, doi:10.1039/c6mt00168h. This article has 82 citations.

11. (garbinski2020bacterialmechanismsof pages 32-35): Luis D. Garbinski. Bacterial mechanisms of toxicity and resistance to organoarsenicals. ArXiv, 2020. URL: https://doi.org/10.25148/etd.fidc009238, doi:10.25148/etd.fidc009238. This article has 0 citations.

12. (fekih2018distributionofarsenic pages 3-4): Ibtissem Ben Fekih, Chengkang Zhang, Yuan Ping Li, Yi Zhao, Hend A. Alwathnani, Quaiser Saquib, Christopher Rensing, and Carlos Cervantes. Distribution of arsenic resistance genes in prokaryotes. Frontiers in Microbiology, Oct 2018. URL: https://doi.org/10.3389/fmicb.2018.02473, doi:10.3389/fmicb.2018.02473. This article has 373 citations and is from a peer-reviewed journal.

13. (rueangmongkolrat2024theroleof pages 8-10): Nattanan Rueangmongkolrat, Pichahpuk Uthaipaisanwong, Kanthida Kusonmano, Sasipa Pruksangkul, and Prinpida Sonthiphand. The role of microbiomes in cooperative detoxification mechanisms of arsenate reduction and arsenic methylation in surface agricultural soil. PeerJ, 12:e18383, Oct 2024. URL: https://doi.org/10.7717/peerj.18383, doi:10.7717/peerj.18383. This article has 3 citations and is from a peer-reviewed journal.

14. (william2023arsenicandmicroorganisms pages 8-9): Vladimir U. William and Hilbert D. Magpantay. Arsenic and microorganisms: genes, molecular mechanisms, and recent advances in microbial arsenic bioremediation. Microorganisms, 12:74, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010074, doi:10.3390/microorganisms12010074. This article has 59 citations.

15. (william2023arsenicandmicroorganisms pages 11-12): Vladimir U. William and Hilbert D. Magpantay. Arsenic and microorganisms: genes, molecular mechanisms, and recent advances in microbial arsenic bioremediation. Microorganisms, 12:74, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010074, doi:10.3390/microorganisms12010074. This article has 59 citations.