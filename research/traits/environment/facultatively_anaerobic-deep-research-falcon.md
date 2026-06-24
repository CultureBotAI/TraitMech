---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:04:45.019609'
end_time: '2026-06-17T22:33:27.250818'
duration_seconds: 1722.23
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: facultatively anaerobic
  trait_identifier: METPO:1000605
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: facultatively_anaerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference in which growth can occur with or without molecular\
    \ oxygen (O\u2082)."
  parent_traits: METPO:1000601
  synonyms: facultative, facultative anaerobe
  evidence_summary: 'https://www.ncbi.nlm.nih.gov/books/NBK482349/: can grow in the
    presence or absence of oxygen (Supports facultative anaerobiosis as growth under
    oxic or anoxic conditions.) | DOI:10.1093/femsre/fuac008: Escherichia coli is
    a facultative anaerobe (Organism example: Escherichia coli is described as facultatively
    anaerobic.)'
  causal_graph_summary: 'facultative_anaerobe_oxygen_switch: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultatively anaerobic
- **METPO identifier:** METPO:1000605
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth can occur with or without molecular oxygen (O₂).
- **Parent traits:** METPO:1000601
- **Synonyms:** facultative, facultative anaerobe
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: can grow in the presence or absence of oxygen (Supports facultative anaerobiosis as growth under oxic or anoxic conditions.) | DOI:10.1093/femsre/fuac008: Escherichia coli is a facultative anaerobe (Organism example: Escherichia coli is described as facultatively anaerobic.)
- **Existing causal graph summary:** facultative_anaerobe_oxygen_switch: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **facultatively anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_anaerobic.yaml`.

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
- **Trait label:** facultatively anaerobic
- **METPO identifier:** METPO:1000605
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth can occur with or without molecular oxygen (O₂).
- **Parent traits:** METPO:1000601
- **Synonyms:** facultative, facultative anaerobe
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: can grow in the presence or absence of oxygen (Supports facultative anaerobiosis as growth under oxic or anoxic conditions.) | DOI:10.1093/femsre/fuac008: Escherichia coli is a facultative anaerobe (Organism example: Escherichia coli is described as facultatively anaerobic.)
- **Existing causal graph summary:** facultative_anaerobe_oxygen_switch: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **facultatively anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_anaerobic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: *facultatively anaerobic* (METPO:1000605)

**Trait label:** facultatively anaerobic  
**METPO:** METPO:1000605  
**Definition (curation-ready):** capacity to sustain growth with or without molecular oxygen by using aerobic respiration when O2 is available, and switching to anaerobic respiration using alternative terminal electron acceptors and/or fermentation when O2 is limiting or absent. This implies regulatory and bioenergetic plasticity rather than mere oxygen tolerance. (brown2023conservedmetabolicregulator pages 1-3, schulzmirbach2024engineeringnewtonaturebiochemical pages 1-2)

### 1) Trait scope (what the trait represents)

**Phenotype represented.** Facultative anaerobiosis is an **oxygen-preference/energy-metabolism phenotype** defined operationally by **growth in both oxic and anoxic conditions**, supported by metabolic reconfiguration across electron acceptors and energy conservation modes (respiration ↔ fermentation). Regulatory systems (e.g., ArcAB and FNR in Enterobacterales) and respiratory-chain remodeling are key determinants of this phenotype. (brown2023conservedmetabolicregulator pages 1-3, ricciardelli2025tracemetalsavailability pages 3-6)

**Boundary cases & nearby traits (important for curation):**
- **Obligate aerobes**: cannot sustain growth without O2 because they lack functional anaerobic respiration/fermentation capacity.
- **Obligate anaerobes**: cannot tolerate/perform in O2 due to oxygen sensitivity; however, recent work emphasizes that some “strict anaerobes” can benefit from very low (nanomolar) O2 and maintain low-O2 respiratory capacity (sometimes termed *nanaerobic* respiration), which can resemble facultative behavior under tightly defined O2 regimes. This is a boundary-case risk for mislabeling. (butler2023bacteroidesfragilismaintains pages 10-11)
- **Microaerophiles**: prefer low O2, often requiring O2 but harmed by atmospheric O2; they are not defined by an ability to grow *without* O2.
- **Aerotolerant anaerobes**: tolerate O2 but do **not** use O2 as a terminal electron acceptor for growth.

**Assay considerations (how to observe/measure the trait):**
- **Controlled oxygen regimes are essential**, including *nanaerobic* (e.g., ~1,000–1,500 ppm O2) versus strictly anaerobic comparisons; Butler et al. used a dedicated gas-flow system to maintain these low-O2 conditions and combined growth assays with membrane enzymology and spectroscopy. (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains pages 7-9)
- **Oxygen consumption rate (OCR)** is a quantitative phenotype of respiratory activity; time-resolved OCR platforms can assay dynamic switching with sequential addition of perturbants/alternative electron acceptors under defined hypoxia. (rossi2026measuringbacterialoxygen pages 1-2)
- **Biofilm microelectrodes** can directly validate O2 gradients/hypoxia, critical for real-world facultative behavior in structured communities. (ren2025theadaptabilityof pages 2-3)

### 2) Current mechanistic understanding (key concepts/definitions)

Facultative anaerobic growth is best modeled as a **causal chain from environment → redox sensing → transcriptional reprogramming → respiratory-chain remodeling → growth**.

**A. Oxygen/redox sensing and transcriptional control**
- **FNR** is an O2-responsive global regulator whose activity depends on an oxygen-labile Fe–S cluster: “In the presence of oxygen, the fumarate and nitrate reduction regulatory protein (FNR) is inactivated through oxidation of its FeS cluster, preventing the transcription of the genes for anaerobic respirations.” (ricciardelli2025tracemetalsavailability pages 3-6)
- **ArcAB (ArcBA)** is a two-component system coordinating aerobic-to-anaerobic transitions. It is explicitly described as a **quinone/quinol redox sensor**: oxidized quinones repress ArcB kinase activity; ArcBA is “a direct sensor of the quinol pool redox state.” (whittle2024effluxpumpsmediate pages 7-9) Mechanistic diversity exists across taxa: E. coli ArcB regulation involves PAS-domain cysteines and quinone-mediated oxidation/reduction; Pasteurellaceae ArcB homologs may lack the PAS domain and thus use different signals (likely metabolite-driven). (alvarez2024diversificationofsignal pages 1-2)
- **Nar systems (NarX/NarQ–NarL/NarP)** sense nitrate/nitrite and induce nitrate/nitrite respiration gene expression while repressing competing pathways (e.g., fumarate respiration/fermentation), implementing hierarchical electron-acceptor prioritization. (ricciardelli2025tracemetalsavailability pages 3-6)

**B. Respiratory chain architecture enabling switching**
A clear mechanistic exemplar is *Bacteroides fragilis* under **anaerobic vs nanaerobic** conditions:
- Electrons enter the quinone pool via **NQR** and **NDH2**, contributing ~77% and ~23% of NADH dehydrogenase activity under nanaerobic conditions (similar under anaerobic conditions). (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains pages 2-5)
- The organism uses a **menaquinone pool** (MK-8 to MK-11, MK-10 predominant) rather than ubiquinone, consistent with low-O2 electron transfer strategies. (butler2023bacteroidesfragilismaintains pages 2-5)
- **Terminal branches switch by acceptor availability**: cytochrome bd oxidase (cyd) uses O2; fumarate reductase (frd) uses fumarate; the relevant enzymes can be present under both conditions, enabling rapid switching. (butler2023bacteroidesfragilismaintains pages 2-5)

(Visual evidence supporting this architecture and the nanaerobic culture system is available from Butler et al. figure/table crops.) (butler2023bacteroidesfragilismaintains media 9271434f, butler2023bacteroidesfragilismaintains media 0e668668)

**C. Cofactor constraints as causal bottlenecks**
- Trace metals gate the ability to use certain electron acceptors because key reductases are **metalloenzymes**. In E. coli, molybdenum availability determines whether molybdoenzyme-based respiration (e.g., nitrate reduction) can proceed; experimental data showed nitrate reduction could be abolished under metal depletion and rescued by adding molybdenum and iron. (ricciardelli2025tracemetalsavailability pages 3-6)
- Fe–S biosynthesis can be essential for anaerobic physiology and in vivo fitness: in *Enterococcus faecium*, Tn-seq identified anaerobic-growth genes, and deletion of **sufB** or **pflA** abolished gastrointestinal colonization in mice. (xu2024thefescluster pages 1-2)

### 3) Recent developments (prioritizing 2023–2024)

**(i) Low-O2 “nanaerobic” respiration and concurrent respiratory capabilities.** Butler et al. (2023) provided a mechanistic and quantitative dissection of respiratory chain contributions under anaerobic vs nanaerobic growth in *B. fragilis*, emphasizing that transcript levels may not predict activity and that direct biochemical assays are needed. (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains pages 2-5)

**(ii) Expanded Arc system signal diversity across taxa.** Alvarez et al. (2024) showed that ArcB homologs can diverge: canonical ArcB uses PAS cysteines and quinones as redox inputs, whereas Pasteurellaceae PAS-less ArcB appears cysteine-independent and more metabolite-responsive—important for avoiding overgeneralization in graph curation. (alvarez2024diversificationofsignal pages 1-2)

**(iii) Infection-relevant anaerobic respiration on host-derived electron acceptors.** Kim et al. (2024) demonstrated intracellular *Salmonella* can use a molybdenum cofactor enzyme complex **DmsABC** to reduce **methionine sulfoxide** as a terminal electron acceptor under conditions where host ROS both deplete O2 and damage aerobic respiratory machinery. (kim2024anaerobicrespirationof pages 1-3)

**(iv) Anaerobic niche adaptation and colonization genes in gut facultative anaerobes.** Xu et al. (2024) linked Fe–S cluster assembly (Suf) and pyruvate-formate lyase activation to anaerobic growth and colonization in *E. faecium*, connecting core metabolism to commensalism/pathogenesis under gut oxygen limitation. (xu2024thefescluster pages 1-2)

### 4) Current applications and real-world implementations (with quantitative data)

**Clinical infections and oxygen-dependent virulence/metabolism**
- **Ocular infection epidemiology:** In a 2015–2023 hospital dataset (2,712 isolates), gram-positive bacteria were 65.08% and *Staphylococcus epidermidis* represented 25.55% of isolates; experimental microoxic culture induced increased energy metabolism, amino-acid metabolism, and membrane transport signatures, supporting a role for oxygen as a cue in commensal-to-pathogen transitions. (lv2024theimpactof pages 1-2)
- **Intracellular survival under oxidative stress:** Host NADPH oxidase-derived ROS can repress aerobic cytochrome gene transcription and impair proton-coupled NADH dehydrogenase, forcing anaerobic strategies; DmsABC-mediated methionine sulfoxide respiration is one such strategy. (kim2024anaerobicrespirationof pages 1-3)

**Biofilms and chronic infection microenvironments**
- Oxygen limitation is linked to antibiotic tolerance: a recent review summarizes evidence that oxygen deficiency accounts for ~70% of antibiotic resistance in mature *Pseudomonas aeruginosa* biofilm cells, supported by microelectrode-confirmed hypoxia gradients. (ren2025theadaptabilityof pages 2-3)

**Bioprocessing / engineered systems**
- **Anaerobic digestion performance:** Addition of trace CaO2 (slow oxygen donor) plus magnetite increased methane yield to **423.4 mL CH4/g VS**, ~**26.8%** above control; CaO2 was interpreted to “enhance the viability of facultative microorganisms,” and magnetite supports conductive electron transfer (DIET) in syntrophic networks—an explicit real-world implementation where facultative oxygen handling improves anaerobic process stability/yield. (zhu2024metaproteomicsanalysisof pages 1-2)

### 5) Candidate causal-graph entities (nodes)

The following artifact provides curation-ready candidate nodes with suggested ontology grounding and evidence.

| Node label | Type | Brief role in facultative anaerobiosis | Example taxa | Suggested grounding | Key supporting source (citation id) |
|---|---|---|---|---|---|
| **Candidate causal-graph nodes** | **Type group** | **Brief role in facultative anaerobiosis** | **Example taxa** | **Suggested grounding** | **Key supporting source (citation id)** |
| Oxygen availability / oxic vs anoxic conditions | Environmental/expt factors | Primary environmental variable defining whether cells use aerobic respiration, anaerobic respiration, or fermentation | *Escherichia coli*, *Salmonella enterica*, *Staphylococcus aureus* | CHEBI:15379 (dioxygen) | (brown2023conservedmetabolicregulator pages 1-3, ricciardelli2025tracemetalsavailability pages 3-6) |
| Nanaerobic / microoxic conditions | Environmental/expt factors | Low-O2 regimes permit concurrent or transitional use of oxidases and anaerobic modules | *Bacteroides fragilis*, *Staphylococcus aureus* | ungrounded | (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains pages 7-9) |
| Biofilm hypoxia | Environmental/expt factors | Local O2 depletion in biofilms drives anaerobic metabolism and stress tolerance | *Pseudomonas aeruginosa* | ENVO:01000736 (biofilm) + ungrounded for hypoxia | (ren2025theadaptabilityof pages 2-3) |
| CCCP proton-motive-force uncoupling | Environmental/expt factors | Experimental ETC/PMF perturbation that reveals ArcA-linked shift toward fermentation | Enterobacterales spp. | CHEBI:5292 | (brown2023conservedmetabolicregulator pages 1-3) |
| ArcAB / ArcBA two-component system | Regulatory systems | Redox-responsive regulator coordinating aerobic-to-anaerobic transition and repressing aerobic respiration / promoting anaerobic programs | *E. coli*, *Salmonella enterica*, *Citrobacter freundii* | GO:0000155 (two-component sensor activity) / ungrounded complex label | (brown2023conservedmetabolicregulator pages 1-3, whittle2024effluxpumpsmediate pages 7-9, alvarez2024diversificationofsignal pages 1-2) |
| FNR (fumarate and nitrate reduction regulator) | Regulatory systems | Fe-S-cluster oxygen sensor activating anaerobic gene expression when O2 is low | *E. coli*, denitrifiers | ungrounded | (ricciardelli2025tracemetalsavailability pages 3-6, seagrove2024theroleof pages 32-35) |
| NarX/NarQ–NarL/NarP | Regulatory systems | Nitrate/nitrite-sensing system that induces nitrate/nitrite respiration genes and reprioritizes electron-acceptor usage | *E. coli* | ungrounded | (ricciardelli2025tracemetalsavailability pages 3-6) |
| Quinone/quinol pool redox state | Electron transport chain components | Internal redox signal sensed by ArcB-like systems to regulate respiratory mode switching | *E. coli*, *Salmonella enterica* | GO:0055114 (oxidation-reduction process) / ungrounded pool label | (whittle2024effluxpumpsmediate pages 7-9, alvarez2024diversificationofsignal pages 14-15) |
| Ubiquinone / ubiquinol pool | Electron transport chain components | High-potential quinone carrier associated with aerobic respiration and Arc redox sensing in many facultative anaerobes | *E. coli* | CHEBI:16389 (ubiquinone-8, candidate) | (alvarez2024diversificationofsignal pages 14-15, soria2024transcriptionalandmetabolic pages 14-15) |
| Menaquinone pool | Electron transport chain components | Lower-potential quinone carrier supporting low-O2 and anaerobic respiration | *Bacteroides fragilis*, *E. coli* | CHEBI:18084 (menaquinone) | (butler2023bacteroidesfragilismaintains pages 2-5) |
| Cytochrome bd oxidase (cyd) | Electron transport chain components | High-affinity terminal oxidase enabling respiration at low O2 | *Bacteroides fragilis*, *E. coli* | GO:0004129 (cytochrome-c oxidase activity, broad) / ungrounded specific complex | (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains pages 2-5) |
| NQR (Na+-translocating NADH:quinone oxidoreductase) | Electron transport chain components | Feeds electrons from NADH into quinone pool during low-O2/anaerobic respiration | *Bacteroides fragilis* | EC:7.2.1.1 | (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains pages 2-5) |
| NDH2 (type II NADH dehydrogenase) | Electron transport chain components | Alternative NADH oxidation route into quinone pool; complements NQR/NDH-I-like functions | *Bacteroides fragilis*, staphylococci | EC:7.1.1.2 | (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains pages 2-5) |
| Nitrate (NO3-) | Terminal electron acceptors | Alternative terminal electron acceptor used when O2 is limiting | *E. coli*, *Salmonella enterica* | CHEBI:17632 | (ricciardelli2025tracemetalsavailability pages 3-6, schulzmirbach2024engineeringnewtonaturebiochemical pages 1-2) |
| Nitrite (NO2-) | Terminal electron acceptors | Respiratory intermediate/alternative electron acceptor reduced in anaerobic metabolism | *E. coli*, *Shewanella oneidensis* | CHEBI:16301 | (ricciardelli2025tracemetalsavailability pages 3-6) |
| Fumarate | Terminal electron acceptors | Alternative terminal electron acceptor for anaerobic respiration | *Bacteroides fragilis*, *E. coli*, *Salmonella enterica* | CHEBI:18012 | (butler2023bacteroidesfragilismaintains pages 2-5, schulzmirbach2024engineeringnewtonaturebiochemical pages 1-2) |
| Dimethyl sulfoxide (DMSO) | Terminal electron acceptors | Alternative terminal electron acceptor in facultative anaerobic respiration | *E. coli*, *Salmonella enterica* | CHEBI:16385 | (schulzmirbach2024engineeringnewtonaturebiochemical pages 1-2, afinanisaUnknownyearmicrobialprimer pages 5-6) |
| Trimethylamine N-oxide (TMAO) | Terminal electron acceptors | Alternative terminal electron acceptor supporting anaerobic respiration | *E. coli* and other facultative anaerobes | CHEBI:15724 | (schulzmirbach2024engineeringnewtonaturebiochemical pages 1-2, afinanisaUnknownyearmicrobialprimer pages 5-6) |
| NarGHI / NarZYV nitrate reductase | Anaerobic respiration modules | Membrane nitrate reductase complex reducing nitrate during anaerobic respiration | *E. coli* | EC:1.7.5.1 | (ricciardelli2025tracemetalsavailability pages 3-6) |
| NapABGHC periplasmic nitrate reductase | Anaerobic respiration modules | Periplasmic nitrate-reduction branch used in alternative respiratory configurations | *E. coli* | EC:1.9.6.1 | (ricciardelli2025tracemetalsavailability pages 3-6) |
| NrfABCD nitrite reductase | Anaerobic respiration modules | Cytochrome c nitrite reductase reducing nitrite to ammonium in anaerobic respiration | *E. coli* | EC:1.7.2.2 | (ricciardelli2025tracemetalsavailability pages 3-6) |
| NirBD nitrite reductase | Anaerobic respiration modules | NADH-dependent nitrite reduction branch in anaerobic metabolism | *E. coli* | EC:1.7.1.15 | (ricciardelli2025tracemetalsavailability pages 3-6) |
| Fumarate reductase (frd) | Anaerobic respiration modules | Reduces fumarate to succinate; core anaerobic respiratory branch | *Bacteroides fragilis*, *E. coli* | EC:1.3.5.4 | (butler2023bacteroidesfragilismaintains pages 2-5) |
| DmsABC dimethyl sulfoxide reductase family complex | Anaerobic respiration modules | Molybdoenzyme complex enabling anaerobic respiration on methionine sulfoxide / DMSO-like acceptors under host oxidative stress | *Salmonella enterica* | EC:1.8.5.3 (family-level candidate) | (kim2024anaerobicrespirationof pages 1-3) |
| Methionine sulfoxide | Anaerobic respiration modules | Host-derived terminal electron acceptor reduced by DmsABC in intracellular anaerobic metabolism | *Salmonella enterica* | CHEBI:17489 | (kim2024anaerobicrespirationof pages 1-3) |
| Pyruvate formate lyase activation (pflA) | Fermentation/overflow modules | Activates pyruvate formate lyase, enabling anaerobic fermentative pyruvate dissimilation | *Enterococcus faecium* | ungrounded | (xu2024thefescluster pages 1-2) |
| Fermentation end products (lactate / acetate / formate) | Fermentation/overflow modules | Readouts and products of fermentative compensation when respiration is limited or uncoupled | Enterobacterales spp., *E. faecium* | CHEBI:24996 / CHEBI:30089 / CHEBI:15740 | (brown2023conservedmetabolicregulator pages 1-3, xu2024thefescluster pages 13-14) |
| SufB Fe-S cluster biosynthesis | Cofactors/metals | Supports assembly of Fe-S proteins required for anaerobic enzymes and gut colonization | *Enterococcus faecium* | ungrounded | (xu2024thefescluster pages 13-14, xu2024thefescluster pages 1-2) |
| Molybdenum cofactor (Moco) biosynthesis / moaABCDE | Cofactors/metals | Required for molybdoenzymes such as nitrate and DMSO-family reductases that expand anaerobic respiratory capacity | *E. coli* | KEGG:ec:moaA / ungrounded pathway label | (ricciardelli2025tracemetalsavailability pages 3-6) |
| Iron-sulfur [4Fe-4S] cluster | Cofactors/metals | Cofactor for FNR and multiple anaerobic enzymes; oxygen-labile sensory/functional module | *E. coli*, denitrifiers, *E. faecium* | CHEBI:30413 | (ricciardelli2025tracemetalsavailability pages 3-6, seagrove2024theroleof pages 32-35, xu2024thefescluster pages 1-2) |
| Molybdenum availability | Cofactors/metals | Gates ability to use molybdoenzyme-dependent electron acceptors | *E. coli* | CHEBI:33363 | (ricciardelli2025tracemetalsavailability pages 3-6) |
| Oxygen microelectrodes | Assays/phenotypic readouts | Measure local O2 gradients/hypoxia that explain facultative shifts in biofilms | *Pseudomonas aeruginosa* biofilms | ungrounded | (ren2025theadaptabilityof pages 2-3) |
| Oxygen consumption rate (OCR) measurements | Assays/phenotypic readouts | Quantitative readout of respiratory activity across oxygen regimes and perturbations | diverse bacteria | GO:0016491 (oxidoreductase activity, broad) / ungrounded assay | (rossi2026measuringbacterialoxygen pages 1-2) |
| Growth under oxic and anoxic conditions | Assays/phenotypic readouts | Core phenotype defining facultative anaerobiosis; measured in controlled O2 growth assays | diverse facultative anaerobes | METPO:1000605 | (butler2023bacteroidesfragilismaintains pages 1-2, brown2023conservedmetabolicregulator pages 1-3) |


*Table: This table lists evidence-backed candidate nodes for a TraitMech-style causal graph of facultative anaerobiosis. It groups environmental, regulatory, respiratory, fermentative, cofactor, and assay entities that are directly supported by the provided context and can guide curation into structured YAML.*

### 6) Evidence-backed candidate causal edges (triples)

The following artifact provides candidate subject–predicate–object edges with snippets, references, and uncertainty notes suitable for review and YAML curation.

| Subject (node) | Predicate (causal verb) | Object (node) | Evidence snippet (quoted or close paraphrase) | Reference | Notes/uncertainty |
|---|---|---|---|---|---|
| O2 | oxidizes/inactivates | FNR [4Fe-4S] oxygen sensor | “In the presence of oxygen, the fumarate and nitrate reduction regulatory protein (FNR) is inactivated through oxidation of its FeS cluster, preventing the transcription of the genes for anaerobic respirations.” (ricciardelli2025tracemetalsavailability pages 3-6) | Ricciardelli et al., 2025, bioRxiv, DOI:10.1101/2025.01.08.631794, https://doi.org/10.1101/2025.01.08.631794 (ricciardelli2025tracemetalsavailability pages 3-6) | Strong mechanistic support; preprint, but statement is explicit. |
| O2 limitation / reducing conditions | activates | ArcB/ArcBA signaling | Under oxygen limitation, ArcBA is “a direct sensor of the quinol pool redox state”; highly reduced quinol pool corresponds to high ArcA activity, consistent with aerobic-to-anaerobic transition. (whittle2024effluxpumpsmediate pages 7-9) | Whittle et al., 2024, mBio, DOI:10.1128/mbio.02370-24, https://doi.org/10.1128/mbio.02370-24 (whittle2024effluxpumpsmediate pages 7-9) | Activation is mediated indirectly through quinol pool redox, not direct O2 binding. |
| Quinone/quinol pool redox state | regulates | ArcB sensor kinase activity | “Oxidized quinones repress the kinase activity of ArcB”; ArcBA is described as “a direct sensor of the quinol pool redox state.” (whittle2024effluxpumpsmediate pages 7-9) | Whittle et al., 2024, mBio, DOI:10.1128/mbio.02370-24, https://doi.org/10.1128/mbio.02370-24 (whittle2024effluxpumpsmediate pages 7-9) | Strong for Enterobacterales; likely broadly applicable to ArcB-like systems but not universal. |
| Ubiquinone and menaquinone electron carriers | act as redox inputs for | ArcB redox regulation | “Ubiquinone and menaquinone electron carriers represent the yin and yang in the redox regulation of the ArcB sensor kinase”; “all three endogenous quinone species… are involved in controlling the activity of… ArcA.” (alvarez2024diversificationofsignal pages 14-15) | Alvarez et al., 2024, PLOS ONE, DOI:10.1371/journal.pone.0315238, https://doi.org/10.1371/journal.pone.0315238 (alvarez2024diversificationofsignal pages 14-15) | Strong for E. coli-type ArcB; some taxa have PAS-less ArcB variants with different sensing. |
| ArcA/ArcAB | represses | aerobic respiration program | “ArcAB, a two-component regulatory system that represses aerobic respiration, is a key mediator of metabolic adaptation.” (brown2023conservedmetabolicregulator pages 1-3) | Brown et al., 2023, mBio, DOI:10.1128/mbio.01448-23, https://doi.org/10.1128/mbio.01448-23 (brown2023conservedmetabolicregulator pages 1-3) | General statement; downstream target genes may differ by taxon. |
| CCCP-induced ETC/PMF perturbation | drives ArcA-mediated shift toward | fermentation | “CCCP treatment altered lactate, acetate, and lactate dehydrogenase activities, indicating an ArcA-driven shift toward fermentation that can be independent of ambient oxygen.” (close paraphrase) (brown2023conservedmetabolicregulator pages 1-3) | Brown et al., 2023, mBio, DOI:10.1128/mbio.01448-23, https://doi.org/10.1128/mbio.01448-23 (brown2023conservedmetabolicregulator pages 1-3) | Supported in bacteremia-associated Enterobacterales; edge includes experimental perturbation. |
| Alternative anaerobic electron acceptors (nitrate, fumarate, DMSO, TMAO) | enable | anaerobic electron transport chain operation | In facultative anaerobes, “alternative terminal electron acceptors (eg nitrate, fumarate, dimethyl sulfoxide or trimethylamine N-oxide) allow” anaerobic ETC operation when O2 is absent. (schulzmirbach2024engineeringnewtonaturebiochemical pages 1-2) | Schulz-Mirbach et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51029-x, https://doi.org/10.1038/s41467-024-51029-x (schulzmirbach2024engineeringnewtonaturebiochemical pages 1-2) | Broad, high-level edge; not all facultative anaerobes use all listed acceptors. |
| Nitrate / nitrite | activates via sensing by | NarX/NarQ → NarL/NarP | “Nitrate/nitrite are sensed by NarX/NarQ, which activate NarL/NarP…” (ricciardelli2025tracemetalsavailability pages 3-6) | Ricciardelli et al., 2025, bioRxiv, DOI:10.1101/2025.01.08.631794, https://doi.org/10.1101/2025.01.08.631794 (ricciardelli2025tracemetalsavailability pages 3-6) | Strong regulatory edge in E. coli-like systems; preprint. |
| NarL/NarP | induces | nar/nap/nrf/nir gene sets | NarX/NarQ “activate NarL/NarP to induce narGHJI/nap and nrf/nir genes and repress frd and fermentation genes.” (ricciardelli2025tracemetalsavailability pages 3-6) | Ricciardelli et al., 2025, bioRxiv, DOI:10.1101/2025.01.08.631794, https://doi.org/10.1101/2025.01.08.631794 (ricciardelli2025tracemetalsavailability pages 3-6) | Strong for canonical nitrate/nitrite control; taxon-specific regulon size may vary. |
| Molybdenum availability | enables | nitrate reductase-dependent anaerobic respiration | “Molybdenum availability is pivotal: without Mo only nitrite/fumarate respiration and fermentation remain”; nitrate reduction was absent in chelex-treated medium and rescued by adding Mo and Fe. (ricciardelli2025tracemetalsavailability pages 3-6) | Ricciardelli et al., 2025, bioRxiv, DOI:10.1101/2025.01.08.631794, https://doi.org/10.1101/2025.01.08.631794 (ricciardelli2025tracemetalsavailability pages 3-6) | Strong physiological support; preprint. Could also be modeled through Moco biosynthesis. |
| DmsABC | reduces | methionine sulfoxide (terminal electron acceptor) | “Anaerobic Salmonella uses the molybdenum cofactor-containing DmsABC enzymatic complex to reduce methionine sulfoxide.” (kim2024anaerobicrespirationof pages 1-3) | Kim et al., 2024, Cell Host & Microbe, DOI:10.1016/j.chom.2024.01.004, https://doi.org/10.1016/j.chom.2024.01.004 (kim2024anaerobicrespirationof pages 1-3) | Strong, host-context specific. |
| DmsABC-dependent methionine sulfoxide respiration | promotes | intracellular Salmonella survival under oxidative stress | DmsABC-associated anaerobic metabolism “protects intracellular Salmonella from the phagocyte NADPH oxidase” and supports redox balancing, methionine supply, and alkaline cytoplasm. (kim2024anaerobicrespirationof pages 1-3) | Kim et al., 2024, Cell Host & Microbe, DOI:10.1016/j.chom.2024.01.004, https://doi.org/10.1016/j.chom.2024.01.004 (kim2024anaerobicrespirationof pages 1-3) | Strong but infection-specific; should be marked context-dependent if curated as generic trait edge. |
| NQR and NDH2 | reduce | menaquinone/quinone pool | In B. fragilis, “Two NADH:quinone oxidoreductases, NQR and NDH2, carry most NADH dehydrogenase activity… channel electrons into the quinone pool.” (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains pages 2-5) | Butler et al., 2023, Journal of Bacteriology, DOI:10.1128/jb.00389-22, https://doi.org/10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 1-2, butler2023bacteroidesfragilismaintains pages 2-5) | Strong but based on Bacteroides; other taxa may use different dehydrogenase sets. |
| Reduced quinone/menaquinol pool | donates electrons to | cytochrome bd oxidase → O2 reduction | “Cytochrome bd oxidase transfers electrons from menaquinol to O2 for aerobic respiration.” (butler2023bacteroidesfragilismaintains pages 2-5) | Butler et al., 2023, Journal of Bacteriology, DOI:10.1128/jb.00389-22, https://doi.org/10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 2-5) | Strong biochemical edge for low-O2 branch. |
| Reduced quinone/menaquinol pool | donates electrons to | fumarate reductase → fumarate reduction | “Fumarate reductase (frd operon) reduces fumarate to succinate for anaerobic respiration.” (butler2023bacteroidesfragilismaintains pages 2-5) | Butler et al., 2023, Journal of Bacteriology, DOI:10.1128/jb.00389-22, https://doi.org/10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 2-5) | Strong biochemical edge for anaerobic branch. |
| sufB and pflA | are required for | anaerobic growth / gastrointestinal colonization | In E. faecium, deletion of “sufB or pflA… abolished gastrointestinal colonization in mice”; sufB deletion caused pronounced anaerobic growth defects. (xu2024thefescluster pages 1-2) | Xu et al., 2024, Gut Microbes, DOI:10.1080/19490976.2024.2359665, https://doi.org/10.1080/19490976.2024.2359665 (xu2024thefescluster pages 1-2) | Strong but taxon-specific; better curated as supporting mechanisms for some facultative anaerobes, not universal. |
| CaO2 + magnetite addition | increases | methane yield in anaerobic digestion via facultative microbes/DIET | Adding trace CaO2 plus magnetite “increased methane yield to 423.4 mL CH4/g VS, ~26.8% above control”; CaO2 “enhanced the viability of facultative microorganisms,” while magnetite supports electron bridges/DIET. (zhu2024metaproteomicsanalysisof pages 1-2) | Zhu et al., 2024, Applied and Environmental Microbiology, DOI:10.1128/aem.01451-23, https://doi.org/10.1128/aem.01451-23 (zhu2024metaproteomicsanalysisof pages 1-2) | Application edge; community-level process, not a direct trait mechanism for a single organism. |
| Oxygen gradient / biofilm hypoxia | increases | antibiotic resistance in mature biofilms | Oxygen microelectrode studies confirm localized hypoxia in biofilms, and oxygen deficiency is reported to account for “~70% of antibiotic resistance in mature biofilm cells.” (ren2025theadaptabilityof pages 2-3) | Ren et al., 2025, Frontiers in Cellular and Infection Microbiology, DOI:10.3389/fcimb.2025.1655335, https://doi.org/10.3389/fcimb.2025.1655335 (ren2025theadaptabilityof pages 2-3) | Useful application/phenotype edge; based on Pseudomonas biofilms and may not generalize to all facultative anaerobes. |


*Table: This table summarizes candidate subject-predicate-object edges for curating a TraitMech graph of facultative anaerobiosis, with source-backed snippets, references, and uncertainty notes. It emphasizes oxygen/redox sensing, respiratory switching, fermentation fallback, and applied ecological or clinical contexts.*

### 7) Expert synthesis and curation guidance (what is safe to curate now)

**High-confidence, cross-taxon core module (recommended for TraitMech core graph):**
- **Environmental O2 availability → redox state → regulation (FNR, ArcAB) → shift between aerobic respiration and anaerobic respiration/fermentation**, with quinone/quinol pools as central integrators. Evidence is explicit for FNR Fe–S oxidation and ArcB quinol redox sensing. (ricciardelli2025tracemetalsavailability pages 3-6, whittle2024effluxpumpsmediate pages 7-9)
- **Alternative terminal electron acceptors enable anaerobic ETC operation**, at least as a general facultative-anaerobe principle (nitrate/fumarate/DMSO/TMAO). (schulzmirbach2024engineeringnewtonaturebiochemical pages 1-2)

**Medium-confidence, taxon-specific modules (curate with taxon constraints or as ‘examples’):**
- **Bacteroides nanaerobic physiology** (NQR/NDH2 → menaquinone → cytochrome bd/fumarate reductase) is strongly evidenced but should be labeled as *Bacteroides*-specific; note that *B. fragilis* is often labeled “strict anaerobe” yet exhibits low-O2 respiration, illustrating boundary complexity. (butler2023bacteroidesfragilismaintains pages 2-5, butler2023bacteroidesfragilismaintains pages 10-11, butler2023bacteroidesfragilismaintains media 9271434f)
- **Salmonella DmsABC → methionine sulfoxide respiration** is robust but context-dependent (intracellular oxidative stress). (kim2024anaerobicrespirationof pages 1-3)
- **E. faecium sufB/pflA dependence for anaerobic growth/colonization** is strong but not universal for all facultative anaerobes. (xu2024thefescluster pages 1-2)

### 8) Warnings / claims that should not yet be curated as general

1. **Do not generalize a single ArcB sensing mechanism to all taxa.** PAS-less ArcB homologs may not use the same cysteine/quinone mechanism; curate “ArcAB senses quinone/quinol redox” as taxon-limited unless your graph explicitly targets γ-Proteobacteria. (alvarez2024diversificationofsignal pages 1-2, whittle2024effluxpumpsmediate pages 7-9)
2. **Avoid treating ‘nanaerobic respiration’ as equivalent to facultative anaerobiosis without explicit growth-with-and-without-O2 evidence**; low-O2 respiration can occur in organisms described as strict anaerobes. (butler2023bacteroidesfragilismaintains pages 10-11)
3. **Preprint caution:** some mechanistic statements and quantitative switching behavior in E. coli under metal depletion come from bioRxiv (not yet peer-reviewed). Use as supportive but consider requiring a peer-reviewed confirmation before elevating to core edges. (ricciardelli2025tracemetalsavailability pages 3-6)

---

## DOI-first bibliography (with URLs and publication dates)

1. Butler NL et al. *Bacteroides fragilis Maintains Concurrent Capability for Anaerobic and Nanaerobic Respiration*. **Journal of Bacteriology** (Jan 2023). DOI: **10.1128/jb.00389-22**. https://doi.org/10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 1-2)
2. Brown AN et al. *Conserved metabolic regulator ArcA responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia*. **mBio** (Oct 2023). DOI: **10.1128/mbio.01448-23**. https://doi.org/10.1128/mbio.01448-23 (brown2023conservedmetabolicregulator pages 1-3)
3. Yaeger LN et al. *Central metabolism is a key player in E. coli biofilm stimulation by sub-MIC antibiotics*. **PLOS Genetics** (Nov 2023). DOI: **10.1371/journal.pgen.1011013**. https://doi.org/10.1371/journal.pgen.1011013 (yaeger2023centralmetabolismis pages 1-2)
4. Kim J-S et al. *Anaerobic respiration of host-derived methionine sulfoxide protects intracellular Salmonella from the phagocyte NADPH oxidase*. **Cell Host & Microbe** (Mar 2024). DOI: **10.1016/j.chom.2024.01.004**. https://doi.org/10.1016/j.chom.2024.01.004 (kim2024anaerobicrespirationof pages 1-3)
5. Xu L et al. *The Fe-S cluster biosynthesis in Enterococcus faecium is essential for anaerobic growth and gastrointestinal colonization*. **Gut Microbes** (Jun 2024). DOI: **10.1080/19490976.2024.2359665**. https://doi.org/10.1080/19490976.2024.2359665 (xu2024thefescluster pages 1-2)
6. Lv H et al. *The impact of oxygen content on Staphylococcus epidermidis pathogenesis in ocular infection based on clinical characteristics, transcriptome and metabolome analysis*. **Frontiers in Microbiology** (Jul 2024). DOI: **10.3389/fmicb.2024.1409597**. https://doi.org/10.3389/fmicb.2024.1409597 (lv2024theimpactof pages 1-2)
7. Zhao J et al. *DegS regulates the aerobic metabolism of Vibrio cholerae via the ArcA-isocitrate dehydrogenase pathway for growth and intestinal colonization*. **Frontiers in Cellular and Infection Microbiology** (Nov 2024). DOI: **10.3389/fcimb.2024.1482919**. https://doi.org/10.3389/fcimb.2024.1482919 (zhao2024degsregulatesthe pages 1-2)
8. Alvarez AF et al. *Diversification of signal identity and modus operandi of the Haemophilus influenzae PAS-less ArcB sensor kinase*. **PLOS ONE** (Dec 2024). DOI: **10.1371/journal.pone.0315238**. https://doi.org/10.1371/journal.pone.0315238 (alvarez2024diversificationofsignal pages 1-2)
9. Whittle EE et al. *Efflux pumps mediate changes to fundamental bacterial physiology via membrane potential*. **mBio** (Oct 2024). DOI: **10.1128/mbio.02370-24**. https://doi.org/10.1128/mbio.02370-24 (whittle2024effluxpumpsmediate pages 7-9)
10. Zhu L et al. *Metaproteomics analysis of anaerobic digestion of food waste by the addition of calcium peroxide and magnetite*. **Applied and Environmental Microbiology** (Feb 2024). DOI: **10.1128/aem.01451-23**. https://doi.org/10.1128/aem.01451-23 (zhu2024metaproteomicsanalysisof pages 1-2)
11. Schulz-Mirbach H et al. *Engineering new-to-nature biochemical conversions by combining fermentative metabolism with respiratory modules*. **Nature Communications** (Aug 2024). DOI: **10.1038/s41467-024-51029-x**. https://doi.org/10.1038/s41467-024-51029-x (schulzmirbach2024engineeringnewtonaturebiochemical pages 1-2)
12. Ricciardelli A et al. *Trace metals availability controls terminal electron acceptor utilization in Escherichia coli*. **bioRxiv** (Jan 2025). DOI: **10.1101/2025.01.08.631794**. https://doi.org/10.1101/2025.01.08.631794 (ricciardelli2025tracemetalsavailability pages 3-6)
13. Ren L et al. *The adaptability of Pseudomonas aeruginosa biofilm in oxygen-limited environments*. **Frontiers in Cellular and Infection Microbiology** (Sep 2025). DOI: **10.3389/fcimb.2025.1655335**. https://doi.org/10.3389/fcimb.2025.1655335 (ren2025theadaptabilityof pages 2-3)



References

1. (brown2023conservedmetabolicregulator pages 1-3): Aric N. Brown, Mark T. Anderson, Sara N. Smith, Michael A. Bachman, and Harry L. T. Mobley. Conserved metabolic regulator arca responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia. Oct 2023. URL: https://doi.org/10.1128/mbio.01448-23, doi:10.1128/mbio.01448-23. This article has 11 citations and is from a domain leading peer-reviewed journal.

2. (schulzmirbach2024engineeringnewtonaturebiochemical pages 1-2): Helena Schulz-Mirbach, Jan Lukas Krüsemann, Theofania Andreadaki, Jana Natalie Nerlich, Eleni Mavrothalassiti, Simon Boecker, Philipp Schneider, Moritz Weresow, Omar Abdelwahab, Nicole Paczia, Beau Dronsella, Tobias J. Erb, Arren Bar-Even, Steffen Klamt, and Steffen N. Lindner. Engineering new-to-nature biochemical conversions by combining fermentative metabolism with respiratory modules. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51029-x, doi:10.1038/s41467-024-51029-x. This article has 32 citations and is from a highest quality peer-reviewed journal.

3. (ricciardelli2025tracemetalsavailability pages 3-6): Annarita Ricciardelli, Benoit de Pins, Jacopo Brusca, Monica Correggia, Luciano Di Iorio, Martina Cascone, Marco Giardina, Stefany Castaldi, Rachele Isticato, Roberta Iacono, Marco Moracci, Nunzia Nappi, Antonino Pollio, Costantino Vetriani, Serena Leone, Angelina Cordone, and Donato Giovannelli. Trace metals availability controls terminal electron acceptor utilization in escherichia coli. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.08.631794, doi:10.1101/2025.01.08.631794. This article has 4 citations.

4. (butler2023bacteroidesfragilismaintains pages 10-11): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

5. (butler2023bacteroidesfragilismaintains pages 1-2): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

6. (butler2023bacteroidesfragilismaintains pages 7-9): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

7. (rossi2026measuringbacterialoxygen pages 1-2): Chiara Scribani Rossi, Simone Angeli, Bruno Casciaro, Maria Rosa Loffredo, Maria Luisa Mangoni, Sharon Spizzichino, Giovanna Boumis, Manuel Espinosa-Urgel, Marzia Arese, Alessio Paone, Francesca Cutruzzolà, and Serena Rinaldo. Measuring bacterial oxygen consumption rate to probe metabolic signature and antimicrobial susceptibility. European Biophysics Journal, Mar 2026. URL: https://doi.org/10.1007/s00249-026-01834-7, doi:10.1007/s00249-026-01834-7. This article has 1 citations.

8. (ren2025theadaptabilityof pages 2-3): Ling Ren, Yang Yuan, Khaled Farea, Xu Feng, Jia He, Yi Liu, and Bowen Zheng. The adaptability of pseudomonas aeruginosa biofilm in oxygen-limited environments. Frontiers in Cellular and Infection Microbiology, Sep 2025. URL: https://doi.org/10.3389/fcimb.2025.1655335, doi:10.3389/fcimb.2025.1655335. This article has 7 citations.

9. (whittle2024effluxpumpsmediate pages 7-9): Emily E. Whittle, Oluwatosin Orababa, Alexander Osgerby, Pauline Siasat, Sarah J. Element, Jessica M. A. Blair, and Tim W. Overton. Efflux pumps mediate changes to fundamental bacterial physiology via membrane potential. mBio, Oct 2024. URL: https://doi.org/10.1128/mbio.02370-24, doi:10.1128/mbio.02370-24. This article has 39 citations and is from a domain leading peer-reviewed journal.

10. (alvarez2024diversificationofsignal pages 1-2): Adrián F. Alvarez, Antonio de Jesús Santillán-Jiménez, Eder Flores-Tamayo, Juan L. Teran-Melo, Oscar J. Vázquez-Ciros, and Dimitris Georgellis. Diversification of signal identity and modus operandi of the haemophilus influenzae pas-less arcb sensor kinase. PLOS ONE, 19:e0315238, Dec 2024. URL: https://doi.org/10.1371/journal.pone.0315238, doi:10.1371/journal.pone.0315238. This article has 0 citations and is from a peer-reviewed journal.

11. (butler2023bacteroidesfragilismaintains pages 2-5): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

12. (butler2023bacteroidesfragilismaintains media 9271434f): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

13. (butler2023bacteroidesfragilismaintains media 0e668668): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

14. (xu2024thefescluster pages 1-2): Linan Xu, Yajing Wu, Xiangpeng Yang, Xinxin Pang, Yansha Wu, Xingshuai Li, Xiayu Liu, Yuzhong Zhao, Lumin Yu, Peikun Wang, Bin Ye, Shijin Jiang, Junfei Ma, and Xinglin Zhang. The fe-s cluster biosynthesis in enterococcus faecium is essential for anaerobic growth and gastrointestinal colonization. Gut Microbes, Jun 2024. URL: https://doi.org/10.1080/19490976.2024.2359665, doi:10.1080/19490976.2024.2359665. This article has 12 citations and is from a peer-reviewed journal.

15. (kim2024anaerobicrespirationof pages 1-3): Ju-Sim Kim, Lin Liu, Sashi Kant, David J. Orlicky, Siva Uppalapati, Alyssa Margolis, Bennett J. Davenport, Thomas E. Morrison, Jennifer Matsuda, Michael McClelland, Jessica Jones-Carson, and Andres Vazquez-Torres. Anaerobic respiration of host-derived methionine sulfoxide protects intracellular salmonella from the phagocyte nadph oxidase. Cell Host &amp; Microbe, 32:411-424.e10, Mar 2024. URL: https://doi.org/10.1016/j.chom.2024.01.004, doi:10.1016/j.chom.2024.01.004. This article has 16 citations and is from a highest quality peer-reviewed journal.

16. (lv2024theimpactof pages 1-2): Hongling Lv, Wenjia Zhang, Zhu Zhao, Yingpu Wei, Zhengyilin Bao, Yizheng Li, Zhulin Hu, Deyao Deng, and Wenli Yuan. The impact of oxygen content on staphylococcus epidermidis pathogenesis in ocular infection based on clinical characteristics, transcriptome and metabolome analysis. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1409597, doi:10.3389/fmicb.2024.1409597. This article has 0 citations and is from a peer-reviewed journal.

17. (zhu2024metaproteomicsanalysisof pages 1-2): Lirong Zhu, Wen Li, Yongli Liu, Jinze Li, Linji Xu, Li Gu, Cong Chen, Yang Cao, and Qiang He. Metaproteomics analysis of anaerobic digestion of food waste by the addition of calcium peroxide and magnetite. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01451-23, doi:10.1128/aem.01451-23. This article has 13 citations and is from a peer-reviewed journal.

18. (seagrove2024theroleof pages 32-35): DJ Seagrove. The role of fnr-regulated srna in controlling bacterial denitrification. Unknown journal, 2024.

19. (alvarez2024diversificationofsignal pages 14-15): Adrián F. Alvarez, Antonio de Jesús Santillán-Jiménez, Eder Flores-Tamayo, Juan L. Teran-Melo, Oscar J. Vázquez-Ciros, and Dimitris Georgellis. Diversification of signal identity and modus operandi of the haemophilus influenzae pas-less arcb sensor kinase. PLOS ONE, 19:e0315238, Dec 2024. URL: https://doi.org/10.1371/journal.pone.0315238, doi:10.1371/journal.pone.0315238. This article has 0 citations and is from a peer-reviewed journal.

20. (soria2024transcriptionalandmetabolic pages 14-15): Sandra Soria, Ofelia E. Carreón-Rodríguez, Ramón de Anda, Noemí Flores, Adelfo Escalante, and Francisco Bolívar. Transcriptional and metabolic response of a strain of escherichia coli pts− to a perturbation of the energetic level by modification of [atp]/[adp] ratio. BioTech, 13:10, Apr 2024. URL: https://doi.org/10.3390/biotech13020010, doi:10.3390/biotech13020010. This article has 4 citations.

21. (afinanisaUnknownyearmicrobialprimer pages 5-6): Q Afinanisa, A Brooks, I Sanyaolu, and A Valiyaparambil. Microbial primer. Unknown journal, Unknown year.

22. (xu2024thefescluster pages 13-14): Linan Xu, Yajing Wu, Xiangpeng Yang, Xinxin Pang, Yansha Wu, Xingshuai Li, Xiayu Liu, Yuzhong Zhao, Lumin Yu, Peikun Wang, Bin Ye, Shijin Jiang, Junfei Ma, and Xinglin Zhang. The fe-s cluster biosynthesis in enterococcus faecium is essential for anaerobic growth and gastrointestinal colonization. Gut Microbes, Jun 2024. URL: https://doi.org/10.1080/19490976.2024.2359665, doi:10.1080/19490976.2024.2359665. This article has 12 citations and is from a peer-reviewed journal.

23. (yaeger2023centralmetabolismis pages 1-2): Luke N. Yaeger, Shawn French, Eric D. Brown, Jean Philippe Côté, and Lori L. Burrows. Central metabolism is a key player in e. coli biofilm stimulation by sub-mic antibiotics. PLOS Genetics, 19:e1011013, Nov 2023. URL: https://doi.org/10.1371/journal.pgen.1011013, doi:10.1371/journal.pgen.1011013. This article has 15 citations and is from a domain leading peer-reviewed journal.

24. (zhao2024degsregulatesthe pages 1-2): Jiajun Zhao, Xiaoyu Huang, Qingqun Li, Fangyu Ren, Huaqin Hu, Jianbo Yuan, Kaiying Wang, Yuanqin Hu, Jian Huang, and Xun Min. Degs regulates the aerobic metabolism of vibrio cholerae via the arca-isocitrate dehydrogenase pathway for growth and intestinal colonization. Frontiers in Cellular and Infection Microbiology, Nov 2024. URL: https://doi.org/10.3389/fcimb.2024.1482919, doi:10.3389/fcimb.2024.1482919. This article has 0 citations.