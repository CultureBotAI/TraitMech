---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:49:02.889173'
end_time: '2026-08-04T00:57:18.763843'
duration_seconds: 495.87
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: haloalkaliphilic
  trait_identifier: METPO:1000621
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: haloalkaliphilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A halophily preference in which an organism requires both high salt
    concentrations and alkaline pH for optimal growth.
  parent_traits: METPO:1000629
  synonyms: ''
  evidence_summary: 'PMID:17203963: aerobic, haloalkaliphilic archaeon Natronomonas
    pharaonis (Organism example: Natronomonas pharaonis is described as haloalkaliphilic.)'
  causal_graph_summary: 'haloalkaliphilic_salt_alkaline_adaptation: 13 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** haloalkaliphilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000621
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism requires both high salt concentrations and alkaline pH for optimal growth.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** PMID:17203963: aerobic, haloalkaliphilic archaeon Natronomonas pharaonis (Organism example: Natronomonas pharaonis is described as haloalkaliphilic.)
- **Existing causal graph summary:** haloalkaliphilic_salt_alkaline_adaptation: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **haloalkaliphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/haloalkaliphilic.yaml`.

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
- **Trait label:** haloalkaliphilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000621
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism requires both high salt concentrations and alkaline pH for optimal growth.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** PMID:17203963: aerobic, haloalkaliphilic archaeon Natronomonas pharaonis (Organism example: Natronomonas pharaonis is described as haloalkaliphilic.)
- **Existing causal graph summary:** haloalkaliphilic_salt_alkaline_adaptation: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **haloalkaliphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/haloalkaliphilic.yaml`.

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


# Curation-focused research report: haloalkaliphilic

**Trait:** haloalkaliphilic  
**Identifier:** `METPO:1000621`  
**Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED  
**Parent:** `METPO:1000629`

## 1. Scope and current interpretation

`METPO:1000621` should denote a **preference or requirement for the conjunction of elevated salinity and alkaline pH**, such that optimal growth occurs under both conditions. It is an ecological–physiological phenotype, not a single molecular mechanism. The supplied definition—“a halophily preference in which an organism requires both high salt concentrations and alkaline pH for optimal growth”—is therefore appropriate.

The strongest phenotype records specify a two-dimensional growth response rather than isolation source alone. *Natranaerobius thermophilus*, for example, grows optimally around 3.3–3.9 M Na+, pH 9.5, and 53°C; the reported salinity range extends approximately 3.1–4.9 M Na+. This is an unambiguous haloalkaliphilic, additionally thermophilic, phenotype. (xing2024thepolyextremophilenatranaerobius pages 1-2) Strain Omega grows from pH 8.5–10.5, optimally at 9.5–10, and from 0.3–3 M total Na+, optimally at 1 M; it is therefore an obligate alkaliphile with moderate salt requirement/tolerance rather than an extreme halophile. (sorokin2018phenotypicandgenomic pages 1-2)

### Boundary cases

- **Halophilic but not haloalkaliphilic:** elevated salt is required or preferred, but optimal pH is neutral or acidic.
- **Alkaliphilic but not haloalkaliphilic:** alkaline pH is preferred or required, but elevated salt is unnecessary.
- **Halotolerant alkaliphile:** grows across high salinity but does not show a demonstrated high-salt optimum or requirement. This is a borderline case under the supplied requirement-based definition.
- **Alkali-tolerant halophile:** survives alkaline assay conditions but has no alkaline optimum.
- **Soda-lake occurrence only:** isolation or metagenomic detection in a haloalkaline habitat is insufficient; growth measurements or another direct phenotype assay are needed.
- **Polyextremophile:** haloalkaliphily may coexist with thermophily, anaerobiosis, or other traits. Those should be represented separately rather than folded into this node.

**Recommended curation rule:** require measured growth at multiple pH and salinity values, preferably a response surface or factorial assay. Record ranges and optima as evidence annotations rather than imposing a universal numerical threshold.

## 2. Mechanistic model

Haloalkaliphily combines two linked challenges. High external salinity lowers water activity and drives osmotic water loss, whereas alkaline pH makes proton acquisition and cytoplasmic acidification difficult. Successful organisms therefore combine: (i) osmotic balancing through intracellular K+ and/or compatible solutes; (ii) Na+/H+ or Na+(K+)/H+ exchange to import protons and control cytoplasmic pH; (iii) membrane and proteome adaptations; and, in some taxa, (iv) sodium- or light-coupled bioenergetics.

The present evidence argues against encoding one universal pathway. A 2024 multi-omics study showed that *N. thermophilus* simultaneously uses compatible-solute and salt-in mechanisms, whereas many older schemes treated these as alternatives. (xing2024thepolyextremophilenatranaerobius pages 1-2) A current haloarchaeal review likewise recognizes K+ accumulation/Na+ exclusion and compatible-solute strategies, with acidic proteins maintaining solubility under hypersaline conditions. (bonnaud2024haloarchaeaaspromising pages 2-4) The graph should consequently allow **alternative and combinatorial taxon-specific modules**.

## 3. Candidate nodes and ontology grounding

Identifiers below are limited to familiar, stable mappings; organism-specific proteins remain label-only where a verified accession was not established from the retrieved evidence.

### Trait and environmental nodes

- haloalkaliphilic — `METPO:1000621`
- high salinity / hypersaline condition — label-only pending the project’s preferred ENVO mapping
- alkaline pH — label-only pending the preferred ENVO/PATO representation
- haloalkaline soda lake — label-only pending habitat-level ENVO review
- increasing external Na+ concentration — experimental factor
- light — experimental/environmental factor

### Chemicals and metabolites

- sodium ion — `CHEBI:29101`
- potassium ion — `CHEBI:29103`
- proton — `CHEBI:15378`
- chloride — `CHEBI:17996`
- glycine betaine — `CHEBI:17750`
- L-glutamate — `CHEBI:29985`
- L-proline — `CHEBI:17203`
- ectoine — `CHEBI:42220`
- hydroxyectoine — label-only unless the exact ChEBI record is verified during curation
- trehalose — `CHEBI:27082`
- sucrose — `CHEBI:17992`

### Transporters, proteins, and complexes

- electrogenic Na+(K+)/H+ antiporter — label-only; use a specific GO/TCDB/UniProt identifier only after identifying the assayed paralog
- glycine-betaine ABC transporter, Opu family — label-only
- glycine-betaine ABC transporter, ProU family — label-only
- sodium/solute symporter, SSS family — label-only
- Na+-translocating F-type ATP synthase — label-only at complex level; subunits require organism-specific mapping
- sodium-translocating proteorhodopsin NaR, strain Omega — gene `CYPRO_0974`; retain as label plus locus tag until a verified UniProt record is selected
- choline-oxidation proteins associated with glycine-betaine synthesis — loci `CYPRO_1993`, `CYPRO_1995`, plus predicted aldehyde dehydrogenase(s); label-only
- acidic proteome / acidic proteins — collective molecular feature, not a single gene product
- respiratory chain — pathway/complex aggregate
- cytoplasmic membrane — `GO:0005886`

### Processes and functions

- cellular potassium-ion homeostasis — `GO:0030007`
- cellular sodium-ion homeostasis — `GO:0006883`
- intracellular pH homeostasis — `GO:0030003`
- response to osmotic stress — `GO:0006970`
- transmembrane transport — `GO:0055085`
- proton transmembrane transport — `GO:1902600`
- compatible-solute accumulation — label-only
- salt-in osmoadaptation — label-only
- cytoplasm acidification — label-only
- light-driven sodium export — label-only
- maintenance of osmotic balance — label-only
- protein solubility/stability at high ionic strength — label-only

### Taxa

- *Natranaerobius thermophilus* — use a verified NCBITaxon identifier during implementation
- strain Omega, deep-lineage Balneolaeota — retain strain label until its current valid taxonomic assignment and NCBITaxon record are checked
- *Natronomonas pharaonis* — organism example already supported by PMID:17203963; verify strain-specific NCBITaxon before YAML insertion

## 4. Candidate causal edges

The following table prioritizes edges sufficiently close to experimental observations for initial graph construction. “Snippet” is a short supporting extract or faithful near-verbatim statement from the retrieved article text.

| # | Subject–predicate–object | Supporting snippet | Reference | Evidence and curation note |
|---|---|---|---|---|
| 1 | high external salinity **increases** intracellular glycine betaine | “intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity” | Xing et al., 2024, DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24), published May 2024 | Direct metabolite measurements across 2.5–4.3 M Na+ with proteomics/ddPCR support; **high confidence, taxon-specific**. (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| 2 | high external salinity **increases** intracellular glutamate | Same snippet as edge 1 | Same reference | Direct measurement; **high confidence, taxon-specific**. (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| 3 | high external salinity **increases** intracellular proline | Same snippet as edge 1 | Same reference | Direct measurement; **high confidence, taxon-specific**. (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| 4 | compatible-solute accumulation **promotes** long-term salinity adaptation | “a hybrid strategy, combining the ‘compatible solute’ and ‘salt-in’ mechanisms, was utilized for osmotic adjustment” | Xing et al., 2024 | Supported by proteome, transcript, metabolite, and K+ measurements; **high confidence for *N. thermophilus***. (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| 5 | intracellular K+ accumulation **promotes** long-term salinity adaptation | “simultaneously accumulating compatible solutes and K+” | Xing et al., 2024 | Direct K+ quantification; represents the salt-in component. Do not generalize to all haloalkaliphilic bacteria. (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| 6 | Opu/ProU glycine-betaine ABC transporters **promote** compatible-solute accumulation | “employs the glycine betaine ABC transporters (Opu and ProU families)…to adapt to high salinity” | Xing et al., 2024 | Expression plus physiological correlation, but individual transporter knockouts were not reported in the retrieved evidence; **moderate-to-high, taxon-specific**. (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| 7 | SSS-family Na+/solute symporters **promote** osmoadaptation | “Na+/solute symporters (SSS family)…to adapt to high salinity” | Xing et al., 2024 | Multi-omics association; transport substrate and necessity may differ among paralogs. **Moderate; retain uncertainty**. (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| 8 | glutamate/proline synthesis pathways **increase** compatible-solute pools | “glutamate and proline synthesis pathways” accompany increased intracellular glutamate and proline | Xing et al., 2024 | Pathway-level inference supported by expression and metabolite data, not individual-gene perturbation. **Moderate-to-high**. (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| 9 | Na+/K+/H+ transporter upregulation **maintains** intracellular K+ and ion homeostasis | “upregulation of Na+/K+/H+ transporters facilitates the maintenance of intracellular K+ concentration” | Xing et al., 2024 | Proteomics, ddPCR, and ion measurements; paralog-specific causality unresolved. (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| 10 | electrogenic Na+(K+)/H+ antiporters **cause** cytoplasm acidification | “utilizes at least eight electrogenic Na+(K+)/H+ antiporters for cytoplasm acidification” | Mesbah et al., 2009, DOI: [10.1111/j.1365-2958.2009.06845.x](https://doi.org/10.1111/j.1365-2958.2009.06845.x), published October 2009 | Strong functional evidence in antiporter-deficient *E. coli* KNabc; activities spanned pH 7.8–10.0 with Na+ K0.5 of 1.0–4.4 mM. **High confidence, heterologous assay and taxon-specific**. (mesbah2009thehalophilicalkalithermophile pages 1-2) |
| 11 | cytoplasm acidification **promotes** intracellular pH homeostasis under alkaline conditions | *N. thermophilus* maintained a transmembrane pH gradient of about one pH unit over its growth range | Mesbah et al., 2009 | Direct physiology. This is a mechanistic bridge toward the trait, but growth impairment after antiporter deletion was not shown in the retrieved evidence. (mesbah2009thehalophilicalkalithermophile pages 1-2) |
| 12 | acidic proteome/cytoplasmic buffering **supports** cytoplasm acidification above optimal external pH | At high external pH, antiport ceased and acidification was attributed to “energy-independent physiochemical effects (cytoplasmic buffering) potentially mediated by an acidic proteome” | Mesbah et al., 2009 | Explicitly **proposed/potential**, not demonstrated as a molecular causal intervention; mark uncertain. (mesbah2009thehalophilicalkalithermophile pages 1-2) |
| 13 | sodium proteorhodopsin `CYPRO_0974` **causes** light-dependent Na+ export | “washed cells of Omega confirmed light-dependent sodium export” | Sorokin et al., 2018, DOI: [10.3389/fmicb.2018.02672](https://doi.org/10.3389/fmicb.2018.02672), published November 2018 | Strong washed-cell experiment: light-induced alkalinization required Na+ and was restored when Na+ was reintroduced. **High confidence for strain Omega**. (sorokin2018phenotypicandgenomic pages 6-7, sorokin2018phenotypicandgenomic pages 7-10, sorokin2018phenotypicandgenomic pages 1-2) |
| 14 | light **activates** sodium-proteorhodopsin-mediated Na+ export | Light-induced alkalinization occurred in Na+-containing medium but ceased when Na2SO4 was replaced with K2SO4 | Sorokin et al., 2018 | Direct controlled assay; suitable as an environmental-factor edge. (sorokin2018phenotypicandgenomic pages 6-7) |
| 15 | glycine-betaine, glutamine, proline, ectoine, and hydroxyectoine accumulation **supports** osmotic balance in soda-lake haloalkaliphiles | Review identifies these compatible solutes as one of two principal osmotic strategies | Sorokin et al., 2014, DOI: [10.1007/s00792-014-0670-9](https://doi.org/10.1007/s00792-014-0670-9), published August 2014 | **Generic review-supported edge**; split by chemical only when primary taxon-specific evidence is available. (sorokin2014microbialdiversityand pages 11-12) |
| 16 | elevated intracellular KCl **supports** osmotic balance | Review describes the “salt in cytoplasm” strategy and predominant K+ use by haloarchaea | Sorokin et al., 2014 | Broad mechanistic consensus, but not universal. **Taxon-dependent**. (sorokin2014microbialdiversityand pages 11-12) |
| 17 | low membrane H+/Na+ permeability **supports** pH and ion homeostasis | Review describes membrane stability and low proton/sodium permeability across pH and salinity ranges | Sorokin et al., 2014 | Structural mechanism is plausible but coarse-grained; curate only if the graph accepts review-level process nodes. (sorokin2014microbialdiversityand pages 11-12) |

The highest-confidence subset is summarized below.

| subject | predicate | object | organism | evidence/assay | confidence | DOI |
|---|---|---|---|---|---|---|
| Na+(K+)/H+ antiporters | cause | cytoplasm acidification | *Natranaerobius thermophilus* | Functional characterization in antiporter-deficient *E. coli* KNabc; overlapping pH profiles and Na+ K0.5 values; direct physiology (mesbah2009thehalophilicalkalithermophile pages 1-2) | high | https://doi.org/10.1111/j.1365-2958.2009.06845.x |
| increasing external salinity | increases | intracellular glycine betaine, glutamate, and proline | *Natranaerobius thermophilus* | iTRAQ proteomics + ddPCR + intracellular metabolite quantification across 2.5–4.3 M Na+ (xing2024thepolyextremophilenatranaerobius pages 1-2) | high | https://doi.org/10.1128/aem.00145-24 |
| glycine betaine ABC transporters (Opu, ProU families), Na+/solute symporters (SSS family), and glutamate/proline synthesis pathways | support | osmoadaptation to high salinity | *Natranaerobius thermophilus* | Multi-omics correlation with rising salinity; transporter/pathway upregulation plus solute measurements (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 10-14) | high | https://doi.org/10.1128/aem.00145-24 |
| upregulated Na+/K+/H+ transporters | maintain | intracellular K+ concentration / ion homeostasis | *Natranaerobius thermophilus* | Proteomics + transcript validation + intracellular K+ measurements under salt stress (xing2024thepolyextremophilenatranaerobius pages 1-2) | high | https://doi.org/10.1128/aem.00145-24 |
| K+ accumulation | supports | osmotic homeostasis (salt-in component) | *Natranaerobius thermophilus* | Direct intracellular K+ increase accompanying long-term salinity adaptation (xing2024thepolyextremophilenatranaerobius pages 1-2) | high | https://doi.org/10.1128/aem.00145-24 |
| acidic proteome / cytoplasmic buffering | supports | cytoplasm acidification at higher external pH | *Natranaerobius thermophilus* | Physiological inference from cessation of electrogenic antiport at high pH and proposed buffering by acidic proteome (mesbah2009thehalophilicalkalithermophile pages 1-2) | medium | https://doi.org/10.1111/j.1365-2958.2009.06845.x |
| sodium-translocating proteorhodopsin | causes | light-dependent Na+ export | strain Omega (deep-lineage Balneolaeota) | Washed-cell light experiments with Na+-dependent alkalinization and sodium replacement controls (sorokin2018phenotypicandgenomic pages 6-7, sorokin2018phenotypicandgenomic pages 7-10, sorokin2018phenotypicandgenomic pages 1-2) | high | https://doi.org/10.3389/fmicb.2018.02672 |


*Table: Compact summary of the strongest directly supported causal triples relevant to haloalkaliphily. It emphasizes experimentally demonstrated transport and osmoadaptation mechanisms that are most suitable for initial TraitMech curation.*

## 5. Suggested graph architecture

A conservative TraitMech graph can be organized as two converging modules:

1. **Osmotic module:** high external salinity → Opu/ProU/SSS transport and glutamate/proline synthesis → compatible-solute accumulation; in parallel, transporter regulation → K+ accumulation → osmotic/ion homeostasis.
2. **Alkaline-pH module:** alkaline external pH plus external Na+ → electrogenic Na+(K+)/H+ antiport → proton entry/cytoplasm acidification → intracellular pH homeostasis.
3. **Optional taxon-specific energy module:** light → NaR `CYPRO_0974` → Na+ export/sodium-motive force. This should be a strain-Omega branch, not a universal haloalkaliphilic mechanism.
4. **Outcome:** osmotic homeostasis plus intracellular pH homeostasis **enables** growth under combined high-salt/alkaline conditions → `METPO:1000621`.

The final “enables haloalkaliphilic growth” links are biologically compelling but should be marked as integrative unless supported by knockout, inhibition, or complementation under factorial salt–pH growth assays.

## 6. Recent developments and quantitative findings

The principal 2024 advance is direct support for a **hybrid**, rather than binary, osmoadaptation model in *N. thermophilus*. Across 2.5–4.3 M Na+, 109 upregulated proteins were examined; ddPCR agreed with protein-expression direction for 107/109 genes (98.2%), and 90.8% were significantly upregulated using the study’s FC ≥1.5 and *P*<0.05 criteria. Four proteins exceeded 100-fold upregulation, including extracellular solute-binding protein B2A2×8 and sodium:neurotransmitter symporter B2A796. Amino-acid transport/metabolism represented 27.5% and energy production/conversion 22.9% of co-upregulated functional assignments. (xing2024thepolyextremophilenatranaerobius pages 10-14) These results support transporter, compatible-solute, energy, and ion-homeostasis nodes, but fold changes alone do not prove indispensability.

The study also observed cytoplasmic acidification at high Na+ and progressively lower median isoelectric points among upregulated proteins, linking salt adaptation to pH/protein-charge adaptation. (xing2024thepolyextremophilenatranaerobius pages 1-2) This is especially relevant to a joint haloalkaline graph, although the causal direction between proteome acidity and cytoplasmic pH remains unresolved.

Strain Omega provides a rare direct demonstration that a microbial rhodopsin can participate in sodium energetics under haloalkaline conditions. It contains NaR locus `CYPRO_0974` with the characteristic NDQ motif, and washed-cell assays established Na+-dependent, light-driven export rather than relying only on sequence annotation. (sorokin2018phenotypicandgenomic pages 6-7, sorokin2018phenotypicandgenomic pages 4-6)

## 7. Applications and real-world relevance

Haloalkaliphilic mechanisms are relevant to processes where ordinary production organisms or enzymes fail because streams are both saline and alkaline. Current application areas include extremozymes, saline/alkaline waste treatment, sulfur remediation, compatible-solute production, and haloarchaeal chassis for green chemistry. The 2024 haloarchaeal-chassis review identifies the limited genetic toolkit and difficulty producing correctly folded halophilic enzymes as major implementation bottlenecks; it argues that native extremophilic chassis could enable functional extremozymes for industrial synthesis. (bonnaud2024haloarchaeaaspromising pages 2-4)

Ecologically, soda lakes support carbon, nitrogen, and sulfur cycling under stable carbonate alkalinity and high salinity. Their organisms provide alkaline- and salt-active enzymes, while sulfur-cycle organisms have been proposed for sulfur remediation. (sorokin2014microbialdiversityand pages 11-12, sorokin2014microbialdiversityand pages 6-8) These are genuine translational opportunities, but most remain strain discovery, enrichment-culture, enzyme-screening, or platform-development activities rather than mature full-scale installations.

The mechanistic graph also has engineering value: Opu/ProU/SSS transport, compatible-solute synthesis, K+ homeostasis, and cation/proton antiport are candidate modules for constructing salt/alkali-robust production hosts. However, transplanting a single transporter is unlikely to reproduce haloalkaliphily because membrane permeability, protein surface chemistry, ATP/sodium energetics, and regulation are coupled.

## 8. Expert interpretation

Three conclusions are sufficiently established for curation:

1. **Haloalkaliphily is mechanistically plural.** Haloarchaea, anaerobic bacteria, and aerobic soda-lake bacteria do not share one universal adaptation cassette.
2. **pH and salt adaptations are coupled.** Na+-dependent proton antiport simultaneously affects Na+ exclusion, proton uptake, membrane potential, and cytoplasmic pH. Treating “halophily” and “alkaliphily” as independent parallel traits would miss this coupling.
3. **The best graph is modular and evidence-qualified.** Directly assayed antiport, solute/K+ measurements, and sodium pumping should form the core. Acidic-proteome buffering, membrane-lipid effects, and genome-predicted pathways belong in taxon-specific or uncertain extensions.

## 9. Warnings: claims not yet ready for unqualified curation

- Do **not** infer haloalkaliphily from a soda-lake source, metagenomic abundance, or gene inventory alone.
- Do **not** assert that all haloalkaliphiles use both salt-in and compatible-solute strategies; the dual strategy is directly supported here for *N. thermophilus*. (xing2024thepolyextremophilenatranaerobius pages 1-2)
- Do **not** make sodium proteorhodopsin universal. The direct evidence is strain-specific to Omega. (sorokin2018phenotypicandgenomic pages 1-2)
- Do **not** equate transporter upregulation with necessity. Opu, ProU, SSS, ATPase, and individual antiporter paralogs need deletion/complementation or specific inhibition for gene-level “required for” edges.
- The acidic-proteome → cytoplasmic buffering edge is explicitly proposed rather than directly perturbed and should remain uncertain. (mesbah2009thehalophilicalkalithermophile pages 1-2)
- Na+-translocating F-type ATP synthase should not automatically be annotated as ATP-producing or Na+-exporting without directionality measurements; F-type complexes can operate differently with physiological state.
- Compatible-solute biosynthesis predicted from loci such as `CYPRO_1993`/`CYPRO_1995` is weaker than direct metabolite-flux evidence. (sorokin2018phenotypicandgenomic pages 6-7)
- Keep *Natronomonas pharaonis* as a validated organism example, but do not transfer mechanisms from *N. thermophilus* or strain Omega to it without organism-specific evidence.
- Verify all NCBITaxon, UniProt, GO, ENVO, Rhea, and KEGG identifiers against current releases before committing YAML. Locus tags are not substitutes for stable cross-species ontology terms.

## 10. DOI-first bibliography

1. Xing Q, Zhang S, Tao X, et al. **The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.** *Applied and Environmental Microbiology*. Published May 2024. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 1-2)
2. Mesbah NM, Cook GM, Wiegel J. **The halophilic alkalithermophile *Natranaerobius thermophilus* adapts to multiple environmental extremes using a large repertoire of Na+(K+)/H+ antiporters.** *Molecular Microbiology*. Published October 2009. DOI: [10.1111/j.1365-2958.2009.06845.x](https://doi.org/10.1111/j.1365-2958.2009.06845.x). (mesbah2009thehalophilicalkalithermophile pages 1-2)
3. Sorokin DY, Muntyan MS, Toshchakov SV, Korzhenkov A, Kublanov IV. **Phenotypic and genomic properties of a novel deep-lineage haloalkaliphilic member of the phylum Balneolaeota from soda lakes possessing Na+-translocating proteorhodopsin.** *Frontiers in Microbiology*. Published November 2018. DOI: [10.3389/fmicb.2018.02672](https://doi.org/10.3389/fmicb.2018.02672). (sorokin2018phenotypicandgenomic pages 6-7, sorokin2018phenotypicandgenomic pages 1-2)
4. Bonnaud E, Oger PM, Ohayon A, Louis Y. **Haloarchaea as promising chassis to green chemistry.** *Microorganisms*. Published August 2024. DOI: [10.3390/microorganisms12081738](https://doi.org/10.3390/microorganisms12081738). (bonnaud2024haloarchaeaaspromising pages 2-4)
5. Sorokin DY, Berben T, Melton ED, Overmars L, Vavourakis CD, Muyzer G. **Microbial diversity and biogeochemical cycling in soda lakes.** *Extremophiles*. Published August 2014. DOI: [10.1007/s00792-014-0670-9](https://doi.org/10.1007/s00792-014-0670-9). (sorokin2014microbialdiversityand pages 11-12, sorokin2014microbialdiversityand pages 6-8)
6. Mesbah NM, Wiegel J. **Life at extreme limits.** *Annals of the New York Academy of Sciences*. Published March 2008. DOI: [10.1196/annals.1419.028](https://doi.org/10.1196/annals.1419.028). (mesbah2008lifeatextreme pages 11-12)

## Curation recommendation

For the first revision of `data/traits/environment/haloalkaliphilic.yaml`, prioritize edges 1–11 and 13–14, with organism and assay qualifiers. Treat edges 12 and 15–17 as uncertain background extensions. The core graph should converge on two proximal causal processes—**osmotic/ion homeostasis** and **intracellular pH homeostasis**—that jointly enable optimal growth at high salinity and alkaline pH.

References

1. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

2. (sorokin2018phenotypicandgenomic pages 1-2): Dimitry Y. Sorokin, Maria S. Muntyan, Stepan V. Toshchakov, Aleksei Korzhenkov, and Ilya V. Kublanov. Phenotypic and genomic properties of a novel deep-lineage haloalkaliphilic member of the phylum balneolaeota from soda lakes possessing na+-translocating proteorhodopsin. Frontiers in Microbiology, Nov 2018. URL: https://doi.org/10.3389/fmicb.2018.02672, doi:10.3389/fmicb.2018.02672. This article has 32 citations and is from a peer-reviewed journal.

3. (bonnaud2024haloarchaeaaspromising pages 2-4): Emma Bonnaud, Philippe M. Oger, Avigaël Ohayon, and Yoann Louis. Haloarchaea as promising chassis to green chemistry. Microorganisms, 12:1738, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081738, doi:10.3390/microorganisms12081738. This article has 8 citations.

4. (mesbah2009thehalophilicalkalithermophile pages 1-2): Noha M. Mesbah, Gregory M. Cook, and Juergen Wiegel. The halophilic alkalithermophile <i>natranaerobius thermophilus</i> adapts to multiple environmental extremes using a large repertoire of na<sup>+</sup>(k<sup>+</sup>)/h<sup>+</sup> antiporters. Oct 2009. URL: https://doi.org/10.1111/j.1365-2958.2009.06845.x, doi:10.1111/j.1365-2958.2009.06845.x. This article has 109 citations and is from a domain leading peer-reviewed journal.

5. (sorokin2018phenotypicandgenomic pages 6-7): Dimitry Y. Sorokin, Maria S. Muntyan, Stepan V. Toshchakov, Aleksei Korzhenkov, and Ilya V. Kublanov. Phenotypic and genomic properties of a novel deep-lineage haloalkaliphilic member of the phylum balneolaeota from soda lakes possessing na+-translocating proteorhodopsin. Frontiers in Microbiology, Nov 2018. URL: https://doi.org/10.3389/fmicb.2018.02672, doi:10.3389/fmicb.2018.02672. This article has 32 citations and is from a peer-reviewed journal.

6. (sorokin2018phenotypicandgenomic pages 7-10): Dimitry Y. Sorokin, Maria S. Muntyan, Stepan V. Toshchakov, Aleksei Korzhenkov, and Ilya V. Kublanov. Phenotypic and genomic properties of a novel deep-lineage haloalkaliphilic member of the phylum balneolaeota from soda lakes possessing na+-translocating proteorhodopsin. Frontiers in Microbiology, Nov 2018. URL: https://doi.org/10.3389/fmicb.2018.02672, doi:10.3389/fmicb.2018.02672. This article has 32 citations and is from a peer-reviewed journal.

7. (sorokin2014microbialdiversityand pages 11-12): Dimitry Y. Sorokin, Tom Berben, Emily Denise Melton, Lex Overmars, Charlotte D. Vavourakis, and Gerard Muyzer. Microbial diversity and biogeochemical cycling in soda lakes. Extremophiles, 18:791-809, Aug 2014. URL: https://doi.org/10.1007/s00792-014-0670-9, doi:10.1007/s00792-014-0670-9. This article has 438 citations and is from a peer-reviewed journal.

8. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

9. (sorokin2018phenotypicandgenomic pages 4-6): Dimitry Y. Sorokin, Maria S. Muntyan, Stepan V. Toshchakov, Aleksei Korzhenkov, and Ilya V. Kublanov. Phenotypic and genomic properties of a novel deep-lineage haloalkaliphilic member of the phylum balneolaeota from soda lakes possessing na+-translocating proteorhodopsin. Frontiers in Microbiology, Nov 2018. URL: https://doi.org/10.3389/fmicb.2018.02672, doi:10.3389/fmicb.2018.02672. This article has 32 citations and is from a peer-reviewed journal.

10. (sorokin2014microbialdiversityand pages 6-8): Dimitry Y. Sorokin, Tom Berben, Emily Denise Melton, Lex Overmars, Charlotte D. Vavourakis, and Gerard Muyzer. Microbial diversity and biogeochemical cycling in soda lakes. Extremophiles, 18:791-809, Aug 2014. URL: https://doi.org/10.1007/s00792-014-0670-9, doi:10.1007/s00792-014-0670-9. This article has 438 citations and is from a peer-reviewed journal.

11. (mesbah2008lifeatextreme pages 11-12): Noha M. Mesbah and Juergen Wiegel. Life at extreme limits. Annals of the New York Academy of Sciences, 1125:44-57, Mar 2008. URL: https://doi.org/10.1196/annals.1419.028, doi:10.1196/annals.1419.028. This article has 134 citations and is from a peer-reviewed journal.