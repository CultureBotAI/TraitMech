---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:57:35.040043'
end_time: '2026-08-04T06:07:37.865426'
duration_seconds: 602.83
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: dissimilatory metal reduction
  trait_identifier: traitmech:000039
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: dissimilatory_metal_reduction
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An anaerobic respiratory metabolism in which an organism conserves energy
    for growth by coupling the oxidation of organic matter or hydrogen to the reduction
    of a metal (e.g. Fe(III), Mn(IV)) as a terminal electron acceptor.
  parent_traits: METPO:1000802
  synonyms: dissimilatory metal-ion reduction
  evidence_summary: 'DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter
    coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical
    reactions in aquatic sediments, soils, and groundwater (Lovley review establishes
    dissimilatory metal (Fe(III)/Mn(IV)) reduction as energy-conserving anaerobic
    respiration; parent of the metal-specific reduction sub-variants.) | PMID:7826009:  (Nealson
    & Saffarini, "Iron and manganese in anaerobic respiration", supports metals as
    terminal electron acceptors in anaerobic respiration.)'
  causal_graph_summary: 'metal_reduction_anaerobic_respiration: 10 nodes, 7 edges'
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
- **Trait label:** dissimilatory metal reduction
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000039
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy for growth by coupling the oxidation of organic matter or hydrogen to the reduction of a metal (e.g. Fe(III), Mn(IV)) as a terminal electron acceptor.
- **Parent traits:** METPO:1000802
- **Synonyms:** dissimilatory metal-ion reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical reactions in aquatic sediments, soils, and groundwater (Lovley review establishes dissimilatory metal (Fe(III)/Mn(IV)) reduction as energy-conserving anaerobic respiration; parent of the metal-specific reduction sub-variants.) | PMID:7826009:  (Nealson & Saffarini, "Iron and manganese in anaerobic respiration", supports metals as terminal electron acceptors in anaerobic respiration.)
- **Existing causal graph summary:** metal_reduction_anaerobic_respiration: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **dissimilatory metal reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_metal_reduction.yaml`.

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
- **Trait label:** dissimilatory metal reduction
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000039
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy for growth by coupling the oxidation of organic matter or hydrogen to the reduction of a metal (e.g. Fe(III), Mn(IV)) as a terminal electron acceptor.
- **Parent traits:** METPO:1000802
- **Synonyms:** dissimilatory metal-ion reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical reactions in aquatic sediments, soils, and groundwater (Lovley review establishes dissimilatory metal (Fe(III)/Mn(IV)) reduction as energy-conserving anaerobic respiration; parent of the metal-specific reduction sub-variants.) | PMID:7826009:  (Nealson & Saffarini, "Iron and manganese in anaerobic respiration", supports metals as terminal electron acceptors in anaerobic respiration.)
- **Existing causal graph summary:** metal_reduction_anaerobic_respiration: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **dissimilatory metal reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_metal_reduction.yaml`.

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


# Curation report: dissimilatory metal reduction

## Trait record and scope

- **Trait:** dissimilatory metal reduction
- **Identifier:** `traitmech:000039`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `METPO:1000802`
- **Synonym:** dissimilatory metal-ion reduction

### Operational definition

This trait is an **energy-conserving anaerobic respiratory capacity** in which oxidation of an electron donor—commonly organic carbon, H₂, or formate—is coupled to reduction of a metal or metal-bearing mineral serving as terminal electron acceptor. The canonical phenotypes are Fe(III) and Mn(IV) respiration, usually assayed as donor-dependent growth, disappearance of Fe(III)/Mn(IV), accumulation of Fe(II)/Mn(II), or transformation of the starting mineral. Foundational reviews distinguish this growth-supporting process from metal-resistance reactions that change metal oxidation state but do not support anaerobic growth (lloyd2003microbialreductionof pages 1-2).

The trait should not imply one universal molecular pathway. Insoluble acceptors often require extracellular electron transfer (EET), but lineages use different conduits. *Shewanella oneidensis* MR-1 uses the Mtr porin–cytochrome pathway, whereas *Geobacter sulfurreducens* uses multiple porin–cytochrome, outer-surface cytochrome, and filament-associated components whose relative functions vary with acceptor and assay (shi2012molecularunderpinningsof pages 1-2, jiang2023thevariedroles pages 1-2).

### Inclusion criteria

1. A metal species is the demonstrated terminal electron acceptor.
2. Reduction is coupled to anaerobic respiration, energy conservation, growth, or a validated respiratory electron-transfer chain.
3. The phenotype is supported by product formation, acceptor loss, growth/yield, electrochemical evidence tied to metal reduction, or genetic/biochemical disruption of the pathway.
4. Both soluble metal complexes and insoluble minerals may qualify. Insoluble Fe(III) oxides are extracellular at circumneutral pH and therefore require electron transfer through or beyond the envelope (shi2012molecularunderpinningsof pages 1-2).

### Boundary cases to exclude or represent separately

- **Assimilatory metal reduction:** reduction for biosynthesis rather than respiratory energy conservation.
- **Detoxification/resistance-only reduction:** for example, a reductase that lowers toxicity without supporting growth. Cr(VI) reduction is especially heterogeneous and should only be included when respiratory coupling is demonstrated (lloyd2003microbialreductionof pages 1-2, lloyd2003microbialreductionof pages 3-5).
- **Indirect abiotic reduction:** biogenic Fe(II) or sulfide can reduce another contaminant metal. This is an environmental consequence, not evidence that the organism respired the secondary metal (lloyd2003microbialreductionof pages 1-2, lloyd2003microbialreductionof pages 3-5).
- **Fe(II) oxidation:** the reverse redox trait; *Dethiobacter alkaliphilus* Z-1002 can perform both, but they require distinct graph branches (zavarzina2023ironorsulfur pages 1-2).
- **Electrode respiration or generic EET:** mechanistically related and useful as proxy assays, but an anode is not a metal terminal acceptor. Do not infer `traitmech:000039` from current generation alone.
- **Metalloid/radionuclide reduction:** arsenate, selenate, U(VI), and Tc(VII) are often discussed with metal reduction, but should be attached only if TraitMech’s intended scope explicitly includes metalloids and radionuclides and respiratory coupling is established (lloyd2003microbialreductionof pages 1-2).

## Current mechanistic model

In the best-resolved *Shewanella* model, donor oxidation reduces the membrane quinone pool. Inner-membrane tetraheme cytochrome CymA oxidizes quinol and passes electrons to periplasmic partners. MtrA, a decaheme cytochrome associated with the MtrB outer-membrane pore, transfers electrons across the outer membrane to surface-exposed MtrC/OmcA. These terminal reductases contact Fe(III) minerals through exposed hemes or exchange electrons with secreted flavins that act as diffusible mediators (shi2012molecularunderpinningsof pages 1-2, shi2012molecularunderpinningsof pages 2-3).

The purified MtrABC complex transfers electrons across a lipid bilayer after incorporation into proteoliposomes, and MtrABC co-expression enables *E. coli* to reduce solid Fe(III) oxide. These observations make the Mtr conduit among the strongest causal modules available for curation, although efficient heterologous reconstruction also requires correct cytochrome maturation, secretion, localization, and MtrB folding (shi2012molecularunderpinningsof pages 2-3, philipp2025identificationoffactors pages 14-16).

In *Geobacter*, multiple cytochromes and PilA-associated structures contribute in acceptor-dependent ways. A 2023 deletion series found that deleting `omcT`, `omcZ`, or `pilA-N` impaired ferrihydrite reduction; deleting all five tested genes (`omcS`, `omcT`, `omcZ`, `omcE`, `pilA-N`) abolished ferrihydrite and anode reduction under the tested conditions. The same mutants retained fumarate growth and soluble Fe(III)-citrate reduction, showing that these components are especially important for solid-phase EET rather than central metabolism or all Fe(III) reduction (jiang2023thevariedroles pages 3-5, jiang2023thevariedroles pages 1-2).

## Candidate nodes

### Trait, pathways, and processes

- `traitmech:000039` — dissimilatory metal reduction
- `METPO:1000802` — supplied parent trait
- Anaerobic respiration — label-only unless a verified ontology term is selected
- Dissimilatory Fe(III) reduction
- Dissimilatory Mn(IV) reduction
- Extracellular electron transfer
- Direct-contact electron transfer
- Flavin-mediated electron transfer
- Mtr pathway / MtrCAB porin–cytochrome conduit
- Geobacter porin–cytochrome pathway
- Long-range extracellular electron transfer — keep taxon/assay qualified
- Reductive mineral dissolution
- Respiratory energy conservation / ATP generation

### Genes, proteins, and complexes

**Shewanella-specific:** `cymA`, CymA; `mtrA`, MtrA; `mtrB`, MtrB; `mtrC`, MtrC; `omcA`, OmcA; MtrABC complex; type-II secretion system; small tetraheme cytochrome/CctA as a possible auxiliary carrier. GO grounding may be applied to broad molecular functions such as quinol dehydrogenase activity, electron-transfer activity, and c-type cytochrome, but gene-specific UniProt accessions should be added only after selecting the exact strain record.

**Geobacter-specific:** `pilA-N`, PilA-N; `omcB`, OmcB; `ombB`, OmbB; `omaB`, OmaB; `omcE`, OmcE; `omcS`, OmcS; `omcT`, OmcT; `omcZ`, OmcZ; conductive pili/e-pili; extracellular cytochrome filaments. The latter two must not be collapsed into one node because their identities and physiological roles remain contested (schwarz2024lackofphysiological pages 8-11, schwarz2024lackofphysiological pages 1-2).

**Dethiobacter candidates:** HydABC uptake hydrogenase; OmhA/OcwA-like Fe(III) reductases; multiple taxon-specific multiheme c-type cytochromes. The 2023 study found 31 predicted multiheme proteins in strain AHT1T and 27 in Z-1002, but many functional assignments were based on homology and differential expression rather than knockout or purified-protein evidence (zavarzina2023ironorsulfur pages 7-8).

### Chemicals and mineral nodes

- Fe(III), ferric iron; Fe(II), ferrous iron
- Mn(IV) oxide; Mn(II)
- Ferrihydrite, hematite, goethite, lepidocrocite
- Fe(III)-citrate
- Magnetite, siderite, rhodochrosite
- Menaquinol/quinol and oxidized quinone
- Flavin mononucleotide (FMN), riboflavin, secreted flavins
- Acetate, H₂, formate, lactate and other taxon-supported electron donors
- O₂ and H₂O₂ as regulatory/stress nodes rather than reactants of the target trait
- Candidate broader acceptors requiring separate evidence: Cr(VI), V(V), U(VI), Tc(VII), Co(III), Pd(II), Au(III), Ag(I), and As(V)

For chemicals, CHEBI identifiers should be resolved programmatically against the exact oxidation-state term before YAML insertion; identifiers are intentionally not guessed here.

### Cellular and environmental nodes

- Inner membrane
- Periplasm
- Outer membrane
- Cell surface/extracellular space
- Insoluble extracellular Fe(III) oxide surface
- Anoxic environment / oxygen limitation
- Oxic–anoxic interface
- Circumneutral sediment, soil, and groundwater
- Soda lake, alkaline subsurface aquifer, and Fe-rich serpentinite
- pH, redox potential, temperature, mineral crystallinity, ligand/complexant availability, and competing electron acceptors

Stable ontology candidates include GO cellular-component terms for inner membrane, periplasmic space, outer membrane, cell surface, and extracellular region, and ENVO terms for sediment, soil, groundwater, soda lake, and anoxic environment. Exact CURIEs should be ontology-lookup validated rather than entered from memory.

## Candidate causal edges

The table below is the recommended starting set. Strong trait-level edges should be separated from taxon-specific mechanism modules in the YAML.

| subject | predicate | object | model/taxon | evidence strength | DOI | short exact supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| dissimilatory metal reduction | uses terminal electron acceptor | Fe(III) (oxy)(hydr)oxide minerals | *Shewanella oneidensis* MR-1; trait-level exemplar | strong | 10.3389/fmicb.2012.00050 | "can use ferric [Fe(III)] (oxy)(hydr)oxide minerals as the terminal electron acceptors for anaerobic respiration" (shi2012molecularunderpinningsof pages 1-2) | Strong exemplar for trait scope; curate at trait level as metal/Fe(III)-accepting anaerobic respiration. |
| dissimilatory metal reduction | uses terminal electron acceptor | Mn(IV) oxides | *Shewanella oneidensis* MR-1; trait-level exemplar | strong | 10.1128/mbio.02589-22 | "These acceptors include soluble molecules such as dimethyl sulfoxide and nitrate and insoluble substrates such as Fe(III) and Mn(IV) oxides" (norman2023acysteinepair pages 1-2) | Supports inclusion of Mn(IV) alongside Fe(III) in scope. |
| CymA | oxidizes | quinol | *Shewanella oneidensis* MR-1 | strong | 10.3389/fmicb.2012.00050 | "CymA is believed to oxidize quinol in the inner-membrane and transfer the released electrons to redox proteins located in the periplasm" (shi2012molecularunderpinningsof pages 2-3) | Taxon-specific mechanistic edge for Shewanella Mtr pathway. |
| MtrAB | transfers electrons across | outer membrane | *Shewanella oneidensis* MR-1 | strong | 10.3389/fmicb.2012.00050 | "Together, MtrAB deliver the electrons through the outer-membrane to the MtrC and OmcA on the outmost bacterial surface" (shi2012molecularunderpinningsof pages 1-2) | Strong direct mechanistic edge; MtrA periplasmic/decaheme, MtrB porin-like sheath. |
| MtrC and OmcA | directly reduce | extracellular Fe(III) oxides | *Shewanella oneidensis* MR-1 | strong | 10.3389/fmicb.2012.00050 | "Functioning as terminal reductases, MtrC and OmcA can bind the surface of Fe(III) oxides and transfer electrons directly to these minerals" (shi2012molecularunderpinningsof pages 1-2) | Strong taxon-specific edge for outer-surface terminal reductases. |
| secreted flavins | shuttle electrons between | extracellular cytochromes and mineral surface | *Shewanella oneidensis* MR-1 | strong | 10.1128/mbio.02589-22 | "These flavins can function as soluble shuttles, transporting electrons between extracellular cytochromes and the mineral surface" (norman2023acysteinepair pages 1-2) | Good edge for mediated EET branch; should be marked taxon-specific to Shewanella-like systems. |
| Fe(III) reduction | produces | Fe(II) | trait-level / environmental consequence | strong | 10.1016/S0168-6445(03)00044-5 | "These processes can result in the release of potentially toxic levels of Fe(II) and Mn(II)" (lloyd2003microbialreductionof pages 1-2) | Product edge is environmentally important; source is review-level rather than single-pathway biochemistry. |
| H2 | serves as electron donor for growth with ferrihydrite | Fe(III) reduction | *Dethiobacter alkaliphilus* strains AHT1T and Z-1002 | moderate | 10.3389/fmicb.2023.1108245 | "culture of strain Z-1002 colonizing a synthesized ferrihydrite particle during the growth with molecular hydrogen" (zavarzina2023ironorsulfur pages 7-8) | Taxon-specific donor edge; mechanistically useful but not universal for all metal reducers. |
| formate | supports selective enrichment with Fe(III) as only electron acceptor | ferrihydrite reduction | *Dethiobacter*-related enrichment from subsurface aquifer | moderate | 10.3389/fmicb.2023.1108245 | "selective media containing formate (10 mM) or acetate (10 mM) with SF (50 mM final Fe(III) content) as the only electron acceptor" (zavarzina2023ironorsulfur pages 12-13) | Assay/enrichment-specific; supports donor compatibility, but not a clean isolate-level universal edge. |
| acetate | serves as electron donor | Fe(III) oxide reduction | *Geobacter sulfurreducens* (experimental condition) | moderate | 10.1128/mbio.00690-24 | "with 10 mM acetate provided as the electron donor and fumarate (40 mM) or Fe(III) oxide (80 mmol/L) as the electron acceptor" (schwarz2024lackofphysiological pages 8-11) | Strongly supports acetate in Geobacter assays; donor edge should remain taxon-specific. |
| oxygen exposure / oxic conditions | lowers affinity of | MtrC for FMN | *Shewanella oneidensis* MR-1 | strong | 10.1128/mbio.02589-22 | "In the presence of oxygen, the disulfide forms, lowering the affinity for FMN and decreasing the rate of peroxide formation" (norman2023acysteinepair pages 1-2) | Strong regulation edge linking oxygen to MtrC-FMN interaction. |
| MtrC CX8C disulfide | controls | FMN reduction | *Shewanella oneidensis* MR-1 | strong | 10.1128/mbio.02589-22 | "FMN reduction in S. oneidensis MR-1 is controlled by the redox-active disulfide on the cytochrome surface" (norman2023acysteinepair pages 1-2) | Useful regulatory edge; likely curate under environmental modulation of EET. |
| deletion of omcT, omcZ, or pilA-N | impairs | ferrihydrite reduction | *Geobacter sulfurreducens* | moderate | 10.3389/fmicb.2023.1251346 | "Deletion of omcT, omcZ or pilA-N alone impaired bacterial ability to reduce ferrihydrite and anodes and to form the co-culture" (jiang2023thevariedroles pages 1-2) | Gene-to-phenotype evidence in Geobacter; taxon-specific and substrate-specific. |
| deletion of all tested genes (omcS/omcT/omcZ/omcE/pilA-N) | abolishes | ferrihydrite reduction and anode reduction | *Geobacter sulfurreducens* | strong | 10.3389/fmicb.2023.1251346 | "Deletion of all tested genes abolished bacterial ability to reduce ferrihydrite and anodes" (jiang2023thevariedroles pages 1-2) | Strong combined-loss phenotype, but not suitable as single-gene universal edge. |
| electrically conductive pili (e-pili) | are required for | long-range extracellular electron transfer / Fe(III) oxide reduction | *Geobacter sulfurreducens* | moderate | 10.1128/mbio.00690-24 | "The results are consistent with the concept that 3 nm diameter electrically conductive pili (e-pili) are required for G. sulfurreducens long-range extracellular electron transfer" (schwarz2024lackofphysiological pages 1-2) | Important but taxon-specific; strong within this paper yet part of a broader controversy. |
| cytochrome filaments (OmcS/OmcE/OmcZ) | are primary conduits for | long-range EET to Fe(III) oxides | *Geobacter sulfurreducens* | disputed | 10.1128/mbio.00690-24 | "These results indicate that cytochrome filaments are not the primary conduits for long-range extracellular electron transport to Fe(III) oxides" (schwarz2024lackofphysiological pages 8-11) | Explicitly disputed; do not curate as established trait-level edge. |
| Fe(III) reduction in sediments | can form reduced minerals | magnetite / siderite / rhodochrosite | environmental consequence across metal-reducing systems | moderate | 10.1016/S0168-6445(03)00044-5 | "a range of reduced minerals can also be formed including magnetite (Fe3O4), siderite (FeCO3) and rhodochrosite (MnCO3)" (lloyd2003microbialreductionof pages 1-2) | Product/mineralization edge is environmentally important but context-dependent, not obligatory for every organism. |
| ferrihydrite reduction during growth with H2 | forms | magnetite crystal | *Dethiobacter alkaliphilus* strain Z-1002 | moderate | 10.3389/fmicb.2023.1108245 | "white arrow indicates a newly formed magnetite crystal" (zavarzina2023ironorsulfur pages 7-8) | Taxon- and condition-specific mineral product. |
| ferrihydrite reduction during growth with H2 | forms | siderite crystal | *Dethiobacter alkaliphilus* strain AHT1T | moderate | 10.3389/fmicb.2023.1108245 | "white arrows indicate newly formed siderite crystal" (zavarzina2023ironorsulfur pages 7-8) | Taxon- and condition-specific mineral product. |


*Table: This table summarizes the strongest curation-ready causal edges for dissimilatory metal reduction (traitmech:000039), emphasizing direct mechanistic evidence, taxon qualifiers, and disputed claims that should be treated cautiously.*

### Additional recommended graph structure

A compact core graph could contain:

1. `anoxic condition — enables — dissimilatory metal reduction`
2. `electron donor oxidation — reduces — quinone pool`
3. `reduced quinone pool — donates electrons via — respiratory electron-transfer chain`
4. `respiratory electron-transfer chain — transfers electrons to — metal terminal electron acceptor`
5. `Fe(III) — is reduced to — Fe(II)`
6. `Mn(IV) — is reduced to — Mn(II)`
7. `electron transfer to terminal acceptor — supports — energy conservation/growth`

Edges 1–7 express the trait mechanism at a lineage-neutral level. The detailed CymA–MtrAB–MtrC/OmcA sequence should be a *Shewanella*-qualified subgraph, while PilA/Omc/Pcc components should be a *Geobacter*-qualified subgraph.

## Recent developments, 2023–2024

### Acceptor-specific genetic requirements in Geobacter

The October 2023 systematic deletion study showed that all tested mutants reduced soluble Fe(III)-citrate without an apparent defect but were impaired in ferrihydrite reduction. This is strong evidence that soluble and particulate Fe(III) phenotypes should not be represented by a single undifferentiated assay node. Measurements used triplicate cultures and quantified 0.5 N HCl-extractable Fe(II) after 15 days (jiang2023thevariedroles pages 3-5).

### Reassessment of conductive nanowires

A May 2024 study reported that an OmcS-deficient strain and a mutant lacking all three known filament-forming cytochromes reduced Fe(III) oxide as well as wild type. In contrast, engineering poorly conductive 3-nm PilA filaments inhibited reduction. The authors concluded that the data support e-pili as key long-range conduits and do not support cytochrome filaments as the primary conduit (schwarz2024lackofphysiological pages 8-11, schwarz2024lackofphysiological pages 1-2). However, the 2023 study found diminished ferrihydrite reduction after several individual cytochrome deletions (jiang2023thevariedroles pages 1-2). Expert curation should therefore encode **gene-to-phenotype observations**, not the disputed universal proposition that either cytochrome filaments or pili alone constitute the sole nanowire mechanism.

The 2024 study also offers useful scale and assay statistics: access to sufficient Fe(III) oxide for replication was estimated to require electrical connection to an extracellular volume 20–50 times the cell volume; cultures used 10 mM acetate and 80 mmol/L Fe(III) oxide under N₂/CO₂ at 30°C, with Fe(II) quantified using ferrozine (schwarz2024lackofphysiological pages 8-11, schwarz2024lackofphysiological pages 1-2).

### Oxygen-responsive control of Shewanella EET

A January 2023 study showed that the MtrC surface CX₈C disulfide controls FMN interaction across oxic–anoxic transitions. Removing Cys453 increased FMN-dependent H₂O₂ generation by more than fivefold, compared with an approximately twofold FMN effect for wild-type soluble MtrC; peroxide/electron efficiency rose from approximately 0.2% without FMN to approximately 1% in the mutant-plus-FMN condition. This supports an oxygen-regulation branch rather than treating the Mtr chain as constitutively equivalent under anoxic and oxic conditions (norman2023acysteinepair pages 1-2, norman2023acysteinepair pages 5-7).

### Expansion beyond conventional model organisms

The July 2023 *D. alkaliphilus* study experimentally established iron reduction in both haloalkaliphilic strains and found distinct sets of multiheme cytochromes upregulated during Fe(III) versus thiosulfate respiration. A formate/ferrihydrite enrichment from an alkaline subsurface aquifer became 33.2% *Dethiobacter*-related, whereas the acetate enrichment contained none. Approximately 25% of surveyed environmental *Dethiobacter* sequences came from soda-lake sediments/alkaline soils, 35% from Fe-rich serpentinites, and 30% from anaerobic bioreactors/digesters (zavarzina2023ironorsulfur pages 1-2, zavarzina2023ironorsulfur pages 12-13). These are valuable ecological associations, but they do not establish that every detected lineage expresses the trait.

## Applications and real-world relevance

1. **Biogeochemical carbon and metal cycling.** Fe(III)- and Mn(IV)-reducing communities can account for substantial organic-matter oxidation in anoxic sediments and alter sediment mineralogy through reductive dissolution (lloyd2003microbialreductionof pages 1-2).
2. **Contaminant transformation and bioremediation.** Metal reducers can directly or indirectly transform U(VI), Cr(VI), Tc(VII), Co(III), and other contaminants. Reduction may immobilize a contaminant, but Fe/Mn oxide dissolution can instead mobilize sorbed trace metals; therefore, “metal reduction promotes remediation” is not universally valid (lloyd2003microbialreductionof pages 1-2, lloyd2003microbialreductionof pages 3-5).
3. **Anaerobic degradation of organic pollutants.** Organic oxidation coupled to Fe(III)/Mn(IV) reduction can support degradation of groundwater contaminants; this is a coupled application edge rather than part of the defining trait (lloyd2003microbialreductionof pages 1-2).
4. **Microbial fuel cells and bioelectrochemical systems.** Mtr- and Geobacter-type EET modules are used to exchange electrons with anodes, enabling current generation, wastewater treatment, waste valorization, and electrobiosynthesis. Electrode modifications, mediators, genetic engineering, and biofilm control are active optimization strategies (hazzan2023strategiesforenhancing pages 23-24, hazzan2023strategiesforenhancing pages 2-3).
5. **Biomineral production.** Reduced products can precipitate as magnetite, siderite, or rhodochrosite depending on geochemistry. The *Dethiobacter* experiments observed magnetite with strain Z-1002 and siderite with AHT1T during H₂/ferrihydrite growth (zavarzina2023ironorsulfur pages 7-8, lloyd2003microbialreductionof pages 1-2).

## Expert interpretation

The authoritative mechanistic literature treats the *Shewanella* Mtr pathway as the best-characterized extracellular metal-reduction conduit, but also emphasizes that it is incomplete and not universal (shi2012molecularunderpinningsof pages 1-2). Recent *Geobacter* studies reinforce a substrate-dependent, partially redundant network rather than a single indispensable terminal reductase (ueki2021cytochromesinextracellular pages 10-12, jiang2023thevariedroles pages 1-2). Accordingly, TraitMech should represent dissimilatory metal reduction as a **functional respiratory class with modular taxon-specific implementations**, not as possession of `mtrCAB`, `pilA`, or any one cytochrome.

## Warnings: claims not yet suitable for unqualified curation

1. **Do not curate `OmcS/OmcZ/OmcE filament — conducts long-range electrons — Fe(III) oxide` as settled.** Physiological evidence is disputed (schwarz2024lackofphysiological pages 8-11, schwarz2024lackofphysiological pages 1-2).
2. **Do not infer the trait from `mtrCAB` homology alone.** Homologs can participate in reverse EET/Fe(II) oxidation or reduction of nonmetal acceptors (shi2012molecularunderpinningsof pages 2-3).
3. **Do not infer growth coupling from metal disappearance alone.** Detoxification, sorption, precipitation, and abiotic reduction by biogenic Fe(II)/sulfide are alternatives (lloyd2003microbialreductionof pages 1-2, lloyd2003microbialreductionof pages 3-5).
4. **Do not merge soluble Fe(III)-citrate and insoluble ferrihydrite assays.** Their EET requirements differ markedly (jiang2023thevariedroles pages 3-5).
5. **Do not treat anode reduction as synonymous with metal reduction.** It is a mechanistic proxy/application and may have different cytochrome requirements (schwarz2024lackofphysiological pages 1-2, jiang2023thevariedroles pages 1-2).
6. **Keep donor and environmental edges qualified.** Acetate, H₂, formate, pH, salinity, and mineral phase effects vary by taxon and experiment (zavarzina2023ironorsulfur pages 7-8, zavarzina2023ironorsulfur pages 12-13, schwarz2024lackofphysiological pages 8-11).
7. **Treat Dethiobacter cytochrome assignments as candidates.** Differential proteomics and homology are supportive but do not prove that an individual protein is the terminal Fe(III) reductase (zavarzina2023ironorsulfur pages 7-8, zavarzina2023ironorsulfur pages 1-2).
8. **Avoid a universal “metal reduction immobilizes contaminants” edge.** Reductive dissolution can release Fe(II), Mn(II), and sorbed toxic metals even when other redox transformations cause immobilization (lloyd2003microbialreductionof pages 1-2).

## DOI-first bibliography

1. Shi L, Rosso KM, Clarke TA, Richardson DJ, Zachara JM, Fredrickson JK. **Molecular underpinnings of Fe(III) oxide reduction by *Shewanella oneidensis* MR-1.** *Frontiers in Microbiology*. Published 15 February 2012. DOI: [10.3389/fmicb.2012.00050](https://doi.org/10.3389/fmicb.2012.00050). (shi2012molecularunderpinningsof pages 1-2)
2. Jiang J et al. **The varied roles of pilA-N, omcE, omcS, omcT, and omcZ in extracellular electron transfer by *Geobacter sulfurreducens*.** *Frontiers in Microbiology*. Published 10 October 2023. DOI: [10.3389/fmicb.2023.1251346](https://doi.org/10.3389/fmicb.2023.1251346). (jiang2023thevariedroles pages 1-2)
3. Norman MP et al. **A cysteine pair controls flavin reduction by extracellular cytochromes during anoxic/oxic environmental transitions.** *mBio*. Published 16 January 2023. DOI: [10.1128/mbio.02589-22](https://doi.org/10.1128/mbio.02589-22). (norman2023acysteinepair pages 1-2)
4. Zavarzina DG et al. **Iron or sulfur respiration—an adaptive choice determining the fitness of a natronophilic bacterium *Dethiobacter alkaliphilus* in geochemically contrasting environments.** *Frontiers in Microbiology*. Published 14 July 2023. DOI: [10.3389/fmicb.2023.1108245](https://doi.org/10.3389/fmicb.2023.1108245). (zavarzina2023ironorsulfur pages 1-2)
5. Schwarz IA et al. **Lack of physiological evidence for cytochrome filaments functioning as conduits for extracellular electron transfer.** *mBio*. Published 2 April 2024; May issue. DOI: [10.1128/mbio.00690-24](https://doi.org/10.1128/mbio.00690-24). (schwarz2024lackofphysiological pages 1-2)
6. Ueki T. **Cytochromes in extracellular electron transfer in *Geobacter*.** *Applied and Environmental Microbiology*. April 2021. DOI: [10.1128/AEM.03109-20](https://doi.org/10.1128/AEM.03109-20). (ueki2021cytochromesinextracellular pages 10-12)
7. Lloyd JR. **Microbial reduction of metals and radionuclides.** *FEMS Microbiology Reviews*. First published online 30 April 2003. DOI: [10.1016/S0168-6445(03)00044-5](https://doi.org/10.1016/S0168-6445(03)00044-5). (lloyd2003microbialreductionof pages 1-2)
8. Hazzan OO, Zhao B, Xiao Y. **Strategies for enhancing extracellular electron transfer in environmental biotechnology: a review.** *Applied Sciences*. November 2023. DOI: [10.3390/app132312760](https://doi.org/10.3390/app132312760). (hazzan2023strategiesforenhancing pages 2-3)
9. Conley BE, Weinstock MT, Bond DR, Gralnick JA. **A hybrid extracellular electron transfer pathway enhances the survival of *Vibrio natriegens*.** *Applied and Environmental Microbiology*. September 2020. DOI: [10.1128/AEM.01253-20](https://doi.org/10.1128/AEM.01253-20). (conley2020ahybridextracellular pages 29-31)
10. Zacharoff LA, El-Naggar MY. **Redox conduction in biofilms: from respiration to living electronics.** *Current Opinion in Electrochemistry*. August 2017. DOI: [10.1016/j.coelec.2017.09.003](https://doi.org/10.1016/j.coelec.2017.09.003). (zacharoff2017redoxconductionin pages 6-7)

References

1. (lloyd2003microbialreductionof pages 1-2): Jonathan R. Lloyd. Microbial reduction of metals and radionuclides. FEMS microbiology reviews, 27 2-3:411-25, Jun 2003. URL: https://doi.org/10.1016/s0168-6445(03)00044-5, doi:10.1016/s0168-6445(03)00044-5. This article has 897 citations and is from a domain leading peer-reviewed journal.

2. (shi2012molecularunderpinningsof pages 1-2): Liang Shi, Kevin M. Rosso, Tomas A. Clarke, David J. Richardson, John M. Zachara, and James K. Fredrickson. Molecular underpinnings of fe(iii) oxide reduction by shewanella oneidensis mr-1. Frontiers in Microbiology, Feb 2012. URL: https://doi.org/10.3389/fmicb.2012.00050, doi:10.3389/fmicb.2012.00050. This article has 293 citations and is from a peer-reviewed journal.

3. (jiang2023thevariedroles pages 1-2): Jie Jiang, Pengchen He, Ying Luo, Zhao-Kuai Peng, Yongguang Jiang, Yidan Hu, Lei Qi, Xiuzhu Dong, Yiran Dong, and Liang Shi. The varied roles of pila-n, omce, omcs, omct, and omcz in extracellular electron transfer by geobacter sulfurreducens. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1251346, doi:10.3389/fmicb.2023.1251346. This article has 41 citations and is from a peer-reviewed journal.

4. (lloyd2003microbialreductionof pages 3-5): Jonathan R. Lloyd. Microbial reduction of metals and radionuclides. FEMS microbiology reviews, 27 2-3:411-25, Jun 2003. URL: https://doi.org/10.1016/s0168-6445(03)00044-5, doi:10.1016/s0168-6445(03)00044-5. This article has 897 citations and is from a domain leading peer-reviewed journal.

5. (zavarzina2023ironorsulfur pages 1-2): Daria G. Zavarzina, Alexander Yu Merkel, Alexandra A. Klyukina, Ivan M. Elizarov, Valeria A. Pikhtereva, Vyacheslav S. Rusakov, Nataliya I. Chistyakova, Rustam H. Ziganshin, Alexey A. Maslov, and Sergey N. Gavrilov. Iron or sulfur respiration—an adaptive choice determining the fitness of a natronophilic bacterium dethiobacter alkaliphilus in geochemically contrasting environments. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1108245, doi:10.3389/fmicb.2023.1108245. This article has 26 citations and is from a peer-reviewed journal.

6. (shi2012molecularunderpinningsof pages 2-3): Liang Shi, Kevin M. Rosso, Tomas A. Clarke, David J. Richardson, John M. Zachara, and James K. Fredrickson. Molecular underpinnings of fe(iii) oxide reduction by shewanella oneidensis mr-1. Frontiers in Microbiology, Feb 2012. URL: https://doi.org/10.3389/fmicb.2012.00050, doi:10.3389/fmicb.2012.00050. This article has 293 citations and is from a peer-reviewed journal.

7. (philipp2025identificationoffactors pages 14-16): Laura-Alina Philipp, Lukas Kneuer, Carina Mayer-Windhorst, Simon Jautelat, Nhat Quang Le, and Johannes Gescher. Identification of factors limiting the efficiency of transplanting extracellular electron transfer chains in <i>escherichia coli</i>. Applied and Environmental Microbiology, Jun 2025. URL: https://doi.org/10.1128/aem.00685-25, doi:10.1128/aem.00685-25. This article has 13 citations and is from a peer-reviewed journal.

8. (jiang2023thevariedroles pages 3-5): Jie Jiang, Pengchen He, Ying Luo, Zhao-Kuai Peng, Yongguang Jiang, Yidan Hu, Lei Qi, Xiuzhu Dong, Yiran Dong, and Liang Shi. The varied roles of pila-n, omce, omcs, omct, and omcz in extracellular electron transfer by geobacter sulfurreducens. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1251346, doi:10.3389/fmicb.2023.1251346. This article has 41 citations and is from a peer-reviewed journal.

9. (schwarz2024lackofphysiological pages 8-11): Ingrid A. Schwarz, Baha Alsaqri, Yassir Lekbach, Kathryn Henry, Sydney Gorman, Trevor Woodard, Laura Dion, Lauren Real, Dawn E. Holmes, Jessica A. Smith, and Derek R. Lovley. Lack of physiological evidence for cytochrome filaments functioning as conduits for extracellular electron transfer. May 2024. URL: https://doi.org/10.1128/mbio.00690-24, doi:10.1128/mbio.00690-24. This article has 15 citations and is from a domain leading peer-reviewed journal.

10. (schwarz2024lackofphysiological pages 1-2): Ingrid A. Schwarz, Baha Alsaqri, Yassir Lekbach, Kathryn Henry, Sydney Gorman, Trevor Woodard, Laura Dion, Lauren Real, Dawn E. Holmes, Jessica A. Smith, and Derek R. Lovley. Lack of physiological evidence for cytochrome filaments functioning as conduits for extracellular electron transfer. May 2024. URL: https://doi.org/10.1128/mbio.00690-24, doi:10.1128/mbio.00690-24. This article has 15 citations and is from a domain leading peer-reviewed journal.

11. (zavarzina2023ironorsulfur pages 7-8): Daria G. Zavarzina, Alexander Yu Merkel, Alexandra A. Klyukina, Ivan M. Elizarov, Valeria A. Pikhtereva, Vyacheslav S. Rusakov, Nataliya I. Chistyakova, Rustam H. Ziganshin, Alexey A. Maslov, and Sergey N. Gavrilov. Iron or sulfur respiration—an adaptive choice determining the fitness of a natronophilic bacterium dethiobacter alkaliphilus in geochemically contrasting environments. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1108245, doi:10.3389/fmicb.2023.1108245. This article has 26 citations and is from a peer-reviewed journal.

12. (norman2023acysteinepair pages 1-2): Michael P. Norman, Marcus J. Edwards, Gaye F. White, Joshua A. J. Burton, Julea N. Butt, David J. Richardson, Ricardo O. Louro, Catarina M. Paquete, and Thomas A. Clarke. A cysteine pair controls flavin reduction by extracellular cytochromes during anoxic/oxic environmental transitions. Feb 2023. URL: https://doi.org/10.1128/mbio.02589-22, doi:10.1128/mbio.02589-22. This article has 16 citations and is from a domain leading peer-reviewed journal.

13. (zavarzina2023ironorsulfur pages 12-13): Daria G. Zavarzina, Alexander Yu Merkel, Alexandra A. Klyukina, Ivan M. Elizarov, Valeria A. Pikhtereva, Vyacheslav S. Rusakov, Nataliya I. Chistyakova, Rustam H. Ziganshin, Alexey A. Maslov, and Sergey N. Gavrilov. Iron or sulfur respiration—an adaptive choice determining the fitness of a natronophilic bacterium dethiobacter alkaliphilus in geochemically contrasting environments. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1108245, doi:10.3389/fmicb.2023.1108245. This article has 26 citations and is from a peer-reviewed journal.

14. (norman2023acysteinepair pages 5-7): Michael P. Norman, Marcus J. Edwards, Gaye F. White, Joshua A. J. Burton, Julea N. Butt, David J. Richardson, Ricardo O. Louro, Catarina M. Paquete, and Thomas A. Clarke. A cysteine pair controls flavin reduction by extracellular cytochromes during anoxic/oxic environmental transitions. Feb 2023. URL: https://doi.org/10.1128/mbio.02589-22, doi:10.1128/mbio.02589-22. This article has 16 citations and is from a domain leading peer-reviewed journal.

15. (hazzan2023strategiesforenhancing pages 23-24): Oluwadamilola Oluwatoyin Hazzan, Biyi Zhao, and Yong Xiao. Strategies for enhancing extracellular electron transfer in environmental biotechnology: a review. Applied Sciences, 13:12760, Nov 2023. URL: https://doi.org/10.3390/app132312760, doi:10.3390/app132312760. This article has 51 citations.

16. (hazzan2023strategiesforenhancing pages 2-3): Oluwadamilola Oluwatoyin Hazzan, Biyi Zhao, and Yong Xiao. Strategies for enhancing extracellular electron transfer in environmental biotechnology: a review. Applied Sciences, 13:12760, Nov 2023. URL: https://doi.org/10.3390/app132312760, doi:10.3390/app132312760. This article has 51 citations.

17. (ueki2021cytochromesinextracellular pages 10-12): Toshiyuki Ueki. Cytochromes in extracellular electron transfer in <i>geobacter</i>. Apr 2021. URL: https://doi.org/10.1128/aem.03109-20, doi:10.1128/aem.03109-20. This article has 205 citations and is from a peer-reviewed journal.

18. (conley2020ahybridextracellular pages 29-31): Bridget E. Conley, Matthew T. Weinstock, Daniel R. Bond, and Jeffrey A. Gralnick. A hybrid extracellular electron transfer pathway enhances the survival of vibrio natriegens. Sep 2020. URL: https://doi.org/10.1128/aem.01253-20, doi:10.1128/aem.01253-20. This article has 40 citations and is from a peer-reviewed journal.

19. (zacharoff2017redoxconductionin pages 6-7): Lori A. Zacharoff and Mohamed Y. El-Naggar. Redox conduction in biofilms: from respiration to living electronics. Current Opinion in Electrochemistry, 4:182-189, Aug 2017. URL: https://doi.org/10.1016/j.coelec.2017.09.003, doi:10.1016/j.coelec.2017.09.003. This article has 53 citations and is from a peer-reviewed journal.