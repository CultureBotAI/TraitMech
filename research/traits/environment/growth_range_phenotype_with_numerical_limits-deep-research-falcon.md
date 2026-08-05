---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:44:08.906745'
end_time: '2026-08-04T00:51:15.318623'
duration_seconds: 426.41
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: growth range phenotype with numerical limits
  trait_identifier: METPO:1000535
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: growth_range_phenotype_with_numerical_limits
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by the span of values within which an organism
    can maintain growth.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports the bounded span of a growth-supporting environmental variable as a standard
    quantitative descriptor.) | DOI:10.1038/nrmicro2549: external pH (pH-homeostasis
    review supports the external-pH range over which cytoplasmic pH homeostasis sustains
    growth as an analogous range descriptor on the pH axis.)'
  causal_graph_summary: 'growth_range_phenotype_descriptor: 15 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** growth range phenotype with numerical limits
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000535
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the span of values within which an organism can maintain growth.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the bounded span of a growth-supporting environmental variable as a standard quantitative descriptor.) | DOI:10.1038/nrmicro2549: external pH (pH-homeostasis review supports the external-pH range over which cytoplasmic pH homeostasis sustains growth as an analogous range descriptor on the pH axis.)
- **Existing causal graph summary:** growth_range_phenotype_descriptor: 15 nodes, 12 edges

## Research Objective

Research the microbial trait **growth range phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/growth_range_phenotype_with_numerical_limits.yaml`.

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
- **Trait label:** growth range phenotype with numerical limits
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000535
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the span of values within which an organism can maintain growth.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the bounded span of a growth-supporting environmental variable as a standard quantitative descriptor.) | DOI:10.1038/nrmicro2549: external pH (pH-homeostasis review supports the external-pH range over which cytoplasmic pH homeostasis sustains growth as an analogous range descriptor on the pH axis.)
- **Existing causal graph summary:** growth_range_phenotype_descriptor: 15 nodes, 12 edges

## Research Objective

Research the microbial trait **growth range phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/growth_range_phenotype_with_numerical_limits.yaml`.

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


# Curation report: growth range phenotype with numerical limits

## Executive summary

**Target:** `METPO:1000535` — *growth range phenotype with numerical limits*  
**Category:** ENVIRONMENT | **Kind:** CLASS | **Status:** REVIEWED  
**Definition supplied:** “A phenotype characterized by the span of values within which an organism can maintain growth.”

The most defensible interpretation is an **assay-qualified numerical interval on one environmental axis**—for example, `[pHmin, pHmax]`, `[Tmin, Tmax]`, or `[Na+min, Na+max]`—within which a specified organism shows a predefined growth endpoint. It is a phenotype descriptor, not itself a single universal mechanism. Mechanistic child graphs should therefore be axis-specific and should connect environmental stress to homeostatic processes and then to observed lower or upper growth boundaries.

A range must not be conflated with an optimum, maximal growth rate, survival without proliferation, or a model-extrapolated boundary. This distinction is experimentally consequential: neutralophilic bacteria commonly grow at external pH 5.5–9.0 while maintaining cytoplasmic pH around 7.5–7.7, whereas *Escherichia coli* and *Salmonella* can survive stomach acidity without growing there. Extremophile occurrence at pH below 3 or above 11 likewise does not establish every strain’s measured growth interval. (krulwich2011molecularaspectsof pages 1-3)

Recent work strengthens three mechanistic graph branches: (i) PMF and proton-ion antiporters supporting pH homeostasis; (ii) compatible-solute, K+, and transporter systems supporting high-salinity growth; and (iii) respiratory-chain branching supporting growth over different oxygen concentrations. However, most studies measure adaptation within a range rather than showing that deletion or gain of one mechanism moves both numerical limits. Accordingly, many edges should be represented as **taxon- and assay-qualified contributors**, not universal causes of “wider growth range.”

## 1. Trait scope and boundary cases

### 1.1 Recommended formal interpretation

A record for `METPO:1000535` should minimally contain:

- organism and preferably strain;
- environmental variable and unit;
- observed lower and upper limits;
- evidence that growth—not merely viability—occurred at each boundary;
- growth endpoint, detection threshold, incubation duration, medium, atmosphere, inoculum, and replication;
- values of major interacting variables, especially temperature, pH, salinity/water activity, oxygen, nutrients, and pressure;
- whether each limit was directly observed, interval-censored, or estimated by a model.

A useful representation is:

`growth_range(axis X) = [lowest tested X supporting criterion G, highest tested X supporting criterion G] under assay A`.

The bounds are often interval-censored: if growth occurs at 35°C but not 37°C, the biological upper limit lies between those test values unless a validated model is used. Even then, the fitted value remains model-dependent.

### 1.2 Nearby traits that must remain separate

1. **Growth optimum:** `Xopt` is the value maximizing growth rate, not the span supporting growth.
2. **Minimum or maximum alone:** these are boundary traits; together they constitute a range.
3. **Growth rate or lag time:** kinetic phenotypes within the range, not the range itself.
4. **Survival/tolerance:** recovery of viable cells after exposure does not demonstrate net growth. The stomach-acid and alkaline-seawater examples for *E. coli* illustrate this distinction. (krulwich2011molecularaspectsof pages 1-3)
5. **Environmental preference:** habitat association or an optimum is not equivalent to experimentally observed limits.
6. **Multivariate growth/no-growth boundary:** pH–temperature–water-activity response surfaces are not reducible to an intrinsic one-dimensional range unless all other variables are fixed.
7. **Adaptation/acclimation:** stress-responsive expression within a tested interval may explain growth capacity but does not by itself prove expansion of that interval.
8. **Theoretical model output:** a nonphysical fitted minimum must not be curated as an observed phenotype.

A 2024 fungal study illustrates these distinctions. For *Mucor circinelloides* on cheese-based agar, estimated `Topt` was 32.1–32.5°C and `Tmax` was 37.2–37.3°C without added salt. Addition of 1% NaCl reduced optimal surface growth rate by about 46% and lowered estimated `Tmax` to 35.1°C. In contrast, fitted negative `Tmin` values were explicitly described as theoretical outputs. Thus, optimum, upper boundary, kinetic rate, and invalid extrapolated lower boundary are separate data objects. (konuchova2024characterisationofthe pages 1-2)

## 2. Candidate nodes grouped by type

### 2.1 Trait and assay nodes

- `METPO:1000535` — growth range phenotype with numerical limits.
- `METPO:1000059` — supplied parent trait.
- Lower numerical growth limit — label-only candidate.
- Upper numerical growth limit — label-only candidate.
- Growth/no-growth endpoint — label-only candidate.
- Cardinal growth parameters: `Xmin`, `Xopt`, `Xmax` — label-only candidates.
- Incubation duration, detection threshold, medium composition, inoculum, and primary/secondary growth model — experimental-factor nodes.

### 2.2 Environmental and physicochemical nodes

- External pH.
- Temperature.
- Salinity; NaCl concentration; sodium-ion concentration.
- Osmolality/osmolarity and water activity.
- Dissolved oxygen concentration.
- Extracellular proton concentration, ion gradients, and osmotic pressure.
- Candidate chemical grounding: proton `CHEBI:15378`; sodium ion `CHEBI:29101`; potassium ion `CHEBI:29103`; chloride `CHEBI:17996`; water `CHEBI:15377`; dioxygen `CHEBI:15379`; glycine betaine `CHEBI:17750`; L-glutamate `CHEBI:29985`; L-proline `CHEBI:17203`. These identifiers should still be validated against the project’s ontology release before commit.

### 2.3 Cellular structures and localizations

- Cytoplasmic membrane / plasma membrane — `GO:0005886`.
- Cytoplasm — `GO:0005737`.
- Cell wall and peptidoglycan sacculus — label-only unless the project selects a specific ontology term.
- Respiratory-chain membrane complexes.
- Anammoxosome/ladderane membrane only for anammox-specific extensions; not a generic node.

### 2.4 Biological processes and molecular functions

- Cytoplasmic pH homeostasis — `GO:0030641`.
- Proton transmembrane transport — `GO:1902600`.
- Ion transmembrane transport — `GO:0034220`.
- Osmoregulation — `GO:0006970`.
- Response to osmotic stress — `GO:0006970` is often used at this level; verify whether the desired graph distinguishes response from regulation.
- Cellular potassium-ion homeostasis — candidate GO grounding should be verified locally.
- Proton motive force and membrane potential generation — label-only candidates if no exact project-approved GO term is selected.
- Compatible-solute accumulation/import/biosynthesis.
- Homeoviscous adaptation and membrane-lipid remodeling.
- Aerobic respiration / electron-transport chain.
- Protein folding and heat-shock response.

### 2.5 Genes, proteins, transporters, and complexes

**pH branch**

- NhaA-like and NhaB-like cation/proton antiporters.
- ClcA-like chloride/proton antiporter.
- Mrp multisubunit Na+/H+ antiporter.
- F1Fo ATP synthase.
- Central-metabolism proton-export processes.
- Urease and ammonia production for acid neutralization, particularly in *Helicobacter pylori*; useful as a taxon-specific branch, not a universal mechanism. (wani2022microbialadaptationto pages 5-8)

**Salinity/osmolarity branch**

- Opu-family and ProU-family glycine-betaine ABC transporters.
- SSS-family Na+/solute symporters.
- Na+/K+/H+ transporters.
- K+ uptake/efflux systems.
- Mechanosensitive channels.
- c-di-AMP signaling machinery.
- Ectoine, glycine-betaine, glutamate, proline, and trehalose biosynthesis/import modules.

**Oxygen branch**

- Type I and type II NADH dehydrogenases.
- Cytochrome-c oxidases aa3, ba3, and bb3.
- Menaquinol:oxygen bd oxidase.
- Succinate dehydrogenase and fumarate reductase.

**Temperature branch**

- Fatty-acid and membrane-lipid remodeling enzymes.
- Molecular chaperones and protein-folding machinery.
- Reverse gyrase/topoisomerase systems as taxon-specific hyperthermophile candidates.

Gene-family labels should not be assigned a single UniProt CURIE without a strain-specific protein accession. The current evidence frequently concerns families or inferred genome annotations rather than a unique protein product.

## 3. Candidate causal edges

The following table summarizes graph architecture and curation priority.

| Environmental axis | Subject | Predicate | Object | Taxon/context | Evidence class | Curation status |
|---|---|---|---|---|---|---|
| External pH | proton motive force (PMF) | enables maintenance of | cytoplasmic pH homeostasis | *Escherichia coli*; extracellular pH shifts; PMF reduction impairs pH maintenance (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9) | direct experimental, model-supported | curate with taxon/context qualifier |
| External pH | proton-ion antiporters | generate/support | membrane potential and PMF | *Escherichia coli*; antiporter-centered electrophysiology model with experimental support (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9) | model-supported, direct experimental | curate as qualified/mechanistic, not universal |
| External pH | external pH range | constrains | growth-supporting interval via need for cytoplasmic pH homeostasis | bacteria broadly; neutralophiles vs extremophiles; growth/survival distinction emphasized (krulwich2011molecularaspectsof pages 1-3) | review synthesis | curate at high level only |
| Osmolarity / salinity | increase or decrease in external osmolarity | causes | water flux across cytoplasmic membrane | bacteria broadly (bremer2019responsesofmicroorganisms pages 1-2) | review synthesis | curate |
| Osmolarity / salinity | water flux across cytoplasmic membrane | disrupts | cellular hydration, molecular crowding, turgor, and integrity | bacteria broadly (bremer2019responsesofmicroorganisms pages 1-2) | review synthesis | curate |
| High salinity | compatible solute accumulation | enables | osmotic adjustment / adaptation to high salinity | *Natranaerobius thermophilus*; glycine betaine, glutamate, proline increase with salinity (xing2024thepolyextremophilenatranaerobius pages 1-2) | direct experimental | curate with taxon qualifier |
| High salinity | K+ accumulation / intracellular K+ maintenance | supports | osmotic adjustment / ion homeostasis under varying salinities | *Natranaerobius thermophilus*; linked to upregulated Na+/K+/H+ transporters (xing2024thepolyextremophilenatranaerobius pages 1-2) | direct experimental | curate with taxon qualifier |
| High salinity | glycine betaine ABC transporters (Opu, ProU), Na+/solute symporters, glutamate/proline synthesis pathways | contribute to | salinity adaptation | *Natranaerobius thermophilus* under 2.5-4.3 M Na+ at pH 9.5, 53°C (xing2024thepolyextremophilenatranaerobius pages 1-2) | direct experimental | curate with taxon qualifier |
| Dissolved oxygen | branched respiratory chain | facilitates growth across | a wide range of dissolved oxygen levels | *Caldalkalibacillus thermarum* chemostats, 0.25%-4.2% O2 (jong2024quantitativeproteomicsreveals pages 1-2) | direct experimental | curate with taxon qualifier |
| Dissolved oxygen | terminal oxidase abundance switching (aa3 vs ba3) | adapts respiration to | different oxygen levels | *Caldalkalibacillus thermarum*; aa3 highest at 4.2% O2, ba3 declines below 0.42% O2 (jong2024quantitativeproteomicsreveals pages 1-2) | direct experimental | curate with taxon qualifier |
| Temperature | lipid composition remodeling / homeoviscous adaptation | maintains | membrane fluidity and stability under temperature stress | extremophiles broadly (maiti2024extrememakeoverthe pages 1-2) | review synthesis | curate at high level only |
| Temperature | membrane lipid remodeling | contributes to | thermal adaptation / thermal resilience | extremophiles and stress biology broadly (maiti2024extrememakeoverthe pages 1-2) | review synthesis | curate cautiously; broad mechanism |
| Salinity + pH | Na+/H+ antiporters | maintain | reverse ΔpH / intracellular pH homeostasis in alkaline environments | alkaliphilic *Bacillus* and related alkaliphiles (maksimova2024metabolicandmorphological pages 1-2) | review synthesis within primary study background | curate cautiously; not direct perturbation in this paper |
| Salinity + pH | broader resistance phenotype | associated with | maintenance of ΔpH and reduced cell damage under low pH/high salt challenge | *Bacillus aequororis* 5-DB vs *B. subtilis* ATCC 6633 (maksimova2024metabolicandmorphological pages 1-2) | quantitative association | hold for prose; not a clean mechanistic edge |
| NaCl / temperature | 1% NaCl addition | reduces | optimal surface growth rate | *Mucor circinelloides* on cheese-based agar (konuchova2024characterisationofthe pages 1-2) | quantitative association | curate as assay-specific phenotype modifier |
| NaCl / temperature | 1% NaCl addition | decreases | estimated Tmax by ~2°C | *Mucor circinelloides* on cheese-based agar cardinal model (konuchova2024characterisationofthe pages 1-2) | quantitative association, model-supported | curate as assay/model-specific |
| Measurement / modeling | cardinal model estimated Tmin | yields | theoretical negative Tmin values | *Mucor circinelloides* growth modeling (konuchova2024characterisationofthe pages 1-2) | model-supported | do not curate as biological mechanism |
| Measurement / modeling | primary model choice (Baranyi vs Huang) | alters | estimated lag phase and surface growth rate parameters | *Mucor circinelloides* on cheese-based agar (konuchova2024characterisationofthe pages 1-2) | quantitative association | curate only as measurement-model artifact |
| Growth range phenotype scope | growth-supporting interval | is distinct from | optimum, growth rate, and survival-only tolerance | bacteria broadly; pH case explicitly distinguishes survival from growth (krulwich2011molecularaspectsof pages 1-3, konuchova2024characterisationofthe pages 1-2) | review synthesis, quantitative association | curate as scope note, not causal edge |


*Table: This table compiles the strongest candidate causal edges relevant to the growth range phenotype with numerical limits, emphasizing mechanisms that expand or constrain growth-supporting intervals across environmental axes. It is useful for prioritizing curation-ready edges versus assay-specific or model-dependent findings.*

### 3.1 Evidence table with supporting snippets

| Proposed subject–predicate–object triple | Reference and supporting snippet | Interpretation and curation note |
|---|---|---|
| **PMF — enables — cytoplasmic pH homeostasis** | Terradot et al. (published 27 Nov 2024): “decreasing the PMF’s strength impairs the cells’ ability to maintain pH”; “a lower magnitude PMF impaired their maintenance of pHi.” DOI: [10.1103/PRXLife.2.043015](https://doi.org/10.1103/PRXLife.2.043015). (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9) | Strongest pH-mechanism edge. The PMF perturbation is experimental, but the broader claim that PMF determines the entire external-pH growth interval remains partly model-mediated. Curate for *E. coli* with assay context. |
| **proton-ion antiporters — support/generate — membrane potential and PMF** | Terradot et al.: “we predict that E. coli also uses proton-ion antiporters”; the authors experimentally found that collapsing PMF depolarized cells, while antiporter-specific operating ranges were model predictions. Predicted least-cost ranges were approximately pH 2–5 for ClcA-like, 5–9 for NhaB-like, and 9–12 for NhaA-like transport. (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9) | Mixed evidence. Curate the mechanistic relation as **model-supported**; do not encode the predicted pH partitions as experimentally measured growth ranges. |
| **external pH outside the homeostatic capacity — prevents — growth** | Krulwich et al. report that most bacteria grow outside their narrow cytoplasmic-pH interval by using sensing and homeostasis systems; neutralophiles grow at external pH 5.5–9.0 while maintaining pHi 7.5–7.7. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549), published May 2011. (krulwich2011molecularaspectsof pages 1-3) | Authoritative review-level mechanism. Appropriate as a high-level edge, with organism-specific measured ranges stored separately. |
| **external osmolarity change — causes — transmembrane water flux** | Bremer and Krämer: “Both increases and decreases in the external osmolarity inevitably trigger water fluxes across the cytoplasmic membrane.” DOI: [10.1146/annurev-micro-020518-115504](https://doi.org/10.1146/annurev-micro-020518-115504), published 2019. (bremer2019responsesofmicroorganisms pages 1-2) | Curation-ready general biophysical edge. |
| **hyperosmotic water loss — decreases — hydration and turgor** | The same review states that water exit under hyperosmotic conditions causes “cytoplasmic dehydration and a drop in turgor to physiologically nonsustainable values.” It identifies turgor as critical for growth and viability. (bremer2019responsesofmicroorganisms pages 1-2) | Curation-ready mechanistic chain connecting high osmolarity to an upper salinity/lower-water-activity boundary. |
| **hypoosmotic water influx — threatens — cellular integrity through excessive turgor** | Bremer and Krämer: excessive water influx under hypoosmotic conditions threatens integrity through increased turgor. Reported turgor estimates span 30–300 kPa in *E. coli* and approximately 1.9 MPa in *Bacillus subtilis*. (bremer2019responsesofmicroorganisms pages 1-2) | Curation-ready, although the numerical turgor values are method-dependent and are not growth-range limits. Mechanosensitive-channel edges require more direct source extraction before inclusion. |
| **compatible-solute accumulation — supports — long-term high-salinity adaptation** | Xing et al. (published 5 Apr 2024) found that glycine betaine, glutamate, and proline increased with salinity in *Natranaerobius thermophilus*. The organism grows at 3.1–4.9 M Na+ and optimally at 3.3–3.9 M Na+; proteomics compared 2.5, 3.1, 3.7, and 4.3 M Na+ at pH 9.5 and 53°C. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 1-2) | Strong quantitative association and mechanistic multi-omics support. Because no knockout moved the range boundary, use “contributes to” rather than “widens.” |
| **Opu/ProU transporters and SSS symporters — contribute to — salinity adaptation** | Xing et al.: the organism “employs the glycine betaine ABC transporters (Opu and ProU families), Na+/solute symporters (SSS family), and glutamate and proline synthesis pathways to adapt to high salinity.” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Curate with strain and condition qualifiers. Evidence combines protein/mRNA/metabolite responses; it is stronger than genome-presence inference but weaker than transporter knockout/complementation. |
| **Na+/K+/H+ transporter upregulation — supports — intracellular K+ maintenance and ion homeostasis** | Xing et al.: “upregulation of Na+/K+/H+ transporters facilitates the maintenance of intracellular K+ concentration, ensuring cellular ion homeostasis under varying salinities.” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Curate as taxon-specific, with evidence class “multi-omics association/mechanistic interpretation.” Avoid claiming universal bacterial action. |
| **compatible-solute import — restores — growth under high salinity** | In *Clostridioides difficile*, 350 mM NaCl significantly reduced growth; carnitine, glycine betaine, γ-butyrobetaine, crotonobetaine, homobetaine, proline-betaine, and DMSP restored growth, whereas choline and proline did not. An OpuF-type ABC transporter imported most effective solutes. DOI: [10.1111/1462-2920.15925](https://doi.org/10.1111/1462-2920.15925), published 2022. (michel2022cellularadaptationof pages 1-1) | Excellent intervention evidence for substrate-specific osmoprotection. Curate individual solute→growth-restoration edges only with the high-salt assay context; this demonstrates rescue at 350 mM, not an entire revised numerical range. |
| **branched respiratory chain — facilitates — growth across dissolved-oxygen levels** | de Jong et al. (published 28 Oct 2024) state that the branched respiratory chain facilitates growth over a wide oxygen range. Chemostats covered 0.25–4.2% O2. DOI: [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929). (jong2024quantitativeproteomicsreveals pages 1-2) | Curate for *Caldalkalibacillus thermarum* TA2.A1. It is a tested operating interval, not necessarily the species’ complete minimum–maximum oxygen range. |
| **oxygen level — regulates — aa3/ba3 terminal-oxidase abundance** | aa3 abundance was highest at 4.2% O2; ba3 predominated at most lower levels but began declining below 0.42% O2. bb3 and bd oxidases were not detected. (jong2024quantitativeproteomicsreveals pages 1-2) | Direct proteomic edge. Do not infer that the undetected oxidases define the lower oxygen boundary. The authors’ sodium:acetate-exporter explanation for lower Mrp abundance is explicitly proposed and should remain uncertain. |
| **Na+/H+ antiport — maintains — reverse ΔpH in alkaline environments** | Maksimova et al. explain that alkaline growth requires pH homeostasis and that Na+/H+ antiporters use the sodium electrochemical gradient to exchange sodium for protons. *Bacillus aequororis* 5-DB grew at pH 11 and 50 g/L NaCl and showed broader stress resistance than *B. subtilis* ATCC 6633. DOI: [10.1155/2024/3087296](https://doi.org/10.1155/2024/3087296), accepted 10 Jul 2024. (maksimova2024metabolicandmorphological pages 1-2) | The general antiporter mechanism comes from background synthesis, while the study’s direct measurements concern metabolic activity, ATP, intracellular pH, and morphology. Curate the mechanism separately from the strain comparison. |
| **lipid-composition remodeling — maintains — membrane structure/fluidity under temperature stress** | Maiti et al. identify homeoviscous adaptation as regulation of lipid composition and osmolyte-mediated adaptation as protection of lipid membranes under stress. DOI: [10.1039/D4CC03114H](https://doi.org/10.1039/D4CC03114H), accepted 20 Aug 2024. (maiti2024extrememakeoverthe pages 1-2) | Suitable as a broad review-supported process edge. Specific lipid→numerical-temperature-range edges need taxon-specific perturbation evidence. |
| **1% NaCl — decreases — fungal surface-growth rate and estimated Tmax** | *M. circinelloides* optimal surface growth rate fell about 46%; estimated `Tmax` changed from 37.2–37.3°C to 35.1°C on cheese-based agar. DOI: [10.1016/j.heliyon.2024.e30812](https://doi.org/10.1016/j.heliyon.2024.e30812), available 7 May 2024. (konuchova2024characterisationofthe pages 1-2) | Strong assay-specific interaction showing that a “temperature range” depends on salinity. Curate as environmental-factor interaction, not an intrinsic species-wide temperature range. |
| **primary growth-model choice — changes — estimated kinetic parameters** | In the same study, Baranyi models consistently estimated longer lag phases and higher surface growth rates than Huang models, although both fitted well (`R² = 0.993 ± 0.002`, as reported). (konuchova2024characterisationofthe pages 1-2) | Experimental-factor edge. Store as provenance/measurement bias rather than biological causation. |

## 4. Suggested causal-graph architecture

A reusable graph should avoid linking every mechanism directly to `METPO:1000535`. A more biologically interpretable structure is:

1. **Environmental value outside the preferred region**  
   → molecular/biophysical stress (proton influx, water loss, membrane rigidification, oxygen limitation).
2. **Stress**  
   → disturbance of an essential state (pHi, turgor, hydration, membrane fluidity, redox/ATP supply).
3. **Homeostatic module**  
   → restoration of the essential state.
4. **Restored state**  
   → permits net growth at that environmental value.
5. **Failure or capacity limit of the module**  
   → lower or upper observed growth boundary.

Examples are:

- high external pH → insufficient proton availability/altered ΔpH → Na+/H+ antiport plus PMF → near-neutral pHi → growth;
- high salinity → water efflux/dehydration/turgor loss → K+ and compatible-solute accumulation → osmotic balance → growth;
- low oxygen → reduced electron-acceptor availability → alternative high-affinity terminal oxidase usage → respiratory energy conservation → growth;
- high/low temperature → altered bilayer order and protein stability → lipid remodeling/chaperone activity → membrane/protein function → growth.

The final edge from “homeostasis” to a wider numerical interval should be asserted only when a perturbation changes an observed limit. Otherwise use **supports growth under condition X** or **contributes to adaptation across tested values**.

## 5. Current applications and real-world implementations

Quantified growth ranges are operational parameters in predictive food microbiology, bioreactor design, environmental biotechnology, and astrobiology. The 2024 *Mucor* study used cardinal models to estimate visible surface-growth kinetics on cheese media; its practical recommendation was that adjusting salt-wash frequency early in ripening could suppress fast fungal growth. The result also quantifies a real process interaction: 1% NaCl reduced growth rate by about 46% and shifted estimated `Tmax` downward by approximately 2°C. (konuchova2024characterisationofthe pages 1-2)

For alkaline and saline bioprocesses, *B. aequororis* 5-DB’s activity at pH 11 and 50 g/L NaCl and *N. thermophilus* growth at 3.1–4.9 M Na+ identify strains and mechanisms relevant to high-salt fermentations and extreme-environment catalysis. Nevertheless, such values are conditional on medium, temperature, and assay and should not be promoted to species-level constants. (xing2024thepolyextremophilenatranaerobius pages 1-2, maksimova2024metabolicandmorphological pages 1-2)

Respiratory-chain plasticity is relevant to microaerobic reactor operation. In *C. thermarum*, oxidase abundance changed across 0.25–4.2% O2, while aa3 and ba3 complexes occupied different oxygen regimes. This offers mechanistic markers for controlling cultures under fluctuating oxygen, but the study did not establish absolute oxygen growth limits. (jong2024quantitativeproteomicsreveals pages 1-2)

## 6. Expert assessment of evidence strength

### High-priority, curation-ready

- External osmolarity change → water flux → hydration/turgor disruption.
- PMF reduction → impaired cytoplasmic-pH maintenance in *E. coli*.
- 350 mM NaCl → reduced *C. difficile* growth; selected compatible solutes → growth restoration.
- Salinity-associated compatible-solute/K+ accumulation in *N. thermophilus*.
- Oxygen level → aa3/ba3 oxidase abundance changes in *C. thermarum*.
- 1% NaCl → lower *Mucor* growth rate and assay-estimated `Tmax`.

### Curate only with evidence qualifiers

- Antiporter identity → a particular external-pH interval: model-supported in Terradot et al., not a direct growth-range experiment.
- Transporter upregulation → broader salinity range: plausible and multi-omics-supported, but no boundary-shifting knockout.
- Branched respiratory chain → “wide oxygen growth range”: supported within tested chemostat conditions, not demonstrated as full cardinal limits.
- Homeoviscous adaptation → wider temperature range: authoritative general mechanism, but taxon-specific numerical effects are needed.

## 7. Warnings: claims not yet suitable for TraitMech

1. **Do not curate survival values as growth limits.** Acid survival or recovery after stress is not proliferation. (krulwich2011molecularaspectsof pages 1-3)
2. **Do not curate nonphysical fitted boundaries.** Negative `Tmin` estimates described as theoretical are model artifacts. (konuchova2024characterisationofthe pages 1-2)
3. **Do not convert an optimum into a range.** The 3.3–3.9 M Na+ optimum for *N. thermophilus* is nested inside its reported 3.1–4.9 M growth range. (xing2024thepolyextremophilenatranaerobius pages 1-2)
4. **Do not infer range expansion from expression alone.** Proteomic induction across salinities or oxygen levels identifies candidate mechanisms but does not prove movement of a lower or upper boundary.
5. **Do not generalize across taxa.** “Salt-in,” compatible-solute, antiporter, membrane-lipid, and terminal-oxidase strategies differ among bacteria, archaea, and fungi.
6. **Do not omit interacting variables.** NaCl changed estimated fungal `Tmax`; therefore, temperature limits without salinity context can be misleading. (konuchova2024characterisationofthe pages 1-2)
7. **Do not equate tested interval with complete range.** Growth or cultivation from 0.25–4.2% O2 establishes performance within that interval, not absolute cardinal oxygen limits. (jong2024quantitativeproteomicsreveals pages 1-2)
8. **Do not assign strain-independent UniProt identifiers to transporter families.** Opu, ProU, SSS, Mrp, NhaA/B, and oxidase labels require strain-specific sequence resolution.
9. **Do not curate proposed explanations as established edges.** The suggestion that a sodium:acetate exporter reduces the need for Mrp under oxygen limitation is explicitly a proposal. (jong2024quantitativeproteomicsreveals pages 1-2)
10. **Avoid a single axis-agnostic mechanism graph.** `METPO:1000535` should be a descriptor hub with separate pH, salinity/water-activity, temperature, oxygen, pressure, and nutrient subgraphs.

## 8. DOI-first bibliography

1. Terradot G, Krasnopeeva E, Swain PS, Pilizota T. **Escherichia coli Maintains pH via the Membrane Potential.** *PRX Life.* Published 27 November 2024. DOI: [10.1103/PRXLife.2.043015](https://doi.org/10.1103/PRXLife.2.043015). (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9)
2. Xing Q, et al. **The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.** *Applied and Environmental Microbiology.* Published 5 April 2024; 90(5). DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 1-2)
3. de Jong SI, et al. **Quantitative proteomics reveals oxygen-induced adaptations in Caldalkalibacillus thermarum TA2.A1 microaerobic chemostat cultures.** *Frontiers in Microbiology.* Published 28 October 2024;15:1468929. DOI: [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929). (jong2024quantitativeproteomicsreveals pages 1-2)
4. Koňuchová M, Boháčiková A, Valík Ľ. **Characterisation of the surface growth of Mucor circinelloides in cheese agar media using predictive mathematical models.** *Heliyon.* Available 7 May 2024;10:e30812. DOI: [10.1016/j.heliyon.2024.e30812](https://doi.org/10.1016/j.heliyon.2024.e30812). (konuchova2024characterisationofthe pages 1-2)
5. Maksimova YG, Eliseeva A, Maksimov A. **Metabolic and Morphological Aspects of Adaptation of Alkaliphilic Bacillus aequororis 5-DB and Alkali-Tolerant Bacillus subtilis ATCC 6633 to Changes in pH and Mineralization.** *International Journal of Microbiology.* Accepted 10 July 2024. DOI: [10.1155/2024/3087296](https://doi.org/10.1155/2024/3087296). (maksimova2024metabolicandmorphological pages 1-2)
6. Maiti A, Erimban S, Daschakraborty S. **Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments.** *Chemical Communications.* Accepted 20 August 2024;60:10280–10294. DOI: [10.1039/D4CC03114H](https://doi.org/10.1039/D4CC03114H). (maiti2024extrememakeoverthe pages 1-2)
7. Michel A-M, et al. **Cellular adaptation of Clostridioides difficile to high salinity encompasses a compatible solute-responsive change in cell morphology.** *Environmental Microbiology.* 2022;24:1499–1517. DOI: [10.1111/1462-2920.15925](https://doi.org/10.1111/1462-2920.15925). (michel2022cellularadaptationof pages 1-1)
8. Wani AK, et al. **Microbial adaptation to different environmental conditions: molecular perspective of evolved genetic and cellular systems.** *Archives of Microbiology.* Published January 2022;204. DOI: [10.1007/s00203-022-02757-5](https://doi.org/10.1007/s00203-022-02757-5). (wani2022microbialadaptationto pages 5-8, wani2022microbialadaptationto pages 11-13, wani2022microbialadaptationto pages 16-18)
9. Bremer E, Krämer R. **Responses of Microorganisms to Osmotic Stress.** *Annual Review of Microbiology.* 2019;73:313–334. DOI: [10.1146/annurev-micro-020518-115504](https://doi.org/10.1146/annurev-micro-020518-115504). (bremer2019responsesofmicroorganisms pages 1-2)
10. Gunde-Cimerman N, Plemenitaš A, Oren A. **Strategies of adaptation of microorganisms of the three domains of life to high salt concentrations.** *FEMS Microbiology Reviews.* Published May 2018;42:353–375. DOI: [10.1093/femsre/fuy009](https://doi.org/10.1093/femsre/fuy009). This is the supplied foundational salinity evidence; its full text was unavailable in the present retrieval, so no new edge above relies solely on it.
11. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology.* Published May 2011;9:330–343. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 1-3)

## Recommended curation decision

Retain `METPO:1000535` as an **axis-neutral phenotype descriptor**, but implement its causal graph through qualified subgraphs. The strongest first-pass YAML should include: environmental value → homeostatic disturbance; homeostatic mechanism → restored cellular state; restored state → growth under the tested condition; and assay/model factors → observed numerical boundary. Direct claims that a mechanism *widens the complete range* should be deferred until deletion, inhibition, complementation, or gain-of-function experiments demonstrate movement of an observed minimum or maximum.

References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (konuchova2024characterisationofthe pages 1-2): Martina Koňuchová, Agáta Boháčiková, and Ľubomír Valík. Characterisation of the surface growth of mucor circinelloides in cheese agar media using predictive mathematical models. Heliyon, 10:e30812, May 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e30812, doi:10.1016/j.heliyon.2024.e30812. This article has 2 citations.

3. (wani2022microbialadaptationto pages 5-8): Atif Khurshid Wani, Nahid Akhtar, Farooq Sher, Acacio Aparecido Navarrete, and Juliana Heloisa Pinê Américo-Pinheiro. Microbial adaptation to different environmental conditions: molecular perspective of evolved genetic and cellular systems. Archives of Microbiology, Jan 2022. URL: https://doi.org/10.1007/s00203-022-02757-5, doi:10.1007/s00203-022-02757-5. This article has 314 citations and is from a peer-reviewed journal.

4. (terradot2024escherichiacolimaintains pages 1-2): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.

5. (terradot2024escherichiacolimaintains pages 8-9): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.

6. (bremer2019responsesofmicroorganisms pages 1-2): Erhard Bremer and Reinhard Krämer. Responses of microorganisms to osmotic stress. Annual review of microbiology, 73:313-334, Sep 2019. URL: https://doi.org/10.1146/annurev-micro-020518-115504, doi:10.1146/annurev-micro-020518-115504. This article has 531 citations and is from a peer-reviewed journal.

7. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

8. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

9. (maiti2024extrememakeoverthe pages 1-2): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 17 citations and is from a domain leading peer-reviewed journal.

10. (maksimova2024metabolicandmorphological pages 1-2): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

11. (michel2022cellularadaptationof pages 1-1): Annika‐Marisa Michel, José Manuel Borrero‐de Acuña, Gabriella Molinari, Can Murat Ünal, Sabine Will, Elisabeth Derksen, Stefan Barthels, Wiebke Bartram, Michel Schrader, Manfred Rohde, Hao Zhang, Tamara Hoffmann, Meina Neumann‐Schaal, Erhard Bremer, and Dieter Jahn. Cellular adaptation of <i>clostridioides difficile</i> to high salinity encompasses a compatible solute‐responsive change in cell morphology. Environmental Microbiology, 24:1499-1517, Feb 2022. URL: https://doi.org/10.1111/1462-2920.15925, doi:10.1111/1462-2920.15925. This article has 13 citations and is from a domain leading peer-reviewed journal.

12. (wani2022microbialadaptationto pages 11-13): Atif Khurshid Wani, Nahid Akhtar, Farooq Sher, Acacio Aparecido Navarrete, and Juliana Heloisa Pinê Américo-Pinheiro. Microbial adaptation to different environmental conditions: molecular perspective of evolved genetic and cellular systems. Archives of Microbiology, Jan 2022. URL: https://doi.org/10.1007/s00203-022-02757-5, doi:10.1007/s00203-022-02757-5. This article has 314 citations and is from a peer-reviewed journal.

13. (wani2022microbialadaptationto pages 16-18): Atif Khurshid Wani, Nahid Akhtar, Farooq Sher, Acacio Aparecido Navarrete, and Juliana Heloisa Pinê Américo-Pinheiro. Microbial adaptation to different environmental conditions: molecular perspective of evolved genetic and cellular systems. Archives of Microbiology, Jan 2022. URL: https://doi.org/10.1007/s00203-022-02757-5, doi:10.1007/s00203-022-02757-5. This article has 314 citations and is from a peer-reviewed journal.