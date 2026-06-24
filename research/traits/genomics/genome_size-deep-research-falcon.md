---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:19:40.550666'
end_time: '2026-06-18T03:34:40.781535'
duration_seconds: 900.23
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: genome size
  trait_identifier: traitmech:000098
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: genome_size
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A quantitative genomics property describing the total length of an organism's
    genome (typically expressed in megabase pairs), which varies widely across prokaryotes
    and reflects lifestyle and evolutionary forces.
  parent_traits: METPO:1000188
  synonyms: genome length
  evidence_summary: 'DOI:10.1038/nrmicro3331:  (Batut et al. review reductive genome
    evolution, linking genome size to population size and lifestyle across prokaryotes.)
    | DOI:10.1038/ismej.2014.60:  (Giovannoni et al. discuss streamlining theory and
    the small genomes of abundant free-living microbes.)'
  causal_graph_summary: 'genome_size_population_lifestyle: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** genome size
- **METPO identifier:** traitmech:000098
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quantitative genomics property describing the total length of an organism's genome (typically expressed in megabase pairs), which varies widely across prokaryotes and reflects lifestyle and evolutionary forces.
- **Parent traits:** METPO:1000188
- **Synonyms:** genome length
- **Existing evidence:** DOI:10.1038/nrmicro3331:  (Batut et al. review reductive genome evolution, linking genome size to population size and lifestyle across prokaryotes.) | DOI:10.1038/ismej.2014.60:  (Giovannoni et al. discuss streamlining theory and the small genomes of abundant free-living microbes.)
- **Existing causal graph summary:** genome_size_population_lifestyle: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **genome size** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/genome_size.yaml`.

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
- **Trait label:** genome size
- **METPO identifier:** traitmech:000098
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quantitative genomics property describing the total length of an organism's genome (typically expressed in megabase pairs), which varies widely across prokaryotes and reflects lifestyle and evolutionary forces.
- **Parent traits:** METPO:1000188
- **Synonyms:** genome length
- **Existing evidence:** DOI:10.1038/nrmicro3331:  (Batut et al. review reductive genome evolution, linking genome size to population size and lifestyle across prokaryotes.) | DOI:10.1038/ismej.2014.60:  (Giovannoni et al. discuss streamlining theory and the small genomes of abundant free-living microbes.)
- **Existing causal graph summary:** genome_size_population_lifestyle: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **genome size** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/genome_size.yaml`.

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


## Research report: Microbial trait “genome size” (TraitMech; METPO traitmech:000098)

### 0) Scope summary (curation-oriented)
**Genome size** (syn. genome length) is a quantitative genomic property: the total length of an organism’s genome (commonly reported in Mbp), and in cultivation-independent studies often operationalized as **average genome size (AGS)** of a community estimated from metagenomes. In TraitMech curation, it is important to distinguish (i) **organismal genome size** (assembled isolate genomes or MAGs) from (ii) **community-aggregated AGS** (marker-gene based estimates from raw reads), and from nearby traits such as **GC content** and **average gene length**, which covary but are distinct properties. Metagenomic AGS can be biased by non-prokaryotic DNA (eukaryotic/viral), motivating explicit “assay bias” nodes/edges or curation metadata. (ngugi2023abioticselectionof pages 1-2, ngugi2023abioticselectionof pages 9-10, eisenhofer2024quantifyingmicrobialdna pages 1-5)

### 1) Key concepts and definitions (current understanding)
#### 1.1 Trait meaning and ecological interpretation
Genome size is frequently interpreted as an axis of **metabolic/functional capacity and ecological strategy**, with small, streamlined genomes linked to reduced metabolic breadth (often oligotrophy/auxotrophy) and larger genomes linked to broader metabolic repertoires and environmental responsiveness. This framing is explicitly used in recent community trait syntheses and marine/soil metagenomics. (ngugi2023abioticselectionof pages 1-2, piton2023lifehistorystrategies pages 1-5)

#### 1.2 Measurement and boundary cases (assay-aware)
**Metagenome-derived AGS**: A common approach uses **MicrobeCensus**, aligning reads to **universally conserved single-copy marker genes** and using their abundance to infer AGS; estimates can be refined by removing eukaryotic and viral reads/contigs to obtain more robust prokaryote-only AGS. (ngugi2023abioticselectionof pages 1-2, ngugi2023abioticselectionof pages 9-10)

**Boundary cases**:
- “Genome size” should not be conflated with **gene length**, **GC%**, or **gene density**. For example, marine studies show average gene length and GC% increase with depth and covary with AGS, while unique gene content per coding length can decline. (ngugi2023abioticselectionof pages 7-8)
- Community-level AGS can be inflated by **eukaryotic DNA** in soil metagenomes; correcting this can materially change estimated mean AGS and strengthen ecological associations. (eisenhofer2024quantifyingmicrobialdna pages 1-5)

### 2) Recent developments and latest research (prioritize 2023–2024)
#### 2.1 Global ocean: abiotic selection of genome size (2023)
A large global meta-analysis of **364 marine metagenomes** found that AGS is strongly structured by **depth and temperature** (environment rather than geography), with **AGS increasing with depth**, and **temperature effects in the photic zone** reported as much stronger than depth effects (rate of change in AGS with temperature reported as **16-fold higher** than with depth up to 200 m). (ngugi2023abioticselectionof pages 1-2, ngugi2023abioticselectionof pages 4-4, ngugi2023abioticselectionof media 6fcc2a7b)

The same work operationalizes **lifestyle** via size-fractionation: **particle-associated communities** have larger AGS than **free-living** communities, with example ranges in Challenger Deep samples (free-living 3.46–4.19 Mbp; particle-associated 3.88–4.92 Mbp). (ngugi2023abioticselectionof pages 4-4, ngugi2023abioticselectionof media 6fcc2a7b)

#### 2.2 Soils: edaphic controls and pH-linked genome-size shifts (2023–2024)
Across **398 soil metagenomes**, soil **pH** and **extractable C:N** are highlighted as strong correlates of community-average genome size and GC%. Low-pH soils tend to host communities with **larger genomes** (and lower GC%), while high-pH/low C:N soils are associated with **smaller genomes** (and higher GC%). (chuckran2023edaphiccontrolson pages 1-6, wang2023bacterialgenomesize pages 2-3)

A 2024 methods-focused reanalysis demonstrates that soils can contain a high fraction of **eukaryotic DNA** (median ~**38.8%** in one reappraised dataset), which **inflated AGS** estimates; after correcting for eukaryotic DNA, the corrected mean AGS was **4.7 Mbp** (reported **31% lower** than the original **6.8 Mbp** estimate) and the negative AGS–pH relationship strengthened (R² reported changing **0.32→0.57** in one dataset; **0.42→0.54** in another). (eisenhofer2024quantifyingmicrobialdna pages 1-5)

A forest pH-gradient study further supports pH-driven community genome-size shifts, noting that genome size decreases as pH rises from acidic toward neutral and providing genus-level examples (e.g., enrichment of a small-genome taxon and loss of large-genome taxa along the gradient). (wang2023bacterialgenomesize pages 2-3)

#### 2.3 Salt stress: domain-specific genome-size strategies (2024)
A 2024 coastal-soil salinity gradient study reports **contrasting eco-evolutionary strategies**: bacteria in high-salinity, carbon-limited soils show **reduced genome sizes** with depletion of metabolic genes (consistent with **genome streamlining**), whereas salt-tolerant archaea show **larger genomes** enriched in salt-resistance, metabolic, and carbon-acquisition genes. (dong2024ecoevolutionarystrategiesfor pages 1-2, dong2024ecoevolutionarystrategiesfor pages 2-3)

Quantitatively, the study reports that most archaeal genomes are small (<2 Mb), yet salt-tolerant archaea (pos-arch) had average genome size **~3.74 Mb**, above a reported phylum baseline, and showed substantially higher carbon-acquisition gene proportions (24.37% vs 12.65% in salt-sensitive archaea). (dong2024ecoevolutionarystrategiesfor pages 2-3, dong2024ecoevolutionarystrategiesfor pages 4-5)

#### 2.4 HGT and genome expansion vs restriction by defence systems (2024)
A global survey of prokaryotic genomes reports extensive HGT across gene trees (detectable transfers in ~66% of trees) and that species have on average **42.5%** (IQR 35.9–50.5%) of genes affected by HGT; the authors note prior evidence that HGT contributes to **genome expansion** and larger genomes with higher fractions of transferred genes. (dmitrijeva2024aglobalsurvey pages 1-2)

Complementarily, a 2024 comparative study links bacterial **defence systems** (including CRISPR-Cas) to altered **gene gain rates** and **pangenome size**. Of 73 defence systems analyzed across 12 species, **6** were associated with **reduced gene gain** (and **3** of those 6 were CRISPR-Cas variants), and genomes hosting these systems tend to have **smaller pangenomes** and fewer phage-related genes—consistent with defence-mediated restriction of prophage integration and gene acquisition. (kogay2024defencesystemsand pages 1-2, kogay2024defencesystemsand pages 4-5)

### 3) Current applications and real-world implementations
1. **Microbial ecology and global-change prediction**: Genome size/AGS is increasingly used as a **community trait** in trait-based ecology to interpret shifts across environmental gradients (ocean depth/temperature; soil pH/C:N; salinity stress) and to parameterize eco-physiological strategies. (ngugi2023abioticselectionof pages 1-2, piton2023lifehistorystrategies pages 1-5, dong2024ecoevolutionarystrategiesfor pages 1-2)
2. **Metagenomic trait estimation pipelines**: Improved methods to estimate AGS by quantifying microbial DNA fractions reduce bias from eukaryotic DNA and improve inference of ecological relationships (e.g., AGS–pH). This is directly applicable to soil and host-associated metagenomes. (eisenhofer2024quantifyingmicrobialdna pages 1-5)
3. **Community assembly and interaction modeling**: Genome size is integrated into genome-resolved modeling of microbial interactions and metabolic cross-feeding; streamlined genomes and auxotrophies are proposed as mechanisms shaping marine community assembly. (giordano2024genomescalecommunitymodelling pages 1-2)

### 4) Expert opinions and analysis (authoritative-source synthesis)
- **Abiotic selection as a primary driver in the ocean**: The global-ocean metagenome analysis explicitly concludes that environmental conditions (temperature/depth and covarying resource regimes) are primary correlates of AGS variation, and uses size-fractionation evidence consistent with ecological strategy differences between particle-associated and free-living microbiomes. (ngugi2023abioticselectionof pages 4-4, ngugi2023abioticselectionof media 6fcc2a7b)
- **Soil pH as a dominant predictor**: Soil studies converge on pH as the strongest correlate of community genomic traits, with mechanistic interpretations spanning physiological stress, carbon availability, and resource limitation shaping the genomic investment in stress tolerance and metabolic breadth. (chuckran2023edaphiccontrolson pages 1-6, wang2023bacterialgenomesize pages 6-7)
- **Domain-specific stress strategies under salinity**: The salinity-gradient study emphasizes that “streamlining” is not universal; bacteria and archaea can show opposite genome-size directions under the same stressor, implying that TraitMech edges should be scoped (e.g., bacterial vs archaeal nodes or taxonomic qualifiers). (dong2024ecoevolutionarystrategiesfor pages 1-2, dong2024ecoevolutionarystrategiesfor pages 2-3)
- **HGT as a genome-expansion force tempered by defence systems**: 2024 comparative genomics supports both (i) extensive HGT across prokaryotes and (ii) defence-system-specific constraints on gene gain and pangenome size, motivating separate nodes for “gene gain rate”, “pangenome size”, “prophage integration”, and “CRISPR-Cas”. (dmitrijeva2024aglobalsurvey pages 1-2, kogay2024defencesystemsand pages 1-2)

### 5) Relevant recent statistics and data highlights
- **Ocean**: particle-associated AGS exceeds free-living AGS in deep samples (example ranges 3.88–4.92 vs 3.46–4.19 Mbp). (ngugi2023abioticselectionof pages 4-4)
- **Ocean**: photic-layer AGS change with temperature reported as **16-fold** higher than with depth (to 200 m). (ngugi2023abioticselectionof pages 1-2, ngugi2023abioticselectionof media 6fcc2a7b)
- **Soil metagenomes**: median eukaryotic DNA fraction **~38.8%** in one soil dataset; corrected mean AGS **4.7 Mbp** (31% lower than 6.8 Mbp) after correcting for eukaryotic DNA; strengthened AGS–pH association (R² 0.32→0.57). (eisenhofer2024quantifyingmicrobialdna pages 1-5)
- **HGT**: transfers detected in **634,352 / 961,821** gene trees (~66%); average **42.5%** of genes affected by HGT per species (IQR 35.9–50.5%). (dmitrijeva2024aglobalsurvey pages 1-2)
- **Defence systems**: among 73 defence systems, **6** associated with reduced gene gain (including **3** CRISPR-Cas systems). (kogay2024defencesystemsand pages 1-2, kogay2024defencesystemsand pages 4-5)

### Visual evidence (recommended for curator review)
The Ngugi et al. (2023) figure crops retrieved here show the reported AGS patterns with depth/temperature and the free-living vs particle-associated contrasts, including the “16-fold” temperature sensitivity statement for photic waters. (ngugi2023abioticselectionof media 6fcc2a7b, ngugi2023abioticselectionof media 584ca537, ngugi2023abioticselectionof media 67f8aad9)

---

## TraitMech curation assets

### A) Candidate nodes grouped by type (with grounding suggestions)
#### Trait node
- **Genome size** (traitmech:000098; METPO reviewed)

#### Environmental / experimental nodes (ENVO where plausible)
- Ocean depth (ENVO:00002042) (used as depth layer/continuous predictor) (ngugi2023abioticselectionof pages 4-4)
- Seawater temperature (ENVO:09200014) (ngugi2023abioticselectionof pages 1-2)
- Soil pH (ENVO:09200009) (chuckran2023edaphiccontrolson pages 1-6, wang2023bacterialgenomesize pages 2-3)
- Salinity / salt stress (ENVO:01000304) (dong2024ecoevolutionarystrategiesfor pages 1-2)
- Extractable soil C:N ratio (label-only; can be modeled as “C:N ratio” without stable CURIE in provided evidence) (chuckran2023edaphiccontrolson pages 1-6)
- Lifestyle: particle-associated vs free-living (label-only; often encoded via size-fractionation) (ngugi2023abioticselectionof pages 4-4)

#### Evolutionary/genomic process nodes (GO where plausible)
- Horizontal gene transfer (GO:0018995) (dmitrijeva2024aglobalsurvey pages 1-2)
- Gene loss (GO:0010629) / genome reduction (label-only if needed) (dong2024ecoevolutionarystrategiesfor pages 5-5)
- Prophage integration (GO:0044826) (mechanistic target of CRISPR-linked effects) (kogay2024defencesystemsand pages 1-2)
- Gene gain rate (label-only; comparative-genomics-derived) (kogay2024defencesystemsand pages 4-5)

#### MGEs and defence systems (label + GO where available)
- Mobile genetic elements (plasmids/phages/ICEs; label-only) (kogay2024defencesystemsand pages 1-2)
- CRISPR-Cas defence system (GO:0098542) (kogay2024defencesystemsand pages 1-2)

#### Functional modules / gene categories (label-only, pathway-level)
- Salt-resistance genes (e.g., Na+ extrusion, K+ uptake, osmolyte synthesis/uptake; label-only) (dong2024ecoevolutionarystrategiesfor pages 5-7, dong2024ecoevolutionarystrategiesfor pages 2-3)
- Carbon acquisition genes / carbon fixation mechanisms (label-only) (dong2024ecoevolutionarystrategiesfor pages 4-5, dong2024ecoevolutionarystrategiesfor pages 2-3)
- Metabolic versatility (label-only; community trait axis) (piton2023lifehistorystrategies pages 1-5)

#### Assay / bias nodes
- Eukaryotic DNA contamination in metagenomes (label-only) (eisenhofer2024quantifyingmicrobialdna pages 1-5)
- Viral DNA contamination in metagenomes (label-only) (ngugi2023abioticselectionof pages 9-10)

### B) Candidate causal edges (evidence-backed)
| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet | Source (first author year, journal) | DOI/URL | Confidence | Notes for curation |
|---|---|---|---|---|---|---|---|
| ocean depth (ENVO:00002042) | positively associated with increased | genome size / AGS (traitmech:000098) | "AGS increases with depth" across epipelagic, mesopelagic, and bathypelagic marine metagenomes; larger deep-ocean genomes reported (ngugi2023abioticselectionof pages 4-4, ngugi2023abioticselectionof media 6fcc2a7b) | Ngugi 2023, Nature Communications | https://doi.org/10.1038/s41467-023-36988-x | high | Community-average AGS from metagenomes; environmental association, not single-gene mechanism |
| seawater temperature (ENVO:09200014) | negatively associated with | genome size / AGS (traitmech:000098) | AGS is highest in perennially cold polar ocean; in photic waters, the rate of AGS change with temperature was "16-fold higher" than with depth (ngugi2023abioticselectionof pages 1-2, ngugi2023abioticselectionof media 6fcc2a7b) | Ngugi 2023, Nature Communications | https://doi.org/10.1038/s41467-023-36988-x | high | Community-level ocean data; robust abiotic predictor |
| particle-associated lifestyle (label) | associated with larger | genome size / AGS (traitmech:000098) | Particle-associated bathypelagic communities had larger genomes than free-living ones; Challenger Deep examples 3.88–4.92 Mbp vs 3.46–4.19 Mbp (ngugi2023abioticselectionof pages 4-4, ngugi2023abioticselectionof media 6fcc2a7b) | Ngugi 2023, Nature Communications | https://doi.org/10.1038/s41467-023-36988-x | high | Lifestyle/ecological state rather than ontology-grounded process |
| nutrient limitation (label) | selects for reduced | genome size / AGS (traitmech:000098) | Authors note nutrient limitation as a major driver of small genomes in oligotrophic photic ocean; streamlining under strong purifying selection (ngugi2023abioticselectionof pages 1-2, ngugi2023abioticselectionof pages 7-8) | Ngugi 2023, Nature Communications | https://doi.org/10.1038/s41467-023-36988-x | medium | Mechanism synthesized from cited literature and ocean patterns |
| soil pH (ENVO:09200009) | negatively associated with | genome size / AGS (traitmech:000098) | Low-pH soils hosted communities with larger average genomes; reanalysis after microbial-DNA correction strengthened the negative AGS–pH relationship (R² from 0.32 to 0.57) (chuckran2023edaphiccontrolson pages 1-6, eisenhofer2024quantifyingmicrobialdna pages 1-5) | Chuckran 2023, bioRxiv; Eisenhofer 2024, ISME Communications | https://doi.org/10.1101/2021.11.17.469016 ; https://doi.org/10.1101/2024.06.20.599828 | high | Community-level soil AGS; strong replicated edaphic pattern |
| extractable soil C:N ratio (label) | positively associated with | genome size / AGS (traitmech:000098) | Extractable C:N was positively correlated with average genome size (p < 0.001); carbon-limited soils favored smaller genomes (chuckran2023edaphiccontrolson pages 1-6) | Chuckran 2023, bioRxiv | https://doi.org/10.1101/2021.11.17.469016 | high | Community-level soil metagenomes; edaphic mechanism |
| carbon limitation (GO:0000016) | selects for smaller | genome size / AGS (traitmech:000098) | "Smaller genomes with higher GC content may reduce the cost of reproduction in carbon-limited soils"; low-C soils selected for smaller genomes (chuckran2023edaphiccontrolson pages 1-6, chuckran2023edaphiccontrolson pages 6-10) | Chuckran 2023, bioRxiv | https://doi.org/10.1101/2021.11.17.469016 | medium | Mechanistic interpretation from stoichiometric model; curate as inferred unless corroborated experimentally |
| salinity / salt stress (ENVO:01000304) | associated with decreased | bacterial genome size (traitmech:000098) | In high-salinity soils, bacteria showed reduced genomes and depletion of metabolic genes, interpreted as genome streamlining (dong2024ecoevolutionarystrategiesfor pages 1-2, dong2024ecoevolutionarystrategiesfor pages 2-3) | Dong 2024, Nature Communications | https://doi.org/10.1038/s41467-024-50368-z | high | Bacteria-specific; taxon-aggregated across coastal soil gradient |
| salinity / salt stress (ENVO:01000304) | associated with increased | archaeal genome size (traitmech:000098) | Salt-tolerant archaea had larger genomes and enrichment of salt-resistance, metabolic, and carbon-acquisition genes; average 3.74 Mb for pos-arch noted (dong2024ecoevolutionarystrategiesfor pages 1-2, dong2024ecoevolutionarystrategiesfor pages 2-3) | Dong 2024, Nature Communications | https://doi.org/10.1038/s41467-024-50368-z | high | Archaea-specific and likely clade-contingent; do not overgeneralize to all archaea |
| salinity / salt stress (ENVO:01000304) | increases abundance of | salt-resistance genes (label) | Both salt-tolerant bacteria and archaea showed elevated salt-resistance KOs; pos-arch had more comprehensive resistance mechanisms (76% vs 20%) (dong2024ecoevolutionarystrategiesfor pages 2-3, dong2024ecoevolutionarystrategiesfor pages 3-4) | Dong 2024, Nature Communications | https://doi.org/10.1038/s41467-024-50368-z | high | Functional node candidate; could split into Na+/H+ antiport, K+ uptake, osmolyte synthesis subnodes |
| gene loss (GO:0010629) | decreases | genome size / AGS (traitmech:000098) | Changes in KO abundance aligned with genome size, indicating protein-encoding gene loss and genome reduction under salinity; >60% of lost pathways were metabolic (dong2024ecoevolutionarystrategiesfor pages 5-5, dong2024ecoevolutionarystrategiesfor pages 5-7) | Dong 2024, Nature Communications | https://doi.org/10.1038/s41467-024-50368-z | high | Strong process-level edge; currently most explicit for bacteria under salt stress |
| horizontal gene transfer (GO:0018995) | increases / expands | genome size or accessory genome (label) | HGT is described as the "driving force behind genome expansion" and species averaged 42.5% of genes affected by HGT (dmitrijeva2024aglobalsurvey pages 1-2) | Dmitrijeva 2024, Nature Ecology & Evolution | https://doi.org/10.1038/s41559-024-02357-0 | high | Broad comparative evidence; object may be better modeled as accessory genome size/pangenome size if distinguished from total genome size |
| mobile genetic elements (plasmids/phages/ICEs; label) | mediate | horizontal gene transfer (GO:0018995) | MGEs are "crucial for horizontal gene transfer" and include plasmids, ICEs, transposons, insertion sequences, and phages (kogay2024defencesystemsand pages 1-2) | Kogay 2024, Environmental Microbiology | https://doi.org/10.1111/1462-2920.16630 | high | Foundational mechanistic edge upstream of genome expansion |
| CRISPR-Cas defense systems (GO:0098542) | decreases | gene gain rate (label) | Of 73 defence systems, 6 were associated with reduced gene gain; 3 were CRISPR-Cas variants, and genomes carrying them had smaller pangenomes/fewer phage-related genes (kogay2024defencesystemsand pages 4-5, kogay2024defencesystemsand pages 1-2) | Kogay 2024, Environmental Microbiology | https://doi.org/10.1111/1462-2920.16630 | high | Good candidate inhibitory edge; species-specific effects noted |
| reduced gene gain rate (label) | decreases | pangenome size (label) | Genomes hosting defence systems associated with reduced gene gain "tend to have smaller pangenome sizes" (kogay2024defencesystemsand pages 1-2, kogay2024defencesystemsand pages 4-5) | Kogay 2024, Environmental Microbiology | https://doi.org/10.1111/1462-2920.16630 | medium | More direct for pangenome than chromosome size; indirect relevance to total genome size |
| prophage integration (GO:0044826) | increases | gene gain / accessory genome content (label) | Defence systems appear to inhibit HGT "primarily by limiting prophage integration"; fewer phage-related genes in genomes with certain CRISPR-Cas systems (kogay2024defencesystemsand pages 1-2, kogay2024defencesystemsand pages 6-7) | Kogay 2024, Environmental Microbiology | https://doi.org/10.1111/1462-2920.16630 | medium | Inferred from comparative genomics; useful upstream mechanistic node |
| metabolic versatility (label) | positively associated with | larger genome size (traitmech:000098) | In soil bacterial communities, a major trait axis reflecting metabolic versatility was strongly positively correlated with genome size (R² = 0.64) (piton2023lifehistorystrategies pages 1-5) | Piton 2023, Nature Microbiology | https://doi.org/10.1038/s41564-023-01465-0 | high | Association between trait axis and genome size; direction likely bidirectional conceptually, but larger genomes enabling versatility is common interpretation |
| eukaryotic DNA contamination in metagenomes (label) | inflates estimate of | community average genome size / AGS (traitmech:000098) | Soil samples contained substantial eukaryotic DNA (median 38.8%); corrected mean AGS was 4.7 Mbp, 31% lower than the original 6.8 Mbp estimate (eisenhofer2024quantifyingmicrobialdna pages 1-5, ngugi2023abioticselectionof pages 9-10) | Eisenhofer 2024, ISME Communications; Ngugi 2023, Nature Communications | https://doi.org/10.1101/2024.06.20.599828 ; https://doi.org/10.1038/s41467-023-36988-x | high | Measurement-bias edge; should inform assay/curation metadata rather than biology-only graph |


*Table: This table summarizes candidate causal and mechanistic edges for a microbial genome size TraitMech graph, spanning abiotic drivers, evolutionary processes, defense systems, functional consequences, and assay biases. It is designed to support curation decisions by pairing each edge with a source-backed snippet, DOI, confidence level, and notes on scope or uncertainty.*

### C) Claims that are currently weak/need caution before curation
1. **“Nutrient limitation → smaller genomes”** is widely invoked, but in the provided evidence it is often a synthesis/interpretation rather than a direct experimental perturbation with measured genome-size evolution; curate as **medium-confidence** unless backed by direct experimental evolution or clear causal identification. (ngugi2023abioticselectionof pages 1-2)
2. **Stoichiometric mechanism for GC/genome size under carbon limitation** (AT vs GC C:N differences) is mechanistically plausible and supported as interpretation, but remains partly **inferred** at community scale; curate with an “inferred mechanism” flag unless direct selection experiments are added. (chuckran2023edaphiccontrolson pages 1-6)
3. **Archaeal genome enlargement under salinity** may be clade- and context-dependent (e.g., enrichment of halophilic Euryarchaeota); curate with **taxonomic qualifiers** (Bacteria vs Archaea; potentially Euryarchaeota-specific). (dong2024ecoevolutionarystrategiesfor pages 2-3)
4. **Defence systems → genome size** is most directly supported for **gene gain rate and pangenome size**, not necessarily assembled chromosome length; curate edges primarily through intermediate nodes (gene gain rate, prophage integration, pangenome size). (kogay2024defencesystemsand pages 1-2, kogay2024defencesystemsand pages 4-5)

---

## DOI-first bibliography (2023–2024 prioritized; with dates/URLs)
1. Ngugi DK, et al. **Abiotic selection of microbial genome size in the global ocean**. *Nature Communications*. 2023-03. DOI: **10.1038/s41467-023-36988-x**. https://doi.org/10.1038/s41467-023-36988-x (ngugi2023abioticselectionof pages 1-2, ngugi2023abioticselectionof pages 4-4)
2. Piton G, et al. **Life history strategies of soil bacterial communities across global terrestrial biomes**. *Nature Microbiology*. 2023-10. DOI: **10.1038/s41564-023-01465-0**. https://doi.org/10.1038/s41564-023-01465-0 (piton2023lifehistorystrategies pages 1-5)
3. Wang C, et al. **Bacterial genome size and gene functional diversity negatively correlate with taxonomic diversity along a pH gradient**. *Nature Communications*. 2023-11. DOI: **10.1038/s41467-023-43297-w**. https://doi.org/10.1038/s41467-023-43297-w (wang2023bacterialgenomesize pages 2-3, wang2023bacterialgenomesize pages 6-7)
4. Rodríguez-Gijón A, et al. **Linking prokaryotic genome size variation to metabolic potential and environment**. *ISME Communications*. 2023-03. DOI: **10.1038/s43705-023-00231-x**. https://doi.org/10.1038/s43705-023-00231-x (rodriguezgijon2023linkingprokaryoticgenome pages 1-2)
5. Dong Y, et al. **Eco-evolutionary strategies for relieving carbon limitation under salt stress differ across microbial clades**. *Nature Communications*. 2024-07. DOI: **10.1038/s41467-024-50368-z**. https://doi.org/10.1038/s41467-024-50368-z (dong2024ecoevolutionarystrategiesfor pages 1-2, dong2024ecoevolutionarystrategiesfor pages 2-3)
6. Dmitrijeva M, et al. **A global survey of prokaryotic genomes reveals the eco-evolutionary pressures driving horizontal gene transfer**. *Nature Ecology & Evolution*. 2024-03. DOI: **10.1038/s41559-024-02357-0**. https://doi.org/10.1038/s41559-024-02357-0 (dmitrijeva2024aglobalsurvey pages 1-2)
7. Kogay R, Wolf YI, Koonin EV. **Defence systems and horizontal gene transfer in bacteria**. *Environmental Microbiology*. 2024-04. DOI: **10.1111/1462-2920.16630**. https://doi.org/10.1111/1462-2920.16630 (kogay2024defencesystemsand pages 1-2, kogay2024defencesystemsand pages 4-5)
8. Eisenhofer R, Alberdi A, Woodcroft BJ. **Quantifying microbial DNA in metagenomes improves microbial trait estimation**. *ISME Communications* (preprint / early version). 2024-06 (posted). DOI: **10.1101/2024.06.20.599828**. https://doi.org/10.1101/2024.06.20.599828 (eisenhofer2024quantifyingmicrobialdna pages 1-5)
9. Chuckran PF, et al. **Edaphic controls on genome size and GC content of bacteria in soil microbial communities**. *bioRxiv* preprint. 2023-11. DOI: **10.1101/2021.11.17.469016**. https://doi.org/10.1101/2021.11.17.469016 (chuckran2023edaphiccontrolson pages 1-6)



References

1. (ngugi2023abioticselectionof pages 1-2): David K. Ngugi, Silvia G. Acinas, Pablo Sánchez, Josep M. Gasol, Susana Agusti, David M. Karl, and Carlos M. Duarte. Abiotic selection of microbial genome size in the global ocean. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-36988-x, doi:10.1038/s41467-023-36988-x. This article has 53 citations and is from a highest quality peer-reviewed journal.

2. (ngugi2023abioticselectionof pages 9-10): David K. Ngugi, Silvia G. Acinas, Pablo Sánchez, Josep M. Gasol, Susana Agusti, David M. Karl, and Carlos M. Duarte. Abiotic selection of microbial genome size in the global ocean. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-36988-x, doi:10.1038/s41467-023-36988-x. This article has 53 citations and is from a highest quality peer-reviewed journal.

3. (eisenhofer2024quantifyingmicrobialdna pages 1-5): Raphael Eisenhofer, Antton Alberdi, and Ben J Woodcroft. Quantifying microbial dna in metagenomes improves microbial trait estimation. ISME Communications, Jan 2024. URL: https://doi.org/10.1101/2024.06.20.599828, doi:10.1101/2024.06.20.599828. This article has 8 citations and is from a peer-reviewed journal.

4. (piton2023lifehistorystrategies pages 1-5): Gabin Piton, Steven D. Allison, Mohammad Bahram, Falk Hildebrand, Jennifer B. H. Martiny, Kathleen K. Treseder, and Adam C. Martiny. Life history strategies of soil bacterial communities across global terrestrial biomes. Nature Microbiology, 8:2093-2102, Oct 2023. URL: https://doi.org/10.1038/s41564-023-01465-0, doi:10.1038/s41564-023-01465-0. This article has 164 citations and is from a highest quality peer-reviewed journal.

5. (ngugi2023abioticselectionof pages 7-8): David K. Ngugi, Silvia G. Acinas, Pablo Sánchez, Josep M. Gasol, Susana Agusti, David M. Karl, and Carlos M. Duarte. Abiotic selection of microbial genome size in the global ocean. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-36988-x, doi:10.1038/s41467-023-36988-x. This article has 53 citations and is from a highest quality peer-reviewed journal.

6. (ngugi2023abioticselectionof pages 4-4): David K. Ngugi, Silvia G. Acinas, Pablo Sánchez, Josep M. Gasol, Susana Agusti, David M. Karl, and Carlos M. Duarte. Abiotic selection of microbial genome size in the global ocean. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-36988-x, doi:10.1038/s41467-023-36988-x. This article has 53 citations and is from a highest quality peer-reviewed journal.

7. (ngugi2023abioticselectionof media 6fcc2a7b): David K. Ngugi, Silvia G. Acinas, Pablo Sánchez, Josep M. Gasol, Susana Agusti, David M. Karl, and Carlos M. Duarte. Abiotic selection of microbial genome size in the global ocean. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-36988-x, doi:10.1038/s41467-023-36988-x. This article has 53 citations and is from a highest quality peer-reviewed journal.

8. (chuckran2023edaphiccontrolson pages 1-6): Peter F. Chuckran, Cody Flagg, Jeffrey Propster, William A. Rutherford, Ella Sieradzki, Steven J. Blazewicz, Bruce Hungate, Jennifer Pett-Ridge, Egbert Schwartz, and Paul Dijkstra. Edaphic controls on genome size and gc content of bacteria in soil microbial communities. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2021.11.17.469016, doi:10.1101/2021.11.17.469016. This article has 62 citations.

9. (wang2023bacterialgenomesize pages 2-3): Cong Wang, Qing-Yi Yu, Niu-Niu Ji, Yong Zheng, John W. Taylor, Liang-Dong Guo, and Cheng Gao. Bacterial genome size and gene functional diversity negatively correlate with taxonomic diversity along a ph gradient. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-43297-w, doi:10.1038/s41467-023-43297-w. This article has 135 citations and is from a highest quality peer-reviewed journal.

10. (dong2024ecoevolutionarystrategiesfor pages 1-2): Yang Dong, Ruirui Chen, Emily B. Graham, Bingqian Yu, Yuanyuan Bao, Xin Li, Xiangwei You, and Youzhi Feng. Eco-evolutionary strategies for relieving carbon limitation under salt stress differ across microbial clades. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50368-z, doi:10.1038/s41467-024-50368-z. This article has 88 citations and is from a highest quality peer-reviewed journal.

11. (dong2024ecoevolutionarystrategiesfor pages 2-3): Yang Dong, Ruirui Chen, Emily B. Graham, Bingqian Yu, Yuanyuan Bao, Xin Li, Xiangwei You, and Youzhi Feng. Eco-evolutionary strategies for relieving carbon limitation under salt stress differ across microbial clades. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50368-z, doi:10.1038/s41467-024-50368-z. This article has 88 citations and is from a highest quality peer-reviewed journal.

12. (dong2024ecoevolutionarystrategiesfor pages 4-5): Yang Dong, Ruirui Chen, Emily B. Graham, Bingqian Yu, Yuanyuan Bao, Xin Li, Xiangwei You, and Youzhi Feng. Eco-evolutionary strategies for relieving carbon limitation under salt stress differ across microbial clades. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50368-z, doi:10.1038/s41467-024-50368-z. This article has 88 citations and is from a highest quality peer-reviewed journal.

13. (dmitrijeva2024aglobalsurvey pages 1-2): Marija Dmitrijeva, Janko Tackmann, João Frederico Matias Rodrigues, Jaime Huerta-Cepas, Luis Pedro Coelho, and Christian von Mering. A global survey of prokaryotic genomes reveals the eco-evolutionary pressures driving horizontal gene transfer. Nature Ecology & Evolution, 8:986-998, Mar 2024. URL: https://doi.org/10.1038/s41559-024-02357-0, doi:10.1038/s41559-024-02357-0. This article has 79 citations and is from a highest quality peer-reviewed journal.

14. (kogay2024defencesystemsand pages 1-2): Roman Kogay, Yuri I. Wolf, and Eugene V. Koonin. Defence systems and horizontal gene transfer in bacteria. Environmental microbiology, 26 4:e16630, Apr 2024. URL: https://doi.org/10.1111/1462-2920.16630, doi:10.1111/1462-2920.16630. This article has 48 citations and is from a domain leading peer-reviewed journal.

15. (kogay2024defencesystemsand pages 4-5): Roman Kogay, Yuri I. Wolf, and Eugene V. Koonin. Defence systems and horizontal gene transfer in bacteria. Environmental microbiology, 26 4:e16630, Apr 2024. URL: https://doi.org/10.1111/1462-2920.16630, doi:10.1111/1462-2920.16630. This article has 48 citations and is from a domain leading peer-reviewed journal.

16. (giordano2024genomescalecommunitymodelling pages 1-2): Nils Giordano, Marinna Gaudin, Camille Trottier, Erwan Delage, Charlotte Nef, Chris Bowler, and Samuel Chaffron. Genome-scale community modelling reveals conserved metabolic cross-feedings in epipelagic bacterioplankton communities. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46374-w, doi:10.1038/s41467-024-46374-w. This article has 76 citations and is from a highest quality peer-reviewed journal.

17. (wang2023bacterialgenomesize pages 6-7): Cong Wang, Qing-Yi Yu, Niu-Niu Ji, Yong Zheng, John W. Taylor, Liang-Dong Guo, and Cheng Gao. Bacterial genome size and gene functional diversity negatively correlate with taxonomic diversity along a ph gradient. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-43297-w, doi:10.1038/s41467-023-43297-w. This article has 135 citations and is from a highest quality peer-reviewed journal.

18. (ngugi2023abioticselectionof media 584ca537): David K. Ngugi, Silvia G. Acinas, Pablo Sánchez, Josep M. Gasol, Susana Agusti, David M. Karl, and Carlos M. Duarte. Abiotic selection of microbial genome size in the global ocean. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-36988-x, doi:10.1038/s41467-023-36988-x. This article has 53 citations and is from a highest quality peer-reviewed journal.

19. (ngugi2023abioticselectionof media 67f8aad9): David K. Ngugi, Silvia G. Acinas, Pablo Sánchez, Josep M. Gasol, Susana Agusti, David M. Karl, and Carlos M. Duarte. Abiotic selection of microbial genome size in the global ocean. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-36988-x, doi:10.1038/s41467-023-36988-x. This article has 53 citations and is from a highest quality peer-reviewed journal.

20. (dong2024ecoevolutionarystrategiesfor pages 5-5): Yang Dong, Ruirui Chen, Emily B. Graham, Bingqian Yu, Yuanyuan Bao, Xin Li, Xiangwei You, and Youzhi Feng. Eco-evolutionary strategies for relieving carbon limitation under salt stress differ across microbial clades. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50368-z, doi:10.1038/s41467-024-50368-z. This article has 88 citations and is from a highest quality peer-reviewed journal.

21. (dong2024ecoevolutionarystrategiesfor pages 5-7): Yang Dong, Ruirui Chen, Emily B. Graham, Bingqian Yu, Yuanyuan Bao, Xin Li, Xiangwei You, and Youzhi Feng. Eco-evolutionary strategies for relieving carbon limitation under salt stress differ across microbial clades. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50368-z, doi:10.1038/s41467-024-50368-z. This article has 88 citations and is from a highest quality peer-reviewed journal.

22. (chuckran2023edaphiccontrolson pages 6-10): Peter F. Chuckran, Cody Flagg, Jeffrey Propster, William A. Rutherford, Ella Sieradzki, Steven J. Blazewicz, Bruce Hungate, Jennifer Pett-Ridge, Egbert Schwartz, and Paul Dijkstra. Edaphic controls on genome size and gc content of bacteria in soil microbial communities. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2021.11.17.469016, doi:10.1101/2021.11.17.469016. This article has 62 citations.

23. (dong2024ecoevolutionarystrategiesfor pages 3-4): Yang Dong, Ruirui Chen, Emily B. Graham, Bingqian Yu, Yuanyuan Bao, Xin Li, Xiangwei You, and Youzhi Feng. Eco-evolutionary strategies for relieving carbon limitation under salt stress differ across microbial clades. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50368-z, doi:10.1038/s41467-024-50368-z. This article has 88 citations and is from a highest quality peer-reviewed journal.

24. (kogay2024defencesystemsand pages 6-7): Roman Kogay, Yuri I. Wolf, and Eugene V. Koonin. Defence systems and horizontal gene transfer in bacteria. Environmental microbiology, 26 4:e16630, Apr 2024. URL: https://doi.org/10.1111/1462-2920.16630, doi:10.1111/1462-2920.16630. This article has 48 citations and is from a domain leading peer-reviewed journal.

25. (rodriguezgijon2023linkingprokaryoticgenome pages 1-2): Alejandro Rodríguez-Gijón, Moritz Buck, Anders F Andersson, Dandan Izabel-Shen, Francisco J A Nascimento, and Sarahi L Garcia. Linking prokaryotic genome size variation to metabolic potential and environment. ISME Communications, Mar 2023. URL: https://doi.org/10.1038/s43705-023-00231-x, doi:10.1038/s43705-023-00231-x. This article has 32 citations and is from a peer-reviewed journal.