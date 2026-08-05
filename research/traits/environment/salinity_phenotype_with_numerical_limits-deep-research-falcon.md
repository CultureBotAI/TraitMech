---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:18:09.064692'
end_time: '2026-08-04T03:31:41.721813'
duration_seconds: 812.66
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: salinity phenotype with numerical limits
  trait_identifier: METPO:1000532
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: salinity_phenotype_with_numerical_limits
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by specific salt concentration values or ranges
    that define growth or activity limits.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports quantitative salinity descriptors (optimum, range, delta) as the standard
    numerical phenotype framing for halophily classification.) | DOI:10.1093/femsre/fuy009:
    Hypersaline environments (Osmoadaptation review supports salinity as the physical
    axis underlying halophily classifications.)'
  causal_graph_summary: 'salinity_phenotype_numerical_axis: 13 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 51
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** salinity phenotype with numerical limits
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000532
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific salt concentration values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports quantitative salinity descriptors (optimum, range, delta) as the standard numerical phenotype framing for halophily classification.) | DOI:10.1093/femsre/fuy009: Hypersaline environments (Osmoadaptation review supports salinity as the physical axis underlying halophily classifications.)
- **Existing causal graph summary:** salinity_phenotype_numerical_axis: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **salinity phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/salinity_phenotype_with_numerical_limits.yaml`.

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
- **Trait label:** salinity phenotype with numerical limits
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000532
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific salt concentration values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports quantitative salinity descriptors (optimum, range, delta) as the standard numerical phenotype framing for halophily classification.) | DOI:10.1093/femsre/fuy009: Hypersaline environments (Osmoadaptation review supports salinity as the physical axis underlying halophily classifications.)
- **Existing causal graph summary:** salinity_phenotype_numerical_axis: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **salinity phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/salinity_phenotype_with_numerical_limits.yaml`.

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


# Curation report: microbial salinity phenotype with numerical limits

## 1. Trait scope

**Trait:** salinity phenotype with numerical limits  
**Identifier:** **METPO:1000532**  
**Parent:** METPO:1000059  
**Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED

### Operational interpretation

This trait should represent an **assay-observed numerical interval or point describing microbial growth or activity as a function of salt concentration**. Curatable forms include:

- minimum salt concentration supporting growth or activity;
- optimum concentration or optimum interval;
- maximum concentration supporting growth or activity;
- complete tested growth/activity range; and
- a perturbation-induced shift in one of these values.

A measurement should preserve: organism and strain; salt identity and composition; concentration and units; medium; temperature; pH; oxygen regime; inoculum and incubation time; endpoint such as growth rate, yield, colony formation, or metabolic activity; and whether the value is observed or merely bounded by the highest concentration tested. For example, *Natranaerobius thermophilus* was tested from 2.5–5.0 M Na⁺ and grew optimally over approximately 3.1–4.3 M in the reported experiment, while its reported growth range was 3.1–4.9 M Na⁺. These values are conditional on its alkaline and thermophilic assay context rather than intrinsic, context-free constants. (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 7-10)

### Boundary cases

1. **Qualitative halophile/halotolerant classifications are not themselves this trait.** They may summarize a numerical range but should not replace the underlying values.
2. **Environmental occurrence is not a growth limit.** Detection or relative abundance in a saline sample supports ecological association, not an isolate’s minimum, optimum, or maximum.
3. **NaCl concentration is not interchangeable with salinity, osmolality, ionic strength, or water activity.** NaCl-saturated brine at 5 M has water activity near 0.755, yet some bacteria and archaea grow optimally there; MgCl₂-rich and other chaotropic brines can be much more inhibitory at superficially comparable salinity. Ion composition, temperature, pH, and chaotropicity must therefore remain assay qualifiers. (lee2018naclsaturatedbrinesare pages 1-3)
4. **Growth under sustained high salt differs from transient salt-upshock response.** Transcript or protein induction alone does not establish a shifted numerical growth limit.
5. **Hypoosmotic downshock survival is adjacent but distinct.** MscL/MscS channels protect cells when salinity falls rapidly; they should not be asserted to increase a sustained high-salt growth maximum without separate evidence. (bialeckafornal2015therateof pages 1-2)
6. **“Survival” and “growth” must not be conflated.** Persistence without biomass increase is an activity/survival phenotype and requires its own endpoint.

## 2. Current mechanistic model

The present consensus is not a strict binary between “salt-in” and “salt-out.” Cells can use a continuum or hybrid strategy:

- external salinity lowers water availability and creates an osmotic gradient;
- rapid K⁺ uptake restores turgor and ionic balance;
- Na⁺ extrusion and pH regulation constrain cytoplasmic Na⁺ toxicity;
- compatible solute synthesis or import supplies less perturbing osmolytes;
- long-term salt-in organisms adapt their proteomes to high intracellular ionic strength; and
- downshock opens mechanosensitive channels to release solutes and prevent lysis.

Recent work is particularly important because it demonstrates hybrid strategies rather than assuming mutually exclusive categories. In *N. thermophilus*, quantitative multi-omics across 2.5, 3.1, 3.7, and 4.3 M Na⁺ supported simultaneous compatible-solute accumulation and K⁺-based ion homeostasis. The organism showed increased glycine betaine, glutamate, and proline; use of Opu/ProU and solute symport systems; upregulated Na⁺/K⁺/H⁺ transport; and decreasing median isoelectric points among upregulated proteins as salinity rose. (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 10-14, xing2024thepolyextremophilenatranaerobius pages 7-10)

## 3. Candidate graph nodes

The following table supplies candidate environmental, molecular, process, and protein-property nodes. Stable CURIEs are proposed only where grounding is sufficiently clear; gene-family nodes remain label-level candidates when an exact ontology term was not verified.

| Entity Type | Label | Suggested CURIE | Role | Evidence Summary |
|---|---|---|---|---|
| Environmental factor | NaCl concentration | CHEBI:26710 | Primary assay variable used to define numerical salinity growth/activity limits; should be recorded with units (mM, M, % w/v) and medium context. | Experimental phenotyping used defined NaCl ranges such as 2.5–5.0 M Na+ for *Natranaerobius thermophilus*, 100–400 mM NaCl for *Clostridioides difficile*, 300–500 mM NaCl for engineered *Synechococcus*, and 0.3–21% NaCl range for *Halomonas elongata* background strain descriptions (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 7-10, michel2022cellularadaptationof pages 2-3, dong2023improvedsalttolerance pages 1-2, khanh2024metabolicpathwayengineering pages 1-2). |
| Environmental factor | Osmolality / water activity | no stable single CURIE; label candidate | Thermodynamic descriptor that modulates salinity phenotype beyond NaCl concentration alone; useful boundary-case node to distinguish salt concentration from biological permissiveness. | Reviews emphasize that water activity, not NaCl alone, constrains habitability; NaCl-saturated brines have aw ~0.755 at 5 M NaCl, yet some halophiles grow optimally there, showing ion composition and other stresses matter (lee2018naclsaturatedbrinesare pages 1-3). |
| Environmental factor | Salinity stress | GO:0009651 | Generic external high-salt condition triggering osmoadaptation pathways and transport responses. | Recent experimental and omics studies frame increased external salinity as the upstream driver of K+ uptake, compatible-solute accumulation, antiporter activity, and proteome remodeling (xing2024thepolyextremophilenatranaerobius pages 1-2, pricewhelan2013transcriptionalprofilingof pages 1-2, xing2024thepolyextremophilenatranaerobius pages 23-24). |
| Cellular process | Ion homeostasis | GO:0055080 | Maintenance of intracellular Na+/K+ balance under elevated salinity; core intermediate between environmental salt and growth tolerance. | Xing 2024 explicitly links Na+/K+/H+ transporters to intracellular K+ homeostasis under rising salinity; *S. aureus* and *E. faecalis* studies tie K+ transport status to growth under NaCl stress (xing2024thepolyextremophilenatranaerobius pages 1-2, pricewhelan2013transcriptionalprofilingof pages 1-2, acciarri2023redundantpotassiumtransporter pages 1-2). |
| Cellular process | Compatible solute biosynthesis | GO:0006970 (broad osmotic stress response; pathway-specific IDs vary) | De novo production of osmoprotective solutes such as ectoine, proline, glutamate, and trehalose that raise cytoplasmic osmotic potential without major macromolecular disruption. | Engineered ectoine synthesis improved cyanobacterial salt tolerance; engineered proline synthesis rescued growth of ectoine-deficient *H. elongata* at high salt; *N. thermophilus* increased glutamate/proline-associated functions with salinity (dong2023improvedsalttolerance pages 1-2, khanh2024metabolicpathwayengineering pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2). |
| Cellular process | Compatible solute uptake | GO:1901700 (response to osmotic stress, broad); transporter-specific grounding preferred | Import of exogenous osmoprotectants such as glycine betaine and related solutes to rapidly relieve osmotic stress. | *C. difficile* relied on OpuF-mediated compatible-solute import under high salinity; *N. thermophilus* used Opu/ProU family transporters and Na+/solute symporters in its dual strategy (michel2022cellularadaptationof pages 2-2, xing2024thepolyextremophilenatranaerobius pages 1-2). |
| Cellular process | Osmotic stress response | GO:0006970 | Parent stress-response process encompassing K+ influx, solute accumulation, transcriptional remodeling, and envelope/cell-shape changes. | Multiple studies explicitly discuss osmotic upshift responses and salt adaptation, including *S. aureus* transcriptional remodeling in 2 M NaCl and *C. difficile* morphology/metabolism changes at 350–400 mM NaCl (pricewhelan2013transcriptionalprofilingof pages 1-2, michel2022cellularadaptationof pages 2-3). |
| Cellular process | Cytoplasmic acidification | label candidate | Proposed intracellular physicochemical adjustment associated with high-salt adaptation, especially in extreme halophiles and polyextremophiles. | Xing 2024 reports cytoplasmic acidification and decreasing median pI of upregulated proteins with increasing salinity in *N. thermophilus*; acidic proteomes are also a hallmark of salt-in strategists in hypersaline systems (xing2024thepolyextremophilenatranaerobius pages 1-2, matarredona2020theroleof pages 3-4). |
| Transporter/enzyme | Trk/Ktr/Kdp potassium uptake systems | Trk/Ktr/Kdp family (label-level grounding) | Mediate K+ accumulation during osmotic upshift; major causal candidates linking salinity increase to salt-in response and improved tolerance. | Wu 2024 identified COG0168 (Trk-type K+ transporter) as the strongest salinity-associated feature across estuarine MAGs; *S. aureus* ktrC disruption caused a significant defect in 2 M NaCl; *H. elongata* mutants lacking Trk systems lost K+ accumulation and required more K+ for growth in highly saline medium (wu2024metagenomicinsightsinto pages 1-2, pricewhelan2013transcriptionalprofilingof pages 1-2, kraegeloh2005potassiumtransportin pages 1-2). |
| Transporter/enzyme | Na+/H+ antiporters (NhaA/NhaB/NhaD) | NhaA/NhaB/NhaD family (label-level grounding) | Export Na+ and contribute to pH/Na+ homeostasis under saline conditions, especially in salt-in or mixed strategies. | *Vibrio cholerae* nhaA/nhaB/nhaD genetics showed antiporter-dependent Na+ resistance under some conditions and essentiality of Vc-NhaA when NQR was inhibited at alkaline pH; metagenomic hypersaline studies also recurrently recover Na+/H+ antiporter genes (herz2003rolesofnhaa pages 1-2, wu2024metagenomicinsightsinto pages 1-2, xamxidin2025metagenomicsassembledgenomesreveal pages 11-12). |
| Transporter/enzyme | Opu/ProU/BetL compatible-solute importers | Opu/ProU/BetL family (label-level grounding) | Import glycine betaine and related osmoprotectants; typically support rapid osmoprotection and extend growth at higher salinity. | *N. thermophilus* used Opu and ProU family ABC transporters; *C. difficile* required an OpuF-type system for major immediate adaptation to high salinity; classic BetL/Opu systems are repeatedly implicated in osmotolerance literature (xing2024thepolyextremophilenatranaerobius pages 1-2, michel2022cellularadaptationof pages 2-2). |
| Transporter/enzyme | Mechanosensitive channels (MscL/MscS) | MscL/MscS family (label-level grounding) | Emergency release valves during hypoosmotic downshock; relevant boundary-case nodes for fluctuating salinity environments rather than direct high-salt growth enhancement. | Experiments show MscL/MscS support survival after osmotic downshock, distinguishing downshock survival from high-salt growth phenotype; should be curated carefully as a boundary mechanism unless fluctuating-salinity context is explicit (bialeckafornal2015therateof pages 1-2). |
| Transporter/enzyme | EctABC pathway enzymes | ectA / ectB / ectC (gene labels); EC IDs vary by step | Biosynthesis of ectoine, a canonical compatible solute that can raise salt tolerance when present or engineered into non-halophiles. | Dong 2023 expressed codon-optimized ectABC from *Halomonas elongata* in *Synechococcus* and increased final OD under 300–400 mM NaCl, with survival at 500 mM NaCl where WT was lethal; Qiao 2024 also analyzed ectABC-linked regulation in *Halomonas campaniensis* under NaCl induction (dong2023improvedsalttolerance pages 1-2). |
| Transporter/enzyme | ProBAC pathway enzymes | proB / proA / proC | Biosynthesis of L-proline as an organic osmolyte; can substitute for ectoine in some engineered strains. | In *H. elongata*, replacement of ectABC with proBm1AC plus ΔputA enabled growth at 8% NaCl, whereas the ectoine-deficient parent could not grow above 4% NaCl, directly supporting proline biosynthesis as a causal determinant of high-salt tolerance (khanh2024metabolicpathwayengineering pages 1-2). |
| Metabolite | Glycine betaine | CHEBI:17750 | Widely used compatible solute imported or accumulated for osmoprotection in salt-out and hybrid strategies. | *N. thermophilus* accumulated glycine betaine with increasing salinity and used Opu/ProU transporters; compatible-solute import is central to *C. difficile* high-salt adaptation (xing2024thepolyextremophilenatranaerobius pages 1-2, michel2022cellularadaptationof pages 2-2). |
| Metabolite | Ectoine | CHEBI:28885 | Canonical compatible solute that enhances salt tolerance when synthesized or accumulated. | Heterologous ectoine synthesis increased *Synechococcus* salt tolerance and restored a sucrose-deficient strain under 300 mM NaCl; ectoine is also a native osmolyte in *Halomonas* species (dong2023improvedsalttolerance pages 1-2, khanh2024metabolicpathwayengineering pages 1-2). |
| Metabolite | 5-hydroxyectoine | CHEBI:58199 | Hydroxylated derivative of ectoine associated with osmoprotection in some halophiles. | Recent and metagenomic studies list 5-hydroxyectoine/ectD among compatible-solute systems in saline habitats; evidence for direct contribution to this exact trait is weaker than for ectoine and glycine betaine (xamxidin2025metagenomicsassembledgenomesreveal pages 11-12). |
| Metabolite | L-proline | CHEBI:17203 | Organic osmolyte that can function as a major compatible solute under high salinity. | Engineered proline overproduction allowed ectoine-deficient *H. elongata* to grow at 8% NaCl; *N. thermophilus* increased intracellular proline with salinity; *C. difficile* long-term adaptation involved L-proline accumulation (khanh2024metabolicpathwayengineering pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2, michel2022cellularadaptationof pages 2-2). |
| Metabolite | L-glutamate | CHEBI:16015 | Early or sustained osmoprotective amino acid and precursor for proline/ectoine-linked osmoadaptation. | Xing 2024 reports increased compatible solutes including glutamate under rising salinity; glutamate is repeatedly described as part of bacterial osmoadaptation and proline biosynthesis precursor (xing2024thepolyextremophilenatranaerobius pages 1-2, khanh2024metabolicpathwayengineering pages 1-2). |
| Metabolite | Trehalose | CHEBI:16589 | Compatible solute used by some bacteria/archaea in salt-out or hybrid strategies. | Metagenomic studies of saline systems recover trehalose-related pathways as salt-out features; evidence here is stronger for association than for direct experimental growth-limit manipulation (xamxidin2025metagenomicsassembledgenomesreveal pages 11-12, ionescu2024extremefluctuationsin pages 1-2). |
| Metabolite | K+ | CHEBI:29103 | Principal cation accumulated in salt-in and hybrid strategies to maintain osmotic balance and support growth under high salinity. | K+ accumulation is central in *N. thermophilus*, haloarchaeal salt-in reviews, Trk/Ktr experimental genetics, and estuarine salinity associations (xing2024thepolyextremophilenatranaerobius pages 1-2, matarredona2020theroleof pages 3-4, kraegeloh2005potassiumtransportin pages 1-2, wu2024metagenomicinsightsinto pages 1-2). |
| Metabolite | Na+ | CHEBI:29101 | External stressor ion and intracellular ion-homeostasis challenge; often expelled or balanced by antiporters while contributing to assay-defined salinity. | Studies quantify salinity using NaCl/Na+ and show responses via Na+/H+ antiport and Na+/K+/H+ transporters; *V. cholerae* antiporter work directly addresses Na+ resistance (herz2003rolesofnhaa pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2, pricewhelan2013transcriptionalprofilingof pages 1-2). |
| Protein property | Acidic proteomes | label candidate | Proteome-level adaptation associated especially with persistent high intracellular KCl in salt-in strategists; may enable protein solubility/function at high salinity. | Haloarchaeal reviews and Danakil metagenomic work describe highly acidic proteomes in organisms thriving at salt-saturating conditions; Xing 2024 observed decreasing pI of upregulated proteins with rising salinity in a bacterium using a hybrid strategy (matarredona2020theroleof pages 3-4, lee2018naclsaturatedbrinesare pages 1-3, xing2024thepolyextremophilenatranaerobius pages 1-2). |


*Table: This table lists candidate nodes for a salinity-phenotype causal graph, grouped across environmental factors, processes, transport systems, metabolites, and proteome properties. It highlights suggested ontology grounding and the strongest available evidence for each node so curators can prioritize which entities are mature enough for TraitMech inclusion.*

### Recommended high-confidence core

For an initial YAML graph, prioritize:

- NaCl concentration — CHEBI:26710;
- Na⁺ — CHEBI:29101;
- K⁺ — CHEBI:29103;
- ectoine — CHEBI:28885;
- glycine betaine — CHEBI:17750;
- L-proline — CHEBI:17203;
- L-glutamate — CHEBI:16015;
- trehalose — CHEBI:16589;
- osmotic stress response — GO:0006970;
- ion homeostasis — GO:0055080;
- *ectA–ectB–ectC*, *proB–proA–proC*, *putA*, *trk/k‌tr/kdp*, *nha*, and *opu/proU* as taxon-qualified gene or family labels pending exact database grounding.

Do not assign one universal UniProt CURIE to a gene family: use the strain-specific protein accession only when the curated edge concerns that exact protein in that strain.

## 4. Evidence-backed candidate causal edges

The table below emphasizes intervention evidence. “Increases” means a demonstrated improvement under the reported assay, not an assumed universal effect across taxa.

| Subject | Predicate | Object | Evidence Snippet | Reference | Taxon | Uncertainty Flags | Notes |
|---|---|---|---|---|---|---|---|
| Salinity stress | upregulates | Trk/Ktr potassium uptake systems | "At higher K+ concentrations, a lower-affinity and more highly expressed type of K+ transporter system, Ktr transporters, was shown to play a significant role in high Na+ tolerance." | 10.1128/mbio.00407-13, Aug 2013 (pricewhelan2013transcriptionalprofilingof pages 1-2) | *Staphylococcus aureus* | Experimentally demonstrated | 2 M NaCl transcriptomics and mutant phenotyping reveal causal role for Ktr in Na+ tolerance |
| High NaCl concentration (3.1-4.3 M) | upregulates | Compatible solute biosynthesis and uptake | "N. thermophilus employs the glycine betaine ABC transporters... and glutamate and proline synthesis pathways to adapt to high salinity. The intracellular content of compatible solutes... increases with rising salinity levels" | 10.1128/aem.00145-24, May 2024 (xing2024thepolyextremophilenatranaerobius pages 1-2) | *Natranaerobius thermophilus* | Experimentally demonstrated | Proteomics and quantification of intracellular metabolites across specific salinity steps |
| Ectoine biosynthesis (*ectABC*) | increases | Salt tolerance limit | "salt tolerance of Synechococcus elongatus PCC 7942 (Syn7942) was significantly improved via expressing the ectoine biosynthetic pathway... the engineered strain could even survive under 500 mM NaCl which was lethal to WT" | 10.3389/fmicb.2023.1123081, Feb 2023 (dong2023improvedsalttolerance pages 1-2) | *Synechococcus elongatus* | Engineered strain | Demonstrates causal sufficiency of ectoine for shifting the numerical NaCl growth limit |
| Proline biosynthesis (*proBm1AC*) | rescues | High-salinity growth (8% NaCl) | "While the Ect-deficient H. elongata KA1 could not grow in minimal media containing more than 4% NaCl, H. elongata HN6 thrived in the medium containing 8% NaCl by accumulating Pro" | 10.1128/aem.01195-24, Sep 2024 (khanh2024metabolicpathwayengineering pages 1-2) | *Halomonas elongata* | Engineered mutant | Replaces native ectoine requirement with engineered proline synthesis to achieve same numerical phenotypic threshold |
| *ktrC* gene disruption | decreases | Growth in 2 M NaCl | "disruption of ktrC resulted in a significant defect in 2 M NaCl, and a ΔktrC ΔkdpA double mutant exhibited both phenotypes." | 10.1128/mbio.00407-13, Aug 2013 (pricewhelan2013transcriptionalprofilingof pages 1-2) | *Staphylococcus aureus* | Experimentally demonstrated | Supports causal necessity of Ktr for the specific 2 M NaCl phenotype |
| Compatible solute import (via OpuF) | restores | Growth at high salinity (350 mM NaCl) | "Addition of the compatible solutes carnitine, glycine-betaine... restored growth... under conditions of high salinity. A bioinformatically-identified OpuF-type ABC-transporter imported most of the used compatible solutes." | 10.1111/1462-2920.15925, Feb 2022 (michel2022cellularadaptationof pages 2-2) | *Clostridioides difficile* | Experimentally demonstrated | 350 mM NaCl was used to test growth restoration and mechanism via OpuF |
| Rising salinity | causes | Cytoplasmic acidification | "N. thermophilus exhibits cytoplasmic acidification in response to high Na+ concentrations. The median isoelectric points of the upregulated proteins decrease with increasing salinity." | 10.1128/aem.00145-24, May 2024 (xing2024thepolyextremophilenatranaerobius pages 1-2) | *Natranaerobius thermophilus* | Proteomic association | Links proteome-level pI adaptation directly to varied quantitative salinity levels |
| MscL/MscS mechanosensitive channels | required for | Hypoosmotic downshock survival | "In E. coli, the native expression of just MscL or MscS is sufficient to provide survival rates of near 100% in a traditional hypo-osmotic shock assay" | 10.1128/jb.02175-14, Jan 2015 (bialeckafornal2015therateof pages 1-2) | *Escherichia coli* | Downshock-specific (boundary case) | Distinguishes response to rapidly dropping salinity (downshock) from growth under continuous high salinity |
| *nhaA* Na+/H+ antiporter deletion | abolishes | Resistance to Na+ at alkaline pH | "in the absence of NQR activity, the Vc-NhaA Na+/H+ antiporter activity becomes essential for the resistance of V. cholerae to Na+ at alkaline pH." | 10.1128/jb.185.4.1236-1244.2003, Feb 2003 (herz2003rolesofnhaa pages 1-2) | *Vibrio cholerae* | Context-specific (requires NQR inhibition) | Highlights that multiple overlapping systems often mask single-gene deletion phenotypes for Na+ tolerance |


*Table: A curation-ready table proposing causal edges for the numerical salinity phenotype graph, supported by specific literature snippets and experimental context.*

### Additional edges suitable for curation

| Subject | Predicate | Object | Evidence and interpretation | Confidence |
|---|---|---|---|---|
| Increased external Na⁺ | induces | compatible-solute and K⁺-homeostasis program | In *N. thermophilus*, intracellular compatible solutes increased with salinity and Na⁺/K⁺/H⁺ transporters were upregulated across defined Na⁺ treatments. This is strong condition-response evidence, though not a knockout test. (xing2024thepolyextremophilenatranaerobius pages 1-2) | Moderate; taxon- and condition-specific |
| *ectABC* expression | increases | final biomass under 300–400 mM NaCl | Engineered *Synechococcus elongatus* had final OD₇₅₀ values 20% above WT at 300 mM and 80% above WT at 400 mM; it survived 500 mM, which was lethal to WT. (dong2023improvedsalttolerance pages 1-2) | High; engineered sufficiency |
| *proBm1AC* expression plus *putA* deletion | increases | maximum demonstrated high-salt growth | The engineered *H. elongata* HN6 accumulated 353.1 ± 40.5 μmol proline/g fresh cells and grew at 8% NaCl, whereas the ectoine-deficient parent could not grow above 4%. (khanh2024metabolicpathwayengineering pages 1-2) | High; composite intervention |
| TrkI/TrkH/TrkA system | enables | K⁺ accumulation in high-salt medium | *H. elongata* lacking both TrkH and TrkI had no detectable K⁺ accumulation; deletion of *trkA* also abolished transport. TrkI was the principal system, with reported Kₘ 1.12 mM versus 3.36 mM for TrkH. (kraegeloh2005potassiumtransportin pages 1-2) | High for K⁺ transport; moderate for the terminal salinity-limit edge |
| *ktrC* | supports | growth at 2 M NaCl | Disruption caused a significant growth defect in *S. aureus* at 2 M NaCl; *kdpA* instead primarily affected low-K⁺ growth, illustrating non-equivalent transporter roles. (pricewhelan2013transcriptionalprofilingof pages 1-2) | High; taxon-specific |
| K⁺ supplementation | rescues | stress-impaired growth of KtrA-defective strains | In *Enterococcus faecalis*, Δ*ktrA* and Δ*kup* Δ*ktrA* strains showed impaired stress growth restored to WT levels by external K⁺. (acciarri2023redundantpotassiumtransporter pages 1-2) | Moderate; reported “stress conditions” require edge-level assay annotation |
| OpuF-mediated compatible-solute import | supports | growth under high salinity | In *C. difficile*, 100–200 mM NaCl had limited growth effects, while 400 mM severely restricted growth; supplied compatible solutes restored growth under high salinity, and OpuF imported most tested solutes. (michel2022cellularadaptationof pages 2-2, michel2022cellularadaptationof pages 2-3) | High for import-mediated protection |
| Rising salinity | associates with | Trk-type transporter abundance | Among 127 estuarine MAGs, eight osmoregulation COGs were selected and COG0168, a Trk-type K⁺ transporter, was the most important salinity-associated feature. (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 17-18) | **Uncertain for causality**; metagenomic association only |
| Rapid salinity decrease | activates | MscL/MscS-mediated solute release and survival | A controlled shift from 0.5 M to 0 M added NaCl tested downshock survival; this is a fluctuation-survival mechanism, not evidence for elevated sustained-salinity growth. (bialeckafornal2015therateof pages 1-2) | High for downshock; out of core trait scope |

## 5. Recent developments, 2023–2024

### Direct numerical phenotype engineering

The strongest recent causal evidence comes from engineered compatible-solute pathways. Ectoine synthesis moved a freshwater cyanobacterium from WT lethality at 500 mM NaCl to survival, while improving biomass at 300–400 mM. This establishes pathway sufficiency and provides a directly curatable shift in the numerical phenotype. (dong2023improvedsalttolerance pages 1-2)

In 2024, replacement of the native ectoine operon with a feedback-resistant proline pathway, combined with deletion of proline catabolism, doubled the demonstrated salt concentration supporting growth of an ectoine-deficient *H. elongata* background from no growth above 4% to growth at 8% NaCl. This result also shows that graph edges should connect alternative osmolyte modules to the phenotype rather than encode ectoine as universally indispensable. (khanh2024metabolicpathwayengineering pages 1-2)

### Hybrid adaptation documented by multi-omics

The *N. thermophilus* study examined triplicate growth conditions, identified 1,489 proteins—52.3% of 2,848 predicted genes—and found 658 differentially expressed proteins across salinities. At 3.1, 3.7, and 4.3 M relative to 2.5 M Na⁺, it reported 415, 365, and 363 differentially expressed proteins, respectively. Transcript–protein agreement was reported for 98.2% of 109 co-upregulated genes. These data support a coordinated hybrid module, but expression changes should be represented as condition-dependent regulatory edges rather than proof that every induced gene raises the upper growth limit. (xing2024thepolyextremophilenatranaerobius pages 10-14, xing2024thepolyextremophilenatranaerobius pages 7-10)

### Natural-gradient genomics

Wu et al. reconstructed 127 MAGs and separated stenohaline from euryhaline distributions. Forty of 12,162 COGs were selected as important features; eight concerned osmoregulation, and COG0168/Trk was ranked highest. This provides a useful candidate-discovery layer, but relative abundance along a gradient can reflect phylogeny, competition, dispersal, nutrients, or covariance with salinity. It should generate **hypothesized edges**, not causal YAML edges, unless paired with isolate phenotyping or perturbation. (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 17-18)

A Dead Sea spring study recovered five bacterial MAGs containing both salt-in and salt-out machinery in an environment fluctuating against a basin of approximately 35% total dissolved salts. The authors explicitly proposed that variable salinity selects scalable hybrid strategies; this remains an ecological hypothesis rather than a measured shift in isolate growth limits. (ionescu2024extremefluctuationsin pages 1-2)

## 6. Applications and real-world relevance

### Saline biomanufacturing and seawater cultivation

Engineering ectoine synthesis into cyanobacterial chassis can facilitate cultivation with saline or seawater-derived resources, potentially reducing freshwater demand in photosynthetic production. The 300–500 mM NaCl phenotype in engineered *Synechococcus* is a proof of concept, not yet evidence of industrial-scale performance. (dong2023improvedsalttolerance pages 1-2)

The engineered *H. elongata* system couples high-salt robustness to production of a proline-rich biomass proposed for aquaculture feed. The strain’s growth at 8% NaCl and intracellular proline titre of 353.1 ± 40.5 μmol/g fresh weight provide concrete process-relevant measurements. (khanh2024metabolicpathwayengineering pages 1-2)

### Agriculture and saline-soil inoculants

Genome-resolved analysis of Sambhar Lake and Drang Mine recovered 67 MAGs. Among MetaSPAdes-derived MAGs, annotations predicted salt-tolerance properties in 91.3%, heavy-metal tolerance and exopolysaccharide biosynthesis in 95.6%, antioxidant biosynthesis in 60.86%, and iron acquisition/potassium solubilization in 91.3%. These statistics identify candidate inoculants, but no controlled field trial or isolate-level numerical salinity phenotype was demonstrated; the application remains prospective. (dindhoria2024metagenomicassembledgenomes pages 1-2, dindhoria2024metagenomicassembledgenomes pages 11-13, dindhoria2024metagenomicassembledgenomes pages 13-13)

### Food safety and clinical ecology

*Ktr* function at 2 M NaCl in *S. aureus* helps explain growth in salt-preserved foods and osmotically challenging host niches. Standard mannitol salt agar contains 7.5% NaCl, illustrating the applied relevance of quantitative tolerance, although selective-medium growth is not necessarily the organism’s optimum or maximum. (pricewhelan2013transcriptionalprofilingof pages 1-2)

For *C. difficile*, 350 mM NaCl was described as physiologically relevant to the intestinal environment, and 400 mM severely restricted growth. Compatible-solute availability can therefore alter apparent salinity limits in host-associated assays and should be recorded as a medium covariate. (michel2022cellularadaptationof pages 2-2, michel2022cellularadaptationof pages 2-3)

## 7. Expert interpretation

Three principles should guide TraitMech curation:

1. **The phenotype is relational.** A salinity limit belongs to an organism–assay–endpoint combination, not to the organism alone.
2. **Mechanistic redundancy is common.** In *V. cholerae*, simultaneous inactivation of *nhaA*, *nhaB*, and *nhaD* did not substantially change exponential growth at high Na⁺ because the NQR sodium pump masked antiporter loss; NhaA became essential only when NQR was inhibited at alkaline pH. A simple universal edge “NhaA increases salt tolerance” would therefore be misleading without context. (herz2003rolesofnhaa pages 1-2)
3. **Water activity and salt chemistry delimit interpretation.** NaCl-saturated habitats at approximately 5 M and aᵥ ≈0.755 can sustain dense, metabolically active ecosystems. Consequently, “percent total salts” is inadequate when different ions contribute distinct kosmotropic, chaotropic, toxic, and energetic effects. (lee2018naclsaturatedbrinesare pages 1-3)

## 8. Warnings: claims not yet ready for TraitMech

- Do **not** curate MAG gene presence as proof that a transporter or pathway causes a numerical salinity limit.
- Do **not** infer an organism’s growth range from the salinity of its collection site.
- Do **not** treat *nhaA/B/D* as independently necessary in *V. cholerae*; the available phenotype is conditional on NQR activity and alkaline pH. (herz2003rolesofnhaa pages 1-2)
- Do **not** curate acidic proteome as a universal consequence or cause of halophily. It is strongest in persistent salt-in strategists and was only an expression/pI association in *N. thermophilus*. (xing2024thepolyextremophilenatranaerobius pages 1-2, matarredona2020theroleof pages 3-4)
- Do **not** place MscL/MscS on the direct high-salt growth path. Their strongest evidence concerns hypoosmotic downshock. (bialeckafornal2015therateof pages 1-2)
- Do **not** merge NaCl %, molar NaCl, molar Na⁺, conductivity, practical salinity units, osmolality, and water activity without explicit conversion assumptions.
- Do **not** translate “grew at the highest tested concentration” into a true maximum; encode it as a lower bound on the maximum.
- Do **not** generalize engineered-pathway sufficiency across taxa without retaining strain and construct context.
- Treat cytoplasmic acidification, acidic-proteome remodeling, chemotaxis, and broad metabolic enrichments as secondary or uncertain nodes until direct interventions connect them to a shifted numerical limit.

## 9. Recommended initial graph architecture

A conservative first graph can use the following backbone:

**external NaCl concentration** → **osmotic stress response** → **K⁺ uptake through Trk/Ktr** → **ion homeostasis** → **growth at elevated salinity**

with parallel branches:

- **ectABC** → **ectoine biosynthesis** → **compatible-solute accumulation** → **growth at elevated salinity**;
- **proBAC with reduced PutA catabolism** → **proline accumulation** → **growth at elevated salinity**;
- **Opu/ProU importers** → **glycine-betaine/compatible-solute uptake** → **growth at elevated salinity**; and
- **Nha/NQR systems** → **Na⁺ extrusion/homeostasis** → **growth at elevated salinity**, explicitly qualified by taxon, pH, and functional redundancy.

Keep **MscL/MscS → downshock survival** in an adjacent fluctuation-response subgraph, not the central sustained-salinity axis.

## 10. DOI-first bibliography

1. Xing Q. et al. “The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress.” *Applied and Environmental Microbiology*. Published May 2024. https://doi.org/10.1128/aem.00145-24. (xing2024thepolyextremophilenatranaerobius pages 1-2)
2. Khanh H.C. et al. “Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient *Halomonas elongata*.” *Applied and Environmental Microbiology*. Published August 19, 2024; September issue. https://doi.org/10.1128/aem.01195-24. (khanh2024metabolicpathwayengineering pages 1-2)
3. Wu Z. et al. “Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary.” *Microbiome*. Published June 2024. https://doi.org/10.1186/s40168-024-01817-w. (wu2024metagenomicinsightsinto pages 1-2)
4. Dindhoria K. et al. “Metagenomic assembled genomes indicated the potential application of hypersaline microbiome for plant growth promotion and stress alleviation in salinized soils.” *mSystems*. Published March 2024. https://doi.org/10.1128/msystems.01050-23. (dindhoria2024metagenomicassembledgenomes pages 1-2)
5. Ionescu D. et al. “Extreme fluctuations in ambient salinity select for bacteria with a hybrid ‘salt-in’/‘salt-out’ osmoregulation strategy.” *Frontiers in Microbiomes*. Published January 8, 2024. https://doi.org/10.3389/frmbi.2023.1329925. (ionescu2024extremefluctuationsin pages 1-2)
6. Dong Z. et al. “Improved salt tolerance of *Synechococcus elongatus* PCC 7942 by heterologous synthesis of compatible solute ectoine.” *Frontiers in Microbiology*. Published February 2, 2023. https://doi.org/10.3389/fmicb.2023.1123081. (dong2023improvedsalttolerance pages 1-2)
7. Acciarri G. et al. “Redundant potassium transporter systems guarantee the survival of *Enterococcus faecalis* under stress conditions.” *Frontiers in Microbiology*. Published February 8, 2023. https://doi.org/10.3389/fmicb.2023.1117684. (acciarri2023redundantpotassiumtransporter pages 1-2)
8. Michel A.-M. et al. “Cellular adaptation of *Clostridioides difficile* to high salinity encompasses a compatible solute-responsive change in cell morphology.” *Environmental Microbiology*. Published February 2022. https://doi.org/10.1111/1462-2920.15925. (michel2022cellularadaptationof pages 2-2)
9. Gunde-Cimerman N., Plemenitaš A., Oren A. “Strategies of adaptation of microorganisms of the three domains of life to high salt concentrations.” *FEMS Microbiology Reviews*. Published May 2018. https://doi.org/10.1093/femsre/fuy009. This is the supplied foundational evidence for quantitative halophily framing.
10. Lee C.J.D. et al. “NaCl-saturated brines are thermodynamically moderate, rather than extreme, microbial habitats.” *FEMS Microbiology Reviews*. Published June 2018. https://doi.org/10.1093/femsre/fuy026. (lee2018naclsaturatedbrinesare pages 1-3)
11. Bialecka-Fornal M. et al. “The rate of osmotic downshock determines the survival probability of bacterial mechanosensitive channel mutants.” *Journal of Bacteriology*. Published January 2015. https://doi.org/10.1128/JB.02175-14. (bialeckafornal2015therateof pages 1-2)
12. Price-Whelan A. et al. “Transcriptional profiling of *Staphylococcus aureus* during growth in 2 M NaCl…” *mBio*. Published August 20, 2013. https://doi.org/10.1128/mBio.00407-13. (pricewhelan2013transcriptionalprofilingof pages 1-2)
13. Kraegeloh A. et al. “Potassium transport in a halophilic member of the Bacteria domain…” *Journal of Bacteriology*. Published February 2005. https://doi.org/10.1128/JB.187.3.1036-1043.2005. (kraegeloh2005potassiumtransportin pages 1-2)
14. Herz K. et al. “Roles of NhaA, NhaB, and NhaD Na⁺/H⁺ antiporters in survival of *Vibrio cholerae* in a saline environment.” *Journal of Bacteriology*. Published February 2003. https://doi.org/10.1128/JB.185.4.1236-1244.2003. (herz2003rolesofnhaa pages 1-2)

References

1. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

2. (xing2024thepolyextremophilenatranaerobius pages 7-10): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

3. (lee2018naclsaturatedbrinesare pages 1-3): Callum J D Lee, Phillip E McMullan, Callum J O’Kane, Andrew Stevenson, Inês C Santos, Chayan Roy, Wriddhiman Ghosh, Rocco L Mancinelli, Melanie R Mormile, Geoffrey McMullan, Horia L Banciu, Mario A Fares, Kathleen C Benison, Aharon Oren, Mike L Dyall-Smith, and John E Hallsworth. Nacl-saturated brines are thermodynamically moderate, rather than extreme, microbial habitats. FEMS microbiology reviews, 42 5:672-693, Jun 2018. URL: https://doi.org/10.1093/femsre/fuy026, doi:10.1093/femsre/fuy026. This article has 94 citations and is from a domain leading peer-reviewed journal.

4. (bialeckafornal2015therateof pages 1-2): Maja Bialecka-Fornal, Heun Jin Lee, and Rob Phillips. The rate of osmotic downshock determines the survival probability of bacterial mechanosensitive channel mutants. Journal of Bacteriology, 197:231-237, Jan 2015. URL: https://doi.org/10.1128/jb.02175-14, doi:10.1128/jb.02175-14. This article has 83 citations and is from a peer-reviewed journal.

5. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

6. (michel2022cellularadaptationof pages 2-3): Annika‐Marisa Michel, José Manuel Borrero‐de Acuña, Gabriella Molinari, Can Murat Ünal, Sabine Will, Elisabeth Derksen, Stefan Barthels, Wiebke Bartram, Michel Schrader, Manfred Rohde, Hao Zhang, Tamara Hoffmann, Meina Neumann‐Schaal, Erhard Bremer, and Dieter Jahn. Cellular adaptation of <i>clostridioides difficile</i> to high salinity encompasses a compatible solute‐responsive change in cell morphology. Environmental Microbiology, 24:1499-1517, Feb 2022. URL: https://doi.org/10.1111/1462-2920.15925, doi:10.1111/1462-2920.15925. This article has 13 citations and is from a domain leading peer-reviewed journal.

7. (dong2023improvedsalttolerance pages 1-2): Zhengxin Dong, Tao Sun, Weiwen Zhang, and Lei Chen. Improved salt tolerance of synechococcus elongatus pcc 7942 by heterologous synthesis of compatible solute ectoine. Frontiers in Microbiology, Feb 2023. URL: https://doi.org/10.3389/fmicb.2023.1123081, doi:10.3389/fmicb.2023.1123081. This article has 21 citations and is from a peer-reviewed journal.

8. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

9. (pricewhelan2013transcriptionalprofilingof pages 1-2): Alexa Price-Whelan, Chun Kit Poon, Meredith A. Benson, Tess T. Eidem, Christelle M. Roux, Jeffrey M. Boyd, Paul M. Dunman, Victor J. Torres, and Terry A. Krulwich. Transcriptional profiling of staphylococcus aureus during growth in 2 m nacl leads to clarification of physiological roles for kdp and ktr k <sup>+</sup> uptake systems. Aug 2013. URL: https://doi.org/10.1128/mbio.00407-13, doi:10.1128/mbio.00407-13. This article has 103 citations and is from a domain leading peer-reviewed journal.

10. (xing2024thepolyextremophilenatranaerobius pages 23-24): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

11. (acciarri2023redundantpotassiumtransporter pages 1-2): Giuliana Acciarri, Fernán O. Gizzi, Mariano A. Torres Manno, Jörg Stülke, Martín Espariz, Víctor S. Blancato, and Christian Magni. Redundant potassium transporter systems guarantee the survival of enterococcus faecalis under stress conditions. Frontiers in Microbiology, Feb 2023. URL: https://doi.org/10.3389/fmicb.2023.1117684, doi:10.3389/fmicb.2023.1117684. This article has 23 citations and is from a peer-reviewed journal.

12. (michel2022cellularadaptationof pages 2-2): Annika‐Marisa Michel, José Manuel Borrero‐de Acuña, Gabriella Molinari, Can Murat Ünal, Sabine Will, Elisabeth Derksen, Stefan Barthels, Wiebke Bartram, Michel Schrader, Manfred Rohde, Hao Zhang, Tamara Hoffmann, Meina Neumann‐Schaal, Erhard Bremer, and Dieter Jahn. Cellular adaptation of <i>clostridioides difficile</i> to high salinity encompasses a compatible solute‐responsive change in cell morphology. Environmental Microbiology, 24:1499-1517, Feb 2022. URL: https://doi.org/10.1111/1462-2920.15925, doi:10.1111/1462-2920.15925. This article has 13 citations and is from a domain leading peer-reviewed journal.

13. (matarredona2020theroleof pages 3-4): Laura Matarredona, Mónica Camacho, Basilio Zafrilla, María-José Bonete, and Julia Esclapez. The role of stress proteins in haloarchaea and their adaptive response to environmental shifts. Biomolecules, 10:1390, Sep 2020. URL: https://doi.org/10.3390/biom10101390, doi:10.3390/biom10101390. This article has 79 citations.

14. (wu2024metagenomicinsightsinto pages 1-2): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 69 citations and is from a highest quality peer-reviewed journal.

15. (kraegeloh2005potassiumtransportin pages 1-2): Annette Kraegeloh, Birgit Amendt, and Hans Jörg Kunte. Potassium transport in a halophilic member of the bacteria domain: identification and characterization of the k+ uptake systems trkh and trki from halomonas elongata dsm 2581t. Journal of Bacteriology, 187:1036-1043, Feb 2005. URL: https://doi.org/10.1128/jb.187.3.1036-1043.2005, doi:10.1128/jb.187.3.1036-1043.2005. This article has 131 citations and is from a peer-reviewed journal.

16. (herz2003rolesofnhaa pages 1-2): Katia Herz, Sophie Vimont, Etana Padan, and Patrick Berche. Roles of nhaa, nhab, and nhad na+/h+ antiporters in survival of vibrio cholerae in a saline environment. Journal of Bacteriology, 185:1236-1244, Feb 2003. URL: https://doi.org/10.1128/jb.185.4.1236-1244.2003, doi:10.1128/jb.185.4.1236-1244.2003. This article has 111 citations and is from a peer-reviewed journal.

17. (xamxidin2025metagenomicsassembledgenomesreveal pages 11-12): Maripat Xamxidin, Xuanqi Zhang, Gang Zheng, Can Chen, and Min Wu. Metagenomics-assembled genomes reveal microbial metabolic adaptation to athalassohaline environment, the case lake barkol, china. Frontiers in Microbiology, Jun 2025. URL: https://doi.org/10.3389/fmicb.2025.1550346, doi:10.3389/fmicb.2025.1550346. This article has 19 citations and is from a peer-reviewed journal.

18. (ionescu2024extremefluctuationsin pages 1-2): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 15 citations.

19. (wu2024metagenomicinsightsinto pages 17-18): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 69 citations and is from a highest quality peer-reviewed journal.

20. (dindhoria2024metagenomicassembledgenomes pages 1-2): Kiran Dindhoria, Raghawendra Kumar, Bhavya Bhargava, and Rakshak Kumar. Metagenomic assembled genomes indicated the potential application of hypersaline microbiome for plant growth promotion and stress alleviation in salinized soils. Mar 2024. URL: https://doi.org/10.1128/msystems.01050-23, doi:10.1128/msystems.01050-23. This article has 27 citations and is from a peer-reviewed journal.

21. (dindhoria2024metagenomicassembledgenomes pages 11-13): Kiran Dindhoria, Raghawendra Kumar, Bhavya Bhargava, and Rakshak Kumar. Metagenomic assembled genomes indicated the potential application of hypersaline microbiome for plant growth promotion and stress alleviation in salinized soils. Mar 2024. URL: https://doi.org/10.1128/msystems.01050-23, doi:10.1128/msystems.01050-23. This article has 27 citations and is from a peer-reviewed journal.

22. (dindhoria2024metagenomicassembledgenomes pages 13-13): Kiran Dindhoria, Raghawendra Kumar, Bhavya Bhargava, and Rakshak Kumar. Metagenomic assembled genomes indicated the potential application of hypersaline microbiome for plant growth promotion and stress alleviation in salinized soils. Mar 2024. URL: https://doi.org/10.1128/msystems.01050-23, doi:10.1128/msystems.01050-23. This article has 27 citations and is from a peer-reviewed journal.