---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:49:25.071003'
end_time: '2026-08-04T08:58:06.859786'
duration_seconds: 521.79
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: intracellular inclusion
  trait_identifier: traitmech:000066
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: intracellular_inclusion
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A morphology trait describing a discrete intracellular body \u2014\
    \ a storage granule, gas-filled structure, or protein-bounded microcompartment/organelle\
    \ \u2014 that compartmentalizes material or function within a prokaryotic cell."
  parent_traits: METPO:1000059
  synonyms: cytoplasmic inclusion
  evidence_summary: 'DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow, "Formation
    and function of bacterial organelles", establish that bacteria contain diverse
    inclusions/organelles (storage granules, gas vesicles, microcompartments, magnetosomes);
    parent of the inclusion sub-variants.) | DOI:10.1038/nrmicro.2018.10:  (Kerfeld
    et al. review bacterial microcompartments as a major class of protein-bounded
    intracellular organelles.)'
  causal_graph_summary: 'inclusion_compartmentalization: 14 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** intracellular inclusion
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000066
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait describing a discrete intracellular body — a storage granule, gas-filled structure, or protein-bounded microcompartment/organelle — that compartmentalizes material or function within a prokaryotic cell.
- **Parent traits:** METPO:1000059
- **Synonyms:** cytoplasmic inclusion
- **Existing evidence:** DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow, "Formation and function of bacterial organelles", establish that bacteria contain diverse inclusions/organelles (storage granules, gas vesicles, microcompartments, magnetosomes); parent of the inclusion sub-variants.) | DOI:10.1038/nrmicro.2018.10:  (Kerfeld et al. review bacterial microcompartments as a major class of protein-bounded intracellular organelles.)
- **Existing causal graph summary:** inclusion_compartmentalization: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **intracellular inclusion** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/intracellular_inclusion.yaml`.

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
- **Trait label:** intracellular inclusion
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000066
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait describing a discrete intracellular body — a storage granule, gas-filled structure, or protein-bounded microcompartment/organelle — that compartmentalizes material or function within a prokaryotic cell.
- **Parent traits:** METPO:1000059
- **Synonyms:** cytoplasmic inclusion
- **Existing evidence:** DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow, "Formation and function of bacterial organelles", establish that bacteria contain diverse inclusions/organelles (storage granules, gas vesicles, microcompartments, magnetosomes); parent of the inclusion sub-variants.) | DOI:10.1038/nrmicro.2018.10:  (Kerfeld et al. review bacterial microcompartments as a major class of protein-bounded intracellular organelles.)
- **Existing causal graph summary:** inclusion_compartmentalization: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **intracellular inclusion** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/intracellular_inclusion.yaml`.

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


# Curation-focused research report: intracellular inclusion

## Record and scope summary

- **Trait:** intracellular inclusion
- **Identifier:** **`traitmech:000066`**
- **Category / kind / status:** MORPHOLOGY / CLASS / REVIEWED
- **Parent:** `METPO:1000059`
- **Synonym:** cytoplasmic inclusion

This trait should denote an **observable, discrete body inside a prokaryotic cell that spatially concentrates material or function**. The class appropriately includes: (i) reserve inclusions such as PHA/PHB, glycogen, and polyphosphate granules; (ii) gas-filled gas vesicles; (iii) protein-shell compartments such as carboxysomes, metabolosomes, and encapsulins; and (iv) specialized membrane-bounded bodies such as magnetosomes and ferrosomes. Bacterial organelles can be bounded by lipid bilayers, protein–lipid monolayers, or proteinaceous shells, and are often species-specific and conditionally produced rather than constitutive. Their boundaries can improve reaction efficiency or protect the cytoplasm from harmful intermediates. (ferrara2024bacterialorganellesin pages 1-2)

The trait is therefore a **broad morphological parent**, not a single conserved pathway. A positive assay may be microscopy-based—phase contrast, fluorescence, TEM/cryo-ET, Raman staining, Nile-red-type lipid staining, magnetic imaging—or inferred from an inclusion-specific phenotype, but gene presence alone should not establish the morphology.

### Boundary cases

**Include** a structure when it is intracellular, spatially discrete, and contains stored material, gas, mineral, or compartmentalized biochemical machinery. A delimiting lipid membrane is not required: PHB granules have a hydrophobic polymer core with surface proteins, gas vesicles have an amphipathic protein shell, and BMCs have tiled protein shells. (rose2023innateandengineered pages 1-2, mullersantos2021theprotectiverole pages 5-6, iburg2024elucidatingtheassembly pages 1-2)

**Exclude or model separately:**

1. Diffuse cytosolic metabolite accumulation without a discrete body.
2. Ordinary soluble enzyme complexes, ribosomes, nucleoids, and cytoskeletal filaments unless they delimit or organize an inclusion.
3. Extracellular precipitates, extracellular polymer, spores, and extracellular vesicles.
4. Generic membrane invaginations lacking demonstrated compartmentalized content or function.
5. Inclusion bodies composed of misfolded recombinant protein, unless TraitMech intentionally includes pathological/engineered protein aggregates.
6. Host-cell inclusions containing intracellular pathogens; these are eukaryotic host compartments, not microbial-cell morphology.
7. Mere capacity inferred from a biosynthetic locus. Many bacterial organelles are induced only under relevant environmental conditions—for example substrate availability, oxygen depletion, sulfur conditions, or iron transitions. (ferrara2024bacterialorganellesin pages 1-2)

## Recommended graph architecture

Because no single gene causes every form of intracellular inclusion, the existing generic `inclusion_compartmentalization` graph should remain a small parent-level graph. Mechanistic detail should be placed in subtype graphs such as **PHA granule**, **gas vesicle**, **carboxysome/BMC**, **magnetosome**, **ferrosome**, **polyphosphate granule**, and **glycogen granule**, connected to `traitmech:000066` by subtype relations.

| subtype | strongest mechanistic nodes | strongest directly supported causal relation | evidence class | recommended curation status |
|---|---|---|---|---|
| BMC/carboxysome | BMC shell proteins; Rubisco; carbonic anhydrase; cargo-encapsulation factors/scaffolds | Protein shell compartmentalizes Rubisco and carbonic anhydrase, creating a favorable microenvironment that enhances carbon fixation; broader claims about selective permeability and assembly determinants are partly simulation- or review-supported (trettel2024modelingbacterialmicrocompartment pages 1-2, rose2023innateandengineered pages 1-2, sarkar2024atomicviewof pages 7-8) | Mixed: review + primary structural/engineering studies; some 2024 simulation/preprint evidence | Curate parent-level compartmentalization edge now; defer detailed pore-selectivity and generalized assembly edges unless tied to specific child traits or primary studies |
| gas vesicle | GvpA; GvpC; GvpN; GvpO; accessory GvpF-L proteins | GvpA forms shell ribs, GvpC stabilizes the exterior surface, and deletion of gvpC reduces strength/changes shape while deletion of gvpN yields only tiny vesicles; several assembly-factor roles remain interaction-based or hypothesized (jost2022interactionofthe pages 1-2, jost2022interactionofthe pages 2-3, jost2022interactionofthe pages 14-15, iburg2024elucidatingtheassembly pages 1-2) | Primary interaction/deletion studies plus some hypothesis | High-priority curation for gas-vesicle child trait; use cautious parent-level links only for inclusion formation/stabilization |
| PHB/PHA granule | PhaC; PhaM; PhaP/phasins; PhaZa depolymerase | PhaM activates PHB synthase and controls granule biogenesis properties including number, localization, and daughter-cell distribution; major phasins regulate granule surface properties and morphology (mullersantos2021theprotectiverole pages 35-36, mullersantos2021theprotectiverole pages 5-6, mullersantos2021theprotectiverole pages 40-41) | Review synthesis grounded in multiple primary studies; some direct overexpression evidence for stress protection (mullersantos2021theprotectiverole pages 9-10) | Curate as strong candidate child-trait mechanism; avoid overgeneralizing stress-protection edges to all intracellular inclusions |
| magnetosome | Magnetosome island; MamAB operon; MamA; MamB; MamM; core mam genes | Magnetosome islands encode >30 MAPs in some taxa, with the mamAB operon essential for magnetosome membrane formation; only a conserved core is universal across magnetotactic bacteria (ferrara2024bacterialorganellesin pages 2-4) | Recent authoritative review summarizing primary genetics | Curate cautiously at child-trait level; do not assign Mam-gene edges to the generic inclusion parent |
| ferrosome | Ferrosome gene cluster; membrane proteins; iron phosphate cargo | Ferrosomes form during iron-deficiency-to-sufficiency transitions and serve as iron-storage organelles under anaerobic conditions, but remobilization and many formation details remain unclear (ferrara2024bacterialorganellesin pages 12-14, ferrara2024bacterialorganellesin pages 1-2) | Recent review, limited mechanistic resolution | Medium priority; retain only broad environment-to-organelle/storage edges until stronger primary mechanistic evidence is assembled |
| polyphosphate/glycogen granules | Polyphosphate: PPK/polyP, acidocalcisome-like storage; Glycogen: GlgC, GlgA, GlgB | Polyphosphate is mainly stored as granules in acidocalcisomes, but precise synthesis/biogenesis mechanisms remain incompletely resolved; glycogen granule synthesis follows the GlgC-GlgA pathway with branching by GlgB, yet this is a polymer-metabolism mechanism more than a general inclusion-formation rule (mullersantos2021theprotectiverole pages 33-34, mullersantos2021theprotectiverole pages 5-6) | Mostly review-level for polyP here; glycogen evidence only indirectly retrieved | Low-to-medium priority for the parent trait; better curated as specific storage-granule child traits after stronger primary evidence collection |


*Table: This table prioritizes major intracellular-inclusion subtypes for curation of traitmech:000066, summarizing the strongest mechanistic nodes, the most directly supported causal relation, and whether evidence is primary, review-based, or simulation-supported. It is designed to help decide which subtype-level mechanisms are ready for conservative TraitMech graph inclusion.*

## Candidate nodes grouped by type

### Trait and compartment nodes

| Candidate node | Grounding | Curation note |
|---|---|---|
| intracellular inclusion | `traitmech:000066` | Target morphology class; quote identifier verbatim in YAML. |
| bacterial microcompartment | `GO:0042579` | High-confidence general BMC compartment grounding. |
| carboxysome | `GO:0031470` | Photosynthetic/autotrophic BMC child. |
| gas vesicle | `GO:0031411` | Gas-filled, protein-shell organelle. |
| magnetosome | `GO:0042599` | Use for the membrane-bounded magnetic-mineral organelle. |
| polyhydroxyalkanoate granule / PHB granule | label-only pending ontology verification | Avoid assigning an unverified CURIE. |
| polyphosphate granule / acidocalcisome-like organelle | label-only pending organism-specific review | “Acidocalcisome” and unbounded polyP granule should not automatically be treated as synonyms. |
| glycogen granule | label-only | Morphological particle; distinguish it from glycogen metabolism. |
| ferrosome | label-only | Membrane-bounded iron-phosphate storage organelle. |
| encapsulin compartment | label-only | Protein nanocompartment containing ferritin-like or enzymatic cargo. |

### Genes, proteins, and complexes

- **BMC/carboxysome:** BMC-H shell proteins, BMC-T trimers, BMC-P vertex pentamers, Rubisco, carbonic anhydrase, CsoS2, CcmM, CcmN, and cargo encapsulation peptides. The strongest generic assertion is that shell proteins self-assemble into a semipermeable envelope around an enzymatic core; detailed components differ between α-carboxysomes, β-carboxysomes, and metabolosomes. (trettel2024modelingbacterialmicrocompartment pages 1-2, trettel2024modelingbacterialmicrocompartment pages 12-12, rose2023innateandengineered pages 1-2)
- **Gas vesicle:** GvpA, GvpC, GvpF, GvpG, GvpH, GvpI, GvpJ, GvpK, GvpL, GvpM, GvpN, and GvpO. In *Halobacterium salinarum*, GvpA/F/G/J/K/L/M/O are reported as essential; GvpC stabilizes the shell and GvpN is required for normal-sized vesicles. Essential sets vary among operons and taxa. (jost2022interactionofthe pages 2-3)
- **Magnetosome:** magnetosome-island genes and Mam proteins, especially the mamAB operon and conserved core MamA/B/E/K/M/O/P/Q/I proteins. *Magnetospirillum gryphiswaldense* MSR-1 has more than 30 magnetosome-associated proteins across five polycistronic operons; the 16–17-kb mamAB operon is essential for magnetosome membrane formation. (ferrara2024bacterialorganellesin pages 2-4)
- **PHA/PHB granule:** PhaC/PhaC1 synthase, PhaM activator/nucleoid tether, PhaP phasins, and PhaZ/PhaZa1 depolymerase. In *Cupriavidus necator*/*Ralstonia eutropha*, seven PhaP phasins have been identified; PhaP1 controls granule surface-to-volume properties. (mullersantos2021theprotectiverole pages 40-41, mullersantos2021theprotectiverole pages 5-6)
- **Polyphosphate granule:** polyphosphate kinase PPK, exopolyphosphatase PPX, polyP, and metal cations. Specific PPK family member and compartment identity must be resolved per taxon.
- **Glycogen granule:** GlgC, GlgA, and GlgB are candidate synthesis nodes; GlgP/GlgX/MalQ belong to mobilization rather than inclusion formation. These should be curated only from glycogen-particle-specific primary evidence.
- **Ferrosome:** ferrosome gene cluster and its encoded membrane proteins; exact gene names differ among taxa. Current synthesis supports only a cluster-level node for the parent report. (ferrara2024bacterialorganellesin pages 12-14)

### Chemicals and metabolic cargo

| Chemical/cargo | Suggested grounding | Role |
|---|---|---|
| carbon dioxide | `CHEBI:16526` | Rubisco substrate and carboxysome cargo flux. |
| hydrogencarbonate/bicarbonate | `CHEBI:17544` | Imported inorganic-carbon species converted to CO₂ by carbonic anhydrase. |
| oxygen | `CHEBI:15379` | Competes with CO₂ at Rubisco; also an environmental regulator for some organelles. |
| acetyl-CoA | `CHEBI:15351` | Central precursor for PHB synthesis. |
| poly(3-hydroxybutyrate) | label-only unless exact ChEBI mapping is verified | Hydrophobic carbon/energy-storage core. |
| 3-hydroxybutyrate | `CHEBI:37054` | PHB mobilization product implicated in stress protection. |
| polyphosphate | `CHEBI:16838` | Phosphate/energy and cation-storage polymer. |
| glycogen | `CHEBI:28087` | Branched glucose-storage polymer. |
| magnetite | `CHEBI:46726` | Common magnetosome magnetic mineral. |
| greigite | label-only pending verified identifier | Alternative magnetosome mineral. |
| iron phosphate / amorphous iron phosphate | label-only | Ferrosome cargo. |

### Environmental and experimental factors

- Carbon excess with limitation of another essential nutrient promotes PHB accumulation; starvation or stress promotes mobilization. PHB is generally described as a mobilizable carbon reserve, and stress-associated products protect against reactive oxygen species and heat damage. (mullersantos2021theprotectiverole pages 9-10, mullersantos2021theprotectiverole pages 40-41)
- Availability of a cognate catabolic substrate can induce metabolosome formation; oxygen depletion or sulfur-rich conditions can induce magnetosome production; ferrosomes occur across iron-deficiency-to-sufficiency transitions. These are subtype- and taxon-specific, not universal parent-trait triggers. (ferrara2024bacterialorganellesin pages 12-14, ferrara2024bacterialorganellesin pages 1-2)
- Experimental factors worth representing include gene deletion, inducible operon expression, heterologous reconstitution, nutrient limitation, iron shift, hydrostatic-pressure collapse, and microscopy/staining assay.

## Candidate evidence-backed edges

Predicates below are deliberately plain-language candidates. TraitMech should map them to its controlled predicate vocabulary.

| # | Subject — predicate — object | Reference and supporting snippet | Curation notes |
|---:|---|---|---|
| 1 | BMC shell proteins — **self-assemble to form** — bacterial microcompartment shell | Rose et al. 2023: shell subunits with BMC domains “tile together to form a semipermeable envelope.” DOI [10.1039/D3TB00098B](https://doi.org/10.1039/D3TB00098B), published May 2023. (rose2023innateandengineered pages 1-2) | Strong parent-level BMC edge; review evidence. |
| 2 | BMC shell — **compartmentalizes** — enzymatic cargo | BMCs are described as an “enzymatic core enclosed in a protein shell” that confines metabolic reactions and sequesters toxic intermediates. (rose2023innateandengineered pages 1-2) | Curate for BMC child; it supports the broader inclusion concept but not every inclusion. |
| 3 | carboxysome shell — **compartmentalizes** — Rubisco and carbonic anhydrase | Trettel et al. 2024: the shell “compartmentalizes Rubisco and carbonic anhydrase to enhance CO2 fixation.” DOI [10.3389/fpls.2024.1346759](https://doi.org/10.3389/fpls.2024.1346759), published February 2024. (trettel2024modelingbacterialmicrocompartment pages 1-2) | Strong mechanistic synthesis; subtype-specific. |
| 4 | cargo interactions — **influence kinetics of** — BMC assembly | 2024 modeling review: “assembly kinetics are dictated by cargo interactions.” (trettel2024modelingbacterialmicrocompartment pages 1-2) | **Uncertain/model-derived.** Do not curate as a universal causal fact without primary experimental support. |
| 5 | shell factors — **determine** — final BMC morphology | Same review states that “final morphology depends on shell factors.” (trettel2024modelingbacterialmicrocompartment pages 1-2) | Useful candidate edge, but broad and based substantially on modeling; curate only with a defined shell protein and primary perturbation. |
| 6 | GvpA — **forms structural ribs of** — gas vesicle shell | Jost & Pfeifer 2022: “GvpA forms the shell ribs.” DOI [10.3389/fmicb.2022.971917](https://doi.org/10.3389/fmicb.2022.971917), published July 2022. (jost2022interactionofthe pages 1-2) | Direct structural edge; taxon context should accompany the evidence. |
| 7 | GvpC — **stabilizes exterior of** — gas vesicle | “GvpC attaches to the exterior surface for stabilization”; removing it produced deformation and an approximately threefold reduction in collapse pressure. (jost2022interactionofthe pages 1-2) | Strong deletion/physical-phenotype edge. |
| 8 | deletion of gvpN — **causes** — tiny gas vesicles | The ΔgvpN strain “produces only tiny vesicles despite normal GvpA/GvpC production.” (jost2022interactionofthe pages 2-3) | Strong phenotype edge in *H. salinarum*; do not generalize unqualified to all taxa. |
| 9 | GvpN — **interacts with** — GvpO | Split-GFP/pulldown work detected GvpN/GvpO heterodimers, as well as homodimers. (jost2022interactionofthe pages 1-2) | Direct molecular interaction, not proof that the interaction powers assembly. |
| 10 | GvpN and GvpO — **interact with** — GvpC C-terminal domain | Both proteins interacted with the C-terminal domain of GvpC. (jost2022interactionofthe pages 1-2) | Direct assay-supported interaction. |
| 11 | GvpN — **hydrolyzes ATP to power** — shell-subunit incorporation | GvpN is an ATPase “hypothesized to power subunit turnover and GvpA incorporation.” (jost2022interactionofthe pages 14-15) | **Do not curate as established causality**; explicitly hypothetical. |
| 12 | gas vesicle formation — **enables** — buoyancy/vertical positioning | Gas vesicles “provide buoyancy for microbial positioning in aqueous environments.” (jost2022interactionofthe pages 1-2) | Functional edge; phenotype should be separated from structural formation. |
| 13 | mamAB operon — **is required for** — magnetosome membrane formation | Ferrara et al. 2024 identify the mamAB operon as essential for membrane formation. DOI [10.1111/mmi.15330](https://doi.org/10.1111/mmi.15330), published November 2024. (ferrara2024bacterialorganellesin pages 2-4) | Strong review synthesis; ideally attach the cited primary deletion study before YAML inclusion. |
| 14 | magnetosome-associated proteins — **coordinate** — magnetite crystal composition, size, shape, and arrangement | More than 30 MAPs in MSR-1 act in a highly regulated process producing defined crystal properties and intracellular organization. (ferrara2024bacterialorganellesin pages 2-4) | Too collective for a precise mechanistic edge; decompose by Mam protein in a magnetosome child graph. |
| 15 | oxygen depletion or sulfur-rich conditions — **promote** — magnetosome formation | Ferrara et al. note that magnetosomes can form under oxygen-depletion or sulfur-rich conditions. (ferrara2024bacterialorganellesin pages 1-2) | **Taxon- and mineral-specific.** Environmental edge needs organism and medium context. |
| 16 | iron-deficiency-to-sufficiency transition — **induces** — ferrosome formation | Ferrosomes are conditionally produced during iron transitions and store amorphous iron phosphate. (ferrara2024bacterialorganellesin pages 12-14, ferrara2024bacterialorganellesin pages 1-2) | Candidate broad edge; obtain the underlying primary study before curation. |
| 17 | ferrosome — **stores** — amorphous iron phosphate | Ferrosomes are described as iron reservoirs under anaerobic conditions. (ferrara2024bacterialorganellesin pages 12-14) | Storage relation is well supported at review level; remobilization mechanism remains unknown. |
| 18 | PhaM — **activates** — PhaC1/PHB synthase | PhaM is identified as the “physiological activator of PHB synthase (PhaC1).” DOI [10.1093/femsre/fuaa058](https://doi.org/10.1093/femsre/fuaa058), published October 2021. (mullersantos2021theprotectiverole pages 35-36) | Strong *C. necator/R. eutropha* subtype edge. |
| 19 | PhaM — **regulates** — PHB-granule number, localization, and partitioning | PhaM controls “number, surface-to-volume ratio, subcellular localization, and distribution to daughter cells.” (mullersantos2021theprotectiverole pages 35-36) | Strong morphology edge, but organism-specific. |
| 20 | PhaP1 phasin — **controls** — PHB-granule surface-to-volume ratio | The major phasin mediates the interface between hydrophobic core and hydrophilic cytoplasm and controls surface-to-volume ratio. (mullersantos2021theprotectiverole pages 5-6) | Good child-trait edge. Do not generalize PhaP1 orthology across all PHA producers. |
| 21 | PhaZa1 depolymerase — **mobilizes** — accumulated PHB | PhaZa1 is described as mobilizing accumulated PHB in *R. eutropha* H16. (mullersantos2021theprotectiverole pages 40-41) | This is inclusion turnover, not formation; retain if the graph models loss/remobilization. |
| 22 | phaP overexpression — **increases** — PHB production and stress resistance | Heterologous phaP expression in *E. coli* enhanced PHB production from glycerol and resistance to heat and paraquat. (mullersantos2021theprotectiverole pages 9-10) | **Engineered and assay-specific.** Do not represent as a universal natural mechanism. |
| 23 | PHB mobilization products — **protect against** — ROS/heat-associated damage | The review reports protective effects of 3-hydroxybutyrate and oligomers against protein aggregation, ROS damage, and heat shock. (mullersantos2021theprotectiverole pages 9-10, mullersantos2021theprotectiverole pages 33-34) | Functionally plausible but downstream of granule morphology; child graph only. |
| 24 | polyphosphate synthesis/accumulation — **produces** — intracellular polyP granules | PolyP is “mainly stored as granules in specific vacuoles called acidocalcisomes.” (mullersantos2021theprotectiverole pages 33-34) | Review-level and focused on photosynthetic microbes; resolve whether the studied prokaryote has a membrane-bound acidocalcisome or an unbounded granule. |

## Recent developments, quantitative evidence, and applications

### 2023–2024 research

1. **BMC diversity and engineering.** A 2023 synthesis reports approximately **7,000 BMC loci across 45 bacterial phyla**, grouped into **68 types/subtypes**, emphasizing that intracellular inclusion formation has repeatedly specialized around different metabolic cargos. BMCs are now engineered as synthetic nanoreactors, catalytic scaffolds, and nucleic-acid or drug-delivery vehicles. (rose2023innateandengineered pages 1-2)
2. **Programmable carboxysome cages.** Li et al. engineered α-carboxysome shells using SpyTag/SpyCatcher and coiled-coil coupling systems, demonstrating programmable cargo-docking sites and capacities. This is a real engineered implementation of inclusion-based cargo loading, but not evidence for a native parent-trait mechanism. DOI [10.1021/acsnano.3c11559](https://doi.org/10.1021/acsnano.3c11559), published February 2024. (li2024nanoengineeringcarboxysomeshells pages 11-12)
3. **Carboxysome modeling.** Trettel et al. integrated shell-pore transport and assembly models for carbon-capture and biomanufacturing design. The work supports testable mechanisms but is a review of computational and experimental studies, not itself a universal causal demonstration. (trettel2024modelingbacterialmicrocompartment pages 1-2)
4. **Atomic permeability estimates.** A 2024 ChemRxiv preprint modeled a 95-nm crowded carboxysome containing 160 Rubisco copies and reported transport simulations with 1,000 CO₂ particles. Its synthetic shell lacked CcmO, encapsulation peptides, and native enzymes, so its predicted permeability must not be curated as native biology. (sarkar2024atomicviewof pages 7-8)
5. **Gas-vesicle interaction mapping.** Iburg et al. 2024 characterized an 11-protein gas-vesicle operon using systematic interaction and deletion analysis. Gas-vesicle shells are approximately **3 nm thick**, can tolerate multiple atmospheres and megapascal-scale surface tension, and may remain stable for months; some engineered vesicles have diameters below **100 nm**. DOI [10.1038/s44318-024-00178-2](https://doi.org/10.1038/s44318-024-00178-2), published September 2024. (iburg2024elucidatingtheassembly pages 1-2)
6. **Iron organelles.** Ferrara et al. 2024 synthesize current knowledge of magnetosomes, ferrosomes, and encapsulated ferritin-like proteins. Magnetosome islands span roughly **80–100 kb**; only nine core genes, `mamABEKMOPQI`, are reported conserved across all magnetotactic bacteria. The review stresses unresolved iron-remobilization and environmental-regulation mechanisms. (ferrara2024bacterialorganellesin pages 2-4, ferrara2024bacterialorganellesin pages 12-14)

### Current and emerging implementations

- **Carbon capture and biomanufacturing:** carboxysome transplantation or redesign seeks to improve CO₂ fixation and create enclosed catalytic modules. This remains largely synthetic-biology research rather than routine industrial deployment. (trettel2024modelingbacterialmicrocompartment pages 1-2)
- **Nanocatalysis and delivery:** engineered BMC/carboxysome shells provide selectively loadable protein cages for catalysis, molecular delivery, and prospective medicine. (li2024nanoengineeringcarboxysomeshells pages 11-12, rose2023innateandengineered pages 1-2)
- **Imaging and therapeutics:** gas vesicles are genetically encoded contrast agents under development for ultrasound, MRI, and optical imaging. GvpC can be modified with foreign peptides for surface display. (jost2022interactionofthe pages 2-3, iburg2024elucidatingtheassembly pages 1-2)
- **Magnetic nanomaterials:** magnetosomes are being investigated for imaging and drug delivery. A 2024 review also identifies encapsulins as potential synthetic bionanoreactors. These remain translational research applications, not evidence that an organism naturally forms inclusions for medical use. (ferrara2024bacterialorganellesin pages 12-14)
- **Bioplastics:** microbial PHA granules are harvested as biodegradable polymer feedstock. The direct causal biology is PhaC-dependent polymer synthesis and granule assembly; commercial productivity, however, depends on fermentation and downstream processing beyond the morphology graph.
- **Stress-tolerant cell factories:** manipulation of phasins can increase PHB production and stress tolerance in engineered hosts, although effects depend on host, carbon source, and assay. (mullersantos2021theprotectiverole pages 9-10)

## Expert analysis for TraitMech curation

The most defensible generic mechanism is:

**inclusion-forming machinery + available cargo/substrate + permissive environmental state → assembly or accumulation of a spatially discrete intracellular body → compartmentalization/storage/buoyancy/navigation.**

That abstraction should not be expanded into gene-level universal edges. Gvp proteins cannot cause a PHB granule; PhaC cannot cause a magnetosome; Mam proteins cannot cause a carboxysome. The parent graph should therefore contain generic concepts such as **cargo accumulation**, **boundary/shell assembly**, **intracellular compartmentalization**, and **discrete inclusion morphology**, while named genes reside under subtype branches.

For a first YAML revision, the highest-priority subtype evidence is: BMC shell→cargo compartmentalization; GvpA→gas-vesicle shell ribs; GvpC→gas-vesicle stabilization; ΔgvpN→small-vesicle phenotype; PhaM→PhaC activation and granule organization; PhaP1→PHB-granule morphology; and mamAB→magnetosome membrane formation. The first six have particularly clear mechanistic or perturbational support in the retrieved evidence. (trettel2024modelingbacterialmicrocompartment pages 1-2, mullersantos2021theprotectiverole pages 35-36, mullersantos2021theprotectiverole pages 5-6, jost2022interactionofthe pages 2-3, jost2022interactionofthe pages 1-2)

## Warnings: claims not yet ready for TraitMech

1. **Do not attach subtype-specific genes directly to `traitmech:000066` as universal causes.** Use child graphs and taxon qualifiers.
2. **Do not curate simulation output as experimental causality.** The 2024 atomic carboxysome permeability study is a preprint using an incomplete synthetic shell. (sarkar2024atomicviewof pages 7-8)
3. **Do not infer function from protein interaction alone.** GvpN–GvpO and Gvp–GvpC contacts are demonstrated; ATP-powered incorporation by GvpN remains a hypothesis. (jost2022interactionofthe pages 1-2, jost2022interactionofthe pages 14-15)
4. **Do not equate every polyphosphate granule with an acidocalcisome.** Membrane enclosure and taxonomic context require direct evidence.
5. **Do not curate iron remobilization from magnetosomes or ferrosomes.** The 2024 review identifies this as unresolved. (ferrara2024bacterialorganellesin pages 12-14)
6. **Do not convert conditional associations into universal environmental edges.** Oxygen, sulfur, substrate, carbon/nutrient imbalance, and iron-shift effects depend on inclusion subtype and organism. (ferrara2024bacterialorganellesin pages 1-2)
7. **Do not treat heterologous constructs as native mechanisms.** Programmable carboxysome cages, gas-vesicle expression in eukaryotes, and phaP-overexpressing *E. coli* are applications or perturbations. (li2024nanoengineeringcarboxysomeshells pages 11-12, mullersantos2021theprotectiverole pages 9-10, jost2022interactionofthe pages 14-15)
8. **Glycogen and polyP mechanisms need additional primary retrieval.** Polymer synthesis is not by itself evidence that a microscopically discrete granule formed.
9. **Ontology identifiers should be validated against the project’s pinned releases.** Label-only nodes are preferable to an invented or obsolete CURIE.

## DOI-first bibliography

1. Ferrara KM, Gupta KR, Pi H. **Bacterial Organelles in Iron Physiology.** *Molecular Microbiology* 122:914–928. Published November 2024. DOI: [10.1111/mmi.15330](https://doi.org/10.1111/mmi.15330). (ferrara2024bacterialorganellesin pages 2-4, ferrara2024bacterialorganellesin pages 12-14, ferrara2024bacterialorganellesin pages 1-2)
2. Iburg M, et al. **Elucidating the assembly of gas vesicles by systematic protein-protein interaction analysis.** *The EMBO Journal* 43:4156–4172. Published September 2024. DOI: [10.1038/s44318-024-00178-2](https://doi.org/10.1038/s44318-024-00178-2). (iburg2024elucidatingtheassembly pages 1-2)
3. Li T, et al. **Nanoengineering Carboxysome Shells for Protein Cages with Programmable Cargo Targeting.** *ACS Nano* 18:7473–7484. Published February 2024. DOI: [10.1021/acsnano.3c11559](https://doi.org/10.1021/acsnano.3c11559). (li2024nanoengineeringcarboxysomeshells pages 11-12)
4. Trettel DS, et al. **Modeling bacterial microcompartment architectures for enhanced cyanobacterial carbon fixation.** *Frontiers in Plant Science* 15. Published February 2024. DOI: [10.3389/fpls.2024.1346759](https://doi.org/10.3389/fpls.2024.1346759). (trettel2024modelingbacterialmicrocompartment pages 1-2)
5. Sarkar D, et al. **Atomic View of Photosynthetic Metabolite Permeability Pathways and Confinement in Cyanobacterial Carboxysomes.** *ChemRxiv*. Published October 2024; preprint. DOI: [10.26434/chemrxiv-2024-kbcdf-v2](https://doi.org/10.26434/chemrxiv-2024-kbcdf-v2). (sarkar2024atomicviewof pages 7-8)
6. Rose SM, Radhakrishnan A, Sinha S. **Innate and engineered attributes of bacterial microcompartments for applications in bio-materials science.** *Journal of Materials Chemistry B* 11:4842–4854. Published May 2023. DOI: [10.1039/D3TB00098B](https://doi.org/10.1039/D3TB00098B). (rose2023innateandengineered pages 1-2)
7. Jost A, Pfeifer F. **Interaction of the gas vesicle proteins GvpA, GvpC, GvpN, and GvpO of Halobacterium salinarum.** *Frontiers in Microbiology* 13. Published July 2022. DOI: [10.3389/fmicb.2022.971917](https://doi.org/10.3389/fmicb.2022.971917). (jost2022interactionofthe pages 2-3, jost2022interactionofthe pages 1-2)
8. Müller-Santos M, et al. **The protective role of PHB and its degradation products against stress situations in bacteria.** *FEMS Microbiology Reviews* 45. Published October 2021. DOI: [10.1093/femsre/fuaa058](https://doi.org/10.1093/femsre/fuaa058). (mullersantos2021theprotectiverole pages 9-10, mullersantos2021theprotectiverole pages 35-36, mullersantos2021theprotectiverole pages 5-6)

The supplied foundational reviews—Greening and Lithgow, DOI [10.1038/s41579-020-0413-0](https://doi.org/10.1038/s41579-020-0413-0), and Kerfeld et al., DOI [10.1038/nrmicro.2018.10](https://doi.org/10.1038/nrmicro.2018.10)—remain appropriate support for the broad parent class, while the subtype-level edges above provide the more actionable basis for revising `data/traits/morphology/intracellular_inclusion.yaml`.

References

1. (ferrara2024bacterialorganellesin pages 1-2): Kristina M. Ferrara, Kuldeepkumar R. Gupta, and Hualiang Pi. Bacterial organelles in iron physiology. Molecular Microbiology, 122:914-928, Nov 2024. URL: https://doi.org/10.1111/mmi.15330, doi:10.1111/mmi.15330. This article has 7 citations and is from a domain leading peer-reviewed journal.

2. (rose2023innateandengineered pages 1-2): S. M. Rose, Aarcha Radhakrishnan, and Sharmistha Sinha. Innate and engineered attributes of bacterial microcompartments for applications in bio-materials science. Journal of materials chemistry. B, 11:4842-4854, May 2023. URL: https://doi.org/10.1039/d3tb00098b, doi:10.1039/d3tb00098b. This article has 12 citations and is from a peer-reviewed journal.

3. (mullersantos2021theprotectiverole pages 5-6): Marcelo Müller-Santos, Janne J Koskimäki, Luis Paulo Silveira Alves, Emanuel Maltempi de Souza, Dieter Jendrossek, and Anna Maria Pirttilä. The protective role of phb and its degradation products against stress situations in bacteria. FEMS microbiology reviews, Oct 2021. URL: https://doi.org/10.1093/femsre/fuaa058, doi:10.1093/femsre/fuaa058. This article has 142 citations and is from a domain leading peer-reviewed journal.

4. (iburg2024elucidatingtheassembly pages 1-2): Manuel Iburg, Andrew P Anderson, Vivian T. Wong, Erica D. Anton, Art He, and George J. Lu. Elucidating the assembly of gas vesicles by systematic protein-protein interaction analysis. Sep 2024. URL: https://doi.org/10.1038/s44318-024-00178-2, doi:10.1038/s44318-024-00178-2. This article has 11 citations.

5. (trettel2024modelingbacterialmicrocompartment pages 1-2): Daniel S. Trettel, Sara L. Pacheco, Asa K. Laskie, Raul Gonzalez-Esquer, Jianping Yu, Harvey J. M. Hou, and Denis Jallet. Modeling bacterial microcompartment architectures for enhanced cyanobacterial carbon fixation. Frontiers in Plant Science, Feb 2024. URL: https://doi.org/10.3389/fpls.2024.1346759, doi:10.3389/fpls.2024.1346759. This article has 11 citations.

6. (sarkar2024atomicviewof pages 7-8): Daipayan Sarkar, Christopher Maffeo, Markus Sutter, Aleksei Aksimentiev, Cheryl Kerfeld, and Josh Vermaas. Atomic view of photosynthetic metabolite permeability pathways and confinement in cyanobacterial carboxysomes. ChemRxiv, Oct 2024. URL: https://doi.org/10.26434/chemrxiv-2024-kbcdf-v2, doi:10.26434/chemrxiv-2024-kbcdf-v2. This article has 9 citations.

7. (jost2022interactionofthe pages 1-2): Alisa Jost and Felicitas Pfeifer. Interaction of the gas vesicle proteins gvpa, gvpc, gvpn, and gvpo of halobacterium salinarum. Frontiers in Microbiology, Jul 2022. URL: https://doi.org/10.3389/fmicb.2022.971917, doi:10.3389/fmicb.2022.971917. This article has 22 citations and is from a peer-reviewed journal.

8. (jost2022interactionofthe pages 2-3): Alisa Jost and Felicitas Pfeifer. Interaction of the gas vesicle proteins gvpa, gvpc, gvpn, and gvpo of halobacterium salinarum. Frontiers in Microbiology, Jul 2022. URL: https://doi.org/10.3389/fmicb.2022.971917, doi:10.3389/fmicb.2022.971917. This article has 22 citations and is from a peer-reviewed journal.

9. (jost2022interactionofthe pages 14-15): Alisa Jost and Felicitas Pfeifer. Interaction of the gas vesicle proteins gvpa, gvpc, gvpn, and gvpo of halobacterium salinarum. Frontiers in Microbiology, Jul 2022. URL: https://doi.org/10.3389/fmicb.2022.971917, doi:10.3389/fmicb.2022.971917. This article has 22 citations and is from a peer-reviewed journal.

10. (mullersantos2021theprotectiverole pages 35-36): Marcelo Müller-Santos, Janne J Koskimäki, Luis Paulo Silveira Alves, Emanuel Maltempi de Souza, Dieter Jendrossek, and Anna Maria Pirttilä. The protective role of phb and its degradation products against stress situations in bacteria. FEMS microbiology reviews, Oct 2021. URL: https://doi.org/10.1093/femsre/fuaa058, doi:10.1093/femsre/fuaa058. This article has 142 citations and is from a domain leading peer-reviewed journal.

11. (mullersantos2021theprotectiverole pages 40-41): Marcelo Müller-Santos, Janne J Koskimäki, Luis Paulo Silveira Alves, Emanuel Maltempi de Souza, Dieter Jendrossek, and Anna Maria Pirttilä. The protective role of phb and its degradation products against stress situations in bacteria. FEMS microbiology reviews, Oct 2021. URL: https://doi.org/10.1093/femsre/fuaa058, doi:10.1093/femsre/fuaa058. This article has 142 citations and is from a domain leading peer-reviewed journal.

12. (mullersantos2021theprotectiverole pages 9-10): Marcelo Müller-Santos, Janne J Koskimäki, Luis Paulo Silveira Alves, Emanuel Maltempi de Souza, Dieter Jendrossek, and Anna Maria Pirttilä. The protective role of phb and its degradation products against stress situations in bacteria. FEMS microbiology reviews, Oct 2021. URL: https://doi.org/10.1093/femsre/fuaa058, doi:10.1093/femsre/fuaa058. This article has 142 citations and is from a domain leading peer-reviewed journal.

13. (ferrara2024bacterialorganellesin pages 2-4): Kristina M. Ferrara, Kuldeepkumar R. Gupta, and Hualiang Pi. Bacterial organelles in iron physiology. Molecular Microbiology, 122:914-928, Nov 2024. URL: https://doi.org/10.1111/mmi.15330, doi:10.1111/mmi.15330. This article has 7 citations and is from a domain leading peer-reviewed journal.

14. (ferrara2024bacterialorganellesin pages 12-14): Kristina M. Ferrara, Kuldeepkumar R. Gupta, and Hualiang Pi. Bacterial organelles in iron physiology. Molecular Microbiology, 122:914-928, Nov 2024. URL: https://doi.org/10.1111/mmi.15330, doi:10.1111/mmi.15330. This article has 7 citations and is from a domain leading peer-reviewed journal.

15. (mullersantos2021theprotectiverole pages 33-34): Marcelo Müller-Santos, Janne J Koskimäki, Luis Paulo Silveira Alves, Emanuel Maltempi de Souza, Dieter Jendrossek, and Anna Maria Pirttilä. The protective role of phb and its degradation products against stress situations in bacteria. FEMS microbiology reviews, Oct 2021. URL: https://doi.org/10.1093/femsre/fuaa058, doi:10.1093/femsre/fuaa058. This article has 142 citations and is from a domain leading peer-reviewed journal.

16. (trettel2024modelingbacterialmicrocompartment pages 12-12): Daniel S. Trettel, Sara L. Pacheco, Asa K. Laskie, Raul Gonzalez-Esquer, Jianping Yu, Harvey J. M. Hou, and Denis Jallet. Modeling bacterial microcompartment architectures for enhanced cyanobacterial carbon fixation. Frontiers in Plant Science, Feb 2024. URL: https://doi.org/10.3389/fpls.2024.1346759, doi:10.3389/fpls.2024.1346759. This article has 11 citations.

17. (li2024nanoengineeringcarboxysomeshells pages 11-12): Tianpei Li, Ping Chang, Weixian Chen, Zhaoyang Shi, Chunling Xue, Gregory F. Dykes, Fang Huang, Qiang Wang, and Lu-Ning Liu. Nanoengineering carboxysome shells for protein cages with programmable cargo targeting. ACS Nano, 18:7473-7484, Feb 2024. URL: https://doi.org/10.1021/acsnano.3c11559, doi:10.1021/acsnano.3c11559. This article has 32 citations and is from a highest quality peer-reviewed journal.