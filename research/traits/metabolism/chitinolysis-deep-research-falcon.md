---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:24:30.059455'
end_time: '2026-06-18T04:31:31.610756'
duration_seconds: 421.55
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chitinolysis
  trait_identifier: traitmech:000112
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: chitinolysis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biopolymer-degradation metabolism in which an organism hydrolyzes
    chitin to N-acetylglucosamine oligomers and monomers using secreted chitinases.
  parent_traits: traitmech:000110
  synonyms: chitinolytic, chitin degradation
  evidence_summary: 'DOI:10.3389/fmicb.2013.00149:  (Beier & Bertilsson review bacterial
    chitin degradation mechanisms and ecophysiological strategies.) | DOI:10.1080/07388550601168223:  (Bhattacharya
    et al. review the properties and potential of bacterial chitinases.)'
  causal_graph_summary: 'chitinolysis_chitinase: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chitinolysis
- **METPO identifier:** traitmech:000112
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes chitin to N-acetylglucosamine oligomers and monomers using secreted chitinases.
- **Parent traits:** traitmech:000110
- **Synonyms:** chitinolytic, chitin degradation
- **Existing evidence:** DOI:10.3389/fmicb.2013.00149:  (Beier & Bertilsson review bacterial chitin degradation mechanisms and ecophysiological strategies.) | DOI:10.1080/07388550601168223:  (Bhattacharya et al. review the properties and potential of bacterial chitinases.)
- **Existing causal graph summary:** chitinolysis_chitinase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **chitinolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/chitinolysis.yaml`.

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
- **Trait label:** chitinolysis
- **METPO identifier:** traitmech:000112
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes chitin to N-acetylglucosamine oligomers and monomers using secreted chitinases.
- **Parent traits:** traitmech:000110
- **Synonyms:** chitinolytic, chitin degradation
- **Existing evidence:** DOI:10.3389/fmicb.2013.00149:  (Beier & Bertilsson review bacterial chitin degradation mechanisms and ecophysiological strategies.) | DOI:10.1080/07388550601168223:  (Bhattacharya et al. review the properties and potential of bacterial chitinases.)
- **Existing causal graph summary:** chitinolysis_chitinase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **chitinolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/chitinolysis.yaml`.

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


# Research Report: Microbial Trait “Chitinolysis” (METPO:traitmech:000112)

## 1) Scope summary (TraitMech curation target)
**Chitinolysis** is best operationalized as the **extracellular (or pericellular) depolymerization/hydrolysis of insoluble chitin** (a β-1,4-linked N-acetyl-D-glucosamine polymer) into **soluble chitooligosaccharides, diacetylchitobiose ((GlcNAc)2), and/or monomeric GlcNAc**, enabled primarily by secreted chitinases and accessory enzymes. A canonical framing is a **three-step process**: (i) extracellular cleavage of insoluble chitin to soluble oligomers, (ii) further hydrolysis to dimers, (iii) cleavage of dimers to monomers (GlcNAc). (beier2013bacterialchitindegradation—mechanisms pages 2-4)

**Adjacent but distinct traits / boundary cases:**
- **Chitin utilization** includes downstream **transport and intracellular catabolism** of chitin-derived sugars (e.g., periplasmic processing, PTS/ABC uptake, cytoplasmic conversion), and should be modeled as connected but not identical to chitinolysis when curating the causal graph. (ran2023genomicanalysisand pages 7-9, sanram2023structuraldisplacementmodel pages 1-2)
- **Chitin deacetylation → chitosan formation** is an important alternative transformation; it can support an alternate degradation route (via chitosanases), but is not “chitinolysis” strictly defined as hydrolysis of chitin to GlcNAc oligomers/monomers. (polishchuk2024genesofstreptomyces pages 1-3)
- **Enzymatic overlap:** chitosanases, cellulases, and lysozyme may bind/hydrolyze related substrates; these create ambiguity in assay interpretation when using plate halos or bulk “chitinase activity” readouts. (beier2013bacterialchitindegradation—mechanisms pages 1-2)

**Assay-observed phenotype proxies** commonly used for this trait include growth on chitin as sole C/N source or in vitro detection of chitinase activity/product release; however, these proxies may conflate extracellular hydrolysis, uptake, and intracellular catabolism. (polishchuk2024genesofstreptomyces pages 1-3, beier2013bacterialchitindegradation—mechanisms pages 2-4)

## 2) Current understanding: mechanistic modules (concepts/definitions)
### 2.1 Core hydrolytic enzymes and reaction products
- In bacteria, chitinases are mainly **glycoside hydrolase families GH18 and GH19**, and strains often encode **multiple chitinases that act synergistically**. (beier2013bacterialchitindegradation—mechanisms pages 2-4)
- Functional roles often partition into **endo-acting chitinases** (internal cleavages producing oligomers) versus **processive exo-acting enzymes** (releasing mainly disaccharides such as (GlcNAc)2). (beier2013bacterialchitindegradation—mechanisms pages 2-4, son2024functionalcomparisonof pages 1-2)
- Further conversion to monomer requires **β-N-acetylglucosaminidase / β-N-acetylhexosaminidase activity**, which can hydrolyze oligomers/dimers to **GlcNAc**. (son2024functionalcomparisonof pages 1-2)

### 2.2 Accessory oxidative depolymerization (LPMO module)
A 2024 synthesis of Streptomyces chitin catabolism highlights **lytic polysaccharide monooxygenases (LPMOs)** as an auxiliary pathway that **oxidatively cleaves chitin and accelerates hydrolysis**, conditioned on cofactors (e.g., reductant and O2/H2O2 per figure described). (polishchuk2024genesofstreptomyces pages 1-3)

### 2.3 Transport and periplasmic processing (Vibrio model system)
Recent 2023 structural/biochemical work provides a high-resolution view of the **“extracellular hydrolysis → outer membrane transport → periplasmic processing → inner membrane uptake → regulation”** chain, especially in marine **Vibrio**:
- **Chitoporin (ChiP/VhChiP)** functions as a **chitooligosaccharide-specific outer membrane porin**, enabling (GlcNAc)n entry to the periplasm. (sanram2023structuraldisplacementmodel pages 1-2, sanram2023structuraldisplacementmodel pages 7-8)
- In the periplasm, imported chitooligosaccharides can be further degraded by enzymes such as **chitin dextrinase / exo-β-N-acetylglucosaminidases** to yield **GlcNAc and (GlcNAc)2**. (sanram2023structuraldisplacementmodel pages 1-2)
- **Inner-membrane uptake** is mediated by a **GlcNAc-specific PTS transporter** and a **(GlcNAc)2 ABC transporter**, respectively. (sanram2023structuraldisplacementmodel pages 1-2)

### 2.4 Regulation by soluble products and two-component sensing
- A general principle (already emphasized in a highly cited ecology/mechanism review) is that **soluble oligomers and GlcNAc can induce chitinase expression**, though the direction of GlcNAc effects may be taxon-dependent (e.g., suppression described for some Streptomyces contexts). (beier2013bacterialchitindegradation—mechanisms pages 2-4)
- In Vibrios, **(GlcNAc)2 is explicitly described as an inducer of chitin catabolic genes**, and control is “tightly controlled by a two-component membrane-bound histidine kinase (the chitin sensor).” (sanram2023structuraldisplacementmodel pages 1-2)
- A 2023 structural paper on periplasmic binding proteins cites **ChiS** as a **noncanonical DNA-binding hybrid sensor kinase** that directly regulates the **chitin utilization program** in *Vibrio cholerae* (i.e., a specific, mechanistically grounded regulator node for causal graphs). (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 16-17, ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 17-17)

## 3) Recent developments and latest research (prioritizing 2023–2024)
### 3.1 2023–2024 advances in “uptake-first” mechanistic clarity (Vibrio)
- **Outer membrane transport mechanism (JBC 2023):** Chitoporin (VhChiP) is described as a trimeric porin with an N-terminal “N-plug” gate; steered MD and mutagenesis support a **displacement mechanism** where sugar translocation triggers N-plug ejection, and quantitative binding affinities for chitohexaose are reported (e.g., K ~2.5–5×10^5 M−1 for chitohexaose binding). (sanram2023structuraldisplacementmodel pages 7-8)
- **Periplasmic binding proteins (Sci Rep 2023):** Periplasmic chitooligosaccharide-binding proteins (CBPs/SBPs) show ligand-length-dependent binding/stabilization and are positioned as functional couplers between periplasmic substrates and ABC uptake/signaling; e.g., binding of (GlcNAc)2–4 increases melting temperature versus apo protein, while monomeric GlcNAc binds weakly. (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 5-7)

### 3.2 2023 mechanistic “enzyme-cascade” annotation at genome scale
A 2023 study of a chitinolytic *Vibrio harveyi* strain reports a **cascade** model: secreted GH18 endochitinases produce oligomers, exo-acting enzymes trim to (GlcNAc)2, and a putative cytoplasmic chitinase hydrolyzes dimers to monomers; it also notes conserved uptake/catabolism operons (Nag and (GlcNAc)2 operons) and a porin (ChiP) for oligomer entry. (ran2023genomicanalysisand pages 7-9)

### 3.3 2024 expansion of “application-ready” enzyme properties
- A 2024 enzyme characterization reports high-yield conversion of colloidal chitin into **GlcNAc and (GlcNAc)2** using a GH18 chitinase (MaChi1), giving concrete mass yields per gram of chitin (see Section 5). (guo2024heterologousexpressionand pages 10-12)
- A 2024 antifungal formulation paper demonstrates that **immobilizing chitinase on UiO-66 MOF nanoparticles** can markedly improve apparent antifungal potency against **multidrug-resistant *Candida auris***. (ismail2024chitinasefunctionalizeduio66framework pages 1-2)

## 4) Candidate nodes for TraitMech causal graph (grouped + grounded)
The following node inventory is intended to be curation-ready (with CURIE grounding where stable and evidence-supported).

| Node type | Label | Brief role in chitinolysis | Suggested grounding CURIE(s) | Evidence citation(s) |
|---|---|---|---|---|
| Phenotype/trait | chitinolysis | Trait representing extracellular and pericellular hydrolysis of insoluble chitin to soluble chitooligosaccharides, diacetylchitobiose, and/or GlcNAc that can then be imported and catabolized | METPO:traitmech:000112; GO:0006032 | (beier2013bacterialchitindegradation—mechanisms pages 2-4, beier2013bacterialchitindegradation—mechanisms pages 1-2) |
| Phenotype/trait | chitin utilization | Broader downstream capacity that includes uptake and intracellular catabolism of chitin-derived sugars; useful boundary node distinct from polymer hydrolysis itself | GO:1901136 | (ran2023genomicanalysisand pages 7-9, sanram2023structuraldisplacementmodel pages 1-2) |
| Substrates & products | chitin | Primary insoluble polymeric substrate for the trait; β-1,4-linked N-acetyl-D-glucosamine polymer | CHEBI:35172 | (beier2013bacterialchitindegradation—mechanisms pages 1-2, son2024functionalcomparisonof pages 1-2) |
| Substrates & products | chitooligosaccharides ((GlcNAc)n) | Soluble extracellular/periplasmic hydrolysis products that act as transport substrates and regulatory signals | CHEBI: not resolved | (beier2013bacterialchitindegradation—mechanisms pages 2-4, ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 1-2, sanram2023structuraldisplacementmodel pages 1-2) |
| Substrates & products | diacetylchitobiose ((GlcNAc)2) | Major product of exo-chitinases and key transported/signaling intermediate in Vibrio systems | CHEBI:28141 | (beier2013bacterialchitindegradation—mechanisms pages 2-4, sanram2023structuraldisplacementmodel pages 1-2, ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 7-10) |
| Substrates & products | N-acetyl-D-glucosamine (GlcNAc) | Monomeric end product and imported carbon/nitrogen source; also can regulate chitinase expression in some taxa | CHEBI:506227 | (beier2013bacterialchitindegradation—mechanisms pages 2-4, sanram2023structuraldisplacementmodel pages 1-2) |
| Substrates & products | chitosan | Product of chitin deacetylation; defines an alternative branch distinct from direct chitin hydrolysis | CHEBI:18154 | (polishchuk2024genesofstreptomyces pages 1-3, beier2013bacterialchitindegradation—mechanisms pages 1-2) |
| Enzymes/proteins | chitinase (GH18/GH19) | Core extracellular hydrolases that cleave internal and/or terminal β-1,4 glycosidic bonds in chitin | GO:0004568; EC:3.2.1.14 | (beier2013bacterialchitindegradation—mechanisms pages 2-4, unuofin2024chitinasesexpandingthe pages 5-6, son2024functionalcomparisonof pages 1-2) |
| Enzymes/proteins | endochitinase | Non-processive/internal bond-cleaving enzyme producing soluble oligomers from insoluble chitin | EC:3.2.1.14 | (beier2013bacterialchitindegradation—mechanisms pages 2-4, son2024functionalcomparisonof pages 1-2) |
| Enzymes/proteins | exochitinase / chitobiosidase | Processive chain-end hydrolase releasing mainly (GlcNAc)2 from chitin/chitodextrins | EC:3.2.1.29 | (beier2013bacterialchitindegradation—mechanisms pages 2-4, son2024functionalcomparisonof pages 1-2) |
| Enzymes/proteins | β-N-acetylhexosaminidase / β-N-acetylglucosaminidase | Hydrolyzes chitooligosaccharides or chitobiose to GlcNAc monomers | EC:3.2.1.52; EC:3.2.1.30 | (polishchuk2024genesofstreptomyces pages 1-3, son2024functionalcomparisonof pages 1-2, sanram2023structuraldisplacementmodel pages 1-2) |
| Enzymes/proteins | lytic polysaccharide monooxygenase (LPMO; AA10) | Oxidatively cleaves crystalline chitin and accelerates hydrolytic depolymerization | EC:1.14.99.54 | (polishchuk2024genesofstreptomyces pages 1-3, unuofin2024chitinasesexpandingthe pages 2-5) |
| Enzymes/proteins | chitin deacetylase / chitooligodeacetylase | Deacetylates chitin or chitooligosaccharides to chitosan/chitosan oligomers; alternative branch from direct hydrolysis | EC:3.5.1.41 | (polishchuk2024genesofstreptomyces pages 1-3) |
| Enzymes/proteins | chitosanase | Hydrolyzes chitosan generated after deacetylation, supporting an alternate catabolic route | EC:3.2.1.132 | (polishchuk2024genesofstreptomyces pages 1-3, beier2013bacterialchitindegradation—mechanisms pages 1-2) |
| Enzymes/proteins | Chi4733 (Vibrio harveyi) | Example GH18 endochitinase producing mainly (GlcNAc)2 and minor (GlcNAc)3 from colloidal chitin | label-only candidate; GH18 family | (ran2023genomicanalysisand pages 7-9, ran2023genomicanalysisand pages 6-7) |
| Enzymes/proteins | Chi540 (Vibrio harveyi) | Example exo-chitinase producing mainly (GlcNAc)2 from colloidal chitin | label-only candidate | (ran2023genomicanalysisand pages 7-9, ran2023genomicanalysisand pages 6-7) |
| Enzymes/proteins | Chi4963 (Vibrio harveyi) | Putative cytoplasmic chitinase involved in hydrolysis of imported dimers to monomers | label-only candidate | (ran2023genomicanalysisand pages 7-9) |
| Transport systems | chitoporin (ChiP/VhChiP/VcChiP) | Outer-membrane porin transporting chitooligosaccharides into the periplasm in marine Vibrios | GO:0015288 (general porin activity, tentative); label-only candidate ChiP | (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 1-2, sanram2023structuraldisplacementmodel pages 1-2, sanram2023structuraldisplacementmodel pages 7-8) |
| Transport systems | periplasmic chitooligosaccharide-binding protein (CBP/SBP) | Periplasmic binding protein that captures (GlcNAc)n and couples transport/signaling in Vibrio | label-only candidate | (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 1-2, ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 5-7, ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 7-10) |
| Transport systems | GlcNAc-specific PTS transporter | Imports GlcNAc across the inner membrane during chitin-derived sugar assimilation | KEGG:K02777/K02778/K02779/K02790 (candidate PTS components) | (beier2013bacterialchitindegradation—mechanisms pages 2-4, sanram2023structuraldisplacementmodel pages 1-2) |
| Transport systems | (GlcNAc)2 ABC transporter | Imports diacetylchitobiose across the inner membrane in Vibrio chitin catabolism | label-only candidate ABC transporter | (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 1-2, sanram2023structuraldisplacementmodel pages 1-2) |
| Transport systems | Ngc transporter | Actinobacterial/Streptomyces transporter for uptake of N-acetylglucosamine and related chitin-derived products | label-only candidate | (polishchuk2024genesofstreptomyces pages 1-3) |
| Regulatory systems | chitooligosaccharide signal | Soluble chitin breakdown products that induce/coordinate the chitin catabolic cascade | GO:0007165 (generic signaling, broad) | (beier2013bacterialchitindegradation—mechanisms pages 2-4, sanram2023structuraldisplacementmodel pages 1-2, sanram2023structuraldisplacementmodel pages 14-15) |
| Regulatory systems | ChiS chitin sensor kinase | Noncanonical two-component/hybrid sensor kinase directly regulating the Vibrio chitin utilization program | label-only candidate; GO:0000155 (signal transduction system) | (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 16-17, sanram2023structuraldisplacementmodel pages 1-2, ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 17-17) |
| Regulatory systems | product induction by soluble oligomers and GlcNAc | Regulatory module in which soluble hydrolysis products induce chitinase/chitin-catabolic gene expression | GO:0010628 (broad positive regulation of gene expression, tentative) | (beier2013bacterialchitindegradation—mechanisms pages 2-4, unuofin2024chitinasesexpandingthe pages 2-5) |
| Environmental/experimental factors | temperature | Major driver of chitinase activity, stability, and community composition; effects vary by enzyme/taxon | ENVO:01000254 | (ran2023genomicanalysisand pages 6-7, beier2013bacterialchitindegradation—mechanisms pages 1-2, unuofin2024chitinasesexpandingthe pages 5-6) |
| Environmental/experimental factors | pH | Major driver of chitinase activity and habitat-specific importance of bacterial vs fungal degradation | ENVO:09200015 | (ran2023genomicanalysisand pages 6-7, beier2013bacterialchitindegradation—mechanisms pages 1-2, unuofin2024chitinasesexpandingthe pages 5-6) |
| Environmental/experimental factors | substrate accessibility / crystallinity | Natural chitin association with proteins/glucans and substrate form affects enzyme access and turnover | label-only candidate | (beier2013bacterialchitindegradation—mechanisms pages 1-2, guo2024heterologousexpressionand pages 10-12) |
| Environmental/experimental factors | alternative carbon and nitrogen sources | Nutrient regime modulates chitinase production and measured hydrolysis activity | label-only candidate | (beier2013bacterialchitindegradation—mechanisms pages 2-4, unuofin2024chitinasesexpandingthe pages 5-6) |
| Environmental/experimental factors | metal ions and chemical inhibitors | Can activate or inhibit specific chitinases, affecting observed chitinolytic phenotype | CHEBI:23367 (metal cation); CHEBI:48139 (SDS) | (ran2023genomicanalysisand pages 6-7, guo2024heterologousexpressionand pages 12-13) |
| Environmental/experimental factors | oxygen / H2O2 / reductant availability | Required cofactors/conditions for LPMO-mediated oxidative cleavage of chitin | CHEBI:15379; CHEBI:16240 | (polishchuk2024genesofstreptomyces pages 1-3) |
| Environmental/experimental factors | habitat context (water vs soil/sediment) | Influences dominance of hydrolysis vs deacetylation-linked routes and community composition | ENVO:00002042; ENVO:00001998; ENVO:00010483 | (beier2013bacterialchitindegradation—mechanisms pages 2-4, beier2013bacterialchitindegradation—mechanisms pages 1-2) |


*Table: This table lists candidate causal-graph nodes for the microbial trait chitinolysis, grouped by biological role and grounded to stable identifiers where possible. It is useful for TraitMech curation because it separates core hydrolytic steps from transport, regulation, and alternative deacetylation/chitosan branches, while showing the specific evidence supporting each node.*

## 5) Candidate causal edges (evidence-backed triples with quotes/snippets)
The following edges are proposed as minimal, evidence-backed starting points for `chitinolysis.yaml` curation.

| Subject node | Predicate | Object node | Evidence snippet | Reference | Notes/curation confidence |
|---|---|---|---|---|---|
| chitinase (GH18/GH19) | hydrolyzes_to | chitooligosaccharides | “extracellular cleavage of insoluble chitin into soluble oligomers” and “chitinases… cleave the β-1,4-glycosidic bonds of chitin to produce chitooligosaccharides” (beier2013bacterialchitindegradation—mechanisms pages 2-4, unuofin2024chitinasesexpandingthe pages 5-6) | 10.3389/fmicb.2013.00149 (2013) https://doi.org/10.3389/fmicb.2013.00149; 10.1007/s11356-024-33728-6 (2024) https://doi.org/10.1007/s11356-024-33728-6 | Core trait-defining edge; broad taxonomic support; high confidence. |
| exochitinase / chitobiosidase | hydrolyzes_to | diacetylchitobiose ((GlcNAc)2) | “processive exoenzymes… release disaccharides” and “chitobiosidases… release di-acetylchitobiose from chain ends” (beier2013bacterialchitindegradation—mechanisms pages 2-4, son2024functionalcomparisonof pages 1-2) | 10.3389/fmicb.2013.00149 (2013) https://doi.org/10.3389/fmicb.2013.00149; 10.3390/toxins16010026 (2024) https://doi.org/10.3390/toxins16010026 | Well-supported mechanistic edge; high confidence. |
| β-N-acetylhexosaminidase / β-N-acetylglucosaminidase | hydrolyzes_to | N-acetyl-D-glucosamine (GlcNAc) | “β-N-acetylglucosaminidases… hydrolyze oligomers ((GlcNAc)2–(GlcNAc)4) to GlcNAc monomers” (son2024functionalcomparisonof pages 1-2) | 10.3390/toxins16010026 (2024) https://doi.org/10.3390/toxins16010026 | Supports monomer-production step; use broad enzyme class node; high confidence. |
| chitoporin (ChiP) | transports_into | periplasmic chitooligosaccharides ((GlcNAc)n) | “transported through outer-membrane chitoporin into the periplasm” and “VhChiP as a chitooligosaccharide-specific outer membrane porin” (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 1-2, sanram2023structuraldisplacementmodel pages 1-2) | 10.1038/s41598-023-47253-y (2023) https://doi.org/10.1038/s41598-023-47253-y; 10.1016/j.jbc.2023.105000 (2023) https://doi.org/10.1016/j.jbc.2023.105000 | Strong for Vibrio; taxon-specific, so mark as lineage-specific if curated globally. |
| periplasmic chitin dextrinase / exo-β-N-acetylglucosaminidase | hydrolyzes_to | GlcNAc and diacetylchitobiose ((GlcNAc)2) | “these are further degraded in the periplasm by chitin dextrinase or exo-β-N-acetylglucosaminidases to D-GlcNAc and (GlcNAc)2” (sanram2023structuraldisplacementmodel pages 1-2) | 10.1016/j.jbc.2023.105000 (2023) https://doi.org/10.1016/j.jbc.2023.105000 | Good mechanistic support; mainly Vibrio/periplasmic pathway context; medium-high confidence. |
| GlcNAc-specific PTS transporter | transports_into | cytoplasmic GlcNAc | “D-GlcNAc and (GlcNAc)2 are then taken up by a GlcNAc-specific PTS transporter” (sanram2023structuraldisplacementmodel pages 1-2) | 10.1016/j.jbc.2023.105000 (2023) https://doi.org/10.1016/j.jbc.2023.105000 | Strong but pathway-specific; suitable as transport edge; high confidence in Vibrio context. |
| (GlcNAc)2 ABC transporter | transports_into | cytoplasmic diacetylchitobiose ((GlcNAc)2) | “D-GlcNAc and (GlcNAc)2 are then taken up by… a (GlcNAc)2 ABC transporter” (sanram2023structuraldisplacementmodel pages 1-2) | 10.1016/j.jbc.2023.105000 (2023) https://doi.org/10.1016/j.jbc.2023.105000 | Strong transport edge; Vibrio-focused; high confidence in that clade. |
| diacetylchitobiose ((GlcNAc)2) | induces_expression_of | chitin catabolic genes | “Expression of the chitin catabolic genes is (GlcNAc)2-inducible” (sanram2023structuraldisplacementmodel pages 1-2) | 10.1016/j.jbc.2023.105000 (2023) https://doi.org/10.1016/j.jbc.2023.105000 | Direct regulatory statement; likely best curated as positive regulation by chitobiose signal; high confidence in Vibrio. |
| ChiS / two-component chitin sensor kinase | positively_regulates | chitin utilization genes | “two-component chitin catabolic sensor/kinase… directly regulates the chitin utilization program” (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 16-17, ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 17-17) | 10.1038/s41598-023-47253-y (2023) https://doi.org/10.1038/s41598-023-47253-y | Strong regulatory node for Vibrio; use taxon-specific note. |
| LPMO (AA10) | oxidatively_cleaves | chitin | “Polysaccharide monooxygenases (LPMOs) oxidatively cleave the polymer and accelerate hydrolysis” (polishchuk2024genesofstreptomyces pages 1-3) | 10.15407/microbiolj86.04.053 (2024) https://doi.org/10.15407/microbiolj86.04.053 | Good support for auxiliary oxidative route; evidence from Streptomyces-focused genomic/functional synthesis; medium confidence for broad curation. |
| LPMO (AA10) | positively_regulates | chitin hydrolysis | “oxidatively cleave the polymer and accelerate hydrolysis” (polishchuk2024genesofstreptomyces pages 1-3) | 10.15407/microbiolj86.04.053 (2024) https://doi.org/10.15407/microbiolj86.04.053 | Useful higher-level edge; somewhat inferred from wording; medium confidence. |
| chitin deacetylase | converts_to | chitosan | “deacetylation by chitindeacetylases and chitooligodeacetylases… producing chitosan oligomers” and “Chitin deacetylation results in the formation of chitosan” (polishchuk2024genesofstreptomyces pages 1-3, unuofin2024chitinasesexpandingthe pages 2-5) | 10.15407/microbiolj86.04.053 (2024) https://doi.org/10.15407/microbiolj86.04.053; 10.3389/fpls.2023.1335646 (2024) https://doi.org/10.3389/fpls.2023.1335646 | Important boundary-case edge: adjacent to, but distinct from, strict chitinolysis. Curate with caution. |
| chitosanase | hydrolyzes_to | chitosan oligomers / monomers | “chitosan oligomers… are then cleaved by chitosanases (GH75)” (polishchuk2024genesofstreptomyces pages 1-3) | 10.15407/microbiolj86.04.053 (2024) https://doi.org/10.15407/microbiolj86.04.053 | Alternative branch after deacetylation; not core chitinolysis unless graph includes chitosan route; medium confidence. |
| Ca2+, Co2+, Sr2+, Mg2+ | positively_regulates | Chi4733 activity | “Chi4733 was… activated by Ca2+, Co2+, Sr2+, and Mg2+” (ran2023genomicanalysisand pages 6-7) | 10.3389/fmicb.2023.1121720 (2023) https://doi.org/10.3389/fmicb.2023.1121720 | Enzyme-specific experimental edge from Vibrio harveyi; curate as assay-specific. |
| Al3+, Zn2+, Cu2+, Ni2+, SDS | inhibits_activity_of | Chi4733 | “Chi4733… inhibited by Al3+, Zn2+, Cu2+, Ni2+ and SDS” (ran2023genomicanalysisand pages 6-7) | 10.3389/fmicb.2023.1121720 (2023) https://doi.org/10.3389/fmicb.2023.1121720 | Assay-specific inhibition edge; not generalizable to all chitinases. |
| Sr2+, Ca2+, Mg2+ | positively_regulates | Chi540 activity | “Chi540… was activated by Sr2+, Ca2+, and Mg2+” (ran2023genomicanalysisand pages 6-7) | 10.3389/fmicb.2023.1121720 (2023) https://doi.org/10.3389/fmicb.2023.1121720 | Enzyme-specific activation edge; assay-specific. |
| K+, Ba2+, Zn2+, Cu2+, Ni2+, SDS, urea | inhibits_activity_of | Chi540 | “Chi540… inhibited by K+, Ba2+, Zn2+, Cu2+, Ni2+, SDS and urea” (ran2023genomicanalysisand pages 6-7) | 10.3389/fmicb.2023.1121720 (2023) https://doi.org/10.3389/fmicb.2023.1121720 | Enzyme-specific inhibition edge; assay-specific; medium confidence for generalized inhibitor node. |


*Table: This table compiles evidence-backed subject-predicate-object edges relevant to microbial chitinolysis, emphasizing core hydrolysis, transport, regulation, and alternative deacetylation branches. It is useful for TraitMech curation because each proposed edge includes a supporting quote, DOI-first reference, and a confidence note indicating whether the claim is broad or taxon-/assay-specific.*

## 6) Current applications and real-world implementations (with recent quantitative data)
### 6.1 Chitin waste valorization to GlcNAc and chitooligosaccharides
A 2024 study using a pH-stable chitinase (MaChi1, GH18) demonstrates conversion of colloidal chitin to value-added products with reported yields of **227.2 mg GlcNAc/g chitin** and **505.9 mg (GlcNAc)2/g chitin**, and conversion peaking at **~75.9% after 12 h** under the authors’ optimal conditions. (guo2024heterologousexpressionand pages 10-12)

### 6.2 Enzyme immobilization as an antifungal strategy (biomedical / infection control)
A 2024 report on chitinase-functionalized UiO-66 MOF nanoparticles (produced chitinase from *Talaromyces varians* SSW3) provides an example of real-world translation steps (strain production optimization → enzyme purification → immobilization → antimicrobial testing). It reports:
- Production improved from **8.97 U/g dry substrate** to **120.41 U/g dry substrate** after statistical optimization. (ismail2024chitinasefunctionalizeduio66framework pages 1-2)
- UiO-66 particle size **70.42 ± 8.43 nm** and immobilization yield **65%** after 6 h loading. (ismail2024chitinasefunctionalizeduio66framework pages 1-2)
- Antifungal potency improved: immobilized chitinase MIC50 **0.89 ± 0.056 U/mL** vs free enzyme **5.582 ± 0.57 U/mL** against *C. auris*. (ismail2024chitinasefunctionalizeduio66framework pages 1-2)

These results support a curation-relevant “application module” edge: **immobilization/formulation → increased stability/effective activity → lower MIC50**, but that edge should be labeled as formulation-specific rather than a universal property of chitinases. (ismail2024chitinasefunctionalizeduio66framework pages 1-2)

### 6.3 Agricultural biocontrol and insecticidal/antifungal activity
A 2024 comparison of chitinases from symbiotic bacteria of entomopathogenic nematodes reports antifungal IC50 values, including **0.031 mg/mL (IC50) against *Fusarium oxysporum*** (for one of the chitinases tested) and other IC50s in the ~0.046–0.072 mg/mL range depending on enzyme/target fungus; the work explicitly frames these as a route toward biological control of insect pests and fungal plant diseases. (son2024functionalcomparisonof pages 1-2)

### 6.4 Environmental and process optimization heuristics (expert synthesis)
A 2024 review emphasizes that chitinase performance/production is shaped by **pH, temperature, nutrient composition, fermentation mode**, and other process factors—supporting the inclusion of environmental/experimental nodes in TraitMech graphs rather than treating chitinolysis as purely gene-centric. (unuofin2024chitinasesexpandingthe pages 5-6)

## 7) Key statistics/data points suitable for curation
- **Enzyme catalytic/assay parameters (example, *Vibrio harveyi* chitinases):** specific activities **175.5 U/mg** (Chi4733) and **134.5 U/mg** (Chi540); temperature optima around **50°C** and **60°C**; pH optima spanning **pH 4–6** and **pH 5–8**; activation by divalent cations (e.g., Ca2+, Mg2+) and inhibition by metals/SDS/urea depending on enzyme. (ran2023genomicanalysisand pages 6-7)
- **Chitoporin substrate-binding:** chitohexaose binding affinity for VhChiP reported as **K ~2.5–5×10^5 M−1**; mechanistic support for gating/displacement by N-plug. (sanram2023structuraldisplacementmodel pages 7-8)
- **Periplasmic CBP binding specificity:** strong stabilization/binding for (GlcNAc)2–4, weak for monomeric GlcNAc; quantitative association constant for (GlcNAc)2 reported (Kassoc ~4.08×10^6 M−1). (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 5-7, ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 7-10)

## 8) Warnings / “do not curate yet” items
1. **Do not equate “growth on chitin” with “chitinolysis” without separating transport/catabolism:** growth phenotypes can reflect uptake and intracellular metabolism rather than extracellular hydrolysis, and can be influenced by cross-feeding in communities. (beier2013bacterialchitindegradation—mechanisms pages 1-2)
2. **Vibrio-specific transport/regulation nodes (ChiP/CBP/ChiS) should be curated with taxon constraints** (e.g., NCBITaxon:662 for *Vibrio* genus) unless broader evidence is added for other clades. (sanram2023structuraldisplacementmodel pages 1-2, ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 16-17)
3. **Deacetylation → chitosan route is a boundary module:** it is mechanistically adjacent and may be important in soils/sediments, but should be modeled as an alternative branch and not merged into the core “hydrolysis-only” definition without an explicit scoping decision. (polishchuk2024genesofstreptomyces pages 1-3, beier2013bacterialchitindegradation—mechanisms pages 2-4)
4. **Ion activation/inhibition edges are often enzyme- and assay-specific** (buffer, substrate form, temperature); curate them as conditional modifiers (experimental factors) rather than general properties of “chitinase.” (ran2023genomicanalysisand pages 6-7)

## DOI-first bibliography (with URLs and publication dates where available)
1. **Guo H-Z, et al. (2024-06).** Heterologous Expression and Characterization of a pH-Stable Chitinase from *Micromonospora aurantiaca* with a Potential Application in Chitin Degradation. *Marine Drugs* 22:287. **DOI:** 10.3390/md22060287. https://doi.org/10.3390/md22060287 (guo2024heterologousexpressionand pages 10-12)
2. **Ismail SA, et al. (2024-07).** Chitinase-functionalized UiO-66 framework nanoparticles active against multidrug-resistant *Candida auris*. *BMC Microbiology* 24. **DOI:** 10.1186/s12866-024-03414-1. https://doi.org/10.1186/s12866-024-03414-1 (ismail2024chitinasefunctionalizeduio66framework pages 1-2)
3. **Unuofin JO, et al. (2024-05).** Chitinases: expanding the boundaries of knowledge beyond routinized chitin degradation. *Environmental Science and Pollution Research* 31:38045–38060. **DOI:** 10.1007/s11356-024-33728-6. https://doi.org/10.1007/s11356-024-33728-6 (unuofin2024chitinasesexpandingthe pages 5-6)
4. **Polishchuk LV (2024-09).** Genes of *Streptomyces globisporus* 1912-4Crt Encoding Chitin Catabolism Enzymes. *Mikrobiolohichnyi Zhurnal* 86:53–63. **DOI:** 10.15407/microbiolj86.04.053. https://doi.org/10.15407/microbiolj86.04.053 (polishchuk2024genesofstreptomyces pages 1-3)
5. **Son D-J, et al. (2024-01).** Functional Comparison of Three Chitinases from Symbiotic Bacteria of Entomopathogenic Nematodes. *Toxins* 16:26. **DOI:** 10.3390/toxins16010026. https://doi.org/10.3390/toxins16010026 (son2024functionalcomparisonof pages 1-2)
6. **Ohnuma T, et al. (2023-11).** Periplasmic chitooligosaccharide-binding protein requires a three-domain organization for substrate translocation. *Scientific Reports* 13. **DOI:** 10.1038/s41598-023-47253-y. https://doi.org/10.1038/s41598-023-47253-y (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 1-2)
7. **Sanram S, et al. (2023-08).** Structural displacement model of chitooligosaccharide transport through chitoporin. *Journal of Biological Chemistry* 299:105000. **DOI:** 10.1016/j.jbc.2023.105000. https://doi.org/10.1016/j.jbc.2023.105000 (sanram2023structuraldisplacementmodel pages 1-2)
8. **Ran L, et al. (2023-07).** Genomic analysis and chitinase characterization of *Vibrio harveyi* WXL538: insight into its adaptation to the marine environment. *Frontiers in Microbiology* 14. **DOI:** 10.3389/fmicb.2023.1121720. https://doi.org/10.3389/fmicb.2023.1121720 (ran2023genomicanalysisand pages 7-9)
9. **Beier S, Bertilsson S (2013-06).** Bacterial chitin degradation—mechanisms and ecophysiological strategies. *Frontiers in Microbiology* 4. **DOI:** 10.3389/fmicb.2013.00149. https://doi.org/10.3389/fmicb.2013.00149 (beier2013bacterialchitindegradation—mechanisms pages 2-4)


References

1. (beier2013bacterialchitindegradation—mechanisms pages 2-4): Sara Beier and Stefan Bertilsson. Bacterial chitin degradation—mechanisms and ecophysiological strategies. Frontiers in Microbiology, Jun 2013. URL: https://doi.org/10.3389/fmicb.2013.00149, doi:10.3389/fmicb.2013.00149. This article has 605 citations and is from a peer-reviewed journal.

2. (ran2023genomicanalysisand pages 7-9): Lingman Ran, Xiaolei Wang, Xinxin He, Ruihong Guo, Yanhong Wu, Pingping Zhang, and Xiao-Hua Zhang. Genomic analysis and chitinase characterization of vibrio harveyi wxl538: insight into its adaptation to the marine environment. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1121720, doi:10.3389/fmicb.2023.1121720. This article has 15 citations and is from a peer-reviewed journal.

3. (sanram2023structuraldisplacementmodel pages 1-2): Surapoj Sanram, Anuwat Aunkham, Robert Robinson, and Wipa Suginta. Structural displacement model of chitooligosaccharide transport through chitoporin. Journal of Biological Chemistry, 299:105000, Aug 2023. URL: https://doi.org/10.1016/j.jbc.2023.105000, doi:10.1016/j.jbc.2023.105000. This article has 3 citations and is from a domain leading peer-reviewed journal.

4. (polishchuk2024genesofstreptomyces pages 1-3): L. V. Polishchuk. Genes of streptomyces globisporus 1912-4crt encoding chitin catabolism enzymes. Mikrobiolohichnyi Zhurnal, 86:53-63, Sep 2024. URL: https://doi.org/10.15407/microbiolj86.04.053, doi:10.15407/microbiolj86.04.053. This article has 1 citations.

5. (beier2013bacterialchitindegradation—mechanisms pages 1-2): Sara Beier and Stefan Bertilsson. Bacterial chitin degradation—mechanisms and ecophysiological strategies. Frontiers in Microbiology, Jun 2013. URL: https://doi.org/10.3389/fmicb.2013.00149, doi:10.3389/fmicb.2013.00149. This article has 605 citations and is from a peer-reviewed journal.

6. (son2024functionalcomparisonof pages 1-2): Da-Jeong Son, Geun-Gon Kim, Ho-Yul Choo, Nam-Jun Chung, and Young-Moo Choo. Functional comparison of three chitinases from symbiotic bacteria of entomopathogenic nematodes. Toxins, 16:26, Jan 2024. URL: https://doi.org/10.3390/toxins16010026, doi:10.3390/toxins16010026. This article has 10 citations.

7. (sanram2023structuraldisplacementmodel pages 7-8): Surapoj Sanram, Anuwat Aunkham, Robert Robinson, and Wipa Suginta. Structural displacement model of chitooligosaccharide transport through chitoporin. Journal of Biological Chemistry, 299:105000, Aug 2023. URL: https://doi.org/10.1016/j.jbc.2023.105000, doi:10.1016/j.jbc.2023.105000. This article has 3 citations and is from a domain leading peer-reviewed journal.

8. (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 16-17): Takayuki Ohnuma, Jun Tsujii, Chikara Kataoka, Teruki Yoshimoto, Daijiro Takeshita, Outi Lampela, André H. Juffer, Wipa Suginta, and Tamo Fukamizo. Periplasmic chitooligosaccharide-binding protein requires a three-domain organization for substrate translocation. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-47253-y, doi:10.1038/s41598-023-47253-y. This article has 1 citations and is from a peer-reviewed journal.

9. (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 17-17): Takayuki Ohnuma, Jun Tsujii, Chikara Kataoka, Teruki Yoshimoto, Daijiro Takeshita, Outi Lampela, André H. Juffer, Wipa Suginta, and Tamo Fukamizo. Periplasmic chitooligosaccharide-binding protein requires a three-domain organization for substrate translocation. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-47253-y, doi:10.1038/s41598-023-47253-y. This article has 1 citations and is from a peer-reviewed journal.

10. (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 5-7): Takayuki Ohnuma, Jun Tsujii, Chikara Kataoka, Teruki Yoshimoto, Daijiro Takeshita, Outi Lampela, André H. Juffer, Wipa Suginta, and Tamo Fukamizo. Periplasmic chitooligosaccharide-binding protein requires a three-domain organization for substrate translocation. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-47253-y, doi:10.1038/s41598-023-47253-y. This article has 1 citations and is from a peer-reviewed journal.

11. (guo2024heterologousexpressionand pages 10-12): Han-Zhong Guo, Dou Wang, Hui-Ting Yang, Yu-Le Wu, Yong-Cheng Li, Guang-Hua Xia, and Xue-Ying Zhang. Heterologous expression and characterization of a ph-stable chitinase from micromonospora aurantiaca with a potential application in chitin degradation. Marine Drugs, 22:287, Jun 2024. URL: https://doi.org/10.3390/md22060287, doi:10.3390/md22060287. This article has 12 citations.

12. (ismail2024chitinasefunctionalizeduio66framework pages 1-2): Shaymaa A. Ismail, Bahgat Fayed, Reda M. Abdelhameed, and Amira A. Hassan. Chitinase-functionalized uio-66 framework nanoparticles active against multidrug-resistant candida auris. BMC Microbiology, Jul 2024. URL: https://doi.org/10.1186/s12866-024-03414-1, doi:10.1186/s12866-024-03414-1. This article has 12 citations and is from a peer-reviewed journal.

13. (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 1-2): Takayuki Ohnuma, Jun Tsujii, Chikara Kataoka, Teruki Yoshimoto, Daijiro Takeshita, Outi Lampela, André H. Juffer, Wipa Suginta, and Tamo Fukamizo. Periplasmic chitooligosaccharide-binding protein requires a three-domain organization for substrate translocation. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-47253-y, doi:10.1038/s41598-023-47253-y. This article has 1 citations and is from a peer-reviewed journal.

14. (ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 7-10): Takayuki Ohnuma, Jun Tsujii, Chikara Kataoka, Teruki Yoshimoto, Daijiro Takeshita, Outi Lampela, André H. Juffer, Wipa Suginta, and Tamo Fukamizo. Periplasmic chitooligosaccharide-binding protein requires a three-domain organization for substrate translocation. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-47253-y, doi:10.1038/s41598-023-47253-y. This article has 1 citations and is from a peer-reviewed journal.

15. (unuofin2024chitinasesexpandingthe pages 5-6): John Onolame Unuofin, Olubusola Ayoola Odeniyi, Omolara Sola Majengbasan, Aboi Igwaran, Karabelo MacMillan Moloantoa, Zenzile Peter Khetsha, Samuel Ayodele Iwarere, and Michael Olawale Daramola. Chitinases: expanding the boundaries of knowledge beyond routinized chitin degradation. Environmental Science and Pollution Research International, 31:38045-38060, May 2024. URL: https://doi.org/10.1007/s11356-024-33728-6, doi:10.1007/s11356-024-33728-6. This article has 58 citations.

16. (unuofin2024chitinasesexpandingthe pages 2-5): John Onolame Unuofin, Olubusola Ayoola Odeniyi, Omolara Sola Majengbasan, Aboi Igwaran, Karabelo MacMillan Moloantoa, Zenzile Peter Khetsha, Samuel Ayodele Iwarere, and Michael Olawale Daramola. Chitinases: expanding the boundaries of knowledge beyond routinized chitin degradation. Environmental Science and Pollution Research International, 31:38045-38060, May 2024. URL: https://doi.org/10.1007/s11356-024-33728-6, doi:10.1007/s11356-024-33728-6. This article has 58 citations.

17. (ran2023genomicanalysisand pages 6-7): Lingman Ran, Xiaolei Wang, Xinxin He, Ruihong Guo, Yanhong Wu, Pingping Zhang, and Xiao-Hua Zhang. Genomic analysis and chitinase characterization of vibrio harveyi wxl538: insight into its adaptation to the marine environment. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1121720, doi:10.3389/fmicb.2023.1121720. This article has 15 citations and is from a peer-reviewed journal.

18. (sanram2023structuraldisplacementmodel pages 14-15): Surapoj Sanram, Anuwat Aunkham, Robert Robinson, and Wipa Suginta. Structural displacement model of chitooligosaccharide transport through chitoporin. Journal of Biological Chemistry, 299:105000, Aug 2023. URL: https://doi.org/10.1016/j.jbc.2023.105000, doi:10.1016/j.jbc.2023.105000. This article has 3 citations and is from a domain leading peer-reviewed journal.

19. (guo2024heterologousexpressionand pages 12-13): Han-Zhong Guo, Dou Wang, Hui-Ting Yang, Yu-Le Wu, Yong-Cheng Li, Guang-Hua Xia, and Xue-Ying Zhang. Heterologous expression and characterization of a ph-stable chitinase from micromonospora aurantiaca with a potential application in chitin degradation. Marine Drugs, 22:287, Jun 2024. URL: https://doi.org/10.3390/md22060287, doi:10.3390/md22060287. This article has 12 citations.