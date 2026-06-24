---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:12:13.364422'
end_time: '2026-06-17T20:25:25.721076'
duration_seconds: 792.36
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: free-living
  trait_identifier: traitmech:000048
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: free_living
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A habitat association in which an organism lives independently in the
    environment, not obligately associated with a host.
  parent_traits: traitmech:000047
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro1341:  (Martiny et al. support biogeographic
    patterning of free-living microbial taxa across environments.) | DOI:10.1038/nrmicro.2017.171:  (Poole
    et al. describe rhizobia in their free-living soil phase, contrasting it with
    the host-associated endosymbiotic phase.)'
  causal_graph_summary: 'free_living_environmental_habitat: 3 nodes, 2 edges'
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
- **Trait label:** free-living
- **METPO identifier:** traitmech:000048
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives independently in the environment, not obligately associated with a host.
- **Parent traits:** traitmech:000047
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro1341:  (Martiny et al. support biogeographic patterning of free-living microbial taxa across environments.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia in their free-living soil phase, contrasting it with the host-associated endosymbiotic phase.)
- **Existing causal graph summary:** free_living_environmental_habitat: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **free-living** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/free_living.yaml`.

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
- **Trait label:** free-living
- **METPO identifier:** traitmech:000048
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives independently in the environment, not obligately associated with a host.
- **Parent traits:** traitmech:000047
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro1341:  (Martiny et al. support biogeographic patterning of free-living microbial taxa across environments.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia in their free-living soil phase, contrasting it with the host-associated endosymbiotic phase.)
- **Existing causal graph summary:** free_living_environmental_habitat: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **free-living** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/free_living.yaml`.

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


# Research Report: TraitMech Causal Graph Candidate — **free-living** (METPO:traitmech:000048)

## 1) Scope summary (trait meaning, definitions, boundary cases)

**Trait definition (curation-ready):** *Free-living* denotes a habitat association in which a microbe lives independently in the environment, **not obligately associated with a host** (TraitMech definition). Operationally, a recent comparative-genomics framework classifies species as **“free”** when they “lived independent of any host, little or no evidence of host association,” and recognizes an intermediate category **“primarily free”** for taxa found in both hosts and the environment but mostly outside hosts. (dewar2024bacteriallifestyleshapes pages 7-8)

**What the trait is (and is not):**
- *Free-living* is an **ecological association**, not a specific physiological pathway. Mechanisms enabling free-living are therefore best represented via **intermediate nodes** (stress tolerance, nutrient acquisition, motility, etc.) rather than a single “free-living gene.” (jaffe2023habitattransitionin pages 8-11, dewar2024bacteriallifestyleshapes pages 7-8)
- **Boundary case 1 — facultative host association:** Many microbes can alternate between host-associated and environmental phases. A clear example is *Vibrio fischeri*, where “~90% of Vibrio cells are vented out of the light organ back to their original planktonic niche,” illustrating cycling between host-associated and free-living states. (jaffe2023habitattransitionin pages 4-6)
- **Boundary case 2 — free-living is not synonymous with planktonic:** Environmental microbes can be free-living yet **biofilm-associated** (surface-attached) rather than planktonic. Environmental biofilms can increase persistence compared to planktonic free-living cells, and should be modeled as a separate state/node. (schaudinn2023francisellatularensissubsp. pages 5-6)
- **Boundary case 3 — “secondary” free-living:** Some lineages appear to revert from endobiotic/host-associated ancestry to free-living via reacquisition/retention of metabolic functions (rare because host dependence often entails pathway loss). (wisniewska2024expandedgeneand pages 1-3)

## 2) Current understanding: mechanistic themes that enable free-living

The convergent mechanistic requirements for environmental independence (across taxa and habitats) include:

### A. Metabolic breadth and retained biosynthesis
Host association (especially obligate and/or vertical transmission) is often accompanied by **genome reduction**, pseudogenization, and **loss of metabolic capacities**, increasing dependence on host-provided nutrients and cofactors. (espada‐hinojosa2024comparativegenomicsof pages 1-2, wang2024comparativegenomicanalysis pages 1-2)

A concrete 2024 example compares **symbiotic vs free-living Fluviibacter**: symbiotic strains have a ~1.67 Mb genome versus ~2.29–2.43 Mb in free-living relatives, with many more pseudogenes (297 vs 38–69). Key carbon-metabolism genes (e.g., phosphofructokinase, pyruvate kinase) are pseudogenized and malate synthase is lost, consistent with reduced ability to metabolize sugars and use acetyl‑CoA relative to free-living strains. (wang2024comparativegenomicanalysis pages 5-7)

### B. Nutrient acquisition (especially phosphorus)
Free-living environmental conditions are often nutrient-limited and variable. In a 2023 experimental system contrasting free-living vs biofilm-associated cells of *Leisingera aquaemixtae* (Roseobacteraceae), warming induced strong transcriptional changes in free-living cells, including upregulation of **phosphorus utilization genes** (pst/ugp/pho/phn). (wang2023biofilmformationstabilizes pages 5-7)

Comparative evidence from a 2024 symbiont/free-living pair (thiotrophic ectosymbiont vs free-living relative) similarly highlights that the more versatile free-living strain possessed additional genes “for the acquisition of phosphorus,” interpreted as adaptive under unstable environmental conditions. (espada‐hinojosa2024comparativegenomicsof pages 1-2)

### C. Motility and chemotaxis (environmental searching)
Environmental independence often requires active movement toward resources and niches. In *Leisingera aquaemixtae*, the genome encodes flagellar assembly genes **fli/flg**, shows **moderate motility**, and free-living cells upregulated motility (flg/fli) and chemotaxis (che) genes in response to warming. (wang2023biofilmformationstabilizes pages 2-5, wang2023biofilmformationstabilizes pages 5-7)

### D. Osmoadaptation across salinity gradients
A major boundary for free-living habitat transitions is the “salt barrier,” requiring coordinated changes in ion usage and osmotic stress responses. Marine adaptation is associated with acquisition of **sodium transporters**, **ectoine synthesis**, and **Na+-translocating NQR** complex components; transitions to low salinity involve loss/replacement of these and acquisition of **mechanosensitive channels**. (jaffe2023habitattransitionin pages 4-6)

Consistently, Paracoccus comparative genomics identifies widespread compatible-solute systems, including a conserved **ectoine cluster**, trehalose synthesis/transport, and glycine-betaine related genes/transporters, supporting osmoprotection as a general environmental persistence mechanism. (hollensteiner2023pangenomeanalysisof pages 11-13)

### E. Biofilms as environmental persistence state (non-host-associated)
A 2023 aquatic study shows *Francisella tularensis* subsp. *holarctica* can colonize natural **ex vivo aquatic biofilms**. Biofilm-associated cells remained culturable longer than planktonic (free-living) cells, and both adopted VBNC-like survival with time. (schaudinn2023francisellatularensissubsp. pages 5-6)

## 3) Recent developments (prioritizing 2023–2024)

### 3.1 Lifestyle as a driver of genome evolution (pangenomes)
A 2024 phylogeny-aware analysis across **126 bacterial species (6,221 genomes)** found **lifestyle** to be a major driver of **pangenome fluidity**, with host-associated species having **lower** fluidity than free-living species. Reported pangenome fluidity ranged from ~1% to >40%, and the authors describe explicit coding categories for free vs primarily free vs host-associated. (dewar2024bacteriallifestyleshapes pages 7-8, dewar2024bacteriallifestyleshapes pages 1-2)

### 3.2 Symbiosis ↔ free-living transitions and the role of gene flow
A 2024 BMC Biology phylogenomic study of diplomonads sequenced transcriptomes from **13 free-living and 1 host-associated** isolate (expanding genome-scale sampling ~threefold), and argues that reversals to free-living are rare because parasites often lose metabolic pathways needed for free-living; the authors propose that regaining host independence may be facilitated by **laterally transferred genes**. (wisniewska2024expandedgeneand pages 1-3)

### 3.3 Experimental quantification of “free-living vs biofilm-associated” responses
In *Leisingera aquaemixtae*, warming from 25°C to 31°C induced **435 DEGs** in free-living cells versus **219 DEGs** in biofilm-associated cells; free-living maximum growth rate increased from **0.066 ± 0.001 h⁻¹** to **0.198 ± 0.005 h⁻¹**. These data support a model in which free-living cells show stronger environmental responsiveness, while biofilms buffer metabolic perturbations. (wang2023biofilmformationstabilizes pages 5-7, wang2023biofilmformationstabilizes media fafff1db, wang2023biofilmformationstabilizes media 08581529)

## 4) Candidate causal graph entities (nodes) grouped by type

### 4.1 Trait/lifestyle state nodes
- **free-living** — METPO:traitmech:000048
- host-associated / endobiotic (label-only; candidate for METPO parent/sibling traits) (dewar2024bacteriallifestyleshapes pages 7-8)
- biofilm-associated (label-only state; not a host-association proxy) (schaudinn2023francisellatularensissubsp. pages 5-6)

### 4.2 Environmental and experimental factors (ENVO where feasible)
- Temperature increase / warming (experimental factor) (wang2023biofilmformationstabilizes pages 5-7)
- Salinity transition / osmotic stress (“salt barrier”) (jaffe2023habitattransitionin pages 4-6)
- Low oxygen conditions (environmental factor; inferred from terminal oxidase choice) (wang2024comparativegenomicanalysis pages 5-7)
- Aquatic multispecies biofilm habitat (environmental reservoir) (schaudinn2023francisellatularensissubsp. pages 5-6)

### 4.3 Processes and molecular functions (GO)
- Horizontal gene transfer — GO:0019860 (dewar2024bacteriallifestyleshapes pages 1-2, wisniewska2024expandedgeneand pages 1-3)
- Motility — GO:0040011; chemotaxis — GO:0006935 (wang2023biofilmformationstabilizes pages 5-7, wang2023biofilmformationstabilizes pages 2-5)
- Phosphate metabolic process / acquisition — GO:0006793 (wang2023biofilmformationstabilizes pages 5-7)
- Biofilm formation / biofilm matrix — GO:0042710 (schaudinn2023francisellatularensissubsp. pages 5-6)

### 4.4 Genes/protein complexes (label sets; grounding varies by database)
- **Phosphate uptake/utilization:** pst, ugp, pho, phn (wang2023biofilmformationstabilizes pages 5-7)
- **Motility:** flg, fli; **Chemotaxis:** che (wang2023biofilmformationstabilizes pages 5-7, wang2023biofilmformationstabilizes pages 2-5)
- **Osmotic adaptation:** NQR complex; sodium transporters; mechanosensitive channels (jaffe2023habitattransitionin pages 4-6)
- **Terminal oxidases:** cytochrome bd-type and cbb3-type oxidases (wang2024comparativegenomicanalysis pages 5-7)

### 4.5 Chemicals / osmolytes / storage compounds (CHEBI where feasible)
- Ectoine — CHEBI:27689 (jaffe2023habitattransitionin pages 4-6, hollensteiner2023pangenomeanalysisof pages 11-13)
- Glycine betaine — CHEBI:17750 (hollensteiner2023pangenomeanalysisof pages 11-13)
- Trehalose (CHEBI grounding not provided in evidence; GO process available) (hollensteiner2023pangenomeanalysisof pages 11-13)
- Poly(3‑hydroxybutyrate) (PHB; CHEBI grounding not provided in evidence) (agudelo2023theroleof pages 2-3)

## 5) Evidence-backed candidate causal edges (curation table)

The following table is designed to be directly curatable into `data/traits/ecology/free_living.yaml` after curator review.

| Subject node (label + CURIE) | Predicate | Object node (label + CURIE) | Evidence snippet | Source (DOI + URL + year) | Curation notes |
|---|---|---|---|---|---|
| free-living lifestyle (METPO:traitmech:000048) | associated_with | larger genome size (label-only) | Free-living genomes “tend to comprise (1) larger genomes” than host-associated Paracoccus; across bacteria, larger genomes correlate with more fluid pangenomes. (dewar2024bacteriallifestyleshapes pages 1-2, hollensteiner2023pangenomeanalysisof pages 11-13) | 10.1073/pnas.2320170121 — https://doi.org/10.1073/pnas.2320170121 (2024); 10.1371/journal.pone.0287947 — https://doi.org/10.1371/journal.pone.0287947 (2023) | Correlational; broad comparative-genomics signal, not a direct mechanism; useful as background edge only. |
| free-living lifestyle (METPO:traitmech:000048) | associated_with | high pangenome fluidity (label-only) | “Pangenome fluidity was lower in host-associated compared with free-living species”; across 126 species lifestyle was the strongest driver. (dewar2024bacteriallifestyleshapes pages 1-2, dewar2024bacteriallifestyleshapes pages 7-8) | 10.1073/pnas.2320170121 — https://doi.org/10.1073/pnas.2320170121 (2024) | Correlational macroevolutionary edge; do not overinterpret as cell-level mechanism. |
| horizontal gene transfer capacity (GO:0019860) | promotes | free-living lifestyle (METPO:traitmech:000048) | Free-living/variable-environment species have more opportunity “to acquire genes horizontally,” and regaining host independence in diplomonads “may have been facilitated by a subset of laterally transferred genes.” (dewar2024bacteriallifestyleshapes pages 1-2, wisniewska2024expandedgeneand pages 1-3, jaffe2023habitattransitionin pages 8-11) | 10.1073/pnas.2320170121 — https://doi.org/10.1073/pnas.2320170121 (2024); 10.1186/s12915-024-02013-w — https://doi.org/10.1186/s12915-024-02013-w (2024); 10.48550/arxiv.2302.00582 — https://doi.org/10.48550/arxiv.2302.00582 (2023) | Mixed evidence: broad comparative plus taxon-specific reversal to free-living; curate as uncertain/generalized. |
| phosphorus acquisition genes pst/ugp/pho/phn (KEGG:K02040/K06163 family; label-level set) | enable | environmental nutrient acquisition (GO:0006793) | In free-living Leisingera, warming upregulated “phosphorus utilization (pst, ugp, pho, phn)” genes; free-living ODIII6 also had additional genes “for the acquisition of phosphorus.” (wang2023biofilmformationstabilizes pages 5-7, espada‐hinojosa2024comparativegenomicsof pages 1-2) | 10.1128/aem.00601-23 — https://doi.org/10.1128/aem.00601-23 (2023); 10.1111/1755-0998.13889 — https://doi.org/10.1111/1755-0998.13889 (2024) | Strong mechanistic plausibility for environmental independence; gene set and phenotype are taxon-specific but curation-worthy. |
| phosphorus acquisition genes pst/ugp/pho/phn (KEGG:K02040/K06163 family; label-level set) | promotes | free-living lifestyle (METPO:traitmech:000048) | Free-living relative ODIII6 possessed extra functions for phosphorus acquisition, illustrating features “adaptive for the unstable environmental conditions.” (espada‐hinojosa2024comparativegenomicsof pages 1-2) | 10.1111/1755-0998.13889 — https://doi.org/10.1111/1755-0998.13889 (2024) | Comparative-genomic inference from one symbiont/free-living pair; useful but uncertain. |
| flagellar assembly genes fli/flg (GO:0009288) | enable | motility (GO:0040011) | Genome of free-living/biofilm-capable Leisingera encoded “flagellar assembly genes (fli, flg)” and a swimming assay showed “moderate motility.” (wang2023biofilmformationstabilizes pages 2-5) | 10.1128/aem.00601-23 — https://doi.org/10.1128/aem.00601-23 (2023) | Direct genotype-to-phenotype evidence; taxon-specific but standardizable. |
| chemotaxis genes che (GO:0006935) | promote | free-living lifestyle (METPO:traitmech:000048) | In free-living Leisingera, warming upregulated “motility (flg, fli), chemotaxis (che)” genes, consistent with higher environmental responsiveness of free-living cells. (wang2023biofilmformationstabilizes pages 5-7) | 10.1128/aem.00601-23 — https://doi.org/10.1128/aem.00601-23 (2023) | Evidence is conditional (temperature response) and from one marine bacterium; curate as uncertain/context-dependent. |
| sodium transporters (label-only) | enable | marine free-living habitat adaptation (ENVO:00002030) | Adaptation to marine habitats involved gains of “sodium transporters” and the “Na+-translocating (NQR) complex.” (jaffe2023habitattransitionin pages 4-6) | 10.48550/arxiv.2302.00582 — https://doi.org/10.48550/arxiv.2302.00582 (2023) | Good habitat-specific mechanistic edge; applies to salinity boundary cases rather than all free-living organisms. |
| ectoine biosynthetic pathway (CHEBI:27689; pathway label) | enables | osmotic stress tolerance (GO:0006970) | Crossing salinity barriers requires osmotic-stress mechanisms; marine adaptation includes “components involved in ectoine synthesis,” and Paracoccus carried “the ectoine cluster… in all strains.” (jaffe2023habitattransitionin pages 4-6, hollensteiner2023pangenomeanalysisof pages 11-13) | 10.48550/arxiv.2302.00582 — https://doi.org/10.48550/arxiv.2302.00582 (2023); 10.1371/journal.pone.0287947 — https://doi.org/10.1371/journal.pone.0287947 (2023) | Strong mechanistic edge for environmental persistence; not specific to free-living alone. |
| ectoine biosynthetic pathway (CHEBI:27689; pathway label) | promotes | free-living lifestyle (METPO:traitmech:000048) | Ectoine-related osmoadaptation is highlighted as part of adaptation to unstable or saline environmental conditions in free-living lineages. (jaffe2023habitattransitionin pages 4-6) | 10.48550/arxiv.2302.00582 — https://doi.org/10.48550/arxiv.2302.00582 (2023) | Broad inference; likely curate through intermediate node “osmotic stress tolerance” rather than directly to trait. |
| trehalose biosynthesis/transport (GO:0005992; sugA/sugB/sugC label set) | enables | stress tolerance in fluctuating environments (GO:0006950) | Paracoccus genomes widely encoded trehalose synthesis/transport; compatible-solute systems were discussed as persistence traits, with some losses in host-associated lineages. (hollensteiner2023pangenomeanalysisof pages 11-13) | 10.1371/journal.pone.0287947 — https://doi.org/10.1371/journal.pone.0287947 (2023) | Mechanistic but indirect for free-living; genus-specific comparative evidence. |
| glycine betaine transport/biosynthesis (CHEBI:17750; betA/betB/betI, opu/proV/proX set) | enables | osmoprotection (GO:0006970) | Hollensteiner et al. identified “betA-betB, betI operon” and multiple glycine-betaine transporters, linking these systems to persistence under environmental stress. (hollensteiner2023pangenomeanalysisof pages 11-13) | 10.1371/journal.pone.0287947 — https://doi.org/10.1371/journal.pone.0287947 (2023) | Good mechanistic edge; free-living link is inferred from comparative ecology, not directly tested. |
| insertion sequence abundance (SO:0000188) | associated_with | free-living lifestyle (METPO:traitmech:000048) | In Paracoccus, host-associated strains had the lowest IS content; authors note that in “free-living bacteria IS elements [are] thought to be more beneficial in fluctuating environments.” (hollensteiner2023pangenomeanalysisof pages 11-13) | 10.1371/journal.pone.0287947 — https://doi.org/10.1371/journal.pone.0287947 (2023) | Correlational and lineage-specific; probably not suitable as a direct causal edge in TraitMech. |
| biofilm extracellular matrix (GO:0042710) | increases | environmental persistence (label-only) | Francisella biofilms formed a dense matrix with eDNA, proteins and lipids, and the biofilm form showed “longer cultivability… when compared to planktonic (free-living) bacteria.” (schaudinn2023francisellatularensissubsp. pages 5-6) | 10.3389/fmicb.2023.1113412 — https://doi.org/10.3389/fmicb.2023.1113412 (2023) | Strong persistence edge, but biofilm is not equivalent to free-living; important boundary case because many free-living cells are surface-associated. |
| biofilm formation (GO:0042710) | buffers_against | temperature-induced metabolic reprogramming (label-only) | Biofilm formation “stabilizes metabolism” whereas free-living cells showed more DEGs and larger shifts in growth and ROS under warming. (wang2023biofilmformationstabilizes pages 5-7, wang2023biofilmformationstabilizes pages 1-2, wang2023biofilmformationstabilizes media fafff1db) | 10.1128/aem.00601-23 — https://doi.org/10.1128/aem.00601-23 (2023) | Useful contrast node for scope: free-living planktonic vs biofilm-associated are different states, not opposite ecological trait classes. |
| low-oxygen terminal oxidases cbb3-type/cytochrome bd (GO:0004129; GO:0015002) | enable | persistence in low-oxygen environmental niches (ENVO:01001026) | Free-living and symbiotic Fluviibacter lacked common cytochrome c oxidase but encoded “cytochrome bd-type and cbb3-type oxidases,” interpreted as adaptation to low O2. (wang2024comparativegenomicanalysis pages 5-7) | 10.1128/aem.01900-23 — https://doi.org/10.1128/aem.01900-23 (2024) | Strong habitat-mechanism edge; not specific to free-living because both free-living and symbiotic strains retained it. |
| complete metabolic capacity for carbon / nitrogen / sulfur / cofactors (label-only) | required_for | free-living lifestyle (METPO:traitmech:000048) | Reversion to free-living is rare because parasites often lose “metabolic pathways that are essential to a free-living life strategy”; symbiotic Fluviibacter showed “reduced metabolic capacities” and host dependence for carbon, organic nitrogen, sulfur, and cofactors. (wisniewska2024expandedgeneand pages 1-3, wang2024comparativegenomicanalysis pages 1-2) | 10.1186/s12915-024-02013-w — https://doi.org/10.1186/s12915-024-02013-w (2024); 10.1128/aem.01900-23 — https://doi.org/10.1128/aem.01900-23 (2024) | Strong high-level edge; causal but somewhat abstract. Better decomposed into specific biosynthetic modules when possible. |
| phosphofructokinase / pyruvate kinase / malate synthase (EC:2.7.1.11 / EC:2.7.1.40 / EC:2.3.3.9) | support | free-living carbon metabolism (label-only) | In symbiotic Fluviibacter, phosphofructokinase and pyruvate kinase were pseudogenized and malate synthase was lost, implying reduced sugar metabolism and acetyl-CoA utilization relative to free-living strains. (wang2024comparativegenomicanalysis pages 5-7) | 10.1128/aem.01900-23 — https://doi.org/10.1128/aem.01900-23 (2024) | Comparative inference from gene loss in symbiont; reasonable mechanistic edge, but should be curated as taxon-specific. |
| uptake/incorporation machinery for foreign DNA (label-only) | promotes | horizontal gene transfer capacity (GO:0019860) | Free-living bacteria and ectosymbionts have access to novel gene pools, whereas obligate symbionts may lose “uptake/incorporation machinery for foreign DNA,” limiting HGT. (espada‐hinojosa2024comparativegenomicsof pages 1-2) | 10.1111/1755-0998.13889 — https://doi.org/10.1111/1755-0998.13889 (2024) | Mechanistically useful intermediate edge; evidence from one symbiont comparison and should be marked uncertain. |


*Table: This table lists candidate causal and associational edges that could support curation of the microbial ecology trait 'free-living'. It emphasizes evidence-backed mechanisms, highlights uncertainty where claims are comparative or correlational, and distinguishes general persistence mechanisms from boundary-case states such as biofilms.*

## 6) Current applications and real-world implementations

### 6.1 Agriculture: rhizobia and soil-phase survival (inoculants, strain selection)
Rhizobia explicitly have a biphasic life cycle including a **free-living soil/rhizosphere phase** and a plant-associated symbiotic phase; a major fitness component is “proliferation and survival in the soil and rhizosphere.” (agudelo2023theroleof pages 1-2)

A 2023 review emphasizes that following nodule senescence, rhizobia can “survive for months or even years” in soil, and that intracellular carbon stores accumulated during symbiosis—especially **PHB**—support environmental persistence and potentially several cell divisions. Some strains can accumulate PHB “up to **50% of the dry weight** of the cells,” and PHB can support “a much longer survival of dormant cells.” The same source proposes **PHB content** in bacteroids as a proxy for estimating soil reproductive ability of released rhizobia, but notes a trade-off: PHB synthesis may divert energy from nitrogen fixation and may trigger plant sanctions. (agudelo2023theroleof pages 2-3)

**Implementation implication:** inoculant development and screening can incorporate PHB-associated traits (storage capacity, dormancy survival) as candidate predictors of soil persistence and competitiveness, while considering the trade-off with symbiotic performance. (agudelo2023theroleof pages 2-3)

### 6.2 Agriculture: co-inoculation and community engineering
Co-inoculation strategies leverage the free-living/rhizosphere phase by adding additional plant-growth-promoting microbes that improve stress tolerance and nodulation outcomes. A quantitative example: co-inoculation of *Rhizobium* TAL‑1148 with Ni-tolerant *Bacillus subtilis* increased faba bean Ni tolerance to **600 mg Ni kg⁻¹** (as reported in the review’s synthesis of primary studies). (goyal2023evaluationoflegume–rhizobial pages 8-10)

A rhizobial eco-evolution review argues that considering whole microbial communities is crucial and proposes an applied direction: **designing synthetic microbial communities** to enhance rhizobial fitness and symbiotic services and mitigate pathogens. (agudelo2023theroleof pages 10-11)

### 6.3 Environmental health: aquatic persistence and reservoirs
Environmental persistence of pathogens can involve free-living and biofilm-associated states. *Francisella tularensis* subsp. *holarctica* (Type B) was shown to colonize natural aquatic multi-species biofilms, with biofilm-associated cells remaining culturable longer than planktonic cells, suggesting biofilms as environmental reservoirs that may influence transmission cycles. (schaudinn2023francisellatularensissubsp. pages 5-6)

### 6.4 Microbial ecology: monitoring and inference from comparative genomics
Large-scale comparative genomics now provides operational lifestyle coding (free vs primarily free vs host-associated) and shows lifestyle-correlated genome properties (pangenome fluidity, genome size relationships). This can be used to prioritize candidate mechanisms for curation and to interpret metagenome-assembled genomes (MAGs) and isolate collections. (dewar2024bacteriallifestyleshapes pages 7-8, dewar2024bacteriallifestyleshapes pages 1-2)

## 7) Key recent statistics/data points (curation-relevant)

- **Pangenome/lifestyle analysis (2024):** 126 species, 6,221 genomes; pangenome fluidity ranged ~1% to >40%; free-living categories are explicitly defined (“free,” “primarily free”). (dewar2024bacteriallifestyleshapes pages 7-8)
- **Free-living vs biofilm experimental response (2023):** 435 DEGs (free-living) vs 219 DEGs (biofilm-associated) under warming; free-living growth rate increased from 0.066 to 0.198 h⁻¹ (25°C → 31°C). (wang2023biofilmformationstabilizes pages 5-7, wang2023biofilmformationstabilizes media fafff1db, wang2023biofilmformationstabilizes media 08581529)
- **Host-associated vs free-living comparative genomics (2024):** symbiotic Fluviibacter genome 1.67 Mb vs 2.29–2.43 Mb free-living; pseudogenes 297 vs 38–69. (wang2024comparativegenomicanalysis pages 5-7)
- **Rhizobial soil-phase persistence and storage (2023):** rhizobia can survive “months or even years” in soil; PHB up to 50% of dry weight; viability of released rhizobia varies widely “from <1% … to almost 100%” depending on host/conditions. (agudelo2023theroleof pages 2-3)
- **Co-inoculation quantitative example (reviewed 2023):** Ni tolerance to 600 mg Ni kg⁻¹ with *Rhizobium* + Ni-tolerant *Bacillus* co-inoculation in faba bean. (goyal2023evaluationoflegume–rhizobial pages 8-10)

## 8) Warnings / “do not yet curate” items

1. **Avoid direct “gene → free-living” edges unless mediated by an interpretable process** (e.g., nutrient acquisition, osmotic stress tolerance, motility). Many genomic signals are correlational across species (e.g., pangenome fluidity, IS abundance) and should be curated as *associations* or as background context rather than strict causal necessities. (dewar2024bacteriallifestyleshapes pages 1-2, dewar2024bacteriallifestyleshapes pages 7-8, hollensteiner2023pangenomeanalysisof pages 11-13)
2. **Biofilm-associated ≠ host-associated** and biofilm is not the negation of free-living; it is often a persistence strategy within the free-living environmental domain. Treat as a separate node/state to prevent ontology conflation. (schaudinn2023francisellatularensissubsp. pages 5-6)
3. **Taxon-specific reversals to free-living** (e.g., diplomonads) are valuable but may involve lineage-specific gene acquisitions; edges derived from such cases should be flagged **uncertain** unless supported across bacteria/archaea broadly. (wisniewska2024expandedgeneand pages 1-3)

---

# DOI-first Bibliography (with URLs and publication dates)

1. Dewar AE, Hao C, Belcher LJ, Ghoul M, West SA. **Bacterial lifestyle shapes pangenomes.** *PNAS* (May 2024). DOI:10.1073/pnas.2320170121. https://doi.org/10.1073/pnas.2320170121 (dewar2024bacteriallifestyleshapes pages 1-2, dewar2024bacteriallifestyleshapes pages 7-8)
2. Jaffe AL, Castelle CJ, Banfield JF. **Habitat transition in the evolution of Bacteria and Archaea.** *Annual Review of Microbiology* (online Sept 2023; preprint Feb 2023). DOI:10.48550/arxiv.2302.00582. https://doi.org/10.48550/arxiv.2302.00582 (jaffe2023habitattransitionin pages 6-8, jaffe2023habitattransitionin pages 8-11, jaffe2023habitattransitionin pages 4-6)
3. Wang M, Lu J, Qin P, et al. **Biofilm formation stabilizes metabolism in a Roseobacteraceae bacterium under temperature increase.** *Applied and Environmental Microbiology* (Oct 2023). DOI:10.1128/aem.00601-23. https://doi.org/10.1128/aem.00601-23 (wang2023biofilmformationstabilizes pages 5-7, wang2023biofilmformationstabilizes pages 2-5, wang2023biofilmformationstabilizes media fafff1db, wang2023biofilmformationstabilizes media 08581529)
4. Hollensteiner J, Schneider D, Poehlein A, Brinkhoff T, Daniel R. **Pan-genome analysis of six Paracoccus type strain genomes reveal lifestyle traits.** *PLOS ONE* (Dec 2023). DOI:10.1371/journal.pone.0287947. https://doi.org/10.1371/journal.pone.0287947 (hollensteiner2023pangenomeanalysisof pages 11-13)
5. Schaudinn C, Rydzewski K, Meister B, Grunow R, Heuner K. **Francisella tularensis subsp. holarctica wild-type is able to colonize natural aquatic ex vivo biofilms.** *Frontiers in Microbiology* (Feb 2023). DOI:10.3389/fmicb.2023.1113412. https://doi.org/10.3389/fmicb.2023.1113412 (schaudinn2023francisellatularensissubsp. pages 5-6)
6. Wang R, Meng Q, Wang X, et al. **Comparative genomic analysis of symbiotic and free-living Fluviibacter phosphoraccumulans strains…** *Applied and Environmental Microbiology* (Feb 2024). DOI:10.1128/aem.01900-23. https://doi.org/10.1128/aem.01900-23 (wang2024comparativegenomicanalysis pages 1-2, wang2024comparativegenomicanalysis pages 5-7)
7. Espada‑Hinojosa S, Karthäuser C, Srivastava A, et al. **Comparative genomics of a vertically transmitted thiotrophic bacterial ectosymbiont and its close free‑living relative.** *Molecular Ecology Resources* (Nov 2024). DOI:10.1111/1755-0998.13889. https://doi.org/10.1111/1755-0998.13889 (espada‐hinojosa2024comparativegenomicsof pages 1-2)
8. Wiśniewska MM, Salomaki ED, Silberman JD, et al. **Expanded gene and taxon sampling of diplomonads shows multiple switches to parasitic and free-living lifestyle.** *BMC Biology* (Sep 2024). DOI:10.1186/s12915-024-02013-w. https://doi.org/10.1186/s12915-024-02013-w (wisniewska2024expandedgeneand pages 1-3)
9. Agudelo MG, Ruiz B, Capela D, Remigi P. **The role of microbial interactions on rhizobial fitness.** *Frontiers in Plant Science* (Oct 2023). DOI:10.3389/fpls.2023.1277262. https://doi.org/10.3389/fpls.2023.1277262 (agudelo2023theroleof pages 2-3, agudelo2023theroleof pages 6-7, agudelo2023theroleof pages 1-2, agudelo2023theroleof pages 10-11)
10. Goyal RK, Habtewold JZ. **Evaluation of legume–rhizobial symbiotic interactions beyond nitrogen fixation…** *Microorganisms* (May 2023). DOI:10.3390/microorganisms11061454. https://doi.org/10.3390/microorganisms11061454 (goyal2023evaluationoflegume–rhizobial pages 10-11, goyal2023evaluationoflegume–rhizobial pages 8-10, goyal2023evaluationoflegume–rhizobial pages 7-8)
11. Grzyb T, Szulc J. **Deciphering molecular mechanisms and diversity of plant holobiont bacteria…** *Int. J. Mol. Sci.* (Dec 2024). DOI:10.3390/ijms252413601. https://doi.org/10.3390/ijms252413601 (grzyb2024decipheringmolecularmechanisms pages 24-25)


References

1. (dewar2024bacteriallifestyleshapes pages 7-8): Anna E. Dewar, Chunhui Hao, Laurence J. Belcher, Melanie Ghoul, and Stuart A. West. Bacterial lifestyle shapes pangenomes. Proceedings of the National Academy of Sciences of the United States of America, May 2024. URL: https://doi.org/10.1073/pnas.2320170121, doi:10.1073/pnas.2320170121. This article has 57 citations and is from a highest quality peer-reviewed journal.

2. (jaffe2023habitattransitionin pages 8-11): Alexander L. Jaffe, Cindy J. Castelle, and Jillian F. Banfield. Habitat transition in the evolution of bacteria and archaea. Annual review of microbiology, Feb 2023. URL: https://doi.org/10.48550/arxiv.2302.00582, doi:10.48550/arxiv.2302.00582. This article has 27 citations and is from a peer-reviewed journal.

3. (jaffe2023habitattransitionin pages 4-6): Alexander L. Jaffe, Cindy J. Castelle, and Jillian F. Banfield. Habitat transition in the evolution of bacteria and archaea. Annual review of microbiology, Feb 2023. URL: https://doi.org/10.48550/arxiv.2302.00582, doi:10.48550/arxiv.2302.00582. This article has 27 citations and is from a peer-reviewed journal.

4. (schaudinn2023francisellatularensissubsp. pages 5-6): Christoph Schaudinn, Kerstin Rydzewski, Beate Meister, Roland Grunow, and Klaus Heuner. Francisella tularensis subsp. holarctica wild-type is able to colonize natural aquatic ex vivo biofilms. Frontiers in Microbiology, Feb 2023. URL: https://doi.org/10.3389/fmicb.2023.1113412, doi:10.3389/fmicb.2023.1113412. This article has 19 citations and is from a peer-reviewed journal.

5. (wisniewska2024expandedgeneand pages 1-3): Monika M. Wiśniewska, Eric D. Salomaki, Jeffrey D. Silberman, Kristina X. Terpis, Eva Mazancová, Petr Táborský, Vasana Jinatham, Eleni Gentekaki, Ivan Čepička, and Martin Kolisko. Expanded gene and taxon sampling of diplomonads shows multiple switches to parasitic and free-living lifestyle. BMC Biology, Sep 2024. URL: https://doi.org/10.1186/s12915-024-02013-w, doi:10.1186/s12915-024-02013-w. This article has 7 citations and is from a domain leading peer-reviewed journal.

6. (espada‐hinojosa2024comparativegenomicsof pages 1-2): Salvador Espada‐Hinojosa, Clarissa Karthäuser, Abhishek Srivastava, Lukas Schuster, Teresa Winter, André Luiz de Oliveira, Frederik Schulz, Matthias Horn, Stefan Sievert, and Monika Bright. Comparative genomics of a vertically transmitted thiotrophic bacterial ectosymbiont and its close free‐living relative. Molecular Ecology Resources, Nov 2024. URL: https://doi.org/10.1111/1755-0998.13889, doi:10.1111/1755-0998.13889. This article has 2 citations and is from a domain leading peer-reviewed journal.

7. (wang2024comparativegenomicanalysis pages 1-2): Ruanlin Wang, Qingyao Meng, Xue Wang, Yu Xiao, Ruijuan Sun, Zhiyun Zhang, Yuejun Fu, Graziano Di Giuseppe, and Aihua Liang. Comparative genomic analysis of symbiotic and free-living fluviibacter phosphoraccumulans strains provides insights into the evolutionary origins of obligate euplotes–bacterial endosymbioses. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01900-23, doi:10.1128/aem.01900-23. This article has 2 citations and is from a peer-reviewed journal.

8. (wang2024comparativegenomicanalysis pages 5-7): Ruanlin Wang, Qingyao Meng, Xue Wang, Yu Xiao, Ruijuan Sun, Zhiyun Zhang, Yuejun Fu, Graziano Di Giuseppe, and Aihua Liang. Comparative genomic analysis of symbiotic and free-living fluviibacter phosphoraccumulans strains provides insights into the evolutionary origins of obligate euplotes–bacterial endosymbioses. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01900-23, doi:10.1128/aem.01900-23. This article has 2 citations and is from a peer-reviewed journal.

9. (wang2023biofilmformationstabilizes pages 5-7): Meng Wang, Jie Lu, Peng Qin, Shuaitao Wang, Wei Ding, Hui-Hui Fu, Yu-Zhong Zhang, and Weipeng Zhang. Biofilm formation stabilizes metabolism in a <i>roseobacteraceae</i> bacterium under temperature increase. Applied and Environmental Microbiology, Oct 2023. URL: https://doi.org/10.1128/aem.00601-23, doi:10.1128/aem.00601-23. This article has 10 citations and is from a peer-reviewed journal.

10. (wang2023biofilmformationstabilizes pages 2-5): Meng Wang, Jie Lu, Peng Qin, Shuaitao Wang, Wei Ding, Hui-Hui Fu, Yu-Zhong Zhang, and Weipeng Zhang. Biofilm formation stabilizes metabolism in a <i>roseobacteraceae</i> bacterium under temperature increase. Applied and Environmental Microbiology, Oct 2023. URL: https://doi.org/10.1128/aem.00601-23, doi:10.1128/aem.00601-23. This article has 10 citations and is from a peer-reviewed journal.

11. (hollensteiner2023pangenomeanalysisof pages 11-13): Jacqueline Hollensteiner, Dominik Schneider, Anja Poehlein, Thorsten Brinkhoff, and Rolf Daniel. Pan-genome analysis of six paracoccus type strain genomes reveal lifestyle traits. PLOS ONE, 18:e0287947, Dec 2023. URL: https://doi.org/10.1371/journal.pone.0287947, doi:10.1371/journal.pone.0287947. This article has 15 citations and is from a peer-reviewed journal.

12. (dewar2024bacteriallifestyleshapes pages 1-2): Anna E. Dewar, Chunhui Hao, Laurence J. Belcher, Melanie Ghoul, and Stuart A. West. Bacterial lifestyle shapes pangenomes. Proceedings of the National Academy of Sciences of the United States of America, May 2024. URL: https://doi.org/10.1073/pnas.2320170121, doi:10.1073/pnas.2320170121. This article has 57 citations and is from a highest quality peer-reviewed journal.

13. (wang2023biofilmformationstabilizes media fafff1db): Meng Wang, Jie Lu, Peng Qin, Shuaitao Wang, Wei Ding, Hui-Hui Fu, Yu-Zhong Zhang, and Weipeng Zhang. Biofilm formation stabilizes metabolism in a <i>roseobacteraceae</i> bacterium under temperature increase. Applied and Environmental Microbiology, Oct 2023. URL: https://doi.org/10.1128/aem.00601-23, doi:10.1128/aem.00601-23. This article has 10 citations and is from a peer-reviewed journal.

14. (wang2023biofilmformationstabilizes media 08581529): Meng Wang, Jie Lu, Peng Qin, Shuaitao Wang, Wei Ding, Hui-Hui Fu, Yu-Zhong Zhang, and Weipeng Zhang. Biofilm formation stabilizes metabolism in a <i>roseobacteraceae</i> bacterium under temperature increase. Applied and Environmental Microbiology, Oct 2023. URL: https://doi.org/10.1128/aem.00601-23, doi:10.1128/aem.00601-23. This article has 10 citations and is from a peer-reviewed journal.

15. (agudelo2023theroleof pages 2-3): Margarita Granada Agudelo, Bryan Ruiz, Delphine Capela, and Philippe Remigi. The role of microbial interactions on rhizobial fitness. Frontiers in Plant Science, Oct 2023. URL: https://doi.org/10.3389/fpls.2023.1277262, doi:10.3389/fpls.2023.1277262. This article has 45 citations.

16. (wang2023biofilmformationstabilizes pages 1-2): Meng Wang, Jie Lu, Peng Qin, Shuaitao Wang, Wei Ding, Hui-Hui Fu, Yu-Zhong Zhang, and Weipeng Zhang. Biofilm formation stabilizes metabolism in a <i>roseobacteraceae</i> bacterium under temperature increase. Applied and Environmental Microbiology, Oct 2023. URL: https://doi.org/10.1128/aem.00601-23, doi:10.1128/aem.00601-23. This article has 10 citations and is from a peer-reviewed journal.

17. (agudelo2023theroleof pages 1-2): Margarita Granada Agudelo, Bryan Ruiz, Delphine Capela, and Philippe Remigi. The role of microbial interactions on rhizobial fitness. Frontiers in Plant Science, Oct 2023. URL: https://doi.org/10.3389/fpls.2023.1277262, doi:10.3389/fpls.2023.1277262. This article has 45 citations.

18. (goyal2023evaluationoflegume–rhizobial pages 8-10): Ravinder K. Goyal and Jemaneh Z. Habtewold. Evaluation of legume–rhizobial symbiotic interactions beyond nitrogen fixation that help the host survival and diversification in hostile environments. Microorganisms, 11:1454, May 2023. URL: https://doi.org/10.3390/microorganisms11061454, doi:10.3390/microorganisms11061454. This article has 71 citations.

19. (agudelo2023theroleof pages 10-11): Margarita Granada Agudelo, Bryan Ruiz, Delphine Capela, and Philippe Remigi. The role of microbial interactions on rhizobial fitness. Frontiers in Plant Science, Oct 2023. URL: https://doi.org/10.3389/fpls.2023.1277262, doi:10.3389/fpls.2023.1277262. This article has 45 citations.

20. (jaffe2023habitattransitionin pages 6-8): Alexander L. Jaffe, Cindy J. Castelle, and Jillian F. Banfield. Habitat transition in the evolution of bacteria and archaea. Annual review of microbiology, Feb 2023. URL: https://doi.org/10.48550/arxiv.2302.00582, doi:10.48550/arxiv.2302.00582. This article has 27 citations and is from a peer-reviewed journal.

21. (agudelo2023theroleof pages 6-7): Margarita Granada Agudelo, Bryan Ruiz, Delphine Capela, and Philippe Remigi. The role of microbial interactions on rhizobial fitness. Frontiers in Plant Science, Oct 2023. URL: https://doi.org/10.3389/fpls.2023.1277262, doi:10.3389/fpls.2023.1277262. This article has 45 citations.

22. (goyal2023evaluationoflegume–rhizobial pages 10-11): Ravinder K. Goyal and Jemaneh Z. Habtewold. Evaluation of legume–rhizobial symbiotic interactions beyond nitrogen fixation that help the host survival and diversification in hostile environments. Microorganisms, 11:1454, May 2023. URL: https://doi.org/10.3390/microorganisms11061454, doi:10.3390/microorganisms11061454. This article has 71 citations.

23. (goyal2023evaluationoflegume–rhizobial pages 7-8): Ravinder K. Goyal and Jemaneh Z. Habtewold. Evaluation of legume–rhizobial symbiotic interactions beyond nitrogen fixation that help the host survival and diversification in hostile environments. Microorganisms, 11:1454, May 2023. URL: https://doi.org/10.3390/microorganisms11061454, doi:10.3390/microorganisms11061454. This article has 71 citations.

24. (grzyb2024decipheringmolecularmechanisms pages 24-25): Tomasz Grzyb and Justyna Szulc. Deciphering molecular mechanisms and diversity of plant holobiont bacteria: microhabitats, community ecology, and nutrient acquisition. International Journal of Molecular Sciences, 25:13601, Dec 2024. URL: https://doi.org/10.3390/ijms252413601, doi:10.3390/ijms252413601. This article has 14 citations.