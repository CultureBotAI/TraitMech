---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:22:58.177396'
end_time: '2026-08-03T23:35:01.115057'
duration_seconds: 722.94
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: human pathogen
  trait_identifier: METPO:1004004
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: human_pathogen
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pathogen that infects organisms of the species Homo sapiens.
  parent_traits: METPO:1004000
  synonyms: ''
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162938: virulence factors
    (Virulence-factor review supports adaptation of bacterial virulence programs to
    the human host environment.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems
    review supports effector delivery as a major mechanism by which bacteria establish
    human infection.)'
  causal_graph_summary: 'human_pathogen_anthropoid_adaptation: 13 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** human pathogen
- **METPO identifier:** METPO:1004004
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pathogen that infects organisms of the species Homo sapiens.
- **Parent traits:** METPO:1004000
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports adaptation of bacterial virulence programs to the human host environment.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports effector delivery as a major mechanism by which bacteria establish human infection.)
- **Existing causal graph summary:** human_pathogen_anthropoid_adaptation: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **human pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/human_pathogen.yaml`.

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
- **Trait label:** human pathogen
- **METPO identifier:** METPO:1004004
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pathogen that infects organisms of the species Homo sapiens.
- **Parent traits:** METPO:1004000
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports adaptation of bacterial virulence programs to the human host environment.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports effector delivery as a major mechanism by which bacteria establish human infection.)
- **Existing causal graph summary:** human_pathogen_anthropoid_adaptation: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **human pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/human_pathogen.yaml`.

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


# Curation report: **human pathogen** (METPO:1004004)

## Executive scope

**Recommended interpretation.** The trait denotes the demonstrated capacity of a microbial **strain or lineage** to establish infection in *Homo sapiens* (NCBITaxon:9606), including opportunistic infection where host state or barrier disruption is required. It is an ecological/host-range class, not a measure of disease severity. The graph endpoint should therefore be **capacity to infect a human host**, with upstream modules for access, colonization, nutrient acquisition, stress survival, immune evasion, replication, tissue damage, and dissemination.

Host association alone is insufficient. Human commensals may carry adhesins, capsules, secretion systems, siderophores, biofilm capacity, or antimicrobial-resistance genes without causing disease. Conversely, a pathogen need not encode every canonical virulence module. Pathogenicity is an emergent host–microbe property rather than an intrinsic consequence of one gene. Host tropism also ranges from human-restricted organisms to broad-host-range zoonoses; spillover into one person is distinct from adaptation that permits sustained human-to-human transmission. Barber and Fitzgerald emphasize that successful host switches require adaptation to distinct anatomy, physiology, immunity, and nutrient availability, and that pathogenicity-related mechanisms include colonization, nutrient acquisition, and immune evasion (barber2024mechanismsofhost pages 1-2).

**Nearby traits to keep separate**

- **Human-associated/commensal:** colonizes humans without demonstrated infection.
- **Pathobiont/opportunistic pathogen:** causes disease only under particular host, microbiome, barrier, or device conditions; still falls under human pathogen when infection is demonstrated, but should retain the qualifier.
- **Virulent:** severity or damage conditional on infection, not synonymous with ability to infect.
- **Zoonotic pathogen:** animal reservoir and transmission route; overlaps only when humans are infected.
- **Serum resistant, intracellular, toxigenic, biofilm forming, or antimicrobial resistant:** component phenotypes, neither individually necessary nor sufficient.
- **Genomically predicted pathogen:** hypothesis requiring phenotypic, epidemiological, or infection-model confirmation.

## Recommended causal architecture

A defensible graph should not use one universal linear chain. Use a convergent architecture:

**human exposure/barrier access → attachment or niche entry → nutrient acquisition + host-stress tolerance + immune evasion → survival/replication in a human niche → tissue invasion, damage, or dysfunction → human infection phenotype**.

Human specificity can enter at several points: adhesin–receptor compatibility, nutrient-receptor compatibility, toxin receptor recognition, or evasion of human complement and cell-autonomous immunity. Small sequence changes may alter these interactions: two substitutions in *Listeria monocytogenes* InlA can shift affinity toward murine E-cadherin, and nucleotide variation in *Salmonella* FimH is associated with host-specific serovars (barber2024mechanismsofhost pages 1-2).

## Candidate nodes by type

### Trait and organism nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| human pathogen | METPO:1004004 | Graph endpoint |
| human host | NCBITaxon:9606 | Host taxon |
| interaction with host | GO:0044406 | Broad process; use more specific child terms where possible |
| pathogenesis | GO:0009405 | Useful intermediate process, not equivalent to endpoint |
| host colonization | Label-only unless a validated local ontology term is selected | Separate asymptomatic colonization from infection |
| dissemination in host | Label-only | Context-dependent |

### Environmental and experimental factors

- Human epithelial or mucosal surface; extracellular matrix; bloodstream; intracellular inclusion/vacuole.
- Wound, disrupted epithelial barrier, indwelling device, dysbiosis, immunocompromise, or elevated glucose: qualifying contexts rather than universal causes.
- Human serum; native serum contains active complement, whereas heat-inactivated serum is an experimental comparator.
- Nutritional immunity: sequestration of iron, zinc, and manganese by transferrin, lactoferrin, hemoglobin-associated pools, and calprotectin.
- Oxidative stress (GO:0006979), host temperature, acid stress, hypoxia, antimicrobial peptides, complement activation (GO:0006956), and immune response (GO:0006955).

### Genes, proteins, transporters, and complexes

- Adhesins: FimH; InlA/InlB; HopQ; Opa; UspA1; fibrinogen-binding proteins; SpsL.
- Host nutrient receptors: TbpA, TdfH, and IsdB.
- Siderophore machinery: enterobactin and EntE/EntF; generic siderophore biosynthesis/export/reuptake.
- Secretion systems and secreted effectors: T3SS and other taxon-specific systems; effectors should be represented individually when perturbation evidence exists.
- Complement-evasion factors: factor-H/C4BP-binding surface proteins, CspA, CHIPS, SCIN, and species-specific IgA proteases.
- Cell-autonomous immune-evasion factors: *Chlamydia trachomatis* GarD and *Shigella flexneri* IpaH7.8.
- Capsule/capsular polysaccharide; extracellular polymeric matrix and biofilm machinery.
- Stress/metabolic regulators: Hfq, ProQ, Skp, superoxide dismutases, isocitrate lyase, and malate synthase.
- Mobile genetic elements: plasmids, prophages, pathogenicity islands, and PICIs. Keep these as evolutionary carriers rather than direct universal causes.

### Chemicals and metabolites

| Entity | Suggested CURIE | Role |
|---|---|---|
| iron(2+) | CHEBI:29033 | Essential metal nutrient |
| zinc(2+) | CHEBI:29105 | Essential metal sequestered by calprotectin |
| thiamine | CHEBI:18385 | Serum-survival intervention in one *K. pneumoniae* strain |
| pyruvate | CHEBI:15361 | Central metabolic intermediate; association requires qualification |
| succinate | CHEBI:30031 | Perturbant that reduced viability in the serum study |
| hydrogen peroxide | CHEBI:16240 | Host oxidative stressor/model oxidant |
| heme | CHEBI:30413 | Iron source acquired from hemoglobin |
| enterobactin | Label-only pending identifier verification | Siderophore; do not guess a CURIE |
| transferrin, calprotectin, hemoglobin | Protein-complex labels | Use host protein identifiers only after species-specific accession review |

### Cellular locations and processes

- Outer membrane (GO:0019867) or bacterial-type cell wall/periplasm, where taxonomically appropriate.
- Extracellular region (GO:0005576), host-cell surface, cytosol, and pathogen-containing vacuole/inclusion.
- Toxin activity (GO:0090729), response to oxidative stress (GO:0006979), complement activation (GO:0006956), biofilm formation, siderophore-mediated iron acquisition, glyoxylate cycle, attachment, invasion, intracellular survival, and resistance to phagocytosis.

Protein accessions should remain label-only until a strain is fixed; TbpA, IsdB, EntE, or EntF are families with organism- and strain-dependent UniProt records.

## Evidence-backed candidate edges

The table below is the high-priority shortlist; the expanded notes following it supply curation snippets and qualifications.

| subject | predicate | object | evidence strength | taxon/context | DOI |
|---|---|---|---|---|---|
| InlA / InlB | binds host receptor with species specificity to promote invasion/colonization | human E-cadherin / human targets | strong, direct; host-specific binding summarized from multiple studies (barber2024mechanismsofhost pages 3-5) | *Listeria monocytogenes*; human vs mouse/rat/guinea pig | 10.1093/femsre/fuae019 |
| CEACAM-binding adhesins (HopQ, Opa, UspA1) | bind selectively to | human CEACAM1, promoting mucosal colonization | strong, direct; human-selective receptor interaction (barber2024mechanismsofhost pages 3-5) | *Helicobacter*, *Neisseria*, *Moraxella* spp. | 10.1093/femsre/fuae019 |
| TbpA | binds / acquires iron from | human transferrin | strong, direct; narrow host specificity for metal acquisition (barber2024mechanismsofhost pages 5-6) | *Neisseria gonorrhoeae*, *N. meningitidis*, *Haemophilus influenzae* | 10.1093/femsre/fuae019 |
| TdfH | binds / scavenges zinc from | human calprotectin | strong, direct; human-selective nutritional immunity evasion (barber2024mechanismsofhost pages 5-6) | *Neisseria gonorrhoeae* | 10.1093/femsre/fuae019 |
| IsdB | scavenges heme more effectively from | human hemoglobin | strong, direct; molecular specificity demonstrated (barber2024mechanismsofhost pages 5-6) | *Staphylococcus aureus* | 10.1093/femsre/fuae019 |
| Enterobactin biosynthesis proteins (EntE, EntF) | are upregulated during | human serum exposure / iron acquisition | strong for taxon-specific serum context; proteomic observation with siderophore increase (moraes2024metabolicreprogrammingof pages 4-5, moraes2024metabolicreprogrammingof pages 7-9) | *Klebsiella pneumoniae* ACH2 in native vs heat-inactivated human serum | 10.1021/acs.jproteome.4c00286 |
| Human-adapted surface proteins for factor H/C4BP recruitment | inhibit | complement activation in human serum | strong, direct but taxon-specific; recurrent mechanism across pathogens (barber2024mechanismsofhost pages 8-10) | *Neisseria* spp., *Borrelia* spp., others | 10.1093/femsre/fuae019 |
| Native human serum exposure | induces | metabolic reprogramming linked to serum resistance | strong in one strain/context; 1250 proteins at 1 h, 1028 at 4 h, 194 exclusive proteins in native serum (moraes2024metabolicreprogrammingof pages 4-5, moraes2024metabolicreprogrammingof pages 1-2) | *K. pneumoniae* ACH2; 1 h and 4 h exposure | 10.1021/acs.jproteome.4c00286 |
| Exogenous thiamine (10 mM) | increases | growth/resistance in human serum | strong intervention in one strain/context (moraes2024metabolicreprogrammingof pages 7-9, moraes2024metabolicreprogrammingof pages 1-2) | *K. pneumoniae* ACH2 in native human serum | 10.1021/acs.jproteome.4c00286 |
| Exogenous succinate (50 mM) | decreases | cell viability / serum resistance | strong intervention in one strain/context (moraes2024metabolicreprogrammingof pages 7-9) | *K. pneumoniae* ACH2 in native human serum | 10.1021/acs.jproteome.4c00286 |
| Glyoxylate cycle activation | contributes to | serum survival / stress response | moderate; supported by exclusive detection of isocitrate lyase and malate synthase plus perturbation logic (moraes2024metabolicreprogrammingof pages 5-6, moraes2024metabolicreprogrammingof pages 7-9) | *K. pneumoniae* ACH2 after 4 h serum exposure | 10.1021/acs.jproteome.4c00286 |
| Horizontal gene transfer / gene acquisition and loss | drives | host adaptation and emergence of human-pathogenic traits | strong, general but broad; includes virulence determinants and host-specific factors (barber2024mechanismsofhost pages 1-2, barber2024mechanismsofhost pages 2-3) | broad bacterial pathogens | 10.1093/femsre/fuae019 |


*Table: This compact curation matrix lists the strongest candidate causal edges for the METPO human pathogen trait using only previously gathered evidence. It is useful as a short-list of high-priority edges for TraitMech curation, with strength, context, and DOI captured in one place.*

| # | Proposed subject–predicate–object | Supporting snippet | Reference and curation note |
|---|---|---|---|
| 1 | **InlA — binds — human E-cadherin** | “InlA binds to human and guinea pig E-cadherin protein, but does not recognize the mouse or rat orthologs.” | 10.1093/femsre/fuae019, published 13 July 2024. Supports receptor compatibility as a host-range mechanism. *Listeria*-specific; do not generalize InlA to all human pathogens (barber2024mechanismsofhost pages 3-5).
| 2 | **InlA/InlB-mediated receptor binding — promotes — host-cell invasion** | InlA and InlB are described as “two surface proteins essential for host cell invasion.” | Same source. Strong mechanistic class edge, but individual receptor pairings should be curated separately (barber2024mechanismsofhost pages 3-5).
| 3 | **HopQ/Opa/UspA1 — selectively bind — human CEACAM1** | Human-specific *Helicobacter*, *Neisseria*, and *Moraxella* encode these adhesins with selectivity for human CEACAM1; binding “subsequently mediates host colonization.” | Same source. Good parallel examples of convergent human-specific attachment, not one cross-taxon molecular complex (barber2024mechanismsofhost pages 3-5).
| 4 | **streptokinase — activates human plasminogen — clot breakdown/dissemination** | Injection of mice with human plasminogen “was sufficient to enhance virulence of *S. pyogenes*,” and transgenic mice expressing human plasminogen rapidly succumbed. | Same source. Strong intervention evidence for a human-specific interaction; taxon-specific (barber2024mechanismsofhost pages 3-5).
| 5 | **host metal sequestration — inhibits — bacterial growth** | Host sequestration of transition metals “presents a major barrier to bacterial growth” and underlies nutritional immunity. | Same source. Broad host-defense edge; strength is established collectively, but exact metal dependence varies by species and niche (barber2024mechanismsofhost pages 5-6).
| 6 | **siderophore secretion/reuptake — promotes — metal acquisition** | Siderophores “effectively compete with host proteins for metals”; metal-bound siderophores are then reacquired through bacterial surface receptors. | Same source. Suitable generic module, but presence does not diagnose pathogenicity because environmental and commensal bacteria also use siderophores (barber2024mechanismsofhost pages 5-6).
| 7 | **TbpA — binds human transferrin — iron acquisition/host tropism** | Rapidly evolving transferrin regions match the TbpA-binding surface; the findings suggest iron acquisition drove host adaptation and restricted tropism. | Same source. Strong evolutionary and structural support; direct endpoint edge to METPO:1004004 would still be too broad (barber2024mechanismsofhost pages 5-6).
| 8 | **IsdB — preferentially binds — human hemoglobin** | *S. aureus* IsdB “bind[s] human hemoglobin more effectively than mouse”; a few substitutions alter primate specificity. | Same source. Supports host-specific heme acquisition (barber2024mechanismsofhost pages 5-6).
| 9 | **TdfH — binds human calprotectin — zinc scavenging** | TdfH binds calprotectin to mediate zinc scavenging and is selective for human calprotectin relative to other mammals. | Same source. Strong, human-specific edge for *N. gonorrhoeae* (barber2024mechanismsofhost pages 5-6).
| 10 | **factor-H/C4BP recruitment — inhibits — complement activation** | Surface proteins binding factor H or C4BP occur in diverse pathogens; human-adapted *Neisseria* inhibit complement in human serum but not other mammalian serum. | Same source. Curate at species/protein level rather than as a universal pathogen property (barber2024mechanismsofhost pages 8-10).
| 11 | **CspA–factor H compatibility — promotes — complement evasion and host transmission** | Variation in factor H and CspA “directly correlated with complement evasion and the ability to transmit to distinct mammalian or avian hosts.” | Same source. Strong for *Borrelia* host tropism, but not specifically human in every species (barber2024mechanismsofhost pages 8-10).
| 12 | **GarD — blocks — ubiquitin decoration of *C. trachomatis* inclusions** | GarD blocks ubiquitin decoration that would normally lead to bacterial clearance and protects inclusions from RNF213 recognition. | Same source. Strong cell-autonomous immune-evasion edge; *C. trachomatis*-specific (barber2024mechanismsofhost pages 7-8).
| 13 | **IpaH7.8 — promotes degradation of — human gasdermin D** | The *Shigella* ubiquitin ligase targets gasdermin D for proteasomal degradation; activity is effective against human but not mouse gasdermin D. | Same source. Strong host-specific anti-pyroptosis mechanism (barber2024mechanismsofhost pages 7-8).
| 14 | **native human serum exposure — induces — enterobactin machinery** | At 1 h, EntE/EntF and enterobactin-related iron uptake were elevated; siderophore production was higher in native serum at both sampled times. | 10.1021/acs.jproteome.4c00286, published 3 October 2024. Direct proteomic/assay evidence in *K. pneumoniae* ACH2, not a universal response (moraes2024metabolicreprogrammingof pages 1-2, moraes2024metabolicreprogrammingof pages 7-9, moraes2024metabolicreprogrammingof pages 4-5).
| 15 | **human serum exposure — induces — time-dependent metabolic reprogramming** | Native versus heat-inactivated serum was tested at 1 and 4 h; 1,250 and 1,028 proteins were detected in native serum, with 194 proteins exclusive to that condition. | Same source. Strong experimental context, but differential abundance does not by itself establish causal necessity (moraes2024metabolicreprogrammingof pages 1-2, moraes2024metabolicreprogrammingof pages 4-5).
| 16 | **exogenous thiamine — increases — growth/resistance in native serum** | “Exogenous thiamine supplementation in serum enhanced resistance.” The intervention used 10 mM thiamine. | Same source. A direct perturbation edge, but one strain and high in-vitro concentration; mark **taxon- and assay-specific** (moraes2024metabolicreprogrammingof pages 7-9).
| 17 | **glyoxylate-cycle activation — supports — serum survival/stress response** | Isocitrate lyase and malate synthase were exclusive to serum-exposed conditions at 4 h; authors conclude the cycle “appears crucial during serum exposure.” | Same source. **Moderate/inferred**: pathway activation plus perturbation logic, without a clean gene knockout in ACH2 (moraes2024metabolicreprogrammingof pages 7-9, moraes2024metabolicreprogrammingof pages 5-6).
| 18 | **exogenous succinate — decreases — cell viability/serum resistance** | Addition of 50 mM succinate decreased CFU/viability and was interpreted as possible catabolite repression of the glyoxylate cycle. | Same source. Direct phenotype but proposed pathway is **inferred**; succinate also reduced viability in control conditions, limiting specificity (moraes2024metabolicreprogrammingof pages 7-9, moraes2024metabolicreprogrammingof pages 5-6).
| 19 | **horizontal gene transfer — enables — host adaptation** | Adaptation can arise through nucleotide changes, gene acquisition/deletion, rearrangement, and HGT; HGT is described as a “major driver” of host adaptation. | 10.1093/femsre/fuae019. Curate as an evolutionary provenance edge to specific acquired modules, not directly to human pathogenicity without lineage evidence (barber2024mechanismsofhost pages 1-2, barber2024mechanismsofhost pages 2-3).
| 20 | **capsule/biofilm formation — inhibits — phagocytosis or complement-mediated clearance** | Foundational synthesis identifies capsules and biofilms as protection against phagocytosis and complement-mediated lysis. | 10.1007/978-3-319-67651-7_1, 2018. Mechanistically credible, but capsule chemistry and effect differ by taxon; prioritize newer organism-specific perturbation studies before adding a universal edge (johnson2018bacterialvirulencefactors pages 1-3).

## Recent findings and quantitative evidence

The most directly useful 2024 experiment is Moraes et al.'s *K. pneumoniae* ACH2 serum study. It used 40% serum, native and heat-inactivated controls, 1- and 4-h timepoints, and three biological plus three technical replicates. Differential abundance used a two-fold threshold with *p* < 0.05 (moraes2024metabolicreprogrammingof pages 2-3). Native-serum proteomics identified 1,250 proteins at 1 h and 1,028 at 4 h; 194 proteins, 15.5%, were exclusive to native serum. At 1 h, RpsD was upregulated 43.33-fold and ecotin downregulated 12.5-fold. At 4 h, Fe-SOD and Cu/Zn-SOD were downregulated 21.73- and 13.75-fold, respectively (moraes2024metabolicreprogrammingof pages 4-5). These are useful state-transition observations, but they should not be encoded as universal human-pathogen mechanisms.

The strongest causal perturbations in that study are thiamine supplementation and succinate addition. Ten millimolar thiamine increased resistance in native serum, whereas 50 mM succinate reduced viability. Glycine at 100 mM had no detectable serum-sensitizing effect (moraes2024metabolicreprogrammingof pages 7-9). The study's authors appropriately state that further experiments are needed to establish the detailed molecular relationship to serum resistance (moraes2024metabolicreprogrammingof pages 9-10).

A complementary 2024 expert review identifies receptor compatibility as a recurring determinant of host range. It highlights human-selective CEACAM adhesins, TbpA–transferrin, TdfH–calprotectin, IsdB–hemoglobin, complement-regulator recruitment, and human-specific antagonism of pyroptosis. The authors' broader analysis is that colonization, nutrient acquisition, and immune evasion are key stages of bacterial host adaptation, while metabolic host specificity remains comparatively underexplored (barber2024mechanismsofhost pages 1-2, barber2024mechanismsofhost pages 6-7, barber2024mechanismsofhost pages 5-6).

## Current applications and implementation relevance

1. **Genome-informed surveillance.** Virulence modules, mobile elements, receptor-binding alleles, and host-adaptation signatures can prioritize isolates for experimental testing. However, whole-genome detection should produce a risk score or candidate mechanism, not an automatic METPO:1004004 assertion.
2. **Humanized infection models.** Human plasminogen mice and receptor-humanized systems overcome false negatives caused by species-specific interactions. The streptokinase/plasminogen example demonstrates why ordinary mouse models can underestimate human-pathogen virulence (barber2024mechanismsofhost pages 3-5).
3. **Anti-virulence targets.** Adhesin–receptor interactions, TbpA/TdfH/IsdB nutrient uptake, complement-evasion proteins, secretion-system effectors, and capsule synthesis are candidate therapeutic or vaccine targets. Their attraction is mechanistic specificity, but redundancy and strain variation must be assessed.
4. **Metabolic sensitization.** The *K. pneumoniae* serum study suggests glyoxylate-cycle disruption or nutrient-pathway interference as possible adjunctive strategies. This remains preclinical and strain-specific; the succinate concentrations and nonspecific viability effect preclude direct clinical extrapolation (moraes2024metabolicreprogrammingof pages 7-9, moraes2024metabolicreprogrammingof pages 5-6).
5. **Diagnostic assay design.** Native-serum survival, epithelial adhesion, complement deposition, phagocytosis, organoid infection, and humanized receptor assays provide phenotype-level validation downstream of genomic prediction.

## Recommended YAML curation policy

Use evidence grades:

- **A—direct causal:** deletion/complementation, purified binding with species comparison, receptor substitution, inhibitor, metabolite perturbation, or humanized-host experiment changes infection-related phenotype.
- **B—strong mechanistic:** structural/biochemical compatibility plus infection evidence, but no direct perturbation in the focal strain.
- **C—associative:** omics abundance, comparative-genomic enrichment, clinical association, or evolutionary signature without functional validation.

Every edge should carry `taxon`, `strain`, `host`, `anatomical_context`, `assay`, and `evidence_strength`. Prefer intermediate phenotypes over shortcuts such as `siderophore -> human pathogen`. A better chain is `enterobactin biosynthesis -> iron acquisition in serum -> growth under nutritional immunity -> bloodstream survival`, with the final link to human infection supported separately.

## Claims not ready for TraitMech curation

- **No single “human-pathogen gene.”** Adhesins, capsules, secretion systems, siderophores, stress enzymes, biofilms, and AMR genes also occur in nonpathogens.
- **Do not infer phenotype from gene presence alone.** Expression, allelic specificity, regulation, genomic background, host receptor compatibility, inoculum, route, and host state matter.
- **Do not universalize taxon-specific edges.** InlA, TdfH, GarD, IpaH7.8, CspA, and the ACH2 metabolic response belong in organism-specific branches.
- **Do not equate serum resistance with human pathogenicity.** It is relevant principally to bloodstream or extracellular dissemination and is unnecessary for pathogens restricted to other niches.
- **Do not curate succinate → glyoxylate-cycle repression as established.** The viability effect was observed, but pathway mediation was proposed rather than genetically demonstrated; control viability also decreased (moraes2024metabolicreprogrammingof pages 7-9, moraes2024metabolicreprogrammingof pages 5-6).
- **Do not curate decreased SOD abundance as improved oxidative-stress resistance.** The 2024 study observed downregulation and reduced activity; compensatory metabolites were hypothesized, not proven (moraes2024metabolicreprogrammingof pages 4-5, moraes2024metabolicreprogrammingof pages 6-7).
- **Do not treat biofilm formation as uniformly pathogenic.** Biofilms can be commensal or environmental and can even contribute to colonization resistance.
- **Do not collapse colonization into infection.** Adhesion can be necessary but may terminate in harmless carriage.
- **Do not assume human restriction from a human isolate.** Comparative host-range or epidemiological evidence is required.
- **Do not add unverified CURIEs.** Species-specific protein accessions and identifiers for enterobactin, serum, capsule subclasses, and anatomical niches should be resolved during implementation.

## DOI-first bibliography

1. Barber MF, Fitzgerald JR. **Mechanisms of host adaptation by bacterial pathogens.** *FEMS Microbiology Reviews* 48, fuae019. Advance publication **13 July 2024**. DOI: [10.1093/femsre/fuae019](https://doi.org/10.1093/femsre/fuae019). Principal recent source for scope, host specificity, colonization, nutrient acquisition, immune evasion, and evolutionary mechanisms (barber2024mechanismsofhost pages 1-2).
2. Moraes ANS et al. **Metabolic Reprogramming of *Klebsiella pneumoniae* Exposed to Serum and Its Potential Implications in Host Immune System Evasion and Resistance.** *Journal of Proteome Research* 23:4896–4906. Published **3 October 2024**; accepted 25 September 2024. DOI: [10.1021/acs.jproteome.4c00286](https://doi.org/10.1021/acs.jproteome.4c00286). Principal recent experimental source for serum-induced iron acquisition and metabolic adaptation (moraes2024metabolicreprogrammingof pages 1-2).
3. Johnson DI. **Bacterial Virulence Factors.** In *Bacterial Pathogens and Their Virulence Factors*. **2018**. DOI: [10.1007/978-3-319-67651-7_1](https://doi.org/10.1007/978-3-319-67651-7_1). Foundational source for host–pathogen framing and major virulence-factor classes (johnson2018bacterialvirulencefactors pages 1-3).
4. Chen Y et al. **Pathogen virulence genes: Advances, challenges and future directions in infectious disease research.** *International Journal of Molecular Medicine* 56:1–32. **August 2025**. DOI: [10.3892/ijmm.2025.5614](https://doi.org/10.3892/ijmm.2025.5614). Supplemental synthesis of adhesins, T3SS, capsule, biofilm, and mobile-element coupling; useful for future updates rather than the 2023–2024 priority set (chen2025pathogenvirulencegenes pages 1-2).
5. Zhang M et al. **Comparative genomics reveals key adaptive mechanisms in pathogen host-niche specialization.** *Frontiers in Microbiology* 16. **June 2025**. DOI: [10.3389/fmicb.2025.1543610](https://doi.org/10.3389/fmicb.2025.1543610). A 4,366-genome analysis reporting enrichment of adhesion and immune-modulation factors in human-associated bacteria; associative evidence only (zhang2025comparativegenomicsreveals pages 1-2).

## Bottom-line recommendation

For `human_pathogen.yaml`, curate a **modular, strain-qualified graph**, not a checklist of virulence genes. The strongest reusable mechanisms are human-receptor-specific attachment, acquisition of host-sequestered nutrients, evasion of human complement or cell-autonomous immunity, and survival in human physiological niches. Connect these modules to METPO:1004004 only through demonstrated infection-relevant phenotypes. The 2024 serum-metabolism findings are valuable organism-specific branches, but thiamine, succinate, and glyoxylate-cycle claims should not be promoted to universal determinants of human pathogenicity.

References

1. (barber2024mechanismsofhost pages 1-2): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

2. (barber2024mechanismsofhost pages 3-5): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

3. (barber2024mechanismsofhost pages 5-6): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

4. (moraes2024metabolicreprogrammingof pages 4-5): Amanda Naiara Silva Moraes, Juliana Miranda Tatara, Rafael Lopes da Rosa, Franciele Maboni Siqueira, Guilherme Domingues, Markus Berger, Jorge Almeida Guimarães, Afonso Luís Barth, Patricia Orlandi Barth, John R. Yates, Walter Orlando Beys-da-Silva, and Lucélia Santi. Metabolic reprogramming of klebsiella pneumoniae exposed to serum and its potential implications in host immune system evasion and resistance. Journal of Proteome Research, 23:4896-4906, Oct 2024. URL: https://doi.org/10.1021/acs.jproteome.4c00286, doi:10.1021/acs.jproteome.4c00286. This article has 6 citations and is from a peer-reviewed journal.

5. (moraes2024metabolicreprogrammingof pages 7-9): Amanda Naiara Silva Moraes, Juliana Miranda Tatara, Rafael Lopes da Rosa, Franciele Maboni Siqueira, Guilherme Domingues, Markus Berger, Jorge Almeida Guimarães, Afonso Luís Barth, Patricia Orlandi Barth, John R. Yates, Walter Orlando Beys-da-Silva, and Lucélia Santi. Metabolic reprogramming of klebsiella pneumoniae exposed to serum and its potential implications in host immune system evasion and resistance. Journal of Proteome Research, 23:4896-4906, Oct 2024. URL: https://doi.org/10.1021/acs.jproteome.4c00286, doi:10.1021/acs.jproteome.4c00286. This article has 6 citations and is from a peer-reviewed journal.

6. (barber2024mechanismsofhost pages 8-10): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

7. (moraes2024metabolicreprogrammingof pages 1-2): Amanda Naiara Silva Moraes, Juliana Miranda Tatara, Rafael Lopes da Rosa, Franciele Maboni Siqueira, Guilherme Domingues, Markus Berger, Jorge Almeida Guimarães, Afonso Luís Barth, Patricia Orlandi Barth, John R. Yates, Walter Orlando Beys-da-Silva, and Lucélia Santi. Metabolic reprogramming of klebsiella pneumoniae exposed to serum and its potential implications in host immune system evasion and resistance. Journal of Proteome Research, 23:4896-4906, Oct 2024. URL: https://doi.org/10.1021/acs.jproteome.4c00286, doi:10.1021/acs.jproteome.4c00286. This article has 6 citations and is from a peer-reviewed journal.

8. (moraes2024metabolicreprogrammingof pages 5-6): Amanda Naiara Silva Moraes, Juliana Miranda Tatara, Rafael Lopes da Rosa, Franciele Maboni Siqueira, Guilherme Domingues, Markus Berger, Jorge Almeida Guimarães, Afonso Luís Barth, Patricia Orlandi Barth, John R. Yates, Walter Orlando Beys-da-Silva, and Lucélia Santi. Metabolic reprogramming of klebsiella pneumoniae exposed to serum and its potential implications in host immune system evasion and resistance. Journal of Proteome Research, 23:4896-4906, Oct 2024. URL: https://doi.org/10.1021/acs.jproteome.4c00286, doi:10.1021/acs.jproteome.4c00286. This article has 6 citations and is from a peer-reviewed journal.

9. (barber2024mechanismsofhost pages 2-3): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

10. (barber2024mechanismsofhost pages 7-8): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

11. (johnson2018bacterialvirulencefactors pages 1-3): Douglas I. Johnson. Bacterial virulence factors. ArXiv, pages 1-38, Nov 2018. URL: https://doi.org/10.1007/978-3-319-67651-7\_1, doi:10.1007/978-3-319-67651-7\_1. This article has 79 citations.

12. (moraes2024metabolicreprogrammingof pages 2-3): Amanda Naiara Silva Moraes, Juliana Miranda Tatara, Rafael Lopes da Rosa, Franciele Maboni Siqueira, Guilherme Domingues, Markus Berger, Jorge Almeida Guimarães, Afonso Luís Barth, Patricia Orlandi Barth, John R. Yates, Walter Orlando Beys-da-Silva, and Lucélia Santi. Metabolic reprogramming of klebsiella pneumoniae exposed to serum and its potential implications in host immune system evasion and resistance. Journal of Proteome Research, 23:4896-4906, Oct 2024. URL: https://doi.org/10.1021/acs.jproteome.4c00286, doi:10.1021/acs.jproteome.4c00286. This article has 6 citations and is from a peer-reviewed journal.

13. (moraes2024metabolicreprogrammingof pages 9-10): Amanda Naiara Silva Moraes, Juliana Miranda Tatara, Rafael Lopes da Rosa, Franciele Maboni Siqueira, Guilherme Domingues, Markus Berger, Jorge Almeida Guimarães, Afonso Luís Barth, Patricia Orlandi Barth, John R. Yates, Walter Orlando Beys-da-Silva, and Lucélia Santi. Metabolic reprogramming of klebsiella pneumoniae exposed to serum and its potential implications in host immune system evasion and resistance. Journal of Proteome Research, 23:4896-4906, Oct 2024. URL: https://doi.org/10.1021/acs.jproteome.4c00286, doi:10.1021/acs.jproteome.4c00286. This article has 6 citations and is from a peer-reviewed journal.

14. (barber2024mechanismsofhost pages 6-7): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

15. (moraes2024metabolicreprogrammingof pages 6-7): Amanda Naiara Silva Moraes, Juliana Miranda Tatara, Rafael Lopes da Rosa, Franciele Maboni Siqueira, Guilherme Domingues, Markus Berger, Jorge Almeida Guimarães, Afonso Luís Barth, Patricia Orlandi Barth, John R. Yates, Walter Orlando Beys-da-Silva, and Lucélia Santi. Metabolic reprogramming of klebsiella pneumoniae exposed to serum and its potential implications in host immune system evasion and resistance. Journal of Proteome Research, 23:4896-4906, Oct 2024. URL: https://doi.org/10.1021/acs.jproteome.4c00286, doi:10.1021/acs.jproteome.4c00286. This article has 6 citations and is from a peer-reviewed journal.

16. (chen2025pathogenvirulencegenes pages 1-2): Yun Chen, Xiaolong Wu, Chengcheng Xu, Jianxiang Huang, Lingyu Zhang, Peng-Fei Qiu, Danlin Zheng, Wang Chen, and Shuyao Zhang. Pathogen virulence genes: advances, challenges and future directions in infectious disease research (review). International Journal of Molecular Medicine, 56:1-32, Aug 2025. URL: https://doi.org/10.3892/ijmm.2025.5614, doi:10.3892/ijmm.2025.5614. This article has 35 citations and is from a peer-reviewed journal.

17. (zhang2025comparativegenomicsreveals pages 1-2): Menglu Zhang, Longxi Han, Caizhi Liao, Weiheng Su, and Chunlai Jiang. Comparative genomics reveals key adaptive mechanisms in pathogen host-niche specialization. Frontiers in Microbiology, Jun 2025. URL: https://doi.org/10.3389/fmicb.2025.1543610, doi:10.3389/fmicb.2025.1543610. This article has 9 citations and is from a peer-reviewed journal.