---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:50:41.163542'
end_time: '2026-08-04T00:01:02.033139'
duration_seconds: 620.87
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: acidophilic
  trait_identifier: METPO:1003003
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: acidophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference in which an organism grows optimally at pH values
    below 5.
  parent_traits: METPO:1003000
  synonyms: acidophil, acidophile
  evidence_summary: 'DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (Supports acidophilic
    growth at strongly acidic external pH.)'
  causal_graph_summary: 'acidophilic_ph_homeostasis: 13 nodes, 11 edges'
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
- **Trait label:** acidophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003003
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism grows optimally at pH values below 5.
- **Parent traits:** METPO:1003000
- **Synonyms:** acidophil, acidophile
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (Supports acidophilic growth at strongly acidic external pH.)
- **Existing causal graph summary:** acidophilic_ph_homeostasis: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/acidophilic.yaml`.

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
- **Trait label:** acidophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003003
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism grows optimally at pH values below 5.
- **Parent traits:** METPO:1003000
- **Synonyms:** acidophil, acidophile
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (Supports acidophilic growth at strongly acidic external pH.)
- **Existing causal graph summary:** acidophilic_ph_homeostasis: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/acidophilic.yaml`.

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


# Curation report: microbial acidophily

## Executive assessment

**Target trait:** acidophilic  
**Identifier:** **METPO:1003003**  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED  
**Definition:** optimal growth at pH values below 5  
**Parent:** METPO:1003000  
**Synonyms:** acidophil; acidophile

The trait should represent a **stable growth preference**, established from a growth-rate or biomass-versus-pH assay, rather than survival after a short acid shock. Extreme acidophiles are a nested boundary class commonly growing at pH 1–3. Their pH-homeostasis systems are often constitutively expressed, unlike inducible acid-stress systems in neutralophiles. Constitutive preparedness may reduce fitness near neutral pH because of energetic costs and proteins specialized for extreme conditions. (krulwich2011molecularaspectsof pages 3-5)

The best-supported causal architecture has two layers: **(i) restriction of proton entry**, principally through unusually impermeable membranes and an inside-positive electrical potential, and **(ii) removal, neutralization, or buffering of protons that enter**. The endpoint is maintenance of an intracellular pH compatible with macromolecular function despite a large transmembrane proton gradient. In thermoacidophilic archaea growing at pH ≤4, intracellular pH is generally 5.4–6.5; *Picrophilus* is exceptional at approximately 4.6. (gonzalezrosales2022integrativegenomicssheds pages 1-2, chong2024archaeamembranesin pages 2-3)

The strongest graph-ready module is the archaeal bipolar-tetraether-membrane chain. Bacterial potassium-potential, hopanoid, porin, and proton-consuming modules are biologically plausible but are more often supported by comparative genomics, expression data, or experiments in only a few taxa. They should therefore carry taxon and evidence qualifiers.

## 1. Trait scope and boundary cases

### Include

1. An organism whose **measured optimum growth pH is <5**, including moderate and extreme acidophiles.
2. The environmental condition of low extracellular pH and mechanisms that causally enable growth under it.
3. Constitutive or environmentally regulated processes that maintain membrane integrity, limit proton influx, sustain intracellular pH, or repair secondary acid damage.
4. Taxon-specific modules when the organism and evidence type are recorded explicitly.

### Exclude or annotate separately

- **Acid resistance/tolerance:** survival at low pH by a neutralophile does not establish optimal growth below pH 5.
- **Acid shock response:** transient induction after abrupt exposure is not equivalent to acidophily.
- **Acid production:** production of lactate, acetate, sulfuric acid, or another acid is a metabolic output, not proof of an acidophilic optimum.
- **Occurrence in an acidic habitat:** metagenomic detection in acid mine drainage does not establish the isolate’s optimum pH.
- **Aciduric phenotype:** persistence over a broad pH range should remain distinct unless the optimum itself is below 5.
- **Extreme acidophily:** useful as a narrower annotation. A major review describes extreme acidophilic bacteria as growing at pH 1–3, but this should not replace the supplied METPO threshold. (krulwich2011molecularaspectsof pages 3-5)
- **Organic-acid resistance:** weak organic acids cross membranes in uncharged form and impose additional anion toxicity; this is not mechanistically identical to adaptation to high extracellular proton activity.

### Recommended assay representation

Record optimum pH, tested pH range, medium and acidulant, temperature, oxygen regime, growth measure, growth phase, and whether pH was controlled. Temperature is especially important for thermoacidophilic membrane phenotypes: *Sulfolobus acidocaldarius* maintains an approximately pH 2.5 outside/pH 6.5 inside gradient over 65–90°C. (chong2024archaeamembranesin pages 3-4)

## 2. Candidate nodes grouped by type

### Trait, environmental, and experimental nodes

- acidophilic — **METPO:1003003**
- parent environmental growth-preference trait — **METPO:1003000**
- acidic environment — candidate **ENVO** grounding should be verified before YAML insertion
- extracellular pH below 5 — label-only assay node
- extreme acidic condition, pH 1–3 — label-only boundary node
- optimum growth pH — label-only experimental factor
- transmembrane pH gradient — label-only process/state
- chloride stress / NaCl exposure — chloride **CHEBI:17996**; sodium chloride **CHEBI:26710**
- elevated temperature — label-only environmental factor

### Chemicals and physicochemical states

- proton — **CHEBI:15378**
- potassium ion — **CHEBI:29103**
- sodium ion — **CHEBI:29101**
- spermidine — **CHEBI:16610**
- glutamate — use the charge-state-specific CHEBI identifier only after checking assay pH
- reactive oxygen species — **CHEBI:26523**
- trehalose — **CHEBI:27082**
- ectoine and hydroxyectoine — verify charge-state-specific CHEBI records before curation
- membrane potential, inside-positive — label-only state
- cytoplasmic buffering capacity — label-only state

### Cellular locations and structures

- plasma membrane — **GO:0005886**
- cytoplasm — **GO:0005737**
- outer membrane — **GO:0019867**
- cell envelope — **GO:0030313**
- capsule polysaccharide layer — label-only candidate
- extracellular polymeric substance/biofilm matrix — label-only candidate
- archaeal bipolar tetraether membrane — label-only candidate

### Lipids and membrane modules

- bipolar tetraether lipids (BTL)
- glycerol dialkyl glycerol tetraether (GDGT)
- glycerol dialkyl calditol tetraether (GDNT)
- polar lipid fraction E (PLFE) of *S. acidocaldarius*
- tetraether:diether ratio
- GDNT:GDGT ratio
- cyclopentane rings in biphytanyl chains
- hopanoids
- acyl/ether glycerol lipids and iso-branched fatty acids — restricted to relevant acidophilic sulfate reducers

The 2024 membrane review reports that BTLs dominate thermoacidophiles inhabiting pH ≤4 at ≥65°C. Their macrocyclic architecture, hydroxyl-rich headgroups, and cyclopentane substitutions alter hydrogen bonding, packing, rigidity, and membrane-volume fluctuations. (chong2024archaeamembranesin pages 1-2)

### Genes, proteins, transporters, and complexes

- **GrsA** and **GrsB**, GDGT ring synthase isoforms — label-only until organism-specific UniProt accessions are selected
- **Kch**, **Kdp**, and **Trk** potassium transport systems
- respiratory-chain proton pumps
- proton-coupled ATPase / H+-ATPase
- cation/H+ antiporters, including predicted NhaA/NhaP-family systems
- **Omp40**, acidophile-associated outer-membrane channel
- **Slp**, starvation-inducible outer-membrane protein
- **AqpF**, proposed proton-blocking aquaporin variant
- glutamate decarboxylase and amino-acid antiporter modules
- urease and urea transport system, where experimentally demonstrated
- cytochrome-c peroxidase and thioredoxin
- PspA and other membrane-stress proteins
- chaperones and DNA-repair systems — retain as broad candidates pending acidophile-specific perturbation evidence

### Processes and molecular functions

- proton transmembrane transport — **GO:1902600**
- cellular pH homeostasis — **GO:0030003**
- potassium-ion transport — **GO:0006813**
- response to oxidative stress — **GO:0006979**
- membrane stabilization / reduced passive proton permeability — label-only mechanistic process
- proton-consuming decarboxylation
- macromolecule repair
- capsule/EPS barrier formation

## 3. Candidate causal edges

Evidence labels are **direct**, **mixed**, **review synthesis**, or **predicted**. “Curate” means suitable at the stated abstraction level; it does not imply universality across all acidophiles.

| # | Subject — predicate — object | Reference and supporting snippet | Curation note |
|---|---|---|---|
| 1 | low extracellular pH — increases — transmembrane proton gradient | Chong 2024: thermoacidophile extracellular conditions can be “3–5 pH units more acidic than the intracellular compartment.” (chong2024archaeamembranesin pages 3-4) | **Curate, high-level.** General physicochemical edge. |
| 2 | BTL-rich archaeal membrane — decreases — passive proton permeability | Chong 2024 reports PLFE permeability of **0.3–0.5 × 10⁻⁸ cm s⁻¹** at 65–82°C versus **3–9 × 10⁻⁸ cm s⁻¹** for egg-yolk phosphatidylcholine liposomes. (chong2024archaeamembranesin pages 2-3) | **Curate; direct model-membrane evidence.** Restrict to thermoacidophilic archaea/PLFE-like membranes. |
| 3 | hydroxyl-rich BTL headgroups — increases — membrane hydrogen-bond networks | The review states that BTL headgroups are rich in hydroxyl groups and form “extensive hydrogen bond networks” on both membrane surfaces. (chong2024archaeamembranesin pages 2-3) | **Curate as mechanistic intermediate; review synthesis.** |
| 4 | cyclopentane-ring addition to GDGT/GDNT — increases — membrane packing and rigidity | Eight-ring GDNT simulations reduced membrane volume **4.9%** and increased interaction energy **35 kcal mol⁻¹** relative to ring-free GDNT. (chong2024archaeamembranesin pages 3-4) | **Curate with computational-evidence qualifier.** |
| 5 | tighter/rigid membrane packing — decreases — proton permeability | Chong states that solute permeability, including proton permeability, decreases when packing is tighter and more rigid. (chong2024archaeamembranesin pages 3-4) | **Curate; supported by biophysical studies summarized in review.** |
| 6 | low passive proton permeability — supports — maintenance of intracellular pH | PLFE properties are described as essential for maintaining pH 2.5 outside and pH 6.5 inside in *S. acidocaldarius*. (chong2024archaeamembranesin pages 3-4) | **Curate, taxon-backed.** Organism-level causality remains partly synthetic. |
| 7 | near-neutral/slightly acidic intracellular pH — enables — intracellular protein and DNA activity | Intracellular pH 4.6–6.5 is described as essential for optimal activities of DNA and intracellular proteins. (chong2024archaeamembranesin pages 2-3) | **Curate at broad process level.** Avoid claiming all enzymes share the same optimum. |
| 8 | GrsA — catalyzes formation of — GDGT-1 through GDGT-4 | Chong 2024: “GrsA catalyzes the synthesis of the first four cyclopentane rings.” (chong2024archaeamembranesin pages 3-4) | **Curate only for organisms carrying characterized GrsA orthologs.** |
| 9 | GrsB — catalyzes formation of — additional GDGT rings 5–8 | Chong 2024: GrsB acts preferentially on GrsA products and generates GDGT-5–8. (chong2024archaeamembranesin pages 3-4) | **Curate only with species-specific protein grounding.** |
| 10 | decreasing environmental pH — associates with — increased GDGT cyclization/grs abundance | Cultivated and environmental lipid analyses generally found more rings as pH decreased; higher *grs* abundance/copy number occurred in more acidic environments. Contradictory datasets also exist. (chong2024archaeamembranesin pages 3-4) | **Uncertain association, not a universal causal edge.** Keep out of the core graph or annotate exceptions. |
| 11 | potassium uptake — generates — inside-positive membrane potential | Acidophile genomic models propose Kch/Kdp/Trk-driven positive potential as a proton-repelling barrier; removal of K+/Na+ lowered acid resistance in some *Sulfolobus* and *Acidithiobacillus*, but “definitive proof is still lacking.” (vergara2020evolutionofpredicted pages 1-3) | **Provisional.** Do not encode as universally demonstrated. |
| 12 | inside-positive membrane potential — decreases — proton influx | Comparative studies place this in the acidophile “first line of defense,” enabling near-neutral cytoplasm against an approximately 10⁵-fold proton gradient. (gonzalezrosales2022integrativegenomicssheds pages 1-2) | **Curate as proposed mechanism with uncertainty flag.** |
| 13 | respiratory-chain proton pumps / proton-coupled ATPases — exports — cytoplasmic protons | The authoritative review states that active pH homeostasis uses “proton-pumping respiratory chain complexes or proton-coupled ATPases.” (krulwich2011molecularaspectsof pages 3-5) | **Curate at process level.** Species-specific direction and complex must be verified experimentally. |
| 14 | cation/H+ antiporter — mediates — active proton transport | Cation/proton antiporters use proton-motive force generated by respiration or ATPases for coupled ion/proton transport. (krulwich2011molecularaspectsof pages 3-5) | **Curate only with transport direction defined for the organism and condition.** Antiporters do not automatically imply proton export. |
| 15 | glutamate decarboxylation — consumes — cytoplasmic proton | Acidithiobacillia comparative genomics lists glutamate decarboxylase among proton-consuming “second-line” mechanisms. (gonzalezrosales2022integrativegenomicssheds pages 1-2) | **Provisional/predicted in acidophiles.** Require enzyme activity, mutant, or flux evidence before a gene-level edge. |
| 16 | spermidine / alkaline cytoplasmic molecules — increases — proton buffering | Spermidine and alkaline amino acids are proposed to increase buffering capacity in acidophiles. (gonzalezrosales2022integrativegenomicssheds pages 1-2, vergara2020evolutionofpredicted pages 1-3) | **Provisional.** Separate buffering from membrane effects of polyamines. |
| 17 | hopanoid biosynthesis — stabilizes — bacterial membrane at low pH | Acidithiobacillia genomics links acquisition of hopanoid biosynthesis to membrane stabilization; low-pH growth defects after hopanoid deletion are reported mainly in other bacterial systems. (gonzalezrosales2022integrativegenomicssheds pages 1-2, vergara2020evolutionofpredicted pages 1-3) | **Provisional for acidophiles.** Stronger taxon-specific knockout evidence is needed. |
| 18 | Omp40 expression — modulates — outer-membrane proton influx | Omp40 increases under low pH in *Fervidacidithiobacillus caldus* and *Acidithiobacillus ferrooxidans*, “suggesting that it controls proton influx.” (gonzalezrosales2022integrativegenomicssheds pages 4-6) | **Uncertain inference from expression.** Do not curate as established transport direction. |
| 19 | Slp outer-membrane protein — decreases — organic-acid influx | The Acidithiobacillia analysis states that Slp prevents organic-acid flux across the outer membrane. (gonzalezrosales2022integrativegenomicssheds pages 4-6) | **Curate only as taxon-specific and organic-acid-specific.** It is not equivalent to blocking free protons. |
| 20 | capsule polysaccharide layer — decreases — harmful external-factor/proton influx | Capsule polysaccharides are described as a protective mechanical barrier that prevents proton influx. (gonzalezrosales2022integrativegenomicssheds pages 4-6) | **Provisional/mixed evidence.** Distinguish capsule from attached-mineral biofilm EPS. |
| 21 | chloride stress — disrupts — inside-positive membrane potential | Prior acidophile experiments summarized by Rivera-Araya et al. show that chloride-associated osmotic imbalance disrupts positive internal potential and promotes proton entry. (riveraaraya2019osmoticimbalancecytoplasm pages 1-2) | **Curate as a negative, stress-context edge.** |
| 22 | chloride-induced proton influx — decreases — cytoplasmic pH | In *Leptospirillum ferriphilum* DSM 14647, NaCl exposure reduced intracellular pH significantly from **6.7 to 5.5**. (riveraaraya2019osmoticimbalancecytoplasm pages 1-2) | **Curate; direct experiment, taxon- and assay-specific.** |
| 23 | chloride-induced cytoplasmic acidification — increases — respiration and oxidative stress | NaCl exposure significantly increased oxygen consumption and intracellular ROS; cytochrome-c peroxidase and thioredoxin activities and corresponding genes increased. (riveraaraya2019osmoticimbalancecytoplasm pages 1-2) | **Curate as a taxon-specific secondary-damage module.** |
| 24 | low proton influx + proton export/consumption/buffering — maintains — intracellular pH compatible with growth | Acidophilic sulfate reducers can maintain intracellular pH around 6 while growing below pH 3 through exclusion, exchange, pumping, consumption, and buffering. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | **Curate as the core convergent mechanism.** Component genes vary among lineages. |
| 25 | maintained intracellular pH — enables — acidophilic growth | This is the principal integrative phenotype edge supported across archaeal membrane, Acidithiobacillia, *Leptospirillum*, and sulfate-reducer literature. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2, chong2024archaeamembranesin pages 3-4) | **Core graph endpoint.** Phrase as “contributes to/enables,” not as a sufficient cause. |

The inspected structural figure corroborates the BTL module: macrocyclic GDGT/GDNT structures span the membrane, sugar/phosphate headgroups form hydrogen-bond networks, rings alter packing/free volume, and *S. acidocaldarius* PLFE liposomes show much smaller temperature-dependent volume fluctuations than DPPC. (chong2024archaeamembranesin media b55a9973)

## 4. Recommended initial TraitMech graph

A conservative first implementation should prioritize the following backbone:

1. `external_pH_below_5 -> increases -> transmembrane_proton_gradient`
2. `acidophile_membrane_barrier -> decreases -> passive_proton_influx`
3. `potassium_dependent_inside_positive_potential -> decreases -> proton_influx` **[uncertain; bacterial/archaeal subsets]**
4. `respiratory_proton_pumping -> decreases -> cytoplasmic_proton_load`
5. `proton_consuming_reactions -> decreases -> cytoplasmic_proton_load` **[taxon-specific]**
6. `cytoplasmic_buffering -> decreases -> change_in_cytoplasmic_pH`
7. `decreased_proton_influx -> contributes_to -> intracellular_pH_homeostasis`
8. `decreased_cytoplasmic_proton_load -> contributes_to -> intracellular_pH_homeostasis`
9. `intracellular_pH_homeostasis -> preserves -> macromolecular_function`
10. `preserved_macromolecular_function -> enables -> acidophilic_growth`
11. `chloride_stress -> disrupts -> inside_positive_membrane_potential` **[negative modifier]**
12. `chloride_stress -> increases -> cytoplasmic_acidification` **[taxon-specific]**

For an archaeal subgraph, add `GrsA/GrsB -> cyclopentane-ring formation -> tighter BTL packing -> lower passive proton permeability`. For a bacterial subgraph, use hopanoids, Omp40, Slp, capsule, Kch/Kdp/Trk, and decarboxylase nodes only with organism-level evidence annotations.

The following evidence-priority summary can guide YAML implementation:

| module | strongest candidate causal chain | evidence class | recommended curation status |
|---|---|---|---|
| Archaeal BTL membrane module | acidic external pH -> increased cyclopentane-ring content / altered GDNT:GDGT and headgroup composition in bipolar tetraether membranes -> tighter packing + stronger H-bond networks + lower passive proton permeability -> maintenance of near-neutral intracellular pH -> supports acidophilic growth (chong2024archaeamembranesin pages 3-4, chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 1-2, chong2024archaeamembranesin media b55a9973) | mixed: direct biophysical measurements in model membranes + review synthesis; organismal linkage largely review-based | curate core membrane-permeability chain now; keep specific regulators/composition shifts as provisional taxon-specific details |
| Bacterial membrane / inside-positive potential module | K+ uptake / Donnan potential -> inside-positive membrane potential -> electrostatic reduction of proton influx -> helps maintain circumneutral cytoplasmic pH -> supports acidophily (gonzalezrosales2022integrativegenomicssheds pages 1-2, vergara2020evolutionofpredicted pages 1-3) | comparative-genomic + review; limited direct support in related acidophiles, not universal proof | provisional; curate as candidate mechanism with uncertainty flag |
| Active proton export / consumption | respiratory-chain proton pumps / proton-coupled ATPases / cation-H+ antiporters and proton-consuming reactions -> proton extrusion or neutralization in cytoplasm -> pH homeostasis under low external pH -> supports acidophilic growth (krulwich2011molecularaspectsof pages 3-5, gonzalezrosales2022integrativegenomicssheds pages 1-2) | review synthesis with examples; some experimental support exists in microbes broadly, but acidophile-wide edge is generalized | curate high-level process edge now; avoid overcommitting to specific transporters unless taxon-specific evidence is added |
| Envelope barrier | outer membrane / surface barrier traits such as Omp40, Slp, capsule polysaccharides, membrane-stabilizing lipids -> reduced proton or organic-acid influx across cell envelope -> decreased cytoplasmic acidification -> supports acidophilic lifestyle (gonzalezrosales2022integrativegenomicssheds pages 4-6, gonzalezrosales2022integrativegenomicssheds pages 1-2) | mixed: comparative-genomic plus expression observations and review interpretation | curate envelope-barrier process node; gene-specific edges remain provisional |
| Chloride failure mode | chloride stress / osmotic imbalance -> disruption of positive internal membrane potential + proton influx -> cytoplasmic pH drop (6.7 to 5.5 in L. ferriphilum) + increased O2 consumption + ROS defense activation -> impaired acidophile physiology / limitation of acidophilic performance (riveraaraya2019osmoticimbalancecytoplasm pages 1-2) | direct experimental evidence in Leptospirillum ferriphilum | curate as taxon-backed negative/limiting module now, clearly marked as stress-context specific |
| Application-context nodes | acidophilic traits + pH-homeostasis mechanisms -> enable bioleaching, AMD treatment, sulfate reduction, and phenotype prediction/cultivation inference; examples include AMD bioreactors enriched from 0.0025%-0.0093% to 27.3%-87.0% Desulfosporosinus and genome-based prediction across 85,205 species (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, barnum2024predictingmicrobialgrowth pages 9-11, riveraaraya2019osmoticimbalancecytoplasm pages 1-2) | application review + computational preprint + experimental context | do not curate as core mechanistic trait edges; keep as contextual metadata / downstream application annotations |


*Table: This table prioritizes major mechanistic modules for curating the acidophilic microbial trait and distinguishes direct evidence from review- or comparative-genomic support. It is useful for deciding which edges are ready for TraitMech entry now versus which should remain provisional.*

## 5. Recent developments, applications, and statistics

### Archaeal membrane biophysics, 2024

The January 2024 review integrates lipidomics, simulations, and liposome experiments into a current model in which thermoacidophiles adjust cyclopentane-ring number, GDNT:GDGT ratio, tetraether:diether ratio, and headgroup glycosylation. The most compelling quantitative result is that *S. acidocaldarius* PLFE liposomes are roughly one order of magnitude less proton-permeable than phosphatidylcholine controls at 65–82°C. However, the review also documents non-monotonic and contradictory ring-versus-pH observations, so “lower pH causes more rings” is not yet a universal rule. (chong2024archaeamembranesin pages 3-4, chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 1-2)

### Acid mine drainage treatment and metal recovery, 2024

Acidophilic sulfate-reducing bacteria couple sulfate reduction to production of sulfide, which can precipitate dissolved metals from acid mine drainage. A 2024 review reports that *Desulfosporosinus* increased from **0.0025–0.0093%** in natural AMD inocula to **27.3–87.0%** in bioreactors operated at approximately pH 2.5–3.5 or using pH 2 sediment. Proposed outputs include treated wastewater, recovered metal sulfides, and metal-sulfide nanoparticles for electronics or biomedical applications. These are downstream applications, not core causal edges for acidophily. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

### Bioleaching under chloride stress

Iron- and sulfur-oxidizing acidophiles are used to mobilize metals from sulfide ores. Chloride limits many such systems by simultaneously imposing osmotic stress, collapsing the protective positive potential, acidifying the cytoplasm, and increasing ROS. The *L. ferriphilum* experiment used up to **150 mM NaCl** and provides a concrete failure-mode module for designing chloride-tolerant bioleaching strains or consortia. (riveraaraya2019osmoticimbalancecytoplasm pages 1-2)

### Genome-based prediction of pH preference, 2024

A March 2024 computational preprint trained growth-condition models using **15,596** bacterial and archaeal genomes and applied them to **85,205** sequenced species, approximately 70% of which were uncultivated. Reported pH-prediction performance reached R²≈0.79 in one cultivated-versus-uncultivated analysis, while predictions from genomes only 10% complete incurred about **0.4 pH-unit error**. This is useful for prioritizing cultivation experiments, but amino-acid composition is predictive rather than a causal mechanism and should not become a TraitMech edge. (barnum2024predictingmicrobialgrowth pages 9-11)

## 6. Expert interpretation

The literature supports **convergent physiology rather than one universal acidophile gene set**. Archaeal tetraether monolayers, bacterial hopanoid/envelope systems, ion-dependent electrical barriers, active transport, buffering, and proton-consuming metabolism can reach the same systems-level endpoint: controlled cytoplasmic proton activity. Comparative genomics indicates that acidophilic Acidithiobacillia evolved from inferred neutrophilic ancestors through gains, duplications, and functional redundancy in first- and second-line defenses, including horizontal transfer of many extreme-acid adaptations. (gonzalezrosales2022integrativegenomicssheds pages 1-2)

Accordingly, the YAML graph should distinguish:

- **core physicochemical edges**, which may be shared broadly;
- **lineage-specific realizations**, such as archaeal BTLs or bacterial hopanoids;
- **gene-presence predictions**, which are not equivalent to active mechanisms;
- **negative modifiers**, such as chloride;
- **downstream industrial applications**, which belong in contextual metadata rather than the core mechanism graph.

## 7. Warnings: claims not ready for TraitMech curation

1. Do not assert that every acidophile uses Kch/Kdp/Trk to establish an inside-positive potential. Direct definitive proof remains incomplete. (vergara2020evolutionofpredicted pages 1-3)
2. Do not infer function from gene presence alone in *Leptospirillum* or Acidithiobacillia; many proposed mechanisms derive from comparative genomics and phylogenetic reconstruction. (vergara2020evolutionofpredicted pages 16-17, vergara2020evolutionofpredicted pages 1-3)
3. Do not encode Omp40 as a proven proton channel or proton blocker. Increased expression at low pH supports involvement but not direction or molecular transport specificity. (gonzalezrosales2022integrativegenomicssheds pages 4-6)
4. Do not generalize the BTL/cyclopentane module to bacteria or to all archaea.
5. Do not encode decreasing pH as invariably increasing GDGT ring number; contradictory observations include a decline from 5.1 rings at pH 3 to 4.1 at pH 1.8 in one *Thermoplasma acidophilum* dataset. (chong2024archaeamembranesin pages 3-4)
6. Do not treat glutamate decarboxylase, urease, amino-acid antiporters, chaperones, or DNA repair as universal acidophily determinants without acidophile-specific perturbation or biochemical evidence.
7. Do not equate capsule, biofilm, and EPS. Evidence that a capsule limits influx does not prove that a mineral-attached biofilm causes intracellular pH homeostasis.
8. Do not use acid-mine-drainage abundance, a predicted pH optimum, or enrichment in a low-pH reactor as sole evidence that an organism satisfies **METPO:1003003**.
9. Do not treat acidophily as sufficient for metal tolerance, halotolerance, thermophily, sulfur oxidation, iron oxidation, or sulfate reduction; these are separable traits.
10. Do not ground uncertain metabolites or proteins with guessed CURIEs. Use label-only nodes until the exact chemical form, species, sequence, and database record are verified.

## DOI-first bibliography

1. Chong, P. L.-G. **“Archaea membranes in response to extreme acidic environments.”** *Frontiers in Biophysics* 1, published **4 January 2024**. DOI: [10.3389/frbis.2023.1338019](https://doi.org/10.3389/frbis.2023.1338019). (chong2024archaeamembranesin pages 1-2)
2. Valdez-Nuñez, L. F. et al. **“Acidophilic sulphate-reducing bacteria: Diversity, ecophysiology, and applications.”** *Environmental Microbiology Reports* 16, published **October 2024**. DOI: [10.1111/1758-2229.70019](https://doi.org/10.1111/1758-2229.70019). (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
3. Barnum, T. P. et al. **“Predicting microbial growth conditions from amino acid composition.”** *bioRxiv*, posted **March 2024**; preprint. DOI: [10.1101/2024.03.22.586313](https://doi.org/10.1101/2024.03.22.586313). (barnum2024predictingmicrobialgrowth pages 9-11)
4. González-Rosales, C. et al. **“Integrative Genomics Sheds Light on Evolutionary Forces Shaping the Acidithiobacillia Class Acidophilic Lifestyle.”** *Frontiers in Microbiology* 12, published **February 2022**. DOI: [10.3389/fmicb.2021.822229](https://doi.org/10.3389/fmicb.2021.822229). (gonzalezrosales2022integrativegenomicssheds pages 1-2)
5. Vergara, E. et al. **“Evolution of Predicted Acid Resistance Mechanisms in the Extremely Acidophilic Leptospirillum Genus.”** *Genes* 11:389, published **April 2020**. DOI: [10.3390/genes11040389](https://doi.org/10.3390/genes11040389). (vergara2020evolutionofpredicted pages 16-17)
6. Rivera-Araya, J. et al. **“Osmotic Imbalance, Cytoplasm Acidification and Oxidative Stress Induction Support the High Toxicity of Chloride in Acidophilic Bacteria.”** *Frontiers in Microbiology* 10:2455, published **29 October 2019**. DOI: [10.3389/fmicb.2019.02455](https://doi.org/10.3389/fmicb.2019.02455). (riveraaraya2019osmoticimbalancecytoplasm pages 1-2)
7. Krulwich, T. A., Sachs, G. & Padan, E. **“Molecular aspects of bacterial pH sensing and homeostasis.”** *Nature Reviews Microbiology* 9:330–343, published **May 2011**. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). This is the supplied existing evidence source and supports the pH 1–3 extreme-acidophile boundary and active transport framework. (krulwich2011molecularaspectsof pages 3-5)

References

1. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (gonzalezrosales2022integrativegenomicssheds pages 1-2): Carolina González-Rosales, Eva Vergara, Mark Dopson, Jorge H. Valdés, and David S. Holmes. Integrative genomics sheds light on evolutionary forces shaping the acidithiobacillia class acidophilic lifestyle. Frontiers in Microbiology, Feb 2022. URL: https://doi.org/10.3389/fmicb.2021.822229, doi:10.3389/fmicb.2021.822229. This article has 31 citations and is from a peer-reviewed journal.

3. (chong2024archaeamembranesin pages 2-3): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

4. (chong2024archaeamembranesin pages 3-4): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

5. (chong2024archaeamembranesin pages 1-2): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

6. (vergara2020evolutionofpredicted pages 1-3): Eva Vergara, Gonzalo Neira, Carolina González, Diego Cortez, Mark Dopson, and David S. Holmes. Evolution of predicted acid resistance mechanisms in the extremely acidophilic leptospirillum genus. Genes, 11:389, Apr 2020. URL: https://doi.org/10.3390/genes11040389, doi:10.3390/genes11040389. This article has 40 citations.

7. (gonzalezrosales2022integrativegenomicssheds pages 4-6): Carolina González-Rosales, Eva Vergara, Mark Dopson, Jorge H. Valdés, and David S. Holmes. Integrative genomics sheds light on evolutionary forces shaping the acidithiobacillia class acidophilic lifestyle. Frontiers in Microbiology, Feb 2022. URL: https://doi.org/10.3389/fmicb.2021.822229, doi:10.3389/fmicb.2021.822229. This article has 31 citations and is from a peer-reviewed journal.

8. (riveraaraya2019osmoticimbalancecytoplasm pages 1-2): Javier Rivera-Araya, Andre Pollender, Dieu Huynh, Michael Schlömann, Renato Chávez, and Gloria Levicán. Osmotic imbalance, cytoplasm acidification and oxidative stress induction support the high toxicity of chloride in acidophilic bacteria. Frontiers in Microbiology, Oct 2019. URL: https://doi.org/10.3389/fmicb.2019.02455, doi:10.3389/fmicb.2019.02455. This article has 56 citations and is from a peer-reviewed journal.

9. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 18 citations and is from a peer-reviewed journal.

10. (chong2024archaeamembranesin media b55a9973): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

11. (barnum2024predictingmicrobialgrowth pages 9-11): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

12. (vergara2020evolutionofpredicted pages 16-17): Eva Vergara, Gonzalo Neira, Carolina González, Diego Cortez, Mark Dopson, and David S. Holmes. Evolution of predicted acid resistance mechanisms in the extremely acidophilic leptospirillum genus. Genes, 11:389, Apr 2020. URL: https://doi.org/10.3390/genes11040389, doi:10.3390/genes11040389. This article has 40 citations.