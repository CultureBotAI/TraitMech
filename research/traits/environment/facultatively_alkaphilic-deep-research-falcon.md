---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:04:03.635980'
end_time: '2026-06-17T22:33:27.632864'
duration_seconds: 1764.0
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: facultatively alkaphilic
  trait_identifier: METPO:1003005
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: facultatively_alkaphilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference in which an organism can grow at alkaline pH
    but does not require it.
  parent_traits: METPO:1003000
  synonyms: facultative alkaliphile, facultative alkaphilic, facultatively alkaliphilic
  evidence_summary: 'DOI:10.3389/fbioe.2015.00075: capable of growing near neutral
    pH (Supports facultative alkaliphiles as alkaline-growing organisms that also
    grow near neutral pH.)'
  causal_graph_summary: 'facultatively_alkaphilic_sodium_cycle_homeostasis: 7 nodes,
    6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 57
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultatively alkaphilic
- **METPO identifier:** METPO:1003005
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism can grow at alkaline pH but does not require it.
- **Parent traits:** METPO:1003000
- **Synonyms:** facultative alkaliphile, facultative alkaphilic, facultatively alkaliphilic
- **Existing evidence:** DOI:10.3389/fbioe.2015.00075: capable of growing near neutral pH (Supports facultative alkaliphiles as alkaline-growing organisms that also grow near neutral pH.)
- **Existing causal graph summary:** facultatively_alkaphilic_sodium_cycle_homeostasis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **facultatively alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_alkaphilic.yaml`.

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
- **Trait label:** facultatively alkaphilic
- **METPO identifier:** METPO:1003005
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism can grow at alkaline pH but does not require it.
- **Parent traits:** METPO:1003000
- **Synonyms:** facultative alkaliphile, facultative alkaphilic, facultatively alkaliphilic
- **Existing evidence:** DOI:10.3389/fbioe.2015.00075: capable of growing near neutral pH (Supports facultative alkaliphiles as alkaline-growing organisms that also grow near neutral pH.)
- **Existing causal graph summary:** facultatively_alkaphilic_sodium_cycle_homeostasis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **facultatively alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_alkaphilic.yaml`.

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


## Curation-focused research report: **facultatively alkaphilic** (METPO:1003005)

### 1) Scope summary (trait meaning, boundaries, assay context)

**Trait definition (target):** *facultatively alkaphilic* denotes a pH growth preference in which an organism **can grow at alkaline pH but does not require it**, i.e., it also grows near neutral pH (as in the template definition). Operationally, cultivation-focused sources distinguish **facultative alkaliphiles** from obligate alkaliphiles by the **lower pH limit for growth**: facultative alkaliphiles have a lower limit *slightly below pH 7 (not less than ~pH 6.0)*, whereas “obligate” alkaliphiles are often defined as growing starting from ~pH 7 to 12 (or not growing at pH 7 or lower, depending on scheme). (kevbrin2019isolationandcultivation pages 1-4)

**Nearby traits / boundary cases to curate carefully:**
- **Obligate alkaliphiles**: growth optima typically at high pH and poor/no growth near neutral pH; contrasts are explicitly drawn against facultative alkaliphiles in cultivation-focused definitions. (kevbrin2019isolationandcultivation pages 1-4, horikoshi2016alkaliphiles pages 2-5)
- **Alkalitolerant/neutralophiles**: organisms with optimum near ~pH 7 (or slightly lower) but with upper growth limits extending to ~pH 8.0–8.5; these are not “true alkaliphiles” in stricter schemes. (kevbrin2019isolationandcultivation pages 1-4)

**Assay considerations for TraitMech curation:**
- Trait assignment depends on **reported growth ranges and optima** (liquid culture with controlled pH, buffered carbonate systems, etc.). The mechanistic literature frequently uses *Bacillus/Alkalihalobacillus* models, and some mechanistic edges may be **taxon-weighted** rather than universal.

### 2) Current mechanistic understanding (key concepts/definitions)

A unifying problem for alkaliphilic growth is that at high external pH the **available proton concentration is extremely low**, yet many alkaliphiles (including strains spanning neutral-to-alkaline pH) still use **proton-coupled F1Fo-ATP synthases** and must keep cytosolic processes functional by maintaining a **cytoplasmic pH substantially below external pH**. (preiss2015alkaliphilicbacteriawith pages 2-3, kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91)

#### 2.1 Cytoplasmic pH homeostasis as the core phenotype
Quantitative physiology shows that alkaliphilic Bacillus can maintain a relatively low intracellular pH even at external pH 10:
- When external pH was 10, intracellular pH was **~8.1** in *Bacillus clarkii* DSM 8720T and in *B. cohnii* YN-2000 (noted as a facultative alkaliphile exemplar in that study). (matsuno2018formationofproton pages 4-5)
- *B. pseudofirmus* OF4 can maintain cytoplasmic pH **≤8.3 at external pH 10.8** and has an upper growth limit near **pH 11.4**, illustrating “inverted ΔpH” (inside more acidic than outside). (preiss2015alkaliphilicbacteriawith pages 4-5)

#### 2.2 Ion cycling and Na+-dependent homeostasis
Many alkaliphiles show **Na+ dependence**, and Na+-coupled systems are central to maintaining cytoplasmic pH and energizing transport:
- A key theme is that **Na+/H+ antiport** can maintain cytoplasmic pH **~2–2.3 units below the external pH**, and viability at high pH can collapse in the absence of Na+. (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91)
- In *Bacillus firmus* RAB at external pH 10.5, **absence of Na+** led to cytoplasmic pH rising to **10.5** and rapid loss of viability, whereas **presence of Na+** restored viability and kept internal pH **<9.0**—strong functional evidence that Na+-coupled antiport is causal for alkaline resistance. (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91)

#### 2.3 Mrp (mrpABCDEFG) multi-subunit Na+/H+ antiporter as a canonical alkaliphily module
A central, repeatedly supported mechanism in Bacillaceae is **electrogenic monovalent cation/proton antiport** mediated by Mrp:
- Mechanistic definition: an “electrogenic exchange” of outward Na+ (sometimes K+) for a greater number of incoming protons supports pH homeostasis at high pH. (preiss2015alkaliphilicbacteriawith pages 3-4)
- The Mrp complex is described as **multi-subunit (often 7 hydrophobic gene products; mrpABCDEFG)** and “plays an essential role… in support of alkaliphily.” (preiss2015alkaliphilicbacteriawith pages 3-4)

A key schematic integrates Mrp with sodium influx routes, pH homeostasis, and ATP synthesis in *B. pseudofirmus* OF4; it explicitly depicts external pH ~10.5 with cytoplasmic pH ~8.3, Na+ influx through multiple channels/symporters, and Na+ efflux via Mrp coupled to H+ influx—useful for causal graph structure. (preiss2015alkaliphilicbacteriawith media 930cd9d4)

#### 2.4 NhaC-family monovalent cation/H+ antiporters as portable alkali-resistance modules (2023–2024 priority)
A 2023 experimental study provides direct gene-to-phenotype evidence for NhaC-family antiporters:
- Heterologous expression of **nhaC1 or nhaC2** in antiporter-deficient *E. coli* KNabc increased alkaline resistance: KNabc/nhaC1 grew up to **pH 8.5**, KNabc/nhaC2 up to **pH 9.5**. (wang2023characterizationoftwo pages 7-8)
- Antiport activity was measured as **pH-dependent across pH 7.0–10.0**, with optimal pH reported near **9.5**. (wang2023characterizationoftwo pages 7-8)

These results support a causal edge from **NhaC antiporter activity → alkaline pH resistance/homeostasis**, albeit with curation notes (archaeal donor, *E. coli* assay system). (wang2023characterizationoftwo pages 7-8, wang2023characterizationoftwo pages 10-12)

#### 2.5 Cell envelope acidity and buffering: teichuronic acid/teichuronopeptide and surface layers
Cell-wall and surface polymers provide a second major mechanistic axis:
- In a facultative alkaliphile model strain context (C-125 lineage), acidic cell-wall polymers (teichuronic acids, teichuronopeptides) are described as buffering/acidifying the cell surface; mutants unable to make teichuronopeptide show high-pH sensitivity, with restoration by tupA. (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91)
- Broader alkaliphile physiology emphasizes acidic non-peptidoglycan polymers and cell wall contributions to keeping the cell surface and cytoplasm at lower pH than the bulk medium; protoplast instability at high pH underscores this dependency. (horikoshi2016alkaliphiles pages 2-5)

#### 2.6 Bioenergetic adaptations: high ΔΨ and Donnan effects
Quantitative bioenergetics show alkaliphiles can sustain high membrane potentials and ATP production under alkaline conditions:
- Membrane potential: **−192 mV** in *B. clarkii* at pH 10 vs **−122 mV** in *B. subtilis* at pH 7. (matsuno2018formationofproton pages 4-5)
- ATP production: *B. clarkii* DSM 8720T produced **7.2 nmol ATP·mg protein−1·min−1** at pH 10; *B. pseudofirmus* OF4 ~**6.6 ± 3.9** at pH 10.5; neutralophilic *B. subtilis* **0.96** at pH 7. (matsuno2018formationofproton pages 4-5)
- Intracellular negative ion capacity: alkaliphiles showed much higher values (e.g., 2.9–3.3×10^6 eq·mg protein−1) than *B. subtilis* (0.7×10^6), supporting Donnan-effect hypotheses for generating high ΔΨ. (matsuno2018formationofproton pages 4-5)

### 3) Recent developments (prioritize 2023–2024)

#### 3.1 2023: antiporter functional characterization and complementation
The 2023 NhaC study supplies a relatively *portable* mechanistic module: NhaC antiporters confer alkaline tolerance in a defined genetic background, and transport is pH-dependent over the neutral-to-alkaline interval. (wang2023characterizationoftwo pages 7-8, wang2023characterizationoftwo pages 10-12)

#### 3.2 2024: proteomics reveals environmental modulation of Mrp usage
A 2024 quantitative proteomics study in the thermoalkaliphile *Caldalkalibacillus thermarum* TA2.A1 found that the **Mrp complex is downregulated under lower dissolved oxygen levels** and proposed that a **sodium:acetate exporter** could reduce reliance on Mrp under strong oxygen limitation. This identifies **oxygen availability as an experimental/environmental factor** that modulates the Na+/H+ antiport module in at least one alkaliphile. (jong2024quantitativeproteomicsreveals pages 1-2)

#### 3.3 2024: comparative genomics links mrpABCDEFG to alkali resistance/halotolerance and habitat transitions
A 2024 genomics study reported that halotolerant, alkali-resistant *Aquibium* species and a non-N2-fixing *Mesorhizobium* lineage possess mrpABCDEFG, while N2-fixing soil-adapted *Mesorhizobium* lack these genes, interpreted as loss of saline/alkaline adaptation functions during habitat change. This supports **mrpABCDEFG as an ecologically selected alkali-resistance module**, although causality is correlative at the comparative-genomics level. (kim2024lineagespecificevolutionof pages 1-2)

### 4) Current applications / real-world implementations (with quantitative benchmarks)

**Industrial enzymes (detergents, pulp/paper, cyclodextrins):**
- Detergents are a major implementation area: detergent enzymes are reported to represent **~30% of global enzyme production**, and alkaline proteases from *Bacillus* spp. are produced commercially for detergents. (horikoshi2016alkaliphiles pages 6-8)
- **Cyclodextrin production** enabled by alkaliphilic CGTases has quantitative process benchmarks: yields of **85–90% from amylose** and **70–80% from potato starch**, and reported reduction of β‑cyclodextrin cost from **199,000 yen to 1,000 yen/kg** (enabling large-scale applications). (horikoshi2016alkaliphiles pages 8-9)
- Pulp/paper: xylanases from alkaliphiles have been applied to debleaching; one report cited **~70% xylan hydrolysis after 24 h** in wood pulp contexts. (horikoshi2016alkaliphiles pages 9-11)
- Industrial-scale enzyme production benchmark: alkaliphilic cellulases were produced at **30 g/L** by overexpression in *Bacillus subtilis* (as a production host). (horikoshi2016alkaliphiles pages 9-11)

**Bioprocess/engineering implementations at high pH:**
- A review notes multiple applications including lab-scale sulfide-removing bioreactors using *Thioalkalivibrio*, microbial fuel cells using alkaliphiles (e.g., *Pseudomonas alcaliphila*), and uses in indigo dye production and metal-contaminated alkaline environments (e.g., *Alkaliphilus metalliredigens*). (preiss2015alkaliphilicbacteriawith pages 2-3)

### 5) Candidate causal-graph nodes and edges for TraitMech curation

The following artifacts are designed for direct use when drafting `data/traits/environment/facultatively_alkaphilic.yaml`.

**Candidate nodes (grouped by type, with grounding suggestions):**
| Node label | Node type | Suggested ontology CURIE(s) if known | Evidence/supporting source(s) (DOI/year) | Notes |
|---|---|---|---|---|
| alkaline external pH | environmental factor | ENVO:01000311 (alkaline water, approximate), label-only for alkaline growth condition | 10.1007/10_2018_84 (2019); 10.3389/fbioe.2015.00075 (2015) (kevbrin2019isolationandcultivation pages 1-4, preiss2015alkaliphilicbacteriawith pages 3-4) | Core environmental context for trait; exact ENVO term for assay condition may need review. |
| sodium availability | environmental factor | CHEBI:29101 | 10.1007/978-981-19-1573-4_3 (2022); 10.1007/978-4-431-55408-0_4 (2021) (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91, horikoshi2016alkaliphiles pages 2-5) | Strong physiological support; many alkaliphiles show Na+-dependence, but strength varies by taxon. |
| low oxygen availability | environmental factor | label-only | 10.3389/fmicb.2024.1468929 (2024) (jong2024quantitativeproteomicsreveals pages 1-2) | Relevant modifier of Mrp abundance in one thermoalkaliphile; not trait-defining. |
| Na+/H+ antiport | process | GO:0015385 (sodium:proton antiporter activity) | 10.3389/fbioe.2015.00075 (2015); 10.1007/978-981-19-1573-4_3 (2022) (preiss2015alkaliphilicbacteriawith pages 3-4, kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91) | Central mechanism for alkaline pH homeostasis. |
| K+/H+ antiport | process | label-only | 10.3389/fbioe.2015.00075 (2015); 10.1007/978-981-19-1573-4_3 (2022) (preiss2015alkaliphilicbacteriawith pages 3-4, kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91) | Mentioned as alternative/complementary monovalent cation antiport; grounding may require more specific transporter terms. |
| sodium motive force | process | label-only | 10.1007/978-981-19-1573-4_3 (2022); 10.3389/fmicb.2025.1637315 (2025) (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91, yumoto2025h+capacitorandatp pages 2-3) | Widely used mechanistic concept; no obvious standard GO/ENVO node. |
| proton motive force | process | GO:1902600 (proton motive force-driven ATP synthesis, related), label-only for PMF | 10.3389/fmicb.2018.02331 (2018); 10.3389/fbioe.2015.00075 (2015) (matsuno2018formationofproton pages 1-2, preiss2015alkaliphilicbacteriawith pages 2-3) | Important bioenergetic intermediate; exact grounding may need curator choice. |
| cytoplasmic pH homeostasis | process | GO:0006885 | 10.1007/978-981-19-1573-4_3 (2022); 10.3389/fmicb.2018.02331 (2018) (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91, matsuno2018formationofproton pages 4-5) | Strong candidate process node directly tied to phenotype. |
| teichuronic acid | metabolite/ion | label-only | 10.1007/978-981-19-1573-4_3 (2022) (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91) | Acidic cell-wall polymer reported for facultative alkaliphilic strain C-125; grounding unclear. |
| teichuronopeptide | metabolite/ion | label-only | 10.1007/978-981-19-1573-4_3 (2022) (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91) | Strongly tied to alkaline sensitivity mutants; taxon-specific. |
| secondary cell wall polymers (SCWP) | cellular component | label-only | 10.3389/fbioe.2015.00075 (2015) (preiss2015alkaliphilicbacteriawith media 930cd9d4) | Figure-level support in B. pseudofirmus OF4 schematic; good component node though exact ontology unresolved. |
| S-layer / acidic secondary cell-wall components | cellular component | GO:0030111 (regulation of cell surface receptor signaling pathway, not suitable), label-only | 10.3389/fmicb.2018.02331 (2018); 10.3389/fmicb.2022.842785 (2022) (matsuno2018formationofproton pages 1-2, goto2022differencesinbioenergetic pages 1-2) | Better kept as label-only candidate until precise component grounding is chosen. |
| membrane potential (ΔΨ) | process | GO:0098800 (inner mitochondrial membrane potential, not suitable), label-only | 10.3389/fmicb.2018.02331 (2018); 10.3389/fmicb.2022.842785 (2022) (matsuno2018formationofproton pages 4-5, goto2022differencesinbioenergetic pages 1-2) | Quantitatively supported but ontology grounding for bacterial transmembrane electrical potential may need custom choice. |
| Donnan effect / intracellular negative ion capacity | process | label-only | 10.3389/fmicb.2018.02331 (2018) (matsuno2018formationofproton pages 4-5, matsuno2018formationofproton pages 1-2) | Mechanistic hypothesis/process-level node; not a standard ontology term. |
| F1Fo-ATP synthase | gene/protein/complex | GO:0046933 | 10.3389/fbioe.2015.00075 (2015); 10.3389/fmicb.2018.02331 (2018) (preiss2015alkaliphilicbacteriawith pages 2-3, matsuno2018formationofproton pages 1-2) | Strong, broadly conserved energy-conversion complex. |
| Mrp Na+/H+ antiporter complex (mrpABCDEFG) | gene/protein/complex | label-only | 10.3389/fbioe.2015.00075 (2015); 10.1128/aem.02091-23 (2024); 10.3389/fmicb.2024.1468929 (2024) (preiss2015alkaliphilicbacteriawith pages 3-4, kim2024lineagespecificevolutionof pages 1-2, jong2024quantitativeproteomicsreveals pages 1-2) | Best-supported transporter complex; exact stable complex identifier not established here. |
| NhaC-family Na+(K+,Li+)/H+ antiporter | gene/protein/complex | label-only | 10.3390/ijms241310786 (2023); 10.1128/aem.00145-24 (2024) (wang2023characterizationoftwo pages 7-8, xing2024thepolyextremophilenatranaerobius pages 19-21) | Strong transporter candidate from 2023–2024 studies; family-level node preferable. |
| MotPS sodium channel | gene/protein/complex | label-only | 10.3389/fbioe.2015.00075 (2015) (preiss2015alkaliphilicbacteriawith pages 4-5, preiss2015alkaliphilicbacteriawith media 930cd9d4) | Included in Na+ cycle schematic; support strongest in Bacillus models. |
| Na+/solute symporter | gene/protein/complex | label-only | 10.3389/fbioe.2015.00075 (2015); 10.1128/aem.00145-24 (2024) (preiss2015alkaliphilicbacteriawith media 930cd9d4, xing2024thepolyextremophilenatranaerobius pages 19-21) | Important for Na+ influx coupled to transport; family identity unresolved. |
| sodium:acetate exporter | gene/protein/complex | label-only | 10.3389/fmicb.2024.1468929 (2024) (jong2024quantitativeproteomicsreveals pages 1-2) | Explicitly hypothetical compensatory mechanism under low O2; curate cautiously. |
| glycine betaine | metabolite/ion | CHEBI:17750 | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 19-21) | Supported in polyextremophile salinity adaptation; indirect relevance to facultative alkaliphily. |
| proline | metabolite/ion | CHEBI:17203 | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 19-21) | Compatible solute / amino acid accumulating under salt stress; relevance to pH adaptation is supportive but not direct. |
| glutamate | metabolite/ion | CHEBI:18237 | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 19-21) | Same caution as proline; useful if graph includes polyextremophile overlap nodes. |
| spermidine | metabolite/ion | CHEBI:15729 | 10.1007/978-981-19-1573-4_3 (2022) (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91) | Reported as a major polyamine at pH 10; plausible membrane-stabilizing node. |
| cytochrome c outer-surface network / H+ capacitor | gene/protein/complex | label-only | 10.3389/fmicb.2018.02331 (2018); 10.3389/fmicb.2022.842785 (2022) (matsuno2018formationofproton pages 1-2, goto2022differencesinbioenergetic pages 1-2) | Mechanistically interesting but still partly model-based; strongest evidence in obligate alkaliphilic Bacillaceae. |
| Bacillus/Alkalihalobacillus pseudofirmus OF4 | cellular component | NCBITaxon:1073221 | 10.3389/fbioe.2015.00075 (2015) (preiss2015alkaliphilicbacteriawith pages 4-5, preiss2015alkaliphilicbacteriawith media 930cd9d4) | Useful exemplar taxon for broad pH-range facultative alkaliphily; taxon node optional in trait graph. |
| Bacillus cohnii / Shouchella cohnii YN-2000 | cellular component | label-only | 10.3389/fmicb.2018.02331 (2018) (matsuno2018formationofproton pages 4-5) | Facultative alkaliphile exemplar with intracellular pH data; taxonomy/identifier should be checked before curation. |


*Table: This table lists candidate causal graph nodes for facultatively alkaphilic growth, grouped by type and annotated with suggested ontology grounding, evidence sources, and curation cautions. It is designed to help prioritize which nodes are mature enough for TraitMech entry versus those that remain taxon-specific or hypothetical.*

**Candidate causal edges (triples with evidence snippets and curation notes):**
| Subject node | Predicate | Object node | Mechanism / interpretation | Evidence snippet | Reference (DOI, year, URL) | Confidence | Notes for curation |
|---|---|---|---|---|---|---|---|
| facultatively alkaphilic growth phenotype [METPO:1003005] | has lower growth limit near | near-neutral pH growth [label-only] | Trait scope: facultative alkaliphiles grow at alkaline pH but also at/near neutral pH, unlike obligate alkaliphiles | “those where the lower limit for growth is slightly less than 7 (not less than 6.0) as facultative alkaliphiles” | 10.1007/10_2018_84, 2019, https://doi.org/10.1007/10_2018_84 | High | Definition edge; phenotype-level, not mechanism. Distinguish from obligate alkaliphile and alkalitolerant organisms. (kevbrin2019isolationandcultivation pages 1-4) |
| alkaline external pH [CHEBI:3311 for H+ context; label-only for condition] | selects for | electrogenic Na+/H+ antiport [GO:0015385 candidate / label-only] | Core adaptation: exchange of outgoing Na+ for a greater number of incoming H+ supports alkaline growth by acidifying cytoplasm | “electrogenic exchange of outwardly moving sodium ions… for a greater number of entering protons” | 10.3389/fbioe.2015.00075, 2015, https://doi.org/10.3389/fbioe.2015.00075 | High | Broadly supported for alkaliphilic Bacillus; likely transferable to facultative alkaliphiles with caution. (preiss2015alkaliphilicbacteriawith pages 3-4) |
| Mrp Na+/H+ antiporter complex [mrpABCDEFG; GO:0015385 candidate / label-only] | enables | alkaliphily / alkaline growth [label-only] | Multi-subunit Mrp is described as essential for electrogenic antiport supporting growth at high pH | “plays an essential role in catalyzing the electrogenic antiport in support of alkaliphily” | 10.3389/fbioe.2015.00075, 2015, https://doi.org/10.3389/fbioe.2015.00075 | High | Strong mechanistic edge, but evidence comes mainly from Bacillus spp.; curate as taxon-weighted if attached to specific clades. (preiss2015alkaliphilicbacteriawith pages 3-4) |
| Mrp Na+/H+ antiporter complex [mrpABCDEFG] | exports | sodium ion [CHEBI:29101] | Mrp contributes to Na+ cycle by exchanging intracellular Na+ for extracellular H+ | “exchange of outward Na+… for uptake of more H+” | 10.3389/fbioe.2015.00075, 2015, https://doi.org/10.3389/fbioe.2015.00075 | High | Mechanistic decomposition of Mrp function. (preiss2015alkaliphilicbacteriawith pages 3-4) |
| Mrp Na+/H+ antiporter complex [mrpABCDEFG] | imports | proton [CHEBI:15378] | Proton capture from alkaline exterior helps maintain lower intracellular pH | “exchange of outward Na+… for uptake of more H+” | 10.3389/fbioe.2015.00075, 2015, https://doi.org/10.3389/fbioe.2015.00075 | High | Same evidence as above; may be modeled as a transport process node instead of direct edge. (preiss2015alkaliphilicbacteriawith pages 3-4) |
| Na+/H+ antiport activity [GO:0015385 candidate / label-only] | maintains | cytoplasmic pH homeostasis [GO:0006885 candidate / label-only] | Antiport can keep cytoplasm substantially below external pH under alkaline conditions | “maintain cytoplasmic pH 2–2.3 units below the external pH” | 10.1007/978-981-19-1573-4_3, 2022, https://doi.org/10.1007/978-981-19-1573-4_3 | High | Useful generic edge for causal graph. Check GO grounding during curation. (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91) |
| sodium ion availability [CHEBI:29101] | positively_regulates | viability at high pH [label-only] | Na+ is required for antiport-driven homeostasis in many alkaliphiles | “without Na+, internal pH rose to 10.5… with Na+ internal pH stayed below 9.0” | 10.1007/978-981-19-1573-4_3, 2022, https://doi.org/10.1007/978-981-19-1573-4_3 | High | Strong physiology evidence, but example is Bacillus firmus RAB at pH 10.5; taxon- and assay-specific. (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91) |
| sodium ion availability [CHEBI:29101] | enables | cytoplasmic pH below 9 at external pH 10.5 [label-only] | Direct quantitative support for Na+-dependent pH homeostasis | “with Na+ internal pH stayed below 9.0” | 10.1007/978-981-19-1573-4_3, 2022, https://doi.org/10.1007/978-981-19-1573-4_3 | High | Quantitative edge from specific Bacillus assay. (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91) |
| acidic cell-wall polymers (teichuronic acid / teichuronopeptide) [label-only] | buffer / acidify | cell surface microenvironment [label-only] | Negatively charged wall polymers help maintain lower pH at cell surface and protect membrane/cytoplasm | “synthesize anionic cell-wall acidic polymers (teichuronic acids, teichuronopeptides) that help buffer the cell surface” | 10.1007/978-981-19-1573-4_3, 2022, https://doi.org/10.1007/978-981-19-1573-4_3 | High | Particularly associated with facultative alkaliphilic strain C-125; good trait-linked candidate. (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91) |
| teichuronopeptide biosynthesis [label-only] | positively_regulates | alkaline pH tolerance [label-only] | Loss of wall acidic polymer production causes alkali sensitivity | “mutants unable to make teichuronopeptide show sensitivity to high pH” | 10.1007/978-981-19-1573-4_3, 2022, https://doi.org/10.1007/978-981-19-1573-4_3 | High | Strong but strain-specific (B. halodurans/C-125 lineage context). (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91) |
| tupA [label-only gene] | positively_regulates | teichuronopeptide production [label-only] | Genetic rescue supports causal role of wall polymer pathway in alkaline adaptation | “restoration by the tupA gene” | 10.1007/978-981-19-1573-4_3, 2022, https://doi.org/10.1007/978-981-19-1573-4_3 | Med | Gene grounding unresolved from provided context; curate cautiously. (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91) |
| alkaline external pH (pH 10) [label-only] | results_in | intracellular pH ~8.1 [label-only] | Facultative/alkaliphilic Bacillus can maintain cytoplasm well below medium pH | “when extracellular pH was 10 the intercellular pH of B. clarkii… and B. cohnii YN-2000 was 8.1” | 10.3389/fmicb.2018.02331, 2018, https://doi.org/10.3389/fmicb.2018.02331 | High | Includes facultative alkaliphile B. cohnii YN-2000; very relevant quantitative phenotype edge. (matsuno2018formationofproton pages 4-5) |
| high intracellular negative ion capacity [label-only] | contributes_to | high membrane electrical potential (ΔΨ) [label-only] | Donnan effect hypothesis: internal impermeant negative charge helps generate large ΔΨ at high pH | “likely contributes to the formation of the high ΔΨ because the intracellular negative ion capacities of alkaliphiles are much higher” | 10.3389/fmicb.2018.02331, 2018, https://doi.org/10.3389/fmicb.2018.02331 | Med | Mechanistic inference/hypothesis, not a single-gene edge. (matsuno2018formationofproton pages 1-2, matsuno2018formationofproton pages 4-5) |
| high membrane electrical potential (ΔΨ) [label-only] | increases | ATP synthase driving force [label-only] | Elevated ΔΨ enhances effective proton motive force per proton in H+-poor alkaline environments | “high membrane electrical potential (ΔΨ)… increases the driving force per H+ for F1Fo-ATPase” | 10.3389/fmicb.2018.02331, 2018, https://doi.org/10.3389/fmicb.2018.02331 | Med | Mechanistic but somewhat model-based; best as process-level edge. (matsuno2018formationofproton pages 1-2) |
| F1Fo-ATP synthase [GO:0046933 candidate / label-only] | supports | ATP production at alkaline pH [GO:0006754 candidate / label-only] | Alkaliphiles still use proton-coupled ATP synthase despite low bulk PMF | “alkaliphilic aerobes often use proton-coupled ATP synthases despite an apparently low bulk proton-motive force” | 10.3389/fbioe.2015.00075, 2015, https://doi.org/10.3389/fbioe.2015.00075 | High | Good general edge; not unique to facultative alkaliphiles. (preiss2015alkaliphilicbacteriawith pages 2-3) |
| Na+ cycle [label-only] | conserves | protons for ATP synthesis [CHEBI:15378 / label-only process] | Respiration-generated proton motive energy is translated into sodium motive force, sparing scarce protons for ATP synthase | “translated by Na+/H+ antiporters… into a transmembrane Na+ potential… reserving scarce protons primarily for driving F1F0-ATP synthase” | 10.3389/fmicb.2025.1637315, 2025, https://doi.org/10.3389/fmicb.2025.1637315 | Med | 2025 review; mechanistically valuable but not within 2023–2024 priority and focused on obligates. (yumoto2025h+capacitorandatp pages 2-3) |
| NhaC-family Na+(K+,Li+)/H+ antiporter [label-only; GO:0015385 candidate] | confers | growth at alkaline pH [label-only] | Heterologous complementation directly links antiporter to alkali resistance | “KNabc/nhaC1 can grow at pH 8.5, while nhaC2 confers higher resistance up to pH 9.5” | 10.3390/ijms241310786, 2023, https://doi.org/10.3390/ijms241310786 | High | Strong experimental evidence, but archaeal donor / E. coli assay system. (wang2023characterizationoftwo pages 7-8) |
| NhaC1 [label-only] | has_activity_range | pH 7.0–10.0 [label-only] | Antiport activity is pH dependent over alkaline range | “antiport activities… are both pH-dependent in the range of pH 7.0–10.0” | 10.3390/ijms241310786, 2023, https://doi.org/10.3390/ijms241310786 | High | Good transport-property edge; assay in everted membrane vesicles. (wang2023characterizationoftwo pages 7-8) |
| NhaC2 [label-only] | has_optimal_activity_at | pH 9.5 [label-only] | NhaC2 shows stronger alkaline adaptation than NhaC1 in complementation assay | “the optimal pH is 9.5” | 10.3390/ijms241310786, 2023, https://doi.org/10.3390/ijms241310786 | High | Assay-specific transporter property. (wang2023characterizationoftwo pages 7-8) |
| NhaC-family Na+/H+ antiporter [label-only] | exports | Na+ / Li+ / K+ [CHEBI:29101, CHEBI:30145, CHEBI:29103] | Monovalent cation extrusion coupled to H+ uptake is a plausible module for facultative alkaliphily | “NhaC proteins primarily extrude intracellular Na+ or Li+” | 10.3390/ijms241310786, 2023, https://doi.org/10.3390/ijms241310786 | High | Useful transport edge; K+ transport supported for some homologs. (wang2023characterizationoftwo pages 10-12) |
| NhaC antiporters [label-only] | positively_regulated_by | salinity stress [label-only] | In polyextremophile N. thermophilus, NhaC proteins are upregulated under higher salinity, supporting ion-homeostasis role | “encodes and upregulates three NhaC-family Na+/H+ antiporters under varying salinities” | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | Med | Salinity rather than pH as direct perturbation; relevant supporting evidence, not trait-defining. (xing2024thepolyextremophilenatranaerobius pages 19-21) |
| mrpABCDEFG operon [label-only] | associated_with | halotolerance and alkali resistance [label-only] | Comparative genomics links presence of Mrp operon to saline-alkaline habitat adaptation | “halotolerant and alkali-resistant Aquibium… possessed… mrpABCDEFG” | 10.1128/aem.02091-23, 2024, https://doi.org/10.1128/aem.02091-23 | Med | Correlative genomics, not direct perturbation. Good comparative-support edge. (kim2024lineagespecificevolutionof pages 1-2) |
| loss of mrpABCDEFG [label-only] | associated_with_loss_of | saline/alkaline habitat adaptation [label-only] | Terrestrial lineages lacking mrp suggest antiporter loss during transition away from alkaline aquatic habitats | “genes acquired for adaptation to highly saline and alkaline environments were lost” | 10.1128/aem.02091-23, 2024, https://doi.org/10.1128/aem.02091-23 | Med | Evolutionary inference; do not overstate as direct phenotype cause. (kim2024lineagespecificevolutionof pages 1-2) |
| low oxygen availability [ENVO:09200000 candidate / label-only] | downregulates | Mrp complex [mrpABCDEFG] | Recent proteomics suggests environmental oxygen modulates reliance on Mrp | “the Mrp… complex was downregulated at lower oxygen concentrations” | 10.3389/fmicb.2024.1468929, 2024, https://doi.org/10.3389/fmicb.2024.1468929 | Med | Important environmental modifier edge; from obligate thermoalkaliphile chemostat study. (jong2024quantitativeproteomicsreveals pages 1-2) |
| sodium:acetate exporter [label-only] | may_compensate_for | reduced Mrp function [label-only] | Hypothesized alternative Na+ export route under oxygen limitation | “a sodium:acetate exporter… decreases the requirement for Mrp under strong oxygen limitation” | 10.3389/fmicb.2024.1468929, 2024, https://doi.org/10.3389/fmicb.2024.1468929 | Low | Explicitly hypothetical; useful warning/optional edge only. (jong2024quantitativeproteomicsreveals pages 1-2) |
| acidic secondary cell-wall components / S-layer proteins [label-only] | attract | proton [CHEBI:15378] | Surface acidity can enrich protons and repel hydroxide, supporting alkaline adaptation | “acidic secondary cell wall components… attract H+ and repel OH−” | 10.3389/fmicb.2018.02331, 2018, https://doi.org/10.3389/fmicb.2018.02331 | Med | Good process-level edge, but generalized from alkaliphiles rather than facultative subset. (matsuno2018formationofproton pages 1-2) |
| facultative alkaliphile phenotype [METPO:1003005] | exemplified_by | Bacillus cohnii YN-2000 [NCBITaxon:label-only] | Quantitative example of facultative alkaliphilic intracellular pH control | “including a facultative alkaliphile, B. cohnii YN-2000” | 10.3389/fmicb.2018.02331, 2018, https://doi.org/10.3389/fmicb.2018.02331 | High | Useful exemplar taxon node for curation notes, not universal mechanism. (matsuno2018formationofproton pages 4-5) |


*Table: This table lists candidate mechanistic and phenotype-level causal edges for curating the trait 'facultatively alkaphilic,' with short evidence snippets, DOI-based references, confidence ratings, and curation notes. It emphasizes antiporters, ion homeostasis, cell-surface buffering, ATP synthesis, and environmental modifiers relevant to alkaline growth without obligate dependence.*

### 6) Expert synthesis (authoritative interpretations)

Across authoritative sources, facultative alkaliphily is best conceptualized as a **systems-level homeostasis trait** whose defining capability is maintaining a near-neutral cytoplasm and functional energetics across a broad external pH range. The most curation-ready mechanistic “backbone” includes (i) **Na+-dependent electrogenic cation/H+ antiport** (Mrp and/or other CPA-family antiporters), (ii) **cell-envelope acidity/buffering** (acidic wall polymers and surface layers), and (iii) **bioenergetic tuning** (high ΔΨ, localized proton capture/retention, and efficient ATP synthesis per proton). (preiss2015alkaliphilicbacteriawith pages 3-4, kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91, matsuno2018formationofproton pages 4-5)

### 7) Warnings / claims not yet ready for TraitMech curation

1. **Oxygen → Mrp downregulation → sodium:acetate exporter compensation** is explicitly framed as a hypothesis in the 2024 proteomics study; this is best curated as **uncertain/low-confidence** or as an “environmental modifier” edge pending direct genetic tests. (jong2024quantitativeproteomicsreveals pages 1-2)
2. **Donnan-effect/negative ion capacity → high ΔΨ → ATP synthesis** is mechanistically plausible and supported by quantitative associations, but still partly model-based and not easily reducible to single gene/protein nodes; curate at the **process level** with medium confidence. (matsuno2018formationofproton pages 4-5)
3. Many cell-wall polymer mechanisms (teichuronopeptide, tupA rescue) are **strain- or lineage-specific**; curate with explicit taxon scope (e.g., *Bacillus halodurans* C-125 lineage) unless broader evidence is added. (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91)

---

## DOI-first bibliography (with URLs and publication dates where available)

1. **Wang Q, Qiao M, Song J.** Characterization of Two Na+(K+, Li+)/H+ Antiporters from *Natronorubrum daqingense*. *Int J Mol Sci.* **Jun 2023**. DOI: **10.3390/ijms241310786**. URL: https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8, wang2023characterizationoftwo pages 10-12)
2. **de Jong SI, et al.** Quantitative proteomics reveals oxygen-induced adaptations in *Caldalkalibacillus thermarum* TA2.A1 microaerobic chemostat cultures. *Front Microbiol.* **Oct 2024**. DOI: **10.3389/fmicb.2024.1468929**. URL: https://doi.org/10.3389/fmicb.2024.1468929 (jong2024quantitativeproteomicsreveals pages 1-2)
3. **Kim M, et al.** Lineage-specific evolution of *Aquibium*, a close relative of *Mesorhizobium*, during habitat adaptation. *Appl Environ Microbiol.* **Feb 2024**. DOI: **10.1128/aem.02091-23**. URL: https://doi.org/10.1128/aem.02091-23 (kim2024lineagespecificevolutionof pages 1-2)
4. **Xing Q, et al.** The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress… *Appl Environ Microbiol.* **May 2024**. DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 19-21)
5. **Kevbrin VV.** Isolation and Cultivation of Alkaliphiles. *Adv Biochem Eng Biotechnol.* **Jan 2019**. DOI: **10.1007/10_2018_84**. URL: https://doi.org/10.1007/10_2018_84 (kevbrin2019isolationandcultivation pages 1-4)
6. **Matsuno T, et al.** Formation of Proton Motive Force Under Low-Aeration Alkaline Conditions in Alkaliphilic Bacteria. *Front Microbiol.* **Oct 2018**. DOI: **10.3389/fmicb.2018.02331**. URL: https://doi.org/10.3389/fmicb.2018.02331 (matsuno2018formationofproton pages 4-5, matsuno2018formationofproton pages 3-4)
7. **Preiss L, Hicks DB, Suzuki S, Meier T, Krulwich TA.** Alkaliphilic Bacteria with Impact on Industrial Applications… *Front Bioeng Biotechnol.* **Jun 2015**. DOI: **10.3389/fbioe.2015.00075**. URL: https://doi.org/10.3389/fbioe.2015.00075 (preiss2015alkaliphilicbacteriawith pages 3-4, preiss2015alkaliphilicbacteriawith media 930cd9d4)
8. **Kanekar PP, Kanekar SP.** Alkaliphilic, Alkalitolerant Microorganisms. In: *Microorganisms for Sustainability.* **Jan 2022**. DOI: **10.1007/978-981-19-1573-4_3**. URL: https://doi.org/10.1007/978-981-19-1573-4_3 (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91, kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 97-99)
9. **Horikoshi K.** Alkaliphiles. In: *Extremophiles.* **Jan 2021**. DOI: **10.1007/978-4-431-55408-0_4**. URL: https://doi.org/10.1007/978-4-431-55408-0_4 (horikoshi2016alkaliphiles pages 6-8, horikoshi2016alkaliphiles pages 8-9)

---

### Included visual evidence
A schematic of the Na+ cycle / Mrp antiporter / cytoplasmic pH maintenance in *B. pseudofirmus* OF4 was extracted (Preiss et al. Figure 2) and can be cited alongside curated edges about Na+ influx routes, Mrp-mediated electrogenic antiport, and maintenance of cytoplasmic pH ~8.3 at external pH ~10.5. (preiss2015alkaliphilicbacteriawith media 930cd9d4)


References

1. (kevbrin2019isolationandcultivation pages 1-4): Vadim V. Kevbrin. Isolation and cultivation of alkaliphiles. Advances in biochemical engineering/biotechnology, pages 53-84, Jan 2019. URL: https://doi.org/10.1007/10\_2018\_84, doi:10.1007/10\_2018\_84. This article has 37 citations.

2. (horikoshi2016alkaliphiles pages 2-5): Koki Horikoshi. Alkaliphiles, pages 53-78. Springer Japan, Jan 2021. URL: https://doi.org/10.1007/978-4-431-55408-0\_4, doi:10.1007/978-4-431-55408-0\_4. This article has 127 citations and is from a peer-reviewed journal.

3. (preiss2015alkaliphilicbacteriawith pages 2-3): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 193 citations.

4. (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91): Pradnya Pralhad Kanekar and Sagar Pralhad Kanekar. Alkaliphilic, Alkalitolerant Microorganisms, pages 71-116. Springer Nature Singapore, Jan 2022. URL: https://doi.org/10.1007/978-981-19-1573-4\_3, doi:10.1007/978-981-19-1573-4\_3. This article has 8 citations.

5. (matsuno2018formationofproton pages 4-5): Toshihide Matsuno, Toshitaka Goto, Shinichi Ogami, Hajime Morimoto, Koji Yamazaki, Norio Inoue, Hidetoshi Matsuyama, Kazuaki Yoshimune, and Isao Yumoto. Formation of proton motive force under low-aeration alkaline conditions in alkaliphilic bacteria. Frontiers in Microbiology, Oct 2018. URL: https://doi.org/10.3389/fmicb.2018.02331, doi:10.3389/fmicb.2018.02331. This article has 214 citations and is from a peer-reviewed journal.

6. (preiss2015alkaliphilicbacteriawith pages 4-5): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 193 citations.

7. (preiss2015alkaliphilicbacteriawith pages 3-4): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 193 citations.

8. (preiss2015alkaliphilicbacteriawith media 930cd9d4): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 193 citations.

9. (wang2023characterizationoftwo pages 7-8): Qi Wang, Mengwei Qiao, and Jinzhu Song. Characterization of two na+(k+, li+)/h+ antiporters from natronorubrum daqingense. International Journal of Molecular Sciences, 24:10786, Jun 2023. URL: https://doi.org/10.3390/ijms241310786, doi:10.3390/ijms241310786. This article has 10 citations.

10. (wang2023characterizationoftwo pages 10-12): Qi Wang, Mengwei Qiao, and Jinzhu Song. Characterization of two na+(k+, li+)/h+ antiporters from natronorubrum daqingense. International Journal of Molecular Sciences, 24:10786, Jun 2023. URL: https://doi.org/10.3390/ijms241310786, doi:10.3390/ijms241310786. This article has 10 citations.

11. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

12. (kim2024lineagespecificevolutionof pages 1-2): Minkyung Kim, Wonjae Kim, Yerim Park, Jaejoon Jung, and Woojun Park. Lineage-specific evolution of aquibium, a close relative of mesorhizobium, during habitat adaptation. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.02091-23, doi:10.1128/aem.02091-23. This article has 4 citations and is from a peer-reviewed journal.

13. (horikoshi2016alkaliphiles pages 6-8): Koki Horikoshi. Alkaliphiles, pages 53-78. Springer Japan, Jan 2021. URL: https://doi.org/10.1007/978-4-431-55408-0\_4, doi:10.1007/978-4-431-55408-0\_4. This article has 127 citations and is from a peer-reviewed journal.

14. (horikoshi2016alkaliphiles pages 8-9): Koki Horikoshi. Alkaliphiles, pages 53-78. Springer Japan, Jan 2021. URL: https://doi.org/10.1007/978-4-431-55408-0\_4, doi:10.1007/978-4-431-55408-0\_4. This article has 127 citations and is from a peer-reviewed journal.

15. (horikoshi2016alkaliphiles pages 9-11): Koki Horikoshi. Alkaliphiles, pages 53-78. Springer Japan, Jan 2021. URL: https://doi.org/10.1007/978-4-431-55408-0\_4, doi:10.1007/978-4-431-55408-0\_4. This article has 127 citations and is from a peer-reviewed journal.

16. (yumoto2025h+capacitorandatp pages 2-3): Isao Yumoto. H+-capacitor and atp production in obligate alkaliphilic bacillaceae: insights into cytochrome c and h+ transport mechanisms. Frontiers in Microbiology, Sep 2025. URL: https://doi.org/10.3389/fmicb.2025.1637315, doi:10.3389/fmicb.2025.1637315. This article has 1 citations and is from a peer-reviewed journal.

17. (matsuno2018formationofproton pages 1-2): Toshihide Matsuno, Toshitaka Goto, Shinichi Ogami, Hajime Morimoto, Koji Yamazaki, Norio Inoue, Hidetoshi Matsuyama, Kazuaki Yoshimune, and Isao Yumoto. Formation of proton motive force under low-aeration alkaline conditions in alkaliphilic bacteria. Frontiers in Microbiology, Oct 2018. URL: https://doi.org/10.3389/fmicb.2018.02331, doi:10.3389/fmicb.2018.02331. This article has 214 citations and is from a peer-reviewed journal.

18. (goto2022differencesinbioenergetic pages 1-2): Toshitaka Goto, Shinichi Ogami, Kazuaki Yoshimume, and Isao Yumoto. Differences in bioenergetic metabolism of obligately alkaliphilic bacillaceae under high ph depend on the aeration conditions. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.842785, doi:10.3389/fmicb.2022.842785. This article has 7 citations and is from a peer-reviewed journal.

19. (xing2024thepolyextremophilenatranaerobius pages 19-21): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

20. (matsuno2018formationofproton pages 3-4): Toshihide Matsuno, Toshitaka Goto, Shinichi Ogami, Hajime Morimoto, Koji Yamazaki, Norio Inoue, Hidetoshi Matsuyama, Kazuaki Yoshimune, and Isao Yumoto. Formation of proton motive force under low-aeration alkaline conditions in alkaliphilic bacteria. Frontiers in Microbiology, Oct 2018. URL: https://doi.org/10.3389/fmicb.2018.02331, doi:10.3389/fmicb.2018.02331. This article has 214 citations and is from a peer-reviewed journal.

21. (kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 97-99): Pradnya Pralhad Kanekar and Sagar Pralhad Kanekar. Alkaliphilic, Alkalitolerant Microorganisms, pages 71-116. Springer Nature Singapore, Jan 2022. URL: https://doi.org/10.1007/978-981-19-1573-4\_3, doi:10.1007/978-981-19-1573-4\_3. This article has 8 citations.