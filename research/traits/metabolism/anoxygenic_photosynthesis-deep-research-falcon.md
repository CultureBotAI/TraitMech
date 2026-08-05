---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:32:01.235910'
end_time: '2026-08-04T05:39:29.297384'
duration_seconds: 448.06
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: anoxygenic photosynthesis
  trait_identifier: traitmech:000035
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: anoxygenic_photosynthesis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phototrophic metabolism that uses light energy with a single photosystem
    and bacteriochlorophyll, using electron donors other than water (e.g. H2S, H2,
    Fe(II), organics) and therefore not evolving oxygen. Characteristic of purple
    and green sulfur bacteria, Chloroflexi, and heliobacteria.
  parent_traits: traitmech:000038
  synonyms: bacterial photosynthesis
  evidence_summary: 'DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard describe anoxygenic
    photosynthesis across five prokaryotic phyla using bacteriochlorophyll and a single
    photosystem without O2 evolution.) | DOI:10.3389/fmicb.2024.1417714:  (Review
    of anoxygenic photosynthesis in green sulfur bacteria supports sulfide as electron
    donor and the absence of oxygen production.)'
  causal_graph_summary: 'anoxygenic_photosynthesis_sulfide_donor: 7 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** anoxygenic photosynthesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000035
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy with a single photosystem and bacteriochlorophyll, using electron donors other than water (e.g. H2S, H2, Fe(II), organics) and therefore not evolving oxygen. Characteristic of purple and green sulfur bacteria, Chloroflexi, and heliobacteria.
- **Parent traits:** traitmech:000038
- **Synonyms:** bacterial photosynthesis
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard describe anoxygenic photosynthesis across five prokaryotic phyla using bacteriochlorophyll and a single photosystem without O2 evolution.) | DOI:10.3389/fmicb.2024.1417714:  (Review of anoxygenic photosynthesis in green sulfur bacteria supports sulfide as electron donor and the absence of oxygen production.)
- **Existing causal graph summary:** anoxygenic_photosynthesis_sulfide_donor: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **anoxygenic photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anoxygenic_photosynthesis.yaml`.

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
- **Trait label:** anoxygenic photosynthesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000035
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy with a single photosystem and bacteriochlorophyll, using electron donors other than water (e.g. H2S, H2, Fe(II), organics) and therefore not evolving oxygen. Characteristic of purple and green sulfur bacteria, Chloroflexi, and heliobacteria.
- **Parent traits:** traitmech:000038
- **Synonyms:** bacterial photosynthesis
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard describe anoxygenic photosynthesis across five prokaryotic phyla using bacteriochlorophyll and a single photosystem without O2 evolution.) | DOI:10.3389/fmicb.2024.1417714:  (Review of anoxygenic photosynthesis in green sulfur bacteria supports sulfide as electron donor and the absence of oxygen production.)
- **Existing causal graph summary:** anoxygenic_photosynthesis_sulfide_donor: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **anoxygenic photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anoxygenic_photosynthesis.yaml`.

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


# Curation report: anoxygenic photosynthesis

## Trait record and scope

- **Trait label:** anoxygenic photosynthesis
- **Trait identifier:** `traitmech:000035`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `traitmech:000038`
- **Synonym:** bacterial photosynthesis

### Recommended scope definition

Anoxygenic photosynthesis is chlorophyll- or bacteriochlorophyll-based conversion of light energy through **one reaction-center system—Type I or Type II—without water oxidation and therefore without molecular-oxygen evolution**. The immediate conserved phenotype is photochemical energy conversion, not necessarily autotrophy. Depending on the organism, the resulting ATP and reductant support photoautotrophic CO₂ fixation or photoheterotrophic assimilation of organic carbon.

Phototrophic sulfur bacteria provide the clearest canonical implementation: they use one photosystem, cannot use water as the electron donor, and commonly use H₂S or other reduced compounds instead. Oxygen can suppress photosynthetic-pigment synthesis in these organisms, while illuminated anoxic water layers and sediments provide characteristic niches. (kushkevych2021anoxygenicphotosynthesisin pages 2-3, kushkevych2021anoxygenicphotosynthesisin pages 1-2)

### Boundaries and nearby traits

1. **Exclude oxygenic photosynthesis.** Two linked photosystems, water oxidation, the oxygen-evolving complex, and O₂ production define the neighboring oxygenic phenotype rather than this trait.
2. **Do not equate the trait with sulfur oxidation.** H₂S, S⁰, and thiosulfate are common donors, but H₂, Fe(II), and organic compounds can also supply electrons. Comparative physiology documents H₂S, S⁰, S₂O₃²⁻, Fe²⁺, and H₂ across different phototrophic lineages. (martin2018aphysiologicalperspective pages 2-3)
3. **Do not require CO₂ fixation.** Photoheterotrophic purple nonsulfur bacteria still perform anoxygenic photophosphorylation while using organic substrates as carbon and electron sources.
4. **Do not define the class as universally anaerobic.** Canonical green and purple sulfur phototrophy is associated with illuminated anoxic environments, but aerobic anoxygenic phototrophs use related Type II reaction centers under oxic conditions. Thus, “absence of O₂ evolution” is universal; “growth only under anoxia” is not.
5. **Treat photoferrotrophy as a subtype.** It couples light-driven energy metabolism and inorganic-carbon fixation to Fe(II) oxidation and occurs in only some purple and green sulfur bacteria. (martin2018aphysiologicalperspective pages 2-3)
6. **Treat chlorosomes as lineage-specific.** They occur in green sulfur bacteria and some Chloroflexota/Acidobacteria, not in all anoxygenic phototrophs.

## Current mechanistic understanding

### Core causal model

A defensible shared backbone is:

**light → antenna-pigment excitation → reaction-center charge separation → membrane electron transfer → proton-motive force → ATP synthesis → light-supported metabolism**.

This backbone then branches by reaction-center class and electron donor:

- **Type I branch:** represented by green sulfur bacteria, heliobacteria, and chloracidobacteria. The homodimeric core transfers electrons toward Fe–S acceptors and can generate strongly reducing equivalents.
- **Type II branch:** represented by purple bacteria and phototrophic Chloroflexota. Reaction-center photochemistry reduces quinone; quinol oxidation through cytochrome complexes supports cyclic electron transport and proton-motive-force formation.
- **Donor modules:** sulfur compounds via SQR/Fcc/Sox/Dsr-associated systems; H₂ via hydrogenases; Fe(II) via taxon-specific extracellular/periplasmic electron-transfer machinery; and organic donors in photoheterotrophs.
- **Assimilation modules:** reverse TCA in canonical green sulfur bacteria, Calvin–Benson–Bassham cycle in many purple bacteria, and 3-hydroxypropionate-related pathways in some Chloroflexota. These should be represented as optional taxon-specific consequences, not necessary parts of the trait.

The 2024 Type I structural synthesis gives unusually strong mechanistic resolution. In *Chlorobaculum tepidum*, a 2.5-Å cryo-EM structure places excitation transfer from chlorosomes through FMO to the PscA core; PscC donates electrons to the P840 bacteriochlorophyll special pair, and PscB contains the terminal FA/FB [4Fe–4S] clusters. In *Heliomicrobium modesticaldum*, a 2.2-Å structure supports direct A₀-to-FX transfer without a quinone intermediate. (niederman2024whatweare pages 1-2, niederman2024whatweare pages 5-7)

## Candidate nodes grouped by type

### Trait, pathways, and processes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| anoxygenic photosynthesis | `traitmech:000035` | Root trait node; retain identifier verbatim. |
| photosynthesis | `GO:0015979` | Broad parent process; too broad to substitute for the trait. |
| photosynthetic electron transport | `GO:0009767` | Broad GO term; annotate reaction-center/taxon context. |
| light harvesting | `GO:0009765` | Antenna-mediated excitation capture. |
| proton-motive-force generation | label only | Prefer a more exact ontology term only after identifier validation. |
| ATP synthesis coupled to proton transport | `GO:0015986` | Downstream bioenergetic process. |
| carbon fixation | `GO:0015977` | Optional output, not constitutive of all anoxygenic phototrophy. |
| reverse TCA cycle | label only | Canonical GSB assimilation branch. |
| Calvin–Benson–Bassham cycle | label only | Common purple-bacterial branch. |
| sulfur-compound oxidation | `GO:0019417` | Donor module, not synonymous with the root trait. |
| photoferrotrophy | label only | Fe(II)-dependent subtype. |
| photoheterotrophy | label only | Boundary-relevant implementation. |

### Environmental and experimental factors

| Candidate node | Suggested grounding | Role |
|---|---|---|
| light | `ENVO:01001852` candidate; validate locally | Required energy input. |
| anoxic environment | `ENVO:01000179` | Typical habitat/assay condition for sulfur phototrophs. |
| low-light condition | label only | Strongly favors chlorosome-bearing GSB. |
| oxygen | `CHEBI:15379` | Does not arise as product; often represses pigment-system synthesis in anaerobic phototrophs. |
| near-infrared radiation | label only | Absorbed by many bacteriochlorophyll antenna systems. |
| pyrite exposure | pyrite label; mineral identifier requires validation | Experimental donor condition in *A. vinosum*. |

### Chemicals, donors, products, and cofactors

| Candidate node | Suggested grounding | Role |
|---|---|---|
| hydrogen sulfide | `CHEBI:16136` | Major reduced-sulfur electron donor. |
| elemental sulfur | `CHEBI:33403` | Intermediate/product of sulfide oxidation. |
| thiosulfate | `CHEBI:26977` | Alternative sulfur donor. |
| sulfate | `CHEBI:16189` | Fully oxidized sulfur product. |
| dihydrogen | `CHEBI:18276` | Alternative electron donor. |
| iron(2+) | `CHEBI:29033` | Electron donor in photoferrotrophy. |
| carbon dioxide | `CHEBI:16526` | Carbon substrate in photoautotrophy. |
| ATP | `CHEBI:15422` | Energy-conservation product. |
| quinone / quinol pool | label only | Type II electron-transfer carrier; ground the specific quinone only where known. |
| bacteriochlorophyll a | label only | Principal pigment in many reaction centers and antennas. |
| bacteriochlorophyll c/d/e/g | label only | Lineage-specific antenna pigments. |
| [4Fe–4S] cluster | `CHEBI:49883` candidate; validate | Type I electron acceptor cofactor. |

### Genes, proteins, enzymes, and complexes

| Candidate node | Grounding strategy | Function / scope |
|---|---|---|
| `pufL`, `pufM` | gene symbols; taxon-specific UniProt entries | Type II reaction-center L/M core subunits. |
| `pufC` | gene symbol | RC-associated cytochrome subunit in some purple bacteria. |
| `pscA` / PscA | gene/protein symbol | Homodimeric Type I RC core in GSB. |
| `pshA` / PshA | gene/protein symbol | Homodimeric Type I RC core in heliobacteria. |
| `pscC` / cytochrome cZ | gene/protein symbol | Electron donor to the GSB P840 special pair. |
| `pscB` / PscB | gene/protein symbol | Houses FA and FB [4Fe–4S] clusters. |
| FMO protein | `GO:0009766` may describe primary antenna complex; verify applicability | Transfers chlorosome excitation to the RC in GSB. |
| chlorosome | `GO:0046930` candidate; validate | Very large antenna organelle/complex in selected lineages. |
| LH1 and LH2 | label only | Purple-bacterial light-harvesting complexes. |
| `bchX`, `bchY`, `bchZ` | gene symbols; EC grounding requires validation | Chlorophyllide reductase components in bacteriochlorophyll biosynthesis. |
| sulfide:quinone oxidoreductase, SQR | `EC:1.8.5.4` candidate; verify current EC | Oxidizes sulfide and reduces quinone. |
| flavocytochrome c sulfide dehydrogenase, FccAB | label/gene symbols | Periplasmic sulfide oxidation. |
| SoxYZ / Sox system | gene/protein symbols | Carrier/module for thiosulfate and sulfur oxidation. |
| reverse Dsr system | gene-family labels | Oxidation of stored sulfur to sulfite in many sulfur phototrophs. |
| cytochrome bc₁ complex | `GO:0005750` is mitochondrial and unsuitable for bacteria; use label or bacterial complex term | Quinol oxidation and proton translocation in Type II cycling. |
| F-type ATP synthase | `GO:0016469` | Uses proton motive force to synthesize ATP. |

### Cellular structures and localizations

- Intracytoplasmic photosynthetic membrane—purple bacteria.
- Cytoplasmic membrane—reaction-center and electron-transfer complexes.
- Chlorosome—peripheral antenna in GSB and selected other lineages.
- FMO baseplate/antenna interface—GSB-specific transfer module.
- Periplasm—FccAB and parts of sulfur oxidation in Gram-negative phototrophs.
- Cytoplasmic sulfur globule—intermediate sulfur storage in many purple sulfur bacteria; not universal.

## Prioritized candidate causal edges

The following table is the recommended initial evidence core. It deliberately separates broadly reusable bioenergetic edges from lineage- or experiment-specific branches.

| subject | predicate | object | scope/taxon | evidence snippet (brief exact/close wording) | DOI | confidence/caveat |
|---|---|---|---|---|---|---|
| light | excites | bacteriochlorophyll pigments | anoxygenic phototrophic sulfur bacteria | “bacteriochlorophylls (major photopigments in antenna and reaction centers)” and light-harvesting complexes/chlorosomes mediate capture of light energy (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | 10.3390/antiox10060829 | High for sulfur phototrophs; generalized wording, not a single molecular event assay |
| chlorosome | transfers excitation to | FMO protein | green sulfur bacteria (GSB) | “chlorosome-based light capture… energy transfer through FMO protein (808 nm absorption maximum) to reaction centers” (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | 10.3390/antiox10060829 | High; taxon-specific to GSB/chlorosome-bearing phototrophs |
| FMO trimer | transfers excitation to | PscA core antenna bacteriochlorophylls | GSB (*Chlorobaculum tepidum*) | “FMO antennae transfer excitations from chlorosomes to the PscA core”; “FMO BChl-3 molecules transfer excitons… to PscA antenna BChls” (niederman2024whatweare pages 1-2, niederman2024whatweare pages 7-9) | 10.3390/biom14030311 | High; structural inference from cryo-EM, taxon-specific |
| PscC (cytochrome cZ) | donates electrons to | P840 special pair (BChl a′) | GSB | “cytochrome cZ (PscC) donates electrons to the BChl a' special pair” (niederman2024whatweare pages 1-2) | 10.3390/biom14030311 | High; structural/mechanistic review, taxon-specific |
| PscA charge separation | enables electron transfer from | A0 to FX [4Fe-4S] | Type I homodimeric RCs; shown in GSB and heliobacteria | “electrons transferred directly from the A0… acceptor to FX [4Fe-4S]”; “A0 and FX positioned 18.1–18.2 Å apart, promoting direct electron transfer” (niederman2024whatweare pages 1-2, niederman2024whatweare pages 5-7) | 10.3390/biom14030311 | High; structural inference, mainly Type I RC phototrophs |
| PscB | houses | FA and FB [4Fe-4S] clusters | GSB; also noted for chloracidobacteria | “PscB houses [4Fe-4S] clusters FA and FB” (niederman2024whatweare pages 1-2, niederman2024whatweare pages 5-7) | 10.3390/biom14030311 | High; structural assignment, Type I RC-specific |
| H2S | is oxidized by | sulfide:quinone oxidoreductase (SQR) | GSB and PSB | “SQR catalyzes H₂S oxidation in both GSB and PSB” (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | 10.3390/antiox10060829 | High; sulfur phototroph-focused |
| SQR-mediated H2S oxidation | transfers electrons to | quinone / quinone-Rieske FeS-cytochrome b pathway | GSB and PSB | “transferring electrons via quinone-Rieske FeS protein-cytochrome b complexes into photosynthetic electron flux” (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | 10.3390/antiox10060829 | Moderate-high; wording compresses pathway components from review |
| reduced sulfur compounds | are oxidized to | elemental sulfur and/or sulfate | PSB and GSB / phototrophic sulfur bacteria | PSB “detoxify hydrogen sulfide by reoxidizing it to elemental sulfur (S0) and sulfate (SO4²−)”; GSB “oxidize H2S to elemental sulfur” (alarcon2024evidenceforautotrophic pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.1128/aem.00863-24; 10.3389/fmicb.2024.1417714 | High for sulfur-oxidizing phototrophs; product distribution is taxon/condition dependent |
| photosynthetic electron transport | generates | proton motive force | purple sulfur bacteria / Type II RC phototrophy | “quinone/quinol and cytochrome b/c complexes driving charge separation, PMF generation” (alarcon2024evidenceforautotrophic pages 1-2) | 10.1128/aem.00863-24 | Moderate-high; summarized from PSB physiology and pyrite paper context |
| proton motive force | drives | ATP synthesis | purple sulfur bacteria / Type II RC phototrophy | “PMF generation, and ATP synthase coupling” (alarcon2024evidenceforautotrophic pages 1-2) | 10.1128/aem.00863-24 | High; standard bioenergetic step but evidence here is review/contextual |
| O2 presence | suppresses | photosynthetic pigment synthesis | anoxygenic phototrophic sulfur bacteria | “depend on anoxic environments as O2 suppresses photosynthetic pigment synthesis”; “pigment synthesis is regulated by… oxygen presence” (kushkevych2021anoxygenicphotosynthesisin pages 2-3, kushkevych2021anoxygenicphotosynthesisin pages 3-5) | 10.3390/antiox10060829 | High; organism-level physiological effect, not necessarily absolute for all anoxygenic phototrophs |
| pyrite (FeS2) | supports | autotrophic growth | *Allochromatium vinosum* (PSB) | “demonstrating, for the first time, the autotrophic growth of purple sulfur bacteria using insoluble pyrite (FeS2) as both the electron and sulfur source” (alarcon2024evidenceforautotrophic pages 1-2) | 10.1128/aem.00863-24 | High; single-species experimental result, should be marked taxon-specific |
| pyrite exposure | induces upregulation of | c- and b-type cytochrome genes (~200-fold) | *Allochromatium vinosum* (PSB) | “Up to ~200-fold upregulation of genes encoding various c- and b-type cytochromes” (alarcon2024evidenceforautotrophic pages 1-2) | 10.1128/aem.00863-24 | High; transcriptomic evidence in pyrite vs sulfide comparison, condition-specific |
| reverse tricarboxylic acid cycle | fixes | CO2 | GSB | “The carbon source of GSB is carbon dioxide, which is assimilated through the reverse tricarboxylic acid cycle” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714 | High; taxon-specific to emphasized GSB examples |


*Table: This table compiles the strongest source-backed causal edges for curation of traitmech:000035 anoxygenic photosynthesis, emphasizing mechanistic entities, taxon scope, and caveats. It is useful as a compact starting point for TraitMech YAML graph construction and uncertainty marking.*

### Additional candidate triples for later branches

| Subject | Predicate | Object | Evidence and snippet | Curation status |
|---|---|---|---|---|
| bacteriochlorophyll | is required for | antenna and reaction-center photochemistry | Bacteriochlorophylls are described as the “major photopigments in antenna and reaction centers.” DOI: [10.3390/antiox10060829](https://doi.org/10.3390/antiox10060829), published May 2021. (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | **Strong**, but specify pigment subtype by lineage. |
| reduced sulfur compounds / H₂ / small organics | act as electron donors for | anoxygenic photosynthesis | The review states that sulfur phototrophs use reduced sulfur compounds, hydrogen, and small organic molecules rather than water. DOI: [10.3390/antiox10060829](https://doi.org/10.3390/antiox10060829), May 2021. (kushkevych2021anoxygenicphotosynthesisin pages 2-3) | **Strong as a disjunction**; do not assert every taxon uses every donor. |
| LH1 | transfers excitation to | Type II reaction center | Purple sulfur bacterial LH1 surrounds the reaction center and contains 16 αβ heterodimers and 32 BChl a molecules. (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | **Strong, purple-bacterial branch.** |
| `bchXYZ` | contributes to | bacteriochlorophyll biosynthesis | Comparative phylogeny identifies light-independent chlorophyllide reductase BchXYZ as common across sampled Type I and Type II anoxygenic phototrophs. | **Moderate for graph inclusion** because the retrieved evidence is phylogenetic rather than a perturbation experiment. |
| Fe(II) | donates electrons to | photoautotrophic carbon fixation | Comparative evidence identifies Fe²⁺ among electron donors used by selected anoxygenic phototrophs. (martin2018aphysiologicalperspective pages 2-3) | **Taxon-specific; uncertain mechanism node until organism-specific proteins are sourced.** |
| CO₂ | is fixed by | reverse TCA cycle | The 2024 review states that GSB assimilate CO₂ through reverse TCA. DOI: [10.3389/fmicb.2024.1417714](https://doi.org/10.3389/fmicb.2024.1417714), July 2024. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | **Strong, GSB branch only.** |

## Recent developments, applications, and data

### 1. Type I reaction-center structures clarified causal architecture

The 2024 structural review synthesizes 2.2–2.6 Å structures from heliobacteria, green sulfur bacteria, and chloracidobacteria. In the GSB complex, A₀ and FX are separated by approximately 18.1–18.2 Å, supporting direct electron transfer; FMO-to-PscA pigment gaps were reported as 21.5–27.0 Å, followed by shorter PscA-antenna-to-P840 distances. These measurements make the excitation-transfer and electron-transfer edges considerably stronger than annotation based only on gene co-occurrence. (niederman2024whatweare pages 1-2, niederman2024whatweare pages 5-7, niederman2024whatweare pages 7-9)

### 2. Pyrite was demonstrated as an electron and sulfur source

A July 2024 *Applied and Environmental Microbiology* study reported the first autotrophic growth of the purple sulfur bacterium *Allochromatium vinosum* with insoluble pyrite, FeS₂, serving as both electron and sulfur source. Pyrite-supported growth was slower than growth with sodium sulfide. Transcriptomics found **up to approximately 200-fold upregulation** of c- and b-type cytochrome genes, upregulation of periplasmic or membrane-associated `fccAB` and `soxYZ`, and suppression of cytoplasmic `dsr` and `apr` groups. The photosynthetic LH and RC genes were also downregulated relative to sulfide controls, indicating that donor identity changes photosystem expression. (alarcon2024evidenceforautotrophic pages 1-2)

This result is relevant to mineral–microbe electron transfer, sulfur and metal biogeochemistry, early-Earth models, and artificial-photosynthesis research. It is not evidence that pyrite is a general donor for purple sulfur bacteria.

### 3. Sulfide detoxification and sulfur recovery

Green and purple sulfur bacteria remove toxic H₂S while producing elemental sulfur and, under some conditions, sulfate. The 2024 GSB review highlights biological sulfide oxidation as an alternative to physicochemical treatment, with separable elemental sulfur as a potentially useful product. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)

Practical configurations include illuminated anaerobic reactors, stratified ponds, and photobioreactors treating sulfide-rich wastewaters. The mechanistic graph can connect H₂S oxidation to reduced sulfide concentration, but treatment performance values should remain in application-specific records rather than the core trait graph.

### 4. Waste-carbon recovery and microbial biomass

Purple nonsulfur bacteria can combine anoxygenic photoheterotrophy with assimilation of volatile fatty acids and other waste organics, enabling wastewater nutrient recovery and production of protein-rich biomass, pigments, coenzyme Q, polyhydroxyalkanoates, or biofertilizer. These are real implementations of the trait’s energetic module, but none is a necessary phenotypic consequence of anoxygenic photosynthesis.

### 5. Biohydrogen and photobioelectrochemical applications

Some purple nonsulfur bacteria use light-derived ATP and reducing power to support nitrogenase-dependent H₂ evolution, while hydrogenases in other taxa mediate H₂ uptake or reversible activation. Biohydrogen production therefore belongs in an organism- and condition-specific extension—not the conserved root graph. Similarly, pyrite-responsive cytochromes suggest extracellular electron-transfer and photoelectrochemical opportunities, but direct causal assignments to individual cytochromes remain unresolved. (alarcon2024evidenceforautotrophic pages 1-2)

## Recommended YAML graph architecture

Use a small universal core with alternative taxonomic modules:

1. **Environmental input:** `light`.
2. **Pigment/antenna:** bacteriochlorophyll-containing antenna.
3. **Reaction-center alternative:**
   - Type I: PscA/PshA → A₀ → FX → PscB/ferredoxin branch;
   - Type II: PufLM → quinone pool → cytochrome bc₁ → cyclic return.
4. **Energy conservation:** electron transport → proton motive force → F-type ATP synthase → ATP.
5. **Electron-donor alternatives:**
   - H₂S → SQR/FccAB → quinone/cytochrome carrier;
   - thiosulfate → Sox system;
   - S⁰ → reverse Dsr pathway;
   - H₂ → hydrogenase;
   - Fe(II) → organism-specific transfer module;
   - organic donor → photoheterotrophic branch.
6. **Assimilation alternatives:** reverse TCA, CBB, 3-hydroxypropionate-related cycle, or organic-carbon assimilation.
7. **Outputs:** no O₂ evolution; ATP production; optional reducing power, carbon fixation, sulfide removal, or biomass production.

This is preferable to a single “sulfide donor” chain because the target is a class-level trait spanning multiple phyla and both reaction-center types.

## Claims that should not yet be curated as universal

1. **“H₂S is the required electron donor.”** It is common in sulfur bacteria but not universal.
2. **“Anoxygenic photosynthesis requires anoxia.”** Strong for canonical sulfur phototrophs and pigment induction in many purple bacteria, but contradicted as a universal statement by aerobic anoxygenic phototrophs.
3. **“All anoxygenic phototrophs possess chlorosomes or FMO.”** False; these are lineage-specific antenna modules.
4. **“All use bacteriochlorophyll.”** Most do, but heliobacterial reaction centers include chlorophyll-like cofactors and nomenclature is lineage-sensitive; curate exact pigments by taxon.
5. **“All fix CO₂.”** False; many are photoheterotrophs.
6. **“All GSB use only reverse TCA and all purple bacteria use CBB.”** Useful generalization but exceptions and mixotrophy require taxon-level confirmation.
7. **“SQR is essential for sulfide-driven phototrophy.”** SQR is important, but FccAB and other routes can contribute; essentiality requires mutants or comparable perturbation evidence.
8. **“PufLM or PscA alone proves the expressed phenotype.”** Marker genes indicate phototrophic potential, not demonstrated activity. Require pigment, transcript/protein, physiological, or photochemical evidence for phenotype calls.
9. **“Pyrite utilization is a general PSB capability.”** The 2024 evidence is specific to *A. vinosum* and its assay conditions. (alarcon2024evidenceforautotrophic pages 1-2)
10. **“The ~200-fold cytochrome response identifies the electron-transfer protein.”** It supports involvement of cytochromes as a group but does not establish which cytochrome directly contacts pyrite.
11. **“O₂ suppresses every anoxygenic photosystem.”** Restrict this edge to anaerobic sulfur phototrophs or individual taxa. (kushkevych2021anoxygenicphotosynthesisin pages 2-3)
12. **Exact CURIEs for chlorosome, FMO, bacteriochlorophyll variants, pyrite, and bacterial bc₁ complex.** Validate against the project’s ontology release before committing; label-only nodes are safer than incorrect identifiers.

## DOI-first bibliography

1. **Kushkevych I, et al.** “Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments.” *Frontiers in Microbiology* 15. **Published July 2024.** DOI: [10.3389/fmicb.2024.1417714](https://doi.org/10.3389/fmicb.2024.1417714). Current overview of GSB physiology, chlorosomes, reverse TCA, sulfide oxidation, and treatment applications. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
2. **Niederman RA.** “What We Are Learning from the Diverse Structures of the Homodimeric Type I Reaction Center-Photosystems of Anoxygenic Phototropic Bacteria.” *Biomolecules* 14. **Published March 2024.** DOI: [10.3390/biom14030311](https://doi.org/10.3390/biom14030311). Structural authority for PscA/PshA, FMO, PscC, PscB, A₀, FX, and Type I electron transfer. (niederman2024whatweare pages 1-2, niederman2024whatweare pages 5-7)
3. **Alarcon HV, et al.** “Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source.” *Applied and Environmental Microbiology* 90(7). **Published July 2024.** DOI: [10.1128/aem.00863-24](https://doi.org/10.1128/aem.00863-24). Experimental pyrite-growth and transcriptomic evidence. (alarcon2024evidenceforautotrophic pages 1-2)
4. **Kushkevych I, et al.** “Anoxygenic Photosynthesis in Photolithotrophic Sulfur Bacteria and Their Role in Detoxication of Hydrogen Sulfide.” *Antioxidants* 10:829. **Published May 2021.** DOI: [10.3390/antiox10060829](https://doi.org/10.3390/antiox10060829). Comparative source for one-photosystem physiology, pigment systems, SQR/Fcc, and sulfide detoxification. (kushkevych2021anoxygenicphotosynthesisin pages 3-5, kushkevych2021anoxygenicphotosynthesisin pages 2-3)
5. **Imhoff JF, et al.** “Phylogeny of Anoxygenic Photosynthesis Based on Sequences of Photosynthetic Reaction Center Proteins and a Key Enzyme in Bacteriochlorophyll Biosynthesis, the Chlorophyllide Reductase.” *Microorganisms* 7:576. **Published November 2019.** DOI: [10.3390/microorganisms7110576](https://doi.org/10.3390/microorganisms7110576). Comparative basis for PufHLM and BchXYZ as phototrophy-system markers.
6. **Martin WF, Bryant DA, Beatty JT.** “A physiological perspective on the origin and evolution of photosynthesis.” *FEMS Microbiology Reviews* 42:205–231. **Published 2018; online record November 2017.** DOI: [10.1093/femsre/fux056](https://doi.org/10.1093/femsre/fux056). Authoritative comparative treatment of reaction centers, electron donors, carbon-fixation pathways, and evolutionary interpretation. (martin2018aphysiologicalperspective pages 2-3)

## Curation conclusion

The existing seven-node sulfide-donor graph is a valid **GSB/PSB sulfur-phototrophy module**, but it is too narrow for the class `traitmech:000035`. The recommended graph should retain that module while adding a universal light-to-ATP backbone, explicit Type I/Type II alternatives, donor and carbon-assimilation branches, and taxon qualifiers. The highest-confidence new additions are the structurally resolved **chlorosome → FMO → PscA**, **PscC → P840**, **A₀ → FX**, and **PscB–FA/FB** relationships, together with the experimentally qualified *A. vinosum* **pyrite → cytochrome response → autotrophic growth** branch.

References

1. (kushkevych2021anoxygenicphotosynthesisin pages 2-3): Ivan Kushkevych, Veronika Bosáková, Monika Vítězová, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis in photolithotrophic sulfur bacteria and their role in detoxication of hydrogen sulfide. Antioxidants, 10:829, May 2021. URL: https://doi.org/10.3390/antiox10060829, doi:10.3390/antiox10060829. This article has 19 citations.

2. (kushkevych2021anoxygenicphotosynthesisin pages 1-2): Ivan Kushkevych, Veronika Bosáková, Monika Vítězová, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis in photolithotrophic sulfur bacteria and their role in detoxication of hydrogen sulfide. Antioxidants, 10:829, May 2021. URL: https://doi.org/10.3390/antiox10060829, doi:10.3390/antiox10060829. This article has 19 citations.

3. (martin2018aphysiologicalperspective pages 2-3): William F Martin, Donald A Bryant, and J Thomas Beatty. A physiological perspective on the origin and evolution of photosynthesis. FEMS Microbiology Reviews, 42:205-231, Nov 2018. URL: https://doi.org/10.1093/femsre/fux056, doi:10.1093/femsre/fux056. This article has 189 citations and is from a domain leading peer-reviewed journal.

4. (niederman2024whatweare pages 1-2): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

5. (niederman2024whatweare pages 5-7): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

6. (kushkevych2021anoxygenicphotosynthesisin pages 3-5): Ivan Kushkevych, Veronika Bosáková, Monika Vítězová, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis in photolithotrophic sulfur bacteria and their role in detoxication of hydrogen sulfide. Antioxidants, 10:829, May 2021. URL: https://doi.org/10.3390/antiox10060829, doi:10.3390/antiox10060829. This article has 19 citations.

7. (niederman2024whatweare pages 7-9): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

8. (alarcon2024evidenceforautotrophic pages 1-2): Hugo V. Alarcon, Jonathon E. Mohl, Grace W. Chong, Ana Betancourt, Yi Wang, Weinan Leng, Jason C. White, and Jie Xu. Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source. Jul 2024. URL: https://doi.org/10.1128/aem.00863-24, doi:10.1128/aem.00863-24. This article has 6 citations and is from a peer-reviewed journal.

9. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 30 citations and is from a peer-reviewed journal.