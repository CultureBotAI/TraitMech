---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:46:25.777447'
end_time: '2026-06-18T12:00:01.990215'
duration_seconds: 816.21
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: mixotrophic
  trait_identifier: METPO:1000652
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: mixotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism can use both organic and inorganic
    carbon sources for growth.
  parent_traits: METPO:1000631
  synonyms: mixotroph
  evidence_summary: 'DOI:10.1128/AEM.01559-06: Evidence for the ubiquity of mixotrophic
    bacteria (Review supports bacterial mixotrophy as combined metabolic modes in
    marine systems.) | DOI:10.1073/pnas.1305998110: combination of modes by which
    an organism can obtain its energy and carbon (Perspective supports mixotrophy
    as combined energy and carbon acquisition modes.)'
  causal_graph_summary: 'mixotrophic_dual_carbon_energy_use: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mixotrophic
- **METPO identifier:** METPO:1000652
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism can use both organic and inorganic carbon sources for growth.
- **Parent traits:** METPO:1000631
- **Synonyms:** mixotroph
- **Existing evidence:** DOI:10.1128/AEM.01559-06: Evidence for the ubiquity of mixotrophic bacteria (Review supports bacterial mixotrophy as combined metabolic modes in marine systems.) | DOI:10.1073/pnas.1305998110: combination of modes by which an organism can obtain its energy and carbon (Perspective supports mixotrophy as combined energy and carbon acquisition modes.)
- **Existing causal graph summary:** mixotrophic_dual_carbon_energy_use: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **mixotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/mixotrophic.yaml`.

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
- **Trait label:** mixotrophic
- **METPO identifier:** METPO:1000652
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism can use both organic and inorganic carbon sources for growth.
- **Parent traits:** METPO:1000631
- **Synonyms:** mixotroph
- **Existing evidence:** DOI:10.1128/AEM.01559-06: Evidence for the ubiquity of mixotrophic bacteria (Review supports bacterial mixotrophy as combined metabolic modes in marine systems.) | DOI:10.1073/pnas.1305998110: combination of modes by which an organism can obtain its energy and carbon (Perspective supports mixotrophy as combined energy and carbon acquisition modes.)
- **Existing causal graph summary:** mixotrophic_dual_carbon_energy_use: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **mixotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/mixotrophic.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **mixotrophic** (METPO:1000652)

## Scope summary (TraitMech curation view)

**Trait label:** mixotrophic (synonym: mixotroph) **METPO:1000652**. **Definition (given):** trophic type in which an organism can use both organic and inorganic carbon sources for growth.

### Current understanding and key definitions
Microbial trophic strategies are commonly decomposed along **energy source** (photo- vs chemo-; and within chemo: organotrophy vs lithotrophy) and **carbon source** (autotrophy = inorganic carbon, heterotrophy = organic carbon). In this framing, **heterotrophy** is “organic compounds … used as a carbon source,” and **autotrophy** is “processes … in which carbon dioxide and water are synthesized to organic carbon compounds” (e.g., Calvin cycle). (eiler2006evidenceforthe pages 2-3)

A widely used operational definition of **mixotrophy** is a **combination of modes** of obtaining energy and carbon. A classic microbial framing emphasizes that organisms can invest in both light-harvesting and organic uptake/degradation machinery and can switch between modes as conditions change; for example, “if organic matter is limiting, a mixotroph can switch to using light as an energy source and use inorganic carbon as a carbon source, and as light gets limiting, it can switch back to degradation of organic substances.” (eiler2006evidenceforthe pages 2-3)

A more recent ocean-microbiome definition describes mixotrophy explicitly as **“the simultaneous utilization of both autotrophic and heterotrophic nutrition.”** (li2024arcobacteraceaeareubiquitous pages 1-2)

A concise perspective definition consistent with METPO:1000652 is: **“Mixotrophy, a combination of modes by which an organism can obtain its energy and carbon.”** (eiler2006evidenceforthe pages 1-2)

### Boundary cases to distinguish during curation
Because METPO:1000652 is carbon-source based (organic + inorganic carbon for growth), it is important to separate true mixotrophy from adjacent phenomena:

1. **Photo-organoheterotrophy without inorganic carbon fixation**: phototrophy supplies ATP (e.g., proteorhodopsin) but biomass carbon remains predominantly organic. Eiler notes that “not all phototrophic organisms fix inorganic carbon,” and that some isolates are “photo(organo)heterotrophs” because they use organic carbon for synthesis. (eiler2006evidenceforthe pages 1-2)

2. **Predominantly chemolithoautotrophic organisms with minor organic C uptake**: Parada et al. show many marine Thaumarchaeota encode both CO2 fixation and organic uptake genes, but most cells assimilated little organic carbon; at the population level, organic carbon assimilation comprised “0.5%–11% of total biomass carbon.” This is mixotrophy under broad definitions, but the small quantitative contribution suggests curating some edges as **weak/condition-dependent**. (parada2023constrainingthecomposition pages 10-13, parada2023constrainingthecomposition pages 17-19)

3. **Genomic potential vs realized flux**: Several 2023–2024 studies infer mixotrophy from co-occurrence/expression of lithotrophic, autotrophic, and heterotrophic modules; for TraitMech edges, label these as **putative** unless supported by isotope fluxes, inhibition/perturbation experiments, or direct growth assays. (li2024arcobacteraceaeareubiquitous pages 1-2, ray2023clearingtheair pages 4-6)


## Recent developments (prioritizing 2023–2024)

### 1) Newly characterized widespread bacterial mixotrophs in the ocean
A 2024 *mSystems* study identifies marine **Arcobacteraceae** as “ubiquitous mixotrophic bacteria” and reports genes spanning heterotrophic functions (e.g., chitin degradation, fatty acid oxidation) plus chemolithotrophic energy metabolisms (sulfur/hydrogen oxidation) and **rTCA** carbon fixation in candidate genera; metatranscriptomes support a mixotroph coupling “sulfur oxidation and denitrification” to carbon fixation while also metabolizing organic matter. (li2024arcobacteraceaeareubiquitous pages 1-2)

### 2) Mixotrophic iron oxidizers supported by genomes + in situ transcripts
A 2024 *Applied and Environmental Microbiology* study reconstructs **Leptothrix ochracea** genomes and argues for **mixotrophic growth on Fe(II) and organic carbon**, based on the co-occurrence and expression of: Fe(II) oxidation genes (**cyc2**, **mtoA**, cytochromes), terminal oxidases supporting microaerobic respiration, a complete **Calvin–Benson–Bassham (CBB)** cycle with **RuBisCO form II**, and multiple organic carbon transport/oxidation modules (e.g., sugars; acetate/lactate/formate). (tothero2024leptothrixochraceagenomes pages 9-13, tothero2024leptothrixochraceagenomes pages 13-15)

### 3) Dark ocean: experimental perturbation links reduced sulfur to DIC fixation
A 2023 *Microbiome* study incubated bathypelagic water and found that **thiosulfate additions enhanced prokaryotic inorganic carbon fixation**, linking reduced sulfur oxidation (sox system) to DIC fixation and to downstream storage biosynthesis (e.g., glycogen, phospholipids). This provides a perturbation-based line of evidence for chemoautotrophic/mixotrophic carbon processing in the dark ocean. (srivastava2023interplaybetweenautotrophic pages 1-2)

### 4) Rhodopsin-supported carbon fixation potentials in natural communities
A 2024 *Microbiology Spectrum* study uses metatranscriptomics to show that expression of **proton-pump rhodopsin (PPR)** is **positively correlated** with expression of genes in multiple non-Calvin carbon fixation (NCF) pathways in several bacterial orders, suggesting that light-driven proton pumping may provide energetic support for NCF in some mixotrophic contexts; the authors emphasize this is correlative and requires experimental validation. (li2024insitucommunity pages 13-15)

### 5) Expert review: atmospheric chemosynthesis and the evidence gap
A 2023 *Microbiology and Molecular Biology Reviews* review highlights co-occurrence of marker genes for **high-affinity H2 oxidation (group 1h [NiFe] hydrogenase, hhySL)** and **CO oxidation (coxL)** with **RuBisCO form IE (rbcL1E)** across many soil lineages, but stresses that “the direct link between trace gas oxidation and carbon fixation remains disputable,” recommending pure-culture and isotope-based validation. This is an important cautionary example for curating edges from MAG co-occurrence alone. (ray2023clearingtheair pages 4-6)


## Candidate mechanistic nodes (grouped by type)

### A) Pathways / metabolic modules
- **Calvin–Benson–Bassham (CBB) cycle** (GO:0019253) (tothero2024leptothrixochraceagenomes pages 13-15)
- **RuBisCO** (EC:4.1.1.39), including **Form II (cbbM/rbcL)** in some bacteria (tothero2024leptothrixochraceagenomes pages 13-15)
- **Reverse TCA (rTCA) cycle** (label-only; KEGG/MetaCyc grounding to be added when mapping) (li2024arcobacteraceaeareubiquitous pages 1-2)
- **3-HP/4-HB carbon fixation pathway** (label-only; archaeal CO2 fixation module) (parada2023constrainingthecomposition pages 10-13)
- **Sulfur oxidation (sox system)** (gene module; label-only) (srivastava2023interplaybetweenautotrophic pages 1-2)
- **Denitrification / DNRA** (label-only) as coupled energy metabolism for fixation (li2024arcobacteraceaeareubiquitous pages 1-2)
- **Ammonia oxidation** (GO:0019415) (amoA marker) (parada2023constrainingthecomposition pages 10-13)
- **Central carbon metabolism**: glycolysis/gluconeogenesis (label-only), PPP (G6PD; KEGG K00036), TCA/rTCA (label-only) (parada2023constrainingthecomposition pages 10-13)
- **Organic acid utilization**: lactate oxidation modules (lctP; ykgEFG), acetate uptake/activation (actP, ackA), formate dehydrogenase (label-only) (tothero2024leptothrixochraceagenomes pages 13-15)

### B) Genes / proteins / complexes (examples suitable as nodes)
- **cyc2** (outer-membrane iron oxidase; label-only/UniProt family) (tothero2024leptothrixochraceagenomes pages 9-13)
- **mtoA** (iron oxidation-associated; label-only) (tothero2024leptothrixochraceagenomes pages 9-13)
- **ccoNOPQ** (cbb3-type high-affinity terminal oxidase; label-only) (tothero2024leptothrixochraceagenomes pages 9-13)
- **cydABX** (bd-type terminal oxidase; label-only) (tothero2024leptothrixochraceagenomes pages 9-13)
- **rbcL/cbbM** (RuBisCO large subunit; label-only) (tothero2024leptothrixochraceagenomes pages 13-15)
- **amoA** (ammonia monooxygenase subunit; label-only) (parada2023constrainingthecomposition pages 10-13)
- **accA** (acetyl-CoA carboxylase subunit; label-only) (parada2023constrainingthecomposition pages 10-13)
- **ureC** (urease; label-only) and **urea active transporters** (label-only) (parada2023constrainingthecomposition pages 10-13)
- **gtsABC / frcABC** (sugar transport systems; label-only) (tothero2024leptothrixochraceagenomes pages 13-15)
- **Proton-pump rhodopsin (PPR/proteorhodopsin-like)** (label-only; widely used annotation) (li2024insitucommunity pages 13-15)
- **coxL** (aerobic CO dehydrogenase large subunit; label-only) (ray2023clearingtheair pages 4-6)
- **hhySL** (group 1h [NiFe] hydrogenase; label-only) (ray2023clearingtheair pages 4-6)
- **rbcL1E** (RuBisCO form IE marker; label-only) (ray2023clearingtheair pages 4-6)

### C) Chemicals / electron donors & acceptors (candidate CHEBI)
- **CO2 / dissolved inorganic carbon** (CHEBI:16526) (tothero2024leptothrixochraceagenomes pages 13-15)
- **Fe(II)** (CHEBI:29033) as lithotrophic electron donor (tothero2024leptothrixochraceagenomes pages 9-13)
- **Thiosulfate** (CHEBI:9568) as reduced sulfur substrate (srivastava2023interplaybetweenautotrophic pages 1-2)
- **Urea** (CHEBI:16199) (parada2023constrainingthecomposition pages 10-13)
- **Acetate** (CHEBI:30089), **lactate** (CHEBI:24996), **formate** (CHEBI:15740) (tothero2024leptothrixochraceagenomes pages 13-15)

### D) Environmental / experimental factors (candidate ENVO)
- **Light limitation** (candidate ENVO term; curate label-only if uncertain) as driver of switching to heterotrophy (eiler2006evidenceforthe pages 2-3)
- **Organic matter limitation / DOC scarcity** (label-only) as driver of switching to autotrophy/phototrophy (eiler2006evidenceforthe pages 2-3)
- **Microaerobic conditions / low oxygen** (ENVO candidate; label-only) selecting for high-affinity oxidases (tothero2024leptothrixochraceagenomes pages 9-13)
- **Thiosulfate amendment** (experimental factor) as perturbation to test sulfur-driven fixation (srivastava2023interplaybetweenautotrophic pages 1-2)


## Evidence-backed candidate causal edges (curation-ready table)
The following table enumerates candidate edges as subject–predicate–object triples with direct snippets and uncertainty notes.

| Edge (Subject —predicate→ Object) | Entity types (S/O) | Suggested CURIE grounding for S and O | Evidence (short quote/snippet) | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| Thiosulfate oxidation —stimulates→ inorganic carbon fixation (DIC fixation) | process → process | S: CHEBI:9568 / sulfur oxidation (label-only); O: GO:0015977 | “Amendment of LSW with thiosulfate and thiosulfate plus DOM enhanced prokaryotic inorganic carbon fixation.” (srivastava2023interplaybetweenautotrophic pages 1-2) | 10.1186/s40168-023-01688-7, 2023, https://doi.org/10.1186/s40168-023-01688-7 | Direct experimental support from bathypelagic incubations; community-level, not single-isolate. |
| sox sulfur-oxidation system —supports→ CO2-fixation pathways | gene module → process | S: sox (label-only); O: GO:0015977 | “elevated expression of genes for sulfur oxidation and CO2-fixation pathways in sulfur-oxidizers” (srivastava2023interplaybetweenautotrophic pages 1-2) | 10.1186/s40168-023-01688-7, 2023, https://doi.org/10.1186/s40168-023-01688-7 | Transcript co-occurrence; causal direction inferred from metabolism. |
| Sulfur oxidation + denitrification —couples to→ carbon fixation | process → process | S: sulfur oxidation + denitrification (label-only); O: carbon fixation (label-only) | “conducts carbon fixation by coupling sulfur oxidation and denitrification and metabolizing organic matter” (li2024arcobacteraceaeareubiquitous pages 1-2) | 10.1128/msystems.00513-24, 2024, https://doi.org/10.1128/msystems.00513-24 | Strong for CAIJNA01-like Arcobacteraceae; taxon-specific. |
| reverse TCA pathway —mediates→ carbon fixation | pathway → process | S: KEGG/MetaCyc rTCA (label-only); O: GO:0015977 | “two mixotrophic Candidatus genera… harbor genes putatively involved in the reverse tricarboxylic acid pathway for carbon fixation” (li2024arcobacteraceaeareubiquitous pages 1-2) | 10.1128/msystems.00513-24, 2024, https://doi.org/10.1128/msystems.00513-24 | Genomic potential; “putatively involved,” so curate as uncertain unless expression/flux evidence added. |
| Cyc2 —transfers electrons from→ Fe(II) oxidation pathway | protein → process | S: Cyc2 (label-only/UniProt family); O: CHEBI:29033 / Fe2+ oxidation (label-only) | “validated iron oxidases (Cyc2 clusters and MtoA) plus periplasmic electron carrier Cyc1 link outer-membrane Fe(II) oxidation to the electron transport chain” (tothero2024leptothrixochraceagenomes pages 9-13) | 10.1128/aem.00599-24, 2024, https://doi.org/10.1128/aem.00599-24 | Mechanistic genomic interpretation; no pure-culture biochemistry yet. |
| MtoA —supports→ Fe(II) oxidation of solid substrates | protein → process | S: MtoA (label-only); O: Fe(II) oxidation (label-only) | “MtoA able to contact solid Fe(II)” (tothero2024leptothrixochraceagenomes pages 9-13) | 10.1128/aem.00599-24, 2024, https://doi.org/10.1128/aem.00599-24 | Substrate-specific role inferred from comparative genomics/literature synthesis. |
| Fe(II) oxidation —feeds electrons to→ electron transport chain | process → complex/process | S: Fe(II) oxidation (label-only); O: GO:0022900 | “Cyc2 clusters and MtoA… link outer-membrane Fe(II) oxidation to the electron transport chain” (tothero2024leptothrixochraceagenomes pages 9-13) | 10.1128/aem.00599-24, 2024, https://doi.org/10.1128/aem.00599-24 | Good candidate edge for iron-oxidizing mixotrophs. |
| Electron transport chain —drives→ ATP synthesis | process/complex → process | S: GO:0022900; O: GO:0015986 | “complete ETC complexes… and F-type ATPase” (tothero2024leptothrixochraceagenomes pages 9-13) | 10.1128/aem.00599-24, 2024, https://doi.org/10.1128/aem.00599-24 | Canonical inference from ETC + ATPase presence; not uniquely mixotrophy-specific. |
| RuBisCO (rbcL/cbbM) —enables→ Calvin-Benson-Bassham cycle | enzyme → pathway | S: EC:4.1.1.39; O: GO:0019253 | “all MAGs encode Form II RuBisCO (rbcL/cbbM) and a full CBB cycle” (tothero2024leptothrixochraceagenomes pages 13-15) | 10.1128/aem.00599-24, 2024, https://doi.org/10.1128/aem.00599-24 | Strong genomic evidence in L. ochracea. |
| Calvin-Benson-Bassham cycle —fixes→ CO2 | pathway → chemical/process | S: GO:0019253; O: CHEBI:16526 | “a full CBB cycle, consistent with CO2 fixation potential” (tothero2024leptothrixochraceagenomes pages 9-13) | 10.1128/aem.00599-24, 2024, https://doi.org/10.1128/aem.00599-24 | Potential supported; quantitative contribution may be small in some taxa. |
| amoA (ammonia monooxygenase) —supports→ ammonia oxidation | gene/enzyme → process | S: amoA (label-only); O: GO:0019415 | “Genes involved in chemoautotrophy included those necessary for ammonia oxidation (e.g. ammonia monooxygenase, amoA)” (parada2023constrainingthecomposition pages 10-13) | 10.1111/1462-2920.16299, 2023, https://doi.org/10.1111/1462-2920.16299 | Strong genomic marker for thaumarchaeal chemolithotrophy. |
| 3-HP/4-HB pathway —mediates→ inorganic carbon fixation | pathway → process | S: 3-HP/4-HB pathway (label-only); O: GO:0015977 | “contained genes for chemoautotrophy (3-HP/4-HB carbon fixation and ammonia oxidation)” (parada2023constrainingthecomposition pages 10-13) | 10.1111/1462-2920.16299, 2023, https://doi.org/10.1111/1462-2920.16299 | Strong pathway-level evidence in Thaumarchaeota. |
| Proton-pump rhodopsin / PPR —generates→ proton gradient | protein → process | S: proteorhodopsin/proton-pump rhodopsin (label-only); O: proton motive force (label-only) | “PPR (rhodopsin) is proposed as a photosystem-independent proton pump that creates a proton gradient to drive ATP synthesis” (li2024insitucommunity pages 13-15) | 10.1128/spectrum.02177-23, 2024, https://doi.org/10.1128/spectrum.02177-23 | Mechanistic claim from transcriptomics plus known rhodopsin biophysics; not directly flux-measured here. |
| Proton gradient —drives→ ATP synthesis | process → process | S: proton motive force (label-only); O: GO:0015986 | “creates a proton gradient to drive ATP synthesis” (li2024insitucommunity pages 13-15) | 10.1128/spectrum.02177-23, 2024, https://doi.org/10.1128/spectrum.02177-23 | Canonical bioenergetic edge. |
| PPR expression —positively correlates with→ non-Calvin carbon fixation gene expression | expression pattern → expression pattern/process | S: PPR expression (label-only); O: NCF gene expression (label-only) | “NCF potential was positively correlated with proton-pump rhodopsin (PPR) expression” (li2024insitucommunity pages 13-15) | 10.1128/spectrum.02177-23, 2024, https://doi.org/10.1128/spectrum.02177-23 | Correlative only; useful as uncertain ecological edge. |
| Endocytosis/phagocytosis —supports or complements→ Calvin carbon fixation (photosynthetic CCF) | process → process | S: GO:0006897 / GO:0006909; O: Calvin carbon fixation (label-only) | “CCF potential exhibited positive or negative correlations with phagotrophy gene expression, suggesting phagotrophy possibly enhances or complements CCF.” (li2024insitucommunity pages 13-15) | 10.1128/spectrum.02177-23, 2024, https://doi.org/10.1128/spectrum.02177-23 | Eukaryotic plankton example; likely outside core bacterial TraitMech unless scope broadens. |
| Polysaccharide ABC transporter / gtsABC / frcABC —imports→ sugars | transporter → chemical | S: polysaccharide ABC transporter / gtsABC / frcABC (label-only); O: sugars (CHEBI:16646 broad candidate) | “sugar transporters (gtsABC, frcABC)… consistent with import and degradation of simple sugars and polysaccharides” (tothero2024leptothrixochraceagenomes pages 13-15) | 10.1128/aem.00599-24, 2024, https://doi.org/10.1128/aem.00599-24 | Good mechanistic uptake edge for heterotrophic arm of mixotrophy. |
| actP/ackA —supports→ acetate import and activation | transporter/enzyme → process | S: actP/ackA (label-only); O: acetate assimilation (label-only; CHEBI:30089 acetate) | “acetate import and activation (actP, ackA)” (tothero2024leptothrixochraceagenomes pages 13-15) | 10.1128/aem.00599-24, 2024, https://doi.org/10.1128/aem.00599-24 | Strong pathway annotation; actual flux inferred. |
| Urea active transporter + ureC —supports→ urea utilization | transporter/enzyme → process | S: urea active transporter + ureC (label-only); O: urea utilization (CHEBI:16199 / label-only) | “contained genes for the utilization of organic nitrogen, including urea degradation (e.g. ureC) and transporters for urea” (parada2023constrainingthecomposition pages 10-13) | 10.1111/1462-2920.16299, 2023, https://doi.org/10.1111/1462-2920.16299 | In Thaumarchaeota, evidence suggests mainly N acquisition rather than major C assimilation. |
| Organic matter limitation —promotes switching to→ light use + inorganic carbon use | environmental factor → process/trait state | S: low organic matter availability (label-only); O: phototrophy + autotrophy (label-only) | “if organic matter is limiting, a mixotroph can switch to using light as an energy source and use inorganic carbon as a carbon source” (eiler2006evidenceforthe pages 2-3) | 10.1128/AEM.01559-06, 2006, https://doi.org/10.1128/AEM.01559-06 | Classic conceptual source; not a single mechanistic experiment. |
| Light limitation —promotes switching to→ degradation of organic substances | environmental factor → process | S: light limitation (ENVO:21000206 candidate); O: organic matter degradation (label-only) | “as light gets limiting, it can switch back to degradation of organic substances” (eiler2006evidenceforthe pages 2-3) | 10.1128/AEM.01559-06, 2006, https://doi.org/10.1128/AEM.01559-06 | Conceptual/general boundary edge rather than gene-level mechanism. |
| Microaerobic conditions —select for/support→ high-affinity terminal oxidases (cbb3-type, bd-type) | environmental factor → protein complex | S: low oxygen / microaerobic conditions (ENVO:01000687 candidate); O: ccoNOPQ/cydABX (label-only) | “high-affinity terminal oxidases (cbb3-type ccoNOPQ and bd-type cydABX) indicative of microaerobic respiration” (tothero2024leptothrixochraceagenomes pages 9-13) | 10.1128/aem.00599-24, 2024, https://doi.org/10.1128/aem.00599-24 | Environmental adaptation edge; inferred from established oxidase physiology. |


*Table: This table lists candidate causal edges for the microbial trait mixotrophic (METPO:1000652), emphasizing evidence-backed mechanistic links among carbon fixation, redox metabolism, transport, and environmental drivers. It is designed to support TraitMech curation by pairing each proposed edge with a quote, source, grounding suggestions, and uncertainty notes.*


## Visual evidence (pathway schematic)
Two cropped figures from *Tothero et al., 2024* summarize (i) genomic pathway presence across *L. ochracea* MAGs and (ii) a schematic metabolic model integrating Fe(II) oxidation, respiration/ETC, CO2 fixation via CBB, and organic carbon utilization—useful as a reference diagram for node/edge curation. (tothero2024leptothrixochraceagenomes media 8c5a0a3a, tothero2024leptothrixochraceagenomes media 1e58a269)


## Relevant statistics and quantitative findings (recent sources)
- **Upper-ocean mixotrophic bacteria abundance estimate (example study cited in PNAS perspective):** mixotrophic bacteria “make up a significant percentage (up to **11%**) of the microbial …” in the referenced context. (eiler2006evidenceforthe pages 1-2)
- **Marine Thaumarchaeota organic carbon contribution:** population-level organic carbon assimilation “comprised just **0.5%–11% of total biomass carbon**” in Parada et al.’s single-cell constrained analysis. (parada2023constrainingthecomposition pages 10-13)
- **Thaumarchaeota prevalence in a sampled community (contextual ecological statistic):** at 150 m depth, Thaumarchaeota OTUs comprised **13% of total 16S rRNA gene DNA reads** and **61% of RNA reads** in situ in Parada et al. (parada2023constrainingthecomposition pages 10-13)
- **Bathypelagic manipulation result (directional quantitative claim):** thiosulfate addition increased inorganic carbon fixation (magnitude not captured in retrieved snippet; curate as qualitative until numeric extraction is added). (srivastava2023interplaybetweenautotrophic pages 1-2)


## Current applications and real-world implementations

### A) Biogeochemical and ecosystem modeling
Mixotrophy challenges the classical dichotomy of “photo(auto)trophs” vs “(organo)heterotrophs” and can force revision of carbon-flow models in marine systems, because mixotrophs may contribute to photo-, hetero-, auto-, and organotrophic processes concurrently. (eiler2006evidenceforthe pages 1-2)

In the deep ocean, experimental evidence that reduced sulfur compounds can enhance DIC fixation supports inclusion of sulfur-driven chemoautotrophic/mixotrophic production and its coupling to organic-matter transformations in carbon budgets. (srivastava2023interplaybetweenautotrophic pages 1-2)

### B) Environmental niche inference from genomes/transcripts
High-affinity terminal oxidases (e.g., cbb3-type, bd-type) alongside Fe(II) oxidation and organic utilization modules can be used as a signature of **microaerobic iron-oxidizing mixotrophy** in wetlands/streams where both Fe(II) and organic carbon are present. (tothero2024leptothrixochraceagenomes pages 9-13)

### C) Biotechnology/engineering direction (conceptual linkage)
Although not required for METPO:1000652 curation, the broader “mixotrophy toolbox” is increasingly being leveraged in engineered systems that integrate light energy capture and carbon fixation. For example, rhodopsin-based artificial photosynthesis is proposed to broaden energy inputs into microbial CO2 fixation systems. (srivastava2023interplaybetweenautotrophic pages 1-2)


## Expert opinions / authoritative analysis (curation cautions)
- **Validation gap warning (authoritative review):** In the atmospheric chemosynthesis literature, the “direct link between trace gas oxidation and carbon fixation remains disputable,” and evidence often comes from marker-gene co-occurrence rather than single-organism demonstrations; recommended next steps include pure-culture experiments and isotope tracing (e.g., 13CO2 SIP). (ray2023clearingtheair pages 4-6)
- **Correlation ≠ causation warning (community transcriptomics):** correlations between rhodopsin expression and non-Calvin carbon fixation gene expression are suggestive but explicitly require laboratory/isotope validation. (li2024insitucommunity pages 13-15)
- **Genetic potential ≠ realized mixotrophic carbon flux:** Thaumarchaeota encode organic uptake genes yet may assimilate little organic carbon in situ, implying that edges from “transporter presence → organic carbon assimilation” should be curated as uncertain unless supported by uptake/flux evidence in the relevant context. (parada2023constrainingthecomposition pages 10-13, parada2023constrainingthecomposition pages 1-6)


## Curation warnings (do not yet curate without additional evidence)

1. **MAG co-occurrence edges** (e.g., hhySL/coxL with rbcL1E) should be curated as **uncertain** until there is single-organism flux evidence or inhibition/perturbation evidence that couples trace-gas oxidation to carbon fixation in the same organism. (ray2023clearingtheair pages 4-6)
2. **Transcript correlation edges** (PPR ↔ NCF genes; phagotrophy ↔ Calvin fixation genes) should be curated as **associational** unless experimental perturbation or isotope tracing confirms directionality. (li2024insitucommunity pages 13-15)
3. **“Small organic carbon uptake” mixotrophy** in largely chemolithoautotrophic taxa (e.g., MGI Thaumarchaeota) should be represented with explicit quantitative qualifiers or uncertainty tags, because organic substrates may primarily satisfy nitrogen demands rather than carbon demands. (parada2023constrainingthecomposition pages 17-19)


## DOI-first bibliography (with URLs and publication dates)

1. **Li J, et al.** *Arcobacteraceae are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans.* **mSystems**. **2024-07**. DOI: **10.1128/msystems.00513-24**. URL: https://doi.org/10.1128/msystems.00513-24 (li2024arcobacteraceaeareubiquitous pages 1-2)
2. **Tothero GK, et al.** *Leptothrix ochracea genomes reveal potential for mixotrophic growth on Fe(II) and organic carbon.* **Applied and Environmental Microbiology**. **2024-09**. DOI: **10.1128/aem.00599-24**. URL: https://doi.org/10.1128/aem.00599-24 (tothero2024leptothrixochraceagenomes pages 9-13, tothero2024leptothrixochraceagenomes pages 13-15, tothero2024leptothrixochraceagenomes media 8c5a0a3a, tothero2024leptothrixochraceagenomes media 1e58a269)
3. **Li H, et al.** *In situ community transcriptomics illuminates CO2-fixation potentials and supporting roles of phagotrophy and proton pump in plankton in a subtropical marginal sea.* **Microbiology Spectrum**. **2024-03**. DOI: **10.1128/spectrum.02177-23**. URL: https://doi.org/10.1128/spectrum.02177-23 (li2024insitucommunity pages 13-15)
4. **Parada AE, et al.** *Constraining the composition and quantity of organic matter used by abundant marine Thaumarchaeota.* **Environmental Microbiology**. **2023-12**. DOI: **10.1111/1462-2920.16299**. URL: https://doi.org/10.1111/1462-2920.16299 (parada2023constrainingthecomposition pages 10-13, parada2023constrainingthecomposition pages 17-19, parada2023constrainingthecomposition pages 1-6)
5. **Srivastava A, et al.** *Interplay between autotrophic and heterotrophic prokaryotic metabolism in the bathypelagic realm revealed by metatranscriptomic analyses.* **Microbiome**. **2023-11**. DOI: **10.1186/s40168-023-01688-7**. URL: https://doi.org/10.1186/s40168-023-01688-7 (srivastava2023interplaybetweenautotrophic pages 1-2)
6. **Ray AE, et al.** *Clearing the air: unraveling past and guiding future research in atmospheric chemosynthesis.* **Microbiology and Molecular Biology Reviews**. **2023-12**. DOI: **10.1128/mmbr.00048-23**. URL: https://doi.org/10.1128/mmbr.00048-23 (ray2023clearingtheair pages 4-6)
7. **Moore LR.** *More mixotrophy in the marine microbial mix.* **PNAS**. **2013-05**. DOI: **10.1073/pnas.1305998110**. URL: https://doi.org/10.1073/pnas.1305998110 (eiler2006evidenceforthe pages 1-2)
8. **Eiler A.** *Evidence for the Ubiquity of Mixotrophic Bacteria in the Upper Ocean: Implications and Consequences.* **Applied and Environmental Microbiology**. **2006-12**. DOI: **10.1128/AEM.01559-06**. URL: https://doi.org/10.1128/AEM.01559-06 (eiler2006evidenceforthe pages 1-2, eiler2006evidenceforthe pages 2-3)


References

1. (eiler2006evidenceforthe pages 2-3): Alexander Eiler. Evidence for the ubiquity of mixotrophic bacteria in the upper ocean: implications and consequences. Dec 2006. URL: https://doi.org/10.1128/aem.01559-06, doi:10.1128/aem.01559-06. This article has 195 citations and is from a peer-reviewed journal.

2. (li2024arcobacteraceaeareubiquitous pages 1-2): Jianyang Li, Shizheng Xiang, Yufei Li, Ruolin Cheng, Qiliang Lai, Liping Wang, Guizhen Li, Chunming Dong, and Zongze Shao. <i>arcobacteraceae</i> are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans. Jul 2024. URL: https://doi.org/10.1128/msystems.00513-24, doi:10.1128/msystems.00513-24. This article has 31 citations and is from a peer-reviewed journal.

3. (eiler2006evidenceforthe pages 1-2): Alexander Eiler. Evidence for the ubiquity of mixotrophic bacteria in the upper ocean: implications and consequences. Dec 2006. URL: https://doi.org/10.1128/aem.01559-06, doi:10.1128/aem.01559-06. This article has 195 citations and is from a peer-reviewed journal.

4. (parada2023constrainingthecomposition pages 10-13): Alma E. Parada, Xavier Mayali, Peter K. Weber, Jessica Wollard, Alyson E. Santoro, Jed A. Fuhrman, Jennifer Pett‐Ridge, and Anne E. Dekas. Constraining the composition and quantity of organic matter used by abundant marine thaumarchaeota. Dec 2023. URL: https://doi.org/10.1111/1462-2920.16299, doi:10.1111/1462-2920.16299. This article has 20 citations and is from a domain leading peer-reviewed journal.

5. (parada2023constrainingthecomposition pages 17-19): Alma E. Parada, Xavier Mayali, Peter K. Weber, Jessica Wollard, Alyson E. Santoro, Jed A. Fuhrman, Jennifer Pett‐Ridge, and Anne E. Dekas. Constraining the composition and quantity of organic matter used by abundant marine thaumarchaeota. Dec 2023. URL: https://doi.org/10.1111/1462-2920.16299, doi:10.1111/1462-2920.16299. This article has 20 citations and is from a domain leading peer-reviewed journal.

6. (ray2023clearingtheair pages 4-6): Angelique E. Ray, Dana Z. Tribbia, Don A. Cowan, and Belinda C. Ferrari. Clearing the air: unraveling past and guiding future research in atmospheric chemosynthesis. Microbiology and Molecular Biology Reviews, Dec 2023. URL: https://doi.org/10.1128/mmbr.00048-23, doi:10.1128/mmbr.00048-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

7. (tothero2024leptothrixochraceagenomes pages 9-13): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

8. (tothero2024leptothrixochraceagenomes pages 13-15): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

9. (srivastava2023interplaybetweenautotrophic pages 1-2): Abhishek Srivastava, Daniele De Corte, Juan A. L. Garcia, Brandon K. Swan, Ramunas Stepanauskas, Gerhard J. Herndl, and Eva Sintes. Interplay between autotrophic and heterotrophic prokaryotic metabolism in the bathypelagic realm revealed by metatranscriptomic analyses. Microbiome, Nov 2023. URL: https://doi.org/10.1186/s40168-023-01688-7, doi:10.1186/s40168-023-01688-7. This article has 10 citations and is from a highest quality peer-reviewed journal.

10. (li2024insitucommunity pages 13-15): Hongfei Li, Jianwei Chen, Liying Yu, Guangyi Fan, Tangcheng Li, Ling Li, Huatao Yuan, Jingtian Wang, Cong Wang, Denghui Li, and Senjie Lin. <i>in situ</i> community transcriptomics illuminates co <sub>2</sub> -fixation potentials and supporting roles of phagotrophy and proton pump in plankton in a subtropical marginal sea. Mar 2024. URL: https://doi.org/10.1128/spectrum.02177-23, doi:10.1128/spectrum.02177-23. This article has 6 citations and is from a domain leading peer-reviewed journal.

11. (tothero2024leptothrixochraceagenomes media 8c5a0a3a): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

12. (tothero2024leptothrixochraceagenomes media 1e58a269): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

13. (parada2023constrainingthecomposition pages 1-6): Alma E. Parada, Xavier Mayali, Peter K. Weber, Jessica Wollard, Alyson E. Santoro, Jed A. Fuhrman, Jennifer Pett‐Ridge, and Anne E. Dekas. Constraining the composition and quantity of organic matter used by abundant marine thaumarchaeota. Dec 2023. URL: https://doi.org/10.1111/1462-2920.16299, doi:10.1111/1462-2920.16299. This article has 20 citations and is from a domain leading peer-reviewed journal.