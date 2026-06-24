---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:54:11.094460'
end_time: '2026-06-18T00:10:22.363332'
duration_seconds: 971.27
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: oxygen preference
  trait_identifier: METPO:1000601
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: oxygen_preference
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that is relating to an organism's oxygen requirements or
    tolerance for growth.
  parent_traits: METPO:1000059
  synonyms: Physiology and metabolism.oxygen tolerance.oxygen tolerance, metabolism
  evidence_summary: 'PMID:21413255: aerobes require molecular oxygen as a terminal
    electron acceptor (Medical Microbiology chapter supports molecular oxygen as the
    environmental axis defining oxygen-preference phenotypes.) | DOI:10.1016/j.bbabio.2011.06.016:
    respiratory quinol:O2 oxidoreductase (Aerobic respiration review supports terminal
    oxidases as the enzymatic interface between cells and ambient O2.)'
  causal_graph_summary: 'oxygen_preference_o2_availability_axis: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** oxygen preference
- **METPO identifier:** METPO:1000601
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is relating to an organism's oxygen requirements or tolerance for growth.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.oxygen tolerance.oxygen tolerance, metabolism
- **Existing evidence:** PMID:21413255: aerobes require molecular oxygen as a terminal electron acceptor (Medical Microbiology chapter supports molecular oxygen as the environmental axis defining oxygen-preference phenotypes.) | DOI:10.1016/j.bbabio.2011.06.016: respiratory quinol:O2 oxidoreductase (Aerobic respiration review supports terminal oxidases as the enzymatic interface between cells and ambient O2.)
- **Existing causal graph summary:** oxygen_preference_o2_availability_axis: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **oxygen preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/oxygen_preference.yaml`.

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
- **Trait label:** oxygen preference
- **METPO identifier:** METPO:1000601
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is relating to an organism's oxygen requirements or tolerance for growth.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.oxygen tolerance.oxygen tolerance, metabolism
- **Existing evidence:** PMID:21413255: aerobes require molecular oxygen as a terminal electron acceptor (Medical Microbiology chapter supports molecular oxygen as the environmental axis defining oxygen-preference phenotypes.) | DOI:10.1016/j.bbabio.2011.06.016: respiratory quinol:O2 oxidoreductase (Aerobic respiration review supports terminal oxidases as the enzymatic interface between cells and ambient O2.)
- **Existing causal graph summary:** oxygen_preference_o2_availability_axis: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **oxygen preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/oxygen_preference.yaml`.

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


# Microbial Trait Causal Graph Curation Report: Oxygen Preference (METPO:1000601)

**Target trait:** oxygen preference (METPO:1000601; ENVIRONMENT; CLASS) — “A phenotype that is relating to an organism's oxygen requirements or tolerance for growth.”

## 1) Scope summary (trait meaning, boundaries, and distinctions)

### Current understanding
“Oxygen preference” is best treated as a **compound phenotype** reflecting (a) the ability to conserve energy via **O2-dependent respiration** (terminal oxidases using O2 as a terminal electron acceptor), and/or (b) the ability to **survive O2 exposure** through O2/ROS detoxification and repair systems, even when O2 is not used for growth-linked respiration. This distinction is critical for curation because some “anaerobes” can be **aerotolerant** without being able to grow aerobically.

### Boundary cases and nearby traits
- **Obligate aerobes:** require O2 as terminal electron acceptor. Example: classical *Bordetella* spp. are described as “obligate aerobes that use only oxygen as the terminal electron acceptor” (mckay2024cytochromeoxidaserequirements pages 1-2).
- **Facultative anaerobes:** grow with or without O2, switching respiratory modules and/or fermentation depending on oxygen/redox state; regulation via ArcAB/FNR and terminal oxidase switching (brown2023conservedmetabolicregulator pages 12-14, brown2023conservedmetabolicregulator pages 1-3, mele2023oxidoreductasesandmetal pages 16-17).
- **Microaerophiles / nanaerobes:** grow best at low O2, often using high-affinity oxidases (e.g., cytochrome bd) while maintaining anaerobic terminal reductases. *Bacteroides fragilis* maintains fumarate reductase activity even “in the presence of oxygen” at nanaerobic O2 (butler2023bacteroidesfragilismaintains pages 7-9) and uses cytochrome bd for O2 reduction (butler2023bacteroidesfragilismaintains pages 2-5).
- **Obligate anaerobes exposed to physiological O2:** may encode dedicated O2-reducing enzymes (flavodiiron proteins, reverse rubrerythrins) with **O2-range-specific protection**, enabling survival through gradients rather than aerobic growth (caulat2024physiologicalroleand pages 1-2).
- **Aerotolerant anaerobes:** survive O2 through ROS detox and repair; survival can be strain-dependent and strongly assay/medium dependent (e.g., cysteine supplementation) (botin2023thetoleranceof pages 1-2).

**Trait separation guidance:**
- Curate **oxygen preference** as the **environmental growth/tolerance phenotype** across O2 tensions.
- Distinguish from nearby traits such as “oxidative stress resistance” (ROS detox capacity) and “aerobic respiration capability” (presence/usage of terminal oxidases), while allowing both as mechanistic parents/children in the causal graph.

## 2) Candidate mechanistic entities (nodes) for a TraitMech causal graph

### A. Environmental & experimental factors
- **Oxygen concentration/tension** (gas phase %, ppm; dissolved O2 µM) (CHEBI:15379 oxygen).
- **Gut oxygen gradients (host context):** longitudinal and lateral gradients; physiological low-O2 exposure as a driver for O2-scavenging systems in anaerobes (caulat2024physiologicalroleand pages 1-2).
- **Periodic oxygen stress / oxic–anoxic cycling:** e.g., 133 µM O2 pulses (50% air saturation) in bioreactor selecting for SRB persistence strategies (dyksma2024growthofsulfatereducing pages 1-2).
- **Medium thiols / reducing agents:** cysteine supplementation affecting extracellular superoxide and survival (CHEBI:15356 cysteine) (botin2023thetoleranceof pages 1-2).
- **ETC perturbation / membrane energetic state:** proton motive force uncoupling by CCCP (CHEBI:64774) as a perturbation revealing ArcA-dependent metabolic switching (brown2023conservedmetabolicregulator pages 10-12).

### B. Respiration pathways and modules
- **Aerobic electron transport chain** (GO:0019646 aerobic electron transport chain; broad).
- **Terminal oxidases (O2 reductases):**
  - **Cytochrome bd-type oxidase** (often high-affinity; quinol:O2 oxidoreductase class; EC mapping can vary by annotation) (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains pages 5-7).
  - **Heme–copper oxidase bo3-type (cyoABCD)** (low-affinity in many bacteria) (mckay2024cytochromeoxidaserequirements pages 1-2, mckay2024cytochromeoxidaserequirements pages 18-20).
  - **cbb3-type heme–copper oxidase** (high-affinity; mentioned as a class in reviews) (mele2023oxidoreductasesandmetal pages 16-17).
- **Alternative terminal reductases under low/no O2:**
  - **Fumarate reductase (frd)** (EC:1.3.5.4) operating concurrently with O2 respiration in *B. fragilis* (butler2023bacteroidesfragilismaintains pages 7-9).
- **Electron entry modules:** NADH:quinone oxidoreductases NQR/NDH2 (quantified in *B. fragilis*) (butler2023bacteroidesfragilismaintains pages 2-5).
- **Electron carriers:** quinone/menaquinone pool (CHEBI:16389 quinone; CHEBI:64716 menaquinone) (butler2023bacteroidesfragilismaintains pages 2-5).

### C. O2/ROS detoxification & repair systems
- **Flavodiiron proteins (FDPs)**: O2-reducing enzymes with strain/species-specific roles (caulat2024physiologicalroleand pages 1-2, botin2023thetoleranceof pages 1-2).
- **Rubrerythrin / reverse rubrerythrin (Rbr/revRbr)**: peroxidase/O2-reductase activities; O2-range specialization in *C. difficile* (caulat2024physiologicalroleand pages 1-2).
- **Superoxide dismutase (SOD)** (EC:1.15.1.1) and **catalase (Cat)** (EC:1.11.1.6): correlated with oxygen tolerance in anammox (okabe2023oxygentoleranceand pages 11-12).
- **Alkyl hydroperoxide reductase (Ahp)** and other peroxidases: included among SRB oxygen-defense suites (dyksma2024growthofsulfatereducing pages 1-2).
- **Repair/chaperone systems** supporting aerotolerance in SRB communities (e.g., thioredoxin, chaperones) (dyksma2024growthofsulfatereducing pages 1-2).

### D. Regulation and sensing (oxygen/redox response)
- **ArcAB two-component system** (ArcB sensor kinase; ArcA response regulator) connecting ETC/quinone state to transcriptional reprogramming (brown2023conservedmetabolicregulator pages 12-14, brown2023conservedmetabolicregulator pages 1-3).
- **FNR** (oxygen-responsive global regulator), cited as working with ArcA for microaerobic programs including cyd expression (mele2023oxidoreductasesandmetal pages 16-17).
- **Rex** (NADH/NAD+ sensor) regulating O2-response modules in anaerobes (caulat2024physiologicalroleand pages 1-2).
- **Spx-family regulator and sigma factors (σA/σB)** controlling induction of O2-reducing enzymes in *C. difficile* (caulat2024physiologicalroleand pages 1-2).

## 3) Evidence-backed candidate causal edges

The following table is structured for direct translation into `oxygen_preference.yaml` edges. It includes mechanistic class, snippets, DOI-first references, and ontology suggestions.

| Edge (subject—predicate—object) | Mechanistic class | Evidence snippet (short quote) | Reference (DOI/URL, year) | Notes/uncertainty | Suggested ontology grounding (CURIEs where clear: GO/CHEBI/ENVO/EC) |
|---|---|---|---|---|---|
| low oxygen tension — selects for / is tolerated by — high-affinity terminal oxidase cytochrome bd-mediated respiration | respiration | “cytochrome bd… transfers electrons from menaquinol to O2 to form water” and B. fragilis grows under “nanaerobic (0–1,500 ppm O2)” conditions (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains pages 7-9) | 10.1128/jb.00389-22 · https://doi.org/10.1128/jb.00389-22 · 2023 | Strong for B. fragilis; generalization to all anaerobes/facultatives should be marked taxon-specific | CHEBI:15379 oxygen; EC:7.1.1.7 ubiquinol oxidase (bd-type, approximate); GO:0019646 aerobic electron transport chain; ENVO:label-only low-oxygen environment |
| cyd operon / cytochrome bd — enables — oxygen-dependent NADH consumption | respiration | “Cytochrome bd activity is assayed as ‘oxygen-dependent NADH consumption.’… Δcyd deletion ‘showed essentially no activity’” (butler2023bacteroidesfragilismaintains pages 5-7) | 10.1128/jb.00389-22 · https://doi.org/10.1128/jb.00389-22 · 2023 | Strong, assay-backed; species-specific to B. fragilis | CHEBI:15379 oxygen; GO:0019646 aerobic electron transport chain; EC:7.1.1.7 |
| nanaerobic growth conditions — increase — cytochrome bd activity | environment/assay | “the measured activity of cytochrome bd increases slightly when cells are grown nanaerobically” and “~5-fold-higher activity when grown nanaerobically versus anaerobically” in one assay setup (butler2023bacteroidesfragilismaintains pages 7-9, butler2023bacteroidesfragilismaintains pages 5-7) | 10.1128/jb.00389-22 · https://doi.org/10.1128/jb.00389-22 · 2023 | Quantitative effect depends on heme precursor conditions (hemin vs PPIX+FeSO4); curate with assay note | CHEBI:15379 oxygen; CHEBI:26214 iron(2+); GO:0019646 |
| oxygen is not strictly necessary for heme d formation/assembly — supports — cytochrome bd assembly under anaerobic and nanaerobic conditions | respiration | “oxygen is not strictly necessary for this conversion” (butler2023bacteroidesfragilismaintains pages 7-9) | 10.1128/jb.00389-22 · https://doi.org/10.1128/jb.00389-22 · 2023 | Useful for assembly node; mechanistic intermediate may require label-only heme d biogenesis node | CHEBI:15379 oxygen; GO:0017004 cytochrome complex assembly (broad) |
| fumarate reductase — remains active under — low oxygen / nanaerobic conditions | respiration | “even in the presence of oxygen, the corresponding terminal enzyme for anaerobic respiration fumarate reductase is also present and active” (butler2023bacteroidesfragilismaintains pages 7-9) | 10.1128/jb.00389-22 · https://doi.org/10.1128/jb.00389-22 · 2023 | Strong for concurrent terminal electron-acceptor capacity; species-specific | CHEBI:18012 fumarate; CHEBI:30031 succinate; EC:1.3.5.4 fumarate reductase; GO:0006123 mitochondrial electron transport, cytochrome c to oxygen not appropriate → label-only anaerobic respiration |
| fumarate reductase deletion — decreases — fumarate-dependent NADH consumption | respiration | “A frd deletion reduced fumarate-dependent NADH consumption to 29% of wild type” (butler2023bacteroidesfragilismaintains pages 2-5) | 10.1128/jb.00389-22 · https://doi.org/10.1128/jb.00389-22 · 2023 | Strong gene-to-function edge in B. fragilis | CHEBI:18012 fumarate; EC:1.3.5.4 |
| menaquinone pool — supplies electrons to — cytochrome bd and fumarate reductase pathways at low O2 | respiration | B. fragilis “produces menaquinones (MK-8 to MK-11; MK-10 most abundant)” and uses cytochrome bd/fumarate reductase under nanaerobic conditions (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains pages 7-9) | 10.1128/jb.00389-22 · https://doi.org/10.1128/jb.00389-22 · 2023 | Inferred pathway edge from same study; acceptable but mark as moderate inference | CHEBI:64716 menaquinone; GO:0055114 oxidation-reduction process |
| obligate aerobic lifestyle — depends on — oxygen as terminal electron acceptor | respiration | Bordetella are “obligate aerobes that use only oxygen as the terminal electron acceptor” (mckay2024cytochromeoxidaserequirements pages 1-2) | 10.1371/journal.ppat.1012084 · https://doi.org/10.1371/journal.ppat.1012084 · 2024 | Good scope-defining edge for obligate aerobe subclass | CHEBI:15379 oxygen; GO:0019646 aerobic electron transport chain |
| cyoABCD1 (bo3-type oxidase) alone — is sufficient for — establishment/persistence in respiratory tract infection | respiration | “CyoABCD1 is sufficient to produce wild-type bacterial burdens in mouse infection models” (mckay2024cytochromeoxidaserequirements pages 1-2) | 10.1371/journal.ppat.1012084 · https://doi.org/10.1371/journal.ppat.1012084 · 2024 | Strong but host-pathogenesis context; curate as taxon-specific (Bordetella) | GO:0019646 aerobic electron transport chain; CHEBI:15379 oxygen; ENVO:00002009 respiratory tract |
| low-affinity bo3-type oxidase Cyo1 — can support — growth in low O2 and in vivo respiratory colonization | respiration | “a strain expressing only the low-affinity Cyo1 was indistinguishable from wild type” and WT can grow in “5% and 2% O2” (mckay2024cytochromeoxidaserequirements pages 18-20) | 10.1371/journal.ppat.1012084 · https://doi.org/10.1371/journal.ppat.1012084 · 2024 | Counterexample to simplistic low-O2 = only high-affinity oxidase rule; retain with caution | CHEBI:15379 oxygen; GO:0019646 |
| bd-type oxidase Cyd1 — is more tolerant of — oxidative/nitrosative stress | detox | “bd-type oxidases are… more tolerant of oxidative and nitrosative stress… [and] detoxify hydrogen peroxide and peroxynitrite” (mckay2024cytochromeoxidaserequirements pages 18-20) | 10.1371/journal.ppat.1012084 · https://doi.org/10.1371/journal.ppat.1012084 · 2024 | Review-like statement embedded in primary paper; broad but credible | CHEBI:15339 peroxynitrite; CHEBI:16240 hydrogen peroxide; GO:0006979 response to oxidative stress |
| declining oxygen availability — shifts terminal oxidase usage from — bo3 to bd | respiration | “bo3 is expressed under fully aerobic conditions and bd-type under microaerobic conditions, with a shift from bo3 to bd as O2 availability falls” (nastasi2024membraneboundredoxenzyme pages 4-7) | 10.3390/ijms25021277 · https://doi.org/10.3390/ijms25021277 · 2024 | Strong for E. coli; phrased from transcriptomics/biochemistry context | CHEBI:15379 oxygen; GO:0019646 aerobic electron transport chain |
| cytochrome bd-I — confers — greater CO-resistant aerobic respiration than bd-II or bo3 | respiration | at 100 µM O2, 96.3 µM CO inhibited bd-I by “11.6% vs. ~43% for bd-II/bo3” (nastasi2024membraneboundredoxenzyme pages 4-7) | 10.3390/ijms25021277 · https://doi.org/10.3390/ijms25021277 · 2024 | Not directly oxygen-preference-defining, but relevant to oxidase ecological fitness; optional edge | CHEBI:17245 carbon monoxide; CHEBI:15379 oxygen |
| oxygen exposure — induces — fdp and revrbr genes via Spx-family regulator | regulation | “an Spx-family regulator… plays a role in the induction of fdp and revrbr genes upon O2 exposure” (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24 · https://doi.org/10.1128/mbio.01591-24 · 2024 | Strong in C. difficile; regulator identity may need gene-level grounding later | CHEBI:15379 oxygen; GO:0006979 response to oxidative stress |
| σA and σB — positively regulate — revrbr2 expression | regulation | “revrbr2 is under the dual control of σA and σB” (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24 · https://doi.org/10.1128/mbio.01591-24 · 2024 | Strong but species-specific regulatory edge | GO:0006355 regulation of DNA-templated transcription; GO:0006979 |
| Rex redox regulator — regulates — fdpF expression | regulation | “fdpF is regulated by Rex, a regulator sensing the NADH/NAD+ ratio” (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24 · https://doi.org/10.1128/mbio.01591-24 · 2024 | Strong; link is redox-state mediated rather than direct O2 sensor | CHEBI:57945 NADH; CHEBI:57540 NAD+; GO:0055114 oxidation-reduction process |
| revRbr2 — protects at — very low O2 tensions (<0.4%) | detox | “revRbr2 is specific to low O2 tensions (<0.4%)” (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24 · https://doi.org/10.1128/mbio.01591-24 · 2024 | Strong O2-range annotation for node function; useful for microaerotolerance graphing | CHEBI:15379 oxygen; GO:0006979 |
| FdpA — protects at — low/intermediate O2 tensions (0.4–1%) | detox | “FdpA [is specific] to low and intermediate O2 tensions (0.4%–1%)” (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24 · https://doi.org/10.1128/mbio.01591-24 · 2024 | Strong O2-range annotation | CHEBI:15379 oxygen; GO:0006979 |
| revRbr1 — protects across — broader O2 range (0.1–4%) | detox | “revRbr1 has a wider spectrum of activity (0.1%–4%)” (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24 · https://doi.org/10.1128/mbio.01591-24 · 2024 | Strong O2-range annotation | CHEBI:15379 oxygen; GO:0006979 |
| FdpF — protects at — >4% O2 and air exposure | detox | “FdpF is more specific to tensions > 4% and air” (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24 · https://doi.org/10.1128/mbio.01591-24 · 2024 | Strong; useful boundary edge for aerotolerance in obligate anaerobes | CHEBI:15379 oxygen; GO:0006979 |
| larger detox-enzyme repertoire — increases — oxygen survival in Faecalibacterium strains | detox | strains with more detoxifying genes “survived longer than strains with few scavenging enzymes” (botin2023thetoleranceof pages 2-5) | 10.1128/aem.00606-23 · https://doi.org/10.1128/aem.00606-23 · 2023 | Comparative/strain-level edge; no single causal gene isolated | GO:0006979 response to oxidative stress |
| O2 or H2O2 stress — upregulates — detoxifying-enzyme genes | regulation | “expression of genes encoding detoxifying enzymes was upregulated in the response to O2 or H2O2 stress” (botin2023thetoleranceof pages 1-2) | 10.1128/aem.00606-23 · https://doi.org/10.1128/aem.00606-23 · 2023 | Strong but gene set is broad; suitable as process-level edge | CHEBI:15379 oxygen; CHEBI:16240 hydrogen peroxide; GO:0006979 |
| cysteine in medium — decreases — extracellular superoxide production | environment/assay | “cysteine… limited the production of extracellular O2•−” (botin2023thetoleranceof pages 1-2) | 10.1128/aem.00606-23 · https://doi.org/10.1128/aem.00606-23 · 2023 | Strong assay/environment factor; may affect observed trait calls | CHEBI:15356 cysteine; CHEBI:18421 superoxide |
| cysteine in medium — improves — survival under high O2 tension | environment/assay | cysteine “improved the survival… under high O2 tension” (botin2023thetoleranceof pages 1-2) | 10.1128/aem.00606-23 · https://doi.org/10.1128/aem.00606-23 · 2023 | Strong; assay-sensitive and taxon-specific | CHEBI:15356 cysteine; CHEBI:15379 oxygen |
| superoxide dismutase activity — is associated with — higher oxygen tolerance in anammox bacteria | detox | “Ca. Scalindua sp. possessed significantly higher Sod activity and therefore exhibited higher oxygen tolerance” (okabe2023oxygentoleranceand pages 11-12) | 10.1038/s43705-023-00251-7 · https://doi.org/10.1038/s43705-023-00251-7 · 2023 | Strong correlation/mechanistic interpretation; still comparative rather than knockout-based | EC:1.15.1.1 superoxide dismutase; CHEBI:18421 superoxide; GO:0004784 superoxide dismutase activity |
| catalase — rapidly degrades — hydrogen peroxide at higher concentrations | detox | “Catalase is the most prominent…” for H2O2 degradation (okabe2023oxygentoleranceand pages 11-12) | 10.1038/s43705-023-00251-7 · https://doi.org/10.1038/s43705-023-00251-7 · 2023 | General biochemical statement used to interpret oxygen tolerance | EC:1.11.1.6 catalase; CHEBI:16240 hydrogen peroxide |
| rubrerythrin / cytochrome c peroxidase — preferentially scavenge — low H2O2 / anoxic conditions | detox | “Ccp and Rbr were active only in the absence of O2… unable to degrade H2O2 quickly” (okabe2023oxygentoleranceand pages 11-12) | 10.1038/s43705-023-00251-7 · https://doi.org/10.1038/s43705-023-00251-7 · 2023 | Supports boundary between anaerobe detox and true oxic growth | CHEBI:16240 hydrogen peroxide; GO:0006979 |
| periodic oxic pulses (133 µM O2; 50% air saturation) — select for — SRB populations maintaining oxygen-defense expression | environment/assay | SRB grew despite “oxygen pulses at 133 µM (50% air saturation)” and maintained “genes for oxygen defense proteins” (dyksma2024growthofsulfatereducing pages 1-2) | 10.1186/s40168-024-01909-7 · https://doi.org/10.1186/s40168-024-01909-7 · 2024 | Community/bioreactor context; not a single-organism gene knockout | CHEBI:15379 oxygen; ENVO:label-only oxic-anoxic transition zone |
| bd-type oxidase CydAB / Roo-NorV / heme-copper oxidases — contribute to — oxygen consumption/defense in sulfate-reducing bacteria | detox | “oxygen-reducing enzymes… Roo/NorV and… bd-type oxidase (CydAB)” were specifically noted as important for oxygen consumption/defense (dyksma2024growthofsulfatereducing pages 1-2) | 10.1186/s40168-024-01909-7 · https://doi.org/10.1186/s40168-024-01909-7 · 2024 | Multi-enzyme community inference; may need taxon-specific curation later | GO:0019646 aerobic electron transport chain; GO:0006979 |
| quinone/ETC redox state — activates via ArcB phosphorylation — ArcA response regulator | regulation | “Quinones of the electron transport chain can transfer electrons to the sensor kinase ArcB, which then phosphorylates and activates ArcA” (brown2023conservedmetabolicregulator pages 12-14) | 10.1128/mbio.01448-23 · https://doi.org/10.1128/mbio.01448-23 · 2023 | Strong mechanistic regulator edge in Enterobacterales | CHEBI:16389 quinone; GO:0000156 phosphorelay response regulator activity |
| ArcA — represses — respiratory operons / aerobic respiration | regulation | “ArcAB is a two-component regulatory system that represses aerobic respiration” (brown2023conservedmetabolicregulator pages 1-3) | 10.1128/mbio.01448-23 · https://doi.org/10.1128/mbio.01448-23 · 2023 | Strong higher-level edge; broad across facultative Enterobacterales | GO:0006355 regulation of DNA-templated transcription; GO:0019646 |
| ArcA activation — mediates shift to — fermentation when ETC/PMF is impaired | regulation | “ArcA mediates the transition to fermentation” and represses “respiratory complexes and pathways feeding the ETC” (brown2023conservedmetabolicregulator pages 10-12) | 10.1128/mbio.01448-23 · https://doi.org/10.1128/mbio.01448-23 · 2023 | Strong, but triggered here by CCCP/PMF uncoupling; indirect proxy for low-respiration state | GO:0045333 cellular respiration; GO:0006113 fermentation |
| CCCP-mediated PMF uncoupling — reveals requirement for — ArcA-dependent fermentative adaptation | environment/assay | arcA mutants showed “longer lag times and slower doubling times” under CCCP treatment (brown2023conservedmetabolicregulator pages 10-12) | 10.1128/mbio.01448-23 · https://doi.org/10.1128/mbio.01448-23 · 2023 | Assay edge; useful as perturbational evidence rather than core trait mechanism | CHEBI:64774 CCCP; GO:0045333 cellular respiration |
| ArcA and FNR — are required for peak expression of — cyd operon under microaerobic conditions | regulation | “ArcA and Fnr are required for peak expression of the cyd operon in Escherichia coli under microaerobic conditions” (mele2023oxidoreductasesandmetal pages 16-17) | 10.1042/EBC20230012 · https://doi.org/10.1042/ebc20230012 · 2023 | Secondary citation within review; useful but weaker than direct primary-source extraction | GO:0006355 regulation of DNA-templated transcription; CHEBI:15379 oxygen |
| oxygen availability / redox state — influences — ArcA-linked stationary-phase physiology | regulation | rpoS transcription is “influenced by oxygen, ArcA, and NADH:NAD+ ratio” in a redox-ArcBA model (whittle2024effluxpumpsmediate pages 9-12) | 10.1128/mbio.02370-24 · https://doi.org/10.1128/mbio.02370-24 · 2024 | Indirect systems-level edge; likely too broad for immediate TraitMech curation | CHEBI:57945 NADH; CHEBI:57540 NAD+; CHEBI:15379 oxygen |


*Table: This table lists candidate, evidence-backed causal edges relevant to microbial oxygen preference, spanning respiration, detoxification, regulation, and assay/environment factors. It is formatted to support TraitMech-style curation with short snippets, references, uncertainty notes, and suggested ontology grounding.*

### Visual evidence (figures)
- Butler et al. include a **cytochrome bd activity assay (oxygen-dependent NADH consumption)** and a **schematic ETC** showing cytochrome bd (O2 terminal acceptor) operating alongside fumarate reductase (fumarate terminal acceptor) under nanaerobic conditions (butler2023bacteroidesfragilismaintains media 1296b3e4, butler2023bacteroidesfragilismaintains media fcd57ce3).

## 4) Recent developments (2023–2024 emphasis)

### 4.1 Quantitative “oxygen tolerance” parameters in anaerobic metabolisms (bioprocess relevance)
Anammox bacteria show widely differing oxygen inhibition kinetics; e.g., a marine “Ca. *Scalindua*” had substantially higher tolerance with **IC50 = 18.0 µM** and **DOmax = 51.6 µM**, compared to freshwater species (IC50 ~2.7–4.2 µM; DOmax ~10.9–26.6 µM). This was linked mechanistically to high **SOD activity** and moderate catalase activity (okabe2023oxygentoleranceand pages 12-12, okabe2023oxygentoleranceand pages 11-12). These quantitative parameters are directly relevant to modeling oxygen preference and stability in engineered nitrogen-removal systems.

### 4.2 O2-range specialization of detox enzymes in obligate anaerobes (fine-grained curation opportunities)
In *Clostridioides difficile* (2024), four O2-reducing enzymes exhibit distinct protective ranges: **revRbr2 (<0.4% O2), FdpA (0.4–1%), revRbr1 (0.1–4%), FdpF (>4% and air)**, governed by multi-layer regulation (σA/σB, Spx, Rex) (caulat2024physiologicalroleand pages 1-2). This supports curating oxygen preference as a function of multiple partially redundant modules rather than a single “aerobe/anaerobe” switch.

### 4.3 Low-O2 respiration in gut-associated anaerobes (“nanaerobic” physiology)
*Bacteroides fragilis* (2023) maintains “concurrent capability” for fumarate respiration and O2 respiration at **nanaerobic 1,000–1,500 ppm O2**, with cytochrome bd-dependent oxygen-dependent NADH consumption and fumarate reductase remaining active even when O2 is present (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains pages 7-9, butler2023bacteroidesfragilismaintains pages 5-7). This mechanism supports colonization of microoxic niches in the gut.

### 4.4 Terminal oxidase repertoires and infection physiology
In *Bordetella* (2024), strains retaining different cytochrome oxidases show that **CyoABCD1 alone** can be sufficient to reach wild-type burdens in murine respiratory infection models, challenging assumptions that high-affinity oxidases are always required in host niches (mckay2024cytochromeoxidaserequirements pages 1-2, mckay2024cytochromeoxidaserequirements pages 18-20). This indicates that oxygen preference can be shaped by **niche oxygen access** and not only enzyme affinity.

### 4.5 Regulatory integration of oxygen/redox signals (expert mechanistic synthesis)
ArcAB is explicitly described as repressing aerobic respiration, with mechanistic linkage via the quinone/ETC state: “quinones… transfer electrons to… ArcB… phosphorylates and activates ArcA” (brown2023conservedmetabolicregulator pages 12-14). Perturbations that mimic low-respiration states (CCCP uncoupling) reveal ArcA-dependent shifts toward fermentation independent of O2 availability (brown2023conservedmetabolicregulator pages 10-12). This supports graph edges that connect **O2 availability → ETC redox poise → ArcAB activation → repression of respiratory operons / induction of fermentation**.

## 5) Current applications & real-world implementations

- **Clinical/pathogenesis:** Oxygen preference shapes colonization and infection. *Bordetella* respiratory infection depends on terminal oxidase sufficiency in vivo (mckay2024cytochromeoxidaserequirements pages 1-2, mckay2024cytochromeoxidaserequirements pages 18-20). In the gut, physiological O2 gradients expose “strict anaerobes” to low O2, selecting for O2-scavenging/detox systems (caulat2024physiologicalroleand pages 1-2).
- **Biotechnology & environmental systems:**
  - **Anammox processes** must account for species-specific oxygen tolerance with quantified IC50/DOmax values impacting reactor control and modeling (okabe2023oxygentoleranceand pages 12-12, okabe2023oxygentoleranceand pages 11-12).
  - **Oxic–anoxic transition zones / peatland bioreactors:** sulfate-reducing bacteria can persist under repeated oxic pulses via oxygen-defense expression programs, relevant to wetland sulfur cycling and engineered bioreactors (dyksma2024growthofsulfatereducing pages 1-2).

## 6) Statistics and quantitative data points for curation

- *B. fragilis* electron entry: NQR vs NDH2 contribute **77% vs 23%** of NADH:quinone oxidoreductase activity under nanaerobic conditions (butler2023bacteroidesfragilismaintains pages 2-5).
- *B. fragilis* nanaerobic definition used: **1,000–1,500 ppm O2**; broader test range **0–1,500 ppm O2** (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains pages 7-9).
- Anammox oxygen tolerance: **IC50 = 18.0 µM; DOmax = 51.6 µM** for marine “Ca. *Scalindua*” vs lower values for freshwater species (okabe2023oxygentoleranceand pages 12-12).
- SRB bioreactor oxygen pulses: **133 µM O2 (50% air saturation)**, weekly oxic periods, with SRB populations reaching **up to 2.9% relative abundance** despite pulses (dyksma2024growthofsulfatereducing pages 1-2).
- *C. difficile* detox enzyme operating ranges: **revRbr2 (<0.4%), FdpA (0.4–1%), revRbr1 (0.1–4%), FdpF (>4% and air)** (caulat2024physiologicalroleand pages 1-2).

## 7) Warnings and curation caveats (what not to curate yet)

1. **Don’t equate “oxygen preference” with “presence of a single oxidase gene.”** Oxidase sufficiency depends on niche oxygen availability (e.g., low-affinity Cyo1 supporting infection) and on detox systems (mckay2024cytochromeoxidaserequirements pages 18-20).
2. **Assay/medium confounding:** Cysteine can reduce extracellular superoxide and improve survival under high O2, potentially shifting phenotype calls (botin2023thetoleranceof pages 1-2). Curate cysteine as an *experimental factor node* where relevant.
3. **Community vs isolate inference:** SRB oxygen-defense conclusions are supported by genome-centric metatranscriptomics in a community reactor. Curate those edges as **contextual/environmental** and avoid over-generalizing to all SRB isolates (dyksma2024growthofsulfatereducing pages 1-2).
4. **Regulatory edges may be taxon-specific:** ArcAB/FNR circuitry is best evidenced for Enterobacterales and cited in reviews for *E. coli* cyd regulation (brown2023conservedmetabolicregulator pages 12-14, mele2023oxidoreductasesandmetal pages 16-17). Use “uncertain” flags when extending to distant taxa.
5. **Terminal oxidase EC/GO grounding can be tricky:** cytochrome bd vs heme–copper oxidases may map to different EC terms depending on annotation conventions; treat EC identifiers as tentative unless confirmed in the target curation ontology.

## 8) DOI-first bibliography (with URLs and publication dates)

- Caulat LC et al. **Physiological role and complex regulation of O2-reducing enzymes in the obligate anaerobe *Clostridioides difficile*.** mBio. **Oct 2024.** https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 1-2)
- McKay LS et al. **Cytochrome oxidase requirements in Bordetella reveal insights into evolution towards life in the mammalian respiratory tract.** PLOS Pathogens. **Jul 2024.** https://doi.org/10.1371/journal.ppat.1012084 (mckay2024cytochromeoxidaserequirements pages 1-2, mckay2024cytochromeoxidaserequirements pages 18-20, mckay2024cytochromeoxidaserequirements pages 8-10)
- Nastasi MR et al. **Cytochrome bd-I promotes carbon monoxide-resistant *E. coli* growth and respiration.** Int J Mol Sci. **Jan 2024.** https://doi.org/10.3390/ijms25021277 (nastasi2024membraneboundredoxenzyme pages 4-7)
- Dyksma S, Pester M. **Growth of sulfate-reducing Desulfobacterota and Bacillota at periodic oxygen stress of 50% air-O2 saturation.** Microbiome. **Oct 2024.** https://doi.org/10.1186/s40168-024-01909-7 (dyksma2024growthofsulfatereducing pages 1-2)
- Brown AN et al. **ArcA responds to oxygen availability… during bacteremia.** mBio. **Oct 2023.** https://doi.org/10.1128/mbio.01448-23 (brown2023conservedmetabolicregulator pages 12-14, brown2023conservedmetabolicregulator pages 1-3, brown2023conservedmetabolicregulator pages 10-12)
- Butler NL et al. **Bacteroides fragilis maintains concurrent capability for anaerobic and nanaerobic respiration.** J Bacteriol. **Jan 2023.** https://doi.org/10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains pages 7-9, butler2023bacteroidesfragilismaintains pages 5-7, butler2023bacteroidesfragilismaintains media 1296b3e4, butler2023bacteroidesfragilismaintains media fcd57ce3)
- Botin T et al. **Tolerance of gut commensal *Faecalibacterium* to oxidative stress is strain dependent and relies on detoxifying enzymes.** Appl Environ Microbiol. **Jul 2023.** https://doi.org/10.1128/aem.00606-23 (botin2023thetoleranceof pages 1-2, botin2023thetoleranceof pages 2-5)
- Okabe S et al. **Oxygen tolerance and detoxification mechanisms of anammox bacteria.** ISME Communications. **May 2023.** https://doi.org/10.1038/s43705-023-00251-7 (okabe2023oxygentoleranceand pages 12-12, okabe2023oxygentoleranceand pages 11-12)
- Mele BH et al. **Oxidoreductases and metal cofactors in the functioning of the earth.** Essays Biochem. **Aug 2023.** https://doi.org/10.1042/ebc20230012 (contains citations to ArcA/FNR control of cyd under microaerobic conditions) (mele2023oxidoreductasesandmetal pages 16-17)

---

## Deliverable notes for `data/traits/environment/oxygen_preference.yaml`

The edges in the table (artifact-00) can be transcribed into YAML as causal relationships with qualifiers for: taxon specificity, assay dependence (e.g., cysteine, CCCP), and ecological context (host, bioreactor, gut gradients). Figures from Butler et al. provide supporting visual evidence for the respiration-module portion of the graph (butler2023bacteroidesfragilismaintains media 1296b3e4, butler2023bacteroidesfragilismaintains media fcd57ce3).

References

1. (mckay2024cytochromeoxidaserequirements pages 1-2): Liliana S. McKay, Alexa R. Spandrio, Richard M. Johnson, M. Ashley Sobran, Sara A. Marlatt, Katlyn B. Mote, Margaret R. Dedloff, Zachary M. Nash, Steven M. Julio, and Peggy A. Cotter. Cytochrome oxidase requirements in bordetella reveal insights into evolution towards life in the mammalian respiratory tract. PLOS Pathogens, 20:e1012084, Jul 2024. URL: https://doi.org/10.1371/journal.ppat.1012084, doi:10.1371/journal.ppat.1012084. This article has 7 citations and is from a highest quality peer-reviewed journal.

2. (brown2023conservedmetabolicregulator pages 12-14): Aric N. Brown, Mark T. Anderson, Sara N. Smith, Michael A. Bachman, and Harry L. T. Mobley. Conserved metabolic regulator arca responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia. Oct 2023. URL: https://doi.org/10.1128/mbio.01448-23, doi:10.1128/mbio.01448-23. This article has 11 citations and is from a domain leading peer-reviewed journal.

3. (brown2023conservedmetabolicregulator pages 1-3): Aric N. Brown, Mark T. Anderson, Sara N. Smith, Michael A. Bachman, and Harry L. T. Mobley. Conserved metabolic regulator arca responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia. Oct 2023. URL: https://doi.org/10.1128/mbio.01448-23, doi:10.1128/mbio.01448-23. This article has 11 citations and is from a domain leading peer-reviewed journal.

4. (mele2023oxidoreductasesandmetal pages 16-17): Bruno Hay Mele, Maria Monticelli, Serena Leone, Deborah Bastoni, Bernardo Barosa, Martina Cascone, Flavia Migliaccio, Francesco Montemagno, Annarita Ricciardelli, Luca Tonietti, Alessandra Rotundi, Angelina Cordone, and Donato Giovannelli. Oxidoreductases and metal cofactors in the functioning of the earth. Essays in Biochemistry, 67:653-670, Aug 2023. URL: https://doi.org/10.1042/ebc20230012, doi:10.1042/ebc20230012. This article has 55 citations and is from a peer-reviewed journal.

5. (butler2023bacteroidesfragilismaintains pages 7-9): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

6. (butler2023bacteroidesfragilismaintains pages 2-5): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

7. (caulat2024physiologicalroleand pages 1-2): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

8. (botin2023thetoleranceof pages 1-2): Tatiana Botin, Luis Ramirez-Chamorro, Jasmina Vidic, Philippe Langella, Isabelle Martin-Verstraete, Jean-Marc Chatel, and Sandrine Auger. The tolerance of gut commensal <i>faecalibacterium</i> to oxidative stress is strain dependent and relies on detoxifying enzymes. Applied and Environmental Microbiology, Jul 2023. URL: https://doi.org/10.1128/aem.00606-23, doi:10.1128/aem.00606-23. This article has 19 citations and is from a peer-reviewed journal.

9. (dyksma2024growthofsulfatereducing pages 1-2): Stefan Dyksma and Michael Pester. Growth of sulfate-reducing desulfobacterota and bacillota at periodic oxygen stress of 50% air-o2 saturation. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01909-7, doi:10.1186/s40168-024-01909-7. This article has 52 citations and is from a highest quality peer-reviewed journal.

10. (brown2023conservedmetabolicregulator pages 10-12): Aric N. Brown, Mark T. Anderson, Sara N. Smith, Michael A. Bachman, and Harry L. T. Mobley. Conserved metabolic regulator arca responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia. Oct 2023. URL: https://doi.org/10.1128/mbio.01448-23, doi:10.1128/mbio.01448-23. This article has 11 citations and is from a domain leading peer-reviewed journal.

11. (butler2023bacteroidesfragilismaintains pages 5-7): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

12. (mckay2024cytochromeoxidaserequirements pages 18-20): Liliana S. McKay, Alexa R. Spandrio, Richard M. Johnson, M. Ashley Sobran, Sara A. Marlatt, Katlyn B. Mote, Margaret R. Dedloff, Zachary M. Nash, Steven M. Julio, and Peggy A. Cotter. Cytochrome oxidase requirements in bordetella reveal insights into evolution towards life in the mammalian respiratory tract. PLOS Pathogens, 20:e1012084, Jul 2024. URL: https://doi.org/10.1371/journal.ppat.1012084, doi:10.1371/journal.ppat.1012084. This article has 7 citations and is from a highest quality peer-reviewed journal.

13. (okabe2023oxygentoleranceand pages 11-12): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

14. (nastasi2024membraneboundredoxenzyme pages 4-7): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

15. (botin2023thetoleranceof pages 2-5): Tatiana Botin, Luis Ramirez-Chamorro, Jasmina Vidic, Philippe Langella, Isabelle Martin-Verstraete, Jean-Marc Chatel, and Sandrine Auger. The tolerance of gut commensal <i>faecalibacterium</i> to oxidative stress is strain dependent and relies on detoxifying enzymes. Applied and Environmental Microbiology, Jul 2023. URL: https://doi.org/10.1128/aem.00606-23, doi:10.1128/aem.00606-23. This article has 19 citations and is from a peer-reviewed journal.

16. (whittle2024effluxpumpsmediate pages 9-12): Emily E. Whittle, Oluwatosin Orababa, Alexander Osgerby, Pauline Siasat, Sarah J. Element, Jessica M. A. Blair, and Tim W. Overton. Efflux pumps mediate changes to fundamental bacterial physiology via membrane potential. mBio, Oct 2024. URL: https://doi.org/10.1128/mbio.02370-24, doi:10.1128/mbio.02370-24. This article has 39 citations and is from a domain leading peer-reviewed journal.

17. (butler2023bacteroidesfragilismaintains media 1296b3e4): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

18. (butler2023bacteroidesfragilismaintains media fcd57ce3): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

19. (okabe2023oxygentoleranceand pages 12-12): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

20. (mckay2024cytochromeoxidaserequirements pages 8-10): Liliana S. McKay, Alexa R. Spandrio, Richard M. Johnson, M. Ashley Sobran, Sara A. Marlatt, Katlyn B. Mote, Margaret R. Dedloff, Zachary M. Nash, Steven M. Julio, and Peggy A. Cotter. Cytochrome oxidase requirements in bordetella reveal insights into evolution towards life in the mammalian respiratory tract. PLOS Pathogens, 20:e1012084, Jul 2024. URL: https://doi.org/10.1371/journal.ppat.1012084, doi:10.1371/journal.ppat.1012084. This article has 7 citations and is from a highest quality peer-reviewed journal.