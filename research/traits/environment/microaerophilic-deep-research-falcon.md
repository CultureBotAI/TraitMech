---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:08:08.627473'
end_time: '2026-08-04T01:15:26.069168'
duration_seconds: 437.44
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: microaerophilic
  trait_identifier: METPO:1000604
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: microaerophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference that requires molecular oxygen (O\u2082) at concentrations\
    \ lower than atmospheric."
  parent_traits: METPO:1000601
  synonyms: Ox_microerophile, microaerophile
  evidence_summary: 'https://www.ncbi.nlm.nih.gov/books/NBK154539/: require oxygen
    to survive but require its presence in lower concentrations (Supports microaerophily
    as oxygen requirement below atmospheric concentration.) | PMID:26284041: C. jejuni
    is a microaerophilic, fastidious bacterium (Organism example: Campylobacter jejuni
    is described as microaerophilic.)'
  causal_graph_summary: 'microaerophile_low_oxygen_respiration: 14 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** microaerophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000604
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that requires molecular oxygen (O₂) at concentrations lower than atmospheric.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_microerophile, microaerophile
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK154539/: require oxygen to survive but require its presence in lower concentrations (Supports microaerophily as oxygen requirement below atmospheric concentration.) | PMID:26284041: C. jejuni is a microaerophilic, fastidious bacterium (Organism example: Campylobacter jejuni is described as microaerophilic.)
- **Existing causal graph summary:** microaerophile_low_oxygen_respiration: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **microaerophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/microaerophilic.yaml`.

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
- **Trait label:** microaerophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000604
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that requires molecular oxygen (O₂) at concentrations lower than atmospheric.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_microerophile, microaerophile
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK154539/: require oxygen to survive but require its presence in lower concentrations (Supports microaerophily as oxygen requirement below atmospheric concentration.) | PMID:26284041: C. jejuni is a microaerophilic, fastidious bacterium (Organism example: Campylobacter jejuni is described as microaerophilic.)
- **Existing causal graph summary:** microaerophile_low_oxygen_respiration: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **microaerophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/microaerophilic.yaml`.

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


# Curation report: microaerophilic (`METPO:1000604`)

## Executive summary

The trait denotes an **oxygen preference requiring molecular oxygen but at concentrations below atmospheric oxygen**. It is best modeled not as one universal pathway, but as an emergent phenotype produced by: (i) a low-O₂ habitat or assay atmosphere; (ii) oxygen/redox sensing; (iii) high-affinity terminal respiration; (iv) proton-motive-force and ATP generation; and (v) protection of oxygen-sensitive enzymes and mitigation of reactive oxygen species (ROS).

The strongest compact TraitMech backbone is:

**low O₂ → oxygen/redox sensor → high-affinity terminal oxidase → O₂ reduction to water → proton-motive force → ATP production → growth under sub-atmospheric O₂**, with an auxiliary branch **excess O₂/respiration → ROS → antioxidant defenses**. However, the specific sensors, oxidases, electron donors, and defenses vary sharply among taxa. FNR/FixLJ and `fixNOQP` evidence should therefore not be asserted universally across all microaerophiles. (price2021bacterialapproachesto pages 4-6, ledermann2021howrhizobiaadapt pages 4-6, borisov2021bacterialoxidasesof pages 1-2)

## 1. Trait scope and boundary conditions

### In scope

`METPO:1000604` should represent a reproducible physiological phenotype in which:

1. O₂ is required for optimal growth, survival, or respiratory energy conservation; and
2. the optimum or permitted range lies below air-equilibrated conditions.

The mechanistic core is often high-affinity oxygen respiration. For example, rhizobial FixNOQP has an apparent O₂ *K*m of 4–7 nM and supports respiration in nodules containing approximately 11 nM free O₂. By comparison, the cited review gives approximately 255 µM dissolved O₂ for water equilibrated with atmospheric oxygen. (ledermann2021howrhizobiaadapt pages 4-6)

### Important boundary cases

- **Microaerophilic versus obligately anaerobic:** obligate anaerobes do not require O₂. Possession of cytochrome bd or measurable O₂ consumption by an organism classified as anaerobic may provide oxygen scavenging, stress protection, or limited energy gain; it does not by itself establish microaerophily. (borisov2021bacterialoxidasesof pages 18-19)
- **Microaerophilic versus aerotolerant anaerobic:** an aerotolerant organism benefits from or withstands oxygen without requiring it for growth. Oxygen tolerance alone is therefore insufficient.
- **Microaerophilic versus facultatively anaerobic:** *E. coli* can induce cytochrome bd at intermediate O₂, but this is a condition-dependent microaerobic program in a facultative organism, not necessarily a species-level microaerophilic preference. (borisov2021bacterialoxidasesof pages 18-19)
- **Microaerophilic versus capnophilic:** elevated CO₂ and reduced O₂ are separate environmental variables, even though clinical culture systems frequently alter both. CO₂ enrichment must not be treated as evidence of an oxygen requirement.
- **Microaerophilic versus oxygen-sensitive:** oxygen-sensitive nitrogenase helps explain why diazotrophs need low O₂, but nitrogenase sensitivity alone does not imply that the whole organism is microaerophilic. (alleman2023mechanismsforgenerating pages 7-9, ledermann2021howrhizobiaadapt pages 4-6)
- **Preference versus assay condition:** growth at 5% O₂ is not sufficient evidence unless compared with anoxia and atmospheric O₂. A curation-quality phenotype should record gas composition, dissolved O₂ when available, medium, vessel geometry, agitation, temperature, growth endpoint, and taxon/strain.

## 2. Candidate nodes grouped by type

### Trait and environmental nodes

- microaerophilic — `METPO:1000604`
- parent trait — `METPO:1000601`
- molecular oxygen — `CHEBI:15379`
- low molecular-oxygen concentration — label-only candidate; represent as a concentration-qualified environmental state rather than inventing a CURIE
- atmospheric oxygen exposure — label-only candidate
- microoxic root-nodule environment — label-only candidate
- nodule oxygen-diffusion barrier — label-only candidate
- host gastric-mucosal microenvironment — label-only candidate
- experimental microaerophilic atmosphere — label-only candidate; attach explicit gas percentages as assay metadata

### Sensors and regulatory modules

- FNR oxygen-responsive transcriptional regulator — label-only until a taxon-specific protein identifier is selected
- FixL/FixJ two-component oxygen-sensing system — label-only/taxon-specific
- FixK/Fnr-family downstream regulator — label-only/taxon-specific
- NifA nitrogen-fixation regulator — label-only/taxon-specific
- ArcB/ArcA redox-responsive two-component system — label-only; primarily a facultative-bacterium context
- Rex NADH/NAD⁺-responsive regulator — label-only; indirect respiratory/redox-state node
- HsrA essential response regulator in *Helicobacter pylori* — label-only until strain-specific grounding
- CagA — label-only in this graph unless a strain-specific UniProt entry is chosen

FNR uses an Fe–S cluster, whereas FixL uses heme-associated oxygen sensing; the 2021 review explicitly describes these systems as directly sensing low O₂ and prioritizing high-affinity oxidases or alternative electron acceptors. (price2021bacterialapproachesto pages 4-6)

### Respiratory proteins and complexes

- `fixNOQP` operon
- cbb₃-type cytochrome-*c* oxidase / FixNOQP complex
- cytochrome bd quinol oxidase / `cydAB`
- cytochrome bd assembly/export system / `cydDC`
- quinone/quinol pool — label-only unless a taxon-specific quinone is established
- respiratory electron-transport chain
- proton-motive force
- oxidative phosphorylation
- ATP synthesis
- hydrogenase and molecular-hydrogen oxidation — taxon-specific auxiliary module for *H. pylori*

FixNOQP is supported as a high-affinity cbb₃ oxidase responsible for rhizobial microaerobic respiration. Cytochrome bd is a quinol:oxygen oxidoreductase that reduces O₂ to water at submicromolar concentrations and generates proton motive force used for ATP production, although it is not itself a classical proton pump. (ledermann2021howrhizobiaadapt pages 4-6, borisov2021bacterialoxidasesof pages 1-2)

### Oxygen-sensitive and protective modules

- nitrogenase complex
- nitrogenase Fe–S clusters
- biological nitrogen fixation
- respiratory protection of nitrogenase
- reactive oxygen species — class node; do not substitute a single chemical without evidence
- hydrogen peroxide — `CHEBI:16240`
- superoxide dismutase
- catalase
- glutathione and glutathione-dependent defenses
- peroxiredoxin/alkyl-hydroperoxide reductase — candidate only; no sufficiently specific edge was recovered here
- protein-quality-control protease ClpP — recent *C. jejuni* persistence context, not established as a microaerophily determinant

Across 18 transcriptome and one proteome data sets reviewed for rhizobial bacteroids, superoxide dismutases and catalases were commonly upregulated, consistent with ROS generated by auto-oxidation of leghemoglobin and ferredoxin. Glutathione-deficient mutants showed reduced symbiotic efficiency. These are strong low-O₂-nodule adaptation observations but not universal microaerophile markers. (ledermann2021howrhizobiaadapt pages 4-6)

### Chemicals and metabolic entities

- molecular oxygen — `CHEBI:15379`; terminal electron acceptor
- water — product of terminal oxygen reduction
- molecular hydrogen — electron donor in the *H. pylori* auxiliary pathway
- NADH and NAD⁺ — respiratory/redox-state indicators
- menaquinone/quinol — taxon-dependent electron carrier
- C₄-dicarboxylates — plant-supplied bacteroid carbon and energy substrates
- dinitrogen and ammonia/ammonium — nitrogenase substrate and product context
- nitric oxide, peroxynitrite, hydrogen sulfide, and hydrogen peroxide — respiratory inhibitors or stressors relevant to cytochrome bd

## 3. Candidate evidence-backed causal edges

The following table is the curation-ready edge set. “High” means the relation is directly stated and supported by biochemical or genetic evidence summarized in an authoritative source. It does not mean the edge is taxonomically universal.

| # | subject | predicate | object | taxon/context | evidence snippet | DOI/date | confidence/curation note |
|---|---|---|---|---|---|---|---|
| 1 | low molecular oxygen (CHEBI:15379) | is directly sensed by | FNR | general bacterial low-O2 sensing | “FNR and FixLJ, that utilize an FeS cluster and heme, respectively, to directly sense the low levels of O2” (price2021bacterialapproachesto pages 4-6) | 10.1111/mmi.14795 / 2021-08 | High for regulator function; review-level; not a universal microaerophile marker |
| 2 | low molecular oxygen (CHEBI:15379) | is directly sensed by | FixLJ two-component system | rhizobia and related microoxic adaptation | “FNR and FixLJ, that utilize an FeS cluster and heme, respectively, to directly sense the low levels of O2” (price2021bacterialapproachesto pages 4-6) | 10.1111/mmi.14795 / 2021-08 | High for sensing claim; review-level; taxon-distributed, not universal |
| 3 | low molecular oxygen (CHEBI:15379) | favors use of | high-affinity cytochrome oxidases | general respiratory adaptation | “to prioritize usage of cytochrome oxidases with high affinity for O2” (price2021bacterialapproachesto pages 4-6) | 10.1111/mmi.14795 / 2021-08 | Moderate-high; review-level; generic mechanistic edge |
| 4 | fixNOQP-encoded cbb3-type cytochrome c oxidase | enables | respiration under microaerobic conditions | rhizobia | “a cytochrome c oxidase, encoded by fixNOQP, is a high-affinity cbb3-type oxidase responsible for respiration under microaerobic conditions in rhizobia” (ledermann2021howrhizobiaadapt pages 4-6) | 10.1128/JB.00539-20 / 2021-05 | High; strong curation candidate; rhizobial-specific |
| 5 | fixNOQP / cbb3-type cytochrome c oxidase | has substrate affinity | O2 Km 4–7 nM | Bradyrhizobium/rhizobial membranes | “Biochemical assays revealed a Km value of 4 to 7 nM for oxygen… corresponding to the cbb3-type cytochrome oxidase FixNOQP” (ledermann2021howrhizobiaadapt pages 4-6) | 10.1128/JB.00539-20 / 2021-05 | High; quantitative and highly useful; taxon/context-specific |
| 6 | nodule oxygen diffusion barrier | decreases availability of | free oxygen (~11 nM) | legume root nodule microoxic environment | “the nodule cortex therefore contains an oxygen diffusion barrier… creating a microoxic environment of around 11 nM free oxygen” (ledermann2021howrhizobiaadapt pages 4-6) | 10.1128/JB.00539-20 / 2021-05 | High; environmental context edge |
| 7 | molecular oxygen (CHEBI:15379) | damages | nitrogenase iron-sulfur clusters | diazotrophic bacteroids | “The iron-sulfur clusters of the nitrogenase enzyme are highly susceptible to molecular oxygen” (ledermann2021howrhizobiaadapt pages 4-6) | 10.1128/JB.00539-20 / 2021-05 | High; foundational mechanistic edge |
| 8 | fixNOQP mutant | decreases | nitrogenase activity | Bradyrhizobium japonicum | “Mutants of fixNOQP in Bradyrhizobium japonicum had only marginal nitrogenase activity” (ledermann2021howrhizobiaadapt pages 4-6) | 10.1128/JB.00539-20 / 2021-05 | High; genetic evidence; taxon-specific phenotype |
| 9 | cytochrome bd quinol oxidase | reduces | O2 to H2O and generates proton motive force | many prokaryotes | “Its primary role is to couple the reduction of molecular oxygen, even at submicromolar concentrations, to water with the generation of a proton motive force used for adenosine triphosphate production” (borisov2021bacterialoxidasesof pages 1-2) | 10.1089/ars.2020.8039 / 2021-06 | High; review-level but central mechanistic edge |
| 10 | cytochrome bd deficiency (cyd mutant / lacking cytochrome bd) | increases susceptibility to | hydrogen peroxide (CHEBI:16240) | E. coli and other bacteria incl. pathogens in microaerobic environments | “Mutant E. coli cells lacking cytochrome bd… showed high susceptibility to H2O2” (borisov2021bacterialoxidasesof pages 18-19) | 10.1089/ars.2020.8039 / 2021-06 | High; review-level summarizing genetic studies; not universal magnitude |
| 11 | cytochrome bd | contributes to respiratory protection of | nitrogenase activity | diazotrophs; A. vinelandii/K. pneumoniae/Azorhizobium | “The hypothesis of respiratory protection, specifically by cytochrome bd, is widely accepted” (borisov2021bacterialoxidasesof pages 18-19) | 10.1089/ars.2020.8039 / 2021-06 | Moderate-high; accepted review claim but mechanism details still debated |
| 12 | cytochrome bd + cytochrome cbb3 double loss | abolishes | symbiotic N2 fixation | Azorhizobium caulinodans root nodule symbiosis | “both cytochrome bd and cytochrome cbb3 contribute equally to nitrogen fixation in root nodule symbiosis; the double mutant totally lacked symbiotic N2 fixation” (borisov2021bacterialoxidasesof pages 18-19) | 10.1089/ars.2020.8039 / 2021-06 | High; strong genetic evidence; taxon-specific |
| 13 | H2 oxidation | feeds electrons into | cbb3/O2 respiratory chain | Helicobacter pylori microaerophilic respiration | “The pathway involves a proton-pumping cytochrome cbb3 oxidase that reduces O2 to water… H. pylori couples H2 oxidation to O2 reduction” (benoit2020molecularhydrogenmetabolism pages 16-18) | 10.1128/MMBR.00092-19 / 2020-02 | Moderate; extracted from review summary; useful but indirect wording from evidence context |
| 14 | HsrA inhibition | disrupts | respiratory chain / ATP generation and induces oxidative stress | Helicobacter pylori; drug action context | “inhibition of HsrA triggers lethal global disturbances in H. pylori physiology including… malfunction of respiratory chain, detriment in ATP generation, and oxidative stress” (casado2024noveldruglikehsra pages 1-2) | 10.3390/ijms251810175 / 2024-09-22 | Moderate-high; recent and relevant, but intervention-specific rather than native trait mechanism |
| 15 | cagA | modulates | repression of electron transport-associated genes | Helicobacter pylori during host-cell coculture | “We observed a general repression of electron transport-associated genes by cagA” (hu2024dualrnasequencing pages 1-2) | 10.1128/mSystems.00206-24 / 2024-03-22 | Moderate; host-interaction-specific transcriptional effect, not direct core microaerophily edge |
| 16 | altering oxygen concentration in H. pylori growth environment | may inhibit survival of | Helicobacter pylori | therapeutic proposal | “altering the oxygen environment in gastric juice for H. pylori to not be able to survive is a hot topic” (huang2024noveltherapeuticregimens pages 1-2) | 10.3389/fmicb.2024.1418129 / 2024-06-07 | Low-moderate; review/proposed intervention, should not be curated as a native causal edge without direct experimental support |


*Table: This table compiles the strongest source-backed candidate causal edges for curating a microaerophilic TraitMech graph. It emphasizes mechanistic respiratory, sensing, and oxidative-stress relationships while flagging review-level, taxon-specific, and intervention-specific claims.*

### Recommended minimal graph

For an initial conservative revision of `microaerophile_low_oxygen_respiration`, prioritize these edges:

1. low O₂ **is sensed by** an oxygen/redox-sensing regulator;
2. oxygen/redox sensing **increases use or expression of** a high-affinity terminal oxidase;
3. high-affinity terminal oxidase **reduces** O₂ **to** water;
4. terminal oxygen reduction **supports generation of** proton-motive force;
5. proton-motive force **supports** ATP production;
6. ATP production under limiting O₂ **supports** microaerophilic growth;
7. elevated respiratory oxygen exposure **increases risk of** ROS stress;
8. antioxidant defenses **decrease** ROS toxicity.

Edges 1 and 2 require taxon-specific implementations. In rhizobia, FixLJ/FixK-NifA and FixNOQP are appropriate; in other taxa they may be absent. Cytochrome bd is a valuable alternative branch but should not be made mandatory because many microaerophiles rely on other terminal oxidases. (price2021bacterialapproachesto pages 4-6, ledermann2021howrhizobiaadapt pages 4-6, borisov2021bacterialoxidasesof pages 1-2)

## 4. Recent developments, applications, and real-world implementation

### Host-associated pathogen adaptation

A 2024 dual-RNA-sequencing study of *H. pylori* interacting with gastric epithelial cells found that CagA modulated a general repression of electron-transport-associated genes and altered oxidative-phosphorylation behavior. This is evidence that respiratory remodeling participates in host adaptation, but it is a coculture- and virulence-factor-specific response rather than a general cause of microaerophily. The paper was published on 22 March 2024. (hu2024dualrnasequencing pages 1-2)

### Respiratory regulation as an antimicrobial target

HsrA inhibitors reported on 22 September 2024 had MICs of 0.031–4 mg/L against antibiotic-resistant *H. pylori* strains. Transcriptomics associated HsrA inhibition with respiratory-chain malfunction, impaired ATP generation, and oxidative stress; the strongest compound also acted against *Campylobacter jejuni*. This supports respiratory regulation as a practical antimicrobial vulnerability in microaerophilic Campylobacterota, but drug perturbation should be represented in a separate intervention graph rather than as a defining native-trait edge. (casado2024noveldruglikehsra pages 1-2)

A separate 2024 multi-omics program applied the PISA-express assay to bacteria to resolve target-specific and off-target responses to candidate *H. pylori* flavodoxin inhibitors. It identifies flavodoxin, menaquinone synthesis, urease, and respiratory complexes as candidate pathogen-selective targets. The study also cites an estimated worldwide *H. pylori* prevalence of 44.3% and resistance exceeding 30% for clarithromycin, metronidazole, and levofloxacin in a US meta-analysis; these numbers describe clinical motivation, not the microaerophilic mechanism. (maity2024mergingmultiomicswith pages 1-4)

### Manipulation of oxygen as therapy

A systematic review published on 7 June 2024 described alteration of gastric oxygen concentration as an emerging strategy intended to make the environment unsuitable for *H. pylori*. The authors characterize this as promising or a “hot topic,” not as an established clinical treatment. It should therefore be retained as a hypothesis/application note and not curated as a proven causal edge. (huang2024noveltherapeuticregimens pages 1-2)

### Agriculture and biological nitrogen fixation

The best quantitatively resolved real-world implementation is the legume–rhizobium nodule. The plant oxygen-diffusion barrier maintains approximately 11 nM free O₂, protecting nitrogenase while high-affinity FixNOQP, with an apparent O₂ *K*m of 4–7 nM, sustains oxidative phosphorylation. `fixNOQP` mutants of *Bradyrhizobium japonicum* retain only marginal nitrogenase activity. This system is directly relevant to rhizobial inoculant selection and engineering for sustainable nitrogen fixation. (alleman2023mechanismsforgenerating pages 7-9, ledermann2021howrhizobiaadapt pages 4-6)

### Cytochrome bd as a drug and biotechnology target

Cytochrome bd is uniquely prokaryotic, contributes to growth under hypoxia and resistance to H₂O₂, NO, peroxynitrite, and H₂S, and has therefore attracted antibacterial interest. Yet its distribution extends to facultative organisms and organisms conventionally called anaerobes, so it is neither necessary nor sufficient as a diagnostic marker of `METPO:1000604`. (borisov2021bacterialoxidasesof pages 1-2, borisov2021bacterialoxidasesof pages 18-19)

## 5. Expert interpretation

The literature supports a **systems-level rather than single-gene definition**. High-affinity oxidases are the most portable mechanistic feature, but even they are not uniquely diagnostic. Oxygen preference emerges from the balance between respiratory energy yield, oxygen influx and consumption, ROS burden, repair capacity, and sensitivity of key metalloproteins.

The rhizobial model illustrates the central physiological paradox particularly well: O₂ is needed for efficient ATP production, while nitrogenase Fe–S clusters are highly oxygen-sensitive. The host diffusion barrier and bacterial high-affinity respiration jointly resolve this conflict. (ledermann2021howrhizobiaadapt pages 4-6)

The cytochrome-bd literature also cautions against treating all oxygen consumption as energy-coupled microaerophily. Proposed roles in nominal anaerobes include oxygen scavenging, survival energy, and dissipation of excess reducing power. Moreover, respiratory protection of nitrogenase is widely accepted, but the review explicitly notes continuing uncertainty over mechanistic details and contributions from redox state, ATP provision, oxygen regulation, and extracellular diffusion barriers. (borisov2021bacterialoxidasesof pages 18-19)

## 6. Warnings: claims not yet suitable for TraitMech curation

1. **Do not assert a universal O₂ percentage.** “Microaerophilic” is operational and taxon/assay dependent. Gas-phase percentage is not equivalent to dissolved O₂.
2. **Do not make FNR, FixLJ, NifA, ArcBA, `fixNOQP`, or `cydAB` necessary components of every microaerophile.** Their evidence is strong but lineage-specific.
3. **Do not infer the trait from genome presence alone.** A high-affinity oxidase can support facultative microaerobic growth, oxygen scavenging in anaerobes, or stress resistance.
4. **Do not conflate cytochrome bd with a proton pump.** It generates proton motive force through scalar chemistry and charge separation but is not a classical proton-pumping oxidase. (borisov2021bacterialoxidasesof pages 1-2)
5. **Do not curate CagA → microaerophily.** The 2024 evidence concerns host-cell-associated respiratory transcriptional remodeling. (hu2024dualrnasequencing pages 1-2)
6. **Do not curate HsrA inhibition or oxygen manipulation as native trait causes.** These belong in drug/intervention graphs. (casado2024noveldruglikehsra pages 1-2, huang2024noveltherapeuticregimens pages 1-2)
7. **Do not promote the 2024 *C. jejuni* ClpP persistence finding into the core graph.** The work links `clpP` to antibiotic persistence and colonization through metabolic downshift, not specifically to the oxygen-preference phenotype; it is also a preprint. (feng2024proteinqualitycontrol pages 1-4)
8. **Treat H₂ oxidation as an auxiliary, taxon-specific electron-donor branch.** Its estimated proton stoichiometry in *H. pylori* remains unproven. (benoit2020molecularhydrogenmetabolism pages 16-18)
9. **Ground proteins at the correct taxonomic level.** UniProt identifiers should be added only after selecting an organism and strain; cross-species label reuse can obscure paralogy and subunit differences.
10. **Preserve evidence modality.** Separate direct biochemistry, mutant phenotypes, transcriptomics, reviews, and therapeutic proposals in YAML provenance fields.

## DOI-first bibliography

1. Alleman AB, Peters JW. “Mechanisms for Generating Low Potential Electrons across the Metabolic Diversity of Nitrogen-Fixing Bacteria.” *Applied and Environmental Microbiology*. Published May 2023. DOI: [10.1128/aem.00378-23](https://doi.org/10.1128/aem.00378-23). (alleman2023mechanismsforgenerating pages 7-9)
2. Mele BH et al. “Oxidoreductases and metal cofactors in the functioning of the earth.” *Essays in Biochemistry* 67:653–670. Published August 2023. DOI: [10.1042/EBC20230012](https://doi.org/10.1042/EBC20230012). (mele2023oxidoreductasesandmetal pages 16-17)
3. Hu W et al. “Dual RNA sequencing of *Helicobacter pylori* and host cell transcriptomes reveals ontologically distinct host-pathogen interaction.” *mSystems* 9. Published 22 March 2024. DOI: [10.1128/msystems.00206-24](https://doi.org/10.1128/msystems.00206-24). (hu2024dualrnasequencing pages 1-2)
4. Huang T-T, Cao Y-X, Cao L. “Novel therapeutic regimens against *Helicobacter pylori*: an updated systematic review.” *Frontiers in Microbiology* 15:1418129. Published 7 June 2024. DOI: [10.3389/fmicb.2024.1418129](https://doi.org/10.3389/fmicb.2024.1418129). (huang2024noveltherapeuticregimens pages 1-2)
5. Casado J et al. “Novel Drug-like HsrA Inhibitors Exhibit Potent Narrow-Spectrum Antimicrobial Activities against *Helicobacter pylori*.” *International Journal of Molecular Sciences* 25:10175. Published 22 September 2024. DOI: [10.3390/ijms251810175](https://doi.org/10.3390/ijms251810175). (casado2024noveldruglikehsra pages 1-2)
6. Feng J et al. “Protein quality control modulates the metabolic conservation in antibiotic tolerant *Campylobacter jejuni*.” bioRxiv preprint. Posted 15 July 2024. DOI: [10.1101/2024.07.15.603561](https://doi.org/10.1101/2024.07.15.603561). (feng2024proteinqualitycontrol pages 1-4)
7. Price EE, Román-Rodríguez F, Boyd JM. “Bacterial approaches to sensing and responding to respiration and respiration metabolites.” *Molecular Microbiology* 116:1009–1021. Published August 2021. DOI: [10.1111/mmi.14795](https://doi.org/10.1111/mmi.14795). (price2021bacterialapproachesto pages 4-6)
8. Ledermann R, Schulte CCM, Poole PS. “How Rhizobia Adapt to the Nodule Environment.” *Journal of Bacteriology* 203. Published May 2021. DOI: [10.1128/JB.00539-20](https://doi.org/10.1128/JB.00539-20). (ledermann2021howrhizobiaadapt pages 4-6)
9. Borisov VB et al. “Bacterial Oxidases of the Cytochrome bd Family: Redox Enzymes of Unique Structure, Function, and Utility As Drug Targets.” *Antioxidants & Redox Signaling* 34:1280–1318. Published June 2021. DOI: [10.1089/ars.2020.8039](https://doi.org/10.1089/ars.2020.8039). (borisov2021bacterialoxidasesof pages 1-2, borisov2021bacterialoxidasesof pages 18-19)
10. Benoit SL, Maier RJ, Sawers RG, Greening C. “Molecular Hydrogen Metabolism: a Widespread Trait of Pathogenic Bacteria and Protists.” *Microbiology and Molecular Biology Reviews* 84. Published February 2020. DOI: [10.1128/MMBR.00092-19](https://doi.org/10.1128/MMBR.00092-19). (benoit2020molecularhydrogenmetabolism pages 16-18)

## Curation recommendation

Expand the existing 14-node/10-edge graph around a **generic high-affinity low-O₂ respiratory backbone**, then place FixLJ/FNR–FixNOQP, cytochrome bd, rhizobial nitrogenase protection, and *H. pylori* H₂ respiration in explicitly taxon-scoped modules. The most defensible new quantitative annotations are **nodule free O₂ ≈11 nM**, **FixNOQP apparent O₂ *K*m 4–7 nM**, and the **marginal nitrogenase activity of *B. japonicum fixNOQP* mutants**. (ledermann2021howrhizobiaadapt pages 4-6)

References

1. (price2021bacterialapproachesto pages 4-6): Erin E. Price, Franklin Román‐Rodríguez, and Jeffrey M. Boyd. Bacterial approaches to sensing and responding to respiration and respiration metabolites. Molecular Microbiology, 116:1009-1021, Aug 2021. URL: https://doi.org/10.1111/mmi.14795, doi:10.1111/mmi.14795. This article has 16 citations and is from a domain leading peer-reviewed journal.

2. (ledermann2021howrhizobiaadapt pages 4-6): Raphael Ledermann, Carolin C. M. Schulte, and Philip S. Poole. How rhizobia adapt to the nodule environment. May 2021. URL: https://doi.org/10.1128/jb.00539-20, doi:10.1128/jb.00539-20. This article has 112 citations and is from a peer-reviewed journal.

3. (borisov2021bacterialoxidasesof pages 1-2): Vitaliy B. Borisov, Sergey A. Siletsky, Alessandro Paiardini, David Hoogewijs, Elena Forte, Alessandro Giuffrè, and Robert K. Poole. Bacterial oxidases of the cytochrome<i>bd</i>family: redox enzymes of unique structure, function, and utility as drug targets. Jun 2021. URL: https://doi.org/10.1089/ars.2020.8039, doi:10.1089/ars.2020.8039. This article has 149 citations and is from a domain leading peer-reviewed journal.

4. (borisov2021bacterialoxidasesof pages 18-19): Vitaliy B. Borisov, Sergey A. Siletsky, Alessandro Paiardini, David Hoogewijs, Elena Forte, Alessandro Giuffrè, and Robert K. Poole. Bacterial oxidases of the cytochrome<i>bd</i>family: redox enzymes of unique structure, function, and utility as drug targets. Jun 2021. URL: https://doi.org/10.1089/ars.2020.8039, doi:10.1089/ars.2020.8039. This article has 149 citations and is from a domain leading peer-reviewed journal.

5. (alleman2023mechanismsforgenerating pages 7-9): Alexander B. Alleman and John W. Peters. Mechanisms for generating low potential electrons across the metabolic diversity of nitrogen-fixing bacteria. Applied and Environmental Microbiology, May 2023. URL: https://doi.org/10.1128/aem.00378-23, doi:10.1128/aem.00378-23. This article has 55 citations and is from a peer-reviewed journal.

6. (benoit2020molecularhydrogenmetabolism pages 16-18): Stéphane L. Benoit, Robert J. Maier, R. Gary Sawers, and Chris Greening. Molecular hydrogen metabolism: a widespread trait of pathogenic bacteria and protists. Microbiology and Molecular Biology Reviews, Feb 2020. URL: https://doi.org/10.1128/mmbr.00092-19, doi:10.1128/mmbr.00092-19. This article has 134 citations and is from a domain leading peer-reviewed journal.

7. (casado2024noveldruglikehsra pages 1-2): Javier Casado, Irene Olivan-Muro, Sonia Algarate, Eduardo Chueca, Sandra Salillas, Adrián Velázquez-Campoy, Elena Piazuelo, María F. Fillat, Javier Sancho, Ángel Lanas, and Andrés González. Novel drug-like hsra inhibitors exhibit potent narrow-spectrum antimicrobial activities against helicobacter pylori. International Journal of Molecular Sciences, 25:10175, Sep 2024. URL: https://doi.org/10.3390/ijms251810175, doi:10.3390/ijms251810175. This article has 3 citations.

8. (hu2024dualrnasequencing pages 1-2): Wei Hu, Zhi Yong Zhai, Zhao Yu Huang, Ze Min Chen, Ping Zhou, Xia Xi Li, Gen Hua Yang, Chong Ju Bao, Li Juan You, Xiao Bing Cui, Gui Li Xia, Mei Ping Ou Yang, Lin Zhang, William Ka Kei Wu, Long Fei Li, Yu Xuan Zhang, Zhan Gang Xiao, and Wei Gong. Dual rna sequencing of <i>helicobacter pylori</i> and host cell transcriptomes reveals ontologically distinct host-pathogen interaction. Apr 2024. URL: https://doi.org/10.1128/msystems.00206-24, doi:10.1128/msystems.00206-24. This article has 4 citations and is from a peer-reviewed journal.

9. (huang2024noveltherapeuticregimens pages 1-2): Ting-Ting Huang, Yong-Xiao Cao, and Lei Cao. Novel therapeutic regimens against helicobacter pylori: an updated systematic review. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1418129, doi:10.3389/fmicb.2024.1418129. This article has 60 citations and is from a peer-reviewed journal.

10. (maity2024mergingmultiomicswith pages 1-4): Ritwik Maity, Xuepei Zhang, Francesca Romana Liberati, Chiara Scribani Rossi, Francesca Cutruzzolà, Serena Rinaldo, Massimiliano Gaetani, José Antonio Aínsa, and Javier Sancho. Merging multi-omics with proteome integral solubility alteration unveils antibiotic mode of action. eLife, Jun 2024. URL: https://doi.org/10.1101/2023.09.07.556692, doi:10.1101/2023.09.07.556692. This article has 11 citations and is from a domain leading peer-reviewed journal.

11. (feng2024proteinqualitycontrol pages 1-4): Jinsong Feng, Shenmiao Li, Yaxi Hu, Martin Stahl, Lina Ma, Katelyn Knuff-Janzen, Kaidi Wang, Marti Z. Hua, Bruce A. Vallance, Michael E. Konkel, B. Brett Finlay, and Xiaonan Lu. Protein quality control modulates the metabolic conservation in antibiotic tolerant campylobacter jejuni. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.15.603561, doi:10.1101/2024.07.15.603561. This article has 0 citations.

12. (mele2023oxidoreductasesandmetal pages 16-17): Bruno Hay Mele, Maria Monticelli, Serena Leone, Deborah Bastoni, Bernardo Barosa, Martina Cascone, Flavia Migliaccio, Francesco Montemagno, Annarita Ricciardelli, Luca Tonietti, Alessandra Rotundi, Angelina Cordone, and Donato Giovannelli. Oxidoreductases and metal cofactors in the functioning of the earth. Essays in Biochemistry, 67:653-670, Aug 2023. URL: https://doi.org/10.1042/ebc20230012, doi:10.1042/ebc20230012. This article has 55 citations and is from a peer-reviewed journal.