---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:56:22.176833'
end_time: '2026-06-18T00:18:40.722342'
duration_seconds: 1338.55
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH delta
  trait_identifier: METPO:1000232
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_delta
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH phenotype with numerical limits expressing the breadth (maximum
    minus minimum) of external pH supporting growth of an organism.
  parent_traits: METPO:1000531, METPO:1000534
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports the breadth of the pH-tolerance span as a derived descriptor reflecting
    overall pH-homeostasis flexibility.) | DOI:10.1016/j.tim.2007.02.005: proton motive
    force (pH-homeostasis review supports the proton motive force as the energetic
    constraint underlying broad versus narrow pH tolerance.)'
  causal_graph_summary: 'ph_delta_homeostasis_flexibility: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta
- **METPO identifier:** METPO:1000232
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits expressing the breadth (maximum minus minimum) of external pH supporting growth of an organism.
- **Parent traits:** METPO:1000531, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the breadth of the pH-tolerance span as a derived descriptor reflecting overall pH-homeostasis flexibility.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the proton motive force as the energetic constraint underlying broad versus narrow pH tolerance.)
- **Existing causal graph summary:** ph_delta_homeostasis_flexibility: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta.yaml`.

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
- **Trait label:** pH delta
- **METPO identifier:** METPO:1000232
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits expressing the breadth (maximum minus minimum) of external pH supporting growth of an organism.
- **Parent traits:** METPO:1000531, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the breadth of the pH-tolerance span as a derived descriptor reflecting overall pH-homeostasis flexibility.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the proton motive force as the energetic constraint underlying broad versus narrow pH tolerance.)
- **Existing causal graph summary:** ph_delta_homeostasis_flexibility: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **pH delta** (METPO:1000232)

**Trait label:** pH delta  
**METPO identifier:** METPO:1000232  
**Definition (given):** “A pH phenotype with numerical limits expressing the breadth (maximum minus minimum) of external pH supporting growth of an organism.”  
**Trait category:** ENVIRONMENT  

### Scope summary (curation-focused)
**What the trait represents.** pH delta is a *derived growth phenotype* defined as the difference between the highest and lowest **external pH values that support growth** under a specified assay regime (medium, buffering, aeration, inoculum history, endpoint definition for “growth”). It is distinct from (i) **pH optimum** (where growth is maximal), and (ii) the individual **minimum pH** and **maximum pH** for growth; pH delta is a summary statistic that collapses both boundaries into a single breadth measure. Quantitatively, it is often implicit in reported “pH optimum (range)” tables or explicit min–max statements (e.g., pH 6.8–11.0 implies pH delta = 4.2). Methanotroph examples include alkaliphiles with broad reported ranges such as *Methylomicrobium buryatense* (optimum 8.5–9.5; range 6.8–11.0) and *M. kenyense* (optimum 9.0–10.0; range 9.0–11.0) (yao2023howmethanotrophsrespond media 1bc0ffc0, yao2023howmethanotrophsrespond media bb130037).

**Boundary cases.** Many studies mix **growth** with **survival** after shock. For curation, pH delta should be tied to demonstrable growth (e.g., growth rate, OD increase, colony expansion), not only viability after exposure. Engineered *E. coli* work explicitly targets “mild acid tolerance” at pH ~5–6, which is more directly compatible with a growth-supporting range than “extreme acid survival” claims (qin2024characterizationofmild pages 1-2). Assay factors (notably buffering) can shift observed ranges; in sediment microcosms, adding HEPES buffer restored pH and relative abundance of taxa suppressed by pH shifts, underscoring that measured pH breadth is partially an assay construct (ianutsevich2023theroleof pages 1-2).

**Mechanistic interpretation (current understanding).** A broad external growth pH range is widely interpreted as emerging from **physicochemical homeostasis**—especially maintenance of intracellular pH and electrochemical gradients—via transport and bioenergetic modules (antiporters, proton pumps, ATPases), plus envelope and osmolyte adaptations that modulate proton permeability and local proton availability (poolman2023physicochemicalhomeostasisin pages 1-2, yao2023howmethanotrophsrespond pages 5-7).

---

## Key concepts and definitions (with current understanding)

### 1) External pH tolerance breadth vs pH homeostasis
- **pH delta (phenotype):** an observed *growth-supporting* external pH span (METPO:1000232).
- **pH homeostasis (mechanism):** the physiological capacity to keep intracellular pH and related physicochemical variables within functional bounds across environments. A 2023 FEMS Microbiology Reviews synthesis describes pH homeostasis as intertwined with PMF, transporters (Na+/H+, K+/H+ antiporters), respiratory chains, F0F1-ATPase, and decarboxylation pathways that prevent internal pH from becoming too low under acid stress (poolman2023physicochemicalhomeostasisin pages 1-2). 

### 2) Quantifying pH delta from reported ranges
- Methanotroph ecophysiology review tables provide many “optimum (range)” entries enabling direct computation of pH delta; Table 1 includes strain-specific pH ranges across acidic to alkaline taxa (yao2023howmethanotrophsrespond media 1bc0ffc0, yao2023howmethanotrophsrespond media bb130037).
- Fungal plate-growth studies can yield pH delta either from explicit “growth range” statements (e.g., *Mollisia* optimum 3.0–5.0) or from “no growth at pH 7.0” style boundaries; these are assay-dependent and may not reflect in situ limits (ianutsevich2023theroleof pages 4-5).

---

## Candidate mechanistic nodes (grouped) with ontology grounding suggestions
The following inventory is intended to seed `ph_delta.yaml` node selection.

| Group | Candidate node | Suggested grounding | Short relevance note |
|---|---|---|---|
| Processes/pathways | pH homeostasis | GO:0006885 | Core mechanistic process underlying ability to maintain growth across varying external pH; directly distinguished from the phenotype itself but a major determinant of wider pH breadth (jiang2024exogenousputrescineplays pages 1-2, ianutsevich2023theroleof pages 1-2). |
| Processes/pathways | Proton motive force generation | GO:0015986 | PMF supports intracellular pH regulation and energizes transport; reviews and physiology studies tie broad pH adaptation to maintenance of Δp/ΔpH across conditions (yao2023howmethanotrophsrespond pages 5-7, jong2024quantitativeproteomicsreveals pages 6-8). |
| Processes/pathways | Oxidative phosphorylation | GO:0006119, KEGG:00190 | Upregulated under acid-adaptation conditions in engineered and community systems, supporting ATP-dependent H+ transport and stress tolerance (jiang2024exogenousputrescineplays pages 9-12, qin2024characterizationofmild pages 1-2). |
| Processes/pathways | Glutamate-dependent acid resistance / GABA shunt | KEGG:00650 | Proton-consuming acid resistance module; putrescine-enhanced acid adaptability and E. coli acid resistance both implicate glutamate/GABA metabolism in reducing intracellular H+ burden (jiang2024exogenousputrescineplays pages 1-2, li2024responseofescherichia pages 10-12). |
| Processes/pathways | Lysine-dependent acid resistance | label-only candidate | Upregulated in engineered acid-tolerant E. coli under pH 6.0 and associated with improved mild-acid growth (qin2024characterizationofmild pages 1-2). |
| Processes/pathways | Arginine/agmatine acid resistance | label-only candidate | Amino-acid decarboxylation/antiport system that consumes protons and can increase low-pH tolerance span in neutralophiles (li2024responseofescherichia pages 10-12). |
| Processes/pathways | Trehalose biosynthetic/metabolic process | GO:0005992 | Broad-range fungi and transcriptomic datasets implicate trehalose and related osmolyte metabolism in pH adaptation and stability across acidic/alkaline conditions (ianutsevich2023theroleof pages 1-2, zhang2023transcriptomeanalysisreveals pages 7-10). |
| Processes/pathways | Compatible solute accumulation | GO:0006970 | Broad pH-range or polyextreme adaptation is associated with osmolytes such as trehalose, polyols, glycine betaine, glutamate, and proline (ianutsevich2023theroleof pages 1-2, ianutsevich2023theroleof pages 4-5). |
| Processes/pathways | Membrane lipid remodeling | GO:0006643 | Changes in fatty-acid saturation and phospholipid composition reduce proton permeability or recalibrate proton capture, especially in acidophiles and alkaliphiles (yao2023howmethanotrophsrespond pages 5-7, li2024responseofescherichia pages 5-7). |
| Processes/pathways | Cell wall / envelope biogenesis remodeling | GO:0009273 | pH adaptation often includes altered porins, peptidoglycan remodeling, and thickened walls; linked to acid and alkaline tolerance in bacteria and fungi (zhang2023transcriptomeanalysisreveals pages 13-14, li2024responseofescherichia pages 5-7). |
| Proteins/complexes/transporters | F-type H+-transporting ATPase / F0F1-ATP synthase | GO:0015078, EC:7.1.2.2, KEGG:K02111/K02112/K02115/K02116 | Central H+ translocation complex; ATPase expression/activity rises under acid-adaptive conditions and is repeatedly linked to pH homeostasis and growth under broad pH windows (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12). |
| Proteins/complexes/transporters | Mrp Na+/H+ antiporter complex (mrpABCDEFG) | KEGG:K05571-K05577 | Strong candidate alkaliphily/broad-range determinant; comparative genomics associates mrp genes with alkali-resistant lineages, and physiology identifies Mrp as vital for H+ import coupled to Na+ export (jong2024quantitativeproteomicsreveals pages 6-8, kim2024lineagespecificevolutionof pages 2-4). |
| Proteins/complexes/transporters | Monovalent cation:H+ antiporter | GO:0015385 | General class covering Na+/H+ or K+/H+ antiport critical for alkaliphiles and broader pH stress adaptability (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12). |
| Proteins/complexes/transporters | Na+/H+ exchanger | label-only candidate | Fungal acidophile genomes and alkaliphile models implicate Na+/H+ exchange in maintaining cytoplasmic pH across external pH extremes (ianutsevich2023theroleof pages 1-2). |
| Proteins/complexes/transporters | Respiratory complex I (NADH dehydrogenase I) | GO:0008137, KEGG:K00330-K00346 | Proton-pumping respiratory complex contributing to pH homeostasis; proteomics in alkaliphile C. thermarum linked regulation of Ndh-I to pH/oxygen adaptation (jong2024quantitativeproteomicsreveals pages 6-8). |
| Proteins/complexes/transporters | Terminal oxidases (cytochrome aa3 / ba3 oxidases) | GO:0004129 | Differential proton translocation stoichiometry affects energetic support for pH homeostasis; observed switch in alkaliphile respiratory chain under varying O2 (jong2024quantitativeproteomicsreveals pages 6-8). |
| Proteins/complexes/transporters | V-type ATPase | GO:0015991 | Reported in acidophilic fungi as one of the proton-pumping systems maintaining intracellular pH near optimal values under acidic environments (ianutsevich2023theroleof pages 1-2). |
| Proteins/complexes/transporters | P-type plasma membrane H+-ATPase Pma1 | UniProtKB:P13587 (species-specific exemplar), GO:0015078 | Acidophilic fungi use Pma1-like proton pumps for pH homeostasis and low-pH growth (ianutsevich2023theroleof pages 1-2). |
| Proteins/complexes/transporters | Potassium uptake transporter (KUP family) | label-only candidate | Acidophile genomes and methanotroph physiology link K+ uptake to positive membrane potential and reduced proton influx (yao2023howmethanotrophsrespond pages 5-7, ianutsevich2023theroleof pages 1-2). |
| Proteins/complexes/transporters | Kdp K+ transporter | KEGG:K01546/K01547/K01548/K01549 | Genome-based pH preference study found Kdp systems enriched in taxa preferring lower pH, suggesting relevance to low-pH adaptation (association, not direct causation) (ramoneda2023buildingagenomebased pages 3-5). |
| Proteins/complexes/transporters | OmpC porin | UniProtKB:P06996 (E. coli exemplar) | Acid tolerance mechanism in E. coli includes OmpC-mediated uptake balance for amino-acid-dependent AR systems; overexpression linked to improved tolerance (li2024responseofescherichia pages 5-7). |
| Proteins/complexes/transporters | OmpF porin | UniProtKB:P02931 (E. coli exemplar) | Downregulation under acid stress can reduce harmful influx and support acid resistance (li2024responseofescherichia pages 5-7). |
| Proteins/complexes/transporters | HdeA periplasmic chaperone | UniProtKB:P0AEK4 (E. coli exemplar) | Protects periplasmic proteins at very low pH; key node for low-pH survival (li2024responseofescherichia pages 5-7). |
| Proteins/complexes/transporters | HdeB periplasmic chaperone | UniProtKB:P0AEK2 (E. coli exemplar) | Active around pH 3–5 and included in engineered modules that improved mild-acid growth windows (qin2024characterizationofmild pages 2-3, li2024responseofescherichia pages 5-7). |
| Proteins/complexes/transporters | Cyclopropane fatty acid synthase | EC:2.1.1.79, KEGG:K00574 | Membrane lipid modification enzyme that reduces proton permeability and supports acid tolerance (li2024responseofescherichia pages 5-7). |
| Proteins/complexes/transporters | Putrescine transport ATPase / polyamine transporters | KEGG:K02052, KEGG:K11076 | Community pH-stress study found these transport functions differentially abundant with pH and putrescine supplementation (jiang2024exogenousputrescineplays pages 9-12). |
| Regulators/signaling | PacC/Rim101 ambient pH response transcription factor | GO:0003677 | Canonical fungal ambient-pH regulator; activated through Pal/Rim pathway to induce alkaline-expression programs and repress acid-expression programs (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2, fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7). |
| Regulators/signaling | Pal/Rim signaling pathway | label-only candidate | Membrane-to-nucleus pH sensing pathway in fungi controlling PacC/Rim101 activation and alkaline adaptation (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7, fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2). |
| Regulators/signaling | PhoP/PhoQ two-component system | KEGG:K07657/K07636 | Acid-adaptation regulator affecting membrane remodeling and multistress resistance, relevant to low-pH side of pH breadth (li2024responseofescherichia pages 5-7). |
| Regulators/signaling | OmpR response regulator | KEGG:K02484 | Noncanonical activation of acid-resistance genes in E. coli review; candidate controller of pH stress response breadth (li2024responseofescherichia pages 10-12). |
| Regulators/signaling | RpoS sigma factor | UniProtKB:P13445 (E. coli exemplar) | Global stress regulator repeatedly implicated in acid resistance and maintenance of viability under low pH (li2024responseofescherichia pages 10-12). |
| Regulators/signaling | GadE transcriptional regulator | UniProtKB:P63284 (E. coli exemplar) | Master regulator of glutamate-dependent acid resistance; engineered overexpression improved acid-tolerant growth and lysine production at pH 6.0 (qin2024characterizationofmild pages 1-2, qin2024characterizationofmild pages 2-3). |
| Regulators/signaling | Two-component response regulator orf00404 | label-only candidate | Heterologous expression in L. plantarum improved growth at pH 4.0, suggesting signaling-control nodes can widen operational pH tolerance (zheng2024heterologousexpressionof pages 1-2). |
| Regulators/signaling | Quorum-sensing lamA-D operon | label-only candidate | Upregulated in acid-tolerant recombinant L. plantarum under pH 4.0 and may participate in coordinated adaptation (zheng2024heterologousexpressionof pages 1-2). |
| Metabolites/chemicals | Proton | CHEBI:24636 | Direct stressor/driver for acid side of the trait; intracellular H+ consumption or export is a recurring causal mechanism (jiang2024exogenousputrescineplays pages 1-2, li2024responseofescherichia pages 10-12). |
| Metabolites/chemicals | Putrescine | CHEBI:17148 | Exogenous putrescine has pH-dependent, switch-like effects on biofilm pH adaptability by modulating H+ consumption, permeability, and ATPase-associated energetics (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12). |
| Metabolites/chemicals | γ-Aminobutyric acid (GABA) | CHEBI:16865 | Product of glutamate decarboxylation pathway linked to proton consumption and acid resistance (jiang2024exogenousputrescineplays pages 1-2, li2024responseofescherichia pages 10-12). |
| Metabolites/chemicals | Glutamate | CHEBI:29985 | Substrate for key proton-consuming acid resistance system; also compatible solute/metabolic hub in stress adaptation (jiang2024exogenousputrescineplays pages 1-2, ianutsevich2023theroleof pages 1-2). |
| Metabolites/chemicals | Arginine | CHEBI:29016 | Substrate in arginine/agmatine acid resistance, relevant to low-pH growth capacity (li2024responseofescherichia pages 10-12). |
| Metabolites/chemicals | Lysine | CHEBI:25094 | Substrate/product context for lysine-dependent acid resistance and industrial low-pH fermentation engineering (qin2024characterizationofmild pages 1-2). |
| Metabolites/chemicals | Trehalose | CHEBI:18128 | Recurrently associated with broad-range fungal pH adaptation and transcriptomic responses; osmoprotective and protein-protective role (ianutsevich2023theroleof pages 1-2, zhang2023transcriptomeanalysisreveals pages 7-10, ianutsevich2023theroleof pages 4-5). |
| Metabolites/chemicals | Arabitol | CHEBI:17522 | Major polyol in narrow-range acidophilic fungus; levels decline under pH stress, making it a candidate mechanistic readout node (ianutsevich2023theroleof pages 4-5). |
| Metabolites/chemicals | Mannitol | CHEBI:29864 | Major polyol in broad-range Mollisia sp.; candidate osmolyte contributing to stable growth over broader acidic range (ianutsevich2023theroleof pages 4-5). |
| Metabolites/chemicals | Glycine betaine | CHEBI:17750 | Compatible solute relevant to polyextreme adaptation and potentially wider pH tolerance via osmotic/ionic homeostasis coupling (ianutsevich2023theroleof pages 1-2). |
| Metabolites/chemicals | Proline | CHEBI:17203 | Compatible solute and stress metabolite implicated in fungal and bacterial pH-associated adaptation (ianutsevich2023theroleof pages 1-2). |
| Metabolites/chemicals | Organic acids | CHEBI:33575 | Industrially relevant drivers of acidification; accumulation lowers medium pH and selects for acid-tolerance mechanisms (li2024responseofescherichia pages 1-2). |
| Cellular structures | Cytoplasmic membrane | GO:0005886 | Primary barrier controlling proton influx/efflux; lipid saturation and composition changes are central to pH tolerance breadth (yao2023howmethanotrophsrespond pages 5-7, li2024responseofescherichia pages 5-7). |
| Cellular structures | Cell wall | GO:0005618 | Fungal cell wall thickening and bacterial peptidoglycan remodeling correlate with pH adaptation (zhang2023transcriptomeanalysisreveals pages 13-14, li2024responseofescherichia pages 5-7). |
| Cellular structures | S-layer | GO:0030111 | In alkaliphilic methanotroph models, acidic S-layer components may attract protons near the cell surface and facilitate alkaline adaptation (yao2023howmethanotrophsrespond pages 5-7). |
| Cellular structures | Periplasm | GO:0042597 | Site of acid-active chaperones HdeA/HdeB and proton-buffering events in Gram-negative acid resistance (li2024responseofescherichia pages 5-7). |
| Cellular structures | Biofilm extracellular polymeric substances | GO:0042710 | Biofilms and EPS can increase resilience to external pH fluctuations and alter local proton microenvironments (jiang2024exogenousputrescineplays pages 1-2). |
| Environmental/assay factors | External pH | ENVO:09200013 | Direct environmental variable defining the phenotype; pH delta is calculated from min/max external pH supporting growth (palmer2024dynamicevolutionof pages 1-5, yao2023howmethanotrophsrespond media 1bc0ffc0). |
| Environmental/assay factors | Acidic environment | ENVO:01000219 | Important context node for low-pH selective pressures; includes habitats down to pH 1 and fermentation acidification (ianutsevich2023theroleof pages 1-2, li2024responseofescherichia pages 1-2). |
| Environmental/assay factors | Alkaline environment | ENVO:01000254 | Important context node for high-pH selective pressures; includes soda soils/lakes and alkaline springs (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7, fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 2-4). |
| Environmental/assay factors | Buffered medium / buffering capacity | label-only candidate | Strong assay modifier because measured growth range depends on whether pH is maintained or allowed to drift during growth (palmer2024dynamicevolutionof pages 1-5, li2024responseofescherichia pages 1-2). |
| Environmental/assay factors | Oxygen availability | ENVO:09200001 | Alters respiratory chain usage and antiporter demands, affecting pH homeostasis capacity in alkaliphiles (jong2024quantitativeproteomicsreveals pages 6-8). |
| Environmental/assay factors | Salinity / Na+ concentration | ENVO:3100031, CHEBI:29101 | Frequently coupled to alkaline adaptation because Na+/H+ antiport and ionic homeostasis are co-selected in haloalkaliphiles (kim2024lineagespecificevolutionof pages 2-4, palmer2024dynamicevolutionof pages 1-5). |
| Environmental/assay factors | Carbon source / medium composition | label-only candidate | PMF, acid production, and pH drift depend strongly on substrate use; several studies show growth and bioenergetics differ by carbon source and pH (jong2024quantitativeproteomicsreveals pages 6-8, li2024responseofescherichia pages 1-2). |
| Environmental/assay factors | Adaptation regime / prior acid exposure | label-only candidate | Mild-acid preadaptation and engineered regulatory states can change the observed pH range supporting growth or survival (qin2024characterizationofmild pages 1-2, zheng2024heterologousexpressionof pages 1-2). |
| Environmental/assay factors | Growth endpoint criterion | label-only candidate | Boundary case for curation: pH delta should reflect growth-supporting range, not merely survival after acid/alkali shock; many papers mix these concepts (qin2024characterizationofmild pages 1-2, li2024responseofescherichia pages 1-2). |


*Table: This table lists candidate mechanistic nodes relevant to microbial pH tolerance breadth, grouped by biological type and annotated with suggested ontology grounding. It is useful for selecting curation-ready TraitMech nodes while separating well-supported mechanisms from label-only candidates that need further grounding.*

---

## Evidence-backed candidate causal edges (triples) for TraitMech
The following table emphasizes edges that are either (i) directly causal in an experiment/engineering context, or (ii) mechanistically explicit in authoritative reviews. Association-only genome correlations are labeled **uncertain**.

| Edge (S–P–O) | Node grounding suggestions | Evidence strength | Taxon/assay scope | Reference | DOI | URL | Publication month/year | Evidence snippet/quote | Curation notes |
|---|---|---|---|---|---|---|---|---|---|
| external pH homeostasis → enables → broader external pH growth breadth (pH delta) | GO:0006885 → METPO:1000232 | strong | General bacteria; review-level mechanism for growth across pH | Poolman, 2023, *Physicochemical homeostasis in bacteria*, FEMS Microbiology Reviews | 10.1093/femsre/fuad033 | https://doi.org/10.1093/femsre/fuad033 | Jun 2023 | “Na+/H+ and K+/H+ antiporters are listed as key regulators of pH homeostasis” and proton-pumping systems “prevent[] the internal pH from becoming too low” (poolman2023physicochemicalhomeostasisin pages 1-2) | Good high-level edge for TraitMech. Mechanistic but not taxon-specific; suitable as parent edge linking homeostasis flexibility to pH delta. |
| proton motive force generation → supports → external pH homeostasis | GO:0015986 → GO:0006885 | strong | General bacteria; review-level | Poolman, 2023, *Physicochemical homeostasis in bacteria*, FEMS Microbiology Reviews | 10.1093/femsre/fuad033 | https://doi.org/10.1093/femsre/fuad033 | Jun 2023 | decarboxylation reactions “can thus causally store free energy as PMF for ATP synthesis” and PMF-linked systems regulate internal pH (poolman2023physicochemicalhomeostasisin pages 1-2) | Strong mechanistic support; this is closer to the existing evidence about PMF than a direct pH-delta edge. |
| F-type H+-transporting ATPase (F0F1-ATPase) activity → supports → external pH homeostasis | GO:0015078, EC:7.1.2.2 → GO:0006885 | strong | General bacteria; review-level | Poolman, 2023, *Physicochemical homeostasis in bacteria*, FEMS Microbiology Reviews | 10.1093/femsre/fuad033 | https://doi.org/10.1093/femsre/fuad033 | Jun 2023 | “F0F1-ATPase is mechanistically described as using three to five protons per ATP synthesized” and is among systems that “prevent[] the internal pH from becoming too low” (poolman2023physicochemicalhomeostasisin pages 1-2) | Strong but broad. Best curated as ATPase → pH homeostasis rather than directly to pH delta. |
| ATPase expression/activity → increases → acid-condition pH stress adaptability | GO:0015078 → label-only candidate: acid pH stress adaptability | strong | Biofilm-based activated sludge; putrescine-treated community under acidic vs alkaline conditions | Jiang et al., 2024, *Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge*, Applied and Environmental Microbiology | 10.1128/AEM.00569-24 | https://doi.org/10.1128/AEM.00569-24 | Jul 2024 | “Putrescine also stimulates ATPase expression, improving H+ transmembrane transport and oxidative phosphorylation, thereby enhancing energy utilization” (jiang2024exogenousputrescineplays pages 1-2) | Strong within this assay; community-level and putrescine-dependent. Curate with assay/treatment qualifier. |
| monovalent cation:H+ antiporter activity → supports → alkaline-condition pH stress adaptability | GO:0015385 → label-only candidate: alkaline pH stress adaptability | strong | Alkaliphiles in community/review context | Jiang et al., 2024, *Exogenous putrescine...*, AEM | 10.1128/AEM.00569-24 | https://doi.org/10.1128/AEM.00569-24 | Jul 2024 | “For alkali tolerance, alkaliphiles use ion-transport mechanisms—monovalent antiporters that exchange Na+ or K+ to facilitate proton entry” (jiang2024exogenousputrescineplays pages 1-2) | Strong conceptually, but generic class rather than named gene. Good candidate edge from antiporter activity to alkaline adaptation/homeostasis. |
| Mrp Na+/H+ antiporter complex presence → associated with → higher-pH preference / alkali resistance | KEGG:K05571-K05577 | uncertain | Comparative genomics across environmental bacteria; not direct phenotype manipulation | Ramoneda et al., 2023, *Building a genome-based understanding of bacterial pH preferences*, Science Advances | 10.1126/sciadv.adf8998 | https://doi.org/10.1126/sciadv.adf8998 | Apr 2023 | “Among the gene types linked to higher-pH preferences were Na+/H+ antiporters (specifically PhaGF, MnhG, MrpF, and YufB)”; authors “caution that presence/association does not prove causation” (ramoneda2023buildingagenomebased pages 3-5) | Keep marked uncertain. Useful as comparative-genomics support for node prioritization, not sufficient alone for a curated causal edge. |
| Mrp Na+/H+ antiporter complex → facilitates → Na+ export coupled to H+ import | KEGG:K05571-K05577 | strong | *Caldalkalibacillus thermarum* physiology/proteomics under varying O2 | de Jong et al., 2024, *Quantitative proteomics reveals oxygen-induced adaptations in Caldalkalibacillus thermarum TA2.A1...*, Frontiers in Microbiology | 10.3389/fmicb.2024.1468929 | https://doi.org/10.3389/fmicb.2024.1468929 | Oct 2024 | Mrp is described as “'a vital protein for alkaliphiles' that 'facilitates the export of Na+ coupled with the import of H+'” (jong2024quantitativeproteomicsreveals pages 6-8) | Strong mechanistic edge for Mrp function. Indirect to pH delta, but highly relevant. |
| low oxygen availability → decreases → Mrp Na+/H+ antiporter abundance | ENVO:09200001 → KEGG:K05571-K05577 | strong | *C. thermarum* chemostat proteomics | de Jong et al., 2024, *Quantitative proteomics...*, Frontiers in Microbiology | 10.3389/fmicb.2024.1468929 | https://doi.org/10.3389/fmicb.2024.1468929 | Oct 2024 | Mrp abundance is “'significantly downregulated at lower O2 concentrations'” (jong2024quantitativeproteomicsreveals pages 6-8) | Important environmental modifier edge. Relevant because pH-delta assays may shift with O2 regime in alkaliphiles. |
| saturated membrane fatty acids / lipid remodeling → decreases → proton permeability | GO:0006643, GO:0005886 | strong | Acidophilic methanotrophs; review of described physiology | Yao et al., 2023, *How methanotrophs respond to pH: A review of ecophysiology*, Frontiers in Microbiology | 10.3389/fmicb.2022.1034164 | https://doi.org/10.3389/fmicb.2022.1034164 | Jan 2023 | acidophilic strains have membranes “enriched in saturated fatty acids to reduce proton permeability” and this “minimizes proton influx in extremely acidic environments” (yao2023howmethanotrophsrespond pages 5-7) | Strong mechanistic edge. Good generalizable node for low-pH side of pH breadth. |
| altered phospholipid composition → regulates → proton flux at high external pH | GO:0006643 | strong | Alkaliphilic methanotrophs | Yao et al., 2023, *How methanotrophs respond to pH...*, Frontiers in Microbiology | 10.3389/fmicb.2022.1034164 | https://doi.org/10.3389/fmicb.2022.1034164 | Jan 2023 | “shifts in phospholipid composition (increased PG, PC, CL; decreased PE, PS, PA) in response to high pH to regulate proton flux” (yao2023howmethanotrophsrespond pages 5-7) | Strong but taxon-specific. Could be curated as membrane lipid composition → alkaline pH homeostasis. |
| acidic S-layer glycoproteins / negative surface charge → promotes → proton capture near cell surface | GO:0030111 | strong | Alkaliphilic methanotrophs | Yao et al., 2023, *How methanotrophs respond to pH...*, Frontiers in Microbiology | 10.3389/fmicb.2022.1034164 | https://doi.org/10.3389/fmicb.2022.1034164 | Jan 2023 | “S-layer glycoproteins ... enhance net negative surface charge to attract external protons” (yao2023howmethanotrophsrespond pages 5-7) | Strong and mechanistically useful for alkaline adaptation. Probably taxon-limited; curate with caution. |
| symporter/antiporter proton discharge systems → decreases → excess intracellular protons | label-only candidate: secondary H+ antiport/symport | strong | Acidophilic methanotrophs | Yao et al., 2023, *How methanotrophs respond to pH...*, Frontiers in Microbiology | 10.3389/fmicb.2022.1034164 | https://doi.org/10.3389/fmicb.2022.1034164 | Jan 2023 | “Secondary symporters/antiporters are reported to remove excess intracellular protons, discharging protons to cope with acid stress” (yao2023howmethanotrophsrespond pages 5-7) | Generic transporter class; useful if grounding to a broad antiporter activity node. |
| trehalose/polyol maintenance → associated with → broader acidic growth range | CHEBI:18128, CHEBI:polyol(label-only) | strong | Acidophilic fungi comparing narrow vs broad pH-range species | Ianutsevich et al., 2023, *The role of osmolytes and membrane lipids in the adaptation of acidophilic fungi*, Microorganisms | 10.3390/microorganisms11071733 | https://doi.org/10.3390/microorganisms11071733 | Jul 2023 | broad-range *Mollisia* sp. “maintained or increased osmolytes and stable membrane lipid composition”, whereas narrow-range *P. gigantea* showed “decreased osmolytes and altered membrane lipids” (ianutsevich2023theroleof pages 1-2) | This is one of the best breadth-specific edges because it explicitly contrasts broad vs narrow pH-range phenotypes. |
| trehalose decrease → associated with → narrower acidic growth performance | CHEBI:18128 | strong | *Phlebiopsis gigantea* vs *Mollisia* sp.; plate growth assays | Ianutsevich et al., 2023, *The role of osmolytes and membrane lipids...*, Microorganisms | 10.3390/microorganisms11071733 | https://doi.org/10.3390/microorganisms11071733 | Jul 2023 | in the narrow-range fungus, total CaP fell threefold, with “trehalose decreasing eightfold” as growth dropped sharply outside optimum (ianutsevich2023theroleof pages 4-5) | Strong phenotype-linked association, but still not a direct intervention. Curate as supportive/conditional unless a direct manipulation study is found. |
| glutamate-dependent acid resistance / GABA pathway → consumes → intracellular H+ | KEGG:00650, CHEBI:29985, CHEBI:16865 | strong | Biofilm-based activated sludge with exogenous putrescine; also supported by E. coli review | Jiang et al., 2024, *Exogenous putrescine...*, AEM | 10.1128/AEM.00569-24 | https://doi.org/10.1128/AEM.00569-24 | Jul 2024 | protonated putrescine “consumes intracellular H+ by enhancing the glutamate-based acid resistance system and the γ-aminobutyric acid pathway” (jiang2024exogenousputrescineplays pages 1-2) | Strong causal edge for pathway function. Supports homeostasis mechanism on low-pH side. |
| amino-acid decarboxylase acid-resistance systems → increase → low-pH tolerance | label-only candidates: glutamate/arginine/lysine decarboxylase systems | strong | *E. coli* review and engineered mild-acid tolerance context | Li et al., 2024, *Response of Escherichia coli to Acid Stress...*, Microorganisms | 10.3390/microorganisms12091774 | https://doi.org/10.3390/microorganisms12091774 | Aug 2024 | review lists “amino-acid decarboxylase systems ... that consume protons and export corresponding amines” as key mechanisms (li2024responseofescherichia pages 10-12) | Review-based but authoritative; suitable for generic mechanistic edge, less suitable for a specific gene edge without primary paper. |
| synthetic acid-tolerance module (gadE + hdeB + sodB + katE) overexpression → increases → growth under mild acid stress | gadE(label-only), hdeB(UniProt exemplar), sodB, katE | strong | Engineered *E. coli* SC3124 at pH 6.0 | Qin et al., 2024, *Characterization of Mild Acid Stress Response in an Engineered Acid-Tolerant Escherichia coli Strain*, Microorganisms | 10.3390/microorganisms12081565 | https://doi.org/10.3390/microorganisms12081565 | Jul 2024 | “the overexpression of synthetic acid-tolerance genes leads to metabolic changes that confer mild acid stress resistance”; final OD600 at pH 6.0 was “131% and 124%” of parent comparisons (qin2024characterizationofmild pages 1-2) | Excellent applied edge. Taxon- and engineering-specific, but directly causal and quantitative. |
| oxidative phosphorylation upregulation → increases → proton export / resistance to cytoplasmic acidification | GO:0006119 → GO:0006885 | strong | Engineered *E. coli* SC3124 at pH 6.0 | Qin et al., 2024, *Characterization of Mild Acid Stress Response...*, Microorganisms | 10.3390/microorganisms12081565 | https://doi.org/10.3390/microorganisms12081565 | Jul 2024 | increased oxidative phosphorylation is described as “generating a proton motive force (PMF) and a higher proton export rate, which causally helps cells resist decreases in cytoplasmic pH” (qin2024characterizationofmild pages 13-14) | Strong and more mechanistic than the engineering module itself; links PMF to acid tolerance. |
| PacC/Rim101 pathway activation → activates/represses → alkaline-/acid-expressed genes | label-only candidate: PacC/Rim101 pathway | strong | Fungal ambient-pH response, especially alkaliphiles/alkali-tolerant fungi | Fernández-López et al., 2023, *Alkaliphilic/Alkali-Tolerant Fungi: Molecular, Biochemical, and Biotechnological Aspects*, Journal of Fungi | 10.3390/jof9060652 | https://doi.org/10.3390/jof9060652 | Jun 2023 | “Active PacC represses acid-expressed genes and activates alkaline-expressed genes” via the Pal/Rim pathway (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2, fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7) | Strong regulatory edge for fungi, but downstream link to pH delta is inferred rather than directly measured. |
| PhoP/PhoQ two-component system → modulates → acid-adaptation membrane remodeling / multistress resistance | KEGG:K07657/K07636 | strong | *E. coli* acid-stress review context | Li et al., 2024, *Response of Escherichia coli to Acid Stress...*, Microorganisms | 10.3390/microorganisms12091774 | https://doi.org/10.3390/microorganisms12091774 | Aug 2024 | the review identifies “PhoQ/PhoP” among regulatory systems modulating acid-resistance genes and notes membrane/LPS remodeling under acid stress (li2024responseofescherichia pages 10-12, li2024responseofescherichia pages 5-7) | Review-derived. Good regulatory node candidate, but direct pH-delta effect should be considered moderate unless primary perturbation data are added. |
| salinity / high Na+ conditions → co-selects for → Na+/H+ antiporter-based pH homeostasis | CHEBI:29101, ENVO:salinity(label-only) | uncertain | Comparative genomics of halo/alkali-resistant lineages | Kim et al., 2024, *Lineage-specific evolution of Aquibium...*, AEM | 10.1128/AEM.02091-23 | https://doi.org/10.1128/AEM.02091-23 | Feb 2024 | “Halotolerant and alkali-resistant Aquibium ... possessed many ... sodium/proton antiporter subunits composed of seven genes (mrpABCDEFG)” (kim2024lineagespecificevolutionof pages 2-4) | Comparative, not manipulative. Useful context edge linking salinity and pH-adaptation mechanisms; mark uncertain. |
| buffering capacity / buffer addition → alters → observed community composition under pH stress | label-only candidate: buffered medium | uncertain | Anoxic marine sediment microcosms after SRB inhibition | Liang et al., 2023, *Niche Modification by Sulfate-Reducing Bacteria Drives Microbial Community Assembly...*, mBio | 10.1128/mbio.03535-22 | https://doi.org/10.1128/mbio.03535-22 | Apr 2023 | “the addition of pH buffer (HEPES) in SRB-inhibited treatment microcosms restored the pH and the relative abundances of these bacteria” (ianutsevich2023theroleof pages 1-2) | Not a direct pH-delta mechanism, but very important assay-factor warning: buffering can change the apparent growth-supporting pH range. Mark uncertain/experimental-factor only. |


*Table: This table compiles curation-ready candidate causal edges for microbial external pH growth breadth, emphasizing recent 2023-2024 evidence. It distinguishes strong mechanistic claims from uncertain comparative or assay-specific associations and notes taxonomic/experimental scope for TraitMech curation.*

---

## Recent developments (prioritizing 2023–2024)

### 1) Genome-to-environment inference of pH preference (and candidate mechanisms)
A 2023 *Science Advances* study built a machine-learning framework to infer bacterial pH preference from genome content using distributions across pH gradients. It identified gene types consistently associated with pH, including multiple **Na+/H+ antiporter components** associated with higher pH preferences, and **Kdp K+ transporters** associated with lower pH preference—while explicitly cautioning that associations do not equal causation (ramoneda2023buildingagenomebased pages 3-5). This is valuable for node prioritization in a causal graph but should be curated as *hypothesis-supporting* unless paired with perturbation evidence.

### 2) Quantitative multi-omics linking pH stress adaptation to energy metabolism and transport
- In 2024 activated-sludge biofilms, exogenous **putrescine** showed a “switch-like” pH-dependent effect, promoting biofilm formation under acid stress but inhibiting under alkaline stress. Mechanistically, protonated putrescine increased membrane permeability, enhanced glutamate-based acid resistance and the GABA pathway (intracellular H+ consumption), and stimulated ATPase expression and oxidative phosphorylation under acidic conditions (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12). The study also reports ATP/ADP shifts and coordinated changes in proton-pump/ATP synthase gene categories across pH regimes (jiang2024exogenousputrescineplays pages 9-12).

### 3) Engineered tolerance modules for low-pH bioprocess operation
A 2024 study on engineered *E. coli* (SC3124) reports that fine-tuning a synthetic module combining **gadE** (proton-consuming AR), **hdeB** (periplasmic chaperone), and ROS scavengers (**sodB**, **katE**) increased growth robustness under mild acid (pH 6.0), with final OD600 reaching **131%** and **124%** of parent comparators (qin2024characterizationofmild pages 1-2). The same work links improved tolerance to upregulated oxidative phosphorylation/TCA and describes oxidative phosphorylation as increasing proton export rate and helping resist cytoplasmic acidification (qin2024characterizationofmild pages 13-14). Applied implications include reduced neutralization costs and broader workable pH windows in fermentation (qin2024characterizationofmild pages 2-3).

### 4) Explicit quantitative pH growth ranges for environmental isolates
A 2024 comparative genomic/evolutionary analysis of geothermal Aquificaceae proposed that diversification into springs spanning extreme chemistries was enabled by the dynamic evolution of nitrogen-cycle and **pH homeostasis genes**, reporting wide growth ranges such as **pH 6.0–9.5** and **pH 5.5–10.0** for two isolates (preprint) (palmer2024dynamicevolutionof pages 1-5). This provides direct min/max pH range statements useful for pH delta phenotyping.

---

## Current applications and real-world implementations

### 1) Industrial fermentation and organic-acid production
Organic acid accumulation can depress medium pH substantially, motivating either neutralization (added base) or strain engineering for operation at lower pH. The 2024 engineered *E. coli* module demonstrates a practical strategy to improve growth and productivity at pH 6.0, with a reported **lysine yield increase up to 115% at pH 6.0** in a bioreactor context (qin2024characterizationofmild pages 2-3). This is a direct example of widening the operational pH window for a production chassis.

### 2) Environmental biotechnology (biofilms, wastewater)
Activated-sludge biofilms are exposed to fluctuating pH; exogenous polyamines (putrescine) are presented as potential “technical measures” to regulate biofilm formation and stability under acidic conditions by enhancing proton consumption pathways and ATPase-driven H+ transport, though effects reverse under alkaline conditions (jiang2024exogenousputrescineplays pages 1-2).

### 3) Extremophile-based processes (acidophiles/alkaliphiles)
Mechanistic features recurring in acidophiles/alkaliphiles—ion/proton antiport, membrane adaptations, and proton capture at the surface—are discussed as general adaptation strategies relevant to technologies that operate under extreme pH (e.g., bioleaching or alkaline bioprocesses), although direct pH-delta engineering outcomes are not uniformly quantified in the provided evidence set (yao2023howmethanotrophsrespond pages 5-7, poolman2023physicochemicalhomeostasisin pages 1-2).

---

## Expert opinions / authoritative synthesis

- **Physicochemical homeostasis viewpoint.** Poolman (2023) frames intracellular pH regulation as part of a broader “physicochemical homeostasis” program linked to cellular energy state and transport. The review emphasizes that antiporters, respiratory proton pumps, F0F1-ATPase, and proton-consuming pathways jointly prevent deleterious cytosolic pH shifts, making them central mechanistic candidates for pH delta breadth (poolman2023physicochemicalhomeostasisin pages 1-2).
- **Ecophysiology viewpoint across taxa.** Yao et al. (2023) synthesize that acidophiles reduce proton influx via saturated membranes and positive membrane potential, while alkaliphiles may rely on negatively charged surface structures (S-layer) and lipid remodeling to capture and route scarce protons, highlighting multiple distinct mechanistic “solutions” that can broaden tolerated external pH ranges (yao2023howmethanotrophsrespond pages 5-7).

---

## Relevant statistics and quantitative data (from recent studies)

1) **Methanotroph pH ranges (for computing pH delta):** Table 1 provides strain-level “pH optimum (range)” values including examples such as *Methylomicrobium buryatense* (range 6.8–11.0) and *M. kenyense* (9.0–11.0) (yao2023howmethanotrophsrespond media 1bc0ffc0, yao2023howmethanotrophsrespond media bb130037).

2) **Acidophilic fungi: narrow vs broad growth performance:** *Phlebiopsis gigantea* shows peak growth rate **3.2 mm/day at pH 4.0** but a sharp decline (threefold lower) at pH 3.0 and 5.0; *Mollisia* sp. has a broader active growth range (3.0–5.0) though lower optimum growth rate (**1.6 mm/day**) (ianutsevich2023theroleof pages 4-5). These comparisons link pH breadth phenotypes to osmolyte and lipid stability (ianutsevich2023theroleof pages 1-2).

3) **Engineered *E. coli* mild-acid growth improvement:** SC3124 final OD600 at pH 6.0 was **131%** and **124%** of parent controls under the compared conditions (qin2024characterizationofmild pages 1-2). A bioreactor application reports lysine yield increases up to **115% at pH 6.0** (qin2024characterizationofmild pages 2-3).

4) **Biofilm energy-state shifts across pH with putrescine:** intracellular ATP and ADP increased by **58%** and **26%** under acidic conditions and decreased under alkaline conditions; oxidative phosphorylation activity increased at low pH and decreased at high pH (jiang2024exogenousputrescineplays pages 9-12).

5) **Aquificaceae isolate growth ranges:** reported growth spans include **pH 6.0–9.5** and **pH 5.5–10.0** (palmer2024dynamicevolutionof pages 1-5).

---

## Ontology grounding notes (CURIE suggestions)
- The node/edge tables above provide suggested CURIEs when stable identifiers were clear. Many elements (e.g., “lysine-dependent acid resistance”) are included as **label-only candidates** pending selection of a reference ontology term (KEGG module, MetaCyc pathway, or GO biological process) appropriate for TraitMech.

---

## Warnings: claims not yet ready for TraitMech curation
1) **Association ≠ causation in genomic pH preference studies.** Gene–pH associations (e.g., MrpF correlating with high pH preference) are valuable for node discovery but should be curated as *uncertain* edges unless paired with perturbation/physiology evidence demonstrating causal effects on growth range (ramoneda2023buildingagenomebased pages 3-5).

2) **Community and treatment specificity.** Putrescine effects were “switch-like” (beneficial under acid, detrimental under alkaline), so edges should carry qualifiers (polyamine addition, biofilm context) and not be generalized to all taxa (jiang2024exogenousputrescineplays pages 1-2).

3) **Growth vs survival phenotypes.** Some acid resistance literature focuses on survival after extreme acid shock rather than growth. Ensure pH delta captures growth-supporting min/max pH boundaries, not survival endpoints (qin2024characterizationofmild pages 1-2).

4) **Assay modifiers.** Buffering, oxygen regime, salinity and carbon source can shift apparent pH limits by changing pH drift, energetics, and ion gradients; include these as experimental-factor nodes or qualifiers in the causal graph (jong2024quantitativeproteomicsreveals pages 6-8, ianutsevich2023theroleof pages 1-2).

---

## DOI-first bibliography (URLs and dates)

- Poolman B. **Physicochemical homeostasis in bacteria.** *FEMS Microbiology Reviews* (Jun 2023). DOI: **10.1093/femsre/fuad033**. https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2)
- Ramoneda J, et al. **Building a genome-based understanding of bacterial pH preferences.** *Science Advances* (Apr 2023). DOI: **10.1126/sciadv.adf8998**. https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5)
- Yao X, Wang J, Hu B. **How methanotrophs respond to pH: A review of ecophysiology.** *Frontiers in Microbiology* (Jan 2023). DOI: **10.3389/fmicb.2022.1034164**. https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond media 1bc0ffc0, yao2023howmethanotrophsrespond media bb130037)
- Ianutsevich EA, et al. **The role of osmolytes and membrane lipids in the adaptation of acidophilic fungi.** *Microorganisms* (Jul 2023). DOI: **10.3390/microorganisms11071733**. https://doi.org/10.3390/microorganisms11071733 (ianutsevich2023theroleof pages 1-2, ianutsevich2023theroleof pages 4-5)
- Fernández-López MG, et al. **Alkaliphilic/Alkali-Tolerant Fungi: Molecular, Biochemical, and Biotechnological Aspects.** *Journal of Fungi* (Jun 2023). DOI: **10.3390/jof9060652**. https://doi.org/10.3390/jof9060652 (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2, fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7, fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 2-4)
- de Jong SI, et al. **Quantitative proteomics reveals oxygen-induced adaptations in Caldalkalibacillus thermarum TA2.A1 microaerobic chemostat cultures.** *Frontiers in Microbiology* (Oct 2024). DOI: **10.3389/fmicb.2024.1468929**. https://doi.org/10.3389/fmicb.2024.1468929 (jong2024quantitativeproteomicsreveals pages 6-8)
- Jiang G, et al. **Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge.** *Applied and Environmental Microbiology* (Jul 2024). DOI: **10.1128/aem.00569-24**. https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12)
- Qin J, et al. **Characterization of Mild Acid Stress Response in an Engineered Acid-Tolerant Escherichia coli Strain.** *Microorganisms* (Jul 2024). DOI: **10.3390/microorganisms12081565**. https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2, qin2024characterizationofmild pages 2-3, qin2024characterizationofmild pages 13-14)
- Li Z, Huang Z, Gu P. **Response of Escherichia coli to Acid Stress: Mechanisms and Applications—A Narrative Review.** *Microorganisms* (Aug 2024). DOI: **10.3390/microorganisms12091774**. https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 10-12, li2024responseofescherichia pages 1-2)
- Palmer M, et al. **Dynamic evolution of nitrogen cycle and pH homeostasis genes enabled the diversification of Pampinifervens gen. nov. (Aquificaceae).** *Research Square (preprint)* (Mar 2024). DOI: **10.21203/rs.3.rs-4032669/v1**. https://doi.org/10.21203/rs.3.rs-4032669/v1 (palmer2024dynamicevolutionof pages 1-5)

---

## Notes toward `data/traits/environment/ph_delta.yaml`
- **Trait definition:** use METPO definition; add curation notes clarifying that pH delta is computed from a growth-supporting pH interval.
- **Core mechanistic hubs:** pH homeostasis (GO:0006885), PMF (GO:0015986), F0F1-ATPase (GO:0015078), monovalent cation/H+ antiport (GO:0015385), membrane lipid remodeling (GO:0006643), amino-acid decarboxylase acid resistance systems (label/KEGG modules), osmolytes (CHEBI:18128 trehalose; polyols), and fungal PacC/Rim101 pathway.
- **Assay modifiers:** buffering, oxygen, salinity, carbon source, and “growth vs survival endpoint” should be explicitly modeled as experimental factors or qualifiers.


References

1. (yao2023howmethanotrophsrespond media 1bc0ffc0): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

2. (yao2023howmethanotrophsrespond media bb130037): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

3. (qin2024characterizationofmild pages 1-2): Jingliang Qin, Han Guo, Xiaoxue Wu, Shuai Ma, Xin Zhang, Xiaofeng Yang, Bin Liu, Lu Feng, Huanhuan Liu, and Di Huang. Characterization of mild acid stress response in an engineered acid-tolerant escherichia coli strain. Microorganisms, 12:1565, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081565, doi:10.3390/microorganisms12081565. This article has 2 citations.

4. (ianutsevich2023theroleof pages 1-2): Elena A. Ianutsevich, Olga A. Danilova, Olga A. Grum-Grzhimaylo, and Vera M. Tereshina. The role of osmolytes and membrane lipids in the adaptation of acidophilic fungi. Microorganisms, 11:1733, Jul 2023. URL: https://doi.org/10.3390/microorganisms11071733, doi:10.3390/microorganisms11071733. This article has 22 citations.

5. (poolman2023physicochemicalhomeostasisin pages 1-2): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

6. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

7. (ianutsevich2023theroleof pages 4-5): Elena A. Ianutsevich, Olga A. Danilova, Olga A. Grum-Grzhimaylo, and Vera M. Tereshina. The role of osmolytes and membrane lipids in the adaptation of acidophilic fungi. Microorganisms, 11:1733, Jul 2023. URL: https://doi.org/10.3390/microorganisms11071733, doi:10.3390/microorganisms11071733. This article has 22 citations.

8. (jiang2024exogenousputrescineplays pages 1-2): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

9. (jong2024quantitativeproteomicsreveals pages 6-8): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

10. (jiang2024exogenousputrescineplays pages 9-12): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

11. (li2024responseofescherichia pages 10-12): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

12. (zhang2023transcriptomeanalysisreveals pages 7-10): Kai Zhang, Wan Wang, and Qian Yang. Transcriptome analysis reveals the regulation of aureobasidium pullulans under different ph stress. International Journal of Molecular Sciences, 24:16103, Nov 2023. URL: https://doi.org/10.3390/ijms242216103, doi:10.3390/ijms242216103. This article has 14 citations.

13. (li2024responseofescherichia pages 5-7): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

14. (zhang2023transcriptomeanalysisreveals pages 13-14): Kai Zhang, Wan Wang, and Qian Yang. Transcriptome analysis reveals the regulation of aureobasidium pullulans under different ph stress. International Journal of Molecular Sciences, 24:16103, Nov 2023. URL: https://doi.org/10.3390/ijms242216103, doi:10.3390/ijms242216103. This article has 14 citations.

15. (kim2024lineagespecificevolutionof pages 2-4): Minkyung Kim, Wonjae Kim, Yerim Park, Jaejoon Jung, and Woojun Park. Lineage-specific evolution of aquibium, a close relative of mesorhizobium, during habitat adaptation. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.02091-23, doi:10.1128/aem.02091-23. This article has 4 citations and is from a peer-reviewed journal.

16. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

17. (qin2024characterizationofmild pages 2-3): Jingliang Qin, Han Guo, Xiaoxue Wu, Shuai Ma, Xin Zhang, Xiaofeng Yang, Bin Liu, Lu Feng, Huanhuan Liu, and Di Huang. Characterization of mild acid stress response in an engineered acid-tolerant escherichia coli strain. Microorganisms, 12:1565, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081565, doi:10.3390/microorganisms12081565. This article has 2 citations.

18. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2): Maikel Gilberto Fernández-López, Ramón Alberto Batista-García, and Elva Teresa Aréchiga-Carvajal. Alkaliphilic/alkali-tolerant fungi: molecular, biochemical, and biotechnological aspects. Journal of Fungi, 9:652, Jun 2023. URL: https://doi.org/10.3390/jof9060652, doi:10.3390/jof9060652. This article has 35 citations.

19. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7): Maikel Gilberto Fernández-López, Ramón Alberto Batista-García, and Elva Teresa Aréchiga-Carvajal. Alkaliphilic/alkali-tolerant fungi: molecular, biochemical, and biotechnological aspects. Journal of Fungi, 9:652, Jun 2023. URL: https://doi.org/10.3390/jof9060652, doi:10.3390/jof9060652. This article has 35 citations.

20. (zheng2024heterologousexpressionof pages 1-2): Yujuan Zheng, Yumiao Zhang, Yifan Zhao, Xiaoqiu Wu, Huan Wang, Hongyu Zhao, Junhua Liu, Bin Liu, Longxiang Liu, and Weiyu Song. Heterologous expression of the oenococcus oeni two-component signal transduction response regulator in the lactiplantibacillus plantarum wcfs1 strain enhances acid stress tolerance. BMC Microbiology, Sep 2024. URL: https://doi.org/10.1186/s12866-024-03498-9, doi:10.1186/s12866-024-03498-9. This article has 4 citations and is from a peer-reviewed journal.

21. (li2024responseofescherichia pages 1-2): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

22. (palmer2024dynamicevolutionof pages 1-5): Marike Palmer, Nancy O. Nou, Lara A. Turello, Carolyn E. Power, John C. Ong, Dengxun Lai, Anna-Louise Reysenbach, Yan-Ling Qi, Jeremy A. Dodsworth, Jian-Yu Jiao, Lan Liu, Zheng-Han Lian, Meng-Meng Li, Yitai Liu, Brandon R. Briggs, Hongyan Zuo, Stephen R. Quake, Emiley A. Eloe-Fadrosh, Tanja Woyke, Hailiang Dong, Wen-Jun Li, Zhengshuang Hua, and Brian P. Hedlund. Dynamic evolution of nitrogen cycle and ph homeostasis genes enabled the diversification of pampinifervens gen. nov. (aquificaceae). Unknown journal, Mar 2024. URL: https://doi.org/10.21203/rs.3.rs-4032669/v1, doi:10.21203/rs.3.rs-4032669/v1.

23. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 2-4): Maikel Gilberto Fernández-López, Ramón Alberto Batista-García, and Elva Teresa Aréchiga-Carvajal. Alkaliphilic/alkali-tolerant fungi: molecular, biochemical, and biotechnological aspects. Journal of Fungi, 9:652, Jun 2023. URL: https://doi.org/10.3390/jof9060652, doi:10.3390/jof9060652. This article has 35 citations.

24. (qin2024characterizationofmild pages 13-14): Jingliang Qin, Han Guo, Xiaoxue Wu, Shuai Ma, Xin Zhang, Xiaofeng Yang, Bin Liu, Lu Feng, Huanhuan Liu, and Di Huang. Characterization of mild acid stress response in an engineered acid-tolerant escherichia coli strain. Microorganisms, 12:1565, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081565, doi:10.3390/microorganisms12081565. This article has 2 citations.