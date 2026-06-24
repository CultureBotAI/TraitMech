---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:25:40.317408'
end_time: '2026-06-18T11:45:24.113025'
duration_seconds: 1183.8
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: hydrogenotrophic
  trait_identifier: METPO:1000646
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: hydrogenotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism uses molecular hydrogen as an electron
    donor for energy generation and carbon dioxide as the primary carbon source.
  parent_traits: METPO:1000631
  synonyms: ''
  evidence_summary: 'DOI:10.21775/cimb.006.159: reversible oxidation of hydrogen gas
    (Review supports hydrogenase-catalyzed H2 oxidation and microbial energy metabolism.)
    | DOI:10.1128/AEM.02473-10: assimilation of CO2 (Review supports CO2 assimilation
    into cellular carbon in autotrophic metabolism.)'
  causal_graph_summary: 'hydrogenotrophic_hydrogen_oxidation_fixation: 9 nodes, 7
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** hydrogenotrophic
- **METPO identifier:** METPO:1000646
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses molecular hydrogen as an electron donor for energy generation and carbon dioxide as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** 
- **Existing evidence:** DOI:10.21775/cimb.006.159: reversible oxidation of hydrogen gas (Review supports hydrogenase-catalyzed H2 oxidation and microbial energy metabolism.) | DOI:10.1128/AEM.02473-10: assimilation of CO2 (Review supports CO2 assimilation into cellular carbon in autotrophic metabolism.)
- **Existing causal graph summary:** hydrogenotrophic_hydrogen_oxidation_fixation: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **hydrogenotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/hydrogenotrophic.yaml`.

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
- **Trait label:** hydrogenotrophic
- **METPO identifier:** METPO:1000646
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses molecular hydrogen as an electron donor for energy generation and carbon dioxide as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** 
- **Existing evidence:** DOI:10.21775/cimb.006.159: reversible oxidation of hydrogen gas (Review supports hydrogenase-catalyzed H2 oxidation and microbial energy metabolism.) | DOI:10.1128/AEM.02473-10: assimilation of CO2 (Review supports CO2 assimilation into cellular carbon in autotrophic metabolism.)
- **Existing causal graph summary:** hydrogenotrophic_hydrogen_oxidation_fixation: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **hydrogenotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/hydrogenotrophic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **hydrogenotrophic** (METPO:1000646)

### Publication scope and evidence basis
This report curates mechanistic entities and causal edges for the microbial trophic trait **hydrogenotrophic** (METPO:1000646), defined as use of **molecular hydrogen (H2)** as an **electron donor** for energy generation and **carbon dioxide (CO2)** as the **primary carbon source**. Evidence is drawn from authoritative reviews and primary research, prioritizing 2023–2024 when available, and includes supporting verbatim snippets for proposed causal edges. (lappan2023molecularhydrogenin pages 1-2, islam2023microbialhydrogencycling pages 2-4, tyne2023identifyingandunderstanding pages 1-3)

---

## 1) Key concepts, definitions, and trait scope

### 1.1 Working definition aligned to METPO
Hydrogenotrophy is best treated as a **physiological capacity** (not a taxon label) characterized by coupling **H2 oxidation** (via hydrogenases) to **energy conservation** (electron transport, ion gradients, ATP synthesis) and **CO2 assimilation or reduction** into biomass or reduced end products. Hydrogenases broadly catalyze reversible H2 interconversion: “hydrogenases catalyze H2 ↔ 2H+ + 2e−” (menez2020abiotichydrogenand pages 5-8). The hydrogenase reaction can directly couple “hydrogen uptake to the reduction of electron acceptors (e.g., nitrate, sulfate, and carbon dioxide)” (gregory2019subsurfacemicrobialhydrogen pages 5-8).

### 1.2 Distinguishing nearby traits and boundary cases

**A. Hydrogenotrophic vs. hydrogen-oxidizing (non-autotrophic):** Some organisms oxidize H2 for energy while remaining primarily heterotrophic or mixotrophic; e.g., marine bacteria oxidize trace gases using “group 1 and 2 [NiFe]-hydrogenases… linked to aerobic respiratory chains” (lappan2023molecularhydrogenin pages 1-2). These cases support H2 oxidation but do not necessarily imply CO2 is the **primary** carbon source.

**B. Hydrogenotrophic vs. hydrogenogenic:** Hydrogenogenic organisms produce H2 as an electron sink during fermentation; this is mechanistically connected but opposite in directionality and should not be conflated with the trophic trait.

**C. Hydrogenotrophic methanogenesis and acetogenesis as subtypes:** In anoxic systems, two major hydrogenotrophic CO2-reducing endpoints are:
- **Methanogenesis:** hydrogenotrophic methanogens convert “H2 and CO2 to CH4” (szuhaj2023regulationofthe pages 1-2) and are described as “hydrogenotrophic (H2/CO2-consuming) methanogens” in subsurface CCS contexts (tyne2023identifyingandunderstanding pages 1-3).
- **Acetogenesis (Wood–Ljungdahl pathway):** acetogens are described as making “a living from acetate formation from two molecules of CO2 via the Wood-Ljungdahl pathway (WLP)” (kremp2022athirdway pages 1-2).

**D. Environmental/assay boundary cases:** Agricultural soils include organisms that can “coupl[e] hydrogen oxidation to carbon fixation” such that “hydrogenotrophic chemosynthesis is a viable energy generation strategy” (islam2023microbialhydrogencycling pages 2-4). However, this claim is partly ecosystem- and taxon-dependent and should be curated with explicit context.

---

## 2) Candidate causal-graph entities (node inventory)

The node inventory below prioritizes entities repeatedly supported by text evidence and/or recent mechanistic work.

| Node label | Node type | Suggested identifier(s) | Evidence support |
|---|---|---|---|
| Wood–Ljungdahl pathway | pathway/module | KEGG:map00720; MetaCyc:PWY-7371 | Acetogens form acetate from CO2 via the WLP; H2 supports autotrophic growth on H2 + CO2, and electron bifurcation is described as essential to WLP operation in acetogens (kremp2022athirdway pages 1-2, katsyv2023molecularbasisof pages 1-2) |
| Hydrogenotrophic methanogenesis | pathway/module | GO:candidate; MetaCyc:candidate | Defined as conversion of H2 and CO2 to CH4 by hydrogenotrophic methanogens; important in CO2 storage and anaerobic systems (szuhaj2023regulationofthe pages 1-2, tyne2023identifyingandunderstanding pages 1-3) |
| Acetogenesis | pathway/module | GO:candidate; MetaCyc:candidate | Listed among major H2-consuming processes; acetogens “scavenge H2” and reduce CO2 to acetate (pichechoquette2019molecularhydrogena pages 8-9, gregory2019subsurfacemicrobialhydrogen pages 5-8) |
| Electron bifurcation | process/function | GO:candidate | Core energy-coupling process in anaerobes using H2 to reduce CO2; HydABC catalyzes bifurcation from H2 to ferredoxin and NAD(P)+ (katsyv2023molecularbasisof pages 1-2, katsyv2023molecularbasisof pages 2-3) |
| H2 oxidation | process/function | GO:candidate | Hydrogenases catalyze H2 ↔ 2H+ + 2e−; H2 oxidation can be coupled to multiple electron acceptors including CO2/HCO3− and O2 (menez2020abiotichydrogenand pages 5-8, gregory2019subsurfacemicrobialhydrogen pages 5-8) |
| CO2 fixation / reduction | process/function | GO:candidate | H2 oxidation can be coupled to carbon fixation in soils and to CO2 reduction in acetogens and methanogens (islam2023microbialhydrogencycling pages 2-4, mrnjavac2023themoon‐formingimpact pages 13-15) |
| Proton gradient / proton motive force | process/function | GO:candidate | Splitting H2 yields electrons and protons that can generate proton gradients and ATP; membrane hydrogenase systems generate H+ gradients (menez2020abiotichydrogenand pages 5-8, kremp2022athirdway pages 2-5) |
| Sodium motive force | process/function | GO:candidate | Group 4 hydrogenases in some methanogens couple H2 oxidation to a sodium ion motive force; Mtr is a Na+-pumping complex in methanogenesis (pichechoquette2019molecularhydrogena pages 6-8, mrnjavac2023themoon‐formingimpact pages 13-15) |
| ATP synthesis | process/function | GO:0006754 | H2-linked ion gradients drive ATP synthesis, including H+-F1Fo ATP synthase in acetogens (kremp2022athirdway pages 1-2, menez2020abiotichydrogenand pages 5-8) |
| [NiFe]-hydrogenase | gene/protein/complex | EC:1.12.-.- | Widespread uptake/respiratory hydrogenases; linked to aerobic respiratory chains and often constrained by O2 sensitivity/affinity differences (lappan2023molecularhydrogenin pages 1-2, menez2020abiotichydrogenand pages 5-8) |
| [FeFe]-hydrogenase | gene/protein/complex | EC:1.12.7.2 | Includes electron-bifurcating HydABC, central to anaerobic H2-based energy coupling in acetogens (katsyv2023molecularbasisof pages 1-2, katsyv2023molecularbasisof pages 2-3) |
| [Fe]-hydrogenase (Hmd) | gene/protein/complex | EC:1.12.98.2 | Methanogen-specific H2-oxidizing enzyme that reduces methenyl-H4MPT with H2; induced under Ni limitation (mrnjavac2023themoon‐formingimpact pages 13-15) |
| Uptake hydrogenase, group 1/2 | gene/protein/complex | HydDB:candidate; EC:1.12.-.- | Marine bacteria use group 1 and 2 [NiFe]-hydrogenases linked to aerobic respiratory chains for H2 oxidation (lappan2023molecularhydrogenin pages 1-2) |
| Hup / group 1d hydrogenase | gene/protein/complex | HydDB:candidate | Low-affinity uptake hydrogenase common in rhizosphere-associated bacteria; recycles endogenously produced H2 (islam2023microbialhydrogencycling pages 2-4, pichechoquette2019molecularhydrogena pages 6-8) |
| Hhy / group 1h hydrogenase | gene/protein/complex | HydDB:candidate | High-affinity hydrogenase oxidizing atmospheric H2 in plant-associated/soil bacteria (islam2023microbialhydrogencycling pages 2-4) |
| Huc / group 2a hydrogenase | gene/protein/complex | HydDB:candidate | Can oxidize both atmospheric and elevated H2; found in plant-associated bacteria (islam2023microbialhydrogencycling pages 2-4) |
| HydABC electron-bifurcating hydrogenase | gene/protein/complex | EC:candidate | Reduces low-potential ferredoxins by oxidizing H2; bifurcates electrons to Fd and NAD(P)+ (katsyv2023molecularbasisof pages 1-2, katsyv2023molecularbasisof pages 2-3) |
| Rnf complex | gene/protein/complex | KEGG:K03616-K03621; EC:7.2.1.1 candidate | Key respiratory enzyme in acetogens essential for chemolithoautotrophic growth on H2 and CO2 (katsyv2023molecularbasisof pages 1-2, kremp2022athirdway pages 1-2) |
| Ech hydrogenase | gene/protein/complex | EC:candidate | Energy-converting hydrogenase, alternative to Rnf in acetogens; part of H2/CO2 chemolithoautotrophic energy conservation (kremp2022athirdway pages 1-2, katsyv2023molecularbasisof pages 1-2) |
| HdrCBA/MvhD-associated complex | gene/protein/complex | KEGG:candidate | Associated with MetVF-type MTHFR in S. ovata; linked to membrane H2 oxidation and possibly electron bifurcation (kremp2022athirdway pages 2-5) |
| MetVF methylene-THF reductase | gene/protein/complex | EC:1.5.1.20 candidate | WLP-linked enzyme; methylene-THF is terminal electron acceptor in a hydrogen-dependent acetogenic respiratory chain (kremp2022athirdway pages 1-2, kremp2022athirdway pages 2-5) |
| ATP synthase (H+-F1Fo ATP synthase) | gene/protein/complex | EC:7.1.2.2 | Synthesizes ATP from H+ gradient in acetogenic H2-driven membrane systems (kremp2022athirdway pages 1-2) |
| Ferredoxin | gene/protein/complex | CHEBI:36110 | Low-potential electron carrier reduced via HydABC or group 4 hydrogenases during H2-dependent metabolism (katsyv2023molecularbasisof pages 1-2, pichechoquette2019molecularhydrogena pages 6-8) |
| NAD(P)+ / NADH | chemical/metabolite | CHEBI:57540; CHEBI:57945; CHEBI:58349; CHEBI:57783 | HydABC couples H2 oxidation to NAD(P)+ reduction; group 3 hydrogenases help balance NAD/NADH pools (katsyv2023molecularbasisof pages 2-3, pichechoquette2019molecularhydrogena pages 6-8) |
| Coenzyme F420 / F420H2 | chemical/metabolite | CHEBI:candidate | Frh is an F420-reducing hydrogenase in methanogens, linking H2 oxidation to methanogenic carbon reduction chemistry (mrnjavac2023themoon‐formingimpact pages 13-15) |
| Methenyl-H4MPT | chemical/metabolite | CHEBI:candidate | Direct substrate reduced by Hmd using H2 in methanogens (mrnjavac2023themoon‐formingimpact pages 13-15) |
| Molecular hydrogen (H2) | chemical/metabolite | CHEBI:18276 | Primary electron donor in hydrogenotrophy; supports growth in marine bacteria and drives methanogenic/acetogenic pathways (lappan2023molecularhydrogenin pages 1-2, szuhaj2023regulationofthe pages 1-2) |
| Carbon dioxide (CO2) | chemical/metabolite | CHEBI:16526 | Primary carbon source/terminal electron acceptor in hydrogenotrophic methanogenesis and autotrophic acetogenesis (szuhaj2023regulationofthe pages 1-2, kremp2022athirdway pages 1-2) |
| Oxygen (O2) | chemical/metabolite | CHEBI:15379 | Terminal electron acceptor for aerobic hydrogen oxidation; also a major constraint due to hydrogenase O2 sensitivity (menez2020abiotichydrogenand pages 5-8, pichechoquette2019molecularhydrogena pages 6-8) |
| Nitrate | chemical/metabolite | CHEBI:17632 | One of several electron acceptors reduced using H2 in hydrogenotrophic respiration (menez2020abiotichydrogenand pages 5-8, gregory2019subsurfacemicrobialhydrogen pages 5-8) |
| Sulfate | chemical/metabolite | CHEBI:16189 | One of several electron acceptors reduced using H2 in anoxic ecosystems (menez2020abiotichydrogenand pages 5-8, gregory2019subsurfacemicrobialhydrogen pages 5-8) |
| Ferric iron / Fe(III) | chemical/metabolite | CHEBI:candidate | H2 oxidation can be coupled to Fe(III) reduction; important in subsurface H2-consuming pathways (menez2020abiotichydrogenand pages 5-8, gregory2019subsurfacemicrobialhydrogen pages 5-8) |
| Acetate | chemical/metabolite | CHEBI:30089 | Product of acetogenesis/WLP from CO2 + H2; also major fermentation intermediate in anaerobic food webs (kremp2022athirdway pages 1-2, pichechoquette2019molecularhydrogena pages 8-9) |
| Methane | chemical/metabolite | CHEBI:16183 | Product of hydrogenotrophic methanogenesis from H2 + CO2 (szuhaj2023regulationofthe pages 1-2, mackie2024—invitedreview pages 1-2) |
| Agricultural soil rhizosphere | environment/assay factor | ENVO:candidate | Plant-associated bacteria encode Hup/Hhy/Huc hydrogenases and can couple H2 oxidation to carbon fixation; relevant boundary case for hydrogenotrophic chemosynthesis (islam2023microbialhydrogencycling pages 2-4) |
| Marine water column | environment/assay factor | ENVO:00002042 candidate | H2-uptake hydrogenases are prevalent and expressed in ocean metagenomes; H2 oxidation capacity increases with depth and decreases with oxygen (lappan2023molecularhydrogenin pages 1-2) |
| Subsurface ecosystem | environment/assay factor | ENVO:00002042 candidate; ENVO:candidate | Hydrogen-based metabolisms are enriched in subsurface communities with high hydrogenase gene abundance (gregory2019subsurfacemicrobialhydrogen pages 5-8, menez2020abiotichydrogenand pages 8-11) |
| Serpentinization / serpentinizing vents | environment/assay factor | ENVO:candidate | Geological setting generating abundant abiotic H2 that supports autotrophic acetogens and methanogens (mrnjavac2023themoon‐formingimpact pages 13-15, menez2020abiotichydrogenand pages 8-11) |
| Depth | environment/assay factor | PATO/ENVO:candidate | In marine systems, H2 oxidation capacity increases with depth (lappan2023molecularhydrogenin pages 1-2) |
| Oxygen concentration | environment/assay factor | PATO:candidate | In marine systems, H2 oxidation capacity decreases with oxygen concentration; O2 also constrains hydrogenase expression/activity (lappan2023molecularhydrogenin pages 1-2, pichechoquette2019molecularhydrogena pages 6-8) |
| Nickel limitation | environment/assay factor | CHEBI:28160 | Under Ni limitation methanogens can rely on Hmd as an alternative H2-oxidizing enzyme (mrnjavac2023themoon‐formingimpact pages 13-15) |


*Table: This table lists candidate nodes for a hydrogenotrophic TraitMech causal graph, grouped by biological entity type and grounded to stable identifiers where possible. It is useful for curating node inventories before asserting causal edges in the YAML graph.*

---

## 3) Evidence-backed causal edges (triples)

The following table proposes candidate edges for inclusion in `data/traits/physiology/hydrogenotrophic.yaml`. Each edge includes a verbatim snippet and notes about scope/uncertainty.

| Subject node (suggested identifier) | Predicate | Object node (suggested identifier) | Evidence snippet (verbatim, short) | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| hydrogenase activity (GO:candidate; EC:candidate) | catalyzes | H2 oxidation / `H2 -> 2H+ + 2e-` (CHEBI:18276 for H2) | “hydrogenases catalyze H2 ↔ 2H+ + 2e−” (menez2020abiotichydrogenand pages 5-8) | 10.2138/gselements.16.1.39 (2020) https://doi.org/10.2138/gselements.16.1.39 | Broad, high-confidence mechanistic edge; exact GO/EC depends on hydrogenase class. |
| uptake [NiFe]-hydrogenase (group 1/2; EC:candidate) | linked_to | aerobic respiratory chain (GO:candidate) | “using group 1 and 2 [NiFe]-hydrogenases and form I carbon monoxide dehydrogenases linked to aerobic respiratory chains” (lappan2023molecularhydrogenin pages 1-2) | 10.1038/s41564-023-01322-0 (2023) https://doi.org/10.1038/s41564-023-01322-0 | Strong for aerobic trace-gas oxidizers; often mixotrophic rather than strict autotrophs. |
| soluble uptake hydrogenase / Hup (group 1d) | channels_electrons_to | electron transport chain (GO:candidate) | “channel electrons to the electron transport chain and supply energy to the cell” (pichechoquette2019molecularhydrogena pages 6-8) | 10.1128/AEM.02418-18 (2019) https://doi.org/10.1128/AEM.02418-18 | Good edge for Hup-type uptake hydrogenases; taxon-specific wording from review. |
| H2 oxidation (CHEBI:18276) | generates | proton gradient / PMF (GO:candidate) | “Splitting H2 yields electrons and protons that can generate proton gradients and ATP” (menez2020abiotichydrogenand pages 5-8) | 10.2138/gselements.16.1.39 (2020) https://doi.org/10.2138/gselements.16.1.39 | General mechanistic statement; curate as process-level, not specific complex. |
| proton gradient / H+ gradient (GO:candidate) | drives | ATP synthase (GO:candidate; EC:7.1.2.2/7.1.2.1 candidate) | “a transmembrane electrochemical H+ gradient is established… that leads to the synthesis of 0.5 mol ATP/mol methylene-THF by a H+-F1Fo ATP synthase” (kremp2022athirdway pages 1-2) | 10.1128/spectrum.01385-22 (2022) https://doi.org/10.1128/spectrum.01385-22 | Strong but specific to *Sporomusa ovata* respiratory chain. |
| H2 oxidation (CHEBI:18276) | coupled_to_reduction_of | O2 (CHEBI:15379) | “hydrogen oxidation can be coupled to reduction of CO2/HCO3-, sulfate, nitrate, ferric iron and O2” (menez2020abiotichydrogenand pages 5-8) | 10.2138/gselements.16.1.39 (2020) https://doi.org/10.2138/gselements.16.1.39 | High-confidence generic edge; not exclusive to hydrogenotrophs with autotrophy. |
| H2 oxidation (CHEBI:18276) | coupled_to_reduction_of | nitrate (CHEBI:17632) | “hydrogen oxidation can be coupled to reduction of CO2/HCO3-, sulfate, nitrate, ferric iron and O2” (menez2020abiotichydrogenand pages 5-8) | 10.2138/gselements.16.1.39 (2020) https://doi.org/10.2138/gselements.16.1.39 | Generic respiratory coupling edge. |
| H2 oxidation (CHEBI:18276) | coupled_to_reduction_of | sulfate (CHEBI:16189) | “hydrogen oxidation can be coupled to reduction of CO2/HCO3-, sulfate, nitrate, ferric iron and O2” (menez2020abiotichydrogenand pages 5-8) | 10.2138/gselements.16.1.39 (2020) https://doi.org/10.2138/gselements.16.1.39 | Generic respiratory coupling edge. |
| H2 oxidation (CHEBI:18276) | coupled_to_reduction_of | ferric iron / Fe(III) (CHEBI:candidate) | “hydrogen oxidation can be coupled to reduction of CO2/HCO3-, sulfate, nitrate, ferric iron and O2” (menez2020abiotichydrogenand pages 5-8) | 10.2138/gselements.16.1.39 (2020) https://doi.org/10.2138/gselements.16.1.39 | Generic respiratory coupling edge; Fe(III) identifier depends on chemical form. |
| hydrogenase reaction (GO:candidate) | couples_H2_uptake_to_reduction_of | carbon dioxide (CHEBI:16526) | “The hydrogenase reaction… is involved in coupling hydrogen uptake to the reduction of electron acceptors (e.g., nitrate, sulfate, and carbon dioxide)” (gregory2019subsurfacemicrobialhydrogen pages 5-8) | 10.3390/microorganisms7020053 (2019) https://doi.org/10.3390/microorganisms7020053 | Direct support for H2→CO2 reduction edge in subsurface hydrogenotrophy. |
| H2 + CO2 availability (CHEBI:18276 + CHEBI:16526) | supports | hydrogenotrophic methanogenesis (GO:candidate; METPO:candidate) | “The hydrogenotrophic methanogens convert H2 and CO2 to CH4” (szuhaj2023regulationofthe pages 1-2) | 10.1007/s00253-023-12700-3 (2023) https://doi.org/10.1007/s00253-023-12700-3 | Strong for methanogenic branch of hydrogenotrophy. |
| [Fe]-hydrogenase / Hmd (EC:candidate) | reduces | methenyl-H4MPT using H2 (CHEBI:candidate) | “Hmd… ‘reduces methenyl-H4MPT with H2’” (mrnjavac2023themoon‐formingimpact pages 13-15) | 10.1002/cplu.202300270 (2023) https://doi.org/10.1002/cplu.202300270 | Strong but methanogen-specific; supports direct hydride transfer branch. |
| acetogens (NCBITaxon:candidate) | use | Wood–Ljungdahl pathway (KEGG/MetaCyc:candidate) | “Acetogenic bacteria… make a living from acetate formation from two molecules of CO2 via the Wood-Ljungdahl pathway (WLP)” (kremp2022athirdway pages 1-2) | 10.1128/spectrum.01385-22 (2022) https://doi.org/10.1128/spectrum.01385-22 | Strong pathway node; trait-level but taxon group statement. |
| H2 (CHEBI:18276) | electron_donor_for | Wood–Ljungdahl-linked respiratory chain (KEGG/MetaCyc:candidate) | “an electron transport chain… leads from molecular hydrogen as an electron donor to an intermediate of the WLP, methylenetetrahydrofolate” (kremp2022athirdway pages 1-2) | 10.1128/spectrum.01385-22 (2022) https://doi.org/10.1128/spectrum.01385-22 | Strong in *S. ovata*; may not generalize to all acetogens. |
| membrane hydrogenase (label candidate) | coupled_to_reduction_of | methylene-THF (CHEBI:candidate) | “hydrogen oxidation is coupled to the reduction of methylene-THF and the generation of a H+ gradient across the membrane” (kremp2022athirdway pages 2-5) | 10.1128/spectrum.01385-22 (2022) https://doi.org/10.1128/spectrum.01385-22 | Strong but organism-specific to cytochrome-containing acetogens. |
| membrane-associated group 4 hydrogenase (EC:candidate) | generates | proton gradient (GO:candidate) | “perform the H2-dependent reduction of ferredoxin, leading to the generation of a proton gradient … and the generation of ATP” (pichechoquette2019molecularhydrogena pages 6-8) | 10.1128/AEM.02418-18 (2019) https://doi.org/10.1128/AEM.02418-18 | Strong review support; especially in acetoclastic methanogens / some methanogens. |
| membrane-associated group 4 hydrogenase (EC:candidate) | generates | sodium ion motive force (GO:candidate) | “in some methanogens group 4 enzymes reduce ferredoxin and couple H2 oxidation to a sodium ion motive force” (pichechoquette2019molecularhydrogena pages 6-8) | 10.1128/AEM.02418-18 (2019) https://doi.org/10.1128/AEM.02418-18 | Important alternative ion-coupling edge; methanogen-specific. |
| HydABC electron-bifurcating [FeFe]-hydrogenase (EC:candidate) | oxidizes | H2 to reduce ferredoxin and NAD(P)+ (CHEBI:candidate) | “HydABC… reduces low-potential ferredoxins (Fd) by oxidizing hydrogen gas (H2)” (katsyv2023molecularbasisof pages 1-2) | 10.1021/jacs.2c11683 (2023) https://doi.org/10.1021/jacs.2c11683 | Strong mechanistic edge; central for anaerobic acetogenic hydrogenotrophy. |
| HydABC (EC:candidate) | mediates | electron bifurcation (GO:candidate) | “The purified HydABC complexes catalyze electron bifurcation from H2 to Fd and NAD(P)+” (katsyv2023molecularbasisof pages 2-3) | 10.1021/jacs.2c11683 (2023) https://doi.org/10.1021/jacs.2c11683 | Strong, direct experimental support. |
| electron bifurcation (GO:candidate) | essential_for | Wood–Ljungdahl pathway operation (KEGG/MetaCyc:candidate) | “electron bifurcation is essential for the operation of the Wood−Ljungdahl pathway” (katsyv2023molecularbasisof pages 1-2) | 10.1021/jacs.2c11683 (2023) https://doi.org/10.1021/jacs.2c11683 | Strong but contextualized to acetogens using HydABC/Rnf/Ech. |
| H2 oxidation (CHEBI:18276) | can_support | carbon fixation / hydrogenotrophic chemosynthesis (GO:candidate) | “By coupling hydrogen oxidation to carbon fixation… hydrogenotrophic chemosynthesis is a viable energy generation strategy” (islam2023microbialhydrogencycling pages 2-4) | 10.1111/1751-7915.14300 (2023) https://doi.org/10.1111/1751-7915.14300 | Useful trait-level edge; agricultural soils, partly inferential/review synthesis. |
| H2-uptake hydrogenase genes (label candidate) | increases_with | depth (ENVO:candidate) | “Capacity for H2 oxidation increases with depth and decreases with oxygen concentration” (lappan2023molecularhydrogenin pages 1-2) | 10.1038/s41564-023-01322-0 (2023) https://doi.org/10.1038/s41564-023-01322-0 | Strong environmental association in marine systems; not universal across habitats. |
| H2-uptake hydrogenase genes (label candidate) | decreases_with | oxygen concentration (CHEBI:15379) | “Capacity for H2 oxidation increases with depth and decreases with oxygen concentration” (lappan2023molecularhydrogenin pages 1-2) | 10.1038/s41564-023-01322-0 (2023) https://doi.org/10.1038/s41564-023-01322-0 | Strong environmental association in marine systems. |
| soluble uptake hydrogenase / Hup (group 1d) | sensitive_to | oxygen (CHEBI:15379) | “upregulated under anoxic conditions due to their O2 sensitivity” (pichechoquette2019molecularhydrogena pages 6-8) | 10.1128/AEM.02418-18 (2019) https://doi.org/10.1128/AEM.02418-18 | Good support for O2 sensitivity constraint; specific to soluble uptake hydrogenases in review. |
| hydrogenase class distribution (label candidate) | constrained_by | O2 sensitivity (CHEBI:15379) | “different sensitivity to O2 and diverse H2 affinities” (menez2020abiotichydrogenand pages 5-8) | 10.2138/gselements.16.1.39 (2020) https://doi.org/10.2138/gselements.16.1.39 | Broad environmental constraint across hydrogenase classes. |
| Ni limitation (CHEBI:28160) | induces_use_of | Hmd [Fe]-hydrogenase (EC:candidate) | “under Ni limitation an alternative H2-oxidizing enzyme, Hmd” (mrnjavac2023themoon‐formingimpact pages 13-15) | 10.1002/cplu.202300270 (2023) https://doi.org/10.1002/cplu.202300270 | Strong but methanogen-specific; important warning against overgeneralization. |
| hydrogenotrophic methanogens (NCBITaxon:candidate) | consume | H2 and CO2 (CHEBI:18276, CHEBI:16526) | “hydrogenotrophic (H2/CO2-consuming) methanogens” (tyne2023identifyingandunderstanding pages 1-3) | 10.1021/acs.est.2c08652 (2023) https://doi.org/10.1021/acs.est.2c08652 | Useful definition/scope edge; review framing for CO2 storage contexts. |
| methanogenic archaea in rumen (NCBITaxon:candidate) | use_H2_to_reduce | CO2 to methane (CHEBI:16526 to CHEBI:16183) | “methanogenic archaea that effectively use the hydrogen produced… to reduce CO2 and produce methane gas” (mackie2024—invitedreview pages 1-2) | 10.5713/ab.23.0294 (2024) https://doi.org/10.5713/ab.23.0294 | Strong ecological application edge for rumen systems. |
| high H2 concentration (CHEBI:18276) | selects_for | low-affinity [NiFe]-hydrogenases (label candidate) | “high concentrations of hydrogen select for a microbial community containing species in possession of low-affinity variants of [NiFe]-hydrogenases” (gregory2019subsurfacemicrobialhydrogen pages 5-8) | 10.3390/microorganisms7020053 (2019) https://doi.org/10.3390/microorganisms7020053 | Environmental-selection edge; community-level inference rather than direct mechanism. |


*Table: This table lists candidate mechanistic edges for curating the hydrogenotrophic trait, with short verbatim evidence, DOI-first references, and notes on scope or uncertainty. It emphasizes hydrogenase-driven H2 oxidation, energy conservation, CO2 reduction/fixation pathways, and key environmental constraints.*

---

## 4) Recent developments (2023–2024 emphasis)

### 4.1 Marine hydrogenotrophy and environmental gradients (2023)
A major 2023 development is direct ecosystem-scale evidence that **marine bacteria consume H2** and that the genomic capacity for H2 oxidation is widespread and regulated by environmental context. Lappan et al. report: “Genes for H2-uptake hydrogenases are prevalent in global ocean metagenomes, highly expressed in metatranscriptomes and found across eight bacterial phyla” and that “Capacity for H2 oxidation increases with depth and decreases with oxygen concentration” (published online 6 Feb 2023; https://doi.org/10.1038/s41564-023-01322-0) (lappan2023molecularhydrogenin pages 1-2). This supports adding **depth** and **oxygen concentration** as environmental nodes modulating hydrogenotrophic energy capture.

### 4.2 Mechanistic resolution of electron-bifurcating hydrogenase HydABC (2023)
HydABC is a key enzyme complex for anaerobic H2-based energy coupling in acetogens and related anaerobes. Katsyv et al. describe HydABC as “the key enzyme responsible for powering these thermodynamically challenging reactions” and that it “reduces low-potential ferredoxins (Fd) by oxidizing hydrogen gas (H2)” (published 22 Feb 2023; https://doi.org/10.1021/jacs.2c11683) (katsyv2023molecularbasisof pages 1-2). They further report that “The purified HydABC complexes catalyze electron bifurcation from H2 to Fd and NAD(P)+” (katsyv2023molecularbasisof pages 2-3). These statements support explicit causal edges from **H2 oxidation** to **ferredoxin reduction**, enabling CO2 fixation biochemistry.

### 4.3 Hydrogenotrophic methanogenesis as an applied control point (2023–2024)
Hydrogenotrophic methanogenesis is emphasized as a controllable, H2-limited process in engineered and host-associated anaerobic ecosystems.
- In power-to-gas relevant contexts, hydrogenotrophic methanogens are described as converting “H2 and CO2 to CH4” and being differentially regulatable (“switched off”/“switched on” within about an hour in an autotrophic methanogen) (published Aug 2023; https://doi.org/10.1007/s00253-023-12700-3) (szuhaj2023regulationofthe pages 1-2).
- In the rumen, methanogens are described as using “the hydrogen produced… to reduce CO2 and produce methane gas” (published Feb 2024; https://doi.org/10.5713/ab.23.0294) (mackie2024—invitedreview pages 1-2).

---

## 5) Current applications and real-world implementations

### 5.1 Gas fermentation and single-cell protein (SCP) from H2/CO2 (2023)
Hydrogenotrophic bacteria are positioned as candidates for industrial gas fermentation to produce microbial biomass. Jain et al. note that “hydrogenotrophic (hydrogen-oxidising) bacteria… produce biomass using gases as their energy and carbon sources” and are “ideal candidates for single-cell protein production” (published 9 Mar 2023; https://doi.org/10.1071/MA23007) (jain2023microbialconversionof pages 1-2). This supports application-facing edges from **H2 oxidation + CO2 fixation → biomass yield**, though strain- and reactor-specific nodes would need additional sources for curation.

### 5.2 CCS (carbon capture and storage) risk and monitoring (2023)
In geological CO2 storage, hydrogenotrophic methanogenesis is described as potentially significant, especially where H2 is bioavailable. Tyne et al. frame methanogens as “dominated by… hydrogenotrophic (H2/CO2-consuming) methanogens” and note significance in depleted oil fields (published 16 Jun 2023; https://doi.org/10.1021/acs.est.2c08652) (tyne2023identifyingandunderstanding pages 1-3). Curatable nodes include **geological reservoir** context and **H2 availability limitation**.

### 5.3 Agriculture and soil hydrogen cycling (2023)
Islam et al. propose that “By coupling hydrogen oxidation to carbon fixation… hydrogenotrophic chemosynthesis is a viable energy generation strategy for bacteria within agricultural soils” (published Jun 2023; https://doi.org/10.1111/1751-7915.14300) (islam2023microbialhydrogencycling pages 2-4). This motivates including **rhizosphere H2 hotspots** and **H2 supplementation** as environmental/experimental factors in the graph.

---

## 6) Statistics and quantitative data suitable for curation

### 6.1 Hydrogen thresholds for key H2-consuming processes (subsurface ecosystems)
Gregory et al. provide quantitative **hydrogen threshold** ranges for major H2-consuming pathways (Table 3). These thresholds are especially useful for edges linking environmental H2 concentration to competitive outcomes among metabolisms (e.g., methanogenesis vs acetogenesis). The table includes, for example, hydrogenotrophic methanogenesis threshold **0.4–95 nM** and acetogenesis threshold **336–3640 nM** (image excerpt) (https://doi.org/10.3390/microorganisms7020053; 2019) (gregory2019subsurfacemicrobialhydrogen media 2a7da234).

### 6.2 Marine incubations used environmentally relevant H2 (~2.5 ppmv) and observed depth/O2 effects
Lappan et al. report ex situ oxidation assays supplemented with “~2.5 ppmv H2” in headspace incubations and link H2 oxidation capacity to “depth” and “oxygen concentration” trends (published online 6 Feb 2023) (lappan2023molecularhydrogenin pages 1-2).

### 6.3 Enzyme-level activity metrics for HydABC
Katsyv et al. report purified complexes with electron-bifurcating activity (units per mg protein) and strict dependence of ferredoxin reduction on pyridine nucleotides: “The purified HydABC complexes catalyze electron bifurcation from H2 to Fd and NAD(P)+” (katsyv2023molecularbasisof pages 2-3). (This is curatable as an edge; enzyme kinetics should be curated with exact assay details if needed.)

---

## 7) Expert synthesis and analysis (curation guidance)

### 7.1 Mechanistic core for TraitMech graph
A minimal, high-confidence mechanistic backbone for **hydrogenotrophic** should include:
1) **H2 oxidation via hydrogenase** → 2) **electron carrier reduction (ferredoxin, NAD(P)H, F420H2)** → 3) **electron transport and/or electron bifurcation** → 4) **ion gradient (H+ and/or Na+)** → 5) **ATP synthase-driven ATP production** → 6) **CO2 fixation/reduction pathway flux** (WLP or methanogenesis). Strong support exists for each component via general reviews and recent primary mechanistic work (menez2020abiotichydrogenand pages 5-8, pichechoquette2019molecularhydrogena pages 6-8, katsyv2023molecularbasisof pages 1-2, kremp2022athirdway pages 1-2).

### 7.2 Environmental gating
Oxygen is repeatedly supported as a constraint (O2 sensitivity of many hydrogenases; association of H2 oxidation capacity with oxygen concentration in marine systems) (lappan2023molecularhydrogenin pages 1-2, pichechoquette2019molecularhydrogena pages 6-8). Nickel limitation is supported as a methanogen-specific constraint affecting hydrogenase usage (Hmd induction) (mrnjavac2023themoon‐formingimpact pages 13-15).

---

## 8) Warnings: edges that may be premature or need qualifiers

1) **Hydrogen oxidation → carbon fixation** is well-supported at a conceptual level in soils and broad geochemical reviews, but organism-specific pathways (Calvin vs WLP vs rTCA) are not always specified in the cited 2023 sources; curate with pathway-agnostic nodes unless a pathway is explicitly supported (islam2023microbialhydrogencycling pages 2-4, menez2020abiotichydrogenand pages 5-8).

2) **Marine H2 oxidation** is strongly supported, but it may often indicate **mixotrophy** (H2 as supplemental energy) rather than strict CO2-as-primary-carbon-source hydrogenotrophy; encode boundary-case notes in the graph (lappan2023molecularhydrogenin pages 1-2).

3) **Kremp et al. (2022)** provides strong mechanistic detail but is largely specific to the cytochrome/quinone-containing acetogen *Sporomusa ovata*; edges should be marked as taxon-specific unless corroborated in additional acetogens (kremp2022athirdway pages 1-2).

4) Some identifiers remain **candidate-only** (e.g., specific ENVO/PATO terms for depth/oxygen concentration or certain methanogenic cofactors) and should not be forced into curation without stable grounding.

---

## DOI-first bibliography (with URLs and publication dates where available)

- **Lappan R, et al.** “Molecular hydrogen in seawater supports growth of diverse marine bacteria.” *Nature Microbiology* (Published online **6 Feb 2023**). DOI: **10.1038/s41564-023-01322-0**. https://doi.org/10.1038/s41564-023-01322-0 (lappan2023molecularhydrogenin pages 1-2)
- **Katsyv A, et al.** “Molecular Basis of the Electron Bifurcation Mechanism in the [FeFe]-Hydrogenase Complex HydABC.” *J. Am. Chem. Soc.* (Published **22 Feb 2023**). DOI: **10.1021/jacs.2c11683**. https://doi.org/10.1021/jacs.2c11683 (katsyv2023molecularbasisof pages 1-2)
- **Tyne RL, et al.** “Identifying and Understanding Microbial Methanogenesis in CO2 Storage.” *Environmental Science & Technology* (Published **16 Jun 2023**). DOI: **10.1021/acs.est.2c08652**. https://doi.org/10.1021/acs.est.2c08652 (tyne2023identifyingandunderstanding pages 1-3)
- **Szuhaj M, et al.** “Regulation of the methanogenesis pathways by hydrogen at transcriptomic level in time.” *Applied Microbiology and Biotechnology* (**Aug 2023**). DOI: **10.1007/s00253-023-12700-3**. https://doi.org/10.1007/s00253-023-12700-3 (szuhaj2023regulationofthe pages 1-2)
- **Islam ZF, Greening C, Hu H-W.** “Microbial hydrogen cycling in agricultural systems – plant beneficial or detrimental?” *Microbial Biotechnology* (**Jun 2023**). DOI: **10.1111/1751-7915.14300**. https://doi.org/10.1111/1751-7915.14300 (islam2023microbialhydrogencycling pages 2-4)
- **Mrnjavac N, et al.** “The Moon-Forming Impact and the Autotrophic Origin of Life.” *ChemPlusChem* (**Oct 2023**). DOI: **10.1002/cplu.202300270**. https://doi.org/10.1002/cplu.202300270 (mrnjavac2023themoon‐formingimpact pages 13-15)
- **Mackie RI, et al.** “Hydrogen production and hydrogen utilization in the rumen: key to mitigating enteric methane production.” *Animal Bioscience* (**Feb 2024**). DOI: **10.5713/ab.23.0294**. https://doi.org/10.5713/ab.23.0294 (mackie2024—invitedreview pages 1-2)
- **Kremp F, et al.** “A Third Way of Energy Conservation in Acetogenic Bacteria.” *Microbiology Spectrum* (Published **14 Jun 2022**). DOI: **10.1128/spectrum.01385-22**. https://doi.org/10.1128/spectrum.01385-22 (kremp2022athirdway pages 1-2)
- **Ménez B.** “Abiotic Hydrogen and Methane: Fuels for Life.” *Elements* (**Feb 2020**). DOI: **10.2138/gselements.16.1.39**. https://doi.org/10.2138/gselements.16.1.39 (menez2020abiotichydrogenand pages 5-8)
- **Piché-Choquette S, Constant P.** “Molecular Hydrogen, a Neglected Key Driver of Soil Biogeochemical Processes.” *Applied and Environmental Microbiology* (**Mar 2019**). DOI: **10.1128/AEM.02418-18**. https://doi.org/10.1128/AEM.02418-18 (pichechoquette2019molecularhydrogena pages 6-8)
- **Gregory SP, et al.** “Subsurface Microbial Hydrogen Cycling: Natural Occurrence and Implications for Industry.” *Microorganisms* (**Feb 2019**). DOI: **10.3390/microorganisms7020053**. https://doi.org/10.3390/microorganisms7020053 (gregory2019subsurfacemicrobialhydrogen pages 5-8)

---

### Appendix: Visual evidence excerpt
A key quantitative table of hydrogen thresholds and reactions (useful for curation) was extracted as an image from Gregory et al. (2019) Table 3 (gregory2019subsurfacemicrobialhydrogen media 2a7da234).


References

1. (lappan2023molecularhydrogenin pages 1-2): Rachael Lappan, Guy Shelley, Zahra F. Islam, Pok Man Leung, Scott Lockwood, Philipp A. Nauer, Thanavit Jirapanjawat, Gaofeng Ni, Ya-Jou Chen, Adam J. Kessler, Timothy J. Williams, Ricardo Cavicchioli, Federico Baltar, Perran L. M. Cook, Sergio E. Morales, and Chris Greening. Molecular hydrogen in seawater supports growth of diverse marine bacteria. Nature Microbiology, 8:581-595, Feb 2023. URL: https://doi.org/10.1038/s41564-023-01322-0, doi:10.1038/s41564-023-01322-0. This article has 79 citations and is from a highest quality peer-reviewed journal.

2. (islam2023microbialhydrogencycling pages 2-4): Zahra F. Islam, Chris Greening, and Hang‐Wei Hu. Microbial hydrogen cycling in agricultural systems – plant beneficial or detrimental? Microbial Biotechnology, 16:1623-1628, Jun 2023. URL: https://doi.org/10.1111/1751-7915.14300, doi:10.1111/1751-7915.14300. This article has 12 citations and is from a peer-reviewed journal.

3. (tyne2023identifyingandunderstanding pages 1-3): R. L. Tyne, P. H. Barry, M. Lawson, K. G. Lloyd, D. Giovannelli, Z. M. Summers, and C. J. Ballentine. Identifying and understanding microbial methanogenesis in co2 storage. Environmental science & technology, 57:9459-9473, Jun 2023. URL: https://doi.org/10.1021/acs.est.2c08652, doi:10.1021/acs.est.2c08652. This article has 33 citations and is from a domain leading peer-reviewed journal.

4. (menez2020abiotichydrogenand pages 5-8): Bénédicte Ménez. Abiotic hydrogen and methane: fuels for life. Elements, 16:39-46, Feb 2020. URL: https://doi.org/10.2138/gselements.16.1.39, doi:10.2138/gselements.16.1.39. This article has 63 citations and is from a domain leading peer-reviewed journal.

5. (gregory2019subsurfacemicrobialhydrogen pages 5-8): Simon P. Gregory, Megan J. Barnett, Lorraine P. Field, and Antoni E. Milodowski. Subsurface microbial hydrogen cycling: natural occurrence and implications for industry. Microorganisms, 7:53, Feb 2019. URL: https://doi.org/10.3390/microorganisms7020053, doi:10.3390/microorganisms7020053. This article has 319 citations.

6. (szuhaj2023regulationofthe pages 1-2): Márk Szuhaj, Balázs Kakuk, Roland Wirth, Gábor Rákhely, Kornél Lajos Kovács, and Zoltán Bagi. Regulation of the methanogenesis pathways by hydrogen at transcriptomic level in time. Applied Microbiology and Biotechnology, 107:6315-6324, Aug 2023. URL: https://doi.org/10.1007/s00253-023-12700-3, doi:10.1007/s00253-023-12700-3. This article has 26 citations and is from a domain leading peer-reviewed journal.

7. (kremp2022athirdway pages 1-2): Florian Kremp, Jennifer Roth, and Volker Müller. A third way of energy conservation in acetogenic bacteria. Aug 2022. URL: https://doi.org/10.1128/spectrum.01385-22, doi:10.1128/spectrum.01385-22. This article has 41 citations and is from a domain leading peer-reviewed journal.

8. (katsyv2023molecularbasisof pages 1-2): Alexander Katsyv, Anuj Kumar, Patricia Saura, Maximilian C. Pöverlein, Sven A. Freibert, Sven T. Stripp, Surbhi Jain, Ana P. Gamiz-Hernandez, Ville R. I. Kaila, Volker Müller, and Jan M. Schuller. Molecular basis of the electron bifurcation mechanism in the [fefe]-hydrogenase complex hydabc. Journal of the American Chemical Society, 145:5696-5709, Feb 2023. URL: https://doi.org/10.1021/jacs.2c11683, doi:10.1021/jacs.2c11683. This article has 74 citations and is from a highest quality peer-reviewed journal.

9. (pichechoquette2019molecularhydrogena pages 8-9): Sarah Piché-Choquette and Philippe Constant. Molecular hydrogen, a neglected key driver of soil biogeochemical processes. Applied and Environmental Microbiology, Mar 2019. URL: https://doi.org/10.1128/aem.02418-18, doi:10.1128/aem.02418-18. This article has 127 citations and is from a peer-reviewed journal.

10. (katsyv2023molecularbasisof pages 2-3): Alexander Katsyv, Anuj Kumar, Patricia Saura, Maximilian C. Pöverlein, Sven A. Freibert, Sven T. Stripp, Surbhi Jain, Ana P. Gamiz-Hernandez, Ville R. I. Kaila, Volker Müller, and Jan M. Schuller. Molecular basis of the electron bifurcation mechanism in the [fefe]-hydrogenase complex hydabc. Journal of the American Chemical Society, 145:5696-5709, Feb 2023. URL: https://doi.org/10.1021/jacs.2c11683, doi:10.1021/jacs.2c11683. This article has 74 citations and is from a highest quality peer-reviewed journal.

11. (mrnjavac2023themoon‐formingimpact pages 13-15): Natalia Mrnjavac, Jessica L. E. Wimmer, Max Brabender, Loraine Schwander, and William F. Martin. The moon‐forming impact and the autotrophic origin of life. ChemPlusChem, Oct 2023. URL: https://doi.org/10.1002/cplu.202300270, doi:10.1002/cplu.202300270. This article has 20 citations and is from a peer-reviewed journal.

12. (kremp2022athirdway pages 2-5): Florian Kremp, Jennifer Roth, and Volker Müller. A third way of energy conservation in acetogenic bacteria. Aug 2022. URL: https://doi.org/10.1128/spectrum.01385-22, doi:10.1128/spectrum.01385-22. This article has 41 citations and is from a domain leading peer-reviewed journal.

13. (pichechoquette2019molecularhydrogena pages 6-8): Sarah Piché-Choquette and Philippe Constant. Molecular hydrogen, a neglected key driver of soil biogeochemical processes. Applied and Environmental Microbiology, Mar 2019. URL: https://doi.org/10.1128/aem.02418-18, doi:10.1128/aem.02418-18. This article has 127 citations and is from a peer-reviewed journal.

14. (mackie2024—invitedreview pages 1-2): Roderick I. Mackie, Hyewon Kim, Na Kyung Kim, and Isaac Cann. — invited review — hydrogen production and hydrogen utilization in the rumen: key to mitigating enteric methane production. Animal Bioscience, 37:323-336, Feb 2024. URL: https://doi.org/10.5713/ab.23.0294, doi:10.5713/ab.23.0294. This article has 42 citations and is from a peer-reviewed journal.

15. (menez2020abiotichydrogenand pages 8-11): Bénédicte Ménez. Abiotic hydrogen and methane: fuels for life. Elements, 16:39-46, Feb 2020. URL: https://doi.org/10.2138/gselements.16.1.39, doi:10.2138/gselements.16.1.39. This article has 63 citations and is from a domain leading peer-reviewed journal.

16. (jain2023microbialconversionof pages 1-2): Surbhi Jain, James Heffernan, Jitendra Joshi, Thomas Watts, Esteban Marcellin, and Chris Greening. Microbial conversion of waste gases into single-cell protein. Microbiology Australia, 44:27-30, Mar 2023. URL: https://doi.org/10.1071/ma23007, doi:10.1071/ma23007. This article has 17 citations.

17. (gregory2019subsurfacemicrobialhydrogen media 2a7da234): Simon P. Gregory, Megan J. Barnett, Lorraine P. Field, and Antoni E. Milodowski. Subsurface microbial hydrogen cycling: natural occurrence and implications for industry. Microorganisms, 7:53, Feb 2019. URL: https://doi.org/10.3390/microorganisms7020053, doi:10.3390/microorganisms7020053. This article has 319 citations.