---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:47:37.313988'
end_time: '2026-06-18T04:16:21.669174'
duration_seconds: 1724.36
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: rRNA operon copy number
  trait_identifier: traitmech:000101
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: rrna_operon_copy_number
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A quantitative genomics property describing the number of ribosomal
    RNA (rrn) operons encoded in a genome, which correlates with maximal growth rate
    and ecological strategy.
  parent_traits: METPO:1000188
  synonyms: rrn copy number
  evidence_summary: 'DOI:10.1128/AEM.66.4.1328-1333.2000:  (Klappenbach, Dunbar &
    Schmidt show rRNA operon copy number reflects ecological strategies, with fast
    responders carrying more copies.) | DOI:10.1038/nmicrobiol.2016.160:  (Roller,
    Stoddard & Schmidt link rrn copy number to bacterial growth rate and growth efficiency.)'
  causal_graph_summary: 'rrn_copy_growth_rate: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** rRNA operon copy number
- **METPO identifier:** traitmech:000101
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quantitative genomics property describing the number of ribosomal RNA (rrn) operons encoded in a genome, which correlates with maximal growth rate and ecological strategy.
- **Parent traits:** METPO:1000188
- **Synonyms:** rrn copy number
- **Existing evidence:** DOI:10.1128/AEM.66.4.1328-1333.2000:  (Klappenbach, Dunbar & Schmidt show rRNA operon copy number reflects ecological strategies, with fast responders carrying more copies.) | DOI:10.1038/nmicrobiol.2016.160:  (Roller, Stoddard & Schmidt link rrn copy number to bacterial growth rate and growth efficiency.)
- **Existing causal graph summary:** rrn_copy_growth_rate: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **rRNA operon copy number** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/rrna_operon_copy_number.yaml`.

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
- **Trait label:** rRNA operon copy number
- **METPO identifier:** traitmech:000101
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quantitative genomics property describing the number of ribosomal RNA (rrn) operons encoded in a genome, which correlates with maximal growth rate and ecological strategy.
- **Parent traits:** METPO:1000188
- **Synonyms:** rrn copy number
- **Existing evidence:** DOI:10.1128/AEM.66.4.1328-1333.2000:  (Klappenbach, Dunbar & Schmidt show rRNA operon copy number reflects ecological strategies, with fast responders carrying more copies.) | DOI:10.1038/nmicrobiol.2016.160:  (Roller, Stoddard & Schmidt link rrn copy number to bacterial growth rate and growth efficiency.)
- **Existing causal graph summary:** rrn_copy_growth_rate: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **rRNA operon copy number** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/rrna_operon_copy_number.yaml`.

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


## Research report: rRNA operon copy number (rrn copy number; traitmech:000101)

### 1) Scope summary (trait meaning, boundaries, nearby traits)

**Definition (TraitMech target):** *rRNA operon copy number* (rrn copy number) is a **genome-encoded quantitative trait**: the number of rRNA operons (typically linked **5S–16S–23S** rRNA gene clusters) encoded by a genome. It is an inherited genomic property and thus differs from dynamic physiological states. (klappenbach2000rrnaoperoncopy pages 1-2, roller2016exploitingrrnaoperon pages 1-5)

**What the trait represents biologically:** rrn copy number modulates the *potential capacity* for rRNA transcription and ribosome biogenesis when conditions favor rapid growth. In fast growth, rrn transcription can represent a large fraction of total transcriptional activity (reported up to ~70%), illustrating why multiple operons can increase the ceiling for rapid ribosome production. (klappenbach2000rrnaoperoncopy pages 1-2)

**Distinguish from nearby traits:**
- **Ribosome abundance (per cell)** and **rRNA transcription level** are *dynamic* and depend on growth conditions and regulation. rrn copy number sets template availability, but RNAP occupancy and ribosome output vary with medium and physiological state (e.g., remaining rrn operons can be driven to higher occupancy when rrn is deleted). (fan2023rnapolymeraseredistribution pages 14-15)
- **16S rRNA gene copy number in amplicon/metataxonomic studies** is often treated as synonymous with rrn copy number, but practical inference can be confounded by intragenomic heterogeneity and bioinformatic clustering thresholds. (pan2023microbialdiversitybiased pages 1-2)
- **Community-weighted mean rrn copy number** is an *aggregate community metric* inferred from taxonomic profiles and reference rrn databases; it reflects the mixture of taxa and is not identical to within-genome evolution of rrn copy number. (he2025microbiallifehistorystrategies pages 13-15)

**Boundary cases important for curation:**
- **Plasmid-borne / plasmid-only rrn operons:** Some bacteria lack chromosomal rrn loci and instead carry their only rrn operon(s) on plasmids, sometimes as tandem arrays. This affects how rrn copy number should be interpreted (genomic location and plasmid copy number complicate “per-genome” counting). (anda2023bacteriacanmaintain pages 1-2)
- **Intragenomic heterogeneity:** Multiple 16S copies within a genome are often not identical; in a survey of 24,248 complete genomes, intragenomic heterogeneity was observed in 60% of prokaryotic genomes (mostly <1% divergence), which can bias diversity estimates and complicate mapping between sequence variants and rrn copy number. (pan2023microbialdiversitybiased pages 1-2)

### 2) Key concepts and current understanding (mechanistic interpretation)

**Core conceptual model:** rrn copy number is widely interpreted as a genomic marker of a life-history strategy spectrum: high-rrn organisms tend to be **fast responders** under pulsed resource availability (often described as copiotrophic/r-strategist tendencies), while low-rrn organisms tend to be favored in **persistent low-resource** settings where efficiency and stress tolerance are prioritized. (klappenbach2000rrnaoperoncopy pages 2-3, klappenbach2000rrnaoperoncopy pages 1-2)

**Mechanistic mediators (molecular entities/processes):**
- **RNA polymerase (RNAP) allocation and occupancy on rrn genes:** In engineered E. coli strains with greatly reduced rrn operons, the remaining operons can reach high RNAP occupancy (~70% in one deletion strain in minimal medium), reflecting compensation by transcriptional redistribution rather than copy-number increase. (fan2023rnapolymeraseredistribution pages 14-15)
- **Physical and physiological limits:** A footprint-based maximum occupancy of ~135 RNAP per rrn operon was discussed, and very high rrn transcription loads are linked to toxicity and DNA damage. (fan2023rnapolymeraseredistribution pages 14-15)
- **Replication–transcription conflicts and stress responses:** High rrn transcription loads were associated with replication–transcription conflicts and an SOS-like response (activation of ~40 genes) in rich medium conditions in rrn-deletion strains, illustrating how rrn-related transcriptional architecture can feed into genome stability and stress physiology. (fan2023rnapolymeraseredistribution pages 14-15)

**Evolutionary/fitness trade-offs:** Klappenbach et al. discuss that extra rrn capacity can be costly under starvation/low nutrient conditions; ribosome degradation in starving cells implies that maintaining excess translation capacity is unfavorable, and adding extra rrn copies (e.g., plasmid-borne) can decrease growth rate in E. coli. (klappenbach2000rrnaoperoncopy pages 2-3)

### 3) Recent developments (prioritize 2023–2024)

**(A) Mechanistic cell-biology update (2023):**
- **RNAP redistribution in minimal-rrn E. coli:** Single-molecule imaging and quantitative modeling show that growth can be partly maintained despite severe rrn deletion via RNAP redistribution to remaining rrn loci; however, high rrn transcription density can lead to genomic instability and stress, emphasizing mechanistic constraints beyond “more rrn = faster growth.” (fan2023rnapolymeraseredistribution pages 14-15)

**(B) Global soil ecology using trait frameworks (2023–2024):**
- **Life-history trait dimensions across biomes:** A global metagenome analysis describes dominant axes of bacterial life-history strategies and links the secondary dimension to maximum growth rate and variation in rrn copy number, with pH, C:N, and precipitation patterns as major environmental drivers of life-history strategy distributions. (piton2023lifehistorystrategies pages 1-5)
- **Biogeography of growth potential (2024):** Soil microbiome potential growth rates (measured/validated using substrate-independent ^18O-H2O incorporation) were reported to correlate positively with rrn operon number and genome size, and to vary with aridity and broader stress/resource gradients (resource-rich acid-neutral cold/humid vs resource-poor dry/hot/hypersaline). (zhou2024thebiogeographyof pages 1-2)

**(C) Methodological work on 16S/rrn copy-number correction (2023):**
- A large-scale evaluation of copy-number prediction with uncertainty modeling reported predictions for **592,605 SILVA OTUs** and testing across **113,842 communities**, concluding that for **99% of communities** copy-number correction should improve compositional/functional profiles inferred from 16S reads, while impacts on beta-diversity tests are limited. (gao2023accountingfor16s pages 1-2)
- A complementary genome-scale survey emphasized copy-number ranges (1–37 in bacteria) and showed how intragenomic heterogeneity and interspecific conservation can bias diversity estimates (overestimation up to 156.5% at 100% identity with full-length 16S). (pan2023microbialdiversitybiased pages 1-2)

### 4) Current applications and real-world implementations

1. **Trait-based microbial ecology:** Community-weighted mean rrn copy number is used as a proxy for the prevalence of fast-growing vs slow-growing strategies in soils and other ecosystems, supporting interpretation of community shifts under disturbance or nutrient enrichment. (he2025microbiallifehistorystrategies pages 13-15, piton2023lifehistorystrategies pages 1-5)
2. **Parameterizing ecosystem and soil carbon models:** rrn-linked growth potential (often in combination with other genomic traits) is used to motivate mechanistic parameterization of microbial physiology in soil carbon cycling models. (zhou2024thebiogeographyof pages 1-2)
3. **16S amplicon bias correction / abundance estimation:** GCN correction methods use predicted 16S copy number to correct relative abundances and functional profile inferences from marker-gene surveys, with recent emphasis on uncertainty quantification. (gao2023accountingfor16s pages 1-2)
4. **Genome interpretation and comparative genomics:** rrn copy number is used in comparative frameworks to predict trait syndromes (e.g., chemotaxis probability, genome size) associated with resource-availability regimes. (roller2016exploitingrrnaoperon pages 1-5)

### 5) Statistics and quantitative findings (recent + foundational)

**Ranges and distributions:**
- Classic range reported in foundational ecology context: rrn copy number ~1–15 across bacteria. (klappenbach2000rrnaoperoncopy pages 1-2)
- Updated genome-scale range: 16S rRNA gene copy number 1–37 in bacteria and 1–5 in archaea (24,248 complete genomes). (pan2023microbialdiversitybiased pages 1-2)
- Comparative genome dataset (Roller et al., n=1,167) rrn distribution across 1–15 copies with per-copy counts: 150, 262, 195, 165, 104, 96, 76, 46, 25, 22, 8, 8, 3, 5, 2 genomes. (roller2016exploitingrrnaoperon pages 5-11)

**Growth-rate scaling:**
- Comparative evidence supports that **maximum growth rate increases approximately proportionally with rrn copy number** on a log2 scale (reported slopes around ~1; including ~0.98 phylogenetic slope shown in Supplementary Table 1 image). (roller2016exploitingrrnaoperon media 09e87f57, roller2016exploitingrrnaoperon pages 1-5)

**Experimental ecology examples (soil):**
- Fast colony-forming soil bacteria: mean ~5.5 small-subunit copies vs ~1.4 for slow responders. (klappenbach2000rrnaoperoncopy pages 1-2)
- 2,4-D pulse microcosms: dominant degraders ~5.4 copies vs ~2.7 in unamended controls. (klappenbach2000rrnaoperoncopy pages 1-2)

**Cell-physiology constraints (E. coli rrn deletion):**
- Remaining rrn operons in deletion strains reach ~70% occupancy; physical maximum discussed ~135 RNAP/rrn operon. (fan2023rnapolymeraseredistribution pages 14-15)

### Expert opinions / interpretations (authoritative sources)

- Foundational interpretation: rrn copy number reflects ecological strategies tied to resource responsiveness; high rrn is associated with rapid response to resource pulses in soils. (klappenbach2000rrnaoperoncopy pages 1-2)
- Comparative-genomics framework: rrn copy number predicts distinct components of reproduction (growth rate vs growth efficiency) favored under contrasting resource-availability regimes, and covaries with other traits such as chemotaxis. (roller2016exploitingrrnaoperon pages 5-11, roller2016exploitingrrnaoperon pages 1-5)
- Recent mechanistic caution: high rrn transcriptional load can induce genomic instability/stress via replication–transcription conflicts, indicating that rrn’s effect is mediated by transcriptional allocation and genome organization rather than copy number alone. (fan2023rnapolymeraseredistribution pages 14-15)

### Candidate graph nodes (grouped by type) and ontology grounding suggestions

**Trait node:**
- rRNA operon copy number — METPO mapping provided: traitmech:000101 (user); (label-only in evidence).

**Genes / proteins / complexes:**
- RNA polymerase (RNAP) — label-only (bacterial multisubunit RNAP).
- Rep_3 family replication initiator — label-only (plasmid replication initiator family). (anda2023bacteriacanmaintain pages 1-2)
- RelA, (p)ppGpp — label-only (stringent response; mechanistic leads). (welfer2025impactsofribosomal pages 5-6)
- RpoS (sigma factor σ38) — label-only. (welfer2025impactsofribosomal pages 5-6)
- ClpXP protease — label-only. (welfer2025impactsofribosomal pages 5-6)

**Biological processes (GO suggested):**
- Chemotaxis — GO:0006935. (roller2016exploitingrrnaoperon pages 1-5)
- SOS response — GO:0009432. (fan2023rnapolymeraseredistribution pages 14-15)
- Response to DNA damage stimulus — GO:0006974 (candidate). (fan2023rnapolymeraseredistribution pages 14-15)
- DNA repair — GO:0006281 (candidate). (fan2023rnapolymeraseredistribution pages 14-15)

**Environmental / experimental factors (ENVO label-only candidates):**
- Resource pulses / nutrient enrichment (soil amendments; e.g., 2,4-D pulse) (klappenbach2000rrnaoperoncopy pages 1-2)
- Fertilization with N and P (agricultural NP inputs) (he2025microbiallifehistorystrategies pages 13-15)
- Aridity / dry climates; hot/hypersaline vs cold/humid gradients (zhou2024thebiogeographyof pages 1-2)
- Soil pH; soil C:N; precipitation patterns (piton2023lifehistorystrategies pages 1-5)

**Chemicals / nutrients (CHEBI suggested where clear):**
- Nitrogen (CHEBI:25555) and phosphorus/phosphate (phosphate CHEBI:26078 as candidate) as fertilization drivers at community level. (he2025microbiallifehistorystrategies pages 13-15)
- 2,4-dichlorophenoxyacetic acid (2,4-D) — label-only (selection pressure/resource pulse context). (klappenbach2000rrnaoperoncopy pages 1-2)

### Candidate causal edges (curation-ready table)

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| Resource pulse / resource availability (label-only; e.g., ENVO resource pulse candidate) | selects for higher | rRNA operon copy number / rrn copy number (traitmech:000101) | Fast colony-forming soil bacteria averaged 5.5 16S copies vs 1.4 for slow responders; after 2,4-D pulses, dominant degraders averaged ~5.4 copies vs ~2.7 in controls. (klappenbach2000rrnaoperoncopy pages 1-2, klappenbach2000rrnaoperoncopy pages 4-5) | 10.1128/AEM.66.4.1328-1333.2000 (2000), https://doi.org/10.1128/AEM.66.4.1328-1333.2000 | Strong ecological/experimental support; community selection edge rather than within-lineage mechanistic change. |
| rRNA operon copy number (traitmech:000101) | increases capacity for | rRNA transcription / rRNA transcription initiation (GO candidate: transcription by RNA polymerase; label-only specificity) | rrn transcription can account for “up to ~70%” of cellular transcription during rapid growth; multiple operons increase ability to raise ribosome synthesis rapidly. (klappenbach2000rrnaoperoncopy pages 1-2) | 10.1128/AEM.66.4.1328-1333.2000 (2000), https://doi.org/10.1128/AEM.66.4.1328-1333.2000 | Mechanistic but partly inferred from classical physiology summarized in paper. |
| Excess rrn copy number / extra plasmid-borne rrn (label-only) | increases | stable RNA concentration (label-only) | Added plasmid-borne rrn copies “increase stable RNA concentrations while concomitantly decreasing growth rates in E. coli.” (klappenbach2000rrnaoperoncopy pages 2-3) | 10.1128/AEM.66.4.1328-1333.2000 (2000), https://doi.org/10.1128/AEM.66.4.1328-1333.2000 | Experimental support cited in review/discussion; should be curated as taxon-specific unless primary source checked. |
| Excess rrn copy number / extra plasmid-borne rrn (label-only) | decreases | growth rate (GO:0040007 growth, candidate) | Extra rrn copies can “decrease growth rates in E. coli,” indicating a cost of excess ribosome capacity. (klappenbach2000rrnaoperoncopy pages 2-3) | 10.1128/AEM.66.4.1328-1333.2000 (2000), https://doi.org/10.1128/AEM.66.4.1328-1333.2000 | Taxon-specific; edge direction pertains to excessive copy number above optimum. |
| rRNA operon copy number (traitmech:000101) | increases | maximum growth rate / maximum reproductive rate (GO:0040007 candidate) | “Maximum reproductive rate… doubles with a doubling of rrn copy number”; phylogenetic slope ~0.98 in log2-log2 space. (roller2016exploitingrrnaoperon pages 5-11, roller2016exploitingrrnaoperon media 09e87f57, roller2016exploitingrrnaoperon pages 1-5) | 10.1038/nmicrobiol.2016.160 (2016), https://doi.org/10.1038/nmicrobiol.2016.160 | Strong cross-species quantitative support; correlational/comparative, not direct manipulation across many taxa. |
| rRNA operon copy number (traitmech:000101) | decreases | growth efficiency / carbon use efficiency (label-only) | Growth efficiency is “inversely related to maximal growth rate and rrn copy number.” (roller2016exploitingrrnaoperon pages 5-11, roller2016exploitingrrnaoperon pages 1-5) | 10.1038/nmicrobiol.2016.160 (2016), https://doi.org/10.1038/nmicrobiol.2016.160 | Comparative/inferred; exact ontology grounding unclear. |
| rRNA operon copy number (traitmech:000101) | increases probability of | chemotactic motility (GO:0006935) | Chemotactic motility shows a positive relationship with log2-rrn; effect size up to +41.25% probability non-phylogenetically, +10.60% phylogenetically. (roller2016exploitingrrnaoperon pages 5-11, roller2016exploitingrrnaoperon pages 1-5) | 10.1038/nmicrobiol.2016.160 (2016), https://doi.org/10.1038/nmicrobiol.2016.160 | Correlational across 1,167 genomes; indirect ecological edge. |
| rRNA operon copy number (traitmech:000101) | positively correlates with | genome size (label-only) | Genome size and rrn copy number show a positive logarithmic relationship; effect size ~+0.66 Mbp phylogenetically for 15 vs 1 rrn. (roller2016exploitingrrnaoperon pages 5-11, roller2016exploitingrrnaoperon pages 1-5) | 10.1038/nmicrobiol.2016.160 (2016), https://doi.org/10.1038/nmicrobiol.2016.160 | Correlational trait-trait association; do not over-interpret as direct causation. |
| Reduced rrn operon number / rrn deletion (label-only) | increases occupancy of | RNA polymerase on remaining rrn operons (GO:0003899 RNA-directed DNA polymerase activity not precise; label-only preferred) | In Δrrn strains, remaining rrn operons reached ~70% RNAP occupancy in M9Glu. (fan2023rnapolymeraseredistribution pages 14-15) | 10.1093/NAR/GKAD511 (2023), https://doi.org/10.1093/NAR/GKAD511 | Strong mechanistic support in E. coli; taxon- and condition-specific. |
| Reduced rrn operon number / rrn deletion (label-only) | redistributes | RNA polymerase clusters to remaining rrn and other genes (label-only) | Δrrn strains “redistribute RNAP” to copies of remaining rrn operons and, in rich medium, to rRNA and mRNA genes. (fan2023rnapolymeraseredistribution pages 14-15) | 10.1093/NAR/GKAD511 (2023), https://doi.org/10.1093/NAR/GKAD511 | Mechanistic, but specific to engineered E. coli deletion strains. |
| High RNAP density on rrn operons (label-only) | causes | DNA damage / genomic instability (GO:0006974 response to DNA damage stimulus; GO:0006281 DNA repair candidate) | Very high RNAP densities on rrn genes are “toxic” and linked to “DNA damage” / “genomic instability.” (fan2023rnapolymeraseredistribution pages 14-15) | 10.1093/NAR/GKAD511 (2023), https://doi.org/10.1093/NAR/GKAD511 | Strong within-study mechanistic claim in E. coli. |
| High rrn transcription / high RNAP density on rrn (label-only) | promotes | replication–transcription conflict (GO candidate; label-only) | High rrn transcription can cause co-directional transcription–replication conflicts and replication restart. (fan2023rnapolymeraseredistribution pages 14-15) | 10.1093/NAR/GKAD511 (2023), https://doi.org/10.1093/NAR/GKAD511 | Mechanistic interpretation from Fan et al.; may warrant “uncertain/inferred” until primary conflict assays are curated directly. |
| Replication–transcription conflict (label-only) | activates | SOS response (GO:0009432 SOS response) | Conflict/high rrn transcription is linked to SOS-like responses with activation of ~40 genes. (fan2023rnapolymeraseredistribution pages 14-15) | 10.1093/NAR/GKAD511 (2023), https://doi.org/10.1093/NAR/GKAD511 | Mechanistic, but indirect in this summary; curate cautiously. |
| Rep_3-family replication initiator gene (label-only; Rep_3 family) | is associated with | plasmid-borne rrn operon maintenance (label-only) | “All the rrn-carrying plasmids… possess replication initiator genes of the Rep_3 family.” (anda2023bacteriacanmaintain pages 1-2) | 10.1038/s41467-023-42681-w (2023), https://doi.org/10.1038/s41467-023-42681-w | Association is strong, but causality for maintenance/stability is inferred. |
| Plasmid-borne rrn operon (label-only) | can substitute for | chromosomal rrn operon localization (label-only) | Some bacteria “carry their sole rrn operon on a plasmid,” and this arrangement was maintained for >492 MYA in Persicobacteraceae. (anda2023bacteriacanmaintain pages 1-2) | 10.1038/s41467-023-42681-w (2023), https://doi.org/10.1038/s41467-023-42681-w | Important boundary case for trait scope; not a generic causal edge about phenotype. |
| Resource-rich, acid-neutral, cold-humid soil conditions (ENVO candidates; label-only composite) | increase | microbial potential growth rate (label-only) | Potential growth is higher in “resource-rich, acid-neutral, cold and humid soils” and lower in resource-poor, dry, hot, hypersaline soils. (zhou2024thebiogeographyof pages 1-2) | 10.1038/s41467-024-53753-w (2024), https://doi.org/10.1038/s41467-024-53753-w | Environmental composite; correlational global biogeography. |
| Microbial potential growth rate (label-only) | positively correlates with | rRNA operon copy number (traitmech:000101) | Potential growth “positively correlates with genome size and the number of ribosomal RNA operons.” (zhou2024thebiogeographyof pages 1-2) | 10.1038/s41467-024-53753-w (2024), https://doi.org/10.1038/s41467-024-53753-w | Correlational; edge direction could also be modeled rrn -> growth potential. |
| Nitrogen fertilization (CHEBI:25555 nitrogen; treatment label-only) | increases | community-weighted rrn copy number (traitmech:000101 as community aggregate, label-only) | Long-term NP fertilization produced “elevated average rrn copy numbers.” (he2025microbiallifehistorystrategies pages 13-15) | 10.1128/msystems.00178-25 (2025), https://doi.org/10.1128/msystems.00178-25 | Community-level edge, not organism-level genome evolution. |
| Phosphorus fertilization (CHEBI:26078 phosphate candidate; treatment label-only) | increases | community-weighted rrn copy number (traitmech:000101 as community aggregate, label-only) | N and P contents “dominantly explained the total variance of the community-level rrn copy number.” (he2025microbiallifehistorystrategies pages 13-15) | 10.1128/msystems.00178-25 (2025), https://doi.org/10.1128/msystems.00178-25 | Community-level, SEM-supported; indirect for within-genome mechanism. |
| 16S rRNA gene copy number variation (label-only) | biases | amplicon-based relative abundance estimates (label-only) | 16S GCN “varies from 1 to more than 15” and biases relative cell abundance estimates from 16S reads. (gao2023accountingfor16s pages 1-2) | 10.1038/s43705-023-00266-0 (2023), https://doi.org/10.1038/s43705-023-00266-0 | Methodological edge relevant to assay interpretation rather than biology of the organism. |
| 16S GCN correction with uncertainty modeling (label-only) | improves | compositional and functional profile estimates from 16S surveys (label-only) | For 113,842 communities, correction should improve profiles for “99% of communities.” (gao2023accountingfor16s pages 1-2) | 10.1038/s43705-023-00266-0 (2023), https://doi.org/10.1038/s43705-023-00266-0 | Assay/analysis edge only; should not be curated as biological mechanism for TraitMech. |
| Intragenomic 16S rRNA heterogeneity (label-only) | inflates | diversity estimates / OTU-ASV splitting (label-only) | Heterogeneity was present in 60% of genomes; at 100% threshold diversity could be overestimated by up to 156.5%. (pan2023microbialdiversitybiased pages 1-2) | 10.1128/AEM.02108-22 (2023), https://doi.org/10.1128/AEM.02108-22 | Methodological boundary case; not a direct biological edge from rrn trait to phenotype. |
| 16S rRNA gene copy number (label-only assay trait) | ranges between | 1–37 in bacteria; 1–5 in archaea (label-only) | Large genome survey found 1–37 bacterial copies and 1–5 archaeal copies. (pan2023microbialdiversitybiased pages 1-2) | 10.1128/AEM.02108-22 (2023), https://doi.org/10.1128/AEM.02108-22 | Descriptive range, not causal; useful as scope metadata rather than graph edge. |


*Table: This table compiles candidate subject-predicate-object edges for curating a TraitMech graph for rRNA operon copy number, with evidence snippets, DOI-first references, and uncertainty notes. It mixes direct mechanistic edges, ecological selection edges, and methodological caution edges so curators can separate strong biological claims from assay-specific or correlational ones.*

### Warnings / curation cautions (do not curate yet, or curate as uncertain)

1. **Community-level rrn shifts vs genome evolution:** Edges like “N/P fertilization increases rrn copy number” are supported as *community-weighted mean shifts* (changes in community composition) and should not be interpreted as within-lineage evolution without additional evidence. (he2025microbiallifehistorystrategies pages 13-15)
2. **Correlational vs causal direction:** Many large comparative-genomics associations (rrn ↔ genome size; rrn ↔ chemotaxis) are strong but correlational; curate with an “association” or “inferred” qualifier unless mechanistic intervention evidence is added. (roller2016exploitingrrnaoperon pages 1-5)
3. **Assay-specific edges:** 16S copy-number correction improves inferred profiles in 16S surveys, but this is a methodological/analytical edge and should generally not be included as a biological causal mechanism in TraitMech. (gao2023accountingfor16s pages 1-2)
4. **Plasmid-only rrn boundary case:** Plasmid location and plasmid copy-number state can decouple “rrn loci count” from “functional rrn dosage per cell,” so curation should represent genomic location explicitly (chromosome vs plasmid) where relevant. (anda2023bacteriacanmaintain pages 1-2)

---

## DOI-first bibliography (with dates and URLs)

- Fan J, El Sayyed H, Pambos OJ, et al. **RNA polymerase redistribution supports growth in E. coli strains with a minimal number of rRNA operons.** *Nucleic Acids Research.* 2023-06. DOI:10.1093/nar/gkad511. URL:https://doi.org/10.1093/nar/gkad511 (fan2023rnapolymeraseredistribution pages 14-15)
- Gao Y, Wu M. **Accounting for 16S rRNA copy number prediction uncertainty and its implications in bacterial diversity analyses.** *ISME Communications.* 2023-06. DOI:10.1038/s43705-023-00266-0. URL:https://doi.org/10.1038/s43705-023-00266-0 (gao2023accountingfor16s pages 1-2)
- Anda M, Yamanouchi S, Cosentino S, et al. **Bacteria can maintain rRNA operons solely on plasmids for hundreds of millions of years.** *Nature Communications.* 2023-11. DOI:10.1038/s41467-023-42681-w. URL:https://doi.org/10.1038/s41467-023-42681-w (anda2023bacteriacanmaintain pages 1-2)
- Pan P, Gu Y, Sun D-L, Wu QL, Zhou N-Y. **Microbial Diversity Biased Estimation Caused by Intragenomic Heterogeneity and Interspecific Conservation of 16S rRNA Genes.** *Applied and Environmental Microbiology.* 2023-05. DOI:10.1128/aem.02108-22. URL:https://doi.org/10.1128/aem.02108-22 (pan2023microbialdiversitybiased pages 1-2)
- Piton G, Allison SD, Bahram M, et al. **Life history strategies of soil bacterial communities across global terrestrial biomes.** *Nature Microbiology.* 2023-10. DOI:10.1038/s41564-023-01465-0. URL:https://doi.org/10.1038/s41564-023-01465-0 (piton2023lifehistorystrategies pages 1-5)
- Zhou Z, Wang C, Cha X, et al. **The biogeography of soil microbiome potential growth rates.** *Nature Communications.* 2024-11. DOI:10.1038/s41467-024-53753-w. URL:https://doi.org/10.1038/s41467-024-53753-w (zhou2024thebiogeographyof pages 1-2)
- Zhang L, Zhao X, Wang J, et al. **Antarctic Soils Select Copiotroph-Dominated Bacteria.** *Microorganisms.* 2024-08. DOI:10.3390/microorganisms12081689. URL:https://doi.org/10.3390/microorganisms12081689 (zhang2024antarcticsoilsselect pages 1-2)
- Roller BRK, Stoddard SF, Schmidt TM. **Exploiting rRNA operon copy number to investigate bacterial reproductive strategies.** *Nature Microbiology.* 2016-09. DOI:10.1038/nmicrobiol.2016.160. URL:https://doi.org/10.1038/nmicrobiol.2016.160 (roller2016exploitingrrnaoperon pages 1-5, roller2016exploitingrrnaoperon media 09e87f57)
- Klappenbach JA, Dunbar JM, Schmidt TM. **rRNA Operon Copy Number Reflects Ecological Strategies of Bacteria.** *Applied and Environmental Microbiology.* 2000-04. DOI:10.1128/aem.66.4.1328-1333.2000. URL:https://doi.org/10.1128/aem.66.4.1328-1333.2000 (klappenbach2000rrnaoperoncopy pages 1-2)

### Figure/table evidence consulted
- Roller et al. 2016 Supplementary Table 1 (image) supporting the quantitative slope near 1.0 for log2(max growth rate) vs log2(rrn copy number). (roller2016exploitingrrnaoperon media 09e87f57)


References

1. (klappenbach2000rrnaoperoncopy pages 1-2): Joel A. Klappenbach, John M. Dunbar, and Thomas M. Schmidt. Rrna operon copy number reflects ecological strategies of bacteria. Applied and Environmental Microbiology, 66:1328-1333, Apr 2000. URL: https://doi.org/10.1128/aem.66.4.1328-1333.2000, doi:10.1128/aem.66.4.1328-1333.2000. This article has 1457 citations and is from a peer-reviewed journal.

2. (roller2016exploitingrrnaoperon pages 1-5): Benjamin R. K. Roller, Steven F. Stoddard, and Thomas M. Schmidt. Exploiting rrna operon copy number to investigate bacterial reproductive strategies. Nature Microbiology, Sep 2016. URL: https://doi.org/10.1038/nmicrobiol.2016.160, doi:10.1038/nmicrobiol.2016.160. This article has 581 citations and is from a highest quality peer-reviewed journal.

3. (fan2023rnapolymeraseredistribution pages 14-15): Jun Fan, Hafez El Sayyed, Oliver J Pambos, Mathew Stracy, Jingwen Kyropoulos, and Achillefs N Kapanidis. Rna polymerase redistribution supports growth in e. coli strains with a minimal number of rrna operons. Nucleic Acids Research, 51:8085-8101, Jun 2023. URL: https://doi.org/10.1093/nar/gkad511, doi:10.1093/nar/gkad511. This article has 18 citations and is from a highest quality peer-reviewed journal.

4. (pan2023microbialdiversitybiased pages 1-2): Piaopiao Pan, Yichao Gu, Dong-Lei Sun, Qinglong L. Wu, and Ning-Yi Zhou. Microbial diversity biased estimation caused by intragenomic heterogeneity and interspecific conservation of 16s rrna genes. Applied and Environmental Microbiology, May 2023. URL: https://doi.org/10.1128/aem.02108-22, doi:10.1128/aem.02108-22. This article has 51 citations and is from a peer-reviewed journal.

5. (he2025microbiallifehistorystrategies pages 13-15): Dan He, Zhongmin Dai, Shuxun Cheng, Haojie Shen, Jiahui Lin, Kankan Zhao, Jorge L. Mazza Rodrigues, Yakov Kuzyakov, and Jianming Xu. Microbial life-history strategies and genomic traits between pristine and cropland soils. May 2025. URL: https://doi.org/10.1128/msystems.00178-25, doi:10.1128/msystems.00178-25. This article has 21 citations and is from a peer-reviewed journal.

6. (anda2023bacteriacanmaintain pages 1-2): Mizue Anda, Shun Yamanouchi, Salvatore Cosentino, Mitsuo Sakamoto, Moriya Ohkuma, Masako Takashima, Atsushi Toyoda, and Wataru Iwasaki. Bacteria can maintain rrna operons solely on plasmids for hundreds of millions of years. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42681-w, doi:10.1038/s41467-023-42681-w. This article has 13 citations and is from a highest quality peer-reviewed journal.

7. (klappenbach2000rrnaoperoncopy pages 2-3): Joel A. Klappenbach, John M. Dunbar, and Thomas M. Schmidt. Rrna operon copy number reflects ecological strategies of bacteria. Applied and Environmental Microbiology, 66:1328-1333, Apr 2000. URL: https://doi.org/10.1128/aem.66.4.1328-1333.2000, doi:10.1128/aem.66.4.1328-1333.2000. This article has 1457 citations and is from a peer-reviewed journal.

8. (piton2023lifehistorystrategies pages 1-5): Gabin Piton, Steven D. Allison, Mohammad Bahram, Falk Hildebrand, Jennifer B. H. Martiny, Kathleen K. Treseder, and Adam C. Martiny. Life history strategies of soil bacterial communities across global terrestrial biomes. Nature Microbiology, 8:2093-2102, Oct 2023. URL: https://doi.org/10.1038/s41564-023-01465-0, doi:10.1038/s41564-023-01465-0. This article has 164 citations and is from a highest quality peer-reviewed journal.

9. (zhou2024thebiogeographyof pages 1-2): Zhenghu Zhou, Chuankuan Wang, Xinyu Cha, Tao Zhou, Xuesen Pang, Fazhu Zhao, Xinhui Han, Gaihe Yang, Gehong Wei, and Chengjie Ren. The biogeography of soil microbiome potential growth rates. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-53753-w, doi:10.1038/s41467-024-53753-w. This article has 76 citations and is from a highest quality peer-reviewed journal.

10. (gao2023accountingfor16s pages 1-2): Yingnan Gao and Martin Wu. Accounting for 16s rrna copy number prediction uncertainty and its implications in bacterial diversity analyses. ISME Communications, Jun 2023. URL: https://doi.org/10.1038/s43705-023-00266-0, doi:10.1038/s43705-023-00266-0. This article has 51 citations and is from a peer-reviewed journal.

11. (roller2016exploitingrrnaoperon pages 5-11): Benjamin R. K. Roller, Steven F. Stoddard, and Thomas M. Schmidt. Exploiting rrna operon copy number to investigate bacterial reproductive strategies. Nature Microbiology, Sep 2016. URL: https://doi.org/10.1038/nmicrobiol.2016.160, doi:10.1038/nmicrobiol.2016.160. This article has 581 citations and is from a highest quality peer-reviewed journal.

12. (roller2016exploitingrrnaoperon media 09e87f57): Benjamin R. K. Roller, Steven F. Stoddard, and Thomas M. Schmidt. Exploiting rrna operon copy number to investigate bacterial reproductive strategies. Nature Microbiology, Sep 2016. URL: https://doi.org/10.1038/nmicrobiol.2016.160, doi:10.1038/nmicrobiol.2016.160. This article has 581 citations and is from a highest quality peer-reviewed journal.

13. (welfer2025impactsofribosomal pages 5-6): Griffin A. Welfer, Ryan A. Brady, S. Kundhavai Natchiar, Zoe L. Watson, Emily J. Rundlet, Jose L. Alejo, Anand P. Singh, Nitish K. Mishra, Roger B. Altman, and Scott C. Blanchard. Impacts of ribosomal rna sequence variation on gene expression and phenotype. Philosophical Transactions of the Royal Society B: Biological Sciences, Mar 2025. URL: https://doi.org/10.1098/rstb.2023.0379, doi:10.1098/rstb.2023.0379. This article has 8 citations and is from a domain leading peer-reviewed journal.

14. (klappenbach2000rrnaoperoncopy pages 4-5): Joel A. Klappenbach, John M. Dunbar, and Thomas M. Schmidt. Rrna operon copy number reflects ecological strategies of bacteria. Applied and Environmental Microbiology, 66:1328-1333, Apr 2000. URL: https://doi.org/10.1128/aem.66.4.1328-1333.2000, doi:10.1128/aem.66.4.1328-1333.2000. This article has 1457 citations and is from a peer-reviewed journal.

15. (zhang2024antarcticsoilsselect pages 1-2): Lujie Zhang, Xue Zhao, Jieying Wang, Liyuan He, Chengjie Ren, Jun Wang, Yaoxin Guo, Ninglian Wang, and Fazhu Zhao. Antarctic soils select copiotroph-dominated bacteria. Microorganisms, 12:1689, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081689, doi:10.3390/microorganisms12081689. This article has 2 citations.