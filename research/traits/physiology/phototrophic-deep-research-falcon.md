---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-29T13:46:01.148710'
end_time: '2026-06-29T14:15:46.669632'
duration_seconds: 1785.52
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: phototrophic
  trait_identifier: METPO:1000660
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: phototrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type characterized by the use of light as the primary energy
    source for metabolic processes, regardless of carbon source.
  parent_traits: METPO:1000631
  synonyms: TT_phototroph, aerobic_anoxygenic_phototrophy, phototroph
  evidence_summary: 'DOI:10.3389/fmicb.2011.00165: use light as the energy source
    (Review supports light-driven ATP and reductant generation by phototrophic bacteria.)
    | DOI:10.1093/femsre/fuv032: bacteriochlorophyll-containing reaction centers (Review
    supports bacteriochlorophyll reaction centers in aerobic anoxygenic phototrophs.)'
  causal_graph_summary: 'phototrophic_light_energy_capture: 13 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** phototrophic
- **METPO identifier:** METPO:1000660
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of light as the primary energy source for metabolic processes, regardless of carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_phototroph, aerobic_anoxygenic_phototrophy, phototroph
- **Existing evidence:** DOI:10.3389/fmicb.2011.00165: use light as the energy source (Review supports light-driven ATP and reductant generation by phototrophic bacteria.) | DOI:10.1093/femsre/fuv032: bacteriochlorophyll-containing reaction centers (Review supports bacteriochlorophyll reaction centers in aerobic anoxygenic phototrophs.)
- **Existing causal graph summary:** phototrophic_light_energy_capture: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **phototrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/phototrophic.yaml`.

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
- **Trait label:** phototrophic
- **METPO identifier:** METPO:1000660
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of light as the primary energy source for metabolic processes, regardless of carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_phototroph, aerobic_anoxygenic_phototrophy, phototroph
- **Existing evidence:** DOI:10.3389/fmicb.2011.00165: use light as the energy source (Review supports light-driven ATP and reductant generation by phototrophic bacteria.) | DOI:10.1093/femsre/fuv032: bacteriochlorophyll-containing reaction centers (Review supports bacteriochlorophyll reaction centers in aerobic anoxygenic phototrophs.)
- **Existing causal graph summary:** phototrophic_light_energy_capture: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **phototrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/phototrophic.yaml`.

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


# Microbial Trait Causal Graph Research Report: Phototrophic (METPO:1000660)

## 1. Trait Scope Summary

The **phototrophic** trait (METPO:1000660) describes a trophic type characterized by the use of light as the primary energy source for metabolic processes, regardless of carbon source. This trait encompasses two independently evolved light-energy transduction systems: **(i) chlorophototrophy**, based on (bacterio)chlorophyll-containing reaction centers that drive cyclic or linear electron transport and generate a proton motive force (PMF) for ATP synthesis; and **(ii) retinalophototrophy**, based on microbial rhodopsins (e.g., proteorhodopsin) that function as single-protein light-driven proton pumps, also generating PMF for ATP production (peterson2023usinglightfor pages 1-5).

Chlorophototrophy is currently known across at least nine bacterial phyla: Cyanobacteria (oxygenic), Proteobacteria (purple bacteria), Chlorobi (green sulfur bacteria), Firmicutes (heliobacteria), Chloroflexi, Acidobacteriota, Gemmatimonadetes, Armatimonadota, and Vulcanimicrbiota (Eremiobacterota) (nishihara2024illuminatingthecoevolution pages 2-3, niederman2024whatweare pages 19-20). Retinalophototrophy is far more phylogenetically widespread, occurring across all three domains of life due to the ease of horizontal gene transfer of a single rhodopsin gene plus four genes for retinal cofactor synthesis, compared to ~30 genes for chlorophototrophy (peterson2023usinglightfor pages 1-5).

### Boundary Cases
- **Aerobic anoxygenic phototrophs (AAPs)** are obligate aerobes that use anoxygenic photosynthesis as a supplementary energy source alongside aerobic respiration (yurkov2025phenomenaldiversityof pages 1-3). They represent a critical boundary case where phototrophy is facultative rather than obligate.
- **Dual phototrophy** systems exist: some organisms possess genes for both bacteriochlorophyll-based and rhodopsin-based phototrophy simultaneously, such as *Sphingomonas* sp. strain AAP5 (yurkov2025phenomenaldiversityof pages 28-29, yurkov2025phenomenaldiversityof pages 19-21).
- **Rhodopsin-based photoheterotrophy** is mechanistically simpler than chlorophototrophy and does not involve redox reactions or carbon fixation; it should be considered a distinct sub-mechanism within the phototrophic trait (peterson2023usinglightfor pages 1-5).

The following conceptual diagram illustrates the overall causal graph structure for the phototrophic trait:

![Microbial Phototrophy Causal Graph](artifact:artifact-02)

*Image: Conceptual flowchart of the core mechanisms underlying the microbial phototrophic trait, showing chlorophototrophic and retinalophototrophic energy-transduction routes, pigment biosynthesis support, regulatory controls, and photoprotective processes. The diagram emphasizes causal flow from environmental inputs to proton motive force and ATP production.*

## 2. Causal Graph Entities (Candidate Nodes)

The following table presents candidate nodes grouped by entity type, with suggested ontology grounding where available:

| Node Label | Node Type | Suggested CURIE | Notes |
|---|---|---|---|
| Light (photons/solar radiation) | environmental_factor | ENVO:01001023 | Primary external energy input for phototrophy; absorbed by (bacterio)chlorophylls or rhodopsins to initiate energy transduction (yurkov2025phenomenaldiversityof pages 3-5, peterson2023usinglightfor pages 1-5). |
| Oxygen (O2) | environmental_factor | CHEBI:15379 | Key boundary condition for aerobic anoxygenic phototrophy; influences redox tuning, pigment synthesis, and photooxidative stress (yurkov2025phenomenaldiversityof pages 12-14, yurkov2025phenomenaldiversityof pages 16-18). |
| Diurnal cycle | environmental_factor | label only | Alternating dark/light regime strongly regulates BChl synthesis, photosystem replenishment, and survival physiology in facultative phototrophs (tinguely2023diurnalcyclesdrive pages 1-2, tinguely2023diurnalcyclesdrive pages 5-8). |
| bchI (Mg-chelatase subunit I) | gene/protein | KEGG:K03405 | Photosynthesis gene cluster component; part of Mg-chelatase required for committing step of (bacterio)chlorophyll biosynthesis (nishihara2024illuminatingthecoevolution pages 8-9, nishihara2024illuminatingthecoevolution pages 9-9). |
| bchD (Mg-chelatase subunit D) | gene/protein | KEGG:K03404 | Mg-chelatase ATPase subunit in conserved BChl synthesis modules; present in phototrophic gene clusters (yurkov2025phenomenaldiversityof pages 14-15, nishihara2024illuminatingthecoevolution pages 8-9). |
| bchH (Mg-chelatase subunit H) | gene/protein | label only | Porphyrin-binding Mg-chelatase subunit; conserved in BChl synthesis regions of the PGC (yurkov2025phenomenaldiversityof pages 12-14, nishihara2024illuminatingthecoevolution pages 8-9). |
| bchM (Mg-protoporphyrin IX methyltransferase) | gene/protein | label only | Conserved pigment synthesis gene downstream of Mg-chelation step in bacteriochlorophyll synthesis (yurkov2025phenomenaldiversityof pages 12-14, nishihara2024illuminatingthecoevolution pages 8-9). |
| bchL | gene/protein | label only | DPOR subunit; part of dark-operative protochlorophyllide reductase complex required for pigment reduction steps in BChl synthesis (nishihara2024illuminatingthecoevolution pages 8-9, nishihara2024illuminatingthecoevolution pages 9-9). |
| bchN | gene/protein | label only | DPOR catalytic subunit; homologous to chlorophyllide reductase-related systems in pigment biosynthesis evolution (nishihara2024illuminatingthecoevolution pages 8-9, nishihara2024illuminatingthecoevolution pages 9-9). |
| bchB | gene/protein | label only | DPOR catalytic partner; supports dark-operative reduction in chlorophyllide/protochlorophyllide pathway (nishihara2024illuminatingthecoevolution pages 8-9, nishihara2024illuminatingthecoevolution pages 9-9). |
| bchX | gene/protein | label only | COR subunit; part of bacteriochlorin-forming reduction machinery in bacteriochlorophyll synthesis (yurkov2025phenomenaldiversityof pages 12-14, nishihara2024illuminatingthecoevolution pages 9-9). |
| bchY | gene/protein | label only | COR catalytic subunit in chlorophyllide a reduction to bacteriochlorophyll intermediates (yurkov2025phenomenaldiversityof pages 12-14, nishihara2024illuminatingthecoevolution pages 9-9). |
| bchZ | gene/protein | label only | COR catalytic partner in bacteriochlorophyll-specific reduction steps (yurkov2025phenomenaldiversityof pages 12-14, nishihara2024illuminatingthecoevolution pages 9-9). |
| pufL | gene/protein | label only | Type II reaction center L subunit in puf operon; forms RC core in purple bacteria/AAPs (yurkov2025phenomenaldiversityof pages 12-14, yurkov2025phenomenaldiversityof pages 3-5). |
| pufM | gene/protein | label only | Type II reaction center M subunit in puf operon; pairs with PufL in photochemical core (yurkov2025phenomenaldiversityof pages 12-14, yurkov2025phenomenaldiversityof pages 3-5). |
| puhA (RC H subunit) | gene/protein | label only | Reaction center H subunit gene in RC assembly region; contributes to Type II RC architecture (yurkov2025phenomenaldiversityof pages 12-14, yurkov2025phenomenaldiversityof pages 3-5). |
| pufBA (LH1 alpha/beta apoproteins) | gene/protein | label only | Encodes LH1 core antenna apoproteins closely associated with the RC in Type II phototrophs (yurkov2025phenomenaldiversityof pages 12-14, yurkov2025phenomenaldiversityof pages 3-5). |
| pucAB (LH2 apoproteins) | gene/protein | label only | Encodes peripheral LH2 antenna proteins; often outside the main PGC and expanded under low light (yurkov2025phenomenaldiversityof pages 14-15, yurkov2025phenomenaldiversityof pages 18-19). |
| ppsR/crtJ (photosynthesis gene regulator) | gene/protein | label only | Redox/light-responsive transcriptional repressor of BChl/carotenoid/photosynthesis genes under aerobic conditions (yurkov2025phenomenaldiversityof pages 14-15, yurkov2025phenomenaldiversityof pages 27-28). |
| ppaA/aerR (antirepressor) | gene/protein | label only | Regulatory antirepressor module associated with photosynthesis gene expression in PGC-containing bacteria (yurkov2025phenomenaldiversityof pages 12-14, yurkov2025phenomenaldiversityof pages 27-28). |
| acsF (aerobic cyclase) | gene/protein | label only | Aerobic Mg-protoporphyrin IX monomethyl ester cyclase enabling BChl synthesis in oxygenated conditions; characteristic of AAPs (yurkov2025phenomenaldiversityof pages 12-14, yurkov2025phenomenaldiversityof pages 1-3). |
| Proteorhodopsin / microbial rhodopsin | gene/protein | label only | Single-gene retinal-dependent light-driven proton pump; mediates retinalophototrophy/photoheterotrophy distinct from chlorophototrophy (peterson2023usinglightfor pages 1-5, peterson2023usinglightfor pages 11-15). |
| Cytochrome c2 | gene/protein | label only | Soluble electron carrier returning electrons from cytochrome bc1 to Type II RC during cyclic electron transport (yurkov2025phenomenaldiversityof pages 12-14, yurkov2025phenomenaldiversityof pages 3-5). |
| PscA (Type I RC core protein, GSB) | gene/protein | label only | Homodimeric Type I RC core apoprotein binding RC and core antenna pigments in green sulfur bacteria/chloracidobacteria (niederman2024whatweare pages 1-2, niederman2024whatweare pages 9-11). |
| PscB (Type I RC [4Fe-4S] subunit) | gene/protein | label only | Type I RC iron-sulfur subunit carrying terminal [4Fe-4S] centers and interfacing functionally with FMO-mediated energy delivery (niederman2024whatweare pages 1-2, niedzwiedzki2025tripletstatedynamicsof pages 1-2). |
| PscC (cytochrome cZ, Type I RC) | gene/protein | label only | Cytochrome donor subunit(s) that re-reduce the Type I RC special pair in green sulfur bacteria (niederman2024whatweare pages 1-2, niederman2024whatweare pages 9-11). |
| FMO protein (Fenna-Matthews-Olson) | gene/protein | label only | Trimeric bacteriochlorophyll a-binding antenna protein transferring excitations from chlorosome/baseplate to Type I RC (xie2023cryoemstructureof pages 1-2, niederman2024whatweare pages 5-7). |
| Mg-chelatase (BchI/D/H complex) | enzyme_complex | EC:6.6.1.1 | Catalyzes Mg insertion into protoporphyrin IX, the committing step of chlorophyll/bacteriochlorophyll synthesis (nishihara2024illuminatingthecoevolution pages 8-9, nishihara2024illuminatingthecoevolution pages 9-9). |
| Dark-operative protochlorophyllide reductase (DPOR, BchL/N/B) | enzyme_complex | EC:1.3.7.7 | Reductive enzyme complex in chlorophyllide/protochlorophyllide pathway; essential to minimal (B)Chl synthesis route (nishihara2024illuminatingthecoevolution pages 8-9, nishihara2024illuminatingthecoevolution pages 9-9). |
| Chlorophyllide a reductase (COR, BchX/Y/Z) | enzyme_complex | EC:1.3.7.15 | Bacteriochlorophyll-specific reductase producing bacteriochlorin-like light-absorbing properties (nishihara2024illuminatingthecoevolution pages 9-9). |
| Type II Reaction Center (RC) complex | enzyme_complex | label only | Pheophytin-quinone type photochemical core of purple bacteria/AAPs; contains BChl, BPhe, quinones, and non-heme iron (yurkov2025phenomenaldiversityof pages 3-5). |
| Type I Reaction Center-Photosystem (RC-PS) complex | enzyme_complex | label only | Fe-S type photochemical complex with homodimeric core and terminal [4Fe-4S] acceptors, characteristic of GSB/heliobacteria/chloracidobacteria (niederman2024whatweare pages 1-2). |
| Light-Harvesting Complex 1 (LH1) | enzyme_complex | label only | Core antenna surrounding or adjoining Type II RC; transfers absorbed energy to RC special pair (yurkov2025phenomenaldiversityof pages 3-5, yurkov2025phenomenaldiversityof pages 1-3). |
| Light-Harvesting Complex 2 (LH2) | enzyme_complex | label only | Peripheral antenna complex variably present in AAPs/purple bacteria; often increased under low light (yurkov2025phenomenaldiversityof pages 3-5, yurkov2025phenomenaldiversityof pages 18-19). |
| Cytochrome bc1 complex | enzyme_complex | EC:7.1.1.8; GO:0045275 | Oxidizes quinol in the Q cycle, transfers electrons to cytochrome c2/c-type donors, and contributes to proton translocation (yurkov2025phenomenaldiversityof pages 3-5, blankenship2021molecularmechanismsof pages 114-117). |
| F1Fo-ATP synthase | enzyme_complex | EC:7.1.2.2; GO:0045259 | Uses proton motive force generated by photosynthetic electron transport or rhodopsin-mediated pumping to synthesize ATP (yurkov2025phenomenaldiversityof pages 3-5, peterson2023usinglightfor pages 11-15). |
| Chlorosome (self-assembled BChl antenna) | cellular_structure | label only | Large self-assembled bacteriochlorophyll antenna in green sulfur bacteria and related taxa; feeds excitation to FMO/baseplate (xie2023cryoemstructureof pages 1-2, niedzwiedzki2025tripletstatedynamicsof pages 1-2). |
| Bacteriochlorophyll a (BChl a) | chemical/metabolite | CHEBI:27888 | Principal photopigment in many anoxygenic phototrophs and AAPs; forms special pairs and antenna pigments (yurkov2025phenomenaldiversityof pages 3-5, yurkov2025phenomenaldiversityof pages 1-3). |
| Bacteriochlorophyll g | chemical/metabolite | label only | Characteristic bacteriochlorophyll of heliobacteria and some Type I RC systems (niederman2024whatweare pages 22-23). |
| Chlorophyll a | chemical/metabolite | CHEBI:18230 | Canonical pigment of oxygenic phototrophs; also present in some unusual anoxygenic systems such as Chloracidobacterium thermophilum (yurkov2025phenomenaldiversityof pages 21-23). |
| Bacteriopheophytin (BPhe) | chemical/metabolite | label only | Primary/early electron acceptor pigment in Type II RC electron transfer chain after excited BChl (yurkov2025phenomenaldiversityof pages 3-5). |
| Carotenoids | chemical/metabolite | CHEBI:23044 | Accessory pigments for light capture and photoprotection; scavenge singlet oxygen and quench harmful excited states (yurkov2025phenomenaldiversityof pages 10-12). |
| Ubiquinone (Coenzyme Q) | chemical/metabolite | CHEBI:16389 | Quinone electron carrier in Type II phototrophs/AAPs; reduced at QA/QB and reoxidized by cytochrome bc1 complex (yurkov2025phenomenaldiversityof pages 3-5, blankenship2021molecularmechanismsof pages 114-117). |
| Menaquinone | chemical/metabolite | CHEBI:18151 | Quinone carrier associated with some anoxygenic phototrophs, including green nonsulfur/heliobacterial systems (blankenship2021molecularmechanismsof pages 145-148, niederman2024whatweare pages 22-23). |
| all-trans-retinal | chemical/metabolite | CHEBI:17898 | Chromophore covalently bound by microbial rhodopsins; required for light absorption in retinalophototrophy (peterson2023usinglightfor pages 1-5, peterson2023usinglightfor pages 11-15). |
| Protoporphyrin IX | chemical/metabolite | CHEBI:15430 | Tetrapyrrole precursor for Mg-chelatase in chlorophyll/bacteriochlorophyll biosynthesis (nishihara2024illuminatingthecoevolution pages 9-9). |
| ATP | chemical/metabolite | CHEBI:15422 | Energy currency generated by photophosphorylation or rhodopsin-driven proton motive force (yurkov2025phenomenaldiversityof pages 3-5, peterson2023usinglightfor pages 11-15). |
| Ferredoxin | chemical/metabolite | label only | Low-potential electron carrier reduced by Type I RC Fe-S pathways and involved in downstream redox metabolism (niederman2024whatweare pages 1-2, xie2023cryoemstructureof pages 1-2). |
| Cyclic electron transport | biological_process | GO:0010598 | Light-driven cyclic flow around anoxygenic reaction centers generating electrochemical potential without net oxygen evolution (yurkov2025phenomenaldiversityof pages 1-3, yurkov2025phenomenaldiversityof pages 3-5). |
| Proton motive force generation | biological_process | label only | Electrochemical gradient formation across membrane via quinone/cytochrome bc1 cycling or rhodopsin proton pumping (yurkov2025phenomenaldiversityof pages 3-5, peterson2023usinglightfor pages 11-15). |
| Photophosphorylation | biological_process | GO:0015986 | ATP synthesis driven by light-generated proton motive force in phototrophic membranes (yurkov2025phenomenaldiversityof pages 1-3, yurkov2025phenomenaldiversityof pages 3-5). |
| BChl biosynthesis | biological_process | label only | Multi-enzyme tetrapyrrole pathway requiring Mg-chelatase, methyltransferase, cyclase, and reductases (nishihara2024illuminatingthecoevolution pages 8-9, nishihara2024illuminatingthecoevolution pages 9-9). |
| Photoprotection | biological_process | label only | Protective dissipation/scavenging processes preventing photooxidative damage, especially via carotenoids (yurkov2025phenomenaldiversityof pages 10-12). |
| Photooxidative stress response | biological_process | label only | Cellular response to combined light, oxygen, and chlorophyll-derived ROS; especially important in AAPs (yurkov2025phenomenaldiversityof pages 16-18, tinguely2023diurnalcyclesdrive pages 1-2). |
| Light-dependent gene regulation | biological_process | label only | Regulation of pigment and photosystem genes by light, photoreceptors, and redox-responsive regulators such as PpsR/CrtJ (yurkov2025phenomenaldiversityof pages 28-29, yurkov2025phenomenaldiversityof pages 27-28). |
| Bacteriochlorophyll biosynthesis pathway | pathway | MetaCyc:PWY-5531 | Core pigment synthesis pathway underpinning chlorophototrophy; represented by conserved bch modules in PGCs (yurkov2025phenomenaldiversityof pages 12-14, nishihara2024illuminatingthecoevolution pages 8-9). |
| Carotenoid biosynthesis pathway | pathway | label only | Accessory pigment pathway encoded by crt genes; contributes to light capture and photoprotection (yurkov2025phenomenaldiversityof pages 14-15, yurkov2025phenomenaldiversityof pages 10-12). |
| Photosynthetic Gene Cluster (PGC, superoperon) | pathway | label only | Conserved superoperon encoding pigment synthesis, RC/LH structural genes, and regulators in many anoxygenic phototrophs/AAPs (yurkov2025phenomenaldiversityof pages 12-14). |
| Retinal biosynthesis pathway | pathway | label only | Small cofactor-production pathway enabling rhodopsin phototrophy; typically far simpler than chlorophototrophy gene sets (peterson2023usinglightfor pages 1-5). |


*Table: This table lists candidate TraitMech nodes for the microbial phototrophic trait, grouped by entity type and grounded to available ontology or database identifiers where possible. It is designed to support curation of causal graph nodes and highlights mechanistic relevance with source-backed notes.*

## 3. Evidence-Backed Causal Edges

The following table presents 30 candidate causal edges as subject-predicate-object triples, each backed by DOI references and supporting evidence snippets:

| Edge ID | Subject | Predicate | Object | Reference (DOI) | Supporting Snippet | Notes/Confidence |
|---|---|---|---|---|---|---|
| E01 | Light | enables | Reaction center photoexcitation | 10.3390/microorganisms13112446 | "Light energy at varying wavelengths is captured by pigments in light-harvesting (LH) complexes and funneled to the reaction center (RC)" (yurkov2025phenomenaldiversityof pages 3-5) | Strong; directly states light input to RC excitation in AAPs. |
| E02 | Light-harvesting complex | transfers_energy_to | Reaction center | 10.3390/microorganisms13112446 | "The photosynthetic apparatus consists of two main components: the reaction center and light-harvesting complexes" and light is "captured by LH complexes and directed to the RC" (yurkov2025phenomenaldiversityof pages 1-3, yurkov2025phenomenaldiversityof pages 3-5) | Strong; core antenna-to-RC edge. |
| E03 | Bacteriochlorophyll a | mediates | Reaction center photoexcitation | 10.3390/microorganisms13112446 | "BChl a molecules (P) become photooxidized" (yurkov2025phenomenaldiversityof pages 3-5) | Strong; BChl a is the RC photochemical pigment. |
| E04 | Type II reaction center | reduces | Ubiquinone | 10.3390/microorganisms13112446 | "Electrons pass through bacteriopheophytin (BPhe) to ubiquinone acceptors at QA and QB sites" (yurkov2025phenomenaldiversityof pages 3-5) | Strong; direct photochemical electron transfer step. |
| E05 | Reduced ubiquinone (quinol) | donates_electrons_to | Cytochrome bc1 complex | 10.1002/9780470758472 | "reduced quinol is released into the membrane and subsequently reoxidized by the cytochrome bc1 complex" (blankenship2021molecularmechanismsof pages 114-117) | Strong; canonical Q-cycle step. |
| E06 | Cytochrome bc1 complex | generates | Proton motive force | 10.3390/microorganisms13112446 | "generates an electrochemical potential across the membrane by transferring protons from the cytoplasm to the periplasm through the Q cycle" (yurkov2025phenomenaldiversityof pages 3-5) | Strong; direct mechanism for PMF generation. |
| E07 | Cytochrome c2 | reduces | Reaction center special pair P+ | 10.3390/microorganisms13112446 | "electrons are transferred to cytochrome c2, which returns to the reaction center" (yurkov2025phenomenaldiversityof pages 3-5) | Strong for Type II cyclic flow in AAPs/purple bacteria. |
| E08 | Proton motive force | drives | F1Fo-ATP synthase | 10.1002/9780470758472 | "This proton motive force is then utilized by ATP synthase to drive phosphate bond energy formation in ATP" (blankenship2021molecularmechanismsof pages 114-117) | Strong; classic chemiosmotic coupling. |
| E09 | F1Fo-ATP synthase | produces | ATP | 10.3390/microorganisms13112446 | "The resulting proton gradient is then utilized by ATP synthase to produce ATP via photophosphorylation" (yurkov2025phenomenaldiversityof pages 3-5) | Strong; direct ATP output edge. |
| E10 | Mg-chelatase | catalyzes | Mg insertion into protoporphyrin IX | 10.1073/pnas.2322120121 | "Mg-chelatase catalyzes the committing step of BChl synthesis" (nishihara2024illuminatingthecoevolution pages 9-9) | Strong; substrate inferred from enzyme identity, well established. |
| E11 | bchI | part_of | Mg-chelatase complex | 10.1073/pnas.2322120121 | "including BchI, BchD, BchH (Mg-chelatase components)" (nishihara2024illuminatingthecoevolution pages 8-9) | Strong; component assignment explicit. |
| E12 | bchD | part_of | Mg-chelatase complex | 10.1073/pnas.2322120121 | "including BchI, BchD, BchH (Mg-chelatase components)" (nishihara2024illuminatingthecoevolution pages 8-9) | Strong. |
| E13 | bchH | part_of | Mg-chelatase complex | 10.1073/pnas.2322120121 | "including BchI, BchD, BchH (Mg-chelatase components)" (nishihara2024illuminatingthecoevolution pages 8-9) | Strong. |
| E14 | Dark-operative protochlorophyllide reductase (BchL/N/B) | reduces | Protochlorophyllide / chlorophyllide intermediate | 10.1073/pnas.2322120121 | "(proto)chlorophyllide reductase... essential for conferring the light-absorbing capacity" (nishihara2024illuminatingthecoevolution pages 9-9) | Moderate-strong; exact substrate wording generalized from source. |
| E15 | Chlorophyllide a reductase (BchX/Y/Z) | reduces | Chlorophyllide a to bacteriochlorophyll intermediate | 10.1073/pnas.2322120121 | "light-operative versions (BchYZ) are homologous" and reductases are "critical for conferring the light-absorbing capacity characteristic of bacteriochlorin pigments" (nishihara2024illuminatingthecoevolution pages 9-9) | Moderate; mechanistically standard but source phrasing is evolutionary/functional. |
| E16 | Carotenoids | quench | Singlet oxygen | 10.3390/microorganisms13112446 | "Carotenoids protect cells by scavenging singlet oxygen and radicals" (yurkov2025phenomenaldiversityof pages 10-12) | Strong; direct photoprotection edge. |
| E17 | Carotenoids | protects_against | Photooxidative stress | 10.3390/microorganisms13112446 | "preventing light damage during intense illumination" and "serving as a protective mechanism against photooxidative stress" (yurkov2025phenomenaldiversityof pages 10-12) | Strong; useful higher-level process edge. |
| E18 | ppsR/crtJ | represses | BChl and carotenoid gene expression | 10.3390/microorganisms13112446 | "crtJ (represses BChl and carotenoid expression under aerobic conditions)" (yurkov2025phenomenaldiversityof pages 14-15) | Strong; direct regulatory edge. |
| E19 | ppaA/aerR | antirepresses_or_promotes | Photosynthesis gene expression | 10.3390/microorganisms13112446 | "ppaA/aerR" are included among regulatory genes in the PGC (yurkov2025phenomenaldiversityof pages 12-14) | Moderate; role as antirepressor is standard but source excerpt is brief. Mark as somewhat inferred. |
| E20 | Proteorhodopsin | pumps | Protons across membrane | 10.1101/2022.12.06.519405 | "pump one proton per photon absorbed" (peterson2023usinglightfor pages 1-5) | Strong; direct mechanism of retinalophototrophy. |
| E21 | all-trans-retinal | is_cofactor_for | Proteorhodopsin | 10.1101/2022.12.06.519405 | "covalently bound to all-trans-retinal pigment" (peterson2023usinglightfor pages 1-5) | Strong; direct cofactor relationship. |
| E22 | Chlorosome | transfers_excitation_to | FMO protein | 10.1073/pnas.2216734120 | "The energy absorbed by the chlorosome is transferred through Fenna-Matthews-Olson proteins" (xie2023cryoemstructureof pages 1-2) | Strong for green sulfur bacteria and related chlorosome-containing taxa. |
| E23 | FMO protein | transfers_excitation_to | Type I reaction center | 10.1073/pnas.2216734120 | "The energy absorbed by the chlorosome is transferred through Fenna-Matthews-Olson proteins to the reaction center" (xie2023cryoemstructureof pages 1-2) | Strong. |
| E24 | Type I reaction center | reduces | Ferredoxin via [4Fe-4S] clusters | 10.3390/biom14030311 | "Type I RC... (Fe-S type, ferredoxin reducing)" and "electrons were transferred directly from the A0 acceptor to the FX [4Fe-4S] component" (niederman2024whatweare pages 1-2) | Strong; hallmark of Type I RCs. |
| E25 | Oxygen | enables | Aerobic anoxygenic phototrophy | 10.3390/microorganisms13112446 | AAPs are "obligate aerobes" and combine anoxygenic photosynthesis with "obligate aerobic respiration" (yurkov2025phenomenaldiversityof pages 1-3) | Strong for AAP subclass; should not be generalized to all phototrophy. |
| E26 | Dark phase | upregulates | BChl biosynthesis genes | 10.1038/s43705-023-00334-5 | "BChl a biosynthesis genes... are consistently downregulated during the day and upregulated at night" (tinguely2023diurnalcyclesdrive pages 5-8) | Strong, but taxon/condition specific to facultative AAP under diurnal cycling. |
| E27 | Light | inhibits | BChl synthesis in AAPs | 10.3390/microorganisms13112446 | "BChl is produced exclusively or predominantly in darkness" and "Light exposure immediately halts pigment synthesis" (yurkov2025phenomenaldiversityof pages 16-18) | Strong for many AAPs; not universal across all phototrophs. |
| E28 | Carbon limitation | induces | Photosynthesis gene expression | 10.3390/microorganisms13112446 | "AAPs switch between aerobic respiration during nutrient abundance... and photosynthesis during carbon limitation" and "Carbon limitation appears to be a key trigger for transcriptional induction" (yurkov2025phenomenaldiversityof pages 19-21, yurkov2025phenomenaldiversityof pages 28-29) | Moderate-strong; ecological/regulatory edge. |
| E29 | Photosynthetic gene cluster (PGC) | encodes | RC/LH/bch/crt genes | 10.3390/microorganisms13112446 | "The photosynthetic gene cluster (PGC) is a superoperon encoding BChl synthesis genes (bch), carotenoid genes (crt), and reaction center/light-harvesting complex proteins (puf and puh)" (yurkov2025phenomenaldiversityof pages 12-14) | Strong; central genomic organization edge. |
| E30 | Photosynthetic growth | yields | Increased ATP relative to dark growth | 10.3390/microorganisms13112446 | "photosynthetic growth in Cg. litoralis yielded 2.4 times more ATP than heterotrophic dark growth" (yurkov2025phenomenaldiversityof pages 18-19) | Strong but species-specific quantitative edge; curate with note on taxon specificity. |


*Table: This table lists candidate subject-predicate-object edges for a phototrophic TraitMech causal graph, with DOI-backed snippets and curation confidence notes. It emphasizes core light-energy capture, electron transport, pigment biosynthesis, regulation, and boundary-case mechanisms.*

### Detailed Edge Annotations

**Core Energy Transduction Chain (E01–E09):** The central causal pathway of chlorophototrophy proceeds: light photons are absorbed by light-harvesting complexes (LH1/LH2 in purple bacteria/AAPs, or chlorosomes→FMO in green sulfur bacteria) and excitation energy is funneled to the reaction center (yurkov2025phenomenaldiversityof pages 3-5, xie2023cryoemstructureof pages 1-2). At the reaction center, bacteriochlorophyll a undergoes photoexcitation and charge separation, with electrons passing through bacteriopheophytin to ubiquinone acceptors at QA and QB sites (yurkov2025phenomenaldiversityof pages 3-5). Reduced quinol diffuses through the membrane to the cytochrome bc1 complex, where the Q cycle translocates protons from cytoplasm to periplasm, generating the electrochemical proton gradient (yurkov2025phenomenaldiversityof pages 3-5, blankenship2021molecularmechanismsof pages 114-117). Cytochrome c2 returns electrons to the reaction center to complete cyclic electron flow (yurkov2025phenomenaldiversityof pages 3-5). The resulting proton motive force drives F1Fo-ATP synthase to produce ATP via photophosphorylation (yurkov2025phenomenaldiversityof pages 3-5, blankenship2021molecularmechanismsof pages 114-117).

**Type I vs. Type II Reaction Centers (E22–E24):** In green sulfur bacteria, the chlorosome—a massive self-assembled antenna containing 50,000–250,000 bacteriochlorophyll molecules—transfers excitation energy through the baseplate to trimeric FMO proteins, each containing eight BChl a per monomer, and onward to the Type I reaction center (xie2023cryoemstructureof pages 1-2, niedzwiedzki2025tripletstatedynamicsof pages 1-2). Type I RCs use [4Fe-4S] clusters as terminal electron acceptors and reduce ferredoxin directly, unlike Type II RCs that reduce quinones (niederman2024whatweare pages 1-2, niederman2024whatweare pages 5-7). The 2023 cryo-EM structure of the complete photosynthetic RC apparatus from *Chlorobaculum tepidum* at 2.5 Å resolution provided unprecedented detail of the FMO-RC-PS complex architecture (xie2023cryoemstructureof pages 1-2).

**Pigment Biosynthesis (E10–E15):** Bacteriochlorophyll biosynthesis requires a minimum of three core enzymatic steps: Mg-chelatase (BchI/D/H complex, EC:6.6.1.1) catalyzes the committing step by inserting Mg²⁺ into protoporphyrin IX; dark-operative protochlorophyllide reductase (DPOR, BchL/N/B, EC:1.3.7.7) reduces protochlorophyllide; and chlorophyllide a reductase (COR, BchX/Y/Z, EC:1.3.7.15) generates bacteriochlorin pigments with the characteristic light-absorbing properties essential for any chlorophototrophy mode (nishihara2024illuminatingthecoevolution pages 8-9, nishihara2024illuminatingthecoevolution pages 9-9). These genes are organized in four conserved regions within the photosynthetic gene cluster (PGC): bchFNBHLM, bchCXYZ, bchIDO, and bchGP, alongside puf/puh genes for RC/LH proteins, crt genes for carotenoid biosynthesis, and regulatory genes (yurkov2025phenomenaldiversityof pages 12-14).

**Retinalophototrophy (E20–E21):** Proteorhodopsin and related microbial rhodopsins pump one proton per photon absorbed across the membrane, generating PMF without engaging in electron transfer reactions (peterson2023usinglightfor pages 1-5). The cofactor all-trans-retinal is covalently bound to the rhodopsin apoprotein and is essential for light absorption (peterson2023usinglightfor pages 1-5, peterson2023usinglightfor pages 11-15). Rhodopsin-mediated PMF can either supplement ATP production through ATP synthase or reduce the ATP cost of maintaining cellular proton gradients (peterson2023usinglightfor pages 11-15).

**Photoprotection (E16–E17):** AAPs produce carotenoids in excess (1:8 to 1:10 ratio with BChl molecules) specifically to mitigate photooxidative damage from simultaneous aerobic growth and light absorption. Carotenoids scavenge singlet oxygen and quench BChl triplet states (yurkov2025phenomenaldiversityof pages 10-12).

**Regulation (E18, E26–E28):** PpsR/CrtJ represses BChl and carotenoid expression under aerobic conditions (yurkov2025phenomenaldiversityof pages 14-15). In AAPs, BChl is produced exclusively or predominantly in darkness; light exposure immediately halts pigment synthesis while darkness initiates gene expression after a ~4-hour delay (yurkov2025phenomenaldiversityof pages 16-18). Diurnal cycling drives rhythmic transcription, with over 50% of temporally regulated genes showing opposite expression between day and night: BChl biosynthesis genes and LH components are upregulated at night, while energy metabolism and cell division genes are upregulated during the day (tinguely2023diurnalcyclesdrive pages 5-8, tinguely2023diurnalcyclesdrive pages 9-10). Carbon limitation is a key trigger for photosynthesis gene induction, as AAPs switch from aerobic respiration during nutrient abundance to photosynthesis during carbon limitation (yurkov2025phenomenaldiversityof pages 19-21). Photosynthetic growth in *Congregibacter litoralis* yielded 2.4 times more ATP than heterotrophic dark growth (yurkov2025phenomenaldiversityof pages 18-19).

## 4. Recent Developments (2023–2025)

- **Cryo-EM structural breakthroughs:** The 2.5 Å cryo-EM structure of the complete photosynthetic RC apparatus from *Chlorobaculum tepidum* (green sulfur bacterium) was resolved in 2023, providing the first atomic-level view of the FMO-RC-PS complex (xie2023cryoemstructureof pages 1-2). A cryo-EM structure of a minimal RC-LH complex from *Chloroflexus aurantiacus* at 3.05 Å resolution revealed a novel semicircular antenna arrangement with only seven LH subunits (DOI:10.1111/jipb.13853).
- **New phototrophic phyla:** *Vulcanimicrobium alpinus* (2022), the first cultivated representative of the candidate phylum Eremiobacterota, was characterized as a metabolically versatile aerobic anoxygenic phototroph (yurkov2025phenomenaldiversityof pages 23-24). Globally distributed Myxococcota with photosynthesis gene clusters were reported in 2023 (yurkov2025phenomenaldiversityof pages 23-24).
- **Diurnal regulation:** Tinguely et al. (2023) demonstrated that diurnal cycles drive rhythmic physiology in the AAP *Porphyrobacter*, with a diphasic life history: dark phases inhibit DNA replication and cause partial cell lysis, while light phases allow recovery and renewed growth (tinguely2023diurnalcyclesdrive pages 1-2, tinguely2023diurnalcyclesdrive pages 9-10).
- **Dual photosynthesis:** Discovery of *Sphingomonas* sp. strain AAP5 exhibiting dual photosynthesis using both BChl and rhodopsin-based systems suggests such dual phototrophy may be more widespread than previously recognized (yurkov2025phenomenaldiversityof pages 19-21).
- **Regulatory mechanisms:** Blue light-dependent LOV-protein LdaP in *Dinoroseobacter shibae* was identified as an antirepressor of photosynthetic gene expression (2024), and small RNA-binding protein CcaF1 promotes photosynthetic complex formation in *Rhodobacter sphaeroides* (2023) (yurkov2025phenomenaldiversityof pages 28-29).

## 5. Ontology Grounding Summary

| Entity | CURIE |
|--------|-------|
| Light | ENVO:01001023 |
| Oxygen | CHEBI:15379 |
| Bacteriochlorophyll a | CHEBI:27888 |
| Chlorophyll a | CHEBI:18230 |
| Carotenoids | CHEBI:23044 |
| Ubiquinone | CHEBI:16389 |
| Menaquinone | CHEBI:18151 |
| all-trans-retinal | CHEBI:17898 |
| Protoporphyrin IX | CHEBI:15430 |
| ATP | CHEBI:15422 |
| Mg-chelatase | EC:6.6.1.1 |
| DPOR | EC:1.3.7.7 |
| COR | EC:1.3.7.15 |
| Cytochrome bc1 complex | EC:7.1.1.8 / GO:0045275 |
| F1Fo-ATP synthase | EC:7.1.2.2 / GO:0045259 |
| Cyclic electron transport | GO:0010598 |
| Photophosphorylation | GO:0015986 |
| BChl biosynthesis pathway | MetaCyc:PWY-5531 |
| bchI | KEGG:K03405 |
| bchD | KEGG:K03404 |

## 6. DOI-First Bibliography

1. Yurkov, V. & Messner, K. (2025). Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. *Microorganisms*, 13, 2446. DOI:10.3390/microorganisms13112446
2. Niederman, R.A. (2024). What we are learning from the diverse structures of the homodimeric Type I reaction center-photosystems of anoxygenic phototropic bacteria. *Biomolecules*, 14, 311. DOI:10.3390/biom14030311
3. Nishihara, A., Tsukatani, Y., Azai, C. & Nobu, M.K. (2024). Illuminating the coevolution of photosynthesis and Bacteria. *PNAS*, 121(25). DOI:10.1073/pnas.2322120121
4. Xie, H. et al. (2023). Cryo-EM structure of the whole photosynthetic reaction center apparatus from *Chlorobaculum tepidum*. *PNAS*, 120(5). DOI:10.1073/pnas.2216734120
5. Tinguely, C., Paulméry, M., Terrettaz, C. & Gonzalez, D. (2023). Diurnal cycles drive rhythmic physiology and promote survival in facultative phototrophic bacteria. *ISME Communications*, 3. DOI:10.1038/s43705-023-00334-5
6. Peterson, A., Baskett, C., Ratcliff, W.C. & Burnetti, A. (2023). Using light for energy: examining the evolution of phototrophic metabolism through synthetic construction. *bioRxiv*. DOI:10.1101/2022.12.06.519405
7. Blankenship, R.E. (2021). Molecular mechanisms of photosynthesis. Wiley. DOI:10.1002/9780470758472
8. Huang, G. et al. (2025). Cryo-EM structure of a minimal reaction center-light-harvesting complex from *Chloroflexus aurantiacus*. *J. Integrative Plant Biology*. DOI:10.1111/jipb.13853
9. Niedzwiedzki, D.M. et al. (2025). Triplet-state dynamics of bacteriochlorophyll a in the FMO complex. *J. Phys. Chem. B*, 129, 4309–4319. DOI:10.1021/acs.jpcb.5c00394

## 7. Curation Warnings

- **Edges E25–E28 (oxygen dependence, dark-phase regulation, carbon limitation):** These are well-supported for aerobic anoxygenic phototrophs but should NOT be generalized to all phototrophic organisms. Anoxygenic phototrophy in green sulfur bacteria and heliobacteria operates under strictly anaerobic conditions.
- **Edge E30 (2.4× ATP yield):** This quantitative claim is species-specific to *Congregibacter litoralis* and should be curated with taxon-specificity annotations.
- **Retinalophototrophy edges (E20–E21):** These represent a mechanistically distinct sub-pathway. Whether rhodopsin-based photoheterotrophy should be included within the same causal graph as chlorophototrophy depends on the intended scope of METPO:1000660. The trait definition ("use of light as the primary energy source... regardless of carbon source") is inclusive.
- **Dual phototrophy (BChl + rhodopsin):** Emerging evidence suggests some organisms employ both systems simultaneously. This is a boundary case that complicates clean separation of chlorophototrophy and retinalophototrophy sub-graphs.
- **PscA/PscB/PscC/FMO nodes:** These are taxon-specific to green sulfur bacteria and related lineages with Type I RCs. They should be curated as optional/taxon-restricted nodes.
- **ppaA/aerR antirepressor (E19):** The supporting evidence is indirect from PGC gene organization descriptions; direct functional characterization evidence should be sought before high-confidence curation.

References

1. (peterson2023usinglightfor pages 1-5): Autumn Peterson, Carina Baskett, William C. Ratcliff, and Anthony Burnetti. Using light for energy: examining the evolution of phototrophic metabolism through synthetic construction. bioRxiv, Apr 2023. URL: https://doi.org/10.1101/2022.12.06.519405, doi:10.1101/2022.12.06.519405. This article has 8 citations.

2. (nishihara2024illuminatingthecoevolution pages 2-3): Arisa Nishihara, Yusuke Tsukatani, Chihiro Azai, and Masaru K. Nobu. Illuminating the coevolution of photosynthesis and bacteria. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2322120121, doi:10.1073/pnas.2322120121. This article has 35 citations and is from a highest quality peer-reviewed journal.

3. (niederman2024whatweare pages 19-20): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

4. (yurkov2025phenomenaldiversityof pages 1-3): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

5. (yurkov2025phenomenaldiversityof pages 28-29): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

6. (yurkov2025phenomenaldiversityof pages 19-21): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

7. (yurkov2025phenomenaldiversityof pages 3-5): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

8. (yurkov2025phenomenaldiversityof pages 12-14): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

9. (yurkov2025phenomenaldiversityof pages 16-18): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

10. (tinguely2023diurnalcyclesdrive pages 1-2): Camille Tinguely, Mélanie Paulméry, Céline Terrettaz, and Diego Gonzalez. Diurnal cycles drive rhythmic physiology and promote survival in facultative phototrophic bacteria. ISME Communications, Sep 2023. URL: https://doi.org/10.1038/s43705-023-00334-5, doi:10.1038/s43705-023-00334-5. This article has 13 citations and is from a peer-reviewed journal.

11. (tinguely2023diurnalcyclesdrive pages 5-8): Camille Tinguely, Mélanie Paulméry, Céline Terrettaz, and Diego Gonzalez. Diurnal cycles drive rhythmic physiology and promote survival in facultative phototrophic bacteria. ISME Communications, Sep 2023. URL: https://doi.org/10.1038/s43705-023-00334-5, doi:10.1038/s43705-023-00334-5. This article has 13 citations and is from a peer-reviewed journal.

12. (nishihara2024illuminatingthecoevolution pages 8-9): Arisa Nishihara, Yusuke Tsukatani, Chihiro Azai, and Masaru K. Nobu. Illuminating the coevolution of photosynthesis and bacteria. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2322120121, doi:10.1073/pnas.2322120121. This article has 35 citations and is from a highest quality peer-reviewed journal.

13. (nishihara2024illuminatingthecoevolution pages 9-9): Arisa Nishihara, Yusuke Tsukatani, Chihiro Azai, and Masaru K. Nobu. Illuminating the coevolution of photosynthesis and bacteria. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2322120121, doi:10.1073/pnas.2322120121. This article has 35 citations and is from a highest quality peer-reviewed journal.

14. (yurkov2025phenomenaldiversityof pages 14-15): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

15. (yurkov2025phenomenaldiversityof pages 18-19): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

16. (yurkov2025phenomenaldiversityof pages 27-28): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

17. (peterson2023usinglightfor pages 11-15): Autumn Peterson, Carina Baskett, William C. Ratcliff, and Anthony Burnetti. Using light for energy: examining the evolution of phototrophic metabolism through synthetic construction. bioRxiv, Apr 2023. URL: https://doi.org/10.1101/2022.12.06.519405, doi:10.1101/2022.12.06.519405. This article has 8 citations.

18. (niederman2024whatweare pages 1-2): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

19. (niederman2024whatweare pages 9-11): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

20. (niedzwiedzki2025tripletstatedynamicsof pages 1-2): Dariusz M. Niedzwiedzki, Anica Dadwal, Po-Lin Chiu, and Haijun Liu. Triplet-state dynamics of bacteriochlorophyll a in the fenna-matthews-olson (fmo) complex and its modulation by pscb, a subunit in the reaction center of chlorobaculum tepidum. The journal of physical chemistry. B, 129:4309-4319, Apr 2025. URL: https://doi.org/10.1021/acs.jpcb.5c00394, doi:10.1021/acs.jpcb.5c00394. This article has 2 citations.

21. (xie2023cryoemstructureof pages 1-2): Hao Xie, Alexandros Lyratzakis, Radhika Khera, Myrto Koutantou, Sonja Welsch, Hartmut Michel, and Georgios Tsiotis. Cryo-em structure of the whole photosynthetic reaction center apparatus from the green sulfur bacterium chlorobaculum tepidum. Proceedings of the National Academy of Sciences of the United States of America, Jan 2023. URL: https://doi.org/10.1073/pnas.2216734120, doi:10.1073/pnas.2216734120. This article has 35 citations and is from a highest quality peer-reviewed journal.

22. (niederman2024whatweare pages 5-7): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

23. (blankenship2021molecularmechanismsof pages 114-117): Robert Eugene Blankenship. Molecular mechanisms of photosynthesis. ArXiv, Dec 2026. URL: https://doi.org/10.1002/9780470758472, doi:10.1002/9780470758472. This article has 4565 citations.

24. (niederman2024whatweare pages 22-23): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

25. (yurkov2025phenomenaldiversityof pages 21-23): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

26. (yurkov2025phenomenaldiversityof pages 10-12): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

27. (blankenship2021molecularmechanismsof pages 145-148): Robert Eugene Blankenship. Molecular mechanisms of photosynthesis. ArXiv, Dec 2026. URL: https://doi.org/10.1002/9780470758472, doi:10.1002/9780470758472. This article has 4565 citations.

28. (tinguely2023diurnalcyclesdrive pages 9-10): Camille Tinguely, Mélanie Paulméry, Céline Terrettaz, and Diego Gonzalez. Diurnal cycles drive rhythmic physiology and promote survival in facultative phototrophic bacteria. ISME Communications, Sep 2023. URL: https://doi.org/10.1038/s43705-023-00334-5, doi:10.1038/s43705-023-00334-5. This article has 13 citations and is from a peer-reviewed journal.

29. (yurkov2025phenomenaldiversityof pages 23-24): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.