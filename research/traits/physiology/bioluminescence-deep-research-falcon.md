---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:35:04.278480'
end_time: '2026-06-18T11:01:16.106495'
duration_seconds: 1571.83
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: bioluminescence
  trait_identifier: traitmech:000085
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: bioluminescence
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A physiological capability to emit visible light through a luciferase-catalyzed
    reaction, frequently regulated by quorum sensing in marine bacteria such as Aliivibrio
    and Photobacterium.
  parent_traits: METPO:1000059
  synonyms: luminescent
  evidence_summary: 'DOI:10.1016/j.csbj.2018.11.003:  (Brodl, Winkler & Macheroux
    review the molecular mechanisms of bacterial bioluminescence and the luciferase
    reaction.) | DOI:10.1146/annurev.cellbio.21.012704.131001:  (Waters & Bassler
    support quorum-sensing regulation of light production in luminous bacteria.)'
  causal_graph_summary: 'bioluminescence_luciferase: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** bioluminescence
- **METPO identifier:** traitmech:000085
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological capability to emit visible light through a luciferase-catalyzed reaction, frequently regulated by quorum sensing in marine bacteria such as Aliivibrio and Photobacterium.
- **Parent traits:** METPO:1000059
- **Synonyms:** luminescent
- **Existing evidence:** DOI:10.1016/j.csbj.2018.11.003:  (Brodl, Winkler & Macheroux review the molecular mechanisms of bacterial bioluminescence and the luciferase reaction.) | DOI:10.1146/annurev.cellbio.21.012704.131001:  (Waters & Bassler support quorum-sensing regulation of light production in luminous bacteria.)
- **Existing causal graph summary:** bioluminescence_luciferase: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **bioluminescence** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/bioluminescence.yaml`.

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
- **Trait label:** bioluminescence
- **METPO identifier:** traitmech:000085
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological capability to emit visible light through a luciferase-catalyzed reaction, frequently regulated by quorum sensing in marine bacteria such as Aliivibrio and Photobacterium.
- **Parent traits:** METPO:1000059
- **Synonyms:** luminescent
- **Existing evidence:** DOI:10.1016/j.csbj.2018.11.003:  (Brodl, Winkler & Macheroux review the molecular mechanisms of bacterial bioluminescence and the luciferase reaction.) | DOI:10.1146/annurev.cellbio.21.012704.131001:  (Waters & Bassler support quorum-sensing regulation of light production in luminous bacteria.)
- **Existing causal graph summary:** bioluminescence_luciferase: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **bioluminescence** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/bioluminescence.yaml`.

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


## Microbial trait causal graph curation report: **Bioluminescence** (METPO traitmech:000085)

### Scope summary (TraitMech curation view)
**Trait definition (operational):** microbial (primarily bacterial) bioluminescence is the physiological capability to emit visible light via a **luciferase-catalyzed oxidation reaction**. In the canonical bacterial system, a heterodimeric luciferase (LuxAB) uses **FMNH2**, **molecular oxygen**, and a **long-chain aliphatic aldehyde** to yield the corresponding acid, oxidized FMN, water, and light with an emission maximum near ~490 nm (brodl2018molecularmechanismsof pages 5-8, tinikul2020bacterialluciferasemolecular pages 1-4).

**Boundary cases and near traits:**
- **Naturally bioluminescent bacteria** vs. **engineered lux reporters**: the same luxCDABE(G) cassette is widely deployed in non-luminous hosts for biosensing/viability readouts; this is an *assay/reporting implementation* boundary case and should be modeled as an assay layer or “engineered reporter system” rather than as the organism’s native ecological trait (farkas2024bioluminescentpseudomonasaeruginosa pages 1-2, łaska2024theexpressionof pages 1-2).
- **Lux (bacterial) vs. other luciferase systems**: lux is “self-sufficient” (substrates are enzymatically generated/recycled) and differs mechanistically from ATP-dependent firefly luciferase systems and many exogenous-luciferin systems (kim2024bioluminescentsystemsfor pages 3-4, tinikul2020bacterialluciferasemolecular pages 1-4).
- **Regulatory context**: in multiple marine luminous bacteria (e.g., *Aliivibrio fischeri*), light production is **density-dependent** and controlled by quorum sensing via autoinducers and LuxI/LuxR-type regulators (septer2024lightingtheway pages 3-5, waters2005quorumsensingcelltocell pages 9-11).

**What NOT to include in the core trait graph (warnings):**
- Edges about antibiotic-induced promoter induction in engineered *E. coli* lux constructs (e.g., micF:luxCDABE) are valuable for biosensor graphs but should be flagged as **assay-specific** rather than core bioluminescence mechanism edges (łaska2024theexpressionof pages 1-2).

### Key concepts & definitions (current understanding)
1. **Lux operon as the mechanistic module.** Across luminous bacteria, the enzymes required for light emission are encoded in a single-promoter operon; Brodl et al. summarize the core order as **luxCDABE** with common variants luxCDABEG and additional regulatory/auxiliary genes in some taxa (brodl2018molecularmechanismsof pages 1-5, brodl2018molecularmechanismsof pages 5-8). A visual summary of operon architectures is available in Brodl et al. Figure 1 (brodl2018molecularmechanismsof media a0e2a9f1).
2. **Biochemical reaction (luciferase).** The general reaction scheme (Scheme 1 in Brodl et al.) explicitly connects substrates (FMNH2, O2, aldehyde) to products (FMN, acid, H2O) and photon emission (~490 nm) (brodl2018molecularmechanismsof pages 5-8, brodl2018molecularmechanismsof media 91bc25ce). Tinikul et al. further emphasize that bacterial luciferase is a flavin-dependent monooxygenase using “reduced flavin mononucleotide, long-chain aldehyde and oxygen” (tinikul2020bacterialluciferasemolecular pages 1-4).
3. **Substrate supply and recycling.** LuxAB does not generate its own reduced flavin; **LuxG** supplies FMNH2 (“LuxG converts free flavin (FMN) to reduced flavin (FMNH2)”) and the **LuxCDE fatty acid reductase complex** supplies aldehyde substrate with explicit ATP- and NADPH-dependent steps (brodl2018molecularmechanismsof pages 5-8).
4. **Quorum sensing regulation (LuxI/LuxR paradigm).** In *V. fischeri*, the lux locus could be cloned into *E. coli* to yield **cell-density-dependent** luminescence; LuxI is identified as the autoinducer synthase and LuxR binds the LuxI-produced AHL (3-oxo-C6-HSL) to activate lux locus expression (septer2024lightingtheway pages 3-5). Waters & Bassler describe *V. fischeri* as the “paradigm” quorum sensing system linked to bioluminescence (waters2005quorumsensingcelltocell pages 9-11).

### Recent developments & latest research (prioritizing 2023–2024)
#### (A) Updated mechanistic/regulatory understanding in the *Vibrio fischeri* model (2024)
Septer & Visick (Journal of Bacteriology, 2024) emphasize that light production occurs **after a lag relative to growth** and that this is mediated by autoinducer production, diffusion, and response (quorum sensing) (septer2024lightingtheway pages 3-5). They report a quantitative ecological statistic: **“Light production is induced over 1,000-fold during symbiosis relative to in vitro measurements”** (septer2024lightingtheway pages 3-5), supporting an environmental/context node (“light organ environment”) that causally modulates expression and/or output.

#### (B) Engineered lux reporters as high-throughput viability/antibacterial screening tools (2024)
Farkas et al. (Scientific Reports, 2024) engineered *P. aeruginosa* and *E. coli* lux reporters for HTS; critically, they show a strong quantitative relationship between luminescence and growth/viability, reporting an **OD600–luminescence correlation r² = 0.90 (14 h)** (farkas2024bioluminescentpseudomonasaeruginosa pages 7-9). They also report antibiotic potency values derived from luminescence: IC50(tetracycline)=0.025 µg/mL; IC50(ofloxacin)=0.002 µg/mL; IC50(colistin)=0.15 µg/mL, as well as assay-quality statistics (Z’ robust 0.72 at 14 h; S/B 581; signal window 208 in one context) (farkas2024bioluminescentpseudomonasaeruginosa pages 7-9). These are strong quantitative edges, but **assay-specific**.

#### (C) Whole-cell lux biosensors for pollutant/drug response profiling (2024)
Łaska et al. (Scientific Reports, 2024) demonstrate promoter–luxCDABE constructs (recA/soxS/micF/rpoB promoters) in *E. coli* and explicitly note that expression of lux produces necessary components for light emission and “require active cellular metabolism” (łaska2024theexpressionof pages 1-2). They quantify a biosensor response statistic: **micF:luxCDABE induction 73.9%** at 0.625 µg/mL kanamycin (łaska2024theexpressionof pages 1-2).

#### (D) Comparative application framing for bioluminescent systems (2024)
Kim et al. (Int. J. Mol. Sci., 2024) provide a current synthesis comparing lux to other luciferase systems (ATP dependence, substrate issues, kinetics) and highlight that bacterial lux is genetically encoded and self-sufficient, with LuxG and LuxCDE furnishing substrates for LuxAB (kim2024bioluminescentsystemsfor pages 3-4). While focused on theranostics broadly, this review helps justify curation of “autonomous luminescence” nodes in engineered contexts.

### Current applications & real-world implementations
1. **Antibiotic and adjuvant discovery (HTS):** Lux-based whole-cell assays can sensitively and quantitatively report viable biomass and dose-dependent inhibition, enabling compound screening and bioactivity-guided fractionation (farkas2024bioluminescentpseudomonasaeruginosa pages 7-9, farkas2024bioluminescentpseudomonasaeruginosa pages 1-2).
2. **Environmental and pharmaceutical-residue monitoring:** Whole-cell biosensors with lux reporters can monitor environmental changes “in real-time,” with promoter-driven lux expression linked to analyte exposure; they are described as fast and sensitive (łaska2024theexpressionof pages 1-2).
3. **Natural symbiosis and host-microbe ecology:** In squid symbiosis, luminescence can be massively induced and is regulated by both quorum and environmental/redox regulators (ArcA example discussed in the 2024 minireview) (septer2024lightingtheway pages 3-5).

### Expert opinions / authoritative synthesis
- **Mechanistic consensus:** Brodl et al. (2018; highly cited) provide a consolidated mechanistic view that bioluminescence is “enabled by a cascade of chemical reactions catalyzed by enzymes encoded by the lux operon” and define the gene→enzyme mapping and reaction stoichiometry (brodl2018molecularmechanismsof pages 1-5, brodl2018molecularmechanismsof pages 5-8).
- **Quorum sensing as foundational regulatory paradigm:** Waters & Bassler (Annual Review, 2005; very highly cited) position *V. fischeri* bioluminescence as the canonical quorum sensing example (waters2005quorumsensingcelltocell pages 9-11). Septer & Visick (2024) update this narrative with modern ecological and regulatory layers and explicit symbiosis induction magnitude (septer2024lightingtheway pages 3-5).

### Recent statistics / quantitative data (curation-relevant)
- **Symbiosis effect size:** “induced over **1,000-fold** during symbiosis relative to in vitro” for *V. fischeri* light production (septer2024lightingtheway pages 3-5).
- **Viability proxy strength:** luminescence vs OD600 correlation **r² = 0.90** at 14 h in an *E. coli* lux+ reporter assay (farkas2024bioluminescentpseudomonasaeruginosa pages 7-9).
- **Antibiotic IC50 from luminescent assay:** tetracycline **0.025 µg/mL**, ofloxacin **0.002 µg/mL**, colistin **0.15 µg/mL** (farkas2024bioluminescentpseudomonasaeruginosa pages 7-9).
- **Biosensor induction:** micF:luxCDABE promoter induction **73.9%** at kanamycin **0.625 µg/mL** (łaska2024theexpressionof pages 1-2).

---

## Candidate nodes (grouped) and ontology grounding

| Node label | Node type (gene/protein/metabolite/process/environment/assay factor) | Suggested identifier(s) | Evidence/justification (short phrase) | Context ID(s) | Notes |
|---|---|---|---|---|---|
| bioluminescence | process | METPO:traitmech:000085; GO:0008218 | Light emission by bacterial luciferase system | (brodl2018molecularmechanismsof pages 1-5, brodl2018molecularmechanismsof pages 5-8) | GO term is general bioluminescence; METPO is target trait |
| bacterial luciferase (LuxAB) | protein | GO:0008778 | Heterodimeric luciferase catalyzes light-emitting reaction | (brodl2018molecularmechanismsof pages 5-8, tinikul2020bacterialluciferasemolecular pages 1-4) | GO:0008778 = bacterial-type luciferase activity |
| luxA | gene |  | Encodes luciferase α subunit | (brodl2018molecularmechanismsof pages 1-5, brodl2018molecularmechanismsof pages 5-8) | Gene-level identifier is taxon-specific; leave ungrounded globally |
| luxB | gene |  | Encodes luciferase β subunit | (brodl2018molecularmechanismsof pages 1-5, brodl2018molecularmechanismsof pages 5-8) | Gene-level identifier is taxon-specific |
| luxC | gene |  | Encodes NADPH-dependent acyl protein reductase | (brodl2018molecularmechanismsof pages 5-8) | Part of fatty acid reductase complex |
| luxD | gene |  | Encodes acyl-transferase | (brodl2018molecularmechanismsof pages 5-8) | Part of fatty acid reductase complex |
| luxE | gene |  | Encodes acyl-protein synthetase | (brodl2018molecularmechanismsof pages 5-8) | Part of fatty acid reductase complex |
| luxG | gene |  | Encodes flavin reductase supplying FMNH2 | (brodl2018molecularmechanismsof pages 5-8) | Accessory/core in many luminous bacteria |
| luxI | gene |  | Autoinducer synthase in LuxI/LuxR quorum sensing | (septer2024lightingtheway pages 3-5) | Regulatory gene, sometimes adjacent/in operon-linked |
| luxR | gene |  | Autoinducer-responsive transcription factor | (septer2024lightingtheway pages 3-5) | Opposite orientation to lux operon in some taxa |
| luciferase α subunit | protein |  | Catalytic α subunit contains active site | (tinikul2020bacterialluciferasemolecular pages 1-4) | Protein product of luxA |
| luciferase β subunit | protein |  | Non-catalytic β subunit stabilizes α subunit | (tinikul2020bacterialluciferasemolecular pages 1-4) | Protein product of luxB |
| fatty acid reductase complex (LuxCDE) | protein |  | Supplies long-chain aldehyde substrate | (brodl2018molecularmechanismsof pages 5-8) | Complex-level node; no stable universal CURIE identified here |
| flavin mononucleotide (FMN) | metabolite | CHEBI:17621 | Oxidized flavin substrate/product in luciferase cycle | (brodl2018molecularmechanismsof pages 5-8, tinikul2020bacterialluciferasemolecular pages 1-4) | Widely used small-molecule identifier |
| reduced flavin mononucleotide (FMNH2) | metabolite | CHEBI:57945 | Reduced flavin used by luciferase | (brodl2018molecularmechanismsof pages 5-8, tinikul2020bacterialluciferasemolecular pages 1-4) | Reduced form may vary across resources; curate with caution |
| NADPH | metabolite | CHEBI:16474 | Reducing equivalent for LuxC aldehyde synthesis | (brodl2018molecularmechanismsof pages 5-8) | Strong support for LuxC step |
| NAD(P)H | metabolite | CHEBI:16480, CHEBI:57783 | Reducing equivalent for LuxG flavin reductase | (brodl2018molecularmechanismsof pages 5-8) | Source text gives NAD(P)H; may map to NADH and/or NADPH depending taxon/enzyme |
| ATP | metabolite | CHEBI:15422 | Required for LuxE fatty acid activation | (brodl2018molecularmechanismsof pages 5-8) | Strong biochemical support |
| molecular oxygen | metabolite | CHEBI:15379 | Required oxidant in luciferase reaction | (brodl2018molecularmechanismsof pages 1-5, brodl2018molecularmechanismsof pages 5-8) | Broadly essential for bacterial light emission |
| long-chain aldehyde | metabolite | CHEBI:35746 | Luciferase substrate; aliphatic aldehydes C8-C16 | (brodl2018molecularmechanismsof pages 5-8, tinikul2020bacterialluciferasemolecular pages 1-4) | Class-level grounding only |
| tetradecanal | metabolite | CHEBI:8768 | Proposed natural aldehyde substrate | (brodl2018molecularmechanismsof pages 5-8) | Taxon/assay variation in preferred chain length |
| long-chain fatty acid | metabolite | CHEBI:15904 | Oxidation product / precursor in substrate cycle | (brodl2018molecularmechanismsof pages 5-8, tinikul2020bacterialluciferasemolecular pages 1-4) | Class-level node may be safer than specific acid |
| 3-oxo-C6-HSL autoinducer | metabolite | CHEBI:78413 | LuxI-produced AHL signal activating LuxR | (septer2024lightingtheway pages 3-5) | Also known as N-(3-oxohexanoyl)-L-homoserine lactone |
| quorum sensing | process | GO:0009372 | Autoinducer-mediated density sensing controls lux expression | (septer2024lightingtheway pages 3-5, waters2005quorumsensingcelltocell pages 9-11) | Central regulatory process, especially in Vibrio/Aliivibrio |
| lux operon | process |  | Single-promoter operon encoding light-production machinery | (brodl2018molecularmechanismsof pages 1-5, brodl2018molecularmechanismsof pages 5-8) | Operon architecture is not an ontology class in standard GO/CHEBI |
| promoter induction | assay factor |  | Reporter promoters drive luxCDABE signal changes | (łaska2024theexpressionof pages 1-2) | Assay-specific node useful for biosensor graphs |
| cell density | environment |  | Autoinducer accumulation and density-dependent luminescence | (septer2024lightingtheway pages 3-5) | Could alternatively be modeled as assay/environmental factor |
| symbiosis light organ environment | environment | ENVO:01000834 | Squid light organ induces strong luminescence in symbiosis | (septer2024lightingtheway pages 3-5) | ENVO term may need curator verification for exact host structure |
| marine habitat | environment | ENVO:00000569 | Bioluminescent bacteria mainly found in marine habitats | (brodl2018molecularmechanismsof pages 1-5) | Broad environmental context, not always required for mechanism |
| viable/metabolically active cell state | assay factor | GO:0016032; GO:0044237 | Only living, energized cells emit light; readout tracks viability | (farkas2024bioluminescentpseudomonasaeruginosa pages 1-2, farkas2024bioluminescentpseudomonasaeruginosa pages 7-9, łaska2024theexpressionof pages 1-2) | Proxy node for biosensor implementations; GO terms are approximate |
| luminescence reporter readout | assay factor |  | Signal used as proxy for viability/metabolic activity | (farkas2024bioluminescentpseudomonasaeruginosa pages 1-2, farkas2024bioluminescentpseudomonasaeruginosa pages 7-9) | Assay/readout node rather than intrinsic mechanism |
| light organ symbiosis | process | GO:0044403 | Colonization of host tissue linked to induced light production | (septer2024lightingtheway pages 3-5) | Host-association process; use if trait graph includes ecological regulation |
| autoinducer diffusion | process | GO:0097667 | Signal diffuses across membranes and between colonization sites | (septer2024lightingtheway pages 3-5) | GO mapping approximate; curate carefully if needed |
| FMN-4a-hydroxide excited state | metabolite |  | Light-emitting intermediate in luciferase reaction | (brodl2018molecularmechanismsof pages 5-8) | Mechanistically important but difficult to ground stably |
| blue-green light emission (~490 nm) | process |  | Characteristic emission peak of bacterial luciferase | (brodl2018molecularmechanismsof pages 5-8, tinikul2020bacterialluciferasemolecular pages 1-4) | Phenotypic output; may not need separate node |
| micF:luxCDABE reporter construct | assay factor |  | Example biosensor construct with 73.9% induction | (łaska2024theexpressionof pages 1-2) | Do not curate into core natural-trait graph unless assay layer is desired |


*Table: This table lists candidate nodes for a TraitMech bioluminescence graph, grouped by biological role and paired with suggested ontology identifiers where stable grounding is feasible. It is useful for separating core natural mechanism nodes from assay-specific reporter and biosensor nodes.*

## Candidate causal edges (triples) with evidence snippets

| Subject node | Predicate | Object node | Evidence snippet (verbatim short quote) | Reference (DOI/URL, year) | Context ID | Notes/uncertainty |
|---|---|---|---|---|---|---|
| luxA + luxB | encodes | LuxAB luciferase heterodimer | “The genes luxA and luxB encode the heterodimeric luciferase” | 10.1016/j.csbj.2018.11.003; https://doi.org/10.1016/j.csbj.2018.11.003 (2018) | (brodl2018molecularmechanismsof pages 5-8) | Strong, peer-reviewed; core structural edge. |
| LuxAB luciferase | catalyzes | monooxygenation of long-chain aliphatic aldehydes | “the heterodimeric enzyme luciferase (LuxAB) catalyzes the monooxygenation of aliphatic aldehydes to the corresponding acids” | 10.1016/j.csbj.2018.11.003; https://doi.org/10.1016/j.csbj.2018.11.003 (2018) | (brodl2018molecularmechanismsof pages 5-8) | Strong, peer-reviewed. |
| FMNH2 + O2 + long-chain aldehyde | are substrates for | LuxAB luciferase reaction | “Long chain aldehydes … reduced flavin mononucleotide (FMNH2) and molecular oxygen (O2) are converted by the enzyme luciferase (LuxAB)” | 10.1016/j.csbj.2018.11.003; https://doi.org/10.1016/j.csbj.2018.11.003 (2018) | (brodl2018molecularmechanismsof pages 5-8) | Strong, peer-reviewed; captures required chemistry. |
| molecular oxygen (O2) | required for | bacterial bioluminescence | “One component that nearly all bioluminescent reactions have in common is the dependence on oxygen.” | 10.1016/j.csbj.2018.11.003; https://doi.org/10.1016/j.csbj.2018.11.003 (2018) | (brodl2018molecularmechanismsof pages 1-5) | Broad statement across bioluminescent systems; still applicable to bacterial trait. |
| LuxG flavin reductase | converts | FMN to FMNH2 | “LuxG converts free flavin (FMN) to reduced flavin (FMNH2)” | 10.1016/j.csbj.2018.11.003; https://doi.org/10.1016/j.csbj.2018.11.003 (2018) | (brodl2018molecularmechanismsof pages 5-8) | Strong, peer-reviewed. |
| NAD(P)H | powers | LuxG flavin reductase activity | “LuxG as a NAD(P)H-dependent flavin reductase” | 10.1016/j.csbj.2018.11.003; https://doi.org/10.1016/j.csbj.2018.11.003 (2018) | (brodl2018molecularmechanismsof pages 5-8) | Strong, peer-reviewed. |
| LuxCDE fatty acid reductase complex | supplies | long-chain aldehyde substrate | “To supply the long-chain aldehyde substrates to the luciferase, the proteins LuxC, LuxD, and LuxE constitute a fatty acid reductase complex” | 10.1016/j.csbj.2018.11.003; https://doi.org/10.1016/j.csbj.2018.11.003 (2018) | (brodl2018molecularmechanismsof pages 5-8) | Strong, peer-reviewed. |
| ATP | required for | LuxE-mediated fatty acid activation | “At the expense of ATP the fatty acid is activated by LuxE to acyl-AMP” | 10.1016/j.csbj.2018.11.003; https://doi.org/10.1016/j.csbj.2018.11.003 (2018) | (brodl2018molecularmechanismsof pages 5-8) | Strong, peer-reviewed; specific to LuxE step. |
| NADPH | required for | LuxC-mediated aldehyde formation | “The latter intermediate is then reduced by NADPH resulting in aldehyde formation” | 10.1016/j.csbj.2018.11.003; https://doi.org/10.1016/j.csbj.2018.11.003 (2018) | (brodl2018molecularmechanismsof pages 5-8) | Strong, peer-reviewed; specific to LuxC step. |
| LuxI | synthesizes | autoinducer 3-oxo-C6-HSL | “identifying LuxI as the autoinducer synthase” and “The LuxI-produced 3-oxo-C6” | 10.1128/jb.00035-24; https://doi.org/10.1128/jb.00035-24 (2024) | (septer2024lightingtheway pages 3-5) | Strong, recent peer-reviewed review. |
| autoinducer 3-oxo-C6-HSL | diffuses across | bacterial membranes | “autoinducer can diffuse across bacterial membranes in culture” | 10.1128/jb.00035-24; https://doi.org/10.1128/jb.00035-24 (2024) | (septer2024lightingtheway pages 3-5) | Strong, recent peer-reviewed review. |
| autoinducer accumulation | permits sensing of | sufficient cell density | “its accumulation could drive changes in gene expression” and “permits the bacteria to sense when there are sufficient numbers” | 10.1128/jb.00035-24; https://doi.org/10.1128/jb.00035-24 (2024) | (septer2024lightingtheway pages 3-5) | Strong, recent peer-reviewed review; summarizes quorum-threshold logic. |
| LuxR | binds | LuxI-produced 3-oxo-C6 | “The LuxI-produced 3-oxo-C6 was later shown to bind the N-terminal domain of the transcription factor LuxR” | 10.1128/jb.00035-24; https://doi.org/10.1128/jb.00035-24 (2024) | (septer2024lightingtheway pages 3-5) | Strong, recent peer-reviewed review. |
| LuxR bound to autoinducer | activates expression of | lux locus | “bind the N-terminal domain of the transcription factor LuxR to activate the expression of the lux locus” | 10.1128/jb.00035-24; https://doi.org/10.1128/jb.00035-24 (2024) | (septer2024lightingtheway pages 3-5) | Strong, recent peer-reviewed review. |
| squid symbiosis | induces | light production >1000-fold relative to in vitro | “Light production is induced over 1,000-fold during symbiosis relative to in vitro measurements” | 10.1128/jb.00035-24; https://doi.org/10.1128/jb.00035-24 (2024) | (septer2024lightingtheway pages 3-5) | Strong, recent peer-reviewed; taxon/context-specific to V. fischeri symbiosis. |
| lux operon expression | produces | components needed for light emission | “Expression of the lux operon produces all the necessary components needed for the emission of light energy by bacteria” | 10.1038/s41598-024-83190-0; https://doi.org/10.1038/s41598-024-83190-0 (2024) | (łaska2024theexpressionof pages 1-2) | Strong, recent peer-reviewed; useful for reporter-system curation. |
| lux genes | require | active cellular metabolism | “These genes require active cellular metabolism.” | 10.1038/s41598-024-83190-0; https://doi.org/10.1038/s41598-024-83190-0 (2024) | (łaska2024theexpressionof pages 1-2) | Strong, recent peer-reviewed; applies especially to assay/readout context. |
| living, energized cells expressing luxCDABE | produce | light | “only living, energized cells expressing luxCDABE produce light” | 10.1038/s41598-024-81926-6; https://doi.org/10.1038/s41598-024-81926-6 (2024) | (farkas2024bioluminescentpseudomonasaeruginosa pages 1-2) | Strong, recent peer-reviewed; assay/implementation context. |
| luminescence | correlates with | viability / OD600 | “found them to have a strong correlation with an r2 of 0.90” | 10.1038/s41598-024-81926-6; https://doi.org/10.1038/s41598-024-81926-6 (2024) | (farkas2024bioluminescentpseudomonasaeruginosa pages 7-9) | Strong, recent peer-reviewed; assay-specific quantitative edge. |
| kanamycin 0.625 µg/mL in micF:luxCDABE reporter | increases | micF promoter induction to 73.9% | “the micF promoter induction relative to the control at a concentration of 0.625 µg/mL is 73.9%” | 10.1038/s41598-024-83190-0; https://doi.org/10.1038/s41598-024-83190-0 (2024) | (łaska2024theexpressionof pages 1-2) | Strong, recent peer-reviewed; assay-specific and not a natural bioluminescence mechanism edge. |


*Table: This table lists candidate subject-predicate-object edges for curating a microbial bioluminescence causal graph, with short supporting quotations, references, and uncertainty notes. It emphasizes core lux operon biochemistry, quorum-sensing regulation, and assay-specific reporter behavior.*

---

## Visual evidence (recommended for curator verification)
Brodl et al. provide (i) a **lux operon architecture schematic** and (ii) the **general reaction equation** as Scheme 1, both useful as curator-facing visuals for confirming node/edge structure (brodl2018molecularmechanismsof media a0e2a9f1, brodl2018molecularmechanismsof media 91bc25ce).

---

## Curation warnings (do-not-curate-yet / uncertain edges)
1. **Assay-specific vs trait mechanism:** Antibiotic-response promoter induction edges (e.g., micF:luxCDABE induction %) reflect *biosensor behavior* and should be isolated to an assay layer, not the core trait mechanism (łaska2024theexpressionof pages 1-2).
2. **Taxon-specific regulatory architecture:** lux operon adjacency/orientation of luxR and inclusion of luxI/luxF/rib genes vary by genus/strain; represent as optional nodes/edges with taxon constraints, guided by operon architecture figures (brodl2018molecularmechanismsof pages 5-8, brodl2018molecularmechanismsof media a0e2a9f1).
3. **Grey literature sources:** Some mechanistic details are also available in non-peer-reviewed or thesis sources in the retrieved corpus; for TraitMech curation, prioritize peer-reviewed evidence (e.g., Brodl 2018; Tinikul 2020; Septer & Visick 2024; Waters & Bassler 2005). Where non-peer-reviewed support was used during retrieval, it should be marked uncertain and replaced with primary literature if possible.

---

## DOI-first bibliography (with publication dates and URLs)
1. Brodl E, Winkler A, Macheroux P. **Molecular Mechanisms of Bacterial Bioluminescence.** *Computational and Structural Biotechnology Journal.* **Nov 2018**. DOI: **10.1016/j.csbj.2018.11.003**. URL: https://doi.org/10.1016/j.csbj.2018.11.003 (brodl2018molecularmechanismsof pages 1-5, brodl2018molecularmechanismsof pages 5-8)
2. Septer AN, Visick KL. **Lighting the way: how the Vibrio fischeri model microbe reveals the complexity of Earth’s “simplest” life forms.** *Journal of Bacteriology.* **May 2024**. DOI: **10.1128/jb.00035-24**. URL: https://doi.org/10.1128/jb.00035-24 (septer2024lightingtheway pages 3-5)
3. Farkas E, et al. **Bioluminescent Pseudomonas aeruginosa and Escherichia coli for whole-cell screening of antibacterial and adjuvant compounds.** *Scientific Reports.* **Dec 2024**. DOI: **10.1038/s41598-024-81926-6**. URL: https://doi.org/10.1038/s41598-024-81926-6 (farkas2024bioluminescentpseudomonasaeruginosa pages 7-9, farkas2024bioluminescentpseudomonasaeruginosa pages 1-2)
4. Łaska G, Matejczyk M, Dauksza U. **The expression of different gene constructs in Escherichia coli SM lux biosensor after exposure to drugs.** *Scientific Reports.* **Dec 2024**. DOI: **10.1038/s41598-024-83190-0**. URL: https://doi.org/10.1038/s41598-024-83190-0 (łaska2024theexpressionof pages 1-2)
5. Kim H, Jung SO, Lee S, Lee Y. **Bioluminescent Systems for Theranostic Applications.** *International Journal of Molecular Sciences.* **Jul 2024**. DOI: **10.3390/ijms25147563**. URL: https://doi.org/10.3390/ijms25147563 (kim2024bioluminescentsystemsfor pages 3-4)
6. Tinikul R, Chunthaboon P, Phonbuppha J, Paladkong T. **Bacterial luciferase: Molecular mechanisms and applications.** *The Enzymes.* **Aug 2020**. DOI: **10.1016/bs.enz.2020.06.001**. URL: https://doi.org/10.1016/bs.enz.2020.06.001 (tinikul2020bacterialluciferasemolecular pages 1-4)
7. Waters CM, Bassler BL. **QUORUM SENSING: Cell-to-Cell Communication in Bacteria.** *Annual Review of Cell and Developmental Biology.* **Nov 2005**. DOI: **10.1146/annurev.cellbio.21.012704.131001**. URL: https://doi.org/10.1146/annurev.cellbio.21.012704.131001 (waters2005quorumsensingcelltocell pages 9-11)


References

1. (brodl2018molecularmechanismsof pages 5-8): Eveline Brodl, Andreas Winkler, and Peter Macheroux. Molecular mechanisms of bacterial bioluminescence. Computational and Structural Biotechnology Journal, 16:551-564, Nov 2018. URL: https://doi.org/10.1016/j.csbj.2018.11.003, doi:10.1016/j.csbj.2018.11.003. This article has 268 citations and is from a peer-reviewed journal.

2. (tinikul2020bacterialluciferasemolecular pages 1-4): Ruchanok Tinikul, Paweenapon Chunthaboon, Jittima Phonbuppha, and Tanakan Paladkong. Bacterial luciferase: molecular mechanisms and applications. The Enzymes, 47:427-455, Aug 2020. URL: https://doi.org/10.1016/bs.enz.2020.06.001, doi:10.1016/bs.enz.2020.06.001. This article has 33 citations.

3. (farkas2024bioluminescentpseudomonasaeruginosa pages 1-2): Eszter Farkas, Geoffrey A. McKay, Lin Tao Hu, Mina Nekouei, Peying Ho, Wilfried Moreira, Chia Ching Chan, Linh Chi Dam, Karine Auclair, Samantha Gruenheid, Lyle Whyte, Peter Dedon, and Dao Nguyen. Bioluminescent pseudomonas aeruginosa and escherichia coli for whole-cell screening of antibacterial and adjuvant compounds. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-81926-6, doi:10.1038/s41598-024-81926-6. This article has 9 citations and is from a peer-reviewed journal.

4. (łaska2024theexpressionof pages 1-2): Grażyna Łaska, Marzena Matejczyk, and Urszula Dauksza. The expression of different gene constructs in escherichia coli sm lux biosensor after exposure to drugs. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-83190-0, doi:10.1038/s41598-024-83190-0. This article has 3 citations and is from a peer-reviewed journal.

5. (kim2024bioluminescentsystemsfor pages 3-4): Hyemin Kim, Seung Oh Jung, Seungchan Lee, and Yujin Lee. Bioluminescent systems for theranostic applications. International Journal of Molecular Sciences, 25:7563, Jul 2024. URL: https://doi.org/10.3390/ijms25147563, doi:10.3390/ijms25147563. This article has 8 citations.

6. (septer2024lightingtheway pages 3-5): Alecia N. Septer and Karen L. Visick. Lighting the way: how the <i>vibrio fischeri</i> model microbe reveals the complexity of earth’s “simplest” life forms. May 2024. URL: https://doi.org/10.1128/jb.00035-24, doi:10.1128/jb.00035-24. This article has 19 citations and is from a peer-reviewed journal.

7. (waters2005quorumsensingcelltocell pages 9-11): Christopher M. Waters and Bonnie L. Bassler. Quorum sensing: cell-to-cell communication in bacteria. Annual Review of Cell and Developmental Biology, 21:319-346, Nov 2005. URL: https://doi.org/10.1146/annurev.cellbio.21.012704.131001, doi:10.1146/annurev.cellbio.21.012704.131001. This article has 3027 citations and is from a domain leading peer-reviewed journal.

8. (brodl2018molecularmechanismsof pages 1-5): Eveline Brodl, Andreas Winkler, and Peter Macheroux. Molecular mechanisms of bacterial bioluminescence. Computational and Structural Biotechnology Journal, 16:551-564, Nov 2018. URL: https://doi.org/10.1016/j.csbj.2018.11.003, doi:10.1016/j.csbj.2018.11.003. This article has 268 citations and is from a peer-reviewed journal.

9. (brodl2018molecularmechanismsof media a0e2a9f1): Eveline Brodl, Andreas Winkler, and Peter Macheroux. Molecular mechanisms of bacterial bioluminescence. Computational and Structural Biotechnology Journal, 16:551-564, Nov 2018. URL: https://doi.org/10.1016/j.csbj.2018.11.003, doi:10.1016/j.csbj.2018.11.003. This article has 268 citations and is from a peer-reviewed journal.

10. (brodl2018molecularmechanismsof media 91bc25ce): Eveline Brodl, Andreas Winkler, and Peter Macheroux. Molecular mechanisms of bacterial bioluminescence. Computational and Structural Biotechnology Journal, 16:551-564, Nov 2018. URL: https://doi.org/10.1016/j.csbj.2018.11.003, doi:10.1016/j.csbj.2018.11.003. This article has 268 citations and is from a peer-reviewed journal.

11. (farkas2024bioluminescentpseudomonasaeruginosa pages 7-9): Eszter Farkas, Geoffrey A. McKay, Lin Tao Hu, Mina Nekouei, Peying Ho, Wilfried Moreira, Chia Ching Chan, Linh Chi Dam, Karine Auclair, Samantha Gruenheid, Lyle Whyte, Peter Dedon, and Dao Nguyen. Bioluminescent pseudomonas aeruginosa and escherichia coli for whole-cell screening of antibacterial and adjuvant compounds. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-81926-6, doi:10.1038/s41598-024-81926-6. This article has 9 citations and is from a peer-reviewed journal.