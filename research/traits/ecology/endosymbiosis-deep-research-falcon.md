---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:11:32.025009'
end_time: '2026-06-17T20:28:29.885887'
duration_seconds: 1017.86
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: endosymbiosis
  trait_identifier: traitmech:000045
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: endosymbiosis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A symbiosis in which the microorganism lives inside the cells or tissues
    of its host. Obligate intracellular endosymbionts (e.g. of insects) frequently
    undergo extreme genome reduction.
  parent_traits: traitmech:000040
  synonyms: endosymbiont
  evidence_summary: 'DOI:10.1038/nrmicro2670:  (McCutcheon & Moran, "Extreme genome
    reduction in symbiotic bacteria", characterize intracellular endosymbionts and
    their diminished genomes.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe
    rhizobia as plant-cell endosymbionts within root nodules, an example of the endosymbiotic
    lifestyle.)'
  causal_graph_summary: 'endosymbiosis_intracellular_genome_reduction: 3 nodes, 2
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 104
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** endosymbiosis
- **METPO identifier:** traitmech:000045
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism lives inside the cells or tissues of its host. Obligate intracellular endosymbionts (e.g. of insects) frequently undergo extreme genome reduction.
- **Parent traits:** traitmech:000040
- **Synonyms:** endosymbiont
- **Existing evidence:** DOI:10.1038/nrmicro2670:  (McCutcheon & Moran, "Extreme genome reduction in symbiotic bacteria", characterize intracellular endosymbionts and their diminished genomes.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia as plant-cell endosymbionts within root nodules, an example of the endosymbiotic lifestyle.)
- **Existing causal graph summary:** endosymbiosis_intracellular_genome_reduction: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **endosymbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/endosymbiosis.yaml`.

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
- **Trait label:** endosymbiosis
- **METPO identifier:** traitmech:000045
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism lives inside the cells or tissues of its host. Obligate intracellular endosymbionts (e.g. of insects) frequently undergo extreme genome reduction.
- **Parent traits:** traitmech:000040
- **Synonyms:** endosymbiont
- **Existing evidence:** DOI:10.1038/nrmicro2670:  (McCutcheon & Moran, "Extreme genome reduction in symbiotic bacteria", characterize intracellular endosymbionts and their diminished genomes.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia as plant-cell endosymbionts within root nodules, an example of the endosymbiotic lifestyle.)
- **Existing causal graph summary:** endosymbiosis_intracellular_genome_reduction: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **endosymbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/endosymbiosis.yaml`.

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


# Microbial Trait Causal Graph Curation Report: Endosymbiosis (traitmech:000045)

## 0. Scope summary (curation-ready)

**Trait definition (operational):** *Endosymbiosis* is an ecological trait in which a microorganism resides **inside host cells or tissues** (e.g., host cytoplasm or nucleus) as part of a stable association that may range from facultative to obligate and often includes metabolic integration and/or transmission adaptations. This aligns with recent mechanistic descriptions of intracellular symbionts occupying host cytoplasm and, in some systems, the host nucleus to evade lysosomal threats. (song2024cellularinteractionsand pages 8-9, ferrarini2023coordinationofhost pages 1-3)

**Key boundaries / near-traits:**
- **Not ectosymbiosis:** organisms living on host surfaces are out of scope for this trait definition.
- **Not transient intracellular infection:** intracellular presence that does not persist (e.g., fails tolerance to host digestion) is not sufficient. Directed endosymbiosis frameworks emphasize that intracellular persistence requires **tolerance** (avoidance of digestion) and **syntrophy** (mutual metabolic dependency), otherwise bacteria are degraded. (meaney2025engineeringrhizobiaendosymbionts pages 63-67, meaney2025engineeringrhizobiaendosymbiontsa pages 67-70)
- **Genome transfer ≠ endosymbiosis:** transfer of a bacterial genome into the host nucleus without persistence of an intact intracellular microbe is a related phenomenon but should be curated separately from the endosymbiosis trait itself. (meaney2025engineeringrhizobiaendosymbiontsa pages 67-70)
- **Endosymbiont–organelle continuum:** some systems blur the boundary between endosymbiont and organelle (e.g., host-to-symbiont protein trafficking), but curation here focuses on the trait “microbe living inside host cells/tissues.” (ling2024acompletedna pages 10-11)

## 1. Key concepts and definitions (current understanding)

### 1.1 Intracellular localization and host compartments
Recent synthesis in ciliate systems describes bacterial endosymbionts colonizing the **host cytoplasm** and, in some cases, the **host nucleus** (e.g., intranuclear symbionts) as strategies to persist and avoid lysosomal threats. (song2024cellularinteractionsand pages 8-9)

### 1.2 Evolutionary signatures: genome reduction and bottlenecks
A recurrent conceptual framework is that an intracellular lifestyle imposes **selective pressures in a confined habitat**, enabling **metabolic gene loss and genome shrinkage** relative to free-living relatives. Quantitatively, free-living bacteria are described as ~2–10 Mb, whereas obligate endosymbionts are often **<1.5 Mb**; example endosymbiont genomes include **Polynucleobacter** endosymbionts (1.7–1.8 Mb vs free-living 2.1–2.5 Mb) and **Holospora** (1.27–1.72 Mb; GC 35.2–37.6%). (song2024cellularinteractionsand pages 8-9)

The same synthesis notes population-genetic drivers such as **few-founder bottlenecks** (“colonies originate from few ancestors”) and “limited recombination,” which can facilitate genome erosion. (song2024cellularinteractionsand pages 8-9)

### 1.3 Metabolic integration and host control
Across insect and plant intracellular symbioses, stable endosymbiosis is frequently underpinned by:
- **Metabolic complementation** (host and symbiont collectively complete nutrient pathways). (bai2024endosymbionttremblayaphenacola pages 1-2, silva2024comparativetranscriptomicsof pages 1-2)
- **Host immune modulation/control** within specialized tissues or cells (e.g., bacteriocytes/bacteriomes), including antimicrobial peptides and peptidoglycan recognition proteins that prevent excessive immune activation. (silva2024comparativetranscriptomicsof pages 19-21, ferrarini2023coordinationofhost pages 6-8)

## 2. Recent developments and latest research (priority 2023–2024)

### 2.1 2024: Cross-endosymbiont assembly of DNA repair restores host thermotolerance (PNAS)
A major mechanistic advance is the demonstration that a complete DNA mismatch repair (MMR) system can be **assembled across two co-resident endosymbionts** in aphids, with clear ecological consequences under heat stress. In this system:
- Obligate **Buchnera** lacks components of mismatch repair, while facultative **Serratia** supplies **MutH**, complementing Buchnera-encoded **MutL/MutS** to form “an active MMR.” (ling2024acompletedna pages 9-10, ling2024acompletedna pages 7-9)
- Protein trafficking across symbionts is supported by detection of **Serratia-derived proteins inside purified Buchnera**, including MutH. (ling2024acompletedna pages 10-11, ling2024acompletedna pages 7-9)
- Reduced Buchnera mutation accumulation is quantified: Buchnera from Serratia-infected aphids show **6 strain-specific SNPs and 1 strain-specific indel**, versus **61 strain-specific SNPs and 11 strain-specific indels** in Serratia-free Buchnera. (ling2024acompletedna pages 6-7)
- This helps preserve an **ibpA promoter** vulnerable to single-adenine deletion; ibpA encodes a small heat-shock protein linked to bacteriocyte cytoskeletal stability. (ling2024acompletedna pages 1-2, ling2024acompletedna pages 7-9)
- Fitness and survival effects under heat are substantial. For example, an ibpA-promoter mutant strain shows delayed first reproduction (**15.6 vs 11.7 days**), fewer progeny (**10.6 vs 33.1**), and lower progeny survival (**66.8% vs 98.3%**) compared with intact-promoter controls; additionally, Serratia-associated rescue under heat is described as “66.8% versus 1.2%” in a key comparison (context-dependent within the study’s strain contrasts). (ling2024acompletedna pages 9-10, ling2024acompletedna pages 7-9)

**Visual summary:** Ling et al.’s schematic model and experimental panels summarize the assembled MMR mechanism and heat-stress phenotypes. (ling2024acompletedna media 64aab6f5, ling2024acompletedna media ad32b376, ling2024acompletedna media 4226544a)

### 2.2 2024: Widespread intracellular insect symbiont with conserved host-interaction machinery (ISME J)
Wierz et al. report **Symbiodolus** as an intracellular symbiont present across life stages and tissues, with ovarian enrichment supporting vertical transmission. Genomes across host taxa show conservation in **secretion systems, effectors, and toxin–antitoxin systems**, consistent with intracellular host interaction requirements. (wierz2024intracellularsymbiontsymbiodolus pages 1-2)

### 2.3 2024: Endosymbiont control of host nutrient signaling and reproduction (ISME J)
In mealybugs, Bai et al. link a highly reduced primary endosymbiont to host reproduction and nutrient signaling:
- The Tremblaya genome is reported as **221.1 kb** (highly reduced). (bai2024endosymbionttremblayaphenacola pages 1-2)
- Antibiotic elimination “significantly decreased” host fecundity. (bai2024endosymbionttremblayaphenacola pages 1-2)
- Altering symbiont abundance activated the host **mTOR pathway**, consistent with amino-acid-mediated regulation of reproduction. (bai2024endosymbionttremblayaphenacola pages 1-2)

### 2.4 2023: Multi-pathway host regulation of symbiont growth and elimination (Microbiome)
Ferrarini et al. provide an unusually dynamic and systems-level view of endosymbiosis regulation over insect development, identifying co-regulated pathways that include **immunity, metabolism, metal control, apoptosis, and autophagy**, with hosts “activat[ing] recycling enzymes along with genes involved in apoptosis and autophagy” during phases associated with bacterial elimination. (ferrarini2023coordinationofhost pages 1-3, ferrarini2023coordinationofhost pages 10-13)

## 3. Current applications and real-world implementations

### 3.1 Agriculture: nutrient management to support rhizobial endosymbiosis
Root nodule symbiosis is highly nutrient demanding. A recent 2024 mini-review notes that up to **20–30% of total plant P and Fe is allocated to nodules**, and that Fe or P deficiency “substantially reduces nitrogen fixation rates,” while P deficiency “significantly reduces nodule formation.” (isidraarellano2024understandingthecrucial pages 1-2)

This indicates practical agronomic leverage points: phosphate and iron availability can be managed to stabilize intracellular symbiosis performance, mediated by plant uptake/homeostasis programs and symbiosome transport systems (e.g., Fe delivery via VTL4/VTL8/MtFPN2; Fe uptake in infected cells via NRAMP1). (isidraarellano2024understandingthecrucial pages 5-6, isidraarellano2024understandingthecrucial pages 11-12)

### 3.2 Pest biology and pest control concepts (emerging, mechanism-driven)
In insect symbioses, host immune effectors (AMPs, PGRPs) and bacterial countermeasures (e.g., LPS modification via arn operon) represent candidate intervention nodes. For example, host PGRP amidases “cleave peptidoglycan to prevent IMD pathway activation,” which is a concrete, mechanistically grounded tolerance mechanism. (silva2024comparativetranscriptomicsof pages 19-21)

In addition, host elimination phases linked to apoptosis/autophagy suggest life-stage-specific windows where symbiont load is controllable. (ferrarini2023coordinationofhost pages 1-3)

### 3.3 Environmental resilience: endosymbiont-mediated heat tolerance
The assembled DNA repair phenotype in aphids provides a mechanistic basis for symbiosis-mediated thermal resilience, linking cross-symbiont DNA repair → reduced mutational burden in obligate symbionts → preserved heat-shock gene regulation → host bacteriocyte stability and fitness. (ling2024acompletedna pages 9-10, ling2024acompletedna pages 7-9, ling2024acompletedna media 64aab6f5)

## 4. Expert opinions and authoritative analysis (from sources)

### 4.1 Host control is multi-layered: immune dampening + targeted antimicrobial regulation
Cockroach bacteriocyte systems illustrate a clear “tolerance” strategy: **PGRP amidase cleavage of peptidoglycan** prevents IMD pathway activation, reducing immune conflict in the bacteriocyte environment. (silva2024comparativetranscriptomicsof pages 19-21)

Weevil systems add a complementary “containment + elimination” strategy: bacteriomes seclude symbionts, while adult stages activate recycling/apoptosis/autophagy programs associated with elimination once symbiont benefit declines. (ferrarini2023coordinationofhost pages 1-3)

### 4.2 Metabolic and metal flux are central to intracellular symbiosis stability
Multiple sources converge on the view that intracellular symbioses are enabled by **bidirectional exchange**, requiring transporters and homeostatic programs:
- In cockroach bacteriocytes, inferred exchange includes urea supply and membrane-localized trehalose and zinc transporters. (silva2024comparativetranscriptomicsof pages 19-21)
- In nodules, iron delivery to bacteroids depends on symbiosome-associated transporters (VTL4/VTL8, MtFPN2) and infected-cell uptake systems (NRAMP1), reflecting strong host investment and control. (isidraarellano2024understandingthecrucial pages 5-6, isidraarellano2024understandingthecrucial pages 11-12)

### 4.3 Genome reduction is common but modifiable by community context
While intracellular symbionts commonly lose functions (including DNA repair), the 2024 PNAS study demonstrates that **co-resident facultative symbionts can functionally compensate** missing core pathways (MMR), changing the evolutionary and ecological outcomes (thermostability). (ling2024acompletedna pages 6-7, ling2024acompletedna pages 7-9)

## 5. Causal-graph entities and candidate nodes (grouped)

The following curation-ready node inventory (with grounding suggestions where possible) is provided as a direct starting point for `data/traits/ecology/endosymbiosis.yaml`.

| Type | Candidate node | Suggested grounding | Evidence/rationale | Citation |
|---|---|---|---|---|
| Host processes/pathways | Autophagy | GO:0006914 | Host autophagy genes are induced in nodules and implicated in symbiosis maintenance; host autophagy also correlates with endosymbiont elimination in insects. | (semenova2024autophagyandsymbiosis pages 7-8, semenova2024autophagyandsymbiosis pages 1-2, ferrarini2023coordinationofhost pages 1-3) |
| Host processes/pathways | Apoptotic process | GO:0006915 | Host genes involved in apoptosis are activated during endosymbiont elimination in the cereal weevil system. | (ferrarini2023coordinationofhost pages 1-3) |
| Host processes/pathways | TOR signaling pathway / mTOR pathway | GO:0031929 | Endosymbiont abundance affects host mTOR signaling in mealybugs; TOR is also discussed as a regulator in nodules. | (bai2024endosymbionttremblayaphenacola pages 1-2, semenova2024autophagyandsymbiosis pages 11-13, ferrarini2023coordinationofhost pages 6-8) |
| Host processes/pathways | IMD pathway activation control | label only | Cockroach PGRP amidases cleave peptidoglycan to prevent IMD pathway activation, supporting symbiosis tolerance. | (silva2024comparativetranscriptomicsof pages 19-21) |
| Host processes/pathways | Phosphate starvation response (PSR) | label only | Pi status regulates nodulation through PHR-centered phosphate starvation signaling. | (isidraarellano2024understandingthecrucial pages 3-5, isidraarellano2024understandingthecrucial pages 5-6) |
| Host processes/pathways | Iron starvation response / iron homeostasis | label only | Iron uptake, distribution, and signaling are central to nodule function and symbiosis efficiency. | (isidraarellano2024understandingthecrucial pages 3-5, isidraarellano2024understandingthecrucial pages 5-6, isidraarellano2024understandingthecrucial pages 11-12) |
| Host processes/pathways | Nodule organogenesis / symbiosome development | label only | NIN and related pathways promote intracellular rhizobial infection and symbiosome development. | (isidraarellano2024understandingthecrucial pages 2-3, isidraarellano2024understandingthecrucial pages 1-2) |
| Host processes/pathways | Membrane trafficking (endocytosis/exocytosis/recycling) | label only | Host membrane trafficking and recycling are enriched during symbiosis and likely govern intracellular accommodation/elimination. | (ferrarini2023coordinationofhost pages 10-13) |
| Symbiont processes/pathways | Genome reduction | label only | Intracellular endosymbionts commonly show reduced genomes relative to free-living relatives. | (song2024cellularinteractionsand pages 8-9, silva2024comparativetranscriptomicsof pages 1-2, meaney2025engineeringrhizobiaendosymbiontsa pages 67-70) |
| Symbiont processes/pathways | Metabolic complementation / amino acid metabolic complementarity | GO:0006520 | Endosymbionts complement host amino acid metabolism in multiple systems. | (bai2024endosymbionttremblayaphenacola pages 1-2, silva2024comparativetranscriptomicsof pages 1-2, ferrarini2023coordinationofhost pages 17-18) |
| Symbiont processes/pathways | DNA mismatch repair | GO:0006298 | A complete MMR system is assembled across two endosymbionts in aphids, preserving genome integrity. | (ling2024acompletedna pages 6-7, ling2024acompletedna pages 9-10, ling2024acompletedna pages 7-9) |
| Symbiont processes/pathways | Lipopolysaccharide modification / AMP resistance | label only | arn operon-mediated LPS modification is linked to resistance against host antimicrobial peptides. | (ferrarini2023coordinationofhost pages 6-8) |
| Symbiont processes/pathways | Protein secretion systems | GO:0009306 | Symbiodolus genomes consistently encode multiple secretion systems linked to host interaction. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2) |
| Symbiont processes/pathways | Toxin-antitoxin system | label only | Symbiodolus retains toxin-antitoxin systems likely related to intracellular persistence/host interactions. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2) |
| Symbiont processes/pathways | Host cell entry / invasion | label only | Host-cell entry is supported by secretion systems/effectors in natural systems and invasin-mediated invasion in engineered systems. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2, meaney2025engineeringrhizobiaendosymbiontsa pages 67-70) |
| Symbiont processes/pathways | Vertical transmission-associated ovary tropism | label only | Intracellular abundance in ovaries indicates transovarial transmission in insect symbionts. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2) |
| Genes/proteins (host) | PGRP-LB_1 / PGRP-LB_2 | label only | Host PGRPs with amidase activity cleave peptidoglycan and help prevent immune overactivation. | (silva2024comparativetranscriptomicsof pages 19-21) |
| Genes/proteins (host) | NIN transcription factor | label only | NIN promotes intracellular rhizobial infection, nodule development, and symbiosome-related programs. | (isidraarellano2024understandingthecrucial pages 2-3, isidraarellano2024understandingthecrucial pages 1-2) |
| Genes/proteins (host) | VTL4 | label only | Symbiosome/bacteroid-associated iron delivery transporter in nodules. | (isidraarellano2024understandingthecrucial pages 5-6, isidraarellano2024understandingthecrucial pages 11-12) |
| Genes/proteins (host) | VTL8 | label only | Symbiosome/bacteroid-associated iron delivery transporter in nodules. | (isidraarellano2024understandingthecrucial pages 5-6, isidraarellano2024understandingthecrucial pages 11-12) |
| Genes/proteins (host) | MtFPN2 | label only | Iron transporter localized to vascular/symbiosome membranes, important for Fe distribution. | (isidraarellano2024understandingthecrucial pages 5-6) |
| Genes/proteins (host) | NRAMP1 | label only | Required for iron uptake by rhizobia-infected nodule cells. | (isidraarellano2024understandingthecrucial pages 11-12) |
| Genes/proteins (host) | PHT1 transporter family | label only | Pi uptake transporters in the phosphate starvation response that influences nodulation. | (isidraarellano2024understandingthecrucial pages 3-5, isidraarellano2024understandingthecrucial pages 5-6) |
| Genes/proteins (host) | PHO1 transporter family | label only | Pi translocation transporters involved in Pi homeostasis during symbiosis. | (isidraarellano2024understandingthecrucial pages 3-5, isidraarellano2024understandingthecrucial pages 5-6) |
| Genes/proteins (host) | TOR kinase | label only | Host nutrient-sensing kinase implicated in nodules and symbiont-responsive signaling. | (semenova2024autophagyandsymbiosis pages 1-2, semenova2024autophagyandsymbiosis pages 11-13) |
| Genes/proteins (host) | CLE peptides (e.g., CLE-RS1/2, MtCLE12/13) | label only | Host peptides mediate autoregulation of nodulation under nutrient-responsive control. | (isidraarellano2024understandingthecrucial pages 3-5) |
| Genes/proteins (host) | HAR1 / SUNN receptor kinases | label only | Shoot receptors for CLE peptides in systemic nodulation control. | (isidraarellano2024understandingthecrucial pages 3-5) |
| Genes/proteins (host) | IMA peptides | label only | Iron-status peptides that modulate Fe deficiency responses and nodulation. | (isidraarellano2024understandingthecrucial pages 5-6) |
| Genes/proteins (host) | FRO2 | label only | Ferric reductase participating in Fe uptake for symbiosis-supporting homeostasis. | (isidraarellano2024understandingthecrucial pages 3-5, isidraarellano2024understandingthecrucial pages 5-6) |
| Genes/proteins (host) | IRT1 | label only | Iron transporter in the Fe uptake pathway relevant to nodules. | (isidraarellano2024understandingthecrucial pages 3-5, isidraarellano2024understandingthecrucial pages 5-6) |
| Genes/proteins (host) | FIT | label only | Host transcription factor controlling Fe starvation responses. | (isidraarellano2024understandingthecrucial pages 5-6) |
| Genes/proteins (host) | ATG gene set (e.g., ATG1, ATG2, ATG7–13, ATG16, ATG18) | label only | Autophagy-related genes are upregulated in nodules, especially in the nitrogen-fixation zone. | (semenova2024autophagyandsymbiosis pages 7-8, semenova2024autophagyandsymbiosis pages 1-2) |
| Genes/proteins (host) | Diptericin-like AMP / Coleoptericin A-like AMP | label only | Host AMPs are implicated in intracellular control of endosymbiont proliferation. | (ferrarini2023coordinationofhost pages 6-8, ferrarini2023coordinationofhost pages 17-18) |
| Genes/proteins (host) | Transferrin (tsf-1) | label only | Host metal-handling protein with expression dynamics correlated to bacterial load. | (ferrarini2023coordinationofhost pages 10-13) |
| Genes/proteins (host) | Ferritin heavy chain-like (fth-1) | label only | Host iron storage/handling protein associated with endosymbiont dynamics. | (ferrarini2023coordinationofhost pages 10-13) |
| Genes/proteins (symbiont) | MutH | label only | Serratia-derived MMR component translocates into Buchnera and complements repair. | (ling2024acompletedna pages 6-7, ling2024acompletedna pages 10-11, ling2024acompletedna pages 7-9) |
| Genes/proteins (symbiont) | MutL | label only | Buchnera-encoded MMR component in assembled inter-symbiont repair system. | (ling2024acompletedna pages 6-7, ling2024acompletedna pages 9-10, ling2024acompletedna pages 7-9) |
| Genes/proteins (symbiont) | MutS | label only | Buchnera-encoded MMR component in assembled inter-symbiont repair system. | (ling2024acompletedna pages 6-7, ling2024acompletedna pages 9-10, ling2024acompletedna pages 7-9) |
| Genes/proteins (symbiont) | ibpA | label only | Buchnera small heat-shock protein gene whose promoter integrity underlies heat tolerance. | (ling2024acompletedna pages 1-2, ling2024acompletedna pages 7-9) |
| Genes/proteins (symbiont) | Arn operon | label only | Encodes LPS modification linked to resistance against host antimicrobial peptides. | (ferrarini2023coordinationofhost pages 6-8) |
| Genes/proteins (symbiont) | SseL | label only | Deubiquitinase/virulence factor inferred to inhibit host autophagic clearance. | (ferrarini2023coordinationofhost pages 6-8) |
| Genes/proteins (symbiont) | Secretion system effectors | label only | Conserved in Symbiodolus and likely involved in host-cell interactions. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2) |
| Genes/proteins (symbiont) | Toxin-antitoxin proteins | label only | Conserved in Symbiodolus genomes associated with intracellular lifestyle. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2) |
| Genes/proteins (symbiont) | 89-kDa invasion-tip protein | label only | In ciliate intranuclear symbionts, infection-form proteins participate in host invasion. | (song2024cellularinteractionsand pages 8-9) |
| Genes/proteins (symbiont) | Periplasmic region protein 1 (63-kDa) | label only | In ciliate intranuclear symbionts, binds host nuclear DNA during invasion. | (song2024cellularinteractionsand pages 8-9) |
| Genes/proteins (symbiont) | Listeriolysin O | label only | Engineering/pathogen-derived factor enabling endosomal escape for intracellular persistence. | (meaney2025engineeringrhizobiaendosymbiontsa pages 67-70) |
| Genes/proteins (symbiont) | SNARE-like proteins | label only | Engineering/pathogen-derived proteins that inhibit lysosomal fusion/proteasomal digestion. | (meaney2025engineeringrhizobiaendosymbiontsa pages 67-70) |
| Genes/proteins (symbiont) | Invasin | label only | Used in directed endosymbiosis as a host-cell entry factor. | (meaney2025engineeringrhizobiaendosymbiontsa pages 67-70) |
| Metabolites/nutrients | Peptidoglycan | CHEBI:73616 | Host PGRPs cleave symbiont peptidoglycan to reduce immune activation. | (silva2024comparativetranscriptomicsof pages 19-21) |
| Metabolites/nutrients | Urea | CHEBI:16199 | Imported into bacteriocytes to support Blattabacterium-associated metabolism. | (silva2024comparativetranscriptomicsof pages 19-21) |
| Metabolites/nutrients | Trehalose | CHEBI:18198 | Trehalose transporters at bacteriocyte membranes are candidate host–symbiont exchange routes. | (silva2024comparativetranscriptomicsof pages 19-21) |
| Metabolites/nutrients | Zinc ion | CHEBI:29105 | Zinc transporter localization suggests metal exchange/handling in bacteriocytes. | (silva2024comparativetranscriptomicsof pages 19-21) |
| Metabolites/nutrients | Iron ion | CHEBI:18248 | High nodule Fe demand and dedicated transport to infected cells/bacteroids are central to rhizobial endosymbiosis. | (isidraarellano2024understandingthecrucial pages 1-2, isidraarellano2024understandingthecrucial pages 5-6, isidraarellano2024understandingthecrucial pages 11-12) |
| Metabolites/nutrients | Phosphate | CHEBI:18367 | High nodule Pi demand and phosphate-homeostasis pathways regulate symbiosis. | (isidraarellano2024understandingthecrucial pages 3-5, isidraarellano2024understandingthecrucial pages 1-2, isidraarellano2024understandingthecrucial pages 5-6) |
| Metabolites/nutrients | Amino acids | CHEBI:33709 | Symbiont-mediated amino acid provisioning is a recurrent mechanism across insect symbioses. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2, bai2024endosymbionttremblayaphenacola pages 1-2, silva2024comparativetranscriptomicsof pages 1-2) |
| Metabolites/nutrients | Cofactors | label only | Symbiodolus retains biosynthetic pathways for several cofactors, suggesting potential host benefit. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2) |
| Metabolites/nutrients | Phenylalanine | CHEBI:28044 | Host phenylalanine metabolism increases when Blattabacterium is depleted, indicating symbiont contribution. | (silva2024comparativetranscriptomicsof pages 1-2) |
| Metabolites/nutrients | Tyrosine | CHEBI:17895 | Host tyrosine metabolism compensates for reduced symbiont function in cockroaches. | (silva2024comparativetranscriptomicsof pages 1-2) |
| Metabolites/nutrients | Uric acid | CHEBI:27226 | Uric acid/uricolytic metabolism is integrated between cockroach and endosymbiont. | (silva2024comparativetranscriptomicsof pages 1-2, silva2024comparativetranscriptomicsof pages 25-26) |
| Metabolites/nutrients | ATP | CHEBI:15422 | ATP exchange is part of directed endosymbiosis examples and high ATP demand underlies N-fixing symbiosis. | (meaney2025engineeringrhizobiaendosymbionts pages 63-67, isidraarellano2024understandingthecrucial pages 1-2) |
| Metabolites/nutrients | Dicarboxylic acids | CHEBI label only | Host-to-bacteroid carbon shift toward dicarboxylic acids is noted in nodules. | (semenova2024autophagyandsymbiosis pages 7-8) |
| Cellular locations/structures | Bacteriocyte | label only | Specialized host cell housing intracellular symbionts in insects. | (bai2024endosymbionttremblayaphenacola pages 1-2, ferrarini2023coordinationofhost pages 1-3, silva2024comparativetranscriptomicsof pages 1-2) |
| Cellular locations/structures | Bacteriome | label only | Organ composed of bacteriocytes that compartmentalizes endosymbionts. | (bai2024endosymbionttremblayaphenacola pages 1-2, ferrarini2023coordinationofhost pages 1-3) |
| Cellular locations/structures | Symbiosome | label only | Intracellular rhizobial compartment central to legume endosymbiosis. | (isidraarellano2024understandingthecrucial pages 2-3, isidraarellano2024understandingthecrucial pages 5-6, semenova2024autophagyandsymbiosis pages 11-13) |
| Cellular locations/structures | Root nodule | PO:0003013 | Specialized plant organ for intracellular rhizobial endosymbiosis. | (isidraarellano2024understandingthecrucial pages 1-2, semenova2024autophagyandsymbiosis pages 1-2) |
| Cellular locations/structures | Nodule nitrogen-fixation zone (Zone III) | label only | Zone with strongest ATG induction and active intracellular symbiosis. | (semenova2024autophagyandsymbiosis pages 7-8) |
| Cellular locations/structures | Ovary | UBERON:0000992 | Ovarian enrichment of intracellular symbionts supports transovarial transmission. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2) |
| Cellular locations/structures | Host cytoplasm | GO:0005737 | Canonical intracellular location for many endosymbionts. | (song2024cellularinteractionsand pages 8-9, ferrarini2023coordinationofhost pages 1-3) |
| Cellular locations/structures | Host nucleus | GO:0005634 | Some ciliate endosymbionts are intranuclear. | (song2024cellularinteractionsand pages 8-9) |
| Cellular locations/structures | Endosome | GO:0005768 | Intracellular barrier escaped by engineered/pathogen-derived mechanisms. | (meaney2025engineeringrhizobiaendosymbiontsa pages 67-70) |
| Cellular locations/structures | Lysosome | GO:0005764 | Host degradative compartment avoided or inhibited by intracellular persistence factors. | (meaney2025engineeringrhizobiaendosymbiontsa pages 67-70) |
| Cellular locations/structures | Endoplasmic reticulum | GO:0005783 | ER is implicated as a membrane source and stress-signaling hub in symbiosome/autophagy biology. | (semenova2024autophagyandsymbiosis pages 1-2, semenova2024autophagyandsymbiosis pages 11-13) |
| Cellular locations/structures | Acidosome / digestive vacuole | label only | Host vacuolar structures involved in activating infectious forms in ciliates. | (song2024cellularinteractionsand pages 8-9) |
| Environmental/experimental factors | Heat stress | label only | Heat stress reveals the fitness consequences of symbiont-mediated DNA repair and ibpA maintenance. | (ling2024acompletedna pages 1-2, ling2024acompletedna pages 9-10, ling2024acompletedna pages 7-9) |
| Environmental/experimental factors | Phosphate limitation | label only | Pi deficiency reduces nodulation and N-fixation. | (isidraarellano2024understandingthecrucial pages 1-2, isidraarellano2024understandingthecrucial pages 5-6) |
| Environmental/experimental factors | Iron limitation | label only | Fe deficiency impairs nodule function and nitrogen fixation. | (isidraarellano2024understandingthecrucial pages 1-2, isidraarellano2024understandingthecrucial pages 5-6) |
| Environmental/experimental factors | Carbon deprivation / sugar deficiency | label only | Nodule cells show signs of sugar limitation linked to autophagy propensity. | (semenova2024autophagyandsymbiosis pages 7-8, semenova2024autophagyandsymbiosis pages 1-2) |
| Environmental/experimental factors | Nitrogen deficiency / suboptimal nitrogen availability | label only | Host nodule cells display nitrogen limitation signals associated with autophagy-related responses. | (semenova2024autophagyandsymbiosis pages 7-8, semenova2024autophagyandsymbiosis pages 1-2) |
| Environmental/experimental factors | Antibiotic treatment (rifampicin) | CHEBI label only | Used to generate quasi-aposymbiotic cockroaches and test endosymbiont function. | (silva2024comparativetranscriptomicsof pages 1-2) |
| Environmental/experimental factors | Directed endosymbiosis engineering / microinjection / PEG-mediated transfer | label only | Experimental methods defining tolerance and syntrophy constraints for intracellular establishment. | (meaney2025engineeringrhizobiaendosymbionts pages 63-67, meaney2025engineeringrhizobiaendosymbiontsa pages 67-70) |
| Environmental/experimental factors | Confined intracellular habitat | label only | Evolutionary context associated with gene loss and genome shrinkage. | (song2024cellularinteractionsand pages 8-9) |
| Transmission modes | Vertical transmission | label only | Stable endosymbioses are commonly vertically transmitted. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2, ferrarini2023coordinationofhost pages 1-3, silva2024comparativetranscriptomicsof pages 1-2) |
| Transmission modes | Transovarial transmission | label only | Supported by ovarian localization/high abundance in insect hosts. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2) |
| Transmission modes | Mixed transmission mode | label only | Symbiodolus likely combines vertical transmission with occasional horizontal transfer. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2) |
| Transmission modes | Horizontal transmission | label only | Lack of cospeciation in Symbiodolus indicates occasional horizontal movement across hosts. | (wierz2024intracellularsymbiontsymbiodolus pages 1-2) |
| Transmission modes | Few-founder transmission bottleneck | label only | Colonies often originate from few ancestors, promoting limited recombination and genome erosion. | (song2024cellularinteractionsand pages 8-9) |


*Table: This table lists candidate node entities for a TraitMech causal graph of microbial endosymbiosis, grouped by biological type and grounded to stable ontologies where possible. It is useful for converting recent evidence into curation-ready YAML nodes while keeping uncertain labels explicit.*

## 6. Evidence-backed candidate causal edges (triples)

The following candidate edges are proposed as subject–predicate–object triples, each accompanied by an evidence snippet, DOI/URL, and curation notes/uncertainty flags.

| Edge (subject—predicate—object) | Evidence snippet (verbatim/near-verbatim) | Reference (first author year, journal) | DOI/URL | Notes for curation (including uncertainty flags) and suggested ontology grounding |
|---|---|---|---|---|
| intracellular endosymbiotic lifestyle — associated with — genome reduction | “selective pressures in confined habitats drive metabolic gene loss and genome shrinkage (free-living 2–10 Mb vs obligate endosymbionts often <1.5 Mb)” (song2024cellularinteractionsand pages 8-9) | Song 2024, ISME J | https://doi.org/10.1093/ismejo/wrae117 | Strong general edge for intracellular endosymbionts, but still a trend rather than absolute rule. Grounding: endosymbiosis [METPO traitmech:000045], genome reduction [label], intracellular anatomical location [GO:0005622 broad host context only]. |
| confined intracellular habitat — drives — metabolic gene loss | “selective pressures in confined habitats drive metabolic gene loss” (song2024cellularinteractionsand pages 8-9) | Song 2024, ISME J | https://doi.org/10.1093/ismejo/wrae117 | Broad evolutionary mechanism; useful as high-level ecology→genome edge. Grounding: intracellular environment [ENVO candidate label], gene loss [label]. |
| transmission bottlenecks / few founding cells — associated with — limited recombination | “colonies originate from few ancestors, limited recombination” (song2024cellularinteractionsand pages 8-9) | Song 2024, ISME J | https://doi.org/10.1093/ismejo/wrae117 | Good mechanistic/evolutionary edge for obligate endosymbiosis; wording is association not direct experiment. Mark moderate confidence. Grounding: population bottleneck [label], recombination [GO:0006310]. |
| host-cell acidification (acidosome + digestive vacuole fusion) — activates — infectious forms of intranuclear symbionts | “host-mediated acidification via fusion of the acidosome and digestive vacuole activates IFs” (song2024cellularinteractionsand pages 8-9) | Song 2024, ISME J | https://doi.org/10.1093/ismejo/wrae117 | Taxon-specific to Holospora-like ciliates; curate only if graph allows lineage-specific mechanisms. Grounding: acidification [GO:0007035 related vacuolar acidification], infectious form [label], Holospora [NCBITaxon candidate]. |
| Symbiodolus genomes — encode — multiple secretion systems | “All sequenced Symbiodolus genomes encode for multiple secretion systems” (wierz2024intracellularsymbiontsymbiodolus pages 1-2) | Wierz 2024, ISME J | https://doi.org/10.1093/ismejo/wrae099 | Strong genomic feature; secretion system type not specified in snippet. Grounding: protein secretion system [GO:0009306 broad], Symbiodolus [NCBITaxon candidate]. |
| multiple secretion systems / effectors / toxin-antitoxin systems — likely facilitate — host-cell entry and host interactions | “multiple secretion systems, alongside effectors and toxin-antitoxin systems, which likely facilitate host-cell entry and interactions with the host” (wierz2024intracellularsymbiontsymbiodolus pages 1-2) | Wierz 2024, ISME J | https://doi.org/10.1093/ismejo/wrae099 | Mechanistic but authors say “likely”; mark uncertain/inferred. Grounding: host cell entry [GO:0046718 candidate broad host cell invasion], effector protein [label], toxin-antitoxin system [GO:0043655 candidate]. |
| high abundance in female ovaries — indicates — transovarial vertical transmission | “high abundance in female ovaries, indicating transovarial vertical transmission” (wierz2024intracellularsymbiontsymbiodolus pages 1-2) | Wierz 2024, ISME J | https://doi.org/10.1093/ismejo/wrae099 | Strong phenotype edge for transmission mechanism. Grounding: ovary [UBERON:0000992], vertical transmission [GO:0018995 candidate label], transovarial transmission [label]. |
| biosynthetic pathways for amino acids and cofactors — suggest — host nutritional benefit | “biosynthetic pathways for several amino acids and cofactors encoded by the bacterial genomes suggest that the symbionts may also be able to provide benefits to the hosts” (wierz2024intracellularsymbiontsymbiodolus pages 1-2) | Wierz 2024, ISME J | https://doi.org/10.1093/ismejo/wrae099 | Useful but explicitly tentative (“suggest”). Mark uncertain. Grounding: amino acid biosynthetic process [GO:1901607], cofactor biosynthetic process [GO:0051186]. |
| host–symbiont amino-acid pathway complementarity — supports — nutritional compensation | “a comprehensive analysis demonstrated complementarity in amino acid metabolic pathways between host and symbiont, supporting nutritional compensation” (bai2024endosymbionttremblayaphenacola pages 1-2) | Bai 2024, ISME J | https://doi.org/10.1093/ismejo/wrae052 | Strong edge for metabolic complementation. Grounding: amino acid metabolic process [GO:0006520], nutritional symbiosis [label], Tremblaya phenacola [NCBITaxon candidate]. |
| antibiotic elimination of Tremblaya — decreases — host fecundity | “Elimination of T. phenacola PSOL through antibiotic treatment significantly decreased P. solenopsis fecundity” (bai2024endosymbionttremblayaphenacola pages 1-2) | Bai 2024, ISME J | https://doi.org/10.1093/ismejo/wrae052 | Strong assay-backed host fitness edge, but antibiotic perturbation can have off-target effects. Mark assay-specific. Grounding: fecundity [PATO:0001914 candidate], antibiotic treatment [CHEBI antibiotic class candidate]. |
| altered endosymbiont abundance — activates — host mTOR pathway | “altering endosymbiont abundance activated the host mechanistic target of rapamycin pathway” (bai2024endosymbionttremblayaphenacola pages 1-2) | Bai 2024, ISME J | https://doi.org/10.1093/ismejo/wrae052 | Strong host signaling edge. Grounding: TOR signaling [GO:0031929], mTOR protein [UniProt host-specific not assigned]. |
| severe genome reduction in Blattabacterium — leads to dependence on — intracellular environment | “has undergone severe genome reduction leading to dependence on the intracellular environment” (silva2024comparativetranscriptomicsof pages 1-2) | Silva 2024, IJMS | https://doi.org/10.3390/ijms25084228 | Strong generalizable edge for obligate intracellular symbionts. Grounding: genome reduction [label], intracellular environment [label], Blattabacterium [NCBITaxon candidate]. |
| host PGRP-LB amidase activity — cleaves — peptidoglycan | “PGRPs with amidase activity that cleave peptidoglycan” (silva2024comparativetranscriptomicsof pages 19-21) | Silva 2024, IJMS | https://doi.org/10.3390/ijms25084228 | Strong mechanistic edge. Grounding: peptidoglycan catabolic process [GO:0009253], peptidoglycan recognition protein [UniProt family/GO molecular function label], peptidoglycan [CHEBI:73616]. |
| PGRP-mediated peptidoglycan cleavage — prevents — IMD pathway activation | “cleave peptidoglycan to prevent IMD pathway activation” (silva2024comparativetranscriptomicsof pages 19-21) | Silva 2024, IJMS | https://doi.org/10.3390/ijms25084228 | Strong host-control edge in cockroach system. Grounding: IMD signaling pathway [label], peptidoglycan [CHEBI:73616]. |
| symbiont presence — induces — PGRP-LB_1 expression | “PGRP-LB_1 expression is induced by symbiont presence” (silva2024comparativetranscriptomicsof pages 19-21) | Silva 2024, IJMS | https://doi.org/10.3390/ijms25084228 | Good host-response edge; taxon-specific. Grounding: regulation of gene expression [GO:0010468], PGRP-LB [protein label]. |
| urea import into bacteriocytes — supplies — Blattabacterium | “urea import into bacteriocytes to supply Blattabacterium” (silva2024comparativetranscriptomicsof pages 19-21) | Silva 2024, IJMS | https://doi.org/10.3390/ijms25084228 | Good metabolite exchange edge; transporter identity not specified in snippet. Grounding: urea [CHEBI:16199], bacteriocyte [cell type label], transport [GO:0006810]. |
| trehalose transporters at bacteriocyte membrane — enable — host–symbiont metabolite exchange | “two trehalose transporters … localized to the bacteriocyte plasma membrane” and “metabolite transporters potentially involved in host–endosymbiont metabolite exchange” (silva2024comparativetranscriptomicsof pages 19-21, silva2024comparativetranscriptomicsof pages 1-2) | Silva 2024, IJMS | https://doi.org/10.3390/ijms25084228 | Evidence for candidate transport role, but exchanged direction/substrate flux not fully established. Mark moderate confidence. Grounding: trehalose transmembrane transporter activity [GO candidate label], trehalose [CHEBI:18198]. |
| zinc transporter at bacteriocyte membrane — associated with — endosymbiosis maintenance | “a zinc transporter localized to the bacteriocyte plasma membrane” (silva2024comparativetranscriptomicsof pages 19-21) | Silva 2024, IJMS | https://doi.org/10.3390/ijms25084228 | Localization supported; functional role in symbiosis is inferential. Mark uncertain. Grounding: zinc ion transmembrane transporter activity [GO:0005385], zinc cation [CHEBI:29105]. |
| intracellular AMP (Diptericin-like) — inhibits — endosymbiont cell division | “analogous to Coleoptericin A which inhibits endosymbiont cell division” (ferrarini2023coordinationofhost pages 6-8) | Ferrarini 2023, Microbiome | https://doi.org/10.1186/s40168-023-01714-8 | Strong concept for host AMP control, but direct inhibitory function is analogy/citation-based in this snippet. Mark moderate confidence. Grounding: antimicrobial peptide activity [GO:0003795 candidate], cell division [GO:0051301]. |
| arn operon-mediated LPS modification — linked to — AMP resistance | “The endosymbiont induces an arn operon for LPS modification linked to AMP resistance” (ferrarini2023coordinationofhost pages 6-8) | Ferrarini 2023, Microbiome | https://doi.org/10.1186/s40168-023-01714-8 | Strong bacterial counter-defense edge. Grounding: lipid A modification [label], lipopolysaccharide [CHEBI:16412], resistance to antimicrobial peptide [label]. |
| host activates apoptosis and autophagy genes — correlates with — endosymbiont elimination | “hosts ‘activate recycling enzymes along with genes involved in apoptosis and autophagy,’ correlating with bacterial elimination” (ferrarini2023coordinationofhost pages 1-3) | Ferrarini 2023, Microbiome | https://doi.org/10.1186/s40168-023-01714-8 | Strong developmental control edge, but correlation not direct causation. Grounding: apoptotic process [GO:0006915], autophagy [GO:0006914], symbiont clearance [label]. |
| bacterial sseL expression — may inhibit — host autophagic clearance | “sseL, a deubiquitinase known to inhibit autophagic clearance, suggesting bacterial modulation of host autophagy” (ferrarini2023coordinationofhost pages 6-8) | Ferrarini 2023, Microbiome | https://doi.org/10.1186/s40168-023-01714-8 | Important but partly inferred from homology/known function. Mark uncertain/taxon-specific. Grounding: deubiquitinase activity [GO:0004843], negative regulation of autophagy [GO:0010507], SseL [protein label]. |
| nodule Pi and Fe allocation — supports — nitrogen-fixing symbiosis | “Up to 20–30% of total plant P and Fe is allocated to nodules” (isidraarellano2024understandingthecrucial pages 1-2) | Isidra-Arellano 2024, Plant Cell Physiol | https://doi.org/10.1093/pcp/pcae128 | Strong environmental/nutrient context edge. Grounding: phosphate [CHEBI:18367], iron cation [CHEBI:18248], root nodule [PO:0005640 candidate]. |
| P deficiency — reduces — nodule formation | “P deficiency significantly reduces nodule formation” (isidraarellano2024understandingthecrucial pages 1-2) | Isidra-Arellano 2024, Plant Cell Physiol | https://doi.org/10.1093/pcp/pcae128 | Strong environmental factor edge for plant endosymbiosis. Grounding: phosphate limitation [ENVO/label], nodule formation [GO candidate label]. |
| Fe deficiency — reduces — nitrogen fixation rates | “Fe or P deficiency substantially reduces nitrogen fixation rates” (isidraarellano2024understandingthecrucial pages 1-2) | Isidra-Arellano 2024, Plant Cell Physiol | https://doi.org/10.1093/pcp/pcae128 | Strong nutrient requirement edge. Grounding: iron limitation [label], nitrogen fixation [GO:0009399]. |
| NIN transcription factor — promotes — intracellular rhizobial infection | “NIN … promotes intracellular rhizobial infection, nodule organogenesis, nodule maturation to the nitrogen-fixing state” (isidraarellano2024understandingthecrucial pages 2-3) | Isidra-Arellano 2024, Plant Cell Physiol | https://doi.org/10.1093/pcp/pcae128 | Strong host developmental-control edge in rhizobial endosymbiosis. Grounding: NIN [gene label], intracellular signal transduction to infection [label], nodulation [GO candidate]. |
| VTL4/VTL8 and MtFPN2 — deliver Fe to — bacteroids/symbiosomes | “Specific transporters deliver Fe to bacteroids/symbiosomes, including VTL4/VTL8 and MtFPN2” (isidraarellano2024understandingthecrucial pages 5-6) | Isidra-Arellano 2024, Plant Cell Physiol | https://doi.org/10.1093/pcp/pcae128 | Strong transporter edge. Grounding: iron ion transport [GO:0006826], symbiosome [label], bacteroid [label], VTL8/MtFPN2 [gene labels]. |
| NRAMP1 — required for — iron uptake by rhizobia-infected nodule cells | “a Medicago NRAMP1 … required for iron uptake by rhizobia-infected nodule cells” (isidraarellano2024understandingthecrucial pages 11-12) | Isidra-Arellano 2024, Plant Cell Physiol | https://doi.org/10.1093/pcp/pcae128 | Strong host transporter requirement edge. Grounding: NRAMP1 [gene label], iron ion transport [GO:0006826]. |
| ATG genes in nodules — indicate induction of — autophagosome formation | “most ATGs upregulated in the nitrogen-fixation zone (zone III)” and “indicating induction and development of autophagosome formation” (semenova2024autophagyandsymbiosis pages 7-8) | Semenova 2024, IJMS | https://doi.org/10.3390/ijms25052918 | Strong host-cell process edge in plant endosymbiosis. Grounding: autophagosome assembly [GO:0000045], ATG genes [gene set label]. |
| carbon/nitrogen deficiency and ER stress — predispose nodule cells to — autophagy | “suboptimal sugar and nitrogen availability … and several ER stress genes are upregulated… making them prone to autophagy” (semenova2024autophagyandsymbiosis pages 1-2) | Semenova 2024, IJMS | https://doi.org/10.3390/ijms25052918 | Useful environmental/stress edge; largely review/synthesis. Grounding: response to endoplasmic reticulum stress [GO:0034976], starvation [GO:0042594], autophagy [GO:0006914]. |
| symbiosome membrane formation — may be similar to — phagophore formation | “membrane formation around intracellular rhizobia (symbiosomes) may be similar to phagophore formation” (semenova2024autophagyandsymbiosis pages 1-2) | Semenova 2024, IJMS | https://doi.org/10.3390/ijms25052918 | Explicit speculation; do not curate as firm causal edge yet. Grounding: symbiosome [label], phagophore assembly site [GO candidate label]. |
| Serratia MutH + Buchnera MutL/MutS — assemble — active mismatch repair system | “Serratia mutH complements Buchnera mutL and mutS to form an active MMR” (ling2024acompletedna pages 9-10) | Ling 2024, PNAS | https://doi.org/10.1073/pnas.2415651121 | Strong mechanistic edge with biochemical support. Grounding: MutH/MutL/MutS [protein labels], mismatch repair [GO:0006298]. |
| assembled MMR — reduces — mutation accumulation in Buchnera | “Incomplete MMR in the Buchnera genome could be complemented by the Serratia genome to reduce mutation accumulation” (ling2024acompletedna pages 6-7) | Ling 2024, PNAS | https://doi.org/10.1073/pnas.2415651121 | Strong causal edge supported by SNP/Indel comparisons. Grounding: mismatch repair [GO:0006298], mutation frequency [PATO/label]. |
| Serratia mutH translocation into Buchnera — enables — inter-symbiont DNA repair complementation | “Serratia mutH could access to Buchnera cells... allowing an active MMR assembly to form” (ling2024acompletedna pages 6-7) | Ling 2024, PNAS | https://doi.org/10.1073/pnas.2415651121 | Strong but unusual cross-cell protein transfer; valuable for graph. Grounding: protein localization to symbiont [label], MutH [protein label]. |
| active MMR — preserves — ibpA promoter integrity | “prevented a single adenine deletion in the promoter of ibpA” (ling2024acompletedna pages 7-9) | Ling 2024, PNAS | https://doi.org/10.1073/pnas.2415651121 | Strong specific edge. Grounding: ibpA [gene label], promoter [SO:0000167], DNA mismatch repair [GO:0006298]. |
| IbpA chaperone expression — stabilizes — bacteriocyte actin / heat tolerance | “IbpA chaperone … stabilizes cytoskeletal actin and confers heat tolerance to the aphid host” (ling2024acompletedna media 64aab6f5) | Ling 2024, PNAS | https://doi.org/10.1073/pnas.2415651121 | Strong figure-supported summary edge. Grounding: small heat shock protein [GO candidate], actin filament organization [GO:0007015], heat tolerance [PATO/label]. |
| syntrophy — required for — directed endosymbiosis establishment | “two boundary conditions for initiating symbiosis: syntrophy … and tolerance” (meaney2025engineeringrhizobiaendosymbionts pages 63-67) | Meaney 2025, thesis/review text | n/a | Useful conceptual edge for engineering and boundary definition; source is not a primary peer-reviewed journal in snippet. Mark lower confidence. Grounding: syntrophy [label], endosymbiosis [traitmech:000045]. |
| tolerance to host digestion — required for — stable intracellular persistence | “the symbiont is non-toxic and not digested by the host” (meaney2025engineeringrhizobiaendosymbionts pages 63-67) | Meaney 2025, thesis/review text | n/a | Conceptual engineering edge; lower confidence/noncanonical source. Grounding: lysosomal degradation [GO:0007040 candidate broad], tolerance [label]. |
| Listeriolysin O — allows — escape from endosomes | “Listeriolysin O) to escape endosomes” (meaney2025engineeringrhizobiaendosymbiontsa pages 67-70) | Meaney 2025, thesis/review text | n/a | Mechanistically plausible from pathogen engineering context, not natural endosymbiosis per se. Mark uncertain/not for core trait unless engineering subgraph desired. Grounding: listeriolysin O [protein label], endosome [GO:0005768]. |
| SNARE-like proteins — inhibit — lysosomal fusion and proteasomal digestion | “SNARE-like proteins can allow bacterial persistence by … inhibiting lysosomal fusion and proteasomal digestion” (meaney2025engineeringrhizobiaendosymbiontsa pages 67-70) | Meaney 2025, thesis/review text | n/a | Engineering/pathogen-derived mechanism, not broadly established across microbial endosymbiosis. Mark uncertain. Grounding: SNARE binding/vesicle fusion [GO candidate], lysosome [GO:0005764], proteasome [GO:0000502]. |
| Mollicutes intracellular lifestyle — associated with — small genomes and low GC | “small genomes (0.6–2.2 Mb), low G+C (25–40%), reduced metabolic capacity requiring host-supplied nutrients” (meaney2025engineeringrhizobiaendosymbiontsa pages 67-70) | Meaney 2025, thesis/review text | n/a | Descriptive feature edge; mainly comparative/engineering candidate organism context. Grounding: Mollicutes [NCBITaxon:31969], genome size [label], GC content [label]. |


*Table: This table lists candidate subject–predicate–object edges for a TraitMech causal graph of microbial endosymbiosis, with supporting snippets, citations, and curation notes. It emphasizes intracellular adaptation, genome reduction, metabolic complementation, host control, and nutrient/transport mechanisms across insect, plant, and protist systems.*

## 7. Warnings / claims not yet ready for TraitMech curation

1. **Speculative mechanism linking symbiosome membrane formation to phagophore formation.** Semenova et al. explicitly frame this as speculation (“may be similar”), so it should be curated only as a hypothesis node/edge or marked uncertain. (semenova2024autophagyandsymbiosis pages 1-2)

2. **Engineering/pathogen-derived persistence mechanisms (Listeriolysin O, SNARE-like proteins).** These are informative for directed endosymbiosis and host digestion barriers but may not represent conserved mechanisms across natural endosymbioses; curate separately or mark as engineering-specific/uncertain. (meaney2025engineeringrhizobiaendosymbiontsa pages 67-70)

3. **Inferred functions from genomic features** (e.g., Symbiodolus “likely facilitate host-cell entry”). These are plausible but not experimentally established in the snippet evidence; mark as inferred. (wierz2024intracellularsymbiontsymbiodolus pages 1-2)

4. **Antibiotic elimination phenotypes** can have off-target effects; edges from antibiotic treatment to host fitness should be tagged as assay-specific and potentially confounded. (bai2024endosymbionttremblayaphenacola pages 1-2, silva2024comparativetranscriptomicsof pages 1-2)

## 8. DOI-first bibliography (with dates and URLs)

1. **Ling X, et al.** *A complete DNA repair system assembled by two endosymbionts restores heat tolerance of the insect host.* **PNAS**. **Dec 2024**. DOI: **10.1073/pnas.2415651121**. URL: https://doi.org/10.1073/pnas.2415651121 (ling2024acompletedna pages 1-2)

2. **Song Q, et al.** *Cellular interactions and evolutionary origins of endosymbiotic relationships with ciliates.* **The ISME Journal**. **Jan 2024**. DOI: **10.1093/ismejo/wrae117**. URL: https://doi.org/10.1093/ismejo/wrae117 (song2024cellularinteractionsand pages 8-9)

3. **Wierz JC, et al.** *Intracellular symbiont Symbiodolus is vertically transmitted and widespread across insect orders.* **The ISME Journal**. **Jan 2024**. DOI: **10.1093/ismejo/wrae099**. URL: https://doi.org/10.1093/ismejo/wrae099 (wierz2024intracellularsymbiontsymbiodolus pages 1-2)

4. **Bai J, et al.** *Endosymbiont Tremblaya phenacola influences the reproduction of cotton mealybugs by regulating the mechanistic target of rapamycin pathway.* **The ISME Journal**. **Jan 2024**. DOI: **10.1093/ismejo/wrae052**. URL: https://doi.org/10.1093/ismejo/wrae052 (bai2024endosymbionttremblayaphenacola pages 1-2)

5. **Silva FJ, et al.** *Comparative Transcriptomics of Fat Bodies between Symbiotic and Quasi-Aposymbiotic Adult Females of Blattella germanica…* **International Journal of Molecular Sciences**. **Apr 2024**. DOI: **10.3390/ijms25084228**. URL: https://doi.org/10.3390/ijms25084228 (silva2024comparativetranscriptomicsof pages 1-2)

6. **Isidra-Arellano MC, Valdés-López O.** *Understanding the Crucial Role of Phosphate and Iron Availability in Regulating Root Nodule Symbiosis.* **Plant and Cell Physiology**. **Oct 2024**. DOI: **10.1093/pcp/pcae128**. URL: https://doi.org/10.1093/pcp/pcae128 (isidraarellano2024understandingthecrucial pages 1-2)

7. **Semenova MG, et al.** *Autophagy and Symbiosis: Membranes, ER, and Speculations.* **International Journal of Molecular Sciences**. **Mar 2024**. DOI: **10.3390/ijms25052918**. URL: https://doi.org/10.3390/ijms25052918 (semenova2024autophagyandsymbiosis pages 1-2)

8. **Ferrarini MG, et al.** *Coordination of host and endosymbiont gene expression governs endosymbiont growth and elimination in the cereal weevil Sitophilus spp.* **Microbiome**. **Dec 2023**. DOI: **10.1186/s40168-023-01714-8**. URL: https://doi.org/10.1186/s40168-023-01714-8 (ferrarini2023coordinationofhost pages 1-3)

9. **Meaney JS.** *Engineering Rhizobia Endosymbionts Towards the Development of Synthetic Nitrogen-Fixing Organelles.* **2025** (venue unclear in retrieved text). URL/DOI not established in evidence; use cautiously for engineering constraints (syntrophy/tolerance; intracellular persistence barriers). (meaney2025engineeringrhizobiaendosymbionts pages 63-67)


References

1. (song2024cellularinteractionsand pages 8-9): Qi Song, Fangqing Zhao, Lina Hou, and Miao Miao. Cellular interactions and evolutionary origins of endosymbiotic relationships with ciliates. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae117, doi:10.1093/ismejo/wrae117. This article has 13 citations.

2. (ferrarini2023coordinationofhost pages 1-3): Mariana Galvão Ferrarini, Agnès Vallier, Carole Vincent-Monégat, Elisa Dell’Aglio, Benjamin Gillet, Sandrine Hughes, Ophélie Hurtado, Guy Condemine, Anna Zaidman-Rémy, Rita Rebollo, Nicolas Parisot, and Abdelaziz Heddi. Coordination of host and endosymbiont gene expression governs endosymbiont growth and elimination in the cereal weevil sitophilus spp. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01714-8, doi:10.1186/s40168-023-01714-8. This article has 17 citations and is from a highest quality peer-reviewed journal.

3. (meaney2025engineeringrhizobiaendosymbionts pages 63-67): JS Meaney. Engineering rhizobia endosymbionts towards the development of synthetic nitrogen-fixing organelles. Unknown journal, 2025.

4. (meaney2025engineeringrhizobiaendosymbiontsa pages 67-70): JS Meaney. Engineering rhizobia endosymbionts towards the development of synthetic nitrogen-fixing organelles. Unknown journal, 2025.

5. (ling2024acompletedna pages 10-11): Xiaoyu Ling, Huijuan Guo, Jian Di, Liqiang Xie, Keyan Zhu-Salzman, Feng Ge, Zihua Zhao, and Yucheng Sun. A complete dna repair system assembled by two endosymbionts restores heat tolerance of the insect host. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2415651121, doi:10.1073/pnas.2415651121. This article has 12 citations and is from a highest quality peer-reviewed journal.

6. (bai2024endosymbionttremblayaphenacola pages 1-2): Jianyang Bai, Zhangqi Zuo, Haonan DuanMu, Meizhen Li, Haojie Tong, Yang Mei, Yiqi Xiao, Kang He, Mingxing Jiang, Shuping Wang, and Fei Li. Endosymbiont tremblaya phenacola influences the reproduction of cotton mealybugs by regulating the mechanistic target of rapamycin pathway. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae052, doi:10.1093/ismejo/wrae052. This article has 9 citations.

7. (silva2024comparativetranscriptomicsof pages 1-2): Francisco J. Silva, Rebeca Domínguez-Santos, Amparo Latorre, and Carlos García-Ferris. Comparative transcriptomics of fat bodies between symbiotic and quasi-aposymbiotic adult females of blattella germanica with emphasis on the metabolic integration with its endosymbiont blattabacterium and its immune system. International Journal of Molecular Sciences, 25:4228, Apr 2024. URL: https://doi.org/10.3390/ijms25084228, doi:10.3390/ijms25084228. This article has 7 citations.

8. (silva2024comparativetranscriptomicsof pages 19-21): Francisco J. Silva, Rebeca Domínguez-Santos, Amparo Latorre, and Carlos García-Ferris. Comparative transcriptomics of fat bodies between symbiotic and quasi-aposymbiotic adult females of blattella germanica with emphasis on the metabolic integration with its endosymbiont blattabacterium and its immune system. International Journal of Molecular Sciences, 25:4228, Apr 2024. URL: https://doi.org/10.3390/ijms25084228, doi:10.3390/ijms25084228. This article has 7 citations.

9. (ferrarini2023coordinationofhost pages 6-8): Mariana Galvão Ferrarini, Agnès Vallier, Carole Vincent-Monégat, Elisa Dell’Aglio, Benjamin Gillet, Sandrine Hughes, Ophélie Hurtado, Guy Condemine, Anna Zaidman-Rémy, Rita Rebollo, Nicolas Parisot, and Abdelaziz Heddi. Coordination of host and endosymbiont gene expression governs endosymbiont growth and elimination in the cereal weevil sitophilus spp. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01714-8, doi:10.1186/s40168-023-01714-8. This article has 17 citations and is from a highest quality peer-reviewed journal.

10. (ling2024acompletedna pages 9-10): Xiaoyu Ling, Huijuan Guo, Jian Di, Liqiang Xie, Keyan Zhu-Salzman, Feng Ge, Zihua Zhao, and Yucheng Sun. A complete dna repair system assembled by two endosymbionts restores heat tolerance of the insect host. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2415651121, doi:10.1073/pnas.2415651121. This article has 12 citations and is from a highest quality peer-reviewed journal.

11. (ling2024acompletedna pages 7-9): Xiaoyu Ling, Huijuan Guo, Jian Di, Liqiang Xie, Keyan Zhu-Salzman, Feng Ge, Zihua Zhao, and Yucheng Sun. A complete dna repair system assembled by two endosymbionts restores heat tolerance of the insect host. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2415651121, doi:10.1073/pnas.2415651121. This article has 12 citations and is from a highest quality peer-reviewed journal.

12. (ling2024acompletedna pages 6-7): Xiaoyu Ling, Huijuan Guo, Jian Di, Liqiang Xie, Keyan Zhu-Salzman, Feng Ge, Zihua Zhao, and Yucheng Sun. A complete dna repair system assembled by two endosymbionts restores heat tolerance of the insect host. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2415651121, doi:10.1073/pnas.2415651121. This article has 12 citations and is from a highest quality peer-reviewed journal.

13. (ling2024acompletedna pages 1-2): Xiaoyu Ling, Huijuan Guo, Jian Di, Liqiang Xie, Keyan Zhu-Salzman, Feng Ge, Zihua Zhao, and Yucheng Sun. A complete dna repair system assembled by two endosymbionts restores heat tolerance of the insect host. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2415651121, doi:10.1073/pnas.2415651121. This article has 12 citations and is from a highest quality peer-reviewed journal.

14. (ling2024acompletedna media 64aab6f5): Xiaoyu Ling, Huijuan Guo, Jian Di, Liqiang Xie, Keyan Zhu-Salzman, Feng Ge, Zihua Zhao, and Yucheng Sun. A complete dna repair system assembled by two endosymbionts restores heat tolerance of the insect host. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2415651121, doi:10.1073/pnas.2415651121. This article has 12 citations and is from a highest quality peer-reviewed journal.

15. (ling2024acompletedna media ad32b376): Xiaoyu Ling, Huijuan Guo, Jian Di, Liqiang Xie, Keyan Zhu-Salzman, Feng Ge, Zihua Zhao, and Yucheng Sun. A complete dna repair system assembled by two endosymbionts restores heat tolerance of the insect host. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2415651121, doi:10.1073/pnas.2415651121. This article has 12 citations and is from a highest quality peer-reviewed journal.

16. (ling2024acompletedna media 4226544a): Xiaoyu Ling, Huijuan Guo, Jian Di, Liqiang Xie, Keyan Zhu-Salzman, Feng Ge, Zihua Zhao, and Yucheng Sun. A complete dna repair system assembled by two endosymbionts restores heat tolerance of the insect host. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2415651121, doi:10.1073/pnas.2415651121. This article has 12 citations and is from a highest quality peer-reviewed journal.

17. (wierz2024intracellularsymbiontsymbiodolus pages 1-2): Jürgen C Wierz, Philipp Dirksen, Roy Kirsch, Ronja Krüsemer, Benjamin Weiss, Yannick Pauchet, Tobias Engl, and Martin Kaltenpoth. Intracellular symbiont symbiodolus is vertically transmitted and widespread across insect orders. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae099, doi:10.1093/ismejo/wrae099. This article has 19 citations.

18. (ferrarini2023coordinationofhost pages 10-13): Mariana Galvão Ferrarini, Agnès Vallier, Carole Vincent-Monégat, Elisa Dell’Aglio, Benjamin Gillet, Sandrine Hughes, Ophélie Hurtado, Guy Condemine, Anna Zaidman-Rémy, Rita Rebollo, Nicolas Parisot, and Abdelaziz Heddi. Coordination of host and endosymbiont gene expression governs endosymbiont growth and elimination in the cereal weevil sitophilus spp. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01714-8, doi:10.1186/s40168-023-01714-8. This article has 17 citations and is from a highest quality peer-reviewed journal.

19. (isidraarellano2024understandingthecrucial pages 1-2): Mariel C. Isidra-Arellano and Oswaldo Valdés-López. Understanding the crucial role of phosphate and iron availability in regulating root nodule symbiosis. Plant and Cell Physiology, 65:1925-1936, Oct 2024. URL: https://doi.org/10.1093/pcp/pcae128, doi:10.1093/pcp/pcae128. This article has 7 citations and is from a domain leading peer-reviewed journal.

20. (isidraarellano2024understandingthecrucial pages 5-6): Mariel C. Isidra-Arellano and Oswaldo Valdés-López. Understanding the crucial role of phosphate and iron availability in regulating root nodule symbiosis. Plant and Cell Physiology, 65:1925-1936, Oct 2024. URL: https://doi.org/10.1093/pcp/pcae128, doi:10.1093/pcp/pcae128. This article has 7 citations and is from a domain leading peer-reviewed journal.

21. (isidraarellano2024understandingthecrucial pages 11-12): Mariel C. Isidra-Arellano and Oswaldo Valdés-López. Understanding the crucial role of phosphate and iron availability in regulating root nodule symbiosis. Plant and Cell Physiology, 65:1925-1936, Oct 2024. URL: https://doi.org/10.1093/pcp/pcae128, doi:10.1093/pcp/pcae128. This article has 7 citations and is from a domain leading peer-reviewed journal.

22. (semenova2024autophagyandsymbiosis pages 7-8): Maria G. Semenova, Alekandra N. Petina, and Elena E. Fedorova. Autophagy and symbiosis: membranes, er, and speculations. International Journal of Molecular Sciences, 25:2918, Mar 2024. URL: https://doi.org/10.3390/ijms25052918, doi:10.3390/ijms25052918. This article has 3 citations.

23. (semenova2024autophagyandsymbiosis pages 1-2): Maria G. Semenova, Alekandra N. Petina, and Elena E. Fedorova. Autophagy and symbiosis: membranes, er, and speculations. International Journal of Molecular Sciences, 25:2918, Mar 2024. URL: https://doi.org/10.3390/ijms25052918, doi:10.3390/ijms25052918. This article has 3 citations.

24. (semenova2024autophagyandsymbiosis pages 11-13): Maria G. Semenova, Alekandra N. Petina, and Elena E. Fedorova. Autophagy and symbiosis: membranes, er, and speculations. International Journal of Molecular Sciences, 25:2918, Mar 2024. URL: https://doi.org/10.3390/ijms25052918, doi:10.3390/ijms25052918. This article has 3 citations.

25. (isidraarellano2024understandingthecrucial pages 3-5): Mariel C. Isidra-Arellano and Oswaldo Valdés-López. Understanding the crucial role of phosphate and iron availability in regulating root nodule symbiosis. Plant and Cell Physiology, 65:1925-1936, Oct 2024. URL: https://doi.org/10.1093/pcp/pcae128, doi:10.1093/pcp/pcae128. This article has 7 citations and is from a domain leading peer-reviewed journal.

26. (isidraarellano2024understandingthecrucial pages 2-3): Mariel C. Isidra-Arellano and Oswaldo Valdés-López. Understanding the crucial role of phosphate and iron availability in regulating root nodule symbiosis. Plant and Cell Physiology, 65:1925-1936, Oct 2024. URL: https://doi.org/10.1093/pcp/pcae128, doi:10.1093/pcp/pcae128. This article has 7 citations and is from a domain leading peer-reviewed journal.

27. (ferrarini2023coordinationofhost pages 17-18): Mariana Galvão Ferrarini, Agnès Vallier, Carole Vincent-Monégat, Elisa Dell’Aglio, Benjamin Gillet, Sandrine Hughes, Ophélie Hurtado, Guy Condemine, Anna Zaidman-Rémy, Rita Rebollo, Nicolas Parisot, and Abdelaziz Heddi. Coordination of host and endosymbiont gene expression governs endosymbiont growth and elimination in the cereal weevil sitophilus spp. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01714-8, doi:10.1186/s40168-023-01714-8. This article has 17 citations and is from a highest quality peer-reviewed journal.

28. (silva2024comparativetranscriptomicsof pages 25-26): Francisco J. Silva, Rebeca Domínguez-Santos, Amparo Latorre, and Carlos García-Ferris. Comparative transcriptomics of fat bodies between symbiotic and quasi-aposymbiotic adult females of blattella germanica with emphasis on the metabolic integration with its endosymbiont blattabacterium and its immune system. International Journal of Molecular Sciences, 25:4228, Apr 2024. URL: https://doi.org/10.3390/ijms25084228, doi:10.3390/ijms25084228. This article has 7 citations.