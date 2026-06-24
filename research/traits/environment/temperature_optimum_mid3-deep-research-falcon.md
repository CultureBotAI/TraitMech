---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:08:23.160391'
end_time: '2026-06-18T02:16:58.005143'
duration_seconds: 514.84
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum mid3
  trait_identifier: METPO:1000445
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum_mid3
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature optimum phenotype with the best-growth ambient temperature\
    \ between approximately 30 and 34 \xB0C, characteristic of mesophilic physiology."
  parent_traits: METPO:1000304
  synonyms: Mesophilie, TO_30_to_34
  evidence_summary: "DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty\
    \ acids (Membrane-adaptation review supports the 30\u201334 \xB0C optimum as a\
    \ typical mesophile setpoint near common host body temperatures.)"
  causal_graph_summary: 'temperature_optimum_mid3_upper_mesophile: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum mid3
- **METPO identifier:** METPO:1000445
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 30 and 34 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_30_to_34
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 30–34 °C optimum as a typical mesophile setpoint near common host body temperatures.)
- **Existing causal graph summary:** temperature_optimum_mid3_upper_mesophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid3.yaml`.

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
- **Trait label:** temperature optimum mid3
- **METPO identifier:** METPO:1000445
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 30 and 34 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_30_to_34
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 30–34 °C optimum as a typical mesophile setpoint near common host body temperatures.)
- **Existing causal graph summary:** temperature_optimum_mid3_upper_mesophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid3.yaml`.

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


## Research report: Microbial trait **temperature optimum mid3** (METPO:1000445)

### 1) Scope summary (trait meaning, boundaries, and assay context)

**Trait definition (curation target).** *temperature optimum mid3* denotes a **growth temperature optimum (TOPT/Topt)** phenotype where an organism’s **best-growth ambient temperature is ~30–34 °C**, consistent with **upper-mesophilic physiology**. In microbial physiology, growth temperature phenotypes are commonly described using **cardinal temperatures** **TMIN, TOPT, TMAX** derived from growth–temperature curves (e.g., specific growth rate vs. temperature) (lehmann2023adaptivelaboratoryevolution pages 1-2).

**Boundary cases / distinction from adjacent classes.** Recent reviews and experimental work consistently place **mesophiles** in a broad band with **TOPT ~20–45 °C**, with **psychrophiles <~15 °C** and **thermophiles >~45 °C** (lehmann2023adaptivelaboratoryevolution pages 1-2, ramon2023ageneraloverview pages 1-2). Thus, **30–34 °C** is best interpreted as a *narrow* curated subclass inside the mesophile range, and should be distinguished from:
- **Lower mesophile / psychrotolerant** organisms that can grow at ~4 °C but have optima >20 °C (ramon2023ageneraloverview pages 1-2).
- **Canonical lab mesophiles with TOPT ~37 °C** (e.g., E. coli cited as optimal at 37 °C) (moon2023temperaturemattersbacterial pages 1-3).

**Assay considerations for curation.** The trait should ideally be supported by **growth rate measurements across temperatures** (not just “survival” or “shock response”), because stress-response activation can occur outside TOPT and does not itself define an optimum (moon2023temperaturemattersbacterial pages 3-5, liang2023developmentofheatshock pages 1-2). For TraitMech curation, mechanistic edges should therefore be framed as *contributors to maintaining growth performance in the upper-mesophile window* (including 30–34 °C), rather than as unique determinants of that narrow interval.

### 2) Key mechanistic concepts (current understanding)

#### 2.1 Homeoviscous adaptation (membrane physical state as a temperature mediator)
Temperature changes alter membrane phase behavior (gel vs liquid-crystalline), affecting thickness and fluidity; organisms remodel membrane composition to restore a functional liquid-crystalline state (“**homeoviscous adaptation**”) (ramon2023ageneraloverview pages 2-4). Molecular levers include:
- **Increasing unsaturation** (often **cis** monounsaturated fatty acids) (ramon2023ageneraloverview pages 2-4).
- **Adjusting branched-chain fatty acids (BCFAs)** and iso/anteiso ratios (sidarta2024lipidphaseseparation pages 12-14, hellequin2023membranelipidadaptation pages 1-2).
- **Switch-like regulatory systems** that sense membrane state and induce lipid remodeling (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 2-5).

#### 2.2 Mesophile fatty-acid pathways and regulators (E. coli model)
A recent cold-adaptation review details E. coli’s key membrane fatty acids—**palmitic (16:0), cis-palmitoleic (16:1Δ9), and cis-vaccenic (18:1Δ11)**—and notes that **cis-vaccenic acid rapidly increases when temperature drops** (ramon2023ageneraloverview pages 2-4). The same source provides a mechanistic control point in E. coli where:
- **FabA** introduces cis double bonds and **FabB** elongates intermediates in UFA biosynthesis.
- **FabR** represses *fabA/fabB* more strongly when bound to UFAs, implementing feedback control over UFA/SFA balance.
These provide candidate mechanistic nodes connecting temperature → membrane composition → growth performance (ramon2023ageneraloverview pages 2-4).

#### 2.3 Membrane-state sensing and desaturase induction (Bacillus subtilis DesK/DesR/Des)
A 2024 Microbiology Spectrum study revisits the canonical **DesK/DesR–Des** system in *B. subtilis*, where DesK senses membrane-thickness changes and induces the lipid desaturase Des (sidarta2024lipidphaseseparation pages 1-2). A key detail for *upper mesophile* temperature ranges is that **a mild shift 37 °C→25 °C** activated the *des* promoter in vivo, while harsher shifts showed complex behavior likely influenced by membrane phase separation (sidarta2024lipidphaseseparation pages 2-5, sidarta2024lipidphaseseparation pages 12-14). This supports a curated concept that some membrane-sensing systems operate on **subtle fluidity/thickness changes** near mesophilic temperatures, not only at extremes (sidarta2024lipidphaseseparation pages 12-14).

#### 2.4 Proteostasis, sigma factors, and chaperone networks near the upper-mesophile band
A 2023 review on bacterial temperature response describes how heat-induced unfolded proteins trigger sigma-factor and chaperone circuits (RpoH/σ32; DnaK/DnaJ; GroEL/GroES; ClpB; HtpG), with explicit temperature-relevant constraints: **DnaK is essential for E. coli above ~30 °C** (moon2023temperaturemattersbacterial pages 5-6). This provides a mechanistic rationale that sustaining growth in the **30–34 °C** optimum class can depend on proteostasis capacity even under “mild” heat relative to colder growth.

### 3) Recent developments (prioritizing 2023–2024)

**(i) Subtle membrane sensing at mesophilic temperatures.** Sidarta et al. (Jun 2024) report that *B. subtilis* DesK detects thickness changes upon 37→25 °C shift and that promoter activation kinetics can be slow; they propose that **phase separation and partitioning of DesK into fluid domains** can impair sensing under harsher cold shock (sidarta2024lipidphaseseparation pages 12-14). This refines older “simple” models of DesK activation by showing strong dependence on membrane mesoscale organization.

**(ii) Lipidomic evidence of homeoviscous adaptation across clinical strains.** Dessenne et al. (Oct 2024) show strain-dependent lipid remodeling in **Acinetobacter baumannii** at **18 °C vs 37 °C**, including consistent increases in **palmitoleic acid (C16:1)** for most strains at 18 °C and identification of candidate desaturase genes; they also highlight that some strains carry **FabA**, despite it being “typically absent” in A. baumannii (dessenne2024lipidomicanalysesreveal pages 1-2). This supports curation of “temperature → unsaturation remodeling” edges while warning that genetic bases vary among strains.

**(iii) Coupling between membrane fluidity and stringent response / division control.** Singh & Harinarayanan (2024) report that when UFA synthesis is reduced (ΔfadR), **growth at lower temperatures becomes dependent on (p)ppGpp**, and that restoring UFA synthesis (via gnsA or fabA/fabB expression) rescues growth at **25–30 °C** under (p)ppGpp limitation (singh2024(p)ppgppbufferscell pages 4-8). This supports a mechanistic bridge from membrane lipid state to global growth-control networks.

### 4) Current applications and real-world implementations

**Bioprocess design and microbial cultivation.** Many industrial and lab processes are optimized for mesophilic growth windows (often around 30–37 °C). The mechanistic nodes summarized here are directly relevant to:
- **Strain robustness** under temperature fluctuations (e.g., fermentation scale-up, where gradients occur). Membrane remodeling and proteostasis circuits are repeatedly implicated as key adaptation layers (sidarta2024lipidphaseseparation pages 1-2, moon2023temperaturemattersbacterial pages 5-6).
- **Controlling pathogenic bacteria in built environments.** Heat stress is used as a control measure (e.g., hot water systems). Experimental evolution shows bacteria such as *Legionella pneumophila* can evolve increased heat-shock survival via mutations in chaperone/protease systems, raising implementation concerns for thermal disinfection strategies (liang2023developmentofheatshock pages 1-2).

### 5) Relevant statistics and quantitative data points (from recent sources)

- **Mesophile TOPT band:** mesophiles described as **TOPT ~20–45 °C** (lehmann2023adaptivelaboratoryevolution pages 1-2, ramon2023ageneraloverview pages 1-2).
- **Proteostasis threshold:** **DnaK essential above ~30 °C in E. coli** (moon2023temperaturemattersbacterial pages 5-6).
- **Membrane composition dominance (B. subtilis):** **80–96% branched-chain fatty acids**; LB-grown cells reported **~5–6% straight-chain fatty acids** and **unsaturated:saturated ratio ~0.075** (sidarta2024lipidphaseseparation pages 12-14).
- **Cold-shock induction threshold:** cold-shock proteins induced at high levels during shifts **below 20 °C** (purwar2024adaptationsofpsychrophilic pages 7-8).
- **Regulatory response magnitude:** transcriptomics cited in Sidarta et al. indicates **1.7-fold induction of des after 60 min at 18 °C** (shifted from 37 °C) in a prior profiling study (sidarta2024lipidphaseseparation pages 12-14).

---

## Candidate causal-graph nodes (grouped by type)

### A. Phenotype / environment / assay nodes
- **Growth temperature optimum (TOPT/Topt)** (phenotype; cardinal temperatures include TMIN/TMAX/TOPT) (lehmann2023adaptivelaboratoryevolution pages 1-2)
- **Ambient temperature** (ENVO:01000342 “temperature” is plausible; if ENVO not used, label-only “environmental temperature”)
- **Cold shock** (label-only; operationally: rapid temperature downshift)
- **Heat shock / mild heat stress** (label-only)
- **Membrane fluidity**, **membrane thickness**, **phase separation** (label-only biophysical nodes) (sidarta2024lipidphaseseparation pages 12-14)

### B. Biological processes (GO candidates)
- **Homeoviscous adaptation** (process node; label-only or map to “membrane lipid metabolic process” GO:0006643 as broader proxy) (ramon2023ageneraloverview pages 2-4)
- **Fatty acid desaturation** (GO:0044550)
- **Response to cold** (GO:0009409), **response to heat** (GO:0009408)
- **Protein folding** (GO:0006457), **protein refolding** (GO:0042026)
- **Stringent response** (GO:0009260)

### C. Genes / proteins / complexes
**Membrane lipid regulation / enzymes**
- *E. coli* UFA pathway: **FabA**, **FabB**, **FabR**, **FadR** (ramon2023ageneraloverview pages 2-4, singh2024(p)ppgppbufferscell pages 4-8)
- *B. subtilis* cold fluidity module: **DesK (sensor histidine kinase)**, **DesR (response regulator)**, **Des (Δ5 acyl-lipid desaturase)** (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 2-5)

**Proteostasis / heat-shock machinery**
- **DnaK/DnaJ** (Hsp70 system), **GroEL/GroES** (chaperonin), **ClpB**, **HtpG** (bacterial Hsp90 homolog) (moon2023temperaturemattersbacterial pages 5-6, moon2023temperaturemattersbacterial pages 3-5)
- **RpoH (σ32)**, **RpoE (σ24)**, **RpoS (σS)** (moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 5-6)

### D. Chemicals / metabolites (CHEBI candidates)
- **Palmitic acid** (16:0), **cis-palmitoleic acid** (16:1), **cis-vaccenic acid** (18:1) (CHEBI terms exist; candidate grounding required) (ramon2023ageneraloverview pages 2-4)
- **(p)ppGpp** (alarmone; CHEBI term exists) (singh2024(p)ppgppbufferscell pages 4-8)
- **Trehalose** (compatible solute linked to low-temperature survival via RpoS regulons) (moon2023temperaturemattersbacterial pages 5-6)

---

## Candidate causal edges (evidence-backed triples)

The following artifact provides curation-ready and cautionary edges derived strictly from the evidence gathered.

| Edge (triple) | Mechanism/interpretation | Evidence snippet (verbatim short quote) | Source (DOI, year, URL) | Confidence/curation note |
|---|---|---|---|---|
| temperature_optimum_mid3 (METPO:1000445) — subclass_of → mesophile temperature range (~20–45 °C) | Places the trait within the mesophilic thermal class; supports boundary against psychrophiles and thermophiles rather than a unique mechanism for 30–34 °C | “mesophiles are described as having TOPT roughly 20–45°C” (lehmann2023adaptivelaboratoryevolution pages 1-2) | 10.3389/fmicb.2023.1265216, 2023, https://doi.org/10.3389/fmicb.2023.1265216 | **High for scope**, not a mechanistic edge; use for ontology/scope only. |
| decreased temperature — rigidifies/thickens → membrane bilayer | Core homeoviscous trigger: cooler conditions shift membrane physical state, creating need for fluidity-restoring responses that help maintain mesophilic growth near lower suboptimal temperatures | “upon temperature decrease the membrane rigidifies and thickens” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | **High** mechanistic support; general temperature-adaptation edge, not specific to 30–34 °C. |
| membrane rigidification/thickening — activates → DesK sensor kinase | In Bacillus subtilis, DesK senses subtle cold-induced membrane changes and initiates a compensatory response | “activating DesK kinase activity” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | **High**, but **taxon-specific** (B. subtilis model). |
| DesK — phosphorylates/activates → DesR | Two-component signaling step linking membrane-state sensing to transcriptional control of desaturase expression | “phosphorylation of DesR” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | **High**, **taxon-specific**. |
| DesR — induces transcription of → des | DesR turns on the desaturase gene as part of the emergency fluidization response | “induction of des transcription” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | **High**, **taxon-specific**. |
| Des (acyl-lipid Δ5 desaturase) — increases_unsaturation_of → membrane fatty acids | Desaturation of existing lipids is a rapid homeoviscous mechanism to restore fluidity after cooling | “resulting desaturation that fluidizes and thins the bilayer” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | **High**, **taxon-specific**; relevant as a candidate mechanism for maintaining growth in upper-mesophile range under downward shifts. |
| 37→25 °C temperature downshift — activates → des promoter | Experimental evidence that a mild shift spanning the upper-mesophile region is sufficient to trigger membrane-thickness sensing in Bacillus | “des promoter activation was observed after a 2-hour shift from 37°C to 25°C” (sidarta2024lipidphaseseparation pages 2-5) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | **High** for assay-specific response; useful because 25 °C is adjacent to the target class, but not direct Topt evidence for 30–34 °C. |
| homeoviscous adaptation — restores → liquid-crystalline membrane state | General process-level node capturing why lipid remodeling supports growth over mesophilic temperatures | “These changes are often referred to as “homeoviscous adaptation”” (ramon2023ageneraloverview pages 2-4) | 10.1007/s42770-023-01057-4, 2023, https://doi.org/10.1007/s42770-023-01057-4 | **High** concept support; broad process edge. |
| monounsaturated fatty acid incorporation — increases → membrane fluidity at lower temperature | Candidate process for maintaining growth near lower mesophilic temperatures by preventing rigidification | “The most common adaptation is the incorporation of monounsaturated fatty acids (MUFA), preferably cis-unsaturated ones” (ramon2023ageneraloverview pages 2-4) | 10.1007/s42770-023-01057-4, 2023, https://doi.org/10.1007/s42770-023-01057-4 | **Moderate**; mechanism is well-supported, but causal link to exact 30–34 °C optimum is indirect. |
| FabA — contributes_to_biosynthesis_of → cis-unsaturated fatty acids | E. coli UFA biosynthesis step that can tune membrane composition and therefore growth across mesophilic temperatures | “FabA introduces cis double bonds” (ramon2023ageneraloverview pages 2-4) | 10.1007/s42770-023-01057-4, 2023, https://doi.org/10.1007/s42770-023-01057-4 | **Moderate**; biochemical role strong, but exact effect on 30–34 °C Topt is inferred. |
| FabB — elongates product of → FabA pathway | Supports production of UFAs used in fluidity control | “FabB elongates the product” (ramon2023ageneraloverview pages 2-4) | 10.1007/s42770-023-01057-4, 2023, https://doi.org/10.1007/s42770-023-01057-4 | **Moderate**; curate as pathway support, not as sole determinant of Topt. |
| FabR bound to UFAs — represses → fabA/fabB expression | Feedback control of UFA biosynthesis in E. coli; plausible determinant of membrane-state setpoint in mesophiles | “binding to UFAs increases repression at fabA/fabB promoters” (ramon2023ageneraloverview pages 2-4) | 10.1007/s42770-023-01057-4, 2023, https://doi.org/10.1007/s42770-023-01057-4 | **Moderate**, **regulatory inference** toward Topt. |
| temperature drop — increases → cis-vaccenic acid (18:1 Δ11) content in E. coli membrane | Specific lipid change associated with cold-side compensation in a mesophile | “When the temperature drops, only cis-vaccenic acid content increases” (ramon2023ageneraloverview pages 2-4) | 10.1007/s42770-023-01057-4, 2023, https://doi.org/10.1007/s42770-023-01057-4 | **High** for species-specific lipid response; indirect for defining upper-mesophile Topt. |
| FadR loss — decreases → unsaturated fatty acid proportion | Demonstrates that E. coli membrane UFA regulation is causal for growth at cooler mesophilic temperatures | “loss (∆fadR) reduces the proportion of unsaturated fatty acids and increases saturated fatty acids” (singh2024(p)ppgppbufferscell pages 4-8) | 10.1111/mmi.15323, 2024, https://doi.org/10.1111/mmi.15323 | **High** in E. coli; may be useful as causal-graph edge for UFA homeostasis. |
| reduced UFA proportion / low membrane fluidity — increases requirement for → (p)ppGpp | Links membrane state to growth-control circuitry; (p)ppGpp buffers division when fluidity is low | “∆fadR required (p)ppGpp more at lower temperatures” (singh2024(p)ppgppbufferscell pages 4-8) | 10.1111/mmi.15323, 2024, https://doi.org/10.1111/mmi.15323 | **High** for E. coli growth phenotype; still indirect for setting Topt 30–34 °C. |
| (p)ppGpp — buffers → cell division under low membrane fluidity | Suggests growth in cooler mesophilic windows depends not only on lipids but on division-control buffering | “Buffers Cell Division When Membrane Fluidity Decreases in Escherichia coli” (singh2024(p)ppgppbufferscell pages 4-8) | 10.1111/mmi.15323, 2024, https://doi.org/10.1111/mmi.15323 | **Moderate-High**; title-level plus summarized evidence, species-specific. |
| gnsA overexpression — restores → 16:1/18:1 proportions toward wild type | Functional rescue linking UFA composition to improved growth under low-fluidity conditions | “restored 16:1 and 18:1 proportions to wild-type and lowered 16:0” (singh2024(p)ppgppbufferscell pages 4-8) | 10.1111/mmi.15323, 2024, https://doi.org/10.1111/mmi.15323 | **Moderate**, probably too strain/assay-specific for broad TraitMech unless represented as E. coli-specific evidence. |
| fabA/fabB expression — increases → palmitoleic acid (16:1) and cis-vaccenic acid (18:1) | Direct genetic manipulation showing candidate lipid effectors for mesophilic membrane fluidity | “primarily increased 16:1 (palmitoleic) and to a smaller extent 18:1” (singh2024(p)ppgppbufferscell pages 4-8) | 10.1111/mmi.15323, 2024, https://doi.org/10.1111/mmi.15323 | **High** for manipulated E. coli system; indirect for exact Topt class. |
| lower temperature — increases anteiso/(iso or normal) 3-OH FA ratio | Supports branched-chain/branched-hydroxy FA remodeling as a temperature-adaptation mechanism | “significant increase in the ratio of anteiso vs. iso or normal 3-OH FAs at lower temperature” (hellequin2023membranelipidadaptation pages 1-2) | 10.3389/fmicb.2023.1032032, 2023, https://doi.org/10.3389/fmicb.2023.1032032 | **Moderate**, **taxon-specific** (soil Bacteroidetes) and not directly tied to 30–34 °C optimum. |
| increased anteiso-BCFA proportion — fluidizes → bacterial membrane | Anteiso chains are more fluidizing than iso chains, offering a plausible mechanism for mesophilic temperature compensation | “Anteiso-BCFAs are noted to be more fluidizing than iso-BCFAs” (wu2023molecularmechanismsof pages 3-5) | 10.3390/cells12101353, 2023, https://doi.org/10.3390/cells12101353 | **Moderate**, mostly review-level synthesis; acceptable as a candidate process edge with uncertainty flag. |
| temperature downshift below 20 °C — induces → cold-shock proteins (CSPs) | Marks a boundary case below the target class; helps distinguish mid3 optimum from colder-adapted states | “CSPs are ‘induced at high levels during temperature shifts below 20 °C’” (purwar2024adaptationsofpsychrophilic pages 7-8) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | **High** for threshold behavior, but **boundary/response edge**, not determinant of 30–34 °C Topt. |
| cold shock — induces high synthesis of → CspA | Molecular indicator of suboptimal low-temperature response in mesophiles | “massive induction of CspA (~15% of protein synthesis after cold shock)” (moon2023temperaturemattersbacterial pages 3-5) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | **High** for cold-stress response; should be marked **uncertain for Topt curation**. |
| low temperature — activates/stabilizes → RpoS | General stress sigma factor contributes to mesophile cold adaptation via low-temperature regulons | “RpoS is induced and active at low temperature” (moon2023temperaturemattersbacterial pages 3-5) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | **Moderate**; stress-response relevance is clear, but direct role in setting optimum is indirect. |
| heat/unfolded proteins — release/activate → RpoH (σ32) | Heat-shock transcriptional activation supports proteostasis near upper temperature limits of mesophiles | “unfolded-protein accumulation causes dissociation of RpoH from DnaK” (moon2023temperaturemattersbacterial pages 5-6, moon2023temperaturemattersbacterial pages 3-5) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | **High** for heat-shock mechanism; **uncertain for exact mid3 Topt** because it describes stress above optimum as well. |
| RpoH — induces → heat-shock genes/chaperones | Connects thermal stress sensing to proteostasis machinery needed for viability in mesophiles | “RpoH drives rapid induction of heat-shock genes” (moon2023temperaturemattersbacterial pages 3-5) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | **High**, but broader than temperature_optimum_mid3. |
| unfolded periplasmic proteins — activates → RpoE | Envelope heat-stress arm that can matter as temperatures rise above preferred mesophilic growth | “RpoE is activated by unfolded periplasmic proteins via RseA cleavage” (moon2023temperaturemattersbacterial pages 3-5) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | **Moderate-High**; mechanism strong, but edge is stress-specific. |
| DnaK/DnaJ/GroEL/GroES/ClpB/HtpG — maintain → proteostasis during temperature shifts | Chaperone network prevents/refolds aggregates and supports viability across mesophilic temperature variation | “DnaK-DnaJ, GroEL-GroES, HtpG, ClpB” and “prevent/resolve aggregates” (moon2023temperaturemattersbacterial pages 5-6, moon2023temperaturemattersbacterial pages 3-5) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | **High** as a general proteostasis module; not uniquely defining 30–34 °C optimum. |
| DnaK — required_for_viability_above → ~30 °C in E. coli | Strong threshold-like evidence relevant to the upper-mesophile band, indicating chaperone dependence even before overt heat stress | “an essential requirement for DnaK above ~30 °C” (moon2023temperaturemattersbacterial pages 5-6) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | **High** and especially relevant to temperature_optimum_mid3; still species-specific (E. coli). |
| psychrophilic GroEL/GroES expression — facilitates growth of → E. coli at 4 °C | Demonstrates chaperone causality for extending growth outside normal mesophilic optimum | “facilitates E. coli growth at 4 °C” (purwar2024adaptationsofpsychrophilic pages 7-8) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | **Moderate**, useful as supporting boundary evidence only; not direct for mid3 curation. |
| constitutively elevated heat-shock gene expression / mutations in DnaJ-DnaK-ClpB-HtpG/ClpX — increases survival after → 55–59 °C heat shock | Shows proteostasis systems causally raise thermal resistance above mesophilic optima | “became insensitive to 55°C and could survive short 59°C heat shocks” (liang2023developmentofheatshock pages 1-2) | 10.1128/aem.00666-23, 2023, https://doi.org/10.1128/aem.00666-23 | **Moderate**, important for upper-bound context but too far above 30–34 °C to curate as direct determinant of mid3. |


*Table: This table lists curation-ready and cautionary candidate subject–predicate–object edges for the microbial trait temperature optimum mid3, restricted to claims supported by the provided evidence contexts. It is useful for selecting mechanistic nodes and filtering out edges that are only stress-response or taxon-specific rather than direct determinants of a 30–34 °C optimum.*

---

## Expert interpretation and curation guidance (what is strong vs. weak for TraitMech)

### Edges likely strong enough to curate (with taxon/context qualifiers)
1. **Temperature → membrane physical state → desaturase/FA remodeling** is consistently supported and mechanistically explicit (homeoviscous adaptation; DesK/DesR/Des; E. coli UFA regulation) (sidarta2024lipidphaseseparation pages 1-2, ramon2023ageneraloverview pages 2-4, sidarta2024lipidphaseseparation pages 12-14).
2. **Upper-mesophile temperatures can require active proteostasis**: the explicit statement that **DnaK becomes essential above ~30 °C** makes proteostasis a plausible direct contributor within the 30–34 °C optimum class (moon2023temperaturemattersbacterial pages 5-6).

### Edges that should be flagged as *uncertain* for “temperature optimum mid3” (even if true generally)
- **Cold shock protein induction** (e.g., below 20 °C) is important for boundary cases but is not direct evidence for a **30–34 °C optimum** (purwar2024adaptationsofpsychrophilic pages 7-8, moon2023temperaturemattersbacterial pages 3-5).
- **Extreme heat survival (55–59 °C)** mechanisms are valuable for understanding upper bounds and real-world control but are too far from the mid3 optimum window to be directly curated as determining TOPT mid3 (liang2023developmentofheatshock pages 1-2).
- Several membrane adaptations (e.g., phase separation effects; strain-to-strain lipidomic variation) indicate mechanistic heterogeneity; these should be curated with organismal context or captured as “possible mechanisms” rather than universal edges (sidarta2024lipidphaseseparation pages 12-14, dessenne2024lipidomicanalysesreveal pages 1-2).

---

## DOI-first bibliography (publication dates and URLs)

1. **Sidarta M, et al.** *Lipid phase separation impairs membrane thickness sensing by the Bacillus subtilis sensor kinase DesK.* **Microbiology Spectrum**. **Jun 2024**. DOI: **10.1128/spectrum.03925-23**. https://doi.org/10.1128/spectrum.03925-23 (sidarta2024lipidphaseseparation pages 12-14, sidarta2024lipidphaseseparation pages 2-5, sidarta2024lipidphaseseparation pages 1-2)
2. **Singh V, Harinarayanan R.** *(p)ppGpp Buffers Cell Division When Membrane Fluidity Decreases in Escherichia coli.* **Molecular Microbiology**. **Oct 2024**. DOI: **10.1111/mmi.15323**. https://doi.org/10.1111/mmi.15323 (singh2024(p)ppgppbufferscell pages 4-8)
3. **Dessenne C, et al.** *Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of Acinetobacter baumannii.* **Microbiology Spectrum**. **Oct 2024**. DOI: **10.1128/spectrum.00757-24**. https://doi.org/10.1128/spectrum.00757-24 (dessenne2024lipidomicanalysesreveal pages 1-2)
4. **Moon S, et al.** *Temperature Matters: Bacterial Response to Temperature Change.* **Journal of Microbiology**. **Mar 2023**. DOI: **10.1007/s12275-023-00031-x**. https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 5-6, moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 1-3)
5. **Ramón A, et al.** *A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.* **Brazilian Journal of Microbiology**. **Jul 2023**. DOI: **10.1007/s42770-023-01057-4**. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 2-4, ramon2023ageneraloverview pages 1-2)
6. **Lehmann M, et al.** *Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.* **Frontiers in Microbiology**. **Oct 2023**. DOI: **10.3389/fmicb.2023.1265216**. https://doi.org/10.3389/fmicb.2023.1265216 (lehmann2023adaptivelaboratoryevolution pages 1-2)
7. **Liang J, et al.** *Development of heat-shock resistance in Legionella pneumophila modeled by experimental evolution.* **Applied and Environmental Microbiology**. **Sep 2023**. DOI: **10.1128/aem.00666-23**. https://doi.org/10.1128/aem.00666-23 (liang2023developmentofheatshock pages 1-2)
8. **Hellequin E, et al.** *Membrane lipid adaptation of soil Bacteroidetes isolates to temperature and pH.* **Frontiers in Microbiology**. **Mar 2023**. DOI: **10.3389/fmicb.2023.1032032**. https://doi.org/10.3389/fmicb.2023.1032032 (hellequin2023membranelipidadaptation pages 1-2)
9. **Purwar S, Srivastava S.** *Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.* **Applied Microbiology: Theory & Technology**. **Oct 2024**. DOI: **10.37256/amtt.5220244537**. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 7-8)

---

## Warnings (claims not ready for direct TraitMech curation)

1. **“Determines TOPT 30–34 °C” vs. “enables growth under shifts.”** Much of the strongest mechanistic evidence is framed as **cold/heat adaptation** (homeoviscous, chaperones) rather than explicitly shifting TOPT into a 30–34 °C optimum. These mechanisms should be curated as **contributors/modulators of growth performance** in the mesophile window unless a primary study directly links them to measured TOPT shifts.
2. **Taxon specificity.** DesK/DesR/Des is a **Bacillus model**; FabA/FabB/FabR/FadR is **E. coli-centered**. These are excellent mechanistic exemplars but should not be asserted as universal across all microbes with mid3 TOPT without qualifier nodes (e.g., NCBITaxon constraints) (ramon2023ageneraloverview pages 2-4, sidarta2024lipidphaseseparation pages 12-14).
3. **Strain-level heterogeneity.** Clinical-strain lipidomes can vary substantially; do not over-generalize single-strain lipidomic observations into universal edges without additional corroboration (dessenne2024lipidomicanalysesreveal pages 1-2).


References

1. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

2. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

3. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

4. (moon2023temperaturemattersbacterial pages 3-5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

5. (liang2023developmentofheatshock pages 1-2): Jeffrey Liang, Gillian Cameron, and Sébastien P. Faucher. Development of heat-shock resistance in <i>legionella pneumophila</i> modeled by experimental evolution. Sep 2023. URL: https://doi.org/10.1128/aem.00666-23, doi:10.1128/aem.00666-23. This article has 19 citations and is from a peer-reviewed journal.

6. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

7. (sidarta2024lipidphaseseparation pages 12-14): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

8. (hellequin2023membranelipidadaptation pages 1-2): Eve Hellequin, Sylvie Collin, Marina Seder-Colomina, Pierre Véquaud, Christelle Anquetil, Adrienne Kish, and Arnaud Huguet. Membrane lipid adaptation of soil bacteroidetes isolates to temperature and ph. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1032032, doi:10.3389/fmicb.2023.1032032. This article has 13 citations and is from a peer-reviewed journal.

9. (sidarta2024lipidphaseseparation pages 1-2): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

10. (sidarta2024lipidphaseseparation pages 2-5): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

11. (moon2023temperaturemattersbacterial pages 5-6): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

12. (dessenne2024lipidomicanalysesreveal pages 1-2): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

13. (singh2024(p)ppgppbufferscell pages 4-8): Vani Singh and Rajendran Harinarayanan. (p)<scp>ppgpp</scp> buffers cell division when membrane fluidity decreases in <i>escherichia coli</i>. Molecular Microbiology, 122:847-865, Oct 2024. URL: https://doi.org/10.1111/mmi.15323, doi:10.1111/mmi.15323. This article has 5 citations and is from a domain leading peer-reviewed journal.

14. (purwar2024adaptationsofpsychrophilic pages 7-8): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

15. (wu2023molecularmechanismsof pages 3-5): Gang Wu, Ralf Baumeister, and Thomas Heimbucher. Molecular mechanisms of lipid-based metabolic adaptation strategies in response to cold. Cells, 12:1353, May 2023. URL: https://doi.org/10.3390/cells12101353, doi:10.3390/cells12101353. This article has 87 citations.