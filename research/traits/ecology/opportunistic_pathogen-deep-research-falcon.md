---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:30:46.252296'
end_time: '2026-08-03T23:38:28.554545'
duration_seconds: 462.3
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: opportunistic pathogen
  trait_identifier: traitmech:000046
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: opportunistic_pathogen
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A host-association lifestyle in which a normally commensal or environmental
    microorganism causes disease only when host defenses are compromised or it reaches
    a normally sterile site.
  parent_traits: METPO:1004000
  synonyms: opportunistic infection
  evidence_summary: 'DOI:10.1016/j.tim.2012.04.005:  (Brown, Cornforth & Mideo, "Evolution
    of virulence in opportunistic pathogens", support context-dependent virulence
    maintained by advantages outside the host.) | DOI:10.1038/s41579-021-00550-7:  (Drew
    et al. support facultative shifts toward parasitism/pathogenicity along the parasite-mutualist
    continuum, the basis of opportunistic disease.)'
  causal_graph_summary: 'opportunistic_pathogen_context_dependent_virulence: 10 nodes,
    9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 70
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** opportunistic pathogen
- **METPO identifier:** traitmech:000046
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A host-association lifestyle in which a normally commensal or environmental microorganism causes disease only when host defenses are compromised or it reaches a normally sterile site.
- **Parent traits:** METPO:1004000
- **Synonyms:** opportunistic infection
- **Existing evidence:** DOI:10.1016/j.tim.2012.04.005:  (Brown, Cornforth & Mideo, "Evolution of virulence in opportunistic pathogens", support context-dependent virulence maintained by advantages outside the host.) | DOI:10.1038/s41579-021-00550-7:  (Drew et al. support facultative shifts toward parasitism/pathogenicity along the parasite-mutualist continuum, the basis of opportunistic disease.)
- **Existing causal graph summary:** opportunistic_pathogen_context_dependent_virulence: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **opportunistic pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/opportunistic_pathogen.yaml`.

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
- **Trait label:** opportunistic pathogen
- **METPO identifier:** traitmech:000046
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A host-association lifestyle in which a normally commensal or environmental microorganism causes disease only when host defenses are compromised or it reaches a normally sterile site.
- **Parent traits:** METPO:1004000
- **Synonyms:** opportunistic infection
- **Existing evidence:** DOI:10.1016/j.tim.2012.04.005:  (Brown, Cornforth & Mideo, "Evolution of virulence in opportunistic pathogens", support context-dependent virulence maintained by advantages outside the host.) | DOI:10.1038/s41579-021-00550-7:  (Drew et al. support facultative shifts toward parasitism/pathogenicity along the parasite-mutualist continuum, the basis of opportunistic disease.)
- **Existing causal graph summary:** opportunistic_pathogen_context_dependent_virulence: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **opportunistic pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/opportunistic_pathogen.yaml`.

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


# Curation report: opportunistic pathogen

**Target:** `traitmech:000046` — opportunistic pathogen  
**Category:** ECOLOGY; **term kind:** CLASS; **mapping:** REVIEWED

## Executive scope

An **opportunistic pathogen** is best modeled as a **relational, context-dependent lifestyle**, not as a constitutive molecular phenotype. A normally commensal or environmental organism becomes disease-causing when host or niche constraints are relaxed—for example through impaired immunity, microbiota disruption, epithelial injury, implantation of a device, or entry into a normally sterile compartment—and when microbial persistence and damage mechanisms are expressed. Recent work reinforces that the same determinants can contribute to harmless colonization and disease; therefore, possession of a biofilm locus, toxin, adhesin, or resistance gene is insufficient by itself to assign the trait. In *Candida albicans*, for example, filamentation and candidalysin can participate in homeostatic colonization, while dysregulated activity produces epithelial damage (froismartins2024candidaalbicansvirulence pages 4-5). Likewise, *Staphylococcus epidermidis* persistence functions used on normal epithelia can be redeployed during device-associated disease (burke2024thepathogenicityand pages 19-20).

A useful high-level graph is:

`commensal/environmental reservoir` → **exposure to enabling host context** → `access or expansion in susceptible niche` → `environmental sensing and physiological adaptation` → `adhesion/biofilm, invasion, immune evasion or toxin activity` → `persistence and host damage` → **opportunistic infection**.

The trait boundary is an ecological outcome: **microbial growth or presence alone is colonization**, whereas infection requires invasion, damage, inflammatory pathology, or clinically meaningful dysfunction. Wound microbiology is explicitly described as a continuum from contamination through colonization to local and systemic infection; not all colonization becomes infection (uberoi2024thewoundmicrobiota pages 1-2).

## 1. Scope and boundary cases

### Included

- **Endogenous commensals becoming pathogenic:** *C. albicans*, enterococci and *S. epidermidis*.
- **Environmental organisms causing disease in susceptible hosts or altered niches:** *Pseudomonas aeruginosa*, *Stenotrophomonas maltophilia*, *Acinetobacter baumannii* and opportunistic *Xanthomonas*.
- **Asymptomatic colonizers expanding after ecological disruption:** post-antibiotic *Clostridioides difficile*.
- **Normally excluded organisms gaining sterile-site access:** skin flora entering through venous catheters or wounds.
- Both **weak host defense** and **excess, non-protective inflammation** can cause disease. Vulvovaginal candidiasis is an important boundary case: systemic immunocompromise is rarely the predisposing factor; candidalysin-driven, ineffective hyperinflammation is central (valentine2024nanobodymediatedneutralizationof pages 1-2).

### Excluded or separately modeled

- **Primary/obligate pathogens:** organisms routinely able to cause disease in immunocompetent hosts without an enabling context. A microbe may nevertheless have both primary and opportunistic manifestations.
- **Pathobiont:** overlapping but not identical. A pathobiont is a resident symbiont with disease potential; an opportunistic pathogen may instead be environmental.
- **Opportunistic infection:** the disease event, not the organismal lifestyle class. It is a synonym in common usage but should ideally be represented as an outcome node.
- **Nosocomial pathogen:** epidemiological setting, not mechanism. Hospital adaptation, resistance, devices and susceptible patients frequently create opportunity but are not defining individually.
- **Antimicrobial resistance:** promotes persistence and treatment failure but does not establish pathogenicity.
- **Biofilm formation:** a common enabling module, but also a normal environmental/commensal growth mode.
- **Detection in a non-sterile specimen:** may represent colonization or contamination. Clinical context and damage evidence are required.

## 2. Candidate graph nodes

Only stable identifiers that can be stated with reasonable confidence are suggested. Gene/protein identifiers should be assigned per reference strain during YAML implementation rather than treated as universal orthologues.

### Trait and organism nodes

- Opportunistic pathogen — `traitmech:000046`
- *Pseudomonas aeruginosa* — `NCBITaxon:287`
- *Candida albicans* — `NCBITaxon:5476`
- *Staphylococcus epidermidis* — `NCBITaxon:1282`
- *Enterococcus faecalis* — `NCBITaxon:1351`
- *Enterococcus faecium* — `NCBITaxon:1352`
- *Acinetobacter baumannii* — `NCBITaxon:470`
- *Stenotrophomonas maltophilia* — `NCBITaxon:40324`
- *Clostridioides difficile* — `NCBITaxon:1496`
- *Arabidopsis thaliana* — `NCBITaxon:3702`
- Opportunistic *Xanthomonas* Leaf131/Leaf148 — retain strain labels and link to the paper’s strain metadata; do not infer a species-level trait from these isolates alone.

### Host and environmental context

- Impaired host defense / immunocompromised host — label-only composite context
- Reduced NADPH-oxidase-dependent ROS defense — taxon-specific host mechanism
- Broad-spectrum antibiotic exposure
- Microbiota dysbiosis / loss of colonization resistance
- Epithelial or skin barrier breach
- Normally sterile site
- Medical-device surface; venous catheter; urinary catheter
- Wound, burn wound, cystic-fibrosis airway, gastrointestinal tract, oral/vaginal mucosa
- Iron limitation / nutritional immunity
- Heme availability
- Carbon-source composition and organic acids
- Desiccation/xeric hospital environment
- High population density / quorum signal accumulation

### Biological processes and structures

- Biofilm formation — `GO:0042710`
- Quorum sensing — `GO:0009372`
- Cell adhesion — `GO:0007155`
- Pathogenesis — `GO:0009405`
- Reactive oxygen species metabolic process — `GO:0072593`
- Type II protein secretion system / T2SS — use a verified GO term during curation; do not assign from memory
- Plant cell-wall degradation
- Hyphal growth / yeast-to-hypha transition
- Epithelial invasion and membrane permeabilization
- Immune evasion, oxidative-stress tolerance, desiccation tolerance
- Nutrient acquisition, siderophore-mediated iron uptake and heme uptake
- Tissue damage, inflammation, dysbiosis and persistent infection

### Genes, proteins, complexes and regulatory RNAs

**Host:** RBOHD/NADPH oxidase; EGFR; MAPK; c-Fos; MAPK phosphatase-1; HIF-1α; IL-17A; IL-22; LL-37; secretory IgA.

**Xanthomonas:** Xps and Xcs T2SS operons; HrpX/HrpG; candidate endoglucanase `ASF73_13775`, serine protease `ASF73_18370`, pectate lyases `ASF73_04230` and `ASF73_20170`, and lysyl endopeptidase `ASF73_20190`.

**P. aeruginosa:** CbrA/CbrB, RhlI/RhlR, LasI/LasR, CrcZ small RNA, Crc/Hfq, Pel exopolysaccharide, CupB/CupC fimbriae, HemO, Has and Phu heme systems, PhuR, pyoverdine, pyochelin, PqsR/MvfR, PQS, type IV pili, Psl, CdrA and cyclic-di-GMP/Wsp signaling.

**C. albicans:** ECE1/Ece1 precursor, candidalysin, ALS3/Als3, HWP1, WOR1, MNT2, MNT3, PMT5, XOG1 and ENG1.

**Other taxa:** *S. epidermidis* SdrG, SesB/SesC and SitC; *C. difficile* CD2831, PilA1, TcdA and TcdB; *S. maltophilia* DSF signaling and SmeYZ/SmeDEF/SbiAB/MacABCsm efflux systems. These are candidate taxon-specific modules, not universal opportunism markers (burke2024thepathogenicityand pages 19-20, jandl2024intestinalbiofilmspathophysiological pages 7-8, mikhailovich2024stenotrophomonasmaltophiliavirulence pages 1-2).

### Chemicals and metabolites

- Iron(II), iron(III), heme, carbon monoxide
- Biliverdin IXβ and biliverdin IXδ — retain label-only unless a verified ChEBI record is checked
- Pyoverdine and pyochelin
- 3-oxo-C12-homoserine lactone, C4-homoserine lactone and PQS
- Short-chain fatty acids: acetate, propionate and butyrate
- Lactic acid
- Indole-3-aldehyde
- p-Cresol
- Candidalysin peptide toxin
- Extracellular polymeric substances: polysaccharides, proteins, lipids and extracellular nucleic acids

## 3. Candidate causal edges

The strongest compact set is summarized below.

| subject | predicate | object | taxon/context | evidence strength | DOI |
|---|---|---|---|---|---|
| Loss of host **RBOHD** | increases susceptibility to | **Xanthomonas** disease severity and leaf tissue degradation | *Arabidopsis thaliana* **rbohD** mutant; opportunistic plant pathogenesis; host-genotype specific (sebastian2024leafmicrobiomedysbiosis pages 1-2) | **Direct experimental**; mutant host comparison in planta; taxon- and assay-specific | 10.1038/s41564-023-01555-z |
| **Compromised immune system** | enriches | opportunistic pathogens leading to dysbiosis | Plant phyllosphere; immunocompromised *Arabidopsis* (sebastian2024leafmicrobiomedysbiosis pages 1-2) | **Direct experimental**; gnotobiotic/SynCom and host-genotype dependent; taxon-specific | 10.1038/s41564-023-01555-z |
| **Xps T2SS** | is required for | leaf tissue degradation | *Xanthomonas* Leaf131/Leaf148; xps and xpsxcs deletion mutants (sebastian2024leafmicrobiomedysbiosis pages 4-5) | **Direct experimental**; gene deletion; strong but taxon-specific | 10.1038/s41564-023-01555-z |
| **Xps T2SS** | enables secretion of | plant cell wall-degrading enzymes | *Xanthomonas* supernatant/proteomics/plate assays (sebastian2024leafmicrobiomedysbiosis pages 4-5) | **Direct experimental**; mutant supernatant loses activity; assay-specific | 10.1038/s41564-023-01555-z |
| Loss of **RhlR + CbrA** | reduces abundance of | **CrcZ** small RNA | *Pseudomonas aeruginosa* PA14 biofilms; quorum- and nutrient-sensing intersection (chen2024combinatorialcontrolof pages 1-2) | **Direct experimental**; double mutant + transcriptomics/reporters; strain/assay-specific | 10.1128/msystems.00372-24 |
| **CrcZ** | antagonizes | **Crc** | *P. aeruginosa* carbon catabolite repression/biofilm regulation (chen2024combinatorialcontrolof pages 1-2) | **Direct experimental/mechanistic** in study framework; strong but species-specific | 10.1128/msystems.00372-24 |
| **Crc** | promotes expression of | **Pel exopolysaccharide** | *P. aeruginosa* PA14 biofilm matrix control (chen2024combinatorialcontrolof pages 1-2) | **Direct experimental**; suppressor genetics/transcriptomics/reporters; strain-specific | 10.1128/msystems.00372-24 |
| **Crc** | promotes expression of | **CupB/CupC fimbriae** | *P. aeruginosa* PA14 biofilm matrix control (chen2024combinatorialcontrolof pages 15-17, chen2024combinatorialcontrolof pages 1-2) | **Direct experimental**; reporters and mutant analyses; strain-specific | 10.1128/msystems.00372-24 |
| **Crc** | promotes | biofilm development | *P. aeruginosa* colony and static biofilm assays (chen2024combinatorialcontrolof pages 15-17, chen2024combinatorialcontrolof pages 1-2) | **Direct experimental**; strong but biofilm-assay specific | 10.1128/msystems.00372-24 |
| **HemO-produced biliverdin IXβ/IXδ** | promotes | swarming/twitching motility and robust biofilm formation | *P. aeruginosa*; hemO allelic strains with exogenous BVIXβ/BVIXδ rescue (shahzad2024pseudomonasaeruginosaheme pages 1-2) | **Direct experimental**; mutant phenotype with chemical rescue; strong, species-specific | 10.1128/mbio.02763-23 |
| Addition of **BVIXβ/BVIXδ** | partially rescues | motility and biofilm defects of hemO mutants | *P. aeruginosa* chronic-infection adaptation model (shahzad2024pseudomonasaeruginosaheme pages 1-2) | **Direct experimental rescue**; very strong but assay-specific | 10.1128/mbio.02763-23 |
| **Candidalysin** | causes | epithelial cell cytotoxicity | *Candida albicans* mucosal infection/VVC models (valentine2024nanobodymediatedneutralizationof pages 1-2) | **Direct experimental background and authoritative synthesis**; species- and host-tissue specific | 10.1128/mbio.03409-23 |
| **Candidalysin-driven tissue damage** | triggers | epithelial signaling and hyperinflammatory responses | *C. albicans* vaginal infection context (valentine2024nanobodymediatedneutralizationof pages 1-2) | **Direct experimental/preclinical**; strong but disease-context specific | 10.1128/mbio.03409-23 |
| **Anti-candidalysin nanobody** | reduces | epithelial damage | *C. albicans* infection of epithelial cells; preclinical neutralization (valentine2024nanobodymediatedneutralizationof pages 1-2) | **Direct experimental**; nanobody perturbation; assay-specific | 10.1128/mbio.03409-23 |
| **Anti-candidalysin nanobody** | reduces | downstream proinflammatory responses and neutrophil recruitment/activation | *C. albicans* VVC preclinical model (valentine2024nanobodymediatedneutralizationof pages 1-2) | **Direct experimental**; strong but preclinical and tissue-context specific | 10.1128/mbio.03409-23 |
| **Catheter insertion** | permits access of flora/contaminants to | underlying/sterile tissues | Venous catheters; healthcare-associated opportunistic infection (bouhrour2024medicaldeviceassociatedbiofilm pages 1-2) | **Authoritative review-supported**; mechanistically plausible, not a single perturbation experiment | 10.3390/pathogens13050393 |
| **Surface adhesion and biofilm formation** | promote | persistence in the host | Medical device-associated infections; broad opportunistic pathogens (bouhrour2024medicaldeviceassociatedbiofilm pages 1-2) | **Authoritative review-supported**; broad, cross-taxon, not single-gene causal | 10.3390/pathogens13050393 |


*Table: This table lists compact, curation-ready candidate causal edges for the opportunistic pathogen trait, prioritizing direct experimental evidence and clearly flagging taxon- or assay-specific claims. It is useful as a starting point for selecting high-confidence nodes and edges for TraitMech YAML curation.*

### Additional review-supported edges

| Candidate triple | Supporting snippet | Reference | Curation note |
|---|---|---|---|
| Broad-spectrum antibiotics **disrupt** microbiota → reduced colonization resistance | Experimental *Candida* colonization often requires “antibiotic-treated/gnotobiotic mice to overcome colonization resistance from complex microbiota.” | Fróis-Martins et al., 2024, DOI [10.1007/s40588-024-00235-8](https://doi.org/10.1007/s40588-024-00235-8) (froismartins2024candidaalbicansvirulence pages 4-5) | Strong ecological mechanism, but treatment and taxon dependent. |
| Post-antibiotic dysbiosis **permits** *C. difficile* overgrowth → toxin-mediated disease | The review identifies post-antibiotic overgrowth and TcdA/TcdB as drivers of symptomatic disease. | Jandl et al., September 2024, DOI [10.1128/cmr.00133-23](https://doi.org/10.1128/cmr.00133-23) (jandl2024intestinalbiofilmspathophysiological pages 7-8) | Curate as a *C. difficile* subgraph, not a universal toxin edge. |
| Intact microbiota and host immunity **restrain** *C. albicans* hyphae/pathogenic potential | “The immune system and microbiota work together to maintain stable colonization and prevent excessive fungal growth and disease.” | Fróis-Martins et al., October 2024, DOI [10.1007/s40588-024-00235-8](https://doi.org/10.1007/s40588-024-00235-8) (froismartins2024candidaalbicansvirulence pages 4-5) | High-confidence conceptual edge; composite mechanism. |
| Candidalysin **activates** EGFR–MAPK signaling → inflammatory cytokines | “Candidalysin-mediated activation of epithelial growth factor receptor (EGFR) induces mitogen-activated protein kinase (MAPK) signaling,” producing inflammatory responses. | Valentine et al., published 13 February 2024, DOI [10.1128/mbio.03409-23](https://doi.org/10.1128/mbio.03409-23) (valentine2024nanobodymediatedneutralizationof pages 1-2) | Direct mucosal mechanism; host-site-specific outcome can be protective or pathological. |
| Lactobacillus-derived lactic acid **acidifies** vaginal mucosa → protection from Candida infection | “Lactobacilli protect against vaginal infections…mainly through the production of lactic acid, which acidifies the vaginal mucosa.” | Katsipoulaki et al., June 2024, DOI [10.1128/mmbr.00021-23](https://doi.org/10.1128/mmbr.00021-23) (katsipoulaki2024candidaalbicansand pages 43-47) | Review-supported; species, concentration and site matter. |
| Microbiota-derived SCFAs **inhibit** *C. albicans* hyphae → reduced colonization | “Acetate, butyrate, and propionate…inhibit germ tube and hypha formation and inhibit colonization in mice.” | Katsipoulaki et al., 2024 (katsipoulaki2024candidaalbicansand pages 43-47) | Curatable in a Candida-specific module; avoid a universal SCFA claim. |
| Microbiota metabolites **reduce** ECE1/ALS3/HWP1 expression → reduced epithelial damage | Metabolites from *Bacteroides ovatus* and *Roseburia* spp. reduced these hypha-associated genes and epithelial damage. | Katsipoulaki et al., 2024 (katsipoulaki2024candidaalbicansand pages 43-47) | Secondary-source evidence; recover the cited primary study before final YAML inclusion. |
| Biofilm EPS **increases resistance to** antimicrobials and immune responses → persistence | Biofilms aid colonization and enhance resistance to antimicrobial substances and host immunity. | Wang et al., December 2023, DOI [10.1186/s43556-023-00164-w](https://doi.org/10.1186/s43556-023-00164-w) (wang2023biofilmformationmechanistic pages 1-2) | Broad consensus edge; specify phenotype and assay where possible. |
| Wsp/cyclic-di-GMP activation **increases** Psl/Pel/CdrA and biofilm → chronic persistence | Wsp deletions and cyclic-di-GMP overproduction were linked to biofilm overproduction and *P. aeruginosa* persistence. | Dekker, January 2024, DOI [10.1146/annurev-pathmechdis-051122-111408](https://doi.org/10.1146/annurev-pathmechdis-051122-111408) (dekker2024withinhostevolutionof pages 12-14) | Retrieve underlying primary experiments before encoding precise alleles. |
| Heme uptake and HemO catabolism **produce** BVIXβ/BVIXδ → sessile adaptation | hemO allelic strains had defective growth, motility and biofilm; exogenous metabolites partially rescued phenotypes. | Shahzad et al., published 6 February 2024, DOI [10.1128/mbio.02763-23](https://doi.org/10.1128/mbio.02763-23) (shahzad2024pseudomonasaeruginosaheme pages 1-2) | Strong knockout/rescue edge; in-vitro chronic-infection adaptation model. |
| Hospital stress tolerance and resistance acquisition **promote** persistence and spread | *A. baumannii* genomic plasticity, resistance acquisition and tolerance of hospital stresses promote spread and long-term contamination. | Lucidi et al., 2024, DOI [10.1080/21505594.2023.2289769](https://doi.org/10.1080/21505594.2023.2289769) (lucidi2024pathogenicityandvirulence pages 1-2) | Composite review edge; break into desiccation, adhesion and resistance modules only with primary evidence. |

## 4. Most defensible YAML architecture

A single universal graph should contain **context gates and generic processes**, with separate taxon-specific evidence branches:

1. `commensal_or_environmental_lifestyle`
2. `host_defense_impairment` / `microbiota_disruption` / `barrier_breach`
3. `niche_access_or_overgrowth`
4. `environmental_sensing_and_metabolic_adaptation`
5. `adhesion_or_biofilm` and/or `invasion_or_toxin_activity`
6. `persistence_or_host_damage`
7. `opportunistic_pathogen`

Recommended representative mechanistic branches are:

- **Plant branch:** RBOHD loss → reduced ROS defense → Xanthomonas enrichment; Xps T2SS → CWDE secretion → tissue degradation → dysbiosis.
- **Pseudomonas persistence branch:** quorum/nutrient sensing → CrcZ/Crc → Pel and Cup fimbriae → biofilm; heme → HemO → BVIXβ/δ signaling → sessile adaptation.
- **Candida mucosal branch:** dysbiosis/altered immunity → hyphal growth → Ece1 processing/candidalysin → epithelial damage → context-specific inflammation.
- **Device branch:** catheter insertion → barrier bypass → surface adhesion → biofilm/persisters → bloodstream or urinary infection.

Do **not** merge these taxon-specific nodes into a claim that all opportunistic pathogens use T2SS, candidalysin, heme signaling, or the Crc pathway.

## 5. Recent developments and applications

### Antivirulence neutralization

Valentine et al. provided a strong 2024 proof of mechanism: llama-derived candidalysin nanobodies localized near invading hyphae and reduced epithelial injury, inflammatory signaling, and neutrophil activation/recruitment without relying on fungal killing. This is a **preclinical** application, not an approved therapy (valentine2024nanobodymediatedneutralizationof pages 1-2). It supports an actionable edge, `anti-candidalysin nanobody inhibits candidalysin`, and illustrates a strategy that may preserve commensal organisms while suppressing damaging activity.

### Biofilm and device interventions

Current implementation centers on aseptic insertion and maintenance, device removal when appropriate, antimicrobial/antifouling catheter materials, and treatment adapted to biofilm-associated resistance. Experimental directions include cationic-peptide or chitosan coatings, enzyme-based matrix disruption, adhesion inhibitors and quorum-quenching approaches (burke2024thepathogenicityand pages 19-20, bouhrour2024medicaldeviceassociatedbiofilm pages 1-2). Biofilm is nevertheless heterogeneous; an intervention effective against planktonic cells or one species cannot be assumed to eradicate polymicrobial device biofilms.

### Quorum- and nutrient-sensing targets

The 2024 *P. aeruginosa* study identifies CrcZ/Crc as a convergence point linking RhlR quorum sensing and CbrA/CbrB nutrient sensing to Pel and Cup matrix components. This refines “quorum sensing causes biofilm” into a conditional regulatory circuit and provides candidate anti-biofilm targets (chen2024combinatorialcontrolof pages 15-17, chen2024combinatorialcontrolof pages 1-2). Because RhlR repressed biofilm in this experimental setting whereas LasR can promote it, a generic edge stating that all quorum sensing uniformly increases biofilm would be incorrect.

### Iron/heme adaptation

Shahzad et al. show that HemO-generated biliverdin IXβ/IXδ are not merely waste products but signaling metabolites coordinating iron-source use, motility and biofilm behavior. This supports multi-target strategies against heme utilization and cooperative persistence, but efficacy in patients has not yet been established (shahzad2024pseudomonasaeruginosaheme pages 1-2).

### Microbiota-preserving interventions

Recent expert synthesis favors retaining or restoring colonization resistance rather than indiscriminately eliminating commensals. Candidate approaches include narrow-spectrum antimicrobials, probiotics or defined microbial metabolites, restoration of SCFA/lactate-producing communities, and precision quorum manipulation. The evidence remains niche- and organism-specific; microbiota transplantation or probiotics should not be represented as universally protective (froismartins2024candidaalbicansvirulence pages 4-5, katsipoulaki2024candidaalbicansand pages 43-47).

## 6. Recent quantitative data

- Medical-device biofilms were estimated to be linked to **60–70% of nosocomial infections**. The reviewed data cite about **80,000 central-venous-catheter bloodstream infections**, predominantly in ICUs, with **12–25% mortality**; catheter-associated UTIs account for up to **40% of nosocomial infections**. Approximately **81%** of vascular catheters retained for 1–14 days were reported colonized by biofilm. These are review-compiled estimates and may reflect different locations and periods rather than a single contemporary surveillance cohort (bouhrour2024medicaldeviceassociatedbiofilm pages 1-2).
- VVC affects approximately **75% of women at least once** during reproductive years; **>5%** experience recurrent VVC, corresponding to an estimated **138 million women annually worldwide**. These figures concern one opportunistic syndrome and should not be generalized to invasive candidiasis (valentine2024nanobodymediatedneutralizationof pages 1-2).
- The Enterococcus review reports mortality ranges of **14.3–32.3%** and European vancomycin-resistant *E. faecium* proportions varying approximately **18–50% by country**; population and infection definitions differ across the underlying surveillance sources (sangiorgio2024theimpactof pages 1-2).
- A 2024 review estimated US *C. difficile* infection cost at about **US$42,000 per case** (jandl2024intestinalbiofilmspathophysiological pages 7-8).
- *A. baumannii* was identified among six leading pathogens for antimicrobial-resistance-associated deaths in the cited 2019 global burden assessment (lucidi2024pathogenicityandvirulence pages 1-2).

## 7. Expert interpretation

The strongest contemporary interpretation is that opportunism is an **emergent property of host–microbe–environment interaction**. Virulence determinants are often maintained because they provide colonization or environmental fitness, not because they evolved solely to damage hosts. The commensal–parasite continuum is evolutionarily dynamic, and symbionts can move rapidly along it (Drew et al., 2021). In *C. albicans*, almost all commensal strains retain pathogenic potential, while host factors and antagonistic microbiota help maintain the commensal phase (katsipoulaki2024candidaalbicansand pages 43-47). The *Xanthomonas* study provides unusually clear causal support: the host `rbohD` defect did not simply alter the community independently; disease and microbiota change depended on the opportunistic strain and its Xps secretion system (sebastian2024leafmicrobiomedysbiosis pages 4-5, sebastian2024leafmicrobiomedysbiosis pages 1-2).

Accordingly, TraitMech should encode **necessary or enabling contexts**, rather than imply that any single microbial gene is sufficient for the class. The graph should also permit host damage to arise from insufficient immunity, microbial activity, or damaging non-protective inflammation.

## 8. Warnings: claims not ready for curation

1. **Do not curate “biofilm formation causes opportunistic pathogenicity” as an unconditional universal edge.** Biofilms occur in benign environmental and commensal states.
2. **Do not use antimicrobial resistance as a defining parent or sufficient cause.** Resistance principally affects persistence, transmission and treatment outcome.
3. **Do not infer disease from detection or abundance alone.** Colonization, contamination and infection must remain separate.
4. **Do not universalize taxon-specific pathways.** Xps T2SS, candidalysin, CrcZ/Crc and HemO–biliverdin signaling belong in evidence branches.
5. **Do not assign precise CURIEs without database verification.** Biliverdin isomers, strain-specific proteins, environmental contexts and T2SS terms should remain label-only until checked.
6. **Do not curate individual Xanthomonas CWDEs as necessary for degradation.** Single candidate deletions were inconsistent, whereas the Xps system and secreted enzyme cocktail had strong support (sebastian2024leafmicrobiomedysbiosis pages 4-5).
7. **Treat Crc-to-matrix regulation as potentially indirect.** The authors found no canonical Crc/Hfq motif in the identified biofilm-matrix transcripts and explicitly note that indirect activation remains possible (chen2024combinatorialcontrolof pages 15-17).
8. **Treat device and burden figures as review-level evidence.** They support clinical relevance, not organism-specific molecular causality.
9. **Recover cited primary studies before encoding microbiota-metabolite edges** involving EntV, p-cresol, SCFAs, lactate or indole-3-aldehyde; the present evidence was extracted from a review (katsipoulaki2024candidaalbicansand pages 43-47).
10. **Do not equate VVC with classic immunodeficiency-driven opportunism.** Its pathology commonly reflects dysbiosis, endocrine/metabolic factors and non-protective inflammation (valentine2024nanobodymediatedneutralizationof pages 1-2).

## DOI-first bibliography

1. Pfeilmeier S, et al. “Leaf microbiome dysbiosis triggered by T2SS-dependent enzyme secretion from opportunistic *Xanthomonas* pathogens.” *Nature Microbiology* 9, 136–149. Published **3 January 2024**. DOI: [10.1038/s41564-023-01555-z](https://doi.org/10.1038/s41564-023-01555-z). (sebastian2024leafmicrobiomedysbiosis pages 4-5, sebastian2024leafmicrobiomedysbiosis pages 1-2)
2. Chen G, et al. “Combinatorial control of *Pseudomonas aeruginosa* biofilm development by quorum-sensing and nutrient-sensing regulators.” *mSystems* 9. Published **14 August 2024**. DOI: [10.1128/msystems.00372-24](https://doi.org/10.1128/msystems.00372-24). (chen2024combinatorialcontrolof pages 15-17, chen2024combinatorialcontrolof pages 1-2)
3. Shahzad S, et al. “*Pseudomonas aeruginosa* heme metabolites biliverdin IXβ and IXδ are integral to lifestyle adaptations associated with chronic infection.” *mBio* 15. Published **6 February 2024**. DOI: [10.1128/mbio.02763-23](https://doi.org/10.1128/mbio.02763-23). (shahzad2024pseudomonasaeruginosaheme pages 1-2)
4. Valentine M, et al. “Nanobody-mediated neutralization of candidalysin prevents epithelial damage and inflammatory responses that drive vulvovaginal candidiasis pathogenesis.” *mBio* 15. Published **13 February 2024**. DOI: [10.1128/mbio.03409-23](https://doi.org/10.1128/mbio.03409-23). (valentine2024nanobodymediatedneutralizationof pages 1-2)
5. Katsipoulaki M, et al. “*Candida albicans* and *Candida glabrata*: global priority pathogens.” *Microbiology and Molecular Biology Reviews* 88. **June 2024**. DOI: [10.1128/mmbr.00021-23](https://doi.org/10.1128/mmbr.00021-23). (katsipoulaki2024candidaalbicansand pages 43-47)
6. Fróis-Martins R, Lagler J, LeibundGut-Landmann S. “*Candida albicans* virulence traits in commensalism and disease.” *Current Clinical Microbiology Reports* 11, 231–240. **October 2024**. DOI: [10.1007/s40588-024-00235-8](https://doi.org/10.1007/s40588-024-00235-8). (froismartins2024candidaalbicansvirulence pages 4-5)
7. Jensen O, et al. “Controlling *Candida*: immune regulation of commensal fungi in the gut.” *Infection and Immunity* 92. **September 2024**. DOI: [10.1128/iai.00516-23](https://doi.org/10.1128/iai.00516-23). (jensen2024controllingcandida pages 10-12)
8. Burke Ó, Zeden MS, O’Gara JP. “The pathogenicity and virulence of the opportunistic pathogen *Staphylococcus epidermidis*.” *Virulence* 15. **June 2024**. DOI: [10.1080/21505594.2024.2359483](https://doi.org/10.1080/21505594.2024.2359483). (burke2024thepathogenicityand pages 19-20)
9. Sangiorgio G, et al. “The impact of *Enterococcus* spp. in the immunocompromised host.” *Pathogens* 13, 409. **May 2024**. DOI: [10.3390/pathogens13050409](https://doi.org/10.3390/pathogens13050409). (sangiorgio2024theimpactof pages 1-2)
10. Jandl B, et al. “Intestinal biofilms: pathophysiological relevance, host defense, and therapeutic opportunities.” *Clinical Microbiology Reviews* 37. **September 2024**. DOI: [10.1128/cmr.00133-23](https://doi.org/10.1128/cmr.00133-23). (jandl2024intestinalbiofilmspathophysiological pages 7-8)
11. Uberoi A, McCready-Vangi A, Grice EA. “The wound microbiota: microbial mechanisms of impaired wound healing and infection.” *Nature Reviews Microbiology* 22, 507–521. **April 2024**. DOI: [10.1038/s41579-024-01035-z](https://doi.org/10.1038/s41579-024-01035-z). (uberoi2024thewoundmicrobiota pages 1-2)
12. Bouhrour N, Nibbering PH, Bendali F. “Medical Device-Associated Biofilm Infections and Multidrug-Resistant Pathogens.” *Pathogens* 13, 393. Published **8 May 2024**. DOI: [10.3390/pathogens13050393](https://doi.org/10.3390/pathogens13050393). (bouhrour2024medicaldeviceassociatedbiofilm pages 1-2)
13. Mikhailovich V, et al. “*Stenotrophomonas maltophilia* virulence: a current view.” *Frontiers in Microbiology* 15. **April 2024**. DOI: [10.3389/fmicb.2024.1385631](https://doi.org/10.3389/fmicb.2024.1385631). (mikhailovich2024stenotrophomonasmaltophiliavirulence pages 1-2)
14. Lucidi M, et al. “Pathogenicity and virulence of *Acinetobacter baumannii*.” *Virulence* 15. 2024; accepted **27 November 2023**. DOI: [10.1080/21505594.2023.2289769](https://doi.org/10.1080/21505594.2023.2289769). (lucidi2024pathogenicityandvirulence pages 1-2)
15. Dekker JP. “Within-host evolution of bacterial pathogens in acute and chronic infection.” *Annual Review of Pathology* 19, 203–226. **January 2024**. DOI: [10.1146/annurev-pathmechdis-051122-111408](https://doi.org/10.1146/annurev-pathmechdis-051122-111408). (dekker2024withinhostevolutionof pages 12-14)
16. Wang X, et al. “Biofilm formation: mechanistic insights and therapeutic targets.” *Molecular Biomedicine* 4, 49. **December 2023**. DOI: [10.1186/s43556-023-00164-w](https://doi.org/10.1186/s43556-023-00164-w). (wang2023biofilmformationmechanistic pages 1-2)
17. Drew GC, Stevens EJ, King KC. “Microbial evolution and transitions along the parasite–mutualist continuum.” *Nature Reviews Microbiology* 19, 623–638. **April 2021**. DOI: [10.1038/s41579-021-00550-7](https://doi.org/10.1038/s41579-021-00550-7).
18. Brown SP, Cornforth DM, Mideo N. “Evolution of virulence in opportunistic pathogens.” *Trends in Microbiology* 20, 336–342. 2012. DOI: [10.1016/j.tim.2012.04.005](https://doi.org/10.1016/j.tim.2012.04.005).

References

1. (froismartins2024candidaalbicansvirulence pages 4-5): Ricardo Fróis-Martins, Julia Lagler, and Salomé LeibundGut-Landmann. Candida albicans virulence traits in commensalism and disease. Current Clinical Microbiology Reports, 11:231-240, Oct 2024. URL: https://doi.org/10.1007/s40588-024-00235-8, doi:10.1007/s40588-024-00235-8. This article has 21 citations.

2. (burke2024thepathogenicityand pages 19-20): Órla Burke, Merve S. Zeden, and James P. O’Gara. The pathogenicity and virulence of the opportunistic pathogen staphylococcus epidermidis. Virulence, Jun 2024. URL: https://doi.org/10.1080/21505594.2024.2359483, doi:10.1080/21505594.2024.2359483. This article has 57 citations and is from a peer-reviewed journal.

3. (uberoi2024thewoundmicrobiota pages 1-2): Aayushi Uberoi, Amelia McCready-Vangi, and Elizabeth A. Grice. The wound microbiota: microbial mechanisms of impaired wound healing and infection. Nature reviews. Microbiology, 22:507-521, Apr 2024. URL: https://doi.org/10.1038/s41579-024-01035-z, doi:10.1038/s41579-024-01035-z. This article has 893 citations.

4. (valentine2024nanobodymediatedneutralizationof pages 1-2): Marisa Valentine, Paul Rudolph, Axel Dietschmann, Antzela Tsavou, Selene Mogavero, Sejeong Lee, Emily L. Priest, Gaukhar Zhurgenbayeva, Nadja Jablonowski, Sandra Timme, Christian Eggeling, Stefanie Allert, Edward Dolk, Julian R. Naglik, Marc T. Figge, Mark S. Gresnigt, and Bernhard Hube. Nanobody-mediated neutralization of candidalysin prevents epithelial damage and inflammatory responses that drive vulvovaginal candidiasis pathogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03409-23, doi:10.1128/mbio.03409-23. This article has 43 citations and is from a domain leading peer-reviewed journal.

5. (jandl2024intestinalbiofilmspathophysiological pages 7-8): Bernhard Jandl, Satish Dighe, Christoph Gasche, Athanasios Makristathis, and Markus Muttenthaler. Intestinal biofilms: pathophysiological relevance, host defense, and therapeutic opportunities. Clinical Microbiology Reviews, Sep 2024. URL: https://doi.org/10.1128/cmr.00133-23, doi:10.1128/cmr.00133-23. This article has 33 citations and is from a highest quality peer-reviewed journal.

6. (mikhailovich2024stenotrophomonasmaltophiliavirulence pages 1-2): Vladimir Mikhailovich, R. Heydarov, Danila O. Zimenkov, and Igor V. Chebotar. Stenotrophomonas maltophilia virulence: a current view. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1385631, doi:10.3389/fmicb.2024.1385631. This article has 38 citations and is from a peer-reviewed journal.

7. (sebastian2024leafmicrobiomedysbiosis pages 1-2): Sebastian Pfeilmeier, Anja Werz, Marine Ote, Miriam Bortfeld-Miller, Pascal Kirner, Andreas Keppler, Lucas Hemmerle, Christoph G. Gäbelein, Gabriella C. Petti, Sarah Wolf, Christine M. Pestalozzi, and Julia A. Vorholt. Leaf microbiome dysbiosis triggered by t2ss-dependent enzyme secretion from opportunistic xanthomonas pathogens. Nature Microbiology, 9:136-149, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01555-z, doi:10.1038/s41564-023-01555-z. This article has 85 citations and is from a highest quality peer-reviewed journal.

8. (sebastian2024leafmicrobiomedysbiosis pages 4-5): Sebastian Pfeilmeier, Anja Werz, Marine Ote, Miriam Bortfeld-Miller, Pascal Kirner, Andreas Keppler, Lucas Hemmerle, Christoph G. Gäbelein, Gabriella C. Petti, Sarah Wolf, Christine M. Pestalozzi, and Julia A. Vorholt. Leaf microbiome dysbiosis triggered by t2ss-dependent enzyme secretion from opportunistic xanthomonas pathogens. Nature Microbiology, 9:136-149, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01555-z, doi:10.1038/s41564-023-01555-z. This article has 85 citations and is from a highest quality peer-reviewed journal.

9. (chen2024combinatorialcontrolof pages 1-2): Gong Chen, Georgia Fanouraki, Aathmaja Anandhi Rangarajan, Bradford T. Winkelman, Jared T. Winkelman, Christopher M. Waters, and Sampriti Mukherjee. Combinatorial control of <i>pseudomonas aeruginosa</i> biofilm development by quorum-sensing and nutrient-sensing regulators. Sep 2024. URL: https://doi.org/10.1128/msystems.00372-24, doi:10.1128/msystems.00372-24. This article has 11 citations and is from a peer-reviewed journal.

10. (chen2024combinatorialcontrolof pages 15-17): Gong Chen, Georgia Fanouraki, Aathmaja Anandhi Rangarajan, Bradford T. Winkelman, Jared T. Winkelman, Christopher M. Waters, and Sampriti Mukherjee. Combinatorial control of <i>pseudomonas aeruginosa</i> biofilm development by quorum-sensing and nutrient-sensing regulators. Sep 2024. URL: https://doi.org/10.1128/msystems.00372-24, doi:10.1128/msystems.00372-24. This article has 11 citations and is from a peer-reviewed journal.

11. (shahzad2024pseudomonasaeruginosaheme pages 1-2): Saba Shahzad, Samuel A. Krug, Susana Mouriño, Weiliang Huang, Maureen A. Kane, and Angela Wilks. <i>pseudomonas aeruginosa</i> heme metabolites biliverdin ixβ and ixδ are integral to lifestyle adaptations associated with chronic infection. Mar 2024. URL: https://doi.org/10.1128/mbio.02763-23, doi:10.1128/mbio.02763-23. This article has 11 citations and is from a domain leading peer-reviewed journal.

12. (bouhrour2024medicaldeviceassociatedbiofilm pages 1-2): Nesrine Bouhrour, P. H. Nibbering, and F. Bendali. Medical device-associated biofilm infections and multidrug-resistant pathogens. Pathogens, May 2024. URL: https://doi.org/10.3390/pathogens13050393, doi:10.3390/pathogens13050393. This article has 150 citations.

13. (katsipoulaki2024candidaalbicansand pages 43-47): Myrto Katsipoulaki, Mark H. T. Stappers, Dhara Malavia-Jones, Sascha Brunke, Bernhard Hube, and Neil A. R. Gow. <i>candida albicans</i> and <i>candida glabrata</i> : global priority pathogens. Jun 2024. URL: https://doi.org/10.1128/mmbr.00021-23, doi:10.1128/mmbr.00021-23. This article has 181 citations and is from a domain leading peer-reviewed journal.

14. (wang2023biofilmformationmechanistic pages 1-2): Xinyu Wang, Ming Liu, Chuanjiang Yu, Jing Li, and Xikun Zhou. Biofilm formation: mechanistic insights and therapeutic targets. Molecular Biomedicine, Dec 2023. URL: https://doi.org/10.1186/s43556-023-00164-w, doi:10.1186/s43556-023-00164-w. This article has 190 citations and is from a peer-reviewed journal.

15. (dekker2024withinhostevolutionof pages 12-14): John P. Dekker. Within-host evolution of bacterial pathogens in acute and chronic infection. Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-111408, doi:10.1146/annurev-pathmechdis-051122-111408. This article has 33 citations and is from a domain leading peer-reviewed journal.

16. (lucidi2024pathogenicityandvirulence pages 1-2): Massimiliano Lucidi, Daniela Visaggio, Antonella Migliaccio, Giulia Capecchi, Paolo Visca, Francesco Imperi, and Raffaele Zarrilli. Pathogenicity and virulence of acinetobacter baumannii: factors contributing to the fitness in healthcare settings and the infected host. Virulence, Dec 2024. URL: https://doi.org/10.1080/21505594.2023.2289769, doi:10.1080/21505594.2023.2289769. This article has 138 citations and is from a peer-reviewed journal.

17. (sangiorgio2024theimpactof pages 1-2): Giuseppe Sangiorgio, Maddalena Calvo, Giuseppe Migliorisi, Floriana Campanile, and Stefania Stefani. The impact of enterococcus spp. in the immunocompromised host: a comprehensive review. Pathogens, 13:409, May 2024. URL: https://doi.org/10.3390/pathogens13050409, doi:10.3390/pathogens13050409. This article has 65 citations.

18. (jensen2024controllingcandida pages 10-12): Owen Jensen, Emma Trujillo, Luke Hanson, and Kyla S. Ost. Controlling <i>candida</i> : immune regulation of commensal fungi in the gut. Infection and Immunity, Sep 2024. URL: https://doi.org/10.1128/iai.00516-23, doi:10.1128/iai.00516-23. This article has 24 citations and is from a peer-reviewed journal.