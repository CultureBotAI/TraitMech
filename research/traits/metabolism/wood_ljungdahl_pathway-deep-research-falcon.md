---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:07:40.182075'
end_time: '2026-06-18T06:21:31.583675'
duration_seconds: 831.4
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Wood-Ljungdahl pathway
  trait_identifier: traitmech:000022
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: wood_ljungdahl_pathway
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An autotrophic carbon-fixation pathway (the reductive acetyl-CoA pathway)
    in which two molecules of CO2 are reduced and combined into acetyl-CoA. It is
    energetically efficient and used by acetogenic bacteria, methanogenic archaea,
    and some sulfate-reducing bacteria.
  parent_traits: traitmech:000019
  synonyms: reductive acetyl-CoA pathway
  evidence_summary: 'DOI:10.1016/j.bbapap.2008.08.012:  (Ragsdale & Pierce, "Acetogenesis
    and the Wood-Ljungdahl pathway of CO2 fixation", is the reference treatment of
    this reductive acetyl-CoA pathway.) | DOI:10.1128/AEM.02473-10:  (Berg review
    places the reductive acetyl-CoA (Wood-Ljungdahl) pathway among the recognized
    autotrophic carbon-fixation pathways.)'
  causal_graph_summary: 'wood_ljungdahl_reductive_acetyl_coa: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Wood-Ljungdahl pathway
- **METPO identifier:** traitmech:000022
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (the reductive acetyl-CoA pathway) in which two molecules of CO2 are reduced and combined into acetyl-CoA. It is energetically efficient and used by acetogenic bacteria, methanogenic archaea, and some sulfate-reducing bacteria.
- **Parent traits:** traitmech:000019
- **Synonyms:** reductive acetyl-CoA pathway
- **Existing evidence:** DOI:10.1016/j.bbapap.2008.08.012:  (Ragsdale & Pierce, "Acetogenesis and the Wood-Ljungdahl pathway of CO2 fixation", is the reference treatment of this reductive acetyl-CoA pathway.) | DOI:10.1128/AEM.02473-10:  (Berg review places the reductive acetyl-CoA (Wood-Ljungdahl) pathway among the recognized autotrophic carbon-fixation pathways.)
- **Existing causal graph summary:** wood_ljungdahl_reductive_acetyl_coa: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **Wood-Ljungdahl pathway** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/wood_ljungdahl_pathway.yaml`.

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
- **Trait label:** Wood-Ljungdahl pathway
- **METPO identifier:** traitmech:000022
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (the reductive acetyl-CoA pathway) in which two molecules of CO2 are reduced and combined into acetyl-CoA. It is energetically efficient and used by acetogenic bacteria, methanogenic archaea, and some sulfate-reducing bacteria.
- **Parent traits:** traitmech:000019
- **Synonyms:** reductive acetyl-CoA pathway
- **Existing evidence:** DOI:10.1016/j.bbapap.2008.08.012:  (Ragsdale & Pierce, "Acetogenesis and the Wood-Ljungdahl pathway of CO2 fixation", is the reference treatment of this reductive acetyl-CoA pathway.) | DOI:10.1128/AEM.02473-10:  (Berg review places the reductive acetyl-CoA (Wood-Ljungdahl) pathway among the recognized autotrophic carbon-fixation pathways.)
- **Existing causal graph summary:** wood_ljungdahl_reductive_acetyl_coa: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **Wood-Ljungdahl pathway** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/wood_ljungdahl_pathway.yaml`.

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


## Microbial Trait Causal Graph Research Report: Wood–Ljungdahl pathway (reductive acetyl-CoA pathway)

**Target trait:** Wood–Ljungdahl pathway (WLP) / reductive acetyl‑CoA pathway (METPO:traitmech:000022)

### 1) Scope summary (trait meaning, readouts, and boundary cases)

**Trait meaning (curation scope).** The Wood–Ljungdahl pathway (WLP) is an autotrophic CO2 fixation pathway in which **two CO2 molecules are reduced and combined into acetyl‑CoA** via two coordinated branches (methyl and carbonyl) that converge at the **CODH/ACS** complex. It is widely described as **energetically efficient** and **strictly anaerobic**, with sensitivity of many enzymes to O2. (zhang2024engineeredacetogenicbacteria pages 2-3, bae2024harnessingacetogenicbacteria pages 2-3, shoemaker2024wood–ljungdahlpathwayencoding pages 11-12)

**Phenotypic/physiological capacity represented.** In TraitMech terms, this trait should be curated as the **genetic/enzymatic capacity for reductive acetyl‑CoA pathway carbon fixation to acetyl‑CoA**, not as an end‑product phenotype (e.g., acetate production) per se. In many acetogens, acetyl‑CoA is subsequently converted to acetate (and other products) to recover ATP and balance redox. (zhang2024engineeredacetogenicbacteria pages 2-3, bae2024harnessingacetogenicbacteria pages 2-3)

**Operational/assay readouts (examples).** Evidence for this trait typically includes:
- Presence of diagnostic gene sets/complexes (e.g., **CODH/ACS and formyl‑THF synthetase**) in genomes/MAGs. (shoemaker2024wood–ljungdahlpathwayencoding pages 3-4)
- Growth on C1 substrates (H2+CO2, CO, formate, methanol) with acetyl‑CoA/acetate production consistent with WLP flux and appropriate energy conservation modules. (bae2024harnessingacetogenicbacteria pages 2-3, moon2024redirectingelectronflow pages 1-2)
- Environmental observations where **dark CO2 fixation** is detected and WLP genes dominate predicted autotrophy in anoxic sediments. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)

**Boundary cases and “nearby” traits.**
- **Acetogenesis (acetate as major end product)** vs **WLP trait**: WLP is the carbon fixation module; acetogenesis includes downstream acetate formation and energy conservation context. (zhang2024engineeredacetogenicbacteria pages 2-3, bae2024harnessingacetogenicbacteria pages 2-3)
- **Methanogenesis vs WLP**: in archaea, WLP/acetyl‑CoA pathway modules may be present without canonical methanogenesis genes (e.g., lacking methyl‑CoM reductase), implying WLP use is not necessarily methanogenic. (vulcano2023potentialforhomoacetogenesis pages 1-2)
- **Degenerated/partial WLP gene sets**: in the human gut, many putative CO utilizers have CODH genes and partial WLP gene sets but frequently **lack the key gene for formate synthesis from CO2**, implying a non‑autotrophic or “remodeled” WLP context. This should be flagged as **partial/degenerate WLP** rather than full trait presence. (katayama2024phylogeneticdiversityofa pages 1-7)

### 2) Key concepts and definitions (current understanding)

**Two-branch architecture.** A 2024 review describes WLP as **two branches**: (i) a **methyl branch** converting CO2 to a methyl group via sequential reactions carried on tetrahydrofolate (THF), and (ii) a **carbonyl branch** reducing CO2 to CO; both converge to produce acetyl‑CoA at the CODH/ACS complex. (zhang2024engineeredacetogenicbacteria pages 2-3)

**Core enzyme set (bacterial WLP framing).** The same review provides a canonical enzyme breakdown:
- **FDH** reduces CO2 to formate; **FTS/Fhs** forms formyl‑THF (ATP‑consuming);
- downstream methyl‑branch enzymes include **methenyl/methylene‑THF interconversions** and **MTHFR (MetF)** to methyl‑THF;
- a **methyltransferase** loads a methyl group onto **CoFeSP (corrinoid Fe‑S protein)**;
- **CODH/ACS** reduces CO2 to CO and condenses CO + methyl + CoA to acetyl‑CoA. (zhang2024engineeredacetogenicbacteria pages 2-3)

**Cofactors and electron carriers.**
- THF is explicitly described as the **C1 carrier** in WLP. (bae2024harnessingacetogenicbacteria pages 2-3)
- A 2024 gas‑fermentation study highlights **vitamin B12/corrinoid** as a critical cofactor mediating methyl transfer from THF to the **Ni‑containing A‑cluster** of ACS. (davin2024clostridiumautoethanogenumalters pages 6-7)
- Structural work (preprint) further specifies that CODH contains an **Fe‑[Ni‑3Fe‑4S] C‑cluster** and ACS contains a **Ni‑Ni‑[4Fe‑4S] A‑cluster**, with electron transfer involving **ferredoxin** through additional Fe‑S clusters. (yin2024snapshotsofacetylcoa pages 1-4)

**Energy conservation concept (WLP is ATP neutral by substrate-level phosphorylation).** A 2024 review emphasizes that acetyl‑CoA → acetate yields one ATP (Ack), but formate activation consumes ATP, giving **net‑zero substrate‑level ATP**, forcing reliance on chemiosmotic coupling. (zhang2024engineeredacetogenicbacteria pages 2-3)

### 3) Recent developments and latest research (2023–2024 prioritized)

#### 3.1 Structural snapshots of CODH/ACS (2024)
A 2024 structural study (bioRxiv) provides mechanistic detail for the **final step of CO2 fixation**, describing electron transfer from ferredoxin to CODH and methyl transfer from CoFeSP to ACS, with large ACS conformational changes and internal CO channeling. (yin2024snapshotsofacetylcoa pages 1-4)

Visual evidence from this work includes a figure overview of the methyl and carbonyl branches and active-site clusters (A- and C-clusters) and a structure figure showing cluster arrangement and conformational states of ACS. (yin2024snapshotsofacetylcoa media 9c293aee, yin2024snapshotsofacetylcoa media e5300409, yin2024snapshotsofacetylcoa media ba390f32)

#### 3.2 Gas fermentation physiology and regulation under variable H2:CO (2024)
In controlled chemostats of **Clostridium autoethanogenum**, raising the **H2:CO uptake ratio** increased CO2 incorporation into ethanol from ~50% (5:1) to **≥75%** (11:1). The authors report that **WLP proteins remained largely consistent** and suggest **post‑translational regulation** (e.g., lysine acetylation) may fine‑tune activity; they also emphasize corrinoid (B12) importance and show shifts in redox/energy components (e.g., RNF subunits). (davin2024clostridiumautoethanogenumalters pages 1-2, davin2024clostridiumautoethanogenumalters pages 6-7)

#### 3.3 Mechanistic genetics of electron-flow redirection enabling CO growth (2024)
A 2024 Nature Communications study on **Acetobacterium woodii** shows that deleting **two [FeFe]-hydrogenases (HydBA and HydA2)** and subsequent adaptation enabled growth on **CO** with acetate production; the study links this to the **hydrogen-dependent CO2 reductase (HDCR)**, which can accept electrons from **reduced ferredoxin**. A fixed mutation in **hycB2** (a ferredoxin-like subunit in the HDCR “nanowire”) is reported in adapted populations. (moon2024redirectingelectronflow pages 1-2, moon2024redirectingelectronflow pages 2-3, moon2024redirectingelectronflow pages 4-6)

The same work provides quantitative physiology relevant to curation: a CO‑adapted ΔhydBA/hydA2 mutant showed **~2× final biomass** on formate vs wild type, with stoichiometry consistent with homoacetogenesis and evidence of altered ATP yields/kinetics. (moon2024redirectingelectronflow pages 3-4, moon2024redirectingelectronflow pages 4-6)

#### 3.4 Ecology: selection for WLP in polyextreme anoxic sediments (2024)
In hypersaline Great Salt Lake sediments, metagenomic reconstruction indicates community shifts from surface aerobic heterotrophy to deeper anaerobic autotrophy; **dark CO2 fixation was detected**, and the primary predicted autotrophic mode was WLP. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)

The authors link this to selection for WLP as a **low energy requiring CO2‑fixation pathway**, and report WLP marker genes (CODH/ACS and Fhs) in MAGs classified as anaerobes (lacking terminal oxidases). (shoemaker2024wood–ljungdahlpathwayencoding pages 11-12, shoemaker2024wood–ljungdahlpathwayencoding pages 3-4)

### 4) Current applications and real-world implementations

**Commercial gas fermentation.** The C. autoethanogenum chemostat study explicitly connects findings to industrial practice, stating that **LanzaTech’s commercial ethanol process uses C. autoethanogenum on industrial waste gases** and that H2 supplementation can drive carbon efficiency. (davin2024clostridiumautoethanogenumalters pages 1-2)

**Engineering acetogens as cell factories.** A 2024 review frames acetogens as microbial platforms for CO/CO2/H2 utilization via WLP and summarizes core steps and energetic constraints that motivate engineering strategies targeting ATP/redox availability and WLP-linked energy conservation. (bae2024harnessingacetogenicbacteria pages 2-3, zhang2024engineeredacetogenicbacteria pages 2-3)

### 5) Expert opinions / authoritative synthesis (from recent reviews)

**Energetic bottleneck and the need for chemiosmotic coupling.** A 2024 review summarizes the consensus that WLP is ATP-neutral by substrate-level phosphorylation, so growth and production require membrane energy conservation via **Rnf or Ech**, which generate ion gradients used by ATP synthase. (zhang2024engineeredacetogenicbacteria pages 2-3, bae2024harnessingacetogenicbacteria pages 2-3)

**Ech vs Rnf types.** A 2024 primary study on Thermoanaerobacter kivui emphasizes that acetogenesis from H2 + CO2 can occur near the thermodynamic limit and distinguishes **Rnf-type** (Fd:NAD+ oxidoreductase with Na+-dependent membrane potential) vs **Ech-type** (ferredoxin-dependent hydrogenase coupled to proton gradient). (baum2024theenergyconvertinghydrogenase pages 1-2)

### 6) Relevant statistics and quantitative data (recent)

- **ATP yields (H2/CO2 → acetate):** ~0.3 mol ATP per mol acetate is cited for acetogenic CO2/H2 conversion in a 2024 review. (bae2024harnessingacetogenicbacteria pages 2-3)
- **Ion-to-ATP coupling in A. woodii:** the same review provides a quantitative relationship of ~3.3 Na+ translocated per 1 mol ATP (A. woodii, Rnf/Na+-dependent). (bae2024harnessingacetogenicbacteria pages 2-3)
- **Product-specific ATP yield range across donors/products:** a 2024 review reports ATP yields spanning roughly **~0.4 to +4.4 mol ATP per mol product** depending on donor (H2, CO, methanol) and product; example values include acetate from H2 ≈ 0.3 ATP, acetate from CO ≈ 1.5 ATP, ethanol from CO ≈ 1.7 ATP, ethanol from MeOH ≈ 0.7 ATP. (bae2024harnessingacetogenicbacteria pages 6-7)
- **Gas-fermentation process statistic:** increasing H2:CO uptake ratio in C. autoethanogenum chemostats increased ethanol carbon derived from CO2 from ~50% to ≥75% (5:1 → 11:1). (davin2024clostridiumautoethanogenumalters pages 1-2)

---

## Candidate nodes for TraitMech curation (grouped)

### A) Pathways / modules
- Wood–Ljungdahl pathway / reductive acetyl‑CoA pathway (METPO:traitmech:000022) (zhang2024engineeredacetogenicbacteria pages 2-3)
- Methyl branch (label-only) (zhang2024engineeredacetogenicbacteria pages 2-3)
- Carbonyl branch (label-only) (zhang2024engineeredacetogenicbacteria pages 2-3)
- Chemiosmotic energy conservation modules: Rnf-type, Ech-type (label-only) (bae2024harnessingacetogenicbacteria pages 2-3, baum2024theenergyconvertinghydrogenase pages 1-2)

### B) Enzymes / complexes (genes often vary by taxon)
- CODH/ACS complex (EC:1.2.7.4; EC:2.3.1.169; label-only complex) (zhang2024engineeredacetogenicbacteria pages 2-3, yin2024snapshotsofacetylcoa pages 1-4)
- CoFeSP (corrinoid iron–sulfur protein; label-only) (zhang2024engineeredacetogenicbacteria pages 2-3, yin2024snapshotsofacetylcoa pages 1-4)
- FDH (formate dehydrogenase; EC label varies by subunit/cofactor) (zhang2024engineeredacetogenicbacteria pages 2-3)
- HDCR (hydrogen‑dependent CO2 reductase; label-only; A. woodii context) (moon2024redirectingelectronflow pages 1-2)
- Fhs/FTS (formyl‑THF synthetase; EC:6.3.4.3) (zhang2024engineeredacetogenicbacteria pages 2-3)
- FolD / methenyl/methylene‑THF enzymes (EC:3.5.4.9; EC:1.5.1.5) (zhang2024engineeredacetogenicbacteria pages 2-3)
- MTHFR/MetF (methylene‑THF reductase; EC:1.5.1.20) (zhang2024engineeredacetogenicbacteria pages 2-3)
- PTA + ACK (acetate formation; label-only enzymes) (zhang2024engineeredacetogenicbacteria pages 2-3)
- Rnf complex (ferredoxin:NAD+ oxidoreductase; label-only) (bae2024harnessingacetogenicbacteria pages 2-3)
- Ech hydrogenase complex (ferredoxin:H+ oxidoreductase; label-only) (bae2024harnessingacetogenicbacteria pages 2-3)

### C) Metabolites / chemicals (suggested CHEBI)
- CO2 (CHEBI:16526), CO (CHEBI:17245), H2 (CHEBI:18276) (bae2024harnessingacetogenicbacteria pages 2-3)
- Formate (CHEBI:15740), acetyl‑CoA (CHEBI:15351), acetate (CHEBI:30089), CoA (CHEBI:15346) (zhang2024engineeredacetogenicbacteria pages 2-3)
- ATP (CHEBI:15422) (zhang2024engineeredacetogenicbacteria pages 2-3)

### D) Cofactors / electron carriers
- THF (CHEBI:15637) as C1 carrier (bae2024harnessingacetogenicbacteria pages 2-3)
- Vitamin B12/corrinoid (CHEBI grounding may vary; label acceptable) (davin2024clostridiumautoethanogenumalters pages 6-7)
- Ferredoxin (reduced) (CHEBI:36110) (yin2024snapshotsofacetylcoa pages 1-4, bae2024harnessingacetogenicbacteria pages 2-3)
- Ni–Fe–S clusters: A‑cluster, C‑cluster (label-only) (yin2024snapshotsofacetylcoa pages 1-4)

### E) Environmental / experimental factors (suggested ENVO label-only)
- Anoxic/anaerobic conditions (ENVO:01000254 label) (shoemaker2024wood–ljungdahlpathwayencoding pages 11-12)
- Hypersaline sediments / depth gradients / sulfide gradients (label-only) (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2, shoemaker2024wood–ljungdahlpathwayencoding pages 3-4)
- Gas feed composition (H2:CO uptake ratio) (label-only) (davin2024clostridiumautoethanogenumalters pages 1-2)
- CO inhibition of hydrogenases/HDCR (label-only) (moon2024redirectingelectronflow pages 6-8)

---

## Candidate causal edges (evidence-backed)

The following table is designed for direct transfer into a TraitMech causal graph curation workflow.

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet | Reference (DOI/URL, year) | Notes/uncertainty |
|---|---|---|---|---|---|
| Wood–Ljungdahl pathway / reductive acetyl-CoA pathway (METPO:traitmech:000022) | has_part | methyl branch (label-only) | “The Wood–Ljungdahl pathway (WLP) is a two-branch autotrophic CO2 fixation pathway: a methyl branch...” (zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fbioe.2024.1395540 / https://doi.org/10.3389/fbioe.2024.1395540, 2024 | Broad review statement; curate as pathway architecture. |
| Wood–Ljungdahl pathway / reductive acetyl-CoA pathway (METPO:traitmech:000022) | has_part | carbonyl branch (label-only) | “...and a carbonyl branch.” (zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fbioe.2024.1395540 / https://doi.org/10.3389/fbioe.2024.1395540, 2024 | Broad review statement; curate as pathway architecture. |
| methyl branch (label-only) | contributes_to | acetyl-CoA (CHEBI:15351) synthesis | “the methyl branch... reduces CO2 to formate and then to methyl-tetrahydrofolate” (davin2024clostridiumautoethanogenumalters pages 1-2) | 10.1186/s13068-024-02554-w / https://doi.org/10.1186/s13068-024-02554-w, 2024 | Object is final branch convergence product; intermediate path may need finer nodes. |
| carbonyl branch (label-only) | contributes_to | acetyl-CoA (CHEBI:15351) synthesis | “the ‘western’ carbonyl branch... reduces CO2 to CO (or uses CO directly); the branches converge at the acetyl-CoA synthase/carbon monoxide dehydrogenase complex” (davin2024clostridiumautoethanogenumalters pages 1-2) | 10.1186/s13068-024-02554-w / https://doi.org/10.1186/s13068-024-02554-w, 2024 | Broad across acetogens; CO-direct entry is condition-specific. |
| formate dehydrogenase / FDH (EC:1.17.1.9 or label-only) | reduces | carbon dioxide (CHEBI:16526) to formate (CHEBI:15740) | “formate dehydrogenase (FDH) reduces CO2 to formate” (zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fbioe.2024.1395540 / https://doi.org/10.3389/fbioe.2024.1395540, 2024 | Canonical bacterial WLP step; some taxa show FDH loss/degeneration. |
| hydrogen-dependent CO2 reductase / HDCR (label-only) | reduces | carbon dioxide (CHEBI:16526) to formate (CHEBI:15740) | “HydA2 is a component of the HDCR that normally transfers electrons from H2 to reduce CO2 to formate” (moon2024redirectingelectronflow pages 1-2) | 10.1038/s41467-024-49680-5 / https://doi.org/10.1038/s41467-024-49680-5, 2024 | Taxon-specific: Acetobacterium woodii HDCR. |
| hydrogen (CHEBI:18276) | enables | HDCR-mediated CO2 reduction (label-only) | “HDCR that normally transfers electrons from H2 to reduce CO2 to formate” (moon2024redirectingelectronflow pages 1-2) | 10.1038/s41467-024-49680-5 / https://doi.org/10.1038/s41467-024-49680-5, 2024 | Taxon-specific: A. woodii. |
| formyl-THF synthetase / FTS / Fhs (EC:6.3.4.3) | catalyzes | formyl-THF formation from formate (label-only) | “formyl-THF synthetase (FTS) forms formyl-THF (consuming one ATP)” (zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fbioe.2024.1395540 / https://doi.org/10.3389/fbioe.2024.1395540, 2024 | Use label-only if substrate/product stoichiometry not separately curated. |
| formyl-THF synthetase / FTS / Fhs (EC:6.3.4.3) | requires | ATP (CHEBI:15422) | “formyl-THF synthetase (FTS) forms formyl-THF (consuming one ATP)” (zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fbioe.2024.1395540 / https://doi.org/10.3389/fbioe.2024.1395540, 2024 | Strong mechanistic edge. |
| FolD / methenyl-THF cyclohydrolase + methylene-THF dehydrogenase (EC:3.5.4.9 / EC:1.5.1.5) | catalyzes | methenyl-THF → methylene-THF conversions (label-only) | “MDH and MTHFR reduce methenyl-THF → methylene-THF → methyl-THF” (zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fbioe.2024.1395540 / https://doi.org/10.3389/fbioe.2024.1395540, 2024 | Review compresses FolD/MDH steps; exact enzyme naming varies by taxon. |
| MTHFR / MetF / methylene-THF reductase (EC:1.5.1.20) | reduces | methylene-THF to methyl-THF (label-only) | “MDH and MTHFR reduce methenyl-THF → methylene-THF → methyl-THF” (zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fbioe.2024.1395540 / https://doi.org/10.3389/fbioe.2024.1395540, 2024 | Broad but enzyme composition “variable” across acetogens. |
| methyltransferase (label-only) | transfers | methyl group (CHEBI:25973) to corrinoid iron-sulfur protein / CoFeSP (label-only) | “methyltransferase transfers the methyl onto a corrinoid iron-sulfur protein (CoFeSP)” (zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fbioe.2024.1395540 / https://doi.org/10.3389/fbioe.2024.1395540, 2024 | Strong pathway step; exact enzyme family differs in bacteria vs archaea. |
| corrinoid iron-sulfur protein / CoFeSP (label-only) | transfers | methyl group (CHEBI:25973) to ACS active site | “methyl-Co(III)-B12 on CoFeSP delivers the methyl to ACS” (yin2024snapshotsofacetylcoa pages 1-4) | 10.1101/2024.08.05.606187 / https://doi.org/10.1101/2024.08.05.606187, 2024 | Preprint; structural evidence strong but mark uncertain until peer review. |
| carbon monoxide dehydrogenase / CODH (EC:1.2.7.4) | reduces | carbon dioxide (CHEBI:16526) to carbon monoxide (CHEBI:17245) | “CODH/ACS reduces CO2 → CO” (zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fbioe.2024.1395540 / https://doi.org/10.3389/fbioe.2024.1395540, 2024 | Reversible enzyme; direction depends on physiology. |
| acetyl-CoA synthase / ACS (EC:2.3.1.169) | condenses | carbon monoxide (CHEBI:17245) + methyl-CoFeSP + CoA (CHEBI:15346) into acetyl-CoA (CHEBI:15351) | “combines CO, methyl-CoFeSP and CoA into acetyl-CoA” (zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fbioe.2024.1395540 / https://doi.org/10.3389/fbioe.2024.1395540, 2024 | Central terminal step of WLP. |
| CODH/ACS complex (label-only) | channels | carbon monoxide (CHEBI:17245) to ACS active site | “CO is channeled internally through a hydrophobic tunnel” (yin2024snapshotsofacetylcoa pages 1-4) | 10.1101/2024.08.05.606187 / https://doi.org/10.1101/2024.08.05.606187, 2024 | Preprint structural claim; useful for mechanistic notes, maybe not first-pass TraitMech edge. |
| CODH/ACS complex (label-only) | contains_cofactor | Ni-Fe-S active-site clusters (label-only) | “CODH carries an Fe-[Ni-3Fe-4S] C-cluster... ACS contains the Ni-Ni-[4Fe-4S] A-cluster” (yin2024snapshotsofacetylcoa pages 1-4) | 10.1101/2024.08.05.606187 / https://doi.org/10.1101/2024.08.05.606187, 2024 | Preprint but aligns with established biochemistry; can ground clusters as label-only. |
| ferredoxin, reduced (CHEBI:36110) | donates_electrons_to | CODH/CO2 reduction steps (label-only) | “ferredoxin docks near the D-cluster and transfers electrons via the B-cluster to the C-cluster” (yin2024snapshotsofacetylcoa pages 1-4) | 10.1101/2024.08.05.606187 / https://doi.org/10.1101/2024.08.05.606187, 2024 | Preprint structural evidence; electron-transfer direction may vary with conditions. |
| tetrahydrofolate / THF (CHEBI:15637) | functions_as | C1 carrier in WLP methyl branch (label-only) | “converts two CO2 to one acetyl‑CoA using THF as the C1 carrier” (bae2024harnessingacetogenicbacteria pages 2-3) | 10.1039/d4cb00099d / https://doi.org/10.1039/d4cb00099d, 2024 | Good cofactor edge. |
| vitamin B12 / corrinoid (CHEBI:176843 or label-only) | enables | methyl transfer to ACS/CODH A-cluster | “Vitamin B12 (corrinoid) is highlighted as a critical WLP cofactor facilitating methyl transfer from tetrahydrofolate to the nickel-containing A-cluster” (davin2024clostridiumautoethanogenumalters pages 6-7) | 10.1186/s13068-024-02554-w / https://doi.org/10.1186/s13068-024-02554-w, 2024 | Strong cofactor edge from chemostat proteomics paper. |
| CODH-mediated CO oxidation (label-only) | generates | reduced ferredoxin (CHEBI:36110) | “CODH-mediated CO oxidation can produce reduced ferredoxin (Fdred) to feed these systems” (bae2024harnessingacetogenicbacteria pages 2-3) | 10.1039/d4cb00099d / https://doi.org/10.1039/d4cb00099d, 2024 | Condition-specific to CO-utilizing mode. |
| acetyl-CoA (CHEBI:15351) | converted_to | acetate (CHEBI:30089) + ATP via PTA/ACK (label-only) | “Acetyl-CoA → acetate via PTA and ACK yields one ATP” (zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fbioe.2024.1395540 / https://doi.org/10.3389/fbioe.2024.1395540, 2024 | Could be split into PTA and ACK edges if desired. |
| Wood–Ljungdahl pathway (METPO:traitmech:000022) | net_slp_balance | zero ATP (label-only) | “activation of formate consumes one ATP, so substrate-level phosphorylation nets zero ATP” (zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fbioe.2024.1395540 / https://doi.org/10.3389/fbioe.2024.1395540, 2024 | High-value trait-level energetic property. |
| Rnf complex (label-only) | conserves_energy_via | ion gradient (GO:0034220 or label-only) | “Rnf is an ion-translocating ferredoxin (Fd):NAD+ oxidoreductase... coupled to generation of a transmembrane proton (H+) or sodium (Na+) gradient” (bae2024harnessingacetogenicbacteria pages 2-3) | 10.1039/d4cb00099d / https://doi.org/10.1039/d4cb00099d, 2024 | Ion specificity is taxon-specific (H+ or Na+). |
| Ech complex (label-only) | conserves_energy_via | proton gradient (GO:1902600 or label-only) | “Ech functions as an Fd:H+ oxidoreductase... to establish a transmembrane H+ gradient” (bae2024harnessingacetogenicbacteria pages 2-3) | 10.1039/d4cb00099d / https://doi.org/10.1039/d4cb00099d, 2024 | Strong general edge for Ech-type acetogens. |
| ion gradient (GO:0034220 or label-only) | drives | ATP synthase (EC:7.1.2.2 / EC:7.1.2.1) | “These ion gradients drive ATP synthase to form ATP via chemiosmotic phosphorylation” (bae2024harnessingacetogenicbacteria pages 2-3) | 10.1039/d4cb00099d / https://doi.org/10.1039/d4cb00099d, 2024 | Broad energy-conservation edge. |
| autotrophic acetogenesis from H2 + CO2 (label-only) | yields | ~0.3 mol ATP per mol acetate (label-only) | “acetogenic CO2/H2 conversion yields about 0.3 mol ATP per mol acetate” (bae2024harnessingacetogenicbacteria pages 2-3) | 10.1039/d4cb00099d / https://doi.org/10.1039/d4cb00099d, 2024 | Quantitative energetic statistic; model-dependent average. |
| anoxia / anaerobic conditions (ENVO:01000254 or label-only) | selected_by / favors | Wood–Ljungdahl pathway prevalence (label-only) | “The pathway is largely restricted to anaerobes, likely because of ‘the O2 sensitivity of many of its enzymes’” (shoemaker2024wood–ljungdahlpathwayencoding pages 11-12) | 10.1093/femsec/fiae105 / https://doi.org/10.1093/femsec/fiae105, 2024 | Best represented as environmental selection, not direct molecular causation. |
| increasing depth in hypersaline Great Salt Lake sediments (ENVO:hypersaline sediment label-only) | selected_by / associated_with | increased prevalence of WLP-encoding anaerobes (label-only) | “increased prevalence of the WL pathway with increasing depth” (shoemaker2024wood–ljungdahlpathwayencoding pages 11-12) | 10.1093/femsec/fiae105 / https://doi.org/10.1093/femsec/fiae105, 2024 | Community-level ecological association, not single-organism causal mechanism. |
| hypersaline, anoxic sediment conditions (label-only) | favor | WLP-based dark CO2 fixation (label-only) | “Dark CO2 fixation was directly detected in sediments, and the primary predicted autotrophic route was the Wood–Ljungdahl pathway” (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2) | 10.1093/femsec/fiae105 / https://doi.org/10.1093/femsec/fiae105, 2024 | Ecological/process edge; may belong in environment-linked subgraph. |
| deletion of hydBA + hydA2 in Acetobacterium woodii (label-only genotype) | enables | growth on CO (CHEBI:17245) | “the mutant acquired the ability to grow on CO and produce acetate” (moon2024redirectingelectronflow pages 1-2) | 10.1038/s41467-024-49680-5 / https://doi.org/10.1038/s41467-024-49680-5, 2024 | Strong but highly taxon- and adaptation-specific; do not generalize to WLP broadly. |
| deletion of hydBA + hydA2 in Acetobacterium woodii (label-only genotype) | increases | ferredoxin-dependent HDCR activity (label-only) | “in the absence of the HydA2 module, the authors observed increased ferredoxin-dependent CO2 reduction by HDCR” (moon2024redirectingelectronflow pages 1-2) | 10.1038/s41467-024-49680-5 / https://doi.org/10.1038/s41467-024-49680-5, 2024 | Taxon-specific mechanistic adaptation. |
| hycB2 mutation in CO-adapted A. woodii (label-only) | associated_with | adapted CO/formate-growth phenotype (label-only) | “Whole-population SNP analysis of CO-adapted cells showed a fixed mutation in hycB2” (moon2024redirectingelectronflow pages 1-2) | 10.1038/s41467-024-49680-5 / https://doi.org/10.1038/s41467-024-49680-5, 2024 | Association, not clean causal proof; mark uncertain for curation. |
| CO-adapted ΔhydBA/hydA2 A. woodii (label-only genotype) | improves | growth on formate (CHEBI:15740) | “The CO-adapted ΔhydBA/hydA2 mutant also attains twice the biomass of wild type when growing on formate” (moon2024redirectingelectronflow pages 1-2) | 10.1038/s41467-024-49680-5 / https://doi.org/10.1038/s41467-024-49680-5, 2024 | Strong phenotype but adaptation-specific. |
| CO (CHEBI:17245) | inhibited_by / reversibly inhibits | HDCR (label-only) | “HDCR is central to CO/formate metabolism and can be inhibited by CO (inhibition is reversible)” (moon2024redirectingelectronflow pages 6-8) | 10.1038/s41467-024-49680-5 / https://doi.org/10.1038/s41467-024-49680-5, 2024 | Taxon-specific to A. woodii study context. |
| reduced ferredoxin (CHEBI:36110) | can_drive | HDCR-mediated CO2 reduction in A. woodii (label-only) | “purified A. woodii HDCR uses reduced ferredoxin for CO2 reduction to formate” (moon2024redirectingelectronflow pages 6-8) | 10.1038/s41467-024-49680-5 / https://doi.org/10.1038/s41467-024-49680-5, 2024 | Taxon-specific but mechanistically informative. |
| elevated H2:CO ratio in C. autoethanogenum chemostats (label-only condition) | increases | CO2 incorporation into ethanol (label-only) | “increasing H2:CO uptake ratios strongly increases CO2 incorporation into ethanol (from ~50% at a 5:1 condition to at least 75% at an 11:1 condition)” (davin2024clostridiumautoethanogenumalters pages 1-2) | 10.1186/s13068-024-02554-w / https://doi.org/10.1186/s13068-024-02554-w, 2024 | Application/process edge; industrially relevant but not core trait mechanism. |
| Clostridium autoethanogenum gas fermentation (NCBITaxon:511437 if desired) | implemented_in | industrial waste-gas ethanol production (label-only) | “LanzaTech’s commercial ethanol process uses C. autoethanogenum on industrial waste gases” (davin2024clostridiumautoethanogenumalters pages 1-2) | 10.1186/s13068-024-02554-w / https://doi.org/10.1186/s13068-024-02554-w, 2024 | Real-world implementation; application edge rather than causal trait graph core. |


*Table: This table compiles evidence-backed candidate subject-predicate-object edges for curating a TraitMech causal graph of the Wood–Ljungdahl pathway. It covers core pathway architecture, enzymes, cofactors, energy conservation, ecological selection, and key perturbation studies, with uncertainty flags where claims are taxon-specific or from preprints.*

---

## Warnings / curation cautions (do not over-generalize)

1. **Preprint evidence:** mechanistic structural claims from Yin et al. 2024 are from bioRxiv and should be marked **uncertain** until peer-reviewed, despite consistency with established CODH/ACS biochemistry. (yin2024snapshotsofacetylcoa pages 1-4)
2. **Taxon-specific genotype/phenotype edges:** ΔhydBA/hydA2 enabling CO growth and hycB2 SNP associations are **Acetobacterium woodii–specific** and depend on adaptation history; curate as organism/condition-specific edges or avoid generalizing to the WLP trait. (moon2024redirectingelectronflow pages 1-2, moon2024redirectingelectronflow pages 4-6)
3. **Partial/degenerate pathways:** gut CO-utilizer “degenerate WLP” gene sets (e.g., missing FDH step) should not be curated as full WLP trait presence without additional evidence for complete pathway and autotrophic function. (katayama2024phylogeneticdiversityofa pages 1-7)
4. **Ecological association vs causation:** depth/hypersalinity associations with WLP prevalence are community-level correlations; curate as “associated_with/selected_by” rather than deterministic mechanistic edges. (shoemaker2024wood–ljungdahlpathwayencoding pages 11-12)

---

## DOI-first bibliography (recent-first; with URLs and publication dates where available)

1. **Moon J., Poehlein A., Daniel R., Müller V.** *Redirecting electron flow in Acetobacterium woodii enables growth on CO and improves growth on formate.* **Nature Communications** (Jun 2024). DOI: **10.1038/s41467-024-49680-5**. https://doi.org/10.1038/s41467-024-49680-5 (moon2024redirectingelectronflow pages 1-2)
2. **Davin M.E. et al.** *Clostridium autoethanogenum alters cofactor synthesis, redox metabolism, and lysine-acetylation in response to elevated H2:CO feedstock ratios for enhancing carbon capture efficiency.* **Biotechnology for Biofuels and Bioproducts** (Sep 2024). DOI: **10.1186/s13068-024-02554-w**. https://doi.org/10.1186/s13068-024-02554-w (davin2024clostridiumautoethanogenumalters pages 1-2)
3. **Bae J. et al.** *Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production.* **RSC Chemical Biology** (Jul 2024). DOI: **10.1039/d4cb00099d**. https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3)
4. **Zhang J.-Z. et al.** *Engineered acetogenic bacteria as microbial cell factory for diversified biochemicals.* **Frontiers in Bioengineering and Biotechnology** (Jul 2024). DOI: **10.3389/fbioe.2024.1395540**. https://doi.org/10.3389/fbioe.2024.1395540 (zhang2024engineeredacetogenicbacteria pages 2-3)
5. **Shoemaker A. et al.** *Wood–Ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at Great Salt Lake, Utah.* **FEMS Microbiology Ecology** (Jul 2024). DOI: **10.1093/femsec/fiae105**. https://doi.org/10.1093/femsec/fiae105 (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)
6. **Baum C. et al.** *The energy-converting hydrogenase Ech2 is important for the growth of the thermophilic acetogen Thermoanaerobacter kivui on ferredoxin-dependent substrates.* **Microbiology Spectrum** (Apr 2024). DOI: **10.1128/spectrum.03380-23**. https://doi.org/10.1128/spectrum.03380-23 (baum2024theenergyconvertinghydrogenase pages 1-2)
7. **Yin M.D. et al.** *Snapshots of acetyl-CoA synthesis, the final step of CO2 fixation in the Wood-Ljungdahl pathway.* **bioRxiv** (Aug 2024). DOI: **10.1101/2024.08.05.606187**. https://doi.org/10.1101/2024.08.05.606187 (yin2024snapshotsofacetylcoa pages 1-4)
8. **Vulcano F. et al.** *Potential for homoacetogenesis via the Wood–Ljungdahl pathway in Korarchaeia lineages from marine hydrothermal vents.* **Environmental Microbiology Reports** (May 2023). DOI: **10.1111/1758-2229.13168**. https://doi.org/10.1111/1758-2229.13168 (vulcano2023potentialforhomoacetogenesis pages 1-2)
9. **Katayama Y.A. et al.** *Phylogenetic diversity of putative nickel-containing carbon monoxide dehydrogenase-encoding prokaryotes in the human gut microbiome.* **Microbial Genomics** (Aug 2024). DOI: **10.1099/mgen.0.001285**. https://doi.org/10.1099/mgen.0.001285 (katayama2024phylogeneticdiversityofa pages 1-7)


References

1. (zhang2024engineeredacetogenicbacteria pages 2-3): Jun-Zhe Zhang, Yu-Zhen Li, Zhi-Ning Xi, Hui-Peng Gao, Quan Zhang, Li-Cheng Liu, Fu-Li Li, and Xiao-Qing Ma. Engineered acetogenic bacteria as microbial cell factory for diversified biochemicals. Frontiers in Bioengineering and Biotechnology, Jul 2024. URL: https://doi.org/10.3389/fbioe.2024.1395540, doi:10.3389/fbioe.2024.1395540. This article has 26 citations.

2. (bae2024harnessingacetogenicbacteria pages 2-3): Jiyun Bae, Chanho Park, Hyunwoo Jung, Sangrak Jin, and Byung-Kwan Cho. Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production. RSC Chemical Biology, 5:812-832, Jul 2024. URL: https://doi.org/10.1039/d4cb00099d, doi:10.1039/d4cb00099d. This article has 19 citations and is from a peer-reviewed journal.

3. (shoemaker2024wood–ljungdahlpathwayencoding pages 11-12): Anna Shoemaker, Andrew Maritan, Su Cosar, Sylvia Nupp, Ana Menchaca, Thomas Jackson, Aria Dang, Bonnie K Baxter, Daniel R Colman, Eric C Dunham, and Eric S Boyd. Wood–ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at great salt lake, utah. FEMS Microbiology Ecology, Jul 2024. URL: https://doi.org/10.1093/femsec/fiae105, doi:10.1093/femsec/fiae105. This article has 11 citations and is from a peer-reviewed journal.

4. (shoemaker2024wood–ljungdahlpathwayencoding pages 3-4): Anna Shoemaker, Andrew Maritan, Su Cosar, Sylvia Nupp, Ana Menchaca, Thomas Jackson, Aria Dang, Bonnie K Baxter, Daniel R Colman, Eric C Dunham, and Eric S Boyd. Wood–ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at great salt lake, utah. FEMS Microbiology Ecology, Jul 2024. URL: https://doi.org/10.1093/femsec/fiae105, doi:10.1093/femsec/fiae105. This article has 11 citations and is from a peer-reviewed journal.

5. (moon2024redirectingelectronflow pages 1-2): Jimyung Moon, Anja Poehlein, Rolf Daniel, and Volker Müller. Redirecting electron flow in acetobacterium woodii enables growth on co and improves growth on formate. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49680-5, doi:10.1038/s41467-024-49680-5. This article has 8 citations and is from a highest quality peer-reviewed journal.

6. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2): Anna Shoemaker, Andrew Maritan, Su Cosar, Sylvia Nupp, Ana Menchaca, Thomas Jackson, Aria Dang, Bonnie K Baxter, Daniel R Colman, Eric C Dunham, and Eric S Boyd. Wood–ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at great salt lake, utah. FEMS Microbiology Ecology, Jul 2024. URL: https://doi.org/10.1093/femsec/fiae105, doi:10.1093/femsec/fiae105. This article has 11 citations and is from a peer-reviewed journal.

7. (vulcano2023potentialforhomoacetogenesis pages 1-2): Francesca Vulcano, Petra Hribovšek, Emily Olesin Denny, Ida H. Steen, and Runar Stokke. Potential for homoacetogenesis via the wood–ljungdahl pathway in korarchaeia lineages from marine hydrothermal vents. Environmental Microbiology Reports, 15:698-707, May 2023. URL: https://doi.org/10.1111/1758-2229.13168, doi:10.1111/1758-2229.13168. This article has 5 citations and is from a peer-reviewed journal.

8. (katayama2024phylogeneticdiversityofa pages 1-7): Yuka Adachi Katayama, Ryoma Kamikawa, and Takashi Yoshida. Phylogenetic diversity of the carbon monoxide-utilizing prokaryotes and their divergent carbon monoxide metabolisms in the human gut microbiome. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2023.10.23.563559, doi:10.1101/2023.10.23.563559. This article has 1 citations.

9. (davin2024clostridiumautoethanogenumalters pages 6-7): Megan E. Davin, R. Adam Thompson, Richard J. Giannone, Lucas W. Mendelson, Dana L. Carper, Madhavi Z. Martin, Michael E. Martin, Nancy L. Engle, Timothy J. Tschaplinski, Steven D. Brown, and Robert L. Hettich. Clostridium autoethanogenum alters cofactor synthesis, redox metabolism, and lysine-acetylation in response to elevated h2:co feedstock ratios for enhancing carbon capture efficiency. Biotechnology for Biofuels and Bioproducts, Sep 2024. URL: https://doi.org/10.1186/s13068-024-02554-w, doi:10.1186/s13068-024-02554-w. This article has 18 citations and is from a domain leading peer-reviewed journal.

10. (yin2024snapshotsofacetylcoa pages 1-4): Max Dongsheng Yin, Olivier N. Lemaire, José Guadalupe Rosas Jiménez, Mélissa Belhamri, Anna Shevchenko, Gerhard Hummer, Tristan Wagner, and Bonnie J. Murphy. Snapshots of acetyl-coa synthesis, the final step of co2 fixation in the wood-ljungdahl pathway. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.05.606187, doi:10.1101/2024.08.05.606187. This article has 2 citations.

11. (yin2024snapshotsofacetylcoa media 9c293aee): Max Dongsheng Yin, Olivier N. Lemaire, José Guadalupe Rosas Jiménez, Mélissa Belhamri, Anna Shevchenko, Gerhard Hummer, Tristan Wagner, and Bonnie J. Murphy. Snapshots of acetyl-coa synthesis, the final step of co2 fixation in the wood-ljungdahl pathway. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.05.606187, doi:10.1101/2024.08.05.606187. This article has 2 citations.

12. (yin2024snapshotsofacetylcoa media e5300409): Max Dongsheng Yin, Olivier N. Lemaire, José Guadalupe Rosas Jiménez, Mélissa Belhamri, Anna Shevchenko, Gerhard Hummer, Tristan Wagner, and Bonnie J. Murphy. Snapshots of acetyl-coa synthesis, the final step of co2 fixation in the wood-ljungdahl pathway. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.05.606187, doi:10.1101/2024.08.05.606187. This article has 2 citations.

13. (yin2024snapshotsofacetylcoa media ba390f32): Max Dongsheng Yin, Olivier N. Lemaire, José Guadalupe Rosas Jiménez, Mélissa Belhamri, Anna Shevchenko, Gerhard Hummer, Tristan Wagner, and Bonnie J. Murphy. Snapshots of acetyl-coa synthesis, the final step of co2 fixation in the wood-ljungdahl pathway. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.05.606187, doi:10.1101/2024.08.05.606187. This article has 2 citations.

14. (davin2024clostridiumautoethanogenumalters pages 1-2): Megan E. Davin, R. Adam Thompson, Richard J. Giannone, Lucas W. Mendelson, Dana L. Carper, Madhavi Z. Martin, Michael E. Martin, Nancy L. Engle, Timothy J. Tschaplinski, Steven D. Brown, and Robert L. Hettich. Clostridium autoethanogenum alters cofactor synthesis, redox metabolism, and lysine-acetylation in response to elevated h2:co feedstock ratios for enhancing carbon capture efficiency. Biotechnology for Biofuels and Bioproducts, Sep 2024. URL: https://doi.org/10.1186/s13068-024-02554-w, doi:10.1186/s13068-024-02554-w. This article has 18 citations and is from a domain leading peer-reviewed journal.

15. (moon2024redirectingelectronflow pages 2-3): Jimyung Moon, Anja Poehlein, Rolf Daniel, and Volker Müller. Redirecting electron flow in acetobacterium woodii enables growth on co and improves growth on formate. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49680-5, doi:10.1038/s41467-024-49680-5. This article has 8 citations and is from a highest quality peer-reviewed journal.

16. (moon2024redirectingelectronflow pages 4-6): Jimyung Moon, Anja Poehlein, Rolf Daniel, and Volker Müller. Redirecting electron flow in acetobacterium woodii enables growth on co and improves growth on formate. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49680-5, doi:10.1038/s41467-024-49680-5. This article has 8 citations and is from a highest quality peer-reviewed journal.

17. (moon2024redirectingelectronflow pages 3-4): Jimyung Moon, Anja Poehlein, Rolf Daniel, and Volker Müller. Redirecting electron flow in acetobacterium woodii enables growth on co and improves growth on formate. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49680-5, doi:10.1038/s41467-024-49680-5. This article has 8 citations and is from a highest quality peer-reviewed journal.

18. (baum2024theenergyconvertinghydrogenase pages 1-2): Christoph Baum, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, Volker Müller, and Mirko Basen. The energy-converting hydrogenase ech2 is important for the growth of the thermophilic acetogen <i>thermoanaerobacter kivui</i> on ferredoxin-dependent substrates. Apr 2024. URL: https://doi.org/10.1128/spectrum.03380-23, doi:10.1128/spectrum.03380-23. This article has 12 citations and is from a domain leading peer-reviewed journal.

19. (bae2024harnessingacetogenicbacteria pages 6-7): Jiyun Bae, Chanho Park, Hyunwoo Jung, Sangrak Jin, and Byung-Kwan Cho. Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production. RSC Chemical Biology, 5:812-832, Jul 2024. URL: https://doi.org/10.1039/d4cb00099d, doi:10.1039/d4cb00099d. This article has 19 citations and is from a peer-reviewed journal.

20. (moon2024redirectingelectronflow pages 6-8): Jimyung Moon, Anja Poehlein, Rolf Daniel, and Volker Müller. Redirecting electron flow in acetobacterium woodii enables growth on co and improves growth on formate. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49680-5, doi:10.1038/s41467-024-49680-5. This article has 8 citations and is from a highest quality peer-reviewed journal.