---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:08:16.101363'
end_time: '2026-06-18T04:24:13.317375'
duration_seconds: 957.22
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Cable bacteria metabolism
  trait_identifier: METPO:1002003
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: cable_bacteria_metabolism
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which electrons are transferred over centimeter-scale
    distances through multicellular filaments.
  parent_traits: METPO:1000060
  synonyms: ''
  evidence_summary: 'DOI:10.1073/pnas.1800367115: Long-distance electron transport
    in individual, living cable bacteria (Study directly demonstrates long-distance
    electron transport in cable bacteria.) | DOI:10.3389/fmars.2017.00028: oxidize
    sulfide in deeper sediments (Study supports electrogenic sulfur oxidation with
    sulfide oxidation and oxygen reduction zones.)'
  causal_graph_summary: 'cable_bacteria_long_distance_electron_transport: 10 nodes,
    9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Cable bacteria metabolism
- **METPO identifier:** METPO:1002003
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which electrons are transferred over centimeter-scale distances through multicellular filaments.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1073/pnas.1800367115: Long-distance electron transport in individual, living cable bacteria (Study directly demonstrates long-distance electron transport in cable bacteria.) | DOI:10.3389/fmars.2017.00028: oxidize sulfide in deeper sediments (Study supports electrogenic sulfur oxidation with sulfide oxidation and oxygen reduction zones.)
- **Existing causal graph summary:** cable_bacteria_long_distance_electron_transport: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **Cable bacteria metabolism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/cable_bacteria_metabolism.yaml`.

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
- **Trait label:** Cable bacteria metabolism
- **METPO identifier:** METPO:1002003
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which electrons are transferred over centimeter-scale distances through multicellular filaments.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1073/pnas.1800367115: Long-distance electron transport in individual, living cable bacteria (Study directly demonstrates long-distance electron transport in cable bacteria.) | DOI:10.3389/fmars.2017.00028: oxidize sulfide in deeper sediments (Study supports electrogenic sulfur oxidation with sulfide oxidation and oxygen reduction zones.)
- **Existing causal graph summary:** cable_bacteria_long_distance_electron_transport: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **Cable bacteria metabolism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/cable_bacteria_metabolism.yaml`.

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


# Research report: Cable bacteria metabolism (METPO:1002003)

## 0) Scope summary (trait definition, boundaries)

**Trait label:** Cable bacteria metabolism (METPO:1002003)

**Operational definition (curation-ready):** A multicellular filament metabolism in which **electrons generated by sulfide oxidation in deeper (more reduced) sediment are transported over millimeter–centimeter distances through an internal conductive network in the filament cell envelope** to support reduction of a spatially separated terminal electron acceptor (classically O2; also NO3− in some contexts) near the sediment surface. This long-distance electron transport (LDET) is a defining physiological capability and is experimentally evidenced by perturbation (oxygen removal, filament cutting) and direct electrical measurements. (yang2024longdistanceelectrontransport pages 1-2, bjerg2018longdistanceelectrontransport pages 1-2, hiralal2024comparativegenomicanalysis pages 1-2)

**Boundary cases / nearby traits to distinguish:**
- **Not simply “sulfide oxidation”:** many bacteria oxidize sulfide locally; the hallmark here is **spatial separation of redox half-reactions** coupled by **centimeter-scale internal electronic conduction**. (yang2024longdistanceelectrontransport pages 1-2, bjerg2018longdistanceelectrontransport pages 1-2)
- **Not classic extracellular electron transfer (EET) alone:** cable bacteria can interact with electrodes (application/assay extension), but the trait primarily concerns **internal filament conduction linking distinct zones** rather than only cell-to-electrode transfer. (bonne2024interactionofliving pages 1-2)
- **Not Geobacter-type micrometer-scale conduction:** cable bacteria conduction occurs across **centimeter-long filaments** and is mechanistically distinct from multiheme-cytochrome nanowire paradigms (modeling/interpretation). (veen2024amodelanalysis pages 1-2)

## 1) Key concepts and current understanding (mechanistic overview)

### 1.1 Spatially separated redox half-reactions (“electric metabolism”)
Cable bacteria couple **sulfide (H2S) oxidation** in deeper sediment to **oxygen reduction** near the sediment–water interface, with electrons transported along the filament to connect the separated half-reactions. This donor/acceptor separation is directly used experimentally by placing a filament with **sulfide at one end and oxygen at the other**. (bjerg2018longdistanceelectrontransport pages 1-2, veen2024amodelanalysis pages 1-2)

### 1.2 Conductive pathway: a periplasmic/cell-envelope fiber network
Multiple 2024 studies converge on a model where a **network of parallel conductive fibers embedded in the cell envelope** mediates LDET along the filament length. Conductive AFM mapping shows current signals aligned with the surface ridge/nanofiber pattern, visually supporting localization of conduction to the nanofiber network. (yang2024longdistanceelectrontransport pages 1-2, hiralal2024comparativegenomicanalysis pages 1-2, yang2024longdistanceelectrontransport media fbde9623)

### 1.3 Nickel-based conduction: Ni cofactor embedded in fibers
Raman microscopy and comparative genomics provide strong evidence that conductive fibers contain a **sulfur-coordinated nickel cofactor** (often described as NiBiD-like / nickel bis(dithiolene)-like). The Raman spectrum simplifies after extraction of the conductive fiber network (“fiber skeletons”), and **Ni-cofactor modes dominate** and show strong **orientation-dependent anisotropy**, supporting that the cofactor is aligned with the fiber axis (i.e., the electron-transport direction). (smets2024multiwavelengthramanmicroscopy pages 1-2, smets2024multiwavelengthramanmicroscopy pages 11-12, hiralal2024comparativegenomicanalysis pages 1-2)

### 1.4 Role of cytochromes: essential in redox-state reporting, but likely not the long-range conductor
A foundational perturbation experiment used resonance Raman microscopy to show a **cytochrome redox gradient** along living filaments that collapses upon **oxygen removal** or **laser cutting**, establishing continuity-dependent LDET. (bjerg2018longdistanceelectrontransport pages 1-2)

However, Raman analysis of extracted conductive fiber skeletons indicates cytochrome signatures disappear while fiber conductivity-related Ni signals remain, implying **cytochromes are not the conductive fibers** (though they may participate in electron loading/unloading). (smets2024multiwavelengthramanmicroscopy pages 10-11)

## 2) Recent developments and latest research (priority 2023–2024)

### 2.1 Quantitative conductivity and direct electronic measurements in freshwater cable bacteria (2024)
Yang et al. (eLife, May 2024) extended direct conductivity characterization to **freshwater cable bacteria (Ca. Electronema)** using interdigitated electrodes and four-probe microelectrode devices, measuring **nanoampere currents up to ~200 μm** and estimating a **nanofiber conductivity of ~0.1 S/cm** under their conditions; they also mapped the conductive network with electrostatic and conductive AFM. (yang2024longdistanceelectrontransport pages 1-2, yang2024longdistanceelectrontransport media fbde9623, yang2024longdistanceelectrontransport media bc0cc273)

### 2.2 Temperature dependence and conduction mechanism inference (2024)
van der Veen et al. (ACS Nano, Nov 2024) measured conductance from room temperature to cryogenic temperatures and argued the data support an **incoherent multistep hopping model** within parallel conduction channels, with low activation energies and high transfer efficiency; at low temperatures conductance becomes nearly temperature-independent, interpreted as involvement of nuclear tunneling. (veen2024temperaturedependentcharacterizationof pages 1-2)

### 2.3 Nickel cofactor fingerprint and orientation dependence (2024)
Smets et al. (Frontiers in Microbiology, Mar 2024) used multi-wavelength Raman microscopy to identify a **13-mode Ni-cofactor vibrational fingerprint** across 405–1,064 nm, with key modes (e.g., **367 and 496 cm−1**) and **2–6× higher intensity when fibers are aligned with incident polarization**, supporting a planar, fiber-aligned cofactor architecture; they note this signature does not match known biological Ni cofactors. (smets2024multiwavelengthramanmicroscopy pages 11-12, smets2024multiwavelengthramanmicroscopy pages 12-14)

### 2.4 Genomic closure and nickel homeostasis adaptations (2024)
- Hiralal et al. (Microbial Genomics, Feb 2024) reported a **closed circular genome** for *Candidatus Electrothrix scaldis* (5.09 Mbp; **4,397 protein-coding genes**; **1,109 (24%) novel vs prior Electrothrix genomes**), including genes consistent with oxygen reduction (aa3-type cytochrome c oxidase), nitrate reduction (nap operon), and expanded Dsr-pathway components. (hiralal2024closingthegenome pages 9-11)
- Hiralal et al. (BMC Genomics, Jul 2024) analyzed **nickel homeostasis genes** across cable bacteria genomes and highlighted genomic adaptation consistent with a **Ni-dependent conduction mechanism**, including multiple predicted Ni import routes and a unique RcnA-like Ni exporter. (hiralal2024comparativegenomicanalysis pages 1-2)

## 3) Current applications and real-world implementations

### 3.1 Bioelectrochemical systems (electrode interactions)
Bonné et al. (Applied and Environmental Microbiology, Aug 2024) demonstrated that living freshwater cable bacteria can be **attracted to carbon electrodes poised at +200 mV (vs Ag/AgCl)**, reversibly **retracting** when potential is switched off. In sediment bioelectrochemical cells, inoculation increased currents (reported averages **~17–78 µA** vs **~4.75 ± 0.5 µA** autoclaved controls), and qPCR/SEM indicated substantial enrichment of cable bacteria on poised electrodes; authors interpret this as evidence consistent with electrode reduction via EET, though they note the mechanism (direct contact vs mediators) remains unresolved. (bonne2024interactionofliving pages 1-2, bonne2024interactionofliving pages 2-5, bonne2024interactionofliving pages 5-8)

### 3.2 Environmental geochemistry / ecosystem engineering (contextual)
Cable bacteria are widely discussed as **sediment biogeochemical “engineers”** due to their ability to connect redox zones and drive distinctive geochemical fingerprints (review context). (yang2024longdistanceelectrontransport pages 18-19, zhuang2024electrontransferin pages 15-16)

## 4) Expert opinions and authoritative analysis (from reviews and synthesis papers)

A 2024 review focusing on sulfur-cycle electron transfer frames cable bacteria as a key example of long-distance electron transfer in sulfur-oxidizing filamentous bacteria, emphasizing that conduction is mediated by **highly conductive periplasmic fibers** and linked to a **nickel-based cofactor**, and highlighting the potential for bioelectronic applications and bioremediation technologies. (zhuang2024electrontransferin pages 6-8)

## 5) Relevant statistics and quantitative data (from recent studies)

- **Nanofiber conductivity in freshwater cable bacteria:** ~**0.1 S/cm** (measurement conditions specified by Yang et al.) and nanoampere currents over **up to ~200 µm** in four-probe measurements. (yang2024longdistanceelectrontransport pages 1-2)
- **High conductivity context:** modeling/synthesis papers cite conductivities that “can exceed **100 S cm−1**” for cable-bacteria fibers (contextualized as prior experimental observations used for modeling). (veen2024amodelanalysis pages 1-2)
- **Genome statistics (closed genome):** 5.09 Mbp; 4,397 protein-coding genes; 1,109 genes (24%) novel vs prior *Ca. Electrothrix* genomes. (hiralal2024closingthegenome pages 9-11)
- **Bioelectrochemical current response with cable bacteria:** averages **~17–78 µA** vs **~4.75 ± 0.5 µA** in autoclaved controls; adding ~10 living filaments raised current from ~2 to ~8 µA within 48 h (assay-specific). (bonne2024interactionofliving pages 2-5)

## 6) Candidate causal-graph content for TraitMech curation

### 6.1 Candidate nodes (grouped by type)

**A. Processes / functions**
- Long-distance electron transport / centimeter-scale electron transport (METPO:1002003; label node)
- Sulfide oxidation (GO:0019419)
- Oxygen reduction / aerobic respiration (label; terminal oxidase-dependent)
- Respiratory nitrate reduction / DNRA (label; supported by nap operon + multiheme cytochrome candidates) (hiralal2024closingthegenome pages 9-11, hiralal2024comparativegenomicanalysis pages 5-7)
- Nickel ion homeostasis (GO:0055074) (hiralal2024comparativegenomicanalysis pages 1-2)

**B. Cellular structures**
- Multicellular filament (label)
- Cell envelope / periplasmic conductive fiber network (label)
- Cell-to-cell junction “cartwheel” conductive structure (label) (hiralal2024comparativegenomicanalysis pages 1-2)
- Surface ridges/nanofiber tracks (label) (yang2024longdistanceelectrontransport media fbde9623)

**C. Chemicals / metabolites / ions**
- Hydrogen sulfide (CHEBI:16189)
- Dioxygen (CHEBI:15379)
- Nitrate (CHEBI:17632)
- Nickel ion (CHEBI:28112)

**D. Cofactors / biomaterials**
- Sulfur-coordinated Ni cofactor (NiBiD-like; label-only until stable ontology is available) (smets2024multiwavelengthramanmicroscopy pages 11-12, hiralal2024comparativegenomicanalysis pages 1-2)

**E. Genes / proteins / complexes (label-only unless curated to UniProt/EC)**
- Dsr pathway components: DsrAB, DsrC, DsrMKJOP (and newly reported dsrJ, dsrO, dsrP, dsrD, dsrT) (hiralal2024closingthegenome pages 11-13)
- Apr/Qmo complex; Sqr; Psr/Phs (pathway inference) (hiralal2024comparativegenomicanalysis pages 5-7)
- Terminal oxidases: aa3-type cytochrome c oxidase (CoxBACD); cytochrome bd quinol oxidase (CydBSA) (genome/strain-specific) (hiralal2024closingthegenome pages 9-11, hiralal2024comparativegenomicanalysis pages 5-7)
- Nitrate reduction: nap operon including napB; putative periplasmic multiheme cytochromes (pOCC/pOOC) (hiralal2024closingthegenome pages 9-11, hiralal2024comparativegenomicanalysis pages 5-7)
- Nickel transport/homeostasis: TonB-dependent uptake, NiCoT transporter, ABC Ni uptake, RcnA-like exporter (hiralal2024comparativegenomicanalysis pages 1-2)

### 6.2 Candidate causal edges (evidence-backed)

The following artifact provides a curation-ready edge table with suggested grounding, snippets, references, and uncertainty flags.

| Edge (S–P–O) | Entity types | Suggested ontology grounding | Evidence snippet | Reference (DOI + URL + year) | Curation notes/uncertainty |
|---|---|---|---|---|---|
| sulfide oxidation **enables electron release for** long-distance electron transport | chemical → process | CHEBI:16189 hydrogen sulfide; GO:0019419 sulfide oxidation; METPO:1002003 cable bacteria metabolism | Cable bacteria couple “oxidation of free sulfide (H2S)” to distant O2 reduction, with electrons conveyed internally along filaments (veen2024amodelanalysis pages 1-2, yang2024longdistanceelectrontransport pages 1-2) | 10.1039/d3cp04466a — https://doi.org/10.1039/d3cp04466a — 2024; 10.7554/eLife.91097 — https://doi.org/10.7554/eLife.91097 — 2024 | Strong trait-level edge; exact immediate electron-releasing enzymatic step should be curated separately if gene-level evidence is needed. |
| oxygen reduction **acts as terminal electron sink for** long-distance electron transport | chemical → process | CHEBI:15379 dioxygen; GO:0016491 oxidoreductase activity; METPO:1002003 | Filaments were placed with “sulfide as electron source and oxygen as electron sink at opposite ends”; removing oxygen caused reduced cytochromes to accumulate (bjerg2018longdistanceelectrontransport pages 1-2) | 10.1073/pnas.1800367115 — https://doi.org/10.1073/pnas.1800367115 — 2018 | Strong physiological edge. Does not by itself identify the terminal oxidase. |
| nitrate reduction **can serve as terminal electron sink for** cable bacteria metabolism | chemical → process | CHEBI:17632 nitrate; GO:0042128 nitrate assimilation/label-only for respiratory nitrate reduction; METPO:1002003 | Freshwater cable bacteria couple sulfide oxidation to “oxygen or nitrate reduction near the surface” (yang2024longdistanceelectrontransport pages 1-2); nap operon plus putative periplasmic octaheme cytochrome suggest DNRA coupling (hiralal2024comparativegenomicanalysis pages 5-7, hiralal2024closingthegenome pages 9-11) | 10.7554/eLife.91097 — https://doi.org/10.7554/eLife.91097 — 2024; 10.1099/mgen.0.001197 — https://doi.org/10.1099/mgen.0.001197 — 2024 | Moderate; taxon/genome-specific details vary. Keep electron-acceptor role distinct from verified growth/energy-conservation claims. |
| conductive periplasmic fiber network **mediates** long-distance electron transport | cellular structure/protein network → process | GO:1990351 cell periphery (broad); label-only: periplasmic conductive fiber network; METPO:1002003 | “Network of parallel conductive fibres embedded in the cell envelope” mediates filament-scale transport; AFM/current mapping implicated the nanofiber network as conductive route (hiralal2024comparativegenomicanalysis pages 1-2, yang2024longdistanceelectrontransport pages 1-2, yang2024longdistanceelectrontransport media fbde9623) | 10.1186/s12864-024-10594-7 — https://doi.org/10.1186/s12864-024-10594-7 — 2024; 10.7554/eLife.91097 — https://doi.org/10.7554/eLife.91097 — 2024 | Core mechanistic edge; grounding for the fiber network is label-only. |
| conductive fibers **are part of** cell envelope | protein structure → cellular component | label-only: conductive fibers; GO:0030313 cell envelope | Fibers are “embedded in the cell envelope” and run along filament length (veen2024temperaturedependentcharacterizationof pages 1-2, hiralal2024comparativegenomicanalysis pages 1-2, smets2024multiwavelengthramanmicroscopy pages 1-2) | 10.1021/acsnano.4c12186 — https://doi.org/10.1021/acsnano.4c12186 — 2024; 10.1186/s12864-024-10594-7 — https://doi.org/10.1186/s12864-024-10594-7 — 2024; 10.3389/fmicb.2024.1208033 — https://doi.org/10.3389/fmicb.2024.1208033 — 2024 | Structural edge useful for node placement/localization. |
| sulfur-ligated nickel cofactor **is component of** conductive fibers | cofactor → protein structure | CHEBI:28112 nickel cation (broad); label-only: NiBiD / sulfur-ligated Ni cofactor | Raman and extraction data show fiber skeletons are enriched in Ni-cofactor-associated modes; the conductive fibers “harbour a novel nickel-containing cofactor” (hiralal2024comparativegenomicanalysis pages 1-2, smets2024multiwavelengthramanmicroscopy pages 1-2, smets2024multiwavelengthramanmicroscopy pages 10-11) | 10.1186/s12864-024-10594-7 — https://doi.org/10.1186/s12864-024-10594-7 — 2024; 10.3389/fmicb.2024.1208033 — https://doi.org/10.3389/fmicb.2024.1208033 — 2024 | Strong, but exact chemistry remains unresolved; use label-only for NiBiD until stable ontology grounding is available. |
| nickel cofactor **supports/mediates** long-range electron transport | cofactor → process | label-only: NiBiD; METPO:1002003 | Authors explicitly link a “Ni-based, long-range electron transport pathway” to the cofactor; orientation-dependent Raman signals align cofactor with fiber/electron path (smets2024multiwavelengthramanmicroscopy pages 12-14, smets2024multiwavelengthramanmicroscopy pages 11-12, smets2024multiwavelengthraman pages 13-14) | 10.3389/fmicb.2024.1208033 — https://doi.org/10.3389/fmicb.2024.1208033 — 2024 | Strong but still mechanistic inference from spectroscopy; exact charge-transfer mechanism remains unresolved. |
| nickel homeostasis genes **promote nickel availability for** Ni-cofactor biosynthesis/homeostasis | genes/process → cofactor availability | label-only: nickel homeostasis genes; GO:0055074 nickel ion homeostasis; CHEBI:28112 | Cable bacteria show “clear genetic adaptation for nickel utilization”; genomes encode Ni importers, chaperones, and unique RcnA export protein, aligning with Ni-dependent conduction (hiralal2024comparativegenomicanalysis pages 1-2) | 10.1186/s12864-024-10594-7 — https://doi.org/10.1186/s12864-024-10594-7 — 2024 | Good systems-level edge; individual gene→cofactor edges should be split when gene-specific identifiers are available. |
| RcnA-like periplasmic nickel export protein **contributes to** nickel homeostasis | protein → process | label-only: RcnA; GO:0055074 nickel ion homeostasis | Cable bacteria encode a “unique periplasmic nickel export protein RcnA” with expanded histidine-rich loop (hiralal2024comparativegenomicanalysis pages 1-2) | 10.1186/s12864-024-10594-7 — https://doi.org/10.1186/s12864-024-10594-7 — 2024 | Moderate; role inferred from comparative genomics, not direct knockout/biochemical test. Mark as inferred. |
| TonB-dependent/Ni-siderophore, NiCoT, and ABC nickel uptake systems **increase intracellular nickel availability** | transporters/genes → chemical availability | label-only: TonB-dependent Ni uptake, NiCoT transporter, ABC nickel uptake; CHEBI:28112 | Comparative genomics identified “Ni import routes… TonB-dependent transporters; cytoplasmic NiCoT and ABC uptake systems” (hiralal2024comparativegenomicanalysis pages 1-2) | 10.1186/s12864-024-10594-7 — https://doi.org/10.1186/s12864-024-10594-7 — 2024 | Inferred genomic edge; transporter identities need locus-level grounding before fine curation. |
| intact electrical connection along filament **maintains** cytochrome redox gradient | process/structure → process | label-only: intact filament conductivity; label-only: cytochrome redox gradient | A redox gradient along filaments “immediately broke down upon removal of oxygen or laser cutting” (bjerg2018longdistanceelectrontransport pages 1-2) | 10.1073/pnas.1800367115 — https://doi.org/10.1073/pnas.1800367115 — 2018 | Strong direct physiological evidence. |
| oxygen removal **causes collapse of** cytochrome redox gradient | experimental factor → process | CHEBI:15379 dioxygen; label-only: cytochrome redox gradient | “Without access to oxygen, a rapid shift toward more reduced cytochromes was observed” because electrons were no longer drained (bjerg2018longdistanceelectrontransport pages 1-2) | 10.1073/pnas.1800367115 — https://doi.org/10.1073/pnas.1800367115 — 2018 | Strong assay-specific causal perturbation. |
| laser cutting of filament **disrupts** long-distance electron transport | experimental factor → process | label-only: laser cutting; METPO:1002003 | Cytochrome redox gradient “immediately broke down upon… laser cutting of the filaments” (bjerg2018longdistanceelectrontransport pages 1-2) | 10.1073/pnas.1800367115 — https://doi.org/10.1073/pnas.1800367115 — 2018 | Strong perturbation evidence for continuity requirement. |
| cytochromes **are not the main conductive fibers in** long-distance electron transport | protein class → process | GO:0020037 heme binding (broad); label-only: cytochromes | Fiber skeletons retain current-carrying fibers after extraction while cytochrome peaks disappear; “cytochromes cannot make up the conductive fibers” (smets2024multiwavelengthramanmicroscopy pages 10-11, smets2024multiwavelengthraman pages 11-12) | 10.3389/fmicb.2024.1208033 — https://doi.org/10.3389/fmicb.2024.1208033 — 2024 | Negative/constraint edge; useful to avoid mis-curation of cytochromes as primary centimeter-scale conductors. |
| periplasmic cytochromes **may load/unload electrons to/from** conductive fibers | protein class → protein structure | label-only: periplasmic cytochromes; label-only: conductive fibers | Raman study hypothesizes cytochromes could play an “auxiliary role” in electron transfer/loading-unloading rather than central conduction (smets2024multiwavelengthramanmicroscopy pages 10-11) | 10.3389/fmicb.2024.1208033 — https://doi.org/10.3389/fmicb.2024.1208033 — 2024 | Uncertain/hypothesized; do not curate as strong edge yet. |
| high fiber conductivity **supports** nanoampere current over ~200 µm in intact cables | physical property → process/assay outcome | label-only: fiber conductivity; label-only: nanoamp current | Four-probe measurements showed nanoamp currents up to ~200 μm and quantified conductivity at ~0.1 S/cm in freshwater cable bacteria (yang2024longdistanceelectrontransport pages 1-2) | 10.7554/eLife.91097 — https://doi.org/10.7554/eLife.91097 — 2024 | Strong assay-supported edge; note value is condition- and taxon-specific. |
| conductive fiber network **can exceed conductivity of** 100 S cm−1 | physical property → material network | label-only: conductive fiber network | Model paper cites experimental conductivity “can exceed 100 S cm−1” for cable-bacterium fibers (veen2024amodelanalysis pages 1-2); Raman paper cites exceptional conductivity >100 S/cm (smets2024multiwavelengthramanmicroscopy pages 1-2) | 10.1039/d3cp04466a — https://doi.org/10.1039/d3cp04466a — 2024; 10.3389/fmicb.2024.1208033 — https://doi.org/10.3389/fmicb.2024.1208033 — 2024 | Secondary/model-backed summary of earlier measurements; keep numeric claims annotated with source context. |
| charge transport in fibers **is consistent with** incoherent multistep hopping | process model → process | label-only: multistep hopping electron transport | Temperature-dependent conductance supports “an incoherent multistep hopping model within parallel conduction channels” (veen2024temperaturedependentcharacterizationof pages 1-2) | 10.1021/acsnano.4c12186 — https://doi.org/10.1021/acsnano.4c12186 — 2024 | Mechanistic model edge; useful but should be flagged as model interpretation rather than directly observed molecular path. |
| cable bacterium cell envelope nanofiber ridges **correlate with** conductive pathways | cellular structure → physical property | label-only: cell-surface ridges; label-only: conductive nanofibers | Conductive AFM mapped current to the ridge pattern, implicating the cell-envelope nanofiber network as conductive route (yang2024longdistanceelectrontransport pages 1-2, yang2024longdistanceelectrontransport media fbde9623) | 10.7554/eLife.91097 — https://doi.org/10.7554/eLife.91097 — 2024 | Strong morphology-to-function edge, particularly for localization. |
| poised carbon electrode at +200 mV vs Ag/AgCl **attracts/promotes attachment of** living cable bacteria | experimental factor/environment → organism behavior | label-only: poised carbon electrode; label-only: electrode colonization/attraction | Live cable bacteria moved toward carbon electrodes poised at +200 mV; when potential was switched off, filaments retracted (bonne2024interactionofliving pages 1-2, bonne2024interactionofliving pages 5-8) | 10.1128/aem.00795-24 — https://doi.org/10.1128/aem.00795-24 — 2024 | Strong behavior edge; pertains to bioelectrochemical systems, not necessarily natural sediment trait expression. |
| cable bacteria attachment to poised electrodes **is associated with** increased current | organism behavior → assay outcome | label-only: electrode colonization; label-only: current production | Inoculation caused sigmoidal current increases; qPCR/SEM showed enrichment of cable bacteria on poised electrodes (bonne2024interactionofliving pages 2-5, bonne2024interactionofliving pages 1-2) | 10.1128/aem.00795-24 — https://doi.org/10.1128/aem.00795-24 — 2024 | Moderate; community members (e.g., co-enriched taxa) may contribute to current. |
| cable bacteria **may reduce** electrodes via extracellular electron transfer | organism/process → chemical/electrode | label-only: extracellular electron transfer to electrode | Authors interpret electrode interaction as “electroactive behavior consistent with EET,” but note direct contact vs mediators remains unresolved (bonne2024interactionofliving pages 2-5, bonne2024interactionofliving pages 5-8) | 10.1128/aem.00795-24 — https://doi.org/10.1128/aem.00795-24 — 2024 | Uncertain; keep as hypothesis/assay-specific edge only. |
| nap operon **supports capacity for** nitrate reduction | gene cluster → process | label-only: nap operon; GO:0008940 nitrate reductase activity | Closed genomes recovered “a full-length nap operon including napB”; an operon with nap genes plus pOCC suggests coupling to DNRA (hiralal2024closingthegenome pages 9-11, hiralal2024comparativegenomicanalysis pages 5-7) | 10.1099/mgen.0.001197 — https://doi.org/10.1099/mgen.0.001197 — 2024; 10.1186/s12864-024-10594-7 — https://doi.org/10.1186/s12864-024-10594-7 — 2024 | Genomic capacity edge; organism-level phenotype may be strain-specific. |
| Dsr-Apr-Qmo-Sqr-Psr/Phs sulfur oxidation pathway **supports** sulfide oxidation metabolism | pathway → process | label-only: Dsr-Apr-Qmo-Sqr-Psr/Phs pathway; GO:0019419 sulfide oxidation | Comparative genomics predicts sulfur oxidation through a “Dsr-Apr-Qmo-Sqr-Psr/Phs pathway” and presence of DsrMKJOPG across closed genomes (hiralal2024comparativegenomicanalysis pages 5-7, hiralal2024closingthegenome pages 11-13) | 10.1186/s12864-024-10594-7 — https://doi.org/10.1186/s12864-024-10594-7 — 2024; 10.1099/mgen.0.001197 — https://doi.org/10.1099/mgen.0.001197 — 2024 | Moderate; pathway-level genomic inference, not direct flux proof in all taxa/conditions. |
| terminal oxygen reduction in cable bacteria **may be non-energy-conserving** | process → bioenergetic outcome | label-only: oxygen reduction; label-only: non-energy-conserving oxygen reduction | eLife summary notes oxygen reduction is hypothesized to be mediated by periplasmic cytochromes “possibly without energy conservation because terminal oxidases are absent” (yang2024longdistanceelectrontransport pages 1-2) | 10.7554/eLife.91097 — https://doi.org/10.7554/eLife.91097 — 2024 | Highly uncertain/hypothesized; should not be curated as established unless corroborated by targeted bioenergetic evidence. |


*Table: This table lists evidence-backed causal edges for cable bacteria metabolism, emphasizing long-distance electron transport, conductive fibers, nickel-dependent conduction, sulfur/nitrate/oxygen redox coupling, and assay perturbations. It is designed to support TraitMech curation by separating strong mechanistic edges from inferred or uncertain claims.*

## 7) Visual evidence (figures/tables)

Yang et al. (eLife 2024) provide figures showing (i) conductive AFM current maps matching the surface ridge/nanofiber pattern and (ii) four-probe/interdigitated electrode setups used to quantify intrinsic conductivity; these support the node localization and measurement edges. (yang2024longdistanceelectrontransport media fbde9623, yang2024longdistanceelectrontransport media bc0cc273, yang2024longdistanceelectrontransport media 0ac9c07e)

## 8) Warnings / claims that should not yet be curated as “strong”

1. **Exact chemical identity of the Ni cofactor:** Raman data strongly indicate a sulfur-ligated Ni moiety with similarity to Ni bis(1,2-dithiolene) complexes, but the **precise molecular structure is not yet resolved**; keep as **label-only cofactor node**. (smets2024multiwavelengthramanmicroscopy pages 12-14, smets2024multiwavelengthramanmicroscopy pages 11-12)
2. **Cytochromes as primary centimeter-scale conductors:** evidence supports cytochromes as redox-active components and reporters, but extracted fiber skeletons indicate cytochromes are **not** the conductive fibers; avoid curating cytochromes as the main long-distance conductor. (smets2024multiwavelengthramanmicroscopy pages 10-11, bjerg2018longdistanceelectrontransport pages 1-2)
3. **Energy conservation by oxygen reduction:** some sources present hypotheses about oxygen reduction possibly lacking energy conservation in some cable bacteria due to missing terminal oxidases; this is **not universally established** and should be marked uncertain unless supported by direct bioenergetic experiments. (yang2024longdistanceelectrontransport pages 1-2)
4. **Electrode reduction mechanism (direct contact vs mediator):** electrode attraction and current increases are well supported, but the mechanism remains unresolved and community co-enrichment may confound attribution; curate as assay-/application-specific and uncertain. (bonne2024interactionofliving pages 5-8)

---

# DOI-first bibliography (with URLs and publication dates)

1. **Yang T, Chavez MS, Niman CM, Xu S, El-Naggar MY.** Long-distance electron transport in multicellular freshwater cable bacteria. *eLife.* **May 2024**. DOI: **10.7554/eLife.91097**. https://doi.org/10.7554/eLife.91097 (yang2024longdistanceelectrontransport pages 1-2)
2. **Smets B, Boschker HTS, Wetherington MT, et al.** Multi-wavelength Raman microscopy of nickel-based electron transport in cable bacteria. *Frontiers in Microbiology.* **Mar 2024**. DOI: **10.3389/fmicb.2024.1208033**. https://doi.org/10.3389/fmicb.2024.1208033 (smets2024multiwavelengthramanmicroscopy pages 1-2)
3. **Hiralal A, Geelhoed JS, Neukirchen S, Meysman FJR.** Comparative genomic analysis of nickel homeostasis in cable bacteria. *BMC Genomics.* **Jul 2024**. DOI: **10.1186/s12864-024-10594-7**. https://doi.org/10.1186/s12864-024-10594-7 (hiralal2024comparativegenomicanalysis pages 1-2)
4. **van der Veen JR, Martinez SH, Wieland A, et al.** Temperature-Dependent Characterization of Long-Range Conduction in Conductive Protein Fibers of Cable Bacteria. *ACS Nano.* **Nov 2024**. DOI: **10.1021/acsnano.4c12186**. https://doi.org/10.1021/acsnano.4c12186 (veen2024temperaturedependentcharacterizationof pages 1-2)
5. **van der Veen JR, Valianti S, van der Zant HSJ, Blanter YM, Meysman FJR.** A model analysis of centimeter-long electron transport in cable bacteria. *PCCP.* **Jan 2024**. DOI: **10.1039/d3cp04466a**. https://doi.org/10.1039/d3cp04466a (veen2024amodelanalysis pages 1-2)
6. **Hiralal A, Geelhoed JS, Hidalgo-Martinez S, et al.** Closing the genome of unculturable cable bacteria using a combined metagenomic assembly of long and short sequencing reads. *Microbial Genomics.* **Feb 2024**. DOI: **10.1099/mgen.0.001197**. https://doi.org/10.1099/mgen.0.001197 (hiralal2024closingthegenome pages 9-11)
7. **Bonné R, Marshall IPG, Bjerg JJ, et al.** Interaction of living cable bacteria with carbon electrodes in bioelectrochemical systems. *Applied and Environmental Microbiology.* **Aug 2024**. DOI: **10.1128/aem.00795-24**. https://doi.org/10.1128/aem.00795-24 (bonne2024interactionofliving pages 1-2)
8. **Zhuang X, Wang S, Wu S.** Electron Transfer in the Biogeochemical Sulfur Cycle. *Life.* **May 2024**. DOI: **10.3390/life14050591**. https://doi.org/10.3390/life14050591 (zhuang2024electrontransferin pages 6-8)
9. **Bjerg JT, Boschker HTS, Larsen S, et al.** Long-distance electron transport in individual, living cable bacteria. *PNAS.* **May 2018**. DOI: **10.1073/pnas.1800367115**. https://doi.org/10.1073/pnas.1800367115 (bjerg2018longdistanceelectrontransport pages 1-2)


References

1. (yang2024longdistanceelectrontransport pages 1-2): Tingting Yang, Marko S. Chavez, Christina M. Niman, Shuai Xu, and Mohamed Y. El-Naggar. Long-distance electron transport in multicellular freshwater cable bacteria. eLife, May 2024. URL: https://doi.org/10.7554/elife.91097, doi:10.7554/elife.91097. This article has 17 citations and is from a domain leading peer-reviewed journal.

2. (bjerg2018longdistanceelectrontransport pages 1-2): Jesper T. Bjerg, Henricus T. S. Boschker, Steffen Larsen, David Berry, Markus Schmid, Diego Millo, Paula Tataru, Filip J. R. Meysman, Michael Wagner, Lars Peter Nielsen, and Andreas Schramm. Long-distance electron transport in individual, living cable bacteria. Proceedings of the National Academy of Sciences, 115:5786-5791, May 2018. URL: https://doi.org/10.1073/pnas.1800367115, doi:10.1073/pnas.1800367115. This article has 180 citations and is from a highest quality peer-reviewed journal.

3. (hiralal2024comparativegenomicanalysis pages 1-2): Anwar Hiralal, Jeanine S. Geelhoed, Sinje Neukirchen, and Filip J. R. Meysman. Comparative genomic analysis of nickel homeostasis in cable bacteria. BMC Genomics, Jul 2024. URL: https://doi.org/10.1186/s12864-024-10594-7, doi:10.1186/s12864-024-10594-7. This article has 11 citations and is from a peer-reviewed journal.

4. (bonne2024interactionofliving pages 1-2): Robin Bonné, Ian P. G. Marshall, Jesper J. Bjerg, Ugo Marzocchi, Jean Manca, Lars Peter Nielsen, and Kartik Aiyer. Interaction of living cable bacteria with carbon electrodes in bioelectrochemical systems. Aug 2024. URL: https://doi.org/10.1128/aem.00795-24, doi:10.1128/aem.00795-24. This article has 15 citations and is from a peer-reviewed journal.

5. (veen2024amodelanalysis pages 1-2): Jasper R. van der Veen, Stephanie Valianti, Herre S. J. van der Zant, Yaroslav M. Blanter, and Filip J. R. Meysman. A model analysis of centimeter-long electron transport in cable bacteria. Physical chemistry chemical physics : PCCP, 26:3139-3151, Jan 2024. URL: https://doi.org/10.1039/d3cp04466a, doi:10.1039/d3cp04466a. This article has 26 citations.

6. (yang2024longdistanceelectrontransport media fbde9623): Tingting Yang, Marko S. Chavez, Christina M. Niman, Shuai Xu, and Mohamed Y. El-Naggar. Long-distance electron transport in multicellular freshwater cable bacteria. eLife, May 2024. URL: https://doi.org/10.7554/elife.91097, doi:10.7554/elife.91097. This article has 17 citations and is from a domain leading peer-reviewed journal.

7. (smets2024multiwavelengthramanmicroscopy pages 1-2): Bent Smets, Henricus T. S. Boschker, Maxwell T. Wetherington, Gérald Lelong, Silvia Hidalgo-Martinez, Lubos Polerecky, Gert Nuyts, Karolien De Wael, and Filip J. R. Meysman. Multi-wavelength raman microscopy of nickel-based electron transport in cable bacteria. Frontiers in Microbiology, Mar 2024. URL: https://doi.org/10.3389/fmicb.2024.1208033, doi:10.3389/fmicb.2024.1208033. This article has 17 citations and is from a peer-reviewed journal.

8. (smets2024multiwavelengthramanmicroscopy pages 11-12): Bent Smets, Henricus T. S. Boschker, Maxwell T. Wetherington, Gérald Lelong, Silvia Hidalgo-Martinez, Lubos Polerecky, Gert Nuyts, Karolien De Wael, and Filip J. R. Meysman. Multi-wavelength raman microscopy of nickel-based electron transport in cable bacteria. Frontiers in Microbiology, Mar 2024. URL: https://doi.org/10.3389/fmicb.2024.1208033, doi:10.3389/fmicb.2024.1208033. This article has 17 citations and is from a peer-reviewed journal.

9. (smets2024multiwavelengthramanmicroscopy pages 10-11): Bent Smets, Henricus T. S. Boschker, Maxwell T. Wetherington, Gérald Lelong, Silvia Hidalgo-Martinez, Lubos Polerecky, Gert Nuyts, Karolien De Wael, and Filip J. R. Meysman. Multi-wavelength raman microscopy of nickel-based electron transport in cable bacteria. Frontiers in Microbiology, Mar 2024. URL: https://doi.org/10.3389/fmicb.2024.1208033, doi:10.3389/fmicb.2024.1208033. This article has 17 citations and is from a peer-reviewed journal.

10. (yang2024longdistanceelectrontransport media bc0cc273): Tingting Yang, Marko S. Chavez, Christina M. Niman, Shuai Xu, and Mohamed Y. El-Naggar. Long-distance electron transport in multicellular freshwater cable bacteria. eLife, May 2024. URL: https://doi.org/10.7554/elife.91097, doi:10.7554/elife.91097. This article has 17 citations and is from a domain leading peer-reviewed journal.

11. (veen2024temperaturedependentcharacterizationof pages 1-2): Jasper R. van der Veen, Silvia Hidalgo Martinez, Albert Wieland, Matteo De Pellegrin, Rick Verweij, Yaroslav M. Blanter, Herre S. J. van der Zant, and Filip J. R. Meysman. Temperature-dependent characterization of long-range conduction in conductive protein fibers of cable bacteria. ACS Nano, 18:32878-32889, Nov 2024. URL: https://doi.org/10.1021/acsnano.4c12186, doi:10.1021/acsnano.4c12186. This article has 17 citations and is from a highest quality peer-reviewed journal.

12. (smets2024multiwavelengthramanmicroscopy pages 12-14): Bent Smets, Henricus T. S. Boschker, Maxwell T. Wetherington, Gérald Lelong, Silvia Hidalgo-Martinez, Lubos Polerecky, Gert Nuyts, Karolien De Wael, and Filip J. R. Meysman. Multi-wavelength raman microscopy of nickel-based electron transport in cable bacteria. Frontiers in Microbiology, Mar 2024. URL: https://doi.org/10.3389/fmicb.2024.1208033, doi:10.3389/fmicb.2024.1208033. This article has 17 citations and is from a peer-reviewed journal.

13. (hiralal2024closingthegenome pages 9-11): Anwar Hiralal, Jeanine S. Geelhoed, Silvia Hidalgo-Martinez, Bent Smets, Jesper R. van Dijk, and Filip J. R. Meysman. Closing the genome of unculturable cable bacteria using a combined metagenomic assembly of long and short sequencing reads. Microbial Genomics, Feb 2024. URL: https://doi.org/10.1099/mgen.0.001197, doi:10.1099/mgen.0.001197. This article has 19 citations and is from a peer-reviewed journal.

14. (bonne2024interactionofliving pages 2-5): Robin Bonné, Ian P. G. Marshall, Jesper J. Bjerg, Ugo Marzocchi, Jean Manca, Lars Peter Nielsen, and Kartik Aiyer. Interaction of living cable bacteria with carbon electrodes in bioelectrochemical systems. Aug 2024. URL: https://doi.org/10.1128/aem.00795-24, doi:10.1128/aem.00795-24. This article has 15 citations and is from a peer-reviewed journal.

15. (bonne2024interactionofliving pages 5-8): Robin Bonné, Ian P. G. Marshall, Jesper J. Bjerg, Ugo Marzocchi, Jean Manca, Lars Peter Nielsen, and Kartik Aiyer. Interaction of living cable bacteria with carbon electrodes in bioelectrochemical systems. Aug 2024. URL: https://doi.org/10.1128/aem.00795-24, doi:10.1128/aem.00795-24. This article has 15 citations and is from a peer-reviewed journal.

16. (yang2024longdistanceelectrontransport pages 18-19): Tingting Yang, Marko S. Chavez, Christina M. Niman, Shuai Xu, and Mohamed Y. El-Naggar. Long-distance electron transport in multicellular freshwater cable bacteria. eLife, May 2024. URL: https://doi.org/10.7554/elife.91097, doi:10.7554/elife.91097. This article has 17 citations and is from a domain leading peer-reviewed journal.

17. (zhuang2024electrontransferin pages 15-16): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 22 citations.

18. (zhuang2024electrontransferin pages 6-8): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 22 citations.

19. (hiralal2024comparativegenomicanalysis pages 5-7): Anwar Hiralal, Jeanine S. Geelhoed, Sinje Neukirchen, and Filip J. R. Meysman. Comparative genomic analysis of nickel homeostasis in cable bacteria. BMC Genomics, Jul 2024. URL: https://doi.org/10.1186/s12864-024-10594-7, doi:10.1186/s12864-024-10594-7. This article has 11 citations and is from a peer-reviewed journal.

20. (hiralal2024closingthegenome pages 11-13): Anwar Hiralal, Jeanine S. Geelhoed, Silvia Hidalgo-Martinez, Bent Smets, Jesper R. van Dijk, and Filip J. R. Meysman. Closing the genome of unculturable cable bacteria using a combined metagenomic assembly of long and short sequencing reads. Microbial Genomics, Feb 2024. URL: https://doi.org/10.1099/mgen.0.001197, doi:10.1099/mgen.0.001197. This article has 19 citations and is from a peer-reviewed journal.

21. (smets2024multiwavelengthraman pages 13-14): B Smets, HTS Boschker, MT Wetherington, and G Lelong. Multi-wavelength raman. Unknown journal, 2024.

22. (smets2024multiwavelengthraman pages 11-12): B Smets, HTS Boschker, MT Wetherington, and G Lelong. Multi-wavelength raman. Unknown journal, 2024.

23. (yang2024longdistanceelectrontransport media 0ac9c07e): Tingting Yang, Marko S. Chavez, Christina M. Niman, Shuai Xu, and Mohamed Y. El-Naggar. Long-distance electron transport in multicellular freshwater cable bacteria. eLife, May 2024. URL: https://doi.org/10.7554/elife.91097, doi:10.7554/elife.91097. This article has 17 citations and is from a domain leading peer-reviewed journal.