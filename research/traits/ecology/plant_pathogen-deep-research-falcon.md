---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:36:10.096040'
end_time: '2026-08-03T23:43:47.719851'
duration_seconds: 457.62
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: plant pathogen
  trait_identifier: METPO:1004003
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: plant_pathogen
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pathogen that infects organisms in the kingdom Viridiplantae.
  parent_traits: METPO:1004000
  synonyms: ''
  evidence_summary: 'DOI:10.1146/annurev.phyto.43.040204.135923: type III secretion
    (Plant-pathology review supports type III secretion of effectors as the central
    mechanism by which bacterial plant pathogens manipulate plant cells.) | DOI:10.1146/annurev.micro.55.1.535:
    cell-wall-degrading enzymes (Plant-pathogen review supports secreted plant-cell-wall-degrading
    enzymes as essential virulence factors of bacterial phytopathogens.)'
  causal_graph_summary: 'plant_pathogen_t3ss_effector_program: 13 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** plant pathogen
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1004003
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pathogen that infects organisms in the kingdom Viridiplantae.
- **Parent traits:** METPO:1004000
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.phyto.43.040204.135923: type III secretion (Plant-pathology review supports type III secretion of effectors as the central mechanism by which bacterial plant pathogens manipulate plant cells.) | DOI:10.1146/annurev.micro.55.1.535: cell-wall-degrading enzymes (Plant-pathogen review supports secreted plant-cell-wall-degrading enzymes as essential virulence factors of bacterial phytopathogens.)
- **Existing causal graph summary:** plant_pathogen_t3ss_effector_program: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **plant pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/plant_pathogen.yaml`.

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
- **Trait label:** plant pathogen
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1004003
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pathogen that infects organisms in the kingdom Viridiplantae.
- **Parent traits:** METPO:1004000
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.phyto.43.040204.135923: type III secretion (Plant-pathology review supports type III secretion of effectors as the central mechanism by which bacterial plant pathogens manipulate plant cells.) | DOI:10.1146/annurev.micro.55.1.535: cell-wall-degrading enzymes (Plant-pathogen review supports secreted plant-cell-wall-degrading enzymes as essential virulence factors of bacterial phytopathogens.)
- **Existing causal graph summary:** plant_pathogen_t3ss_effector_program: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **plant pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/plant_pathogen.yaml`.

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


# Curation report: microbial **plant pathogen** trait

## 1. Scope summary

**Target trait:** `METPO:1004003`  
**Label:** plant pathogen  
**Category:** ECOLOGY  
**Term kind:** CLASS  
**Mapping status:** REVIEWED  
**Definition:** “A pathogen that infects organisms in the kingdom Viridiplantae.”  
**Parent:** `METPO:1004000`

### Recommended interpretation

`METPO:1004003` should represent an **organism-level, host- and context-dependent capacity to enter or colonize a Viridiplantae host, overcome or exploit host defenses, multiply in planta, and produce disease or transmissible infection**. It is not equivalent to possession of any single virulence gene. Plant pathogenicity is normally realized through a sequence of modules—environmental sensing, surface survival, entry, adhesion, nutrient acquisition, immune manipulation, tissue damage, multiplication, and dissemination—whose relative importance differs among bacterial, fungal, oomycete, phytoplasma, and protist pathogens.

The current 13-node T3SS-effector graph captures a major **bacterial hemibiotroph** mechanism, but it is not an adequate universal definition. Hrp T3SSs inject many effectors and are central in numerous Gram-negative bacterial phytopathogens, whereas fungal and oomycete pathogens commonly use secreted effectors and specialized penetration or feeding structures. Even within bacteria, soft-rot pathogens can depend more strongly on type II-secreted plant-cell-wall-degrading enzymes than on the canonical T3SS program. (o’malley2021regulationofthe pages 1-2, pfeilmeier2016bacterialpathogenesisof pages 7-8, santosbriones2024algorithmsforeffector pages 2-4, leivamora2024uncoveringthemechanisms pages 2-4)

### Boundary cases

* **Commensal, epiphytic, rhizosphere, and endophytic colonizers are not plant pathogens** unless there is evidence of disease-producing infection under an appropriate host and environment.
* **Virulence is not identical to pathogenicity.** Pathogenicity is the qualitative capacity to cause disease; virulence is its degree in a specified host, genotype, inoculum, environment, and assay.
* **Avirulence effectors are context-dependent.** An effector may promote susceptibility in one host but trigger resistance and hypersensitive cell death when recognized by the corresponding plant immune receptor.
* **Presence of a T3SS, T6SS, effector-like sequence, cell-wall-degrading enzyme, flagellum, siderophore, or biofilm locus is insufficient by itself.** These systems also occur in nonpathogenic plant-associated microbes.
* **Direct infiltration bypasses natural entry.** Flagellar mutants of *Pseudomonas syringae* and *Ralstonia solanacearum* are impaired following inoculation onto intact surfaces but not necessarily after direct infiltration; therefore, such results support an entry-stage edge rather than a universal intracellular virulence edge. (pfeilmeier2016bacterialpathogenesisof pages 7-8)
* **Latent or opportunistic disease requires metadata.** Host species and genotype, tissue, developmental state, inoculation route, dose, temperature, humidity, wounding, and disease endpoint should accompany evidence.
* **“Plant pathogen” should be assigned to the microbial entity, not to an isolated protein.** Proteins and pathways are mechanistic contributors to the terminal trait.

## 2. Current mechanistic model

A defensible cross-taxon causal architecture is:

**plant/environmental cues → virulence-program activation → access and attachment → host-barrier penetration → effector/toxin/enzyme deployment → defense suppression or tissue damage → in-planta multiplication and spread → `METPO:1004003`**.

In *P. syringae*, low nitrogen-to-carbon conditions, acidic pH, and plant-derived metabolites induce the Hrp program. Citric acid, aspartate, glutamate, and fructose-associated signals can strongly induce T3SS genes; plant signals produced approximately tenfold enhancement in the reviewed experiments. The AauSR two-component system and AatQMP transporter connect acidic-amino-acid perception to Hrp regulation. These observations are strong but species- and assay-specific. (o’malley2021regulationofthe pages 5-6, o’malley2021regulationofthe pages 15-17)

The Hrp injectisome then delivers effectors into the plant cytosol. A reviewed *P. syringae* system delivers more than 20 effectors, which collectively inhibit immune signaling or disrupt cell-surface immune-receptor functions. HrpRS and the alternative sigma factor HrpL are major regulatory nodes. (o’malley2021regulationofthe pages 1-2)

## 3. Candidate nodes grouped by type

### A. Trait and host-context nodes

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| plant pathogen | Trait class | `METPO:1004003` | Terminal trait; quote identifier verbatim in YAML. |
| Viridiplantae host | Taxon/context | `NCBITaxon:33090` | Verify that TraitMech accepts host-taxon nodes before use. |
| intact plant surface | Environment/anatomical context | Label only | Important for natural-entry assays. |
| plant apoplast | Cellular/extracellular compartment | GO label candidate; identifier should be ontology-validated | Principal niche for many bacterial phytopathogens. |
| xylem | Plant anatomical niche | Plant Ontology candidate; validate identifier | Relevant to vascular pathogens such as *Ralstonia* and *Xanthomonas* lineages. |
| acidic, nutrient-limited plant environment | Experimental/environmental factor | Label only | Do not model as universally required. |

### B. Regulatory and sensory modules

* Plant-derived citric acid, aspartate, glutamate, fructose, and related host metabolites.
* AauSR two-component system; AatQMP ABC transporter.
* HrpRS–HrpL regulatory cascade.
* Cyclic di-GMP: a context-dependent switch inversely coordinating T3SS expression and flagellar motility in the reviewed *P. syringae* systems. (o’malley2021regulationofthe pages 15-17)
* Quorum sensing, diffusible signal factor signaling, and quorum quenching should remain **taxon-specific extension nodes** until direct phytopathogen evidence is attached; generic pathogen or biofilm reviews are not adequate evidence for `METPO:1004003`.

### C. Access, attachment, and infection structures

* Bacterial flagellum and flagellar motility—candidate grounding `GO:0009288` for “bacterial-type flagellum”; validate the exact relation to the motility process.
* Chemotaxis—label or validated GO process.
* Type IV pilus; surface attachment; biofilm formation.
* Appressorium; penetration peg; mechanical turgor pressure.
* Haustorium; nutrient-extraction interface; effector-delivery interface.

Flagella support early entry from intact plant surfaces, while type IV pili support attachment, biofilm formation, and virulence in examined *P. syringae* and *R. solanacearum* systems. In biotrophic fungi, melanized appressoria and penetration pegs combine pressure with cutinase, cellulase, pectinase, xylanase, and protease activities, whereas haustoria provide specialized nutrient and host-interaction interfaces. (pfeilmeier2016bacterialpathogenesisof pages 7-8, leivamora2024uncoveringthemechanisms pages 2-4)

### D. Secretion systems and exported cargo

* Hrp type III secretion system/injectisome—`GO:0030254` is a candidate for the type III secretion process, subject to ontology validation.
* T3SS translocon and HrpA1 pilus.
* Type III effectors, including taxon-specific Avr/Hop families.
* Type II secretion system.
* Pectinases, cellulases, pectin esterases, endoglucanases, xylanases, cutinases, proteases, and other plant-cell-wall-degrading enzymes.
* Type VI secretion system, Hcp, and T6SS effectors—retain outside the core graph pending stronger plant-directed evidence.
* Secreted fungal and oomycete effectors.

### E. Host targets and outcomes

* Pattern-recognition receptors and pattern-triggered immunity.
* Salicylic-acid and jasmonic-acid defense pathways.
* Reactive-oxygen-species burst and antioxidant defenses.
* Callose deposition and defense-related vesicle transport.
* Plant cell wall, middle lamella, and plasma membrane.
* Stomatal immunity.
* Apoplastic multiplication, tissue maceration, necrosis, nutrient release, vascular colonization, and systemic spread.

Named fungal examples include TalSP, TaNUDX23, PstGSRE4, and *Ustilago maydis* Pep1. The reviewed mechanisms include interference with PRRs, callose, salicylic-acid metabolism, vesicle traffic, and ROS. Catalase and superoxide dismutase activities can neutralize host ROS. These named edges should be represented as lineage-specific subgraphs rather than universal fungal-pathogen requirements. (leivamora2024uncoveringthemechanisms pages 4-5)

Cross-kingdom convergence is mechanistically informative: *U. maydis* Cmu1 diverts chorismate-related salicylic-acid biosynthesis, while *Verticillium dahliae* VdIsc1 and *Phytophthora sojae* PsIsc1 use isochorismatase activity to reduce host salicylic acid. The bacterial HopI1 effector likewise reduces salicylic acid through chloroplast perturbation. (santosbriones2024algorithmsforeffector pages 1-2)

## 4. Candidate causal edges

The following table is a compact graph-design overview.

| subject | predicate | object | scope/taxon | confidence | suggested grounding |
|---|---|---|---|---|---|
| plant-derived organic acids and amino acids | induce | HrpRS/HrpL-regulated Hrp T3SS expression | Bacterial phytopathogens; strongest direct evidence in *Pseudomonas syringae*; host-signal regulation is taxon-tested, not universalized (o’malley2021regulationofthe pages 5-6, o’malley2021regulationofthe pages 1-2, o’malley2021regulationofthe pages 15-17) | high | subject: label-only candidate; object: Hrp T3SS / GO:0030254 candidate for type III secretion process |
| Hrp type III secretion system | translocates | effector proteins into plant cells | Bacterial phytopathogens broadly; classic Hrp T3SS model (o’malley2021regulationofthe pages 1-2, santosbriones2024algorithmsforeffector pages 2-4) | high | subject: Hrp T3SS / GO:0030254 candidate; object: type III effector proteins (label-only candidate) |
| type III effector proteins | suppress | plant immunity | Bacterial phytopathogens broadly; includes inhibition of immune signaling and disruption of cell-surface immune receptors (o’malley2021regulationofthe pages 1-2, santosbriones2024algorithmsforeffector pages 2-4) | high | subject: type III effector proteins (label-only candidate); object: plant immunity / defense response (label-only candidate) |
| bacterial-type flagellum / flagellar motility | enables | entry from intact plant surface | Strongest evidence in *Ralstonia solanacearum* and *Pseudomonas syringae*; surface inoculation context-specific (pfeilmeier2016bacterialpathogenesisof pages 7-8) | high | subject: GO:0009288; object: plant surface entry (label-only candidate) |
| type IV pili | promote | attachment and biofilm formation | Strongest evidence in *P. syringae* and *R. solanacearum*; relevant to early colonization (pfeilmeier2016bacterialpathogenesisof pages 7-8) | moderate-high | subject: type IV pili (label-only candidate); object: attachment / biofilm formation (label-only candidate) |
| type II secretion system | secretes | plant-cell-wall-degrading enzymes | Bacterial phytopathogens broadly; foundational phytopathogen mechanism (pfeilmeier2016bacterialpathogenesisof pages 7-8) | high | subject: type II secretion system (label-only candidate); object: plant-cell-wall-degrading enzymes (label-only candidate) |
| plant-cell-wall-degrading enzymes | promote | apoplastic/tissue spread | Bacterial phytopathogens broadly; supports connective lamella/structural breakdown and spread (pfeilmeier2016bacterialpathogenesisof pages 7-8) | high | subject: plant-cell-wall-degrading enzymes (label-only candidate); object: apoplastic spread / tissue maceration (label-only candidate) |
| coronatine and related phytotoxins | suppress | stomatal and salicylic-acid-associated defenses | Strong for selected bacterial phytopathogens including *P. syringae* pathovars; not universal across all plant pathogens (pfeilmeier2016bacterialpathogenesisof pages 7-8) | moderate-high | subject: coronatine / phytotoxins (label-only candidate); object: stomatal defense; SA defense (label-only candidates) |
| appressorium | enables | host penetration | Biotrophic fungi; review-level generalization across fungal pathogens (leivamora2024uncoveringthemechanisms pages 2-4) | high | subject: appressorium (label-only candidate); object: host penetration (label-only candidate) |
| haustorium | enables | nutrient extraction and effector-host interface | Biotrophic fungi; specialized infection structure (leivamora2024uncoveringthemechanisms pages 2-4) | high | subject: haustorium (label-only candidate); object: nutrient extraction / effector interface (label-only candidates) |
| fungal secreted effectors | suppress | salicylic acid, jasmonic acid, ROS, and PRR-linked defenses | Biotrophic fungi broadly; named effectors support multiple submechanisms but remain lineage-specific in details (leivamora2024uncoveringthemechanisms pages 4-5, leivamora2024uncoveringthemechanisms pages 2-4, santosbriones2024algorithmsforeffector pages 1-2, leivamora2024uncoveringthemechanisms pages 23-25) | high | subject: fungal effector proteins (label-only candidate); object: SA defense / JA defense / ROS burst / PRR signaling (label-only candidates) |
| T6SS | may affect | plant cells or plant-directed virulence | Plant-pathogenic bacteria; evidence currently prediction-heavy and incomplete, with authors calling for biochemical confirmation; not for core graph (matte2024t6ssinplant pages 5-7) | low / uncertain | subject: type VI secretion system (label-only candidate); object: plant-directed virulence (label-only candidate) |
| plant pathogen trait | realized by | successful deployment of adhesion, entry, secretion, toxin, and effector programs in planta | Cross-kingdom summary edge for METPO trait; integrative and inferred from multiple mechanisms, not a single direct assay edge (o’malley2021regulationofthe pages 1-2, pfeilmeier2016bacterialpathogenesisof pages 7-8, leivamora2024uncoveringthemechanisms pages 2-4) | moderate | object: METPO:1004003 |


*Table: This table compiles the strongest curation-ready causal edges for the microbial trait plant pathogen (METPO:1004003), emphasizing broadly supported mechanisms and clearly flagging uncertain T6SS-related claims. It is designed to help prioritize edges for TraitMech graph construction while keeping ontology grounding conservative.*

### Evidence table with source snippets

| # | Subject–predicate–object triple | Supporting source wording or close excerpt | Reference | Interpretation and curation status |
|---:|---|---|---|---|
| 1 | plant-derived aspartate/glutamate → **induces** → Hrp T3SS expression | “specific plant-derived amino acids and organic acids…induce T3SS-encoding genes”; fructose is required for maximal induction | O’Malley & Anderson, 2021 | **Curate as taxon-specific.** Strong for *P. syringae*; do not state that every plant pathogen senses these metabolites. (o’malley2021regulationofthe pages 5-6, o’malley2021regulationofthe pages 15-17) |
| 2 | AauSR–AatQMP sensory module → **activates** → T3SS-gene regulation | AauSR “transduces acidic amino acid signals via the AatQMP ABC transporter to regulate T3SS genes” | O’Malley & Anderson, 2021 | **Curate only in a *P. syringae* branch.** Direct mechanistic regulatory edge. (o’malley2021regulationofthe pages 15-17) |
| 3 | HrpRS/HrpL → **positively regulates** → T3SS deployment | HrpRS and HrpL are described as master regulators encoded in the T3SS pathogenicity island | O’Malley & Anderson, 2021 | **High-confidence bacterial edge**, but taxonomic distribution must be recorded. (o’malley2021regulationofthe pages 1-2) |
| 4 | Hrp T3SS → **translocates** → effector proteins into plant cytosol | The T3SS is a “syringe-like translocon” delivering more than 20 effectors directly into host cytosol | O’Malley & Anderson, 2021 | **Core edge for the existing bacterial program.** The number is system-specific, not a class requirement. (o’malley2021regulationofthe pages 1-2) |
| 5 | T3SS effectors → **suppresses/disrupts** → plant immune signaling and immune-receptor function | Effectors “suppress host immune responses by inhibiting immune signaling and disrupting plant cell-surface immune receptors” | O’Malley & Anderson, 2021 | **Core causal edge.** Keep the object broad unless a named effector–target experiment is cited. (o’malley2021regulationofthe pages 1-2) |
| 6 | Hrp T3SS and its collective effectors → **promotes** → bacterial pathogenicity/in-planta growth | hrp genes encode the T3SS and are required for disease establishment; effector ensembles are collectively important for pathogenicity | Santos-Briones et al., 2024 | **High-confidence review-level edge.** Avoid claiming that every individual effector is necessary. (santosbriones2024algorithmsforeffector pages 2-4) |
| 7 | bacterial flagellar motility → **enables** → natural entry from intact plant surface | Flagellar-gene deletions compromise infection from intact surfaces but not after direct infiltration | Pfeilmeier et al., 2016 | **Curate with assay qualifier.** This is an entry edge, not proof that flagella universally increase growth after entry. (pfeilmeier2016bacterialpathogenesisof pages 7-8) |
| 8 | type IV pili → **promotes** → attachment and biofilm formation | Type IV pili are required for “biofilm formation, attachment, and virulence” in examined *Pseudomonas* and *Ralstonia* systems | Pfeilmeier et al., 2016 | **Moderate-to-high confidence; taxon-specific.** Biofilm alone is not diagnostic of pathogenicity. (pfeilmeier2016bacterialpathogenesisof pages 7-8) |
| 9 | type II secretion system → **secretes** → plant-cell-wall-degrading enzymes | T2SS releases enzymes that degrade structural molecules and connective lamellae | Pfeilmeier et al., 2016 | **Core alternative bacterial module.** Especially relevant to soft-rot and tissue-macerating pathogens. (pfeilmeier2016bacterialpathogenesisof pages 7-8) |
| 10 | plant-cell-wall-degrading enzymes → **facilitates** → tissue/apoplastic spread | Enzymatic breakdown of structural molecules and connective lamellae facilitates apoplastic spread | Pfeilmeier et al., 2016 | **High-confidence functional edge.** Use enzyme-family or EC-level nodes only when a source identifies the enzyme. (pfeilmeier2016bacterialpathogenesisof pages 7-8) |
| 11 | coronatine/syringolin-associated phytotoxin program → **overcomes** → stomatal or salicylic-acid-associated immunity | Coronatine and syringolin A are described as overcoming stomatal immunity through interference with NPR1-dependent salicylic-acid signaling | Pfeilmeier et al., 2016 | **Taxon- and toxin-specific.** Split coronatine and syringolin edges when primary references are added. (pfeilmeier2016bacterialpathogenesisof pages 7-8) |
| 12 | syringomycin/syringopeptin → **forms pores in** → plant plasma membrane | Lipodepsipeptides “form pores in plant cell membranes causing tissue necrosis” | Pfeilmeier et al., 2016 | **Curatable in a *P. syringae* toxin branch**, not in the universal core. (pfeilmeier2016bacterialpathogenesisof pages 7-8) |
| 13 | fungal appressorium/penetration peg → **enables** → host-wall penetration | Appressoria and penetration pegs combine “mechanical turgor pressure and enzymatic activity” to breach host barriers | Leiva-Mora et al., 2024 | **Review-supported fungal edge.** Applicability varies by fungal lifestyle. (leivamora2024uncoveringthemechanisms pages 2-4) |
| 14 | fungal haustorium → **enables** → nutrient extraction and intimate host interaction | Haustoria are described as specialized infection structures enabling nutrient extraction | Leiva-Mora et al., 2024 | **Curate for biotrophs only.** Not applicable to all fungal pathogens. (leivamora2024uncoveringthemechanisms pages 2-4) |
| 15 | fungal secreted effectors → **suppresses** → PRR, callose, SA/JA, vesicle, or ROS defenses | Named effectors inhibit callose, alter salicylic-acid pathways, disrupt PRRs or vesicle transport, and neutralize ROS | Leiva-Mora et al., 2024 | **Curate as several named, lineage-specific edges**, not one universal mandatory chain. (leivamora2024uncoveringthemechanisms pages 4-5, leivamora2024uncoveringthemechanisms pages 2-4) |
| 16 | Cmu1/VdIsc1/PsIsc1 → **reduces** → host salicylic acid | Cmu1 interferes with chorismate-dependent SA synthesis; VdIsc1 and PsIsc1 lower SA through isochorismatase activity | Santos-Briones et al., 2024 | **Strong mechanistic candidates**, but retrieve the underlying primary studies before final production curation. (santosbriones2024algorithmsforeffector pages 1-2) |
| 17 | T6SS → **promotes** → intermicrobial competition during plant colonization | Plant pathogens deploy T6SSs during colonization; *P. syringae* competition associated with Hcp is reported | Matte et al., 2024 | **Uncertain as a trait-defining edge.** Competition may support colonization but does not establish plant-cell attack. (matte2024t6ssinplant pages 5-7) |
| 18 | predicted T6SS pectinase/lipase/nuclease cargo → **damages** → plant wall, membrane, or nucleic acid | Candidate enzymes are largely predicted; plant delivery and biochemical activity often remain unconfirmed | Matte et al., 2024 | **Do not curate as established causality.** Preserve as hypotheses with `uncertain: true` only if TraitMech stores prospective edges. (matte2024t6ssinplant pages 5-7) |

## 5. Recent developments, applications, and expert analysis

### Effectoromics and computational discovery

A 2024 review separates translocated bacterial/oomycete effectors from conventionally secreted fungal, phytoplasma, nematode, and insect effectors. Because effectors can be poorly conserved in primary sequence, current prediction is moving toward combinations of secretion features, short linear motifs, protein domains, structural similarity, and three-dimensional models. This supports a practical pipeline of **prediction → secretion/translocation assay → host-target assay → mutant/complementation test → plant disease assay**. Predictions alone should never create positive causal edges in TraitMech. (santosbriones2024algorithmsforeffector pages 1-2)

The same literature shows convergent targeting of salicylic-acid metabolism by sequence-divergent bacterial, fungal, and oomycete effectors. This favors representing host-defense processes as reusable graph nodes connected to taxon-specific effector modules rather than forcing all pathogens into one homologous-effector architecture. (santosbriones2024algorithmsforeffector pages 1-2)

### Resistance breeding and surveillance

Effector repertoires and cognate plant receptors are used in resistance-gene discovery, effector-assisted screening, and deployment of cultivar resistance. However, an effector can be a virulence determinant in a susceptible plant and an avirulence determinant in a resistant genotype. Graph records therefore need a host-genotype qualifier and should distinguish **suppresses immunity** from **is recognized by immune receptor and activates defense**.

### Anti-virulence and biological control

Mechanistic nodes create intervention points: inhibit Hrp regulation or secretion, block effector activity, inhibit cell-wall-degrading enzymes, quench quorum signals in taxa where quorum control is experimentally demonstrated, compete for iron, disrupt attachment/biofilm formation, or deploy antagonists that exploit intermicrobial competition. These are applications of the graph, but intervention efficacy should not be inferred from pathway presence alone.

T6SS research is particularly instructive. A 2024 expert review notes that approximately one quarter of Gram-negative bacteria encode a T6SS and that these systems are enriched in Proteobacteria, including important phytopathogens. Nevertheless, many proposed plant-directed pectinases, phospholipases, and nucleases remain bioinformatically predicted, and delivery across the plant wall or activity in plant cells has not been established. The expert conclusion is therefore that T6SS-mediated microbial competition is better supported than direct plant-cell intoxication. (matte2024t6ssinplant pages 5-7)

### Quantitative evidence available from the retrieved mechanistic literature

* The reviewed *P. syringae* T3SS can deliver **more than 20 distinct effectors** into host cells. This is a system-specific repertoire statistic, not a threshold for the trait. (o’malley2021regulationofthe pages 1-2)
* Plant-derived signals produced an approximately **tenfold increase** in T3SS-gene expression in the reviewed assays. This supports inducible environmental control rather than constitutive expression. (o’malley2021regulationofthe pages 5-6)
* T6SS genes are estimated to occur in roughly **one quarter of Gram-negative bacteria**, demonstrating why T6SS presence lacks specificity for plant pathogenicity. (matte2024t6ssinplant pages 5-7)

Global crop-loss figures were not used as graph evidence because such estimates aggregate fungi, oomycetes, bacteria, viruses, pests, post-harvest losses, and abiotic stress under differing definitions. They should be retained as report-level context, not converted into organism-level causal edges.

## 6. Ontology-grounding recommendations

1. Use `METPO:1004003` only for the terminal organism trait.
2. Use `NCBITaxon:33090` for Viridiplantae only after confirming the repository’s taxon-prefix conventions.
3. Candidate GO terms such as `GO:0030254` and `GO:0009288` must be checked against the current ontology release before commit. A process term should not be substituted for a cellular component or vice versa.
4. Ground chemicals such as citrate, aspartate, glutamate, fructose, salicylic acid, jasmonic acid, and cyclic di-GMP to current ChEBI records only after identifier validation. No unverified ChEBI CURIE should be inserted.
5. Ground individual enzymes to EC, Rhea, UniProt, or GO only when the source identifies the catalytic activity or protein unambiguously. “Pectinase” and “cellulase” are functional umbrellas, not single enzymes.
6. Preserve strain-level identity for effectors. Names such as HopI1, Cmu1, VdIsc1, PsIsc1, TalSP, TaNUDX23, and Pep1 should be tied to taxon and, where possible, a reviewed UniProt accession.
7. Label-only nodes are preferable to invented or semantically approximate identifiers.

## 7. Recommended YAML architecture

Rather than expanding one linear T3SS graph into a purported universal pathway, use a modular structure:

* `plant_pathogen_environmental_sensing`
* `plant_pathogen_surface_entry_attachment`
* `plant_pathogen_t3ss_effector_program` — retain the existing 13-node graph
* `plant_pathogen_t2ss_pcwde_program`
* `plant_pathogen_phytotoxin_program`
* `plant_pathogen_fungal_penetration_effector_program`
* `plant_pathogen_oomycete_effector_program`
* `plant_pathogen_intermicrobial_competition` — provisional; T6SS claims carefully qualified

Each module should converge only after an experimentally demonstrated phenotype such as increased in-planta population, lesion formation, wilting, tissue maceration, systemic movement, or reduced disease following gene deletion with restoration by complementation.

## 8. Claims not yet safe to curate

1. **T6SS directly injects predicted pectinases, phospholipases, or nucleases into plant cells.** Most reviewed candidates lack delivery and biochemical validation. (matte2024t6ssinplant pages 5-7)
2. **Every plant pathogen requires a T3SS.** This excludes Gram-positive bacteria, phytoplasmas, fungi, oomycetes, and T3SS-independent bacterial strategies.
3. **T3SS presence predicts pathogenicity.** Secretion machinery without the correct effector repertoire, regulation, host access, and susceptible host context is insufficient.
4. **Biofilm formation or flagellar motility is specific to plant pathogens.** Both are widespread microbial traits; direct infiltration can erase the apparent requirement for motility. (pfeilmeier2016bacterialpathogenesisof pages 7-8)
5. **A predicted effector is a validated virulence factor.** Sequence or structure prediction must be followed by experimental secretion/translocation and disease evidence. (santosbriones2024algorithmsforeffector pages 1-2)
6. **All fungal pathogens form appressoria or haustoria.** These structures are lifestyle- and lineage-dependent. (leivamora2024uncoveringthemechanisms pages 2-4)
7. **A named effector always suppresses immunity.** The same molecule may activate effector-triggered immunity in a resistant genotype.
8. **Cross-kingdom small-RNA silencing should be added as a general plant-pathogen mechanism.** The retrieved evidence did not provide a sufficiently direct, primary mechanistic chain for broad TraitMech curation.
9. **Quorum sensing, siderophore uptake, exopolysaccharide production, or DSF signaling should be universal core nodes.** These are promising lineage-specific extensions, but the retrieved plant-pathogen evidence was not sufficiently direct for universal edges.
10. **Climate change causes the trait.** Climate can alter host susceptibility, pathogen ranges, and disease severity, but it is an epidemiological modifier rather than the defining molecular mechanism of `METPO:1004003`.

## 9. DOI-first bibliography

1. O’Malley MR, Anderson JC. **Regulation of the *Pseudomonas syringae* Type III Secretion System by Host Environment Signals.** *Microorganisms*. Published June 2021;9:1227. DOI: [10.3390/microorganisms9061227](https://doi.org/10.3390/microorganisms9061227). (o’malley2021regulationofthe pages 5-6, o’malley2021regulationofthe pages 1-2, o’malley2021regulationofthe pages 15-17)
2. De los Santos-Briones C, et al. **Algorithms for Effector Prediction in Plant Pathogens and Pests: Achievements and Current Challenges.** *Microbiology Research*. Published October 2024;15:2162–2183. DOI: [10.3390/microbiolres15040145](https://doi.org/10.3390/microbiolres15040145). (santosbriones2024algorithmsforeffector pages 1-2, santosbriones2024algorithmsforeffector pages 2-4)
3. Matte LM, Genal AV, Landolt EF, Danka ES. **T6SS in plant pathogens: unique mechanisms in complex hosts.** *Infection and Immunity*. Published September 2024;92(9). DOI: [10.1128/iai.00500-23](https://doi.org/10.1128/iai.00500-23). (matte2024t6ssinplant pages 5-7)
4. Leiva-Mora M, et al. **Uncovering the Mechanisms: The Role of Biotrophic Fungi in Activating or Suppressing Plant Defense Responses.** *Journal of Fungi*. Published September 2024;10:635. DOI: [10.3390/jof10090635](https://doi.org/10.3390/jof10090635). (leivamora2024uncoveringthemechanisms pages 4-5, leivamora2024uncoveringthemechanisms pages 2-4, leivamora2024uncoveringthemechanisms pages 23-25)
5. Pfeilmeier S, Caly DL, Malone JG. **Bacterial pathogenesis of plants: future challenges from a microbial perspective.** *Molecular Plant Pathology*. Published August 2016;17:1298–1313. DOI: [10.1111/mpp.12427](https://doi.org/10.1111/mpp.12427). (pfeilmeier2016bacterialpathogenesisof pages 7-8)

## Curation conclusion

The strongest immediate expansion of `data/traits/ecology/plant_pathogen.yaml` is not a larger universal T3SS chain, but a **modular causal graph** in which host sensing, natural entry, adhesion, T3SS-mediated immune manipulation, T2SS-mediated wall degradation, phytotoxin activity, and fungal penetration/effector programs independently converge on experimentally measured in-planta disease. The T3SS and PCWDE edges are ready for careful curation; fungal appressorium/haustorium and named-effector branches are suitable with lifestyle and taxon qualifiers. Predicted T6SS plant-target effects, generic quorum-sensing claims, and computationally predicted effectors should remain explicitly uncertain until primary functional evidence is attached.

References

1. (o’malley2021regulationofthe pages 1-2): Megan R. O’Malley and Jeffrey C. Anderson. Regulation of the pseudomonas syringae type iii secretion system by host environment signals. Microorganisms, 9:1227, Jun 2021. URL: https://doi.org/10.3390/microorganisms9061227, doi:10.3390/microorganisms9061227. This article has 53 citations.

2. (pfeilmeier2016bacterialpathogenesisof pages 7-8): Sebastian Pfeilmeier, Delphine L. Caly, and Jacob G. Malone. Bacterial pathogenesis of plants: future challenges from a microbial perspective. Molecular Plant Pathology, 17:1298-1313, Aug 2016. URL: https://doi.org/10.1111/mpp.12427, doi:10.1111/mpp.12427. This article has 169 citations and is from a peer-reviewed journal.

3. (santosbriones2024algorithmsforeffector pages 2-4): César De los Santos-Briones, Karla Gisel Carreón-Anguiano, Sara E. Vila-Luna, Jewel Nicole Anna Todd, Ignacio Islas-Flores, Luis Sáenz-Carbonell, Pablo Alejandro Gamas-Trujillo, and Blondy Canto-Canché. Algorithms for effector prediction in plant pathogens and pests: achievements and current challenges. Microbiology Research, 15:2162-2183, Oct 2024. URL: https://doi.org/10.3390/microbiolres15040145, doi:10.3390/microbiolres15040145. This article has 4 citations.

4. (leivamora2024uncoveringthemechanisms pages 2-4): Michel Leiva-Mora, Yanelis Capdesuñer, Ariel Villalobos-Olivera, Roberto Moya-Jiménez, Luis Rodrigo Saa, and Marcos Edel Martínez-Montero. Uncovering the mechanisms: the role of biotrophic fungi in activating or suppressing plant defense responses. Journal of Fungi, 10:635, Sep 2024. URL: https://doi.org/10.3390/jof10090635, doi:10.3390/jof10090635. This article has 26 citations.

5. (o’malley2021regulationofthe pages 5-6): Megan R. O’Malley and Jeffrey C. Anderson. Regulation of the pseudomonas syringae type iii secretion system by host environment signals. Microorganisms, 9:1227, Jun 2021. URL: https://doi.org/10.3390/microorganisms9061227, doi:10.3390/microorganisms9061227. This article has 53 citations.

6. (o’malley2021regulationofthe pages 15-17): Megan R. O’Malley and Jeffrey C. Anderson. Regulation of the pseudomonas syringae type iii secretion system by host environment signals. Microorganisms, 9:1227, Jun 2021. URL: https://doi.org/10.3390/microorganisms9061227, doi:10.3390/microorganisms9061227. This article has 53 citations.

7. (leivamora2024uncoveringthemechanisms pages 4-5): Michel Leiva-Mora, Yanelis Capdesuñer, Ariel Villalobos-Olivera, Roberto Moya-Jiménez, Luis Rodrigo Saa, and Marcos Edel Martínez-Montero. Uncovering the mechanisms: the role of biotrophic fungi in activating or suppressing plant defense responses. Journal of Fungi, 10:635, Sep 2024. URL: https://doi.org/10.3390/jof10090635, doi:10.3390/jof10090635. This article has 26 citations.

8. (santosbriones2024algorithmsforeffector pages 1-2): César De los Santos-Briones, Karla Gisel Carreón-Anguiano, Sara E. Vila-Luna, Jewel Nicole Anna Todd, Ignacio Islas-Flores, Luis Sáenz-Carbonell, Pablo Alejandro Gamas-Trujillo, and Blondy Canto-Canché. Algorithms for effector prediction in plant pathogens and pests: achievements and current challenges. Microbiology Research, 15:2162-2183, Oct 2024. URL: https://doi.org/10.3390/microbiolres15040145, doi:10.3390/microbiolres15040145. This article has 4 citations.

9. (leivamora2024uncoveringthemechanisms pages 23-25): Michel Leiva-Mora, Yanelis Capdesuñer, Ariel Villalobos-Olivera, Roberto Moya-Jiménez, Luis Rodrigo Saa, and Marcos Edel Martínez-Montero. Uncovering the mechanisms: the role of biotrophic fungi in activating or suppressing plant defense responses. Journal of Fungi, 10:635, Sep 2024. URL: https://doi.org/10.3390/jof10090635, doi:10.3390/jof10090635. This article has 26 citations.

10. (matte2024t6ssinplant pages 5-7): Lexie M. Matte, Abigail V. Genal, Emily F. Landolt, and Elizabeth S. Danka. T6ss in plant pathogens: unique mechanisms in complex hosts. Infection and Immunity, Sep 2024. URL: https://doi.org/10.1128/iai.00500-23, doi:10.1128/iai.00500-23. This article has 18 citations and is from a peer-reviewed journal.