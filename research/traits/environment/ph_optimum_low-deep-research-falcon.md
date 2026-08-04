---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:38:06.902716'
end_time: '2026-08-04T02:48:16.470982'
duration_seconds: 609.57
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH optimum low
  trait_identifier: METPO:1000455
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_optimum_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH optimum phenotype with the best-growth external pH at or below
    approximately 6, corresponding to acidophilic or extreme-acidophilic physiology.
  parent_traits: METPO:1000331
  synonyms: Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile,
    Obligative acidophile, pHO_0_to_6
  evidence_summary: 'DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis
    review supports growth at acidic external pH as the acidophilic / extreme-acidophilic
    category.)'
  causal_graph_summary: 'ph_optimum_low_acidophile_setpoint: 12 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH optimum low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000455
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH at or below approximately 6, corresponding to acidophilic or extreme-acidophilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile, Obligative acidophile, pHO_0_to_6
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis review supports growth at acidic external pH as the acidophilic / extreme-acidophilic category.)
- **Existing causal graph summary:** ph_optimum_low_acidophile_setpoint: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **pH optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_low.yaml`.

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
- **Trait label:** pH optimum low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000455
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH at or below approximately 6, corresponding to acidophilic or extreme-acidophilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile, Obligative acidophile, pHO_0_to_6
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis review supports growth at acidic external pH as the acidophilic / extreme-acidophilic category.)
- **Existing causal graph summary:** ph_optimum_low_acidophile_setpoint: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **pH optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_low.yaml`.

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


# Curation report: microbial **pH optimum low**

## 1. Scope and curation interpretation

**Target:** `METPO:1000455`  
**Label:** pH optimum low  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED  
**Parent:** `METPO:1000331`

### Recommended operational meaning

`METPO:1000455` denotes a reproducible **growth-rate, biomass-yield, or comparable best-growth optimum at external pH ≤ approximately 6**. It includes moderate acidophiles and extreme acidophiles, but it should not imply that every organism carrying the trait grows across the entire pH 0–6 interval. A widely used literature subdivision is moderate acidophily at an optimum ≤5 and extreme acidophily at an optimum ≤3. Acidophily is fundamentally an optimum-growth phenotype, not merely survival after acid challenge. (gonzalezrosales2022integrativegenomicssheds pages 1-2, krulwich2011molecularaspectsof pages 1-3)

The supplied synonym **pHO_0_to_6** is therefore appropriate as a coarse bin, whereas “acid tolerant” is broader and potentially misleading. For example, the obligate acidophile *“Candidatus Nitrosotalea devanaterra”* has a reported optimum of pH 4.0–5.5 and does not grow above pH 6.5—evidence for a low-pH optimum rather than transient acid resistance. (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5)

### Boundaries

Include:

- best growth at external pH ≤ approximately 6;
- obligate and facultative acidophiles when an optimum is measured;
- extreme acidophiles, commonly defined by optimum ≤3;
- assay observations based on growth rate, biomass, colony formation, or another clearly specified growth endpoint.

Do **not** equate the trait with:

- survival following a short acid shock;
- a low minimum growth pH when the optimum is neutral;
- acid resistance or acid tolerance in neutralophiles;
- acid production, fermentation end products, or medium acidification;
- isolation from an acidic habitat without a measured growth optimum;
- intracellular or organellar acidity;
- growth inhibition by low pH.

A source can therefore support a homeostasis mechanism without proving `METPO:1000455`. The strongest trait annotation requires a growth curve or equivalent optimum assay plus mechanistic evidence from the same organism.

## 2. Current mechanistic model

Acidophiles maintain a cytoplasm substantially less acidic than their environment. Extreme acidophiles can face proton gradients exceeding 10⁴-fold—and comparative work reports gradients as high as 10⁵-fold—while retaining near-neutral or approximately pH 6 cytoplasm. *Acidithiobacillus ferrooxidans*, for example, grows near external pH 2 while maintaining pH homeostasis. (vergara2020evolutionofpredicted pages 1-3, gonzalezrosales2022integrativegenomicssheds pages 1-2, krulwich2011molecularaspectsof pages 1-3)

The consensus model has two interacting layers:

1. **First-line proton exclusion:** a proton-resistant membrane/envelope and an inside-positive, “reversed” membrane potential reduce inward proton movement.
2. **Second-line correction:** proton pumps, antiporters, proton-consuming reactions, buffering, repair, and turnover restore cytoplasmic conditions after protons enter.

This is not a single universal pathway. Bacterial hopanoid membranes, archaeal ether-lipid architectures, different K⁺ transport systems, and lineage-specific respiratory or buffering modules can implement analogous functions. Comparative genomics suggests that Acidithiobacillia acquired many extreme-acid adaptation systems through horizontal gene transfer and expanded redundant “second-line” systems, but much of that reconstruction remains predictive. (gonzalezrosales2022integrativegenomicssheds pages 1-2, vergara2020evolutionofpredicted pages 16-17)

## 3. Candidate nodes grouped by type

### Trait and environmental nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| pH optimum low | `METPO:1000455` | Quote identifier verbatim. |
| low external pH | Label-only environmental quality | Record numerical pH and assay medium rather than treating all acidic conditions as identical. |
| extreme low external pH | Label-only; operationally optimum ≤3 | Literature threshold, not necessarily an ontology class. |
| external-to-cytoplasmic proton gradient | Label-only | Direction and magnitude should be explicit. |
| chloride exposure | `CHEBI:17996` chloride | Important negative modifier in some acidophiles. |
| acid mine drainage | ENVO candidate; verify exact current term during ingestion | Habitat does not by itself establish the trait. |

### Chemicals and electrochemical entities

| Candidate node | Suggested grounding |
|---|---|
| proton / hydrogen ion | `CHEBI:15378` |
| potassium ion | `CHEBI:29103` |
| sodium ion | `CHEBI:26710` |
| inside-positive membrane potential | Label-only |
| proton-motive force | Label-only unless the project has an approved electrochemical ontology mapping |
| spermidine | ChEBI candidate; verify identifier before YAML insertion |
| hopanoids | ChEBI-class candidate; exact lipid species should be used when measured |
| poly-γ-glutamate | Label-only pending polymer-specific grounding |
| hydroxyectoine and trehalose | ChEBI candidates; verify exact forms |

### Cellular structures and processes

| Candidate node | Suggested grounding |
|---|---|
| plasma/cytoplasmic membrane | `GO:0005886` |
| hydrogen-ion transport | `GO:0006818` |
| potassium-ion transport | `GO:0006813` |
| DNA repair | `GO:0006281` |
| protein folding | `GO:0006457` |
| cytoplasmic pH homeostasis | Label-only unless a verified GO term is selected |
| reduced membrane proton permeability | Label-only measurable property |
| macromolecular damage repair | Label-only umbrella process |

### Genes, proteins, transporters, and complexes

- **Kch, Kdp, and Trk potassium-transport systems:** candidates for generating the inside-positive potential; presence and directionality must be verified per taxon.
- **KdpC/KdpD:** transcriptionally responsive under chloride stress in *Leptospirillum ferriphilum*, but expression under stress is not proof that these proteins set the organism’s pH optimum. (riveraaraya2019osmoticimbalancecytoplasm pages 1-2)
- **NhaA/NhaP-like Na⁺/H⁺ antiporters and ClcA:** proposed second-line proton-handling systems in *Leptospirillum*; mostly comparative-genomic predictions. (vergara2020evolutionofpredicted pages 1-3, vergara2020evolutionofpredicted pages 16-17)
- **Electron-transfer-chain-linked proton pumps:** expressed candidates in *“Ca. N. devanaterra”*; biochemical directionality remains to be demonstrated for each complex. (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5)
- **Glutamate and arginine decarboxylation systems:** proton-consuming candidates; avoid universalizing neutralophile acid-resistance pathways to obligate acidophiles. (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5, gonzalezrosales2022integrativegenomicssheds pages 1-2)
- **Carbonic anhydrase:** possible buffering/homeostasis component in *“Ca. N. devanaterra”*; presently a taxon-specific candidate. (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5)
- **Omp40, PspA, and Slp-family outer-membrane proteins:** proposed contributors to envelope impermeability or organic-acid exclusion; family and taxon-specific evidence should be retained. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, vergara2020evolutionofpredicted pages 1-3)
- **Hopanoid-biosynthesis enzymes:** plausible membrane-stabilization module in bacterial acidophiles; gene presence is weaker than a mutant or lipid-permeability phenotype. (vergara2020evolutionofpredicted pages 1-3, gonzalezrosales2022integrativegenomicssheds pages 1-2)

### Metabolic and ecological modules

- aerobic Fe²⁺ oxidation and reduced-sulfur oxidation in biomining taxa;
- dissimilatory sulfate reduction in acidophilic sulfate-reducing bacteria;
- acidophilic ammonia oxidation in *“Ca. N. devanaterra”*;
- cytoplasmic buffering and proton-consuming amino-acid reactions;
- compatible-solute synthesis and oxidative-stress mitigation under combined chloride/acidity stress.

These metabolic modules permit energy conservation or stress mitigation at low pH, but none should automatically be asserted as a universal cause of the phenotype.

## 4. Candidate causal edges

The compact priority view is followed by edge-specific supporting snippets and curation qualifications.

| subject | predicate | object | confidence/evidence type | taxonomic scope | key DOI |
|---|---|---|---|---|---|
| low external pH | causes | steep inward proton gradient across cell membrane | High; authoritative review/physiology synthesis (krulwich2011molecularaspectsof pages 1-3) | Broad acidophiles | 10.1038/nrmicro2549 |
| low membrane proton permeability | reduces | proton influx into cytoplasm | Moderate-High; review plus comparative physiology/genomics (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2) | Broad acidophiles; aSRB; Acidithiobacillia | 10.1111/1758-2229.70019 |
| hopanoid biosynthesis / hopanoid-rich membrane | stabilizes | membrane at low pH | Moderate; comparative-genomic/evolutionary inference with supporting prior experiments in other taxa (vergara2020evolutionofpredicted pages 1-3, gonzalezrosales2022integrativegenomicssheds pages 1-2) | Bacterial acidophiles, especially Acidithiobacillia/Leptospirillum | 10.3389/fmicb.2021.822229 |
| acid-stable membrane composition | enables | low-pH growth/homeostasis | Moderate; experimental lipid-composition association in Acididesulfobacillus acetoxydans and archaeal multi-omics indication (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5) | aSRB; acidophilic archaea | 10.1111/1758-2229.70019 |
| K+ uptake / potassium transporters | generates | inside-positive (reversed) membrane potential | High; review plus comparative-genomic support (krulwich2011molecularaspectsof pages 1-3, vergara2020evolutionofpredicted pages 1-3, gonzalezrosales2022integrativegenomicssheds pages 1-2) | Broad acidophiles; Leptospirillum; Acidithiobacillia | 10.1038/nrmicro2549 |
| inside-positive (reversed) membrane potential | reduces | proton entry into cytoplasm | High; mechanistic review and comparative-genomic synthesis (krulwich2011molecularaspectsof pages 1-3, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2) | Broad acidophiles | 10.1038/nrmicro2549 |
| proton pumps / electron-transport-linked proton extrusion | exports | cytoplasmic protons | Moderate; experimental expression support in acidophilic archaeon plus review synthesis (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Acidophilic archaea; broad acidophiles | 10.1128/AEM.04031-15 |
| Na+/H+ antiporters | exports | protons from cytoplasm | Moderate; comparative-genomic/predicted for Leptospirillum and broad synthesis (vergara2020evolutionofpredicted pages 1-3) | Leptospirillum and other bacterial acidophiles | 10.3390/genes11040389 |
| proton-consuming / buffering reactions | increases | cytoplasmic pH | Moderate; genome-informed and review-level evidence for glutamate decarboxylation, arginine/glutamate pathways, carbonic anhydrase (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5, gonzalezrosales2022integrativegenomicssheds pages 1-2) | Acidophilic archaea; broad acidophiles | 10.1128/AEM.04031-15 |
| DNA repair and acid-stable protein synthesis | mitigates | low-pH-associated macromolecular damage | Moderate; recent review/synthesis (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | aSRB and likely broader acidophiles | 10.1111/1758-2229.70019 |
| chloride exposure | causes | cytoplasmic acidification | High; directly measured experiment in Leptospirillum ferriphilum (intracellular pH 6.7 -> 5.5 under NaCl stress) (riveraaraya2019osmoticimbalancecytoplasm pages 1-2) | Leptospirillum ferriphilum | 10.3389/fmicb.2019.02455 |
| chloride exposure | inhibits | acidophile physiology / pH homeostasis | High; direct physiology plus transcriptional stress response experiment (riveraaraya2019osmoticimbalancecytoplasm pages 1-2) | Leptospirillum ferriphilum | 10.3389/fmicb.2019.02455 |


*Table: This table summarizes the highest-priority causal edges for curating METPO:1000455, emphasizing mechanisms with the strongest experimental or authoritative-review support. It also flags which claims are directly measured versus comparative-genomic or predicted, helping prioritize cautious TraitMech curation.*

| # | Proposed subject–predicate–object triple | Reference and supporting snippet | Curation assessment |
|---|---|---|---|
| 1 | **low external pH — creates → large inward proton gradient** | Krulwich et al.: acidophiles have an exceptional large ΔpH with “pHin > pHout”; extreme *Leptospirillum* faces a “>10⁴-fold proton gradient.” DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549), May 2011; DOI: [10.3390/genes11040389](https://doi.org/10.3390/genes11040389), April 2020. (krulwich2011molecularaspectsof pages 1-3, vergara2020evolutionofpredicted pages 1-3) | **High confidence**, physical/physiological relationship. Prefer a continuous pH-gradient node rather than a binary state. |
| 2 | **low membrane proton permeability — decreases → proton influx** | The 2024 aSRB review identifies “proton exclusion” through hopanoid lipids and membrane proteins; Acidithiobacillia analysis classifies prevention of proton influx as the “first line of defense.” DOI: [10.1111/1758-2229.70019](https://doi.org/10.1111/1758-2229.70019), October 2024; DOI: [10.3389/fmicb.2021.822229](https://doi.org/10.3389/fmicb.2021.822229), February 2022. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2) | **Moderate–high**, broad mechanism. Direct permeability measurements are preferable for taxon-level assertions. |
| 3 | **hopanoid biosynthesis — stabilizes → membrane at low pH** | Comparative studies identify hopanoid biosynthesis in “membrane stabilization at low pH”; hopanoid-gene deletion impairs low-pH growth in supporting organisms. DOI: [10.3389/fmicb.2021.822229](https://doi.org/10.3389/fmicb.2021.822229); DOI: [10.3390/genes11040389](https://doi.org/10.3390/genes11040389). (vergara2020evolutionofpredicted pages 1-3, gonzalezrosales2022integrativegenomicssheds pages 1-2) | **Moderate; taxon-sensitive.** Much acidophile-specific evidence is genomic or transferred from experiments in other organisms. Do not apply to Archaea. |
| 4 | **acid-stable membrane composition — supports → cytoplasmic pH homeostasis/low-pH growth** | In *Acididesulfobacillus acetoxydans* grown at pH 3.9–5.0, increased acyl/ether glycerol lipids, a saturated ether moiety, and branched iso-C15:0 were associated with acid resistance. *“Ca. N. devanaterra”* lipid profiling found a composition not dominated by crenarchaeol, unlike neutrophilic ammonia-oxidizing archaea. DOI: [10.1111/1758-2229.70019](https://doi.org/10.1111/1758-2229.70019); DOI: [10.1128/AEM.04031-15](https://doi.org/10.1128/AEM.04031-15), May 2016. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5) | **Moderate association**, not a universal lipid recipe. Preserve organism, growth pH, and analytical method. |
| 5 | **K⁺ uptake — generates → inside-positive membrane potential** | Kch, Kdp, and Trk systems are proposed to produce the acidophile’s inside-positive potential; removal of K⁺/Na⁺ decreased acid resistance in supporting *Sulfolobus* and *Acidithiobacillus* experiments. DOI: [10.3390/genes11040389](https://doi.org/10.3390/genes11040389). (vergara2020evolutionofpredicted pages 1-3) | **Moderate–high mechanistic support**, but transporter-specific assignments in *Leptospirillum* remain partly predictive. |
| 6 | **inside-positive membrane potential — decreases → proton entry** | The reversed potential “partially offsets” the large ΔpH; recent aSRB synthesis describes electrostatic proton repulsion after K⁺/Na⁺ accumulation. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549); DOI: [10.1111/1758-2229.70019](https://doi.org/10.1111/1758-2229.70019). (krulwich2011molecularaspectsof pages 1-3, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | **High confidence** as a general electrochemical mechanism. It contributes to homeostasis but does not alone prove a low-pH optimum. |
| 7 | **electron-transfer-chain-linked proton pumps — export → cytoplasmic H⁺** | The *“Ca. N. devanaterra”* study identifies proton pumps coupled to electron-transfer chains as candidate active proton-removal systems, and the candidate genes were expressed during acidophilic growth. DOI: [10.1128/AEM.04031-15](https://doi.org/10.1128/AEM.04031-15). (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5) | **Moderate; expression-supported prediction.** Require biochemical directionality or perturbation before asserting a specific pump as causal. |
| 8 | **Na⁺/H⁺ antiporter — exports → cytoplasmic H⁺** | NhaA/NhaP-type antiporters are placed in the “second line of defense” for proton expulsion in comparative *Leptospirillum* analyses. DOI: [10.3390/genes11040389](https://doi.org/10.3390/genes11040389). (vergara2020evolutionofpredicted pages 1-3, vergara2020evolutionofpredicted pages 16-17) | **Uncertain/moderate.** Comparative-genomic prediction; transport direction depends on ion gradients and physiological conditions. |
| 9 | **proton-consuming and buffering reactions — increase/stabilize → cytoplasmic pH** | Candidate mechanisms include carbonic anhydrase and arginine/glutamate decarboxylation; Acidithiobacillia analyses specifically identify glutamate decarboxylation as proton-consuming. DOI: [10.1128/AEM.04031-15](https://doi.org/10.1128/AEM.04031-15); DOI: [10.3389/fmicb.2021.822229](https://doi.org/10.3389/fmicb.2021.822229). (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5, gonzalezrosales2022integrativegenomicssheds pages 1-2) | **Moderate to weak**, pathway- and taxon-specific. Separate each reaction in YAML and require substrate availability. |
| 10 | **DNA repair/acid-stable protein production — mitigates → acid-associated macromolecular damage** | The 2024 aSRB synthesis lists “DNA repair and acid-stable protein synthesis” among damage-mitigation mechanisms. DOI: [10.1111/1758-2229.70019](https://doi.org/10.1111/1758-2229.70019). (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | **Weak–moderate for trait causality.** This is review-level and nonspecific; curate only with gene-level perturbation or strong comparative evidence. |
| 11 | **chloride exposure — causes → cytoplasmic acidification** | In *L. ferriphilum* DSM 14647 exposed to up to 150 mM NaCl, intracellular pH fell “from 6.7 to 5.5.” DOI: [10.3389/fmicb.2019.02455](https://doi.org/10.3389/fmicb.2019.02455), October 2019. (riveraaraya2019osmoticimbalancecytoplasm pages 1-2) | **High confidence; direct experiment**, but assay- and taxon-specific. This is a modifier/inhibitory edge rather than a cause of acidophily. |
| 12 | **chloride exposure — increases → oxidative/osmotic stress responses** | The same experiment found increased oxygen consumption and ROS, induction of `kdpC/kdpD`, `ectC/ectD`, `otsB`, `ccp`, and `trx`, and increased hydroxyectoine, trehalose, peroxidase, and thioredoxin activities. (riveraaraya2019osmoticimbalancecytoplasm pages 1-2) | **High confidence for the experiment.** Do not collapse this multifactorial response into a single pH-homeostasis mechanism. |
| 13 | **acidophilic growth machinery — enables → biomining at pH 1–3** | A 2024 review reports commercial copper-tailings bioleaching and optimal pH 1.0–3.0 for many systems, with mesophiles, moderate thermophiles, and extreme thermophiles occupying different temperature regimes. DOI: [10.3390/min14101051](https://doi.org/10.3390/min14101051), October 2024. (zhang2024accumulatedcoppertailing pages 5-8, zhang2024accumulatedcoppertailing pages 1-2) | **Application-level association**, not a direct molecular edge to the trait. Keep outside the core homeostasis subgraph or label as an enabled process. |

## 5. Recent developments and quantitative evidence

### 2024 acidophilic sulfate reducers

A recent synthesis defines acidophilic sulfate-reducing bacteria as organisms active below pH 5 and reports that acidophiles can maintain internal pH around 6 while growing below external pH 3. It highlights proton impermeability and Donnan/inside-positive potential, as well as lipid remodeling in *A. acetoxydans*. The authors explicitly describe several mechanisms as “likely” and call for pure-culture confirmation; this is important because a 2024 review is current evidence synthesis, not equivalent to gene knockout data. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

These organisms are being developed for acid-mine-drainage treatment: sulfate reduction generates sulfide that can precipitate dissolved metals, enabling water treatment, metal recovery, and potentially production of metal-sulfide nanoparticles. These application claims are supported at review level and should not be inserted as universal determinants of low-pH optimum. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

### 2024 bioleaching implementations

Commercial-scale copper-tailings bioleaching is reported at Dexing, Zijinshan, and Jinchuan in China. The review lists a 1,000-t Dexing operation dating to 1987, a 10,000-t scale at Zijinshan, and organisms including *Acidithiobacillus*, *Leptospirillum*, *Sulfobacillus*, *Ferroplasma*, and thermoacidophilic archaea. Reported operating envelopes include dissolved oxygen of 1.5–4.1 mg/L, 20–40 °C for mesophiles, 40–60 °C for moderate thermophiles, and >65 °C for extreme thermophiles. (zhang2024accumulatedcoppertailing pages 5-8, zhang2024accumulatedcoppertailing pages 1-2)

Reported copper recoveries vary strongly by organism, temperature, mineral, and reactor: 16.59–30% with natural acid-mine-drainage communities, 40% with *A. caldus* at 45 °C, 90% with mixed thermophiles at 45 °C, and 97% with *Sulfolobus acidocaldarius* at 70 °C in a chalcopyrite system. These are cross-study application figures, not controlled evidence that low-pH optimum alone caused the differences. The same review estimates that about 20 million tonnes of tailings above 0.1% Cu could be economically relevant to bioleaching. (zhang2024accumulatedcoppertailing pages 5-8)

### Multi-omics and evolutionary analysis

The strongest modern trend is integration of comparative genomics, transcriptomics, and lipidomics. In *“Ca. N. devanaterra”*, candidate homeostasis genes were expressed during acidophilic growth and HPLC–MS showed a membrane-lipid profile distinct from neutrophilic ammonia-oxidizing archaea. Nevertheless, expression and lipid association identify candidates; they do not establish causal necessity. (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5)

Acidithiobacillia comparative genomics links the evolutionary transition from a neutrophilic ancestor to gene gains for hopanoid synthesis, positive-potential generation, proton neutralization, and proton export. It also suggests extensive horizontal transfer and functional redundancy, providing an expert evolutionary model but not direct physiological validation of every edge. (gonzalezrosales2022integrativegenomicssheds pages 1-2)

## 6. Recommended minimal TraitMech graph

For an initial conservative revision of `ph_optimum_low_acidophile_setpoint`, prioritize this backbone:

1. `low external pH` → **creates** → `large inward proton gradient`.
2. `acid-stable low-proton-permeability membrane` → **reduces** → `proton influx`.
3. `potassium uptake` → **generates** → `inside-positive membrane potential`.
4. `inside-positive membrane potential` → **reduces** → `proton influx`.
5. `proton export and proton-consuming reactions` → **increase/stabilize** → `cytoplasmic pH`.
6. `stable cytoplasmic pH` → **supports** → `growth at low external pH`.
7. `growth optimum at external pH ≤ approximately 6` → **realizes** → `METPO:1000455`.

Add hopanoids, particular transporters, decarboxylases, archaeal lipids, and repair systems only in taxon-qualified branches. The final edge from homeostasis to the trait should be treated as a systems-level relationship: maintaining cytoplasmic pH is generally necessary, but a low optimum also depends on acid-adapted enzymes, nutrient chemistry, energy metabolism, and regulatory architecture.

## 7. Claims not yet suitable for unconditional curation

1. **Gene presence implies acidophily.** Kdp, NhaA/NhaP, decarboxylases, chaperones, and DNA-repair genes occur in many non-acidophiles.
2. **Hopanoids universally cause low-pH optimum.** Evidence is strongest for selected bacteria; Archaea use fundamentally different membrane chemistry.
3. **Every K⁺ transporter generates the reversed potential.** Transport direction, regulation, and energetic coupling must be established in the organism and condition.
4. **Every antiporter exports protons at low pH.** Directionality can reverse with electrochemical conditions.
5. **Transcript induction establishes necessity.** The *“Ca. N. devanaterra”* and chloride-response data identify active candidates but require genetic or biochemical tests for causality. (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5, riveraaraya2019osmoticimbalancecytoplasm pages 1-2)
6. **Near-neutral cytoplasm is universal.** Some reports use approximately pH 6 rather than strict neutrality, and values can be inferred rather than directly measured in difficult taxa. In *Leptospirillum*, approximately pH 6 was explicitly described as hypothetical in one genomic reconstruction. (vergara2020evolutionofpredicted pages 16-17)
7. **Acid-mine habitat establishes `METPO:1000455`.** Habitat metadata and metal tolerance cannot replace a growth-optimum assay.
8. **Sulfate reduction, iron oxidation, sulfur oxidation, or ammonia oxidation universally causes acidophily.** These are lineage-specific energy metabolisms compatible with low-pH growth.
9. **Chloride response is a core positive mechanism.** The direct evidence instead shows chloride-driven cytoplasmic acidification and oxidative/osmotic injury in *L. ferriphilum*. (riveraaraya2019osmoticimbalancecytoplasm pages 1-2)
10. **Application recovery percentages are trait-effect sizes.** Bioleaching recovery also depends on mineralogy, temperature, oxygen, pulp density, reactor design, and community composition. (zhang2024accumulatedcoppertailing pages 5-8)

## 8. DOI-first bibliography

1. **Valdez-Nuñez LF et al.** “Acidophilic sulphate-reducing bacteria: Diversity, ecophysiology, and applications.” *Environmental Microbiology Reports*. Published October 2024. DOI: [10.1111/1758-2229.70019](https://doi.org/10.1111/1758-2229.70019). (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
2. **Zhang J et al.** “Accumulated Copper Tailing Solid Wastes with Specific Compositions Encourage Advances in Microbial Leaching.” *Minerals* 14:1051. Published October 2024. DOI: [10.3390/min14101051](https://doi.org/10.3390/min14101051). (zhang2024accumulatedcoppertailing pages 5-8, zhang2024accumulatedcoppertailing pages 1-2)
3. **González-Rosales C et al.** “Integrative Genomics Sheds Light on Evolutionary Forces Shaping the Acidithiobacillia Class Acidophilic Lifestyle.” *Frontiers in Microbiology* 12. Published February 2022. DOI: [10.3389/fmicb.2021.822229](https://doi.org/10.3389/fmicb.2021.822229). (gonzalezrosales2022integrativegenomicssheds pages 1-2)
4. **Vergara E et al.** “Evolution of Predicted Acid Resistance Mechanisms in the Extremely Acidophilic Leptospirillum Genus.” *Genes* 11:389. Published April 2020. DOI: [10.3390/genes11040389](https://doi.org/10.3390/genes11040389). (vergara2020evolutionofpredicted pages 1-3, vergara2020evolutionofpredicted pages 16-17)
5. **Rivera-Araya J et al.** “Osmotic Imbalance, Cytoplasm Acidification and Oxidative Stress Induction Support the High Toxicity of Chloride in Acidophilic Bacteria.” *Frontiers in Microbiology* 10. Published October 2019. DOI: [10.3389/fmicb.2019.02455](https://doi.org/10.3389/fmicb.2019.02455). (riveraaraya2019osmoticimbalancecytoplasm pages 1-2)
6. **Lehtovirta-Morley LE et al.** “Identifying Potential Mechanisms Enabling Acidophily in the Ammonia-Oxidizing Archaeon ‘Candidatus Nitrosotalea devanaterra’.” *Applied and Environmental Microbiology* 82:2608–2619. Published May 2016. DOI: [10.1128/AEM.04031-15](https://doi.org/10.1128/AEM.04031-15). (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5)
7. **Krulwich TA, Sachs G, Padan E.** “Molecular aspects of bacterial pH sensing and homeostasis.” *Nature Reviews Microbiology* 9:330–343. Published May 2011. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 1-3)

**Overall curation judgment:** the most defensible universal graph is a homeostasis-centered causal chain linking low external pH to proton pressure, proton exclusion and electrostatic repulsion, corrective proton handling, stabilized cytoplasmic pH, and low-pH growth. Specific genes and lipid modules should be represented as taxon-qualified implementations, with comparative-genomic predictions marked uncertain until perturbation or direct transport/permeability measurements are available.

References

1. (gonzalezrosales2022integrativegenomicssheds pages 1-2): Carolina González-Rosales, Eva Vergara, Mark Dopson, Jorge H. Valdés, and David S. Holmes. Integrative genomics sheds light on evolutionary forces shaping the acidithiobacillia class acidophilic lifestyle. Frontiers in Microbiology, Feb 2022. URL: https://doi.org/10.3389/fmicb.2021.822229, doi:10.3389/fmicb.2021.822229. This article has 31 citations and is from a peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

3. (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5): Laura E. Lehtovirta-Morley, Luis A. Sayavedra-Soto, Nicolas Gallois, Stefan Schouten, Lisa Y. Stein, James I. Prosser, and Graeme W. Nicol. Identifying potential mechanisms enabling acidophily in the ammonia-oxidizing archaeon “candidatus nitrosotalea devanaterra”. Applied and Environmental Microbiology, 82:2608-2619, May 2016. URL: https://doi.org/10.1128/aem.04031-15, doi:10.1128/aem.04031-15. This article has 182 citations and is from a peer-reviewed journal.

4. (vergara2020evolutionofpredicted pages 1-3): Eva Vergara, Gonzalo Neira, Carolina González, Diego Cortez, Mark Dopson, and David S. Holmes. Evolution of predicted acid resistance mechanisms in the extremely acidophilic leptospirillum genus. Genes, 11:389, Apr 2020. URL: https://doi.org/10.3390/genes11040389, doi:10.3390/genes11040389. This article has 40 citations.

5. (vergara2020evolutionofpredicted pages 16-17): Eva Vergara, Gonzalo Neira, Carolina González, Diego Cortez, Mark Dopson, and David S. Holmes. Evolution of predicted acid resistance mechanisms in the extremely acidophilic leptospirillum genus. Genes, 11:389, Apr 2020. URL: https://doi.org/10.3390/genes11040389, doi:10.3390/genes11040389. This article has 40 citations.

6. (riveraaraya2019osmoticimbalancecytoplasm pages 1-2): Javier Rivera-Araya, Andre Pollender, Dieu Huynh, Michael Schlömann, Renato Chávez, and Gloria Levicán. Osmotic imbalance, cytoplasm acidification and oxidative stress induction support the high toxicity of chloride in acidophilic bacteria. Frontiers in Microbiology, Oct 2019. URL: https://doi.org/10.3389/fmicb.2019.02455, doi:10.3389/fmicb.2019.02455. This article has 56 citations and is from a peer-reviewed journal.

7. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 18 citations and is from a peer-reviewed journal.

8. (zhang2024accumulatedcoppertailing pages 5-8): Juan Zhang, Xiaojun Liu, Xinyue Du, Xin Wang, Yifan Zeng, and Shu-kai Fan. Accumulated copper tailing solid wastes with specific compositions encourage advances in microbial leaching. Minerals, 14:1051, Oct 2024. URL: https://doi.org/10.3390/min14101051, doi:10.3390/min14101051. This article has 5 citations.

9. (zhang2024accumulatedcoppertailing pages 1-2): Juan Zhang, Xiaojun Liu, Xinyue Du, Xin Wang, Yifan Zeng, and Shu-kai Fan. Accumulated copper tailing solid wastes with specific compositions encourage advances in microbial leaching. Minerals, 14:1051, Oct 2024. URL: https://doi.org/10.3390/min14101051, doi:10.3390/min14101051. This article has 5 citations.