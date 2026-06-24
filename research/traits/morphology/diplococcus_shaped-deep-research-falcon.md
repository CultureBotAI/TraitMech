---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:22:37.444508'
end_time: '2026-06-18T07:41:53.935434'
duration_seconds: 1156.49
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: diplococcus shaped
  trait_identifier: METPO:1000671
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: diplococcus_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which spherical cells remain attached in pairs following
    cell division, forming characteristic doublets.
  parent_traits: METPO:1000666
  synonyms: diplococcus-shaped
  evidence_summary: 'DOI:10.1038/ncomms4842: Separation of daughter cells during bacterial
    cell division (Supports diplococcus-like paired morphology as linked to septal
    cross-wall splitting and daughter-cell separation.)'
  causal_graph_summary: 'diplococcus_shaped_septal_separation: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** diplococcus shaped
- **METPO identifier:** METPO:1000671
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which spherical cells remain attached in pairs following cell division, forming characteristic doublets.
- **Parent traits:** METPO:1000666
- **Synonyms:** diplococcus-shaped
- **Existing evidence:** DOI:10.1038/ncomms4842: Separation of daughter cells during bacterial cell division (Supports diplococcus-like paired morphology as linked to septal cross-wall splitting and daughter-cell separation.)
- **Existing causal graph summary:** diplococcus_shaped_septal_separation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **diplococcus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/diplococcus_shaped.yaml`.

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
- **Trait label:** diplococcus shaped
- **METPO identifier:** METPO:1000671
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which spherical cells remain attached in pairs following cell division, forming characteristic doublets.
- **Parent traits:** METPO:1000666
- **Synonyms:** diplococcus-shaped
- **Existing evidence:** DOI:10.1038/ncomms4842: Separation of daughter cells during bacterial cell division (Supports diplococcus-like paired morphology as linked to septal cross-wall splitting and daughter-cell separation.)
- **Existing causal graph summary:** diplococcus_shaped_septal_separation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **diplococcus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/diplococcus_shaped.yaml`.

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


# Microbial Trait Causal Graph Research Report: diplococcus shaped (METPO:1000671)

## Scope summary (TraitMech curation perspective)
The trait **diplococcus shaped** (METPO:1000671) denotes a morphological **cell arrangement state** where **spherical/ovoid cells remain attached as pairs** after cytokinesis due to incomplete or regulated septal splitting, rather than separating fully into single cocci. Mechanistically, the phenotype is governed by the **timing, localization, and activity of septal cell-wall remodeling enzymes** (especially peptidoglycan hydrolases/autolysins) that cut the division septum and/or un-crosslink peptidoglycan at the correct stage to achieve daughter-cell separation without lysis (martinezcaballero2023molecularbasisof pages 1-3, salamaga2023amoonlightingrole pages 4-6).

**Boundary cases / related morphologies** important for annotation:
- **Chains (streptococcal-like chaining):** repeated divisions without complete separation produce **long chains** of attached daughter cells; e.g., in *Enterococcus faecalis*, loss of the septum-cleaving autolysin AtlA yields “long chains” (salamaga2023amoonlightingrole pages 1-2). In *Streptococcus pneumoniae*, loss of the late-division glycosyl hydrolase LytB yields “long chains of daughter cells linked by the tip of the new cell pole” (martinezcaballero2023molecularbasisof pages 1-3). Division-plane logic also contributes: *S. pneumoniae* divides along consecutive parallel planes, leading to chains (ramosleon2025howdospherical pages 2-3).
- **Clumps/clusters (aggregation due to separation failure):** in Gram-negatives such as *Neisseria meningitidis*, disruption of septal separation factors yields **large clumps of unseparated cells** instead of the “characteristic diplococci” (chan2022theamicnlpdpathway pages 1-2).
- **Taxon dependence:** diplococcal morphology can arise from different enzymatic “last-step” machineries across taxa (e.g., AtlA in *E. faecalis*; LytB in pneumococcus; AmiC/NlpD/LtgC pathway components in *Neisseria*), so TraitMech edges should be curated with explicit **NCBITaxon constraints** where appropriate (salamaga2023amoonlightingrole pages 4-6, martinezcaballero2023molecularbasisof pages 1-3, chan2022theamicnlpdpathway pages 1-2, schaub2023mutationalanalysisof pages 1-7).

## Key concepts and current understanding (mechanistic definitions)

### Concept 1: Septum cleavage and daughter-cell separation
A recurrent mechanistic theme is that diplococcal/short-chain morphologies are produced by **regulated septal peptidoglycan cleavage** at the end of division. In *E. faecalis*, “minimisation of cell chain size relies on the activity of a peptidoglycan hydrolase called AtlA, dedicated to septum cleavage” (salamaga2023amoonlightingrole pages 4-6). In *S. pneumoniae*, LytB is described as the **sole peptidoglycan glycosyl hydrolase dedicated to the very late step of cell division** (martinezcaballero2023molecularbasisof pages 1-3).

### Concept 2: Spatial control of autolysins (avoid lysis, ensure correct geometry)
Because peptidoglycan hydrolases can be lethal if mislocalized, bacteria evolve mechanisms to restrict them to the septum. In *E. faecalis*, AtlA septal targeting depends on its LysM repeats and a membrane-associated partner AdmA; deletion of admA abolishes AtlA septal localization and sequesters the fusion in the cytoplasm (salamaga2023amoonlightingrole pages 4-6, salamaga2023amoonlightingrole pages 1-2). In *S. pneumoniae*, LytB localization is coordinated by **wall teichoic acids (WTA)** and the Ser/Thr kinase **StkP** via its PASTA4 domain (martinezcaballero2023molecularbasisof pages 10-11, martinezcaballero2023molecularbasisof pages 8-10, martinezcaballero2023molecularbasisof pages 6-8).

### Concept 3: Cell-envelope polymers as “address labels” for separation enzymes
In pneumococcus, LytB preferentially binds WTA (not LTA), and phosphorylcholine decoration contributes to stable attachment; WTA deficiency reduces GFP-LytB binding while LTA deficiency does not (martinezcaballero2023molecularbasisof pages 8-10). This provides a polymer-mediated mechanism to position separation factors at the correct surface domain.

## Recent developments (prioritizing 2023–2024)

### 1) 2023 Cell Reports: molecular control of final pneumococcal separation (LytB–WTA–StkP)
Martínez-Caballero et al. (2023) resolved a multi-component control logic for the **final step of daughter-cell separation** in *S. pneumoniae* (doi:10.1016/j.celrep.2023.112756; July 2023; https://doi.org/10.1016/j.celrep.2023.112756). Key advances:
- **Dedicated late-step hydrolase:** LytB as a late-division peptidoglycan hydrolase; LytB loss causes chaining (martinezcaballero2023molecularbasisof pages 1-3).
- **Domain logic:** LytB’s C subdomain is required for activity and chaining control; exogenous WT LytB reduces chaining (mean **7.3%** chained), while catalytic domain alone yields much higher chaining (mean **56.3%**) and lacking C subdomain remains elevated (mean **42%**) (martinezcaballero2023molecularbasisof pages 6-8, martinezcaballero2023molecularbasisof media 2716fb17).
- **Localization coupling:** LytB C subdomain anchors via **WTA**, while the N/M region binds **StkP PASTA4** (KD **22 μM**), connecting septal kinase localization to hydrolase positioning (martinezcaballero2023molecularbasisof pages 6-8, martinezcaballero2023molecularbasisof pages 10-11, martinezcaballero2023molecularbasisof pages 8-10).

### 2) 2023 Communications Biology: intracellular septal targeting of an autolysin via LysM “moonlighting” (AtlA–AdmA)
Salamaga et al. (2023) described a previously underappreciated mechanism: LysM repeats can recruit a hydrolase to the septum **inside the cell before secretion**, via the membrane-anchored partner AdmA (doi:10.1038/s42003-023-04808-z; April 2023; https://doi.org/10.1038/s42003-023-04808-z) (salamaga2023amoonlightingrole pages 1-2, salamaga2023amoonlightingrole pages 4-6). This clarifies how diplococci/short chains can be maintained while preventing generalized wall damage.

Quantitative phenotype support includes flow-cytometry-based chain-length comparisons (median FSC) and p-values for ΔadmA and LysM-swap strains (e.g., JH2-2 vs ΔadmA P=0.0015; JH2-2 vs atlA1-6HB ****P=2.3×10−8) (salamaga2023amoonlightingrole pages 6-8, salamaga2023amoonlightingrole pages 4-6).

### 3) 2023 PLOS Biology: competence-driven cell wall remodeling via fratricin CbpD and TA flux (LytR/ComM)
Minhas et al. (2023) connected pneumococcal competence to cell-wall remodeling: competence induces the fratricin **CbpD**, a choline-binding PGN-cleaving protein that targets newly synthesized PGN (PBP2x/FtsW-dependent) (doi:10.1371/journal.pbio.3001990; Jan 2023; https://doi.org/10.1371/journal.pbio.3001990) (vikrant2023competenceremodelsthe pages 12-13). A genome-wide CRISPRi-seq analysis found teichoic-acid biosynthesis genes essential during competence, and LytR is described as a major enzyme mediating WTA formation/anchoring; competence shifts LTA/WTA amounts (flux from LTA toward WTA), and ComM works with LytR to provide immunity to CbpD (vikrant2023competenceremodelsthe pages 1-2, vikrant2023competenceremodelsthe pages 12-13, vikrant2023competenceremodelsthe pages 9-10). These findings are relevant to diplococcus trait graphs because they implicate **environmental/physiological state (competence)** as an upstream modulator of septal wall architecture, which can plausibly shift separation outcomes.

### 4) 2024 Communications Biology: diplococci observed in vivo with quantitative infection dynamics
Aggarwal et al. (2024) reported that “intact diplococci predominated” in early lung infection after inoculation with WT *S. pneumoniae* and quantified strong within-host population turnover: **>97% of clones** became undetectable in lungs by **2 days post-inoculation**, leaving a population dominated by a single lineage (doi:10.1038/s42003-024-07176-4; Dec 2024; https://doi.org/10.1038/s42003-024-07176-4) (aggarwal2024pneumococcalpneumoniais pages 2-3). This provides recent, quantitative context where diplococcal morphology is an in vivo dominant form during pathogenesis.

## Current applications and real-world implementations

1) **Virulence/immune evasion framing for morphotype control:** In *E. faecalis*, the diplococci/short-chain state is presented as advantageous for immune evasion and dissemination; AtlA-mediated minimization of chain size is implicated in reduced phagocyte uptake (salamaga2023amoonlightingrole pages 1-2). This supports using “diplococcus shaped” as a trait relevant to host interaction phenotypes.

2) **Targeting cell separation for anti-infective strategies:** Multiple sources highlight that late-stage hydrolases (LytB, AtlA) are tightly regulated to prevent lysis while enabling separation, suggesting they are plausible antimicrobial targets or adjuvant targets (martinezcaballero2023molecularbasisof pages 10-11, salamaga2023amoonlightingrole pages 1-2). The pneumococcal system particularly points to **enzyme–polymer–kinase** coupling (LytB–WTA–StkP) as a druggable regulatory axis (martinezcaballero2023molecularbasisof pages 10-11).

3) **Microscopy and quantitative morphometrics pipelines:** The recent studies operationalize diplococcus/chain phenotypes with quantitative readouts—e.g., percent chained cells in *S. pneumoniae* separation assays and chain-length measures in *E. faecalis* via imaging and flow cytometry—providing implementation patterns for trait assays (martinezcaballero2023molecularbasisof pages 6-8, salamaga2023amoonlightingrole pages 6-8).

## Candidate causal-graph nodes (grouped by type)

### Phenotype nodes
- **diplococcus shaped** (METPO:1000671)
- short cell chains (label-only)
- long cell chains / chaining phenotype (label-only)
- cell clumps / clusters of unseparated cells (label-only)

### Biological processes / mechanistic steps
- septum cleavage (label-only) (salamaga2023amoonlightingrole pages 4-6)
- daughter cell separation / final separation (label-only) (martinezcaballero2023molecularbasisof pages 1-3)
- septal peptidoglycan breakdown / remodeling (label-only) (schaub2023mutationalanalysisof pages 1-7)
- competence-induced cell wall remodeling (label-only) (vikrant2023competenceremodelsthe pages 12-13)

### Genes/proteins/complexes (label-level unless UniProt available)
**Enterococcus faecalis (NCBITaxon:1351)**
- AtlA (septum-cleaving N-acetylglucosaminidase) (salamaga2023amoonlightingrole pages 4-6)
- AtlA LysM repeats/domain (salamaga2023amoonlightingrole pages 4-6)
- AdmA (membrane-anchored partner for AtlA septal recruitment) (salamaga2023amoonlightingrole pages 4-6)

**Streptococcus pneumoniae (NCBITaxon:1313)**
- LytB (N-acetylglucosaminidase; late division hydrolase) (martinezcaballero2023molecularbasisof pages 1-3)
- StkP (Ser/Thr kinase; PASTA4 domain binds LytB NM region) (martinezcaballero2023molecularbasisof pages 6-8)
- CbpD (competence fratricin; CHAP-domain PGN cleaving) (vikrant2023competenceremodelsthe pages 2-4, vikrant2023competenceremodelsthe pages 12-13)
- LytR (LCP-family WTA anchoring enzyme) (vikrant2023competenceremodelsthe pages 12-13)
- ComM (competence-induced immunity factor) (vikrant2023competenceremodelsthe pages 12-13)

**Neisseria meningitidis (NCBITaxon:487)**
- AmiC (periplasmic amidase) (chan2022theamicnlpdpathway pages 1-2)
- NlpD (outer membrane lipoprotein; cell separation factor) (chan2022theamicnlpdpathway pages 1-2)

**Neisseria gonorrhoeae (NCBITaxon:485)**
- LtgC (lytic transglycosylase; required for separation) (schaub2023mutationalanalysisof pages 1-7)
- AmiC, NlpD (as separation pathway components, per preprint summary) (schaub2023mutationalanalysisof pages 1-7)

### Cell-envelope polymers / chemicals
- wall teichoic acid (WTA; label-only) (martinezcaballero2023molecularbasisof pages 8-10)
- lipoteichoic acid (LTA; label-only) (martinezcaballero2023molecularbasisof pages 8-10)
- phosphorylcholine (PCho; CHEBI candidate but not asserted as CURIE here) (martinezcaballero2023molecularbasisof pages 8-10)

### Environmental/experimental factors
- competence induction / competence state (label-only) (vikrant2023competenceremodelsthe pages 1-2)
- fratricide pressure (CbpD activity) (label-only) (vikrant2023competenceremodelsthe pages 12-13)

## Candidate evidence-backed causal edges
The curation-ready edge table is provided as an artifact below.

| Edge (subject–predicate–object) | Evidence organism/taxon | Reference (DOI + URL + year) | Publication date (month/year if known) | Supporting snippet (short quote) | Notes for curation (mechanism, assay, strength/uncertainty) | Suggested ontology grounding (CURIEs for subject/object if available; otherwise label) |
|---|---|---|---|---|---|---|
| AtlA activity → promotes → septum cleavage | *Enterococcus faecalis* | 10.1038/s42003-023-04808-z • https://doi.org/10.1038/s42003-023-04808-z • 2023 | Apr 2023 | “In *E. faecalis*, the N-acetylglucosaminidase AtlA is dedicated to septum cleavage” (salamaga2023amoonlightingrole pages 4-6) | Strong direct statement from peer-reviewed primary study; septum-cleaving autolysin mechanism central to paired/short-chain morphology. | subject: AtlA autolysin [label]; object: GO:0009252 peptidoglycan biosynthetic process? better label “septum cleavage” [label/process] |
| AtlA inactivation → causes → long cell chains / loss of diplococci-short-chain morphology | *Enterococcus faecalis* | 10.1038/s42003-023-04808-z • https://doi.org/10.1038/s42003-023-04808-z • 2023 | Apr 2023 | “Inactivation of atlA leads to the formation of long chains” (salamaga2023amoonlightingrole pages 1-2) | Strong phenotype edge; directly distinguishes diplococcus/short-chain boundary from chaining. Trait curation note: outcome is loss of diplococcus-shaped phenotype rather than direct positive assertion. | subject: AtlA autolysin [label]; object: long cell chains [label], METPO:1000671 inverse-related |
| Septum cleavage by AtlA → decreases → cell chain length / favors diplococci-short chains | *Enterococcus faecalis* | 10.1038/s42003-023-04808-z • https://doi.org/10.1038/s42003-023-04808-z • 2023 | Apr 2023 | “Minimisation of cell chain size relies on the activity of a peptidoglycan hydrolase called AtlA, dedicated to septum cleavage” (salamaga2023amoonlightingrole pages 4-6) | Mechanistic positive edge for TraitMech: septum cleavage is proximate process producing paired cells rather than long chains. | subject: septum cleavage [label]; object: short chains/diplococci [label; METPO:1000671 related] |
| AtlA LysM domain → required for → AtlA septal localization | *Enterococcus faecalis* | 10.1038/s42003-023-04808-z • https://doi.org/10.1038/s42003-023-04808-z • 2023 | Apr 2023 | “Truncation of LysM domain alters septum recruitment of AtlA-GFP fusions” and “AtlA LysM truncations lead to the sequestration of AtlA inside the cell” (salamaga2023amoonlightingrole pages 4-6) | Strong direct localization evidence from GFP fusions/imaging; supports upstream control of separation enzyme placement. | subject: LysM domain [PFAM/domain label]; object: septal localization of AtlA [label] |
| AdmA → promotes → AtlA septal localization | *Enterococcus faecalis* | 10.1038/s42003-023-04808-z • https://doi.org/10.1038/s42003-023-04808-z • 2023 | Apr 2023 | “the admA deletion abolished the septal localization of AtlA and led to the sequestration of the GFP fusion in the cytoplasm” (salamaga2023amoonlightingrole pages 4-6) | Strong direct genetic evidence; AdmA is a membrane/cytoplasmic partner controlling spatial targeting of autolysin. | subject: AdmA [label]; object: AtlA septal localization [label] |
| AtlA septal localization → enables → daughter cell separation | *Enterococcus faecalis* | 10.1038/s42003-023-04808-z • https://doi.org/10.1038/s42003-023-04808-z • 2023 | Apr 2023 | “the restricted localization of AtlA at the septum… evolved to restrict the subcellular localization of a potentially lethal autolysin to its site of action” (salamaga2023amoonlightingrole pages 1-2) | Moderately direct; inferred from recruitment-to-site-of-action plus chaining phenotypes when localization fails. Mark as slightly inferred but strong. | subject: AtlA septal localization [label]; object: daughter cell separation [GO:0051304? close; label preferred] |
| AtlA LysM-repeat composition/recruitment defects → causes → longer cell chains | *Enterococcus faecalis* | 10.1038/s42003-023-04808-z • https://doi.org/10.1038/s42003-023-04808-z • 2023 | Apr 2023 | “Replacing AtlA LysM repeats with AtlB repeats produced strains that ‘formed longer cell chains’” and FSC comparison “****P = 2.3 × 10−8” (salamaga2023amoonlightingrole pages 4-6) | Strong quantitative morphology support; useful downstream phenotype edge for curated variants. Taxon-specific to *E. faecalis*. | subject: altered AtlA LysM repeats [label]; object: long cell chains [label] |
| LytB → promotes → final separation of daughter cells | *Streptococcus pneumoniae* | 10.1016/j.celrep.2023.112756 • https://doi.org/10.1016/j.celrep.2023.112756 • 2023 | Jul 2023 | “LytB… is described as the sole PG glycosyl hydrolase dedicated to the very late step of pneumococcal cell division” (martinezcaballero2023molecularbasisof pages 1-3) | Strong direct statement; core species-specific positive edge for diplococcus morphology in pneumococcus. | subject: LytB [label]; object: final separation of daughter cells [label] |
| Loss of LytB → causes → chaining phenotype | *Streptococcus pneumoniae* | 10.1016/j.celrep.2023.112756 • https://doi.org/10.1016/j.celrep.2023.112756 • 2023 | Jul 2023 | “the pneumococcus forms long chains of daughter cells linked by the tip of the new cell pole” (martinezcaballero2023molecularbasisof pages 1-3) | Strong phenotype edge delimiting trait boundary: failure of final separation shifts from paired cells toward chains. | subject: loss of LytB [label]; object: chaining phenotype [label] |
| LytB C subdomain → required for → proper cell separation activity | *Streptococcus pneumoniae* | 10.1016/j.celrep.2023.112756 • https://doi.org/10.1016/j.celrep.2023.112756 • 2023 | Jul 2023 | “deletion of C (lytB-ΔC) produces chaining similar to ΔlytB” and exogenous WT LytB restores separation “mean 7.3% chained,” whereas “LytBcat” gives “56.3%” and “LytBNM-cat” “42%” chained (martinezcaballero2023molecularbasisof pages 6-8, martinezcaballero2023molecularbasisof media 2716fb17) | Strong quantitative evidence from mutant/complementation assays. Include figure support for chaining percentages. | subject: LytB C subdomain [label]; object: daughter cell separation [label] |
| LytB C subdomain → mediates → wall teichoic acid binding | *Streptococcus pneumoniae* | 10.1016/j.celrep.2023.112756 • https://doi.org/10.1016/j.celrep.2023.112756 • 2023 | Jul 2023 | “the C subdomain mediates cell-wall attachment via specific recognition of wall teichoic acids (WTA)” (martinezcaballero2023molecularbasisof pages 10-11, martinezcaballero2023molecularbasisof pages 8-10) | Strong biochemical/cellular mechanism; important grounding of polymer-binding determinant upstream of separation. | subject: LytB C subdomain [label]; object: wall teichoic acid [label/CHEBI unclear] |
| Wall teichoic acid → promotes → LytB binding/localization | *Streptococcus pneumoniae* | 10.1016/j.celrep.2023.112756 • https://doi.org/10.1016/j.celrep.2023.112756 • 2023 | Jul 2023 | “GFP-LytB binding is reduced in WTA-deficient cells but preserved in LTA-deficient cells” (martinezcaballero2023molecularbasisof pages 8-10) | Strong comparative evidence distinguishing WTA from LTA; supports specific envelope-polymer dependency. | subject: wall teichoic acid [label]; object: LytB localization/binding [label] |
| StkP PASTA4 domain → promotes → LytB septal localization | *Streptococcus pneumoniae* | 10.1016/j.celrep.2023.112756 • https://doi.org/10.1016/j.celrep.2023.112756 • 2023 | Jul 2023 | “the temporal and spatial localization of LytB is governed by the interaction between specific modules of LytB and the final PASTA domain of StkP” (martinezcaballero2023molecularbasisof pages 1-3); “Deletion of StkP PASTA4 causes chaining and mislocalization of LytB” (martinezcaballero2023molecularbasisof pages 6-8) | Strong direct structural/cellular evidence. Good candidate regulator node upstream of separation. | subject: StkP PASTA4 domain [label]; object: LytB septal localization [label] |
| LytB NM region ↔ interacts with ↔ StkP PASTA4 | *Streptococcus pneumoniae* | 10.1016/j.celrep.2023.112756 • https://doi.org/10.1016/j.celrep.2023.112756 • 2023 | Jul 2023 | “The N–M (NM) region interacts specifically with the distal PASTA4 repeat of… StkP (KD = 22 μM)” (martinezcaballero2023molecularbasisof pages 6-8) | Strong physical interaction edge; useful if graph supports binding interactions distinct from causal regulation. | subject: LytB NM region [label]; object: StkP PASTA4 [label] |
| Phosphorylcholine on WTA → stabilizes → LytB attachment/activity | *Streptococcus pneumoniae* | 10.1016/j.celrep.2023.112756 • https://doi.org/10.1016/j.celrep.2023.112756 • 2023 | Jul 2023 | “phosphorylcholine (PCho) is critical for stable binding; replacement by ethanolamine (PEA) destabilizes attachment and correlates with loss of autolysin activity and increased chaining” (martinezcaballero2023molecularbasisof pages 8-10) | Strong but chemistry-specific edge; useful if polymer decoration level is curated. | subject: CHEBI: phosphocholine? candidate label “phosphorylcholine”; object: LytB attachment/activity [label] |
| AmiC → required for → cell separation | *Neisseria meningitidis* | 10.1128/iai.00485-21 • https://doi.org/10.1128/iai.00485-21 • 2022 | Mar 2022 | “Mutations in amiC… produce large clumps of unseparated cells instead of the characteristic diplococci” (chan2022theamicnlpdpathway pages 1-2) | Strong direct evidence, though 2022 not 2023–2024. Good conserved Gram-negative separation mechanism. | subject: AmiC amidase [label]; object: cell separation [label] |
| NlpD → activates/promotes → AmiC-dependent cell separation | *Neisseria meningitidis* | 10.1128/iai.00485-21 • https://doi.org/10.1128/iai.00485-21 • 2022 | Mar 2022 | “AmiC and NlpD were found to function in cell separation” and NlpD localizes “to the septum” (chan2022theamicnlpdpathway pages 1-2) | Strong direct evidence; activator relationship to AmiC is supported in pathway model but activation verb may be partly inferred from known amidase-activator role. Mark slight uncertainty if using “activates.” | subject: NlpD [label]; object: AmiC-dependent cell separation [label] |
| AmiC/NlpD pathway disruption → causes → clumps instead of characteristic diplococci | *Neisseria meningitidis* | 10.1128/iai.00485-21 • https://doi.org/10.1128/iai.00485-21 • 2022 | Mar 2022 | “mutation of either amiC or nlpD resulted in large clumps of unseparated *N. meningitidis* cells instead of the characteristic diplococci” (chan2022theamicnlpdpathway pages 1-2) | Strong phenotype edge defining negative side of trait in Neisseria. | subject: amiC or nlpD mutation [label]; object: clumps/unseparated cells [label] |
| LtgC → required for → cell separation | *Neisseria gonorrhoeae* | 10.1101/2023.06.20.545760 • https://doi.org/10.1101/2023.06.20.545760 • 2023 | Jun 2023 | “deletion of ltgC in *Neisseria gonorrhoeae* results in growth in clusters of around 6-20 cells rather than as normal diplococci or monococci” (schaub2023mutationalanalysisof pages 1-7) | Strong primary evidence but preprint. Useful with uncertainty flag until peer-reviewed version available. | subject: LtgC lytic transglycosylase [label]; object: cell separation [label] |
| LtgC domain 3 → promotes → AmiC binding | *Neisseria gonorrhoeae* | 10.1101/2023.06.20.545760 • https://doi.org/10.1101/2023.06.20.545760 • 2023 | Jun 2023 | “LtgC was found to bind AmiC… and domain 3 mutations reduced binding” (schaub2023mutationalanalysisof pages 1-7) | Strong mechanistic preprint evidence linking transglycosylase–amidase interaction to separation complex assembly. | subject: LtgC domain 3 [label]; object: AmiC [label] |
| LtgC enzymatic activity loss or domain-3 mutation → causes → clusters of 6–20 cells / failure of diplococcus morphology | *Neisseria gonorrhoeae* | 10.1101/2023.06.20.545760 • https://doi.org/10.1101/2023.06.20.545760 • 2023 | Jun 2023 | “around 6-20 cells rather than as normal diplococci or monococci” and “All the mutants showed defects in cell separation” (schaub2023mutationalanalysisof pages 1-7) | Strong phenotype edge; preprint and species-specific. Good quantitative morphology statistic. | subject: ltgC mutant [label]; object: clusters of 6–20 cells [label] |
| Septal peptidoglycan breakdown by AmiC + NlpD + LtgC → enables → normal diplococci/monococci morphology | *Neisseria gonorrhoeae* | 10.1101/2023.06.20.545760 • https://doi.org/10.1101/2023.06.20.545760 • 2023 | Jun 2023 | “The peptidoglycan breakdown that occurs at the septum following cell division… requires three proteins, amidase AmiC, amidase activator NlpD, and lytic transglycosylase LtgC” (schaub2023mutationalanalysisof pages 1-7) | Strong summary edge but combines three proteins in one node; acceptable as pathway-level statement. | subject: AmiC/NlpD/LtgC septal PG breakdown pathway [label]; object: normal diplococci morphology [METPO:1000671 related] |
| Competence induction → increases essentiality of → teichoic acid biosynthesis genes | *Streptococcus pneumoniae* | 10.1371/journal.pbio.3001990 • https://doi.org/10.1371/journal.pbio.3001990 • 2023 | Jan 2023 | “genes involved in teichoic acid (TA) biosynthesis are essential during competence” (vikrant2023competenceremodelsthe pages 1-2) | Strong CRISPRi-seq evidence for competence-linked envelope remodeling context. | subject: competence [GO:0030420 bacterial competence? label]; object: teichoic acid biosynthesis genes [pathway label] |
| LytR → mediates → WTA formation/anchoring to PGN | *Streptococcus pneumoniae* | 10.1371/journal.pbio.3001990 • https://doi.org/10.1371/journal.pbio.3001990 • 2023 | Jan 2023 | “LytR is the major enzyme mediating the final step in WTA formation” and “anchors the TA precursor to PGN to create WTA” (vikrant2023competenceremodelsthe pages 1-2, vikrant2023competenceremodelsthe pages 12-13) | Strong direct role in cell-wall polymer attachment; relevant upstream factor for autolysin positioning. | subject: LytR [label/LCP family protein]; object: wall teichoic acid formation [label] |
| ComM + LytR → promote → immunity to CbpD / septal remodeling toward WTA | *Streptococcus pneumoniae* | 10.1371/journal.pbio.3001990 • https://doi.org/10.1371/journal.pbio.3001990 • 2023 | Jan 2023 | “ComM works in concert with LytR, and expression of both genes provides optimal immunity towards CbpD” (vikrant2023competenceremodelsthe pages 12-13) | Strong direct statement for combined node. Useful pathway-level curation. | subject: ComM + LytR [label]; object: immunity to CbpD / septal remodeling [label] |
| Competence / ComM / LytR activation → shifts → TA flux from LTA toward WTA | *Streptococcus pneumoniae* | 10.1371/journal.pbio.3001990 • https://doi.org/10.1371/journal.pbio.3001990 • 2023 | Jan 2023 | “the levels or relative amounts of LTA and WTA are altered when competence is triggered” and “the flux of TA from LTA increases towards WTA during competence development” (vikrant2023competenceremodelsthe pages 12-13, vikrant2023competenceremodelsthe pages 9-10) | Good mechanistic edge from labeling experiments; directly relevant to wall remodeling. | subject: competence/ComM/LytR [label]; object: increased WTA:LTA ratio [label] |
| CbpD → remodels → septal/newly synthesized peptidoglycan | *Streptococcus pneumoniae* | 10.1371/journal.pbio.3001990 • https://doi.org/10.1371/journal.pbio.3001990 • 2023 | Jan 2023 | “CbpD only attacks PGN that is newly synthesized by PBP2x and FtsW” (vikrant2023competenceremodelsthe pages 12-13) | Strong direct mechanism connecting competence fratricin to septal cell-wall remodeling. | subject: CbpD [label]; object: newly synthesized septal peptidoglycan [label] |
| Competence/CbpD-dependent septal remodeling → increases → midcell surface exposure of PspA/PspC | *Streptococcus pneumoniae* | 10.1371/journal.pbio.3001990 • https://doi.org/10.1371/journal.pbio.3001990 • 2023 | Jan 2023 | “PspA and PspC become more surface-exposed at midcell during competence, in a CbpD-dependent manner” (vikrant2023competenceremodelsthe pages 1-2, vikrant2023competenceremodelsthe pages 12-13) | Strong direct edge for application context; not morphology itself but consequence of same remodeling axis. | subject: competence/CbpD septal remodeling [label]; object: midcell PspA/PspC exposure [label] |
| Increased WTA plus ComM/LytR activity → may delay → cell division/final separation | *Streptococcus pneumoniae* | 10.1371/journal.pbio.3001990 • https://doi.org/10.1371/journal.pbio.3001990 • 2023 | Jan 2023 | “could inhibit divisome activity (PBP2x) making cells resistant to CbpD and causing a ‘delay in division’” (vikrant2023competenceremodelsthe pages 12-13) | Explicitly mark uncertain/inferred: authors propose model rather than direct morphology readout. Potential bridge to paired/chain state under competence. | subject: increased WTA with ComM/LytR [label]; object: delayed division [label] |
| Mutation of cell-separation genes (amiC/nlpD/ltgC) → causes → clumps/clusters instead of diplococci | *Neisseria* spp. | 10.1128/iai.00485-21 • https://doi.org/10.1128/iai.00485-21 • 2022; 10.1101/2023.06.20.545760 • https://doi.org/10.1101/2023.06.20.545760 • 2023 | Mar 2022; Jun 2023 | “large clumps of unseparated… instead of the characteristic diplococci” and “clusters of around 6-20 cells rather than as normal diplococci” (chan2022theamicnlpdpathway pages 1-2, schaub2023mutationalanalysisof pages 1-7) | Cross-study synthesis edge; valuable for generic trait graph but broader than single experiment. Mark as synthesis across taxa/species. | subject: mutation in cell-separation genes [label]; object: clumps/clusters instead of diplococci [label] |


*Table: This table compiles candidate causal edges for curating the diplococcus-shaped microbial trait, linking autolysins, septal localization factors, teichoic acids, and separation defects to paired-cell versus chain/cluster morphologies. It emphasizes direct mechanistic evidence, recent 2023 studies, and flags inferred or preprint-supported claims for careful curation.*

## Visual evidence (figures/tables)
Martínez-Caballero et al. include microscopy and quantification of chaining (% chains) used to support the functional requirement of LytB domains and exogenous complementation; these images also show domain organization and interaction interface relevant to curation (martinezcaballero2023molecularbasisof media 2716fb17, martinezcaballero2023molecularbasisof media 1c0b1d78, martinezcaballero2023molecularbasisof media 7658a55c, martinezcaballero2023molecularbasisof media 17a8ff81).

## Warnings / claims not yet ready for curation
1) **Preprint-only mechanistic claims:** The *N. gonorrhoeae* LtgC work is currently a bioRxiv preprint (doi:10.1101/2023.06.20.545760). Edges relying solely on this should be marked **uncertain** pending peer-reviewed publication (schaub2023mutationalanalysisof pages 1-7).
2) **Competence → delayed division → diplococcus/chain shift:** Minhas et al. provide strong evidence for competence-driven TA remodeling and CbpD targeting of nascent PGN, but links from these events to a specific diplococcus-versus-chain outcome are partly model-based; curate as **hypothesis/inferred** unless a direct morphology readout is added (vikrant2023competenceremodelsthe pages 12-13).
3) **Ontology identifiers for proteins/chemicals:** UniProt accessions, MetaCyc/KEGG reaction IDs, and definitive CHEBI identifiers were not present in the extracted text; keep these nodes as **label-only** until grounded from sequence/database lookups.

## DOI-first bibliography (with URLs and publication dates where available)
1) Martínez-Caballero S, et al. *Molecular basis of the final step of cell division in Streptococcus pneumoniae.* **Cell Reports**. **July 2023**. DOI: **10.1016/j.celrep.2023.112756**. URL: https://doi.org/10.1016/j.celrep.2023.112756 (martinezcaballero2023molecularbasisof pages 1-3, martinezcaballero2023molecularbasisof pages 6-8, martinezcaballero2023molecularbasisof pages 10-11, martinezcaballero2023molecularbasisof pages 8-10, martinezcaballero2023molecularbasisof media 2716fb17).
2) Salamaga B, et al. *A moonlighting role for LysM peptidoglycan binding domains underpins Enterococcus faecalis daughter cell separation.* **Communications Biology**. **April 2023**. DOI: **10.1038/s42003-023-04808-z**. URL: https://doi.org/10.1038/s42003-023-04808-z (salamaga2023amoonlightingrole pages 1-2, salamaga2023amoonlightingrole pages 4-6, salamaga2023amoonlightingrole pages 6-8).
3) Minhas V, et al. *Competence remodels the pneumococcal cell wall exposing key surface virulence factors that mediate increased host adherence.* **PLOS Biology**. **January 2023**. DOI: **10.1371/journal.pbio.3001990**. URL: https://doi.org/10.1371/journal.pbio.3001990 (vikrant2023competenceremodelsthe pages 12-13, vikrant2023competenceremodelsthe pages 1-2, vikrant2023competenceremodelsthe pages 9-10).
4) Aggarwal SD, et al. *Pneumococcal pneumonia is driven by increased bacterial turnover due to bacteriocin-mediated intra-strain competition.* **Communications Biology**. **December 2024**. DOI: **10.1038/s42003-024-07176-4**. URL: https://doi.org/10.1038/s42003-024-07176-4 (aggarwal2024pneumococcalpneumoniais pages 2-3, aggarwal2024pneumococcalpneumoniais pages 3-5).
5) Schaub RE, et al. *Mutational analysis of LtgC, a lytic transglycosylase required for cell separation in Neisseria gonorrhoeae.* **bioRxiv**. **June 2023**. DOI: **10.1101/2023.06.20.545760**. URL: https://doi.org/10.1101/2023.06.20.545760 (preprint) (schaub2023mutationalanalysisof pages 1-7).
6) Chan JM, et al. *The AmiC/NlpD Pathway Dominates Peptidoglycan Breakdown in Neisseria meningitidis and Affects Cell Separation, NOD1 Agonist Production, and Infection.* **Infection and Immunity**. **March 2022**. DOI: **10.1128/iai.00485-21**. URL: https://doi.org/10.1128/iai.00485-21 (chan2022theamicnlpdpathway pages 1-2).
7) Ramos-León F, Ramamurthi KS. *How do spherical bacteria regulate cell division?* **Biochemical Society Transactions**. **April 2025**. DOI: **10.1042/bst20240956**. URL: https://doi.org/10.1042/bst20240956 (background division-plane logic; not 2023–2024 but useful for boundary reasoning) (ramosleon2025howdospherical pages 2-3, ramosleon2025howdospherical pages 10-11).


References

1. (martinezcaballero2023molecularbasisof pages 1-3): Siseth Martínez-Caballero, Céline Freton, Rafael Molina, Sergio G. Bartual, Virginie Gueguen-Chaignon, Chryslène Mercy, Federico Gago, Kiran V. Mahasenan, Inés G. Muñoz, Mijoon Lee, Dusan Hesek, Shahriar Mobashery, Juan A. Hermoso, and Christophe Grangeasse. Molecular basis of the final step of cell division in streptococcus pneumoniae. Cell reports, 42:112756-112756, Jul 2023. URL: https://doi.org/10.1016/j.celrep.2023.112756, doi:10.1016/j.celrep.2023.112756. This article has 20 citations and is from a highest quality peer-reviewed journal.

2. (salamaga2023amoonlightingrole pages 4-6): Bartłomiej Salamaga, Robert D. Turner, Fathe Elsarmane, Nicola F. Galley, Saulius Kulakauskas, and Stéphane Mesnage. A moonlighting role for lysm peptidoglycan binding domains underpins enterococcus faecalis daughter cell separation. Communications Biology, 6:1-10, Apr 2023. URL: https://doi.org/10.1038/s42003-023-04808-z, doi:10.1038/s42003-023-04808-z. This article has 13 citations and is from a peer-reviewed journal.

3. (salamaga2023amoonlightingrole pages 1-2): Bartłomiej Salamaga, Robert D. Turner, Fathe Elsarmane, Nicola F. Galley, Saulius Kulakauskas, and Stéphane Mesnage. A moonlighting role for lysm peptidoglycan binding domains underpins enterococcus faecalis daughter cell separation. Communications Biology, 6:1-10, Apr 2023. URL: https://doi.org/10.1038/s42003-023-04808-z, doi:10.1038/s42003-023-04808-z. This article has 13 citations and is from a peer-reviewed journal.

4. (ramosleon2025howdospherical pages 2-3): Félix Ramos-León and Kumaran S. Ramamurthi. How do spherical bacteria regulate cell division? Biochemical Society Transactions, 53:447-460, Apr 2025. URL: https://doi.org/10.1042/bst20240956, doi:10.1042/bst20240956. This article has 4 citations and is from a peer-reviewed journal.

5. (chan2022theamicnlpdpathway pages 1-2): Jia Mun Chan, Kathleen T. Hackett, Katelynn L. Woodhams, Ryan E. Schaub, and Joseph P. Dillard. The amic/nlpd pathway dominates peptidoglycan breakdown in neisseria meningitidis and affects cell separation, nod1 agonist production, and infection. Mar 2022. URL: https://doi.org/10.1128/iai.00485-21, doi:10.1128/iai.00485-21. This article has 6 citations and is from a peer-reviewed journal.

6. (schaub2023mutationalanalysisof pages 1-7): Ryan E. Schaub, Krizia Perez-Medina, Joshua Tomberg, Robert A. Nicholas, and Joseph P. Dillard. Mutational analysis of ltgc, a lytic transglycosylase required for cell separation in neisseria gonorrhoeae. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.20.545760, doi:10.1101/2023.06.20.545760. This article has 1 citations.

7. (martinezcaballero2023molecularbasisof pages 10-11): Siseth Martínez-Caballero, Céline Freton, Rafael Molina, Sergio G. Bartual, Virginie Gueguen-Chaignon, Chryslène Mercy, Federico Gago, Kiran V. Mahasenan, Inés G. Muñoz, Mijoon Lee, Dusan Hesek, Shahriar Mobashery, Juan A. Hermoso, and Christophe Grangeasse. Molecular basis of the final step of cell division in streptococcus pneumoniae. Cell reports, 42:112756-112756, Jul 2023. URL: https://doi.org/10.1016/j.celrep.2023.112756, doi:10.1016/j.celrep.2023.112756. This article has 20 citations and is from a highest quality peer-reviewed journal.

8. (martinezcaballero2023molecularbasisof pages 8-10): Siseth Martínez-Caballero, Céline Freton, Rafael Molina, Sergio G. Bartual, Virginie Gueguen-Chaignon, Chryslène Mercy, Federico Gago, Kiran V. Mahasenan, Inés G. Muñoz, Mijoon Lee, Dusan Hesek, Shahriar Mobashery, Juan A. Hermoso, and Christophe Grangeasse. Molecular basis of the final step of cell division in streptococcus pneumoniae. Cell reports, 42:112756-112756, Jul 2023. URL: https://doi.org/10.1016/j.celrep.2023.112756, doi:10.1016/j.celrep.2023.112756. This article has 20 citations and is from a highest quality peer-reviewed journal.

9. (martinezcaballero2023molecularbasisof pages 6-8): Siseth Martínez-Caballero, Céline Freton, Rafael Molina, Sergio G. Bartual, Virginie Gueguen-Chaignon, Chryslène Mercy, Federico Gago, Kiran V. Mahasenan, Inés G. Muñoz, Mijoon Lee, Dusan Hesek, Shahriar Mobashery, Juan A. Hermoso, and Christophe Grangeasse. Molecular basis of the final step of cell division in streptococcus pneumoniae. Cell reports, 42:112756-112756, Jul 2023. URL: https://doi.org/10.1016/j.celrep.2023.112756, doi:10.1016/j.celrep.2023.112756. This article has 20 citations and is from a highest quality peer-reviewed journal.

10. (martinezcaballero2023molecularbasisof media 2716fb17): Siseth Martínez-Caballero, Céline Freton, Rafael Molina, Sergio G. Bartual, Virginie Gueguen-Chaignon, Chryslène Mercy, Federico Gago, Kiran V. Mahasenan, Inés G. Muñoz, Mijoon Lee, Dusan Hesek, Shahriar Mobashery, Juan A. Hermoso, and Christophe Grangeasse. Molecular basis of the final step of cell division in streptococcus pneumoniae. Cell reports, 42:112756-112756, Jul 2023. URL: https://doi.org/10.1016/j.celrep.2023.112756, doi:10.1016/j.celrep.2023.112756. This article has 20 citations and is from a highest quality peer-reviewed journal.

11. (salamaga2023amoonlightingrole pages 6-8): Bartłomiej Salamaga, Robert D. Turner, Fathe Elsarmane, Nicola F. Galley, Saulius Kulakauskas, and Stéphane Mesnage. A moonlighting role for lysm peptidoglycan binding domains underpins enterococcus faecalis daughter cell separation. Communications Biology, 6:1-10, Apr 2023. URL: https://doi.org/10.1038/s42003-023-04808-z, doi:10.1038/s42003-023-04808-z. This article has 13 citations and is from a peer-reviewed journal.

12. (vikrant2023competenceremodelsthe pages 12-13): Vikrant Minhas, Arnau Domenech, Dimitra Synefiaridou, Daniel Straume, Max Brendel, Gonzalo Cebrero, Xue Liu, Charlotte Costa, Mara Baldry, Jean-Claude Sirard, Camilo Perez, Nicolas Gisch, Sven Hammerschmidt, Leiv Sigve Håvarstein, and Jan-Willem Veening. Competence remodels the pneumococcal cell wall exposing key surface virulence factors that mediate increased host adherence. PLOS Biology, Jan 2023. URL: https://doi.org/10.1371/journal.pbio.3001990, doi:10.1371/journal.pbio.3001990. This article has 30 citations and is from a highest quality peer-reviewed journal.

13. (vikrant2023competenceremodelsthe pages 1-2): Vikrant Minhas, Arnau Domenech, Dimitra Synefiaridou, Daniel Straume, Max Brendel, Gonzalo Cebrero, Xue Liu, Charlotte Costa, Mara Baldry, Jean-Claude Sirard, Camilo Perez, Nicolas Gisch, Sven Hammerschmidt, Leiv Sigve Håvarstein, and Jan-Willem Veening. Competence remodels the pneumococcal cell wall exposing key surface virulence factors that mediate increased host adherence. PLOS Biology, Jan 2023. URL: https://doi.org/10.1371/journal.pbio.3001990, doi:10.1371/journal.pbio.3001990. This article has 30 citations and is from a highest quality peer-reviewed journal.

14. (vikrant2023competenceremodelsthe pages 9-10): Vikrant Minhas, Arnau Domenech, Dimitra Synefiaridou, Daniel Straume, Max Brendel, Gonzalo Cebrero, Xue Liu, Charlotte Costa, Mara Baldry, Jean-Claude Sirard, Camilo Perez, Nicolas Gisch, Sven Hammerschmidt, Leiv Sigve Håvarstein, and Jan-Willem Veening. Competence remodels the pneumococcal cell wall exposing key surface virulence factors that mediate increased host adherence. PLOS Biology, Jan 2023. URL: https://doi.org/10.1371/journal.pbio.3001990, doi:10.1371/journal.pbio.3001990. This article has 30 citations and is from a highest quality peer-reviewed journal.

15. (aggarwal2024pneumococcalpneumoniais pages 2-3): Surya D. Aggarwal, Kristen L. Lokken-Toyli, and Jeffrey N. Weiser. Pneumococcal pneumonia is driven by increased bacterial turnover due to bacteriocin-mediated intra-strain competition. Communications Biology, Dec 2024. URL: https://doi.org/10.1038/s42003-024-07176-4, doi:10.1038/s42003-024-07176-4. This article has 8 citations and is from a peer-reviewed journal.

16. (vikrant2023competenceremodelsthe pages 2-4): Vikrant Minhas, Arnau Domenech, Dimitra Synefiaridou, Daniel Straume, Max Brendel, Gonzalo Cebrero, Xue Liu, Charlotte Costa, Mara Baldry, Jean-Claude Sirard, Camilo Perez, Nicolas Gisch, Sven Hammerschmidt, Leiv Sigve Håvarstein, and Jan-Willem Veening. Competence remodels the pneumococcal cell wall exposing key surface virulence factors that mediate increased host adherence. PLOS Biology, Jan 2023. URL: https://doi.org/10.1371/journal.pbio.3001990, doi:10.1371/journal.pbio.3001990. This article has 30 citations and is from a highest quality peer-reviewed journal.

17. (martinezcaballero2023molecularbasisof media 1c0b1d78): Siseth Martínez-Caballero, Céline Freton, Rafael Molina, Sergio G. Bartual, Virginie Gueguen-Chaignon, Chryslène Mercy, Federico Gago, Kiran V. Mahasenan, Inés G. Muñoz, Mijoon Lee, Dusan Hesek, Shahriar Mobashery, Juan A. Hermoso, and Christophe Grangeasse. Molecular basis of the final step of cell division in streptococcus pneumoniae. Cell reports, 42:112756-112756, Jul 2023. URL: https://doi.org/10.1016/j.celrep.2023.112756, doi:10.1016/j.celrep.2023.112756. This article has 20 citations and is from a highest quality peer-reviewed journal.

18. (martinezcaballero2023molecularbasisof media 7658a55c): Siseth Martínez-Caballero, Céline Freton, Rafael Molina, Sergio G. Bartual, Virginie Gueguen-Chaignon, Chryslène Mercy, Federico Gago, Kiran V. Mahasenan, Inés G. Muñoz, Mijoon Lee, Dusan Hesek, Shahriar Mobashery, Juan A. Hermoso, and Christophe Grangeasse. Molecular basis of the final step of cell division in streptococcus pneumoniae. Cell reports, 42:112756-112756, Jul 2023. URL: https://doi.org/10.1016/j.celrep.2023.112756, doi:10.1016/j.celrep.2023.112756. This article has 20 citations and is from a highest quality peer-reviewed journal.

19. (martinezcaballero2023molecularbasisof media 17a8ff81): Siseth Martínez-Caballero, Céline Freton, Rafael Molina, Sergio G. Bartual, Virginie Gueguen-Chaignon, Chryslène Mercy, Federico Gago, Kiran V. Mahasenan, Inés G. Muñoz, Mijoon Lee, Dusan Hesek, Shahriar Mobashery, Juan A. Hermoso, and Christophe Grangeasse. Molecular basis of the final step of cell division in streptococcus pneumoniae. Cell reports, 42:112756-112756, Jul 2023. URL: https://doi.org/10.1016/j.celrep.2023.112756, doi:10.1016/j.celrep.2023.112756. This article has 20 citations and is from a highest quality peer-reviewed journal.

20. (aggarwal2024pneumococcalpneumoniais pages 3-5): Surya D. Aggarwal, Kristen L. Lokken-Toyli, and Jeffrey N. Weiser. Pneumococcal pneumonia is driven by increased bacterial turnover due to bacteriocin-mediated intra-strain competition. Communications Biology, Dec 2024. URL: https://doi.org/10.1038/s42003-024-07176-4, doi:10.1038/s42003-024-07176-4. This article has 8 citations and is from a peer-reviewed journal.

21. (ramosleon2025howdospherical pages 10-11): Félix Ramos-León and Kumaran S. Ramamurthi. How do spherical bacteria regulate cell division? Biochemical Society Transactions, 53:447-460, Apr 2025. URL: https://doi.org/10.1042/bst20240956, doi:10.1042/bst20240956. This article has 4 citations and is from a peer-reviewed journal.