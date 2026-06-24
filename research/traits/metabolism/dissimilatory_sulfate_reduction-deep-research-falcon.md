---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:42:31.296696'
end_time: '2026-06-18T05:12:30.801236'
duration_seconds: 1799.5
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dissimilatory sulfate reduction
  trait_identifier: traitmech:000105
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: dissimilatory_sulfate_reduction
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An anaerobic respiratory metabolism in which an organism uses sulfate
    as the terminal electron acceptor, reducing it to hydrogen sulfide while oxidizing
    organic matter or hydrogen for energy.
  parent_traits: METPO:1000802
  synonyms: sulfate respiration
  evidence_summary: 'DOI:10.1038/nrmicro1892:  (Muyzer & Stams review sulfate-reducing
    bacteria, which respire sulfate to sulfide in anoxic habitats.) | DOI:10.3389/fmicb.2011.00081:  (Plugge
    et al. review the metabolic flexibility of sulfate-reducing bacteria.)'
  causal_graph_summary: 'sulfate_reduction_to_sulfide: 4 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory sulfate reduction
- **METPO identifier:** traitmech:000105
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism uses sulfate as the terminal electron acceptor, reducing it to hydrogen sulfide while oxidizing organic matter or hydrogen for energy.
- **Parent traits:** METPO:1000802
- **Synonyms:** sulfate respiration
- **Existing evidence:** DOI:10.1038/nrmicro1892:  (Muyzer & Stams review sulfate-reducing bacteria, which respire sulfate to sulfide in anoxic habitats.) | DOI:10.3389/fmicb.2011.00081:  (Plugge et al. review the metabolic flexibility of sulfate-reducing bacteria.)
- **Existing causal graph summary:** sulfate_reduction_to_sulfide: 4 nodes, 2 edges

## Research Objective

Research the microbial trait **dissimilatory sulfate reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_sulfate_reduction.yaml`.

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
- **Trait label:** dissimilatory sulfate reduction
- **METPO identifier:** traitmech:000105
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism uses sulfate as the terminal electron acceptor, reducing it to hydrogen sulfide while oxidizing organic matter or hydrogen for energy.
- **Parent traits:** METPO:1000802
- **Synonyms:** sulfate respiration
- **Existing evidence:** DOI:10.1038/nrmicro1892:  (Muyzer & Stams review sulfate-reducing bacteria, which respire sulfate to sulfide in anoxic habitats.) | DOI:10.3389/fmicb.2011.00081:  (Plugge et al. review the metabolic flexibility of sulfate-reducing bacteria.)
- **Existing causal graph summary:** sulfate_reduction_to_sulfide: 4 nodes, 2 edges

## Research Objective

Research the microbial trait **dissimilatory sulfate reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_sulfate_reduction.yaml`.

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


# Research Report (TraitMech curation): Dissimilatory sulfate reduction (METPO: traitmech:000105)

## 0. Executive scope summary
Dissimilatory sulfate reduction (DSR; “sulfate respiration”) is an anaerobic energy-conserving respiratory metabolism in which microorganisms use sulfate (SO4^2−) as a terminal electron acceptor and reduce it to sulfide (H2S/HS−), typically excreting sulfide into the environment. Canonically, sulfate is activated to adenosine-5′-phosphosulfate (APS) by sulfate adenylyltransferase (Sat), APS is reduced to sulfite by APS reductase (AprAB) receiving electrons via QmoABC, and sulfite is reduced by DsrAB with the sulfur relay protein DsrC to a DsrC-trisulfide that is finally reduced to sulfide by the membrane DsrMK(JOP) complex, coupling this terminal step to energy conservation. (neukirchen2023stepwisepathwayfor pages 1-2, diao2023globaldiversityand pages 2-3, bernardino2023elucidatingthephysiological pages 32-33)

**Trait boundaries:**
* Assimilatory sulfate reduction is a biosynthetic route that shares initial sulfate activation but diverts through a PAPS intermediate for incorporation of reduced sulfur into biomass, not net sulfide excretion (fan2023recentadvancesin pages 5-6).
* “Reverse Dsr” (rDsr) sulfur oxidation can run Dsr-associated modules in the opposite direction to oxidize reduced sulfur; some organisms oxidize sulfide by operating the canonical sulfate-reduction pathway in reverse, meaning dsrAB presence alone does not guarantee sulfate-respiring DSR phenotype (diao2023globaldiversityand pages 2-3, neukirchen2023stepwisepathwayfor pages 1-2).

## 1. Key concepts and definitions (current understanding)
### 1.1 Dsr-pathway as the mechanistic core of sulfate respiration
A widely used current definition of the intracellular DSR mechanism is the “Dsr-pathway,” comprising Sat, AprAB, DsrAB, and DsrC, with electron-transfer complexes QmoAB(C) and DsrMK(JOP) delivering reducing equivalents to AprAB and DsrC, respectively (diao2023globaldiversityand pages 2-3). This pathway is frequently treated as the canonical mechanistic module for dissimilatory sulfate/sulfite reduction across taxa, while acknowledging exceptions and variations in electron transfer and membrane architecture (ferreira2023unravelingthemetabolic pages 20-24).

### 1.2 Distinguishing DSR from assimilatory sulfate reduction
In engineered/biotechnology-focused literature, dissimilatory sulfate reduction is described as “sulfate respiration” using electron donors such as formate, acetate, butyrate and H2, producing sulfide as the end product, whereas assimilatory sulfate reduction branches by phosphorylation of APS to PAPS (via adenylate kinase) and subsequent reduction for biosynthetic incorporation (fan2023recentadvancesin pages 5-6). This provides a concrete curation boundary: **DSR trait corresponds to respiratory sulfide production, not the PAPS-dependent biosynthetic assimilation route**.

### 1.3 Directionality and boundary cases: rDsr and ambiguous gene inventories
Recent reviews emphasize that functional inference from genomes is complicated: some organisms (e.g., examples discussed in review) can oxidize sulfide by operating the canonical sulfate reduction pathway in reverse, including having a reductive-type DsrAB, and DsrL types can blur oxidative vs reductive inference (diao2023globaldiversityand pages 2-3). Thus, TraitMech curation should treat directionality markers (e.g., dsrD, dsrL, dsrEFH) as *probabilistic* rather than definitive.

## 2. Canonical mechanistic pathway and candidate causal-graph entities
### 2.1 Pathway overview (with figure evidence)
A pathway schematic consistent with canonical sulfate respiration (SO4^2− → APS → SO3^2− → sulfide) and the involvement of Sat, AprAB, QmoABC and the DsrAB/DsrC/DsrMK complex is shown in a figure retrieved from Neukirchen et al. 2023 (ISMEJ) (neukirchen2023stepwisepathwayfor media 6ece0beb).

### 2.2 Candidate nodes (curation inventory)
A structured candidate node inventory (pathway modules, enzymes/genes/complexes, metabolites, cofactors, compartments, environmental factors, and applications) with suggested ontology grounding is provided below:

| Group | Label | Suggested grounding | Notes |
|---|---|---|---|
| Pathway/module | Dissimilatory sulfate reduction (sulfate respiration) | GO:0097473 | Anaerobic respiratory pathway reducing sulfate to sulfide; core trait represented by sat/aprAB/dsrAB/dsrC with Qmo and DsrMK(JOP) support in canonical sulfate reducers (diao2023globaldiversityand pages 2-3, neukirchen2023stepwisepathwayfor pages 1-2, bernardino2023elucidatingthephysiological pages 32-33). |
| Pathway/module | Dsr-pathway core module |  | Intracellular pathway comprising Sat, AprAB, DsrAB, DsrC, QmoAB(C), and DsrMK(JOP); used by many sulfate/sulfite reducers (diao2023globaldiversityand pages 2-3). |
| Pathway/module | Sulfite reduction submodule | GO:0097472 | Minimal ancient reductive module centered on DsrABCMK(N); can support sulfite reduction even where sulfate activation/reduction modules are absent (neukirchen2023stepwisepathwayfor pages 1-2, neukirchen2023stepwisepathwayfor pages 2-3). |
| Pathway/module | Sulfate activation and APS reduction module |  | Converts sulfate to APS (Sat) and APS to sulfite (AprAB), typically with Qmo-mediated electron input; required for sulfate, but not necessarily sulfite, respiration (neukirchen2023stepwisepathwayfor pages 1-2, bernardino2023elucidatingthephysiological pages 32-33, ferreira2023unravelingthemetabolic pages 20-24). |
| Pathway/module | Qrc-Qmo redox loop |  | Proposed energy-conserving loop coupling periplasmic electron flow to menaquinone reduction (Qrc) and APS reduction (Qmo→AprAB) (ferreira2023unravelingthemetabolic pages 20-24, bernardino2023elucidatingthephysiological pages 32-33). |
| Pathway/module | Reverse Dsr sulfur oxidation (boundary case) | GO:0019419 | Sulfur oxidizers can run Dsr-associated modules in reverse; not equivalent to the trait and should be curated separately/flagged (diao2023globaldiversityand pages 2-3, neukirchen2023stepwisepathwayfor pages 1-2, ferreira2023unravelingthemetabolic pages 20-24). |
| Pathway/module | Assimilatory sulfate reduction (boundary case) | GO:0000103 | Biosynthetic pathway to cell sulfur, distinguished from respiratory DSR; proceeds via PAPS branch rather than sulfide-excreting respiration (fan2023recentadvancesin pages 5-6). |
| Enzymes/complexes | Sulfate adenylyltransferase (Sat; sat) | EC:2.7.7.4 | Activates sulfate with ATP to adenosine-5'-phosphosulfate (APS); canonical first step of sulfate respiration (diao2023globaldiversityand pages 2-3, neukirchen2023stepwisepathwayfor pages 1-2, bernardino2023elucidatingthephysiological pages 32-33). |
| Enzymes/complexes | Adenylylsulfate reductase (AprAB; aprA, aprB) | EC:1.8.99.2 | Reduces APS to sulfite; physiological electron partner is QmoABC in many sulfate reducers (neukirchen2023stepwisepathwayfor pages 1-2, bernardino2023elucidatingthephysiological pages 32-33, ferreira2023unravelingthemetabolic pages 20-24). |
| Enzymes/complexes | Quinone-interacting membrane complex (QmoABC; qmoA, qmoB, qmoC) | KEGG:K00394/K00395/K00396 | Transfers reducing equivalents from menaquinol toward AprAB; essential for sulfate but not sulfite reduction in D. vulgaris mutant evidence discussed in source texts (bernardino2023elucidatingthephysiological pages 32-33, ferreira2023unravelingthemetabolic pages 20-24). |
| Enzymes/complexes | Dissimilatory sulfite reductase (DsrAB; dsrA, dsrB) | EC:1.8.99.5 | Central hallmark enzyme of SRM; reduces sulfite with DsrC involvement and serves as major marker gene family (diao2023globaldiversityand pages 1-2, diao2023globaldiversityand pages 2-3, neukirchen2023stepwisepathwayfor pages 1-2). |
| Enzymes/complexes | DsrC sulfur relay protein (dsrC) |  | Cosubstrate/partner of DsrAB; forms DsrC-trisulfide intermediate subsequently reduced to release sulfide (diao2023globaldiversityand pages 2-3, bernardino2023elucidatingthephysiological pages 32-33, ferreira2023unravelingthemetabolic pages 20-24). |
| Enzymes/complexes | DsrMKJOP membrane complex (dsrM, dsrK, dsrJ, dsrO, dsrP) |  | Proposed terminal reductase complex reducing DsrC-trisulfide to sulfide and linking the step to chemiosmotic energy conservation (neukirchen2023stepwisepathwayfor pages 1-2, bernardino2023elucidatingthephysiological pages 32-33, ferreira2023unravelingthemetabolic pages 20-24). |
| Enzymes/complexes | DsrMK subcomplex |  | Minimal version found in some archaea/Gram-positive organisms lacking JOP; associated with sulfite reduction and distinct bioenergetic solutions (neukirchen2023stepwisepathwayfor pages 1-2, neukirchen2023stepwisepathwayfor pages 2-3, ferreira2023unravelingthemetabolic pages 20-24). |
| Enzymes/complexes | QrcABCD quinone reductase (qrcA, qrcB, qrcC, qrcD) |  | Conserved in many Desulfobacterota; reduces menaquinone using periplasmic electrons and contributes to electrogenic redox loop (bernardino2023elucidatingthephysiological pages 32-33, ferreira2023unravelingthemetabolic pages 20-24). |
| Enzymes/complexes | TpIc3 tetraheme cytochrome c3 |  | Periplasmic redox hub routing electrons from H2/formate oxidation toward Qrc in Desulfobacterota-like systems (bernardino2023elucidatingthephysiological pages 32-33, ferreira2023unravelingthemetabolic pages 20-24). |
| Enzymes/complexes | DsrD allosteric activator (dsrD) |  | Usually associated with reductive Dsr systems; allosteric activator of DsrAB and useful but imperfect directionality marker; not always essential (diao2023globaldiversityand pages 2-3, bernardino2023elucidatingthephysiological pages 32-33). |
| Enzymes/complexes | DsrL oxidoreductase (dsrL) |  | Boundary-case marker: classically linked to sulfur oxidation, but some reductive/disproportionating lineages also encode DsrL, complicating inference (diao2023globaldiversityand pages 1-2, diao2023globaldiversityand pages 2-3, ferreira2023unravelingthemetabolic pages 20-24). |
| Enzymes/complexes | DsrEFH sulfur-transfer complex (dsrE, dsrF, dsrH) |  | Boundary-case node mainly associated with sulfur oxidation/rDsr systems; co-encoding with reductive markers can create ambiguity (diao2023globaldiversityand pages 1-2, neukirchen2023stepwisepathwayfor pages 2-3, ferreira2023unravelingthemetabolic pages 20-24). |
| Enzymes/complexes | DsrN siroheme amidase (dsrN) |  | Cofactor maturation enzyme for DsrAB siroheme amide; part of minimal/associated Dsr systems in many lineages (neukirchen2023stepwisepathwayfor pages 2-3). |
| Enzymes/complexes | HdrBC replacement module |  | In some Gram-positive sulfate reducers, hdrBC substitutes for qmoC-like function, suggesting soluble electron donation to APS reduction (ferreira2023unravelingthemetabolic pages 20-24). |
| Enzymes/complexes | Membrane ATP synthase | GO:0046933 | Downstream energy-conserving ATP synthesis using proton motive force generated by respiratory sulfate reduction (bernardino2023elucidatingthephysiological pages 32-33). |
| Electron donors/acceptors | Sulfate | CHEBI:16189 | Terminal electron acceptor defining the trait in canonical sulfate respiration (diao2023globaldiversityand pages 1-2, fan2023recentadvancesin pages 5-6). |
| Electron donors/acceptors | Sulfite | CHEBI:17980 | Intermediate and, in many taxa, alternative electron acceptor; sulfite reduction is more widespread than sulfate reduction (ferreira2023unravelingthemetabolic pages 20-24). |
| Electron donors/acceptors | Thiosulfate | CHEBI:30097 | Alternative sulfur electron acceptor in some sulfate reducers via upstream reduction to sulfite; trait-adjacent but not equivalent to sulfate respiration (ferreira2023unravelingthemetabolic pages 20-24). |
| Electron donors/acceptors | Organosulfonates |  | Some partial Dsr-pathway users reduce organosulfonates and retain DsrD-linked machinery; boundary case relative to full sulfate respiration (diao2023globaldiversityand pages 2-3). |
| Electron donors/acceptors | Hydrogen (H2) | CHEBI:18276 | Common electron donor supporting sulfate respiration and linked periplasmic electron transfer systems (fan2023recentadvancesin pages 5-6, bernardino2023elucidatingthephysiological pages 32-33). |
| Electron donors/acceptors | Formate | CHEBI:15740 | Common electron donor feeding periplasmic electron transfer in several sulfate reducers (fan2023recentadvancesin pages 5-6, bernardino2023elucidatingthephysiological pages 32-33). |
| Electron donors/acceptors | Acetate | CHEBI:30089 | Representative organic electron donor/substrate in SRB metabolism and competition contexts (fan2023recentadvancesin pages 5-6). |
| Electron donors/acceptors | Butyrate | CHEBI:17968 | Representative organic electron donor for sulfate respiration in engineering and environmental contexts (fan2023recentadvancesin pages 5-6). |
| Electron donors/acceptors | Organic matter / CH2O |  | Generic oxidizable carbon source supplying electrons for sulfate reduction and metal-precipitating bioremediation equations (fan2023recentadvancesin pages 5-6). |
| Metabolites/intermediates | Adenosine-5'-phosphosulfate (APS) | CHEBI:17044 | Activated sulfate intermediate produced by Sat and consumed by AprAB (neukirchen2023stepwisepathwayfor pages 1-2, bernardino2023elucidatingthephysiological pages 32-33). |
| Metabolites/intermediates | Sulfite | CHEBI:17980 | Product of APS reduction and substrate of DsrAB (diao2023globaldiversityand pages 2-3, neukirchen2023stepwisepathwayfor pages 1-2). |
| Metabolites/intermediates | Sulfide / hydrogen sulfide / HS- | CHEBI:16199 | Final reduced sulfur product of trait; often excreted and can precipitate metals or drive corrosion (fan2023recentadvancesin pages 5-6, yan2023insightsintoremediation pages 1-2, sun2023biomineralizationtoprevent pages 1-2). |
| Metabolites/intermediates | DsrC-trisulfide |  | Proposed immediate product of DsrAB+DsrC and substrate of DsrMKJOP terminal reduction (bernardino2023elucidatingthephysiological pages 32-33, ferreira2023unravelingthemetabolic pages 20-24). |
| Metabolites/intermediates | Menaquinone / menaquinol (MK/MKH2) | CHEBI:18009 | Membrane quinone pool donating electrons to Qmo and DsrMK-linked steps (bernardino2023elucidatingthephysiological pages 32-33, ferreira2023unravelingthemetabolic pages 20-24). |
| Metabolites/intermediates | Pyrophosphate (PPi) | CHEBI:18361 | Released during sulfate activation; hydrolysis helps drive the otherwise endergonic activation step (neukirchen2023stepwisepathwayfor pages 1-2, ferreira2023unravelingthemetabolic pages 20-24). |
| Metabolites/intermediates | AMP | CHEBI:16027 | Product of APS reduction by AprAB (neukirchen2023stepwisepathwayfor pages 1-2, bernardino2023elucidatingthephysiological pages 32-33). |
| Metabolites/intermediates | ATP | CHEBI:15422 | Consumed in sulfate activation; ATP synthesis recovered via chemiosmotic conservation in respiration (bernardino2023elucidatingthephysiological pages 32-33, ferreira2023unravelingthemetabolic pages 20-24). |
| Metabolites/intermediates | Elemental sulfur / zero-valent sulfur (boundary/side product) | CHEBI:26806 | Relevant to cryptic sulfur cycling and some noncanonical sulfate-reducing outputs; not core universal DSR product (diao2023globaldiversityand pages 2-3). |
| Cofactors | Siroheme | CHEBI:60579 | Catalytic cofactor of DsrAB for sulfite reduction (bernardino2023elucidatingthephysiological pages 32-33, neukirchen2023stepwisepathwayfor pages 2-3). |
| Cofactors | Siroheme amide |  | Mature prosthetic form in DsrAB supported by DsrN-mediated amidation (neukirchen2023stepwisepathwayfor pages 2-3). |
| Cofactors | [4Fe-4S] clusters | CHEBI:30413 | Present in DsrAB, Qmo, DsrK/O and other electron-transfer proteins of the pathway (bernardino2023elucidatingthephysiological pages 32-33). |
| Cofactors | FAD | CHEBI:16238 | Present in QmoABC and other redox proteins associated with DSR electron transfer (bernardino2023elucidatingthephysiological pages 32-33). |
| Cofactors | Heme b | CHEBI:60344 | Present in QmoC/DsrM-like membrane redox subunits (bernardino2023elucidatingthephysiological pages 32-33). |
| Cofactors | c-type hemes | CHEBI:61717 | Present in periplasmic cytochromes such as TpIc3 and DsrJ-associated modules in some taxa (bernardino2023elucidatingthephysiological pages 32-33). |
| Cofactors | NADPH (assimilatory boundary) | CHEBI:16474 | Mentioned for assimilatory sulfate reduction branch; helps separate biosynthetic sulfur assimilation from respiratory trait (fan2023recentadvancesin pages 5-6). |
| Cellular locations | Cytoplasm | GO:0005737 | Site of Sat, AprAB, DsrAB, DsrC reactions and major sulfur intermediates in canonical pathway diagrams (diao2023globaldiversityand pages 2-3, bernardino2023elucidatingthephysiological pages 32-33). |
| Cellular locations | Cytoplasmic membrane / plasma membrane | GO:0005886 | Location of QmoABC, DsrMKJOP, QrcABCD and chemiosmotic coupling (bernardino2023elucidatingthephysiological pages 32-33, ferreira2023unravelingthemetabolic pages 20-24). |
| Cellular locations | Periplasm | GO:0042597 | Relevant in Gram-negative sulfate reducers for TpIc3, Qrc-linked input and possibly DsrJOP interactions (bernardino2023elucidatingthephysiological pages 32-33, ferreira2023unravelingthemetabolic pages 20-24). |
| Cellular locations | Extracellular environment | GO:0005576 | Sulfide often diffuses/exits cells and impacts surrounding geochemistry, corrosion and metal precipitation (fan2023recentadvancesin pages 5-6, sun2023biomineralizationtoprevent pages 1-2). |
| Environmental/expt factors | Anoxic / anaerobic conditions | ENVO:01000254 | Trait is fundamentally anaerobic respiratory metabolism favored in oxygen-depleted environments (diao2023globaldiversityand pages 1-2, neukirchen2023stepwisepathwayfor pages 1-2). |
| Environmental/expt factors | High sulfate availability |  | Strong driver in marine sediments and many engineered systems; sulfate concentration shapes SRM activity/community structure (diao2023globaldiversityand pages 1-2, yan2023insightsintoremediation pages 1-2). |
| Environmental/expt factors | Low-sulfate cryptic sulfur cycle |  | Important environmental context where sulfate reduction remains active despite low sulfate due to rapid sulfur recycling (diao2023globaldiversityand pages 1-2, diao2023globaldiversityand pages 2-3). |
| Environmental/expt factors | Low pH / acidic mine environments | ENVO:09200014 | Relevant to bioremediation deployment; harsh acidity can limit SRB and motivate combined chemical-biological treatment (yan2023insightsintoremediation pages 1-2, fan2023recentadvancesin pages 5-6). |
| Environmental/expt factors | pH |  | Strongly correlates with community structure and remediation performance in sulfate-rich contaminated soils (yan2023insightsintoremediation pages 1-2). |
| Environmental/expt factors | Redox potential (Eh) |  | Reported environmental variable associated with SRB community structure and function in remediation experiments (yan2023insightsintoremediation pages 1-2). |
| Environmental/expt factors | Heavy metals (Pb, Zn, Mn, Cu, Cd, U, Sb) | CHEBI:25038 | Metals can be immobilized by biogenic sulfide as insoluble metal sulfides; also shape engineered applications (yan2023insightsintoremediation pages 1-2, fan2023recentadvancesin pages 5-6). |
| Environmental/expt factors | Calcium hydroxide amendment | CHEBI:31341 | Combined with SRB to improve remediation under acidic/high-sulfate soil conditions (yan2023insightsintoremediation pages 1-2). |
| Applications/contexts | Rare earth mine soil remediation | ENVO:00001998 | SRB inoculation increased sulfate respiration and removal/immobilization of sulfate and metals in contaminated soils (yan2023insightsintoremediation pages 1-2). |
| Applications/contexts | Acid mine drainage / metallic wastewater treatment | ENVO:00001991 | Classic applied context for sulfide-generating SRB systems precipitating heavy metals and generating alkalinity (fan2023recentadvancesin pages 5-6). |
| Applications/contexts | Heavy-metal sulfide precipitation |  | Mechanistic application node linking sulfide output to PbS/ZnS/CuS/MnS and similar immobilization products (yan2023insightsintoremediation pages 1-2, fan2023recentadvancesin pages 5-6). |
| Applications/contexts | Microbially induced corrosion (MIC) of concrete |  | Sulfate reduction generates H2S that can fuel sulfuric acid formation and concrete damage in marine infrastructure (sun2023biomineralizationtoprevent pages 1-2). |
| Applications/contexts | Corrosive SRB biofilms |  | SRB-dominated biofilms are major corrosive communities; suppression of SRB abundance is a mitigation target (sun2023biomineralizationtoprevent pages 1-2). |
| Applications/contexts | Marine and coastal sediments | ENVO:00000316 | Major natural setting where sulfate reduction drives large fractions of organic carbon mineralization (diao2023globaldiversityand pages 1-2). |
| Applications/contexts | Freshwater sediments / peatlands / rice paddies | ENVO:00000873 | Low-sulfate systems with cryptic sulfur cycling and important SRM-methanogen competition (diao2023globaldiversityand pages 1-2, diao2023globaldiversityand pages 2-3). |
| Applications/contexts | Wastewater sulfate-reduction bioreactors |  | Engineered systems for phenol, antibiotic, metal and sulfate treatment using sulfate respiration (fan2023recentadvancesin pages 5-6). |


*Table: This table lists candidate nodes for a TraitMech causal graph of dissimilatory sulfate reduction, organized by mechanistic and environmental type. It includes suggested ontology grounding and notes on boundary-case markers such as dsrD, dsrL, and dsrEFH to support careful curation.*

## 3. Evidence-backed candidate causal edges (triples)
A curation-ready table of candidate causal edges with verbatim snippets, references, and uncertainty notes is provided here:

| Subject node | Predicate | Object node | Evidence snippet (verbatim quote) | Reference (DOI + URL + publication date) | Notes |
|---|---|---|---|---|---|
| sulfate | is transported into | cell/cytoplasm | "Sulfate (SO42-) is transported inside the cell" (ferreira2023unravelingthemetabolic pages 20-24) | Ferreira 2023; DOI not available in retrieved metadata; source text in corpus; publication year 2023 | Candidate upstream transport edge. Ground transporter as label-only unless a sulfate transporter gene is evidenced in a primary source. **Uncertainty:** medium (transporter identity not specified). |
| sulfate | is activated by | Sat (sulfate adenylyltransferase) | "Sulfate is taken up from the environment via sulfate transporters and activated by the enzyme ATP sulfurylase (Sat)" (fan2023recentadvancesin pages 5-6) | Fan et al. 2023. DOI:10.3390/antiox12030767. https://doi.org/10.3390/antiox12030767. Published Mar 2023 | Strong canonical step for sulfate respiration. Curate as core DSR edge. |
| Sat | produces | APS | "activated by the enzyme ATP sulfurylase (Sat) to form adenosine-5′-phosphosulfate (APS)" (fan2023recentadvancesin pages 5-6) | Fan et al. 2023. DOI:10.3390/antiox12030767. https://doi.org/10.3390/antiox12030767. Published Mar 2023 | Strong core edge. APS can be grounded to CHEBI:17044. |
| AprAB | reduces | APS to sulfite | "The APS reductase AprAB receives electrons from the quinone-interacting membrane complex QmoABC" and "APS is reduced to sulﬁte serving as substrate of the Dsr cascade" (neukirchen2023stepwisepathwayfor pages 1-2) | Neukirchen et al. 2023. DOI:10.1038/s41396-023-01477-y. https://doi.org/10.1038/s41396-023-01477-y. Published 19 Jul 2023 | Strong canonical step. Curate as AprAB causally converting APS to sulfite. |
| QmoABC | transfers electrons to | AprAB | "it has been proposed that the QmoC transfers electrons from the menaquinone pool to QmoAB which then delivers the electrons to AprAB" (bernardino2023elucidatingthephysiological pages 32-33) | Bernardino 2023; DOI not available in retrieved metadata; source text in corpus; publication year 2023 | Strong mechanistic edge, though phrased as proposal. Supported by mutant and interaction evidence in same source. **Uncertainty:** low-medium. |
| DsrAB + DsrC | produces | DsrC-trisulfide | "DsrAB produces a DsrC-trisulﬁde from sulﬁte and the DsrC protein" (neukirchen2023stepwisepathwayfor pages 1-2) | Neukirchen et al. 2023. DOI:10.1038/s41396-023-01477-y. https://doi.org/10.1038/s41396-023-01477-y. Published 19 Jul 2023 | Strong core edge for sulfite reduction intermediate. Curate as central mechanistic step. |
| DsrMKJOP | reduces | DsrC-trisulfide to sulfide + regenerated DsrC | "The DsrC-trisulﬁde is then reduced by the DsrMK(JOP) membrane complex recycling DsrC and releasing sulﬁde while coupling this reduction to energy conservation" (neukirchen2023stepwisepathwayfor pages 1-2) | Neukirchen et al. 2023. DOI:10.1038/s41396-023-01477-y. https://doi.org/10.1038/s41396-023-01477-y. Published 19 Jul 2023 | Strong edge; directly links terminal reductase complex to product formation and DsrC recycling. |
| QrcABCD | reduces | menaquinone pool using periplasmic electrons | "electrons from the periplasmic TpIc3 cytochrome, together with protons from the cytoplasm, are used by QrcABCD to reduce the menaquinone pool" (ferreira2023unravelingthemetabolic pages 20-24) | Ferreira 2023; DOI not available in retrieved metadata; source text in corpus; publication year 2023 | Good mechanistic edge for Desulfobacterota-like systems. **Uncertainty:** medium (taxon-specific, not universal). |
| Qrc-Qmo redox loop | supports | energetically favorable APS reduction / proton motive force | "there is a redox loop mechanism between QmoABC and the QrcABCD membrane complex" and "QmoABC then oxidizes menaquinol to donate electrons to AprAB, together with proton transfer to the periplasm" (ferreira2023unravelingthemetabolic pages 20-24) | Ferreira 2023; DOI not available in retrieved metadata; source text in corpus; publication year 2023 | Useful higher-level energy-conservation edge. Likely curate as process-level edge rather than direct molecular reaction. **Uncertainty:** medium. |
| dsrD | activates | DsrAB | "DsrD acts as an allosteric activator of DsrAB" (diao2023globaldiversityand pages 2-3) | Diao et al. 2023. DOI:10.1093/femsre/fuad058. https://doi.org/10.1093/femsre/fuad058. Published 5 Oct 2023 | Strong curation candidate for accessory regulation. Note that DsrD is not essential in all taxa. |
| dsrAB | is marker for | sulfate/sulfite-reducing microorganisms (SRM) | "A hallmark of SRM is the dissimilatory sulfite reductase encoded by the genes dsrAB" (diao2023globaldiversityand pages 1-2) | Diao et al. 2023. DOI:10.1093/femsre/fuad058. https://doi.org/10.1093/femsre/fuad058. Published 5 Oct 2023 | Strong marker edge for annotation/inference, but marker ≠ phenotype in all cases because of rDsr and mixed systems. |
| reductive-type Dsr pathway | can operate in reverse to oxidize | sulfide (rDsr boundary case) | "Both can oxidize sulfide by operating the canonical pathway of sulfate reduction in reverse, including a reductive-type DsrAB" (diao2023globaldiversityand pages 2-3) | Diao et al. 2023. DOI:10.1093/femsre/fuad058. https://doi.org/10.1093/femsre/fuad058. Published 5 Oct 2023 | **Boundary-case edge; uncertain for trait curation.** Important warning that dsrAB alone does not prove sulfate respiration. |
| assimilatory sulfate reduction | branches via | PAPS | "assimilatory sulfate reduction requires the transfer of phosphate to adenosine-5′-phosphate sulfate (APS) by adenylate kinase to produce phosphoryl adenosine-5′-phosphate sulfate (PAPS)" (fan2023recentadvancesin pages 5-6) | Fan et al. 2023. DOI:10.3390/antiox12030767. https://doi.org/10.3390/antiox12030767. Published Mar 2023 | **Boundary-case edge; uncertain for TraitMech DSR graph.** Use to distinguish biosynthetic sulfur assimilation from respiratory DSR. |
| biogenic sulfide (H2S) | precipitates | metal ions as insoluble metal sulfides | "H2S + M2+ →MS + 2H+" (fan2023recentadvancesin pages 5-6) | Fan et al. 2023. DOI:10.3390/antiox12030767. https://doi.org/10.3390/antiox12030767. Published Mar 2023 | Strong applied edge relevant to bioremediation. Suitable as downstream ecological/application consequence, not core intracellular mechanism. |
| sulfate reduction by SRB | contributes to | microbially induced corrosion of concrete | "(1) sulfate (SO42−) is converted to sulfide (H2S) through the biological activities of sulfate-reducing bacteria (SRB) residing in biofilms. (2) H2S is then converted to sulfuric acid (H2SO4) by sulfur-oxidizing bacteria (SOB). (3) Sulfuric acid reacts with the concrete matrix" (sun2023biomineralizationtoprevent pages 1-2) | Sun et al. 2023. DOI:10.1021/acs.est.3c04680. https://doi.org/10.1021/acs.est.3c04680. Published 5 Dec 2023 | Strong applied multi-step consequence edge. Best modeled as chain: SRB sulfate reduction → H2S → sulfuric acid formation → concrete corrosion. |
| SRB + Ca(OH)2 treatment | improves removal of | sulfate and heavy metals in contaminated soil | "CM-M treatment had a more efficient removal effect for SO42−, Pb, Zn, and Mn than the others, up to 94.6, 88.3, 98.7, and 91%, respectively" (yan2023insightsintoremediation pages 1-2) | Yan et al. 2023. DOI:10.3389/fmicb.2023.1050635. https://doi.org/10.3389/fmicb.2023.1050635. Published 23 Mar 2023 | Strong application edge for engineered remediation. Assay/environment-specific; not a universal biological mechanism. **Uncertainty:** low for application, high for generalization. |


*Table: This table compiles evidence-backed candidate causal edges for dissimilatory sulfate reduction, including core pathway steps, energetic modules, marker/diagnostic edges, boundary cases, and applied environmental consequences. It is designed to support TraitMech curation by separating strong core mechanistic claims from taxon-specific or assay-specific inferences.*

## 4. Recent developments and latest research (prioritize 2023–2024)
### 4.1 Expansion of known DSR diversity and quantitative ecology
A 2023 FEMS Microbiology Reviews synthesis analyzed **950 mainly metagenome-derived dsrAB-carrying genomes** to redefine global diversity of microorganisms with potential for dissimilatory sulfate/sulfite reduction (diao2023globaldiversityand pages 1-2, diao2023globaldiversityand pages 3-4). This review emphasizes that the dsrAB marker occurs across broad phylogenetic breadth, including many uncultured lineages, and that dsrAB-based surveys dramatically outpace cultured diversity; e.g., dsrB amplicon sequencing identified **167,397 species-level OTUs across 14 environments**, and comparison to ~460 described SRM implies **>99% of SRM diversity is uncultured** (diao2023globaldiversityand pages 2-3). 

The same review contextualizes DSR’s biogeochemical scale with concrete quantitative estimates: **~1/3 of the ~260 Tmol organic carbon reaching the seabed annually is mineralized via sulfate reduction** and **~90% of produced sulfide is re-oxidized**; sulfate reduction represents **~25% of global sediment oxygen consumption**, and in coastal sediments accounts for **~50% of organic carbon mineralization** (diao2023globaldiversityand pages 1-2). These values are suitable as high-level “expert consensus” statistics for trait importance.

### 4.2 Evolutionary and mechanistic refinement of Dsr-associated modules
A 2023 ISME Journal comparative genomics study across >195,000 metagenomes supports that the minimal DsrABCMK(N) protein set likely had a primordial function in sulfite reduction, and that acquisition of additional Dsr proteins (e.g., DsrJOPT) increased pathway complexity; it also emphasizes that innovations in Qmo complex types enabled sulfate (not only sulfite) as electron acceptor and that the Dsr pathway for sulfur oxidation evolved multiple times (neukirchen2023stepwisepathwayfor pages 1-2). This frames a key boundary: **sulfite reduction is more ancient/minimal; sulfate respiration requires additional modules enabling APS reduction**.

### 4.3 Increasing emphasis on “cryptic sulfur cycling” and climate/ecosystem coupling
The 2023 FEMS Microbiology Reviews article notes oxygen minimum zones and low-sulfate habitats can show “cryptic sulfur cycling,” where sulfide produced by sulfate reduction is rapidly re-oxidized, and that SRM can compete with methanogenic networks in low-sulfate environments, partially diverting carbon flux from CH4 to CO2 (diao2023globaldiversityand pages 1-2, diao2023globaldiversityand pages 2-3). This is a mechanistically relevant environmental coupling to include as ENVO-context nodes rather than core intracellular steps.

### 4.4 2024 terrestrial-SRP ecology synthesis
A 2024 Applied and Environmental Microbiology review emphasizes terrestrial sulfate reducers are often part of a “rare biosphere” and that metabarcoding across >200 samples revealed **>150,000 new species-level Dsr OTUs**, with cultivated sulfate reducers comprising **<1%** of discovered copies; ~30% of uncovered gene copies are attributed to unknown taxa (demin2024sulfatereducingbacteriaunearthed pages 8-10). These results strengthen the warning that genome-based identification of DSR potential often lacks phenotypic confirmation.

## 5. Current applications and real-world implementations (with quantitative outcomes)
### 5.1 Bioremediation of sulfate and heavy metals
**Rare-earth mine soil remediation (combined chemical + SRB):** A 2023 Frontiers in Microbiology study reports that a Ca(OH)2 + SRB treatment (CM-M) removed contaminants “up to **94.6% (SO4^2−), 88.3% (Pb), 98.7% (Zn), and 91% (Mn)**,” and mechanistically links SRB sulfate reduction to S^2− production and insoluble metal sulfide precipitation (yan2023insightsintoremediation pages 1-2).

**Coal mine soil bioremediation with plants:** A 2023 Frontiers study applying a predominant SRB consortium (mainly Desulfovibrio and Desulfobulbus OTUs) reports improved metal immobilization, with conversion of metals to residual forms rising **from 23.47% to 75.98%** (yang2023harnessingsulfatereducingbacteria pages 1-2). 

**Sulfate-reduction bioreactor use cases:** A 2023 Antioxidants review summarizes sulfate reduction biotechnology for industrial wastewaters; e.g., “up to **98.3% antimony removal**” in SRB reactors with Fe(II) participation (fan2023recentadvancesin pages 5-6). It also provides mechanistic reaction statements for sulfide-driven metal precipitation (fan2023recentadvancesin pages 5-6).

### 5.2 Microbiologically influenced corrosion (MIC) and infrastructure impacts
An Environmental Science & Technology paper (received 16 Jun 2023; published 5 Dec 2023) provides a clear multi-step MIC mechanism on concrete: (1) SRB convert sulfate to sulfide (H2S), (2) sulfur-oxidizing bacteria convert H2S to sulfuric acid, and (3) sulfuric acid reacts with concrete matrix to form gypsum/ettringite and fractures (sun2023biomineralizationtoprevent pages 1-2). It also cites economic scale: MIC contributes to global economic loss of approximately “**~US$800 billion annually**,” and annual rehabilitation costs for MIC concrete are estimated at “**£85 million in the U.K. and over €450 million in Germany**” (sun2023biomineralizationtoprevent pages 1-2). The study reports biomineralization-based protection inhibited corrosion by decreasing SRB abundance and limiting sulfate diffusion (sun2023biomineralizationtoprevent pages 1-2).

## 6. Expert opinions and authoritative synthesis
The 2023 FEMS Microbiology Reviews article provides authoritative framing that sulfate/sulfite-reducing microorganisms (SRM) are ubiquitous and that dsrAB-encoded dissimilatory sulfite reductase is a hallmark; it stresses that genomic signals can challenge earlier generalizations about SRM energy metabolism and that DsrL and rDsr can complicate directionality inference (diao2023globaldiversityand pages 1-2, diao2023globaldiversityand pages 2-3). This can be treated as an “expert consensus” caution for TraitMech curation.

## 7. Warnings: claims that should not yet be curated (or should be flagged uncertain)
1. **Do not equate dsrAB presence with sulfate respiration phenotype without context.** Some organisms oxidize sulfide by running the canonical sulfate-reduction pathway in reverse (rDsr-like behavior), and directionality markers (dsrD, dsrL, dsrEFH) can be mixed (diao2023globaldiversityand pages 2-3, diao2023globaldiversityand pages 1-2).
2. **Electron transfer/energy conservation modules can be taxon-specific.** Qrc-Qmo redox-loop descriptions apply strongly to some Gram-negative Desulfobacterota-like systems, whereas Gram-positive sulfate reducers may lack QmoC and DsrJOP and use alternative components (hdrBC substitution; DsrMK-only) (ferreira2023unravelingthemetabolic pages 20-24).
3. **“Terminal reductase complex” status of DsrMKJOP is strongly supported conceptually but still contains mechanistic unknowns.** The identity of the two-electron donor to DsrAB and some details of DsrC-trisulfide reduction are explicitly described as unresolved questions in a mechanistic synthesis (ferreira2023unravelingthemetabolic pages 20-24).
4. **Assimilatory sulfate reduction should not be merged into DSR trait.** Assimilatory uses PAPS branch and biomass incorporation rather than sulfide excretion (fan2023recentadvancesin pages 5-6).

## 8. DOI-first bibliography (with URLs and publication dates where available)
* Diao M, Dyksma S, Koeksoy E, et al. **Global diversity and inferred ecophysiology of microorganisms with the potential for dissimilatory sulfate/sulfite reduction.** *FEMS Microbiology Reviews.* Advance access publication date **5 Oct 2023**. DOI: **10.1093/femsre/fuad058**. URL: https://doi.org/10.1093/femsre/fuad058 (diao2023globaldiversityand pages 1-2, diao2023globaldiversityand pages 2-3)
* Neukirchen S, Pereira IAC, Sousa FL. **Stepwise pathway for early evolutionary assembly of dissimilatory sulfite and sulfate reduction.** *The ISME Journal.* Published online **19 Jul 2023**. DOI: **10.1038/s41396-023-01477-y**. URL: https://doi.org/10.1038/s41396-023-01477-y (neukirchen2023stepwisepathwayfor pages 1-2, neukirchen2023stepwisepathwayfor media 6ece0beb)
* Fan K, Wang W, Xu X-J, et al. **Recent advances in biotechnologies for the treatment of environmental pollutants based on reactive sulfur species.** *Antioxidants.* **Mar 2023**. DOI: **10.3390/antiox12030767**. URL: https://doi.org/10.3390/antiox12030767 (fan2023recentadvancesin pages 5-6)
* Yan X, Gao B, Wang J, et al. **Insights into remediation effects and bacterial diversity of different remediation measures in rare earth mine soil with SO42− and heavy metals.** *Frontiers in Microbiology.* **23 Mar 2023**. DOI: **10.3389/fmicb.2023.1050635**. URL: https://doi.org/10.3389/fmicb.2023.1050635 (yan2023insightsintoremediation pages 1-2)
* Sun X, Wai OWH, Xie J, Li X. **Biomineralization To Prevent Microbially Induced Corrosion on Concrete for Sustainable Marine Infrastructure.** *Environmental Science & Technology.* Received **16 Jun 2023**; Published **5 Dec 2023** (journal issue shows 2024 volume). DOI: **10.1021/acs.est.3c04680**. URL: https://doi.org/10.1021/acs.est.3c04680 (sun2023biomineralizationtoprevent pages 1-2)
* Yang Z, Wu Q, Liu Z, et al. **Harnessing sulfate-reducing bacteria with plants growing to revitalize metal-tainted coal mine soils in Midwest China.** *Frontiers in Microbiology.* Published **15 Nov 2023**. DOI: **10.3389/fmicb.2023.1306573**. URL: https://doi.org/10.3389/fmicb.2023.1306573 (yang2023harnessingsulfatereducingbacteria pages 1-2)
* Demin KA, Prazdnova EV, Minkina TM, Gorovtsov AV. **Sulfate-reducing bacteria unearthed: ecological functions of the diverse prokaryotic group in terrestrial environments.** *Applied and Environmental Microbiology.* **Apr 2024**. DOI: **10.1128/aem.01390-23**. URL: https://doi.org/10.1128/aem.01390-23 (demin2024sulfatereducingbacteriaunearthed pages 8-10)
* Klier KM, Martin C, Langwig MV, Anantharaman K. **Evolutionary history and origins of Dsr-mediated sulfur oxidation.** *The ISME Journal.* **Jan 2024**. DOI: **10.1093/ismejo/wrae167**. URL: https://doi.org/10.1093/ismejo/wrae167 (klier2024evolutionaryhistoryand pages 1-2)

### Non-DOI corpus sources used for mechanistic detail
* Bernardino RM. **Elucidating the physiological role of the DsrJ cytochrome in dissimilatory sulfate metabolism.** (source in corpus; DOI not captured) (bernardino2023elucidatingthephysiological pages 32-33)
* Ferreira DMA. **Unraveling the metabolic pathway of dissimilatory sulfate reduction.** (source in corpus; DOI not captured) (ferreira2023unravelingthemetabolic pages 20-24)

---

## Appendix: Curation-ready figure evidence
A cropped figure illustrating the complete sulfate respiration pathway module (Sat → AprAB → DsrAB/DsrC → DsrMKJOP) was retrieved from Neukirchen et al. 2023 (ISMEJ) (neukirchen2023stepwisepathwayfor media 6ece0beb).


References

1. (neukirchen2023stepwisepathwayfor pages 1-2): Sinje Neukirchen, Inês A C Pereira, and Filipa L Sousa. Stepwise pathway for early evolutionary assembly of dissimilatory sulfite and sulfate reduction. The ISME Journal, 17:1680-1692, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01477-y, doi:10.1038/s41396-023-01477-y. This article has 70 citations.

2. (diao2023globaldiversityand pages 2-3): Muhe Diao, Stefan Dyksma, Elif Koeksoy, David Kamanda Ngugi, Karthik Anantharaman, Alexander Loy, and Michael Pester. Global diversity and inferred ecophysiology of microorganisms with the potential for dissimilatory sulfate/sulfite reduction. FEMS Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1093/femsre/fuad058, doi:10.1093/femsre/fuad058. This article has 87 citations and is from a domain leading peer-reviewed journal.

3. (bernardino2023elucidatingthephysiological pages 32-33): RM Bernardino. Elucidating the physiological role of the dsrj cytochrome in dissimilatory sulfate metabolism. Unknown journal, 2023.

4. (fan2023recentadvancesin pages 5-6): Kaili Fan, Wei Wang, Xi-Jun Xu, Yuan Yuan, Nanqi Ren, Duu-Jong Lee, and Chuan Chen. Recent advances in biotechnologies for the treatment of environmental pollutants based on reactive sulfur species. Antioxidants, 12:767, Mar 2023. URL: https://doi.org/10.3390/antiox12030767, doi:10.3390/antiox12030767. This article has 23 citations.

5. (ferreira2023unravelingthemetabolic pages 20-24): DMA Ferreira. Unraveling the metabolic pathway of dissimilatory sulfate reduction. Unknown journal, 2023.

6. (neukirchen2023stepwisepathwayfor media 6ece0beb): Sinje Neukirchen, Inês A C Pereira, and Filipa L Sousa. Stepwise pathway for early evolutionary assembly of dissimilatory sulfite and sulfate reduction. The ISME Journal, 17:1680-1692, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01477-y, doi:10.1038/s41396-023-01477-y. This article has 70 citations.

7. (neukirchen2023stepwisepathwayfor pages 2-3): Sinje Neukirchen, Inês A C Pereira, and Filipa L Sousa. Stepwise pathway for early evolutionary assembly of dissimilatory sulfite and sulfate reduction. The ISME Journal, 17:1680-1692, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01477-y, doi:10.1038/s41396-023-01477-y. This article has 70 citations.

8. (diao2023globaldiversityand pages 1-2): Muhe Diao, Stefan Dyksma, Elif Koeksoy, David Kamanda Ngugi, Karthik Anantharaman, Alexander Loy, and Michael Pester. Global diversity and inferred ecophysiology of microorganisms with the potential for dissimilatory sulfate/sulfite reduction. FEMS Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1093/femsre/fuad058, doi:10.1093/femsre/fuad058. This article has 87 citations and is from a domain leading peer-reviewed journal.

9. (yan2023insightsintoremediation pages 1-2): Xiao Yan, Bowen Gao, Jianlei Wang, Xuezhe Zhu, and Mingjiang Zhang. Insights into remediation effects and bacterial diversity of different remediation measures in rare earth mine soil with so42− and heavy metals. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1050635, doi:10.3389/fmicb.2023.1050635. This article has 20 citations and is from a peer-reviewed journal.

10. (sun2023biomineralizationtoprevent pages 1-2): Xiaohao Sun, Onyx W. H. Wai, Jiawen Xie, and Xiangdong Li. Biomineralization to prevent microbially induced corrosion on concrete for sustainable marine infrastructure. Environmental Science & Technology, 58:522-533, Dec 2023. URL: https://doi.org/10.1021/acs.est.3c04680, doi:10.1021/acs.est.3c04680. This article has 83 citations and is from a domain leading peer-reviewed journal.

11. (diao2023globaldiversityand pages 3-4): Muhe Diao, Stefan Dyksma, Elif Koeksoy, David Kamanda Ngugi, Karthik Anantharaman, Alexander Loy, and Michael Pester. Global diversity and inferred ecophysiology of microorganisms with the potential for dissimilatory sulfate/sulfite reduction. FEMS Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1093/femsre/fuad058, doi:10.1093/femsre/fuad058. This article has 87 citations and is from a domain leading peer-reviewed journal.

12. (demin2024sulfatereducingbacteriaunearthed pages 8-10): Konstantin A. Demin, Evgeniya V. Prazdnova, Tatiana M. Minkina, and Andrey V. Gorovtsov. Sulfate-reducing bacteria unearthed: ecological functions of the diverse prokaryotic group in terrestrial environments. Apr 2024. URL: https://doi.org/10.1128/aem.01390-23, doi:10.1128/aem.01390-23. This article has 78 citations and is from a peer-reviewed journal.

13. (yang2023harnessingsulfatereducingbacteria pages 1-2): Zhendong Yang, Qihong Wu, Zhenghua Liu, Xiang Qi, Zhenyu Zhang, Miao He, Cong Peng, Li Zeng, Jing Wang, Fan Li, Zhaoyue Yang, and Huaqun Yin. Harnessing sulfate-reducing bacteria with plants growing to revitalize metal-tainted coal mine soils in midwest china: metal sequestration performance, ecological networking interaction, and functional enzymatic prediction. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1306573, doi:10.3389/fmicb.2023.1306573. This article has 8 citations and is from a peer-reviewed journal.

14. (klier2024evolutionaryhistoryand pages 1-2): Katherine M. Klier, Cody Martin, Marguerite V. Langwig, and Karthik Anantharaman. Evolutionary history and origins of dsr-mediated sulfur oxidation. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae167, doi:10.1093/ismejo/wrae167. This article has 19 citations.