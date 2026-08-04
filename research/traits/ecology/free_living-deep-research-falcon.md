---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:13:28.754080'
end_time: '2026-08-03T23:24:02.911877'
duration_seconds: 634.16
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
  causal_graph_summary: 'free_living_environmental_habitat: 9 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
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
- **Existing causal graph summary:** free_living_environmental_habitat: 9 nodes, 7 edges

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
- **Existing causal graph summary:** free_living_environmental_habitat: 9 nodes, 7 edges

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


# Curation report: microbial trait **free-living**

**Target:** `traitmech:000048` | **Category:** ECOLOGY | **Term kind:** CLASS | **Definition:** a habitat association in which an organism lives independently in the environment, rather than being obligately associated with a host.

## 1. Scope and current interpretation

For TraitMech, **free-living should be modeled primarily as an organism–habitat association**, not as a single molecular phenotype. The strongest operational evidence is that an organism can maintain itself—and preferably grow or complete repeated generations—in soil, sediment, water, or another non-host environmental matrix without an obligatory host. Environmental occurrence alone is insufficient: DNA, dormant cells, released symbionts, or extracellular stages of obligate parasites can all be detected outside hosts.

The trait is compatible with facultative host association. Rhizobia, for example, alternate between an independent soil phase and a host-associated nodule phase. Accordingly, “free-living” and “capable of symbiosis” are not mutually exclusive organism-level annotations. Habitat transitions also occur over evolutionary time and involve combinations of dispersal, environmental filtering, gene acquisition/loss, and physiological remodeling rather than a universal free-living gene set. Salinity transitions illustrate this multidimensional architecture: implicated adaptations include ion transport, osmotic-stress responses, membrane-lipid changes, osmolyte synthesis, respiratory-chain changes, and broader metabolic remodeling. (jaffe2023habitattransitionin pages 4-6, jaffe2023habitattransitionin pages 6-8)

### Boundary cases

1. **Facultative symbionts:** curate a free-living phase if independent environmental maintenance is demonstrated; retain the host-associated phase as a separate state.
2. **Environmental persistence without growth:** survival, dormancy, spores, or a viable-but-nonculturable state supports environmental persistence, not by itself a free-living lifestyle.
3. **Particle-associated microbes:** attachment to detritus or mineral particles is generally compatible with free living unless the organism depends obligatorily on another living cell.
4. **Predators and parasites of other microbes:** physical occurrence in water or soil does not establish independence if growth requires a cellular host.
5. **Metagenome-only predictions:** genome completeness, biosynthetic pathways, and lack of visible attachment can support an inferred annotation but should not replace cultivation, stable-isotope activity, single-cell observations, or repeated environmental replication.
6. **Auxotrophy:** absence of one biosynthetic pathway does not disqualify free living; environmental cross-feeding is common. Conversely, metabolic completeness does not prove free living.
7. **“Planktonic” versus “sessile”:** these are physical growth states within a free-living phase, not synonyms for free-living versus host-associated.

## 2. Candidate graph nodes

### Trait and ecological-state nodes

- **free-living** — `METPO:traitmech:000048`
- free-living environmental phase — label-only candidate
- host-associated phase — label-only candidate
- motile environmental state — label-only candidate
- sessile environmental state/biofilm — label-only candidate
- independent environmental growth — label-only candidate; recommended operational endpoint
- environmental persistence without demonstrated growth — label-only boundary node

### Environmental factors and habitats

- soil, sediment, freshwater, seawater, and pelagic environment — use appropriate ENVO terms only after selecting the exact habitat represented by each experiment
- salinity and salinity gradient
- low pH/acid stress
- osmotic stress, desiccation, temperature stress
- nutrient limitation; nitrogenous nutrient availability
- oxygen availability and oxidative stress
- spatial separation/dispersal limitation

Environmental filtering and dispersal are central ecological determinants. Habitat contiguity facilitates transitions, whereas the freshwater–marine salinity boundary requires coordinated physiological and genomic adaptation. (jaffe2023habitattransitionin pages 4-6, jaffe2023habitattransitionin pages 6-8)

### Chemicals and metabolites

- cyclic di-GMP — ChEBI grounding should be verified during implementation rather than inferred from the paper text
- sodium ion — `CHEBI:29101`
- ectoine — use a verified ChEBI record during curation
- proline — `CHEBI:17203`
- exopolysaccharide — class-level label unless a chemically defined polymer is specified
- nitrogenous nutrients — broad label; replace with a defined compound where the source permits

### Genes, proteins, and complexes

- **RgsP**, c-di-GMP phosphodiesterase; taxon-specific protein node
- **SMc03178**, predicted/characterized diguanylate cyclase in *Sinorhizobium meliloti*
- **BgsA**, glycosyltransferase implicated in c-di-GMP-dependent exopolysaccharide production
- **McrA**, PilZ-domain c-di-GMP effector regulating motility
- **CuxR**, c-di-GMP-responsive transcription factor
- GGDEF-domain diguanylate cyclases
- EAL/HD-GYP-domain phosphodiesterases
- type IV secretion system (T4SS)
- sodium transporters
- NQR NADH:quinone oxidoreductase
- mechanosensitive channels
- cytochrome-*o* ubiquinol oxidase
- nutrient-uptake transport systems

Protein identifiers should be assigned only after strain-specific sequence resolution. Gene symbols such as **McrA** are ambiguous across taxa and should never be mapped to UniProt by name alone.

### Processes and modules

- c-di-GMP biosynthesis and degradation
- motile-to-sessile transition
- swimming motility
- chemotaxis
- surface attachment and biofilm formation
- exopolysaccharide biosynthesis
- osmoadaptation/osmolyte biosynthesis
- ion homeostasis
- nutrient acquisition
- horizontal gene transfer/genetic exchange
- pangenome diversification
- membrane-lipid remodeling
- respiratory-chain remodeling
- general environmental stress adaptation

## 3. Candidate causal edges

The table below separates direct molecular mechanisms from ecological or comparative-genomic associations. Only the high-confidence, taxon-specific molecular edges should be treated as causal without qualification.

| subject | predicate | object | taxon/context | evidence snippet | DOI/date | evidence class/confidence | curation note |
|---|---|---|---|---|---|---|---|
| salinity gradient / marine habitat | selects for | sodium transporters, osmotic-stress response mechanisms, lipid composition changes, metabolic pathway modifications | free-living bacteria/archaea crossing freshwater–marine barrier | “Salt barrier crossing involves multiple genetic adaptations including ion transporters, osmotic stress response mechanisms, lipid composition changes, and metabolic pathway modifications.” (jaffe2023habitattransitionin pages 4-6) | 10.48550/arxiv.2302.00582 / 2023 | review synthesis; mechanistic but broad; medium confidence | Good environmental-factor edge for habitat filtering; not specific to one gene, so curate as broad process-level node only. |
| lower nutrient availability / freshwater conditions | selects for acquisition of | nutrient uptake systems for nitrogenous compounds | aquatic habitat transition context | “gene acquisition for nutrient uptake systems (nitrogenous compounds in freshwater)” (jaffe2023habitattransitionin pages 6-8) | 10.48550/arxiv.2302.00582 / 2023 | review synthesis; inferred from comparative genomics; medium confidence | Useful environment→function edge; not unique to free-living lifestyle. |
| RgsP phosphodiesterase | degrades | c-di-GMP | *Sinorhizobium meliloti* Rm2011 free-living regulatory network | “RgsP phosphodiesterase degrades c-di-GMP and is essential for cell wall growth localization” (krol2020cyclicdigmpsignaling pages 3-5) | 10.1515/hsz-2020-0232 / 2020 | mechanistic; taxon-specific; high confidence | Strong molecular edge, but only for rhizobial free-living phase regulation, not universal free-living marker. |
| SMc03178 diguanylate cyclase | synthesizes | c-di-GMP | *Sinorhizobium meliloti* Rm2011 | “SMc03178 diguanylate cyclase synthesizes c-di-GMP” (krol2020cyclicdigmpsignaling pages 3-5) | 10.1515/hsz-2020-0232 / 2020 | mechanistic; taxon-specific; high confidence | Strong enzyme→messenger edge. |
| elevated c-di-GMP | promotes | exopolysaccharide biosynthesis via BgsA glycosyltransferase | *Sinorhizobium meliloti* free-living sessile state | “elevated c-di-GMP promotes exopolysaccharide biosynthesis through BgsA glycosyltransferase” (krol2020cyclicdigmpsignaling pages 3-5) | 10.1515/hsz-2020-0232 / 2020 | mechanistic; taxon-specific; high confidence | Candidate edge for motile↔sessile switching relevant to soil persistence. |
| c-di-GMP-bound McrA (PilZ protein) | represses | swimming motility | *Sinorhizobium meliloti* | “McrA PilZ domain protein represses swimming motility in response to c-di-GMP” (krol2020cyclicdigmpsignaling pages 3-5) | 10.1515/hsz-2020-0232 / 2020 | mechanistic; taxon-specific; high confidence | Good protein-mediated motility edge; not a general free-living hallmark. |
| c-di-GMP-null state (c-di-GMP0 strain lacking 16 GGDEF proteins) | causes | attenuated growth under acidic stress | *Sinorhizobium meliloti* environmental adaptation | “A c-di-GMP0 strain lacking 16 GGDEF domain proteins shows attenuated growth under acidic stress” (krol2020cyclicdigmpsignaling pages 3-5) | 10.1515/hsz-2020-0232 / 2020 | causal mutant phenotype; taxon-specific; high confidence | Strong stress-adaptation edge for soil free-living phase; narrow taxonomic scope. |
| elevated c-di-GMP | increases | host association / persistence / biofilm formation | *Pseudomonas lurida*–*Caenorhabditis elegans* experimental evolution | “upregulation of bacterial c-di-GMP causally promotes host-microbe symbiosis establishment… elevated c-di-GMP… consistently increased host association” (obeng2023bacterialcdigmphas pages 1-2) | 10.1038/s41564-023-01468-x / 2023 | experimental causal; high confidence | Negative boundary marker: supports host-associated transition, so should be flagged as not a direct positive mechanism for the free-living trait. |
| free-living lifestyle / more variable environment | is associated with | higher pangenome fluidity and greater opportunity for HGT/gene retention | 126 bacterial species comparative analysis | “pangenome fluidity was significantly lower in host-associated species compared with free-living species” and free-living species “experience more variable environments, providing greater opportunities for horizontal gene transfer and retention of diverse genes” (dewar2024bacteriallifestyleshapes pages 1-2, dewar2024bacteriallifestyleshapes pages 3-5) | 10.1073/pnas.2320170121 / 2024 | comparative/phylogenetic association; medium confidence | Useful high-level ecology→genome-plasticity edge; not direct molecular causation. |
| T4SS genes | enable | genetic exchange / adaptation to dynamic environments | free-living *Paracoccus* genomes | “Free-living genomes share genes linked to genetic exchange via T4SS… enabling adaptation to dynamic environments.” (hollensteiner2023pangenomeanalysisof pages 1-2) | 10.1371/journal.pone.0287947 / 2023 | comparative-genomic association; genus-specific; medium confidence | Candidate genomic-signature edge for free-living *Paracoccus*; should be marked inferred and clade-limited. |


*Table: This table compiles compact, curation-ready candidate causal edges for the microbial trait free-living, emphasizing evidence strength, taxonomic scope, and whether each claim is mechanistic, correlational, or a boundary marker. It is useful for deciding which edges are appropriate for TraitMech curation and which should remain flagged as uncertain or context-specific.*

### Recommended interpretation for YAML construction

A conservative graph should use **independent growth in an environmental habitat** as the terminal phenotype. Molecular mechanisms should connect to intermediate phenotypes such as acid-stress growth, motility, attachment, osmoadaptation, or nutrient acquisition—not directly to `free-living` unless an intervention demonstrates loss or gain of independent environmental growth.

The strongest presently supported mechanistic subgraph is taxon-specific to *S. meliloti*: SMc03178 promotes c-di-GMP synthesis; RgsP promotes c-di-GMP degradation; c-di-GMP signaling acts through effectors including McrA and CuxR; and elevated c-di-GMP promotes exopolysaccharide production while repressing swimming. A strain lacking 16 GGDEF-domain proteins had attenuated growth under acidic stress, linking this regulatory network experimentally to environmental fitness. (krol2020cyclicdigmpsignaling pages 3-5, krol2020cyclicdigmpsignaling pages 1-2)

However, c-di-GMP is not directionally diagnostic of free living. Experimental evolution of *Pseudomonas lurida* with *Caenorhabditis elegans* showed that mutations increasing c-di-GMP, and engineered elevation of c-di-GMP across pseudomonads, increased biofilm formation, host persistence, and host association. Thus, c-di-GMP should be curated as a context-dependent lifestyle-state regulator, not as a universal positive marker of free living. (obeng2023bacterialcdigmphas pages 1-2)

## 4. Recent developments and quantitative evidence

### 4.1 Lifestyle and pangenome structure—2024

Dewar and colleagues compared **126 bacterial species** using phylogenetically informed methods. Pangenome fluidity ranged from **0.012 to 0.41**, with a median of **0.20**, and their model explained approximately **30%** of between-species variation. Host-associated species had lower pangenome fluidity than free-living species. The authors nevertheless cautioned that phylogenetic correlations cannot alone identify molecular causality; variable environments and increased opportunities for horizontal transfer or gene retention remain explanatory mechanisms rather than organism-level diagnostic tests. (dewar2024bacteriallifestyleshapes pages 3-5, dewar2024bacteriallifestyleshapes pages 1-2)

**Curation consequence:** an edge such as `free-living lifestyle — associated_with → higher pangenome fluidity` is supportable. `Free-living lifestyle — causes → HGT` is too strong without a more direct design.

### 4.2 Genomic plasticity in *Paracoccus*—2023

A six-type-strain comparison reported an open *Paracoccus* pangenome containing **13,819 genes**, with a minimal chromosomal core of **8.84%**. Free-living genomes tended to be larger, contain more extrachromosomal elements, genomic islands, and insertion sequences, and share T4SS-linked genetic-exchange genes. These findings suggest adaptation to dynamic environments but are based on a small, genus-specific comparison. (hollensteiner2023pangenomeanalysisof pages 1-2)

**Curation consequence:** retain T4SS/genetic-exchange edges as *Paracoccus*-specific and inferred; do not generalize them to all free-living microorganisms.

### 4.3 Experimental transition toward host association—2023

After experimental evolution with a nematode host, *P. lurida* repeatedly evolved host-specialist phenotypes. Mutations converged on increased c-di-GMP, and targeted elevation of the messenger increased host association in multiple *Pseudomonas* backgrounds. This is especially valuable as a **boundary experiment**: a regulatory system active in environmental motile/sessile switching can also causally drive movement toward host association. (obeng2023bacterialcdigmphas pages 1-2)

### 4.4 Habitat transitions—2023 synthesis

Recent expert synthesis emphasizes that transitions between terrestrial/freshwater and marine habitats require coordinated changes rather than one canonical module. Marine adaptation has been associated with sodium transporters, compatible-solute systems such as ectoine or proline, NQR respiratory complexes, and proteome-level charge shifts; transitions toward lower salinity can involve transporter loss, NQR replacement, and mechanosensitive channels. Acquisition of nutrient-uptake systems, rhodopsin-mediated phototrophy, and oxidative-stress functions can accompany other environmental transitions. (jaffe2023habitattransitionin pages 4-6, jaffe2023habitattransitionin pages 6-8)

These are authoritative process-level hypotheses, but most are lineage- and transition-specific comparative inferences. They should be represented as habitat-adaptation modules below the broad free-living trait, not as obligatory criteria.

## 5. Applications and real-world implementations

1. **Agricultural inoculants.** Rhizobial products must survive manufacturing, storage, soil stress, dispersal, root location, and competition before nodulation. The c-di-GMP-controlled balance among motility, attachment, exopolysaccharide production, and stress tolerance is therefore relevant to strain formulation and field establishment. The evidence currently supports these as rhizobial engineering targets, not universal free-living determinants. (krol2020cyclicdigmpsignaling pages 3-5, krol2020cyclicdigmpsignaling pages 1-2)
2. **Environmental monitoring.** Salinity, nutrient regime, and geography can structure environmental populations; trait annotation can improve interpretation of biogeographic surveys and distinguish habitat filtering from host selection. (jaffe2023habitattransitionin pages 4-6, jaffe2023habitattransitionin pages 6-8)
3. **Bioremediation and wastewater biotechnology.** Environmental independence, substrate uptake at low concentration, stress tolerance, and reversible attachment are practical selection criteria for inoculated strains. These application criteria require direct reactor/field validation and should not be inferred solely from genome content.
4. **Synthetic ecology and minimal cells.** Biosynthetic completeness and transport capabilities help assess whether an engineered organism can grow without host-derived metabolites. Nevertheless, medium dependence and community cross-feeding mean that “autonomous in defined medium” is an assay-specific phenotype rather than proof of environmental free living.
5. **Biosecurity and pathogen ecology.** The causal c-di-GMP result demonstrates that environmental isolates can evolve stronger host association rapidly under selection. Trait graphs should therefore permit state transitions rather than impose a permanent free-living/host-associated dichotomy. (obeng2023bacterialcdigmphas pages 1-2)

## 6. Expert assessment

The literature supports a **distributed-mechanism model**. Free-living organisms must solve nutrient acquisition, energy generation, biosynthesis or environmental metabolite scavenging, stress sensing, homeostasis, dispersal, and survival during resource fluctuation. Which mechanism is necessary depends on the habitat and lineage. Broad comparative patterns—larger accessory gene pools, transport diversity, or metabolic versatility—are useful priors but are neither necessary nor sufficient definitions. The 2024 cross-species pangenome analysis is authoritative evidence that lifestyle predicts genome organization, while explicitly warning against converting every association into a molecular causal edge. (dewar2024bacteriallifestyleshapes pages 3-5, dewar2024bacteriallifestyleshapes pages 1-2)

For TraitMech, the graph should therefore distinguish:

- **definitional edge:** organism `capable_of` independent maintenance/growth in an environmental habitat;
- **environmental-selection edges:** salinity/nutrients/oxygen `select_for` specific adaptation modules;
- **mechanistic fitness edges:** a gene or pathway `promotes` stress growth, nutrient acquisition, motility, or attachment;
- **lifestyle-transition edges:** regulators such as c-di-GMP `modulate` motile, sessile, and host-associated states;
- **comparative associations:** free-living lifestyle `associated_with` pangenome fluidity or genomic plasticity.

## 7. Claims not yet suitable for direct TraitMech curation

- **Do not curate a universal “free-living gene.”** No retrieved evidence supports one.
- **Do not use detection outside a host as proof of independent living.** Released symbionts and dormant or inactive cells are confounders.
- **Do not require complete amino-acid or cofactor biosynthesis.** Environmental free-living taxa may use cross-feeding or high-affinity uptake.
- **Do not equate larger genomes, mobile elements, T4SS, or high pangenome fluidity with the trait.** These are comparative tendencies and can occur in host-associated organisms. (hollensteiner2023pangenomeanalysisof pages 1-2, dewar2024bacteriallifestyleshapes pages 3-5, dewar2024bacteriallifestyleshapes pages 1-2)
- **Do not curate c-di-GMP as simply promoting free living.** Its effects are state- and host-context dependent; experimentally, elevated c-di-GMP can promote host association. (obeng2023bacterialcdigmphas pages 1-2, krol2020cyclicdigmpsignaling pages 3-5)
- **Do not generalize the *S. meliloti* c-di-GMP-null acid-growth phenotype across bacteria.** It is a strong but taxon-specific causal result. (krol2020cyclicdigmpsignaling pages 3-5)
- **Do not represent salinity-adaptation modules as universally necessary.** They apply to particular freshwater–marine transitions. (jaffe2023habitattransitionin pages 4-6)
- **Do not assign UniProt, EC, KEGG, or Rhea identifiers by gene name alone.** Resolve strain, sequence, reaction, and experimental function first.
- **Do not curate review-level “selects for” statements as direct biochemical causation.** Preserve evidence type and uncertainty.

## 8. DOI-first bibliography

1. Dewar AE, Hao C, Belcher LJ, Ghoul M, West SA. **Bacterial lifestyle shapes pangenomes.** *PNAS*. Published May 2024. DOI: [10.1073/pnas.2320170121](https://doi.org/10.1073/pnas.2320170121). (dewar2024bacteriallifestyleshapes pages 3-5, dewar2024bacteriallifestyleshapes pages 1-2)
2. Obeng N et al. **Bacterial c-di-GMP has a key role in establishing host–microbe symbiosis.** *Nature Microbiology*. Published August 2023; 8:1809–1819. DOI: [10.1038/s41564-023-01468-x](https://doi.org/10.1038/s41564-023-01468-x). (obeng2023bacterialcdigmphas pages 1-2)
3. Hollensteiner J et al. **Pan-genome analysis of six Paracoccus type strain genomes reveal lifestyle traits.** *PLOS ONE*. Published December 2023; 18:e0287947. DOI: [10.1371/journal.pone.0287947](https://doi.org/10.1371/journal.pone.0287947). (hollensteiner2023pangenomeanalysisof pages 1-2)
4. Jaffe AL, Castelle CJ, Banfield JF. **Habitat transition in the evolution of bacteria and archaea.** *Annual Review of Microbiology*. 2023. Retrieved manuscript DOI: [10.48550/arXiv.2302.00582](https://doi.org/10.48550/arxiv.2302.00582). Note that the retrieved DOI is the manuscript record and should be replaced by the journal DOI in production metadata if independently verified. (jaffe2023habitattransitionin pages 4-6, jaffe2023habitattransitionin pages 6-8)
5. Krol E, Schäper S, Becker A. **Cyclic di-GMP signaling controlling the free-living lifestyle of alpha-proteobacterial rhizobia.** *Biological Chemistry*. Published November 2020; 401:1335–1348. DOI: [10.1515/hsz-2020-0232](https://doi.org/10.1515/hsz-2020-0232). (krol2020cyclicdigmpsignaling pages 3-5, krol2020cyclicdigmpsignaling pages 1-2)
6. Martiny JBH et al. **Microbial biogeography: putting microorganisms on the map.** *Nature Reviews Microbiology*. Published February 2006; 4:102–112. DOI: [10.1038/nrmicro1341](https://doi.org/10.1038/nrmicro1341). This foundational source supports biogeographic patterning but not a specific molecular causal edge.

## Recommended minimal graph core

The most defensible initial YAML expansion is:

1. `environmental habitat → permits/contains → independent microbial growth`;
2. `independent microbial growth → supports classification as → free-living`;
3. `salinity/nutrient/pH stress → selects for or activates → habitat-specific adaptation module`;
4. for *S. meliloti*, `SMc03178 → synthesizes → c-di-GMP`, `RgsP → degrades → c-di-GMP`, `c-di-GMP–McrA signaling → represses → swimming motility`, and `elevated c-di-GMP → promotes → BgsA-dependent exopolysaccharide biosynthesis`; and
5. `free-living lifestyle → associated_with → elevated pangenome fluidity`, explicitly marked comparative rather than universally causal. (dewar2024bacteriallifestyleshapes pages 3-5, dewar2024bacteriallifestyleshapes pages 1-2, krol2020cyclicdigmpsignaling pages 3-5)

This yields a compact graph that captures the ecological definition while avoiding the unsupported claim that any one stress-response or metabolic module causes the broad free-living trait.

References

1. (jaffe2023habitattransitionin pages 4-6): Alexander L. Jaffe, Cindy J. Castelle, and Jillian F. Banfield. Habitat transition in the evolution of bacteria and archaea. Annual review of microbiology, Feb 2023. URL: https://doi.org/10.48550/arxiv.2302.00582, doi:10.48550/arxiv.2302.00582. This article has 28 citations and is from a peer-reviewed journal.

2. (jaffe2023habitattransitionin pages 6-8): Alexander L. Jaffe, Cindy J. Castelle, and Jillian F. Banfield. Habitat transition in the evolution of bacteria and archaea. Annual review of microbiology, Feb 2023. URL: https://doi.org/10.48550/arxiv.2302.00582, doi:10.48550/arxiv.2302.00582. This article has 28 citations and is from a peer-reviewed journal.

3. (krol2020cyclicdigmpsignaling pages 3-5): Elizaveta Krol, Simon Schäper, and Anke Becker. Cyclic di-gmp signaling controlling the free-living lifestyle of alpha-proteobacterial rhizobia. Biological Chemistry, 401:1335-1348, Nov 2020. URL: https://doi.org/10.1515/hsz-2020-0232, doi:10.1515/hsz-2020-0232. This article has 28 citations and is from a peer-reviewed journal.

4. (obeng2023bacterialcdigmphas pages 1-2): Nancy Obeng, Anna Czerwinski, Daniel Schütz, Jan Michels, Jan Leipert, Florence Bansept, Maria Garcia Garcia, Thekla Schultheiß1†, Melinda Kemlein, Janina Fuß, Arne Traulsen, Holger Sondermann, Andreas Tholey, and Hinrich Schulenburg. Bacterial c-di-gmp has a key role in establishing host–microbe symbiosis. Nature Microbiology, 8:1809-1819, Aug 2023. URL: https://doi.org/10.1038/s41564-023-01468-x, doi:10.1038/s41564-023-01468-x. This article has 60 citations and is from a highest quality peer-reviewed journal.

5. (dewar2024bacteriallifestyleshapes pages 1-2): Anna E. Dewar, Chunhui Hao, Laurence J. Belcher, Melanie Ghoul, and Stuart A. West. Bacterial lifestyle shapes pangenomes. Proceedings of the National Academy of Sciences of the United States of America, May 2024. URL: https://doi.org/10.1073/pnas.2320170121, doi:10.1073/pnas.2320170121. This article has 67 citations and is from a highest quality peer-reviewed journal.

6. (dewar2024bacteriallifestyleshapes pages 3-5): Anna E. Dewar, Chunhui Hao, Laurence J. Belcher, Melanie Ghoul, and Stuart A. West. Bacterial lifestyle shapes pangenomes. Proceedings of the National Academy of Sciences of the United States of America, May 2024. URL: https://doi.org/10.1073/pnas.2320170121, doi:10.1073/pnas.2320170121. This article has 67 citations and is from a highest quality peer-reviewed journal.

7. (hollensteiner2023pangenomeanalysisof pages 1-2): Jacqueline Hollensteiner, Dominik Schneider, Anja Poehlein, Thorsten Brinkhoff, and Rolf Daniel. Pan-genome analysis of six paracoccus type strain genomes reveal lifestyle traits. PLOS ONE, 18:e0287947, Dec 2023. URL: https://doi.org/10.1371/journal.pone.0287947, doi:10.1371/journal.pone.0287947. This article has 17 citations and is from a peer-reviewed journal.

8. (krol2020cyclicdigmpsignaling pages 1-2): Elizaveta Krol, Simon Schäper, and Anke Becker. Cyclic di-gmp signaling controlling the free-living lifestyle of alpha-proteobacterial rhizobia. Biological Chemistry, 401:1335-1348, Nov 2020. URL: https://doi.org/10.1515/hsz-2020-0232, doi:10.1515/hsz-2020-0232. This article has 28 citations and is from a peer-reviewed journal.