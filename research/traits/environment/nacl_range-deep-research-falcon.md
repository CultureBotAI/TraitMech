---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:20:52.515868'
end_time: '2026-06-17T23:32:46.609964'
duration_seconds: 714.09
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl range
  trait_identifier: METPO:1000334
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_range
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A salinity phenotype with numerical limits that bounds the minimum and
    maximum NaCl concentrations supporting growth of an organism.
  parent_traits: METPO:1000532, METPO:1000535
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports the span of NaCl concentrations supporting growth as a standard halophily
    descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high salt concentrations
    (Saline-Systems review supports osmotic-tolerance breadth as the basis of the
    NaCl-range phenotype.)'
  causal_graph_summary: 'nacl_range_tolerance_breadth: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range
- **METPO identifier:** METPO:1000334
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits that bounds the minimum and maximum NaCl concentrations supporting growth of an organism.
- **Parent traits:** METPO:1000532, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the span of NaCl concentrations supporting growth as a standard halophily descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high salt concentrations (Saline-Systems review supports osmotic-tolerance breadth as the basis of the NaCl-range phenotype.)
- **Existing causal graph summary:** nacl_range_tolerance_breadth: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **NaCl range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range.yaml`.

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
- **Trait label:** NaCl range
- **METPO identifier:** METPO:1000334
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits that bounds the minimum and maximum NaCl concentrations supporting growth of an organism.
- **Parent traits:** METPO:1000532, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the span of NaCl concentrations supporting growth as a standard halophily descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high salt concentrations (Saline-Systems review supports osmotic-tolerance breadth as the basis of the NaCl-range phenotype.)
- **Existing causal graph summary:** nacl_range_tolerance_breadth: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **NaCl range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **NaCl range** (METPO:1000334)

## 1) Scope summary (trait meaning and boundaries)

**Trait definition (operational):** *NaCl range* is the **numerical lower and upper NaCl concentrations that bound conditions under which an organism can grow**, as determined by a defined growth assay (e.g., OD600 increase, colony formation, or other viability/growth metrics) across a salinity gradient (METPO:1000334). This is distinct from (i) **NaCl optimum** (the concentration giving maximal growth rate/biomass), (ii) categorical ecological labels (slight/moderate/extreme halophile), and (iii) general **osmotic tolerance** measured with non-NaCl osmolytes or different ions. This distinction matters because growth boundaries can shift with **ion identity**, **media composition**, and **measurement endpoint**. (xing2024thepolyextremophilenatranaerobius pages 6-7, schneegurt2012mediaandconditions pages 6-9)

**Boundary cases / nearby traits to separate during curation:**
- **Obligate haloarchaea** can show a *hard lower boundary* where cells lyse or lose morphology at low NaCl; Schneegurt summarizes that halophilic archaea “generally require NaCl of at least 1.5 M” and that “significant cell lysis occurred below 1.5 M,” implying a sharp lower-limit phenotype that is different from merely “reduced growth.” (schneegurt2012mediaandconditions pages 6-9)
- **Assay/reporting artifacts:** Many standard recipes report salinity as **% (total salts)**, while physiology papers often report **molar NaCl**; these are not interchangeable without additional composition information. (schneegurt2012mediaandconditions pages 6-9)
- **Water activity framing:** Growth limits are frequently constrained by **water activity (aw)** rather than NaCl specifically, and aw may be experimentally manipulated by salts or sugars; thus, NaCl range should be curated as **NaCl-specific** unless explicitly stated as aw/osmolarity range. (bartha2022investigatingextremotolerantmicrobes pages 21-25)

## 2) Key concepts and current mechanistic understanding (2023–2024 prioritized)

### 2.1 Two principal osmoadaptation paradigms that shape NaCl growth limits
1) **“Salt-in” strategy:** Cells accumulate inorganic ions (notably **K+ and Cl−**) to balance external osmotic pressure, requiring cellular macromolecules (especially proteins) to function at high ionic strength; this can enforce a **high minimal salinity requirement** because low salt destabilizes macromolecules. This framework is explicitly discussed in the context of salt-in vs compatible-solute strategies (with representative intracellular KCl values) and is aligned with low-salt lysis sensitivity described for haloarchaea. (bartha2022investigatingextremotolerantmicrobes pages 21-25, schneegurt2012mediaandconditions pages 6-9)

2) **“Salt-out/compatible solute” strategy:** Cells maintain low cytosolic inorganic ion concentrations and instead accumulate **compatible solutes** (osmolytes), either by **uptake** or **biosynthesis** (e.g., glycine betaine, glutamate, proline), supporting growth across broader salinity ranges but often at higher energetic cost. (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 17-19)

### 2.2 Ion homeostasis nodes that causally impact NaCl range

**Potassium uptake systems (Trk/Ktr/Kdp/Kup/KimA):** Rapid **K+ uptake** is a canonical early response to osmotic upshift; subsequent osmolyte accumulation partially replaces K+ as a compatible osmotic component. A 2024 MMBR review synthesizes extensive evidence that the second messenger **c-di-AMP** directly regulates potassium homeostasis by binding to potassium transport systems (including Trk/Ktr gating subunits and high-affinity systems such as KimA/Kup), generally inhibiting K+ uptake when c-di-AMP is high. This establishes a mechanistic route linking signaling state → K+ flux → osmotic tolerance → NaCl growth boundaries. (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 6-8)

**Na+/H+ antiporters:** In high-salt conditions, maintaining low cytosolic Na+ and pH balance depends on Na+ export systems. In the 2024 *Natranaerobius thermophilus* multi-omics study, Na+/H+ antiporters (e.g., NhaC family entries) are among the transport functions present and responsive to salinity, consistent with a role in maintaining ionic homeostasis at high external Na+. (xing2024thepolyextremophilenatranaerobius pages 6-7)

### 2.3 Compatible solutes and transport systems that causally impact NaCl range

The 2024 *Natranaerobius thermophilus* study provides direct quantitative evidence that compatible solutes increase across salinity conditions, supporting the concept that compatible-solute systems extend the upper NaCl limit:
- Intracellular **glycine betaine** rises from ~52.7 mM (2.5 M Na+) to ~893.1 mM (4.3 M Na+). (xing2024thepolyextremophilenatranaerobius pages 17-19)
- Intracellular **glutamate** rises to ~221.3 mM at 4.3 M Na+. (xing2024thepolyextremophilenatranaerobius pages 17-19)
- Intracellular **proline** remains substantial (reported ~67–130 mM across conditions), indicating osmolyte involvement although the directionality may be non-monotonic and should be curated cautiously. (xing2024thepolyextremophilenatranaerobius pages 17-19)

Transporter families implicated include **glycine betaine ABC transporters (Opu/ProU families)**, BCCT-type uptake components, and **PutP** (Na+/proline symporter), with differential regulation across salinities in proteomics and targeted validation. (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 17-19)

### 2.4 Regulation: cyclic di-AMP as a causal controller of NaCl tolerance breadth

Two 2024 authoritative sources provide convergent evidence that **c-di-AMP is a master regulator of cell volume/osmotic homeostasis**, acting through potassium and osmolyte transport (review synthesis plus primary functional genetics):
- Review-level mechanism: c-di-AMP binds potassium transport components and also binds **OpuA-like compatible-solute importers**, connecting c-di-AMP levels to both K+ and osmolyte handling. (foster2024bacterialcellvolume pages 12-13, foster2024bacterialcellvolume pages 8-10)
- Primary evidence in *Bacillus anthracis*: Elevated c-di-AMP (via PDE inactivation) is associated with **inability to grow at mild salt**, and expression of potassium uptake components **partially rescues growth at 2.5% NaCl**; c-di-AMP represses the **kdp operon** via a c-di-AMP-responsive **ydaO riboswitch**, and c-di-AMP targets include **KtrC** and **KdpD**. (hu2024cdiampaccumulationimpairs pages 2-6, hu2024cdiampaccumulationimpairs pages 6-9)

This yields a curation-relevant causal chain: **c-di-AMP → (↓ K+ uptake; altered osmolyte import) → altered osmotic balance → narrower/wider NaCl growth range**. (hu2024cdiampaccumulationimpairs pages 2-6, foster2024bacterialcellvolume pages 8-10)

## 3) Recent developments / latest research emphasis (2023–2024)

### 3.1 Quantitative multi-omics linking salinity gradients to intracellular osmolytes and ions (2024)
A key recent development is the use of multi-omics plus targeted metabolite/ion quantification across defined salinity levels to mechanistically ground growth-range observations. In *N. thermophilus*, the authors explicitly report a **growth range of 2.5–5.0 M total Na+** and an **optimal range of 3.1–4.3 M**, while also measuring intracellular osmolytes and K+ and annotating salinity-responsive transporters. (xing2024thepolyextremophilenatranaerobius pages 6-7)

### 3.2 Signaling-centric view of osmotic tolerance (2024)
The 2024 MMBR review reframes osmoadaptation as a **quantitative cell-volume control problem**, with c-di-AMP as a central regulator. It highlights that misregulation (too high or too low c-di-AMP) causes characteristic phenotypes (e.g., hypertonic sensitivity, altered cell size), and that suppressors frequently map to potassium/compatible-solute transport, directly connecting regulation to salt tolerance phenotypes that can shift NaCl growth boundaries. (foster2024bacterialcellvolume pages 12-13, foster2024bacterialcellvolume pages 6-8)

### 3.3 Mechanistically precise regulatory edges via riboswitches and transporter targeting (2024)
The *B. anthracis* primary study provides an unusually curation-friendly regulatory mechanism: c-di-AMP represses potassium uptake gene expression via a **riboswitch-mediated transcription termination** mechanism upstream of the kdp operon. (hu2024cdiampaccumulationimpairs pages 6-9)

## 4) Current applications and real-world implementations

Although METPO:1000334 is a phenotype trait rather than an application, NaCl-range mechanisms are directly used in:

1) **Bioprocess design for halophiles (open/unsterile fermentation):** High-salinity growth capability (wide/upper NaCl range) is exploited to reduce contamination risk and enable industrial processes in saline media. Mechanistic understanding emphasizes osmolyte uptake/biosynthesis and ion homeostasis as engineering levers, consistent with the compatible-solute and transporter-centric evidence compiled here. (xing2024thepolyextremophilenatranaerobius pages 6-7, foster2024bacterialcellvolume pages 12-13)

2) **Microbial cultivation and media engineering for halophiles/haloarchaea:** Schneegurt catalogs that many standard culture recipes specify salinity in **%**, including ≥20% media for haloarchaea, and documents a strong lower salt constraint for many haloarchaea (lysis below ~1.5 M NaCl). This is directly relevant for practical strain isolation/maintenance and for how NaCl-range assays should be parameterized. (schneegurt2012mediaandconditions pages 6-9)

## 5) Relevant statistics and data points (recent studies)

**Quantitative NaCl/Na+ range and intracellular osmolytes (2024):**
- *N. thermophilus* grows between **2.5–5.0 M total Na+** (reported as ~14.63%–29.25% Na+, wt/vol) with an **optimal** range **3.1–4.3 M** (~18.14%–25.16% wt/vol). (xing2024thepolyextremophilenatranaerobius pages 6-7)
- Intracellular glycine betaine increases from **~52.7 mM → ~893.1 mM** across 2.5 → 4.3 M Na+. (xing2024thepolyextremophilenatranaerobius pages 17-19)
- Intracellular glutamate increases up to **~221.3 mM** at 4.3 M Na+. (xing2024thepolyextremophilenatranaerobius pages 17-19)
- Media composition can measurably contribute osmolytes: yeast extract in the *N. thermophilus* medium contained glycine betaine contributing **~52 mg/L** in the culture medium (important for interpreting transporter edges and reproducibility of NaCl-range results). (xing2024thepolyextremophilenatranaerobius pages 17-19)

**Lower-bound constraint example (2012 synthesis):**
- For halophilic archaea, Schneegurt reports a typical lower bound: “**require NaCl of at least 1.5 M**” and “**cell lysis occurred below 1.5 M**” in low NaCl, emphasizing that for some taxa NaCl range is constrained by structural integrity rather than only growth rate reduction. (schneegurt2012mediaandconditions pages 6-9)

**Salt-stress sensitivity via regulatory perturbation (2024):**
- In *B. anthracis*, c-di-AMP-accumulating mutants show **growth impairment at mild salt**, and K+ uptake-related components partially rescue growth at **2.5% NaCl**, linking second messenger level to salt tolerance. (hu2024cdiampaccumulationimpairs pages 2-6)

## 6) Candidate causal-graph nodes (grouped by type; ontology grounding suggestions)

### 6.1 Phenotype / trait nodes
- **NaCl range** (METPO:1000334)
- Label-only: *minimum NaCl concentration supporting growth*, *maximum NaCl concentration supporting growth* (subcomponents of NaCl range)

### 6.2 Environmental / assay factor nodes
- **NaCl concentration reporting**: label-only nodes for “M NaCl”, “% (w/v)”, “% total salts”, “ppt”, because these are not equivalent without composition conversion (Schneegurt). (schneegurt2012mediaandconditions pages 6-9)
- **Water activity** (label-only: aw) as an orthogonal constraint; often manipulated by salts/sugars. (bartha2022investigatingextremotolerantmicrobes pages 21-25)
- **Media osmolyte content**: e.g., yeast extract-derived glycine betaine in medium. (xing2024thepolyextremophilenatranaerobius pages 17-19)

### 6.3 Chemical / metabolite nodes (CHEBI)
- Sodium(1+) **Na+** (CHEBI:29101)
- Sodium chloride **NaCl** (CHEBI:26710)
- Potassium(1+) **K+** (CHEBI:29103)
- Chloride **Cl−** (CHEBI:17996)
- **Glycine betaine** (CHEBI:17750)
- **L-glutamate** (CHEBI:29985)
- **L-proline** (CHEBI:26271)
- **c-di-AMP** (CHEBI:191516)

### 6.4 Genes / proteins / complexes (label-only unless curated to UniProt/KEGG/GO later)
- **TrkA/TrkH** potassium uptake system (K+ uptake) (xing2024thepolyextremophilenatranaerobius pages 6-7)
- **Ktr/Kdp** potassium uptake systems (regulated by c-di-AMP; Kdp riboswitch control) (hu2024cdiampaccumulationimpairs pages 6-9, foster2024bacterialcellvolume pages 6-8)
- **KimA/Kup** high-affinity potassium transporters (review-level) (foster2024bacterialcellvolume pages 8-10)
- **Na+/H+ antiporter NhaC** (xing2024thepolyextremophilenatranaerobius pages 6-7)
- **Opu/ProU** glycine betaine/proline ABC transporters (xing2024thepolyextremophilenatranaerobius pages 17-19)
- **PutP** Na+/proline symporter (xing2024thepolyextremophilenatranaerobius pages 17-19)
- **ydaO riboswitch** upstream of kdp operon (hu2024cdiampaccumulationimpairs pages 6-9)

### 6.5 Biological processes / functions (GO candidates)
- Response to osmotic stress (GO:0006970; candidate)
- Potassium ion transport (GO:0006813)
- Sodium:proton antiporter activity (GO:0015385; candidate)
- ATPase-coupled organic osmolyte transport (GO:0015419; candidate)

## 7) Evidence-backed candidate edges (curation table)

The following table is designed for direct translation into a TraitMech/TraitGraph YAML (subject–predicate–object), with evidence snippets, DOI-first references, and curation caveats.

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet (verbatim short quote) | Source | DOI | URL | Publication date | Notes |
|---|---|---|---|---|---|---|---|---|
| Extracellular Na+ concentration / salinity (CHEBI:26710 sodium cation; label-only: external salinity) | increases | intracellular glycine betaine concentration (CHEBI:17750) | "intracellular glycine betaine measured 52.7, 279.7, 448.0, and 893.1 mM across 2.5–4.3 M Na+" (xing2024thepolyextremophilenatranaerobius pages 17-19) | Xing et al., 2024, *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+* | 10.1128/AEM.00145-24 | https://doi.org/10.1128/AEM.00145-24 | May 2024 | Strong but taxon-specific; direct quantitative support for compatible-solute accumulation as Na+ rises in *N. thermophilus*. |
| Extracellular Na+ concentration / salinity (CHEBI:26710; label-only: external salinity) | increases | intracellular L-glutamate concentration (CHEBI:29985) | "Glutamate is a second major compatible solute (11.0–221.3 mM across 2.5–4.3 M Na+)" (xing2024thepolyextremophilenatranaerobius pages 17-19) | Xing et al., 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.00145-24 | https://doi.org/10.1128/AEM.00145-24 | May 2024 | Strong but taxon-specific; supports glutamate as an osmoadaptive solute affecting upper NaCl tolerance. |
| Extracellular Na+ concentration / salinity (CHEBI:26710; label-only: external salinity) | modulates | intracellular L-proline concentration (CHEBI:26271) | "proline varied (67.0–130 mM)" (xing2024thepolyextremophilenatranaerobius pages 17-19) | Xing et al., 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.00145-24 | https://doi.org/10.1128/AEM.00145-24 | May 2024 | Moderate support; direction is not strictly monotonic in snippet, so curate as uncertain/modulates rather than increases. |
| Glycine betaine ABC transporters Opu/ProU family (GO:0015419 ATPase-coupled organic osmolyte transmembrane transporter activity; label-only: OpuA/OpuB/ProU) | promote accumulation of | glycine betaine (CHEBI:17750) | "ABC-type glycine betaine transporters are implicated in uptake" (xing2024thepolyextremophilenatranaerobius pages 17-19) | Xing et al., 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.00145-24 | https://doi.org/10.1128/AEM.00145-24 | May 2024 | Good mechanistic candidate; taxon-specific and partly inferred from transporter annotation/expression plus intracellular measurements. |
| PutP Na+/proline symporter (label-only: PutP; GO:0015191 L-proline transmembrane transporter activity candidate) | contributes to | proline uptake / osmoadaptation (CHEBI:26271 L-proline; GO:0006970 response to osmotic stress) | "The Na+/proline symporter PutP is differentially regulated (up at 3.1 M)." (xing2024thepolyextremophilenatranaerobius pages 17-19) | Xing et al., 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.00145-24 | https://doi.org/10.1128/AEM.00145-24 | May 2024 | Useful edge but uncertain because the snippet shows regulation, not direct flux measurement; taxon-specific. |
| TrkA/TrkH potassium uptake system (label-only: TrkA/TrkH; GO:0006813 potassium ion transport) | promotes | intracellular K+ accumulation (CHEBI:29103 potassium(1+)) | "Proteomic data list K+ uptake systems (TrkA/TrkH)" (xing2024thepolyextremophilenatranaerobius pages 6-7) | Xing et al., 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.00145-24 | https://doi.org/10.1128/AEM.00145-24 | May 2024 | Candidate edge supported by transporter presence in a study showing rising intracellular K+ with salinity; causal link is mechanistically standard but not directly knocked out here, so mark inferred/taxon-specific. |
| NhaC Na+/H+ antiporter (label-only: NhaC; GO:0015385 sodium:proton antiporter activity candidate) | promotes | Na+ efflux / ion homeostasis under salt stress (CHEBI:29101 sodium(1+); GO:0055085 transmembrane transport) | "multiple Na+/H+ antiporters (NhaC entries) are present and some are upregulated at higher salinities" (xing2024thepolyextremophilenatranaerobius pages 6-7) | Xing et al., 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.00145-24 | https://doi.org/10.1128/AEM.00145-24 | May 2024 | Good candidate but inferred from annotation/expression; direct Na+ efflux not measured in provided snippet. |
| Compatible-solute accumulation (GO:0015891 compatible solute transport; label-only: osmolyte accumulation) | broadens | NaCl growth range (METPO:1000334) | "supporting a dual strategy of K+ accumulation plus compatible solute uptake/accumulation" (xing2024thepolyextremophilenatranaerobius pages 6-7) | Xing et al., 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.00145-24 | https://doi.org/10.1128/AEM.00145-24 | May 2024 | Higher-level phenotype edge; useful summary edge, but should be marked inferred from correlative multi-omics and growth-range data. |
| K+ accumulation / salt-in component (CHEBI:29103; label-only: salt-in osmoadaptation) | supports growth at | high Na+ / upper NaCl limit (METPO:1000334) | "The organism uses a dual strategy—accumulating compatible solutes and K+" (xing2024thepolyextremophilenatranaerobius pages 17-19) | Xing et al., 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.00145-24 | https://doi.org/10.1128/AEM.00145-24 | May 2024 | Strong organism-level support, but mechanistic edge to NaCl-range breadth remains inferred unless paired with perturbation data. |
| c-di-AMP (CHEBI:191516 cyclic di-AMP) | inhibits | Trk/Ktr potassium influx systems (label-only: TrkAH/KtrAB/KtrCD) | "low-affinity potassium import systems TrkAH, KtrAB and KtrCD have gating subunits that bind c-di-AMP" and this binding "inhibiting potassium influx" (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10) | Foster et al., 2024, *Bacterial cell volume regulation and the importance of cyclic di-AMP* | 10.1128/MMBR.00181-23 | https://doi.org/10.1128/MMBR.00181-23 | Jun 2024 | Broad, high-authority review support; mechanistically strong across multiple bacteria, not specific to one taxon. |
| c-di-AMP (CHEBI:191516) | inhibits | KimA/Kup high-affinity K+ uptake transporters (label-only: KimA, KupA/KupB) | "High-affinity transporters (KimA, KupA/KupB) are inhibited directly by cyclic di-AMP" (foster2024bacterialcellvolume pages 8-10) | Foster et al., 2024, *MMBR* | 10.1128/MMBR.00181-23 | https://doi.org/10.1128/MMBR.00181-23 | Jun 2024 | Strong review-based edge; relevant to lower/upper NaCl limits through K+ homeostasis, but taxon distribution varies. |
| c-di-AMP (CHEBI:191516) | inhibits | Kdp system transcription / KdpFABC expression (label-only: KdpD/KdpFABC; GO:0006813 potassium ion transport) | "KdpD binding of cyclic di-AMP inhibits kdpFABC transcription" (foster2024bacterialcellvolume pages 8-10) | Foster et al., 2024, *MMBR* | 10.1128/MMBR.00181-23 | https://doi.org/10.1128/MMBR.00181-23 | Jun 2024 | Strong review support; suitable regulatory edge. |
| c-di-AMP (CHEBI:191516) | binds and regulates | OpuA-like compatible-solute importers (label-only: OpuAA/OpuCA; GO:0015419) | "It binds OpuA-like ABC compatible-solute importers" (foster2024bacterialcellvolume pages 12-13) | Foster et al., 2024, *MMBR* | 10.1128/MMBR.00181-23 | https://doi.org/10.1128/MMBR.00181-23 | Jun 2024 | Strong review-level evidence for regulatory linkage; effect direction on transport may be context-dependent, so avoid over-specifying activation/inhibition unless a primary source is added. |
| Elevated c-di-AMP (CHEBI:191516) | causes | salt sensitivity / narrower NaCl tolerance (METPO:1000334) | "high cyclic di-AMP levels correlate with salt sensitivity" (foster2024bacterialcellvolume pages 8-10) | Foster et al., 2024, *MMBR* | 10.1128/MMBR.00181-23 | https://doi.org/10.1128/MMBR.00181-23 | Jun 2024 | High-value phenotype edge, but broad and synthesized from multiple organisms; curate as review-supported, not one-organism direct. |
| c-di-AMP (CHEBI:191516) | represses | kdp operon transcripts via ydaO riboswitch (label-only: ydaO riboswitch, KdpFABC) | "c-di-AMP represses kdp transcription by promoting transcriptional termination at this riboswitch" (hu2024cdiampaccumulationimpairs pages 6-9) | Hu et al., 2024, *c-di-AMP accumulation impairs toxin expression of Bacillus anthracis by down-regulating potassium importers* | 10.1128/SPECTRUM.03786-23 | https://doi.org/10.1128/SPECTRUM.03786-23 | Aug 2024 | Strong primary evidence; taxon-specific to *B. anthracis* but mechanistically precise. |
| c-di-AMP accumulation (CHEBI:191516) | inhibits | KtrCB/CD and KdpFABC-mediated K+ uptake (label-only: KtrCB/CD, KdpFABC) | "co-production of a diadenylate cyclase (CdaA) inhibited growth when KtrCB/D or KdpFABC/D were expressed" (hu2024cdiampaccumulationimpairs pages 2-6) | Hu et al., 2024, *Microbiology Spectrum* | 10.1128/SPECTRUM.03786-23 | https://doi.org/10.1128/SPECTRUM.03786-23 | Aug 2024 | Strong functional evidence using heterologous/physiological assays; taxon-specific but highly relevant for causal graph regulation branch. |
| Reduced K+ uptake (label-only: low intracellular K+) | decreases tolerance to | NaCl stress / growth at elevated NaCl (METPO:1000334) | "ΔΔPDE mutants with accumulated c-di-AMP could not grow at mild salt concentrations" and "KtrC and KdpD partially rescued growth at 2.5% NaCl" (hu2024cdiampaccumulationimpairs pages 2-6) | Hu et al., 2024, *Microbiology Spectrum* | 10.1128/SPECTRUM.03786-23 | https://doi.org/10.1128/SPECTRUM.03786-23 | Aug 2024 | Strong edge for phenotype impact, but assay-specific (2.5% NaCl) and *B. anthracis*-specific. |
| Salt-in strategy (label-only: intracellular KCl accumulation) | requires | intracellular accumulation of K+ and Cl- (CHEBI:29103, CHEBI:17996) | "the 'salt-in' strategy (accumulation of inorganic ions, mainly K+ and Cl- at ~4.5 M KCl, coupled with Na+ exclusion)" (bartha2022investigatingextremotolerantmicrobes pages 21-25) | Bartha, 2022, *Investigating extremotolerant microbes in non-extreme environments and altering the salinity growth limits of halophiles* | n/a | n/a | 2022 | Background/mechanism edge; useful but from a less authoritative source and may need confirmation from a peer-reviewed primary/review before hard curation. |
| Compatible-solute / salt-out strategy (label-only: compatible-solute accumulation) | uses | organic osmolytes instead of high intracellular salt (label-only: glycerol, proline, ectoine, betaine) | "the 'compatible-solute' strategy" and "glycerol cited as an example" (bartha2022investigatingextremotolerantmicrobes pages 21-25) | Bartha, 2022, *Investigating extremotolerant microbes...* | n/a | n/a | 2022 | General mechanism edge; useful for scope framing, but weak for specific node grounding unless supported by stronger literature. |
| Water activity (label-only: aw) | constrains | microbial growth across salinity conditions (ENVO:saline environment candidate; METPO:1000334) | "Water activity (aw) is the ratio..." with "common microbial thresholds" and that aw is "commonly manipulated by adjusting salt/sugar concentrations in media" (bartha2022investigatingextremotolerantmicrobes pages 21-25) | Bartha, 2022, *Investigating extremotolerant microbes...* | n/a | n/a | 2022 | Assay/environment factor edge; important for phenotype interpretation, but indirect with respect to NaCl-specific mechanism. |
| NaCl concentration reporting units (label-only: M NaCl, % salinity) | determine assay comparability of | NaCl growth range observations (METPO:1000334) | "many ATCC recipes report salinity as percent" and "Molar NaCl concentrations are used in physiological studies" (schneegurt2012mediaandconditions pages 6-9) | Schneegurt, 2012, *Media and conditions for the growth of halophilic and halotolerant bacteria and archaea* | 10.1007/978-94-007-5539-0_2 | https://doi.org/10.1007/978-94-007-5539-0_2 | Jan 2012 | Assay/reporting edge rather than biological mechanism; important curation warning because percent salts, total salts, and molar NaCl are not interchangeable. |
| NaCl below organism-specific minimum (CHEBI:26710 sodium chloride) | causes | growth failure / lysis in extreme halophiles (label-only: lower NaCl limit) | "halophilic archaea generally require NaCl of at least 1.5 M" and "significant cell lysis occurred below 1.5 M" (schneegurt2012mediaandconditions pages 6-9) | Schneegurt, 2012, *Media and conditions for the growth of halophilic and halotolerant bacteria and archaea* | 10.1007/978-94-007-5539-0_2 | https://doi.org/10.1007/978-94-007-5539-0_2 | Jan 2012 | Strong for scope/boundary of obligate halophiles; not universal across all microbes, so curate as clade-specific/background. |


*Table: This table compiles candidate causal edges for the microbial trait NaCl range, linking ion homeostasis, compatible solutes, regulatory systems, and assay factors to minimum/maximum salt-supported growth. It is designed to support TraitMech curation by pairing each proposed edge with a short evidence snippet, source metadata, and caveats about taxon specificity or uncertainty.*

### Visual evidence (quantitative trend)
Figure evidence for salinity-dependent intracellular osmolytes and K+ in *N. thermophilus* (hybrid strategy; direct relevance to upper-range mechanisms): (xing2024thepolyextremophilenatranaerobius media 35b012bf)

## 8) Warnings / claims to treat as uncertain before curation

1) **Unit harmonization is mandatory:** “% salinity”, “% total salts”, “M NaCl”, “M total Na+”, and “ppt” can refer to different chemical realities; Schneegurt explicitly notes frequent use of **percent salinity in media recipes** versus molar NaCl in physiological studies, so edges that connect “external NaCl” to phenotypes should only be curated when the unit/definition is explicit or normalized. (schneegurt2012mediaandconditions pages 6-9)

2) **Media composition confounds mechanistic interpretation:** In *N. thermophilus*, yeast extract contributes measurable glycine betaine to the medium; therefore, edges involving “glycine betaine uptake → tolerance” can be assay-dependent (availability of exogenous osmolyte). (xing2024thepolyextremophilenatranaerobius pages 17-19)

3) **Transporter expression ≠ causal necessity:** Several edges in the artifact infer function from transporter presence/differential regulation rather than genetic necessity; these should be marked **inferred/taxon-specific** unless supported by knockout/transport assays in the same organism. (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 17-19)

4) **Salt-in vs salt-out generalities:** General descriptions of strategies (and example intracellular KCl values) are useful for scope, but some of this comes from a less authoritative source in the current evidence set; for permanent curation of quantitative claims (e.g., exact intracellular KCl levels), prefer peer-reviewed reviews/primaries. (bartha2022investigatingextremotolerantmicrobes pages 21-25)

## 9) DOI-first bibliography (with URLs and publication dates)

1) **Xing Q, Zhang S, Tao X, et al.** *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.* **Applied and Environmental Microbiology**. **May 2024**. DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius media 35b012bf)

2) **Foster AJ, van den Noort M, Poolman B.** *Bacterial cell volume regulation and the importance of cyclic di-AMP.* **Microbiology and Molecular Biology Reviews**. **Jun 2024**. DOI: **10.1128/mmbr.00181-23**. URL: https://doi.org/10.1128/mmbr.00181-23 (foster2024bacterialcellvolume pages 12-13, foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 6-8)

3) **Hu J, Yao J, Lei C, Sun X.** *c-di-AMP accumulation impairs toxin expression of Bacillus anthracis by down-regulating potassium importers.* **Microbiology Spectrum**. **Aug 2024**. DOI: **10.1128/spectrum.03786-23**. URL: https://doi.org/10.1128/spectrum.03786-23 (hu2024cdiampaccumulationimpairs pages 2-6, hu2024cdiampaccumulationimpairs pages 6-9)

4) **Schneegurt MA.** *Media and conditions for the growth of halophilic and halotolerant bacteria and archaea.* (Book chapter; accessed as text). **Jan 2012**. DOI: **10.1007/978-94-007-5539-0_2**. URL: https://doi.org/10.1007/978-94-007-5539-0_2 (schneegurt2012mediaandconditions pages 6-9)

5) **Bartha E.** *Investigating extremotolerant microbes in non-extreme environments and altering the salinity growth limits of halophiles.* **2022**. (No DOI in retrieved text.) (bartha2022investigatingextremotolerantmicrobes pages 21-25)


References

1. (xing2024thepolyextremophilenatranaerobius pages 6-7): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

2. (schneegurt2012mediaandconditions pages 6-9): Mark A. Schneegurt. Media and conditions for the growth of halophilic and halotolerant bacteria and archaea. ArXiv, pages 35-58, Jan 2012. URL: https://doi.org/10.1007/978-94-007-5539-0\_2, doi:10.1007/978-94-007-5539-0\_2. This article has 106 citations.

3. (bartha2022investigatingextremotolerantmicrobes pages 21-25): E Bartha. Investigating extremotolerant microbes in non-extreme environments and altering the salinity growth limits of halophiles. Unknown journal, 2022.

4. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

5. (foster2024bacterialcellvolume pages 8-10): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

6. (foster2024bacterialcellvolume pages 6-8): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

7. (foster2024bacterialcellvolume pages 12-13): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

8. (hu2024cdiampaccumulationimpairs pages 2-6): Jia Hu, Junmin Yao, Chengfeng Lei, and Xiulian Sun. C-di-amp accumulation impairs toxin expression of <i>bacillus anthracis</i> by down-regulating potassium importers. Aug 2024. URL: https://doi.org/10.1128/spectrum.03786-23, doi:10.1128/spectrum.03786-23. This article has 4 citations and is from a domain leading peer-reviewed journal.

9. (hu2024cdiampaccumulationimpairs pages 6-9): Jia Hu, Junmin Yao, Chengfeng Lei, and Xiulian Sun. C-di-amp accumulation impairs toxin expression of <i>bacillus anthracis</i> by down-regulating potassium importers. Aug 2024. URL: https://doi.org/10.1128/spectrum.03786-23, doi:10.1128/spectrum.03786-23. This article has 4 citations and is from a domain leading peer-reviewed journal.

10. (xing2024thepolyextremophilenatranaerobius media 35b012bf): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.