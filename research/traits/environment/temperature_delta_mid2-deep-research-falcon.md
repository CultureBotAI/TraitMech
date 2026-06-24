---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:46:18.779624'
end_time: '2026-06-18T02:04:56.355198'
duration_seconds: 1117.58
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature delta mid2
  trait_identifier: METPO:1000486
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_delta_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature delta phenotype with a growth-supporting temperature\
    \ breadth of approximately 20\u201330 \xB0C, characteristic of organisms with\
    \ broad thermal-tolerance breadth."
  parent_traits: METPO:1000303
  synonyms: Td_20_30
  evidence_summary: 'DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty
    acids (Membrane-adaptation review supports broad homoviscous remodeling capacity
    as the basis of eurythermal physiology.)'
  causal_graph_summary: 'temperature_delta_mid2_broad_breadth: 3 nodes, 2 edges'
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
- **Trait label:** temperature delta mid2
- **METPO identifier:** METPO:1000486
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 20–30 °C, characteristic of organisms with broad thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_20_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports broad homoviscous remodeling capacity as the basis of eurythermal physiology.)
- **Existing causal graph summary:** temperature_delta_mid2_broad_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_mid2.yaml`.

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
- **Trait label:** temperature delta mid2
- **METPO identifier:** METPO:1000486
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 20–30 °C, characteristic of organisms with broad thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_20_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports broad homoviscous remodeling capacity as the basis of eurythermal physiology.)
- **Existing causal graph summary:** temperature_delta_mid2_broad_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_mid2.yaml`.

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


## Curation-focused research report: METPO:1000486 temperature delta mid2 (Td_20_30)

### Scope summary (TraitMech curation intent)
**Temperature delta mid2 (Td_20_30; METPO:1000486)** represents a **growth-supporting temperature breadth** of ~**20–30 °C** (ΔT between *Tmin for growth* and *Tmax for growth*), i.e., an organism can sustain growth across a relatively broad moderate temperature window (thermal generalist/eurythermal physiology). This is distinct from (i) **thermal optimum (TOPT)** categories (psychrophile/mesophile/thermophile definitions by TOPT) and (ii) narrow-range strains that may have similar TOPT but small ΔT. Cardinal-temperature context and examples of broad temperature functionality appear in recent bacterial stress-response reviews and culture studies, including experimentally demonstrated function from **5–37 °C** for a cold-tolerant denitrifier and **15–30 °C** culturing for a brGDGT-producing bacterium (moon2023temperaturemattersbacterial pages 1-3, yang2023insightintothe pages 1-2, halamka2023productionofdiverse pages 1-2).

**Boundary cases for curation**
- Td_20_30 is about **breadth**, not necessarily “cold specialist” (psychrophile) or “heat specialist” (thermophile). For example, *Bacillus simplex* H‑b shows cold function (5 °C) while still operating up to 30–37 °C (yang2023insightintothe pages 1-2), whereas archaeal thermoacidophiles may have large ΔT at high absolute temperatures.
- Many mechanisms below are **temperature-stress responses** that can support breadth, but they may also occur in specialists; edges should be curated only when they plausibly support **growth across temperatures**, not merely survival.

---

### Key concepts and definitions (current understanding)
1. **Homeoviscous adaptation (HVA)**: regulation of membrane composition to maintain appropriate membrane physical properties (fluidity/thickness/order) across temperatures. Mechanisms include fatty-acid desaturation, branched-chain FA remodeling, sterol/hopanoid modulation, and phospholipid headgroup remodeling (sidarta2024lipidphaseseparation pages 1-2, maiti2024extrememakeoverthe pages 4-5, safronova2023fromhotto pages 8-10).
2. **Regulon-level temperature response**: temperature shifts are sensed via multiple layers including DNA topology and RNA thermometers (translation control), sigma factors (e.g., RpoS), and stress assemblies like bacterial RNP condensates (BR-bodies) that influence mRNA decay and stress resistance (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 9-10).
3. **Tetraether lipid modification as thermal/pH/O2 response**: in archaea (GDGT ring cyclization controlled by grs genes) and in some bacteria (branched GDGT methylation/cyclization), lipid structural indices (Ring Index, MBT′5Me, CBT5Me) provide measurable outputs linked to environmental temperature and other variables (chiu2023membranelipidand pages 13-14, halamka2023productionofdiverse pages 5-6).

---

### Recent developments (prioritizing 2023–2024)
#### 1) Membrane thickness sensing & desaturation regulation in *Bacillus subtilis* (2024)
A 2024 Microbiology Spectrum study revisited the canonical **DesK/DesR/des** system and emphasized that in vivo temperature adaptation can depend strongly on **membrane domain behavior (phase separation)**: **DesK senses membrane thickness/rigidification**, activates DesR, induces **des** desaturase expression, and desaturation fluidizes the membrane in a negative-feedback loop; however, **phase separation can impair DesK sensing** under harsh cold/antibiotic stress (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 14-16). The study also highlights that **branched-chain fatty acids dominate B. subtilis membranes (80–96%)**, with a very low unsaturated:saturated ratio, implying that **BCFA remodeling may be the main fluidity lever** in this organism rather than desaturation (sidarta2024lipidphaseseparation pages 14-16).

#### 2) Quantitative lipidome “two-stage” cold adaptation in a minimal microbe model (2023 preprint)
Quantitative shotgun lipidomics of *Mycoplasma mycoides* and minimal cell JCVI‑Syn3B describes a **two-stage cold response**: after a **37 → 25 °C** shift, an initial rapid **~7 mol% decrease in cholesterol** occurs (≈1 h in *M. mycoides*), followed by slower remodeling of headgroups and acyl chains; e.g., **PC decreased ~10 mol%**, while **PG and sphingomyelin increased** over 24 h (safronova2023fromhotto pages 8-10). While this is a preprint in the extracted evidence, it provides an explicitly time-resolved, quantitative lipid adaptation framework useful for mechanistic node/edge selection (safronova2023fromhotto pages 8-10).

#### 3) Controlled culture evidence that bacterial brGDGT membrane tetraethers respond to temperature, pH, and O2 (2023)
A major advance for mechanistic interpretation of brGDGT temperature proxies is **culturing evidence** from *Solibacter usitatus* (Acidobacteria): it was grown at **15–30 °C**, **pH 5.0–6.5**, and **O2 1–21%**, with growth rates **0.23–1.45 day−1** and tetraethers comprising **10–47%** of membrane lipids (mean **24 ± 9%**) (halamka2023productionofdiverse pages 1-2, halamka2023productionofdiverse pages 5-6). The methylation proxy **MBT′5Me correlated positively with culture temperature and growth rate**, while cyclization proxy **CBT5Me correlated significantly only with pH** (halamka2023productionofdiverse pages 5-6). Under oxygen manipulation at **25 °C, pH 5.5**, specific brGDGT isomers shifted quantitatively with O2 (see Figure evidence) (halamka2023productionofdiverse pages 10-11, halamka2023productionofdiverse media bbc0c0e5).

#### 4) Archaeal GDGT cyclization + gene-expression coupling under defined cold shift (2023)
In *Saccharolobus islandicus* REY15A, a **10 °C cold shift (76 → 66 °C)** and an acid shift (pH 3.4→2.4) slowed growth and altered membrane GDGT cyclization (chiu2023membranelipidand pages 7-9, chiu2023membranelipidand pages 5-6). Doubling times increased from **6.8 ± 0.1 h** (optimal) to **14.0 ± 0.5 h** (cold); stress reduced average cyclization and cold-stress lipid profiles showed reduced abundance of **≥5-ring GDGTs**, with stress-responsive **grsB** expression changes (chiu2023membranelipidand pages 5-6, chiu2023membranelipidand pages 13-14).

#### 5) Multi-mechanism cold adaptation enabling function across a broad ΔT (2023)
A transcriptomics-guided study of **aerobic denitrifier *Bacillus simplex* H‑b** reports functional denitrification across **5–37 °C** and a **nitrogen removal rate 27.22% at 5 °C** (yang2023insightintothe pages 1-2). The cold-response program included increased unsaturated FAs, accumulation of ATP and EPS, changes in sigma factors, oxidative stress enzymes, and **upregulation of chaperones** (GroES/GroEL, DnaK/DnaJ/GrpE; plus Hsp15/Hsp33; Clp protease family) (yang2023insightintothe pages 1-2, yang2023insightintothe pages 10-12).

---

### Current applications and real-world implementations
1. **Low-temperature wastewater nitrogen removal**: Cold-tolerant denitrifiers like *Bacillus simplex* H‑b are explicitly positioned as candidates for **nitrogen-contaminated wastewater treatment at low temperatures**; mechanistic understanding is framed as enabling improved application in cold regions (yang2023insightintothe pages 1-2).
2. **Biomarker/proxy applications (brGDGT/GDGT) for temperature reconstruction**: The Solibacter brGDGT culturing study provides physiological support for temperature–methylation relationships underlying **brGDGT paleothermometry**, while also identifying pH and O2 as modifying variables relevant to proxy interpretation (halamka2023productionofdiverse pages 1-2, halamka2023productionofdiverse pages 5-6).

---

### Expert opinions / authoritative analyses (from the retrieved sources)
- **Temperature sensing and response are multi-layered**: A high-citation 2023 review emphasizes DNA topology, RNA thermometers, sigma factors, and stress assemblies (BR-bodies) as central to bacterial responses to temperature change, illustrating expert consensus that breadth-supporting physiology is not reducible to a single pathway (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 9-10).
- **In vivo membrane sensing may be constrained by membrane organization**: The 2024 DesK study argues that phase separation and domain partitioning can limit sensor function in vivo, implying that “canonical” pathways may behave differently under severe perturbations than in controlled in vitro systems (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 14-16).
- **Transcript→lipid mapping can be unreliable in archaea**: The archaeal study highlights that **grsB transcription changes do not always predict GDGT cyclization outcomes**, cautioning against curating direct transcription→lipid edges without strong coupled measurements (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 14-15).

---

### Candidate nodes grouped by type (curation-ready inventory)
The following curated inventory is provided as a structured artifact:

| Node label | Type | Suggested ontology grounding | Evidence/source supporting inclusion (short) | Notes |
|---|---|---|---|---|
| temperature delta mid2 / Td_20_30 | phenotype/trait | METPO:1000486 | Broad growth-supporting temperature breadth concept for organisms sustaining growth across moderate thermal spans; supported indirectly by broad-span culture studies and temperature-response mechanisms (yang2023insightintothe pages 1-2, halamka2023productionofdiverse pages 1-2) | Core target trait; phenotype-level node rather than mechanism |
| broad thermal tolerance breadth / eurythermal growth | phenotype/trait |  | Bacillus simplex H-b showed aerobic denitrification from 5–37 °C; Solibacter usitatus was cultured from 15–30 °C with measurable growth across conditions (yang2023insightintothe pages 1-2, halamka2023productionofdiverse pages 5-6) | Label-only candidate summarizing growth breadth; not a specific ontology term identified |
| decreased temperature / cold stress | environmental factor | ENVO:01001615 | Cold stress triggered des-system responses, trehalose-associated responses, archaeal GDGT changes, and chaperone induction (sidarta2024lipidphaseseparation pages 1-2, moon2023temperaturemattersbacterial pages 9-10, chiu2023membranelipidand pages 13-14, yang2023insightintothe pages 10-12) | High-confidence environmental driver |
| increased temperature / heat stress | environmental factor |  | Heat induces BR-bodies and shapes membrane remodeling across taxa (moon2023temperaturemattersbacterial pages 9-10, maiti2024extrememakeoverthe pages 4-5) | Label-only; useful as opposing temperature-state node |
| oxygen concentration / O2 limitation | environmental factor | ENVO:01000328 | Solibacter brGDGT composition changed across 21%, 5%, and 1% O2; rare isomers increased as O2 decreased (halamka2023productionofdiverse pages 10-11, halamka2023productionofdiverse pages 5-6) | Important interacting environmental factor; not temperature-specific |
| pH | environmental factor |  | brGDGT methylation/cyclization responses in Solibacter and GDGT regulation in archaea were pH sensitive (halamka2023productionofdiverse pages 5-6, chiu2023membranelipidand pages 13-14) | Important confounder/modifier for temperature-lipid edges |
| growth rate | assay factor |  | Solibacter growth rates ranged 0.23–1.45 day−1 across temperature/pH/O2 conditions and correlated with temperature (halamka2023productionofdiverse pages 5-6, halamka2023productionofdiverse pages 8-9) | Measurement/output variable, not mechanism |
| doubling time | assay factor |  | S. islandicus doubling time increased from 6.8 h optimal to 14.0 h under cold stress (chiu2023membranelipidand pages 5-6) | Measurement/output variable |
| ring index (RI) | assay factor |  | Archaeal GDGT cyclization summarized by RI; stress lowered average cyclization and altered RI (chiu2023membranelipidand pages 13-14, chiu2023membranelipidand pages 5-6) | Proxy/measurement, not direct molecular entity |
| MBT′5Me | assay factor |  | Solibacter brGDGT methylation index positively correlated with temperature and growth rate (halamka2023productionofdiverse pages 5-6, halamka2023productionofdiverse pages 8-9) | Proxy/measurement node; curate separately from lipid species |
| CBT5Me | assay factor |  | Solibacter cyclization proxy correlated significantly with pH (halamka2023productionofdiverse pages 5-6) | Proxy/measurement node; environmentally confounded |
| membrane fluidity / homeoviscous adaptation | molecular process |  | Des-mediated FA desaturation and broader lipid remodeling were interpreted as homeoviscous adaptation (sidarta2024lipidphaseseparation pages 1-2, safronova2023fromhotto pages 10-12) | Central mechanistic process; label-only preferred |
| membrane thickness sensing | molecular process | GO:0007165 | DesK directly detects membrane thickness changes associated with rigidification (sidarta2024lipidphaseseparation pages 1-2) | Process-level node derived mainly from B. subtilis |
| fatty-acid desaturation | molecular process | GO:0006636 | Rapid change in saturated:unsaturated ratio via desaturation of existing lipids under cold adaptation (sidarta2024lipidphaseseparation pages 1-2, maiti2024extrememakeoverthe pages 4-5) | Strong mechanism across bacteria; may be minor in some taxa |
| branched-chain fatty-acid remodeling / iso:anteiso remodeling | molecular process |  | B. subtilis relies strongly on BCFA content and iso:anteiso ratio for fluidity regulation (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 14-16) | Strong but taxon-weighted toward Bacillus |
| trehalose biosynthesis | molecular process | GO:0005992 | otsAB operon synthesizes trehalose and is induced by cold shock/RpoS-dependent pathways (moon2023temperaturemattersbacterial pages 9-10) | Strong process node |
| mRNA decay in BR-bodies | molecular process | GO:0006402 | BR-bodies with RNase E and degradosome components accelerate mRNA decay during stress (moon2023temperaturemattersbacterial pages 9-10) | Stress-response process; broader than temperature breadth alone |
| GDGT cyclization | molecular process |  | Archaeal cells adjust GDGT ring number with cold/acid stress; lower cold-stress RI and fewer ≥5-ring GDGTs reported (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 13-14) | Strong archaeal process node |
| mevalonate pathway | molecular process | KEGG:map00900 | Multiple MVA-pathway genes were upregulated under stress in S. islandicus (chiu2023membranelipidand pages 7-9) | Archaeal lipid-biosynthesis context |
| chaperone-mediated protein folding / temperature stress response | molecular process | GO:0006457 | GroES/GroEL, DnaK/DnaJ/GrpE, Hsp15/Hsp33, and Clp family were upregulated under low temperature in Bacillus simplex H-b (yang2023insightintothe pages 10-12) | Strong cold-response mechanism, especially for bacteria |
| antioxidant response | molecular process | GO:0006979 | Catalase, superoxide dismutase, peroxidase, and alkyl hydroperoxide reductase were induced in cold adaptation study (yang2023insightintothe pages 10-12) | Stress-protection mechanism; indirect link to breadth |
| extracellular polymeric substance formation | molecular process | GO:0045226 | Bacillus simplex H-b accumulated EPS at low temperature (yang2023insightintothe pages 1-2) | Likely adaptive but broad and strain-specific |
| DesK | gene/protein |  | Bacillus subtilis membrane sensor kinase that detects thickness/rigidification (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 14-16) | Taxon-specific model protein |
| DesR | gene/protein |  | DesK phosphorylates DesR to activate des expression (sidarta2024lipidphaseseparation pages 1-2) | Taxon-specific response regulator |
| Des (acyl-lipid desaturase) | gene/protein | EC:1.14.19.- | Des expression mediates FA desaturation during cold adaptation (sidarta2024lipidphaseseparation pages 1-2) | Enzyme class grounding approximate |
| RNase E | gene/protein |  | Core BR-body scaffold; required with IDR-containing C-terminus (moon2023temperaturemattersbacterial pages 9-10) | Stress-condensate protein, especially Proteobacteria models |
| RhlB | gene/protein |  | Listed as BR-body/degradosome component (moon2023temperaturemattersbacterial pages 9-10) | Accessory component |
| PNPase | gene/protein |  | Listed as BR-body/degradosome component (moon2023temperaturemattersbacterial pages 9-10) | Accessory component |
| RpoS (σS) | gene/protein |  | RpoS-dependent induction of otsAB and low-temperature biofilm-associated gene regulation (moon2023temperaturemattersbacterial pages 9-10) | Important general stress sigma factor |
| OtsA | gene/protein | EC:2.4.1.15 | Trehalose-6-phosphate synthase in otsAB operon (moon2023temperaturemattersbacterial pages 9-10) | Strong, broadly conserved enzyme |
| OtsB | gene/protein | EC:3.1.3.12 | Trehalose-6-phosphate phosphatase in otsAB operon (moon2023temperaturemattersbacterial pages 9-10) | Strong, broadly conserved enzyme |
| GroEL | gene/protein |  | Upregulated in Bacillus simplex H-b at low temperature (yang2023insightintothe pages 10-12) | Chaperone; strain-specific evidence but broadly plausible |
| GroES | gene/protein |  | Upregulated in Bacillus simplex H-b at low temperature (yang2023insightintothe pages 10-12) | Chaperone; strain-specific evidence but broadly plausible |
| DnaK | gene/protein |  | Upregulated in Bacillus simplex H-b at low temperature (yang2023insightintothe pages 10-12) | Chaperone; strain-specific evidence but broadly plausible |
| DnaJ | gene/protein |  | Upregulated in Bacillus simplex H-b at low temperature (yang2023insightintothe pages 10-12) | Chaperone; strain-specific evidence but broadly plausible |
| GrpE | gene/protein |  | Upregulated in Bacillus simplex H-b at low temperature (yang2023insightintothe pages 10-12) | Chaperone cofactor |
| Hsp15 | gene/protein |  | Upregulated in Bacillus simplex H-b at low temperature (yang2023insightintothe pages 10-12) | Stress protein; strain-specific |
| Hsp33 | gene/protein |  | Upregulated in Bacillus simplex H-b at low temperature (yang2023insightintothe pages 10-12) | Stress protein; strain-specific |
| Clp protease family | gene/protein |  | Upregulated in Bacillus simplex H-b at low temperature (yang2023insightintothe pages 10-12) | Protein quality control |
| catalase | gene/protein | EC:1.11.1.6 | Induced antioxidant enzyme under low temperature in Bacillus simplex H-b (yang2023insightintothe pages 10-12) | Supportive, indirect breadth mechanism |
| superoxide dismutase | gene/protein | EC:1.15.1.1 | Induced antioxidant enzyme under low temperature in Bacillus simplex H-b (yang2023insightintothe pages 10-12) | Supportive, indirect breadth mechanism |
| alkyl hydroperoxide reductase | gene/protein |  | Induced antioxidant enzyme under low temperature in Bacillus simplex H-b (yang2023insightintothe pages 10-12) | Supportive, indirect breadth mechanism |
| sigma-B | gene/protein |  | One of the sigma factors induced in Bacillus simplex H-b cold response (yang2023insightintothe pages 10-12) | Regulatory/stress-associated; strain-specific evidence |
| sigma-54 | gene/protein |  | One of the sigma factors induced in Bacillus simplex H-b cold response (yang2023insightintothe pages 10-12) | Regulatory/stress-associated |
| sigma-70 | gene/protein |  | One of the sigma factors induced in Bacillus simplex H-b cold response (yang2023insightintothe pages 10-12) | Housekeeping/stress-associated |
| grsB | gene/protein |  | Archaeal GDGT ring synthase responsive to cold/acid stress; downregulated in cold and linked to ≥5-ring GDGTs (chiu2023membranelipidand pages 13-14, chiu2023membranelipidand pages 14-15) | Strong archaeal candidate; specific to GDGT producers |
| grsA | gene/protein |  | Present in S. islandicus genome; no strong differential expression in excerpt (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 13-14) | Include as pathway component, but weaker direct support |
| PMK | gene/protein | EC:2.7.4.2 | Phosphomevalonate kinase upregulated only under cold stress in S. islandicus (chiu2023membranelipidand pages 7-9) | Archaeal MVA-pathway component |
| IPK | gene/protein | EC:2.7.4.26 | Isopentenyl phosphate kinase upregulated under acid stress in S. islandicus (chiu2023membranelipidand pages 7-9) | Pathway component; less directly temperature-linked |
| HMGR | gene/protein | EC:1.1.1.34 | Mevalonate-pathway gene upregulated in early stationary phase under stress (chiu2023membranelipidand pages 7-9) | Archaeal lipid precursor pathway |
| HMGS | gene/protein | EC:2.3.3.10 | Mevalonate-pathway gene upregulated in early stationary phase under stress (chiu2023membranelipidand pages 7-9) | Archaeal lipid precursor pathway |
| AACT | gene/protein | EC:2.3.1.9 | Mevalonate-pathway gene upregulated in early stationary phase under stress (chiu2023membranelipidand pages 7-9) | Archaeal lipid precursor pathway |
| GGPP synthase | gene/protein | EC:2.5.1.29 | Upregulated under acid stress in S. islandicus (chiu2023membranelipidand pages 14-15) | Lipid precursor enzyme; stress linked |
| GGGP synthase | gene/protein | EC:2.7.8.12 | Downregulated under acid stress in S. islandicus (chiu2023membranelipidand pages 14-15) | Archaeal ether-lipid pathway component |
| Tes homolog / tetraether synthase homolog | gene/protein |  | Solibacter data suggest a Tes-homolog pathway for tetraether synthesis (halamka2023productionofdiverse pages 1-2, stonik2024structurediversityand pages 17-19) | Inferred biosynthetic component; more indirect evidence |
| unsaturated fatty acids | lipid/metabolite | CHEBI:27208 | Higher proportions at low temperature in Bacillus simplex H-b; des-mediated production in Bacillus model (yang2023insightintothe pages 1-2, sidarta2024lipidphaseseparation pages 1-2) | High-confidence lipid class node |
| branched-chain fatty acids | lipid/metabolite |  | B. subtilis membranes are 80–96% BCFA and use BCFA composition as main fluidity regulator (sidarta2024lipidphaseseparation pages 14-16) | Strong Bacillus-focused node |
| trehalose | lipid/metabolite | CHEBI:18150 | Product of otsAB pathway; supports cold-shock tolerance (moon2023temperaturemattersbacterial pages 9-10) | Compatible solute, not lipid |
| cholesterol | lipid/metabolite | CHEBI:16113 | Cold shift caused ~7 mol% cholesterol decrease in Mycoplasma mycoides (safronova2023fromhotto pages 8-10) | Strong but taxon-specific to sterol-requiring mycoplasmas |
| cardiolipin | lipid/metabolite | CHEBI:28494 | Rapid shift in cardiolipin during two-stage cold adaptation response (safronova2023fromhotto pages 1-3, safronova2023fromhotto pages 8-10) | Strong membrane-remodeling node |
| phosphatidylcholine (PC) | lipid/metabolite | CHEBI:64482 | Decreased nearly 10 mol% after cold shift in M. mycoides (safronova2023fromhotto pages 8-10) | Strong but taxon/context-specific |
| phosphatidylglycerol (PG) | lipid/metabolite | CHEBI:17517 | Increased monotonically during cold adaptation in M. mycoides (safronova2023fromhotto pages 8-10) | Strong but taxon/context-specific |
| sphingomyelin (SM) | lipid/metabolite | CHEBI:64583 | Increased during cold adaptation; remodeling deficiency linked to impaired adaptation in Syn3B (safronova2023fromhotto pages 1-3, safronova2023fromhotto pages 8-10) | Strong for mycoplasma/minimal-cell system |
| GDGTs | lipid/metabolite |  | S. islandicus contained GDGT-0 through GDGT-6 and altered average cyclization under cold/acid stress (chiu2023membranelipidand pages 5-6, chiu2023membranelipidand pages 1-2) | Archaeal membrane-spanning lipids |
| highly cyclized GDGTs (≥5-ring) | lipid/metabolite |  | Lower abundance under cold stress in S. islandicus; linked to grsB activity (chiu2023membranelipidand pages 14-15, chiu2023membranelipidand pages 13-14) | Specific archaeal lipid state |
| brGDGTs | lipid/metabolite |  | Solibacter membranes contained 10–47% tetraethers including diverse brGDGTs (halamka2023productionofdiverse pages 5-6, halamka2023productionofdiverse pages 1-2) | Strong bacterial tetraether node |
| brGDGT Ia | lipid/metabolite |  | Dominant Solibacter brGDGT; shifts with O2 and other conditions (halamka2023productionofdiverse pages 10-11, halamka2023productionofdiverse media bbc0c0e5) | Species-specific measurement node if overly granular |
| brGDGT IIa | lipid/metabolite |  | Increased under 5% O2 relative to 21% O2 in Solibacter (halamka2023productionofdiverse pages 10-11, halamka2023productionofdiverse media bbc0c0e5) | Species-specific measurement node if overly granular |
| brGDGT IIIa-2 | lipid/metabolite |  | Increased strongly as O2 decreased in Solibacter (halamka2023productionofdiverse pages 10-11, halamka2023productionofdiverse media bbc0c0e5) | Rare isomer; likely best treated as assay-detail unless needed |
| brGDGT IIIb-2 | lipid/metabolite |  | Increased strongly as O2 decreased in Solibacter (halamka2023productionofdiverse pages 10-11, halamka2023productionofdiverse media bbc0c0e5) | Rare isomer; likely best treated as assay-detail unless needed |
| extracellular polymeric substances (EPS) | lipid/metabolite |  | EPS accumulated at low temperature in Bacillus simplex H-b (yang2023insightintothe pages 1-2) | Broad material class; strain-specific |
| DesKR two-component system | regulatory system | GO:0000160 | DesK/DesR controls des expression in response to membrane rigidification/cold adaptation (sidarta2024lipidphaseseparation pages 1-2) | High-confidence regulatory system |
| RpoS regulon | regulatory system |  | Controls otsAB induction and low-temperature biofilm-related regulation (moon2023temperaturemattersbacterial pages 9-10) | Broad bacterial stress regulatory module |
| BR-body / degradosome stress condensate | regulatory system |  | RNase E-centered condensates form under heat/stress and support mRNA decay/stress resistance (moon2023temperaturemattersbacterial pages 9-10) | Functional regulatory assembly; label-only |
| sigma-factor stress regulation | regulatory system |  | sigma-54, sigma-70, sigma-B changed in Bacillus simplex H-b during low-temperature response (yang2023insightintothe pages 10-12) | Broad regulatory grouping |
| archaeal GDGT ring-synthase regulatory module | regulatory system |  | grsB expression changed under cold/acid stress but transcript levels did not fully predict lipid output (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 14-15) | Useful pathway-level abstraction; caution on direct transcript→lipid inference |


*Table: This table lists candidate nodes for a temperature_delta_mid2 causal graph, grouped by node type and grounded where possible to standard ontologies. It highlights the most curation-ready entities from recent bacterial and archaeal temperature-adaptation studies while flagging taxon-specific and proxy-style nodes.*

---

### Candidate causal edges (triples) with evidence snippets and curation notes
The following edge table focuses on graph-building for `temperature_delta_mid2.yaml`:

| Subject node (label + CURIE if available) | Predicate | Object node (label + CURIE if available) | Evidence snippet (short quote) | Source (authors, year, title, DOI, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| membrane rigidification / decreased temperature (ENVO:01001615 candidate for cold environment; label-only for membrane rigidification) | activates | DesK sensor kinase (label-only; Bacillus subtilis DesK) | “DesK… directly detects membrane thickness… upon activation by membrane rigidification” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta et al., 2024, *Lipid phase separation impairs membrane thickness sensing by the Bacillus subtilis sensor kinase DesK*, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23 | Strong for B. subtilis membrane-thickness sensing; taxon-specific. |
| DesK sensor kinase (label-only) | phosphorylates / activates | DesR response regulator (label-only) | “autophosphorylates at His188, phosphorylates DesR” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta et al., 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23 | Canonical DesKR two-component edge; good mechanistic support. |
| DesR response regulator (label-only) | positively regulates expression of | des acyl-lipid desaturase gene (label-only) | “phosphorylates DesR, and activates Pdes to induce des expression” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta et al., 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23 | Strong in B. subtilis; expression edge directly supported. |
| des acyl-lipid desaturase (EC:1.14.19.- candidate) | increases abundance of | unsaturated fatty acids (CHEBI:27208) | “a rapid change in the saturated:unsaturated fatty acid ratio by desaturation of existing lipids” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta et al., 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23 | Enzyme class grounding approximate; product-level mechanism strong. |
| unsaturated fatty acids (CHEBI:27208) | increases | membrane fluidity / homeoviscous adaptation (GO:0006884 broad membrane-related process not exact; label-only preferred) | “desaturation fluidizes the membrane” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta et al., 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23 | Strong general mechanism; membrane fluidity node may remain label-only. |
| decreased temperature (ENVO:01001615 candidate) | increases expression/activity of | RpoS sigma factor (label-only; σS) | “At lower temperatures RpoS upregulates biofilm-related genes” and “otsAB induction is RpoS-dependent and triggered by… cold shock” (moon2023temperaturemattersbacterial pages 9-10) | Moon et al., 2023, *Temperature Matters: Bacterial Response to Temperature Change*, DOI:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | Direct cold→RpoS wording is indirect in excerpt; moderate confidence. |
| RpoS sigma factor (label-only) | positively regulates expression of | otsAB operon (otsA trehalose-6-phosphate synthase + otsB trehalose-6-phosphate phosphatase; label-only) | “otsAB induction is RpoS-dependent and triggered by osmotic stress, cold shock, or stationary phase” (moon2023temperaturemattersbacterial pages 9-10) | Moon et al., 2023, DOI:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | Strong operon-regulation edge. |
| otsA/otsB pathway (trehalose biosynthesis; GO:0005992 trehalose biosynthetic process candidate) | produces | trehalose (CHEBI:18150) | “trehalose helps cold shock tolerance and is synthesized by the otsAB operon” (moon2023temperaturemattersbacterial pages 9-10) | Moon et al., 2023, DOI:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | Strong metabolic edge. |
| trehalose (CHEBI:18150) | contributes to | cold tolerance / cold-shock tolerance (GO:0009409 response to cold, broad) | “trehalose helps cold shock tolerance” (moon2023temperaturemattersbacterial pages 9-10) | Moon et al., 2023, DOI:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | Strong but broad phenotype edge. |
| temperature stress / heat (label-only) | induces | BR-body formation (label-only; bacterial RNP condensates) | “BR-body formation is induced by stresses and by heat (notably reported at 42 °C)” (moon2023temperaturemattersbacterial pages 9-10) | Moon et al., 2023, DOI:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | Strong for stress induction; more heat-focused than broad Td_20_30. |
| RNase E-containing BR-body (RNase E, RhlB, aconitase, RNase D, PNPase; label-only complex) | promotes | mRNA decay (GO:0006402) | “aids stress resistance and accelerated mRNA decay” (moon2023temperaturemattersbacterial pages 9-10) | Moon et al., 2023, DOI:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | Strong functional edge; condensate-complex node label-only. |
| BR-body formation (label-only) | contributes to | stress resistance (GO:0006950 response to stress, broad) | “BR-body formation… aids stress resistance” (moon2023temperaturemattersbacterial pages 9-10) | Moon et al., 2023, DOI:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | Strong but broad. |
| cold shift 37→25 °C (label-only experimental factor) | causes | cholesterol efflux / decreased cholesterol abundance (CHEBI:16113) | “initial ~7 mol% decrease in cholesterol… rapidly in M. mycoides” (safronova2023fromhotto pages 8-10) | Safronova et al., 2023 preprint, *From hot to cold: dissecting lipidome adaptation in Mycoplasma mycoides and the Minimal Cell JCVI-Syn3B*, DOI:10.1101/2023.11.10.566608, https://doi.org/10.1101/2023.11.10.566608 | Preprint; strong quantitative evidence but not peer-reviewed in cited version. |
| cold shift 37→25 °C (label-only experimental factor) | causes | phospholipid headgroup remodeling (PC↓, PG↑, SM↑; label-only process) | “PC decreased nearly 10 mol%… while PG and SM increased monotonically” (safronova2023fromhotto pages 8-10) | Safronova et al., 2023 preprint, DOI:10.1101/2023.11.10.566608, https://doi.org/10.1101/2023.11.10.566608 | Preprint; mechanistic and quantitative. |
| cholesterol efflux + headgroup remodeling (label-only) | contributes to | homeoviscous adaptation / thermal acclimation (label-only) | “two-stage cold response… rapid cholesterol efflux followed by gradual acyl-chain remodeling” (safronova2023fromhotto pages 8-10) | Safronova et al., 2023 preprint, DOI:10.1101/2023.11.10.566608, https://doi.org/10.1101/2023.11.10.566608 | Inferred integrative edge from reported adaptation sequence; moderate confidence. |
| temperature (label-only environmental factor) | positively correlates with | brGDGT methylation index MBT′5Me (label-only measurement node) | “MBT′5Me… correlated positively with culture temperature and growth rate” (halamka2023productionofdiverse pages 5-6) | Halamka et al., 2023, *Production of diverse brGDGTs by Acidobacterium Solibacter usitatus in response to temperature, pH, and O2…*, DOI:10.1111/gbi.12525, https://doi.org/10.1111/gbi.12525 | Strong culture evidence; proxy/index node rather than direct molecular entity. |
| pH (CHEBI:none; environmental pH label-only) | negatively modulates | brGDGT methylation index MBT′5Me (label-only) | “higher pH systematically increased the degree of methylation” at low T, but excerpt also notes “MBT′5Me… negatively with pH at 15–20°C” (halamka2023productionofdiverse pages 1-2, halamka2023productionofdiverse pages 5-6) | Halamka et al., 2023, DOI:10.1111/gbi.12525, https://doi.org/10.1111/gbi.12525 | Wording in extracted summaries is somewhat inconsistent; curate carefully against full paper. |
| pH (label-only) | correlates with | brGDGT cyclization index CBT5Me (label-only measurement node) | “CBT5Me (cyclization proxy) correlated significantly only with culture pH” (halamka2023productionofdiverse pages 5-6) | Halamka et al., 2023, DOI:10.1111/gbi.12525, https://doi.org/10.1111/gbi.12525 | Good for environmental-factor→proxy edge; proxy not equal to direct mechanism. |
| low O2 / oxygen limitation (ENVO:01000328 candidate hypoxic environment) | alters composition of | brGDGTs including IIIa-2 and IIIb-2 (label-only lipids) | “IIIa-2 and IIIb-2 show strong negative correlations with %O2… increase from near-zero at 21% O2 to several percent at low O2” (halamka2023productionofdiverse pages 10-11, halamka2023productionofdiverse media bbc0c0e5) | Halamka et al., 2023, DOI:10.1111/gbi.12525, https://doi.org/10.1111/gbi.12525 | Strong quantitative culture result. |
| cold shift 76→66 °C (label-only experimental factor) | downregulates | grsB GDGT ring synthase gene (label-only; archaeal grsB) | “cold stress decreased grsB” and in S. islandicus “downregulated grsB” (chiu2023membranelipidand pages 13-14, chiu2023membranelipidand pages 7-9) | Chiu et al., 2023, *Membrane lipid and expression responses of Saccharolobus islandicus REY15A to acid and cold stress*, DOI:10.3389/fmicb.2023.1219779, https://doi.org/10.3389/fmicb.2023.1219779 | Strong for this archaeon and condition. |
| grsB GDGT ring synthase (label-only) | promotes formation of | highly cyclized GDGTs (≥5-ring GDGTs; label-only, GDGTs CHEBI not clear) | “grsB-associated formation of ≥5-ring GDGTs” and cold profiles had “lower abundances of GDGTs with ≥5 rings” (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 13-14) | Chiu et al., 2023, DOI:10.3389/fmicb.2023.1219779, https://doi.org/10.3389/fmicb.2023.1219779 | Strong but relationship may vary with substrate availability (authors note complexity). |
| lower GDGT cyclization / lower ring index (label-only) | associated with | slower growth rate / increased doubling time (label-only phenotype) | “doubling times increased from 6.8 ± 0.1 h (optimal) to… 14.0 ± 0.5 h (cold)” and “both stressors produced decreased GDGT cyclization” (chiu2023membranelipidand pages 5-6, chiu2023membranelipidand pages 15-16) | Chiu et al., 2023, DOI:10.3389/fmicb.2023.1219779, https://doi.org/10.3389/fmicb.2023.1219779 | Association across same experiment; causality plausible but not directly proven. |
| low temperature 5 °C (ENVO:01001615 candidate) | upregulates | heat-shock/chaperone proteins Hsp15, Hsp33, GroES, GroEL, DnaJ, DnaK, GrpE, Clp protease family (label-only proteins) | “heat-shock proteins were upregulated: ‘Hsp15, Hsp33, GroES, GroEL, DnaJ, DnaK, GrpE, and Clp protease family’” (yang2023insightintothe pages 10-12) | Yang et al., 2023, *Insight into the Cold Adaptation Mechanism of an Aerobic Denitrifying Bacterium: Bacillus simplex H-b*, DOI:10.1128/aem.01928-22, https://doi.org/10.1128/aem.01928-22 | Strong transcriptional support in one strain. |
| chaperone upregulation (GroEL/DnaK/GrpE etc.; label-only process) | contributes to | cold tolerance / survival at 5 °C (GO:0009409 broad) | “combining multiple regulatory mechanisms… enabled the growth… at 5°C” (yang2023insightintothe pages 1-2) | Yang et al., 2023, DOI:10.1128/aem.01928-22, https://doi.org/10.1128/aem.01928-22 | Causal contribution inferred from transcriptomic synthesis, not single-gene perturbation. |
| low temperature 5 °C (label-only) | increases proportion of | unsaturated fatty acids (CHEBI:27208) | “At low temperatures the strain showed higher proportions of unsaturated fatty acids” (yang2023insightintothe pages 1-2) | Yang et al., 2023, DOI:10.1128/aem.01928-22, https://doi.org/10.1128/aem.01928-22 | Strong physiological edge; no exact percentages in excerpt. |
| decreased temperature (label-only) | remodels | branched-chain fatty acid composition / iso:anteiso ratio (label-only; BCFA process) | “long-term remodeling of branched-chain fatty acid content and the iso:anteiso ratio via de novo synthesis” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta et al., 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23 | Strong in B. subtilis; branch remodeling emphasized over desaturation. |
| branched-chain fatty acid iso/anteiso remodeling (label-only) | regulates | membrane fluidity (label-only) | “B. subtilis membranes are dominated by branched-chain fatty acids… suggesting branched-chain FA composition… is the main fluidity regulator” (sidarta2024lipidphaseseparation pages 14-16) | Sidarta et al., 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23 | Strong for B. subtilis; likely generalizable only cautiously. |
| temperature decrease / cold adaptation (label-only) | associated with | increased short-chain fatty acids and plasmalogens (label-only lipid classes) | “proportion of short-chain fatty acids increased at 50°C vs. 66°C… Adpt45_67 also showed a significantly increased proportion of plasmalogens” (lehmann2023adaptivelaboratoryevolution pages 1-2) | Lehmann et al., 2023, *Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum*, DOI:10.3389/fmicb.2023.1265216, https://doi.org/10.3389/fmicb.2023.1265216 | Useful candidate edge for thermophile-to-lower-T adaptation; mechanism unresolved, taxon-specific. |


*Table: This table lists candidate causal graph edges for the temperature delta mid2 microbial trait, with supporting snippets, source citations, and curation notes. It is useful as a starting artifact for selecting high-confidence TraitMech nodes and edges while flagging taxon-specific or proxy-based claims.*

Additionally, quantitative support for **O2-dependent shifts in brGDGT composition** in *Solibacter usitatus* is available as a figure extraction (Figure 3), showing percent changes for specific brGDGTs across **21%, 5%, 1% O2** at **25 °C and pH 5.5** (halamka2023productionofdiverse media bbc0c0e5).

---

### Relevant recent statistics and data points (for curation notes)
- **Solibacter usitatus (Geobiology 2023)**: cultured at **15–30 °C**, **pH 5.0–6.5**, **O2 1–21%**; growth rates **0.23–1.45 day−1**; tetraethers **10–47%** of membrane (mean **24 ± 9%**) (halamka2023productionofdiverse pages 1-2, halamka2023productionofdiverse pages 5-6).
- **Bacillus simplex H‑b (AEM 2023)**: aerobic denitrification functional from **5–37 °C**; **27.22% nitrogen removal at 5 °C** (yang2023insightintothe pages 1-2).
- **Saccharolobus islandicus (Frontiers in Microbiology 2023)**: cold shift **76→66 °C**; doubling time increased from **6.8 ± 0.1 h** to **14.0 ± 0.5 h** (chiu2023membranelipidand pages 7-9, chiu2023membranelipidand pages 5-6).
- **Mycoplasma lipidome (bioRxiv 2023)**: after **37→25 °C shift**, cholesterol decreased by **~7 mol%** and PC decreased **~10 mol%**, with PG/SM increasing over 24 h (safronova2023fromhotto pages 8-10).

---

### Warnings / “do not curate yet” items
1. **Proxy nodes vs mechanism nodes**: MBT′5Me/CBT5Me and RI are measurement proxies; curate as assay outputs or intermediate readouts rather than as mechanistic entities unless your schema supports “measurement nodes” (halamka2023productionofdiverse pages 5-6, chiu2023membranelipidand pages 5-6).
2. **Association vs causality**: Several edges are “associated with” (e.g., lower GDGT cyclization with slower growth) but not experimentally perturbed to prove direct causation; mark such edges as uncertain or keep at pathway-level (chiu2023membranelipidand pages 5-6, chiu2023membranelipidand pages 15-16).
3. **Taxon specificity**: DesKR/Des and BCFA dominance are strong in *B. subtilis* but may not generalize to other bacteria without additional evidence (sidarta2024lipidphaseseparation pages 14-16, sidarta2024lipidphaseseparation pages 1-2).
4. **Preprint status**: the detailed time-resolved lipidome adaptation model is from a 2023 bioRxiv preprint in the extracted evidence; treat as provisional or cross-check against the peer-reviewed version if available (safronova2023fromhotto pages 8-10).
5. **Transcript→lipid inference caution in archaea**: grsB transcription does not always predict highly cyclized GDGT abundance; avoid overconfident edges from expression alone (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 14-15).

---

## DOI-first bibliography (publication date and URL where available)

1. **Sidarta M, et al. (2024-06)**. *Lipid phase separation impairs membrane thickness sensing by the Bacillus subtilis sensor kinase DesK*. **Microbiology Spectrum**. DOI: **10.1128/spectrum.03925-23**. URL: https://doi.org/10.1128/spectrum.03925-23 (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 14-16)
2. **Maiti A, Erimban S, Daschakraborty S. (2024-08)**. *Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments*. **Chemical Communications**. DOI: **10.1039/D4CC03114H**. URL: https://doi.org/10.1039/d4cc03114h (maiti2024extrememakeoverthe pages 4-5)
3. **Moon S, et al. (2023-03)**. *Temperature Matters: Bacterial Response to Temperature Change*. **Journal of Microbiology**. DOI: **10.1007/s12275-023-00031-x**. URL: https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 9-10)
4. **Yang Q, et al. (2023-02)**. *Insight into the Cold Adaptation Mechanism of an Aerobic Denitrifying Bacterium: Bacillus simplex H-b*. **Applied and Environmental Microbiology**. DOI: **10.1128/aem.01928-22**. URL: https://doi.org/10.1128/aem.01928-22 (yang2023insightintothe pages 1-2, yang2023insightintothe pages 10-12)
5. **Halamka TA, et al. (2023-09)**. *Production of diverse brGDGTs by Acidobacterium Solibacter usitatus in response to temperature, pH, and O2 provides a culturing perspective on brGDGT proxies and biosynthesis*. **Geobiology**. DOI: **10.1111/gbi.12525**. URL: https://doi.org/10.1111/gbi.12525 (halamka2023productionofdiverse pages 1-2, halamka2023productionofdiverse pages 5-6, halamka2023productionofdiverse pages 10-11, halamka2023productionofdiverse media bbc0c0e5)
6. **Chiu BK, et al. (2023-08)**. *Membrane lipid and expression responses of Saccharolobus islandicus REY15A to acid and cold stress*. **Frontiers in Microbiology**. DOI: **10.3389/fmicb.2023.1219779**. URL: https://doi.org/10.3389/fmicb.2023.1219779 (chiu2023membranelipidand pages 7-9, chiu2023membranelipidand pages 5-6, chiu2023membranelipidand pages 13-14, chiu2023membranelipidand pages 1-2)
7. **Lehmann M, et al. (2023-10)**. *Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum*. **Frontiers in Microbiology**. DOI: **10.3389/fmicb.2023.1265216**. URL: https://doi.org/10.3389/fmicb.2023.1265216 (lehmann2023adaptivelaboratoryevolution pages 1-2, lehmann2023adaptivelaboratoryevolution pages 6-7)
8. **Safronova N, Junghans L, Saenz JP. (2023-11, preprint)**. *From hot to cold: dissecting lipidome adaptation in Mycoplasma mycoides and the Minimal Cell JCVI-Syn3B*. **bioRxiv**. DOI: **10.1101/2023.11.10.566608**. URL: https://doi.org/10.1101/2023.11.10.566608 (safronova2023fromhotto pages 8-10, safronova2023fromhotto pages 1-3)


References

1. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

2. (yang2023insightintothe pages 1-2): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 16 citations and is from a peer-reviewed journal.

3. (halamka2023productionofdiverse pages 1-2): Toby A. Halamka, Jonathan H. Raberg, Jamie M. McFarlin, Adam D. Younkin, Christopher Mulligan, Xiao‐Lei Liu, and Sebastian H. Kopf. Production of diverse brgdgts by acidobacterium solibacter usitatus in response to temperature, ph, and o2 provides a culturing perspective on brgdgt proxies and biosynthesis. Geobiology, 21:102-118, Sep 2023. URL: https://doi.org/10.1111/gbi.12525, doi:10.1111/gbi.12525. This article has 132 citations and is from a domain leading peer-reviewed journal.

4. (sidarta2024lipidphaseseparation pages 1-2): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Microbiology Spectrum, Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

5. (maiti2024extrememakeoverthe pages 4-5): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

6. (safronova2023fromhotto pages 8-10): Nataliya Safronova, Lisa Junghans, and James P Saenz. From hot to cold: dissecting lipidome adaptation in mycoplasma mycoides and the minimal cell jcvi-syn3b. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2023.11.10.566608, doi:10.1101/2023.11.10.566608. This article has 1 citations.

7. (moon2023temperaturemattersbacterial pages 9-10): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

8. (chiu2023membranelipidand pages 13-14): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

9. (halamka2023productionofdiverse pages 5-6): Toby A. Halamka, Jonathan H. Raberg, Jamie M. McFarlin, Adam D. Younkin, Christopher Mulligan, Xiao‐Lei Liu, and Sebastian H. Kopf. Production of diverse brgdgts by acidobacterium solibacter usitatus in response to temperature, ph, and o2 provides a culturing perspective on brgdgt proxies and biosynthesis. Geobiology, 21:102-118, Sep 2023. URL: https://doi.org/10.1111/gbi.12525, doi:10.1111/gbi.12525. This article has 132 citations and is from a domain leading peer-reviewed journal.

10. (sidarta2024lipidphaseseparation pages 14-16): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Microbiology Spectrum, Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

11. (halamka2023productionofdiverse pages 10-11): Toby A. Halamka, Jonathan H. Raberg, Jamie M. McFarlin, Adam D. Younkin, Christopher Mulligan, Xiao‐Lei Liu, and Sebastian H. Kopf. Production of diverse brgdgts by acidobacterium solibacter usitatus in response to temperature, ph, and o2 provides a culturing perspective on brgdgt proxies and biosynthesis. Geobiology, 21:102-118, Sep 2023. URL: https://doi.org/10.1111/gbi.12525, doi:10.1111/gbi.12525. This article has 132 citations and is from a domain leading peer-reviewed journal.

12. (halamka2023productionofdiverse media bbc0c0e5): Toby A. Halamka, Jonathan H. Raberg, Jamie M. McFarlin, Adam D. Younkin, Christopher Mulligan, Xiao‐Lei Liu, and Sebastian H. Kopf. Production of diverse brgdgts by acidobacterium solibacter usitatus in response to temperature, ph, and o2 provides a culturing perspective on brgdgt proxies and biosynthesis. Geobiology, 21:102-118, Sep 2023. URL: https://doi.org/10.1111/gbi.12525, doi:10.1111/gbi.12525. This article has 132 citations and is from a domain leading peer-reviewed journal.

13. (chiu2023membranelipidand pages 7-9): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

14. (chiu2023membranelipidand pages 5-6): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

15. (yang2023insightintothe pages 10-12): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 16 citations and is from a peer-reviewed journal.

16. (chiu2023membranelipidand pages 1-2): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

17. (chiu2023membranelipidand pages 14-15): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

18. (halamka2023productionofdiverse pages 8-9): Toby A. Halamka, Jonathan H. Raberg, Jamie M. McFarlin, Adam D. Younkin, Christopher Mulligan, Xiao‐Lei Liu, and Sebastian H. Kopf. Production of diverse brgdgts by acidobacterium solibacter usitatus in response to temperature, ph, and o2 provides a culturing perspective on brgdgt proxies and biosynthesis. Geobiology, 21:102-118, Sep 2023. URL: https://doi.org/10.1111/gbi.12525, doi:10.1111/gbi.12525. This article has 132 citations and is from a domain leading peer-reviewed journal.

19. (safronova2023fromhotto pages 10-12): Nataliya Safronova, Lisa Junghans, and James P Saenz. From hot to cold: dissecting lipidome adaptation in mycoplasma mycoides and the minimal cell jcvi-syn3b. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2023.11.10.566608, doi:10.1101/2023.11.10.566608. This article has 1 citations.

20. (stonik2024structurediversityand pages 17-19): Valentin A. Stonik, Tatyana N. Makarieva, Larisa K. Shubina, Alla G. Guzii, and Natalia V. Ivanchina. Structure diversity and properties of some bola-like natural products. Marine Drugs, 23:3, Dec 2024. URL: https://doi.org/10.3390/md23010003, doi:10.3390/md23010003. This article has 3 citations.

21. (safronova2023fromhotto pages 1-3): Nataliya Safronova, Lisa Junghans, and James P Saenz. From hot to cold: dissecting lipidome adaptation in mycoplasma mycoides and the minimal cell jcvi-syn3b. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2023.11.10.566608, doi:10.1101/2023.11.10.566608. This article has 1 citations.

22. (chiu2023membranelipidand pages 15-16): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

23. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

24. (lehmann2023adaptivelaboratoryevolution pages 6-7): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.