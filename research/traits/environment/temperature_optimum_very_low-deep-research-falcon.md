---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:13:34.844226'
end_time: '2026-06-18T02:23:45.177225'
duration_seconds: 610.33
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum very low
  trait_identifier: METPO:1000441
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum_very_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature optimum phenotype with the best-growth ambient temperature\
    \ at or below approximately 10 \xB0C, characteristic of psychrophilic physiology."
  parent_traits: METPO:1000304
  synonyms: Psychrophile, TO_<=10
  evidence_summary: 'DOI:10.1038/sj.embor.7400662: growing well at temperatures around
    the freezing point of water (Psychrophile review supports growth at very low temperatures
    as the psychrophilic optimum.)'
  causal_graph_summary: 'temperature_optimum_very_low_psychrophile_setpoint: 4 nodes,
    3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum very low
- **METPO identifier:** METPO:1000441
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature at or below approximately 10 °C, characteristic of psychrophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Psychrophile, TO_<=10
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports growth at very low temperatures as the psychrophilic optimum.)
- **Existing causal graph summary:** temperature_optimum_very_low_psychrophile_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_very_low.yaml`.

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
- **Trait label:** temperature optimum very low
- **METPO identifier:** METPO:1000441
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature at or below approximately 10 °C, characteristic of psychrophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Psychrophile, TO_<=10
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports growth at very low temperatures as the psychrophilic optimum.)
- **Existing causal graph summary:** temperature_optimum_very_low_psychrophile_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_very_low.yaml`.

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


## Research report: Microbial trait “temperature optimum very low” (METPO:1000441)

### Scope summary (trait meaning and boundaries)
**Trait definition (curation target).** *Temperature optimum very low* refers to a **psychrophilic temperature optimum**, i.e., organisms whose best-growth (Topt) occurs at **~10 °C or below** (your METPO definition), with physiology specialized for persistent cold. A widely used operational definition (Morita 1975) specifies psychrophiles with **Tmin ≤ 0 °C, Topt ≤ ~15 °C, and Tmax ≤ ~20 °C**. (moyer2017psychrophilesandpsychrotrophs pages 1-2, hamdan2018psychrophilesecologicalsignificance pages 1-2, ramon2023ageneraloverview pages 1-2)

**Distinguishing boundary cases.**
- **Psychrophile vs psychrotolerant/psychrotroph:** Psychrotolerant organisms can grow at low temperature but retain a **higher Topt** (often >20 °C), whereas psychrophiles have a low Topt and often low Tmax. (moyer2017psychrophilesandpsychrotrophs pages 1-2, ramon2023ageneraloverview pages 1-2)
- **Subzero growth is not sufficient** to label an organism as psychrophile: *Planococcus halocryophilus* can grow to ~−15 °C yet is described as **psychrotolerant** because its optimum/max temperatures are much higher (optimum ~25 °C, max ~37 °C). (moyer2017psychrophilesandpsychrotrophs pages 1-2)
- **Conceptual caution (expert perspective):** Cavicchioli emphasizes that classification solely by lab-derived Topt/Tmax can be misleading ecologically; many isolates from cold environments grow well above in situ temperatures, and terminology/cutoffs are inconsistent across literature. This supports treating METPO:1000441 as a **phenotype derived from growth curves** (assay-defined), not a strict ecological class. (cavicchioli2016ontheconcept pages 1-2)

**Recommended curation interpretation for METPO:1000441.** Curate this trait when a growth-rate-vs-temperature curve or equivalent assay supports **optimal growth at ≤10 °C** (or clearly within classic psychrophile definitions) and the organism shows cold-specialized physiology (e.g., low Tmax, cold-active proteome). Use **psychrotolerant** trait(s) when growth occurs at 0–4 °C but **Topt is >10–15 °C**. (moyer2017psychrophilesandpsychrotrophs pages 1-2, ramon2023ageneraloverview pages 1-2)

---

### Key concepts and definitions (current understanding)
1. **Cardinal temperatures (Tmin/Topt/Tmax).** Psychrophile definitions commonly use a triad of cardinal temperatures (minimum, optimum, maximum) that are all shifted low; one cited criterion is Tmin/Topt/Tmax at or below 0/15/20 °C. (hamdan2018psychrophilesecologicalsignificance pages 1-2, moyer2017psychrophilesandpsychrotrophs pages 1-2)
2. **Homeoviscous/homeophasic adaptation.** Low temperature reduces membrane fluidity; cold-adapted organisms remodel lipids (e.g., unsaturated/branched/shorter chains) to maintain functional membranes for transport and bioenergetics. (damico2006psychrophilicmicroorganismschallenges pages 2-3, moyer2017psychrophilesandpsychrotrophs pages 2-3)
3. **Cold-shock / RNA and translation constraints.** At low temperature, nucleic-acid secondary structures and slowed translation require RNA-binding proteins/chaperones and other translation-support systems (cold shock proteins, TRAM-domain RNA chaperones in some archaea). (damico2006psychrophilicmicroorganismschallenges pages 2-3, siddiqui2013psychrophiles pages 9-11)
4. **Proteostasis under cold.** Low temperature can destabilize folding equilibria and slow folding; chaperones (e.g., Hsp70 family members; review lists GroEL/DnaK/GroES and Clp proteases) and folding catalysts (e.g., peptidyl-prolyl isomerases) support growth. (damico2006psychrophilicmicroorganismschallenges pages 2-3, purwar2024adaptationsofpsychrophilic pages 6-7)
5. **Cryoprotection near/below freezing.** EPS matrices, compatible solutes (e.g., trehalose, glycine betaine), and ice-binding/antifreeze proteins modulate freezing stress (freeze-thaw, ice recrystallization, thermal hysteresis). (damico2006psychrophilicmicroorganismschallenges pages 2-3, hamdan2018psychrophilesecologicalsignificance pages 2-2, ramon2023ageneraloverview pages 12-14)

---

### Candidate causal-graph nodes (entities), grouped by type
Below are **candidate nodes** suitable for TraitMech graph building; many can be grounded to stable ontologies.

#### Phenotype nodes
- **temperature optimum very low** (METPO:1000441)
- **psychrophile** (label; synonym to METPO class usage)
- **growth at 0 °C / subzero growth** (label; phenotype qualifier)

#### Environmental and experimental factor nodes
- **low temperature** (ENVO:01000230; label for “cold stress”)
- **freeze–thaw cycles** (label)
- **ice presence / freezing conditions** (label)

#### Molecular processes / functions
- **membrane fluidity maintenance (homeoviscous adaptation)** (label)
- **fatty acid desaturation** (GO:0102331 “fatty acid desaturase activity” can be used where appropriate)
- **protein folding / chaperone-mediated folding** (GO:0006457)
- **translation under cold stress** (GO:0006412)
- **response to oxidative stress** (GO:0006979)

#### Genes/proteins/complexes (candidate node families)
- **fatty-acid desaturases** (EC:1.14.19.-)
- **cold shock proteins (Csp family)** (label; GO:0003723 RNA binding often applicable)
- **TRAM-domain RNA chaperones (Ctr proteins; archaea)** (label) (siddiqui2013psychrophiles pages 9-11)
- **Hsp70/Hsp60 systems** (label; review mentions GroEL/DnaK/GroES) (purwar2024adaptationsofpsychrophilic pages 6-7)
- **Clp proteases** (label) (purwar2024adaptationsofpsychrophilic pages 6-7)
- **antifreeze proteins / ice-binding proteins** (label)
- **superoxide dismutase** (EC:1.15.1.1)
- **catalase / catalase–peroxidase** (EC:1.11.1.6; EC:1.11.1.21)

#### Chemicals/metabolites
- **unsaturated fatty acids** (CHEBI:51006)
- **trehalose** (CHEBI:18150)
- **glycine betaine** (CHEBI:17750)
- **exopolysaccharides (EPS)** (label; chemical mixture)

#### Pathways/modules (use as mid-level nodes)
- **fatty-acid biosynthesis and remodeling** (GO:0006633)
- **compatible-solute synthesis/uptake (osmoprotection/cryoprotection)** (label)
- **antioxidant enzyme systems** (label)

---

### Evidence-backed candidate causal edges (triples)
The table below is designed for direct curation into a TraitMech-style YAML as candidate edges.

| Edge (subject–predicate–object) | Entity types | Suggested ontology grounding (CURIEs where possible; label-only if unclear) | Evidence snippet (verbatim short quote) | Source (DOI, year, URL) | Curation notes (strength/uncertainty, taxon/assay specificity) |
|---|---|---|---|---|---|
| low temperature → decreases fluidity of → cell membrane | environmental factor → process/property → cellular component | ENVO:01000230 low temperature; GO:0005886 plasma membrane; label-only: membrane fluidity | "the decrease in cell membrane fluidity is the primary signal for cold-tolerant" (bao2023miningofkey pages 1-2) | 10.3389/fmicb.2023.1215837, 2023, https://doi.org/10.3389/fmicb.2023.1215837 | Strong for cold response generally; direct causal framing in psychrotolerant *Pseudomonas fragi* D12, but broadly consistent with psychrophily. |
| low temperature → selects for → temperature optimum very low phenotype | environmental factor → evolutionary pressure → phenotype | ENVO:01000230 low temperature; METPO:1000441 temperature optimum very low; label-only: selection in permanently cold environments | "psychrophilic microorganisms prevail in permanently cold environments (< 5 C" (ramon2023ageneraloverview pages 1-2) | 10.1007/s42770-023-01057-4, 2023, https://doi.org/10.1007/s42770-023-01057-4 | Broad ecological inference rather than direct experiment; curate as higher-level ecological edge with uncertainty. |
| fatty acid desaturase activity → increases abundance of → unsaturated fatty acids | enzyme activity → chemical class → membrane trait | EC:1.14.19.- fatty-acid desaturases; CHEBI:51006 unsaturated fatty acid | "activation of desaturases, increased unsaturated acyl chains" (hamdan2018psychrophilesecologicalsignificance pages 2-2) | 10.17159/sajs.2018/20170254, 2018, https://doi.org/10.17159/sajs.2018/20170254 | Foundational review evidence; mechanism broadly accepted, but not tied to one universally conserved gene family. |
| increased unsaturated fatty acids → maintains → membrane fluidity at low temperature | chemical class → process/property → cellular component/property | CHEBI:51006 unsaturated fatty acid; label-only: membrane fluidity; GO:0005886 plasma membrane | "maintain membrane fluidity by improving the ratio of unsaturated fatty" (yang2023insightintothe pages 1-2) | 10.1128/AEM.01928-22, 2023, https://doi.org/10.1128/AEM.01928-22 | Strong, recent transcriptome/physiology support in *Bacillus simplex* H-b; likely generalizable. |
| membrane biogenesis / fatty acid desaturation genes → contribute to → low-temperature membrane adaptation | pathway/gene set → process → phenotype-supporting process | GO:0006633 fatty acid biosynthetic process; GO:0016117 carotenoid biosynthetic process?; label-only: fatty acid desaturation genes | "upregulate genes involved in membrane biogenesis, fatty acid synthesis, fatty acid desaturation" (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Review synthesis; useful as pathway-level node, but specific taxa/genes should be added before gene-level curation. |
| cold shock proteins / RNA chaperones → support → translation at low temperature | protein family → biological process → process context | GO:0003723 RNA binding; label-only: cold shock protein (Csp); GO:0006412 translation | "Cold-shock proteins are major cold responses, functioning in regulation of transcription/translation" (hamdan2018psychrophilesecologicalsignificance pages 2-2) | 10.17159/sajs.2018/20170254, 2018, https://doi.org/10.17159/sajs.2018/20170254 | Strong general mechanism from review; broad but not always Csp-based in archaea/fungi. |
| TRAM-domain RNA chaperones (Ctr proteins) → enable → RNA function during cold growth | protein family → molecular function/process → cold adaptation | label-only: Ctr protein; InterPro/Pfam TRAM domain unlabeled here; GO:0003723 RNA binding | "instead upregulate single-TRAM-domain RNA chaperones (Ctr proteins)—M. burtonii shows high Ctr abundance at −2°C" (siddiqui2013psychrophiles pages 9-11) | 10.1146/annurev-earth-040610-133514, 2013, https://doi.org/10.1146/annurev-earth-040610-133514 | Taxon-specific archaeal mechanism; mark uncertain for universal psychrophile graph but useful candidate branch. |
| molecular chaperones → restore → normal transcription and translation under low temperature | protein class → biological process → cellular response | GO:0006457 protein folding; GO:0006412 translation; label-only: molecular chaperones | "increases in the expression of molecular chaperones and transcription factors, enabling the bacteria to restore normal transcription and translation" (bao2023miningofkey pages 1-2) | 10.3389/fmicb.2023.1215837, 2023, https://doi.org/10.3389/fmicb.2023.1215837 | Strong, recent support; mechanism observed during 15°C to 4°C response in *P. fragi* D12. |
| GroEL / DnaK / GroES → promote → protein folding / cold-denaturation resistance | chaperone proteins → biological process → phenotype-supporting process | UniProt/GO label-only: GroEL, DnaK, GroES; GO:0006457 protein folding | "Key chaperones and proteostasis factors cited include ... 'GroEL, DnaK, and GroES.'" (purwar2024adaptationsofpsychrophilic pages 6-7) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Review-level evidence; good candidate nodes but needs primary-source taxon support for strong mechanistic curation. |
| Clp proteases → provide → protein quality control during cold stress | protease complex → biological process → stress adaptation | label-only: Clp protease; GO:0006511 ubiquitin-independent protein catabolic process? label-only preferred | "Key chaperones and proteostasis factors cited include 'caseinolytic proteases (Clps)'" (purwar2024adaptationsofpsychrophilic pages 6-7) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Review evidence only; role in psychrophiles plausible but should be flagged as weaker without primary psychrophile perturbation data. |
| extracellular polymeric substances (EPS) → protect against → freeze-thaw / low-temperature damage | extracellular polymer → protective process → stress phenotype | GO:0045226 extracellular matrix structural constituent? label-only: EPS; CHEBI label-only polysaccharide mixture | "EPS act as cryoprotectants ('providing protection against freeze-thaw cycles')" (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Strong review statement; EPS composition varies widely, so keep node broad. |
| EPS production → reduces freezing point of → local environment / protects extracellular enzymes | extracellular polymer production → physical effect → extracellular proteins | label-only: extracellular polymeric substances; ENVO:01000230 low temperature; GO:0005576 extracellular region | "can reduce the freezing point of the environment" and "protect extracellular enzymes from low-temperature deformation" (bao2023miningofkey pages 1-2) | 10.3389/fmicb.2023.1215837, 2023, https://doi.org/10.3389/fmicb.2023.1215837 | Recent source; mechanistic details may depend on assay/system. Good candidate edge with medium confidence. |
| trehalose → acts as → cryoprotectant | metabolite → role → stress-protective effect | CHEBI:18150 trehalose; label-only: cryoprotectant | "Compatible solutes (trehalose) and extracellular polysaccharides (EPSs) act as cryoprotectants" (damico2006psychrophilicmicroorganismschallenges pages 2-3) | 10.1038/sj.embor.7400662, 2006, https://doi.org/10.1038/sj.embor.7400662 | Foundational and widely accepted; not unique to psychrophiles. |
| glycine betaine → stabilizes → proteins/membranes during cold stress | compatible solute → protective process → cellular structures | CHEBI:17750 glycine betaine; GO:0016020 membrane | "including glycine betaine and trehalose — prevent protein aggregation and stabilize membranes" (hamdan2018psychrophilesecologicalsignificance pages 2-2) | 10.17159/sajs.2018/20170254, 2018, https://doi.org/10.17159/sajs.2018/20170254 | Strong review evidence; broad across cold-adapted microbes, not exclusive to psychrophiles. |
| antifreeze proteins / ice-binding proteins → inhibit → ice recrystallization | protein family → physical process → ice crystal growth | label-only: antifreeze protein; label-only: ice-binding protein; GO label-only: ice binding | "AFPs, also known as Ice Binding Proteins (IBPs)" and roles in "ice recrystallization inhibition critical for survival at subzero temperatures" (purwar2024adaptationsofpsychrophilic pages 6-7) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Strong review support; ice-binding protein families are polyphyletic and structurally diverse. |
| antifreeze proteins → cause → thermal hysteresis / lower freezing point | protein family → physical effect → cold survival | label-only: antifreeze protein; label-only: thermal hysteresis | "AFPs lower freezing point via thermal hysteresis" (ramon2023ageneraloverview pages 12-14) | 10.1007/s42770-023-01057-4, 2023, https://doi.org/10.1007/s42770-023-01057-4 | Strong, recent review statement; appropriate as process-level edge. |
| superoxide dismutase / catalase → mitigate → oxidative stress at low temperature | enzymes → stress response → ROS | EC:1.15.1.1 superoxide dismutase; EC:1.11.1.6 catalase; GO:0006979 response to oxidative stress; CHEBI:26523 reactive oxygen species | "produce antioxidant enzymes, such as catalase and superoxide dismutase, to prevent oxidative damage" (bao2023miningofkey pages 1-2) | 10.3389/fmicb.2023.1215837, 2023, https://doi.org/10.3389/fmicb.2023.1215837 | Strong recent support in cold-response experiment; likely broadly applicable, though exact enzymes vary. |
| peroxide stress enzymes / thioredoxin system → support → freezing-temperature growth | enzymes/pathway → stress mitigation → phenotype support | label-only: thioredoxin reductase; EC:1.11.1.7 catalase-peroxidase; EC:1.15.1.1 SOD | "Several superoxide dismutase related proteins were identified"; "One thioredoxin reductase enzyme was identified"; "two putative catalase–peroxidase enzymes" (zerouki2023wholegenomesequenceand pages 10-12) | 10.1007/s00438-023-02073-7, 2023, https://doi.org/10.1007/s00438-023-02073-7 | Primary omics evidence from *Phacidium infestans* grown at −3°C vs 22°C; good fungal-specific support. |
| increased enzyme structural flexibility → increases → catalytic activity at low temperature | protein structural property → enzyme function → phenotype support | label-only: enzyme structural flexibility; GO:0003824 catalytic activity | "Cold-adapted enzymes display increased structural flexibility and higher catalytic efficiency" (hamdan2018psychrophilesecologicalsignificance pages 2-2) | 10.17159/sajs.2018/20170254, 2018, https://doi.org/10.17159/sajs.2018/20170254 | Foundational/general mechanism; applies broadly but not a single discrete gene/pathway node. |
| cold-adapted enzymes → sustain → metabolic flux at low temperature | enzyme class → physiological process → growth phenotype | label-only: cold-adapted enzyme; GO:0008152 metabolic process; METPO:1000441 | "synthesize cold-active enzymes to sustain their cell cycle" (damico2006psychrophilicmicroorganismschallenges pages 2-3) | 10.1038/sj.embor.7400662, 2006, https://doi.org/10.1038/sj.embor.7400662 | Strong foundational support; useful phenotype-proximal edge, though mechanistically broad. |
| microbiome-derived cryoprotective proteins → enhance resistance to → freezing conditions | protein set / community trait → phenotype → environmental stress survival | label-only: cryoprotective protein; ENVO:01000230 low temperature | "Resistance to freezing conditions ... is enhanced by cryoprotective proteins produced by their microbiome" (buschi2024resistancetofreezing pages 1-2) | 10.1126/sciadv.adk9117, 2024, https://doi.org/10.1126/sciadv.adk9117 | High-quality recent evidence, but host-associated holobiont context; probably out of scope for core microbial single-genome TraitMech unless microbiome interactions are modeled. |


*Table: This table compiles curation-ready candidate causal edges for the trait 'temperature optimum very low (psychrophile)'. It emphasizes recent 2023-2024 evidence while also including foundational citations for broadly accepted mechanisms.*

---

### Recent developments (prioritizing 2023–2024)
#### 1) Omics-driven mechanistic inventories and quantitative gene sets
- **Genome + transcriptome mining in a cold-tolerant bacterium.** *Pseudomonas fragi* D12 comparative genomics and transcriptomics identified **124** potential cold-adaptation genes and a defined subset connected to membrane remodeling, including **46 genes linked to membrane fluidity** (4 in unsaturated fatty-acid synthesis; 42 in fatty-acid degradation). (bao2023miningofkey pages 6-7)
- **Transcriptomics in functional low-temperature bioprocess bacteria.** *Bacillus simplex* H-b showed measurable nitrogen removal at **5 °C** (reported **27.22%**), with low temperature shifting nitrogen usage toward assimilation plus EPS and ATP accumulation, and higher unsaturated fatty acids—illustrating multi-layer cold adaptation in a real-world relevant function (aerobic denitrification). (yang2023insightintothe pages 1-2)

#### 2) Freezing-temperature fungal omics links cryoprotection, antioxidants, and IBPs
- **Growth at −3 °C vs 22 °C in *Phacidium infestans*.** A combined genome/proteome/metabolome analysis found trehalose-pathway genes and multiple antioxidant enzymes (SODs, thioredoxin reductase, catalases/catalase–peroxidases), along with candidate fungal **ice-binding proteins** supported by phylogenetic analysis. (zerouki2023wholegenomesequenceand pages 10-12, zerouki2023wholegenomesequenceand media c5f36001)
- **Quantitative metabolomics differences at freezing temperature.** In *P. infestans*, selected metabolites differed between −3 °C and 22 °C: **sepiapterin and neopterin were ~2–3× more abundant at −3 °C** (p<0.05), and dihydrolipoamide was also significantly higher (p<0.001). The paper provides a concrete table suitable for curation as supporting quantitative evidence for cold-growth metabolic shifts. (zerouki2023wholegenomesequenceand pages 10-12, zerouki2023wholegenomesequenceand media 11f52b6f)

#### 3) Structural diversity of ice-binding proteins and regulatory layers
- A 2023 review synthesizes IBP diversity (INPs vs AFPs), notes independent origins, and gives structural/size examples including *Pseudomonas* InaZ (INP >120 kDa) and repeat-unit architecture relevant to ice binding. (ramon2023ageneraloverview pages 12-14)

#### 4) Systems-level statistics on available psychrophile genomes
- A 2024 review reports psychrophile genome availability in GOLD as **83 complete/permanent draft genomes** and **102 targeted/incomplete**, with **43.4% from marine/Antarctic sources**. (purwar2024adaptationsofpsychrophilic pages 3-4)

---

### Current applications and real-world implementations
1. **Low-temperature wastewater nitrogen removal.** Cold-adapted aerobic denitrifiers are positioned for **nitrogen-contaminated wastewater treatment in cold regions**; *Bacillus simplex* H-b retained a reported nitrogen removal rate at **5 °C** while showing multi-layer cold adaptation (lipid remodeling, EPS, stress responses). (yang2023insightintothe pages 1-2)
2. **Biotechnological exploitation of cryoprotective proteins/IBPs.** Antarctic host-associated systems indicate microbiome-derived cryoprotective proteins can enhance freezing tolerance and may have “nature-based biotechnological applications.” This is strong evidence for applied bioprospecting, though the mechanism is in a holobiont context. (buschi2024resistancetofreezing pages 1-2)
3. **Cold-active enzymes and industrial biocatalysis.** Psychrophiles are recognized sources of cold-active enzymes enabling activity at low/moderate temperatures with potential energy savings; this is a continuing application focus in the psychrophile literature. (hamdan2018psychrophilesecologicalsignificance pages 2-2, damico2006psychrophilicmicroorganismschallenges pages 2-3)

---

### Expert opinions and authoritative analyses (interpretive synthesis)
- **Operational definitions are useful but imperfect.** Morita-style thresholds (Tmin/Topt/Tmax) are still widely used in reviews and reference works (moyer2017psychrophilesandpsychrotrophs pages 1-2, hamdan2018psychrophilesecologicalsignificance pages 1-2), but Cavicchioli argues strongly that **lab-based Topt/Tmax alone can misrepresent ecological psychrophily** and that “psychrophile/psychrotolerant” boundaries remain inconsistently applied. This supports a curation approach that ties METPO:1000441 to **assay-defined temperature optima** while capturing ecology as additional evidence, not a strict prerequisite. (cavicchioli2016ontheconcept pages 1-2)
- **Mechanistic convergence with diversity of implementations.** Across bacteria/archaea/fungi, core constraints (membrane rigidity, RNA/protein folding, ice damage, ROS) are repeatedly addressed by convergent solutions (lipid remodeling, RNA chaperones, chaperones/proteases, EPS/solutes, IBPs, antioxidant systems), but the **specific molecular actors differ by lineage** (e.g., TRAM-domain chaperones in some archaea). (siddiqui2013psychrophiles pages 9-11, zerouki2023wholegenomesequenceand pages 10-12, damico2006psychrophilicmicroorganismschallenges pages 2-3)

---

### Statistics and quantitative data (recent studies)
- **Genome resource statistics:** 83 complete/permanent draft and 102 targeted/incomplete psychrophile genomes in GOLD; 43.4% marine/Antarctic sources. (purwar2024adaptationsofpsychrophilic pages 3-4)
- **Functional performance at low temperature:** *Bacillus simplex* H-b reported 27.22% nitrogen removal at 5 °C. (yang2023insightintothe pages 1-2)
- **Freezing-temperature metabolite shifts:** in *Phacidium infestans* (−3 °C vs 22 °C), sepiapterin and neopterin increased ~2–3× at −3 °C (p<0.05), with specific peak areas listed in Table 4. (zerouki2023wholegenomesequenceand pages 10-12, zerouki2023wholegenomesequenceand media 11f52b6f)
- **Quantified cold-adaptation gene inventory:** *Pseudomonas fragi* D12 identified 124 candidate cold-adaptation genes; 46 associated with membrane fluidity (4 unsaturated FA synthesis; 42 FA degradation). (bao2023miningofkey pages 6-7)

---

## Warnings / “do not curate yet” flags
1. **Avoid equating “growth at subzero temperature” with psychrophily.** Subzero growth can occur in psychrotolerant organisms with high Topt; ensure **Topt ≤10 °C** is supported for METPO:1000441. (moyer2017psychrophilesandpsychrotrophs pages 1-2)
2. **Be cautious with review-only gene naming (GroEL/DnaK/Clp).** The 2024 review lists these as relevant, but gene-level edges should ideally be supported by **primary perturbation/omics evidence in psychrophiles** before strong curation. Consider curating them first as **generic chaperone/proteostasis nodes** with weaker confidence. (purwar2024adaptationsofpsychrophilic pages 6-7)
3. **Holobiont microbiome cryoprotection is context-specific.** Microbiome-derived cryoprotective proteins enhancing animal freezing tolerance are compelling (high-authority 2024 study) but may be outside a **single-microbe trait** causal graph unless the graph explicitly models host association. (buschi2024resistancetofreezing pages 1-2)
4. **Definition inconsistency across literature.** Some sources use differing numeric ranges; treat definitions as operational and record assay conditions. (cavicchioli2016ontheconcept pages 1-2)

---

## DOI-first bibliography (publication date, URL)
- Ramón A, et al. **2023-07**. *A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.* Brazilian Journal of Microbiology. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 12-14)
- Moon S, et al. **2023-03**. *Temperature Matters: Bacterial Response to Temperature Change.* Journal of Microbiology. https://doi.org/10.1007/s12275-023-00031-x (used indirectly as retrieval; definitional synthesis supported primarily by Morita-based sources above)
- Bao C, et al. **2023-07**. *Mining of key genes for cold adaptation from Pseudomonas fragi D12…* Frontiers in Microbiology. https://doi.org/10.3389/fmicb.2023.1215837 (bao2023miningofkey pages 1-2, bao2023miningofkey pages 6-7)
- Yang Q, et al. **2023-02**. *Insight into the Cold Adaptation Mechanism… Bacillus simplex H-b.* Applied and Environmental Microbiology. https://doi.org/10.1128/aem.01928-22 (yang2023insightintothe pages 1-2)
- Zerouki C, et al. **2023-10**. *Whole-genome sequence and mass spectrometry study… growing at freezing temperatures.* Molecular Genetics and Genomics. https://doi.org/10.1007/s00438-023-02073-7 (zerouki2023wholegenomesequenceand pages 10-12, zerouki2023wholegenomesequenceand media c5f36001, zerouki2023wholegenomesequenceand media 11f52b6f)
- Buschi E, et al. **2024-06**. *Resistance to freezing… enhanced by cryoprotective proteins produced by their microbiome.* Science Advances. https://doi.org/10.1126/sciadv.adk9117 (buschi2024resistancetofreezing pages 1-2)
- Purwar S, Srivastava S. **2024-10**. *Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.* Applied Microbiology: Theory & Technology. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 1-3, purwar2024adaptationsofpsychrophilic pages 6-7, purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 3-4)
- Moyer CL, Collins RE, Morita RY. **2017-01**. *Psychrophiles and Psychrotrophs.* Reference Module in Life Sciences (Elsevier). https://doi.org/10.1016/B978-0-12-809633-8.02282-2 (moyer2017psychrophilesandpsychrotrophs pages 1-2)
- Cavicchioli R. **2016-09**. *On the concept of a psychrophile.* ISME J. https://doi.org/10.1038/ismej.2015.160 (cavicchioli2016ontheconcept pages 1-2)
- Hamdan A. **2018-05**. *Psychrophiles: ecological significance and potential industrial application.* S Afr J Sci. https://doi.org/10.17159/sajs.2018/20170254 (hamdan2018psychrophilesecologicalsignificance pages 1-2, hamdan2018psychrophilesecologicalsignificance pages 2-2)
- D’Amico S, et al. **2006-04**. *Psychrophilic microorganisms: challenges for life.* EMBO Reports. https://doi.org/10.1038/sj.embor.7400662 (damico2006psychrophilicmicroorganismschallenges pages 1-2, damico2006psychrophilicmicroorganismschallenges pages 2-3)
- Siddiqui KS, et al. **2013-05**. *Psychrophiles.* Annual Review of Earth and Planetary Sciences. https://doi.org/10.1146/annurev-earth-040610-133514 (siddiqui2013psychrophiles pages 9-11)


References

1. (moyer2017psychrophilesandpsychrotrophs pages 1-2): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 185 citations.

2. (hamdan2018psychrophilesecologicalsignificance pages 1-2): Amira Hamdan. Psychrophiles: ecological significance and potential industrial application. South African Journal of Science, 114:6, May 2018. URL: https://doi.org/10.17159/sajs.2018/20170254, doi:10.17159/sajs.2018/20170254. This article has 70 citations and is from a peer-reviewed journal.

3. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

4. (cavicchioli2016ontheconcept pages 1-2): Ricardo Cavicchioli. On the concept of a psychrophile. The ISME Journal, 10:793-795, Sep 2016. URL: https://doi.org/10.1038/ismej.2015.160, doi:10.1038/ismej.2015.160. This article has 131 citations.

5. (damico2006psychrophilicmicroorganismschallenges pages 2-3): Salvino D'Amico, Tony Collins, Jean‐Claude Marx, Georges Feller, Charles Gerday, and Charles Gerday. Psychrophilic microorganisms: challenges for life. The EMBO Reports, 7:385-389, Apr 2006. URL: https://doi.org/10.1038/sj.embor.7400662, doi:10.1038/sj.embor.7400662. This article has 1134 citations.

6. (moyer2017psychrophilesandpsychrotrophs pages 2-3): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 185 citations.

7. (siddiqui2013psychrophiles pages 9-11): Khawar S. Siddiqui, Timothy J. Williams, David Wilkins, Sheree Yau, Michelle A. Allen, Mark V. Brown, Federico M. Lauro, and Ricardo Cavicchioli. Psychrophiles. Annual Review of Earth and Planetary Sciences, 41:87-115, May 2013. URL: https://doi.org/10.1146/annurev-earth-040610-133514, doi:10.1146/annurev-earth-040610-133514. This article has 195 citations and is from a highest quality peer-reviewed journal.

8. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

9. (hamdan2018psychrophilesecologicalsignificance pages 2-2): Amira Hamdan. Psychrophiles: ecological significance and potential industrial application. South African Journal of Science, 114:6, May 2018. URL: https://doi.org/10.17159/sajs.2018/20170254, doi:10.17159/sajs.2018/20170254. This article has 70 citations and is from a peer-reviewed journal.

10. (ramon2023ageneraloverview pages 12-14): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

11. (bao2023miningofkey pages 1-2): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 21 citations and is from a peer-reviewed journal.

12. (yang2023insightintothe pages 1-2): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 16 citations and is from a peer-reviewed journal.

13. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

14. (zerouki2023wholegenomesequenceand pages 10-12): C. Zerouki, K. Chakraborty, S. Kuittinen, A. Pappinen, and O. Turunen. Whole-genome sequence and mass spectrometry study of the snow blight fungus phacidium infestans (karsten) dsm 5139 growing at freezing temperatures. Molecular Genetics and Genomics, 298:1449-1466, Oct 2023. URL: https://doi.org/10.1007/s00438-023-02073-7, doi:10.1007/s00438-023-02073-7. This article has 10 citations and is from a peer-reviewed journal.

15. (buschi2024resistancetofreezing pages 1-2): Emanuela Buschi, Antonio Dell’Anno, Michael Tangherlini, Marco Candela, Simone Rampelli, Silvia Turroni, Giorgia Palladino, Erika Esposito, Marco Lo Martire, Luigi Musco, Sergio Stefanni, Cristina Munari, Jessica Fiori, Roberto Danovaro, and Cinzia Corinaldesi. Resistance to freezing conditions of endemic antarctic polychaetes is enhanced by cryoprotective proteins produced by their microbiome. Science Advances, Jun 2024. URL: https://doi.org/10.1126/sciadv.adk9117, doi:10.1126/sciadv.adk9117. This article has 4 citations and is from a highest quality peer-reviewed journal.

16. (bao2023miningofkey pages 6-7): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 21 citations and is from a peer-reviewed journal.

17. (zerouki2023wholegenomesequenceand media c5f36001): C. Zerouki, K. Chakraborty, S. Kuittinen, A. Pappinen, and O. Turunen. Whole-genome sequence and mass spectrometry study of the snow blight fungus phacidium infestans (karsten) dsm 5139 growing at freezing temperatures. Molecular Genetics and Genomics, 298:1449-1466, Oct 2023. URL: https://doi.org/10.1007/s00438-023-02073-7, doi:10.1007/s00438-023-02073-7. This article has 10 citations and is from a peer-reviewed journal.

18. (zerouki2023wholegenomesequenceand media 11f52b6f): C. Zerouki, K. Chakraborty, S. Kuittinen, A. Pappinen, and O. Turunen. Whole-genome sequence and mass spectrometry study of the snow blight fungus phacidium infestans (karsten) dsm 5139 growing at freezing temperatures. Molecular Genetics and Genomics, 298:1449-1466, Oct 2023. URL: https://doi.org/10.1007/s00438-023-02073-7, doi:10.1007/s00438-023-02073-7. This article has 10 citations and is from a peer-reviewed journal.

19. (purwar2024adaptationsofpsychrophilic pages 3-4): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

20. (purwar2024adaptationsofpsychrophilic pages 1-3): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

21. (damico2006psychrophilicmicroorganismschallenges pages 1-2): Salvino D'Amico, Tony Collins, Jean‐Claude Marx, Georges Feller, Charles Gerday, and Charles Gerday. Psychrophilic microorganisms: challenges for life. The EMBO Reports, 7:385-389, Apr 2006. URL: https://doi.org/10.1038/sj.embor.7400662, doi:10.1038/sj.embor.7400662. This article has 1134 citations.