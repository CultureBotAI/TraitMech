---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:58:08.101882'
end_time: '2026-06-18T05:07:52.917104'
duration_seconds: 584.82
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: fermentative hydrogen production
  trait_identifier: traitmech:000109
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: fermentative_hydrogen_production
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A fermentation in which an organism disposes of excess reducing equivalents
    by producing molecular hydrogen (H2), typically via hydrogenases acting on reduced
    ferredoxin or formate.
  parent_traits: METPO:1002005
  synonyms: biohydrogen production
  evidence_summary: 'DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy
    conservation supports H2 production as a redox-balancing fermentation output via
    hydrogenases.) | DOI:10.1016/S0360-3199(02)00131-3:  (Hallenbeck & Benemann review
    biological hydrogen production, including dark fermentative H2 generation.)'
  causal_graph_summary: 'fermentative_h2_production: 3 nodes, 2 edges'
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
- **Trait label:** fermentative hydrogen production
- **METPO identifier:** traitmech:000109
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which an organism disposes of excess reducing equivalents by producing molecular hydrogen (H2), typically via hydrogenases acting on reduced ferredoxin or formate.
- **Parent traits:** METPO:1002005
- **Synonyms:** biohydrogen production
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports H2 production as a redox-balancing fermentation output via hydrogenases.) | DOI:10.1016/S0360-3199(02)00131-3:  (Hallenbeck & Benemann review biological hydrogen production, including dark fermentative H2 generation.)
- **Existing causal graph summary:** fermentative_h2_production: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **fermentative hydrogen production** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/fermentative_hydrogen_production.yaml`.

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
- **Trait label:** fermentative hydrogen production
- **METPO identifier:** traitmech:000109
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which an organism disposes of excess reducing equivalents by producing molecular hydrogen (H2), typically via hydrogenases acting on reduced ferredoxin or formate.
- **Parent traits:** METPO:1002005
- **Synonyms:** biohydrogen production
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports H2 production as a redox-balancing fermentation output via hydrogenases.) | DOI:10.1016/S0360-3199(02)00131-3:  (Hallenbeck & Benemann review biological hydrogen production, including dark fermentative H2 generation.)
- **Existing causal graph summary:** fermentative_h2_production: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **fermentative hydrogen production** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/fermentative_hydrogen_production.yaml`.

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


## Research report: Fermentative hydrogen production (TraitMech: fermentative_h2_production; METPO traitmech:000109)

### 1) Scope summary (trait meaning, boundaries, and how it is observed)

**Trait definition (operationalized):** *Fermentative hydrogen production* is the physiological capacity to generate molecular hydrogen (H2) as an end product of **anaerobic fermentation** to dispose of excess reducing equivalents, typically through **hydrogenase-catalyzed reduction of protons using reduced ferredoxin and/or NADH**, and/or via **formate cleavage** by formate:hydrogen lyase (FHL) in some taxa. (taggar2024hydrogenproductionvia pages 5-7, taggar2024hydrogenproductionvia pages 7-8, cha2024metabolicengineeringof pages 3-4)

**What this trait is not (boundary cases):**
- Not **photofermentation/photobiological H2 production** (light-dependent processes); dark fermentation is explicitly distinguished as H2 production “in the absence of light.” (taggar2024hydrogenproductionvia pages 5-7)
- Not **respiratory H2 oxidation** (H2 consumption for energy conservation). A key boundary is that some hydrogenase complexes (e.g., HydABC) are best characterized in the **H2-oxidizing direction** (reducing ferredoxin and NAD(P)+) but are mechanistically related to fermentative redox balancing; curating a *fermentative* H2-production edge from HydABC should be flagged unless a source directly demonstrates the H2-evolving direction in vivo for the relevant organism. (katsyv2023molecularbasisof pages 2-3, katsyv2023molecularbasisof pages 1-2)
- Not **methanogenesis**; however, hydrogenotrophic partners (e.g., methanogens) can indirectly modulate this trait via interspecies H2 transfer, changing H2 yields and fermentation product ratios. (kaminsky2023rumenlachnospiraceaeisolate pages 7-10)

**Assay/phenotype readouts:** common measurements include H2 evolved (e.g., mmol/L, µmol per tube) and shifts in fermentation end-products (acetate vs butyrate) under different conditions (substrate, pH, and H2 partial pressure). (kaminsky2023rumenlachnospiraceaeisolate pages 7-10)

---

### 2) Key concepts and current mechanistic understanding (2023–2024 emphasis)

#### 2.1 Core redox logic: why H2 is produced
During fermentation, cells must reoxidize electron carriers generated in catabolism. A central mechanistic frame is that pyruvate oxidation generates **reduced ferredoxin**, and hydrogenases dispose of those reducing equivalents by producing H2. (udegbe2023metabolicengineeringof pages 36-40, cha2024metabolicengineeringof pages 3-4)

#### 2.2 Major enzymatic routes to H2 in fermentation

**A. Ferredoxin-linked H2 evolution (common in strict anaerobes)**
- **Pyruvate:ferredoxin oxidoreductase (PFOR; EC 1.2.7.1)** generates reduced ferredoxin during pyruvate conversion. (udegbe2023metabolicengineeringof pages 36-40)
- **[FeFe]-hydrogenases** (often HydA-type in clostridia and other anaerobes) produce H2 from reduced ferredoxin. (talapko2023biologicalhydrogenproduction pages 4-6, udegbe2023metabolicengineeringof pages 36-40)

**B. NADH + ferredoxin “confurcating/bifurcating” H2 evolution (important for thermodynamics)**
- In the thermophile *Caldicellulosiruptor bescii*, a **bifurcating [Fe–Fe] hydrogenase** is described to oxidize **both NADH and reduced ferredoxin** to produce H2, linking NADH reoxidation and ferredoxin disposal. (cha2024metabolicengineeringof pages 3-4)
- In a 2024 gut-microbiome preprint, a **trimeric electron-confurcating [FeFe]-hydrogenase (group A3)** is described to “confurcate electrons from reduced ferredoxin and NADH to H2,” explicitly framing this enzyme class as a fermentative redox-balancing module. (welsh2024awidespreadhydrogenase pages 8-10)

**C. Formate route (common in facultative/enteric-type fermentation)**
- **Pyruvate formate lyase (PFL; EC 2.3.1.54)** produces formate, and the **formate:hydrogen lyase (FHL)** complex converts formate to H2 + CO2; this is noted as occurring under acidic conditions in the review context. (taggar2024hydrogenproductionvia pages 5-7)

#### 2.3 Energy conservation and modular electron transfer complexes (context for node selection)
A 2024 fermentation systems review emphasizes the importance of electron-carrier accounting and highlights complexes such as **Nfn** and **Rnf** that shape reduced ferredoxin/NAD(P)H balance in fermentative pathways, and it explicitly incorporates **H2 partial pressure** into energetic calculations (using H2(g) = 10−3 bar as a high environmental value). (hackmann2024thevastlandscape pages 10-11)

An organism-level experimental/genomic study (rumen Lachnospiraceae isolate NK3A20) reports that the genome encodes multiple hydrogenases including **a membrane-bound Ech hydrogenase**, as well as **Bcd–Etf** and **Rnf**, which the authors state “may be involved” in modulating observed H2-linked pathway changes—this is mechanistically plausible but explicitly speculative and should be curated as uncertain. (kaminsky2023rumenlachnospiraceaeisolate pages 1-3)

#### 2.4 Recent structural/mechanistic advance (2023): HydABC electron bifurcation mechanism
A high-impact 2023 JACS study resolves the mechanism of the **electron-bifurcating [FeFe]-hydrogenase HydABC**, showing how a single FMN cofactor and conformational gating couple electron transfer to NAD(P)+ and ferredoxin. The authors describe that HydABC “couples H2 oxidation to the simultaneous reduction of ferredoxin and NAD(P)+,” with ferredoxin reduction “strictly dependent on NAD(P)+.” (katsyv2023molecularbasisof pages 2-3)

While this paper is primarily in the **H2-oxidizing** direction, it is directly relevant to TraitMech curation because it provides a mechanistic template for bifurcating/confurcating redox modules that—in other organisms and directions—support fermentative H2 formation and redox balancing. (katsyv2023molecularbasisof pages 2-3, katsyv2023molecularbasisof pages 8-9)

---

### 3) Candidate causal-graph nodes (curation-focused)

#### 3.1 Pathways / metabolic modules
- Dark fermentation (general process node). (taggar2024hydrogenproductionvia pages 5-7)
- Acetate-producing fermentation branch (electron-disposal favorable for higher H2 yields). (cha2024metabolicengineeringof pages 3-4)
- Butyrate-producing branch (reduced end-product sink favored under high H2). (kaminsky2023rumenlachnospiraceaeisolate pages 11-13)
- Formate pathway (PFL → FHL → H2 + CO2) (enteric/facultative boundary). (taggar2024hydrogenproductionvia pages 5-7)

#### 3.2 Genes / proteins / enzyme complexes
- **PFOR** (EC:1.2.7.1) (pyruvate → acetyl-CoA; reduces ferredoxin). (udegbe2023metabolicengineeringof pages 36-40)
- **[FeFe]-hydrogenases** (HydA-like; group B; group A3 confurcating). (talapko2023biologicalhydrogenproduction pages 4-6, welsh2024awidespreadhydrogenase pages 8-10)
- **Bifurcating [FeFe]-hydrogenase** in *C. bescii* (oxidizes NADH + reduced ferredoxin → H2). (cha2024metabolicengineeringof pages 3-4)
- **PFL** (EC:2.3.1.54) and **FHL** complex (formate → H2 + CO2). (taggar2024hydrogenproductionvia pages 5-7)
- **HydABC** electron-bifurcating [FeFe]-hydrogenase (structurally defined electron bifurcation module; directionality caveat). (katsyv2023molecularbasisof pages 2-3)
- **Ech hydrogenase, Rnf, Bcd–Etf** (genome-inferred modulators in NK3A20; uncertain functional edges). (kaminsky2023rumenlachnospiraceaeisolate pages 1-3)

#### 3.3 Chemicals / metabolites / redox carriers
Suggested groundings (where stable):
- H2 (CHEBI:18276)
- CO2 (CHEBI:16526)
- Formate (CHEBI:15740)
- NADH (CHEBI:57945)
- NAD+ (CHEBI:57540), NADP+ (CHEBI:58349)
- Acetate (CHEBI:30089)
- Butyrate (CHEBI:15522)
- Ferredoxin (CHEBI:18248); reduced ferredoxin (label-only or CHEBI candidate depending on allowed term)

#### 3.4 Environmental and experimental factors (ENVO/label candidates)
- Hydrogen partial pressure / dissolved H2 (key regulator). (kaminsky2023rumenlachnospiraceaeisolate pages 1-3, taggar2024hydrogenproductionvia pages 7-8)
- pH (affects hydrogenase activity; acidic conditions activate FHL in some contexts). (talapko2023biologicalhydrogenproduction pages 2-4, taggar2024hydrogenproductionvia pages 5-7)
- Temperature (mesophilic vs thermophilic regimes). (taggar2024hydrogenproductionvia pages 7-8)
- Substrate identity (e.g., glucose vs galacturonic acid; uronic acids). (kaminsky2023rumenlachnospiraceaeisolate pages 1-3)
- Coculture with hydrogenotrophic methanogen (interspecies hydrogen transfer). (kaminsky2023rumenlachnospiraceaeisolate pages 7-10)

---

### 4) Evidence-backed candidate causal edges (triples) for TraitMech

The following curation-ready table compiles candidate edges with quotes, DOI-first references, and uncertainty flags.

| Edge (S-P-O) | Node type(s) | Suggested ontology grounding (CURIEs where possible) | Evidence snippet (short quote) | Reference (DOI, publication year, URL) | Uncertainty/notes |
|---|---|---|---|---|---|
| pyruvate:ferredoxin oxidoreductase (PFOR) — produces — reduced ferredoxin | enzyme → metabolite | EC:1.2.7.1; GO:0018293; CHEBI:18248 (ferredoxin); CHEBI:17621 (reduced ferredoxin, candidate) | “pyruvate:ferredoxin oxidoreductase (PFOR) reduces ferredoxin (Fd) concurrently with pyruvate conversion” (udegbe2023metabolicengineeringof pages 36-40) | 2023, Udegbe, URL not available in context | Strong mechanistic edge, but source metadata are weak/unknown-journal; better to backfill with primary biochemical source before final curation. |
| reduced ferredoxin — donates electrons to — [FeFe] hydrogenase | metabolite → enzyme | CHEBI:17621 (candidate reduced ferredoxin); GO:0015705 (hydrogen transport not exact); EC:1.12.7.- ([FeFe]-hydrogenase class, candidate) | “hydrogenases produce H2 from reduced Fd” (udegbe2023metabolicengineeringof pages 36-40) | 2023, Udegbe, URL not available in context | Mechanistically central; ontology grounding for specific hydrogenase subtype should be refined during curation. |
| [FeFe] hydrogenase — produces — H2 | enzyme → chemical | EC:1.12.7.- (candidate); CHEBI:18276 (molecular hydrogen) | “[FeFe]-hydrogenases explicitly noted as producers of H2” (talapko2023biologicalhydrogenproduction pages 4-6) | 10.3390/en16083321, 2023, https://doi.org/10.3390/en16083321 | Strong broad edge for dark fermentation; subtype-specific nodes may be needed for HydA, group B, or bifurcating hydrogenases. |
| NADH:ferredoxin oxidoreductase — reduces — ferredoxin | enzyme/complex → metabolite | EC:7.2.1.2 or candidate label; CHEBI:57945 (NADH); CHEBI:18248 (ferredoxin) | “NADH can be oxidized to reduce Fd via NADH:ferredoxin oxidoreductase (NFOR)” (udegbe2023metabolicengineeringof pages 36-40) | 2023, Udegbe, URL not available in context | Useful for redox-balancing subgraph; exact EC may vary by organism/complex. |
| NADH:ferredoxin oxidoreductase — increases capacity for — H2 production | enzyme/complex → process | candidate label; METPO:traitmech:000109; CHEBI:57945; CHEBI:18276 | “yielding extra H2” (udegbe2023metabolicengineeringof pages 36-40) | 2023, Udegbe, URL not available in context | Inferred from electron routing; should be marked uncertain until supported by primary organism-specific data. |
| pyruvate formate lyase (PFL) — produces — formate | enzyme → metabolite | EC:2.3.1.54; CHEBI:15740 (formate) | “Formate produced by pyruvate formate lyase (PFL)” (taggar2024hydrogenproductionvia pages 5-7) | 10.35812/cellulosechemtechnol.2024.58.90, 2024, https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Strong for enteric/formate route; may be taxon-biased relative to clostridial ferredoxin route. |
| formate:hydrogen lyase (FHL) — converts — formate to H2 + CO2 | complex → metabolites | candidate FHL complex; CHEBI:15740 (formate); CHEBI:18276 (H2); CHEBI:16526 (CO2) | “the formate:hydrogen lyase (FHL) complex is also noted to produce H2 from formate under acidic conditions” (taggar2024hydrogenproductionvia pages 5-7) | 10.35812/cellulosechemtechnol.2024.58.90, 2024, https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Strong pathway edge, but mostly characteristic of facultative anaerobes/enterics; mark taxon-scoped if curated. |
| acidic conditions — activate/enable — FHL-mediated H2 production | environment → process/complex | ENVO:00002009 (acidic environment, candidate); candidate FHL complex | “FHL cleaves formate under acidic conditions” (taggar2024hydrogenproductionvia pages 5-7) | 10.35812/cellulosechemtechnol.2024.58.90, 2024, https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Assay/environment-dependent; use with caution as conditional edge. |
| bifurcating [FeFe] hydrogenase — oxidizes — NADH and reduced ferredoxin | enzyme/complex → metabolites | candidate HydABC-like complex; CHEBI:57945 (NADH); CHEBI:17621 (reduced ferredoxin, candidate) | “bifurcating [Fe–Fe] hydrogenase oxidizes both NADH ... and reduced ferredoxin ... to produce H2” (cha2024metabolicengineeringof pages 3-4) | 10.1007/s00253-023-12974-7, 2024, https://doi.org/10.1007/s00253-023-12974-7 | Strong for C. bescii and related thermophiles; direction here is H2-producing confurcation in fermentation context. |
| bifurcating [FeFe] hydrogenase — produces — H2 | enzyme/complex → chemical | candidate HydABC-like complex; CHEBI:18276 | “oxidizes both NADH ... and reduced ferredoxin ... to produce H2” (cha2024metabolicengineeringof pages 3-4) | 10.1007/s00253-023-12974-7, 2024, https://doi.org/10.1007/s00253-023-12974-7 | Strong, directly supports fermentative H2 trait. |
| acetate formation — is coupled to — H2 production | pathway/process → process | candidate acetate fermentation pathway; CHEBI:30089 (acetate); METPO:traitmech:000109 | “Acetate formation is coupled to H2 production to reoxidize NADH and ferredoxin” (cha2024metabolicengineeringof pages 3-4) | 10.1007/s00253-023-12974-7, 2024, https://doi.org/10.1007/s00253-023-12974-7 | Strong in the cited thermophile; may not generalize to all fermenters with same magnitude. |
| membrane [NiFe] hydrogenase — contributes to — proton motive force generation | enzyme/complex → process | [NiFe] hydrogenase candidate; GO:0015986 | “a membrane [Ni–Fe] hydrogenase whose principal role is proton pumping to generate proton motive force” (cha2024metabolicengineeringof pages 3-4) | 10.1007/s00253-023-12974-7, 2024, https://doi.org/10.1007/s00253-023-12974-7 | Important neighboring mechanism, but not a direct H2-production edge; include only if graph models energy coupling. |
| HydABC electron-bifurcating [FeFe] hydrogenase — couples — ferredoxin and NAD(P)+ redox chemistry | complex → metabolites/process | candidate HydABC; CHEBI:18248 (ferredoxin); CHEBI:57540 (NAD+); CHEBI:58349 (NADP+) | “HydABC couples H2 oxidation to the simultaneous reduction of ferredoxin and NAD(P)+” (katsyv2023molecularbasisof pages 2-3) | 10.1021/jacs.2c11683, 2023, https://doi.org/10.1021/jacs.2c11683 | High-quality structural/mechanistic evidence, but demonstrated in the H2-oxidizing direction; reverse H2-producing use in fermentation is mechanistically relevant yet partly inferred. |
| HydABC electron-bifurcating [FeFe] hydrogenase — supports — cellular redox balancing | complex → biological process | candidate HydABC; GO:0055114 (oxidation-reduction process) | “helping to balance cellular redox” (katsyv2023molecularbasisof pages 1-2) | 10.1021/jacs.2c11683, 2023, https://doi.org/10.1021/jacs.2c11683 | Good expert/mechanistic support for role; not direct phenotype measurement. |
| group A3 electron-confurcating [FeFe] hydrogenase — oxidizes — NADH and reduced ferredoxin to make H2 | enzyme/complex → metabolites/process | candidate group A3 [FeFe]-hydrogenase; CHEBI:57945; CHEBI:17621; CHEBI:18276 | “confurcate electrons from reduced ferredoxin and NADH to H2” (welsh2024awidespreadhydrogenase pages 8-10) | 10.1101/2024.08.15.608110, 2024, https://doi.org/10.1101/2024.08.15.608110 | Preprint; strong mechanistic wording, but not peer-reviewed yet. |
| group B [FeFe] hydrogenase — reoxidizes — ferredoxin during fermentation | enzyme → metabolite/process | candidate group B [FeFe]-hydrogenase; CHEBI:18248; GO:0055114 | “Bacteroides prominently use group B [FeFe]-hydrogenases to reoxidize ferredoxin during fermentation” (welsh2024awidespreadhydrogenase pages 8-10) | 10.1101/2024.08.15.608110, 2024, https://doi.org/10.1101/2024.08.15.608110 | Preprint; highly relevant for gut fermenters. Direct H2-production edge is implied but this wording is about ferredoxin reoxidation. |
| low H2 partial pressure — stimulates — H2 formation | environmental factor → process | candidate H2 partial pressure node; CHEBI:18276 | “Low ambient H2 stimulated hydrogen (H2) formation, whereas high H2 inhibited H2 formation” (kaminsky2023rumenlachnospiraceaeisolate pages 1-3) | 10.1128/aem.00634-23, 2023, https://doi.org/10.1128/aem.00634-23 | Strong experimental edge from isolate NK3A20; likely broadly relevant across fermenters. |
| high H2 partial pressure — inhibits — H2 formation | environmental factor → process | candidate H2 partial pressure node; CHEBI:18276 | “high H2 inhibited H2 formation” (kaminsky2023rumenlachnospiraceaeisolate pages 1-3) | 10.1128/aem.00634-23, 2023, https://doi.org/10.1128/aem.00634-23 | Strong experimental support. |
| high H2 partial pressure — shifts fermentation toward — butyrate formation | environmental factor → metabolite/pathway outcome | candidate H2 partial pressure node; CHEBI:15522 (butyrate) | “use of those electrons to form butyrate” and “more butyrate formation and less acetate and H2 ... when H2 partial pressures were high” (kaminsky2023rumenlachnospiraceaeisolate pages 11-13) | 10.1128/aem.00634-23, 2023, https://doi.org/10.1128/aem.00634-23 | Strong experimental edge, but organism-specific quantitative effect sizes vary with substrate. |
| low H2 partial pressure / methanogen coculture — shifts fermentation toward — acetate and H2 | environmental factor/community interaction → metabolites/outcome | candidate methanogen coculture node; CHEBI:30089 (acetate); CHEBI:18276 | “Lowering H2 by coculture with the hydrogenotrophic methanogen ... shifted NK3A20 fermentation toward increased acetate and H2 and decreased butyrate” (kaminsky2023rumenlachnospiraceaeisolate pages 7-10) | 10.1128/aem.00634-23, 2023, https://doi.org/10.1128/aem.00634-23 | Strong edge; explicitly combines interspecies H2 transfer with product-shift outcome. |
| methanogen coculture — decreases — butyrate formation | community interaction → metabolite outcome | candidate methanogen coculture node; CHEBI:15522 | “increased acetate and H2 and decreased butyrate” (kaminsky2023rumenlachnospiraceaeisolate pages 7-10) | 10.1128/aem.00634-23, 2023, https://doi.org/10.1128/aem.00634-23 | Strong in coculture experiment. |
| elevated dissolved H2 — feedback inhibits — hydrogenase activity | environmental factor → molecular function | candidate dissolved H2 node; candidate hydrogenase activity node | “increased dissolved H2 in the medium reduces hydrogenase activity ... via feedback inhibition” (taggar2024hydrogenproductionvia pages 7-8) | 10.35812/cellulosechemtechnol.2024.58.90, 2024, https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Review-level claim; useful but should ideally be backed by primary measurements in final graph. |
| low H2 partial pressure (<60 Pa) — enables — NADH-derived H2 formation | environmental factor → process | candidate H2 partial pressure node; CHEBI:57945; CHEBI:18276 | “hydrogen formation from NADH ... requires very low H2 partial pressure (‘less than 60Pa’)” (taggar2024hydrogenproductionvia pages 5-7) | 10.35812/cellulosechemtechnol.2024.58.90, 2024, https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Quantitative threshold from review; curate as conditional/uncertain until traced to original source. |
| acidic pH / low pH — inhibits — hydrogenase activity and H2 yield | environmental factor → process/function | candidate pH node; candidate hydrogenase activity node | “acidification ... lowers pH and inhibits hydrogenases” (taggar2024hydrogenproductionvia pages 7-8) | 10.35812/cellulosechemtechnol.2024.58.90, 2024, https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Review-level summary; pH optimum is system-specific. |
| pH — affects — dark fermentative H2 yield | environmental factor → outcome | candidate pH node; METPO:traitmech:000109 | “pH affects the activity of hydrogenase enzymes” (talapko2023biologicalhydrogenproduction pages 2-4) | 10.3390/en16083321, 2023, https://doi.org/10.3390/en16083321 | Broad but useful environmental edge; not directional without specific optimum context. |
| higher temperature — can increase — H2 yield | environmental factor → outcome | candidate temperature node; METPO:traitmech:000109 | “Higher temperature improves H2 yield” (udegbe2023metabolicengineeringof pages 36-40) | 2023, Udegbe, URL not available in context | Weak-to-moderate due to source quality and strong process dependence. |
| substrate type — modulates — H2 yield and end-product distribution | environmental factor/substrate → outcome | candidate substrate node | “end product ratios varied when grown with different substrates” and “lower hydrogen yields on uronic acids versus glucose” (kaminsky2023rumenlachnospiraceaeisolate pages 1-3) | 10.1128/aem.00634-23, 2023, https://doi.org/10.1128/aem.00634-23 | Strong experimental support for substrate dependence. |
| galacturonic acid substrate — shifts fermentation toward — acetate-dominant, lower-H2 state | substrate → outcome | CHEBI:61717 (galacturonic acid, candidate); CHEBI:30089; CHEBI:18276 | “shifted to mainly acetate in the presence of galacturonic acid” and “lower hydrogen yields on uronic acids versus glucose” (kaminsky2023rumenlachnospiraceaeisolate pages 1-3) | 10.1128/aem.00634-23, 2023, https://doi.org/10.1128/aem.00634-23 | Strong but taxon-specific. |
| glucose substrate — supports — higher H2 and butyrate production than galacturonic acid | substrate → outcome | CHEBI:17234 (glucose); CHEBI:18276; CHEBI:15522 | “produced acetate, butyrate, H2, and formate from glucose” and “lower hydrogen yields on uronic acids versus glucose” (kaminsky2023rumenlachnospiraceaeisolate pages 1-3) | 10.1128/aem.00634-23, 2023, https://doi.org/10.1128/aem.00634-23 | Strong within NK3A20 experiment. |
| Ech hydrogenase — may modulate — H2 formation / pathway shifts | complex → process | candidate Ech hydrogenase; [NiFe] group 4e candidate | “a membrane-bound Ech hydrogenase ... may be involved in modulating the observed metabolic pathway changes” (kaminsky2023rumenlachnospiraceaeisolate pages 1-3) | 10.1128/aem.00634-23, 2023, https://doi.org/10.1128/aem.00634-23 | Explicitly speculative in source; mark uncertain and avoid hard curation without direct functional evidence. |
| Rnf complex — may modulate — H2 formation / pathway shifts | complex → process | candidate Rnf complex | “an Rnf complex ... may be involved in modulating the observed metabolic pathway changes” (kaminsky2023rumenlachnospiraceaeisolate pages 1-3) | 10.1128/aem.00634-23, 2023, https://doi.org/10.1128/aem.00634-23 | Speculative genomic inference only; likely warning candidate rather than curated edge. |
| Bcd-Etf complex — may modulate — butyrate-linked electron flow and H2 formation | complex → pathway/process | candidate butyryl-CoA dehydrogenase/electron transfer flavoprotein complex | “an electron-bifurcating butyryl-CoA dehydrogenase complex (Bcd-Etf) ... may be involved in modulating the observed metabolic pathway changes” (kaminsky2023rumenlachnospiraceaeisolate pages 1-3) | 10.1128/aem.00634-23, 2023, https://doi.org/10.1128/aem.00634-23 | Speculative genomic inference; useful hypothesis node but weak edge for immediate curation. |
| deletion of lactate dehydrogenase (ldh) — increases — H2 yield | gene perturbation → outcome | candidate ldh gene; EC:1.1.1.27; METPO:traitmech:000109 | “ldh chromosomal deletion ... increased H2 yields from biomass by 63% and 25% versus wild type” (cha2024metabolicengineeringof pages 3-4) | 10.1007/s00253-023-12974-7, 2024, https://doi.org/10.1007/s00253-023-12974-7 | Engineering/perturbation edge rather than native causal graph edge; may belong in intervention annotations. |


*Table: This table compiles evidence-backed candidate subject-predicate-object edges for a TraitMech causal graph of fermentative hydrogen production. It emphasizes mechanistic enzymes, redox metabolites, environmental drivers, and product-shift outcomes, while flagging taxon-specific or weakly supported claims.*

---

### 5) Recent developments (2023–2024) and expert analysis

**(i) Quantitative, ecology-relevant regulation by H2 partial pressure (primary experimental evidence, 2023):**
AEM 2023 reports that isolate NK3A20 “modulates hydrogen production” in response to substrate and H2, with “Low ambient H2” stimulating H2 formation and “high H2” inhibiting it and shifting fermentation toward more reduced acids; coculture with a hydrogenotrophic methanogen lowered H2 and shifted products toward acetate and H2 (and away from butyrate). (kaminsky2023rumenlachnospiraceaeisolate pages 1-3, kaminsky2023rumenlachnospiraceaeisolate pages 7-10)

**(ii) Thermophile-focused engineering perspective (review, 2024):**
A 2024 review on *Caldicellulosiruptor bescii* highlights a bifurcating [Fe–Fe] hydrogenase that can oxidize NADH and reduced ferredoxin to produce H2, and describes how competing electron sinks (e.g., lactate formation) reduce H2, making ldh deletion an engineering target. (cha2024metabolicengineeringof pages 3-4)

**(iii) Mechanistic enzyme physics for electron bifurcation (structural study, 2023):**
HydABC cryo-EM/biochemistry provides a modern mechanistic account of how bifurcating hydrogenases gate electron flow between NAD(P)+ and ferredoxin branches via a single FMN and conformational gating, establishing molecular principles that can be reused in causal-graph nodes/edges for redox coupling. (katsyv2023molecularbasisof pages 2-3, katsyv2023molecularbasisof pages 8-9)

**(iv) Systems-level fermentation accounting and thermodynamic realism (review, 2024):**
A 2024 FEMS Microbiology Reviews synthesis treats H2 and formate as key electron carriers tied to reduced ferredoxin, and explicitly incorporates environmental H2 partial pressure into thermodynamic accounting, emphasizing that environmental conditions constrain which fermentative redox-balancing routes are feasible. (hackmann2024thevastlandscape pages 10-11)

**(v) Human gut fermentative H2 as a microbiome function (preprint, 2024; caution):**
A 2024 bioRxiv preprint claims group B [FeFe]-hydrogenases drive most fermentative H2 production in the gut and highlights confurcating group A3 hydrogenases as mechanistically capable of coupling NADH + ferredoxin oxidation to H2. As a preprint, it is best used for hypothesis generation unless peer-reviewed confirmation is available. (welsh2024awidespreadhydrogenase pages 8-10)

---

### 6) Current applications and real-world implementations

**Waste-to-H2 via dark fermentation:** Dark fermentation is emphasized as a promising biowaste valorization route. A 2023 Energies review discusses dark fermentation for H2 from biowaste and links yields to fermentation branches (acetate vs butyrate) via the Thauer limit framework. (talapko2023biologicalhydrogenproduction pages 4-6)

**Process integration and scale-up considerations:** A 2024 review highlights bioreactor choices and integration strategies to improve yield/productivity and emphasizes that dark fermentation is “efficient and cost-effective” among biohydrogen routes, with optimization across inoculum, physical-chemical parameters, and engineering/genetic interventions. (albuquerque2024biohydrogenproducedvia pages 1-2)

**Consolidated bioprocessing (CBP) using thermophiles:** The 2024 *C. bescii* review frames it as a CBP organism capable of decomposing and fermenting plant biomass without conventional pretreatment and reviews metabolic engineering targets to improve H2 production. (cha2024metabolicengineeringof pages 3-4)

---

### 7) Recent statistics and data points (for curation notes)

**Stoichiometric/theoretical constraints (Thauer-type limits):**
- Maximum theoretical yields in dark fermentation depend on end-products, often summarized as **4 mol H2/mol glucose** (acetate pathway) vs **2 mol H2/mol glucose** (butyrate pathway). (talapko2023biologicalhydrogenproduction pages 2-4, talapko2023biologicalhydrogenproduction pages 4-6)
- Practical mixed-product yields around **~1–2.5 mol H2/mol glucose** are reported in a 2024 review context. (taggar2024hydrogenproductionvia pages 5-7)

**Reported yields and productivity examples from recent reviews:**
- Reported strain yields in a 2024 review include (examples) **2.61 mol H2/mol glucose** (C. tyrobutyricum ATCC25755 WT), **3.20 mol H2/mol glucose** (C. tyrobutyricum DG-8 on cassava starch), and **3.01 mol H2/mol glucose** (C. acetobutylicum ATCC 824). (albuquerque2024biohydrogenproducedvia pages 1-2)
- A reported productivity example: **620 ± 60 mL H2·h−1·L−1** in batch SSF (96 h; 100 g/L initial sugar) in a 2024 review excerpt. (albuquerque2024biohydrogenproducedvia pages 1-2)

**Primary experimental quantification tied to H2 partial pressure manipulation (2023):**
- NK3A20 produced “up to **32 mmol/L H2**” on glucose; table-reported H2 amounts include **66.37 ± 7.16 µmol/tube** (25 µmol glucose) and **123.27 ± 6.03 µmol/tube** (50 µmol glucose). (kaminsky2023rumenlachnospiraceaeisolate pages 7-10)

---

### 8) Warnings / curation caveats (what not to curate yet)

1. **Speculative complex involvement (Ech/Rnf/Bcd–Etf):** In NK3A20, Ech, Rnf, and Bcd–Etf are suggested as systems that “may be involved” in modulating pathway changes; absent direct functional assays, these edges should be flagged **UNCERTAIN** or held until primary verification. (kaminsky2023rumenlachnospiraceaeisolate pages 1-3)
2. **HydABC directionality:** The 2023 HydABC structural study provides high-confidence mechanism for H2 oxidation coupled to NAD(P)+ and ferredoxin reduction; using it as direct evidence of **fermentative H2 production** requires additional organism-specific evidence of reverse-direction physiological function. (katsyv2023molecularbasisof pages 2-3)
3. **Preprint evidence:** The gut hydrogenase synthesis is a bioRxiv preprint; curate as **hypothesis-level** unless peer-reviewed publication becomes available. (welsh2024awidespreadhydrogenase pages 8-10)
4. **Non-authoritative/unknown-journal source:** One excerpted engineering review (Udegbe 2023) is indexed with “Unknown journal” metadata in this retrieval context; it contains useful mechanistic statements but should be supported by peer-reviewed primary sources before being used as sole evidence for irreversible edges. (udegbe2023metabolicengineeringof pages 36-40)

---

## DOI-first bibliography (with publication dates and URLs)

1. Hackmann TJ. *The vast landscape of carbohydrate fermentation in prokaryotes.* **FEMS Microbiology Reviews** (May 2024). DOI: **10.1093/femsre/fuae016**. https://doi.org/10.1093/femsre/fuae016 (hackmann2024thevastlandscape pages 10-11)
2. Taggar MS et al. *Hydrogen production via dark fermentation: a review of influential factors.* **Cellulose Chemistry and Technology** (Nov 2024). DOI: **10.35812/cellulosechemtechnol.2024.58.90**. https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 (taggar2024hydrogenproductionvia pages 5-7, taggar2024hydrogenproductionvia pages 7-8)
3. Albuquerque MM et al. *Biohydrogen produced via dark fermentation: a review.* **Methane** (Sep 2024). DOI: **10.3390/methane3030029**. https://doi.org/10.3390/methane3030029 (albuquerque2024biohydrogenproducedvia pages 1-2)
4. Cha M et al. *Metabolic engineering of Caldicellulosiruptor bescii for hydrogen production.* **Applied Microbiology and Biotechnology** (Jan 2024). DOI: **10.1007/s00253-023-12974-7**. https://doi.org/10.1007/s00253-023-12974-7 (cha2024metabolicengineeringof pages 3-4, cha2024metabolicengineeringof pages 7-8)
5. Kaminsky RA et al. *Rumen Lachnospiraceae isolate NK3A20 exhibits metabolic flexibility in response to substrate and coculture with a methanogen.* **Applied and Environmental Microbiology** (Oct 2023). DOI: **10.1128/aem.00634-23**. https://doi.org/10.1128/aem.00634-23 (kaminsky2023rumenlachnospiraceaeisolate pages 1-3, kaminsky2023rumenlachnospiraceaeisolate pages 7-10, kaminsky2023rumenlachnospiraceaeisolate pages 11-13, kaminsky2023rumenlachnospiraceaeisolate pages 10-11)
6. Talapko D et al. *Biological hydrogen production from biowaste using dark fermentation, storage and transportation.* **Energies** (Apr 2023). DOI: **10.3390/en16083321**. https://doi.org/10.3390/en16083321 (talapko2023biologicalhydrogenproduction pages 4-6, talapko2023biologicalhydrogenproduction pages 2-4)
7. Katsyv A et al. *Molecular basis of the electron bifurcation mechanism in the [FeFe]-hydrogenase complex HydABC.* **Journal of the American Chemical Society** (Feb 2023). DOI: **10.1021/jacs.2c11683**. https://doi.org/10.1021/jacs.2c11683 (katsyv2023molecularbasisof pages 2-3, katsyv2023molecularbasisof pages 8-9, katsyv2023molecularbasisof pages 7-8, katsyv2023molecularbasisof pages 1-2)

Preprint (use with caution):
8. Welsh C et al. *A widespread hydrogenase drives fermentative growth of gut bacteria in healthy people.* **bioRxiv** (Aug 2024). DOI: **10.1101/2024.08.15.608110**. https://doi.org/10.1101/2024.08.15.608110 (welsh2024awidespreadhydrogenase pages 8-10)


References

1. (taggar2024hydrogenproductionvia pages 5-7): Monica SACHDEVA TAGGAR, Amanpreet Kaur, Chahak Jain, Anu Kalia, and Sarbjit SINGH SOOCH. Hydrogen production via dark fermentation: a review of influential factors. Cellulose Chemistry and Technology, 58:1051-1063, Nov 2024. URL: https://doi.org/10.35812/cellulosechemtechnol.2024.58.90, doi:10.35812/cellulosechemtechnol.2024.58.90. This article has 11 citations and is from a peer-reviewed journal.

2. (taggar2024hydrogenproductionvia pages 7-8): Monica SACHDEVA TAGGAR, Amanpreet Kaur, Chahak Jain, Anu Kalia, and Sarbjit SINGH SOOCH. Hydrogen production via dark fermentation: a review of influential factors. Cellulose Chemistry and Technology, 58:1051-1063, Nov 2024. URL: https://doi.org/10.35812/cellulosechemtechnol.2024.58.90, doi:10.35812/cellulosechemtechnol.2024.58.90. This article has 11 citations and is from a peer-reviewed journal.

3. (cha2024metabolicengineeringof pages 3-4): Minseok Cha, Jung Kon Kim, Won-Heong Lee, Hyoungwoon Song, Tae-Gi Lee, Sun-Ki Kim, and Soo-Jung Kim. Metabolic engineering of caldicellulosiruptor bescii for hydrogen production. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12974-7, doi:10.1007/s00253-023-12974-7. This article has 9 citations and is from a domain leading peer-reviewed journal.

4. (katsyv2023molecularbasisof pages 2-3): Alexander Katsyv, Anuj Kumar, Patricia Saura, Maximilian C. Pöverlein, Sven A. Freibert, Sven T. Stripp, Surbhi Jain, Ana P. Gamiz-Hernandez, Ville R. I. Kaila, Volker Müller, and Jan M. Schuller. Molecular basis of the electron bifurcation mechanism in the [fefe]-hydrogenase complex hydabc. Journal of the American Chemical Society, 145:5696-5709, Feb 2023. URL: https://doi.org/10.1021/jacs.2c11683, doi:10.1021/jacs.2c11683. This article has 74 citations and is from a highest quality peer-reviewed journal.

5. (katsyv2023molecularbasisof pages 1-2): Alexander Katsyv, Anuj Kumar, Patricia Saura, Maximilian C. Pöverlein, Sven A. Freibert, Sven T. Stripp, Surbhi Jain, Ana P. Gamiz-Hernandez, Ville R. I. Kaila, Volker Müller, and Jan M. Schuller. Molecular basis of the electron bifurcation mechanism in the [fefe]-hydrogenase complex hydabc. Journal of the American Chemical Society, 145:5696-5709, Feb 2023. URL: https://doi.org/10.1021/jacs.2c11683, doi:10.1021/jacs.2c11683. This article has 74 citations and is from a highest quality peer-reviewed journal.

6. (kaminsky2023rumenlachnospiraceaeisolate pages 7-10): Rachel A. Kaminsky, Peter M. Reid, Eric Altermann, Nikki Kenters, William J. Kelly, Samantha J. Noel, Graeme T. Attwood, and Peter H. Janssen. Rumen <i>lachnospiraceae</i> isolate nk3a20 exhibits metabolic flexibility in response to substrate and coculture with a methanogen. Applied and Environmental Microbiology, Oct 2023. URL: https://doi.org/10.1128/aem.00634-23, doi:10.1128/aem.00634-23. This article has 38 citations and is from a peer-reviewed journal.

7. (udegbe2023metabolicengineeringof pages 36-40): FC Udegbe. Metabolic engineering of solventogenic clostridium species for improved hydrogen production. Unknown journal, 2023.

8. (talapko2023biologicalhydrogenproduction pages 4-6): Domagoj Talapko, Jasminka Talapko, Ivan Erić, and Ivana Škrlec. Biological hydrogen production from biowaste using dark fermentation, storage and transportation. Energies, 16:3321, Apr 2023. URL: https://doi.org/10.3390/en16083321, doi:10.3390/en16083321. This article has 50 citations.

9. (welsh2024awidespreadhydrogenase pages 8-10): Caitlin Welsh, Princess R. Cabotaje, Vanessa R. Marcelino, Thomas D. Watts, Duncan J. Kountz, Jodee A. Gould, Nhu Quynh Doan, James P. Lingford, Jessica Solari, Gemma L. D’Adamo, Ping Huang, Natasha Bong, Emily L. Gulliver, Remy B. Young, Kaija Walter, Patricia G. Wolf, Jason M. Ridlon, H. Rex Gaskins, Edward M. Giles, Dena Lyras, Rachael Lappan, Gustav Berggren, Samuel C. Forster, and Chris Greening. A widespread hydrogenase drives fermentative growth of gut bacteria in healthy people. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.15.608110, doi:10.1101/2024.08.15.608110. This article has 5 citations.

10. (hackmann2024thevastlandscape pages 10-11): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

11. (kaminsky2023rumenlachnospiraceaeisolate pages 1-3): Rachel A. Kaminsky, Peter M. Reid, Eric Altermann, Nikki Kenters, William J. Kelly, Samantha J. Noel, Graeme T. Attwood, and Peter H. Janssen. Rumen <i>lachnospiraceae</i> isolate nk3a20 exhibits metabolic flexibility in response to substrate and coculture with a methanogen. Applied and Environmental Microbiology, Oct 2023. URL: https://doi.org/10.1128/aem.00634-23, doi:10.1128/aem.00634-23. This article has 38 citations and is from a peer-reviewed journal.

12. (katsyv2023molecularbasisof pages 8-9): Alexander Katsyv, Anuj Kumar, Patricia Saura, Maximilian C. Pöverlein, Sven A. Freibert, Sven T. Stripp, Surbhi Jain, Ana P. Gamiz-Hernandez, Ville R. I. Kaila, Volker Müller, and Jan M. Schuller. Molecular basis of the electron bifurcation mechanism in the [fefe]-hydrogenase complex hydabc. Journal of the American Chemical Society, 145:5696-5709, Feb 2023. URL: https://doi.org/10.1021/jacs.2c11683, doi:10.1021/jacs.2c11683. This article has 74 citations and is from a highest quality peer-reviewed journal.

13. (kaminsky2023rumenlachnospiraceaeisolate pages 11-13): Rachel A. Kaminsky, Peter M. Reid, Eric Altermann, Nikki Kenters, William J. Kelly, Samantha J. Noel, Graeme T. Attwood, and Peter H. Janssen. Rumen <i>lachnospiraceae</i> isolate nk3a20 exhibits metabolic flexibility in response to substrate and coculture with a methanogen. Applied and Environmental Microbiology, Oct 2023. URL: https://doi.org/10.1128/aem.00634-23, doi:10.1128/aem.00634-23. This article has 38 citations and is from a peer-reviewed journal.

14. (talapko2023biologicalhydrogenproduction pages 2-4): Domagoj Talapko, Jasminka Talapko, Ivan Erić, and Ivana Škrlec. Biological hydrogen production from biowaste using dark fermentation, storage and transportation. Energies, 16:3321, Apr 2023. URL: https://doi.org/10.3390/en16083321, doi:10.3390/en16083321. This article has 50 citations.

15. (albuquerque2024biohydrogenproducedvia pages 1-2): Marcela Moreira Albuquerque, Gabriela de Bona Sartor, Walter Jose Martinez-Burgos, Thamarys Scapini, Thiago Edwiges, Carlos Ricardo Soccol, and Adriane Bianchi Pedroni Medeiros. Biohydrogen produced via dark fermentation: a review. Methane, 3:500-532, Sep 2024. URL: https://doi.org/10.3390/methane3030029, doi:10.3390/methane3030029. This article has 94 citations.

16. (cha2024metabolicengineeringof pages 7-8): Minseok Cha, Jung Kon Kim, Won-Heong Lee, Hyoungwoon Song, Tae-Gi Lee, Sun-Ki Kim, and Soo-Jung Kim. Metabolic engineering of caldicellulosiruptor bescii for hydrogen production. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12974-7, doi:10.1007/s00253-023-12974-7. This article has 9 citations and is from a domain leading peer-reviewed journal.

17. (kaminsky2023rumenlachnospiraceaeisolate pages 10-11): Rachel A. Kaminsky, Peter M. Reid, Eric Altermann, Nikki Kenters, William J. Kelly, Samantha J. Noel, Graeme T. Attwood, and Peter H. Janssen. Rumen <i>lachnospiraceae</i> isolate nk3a20 exhibits metabolic flexibility in response to substrate and coculture with a methanogen. Applied and Environmental Microbiology, Oct 2023. URL: https://doi.org/10.1128/aem.00634-23, doi:10.1128/aem.00634-23. This article has 38 citations and is from a peer-reviewed journal.

18. (katsyv2023molecularbasisof pages 7-8): Alexander Katsyv, Anuj Kumar, Patricia Saura, Maximilian C. Pöverlein, Sven A. Freibert, Sven T. Stripp, Surbhi Jain, Ana P. Gamiz-Hernandez, Ville R. I. Kaila, Volker Müller, and Jan M. Schuller. Molecular basis of the electron bifurcation mechanism in the [fefe]-hydrogenase complex hydabc. Journal of the American Chemical Society, 145:5696-5709, Feb 2023. URL: https://doi.org/10.1021/jacs.2c11683, doi:10.1021/jacs.2c11683. This article has 74 citations and is from a highest quality peer-reviewed journal.