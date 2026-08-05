---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:54:30.062095'
end_time: '2026-08-04T11:04:30.246931'
duration_seconds: 600.18
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemolithotrophic
  trait_identifier: METPO:1000639
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemolithotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type characterized by the use of inorganic chemical compounds
    as electron donors and carbon dioxide as the primary carbon source for energy
    generation and biosynthesis.
  parent_traits: METPO:1000631
  synonyms: chemolithotroph
  evidence_summary: "DOI:10.1016/B978-0-12-378630-2.00219-X: chemolithotrophic bacteria\
    \ and archaea (Review supports inorganic compound oxidation as chemolithotrophic\
    \ growth.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing\
    \ bacteria (Review supports ammonia oxidation as an example chemolithoautotrophic\
    \ process.) | PMID:12700255: Nitrosomonas europaea (Organism example: Nitrosomonas\
    \ europaea is the model chemolithotrophic ammonia-oxidizing bacterium, conserving\
    \ energy from NH3 \u2192 NO2- oxidation (Chain et al. 2003, J Bacteriol, complete\
    \ genome).)"
  causal_graph_summary: 'chemolithotrophic_inorganic_oxidation: 15 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 60
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemolithotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000639
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of inorganic chemical compounds as electron donors and carbon dioxide as the primary carbon source for energy generation and biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: chemolithotrophic bacteria and archaea (Review supports inorganic compound oxidation as chemolithotrophic growth.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation as an example chemolithoautotrophic process.) | PMID:12700255: Nitrosomonas europaea (Organism example: Nitrosomonas europaea is the model chemolithotrophic ammonia-oxidizing bacterium, conserving energy from NH3 → NO2- oxidation (Chain et al. 2003, J Bacteriol, complete genome).)
- **Existing causal graph summary:** chemolithotrophic_inorganic_oxidation: 15 nodes, 10 edges

## Research Objective

Research the microbial trait **chemolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithotrophic.yaml`.

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
- **Trait label:** chemolithotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000639
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of inorganic chemical compounds as electron donors and carbon dioxide as the primary carbon source for energy generation and biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: chemolithotrophic bacteria and archaea (Review supports inorganic compound oxidation as chemolithotrophic growth.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation as an example chemolithoautotrophic process.) | PMID:12700255: Nitrosomonas europaea (Organism example: Nitrosomonas europaea is the model chemolithotrophic ammonia-oxidizing bacterium, conserving energy from NH3 → NO2- oxidation (Chain et al. 2003, J Bacteriol, complete genome).)
- **Existing causal graph summary:** chemolithotrophic_inorganic_oxidation: 15 nodes, 10 edges

## Research Objective

Research the microbial trait **chemolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithotrophic.yaml`.

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


# Curation report: chemolithotrophic

## 1. Executive scope

**Trait:** chemolithotrophic  
**Identifier:** `METPO:1000639`  
**Category:** PHYSIOLOGY; **term kind:** CLASS; **mapping:** REVIEWED  
**Parent:** `METPO:1000631`  
**Synonym:** chemolithotroph

For this term, the defensible scope is **chemolithoautotrophy**: a cell oxidizes one or more inorganic chemical electron donors, conserves the released energy as ATP and reducing power, and uses CO2/dissolved inorganic carbon as its primary biomass-carbon source. The phenotype therefore requires both an **energy module** and an **autotrophic carbon-assimilation module**. Oxidation of an inorganic compound alone is insufficient.

This interpretation agrees with contemporary descriptions of chemolithoautotrophs as organisms that use energy released by oxidation of reduced compounds to drive inorganic-carbon fixation. It also matches the supplied definition more narrowly than the broader usage of “chemolithotroph,” which can include organisms using inorganic donors but organic carbon. (laufermeiser2024oxidationofsulfur pages 1-2, bayer2024contributionofammonia pages 1-4)

### Recommended inclusion criteria

Curate the trait when evidence establishes:

1. Growth or energy conservation supported by an inorganic donor such as NH3, NO2−, H2, Fe2+, H2S/HS−, S0, thiosulfate, CO, or another reduced inorganic compound.
2. CO2/HCO3−/DIC as the primary carbon source, preferably demonstrated by growth in mineral medium, isotope incorporation, or a complete and expressed fixation pathway.
3. A compatible electron acceptor and respiratory or energy-conserving mechanism.
4. Biomass production or sustained growth—not merely oxidation, detoxification, or transient maintenance.

### Boundary cases

- **Chemolithoheterotrophy:** inorganic donor oxidation with organic carbon as the biomass source is outside this term. *Arcobacter peruensis* oxidizes sulfide and reduces nitrate but assimilates acetate and does not substantially fix CO2; it is therefore a strong negative-control example. (callbeck2019arcobacterperuensissp. pages 1-2)
- **Mixotrophy:** simultaneous CO2 fixation and organic-carbon uptake should be represented separately or qualified as facultative/mixotrophic. In sulfur-stimulated groundwater microcosms, mixotrophs rather than strict autotrophs dominated and balanced CO2 fixation with organic-carbon uptake. (taubert2022bolsteringfitnessvia pages 1-2)
- **Electroautotrophy:** direct uptake of electrode-derived electrons can support CO2 fixation, but it is mechanistically distinct because the energy input is an electrode rather than oxidation of an inorganic chemical donor. *Acidithiobacillus ferrooxidans* changes pilin, porin, EPS, and electron-transfer expression under electrode growth. (wang2024characterizethegrowth pages 22-23)
- **Photolithoautotrophy:** light, rather than chemical oxidation, is the principal energy source and should be excluded.
- **Methanotrophy/methylotrophy:** methane and reduced one-carbon organics are generally treated as organic substrates, not lithotrophic donors. H2-supported growth by a methanotroph may represent mixotrophic flexibility rather than the defining trait.
- **Sulfur detoxification:** possession or activity of Sqr alone does not establish energy-conserving sulfur chemolithotrophy. Donor disappearance must be linked to respiration, ATP/reductant formation, CO2 fixation, and growth.
- **Genomic potential alone:** donor-oxidation genes plus carbon-fixation genes are suggestive but do not prove that the modules are simultaneously functional.

## 2. Candidate nodes

Only identifiers that can be used with high confidence are given below. Nodes whose exact database accession depends on protonation state, species, enzyme family, or taxonomic context should remain **label-only pending ontology lookup** rather than receive a guessed CURIE.

### Trait and biological-process nodes

- chemolithotrophic — `METPO:1000639`
- Calvin–Benson–Bassham cycle — `GO:0019253`
- proton transmembrane transport — `GO:0015992`
- ATP synthesis coupled to proton transport — use the appropriate GO child after confirming cellular context
- reductive TCA cycle — label only pending exact pathway grounding
- 3-hydroxypropionate/4-hydroxybutyrate cycle — label only pending exact pathway grounding
- Wood–Ljungdahl pathway, 3-hydroxypropionate bicycle, dicarboxylate/4-hydroxybutyrate cycle — optional taxon-specific alternatives; do not imply that every chemolithotroph uses the CBB cycle
- phosphoglycolate salvage; glycerate pathway; malate cycle — label-only maintenance modules

### Chemicals and environmental factors

**Electron donors:** ammonia, nitrite, molecular hydrogen, ferrous iron, hydrogen sulfide/sulfide, elemental sulfur, thiosulfate, carbon monoxide, and potentially other reduced inorganic species. Preserve chemical state explicitly—for example, NH3 rather than NH4+ for AMO substrate and Fe2+ rather than generic “iron.” The 2023 AOA review states that NH3, not NH4+, is the AMO substrate. (wright2023nitrificationandbeyond pages 1-2)

**Carbon source:** carbon dioxide — `CHEBI:16526`; bicarbonate/DIC may be included as experimentally supplied inorganic-carbon forms.

**Electron acceptors:** oxygen, nitrate, and—in taxon-specific anaerobic systems—Fe3+. Hydrogen-grown *A. ferrooxidans* can transfer electrons to O2 aerobically or Fe3+ anaerobically. (kucera2020amodelof pages 1-2, kucera2020amodelof pages 4-8)

**Energy/redox products:** ATP — `CHEBI:15422`; NADH — `CHEBI:57540`; NADPH; proton motive force; quinone/quinol pools.

**Environmental nodes:** oxic, microoxic, and anoxic conditions; low pH; hydrothermal vent mixing zone; aphotic/dark ocean; groundwater; sulfide–nitrate redoxcline; bioleaching reactor; donor concentration; CO2 availability; temperature and salinity.

**Experimental factor:** phenylacetylene, an AMO inhibitor used to estimate ammonia-oxidizer-supported DIC fixation. Because the recent quantitative study is a preprint and inhibitor specificity is assay-dependent, this node should be explicitly qualified. (bayer2024contributionofammonia pages 1-4)

### Genes, proteins, enzymes, and complexes

- **Ammonia module:** `amoA`, `amoB`, `amoC`; archaeal `amoX`, `amoY`, `amoZ`; ammonia monooxygenase complex; Amt and Rh-type ammonia/ammonium transport systems; downstream hydroxylamine/NO-processing components. Archaeal downstream chemistry remains incompletely resolved. (wright2023nitrificationandbeyond pages 3-5)
- **Hydrogen module:** uptake [NiFe] hydrogenases, including taxon-specific `hyaAB`, `hupUV`, Hyn, Hup, and Hox systems; associated Fe–S electron-transfer proteins. (laufermeiser2024oxidationofsulfur pages 4-6, kucera2020amodelof pages 1-2)
- **Sulfur module:** Sox system (`sox` genes), Sqr/SQO, sulfur oxygenase reductase, thiosulfate:quinone oxidoreductase, and oxidative/reverse Dsr components. These should be modeled as alternative, taxon-specific branches rather than one universal linear pathway. (zeldes2019determinantsofsulfur pages 1-5, laufermeiser2024oxidationofsulfur pages 4-6, srivastava2023interplaybetweenautotrophic pages 5-7)
- **Iron module:** Cyc2, rusticyanin, Cyc1/cytochrome c552, high-potential Fe–S protein, cytochrome bc1, terminal oxidases, and reverse electron-transport machinery in acidophiles. In neutrophilic *Hydrogenovibrio*, known `cyc2`/`mtoAB` genes were not identified, so its Fe(II)-oxidation mechanism remains unresolved. (laufermeiser2024oxidationofsulfur pages 4-6)
- **Electron transport and bioenergetics:** quinone/quinol pool, cytochrome bc1, cytochrome c4, cytochrome aa3 oxidase, cytochrome bd oxidase, complex I/NADH dehydrogenase, and F1F0 ATP synthase.
- **CBB module:** Rubisco — `EC:4.1.1.39`; phosphoribulokinase/CbbP — `EC:2.7.1.19`; `cbbL`, `cbbS`, `cbbM`, `cbbR`; carboxysome shell proteins; Rubisco activases CbbQ/CbbX. The CBB cycle is distinguished by Rubisco and phosphoribulokinase, while carboxysomes elevate CO2 around Rubisco. (asplundsamuelsson2021widerangeof pages 1-2, esparza2010genesandpathways pages 1-2)
- **Alternative carbon-fixation modules:** ATP citrate lyase (`acl`), 2-oxoglutarate:ferredoxin oxidoreductase (`ogor`), and fumarate reductase (`frd`) for the reductive TCA candidate branch; enzymes of the archaeal 3-HP/4-HB cycle.

### Taxon/example nodes

- *Nitrosomonas europaea*: model bacterial ammonia oxidizer; supplied evidence remains appropriate.
- ammonia-oxidizing archaea: abundant, ecologically important ammonia-to-nitrite chemolithoautotrophs. (wright2023nitrificationandbeyond pages 1-2)
- *Hydrogenovibrio* strain 104 and related isolates: experimentally verified Fe2+, H2, and thiosulfate oxidation coupled to CO2 fixation. (laufermeiser2024oxidationofsulfur pages 4-6, laufermeiser2024oxidationofsulfur pages 1-2)
- *Acidithiobacillus ferrooxidans*: acidophilic iron-, sulfur-, and H2-utilizing model with well-developed electron-transport and CBB models. (esparza2010genesandpathways pages 1-2, kucera2020amodelof pages 1-2)
- *Acidianus brierleyi* and other Sulfolobales: sulfur oxidation coupled to the 3-HP/4-HB cycle. (zeldes2019determinantsofsulfur pages 1-5)
- *Cupriavidus necator* H16 — `NCBITaxon:381666`: H2-oxidizing CBB-model organism and experimental model of phosphoglycolate salvage. (claassens2020phosphoglycolatesalvagein pages 1-2)
- *Arcobacter peruensis*: negative/boundary example for chemolithoheterotrophy. (callbeck2019arcobacterperuensissp. pages 1-2)

## 3. Evidence-backed candidate causal edges

The following artifact is the principal curation table. It includes subject–predicate–object triples, suggested grounding, DOI/year, supporting snippets, and explicit uncertainty or taxonomic restrictions.

| Subject | Predicate | Object | Suggested grounding | Evidence DOI/year | Supporting snippet | Scope/uncertainty |
|---|---|---|---|---|---|---|
| chemolithotrophic growth | has defining feature | inorganic electron donor oxidation coupled to autotrophic CO2 fixation | METPO:1000639; CHEBI:16526 (CO2) | 10.1093/ismejo/wrae173 (2024) | “oxidation of these reduced substances to conserve energy that can be utilized for autotrophic CO2 fixation” (laufermeiser2024oxidationofsulfur pages 1-2) | Generic scope statement; supported in hydrothermal vent context but consistent with trait definition. |
| chemolithotrophic growth | excludes | organic carbon as primary biomass carbon source | label only | 10.1128/AEM.01344-19 (2019) | “assimilated acetate but did not fix CO2, thus coupling heterotrophic growth to sulfide oxidation and denitrification” (callbeck2019arcobacterperuensissp. pages 1-2) | Boundary/counterexample: defines chemolithoheterotrophy, not chemolithotrophy sensu this term. |
| reduced sulfur compounds | can fuel | chemolithoautotrophic activity | CHEBI:26896 (sulfur compound) | 10.1038/s41396-021-01163-x (2022) | “inorganic electron donors such as reduced nitrogen, iron, and sulfur fuel chemolithoautotrophic activity” (taubert2022bolsteringfitnessvia pages 1-2) | Generic environmental support. |
| ammonia (NH3) | is substrate for | ammonia monooxygenase (AMO) | CHEBI:16134; GO:0008178? label only for AMO complex | 10.1038/s41396-023-01467-0 (2023) | “Ammonia (NH3), rather than ammonium (NH4+), is the substrate oxidised by the key enzyme ammonia monooxygenase (AMO)” (wright2023nitrificationandbeyond pages 1-2) | Strong for AOA/AOB ammonia oxidation module. |
| ammonia monooxygenase (AmoA/AmoB/AmoC complex) | oxidizes | ammonia during chemolithotrophy | label only | 10.1038/s41396-023-01467-0 (2023) | “The AMO is predicted to exist as a heterotrimeric complex composed of three subunits in bacteria: AmoA, AmoB, and AmoC” (wright2023nitrificationandbeyond pages 3-5) | Mechanistic edge is standard but wording here is partly predictive for AOA; curate with note that archaeal AMO has extra subunits AmoX/Y/Z. |
| ammonia oxidation pathway | generates | reductant for ATP synthesis and carbon fixation | label only | 10.1038/s41396-023-01467-0 (2023) | “two net electrons per ammonia molecule are generated from the ammonia oxidation pathway and this reductant powers the ATP synthesis and cellular anabolism, including carbon fixation” (wright2023nitrificationandbeyond pages 3-5) | Strong for AOA review-level mechanism. |
| phenylacetylene | inhibits | ammonia monooxygenase-dependent dark DIC fixation contribution | CHEBI: label only; AMO label only | 10.1101/2024.11.16.623942 (2024) | “phenylacetylene - a specific inhibitor of the ammonia monooxygenase enzyme - to selectively inhibit ammonia oxidizers” (bayer2024contributionofammonia pages 1-4) | Preprint; assay-specific inhibitor evidence. |
| ammonia oxidizers | contribute to | 2–22% of depth-integrated dark DIC fixation in eastern tropical Pacific | label only | 10.1101/2024.11.16.623942 (2024) | “accounting for 2 to 22% of the depth-integrated rates… up to 50% of dark DIC fixation” (bayer2024contributionofammonia pages 1-4) | Recent quantitative ecological result; preprint, not trait-mechanistic edge per se. |
| [NiFe] hydrogenase | oxidizes | H2 | EC:1.12.-.- (broad); CHEBI:18276 | 10.3389/fmicb.2020.610836 (2020) | “[NiFe] hydrogenases oxidize hydrogen to two protons and two electrons” (kucera2020amodelof pages 1-2) | Strong for hydrogen-oxidation module in A. ferrooxidans. |
| [NiFe] hydrogenase | reduces | ubiquinone to ubiquinol via associated Fe-S proteins | CHEBI:16389 (ubiquinone-8) label only if specificity uncertain | 10.3389/fmicb.2020.610836 (2020) | “The electrons are used to reduce membrane-soluble ubiquinone to ubiquinol. Genetically associated iron-sulfur proteins mediate electron relay” (kucera2020amodelof pages 1-2) | Strong but taxon-specific to A. ferrooxidans model. |
| ubiquinol | transfers electrons to | cytochrome aa3 oxidase via cytochrome bc1 and cytochrome c4 | GO:0008121? label only | 10.3389/fmicb.2020.610836 (2020) | “reduced ubiquinol transfers electrons to either cytochrome aa3 oxidase via cytochrome bc1 complex and cytochrome c4” (kucera2020amodelof pages 1-2) | Aerobic hydrogen oxidation in A. ferrooxidans; taxon-specific. |
| ubiquinol | transfers electrons to | cytochrome bd oxidase | label only | 10.3389/fmicb.2020.610836 (2020) | “or the alternate directly to cytochrome bd oxidase” (kucera2020amodelof pages 1-2) | Aerobic branch; taxon-specific. |
| anaerobic hydrogen oxidation | transfers electrons to | ferric iron via outer-membrane cytochrome c / rusticyanin cascade | CHEBI:29033 (Fe3+) label only for proteins | 10.3389/fmicb.2020.610836 (2020) | “transfers electrons to outer membrane cytochrome c (ferrireductase) via… cytochrome c552, rusticyanin, and high potential iron-sulfur protein” (kucera2020amodelof pages 1-2) | Taxon-specific model for A. ferrooxidans. |
| hydrogen oxidation | generates | proton gradient | GO:0015992 | 10.3389/fmicb.2020.610836 (2020) | “The proton gradient generated by hydrogen oxidation maintains the membrane potential” (kucera2020amodelof pages 1-2) | Strong, taxon-specific. |
| proton gradient | enables generation of | ATP and NADH | CHEBI:15422 (ATP); CHEBI:57540 (NADH) | 10.3389/fmicb.2020.610836 (2020) | “allows the generation of ATP and NADH” (kucera2020amodelof pages 1-2) | Strong, taxon-specific. |
| Hydrogenovibrio strain 104 | fixes CO2 via | Calvin-Benson-Bassham cycle | GO:0019253 | 10.1093/ismejo/wrae173 (2024) | “Autotrophic CO2 fixation in Hydrogenovibrio is operated by the Calvin-Benson-Bassham cycle with RubisCO as the key carboxylating enzyme” (laufermeiser2024oxidationofsulfur pages 4-6) | Strong, taxon-specific. |
| RubisCO | is key carboxylating enzyme of | Calvin-Benson-Bassham cycle | EC:4.1.1.39; GO:0016984 | 10.1093/ismejo/wrae173 (2024) | “with RubisCO as the key carboxylating enzyme” (laufermeiser2024oxidationofsulfur pages 4-6) | Strong, generalizable. |
| thiosulfate oxidation by Hydrogenovibrio strain 104 | supports | higher CO2 fixation than H2 or Fe(II) oxidation | CHEBI:9569 (thiosulfate) | 10.1093/ismejo/wrae173 (2024) | “The highest rates of 14C-HCO3− fixation… were found when the culture was grown with S2O32−, whereas the lowest… with Fe(II)” (laufermeiser2024oxidationofsulfur pages 4-6) | Quantitative taxon-specific physiology. |
| Hydrogenovibrio strain 104 | exhibits CO2 fixation rate | 23.30 fmol C cell−1 h−1 on thiosulfate | label only | 10.1093/ismejo/wrae173 (2024) | “S2O32− oxidation strain 104 … 23.30 ± 1.72 fmol C-fixation cell−1 h−1” (laufermeiser2024oxidationofsulfur pages 4-6) | Quantitative trait evidence; strain-specific. |
| Hydrogenovibrio spp. | possess | group 1 (hyaAB) and group 2b (hupUV) hydrogenases | label only | 10.1093/ismejo/wrae173 (2024) | “possess [NiFe]-hydrogenases of group 1 (hyaAB) and group 2b (hupUV)” (laufermeiser2024oxidationofsulfur pages 4-6) | Strong for hydrogen module in this genus. |
| hydrogenase-related genes | are upregulated by | H2 growth condition | label only | 10.1093/ismejo/wrae173 (2024) | “Hydrogenase-related genes were upregulated in cells grown on H2 relative to those on S2O32−” (laufermeiser2024oxidationofsulfur pages 4-6) | Transcriptomic; use as supportive, not sole causal proof. |
| Sox enzyme system | participates in | thiosulfate oxidation | label only | 10.1093/ismejo/wrae173 (2024) | “Hydrogenovibrio species rely on the Sox enzyme system… for S2O32− oxidation” (laufermeiser2024oxidationofsulfur pages 4-6) | Strong for sulfur/thiosulfate module in Hydrogenovibrio. |
| sulfide:quinone reductase (Sqr) | participates in | thiosulfate/sulfide-linked sulfur oxidation | label only | 10.1093/ismejo/wrae173 (2024) | “rely on the Sox enzyme system and the sulfide:quinone reductase (Sqr) for S2O32− oxidation” (laufermeiser2024oxidationofsulfur pages 4-6) | Mechanistically plausible but wording conflates sulfur species; taxon-specific. |
| thiosulfate amendment | stimulates transcription of | reductive TCA cycle genes (acl, ogor, frd) | label only | 10.1186/s40168-023-01688-7 (2023) | “stimulation of transcription of genes involved in the reductive citric acid cycle (ATP citrate lyase (acl), 2-oxoglutarate:ferredoxin oxidoreductase (ogor), fumarate reductase (frd))” (srivastava2023interplaybetweenautotrophic pages 5-7) | Transcriptomic community evidence; inferred chemoautotrophy pathway. |
| sulfur oxidation gene expression | can couple to | CO2 fixation pathways in dark ocean communities | label only | 10.1186/s40168-023-01688-7 (2023) | “genes involved in energy production via sulfur oxidation and coupled to CO2 fixation pathways” (srivastava2023interplaybetweenautotrophic pages 1-2) | Community-level, transcript-based; not organism-resolved. |
| sox transcripts | increase under | thiosulfate amendment | label only | 10.1186/s40168-023-01688-7 (2023) | “Gene expression of sox enzymes slightly increased” (srivastava2023interplaybetweenautotrophic pages 5-7) | Weak effect size (~1.3-fold with thiosulfate+DOM); transcriptomic only. |
| dsr transcripts | increase under | thiosulfate + DOM amendment | label only | 10.1186/s40168-023-01688-7 (2023) | “Transcripts of dissimilatory sulfite reductase (dsr) subunits were ~two-fold upregulated” (srivastava2023interplaybetweenautotrophic pages 5-7) | Transcriptomic only; role in oxidation vs reduction context may vary by taxon. |
| sulfur oxygenase reductase (SOR) | disproportionates | elemental sulfur to H2S and sulfite | label only | 10.1111/1462-2920.14712 (2019) | “sulfur oxygenase reductase (SOR) that disproportionates S° into H2S and sulfite (SO32-)” (zeldes2019determinantsofsulfur pages 1-5) | Strong for Sulfolobales sulfur chemolithotrophy. |
| thiosulfate-quinone oxidoreductase (TQO) | contributes to | sulfur oxidation capacity | label only | 10.1111/1462-2920.14712 (2019) | “heterologous expression of both SOR and membrane-bound thiosulfate-quinone oxidoreductase (TQO)… ‘restored’ sulfur oxidation capacity” (zeldes2019determinantsofsulfur pages 1-5) | Sulfolobales-specific; sulfur oxidation alone did not restore autotrophy. |
| sulfur oxidation capacity alone | is insufficient for | chemolithoautotrophic growth without carbon fixation gene regulation | label only | 10.1111/1462-2920.14712 (2019) | “restored sulfur oxidation capacity… but not autotrophy… failed to up-regulate key 3-HP/4-HB cycle genes” (zeldes2019determinantsofsulfur pages 1-5) | Important causal boundary: donor oxidation ≠ full trait. |
| 3-hydroxypropionate/4-hydroxybutyrate cycle genes | are required for | sulfur chemolithoautotrophy in Sulfolobales | GO:0019646? label only | 10.1111/1462-2920.14712 (2019) | “failed to up-regulate key 3-HP/4-HB cycle genes used by A. brierleyi to drive chemolithoautotrophy” (zeldes2019determinantsofsulfur pages 1-5) | Strong within Sulfolobales; regulatory dependence noted. |
| Fe2+ oxidation in A. ferrooxidans | supplies energy/reducing power for | obligate chemolithoautotrophic growth | CHEBI:29033? Fe3+/CHEBI:29033 not donor; Fe2+ label only | 10.1186/1471-2180-10-229 (2010) | “gains energy and reducing power from the oxidation of ferrous iron and reduced inorganic sulfur compounds” (esparza2010genesandpathways pages 1-2) | Strong organism-level evidence. |
| reduced inorganic sulfur compounds oxidation in A. ferrooxidans | supplies energy/reducing power for | obligate chemolithoautotrophic growth | label only | 10.1186/1471-2180-10-229 (2010) | “gains energy and reducing power from the oxidation of ferrous iron and reduced inorganic sulfur compounds” (esparza2010genesandpathways pages 1-2) | Strong organism-level evidence. |
| A. ferrooxidans genome | encodes | cbb1-cbb4 operons for Calvin cycle and carboxysomes | label only | 10.1186/1471-2180-10-229 (2010) | “Four gene clusters (termed cbb1-4)… including form I… RubisCO… and the CO2-concentrating carboxysomes” (esparza2010genesandpathways pages 1-2) | Strong for carbon-fixation module. |
| CbbR | binds upstream of | cbb1/cbb2/cbb3 operons | label only | 10.1186/1471-2180-10-229 (2010) | “EMSAs confirmed that purified CbbR is able to bind to the upstream regions of the cbb1, cbb2 and cbb3 operons” (esparza2010genesandpathways pages 1-2) | Regulatory edge; in vitro binding evidence. |
| phosphoribulokinase (cbbP) | is enzyme of | Calvin cycle | EC:2.7.1.19 | 10.1186/1471-2180-10-229 (2010) | “cbbP, encoding phosphoribulokinase (EC 2.7.1.19)” (esparza2010genesandpathways pages 1-2) | Strong. |
| Calvin cycle | requires hallmark enzymes | Rubisco and phosphoribulokinase | EC:4.1.1.39; EC:2.7.1.19 | 10.1371/journal.pcbi.1008742 (2021) | “The Calvin cycle is distinguished by phosphoribulokinase (Prk)… and ribulose bisphosphate carboxylase/oxygenase (Rubisco)” (asplundsamuelsson2021widerangeof pages 1-2) | General comparative-genomics support. |
| carboxysome proteins | raise concentration of | CO2 around Rubisco | GO:0031469? label only | 10.1371/journal.pcbi.1008742 (2021) | “carboxysome proteins (that raise CO2 concentration around Rubisco)” (asplundsamuelsson2021widerangeof pages 1-2) | Strong general support. |
| Calvin cycle-positive microbes | are commonly associated with | hydrogenase genes | label only | 10.1371/journal.pcbi.1008742 (2021) | “chemoautotrophy in Calvin cycle-positive organisms was commonly enabled by hydrogenase” (asplundsamuelsson2021widerangeof pages 1-2) | Comparative-genomics association; inferred, not direct mechanism. |
| aerobic Calvin-cycle chemolithoautotrophs | must recycle | 2-phosphoglycolate | CHEBI:17363? label only if uncertain | 10.1073/pnas.2012288117 (2020) | “aerobic chemolithoautotrophic bacteria that operate the Calvin cycle… must also recycle phosphoglycolate” (claassens2020phosphoglycolatesalvagein pages 1-2) | Strong for maintenance submodule. |
| Cupriavidus necator H16 | mainly uses | glycerate pathway for phosphoglycolate salvage | NCBITaxon:381666 | 10.1073/pnas.2012288117 (2020) | “mainly reassimilates 2-phosphoglycolate via the glycerate pathway” (claassens2020phosphoglycolatesalvagein pages 1-2) | Strong but taxon-specific. |
| malate cycle | can support | phosphoglycolate salvage in chemolithoautotrophs | label only | 10.1073/pnas.2012288117 (2020) | “a secondary route, which we term the malate cycle, supports photorespiration” (claassens2020phosphoglycolatesalvagein pages 1-2) | Experimental in C. necator; broader distribution inferred bioinformatically. |
| Arcobacter peruensis | lacks | autotrophic CO2 fixation despite sulfide oxidation and denitrification genes | NCBITaxon:label only | 10.1128/AEM.01344-19 (2019) | “possesses genes encoding sulfide oxidation and denitrification pathways but lacks the ability to fix CO2” (callbeck2019arcobacterperuensissp. pages 1-2) | Boundary counterexample: chemolithoheterotrophy. |
| sulfide + nitrate + acetate | supports best growth of | Arcobacter peruensis | CHEBI:16189 (acetate) label only others | 10.1128/AEM.01344-19 (2019) | “grew best on a mix of sulfide, nitrate, and acetate” (callbeck2019arcobacterperuensissp. pages 1-2) | Counterexample showing inorganic donor use without autotrophic carbon sourcing. |
| mixotrophs in groundwater | can balance | CO2 fixation and organic carbon uptake | label only | 10.1038/s41396-021-01163-x (2022) | “balancing CO2 fixation and uptake of available organic compounds” (taubert2022bolsteringfitnessvia pages 1-2) | Boundary case: not strict chemolithotrophy. |
| groundwater microcosm activity | replaced | 43% and 80% of microbial carbon with 13C by days 21 and 70 | label only | 10.1038/s41396-021-01163-x (2022) | “replacement of 43% and 80% of total microbial carbon stores… with 13C in just 21 and 70 days” (taubert2022bolsteringfitnessvia pages 1-2) | Quantitative ecosystem result; mixotrophy caveat. |
| electrode-derived electrons | can support | electroautotrophic growth distinct from chemoautotrophy | label only | 10.3390/microorganisms12030590 (2024) | “utilize either Fe2+ oxidation (chemoautotrophy) or direct electrons from solid electrodes (electroautotrophy) as sole energy sources” (wang2024characterizethegrowth pages 22-23) | Boundary counterexample: not chemolithotrophy because donor is not an inorganic chemical compound. |
| electroautotrophic growth in A. ferrooxidans | upregulates | pilin/porin and direct electron transfer functions | label only | 10.3390/microorganisms12030590 (2024) | “genes encoding transmembrane proteins for direct electron transfer (pilin, porin) showed increased expression” (wang2024characterizethegrowth pages 22-23) | Transcriptomic boundary evidence; not curate as chemolithotrophy mechanism. |
| electroautotrophic growth in A. ferrooxidans | downregulates | genes essential for chemoautotrophy | label only | 10.3390/microorganisms12030590 (2024) | “genes essential for chemoautotrophy showed decreased expression” (wang2024characterizethegrowth pages 22-23) | Boundary evidence separating mechanisms. |
| A. ferrooxidans biomining metabolism | generates | Fe(III) ions that react with metal sulfides | CHEBI:29033 (Fe3+) label only for metal sulfides | 10.3390/microorganisms12122407 (2024) | “A. ferrooxidans catalyzes the extraction of elements by generating iron (III) ions in oxic conditions, which are able to react with metal sulfides” (tonietti2024unveilingthebioleaching pages 1-2) | Application-focused review; useful for implementation context, less direct for trait graph. |
| A. ferrooxidans | mobilizes elements in bioleaching because of | ferrous iron and sulfur oxidation chemolithoautotrophy | label only | 10.3390/microorganisms12122407 (2024) | “derive energy through the oxidation of inorganic compounds and fix carbon dioxide as their carbon source” (tonietti2024unveilingthebioleaching pages 1-2) | Application review; broad organism-level confirmation. |
| Kucera Figure 4 model | integrates | hydrogenases, quinone pool, cytochromes, proton flow, ATP/NADH, and Calvin cycle | label only | 10.3389/fmicb.2020.610836 (2020) | Figure described as including “hydrogenases… quinone pool… cytochromes… proton flow… ATP and NADH production, and the CO2 fixation pathway (Calvin cycle)” (kucera2020amodelof media efa0d4aa) | Image-derived support for pathway organization; use as corroborative visual evidence. |


*Table: This table compiles candidate causal edges for curating the chemolithotrophic trait, including generic mechanisms, donor-specific modules, carbon fixation pathways, and boundary counterexamples. It highlights where evidence is direct versus transcriptomic, comparative, model-based, or preprint-only.*

### Highest-confidence core for the YAML graph

A compact, taxon-neutral core should contain these logical edges:

1. **inorganic electron donor — is oxidized by → donor-oxidation module**
2. **donor-oxidation module — transfers electrons to → respiratory electron-transport chain**
3. **respiratory electron-transport chain — generates → ion motive force**
4. **ion motive force — drives → ATP synthesis**
5. **electron transport/reverse electron transport — generates → reducing power**
6. **ATP + reducing power — enable → autotrophic CO2 fixation**
7. **autotrophic CO2 fixation — produces → biomass carbon**
8. **inorganic donor oxidation + CO2-derived biomass + growth — realizes → `METPO:1000639`**

Edges 1–5 should branch into donor- and taxon-specific subgraphs. A single universal enzyme chain would be biologically inaccurate.

### Mechanistic exemplar: hydrogen oxidation

In *A. ferrooxidans*, [NiFe] hydrogenases oxidize H2 to protons and electrons; Fe–S proteins relay electrons to ubiquinone. Aerobically, ubiquinol feeds cytochrome aa3 through bc1/cytochrome c4 or cytochrome bd directly, reducing O2. Anaerobically, a cytochrome/rusticyanin cascade transfers electrons to Fe3+. The resulting proton gradient sustains membrane potential and ATP/NADH generation. (kucera2020amodelof pages 1-2)

The published pathway figure visually integrates hydrogenases, the quinone pool, cytochromes, terminal acceptors, proton movement, ATP/NADH formation, and CBB carbon fixation. It should be treated as a **taxon-specific mechanistic model**, not a universal chemolithotrophy diagram. (kucera2020amodelof media efa0d4aa)

### Mechanistic exemplar: ammonia oxidation

AMO oxidizes NH3 and is a copper-dependent membrane complex. Bacterial AMO is represented by AmoABC; archaeal AMO is divergent and includes additional proposed subunits. The current AOA model yields two net electrons per ammonia, which support ATP synthesis and anabolism, including carbon fixation, but the hydroxylamine/NO branch and exact electron carriers remain unresolved. (wright2023nitrificationandbeyond pages 1-2, wright2023nitrificationandbeyond pages 3-5)

### Mechanistic exemplar: sulfur oxidation

Sulfur chemolithotrophy is modular. Sox, Sqr/SQO, TQO, SOR, and oxidative Dsr pathways occur in different combinations. In Sulfolobales, SOR disproportionates S0 to H2S and sulfite, while quinone-linked enzymes deliver electrons to respiration; CO2 fixation proceeds through the 3-HP/4-HB cycle. Crucially, restoring SOR and TQO restored sulfur oxidation in *Sulfolobus acidocaldarius* but did not restore autotrophy because key 3-HP/4-HB genes were not appropriately upregulated. This is direct evidence that donor oxidation alone does not establish the trait. (zeldes2019determinantsofsulfur pages 1-5)

## 4. Recent developments, 2023–2024

### Multi-donor chemolithoautotrophy at hydrothermal vents

Laufer-Meiser and colleagues isolated three *Hydrogenovibrio* strains able to grow with Fe2+, H2, or thiosulfate. For strain 104, cell-specific CO2-fixation rates were **23.30 ± 1.72 fmol C cell−1 h−1 on thiosulfate**, **0.29 ± 0.019 on H2**, and **0.09 ± 0.082 on Fe2+**. Maximum thiosulfate-oxidation rates among the three cultures ranged from 1.05 to 2.06 μmol ml−1 h−1. The authors estimated per-vent-per-hour potentials of 10, 24, and 952 mmol for Fe, H2, and thiosulfate oxidation and 0.3, 1, and 84 mmol CO2 fixation, respectively. Known Fe-oxidation genes were not detected, making the Fe branch physiologically established but molecularly unresolved. Published 14 September 2024. (laufermeiser2024oxidationofsulfur pages 4-6, laufermeiser2024oxidationofsulfur pages 1-2)

### Revised understanding of ammonia-oxidizing archaea

The 2023 authoritative review emphasizes wide ecological variation rather than a single uniformly streamlined phenotype. Apparent ammonia affinities span more than four orders of magnitude: from **<2.8 nM** in some Nitrosopumilales/“Ca. Nitrosotaleales” to **>12 μM** in characterized *Nitrosocosmicus*. Oxygen affinity and nitrogen-assimilation systems further differentiate niches. Published 14 July 2023. (wright2023nitrificationandbeyond pages 1-2, wright2023nitrificationandbeyond pages 3-5)

### Dark-ocean sulfur-supported carbon fixation

At approximately 2,000 m depth in Labrador Sea Water, 1 μM thiosulfate increased inorganic-carbon fixation and stimulated sulfur oxidizers. Reductive-TCA transcripts—including `acl`, `ogor`, and `frd`—rose by as much as sixfold; cardiolipin-synthase expression increased up to 2.5-fold, and community-level `dsr` transcripts were approximately doubled under thiosulfate plus DOM. However, organism-resolved coupling was incomplete, and organic-carbon addition promoted strong heterotrophic responses. Published 2023. (srivastava2023interplaybetweenautotrophic pages 1-2, srivastava2023interplaybetweenautotrophic pages 5-7)

### How much dark-ocean fixation is fueled by ammonia oxidation?

A November 2024 **bioRxiv preprint** used phenylacetylene inhibition across the eastern tropical/subtropical Pacific. It estimated that ammonia oxidizers supplied **2–22%** of depth-integrated dark DIC fixation, reaching **up to 50%** near nitrification maxima. Although ammonia-oxidizing archaea can represent up to **40% of deep-water microbial cells**, the result challenges the assumption that nitrification dominates dark-ocean DIC fixation. This ecological claim should remain provisional until peer review and independent validation of inhibitor specificity. (bayer2024contributionofammonia pages 1-4)

### Distinguishing chemical from electrode-driven autotrophy

A 2024 comparison of *A. ferrooxidans* reported 493 differentially expressed genes between electroautotrophic and Fe2+-supported chemoautotrophic growth. Electrode growth increased pilin, porin, EPS, and direct-electron-transfer signatures, while canonical chemoautotrophic genes decreased and CO2 fixation was more restricted. This provides a useful experimental boundary for TraitMech. Published March 2024. (wang2024characterizethegrowth pages 22-23)

## 5. Applications and real-world implementations

### Biomining and bioleaching

*A. ferrooxidans* oxidizes Fe2+ to Fe3+ under oxic conditions; Fe3+ then chemically attacks metal sulfides, regenerating soluble metal and reduced iron for continued microbial oxidation. A 2024 review reports mobilization of Li, P, V, Cr, Fe, Ni, Cu, Zn, Ga, As, Mo, W, Pb, and U and describes the organism as a key biomining platform. Benefits include reduced reliance on energy-intensive extraction, but slow kinetics, metal toxicity, acid generation, acid-mine-drainage risk, regulatory constraints, and incomplete life-cycle evidence remain important limitations. (tonietti2024unveilingthebioleaching pages 1-2, cozma2024biorecoveryofmetals pages 1-2)

### Wastewater nitrogen removal

Ammonia- and nitrite-oxidizing chemolithoautotrophs underpin nitrification in activated sludge, biofilms, and engineered partial-nitritation systems. Their ammonia and oxygen affinities, inhibition profiles, growth yield, and N2O production determine process stability. These applications are genuine implementations of donor-specific chemolithotrophy, but the graph should represent wastewater treatment as a context or application rather than as a defining mechanism. The AOA review also connects nitrifier physiology to nitrate pollution, N2O emissions, food security, and climate. (wright2023nitrificationandbeyond pages 1-2, wright2023nitrificationandbeyond pages 3-5)

### Carbon capture and gas fermentation

H2-oxidizing bacteria combine renewable H2, O2 or another acceptor, and CO2 to produce biomass or chemicals. The mechanistic graph supports these systems through hydrogenase → respiratory chain → ATP/reductant → CBB fixation. Industrial performance, however, additionally depends on gas transfer, explosion control, H2 source, O2 demand, and product engineering; these process-level edges should not be asserted from trait evidence alone.

### Ecosystem primary production

Chemolithoautotrophy supplies new organic carbon in hydrothermal vents, groundwater, redoxclines, and the dark ocean. Nevertheless, metagenomic pathway abundance cannot be converted directly into realized carbon flux. For example, sulfur-stimulated groundwater microcosms replaced **43% and 80%** of microbial carbon with ^13C after 21 and 70 days, respectively, but the most active organisms were mixotrophs rather than strict autotrophs. (taubert2022bolsteringfitnessvia pages 1-2)

## 6. Expert interpretation for TraitMech design

The most robust design is a **two-gate causal graph**:

- **Gate A—lithotrophic energy acquisition:** demonstrated inorganic-donor oxidation must generate electron flow, an ion gradient, ATP, and reductant.
- **Gate B—autotrophic carbon acquisition:** a functional fixation pathway must convert CO2/DIC into biomass.

Only when both gates support growth should the terminal trait node be asserted. This prevents false positives from sulfur-detoxifying heterotrophs, organisms carrying silent fixation genes, anaplerotic DIC incorporation, and electrode-grown autotrophs. The Sulfolobales restoration experiment is particularly informative: biochemical restoration of sulfur oxidation without coordinated carbon-fixation regulation did not restore chemolithoautotrophy. (zeldes2019determinantsofsulfur pages 1-5)

The graph should use **alternative-pathway sets**, not require Rubisco universally. The CBB cycle is common—6.0% of genomes in one broad microbial survey contained it—but chemolithoautotrophs also use reductive TCA, 3-HP/4-HB, Wood–Ljungdahl, and other pathways. (asplundsamuelsson2021widerangeof pages 1-2)

## 7. Curation warnings

1. **Do not curate `gene present → chemolithotrophic` as a sufficient edge.** Require pathway completeness, expression, physiology, or isotope-supported growth.
2. **Do not equate DIC incorporation with autotrophy.** Heterotrophic anaplerosis can fix measurable DIC; organic-carbon dependence must be assessed. (srivastava2023interplaybetweenautotrophic pages 5-7, bayer2024contributionofammonia pages 1-4)
3. **Do not equate inorganic-donor oxidation with autotrophic growth.** *A. peruensis* and sulfur-detoxifying organisms are counterexamples. (callbeck2019arcobacterperuensissp. pages 1-2)
4. **Keep archaeal and bacterial ammonia oxidation separate below AMO.** Archaeal downstream intermediates, active-site architecture, and respiratory components remain incompletely resolved. (wright2023nitrificationandbeyond pages 3-5)
5. **Do not curate a specific Fe(II)-oxidation enzyme for the 2024 *Hydrogenovibrio* isolates.** Fe oxidation and growth were measured, but `cyc2`/`mtoAB` were not detected and the pathway is unknown. (laufermeiser2024oxidationofsulfur pages 4-6)
6. **Treat community transcript correlations as uncertain causal edges.** The dark-ocean `sox`/`dsr` and fixation-pathway associations are not always resolved to the same organism. (srivastava2023interplaybetweenautotrophic pages 1-2, srivastava2023interplaybetweenautotrophic pages 5-7)
7. **Qualify all taxon-specific respiratory chains.** The rusticyanin/cytochrome model from acidophilic *A. ferrooxidans* is not universal. (kucera2020amodelof pages 1-2, kucera2020amodelof media efa0d4aa)
8. **Keep the 2024 ammonia-oxidizer DIC percentages out of the mechanistic core.** They are ecological, inhibitor-dependent, and preprint evidence. (bayer2024contributionofammonia pages 1-4)
9. **Verify ontology accessions before YAML insertion.** In particular, protonation-specific chemicals, Sox/Dsr complexes, hydrogenase groups, carboxysomes, and alternative fixation cycles require database-specific confirmation. Label-only nodes are preferable to invented CURIEs.
10. **Avoid antimonite, CO, nitrite oxidation, and methane branches in the first revision unless direct full-text mechanistic evidence is added.** The current evidence set does not support these branches at the same depth as ammonia, H2, sulfur, and Fe2+.

## 8. DOI-first bibliography

1. Laufer-Meiser K. et al. **Oxidation of sulfur, hydrogen, and iron by metabolically versatile Hydrogenovibrio from deep sea hydrothermal vents.** *ISME Journal*. Published 14 September 2024. DOI: [10.1093/ismejo/wrae173](https://doi.org/10.1093/ismejo/wrae173). (laufermeiser2024oxidationofsulfur pages 4-6, laufermeiser2024oxidationofsulfur pages 1-2)
2. Wang Q. et al. **Characterize the Growth and Metabolism of Acidithiobacillus ferrooxidans under Electroautotrophic and Chemoautotrophic Conditions.** *Microorganisms*. Published March 2024. DOI: [10.3390/microorganisms12030590](https://doi.org/10.3390/microorganisms12030590). (wang2024characterizethegrowth pages 22-23)
3. Tonietti L. et al. **Unveiling the Bioleaching Versatility of Acidithiobacillus ferrooxidans.** *Microorganisms*. Published 23 November 2024. DOI: [10.3390/microorganisms12122407](https://doi.org/10.3390/microorganisms12122407). (tonietti2024unveilingthebioleaching pages 1-2)
4. Cozma P. et al. **Bio-Recovery of Metals through Biomining within Circularity-Based Solutions.** *Processes*. Published 23 August 2024. DOI: [10.3390/pr12091793](https://doi.org/10.3390/pr12091793). (cozma2024biorecoveryofmetals pages 1-2)
5. Bayer B. et al. **Contribution of ammonia oxidizers to inorganic carbon fixation in the dark ocean.** *bioRxiv* preprint. Posted November 2024. DOI: [10.1101/2024.11.16.623942](https://doi.org/10.1101/2024.11.16.623942). (bayer2024contributionofammonia pages 1-4)
6. Wright C.L., Lehtovirta-Morley L.E. **Nitrification and beyond: metabolic versatility of ammonia oxidising archaea.** *ISME Journal*. Published 14 July 2023. DOI: [10.1038/s41396-023-01467-0](https://doi.org/10.1038/s41396-023-01467-0). (wright2023nitrificationandbeyond pages 1-2, wright2023nitrificationandbeyond pages 3-5)
7. Srivastava A. et al. **Interplay between autotrophic and heterotrophic prokaryotic metabolism in the bathypelagic realm revealed by metatranscriptomic analyses.** *Microbiome*. Published 2023. DOI: [10.1186/s40168-023-01688-7](https://doi.org/10.1186/s40168-023-01688-7). (srivastava2023interplaybetweenautotrophic pages 1-2, srivastava2023interplaybetweenautotrophic pages 5-7)
8. Taubert M. et al. **Bolstering fitness via CO2 fixation and organic carbon uptake: mixotrophs in modern groundwater.** *ISME Journal*. Online 7 December 2021; volume year 2022. DOI: [10.1038/s41396-021-01163-x](https://doi.org/10.1038/s41396-021-01163-x). (taubert2022bolsteringfitnessvia pages 1-2)
9. Asplund-Samuelsson J., Hudson E.P. **Wide range of metabolic adaptations to the acquisition of the Calvin cycle revealed by comparison of microbial genomes.** *PLOS Computational Biology*. Published 8 February 2021. DOI: [10.1371/journal.pcbi.1008742](https://doi.org/10.1371/journal.pcbi.1008742). (asplundsamuelsson2021widerangeof pages 1-2)
10. Kucera J. et al. **A Model of Aerobic and Anaerobic Metabolism of Hydrogen in the Extremophile Acidithiobacillus ferrooxidans.** *Frontiers in Microbiology*. Published 30 November 2020. DOI: [10.3389/fmicb.2020.610836](https://doi.org/10.3389/fmicb.2020.610836). (kucera2020amodelof pages 1-2, kucera2020amodelof pages 4-8, kucera2020amodelof media efa0d4aa)
11. Claassens N.J. et al. **Phosphoglycolate salvage in a chemolithoautotroph using the Calvin cycle.** *PNAS*. Published 2020. DOI: [10.1073/pnas.2012288117](https://doi.org/10.1073/pnas.2012288117). (claassens2020phosphoglycolatesalvagein pages 1-2)
12. Callbeck C.M. et al. **Arcobacter peruensis sp. nov., a Chemolithoheterotroph Isolated from Sulfide- and Organic-Rich Coastal Waters off Peru.** *Applied and Environmental Microbiology*. Published 27 November 2019. DOI: [10.1128/AEM.01344-19](https://doi.org/10.1128/AEM.01344-19). (callbeck2019arcobacterperuensissp. pages 1-2)
13. Zeldes B.M. et al. **Determinants of Sulfur Chemolithoautotrophy in the Extremely Thermoacidophilic Sulfolobales.** *Environmental Microbiology*. Published October 2019. DOI: [10.1111/1462-2920.14712](https://doi.org/10.1111/1462-2920.14712). (zeldes2019determinantsofsulfur pages 1-5)
14. Esparza M. et al. **Genes and pathways for CO2 fixation in the obligate, chemolithoautotrophic acidophile Acidithiobacillus ferrooxidans.** *BMC Microbiology*. Published August 2010. DOI: [10.1186/1471-2180-10-229](https://doi.org/10.1186/1471-2180-10-229). (esparza2010genesandpathways pages 1-2)

References

1. (laufermeiser2024oxidationofsulfur pages 1-2): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 9 citations.

2. (bayer2024contributionofammonia pages 1-4): Barbara Bayer, Katharina Kitzinger, Nicola L. Paul, Justine B. Albers, Mak A. Saito, Michael Wagner, Craig A. Carlson, and Alyson E. Santoro. Contribution of ammonia oxidizers to inorganic carbon fixation in the dark ocean. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.16.623942, doi:10.1101/2024.11.16.623942. This article has 1 citations.

3. (callbeck2019arcobacterperuensissp. pages 1-2): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 61 citations and is from a peer-reviewed journal.

4. (taubert2022bolsteringfitnessvia pages 1-2): Martin Taubert, Will A Overholt, Beatrix M Heinze, Georgette Azemtsop Matanfack, Rola Houhou, Nico Jehmlich, Martin von Bergen, Petra Rösch, Jürgen Popp, and Kirsten Küsel. Bolstering fitness via co2 fixation and organic carbon uptake: mixotrophs in modern groundwater. The ISME Journal, 16:1153-1162, Dec 2022. URL: https://doi.org/10.1038/s41396-021-01163-x, doi:10.1038/s41396-021-01163-x. This article has 69 citations.

5. (wang2024characterizethegrowth pages 22-23): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 11 citations.

6. (wright2023nitrificationandbeyond pages 1-2): Chloe L Wright and Laura E Lehtovirta-Morley. Nitrification and beyond: metabolic versatility of ammonia oxidising archaea. The ISME Journal, 17:1358-1368, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01467-0, doi:10.1038/s41396-023-01467-0. This article has 157 citations.

7. (kucera2020amodelof pages 1-2): Jiri Kucera, Jan Lochman, Pavel Bouchal, Eva Pakostova, Kamil Mikulasek, Sabrina Hedrich, Oldrich Janiczek, Martin Mandl, and D. Barrie Johnson. A model of aerobic and anaerobic metabolism of hydrogen in the extremophile acidithiobacillus ferrooxidans. Frontiers in Microbiology, Nov 2020. URL: https://doi.org/10.3389/fmicb.2020.610836, doi:10.3389/fmicb.2020.610836. This article has 51 citations and is from a peer-reviewed journal.

8. (kucera2020amodelof pages 4-8): Jiri Kucera, Jan Lochman, Pavel Bouchal, Eva Pakostova, Kamil Mikulasek, Sabrina Hedrich, Oldrich Janiczek, Martin Mandl, and D. Barrie Johnson. A model of aerobic and anaerobic metabolism of hydrogen in the extremophile acidithiobacillus ferrooxidans. Frontiers in Microbiology, Nov 2020. URL: https://doi.org/10.3389/fmicb.2020.610836, doi:10.3389/fmicb.2020.610836. This article has 51 citations and is from a peer-reviewed journal.

9. (wright2023nitrificationandbeyond pages 3-5): Chloe L Wright and Laura E Lehtovirta-Morley. Nitrification and beyond: metabolic versatility of ammonia oxidising archaea. The ISME Journal, 17:1358-1368, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01467-0, doi:10.1038/s41396-023-01467-0. This article has 157 citations.

10. (laufermeiser2024oxidationofsulfur pages 4-6): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 9 citations.

11. (zeldes2019determinantsofsulfur pages 1-5): Benjamin M. Zeldes, Andrew J. Loder, James A. Counts, Mashkurul Haque, Karl A. Widney, Lisa M. Keller, Sonja‐Verena Albers, and Robert M. Kelly. Determinants of sulfur chemolithoautotrophy in the extremely thermoacidophilic sulfolobales. Environmental microbiology, 21:3696-3710, Oct 2019. URL: https://doi.org/10.1111/1462-2920.14712, doi:10.1111/1462-2920.14712. This article has 30 citations and is from a domain leading peer-reviewed journal.

12. (srivastava2023interplaybetweenautotrophic pages 5-7): Abhishek Srivastava, Daniele De Corte, Juan A. L. Garcia, Brandon K. Swan, Ramunas Stepanauskas, Gerhard J. Herndl, and Eva Sintes. Interplay between autotrophic and heterotrophic prokaryotic metabolism in the bathypelagic realm revealed by metatranscriptomic analyses. Microbiome, Nov 2023. URL: https://doi.org/10.1186/s40168-023-01688-7, doi:10.1186/s40168-023-01688-7. This article has 10 citations and is from a highest quality peer-reviewed journal.

13. (asplundsamuelsson2021widerangeof pages 1-2): Johannes Asplund-Samuelsson and Elton P. Hudson. Wide range of metabolic adaptations to the acquisition of the calvin cycle revealed by comparison of microbial genomes. PLOS Computational Biology, 17:e1008742, Feb 2021. URL: https://doi.org/10.1371/journal.pcbi.1008742, doi:10.1371/journal.pcbi.1008742. This article has 40 citations and is from a highest quality peer-reviewed journal.

14. (esparza2010genesandpathways pages 1-2): Mario Esparza, Juan Pablo Cárdenas, Botho Bowien, Eugenia Jedlicki, and David S Holmes. Genes and pathways for co2 fixation in the obligate, chemolithoautotrophic acidophile, acidithiobacillus ferrooxidans, carbon fixation in a. ferrooxidans. BMC Microbiology, 10:229-229, Aug 2010. URL: https://doi.org/10.1186/1471-2180-10-229, doi:10.1186/1471-2180-10-229. This article has 111 citations and is from a peer-reviewed journal.

15. (claassens2020phosphoglycolatesalvagein pages 1-2): Nico J. Claassens, Giovanni Scarinci, Axel Fischer, Avi I. Flamholz, William Newell, Stefan Frielingsdorf, Oliver Lenz, and Arren Bar-Even. Phosphoglycolate salvage in a chemolithoautotroph using the calvin cycle. Proceedings of the National Academy of Sciences of the United States of America, 117:22452-22461, Aug 2020. URL: https://doi.org/10.1073/pnas.2012288117, doi:10.1073/pnas.2012288117. This article has 68 citations and is from a highest quality peer-reviewed journal.

16. (srivastava2023interplaybetweenautotrophic pages 1-2): Abhishek Srivastava, Daniele De Corte, Juan A. L. Garcia, Brandon K. Swan, Ramunas Stepanauskas, Gerhard J. Herndl, and Eva Sintes. Interplay between autotrophic and heterotrophic prokaryotic metabolism in the bathypelagic realm revealed by metatranscriptomic analyses. Microbiome, Nov 2023. URL: https://doi.org/10.1186/s40168-023-01688-7, doi:10.1186/s40168-023-01688-7. This article has 10 citations and is from a highest quality peer-reviewed journal.

17. (tonietti2024unveilingthebioleaching pages 1-2): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 57 citations.

18. (kucera2020amodelof media efa0d4aa): Jiri Kucera, Jan Lochman, Pavel Bouchal, Eva Pakostova, Kamil Mikulasek, Sabrina Hedrich, Oldrich Janiczek, Martin Mandl, and D. Barrie Johnson. A model of aerobic and anaerobic metabolism of hydrogen in the extremophile acidithiobacillus ferrooxidans. Frontiers in Microbiology, Nov 2020. URL: https://doi.org/10.3389/fmicb.2020.610836, doi:10.3389/fmicb.2020.610836. This article has 51 citations and is from a peer-reviewed journal.

19. (cozma2024biorecoveryofmetals pages 1-2): Petronela Cozma, Camelia Bețianu, Raluca-Maria Hlihor, Isabela Maria Simion, and Maria Gavrilescu. Bio-recovery of metals through biomining within circularity-based solutions. Processes, 12:1793, Aug 2024. URL: https://doi.org/10.3390/pr12091793, doi:10.3390/pr12091793. This article has 37 citations.