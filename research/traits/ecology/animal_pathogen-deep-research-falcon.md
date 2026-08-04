---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T22:35:05.128001'
end_time: '2026-08-03T22:42:37.708409'
duration_seconds: 452.58
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: animal pathogen
  trait_identifier: METPO:1004002
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: animal_pathogen
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pathogen that infects organisms in the kingdom Metazoa.
  parent_traits: METPO:1004000
  synonyms: ''
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162938: virulence factors
    (Virulence-factor review supports adaptation of bacterial virulence programs to
    animal hosts.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems
    review supports T3SS/T6SS effector delivery as a major mechanism by which bacteria
    infect animal hosts.)'
  causal_graph_summary: 'animal_pathogen_metazoan_adaptation: 17 nodes, 15 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 59
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** animal pathogen
- **METPO identifier:** METPO:1004002
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pathogen that infects organisms in the kingdom Metazoa.
- **Parent traits:** METPO:1004000
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports adaptation of bacterial virulence programs to animal hosts.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports T3SS/T6SS effector delivery as a major mechanism by which bacteria infect animal hosts.)
- **Existing causal graph summary:** animal_pathogen_metazoan_adaptation: 17 nodes, 15 edges

## Research Objective

Research the microbial trait **animal pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/animal_pathogen.yaml`.

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
- **Trait label:** animal pathogen
- **METPO identifier:** METPO:1004002
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pathogen that infects organisms in the kingdom Metazoa.
- **Parent traits:** METPO:1004000
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports adaptation of bacterial virulence programs to animal hosts.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports T3SS/T6SS effector delivery as a major mechanism by which bacteria infect animal hosts.)
- **Existing causal graph summary:** animal_pathogen_metazoan_adaptation: 17 nodes, 15 edges

## Research Objective

Research the microbial trait **animal pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/animal_pathogen.yaml`.

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


# Curation report: **animal pathogen** (METPO:1004002)

## Executive curation recommendation

The trait should represent the **realized, strain-level capacity of a microorganism to establish infection in a host belonging to Metazoa**, rather than the mere presence of a virulence-associated gene. A defensible general graph should center on five recurring functions: **host attachment/colonization, acquisition of host-limited nutrients, resistance or manipulation of host defenses, host damage, and persistence/dissemination**. Individual adhesins, secretion systems, toxins, capsules, and metabolic pathways should normally be modeled as taxon- or niche-specific implementations of those functions.

A 2024 authoritative review frames bacterial host adaptation around colonization, nutrient acquisition, and immune evasion and emphasizes that host range varies from single-host restriction to infection of diverse vertebrates and invertebrates. It also notes that successful establishment requires adaptation to host-specific anatomy, physiology, immunity, and nutrient availability (published 13 July 2024; https://doi.org/10.1093/femsre/fuae019). (barber2024mechanismsofhost pages 1-2)

| module | recommended graph status | representative nodes | strongest evidence type | principal caveat |
|---|---|---|---|---|
| Adhesion / host attachment | core | adhesin; fimbriae/pili; host receptor (E-cadherin, CEACAM, fibrinogen); biofilm-associated protein BAP | Broad review plus experimental host-specific binding examples across pathogens (barber2024mechanismsofhost pages 3-5, barber2024mechanismsofhost pages 5-6, lucidi2024pathogenicityandvirulence pages 4-5) | Exact adhesin-receptor pairs are often host- and taxon-specific, so curate generic adhesion as core and specific receptors as context/taxon-specific. |
| Secretion systems / effector export | taxon-specific | type III secretion system; type I secretion system; type II secretion system; secreted effector; RTX toxin; LipA lipase | Strong mechanistic evidence in specific Gram-negative pathogens, including in vivo mutant phenotypes in *A. baumannii* (barber2024mechanismsofhost pages 7-8, lucidi2024pathogenicityandvirulence pages 5-7) | No single secretion system is universal across animal pathogens; avoid generalizing one apparatus to the whole trait. |
| Toxins / host damage | core | toxin; pore-forming toxin; leukocidin; superantigen; urease; exotoxin A | Broad cross-pathogen review plus animal infection data and host-specific toxin tropism (barber2024mechanismsofhost pages 10-11, eidaroos2024theimpactof pages 1-2, yang2024unveilingthehidden pages 2-4) | Toxin classes are widespread but highly heterogeneous; individual toxins should usually be taxon-specific nodes. |
| Capsule / complement evasion / anti-phagocytosis | core | capsule/capsular polysaccharide; factor H-binding protein; C4BP-binding protein; SCIN; CHIPS; C3b masking | Broad mechanistic review with direct complement-evasion and capsule-function evidence (barber2024mechanismsofhost pages 8-10, gao2024bacterialcapsulesoccurrence pages 5-7, gao2024bacterialcapsulesoccurrence pages 3-5) | Capsules can also reduce adhesion or vary by serotype; effects are sometimes conditional rather than uniformly positive for pathogenesis. |
| Iron acquisition / nutritional immunity escape | core | siderophore; TonB-dependent receptor; transferrin-binding protein A (TbpA); hemoglobin receptor IsdB; calprotectin-binding receptor TdfH; heme uptake | Strong broad evidence from host-pathogen iron reviews and host-specific receptor examples (barber2024mechanismsofhost pages 5-6, ullah2023keyplayersin pages 1-2, stelitano2023ironacquisitionand pages 2-4) | Iron acquisition is broadly important, but named receptors are often host-restricted or lineage-specific; curate generic module as core, named proteins as context/taxon-specific. |
| Quorum sensing / biofilm persistence | context | quorum sensing; autoinducer; LuxI/LuxR-like system; Agr; biofilm; extracellular matrix/EPS | Reviews and animal/clinical isolate studies linking QS to virulence/biofilm and biofilm to antimicrobial tolerance (juszczukkubiak2024molecularaspectsof pages 2-3, juszczukkubiak2024molecularaspectsof pages 5-7, eidaroos2024theimpactof pages 1-2) | Important for persistence and regulation, but not required for all animal pathogens or all infection stages; better as context unless trait graph models chronicity/persistence. |
| Metabolic host adaptation / host nutrient use | context | lactose utilization; carbohydrate transporter; phenylacetic acid metabolism; hydrogenase/FHL; nickel-dependent urease maturation | Good recent evidence for host-specific nutrient adaptation in selected pathogens (barber2024mechanismsofhost pages 6-7, yang2024unveilingthehidden pages 2-4, lucidi2024pathogenicityandvirulence pages 4-5) | Often reflects niche-specific adaptation (mastitis, urinary tract, chronic infection) rather than a universal determinant of animal pathogenicity. |
| Environmental cues / host microenvironment sensing | context | urea; anaerobiosis; stationary phase; osmotic stress; elevated glucose; folate stress / antibiotic exposure | Specific mechanistic studies showing cue-dependent induction of virulence modules (barber2024mechanismsofhost pages 6-7, yang2024unveilingthehidden pages 2-4, lucidi2024pathogenicityandvirulence pages 4-5) | Cue-response relationships are highly condition-, tissue-, and taxon-specific; curate only when linked to a defined infection niche. |


*Table: This table prioritizes mechanistic modules for curation of the microbial trait animal pathogen, distinguishing broadly curatable core processes from context-dependent or taxon-specific mechanisms. It is useful for deciding which nodes and edges should enter a general TraitMech graph versus remain lineage- or niche-restricted.*

## 1. Trait scope and boundaries

### In scope

* **Phenotype:** reproducible ability of a microbial strain to colonize or invade a Metazoan host and produce an infection phenotype under natural or experimentally justified conditions.
* **Host range:** humans, livestock, companion animals, wildlife, fish, and invertebrate animals all qualify. “Animal pathogen” does not imply zoonosis or broad host range.
* **Mechanistic realization:** attachment to host tissue, invasion or extracellular persistence, acquisition of limiting nutrients, evasion or manipulation of immunity, host-cell/tissue damage, and dissemination.
* **Evidence standard:** infection of a relevant animal or validated host-cell/tissue model, preferably supported by genetic perturbation, complementation, biochemical interaction, or epidemiological attribution.

### Important distinctions

1. **Pathogenicity versus virulence.** Pathogenicity is the ability to cause infection/disease; virulence is its degree or severity. A low-virulence pathogen still belongs in the class.
2. **Colonizer/commensal versus pathogen.** Colonization may precede infection but is not sufficient by itself. Staphylococci illustrate this boundary: all are members of mammalian epithelial microbiota, yet only some species or lineages commonly cause disease, and colonization is a frequent source of infection (published 26 September 2023; https://doi.org/10.3390/ijms241914587). (cheung2023virulencemechanismsof pages 1-2)
3. **Opportunistic pathogen.** Opportunism is compatible with the trait, but host compromise, barrier disruption, device implantation, or dysbiosis should be represented as contextual enabling factors—not as microbial mechanisms.
4. **Zoonotic/vector-borne/reservoir status.** These are transmission/ecological traits. A strain can be an animal pathogen without transmission between animal species.
5. **Toxigenic but non-invasive microbes.** Intoxication from a preformed toxin does not automatically demonstrate infection; distinguish toxin producer, foodborne intoxication, and pathogen.
6. **Plant pathogens and environmental survival.** These do not satisfy METPO:1004002 unless the same strain has evidence of infection in a Metazoan host.
7. **Virulence-gene detection alone.** PCR detection, genome annotation, or in-vitro cytotoxicity is supporting evidence but not sufficient to assert the class.

Host specificity is often quantitative rather than absolute. For example, *S. pseudintermedius* is a major canine pathogen but occurs at lower rates in other hosts; cats reportedly have an approximately 6.5-fold lower colonization rate than dogs. Therefore, host-specificity assertions should be attached to strain/lineage and host nodes rather than inferred from the species name alone. (cheung2023virulencemechanismsof pages 9-10)

## 2. Candidate nodes grouped by type

Only high-confidence identifiers are supplied below. Label-only nodes are intentional where a universal identifier would be misleading or requires database verification.

### Trait, host, and environmental nodes

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| animal pathogen | microbial trait | **METPO:1004002** | Target node. |
| Metazoa | host taxon | **NCBITaxon:33208** | Use a more specific host taxon whenever evidence permits. |
| host epithelial surface | anatomical/environmental context | label-only | Includes skin and gastrointestinal, respiratory, and urogenital mucosa. |
| bloodstream | host compartment | label-only | Iron-rich but complement-exposed systemic niche. |
| intracellular pathogen-containing compartment | localization | label-only | Relevant to *Salmonella*, *Legionella*, *Chlamydia*, and mycobacteria. |
| low iron / nutritional immunity | host environmental factor | label-only | Host sequestration of Fe and other metals. |
| urea-rich urinary tract | host environmental factor | label-only | Relevant to urease-positive urinary pathogens. |
| anaerobiosis | environmental factor | **ENVO term to verify** | Induces formate-hydrogenlyase-associated genes in *Proteus*. |
| elevated host glucose | environmental factor | label-only | Contextual risk factor; affects both host immunity and pathogen physiology. |
| osmotic stress | experimental/environmental factor | label-only | Capsule and envelope responses are taxon-specific. |
| subinhibitory trimethoprim–sulfamethoxazole | experimental factor | label-only | Reported to induce phenylacetic-acid-dependent biofilm regulation in *A. baumannii*. |

### Biological processes and functions

| Candidate node | Suggested grounding | Role |
|---|---|---|
| adhesion to host | **GO:0044406** | Initial attachment/colonization process; confirm current GO label before import. |
| biofilm formation | **GO:0042710** | Persistence on host or abiotic surfaces. |
| quorum sensing | **GO:0009372** | Density-dependent regulation of collective behavior. |
| pathogenesis | **GO:0009405** | Broad process node; avoid circular use as the sole parent of the target trait. |
| protein secretion / effector translocation | GO term dependent on system | Delivery or export of virulence proteins. |
| evasion or modulation of host immunity | label-only or specific GO term | Capsule, complement regulators, antibody proteases, intracellular effectors. |
| nutritional immunity escape | label-only | Acquisition of host-sequestered Fe, Zn, or Mn. |
| host-cell lysis / tissue damage | label-only | Toxins, proteases, urease-generated ammonia. |
| dissemination | label-only | Movement from colonized site to deeper tissue or bloodstream. |

### Molecular entities, structures, and complexes

* **Adhesion:** adhesin; fimbriae/pili; FimH; InlA; E-cadherin; CEACAM-binding adhesins; fibrinogen-binding proteins; *S. pseudintermedius* SpsD/SpsO; *A. baumannii* Csu pili, type IV pili, BAP/BLP1/BLP2.
* **Secretion:** T1SS, T2SS, T3SS; T1SSa; RTX toxin; LipA lipase; CpaA metalloprotease; secreted effector.
* **Immune evasion:** capsule/capsular polysaccharide; factor H; C4BP; C3b/iC3b; SCIN; CHIPS; protein A; IgA protease; GarD; IpaH7.8.
* **Nutrient acquisition:** siderophore; enterobactin; TonB-dependent receptor; TbpA; IsdB; TdfH; hemophore; transferrin; lactoferrin; hemoglobin/heme; Fur; siderophore uptake ABC transporter.
* **Regulation and persistence:** autoinducer; AHL; AIP; LuxI/LuxR; LasI/LasR; RhlI/RhlR; AgrA/AgrC/RNAIII; EPS matrix; PNAG/PIA; Pel/Psl.
* **Damage/metabolism:** leukocidin; pore-forming toxin; superantigen; exotoxin A; elastase; pyocyanin; urease UreABC; UreR; nickel uptake/maturation proteins UreDEFG; hydrogenase/FHL modules Hyb/Hyf; ammonia.

### Chemicals

| Entity | Grounding | Note |
|---|---|---|
| iron atom / Fe | **CHEBI:18248** | Prefer oxidation-state-specific terms where the reaction requires them. |
| iron(2+) | **CHEBI:29033** | Ferrous iron. |
| iron(3+) | **CHEBI:29034** | Ferric iron bound by many siderophores. |
| heme | **CHEBI:30413** | Verify whether heme b or a more specific form is required. |
| urea | **CHEBI:16199** | Substrate for urease. |
| ammonia | **CHEBI:16134** | Product contributing to alkaline urine and tissue toxicity. |
| nickel(2+) | **CHEBI:49786** | Required for urease maturation; verify before import. |
| N-acetylneuraminic acid | **CHEBI:17012** | Neu5Ac; typhoid-toxin receptor glycan determinant. |
| cyclic GMP | **CHEBI:16356** | Enterotoxin-triggered host second messenger; verify current CHEBI record. |

## 3. Proposed evidence-backed causal edges

Predicates are deliberately mechanistic. “Promotes” should not be interpreted as necessary or universal unless the notes say so.

| # | Subject — predicate → object | Reference and supporting snippet | Curation assessment |
|---:|---|---|---|
| 1 | bacterial adhesin — **binds** → host receptor | Barber & Fitzgerald 2024: “The expression of bacterial surface molecules termed adhesins is critical for adherence to host tissues.” https://doi.org/10.1093/femsre/fuae019 (barber2024mechanismsofhost pages 3-5) | **Core, broad.** Parent edge for taxon-specific adhesin–receptor interactions. |
| 2 | InlA — **binds** → host E-cadherin | The same review states that InlA binds human and guinea-pig E-cadherin but not mouse or rat orthologs; two amino-acid substitutions can alter affinity and invasion. (barber2024mechanismsofhost pages 1-2, barber2024mechanismsofhost pages 3-5) | **Strong, taxon/host-specific.** Do not generalize InlA to all pathogens. |
| 3 | adhesin–host receptor binding — **promotes** → host colonization/invasion | Figure text: “Binding of bacterial adhesins to epithelial CEACAM subsequently mediates host colonization.” (barber2024mechanismsofhost pages 3-5) | **Strong but receptor-specific.** Appropriate intermediate edge. |
| 4 | SpsD/SpsO — **promote** → adherence to canine corneocytes | Heterologous expression of *spsD* and *spsO* increased adherence to canine corneocytes ex vivo. https://doi.org/10.3390/ijms241914587 (cheung2023virulencemechanismsof pages 9-10) | **Experimental, taxon- and assay-specific.** Ex-vivo adhesion is not alone proof of infection. |
| 5 | BAP/BLP1/BLP2 — **promote** → biofilm and epithelial-cell adherence | The *A. baumannii* review states that BAP “induces biofilm growth and adherence to host epithelial cells,” while BLP1/2 positively regulate both. https://doi.org/10.1080/21505594.2023.2289769 (lucidi2024pathogenicityandvirulence pages 4-5) | **Strong, taxon-specific.** |
| 6 | T1SS — **secretes** → RTX toxin and BAP | *A. baumannii* T1SSa was required for secretion of RTX toxin and BAP; T1SS mutants had biofilm defects and slight attenuation in *Galleria*. (lucidi2024pathogenicityandvirulence pages 5-7, lucidi2024pathogenicityandvirulence pages 4-5) | **Moderate.** RTX function remains untested in Acinetobacter; curate BAP secretion, mark RTX→virulence uncertain. |
| 7 | T2SS — **secretes** → LipA and other effectors | T2SS substrates include toxins, lipases, metalloproteases, and digestive enzymes; LipA was experimentally validated as an *A. baumannii* T2SS substrate. (lucidi2024pathogenicityandvirulence pages 5-7) | **Strong for secretion; taxon-specific.** |
| 8 | T2SS activity — **promotes** → in-vivo colonization/virulence | T2SS-defective *A. baumannii* showed reduced lung CFU, a 10-fold reduction in catheter binding/bladder colonization, and reduced competitiveness in septicemia. (lucidi2024pathogenicityandvirulence pages 5-7) | **Strong experimental edge, model-specific.** Do not infer that every T2SS effector has the same effect. |
| 9 | capsule — **masks** → surface antigen and C3b/iC3b | Gao et al. 2024: CPS “impedes the binding of IgG” and masks C3b, thereby reducing receptor-mediated uptake. https://doi.org/10.1038/s41522-024-00497-6 (gao2024bacterialcapsulesoccurrence pages 5-7, gao2024bacterialcapsulesoccurrence pages 3-5) | **Core mechanism, broad but not universal.** |
| 10 | capsule-mediated C3b masking — **reduces** → opsonophagocytosis/complement killing | The review reports that capsules prevent C3b receptor binding and confer resistance to complement-mediated killing. (gao2024bacterialcapsulesoccurrence pages 5-7) | **Strong.** Preserve organism/serotype context in evidence annotations. |
| 11 | factor-H/C4BP-binding surface protein — **recruits** → host complement regulator | Diverse *Neisseria*, *Streptococcus*, *Haemophilus*, and *Borrelia* proteins bind factor H or C4BP; such binding mediates complement evasion. (barber2024mechanismsofhost pages 8-10) | **Core function; implementations taxon-specific.** |
| 12 | SCIN — **inhibits** → C3 convertase | SCIN binds C3 convertase and prevents cleavage/activation; CHIPS blocks C5a/formyl-peptide receptor-mediated chemotaxis. (barber2024mechanismsofhost pages 8-10) | **Strong, *S. aureus*-specific and frequently host-specific.** |
| 13 | siderophore secretion — **chelates** → extracellular Fe3+ | Siderophores are secreted metabolites that bind Fe3+ and are internalized through specific receptors. https://doi.org/10.3390/ijms24076181 (stelitano2023ironacquisitionand pages 2-4) | **Core, broad.** |
| 14 | ferric-siderophore uptake system — **increases** → bacterial iron acquisition | Gram-negative uptake commonly uses a TonB-dependent outer-membrane receptor followed by periplasmic binding and an inner-membrane ABC transporter; Gram-positive uptake uses surface proteins and ABC transporters. (stelitano2023ironacquisitionand pages 2-4) | **Core module with envelope-specific branches.** |
| 15 | host transferrin/lactoferrin/lipocalin-2 — **reduces** → pathogen-accessible iron | Host iron-binding proteins limit iron available to pathogens; lipocalin-2 sequesters iron-laden enterobactin. https://doi.org/10.3389/fimmu.2023.1279826; https://doi.org/10.1016/j.chom.2023.08.018 (spiga2023ironacquisitionby pages 1-3, ullah2023keyplayersin pages 1-2) | **Core host constraint.** It is a negative edge to pathogen growth, not a microbial trait mechanism. |
| 16 | TbpA/IsdB/TdfH — **acquire** → host-bound metal nutrient | TbpA binds transferrin, IsdB scavenges heme from hemoglobin, and TdfH binds calprotectin to obtain zinc; each can show host-species selectivity. (barber2024mechanismsofhost pages 5-6) | **Strong, named receptor edges are host/taxon-specific.** |
| 17 | quorum-sensing autoinducer threshold — **activates** → virulence/biofilm gene expression | QS is density-dependent; once autoinducer reaches threshold, cognate sensors alter global expression. In *P. aeruginosa*, Las/Rhl regulate elastase, proteases, exotoxin A, rhamnolipid, pyocyanin, and lectin genes. https://doi.org/10.3390/ijms25052655 (juszczukkubiak2024molecularaspectsof pages 2-3) | **Strong regulatory mechanism; not universal.** |
| 18 | AgrA/AgrC/RNAIII — **activates** → staphylococcal toxin expression | The Agr system activates α-hemolysin, coagulase, and enterotoxin genes; in *S. pseudintermedius*, Agr activation transcribes some toxin genes, but its role in animal disease remains unresolved. (juszczukkubiak2024molecularaspectsof pages 5-7, cheung2023virulencemechanismsof pages 9-10) | **Strong in *S. aureus*; uncertain disease-level edge in *S. pseudintermedius*.** |
| 19 | biofilm matrix — **reduces** → antimicrobial penetration/host clearance | Biofilm bacteria may exhibit about 1,000-fold greater antibiotic resistance; poultry isolates also showed biofilms hinder phagocytosis and support long-term colonization. (eidaroos2024theimpactof pages 1-2, juszczukkubiak2024molecularaspectsof pages 2-3) | **Contextual core for persistence, not required for acute pathogenicity.** |
| 20 | bacterial toxin — **damages** → host cell/tissue | Pathogenic bacteria are often distinguished by potent toxins; toxins lyse leukocytes, support immune evasion, release nutrients, and facilitate transmission. (barber2024mechanismsofhost pages 10-11) | **Core functional edge, but toxin identity must be specified in taxon graphs.** |
| 21 | leukocidin–host receptor binding — **causes** → leukocyte lysis | Host-restricted examples include bovine LukMF′–CCR1 and equine LukPQ–CXCR1/CXCR2; humanized receptor mice gained susceptibility to LukAB-associated infection. (barber2024mechanismsofhost pages 10-11) | **Strong, receptor- and host-specific.** |
| 22 | UreR plus urea — **activates** → *ureABCDEFG* expression | In *P. mirabilis*, “in the presence of urea,” UreR activates the urease cluster; UreABC supplies structural subunits and UreDEFG supports nickel insertion. https://doi.org/10.3389/fcimb.2024.1465460 (yang2024unveilingthehidden pages 2-4) | **Strong, urinary-pathogen-specific.** |
| 23 | urease — **converts** → urea to ammonia and CO2 | Ammonia raises urinary pH, promoting precipitation and infection stones; ammonia also contributes to urinary tissue toxicity. (yang2024unveilingthehidden pages 2-4) | **Strong biochemical and disease edge.** Ground with an EC/Rhea reaction only after identifier verification. |
| 24 | urease activity — **promotes** → urinary colonization/stone formation | A *ureC* mutant produced no extracellular mineral clusters and had 23-fold fewer CFU at 24 h without an in-vitro growth defect. (yang2024unveilingthehidden pages 2-4) | **Strong animal-model evidence, taxon/niche-specific.** |
| 25 | host-specific nutrient utilization — **promotes** → host adaptation | Bovine mastitis isolates of *S. aureus* showed enhanced lactose utilization; bovine-adapted *Campylobacter* grew better under vitamin-B5 limitation. (barber2024mechanismsofhost pages 6-7) | **Moderate-to-strong but lineage-specific.** Use as examples under a generic nutrient-adaptation node. |
| 26 | elevated glucose — **enhances** → *S. aureus* virulence | In diabetic mouse models, elevated glucose both dampened neutrophil responses and enhanced bacterial virulence. (barber2024mechanismsofhost pages 6-7) | **Contextual and bidirectional.** Do not encode as an intrinsic microbial trait edge without the host context. |

## 4. Suggested graph architecture

A compact general graph could use the following structure:

1. **host-compatible adhesin/receptor interaction** → host attachment → colonization;
2. **host nutrient limitation** → induces/selects nutrient-acquisition systems → microbial growth in host;
3. **capsule/complement evasion or intracellular defense effector** → reduced immune clearance → persistence;
4. **secretion apparatus** → exported effector/toxin → host manipulation or damage;
5. **quorum sensing and/or biofilm**, where present → coordinated virulence/persistence;
6. colonization + growth + persistence + damage → **animal pathogen phenotype**.

The terminal edge should be interpreted as an evidence synthesis rather than a universal Boolean rule. Different pathogens can realize the trait without toxins, capsules, biofilms, or a particular secretion system.

## 5. Recent developments, applications, and quantitative findings

### Host-adaptation genomics and receptor biology

Recent work emphasizes that very small sequence changes can shift host tropism: host-associated *Salmonella* serovars carry FimH variation, and two InlA amino-acid substitutions alter E-cadherin affinity and host-cell invasion. Horizontal gene transfer, gene loss, and genome rearrangement also contribute to animal-host adaptation. These results support strain-level, allele-aware graph nodes rather than species-wide annotations. (barber2024mechanismsofhost pages 1-2)

### Anti-virulence and vaccine targets

Mechanistic interfaces are being exploited therapeutically. The host-adaptation review identifies **dltB** as an antimicrobial target emerging from a rabbit host-switch study and notes therapeutic development against host-specific leukocidins. Factor-H-binding proteins and capsule components are also attractive vaccine/antibody targets because they directly mediate immune-interface interference. (barber2024mechanismsofhost pages 11-12)

Iron uptake is particularly attractive because siderophore synthesis, TonB/ABC uptake, and mycobacterial IrtA/IrtB systems differ from host pathways. Current strategies include inhibiting siderophore biosynthesis or iron sensing, using gallium or chelators, and exploiting uptake systems as “Trojan horse” drug-delivery routes. However, nonspecific iron chelation can also deplete host iron and cause toxicity. (stelitano2023ironacquisitionand pages 2-4)

Quorum quenching is under investigation as a non-bactericidal strategy using signal-degrading enzymes, receptor inhibitors, antibodies, nanoparticles, probiotics, phages, antimicrobial peptides, and precision genome targeting. The literature remains largely preclinical, and efficacy is likely to depend on infection site, microbial community, and whether QS is required in vivo. (juszczukkubiak2024molecularaspectsof pages 2-3)

### Recent quantitative evidence

* In a 2024 poultry study, *P. aeruginosa* was isolated from **25% of 160 samples** from respiratory-distressed layer chickens; **95%** of isolates were XDR. The genes *lasI*, *lasR*, *toxA/exoU*, *pslA*, *fliC*, and *pelA* occurred at 100%, 89.5%, 78.9%, 100%, 84.2%, and 10.5%, respectively. These are prevalence/correlation data, not proof that each gene causes avian pathogenicity (accepted 18 May 2024; https://doi.org/10.22099/IJVR.2024.47975.6969). (eidaroos2024theimpactof pages 1-2)
* T2SS-deficient *A. baumannii* showed a **10-fold** decrease in catheter binding and bladder colonization in a mouse CAUTI model. (lucidi2024pathogenicityandvirulence pages 5-7)
* A *P. mirabilis ureC* mutant had **23-fold fewer CFU at 24 h** and failed to produce extracellular mineral clusters despite lacking an in-vitro growth defect. (yang2024unveilingthehidden pages 2-4)
* In polymicrobial *P. mirabilis–Enterococcus faecalis* infection, **96%** of mice developed bacteremia and **56%** developed urolithiasis—18 and 30 percentage points above *P. mirabilis* monoinfection, respectively. This supports community context as a modifier, not a universal microbial edge. (yang2024unveilingthehidden pages 2-4)
* A review reports that biofilm-associated bacteria can be approximately **1,000-fold** more antibiotic resistant than planktonic cells; this should be treated as an approximate cross-study value rather than a universal constant. (juszczukkubiak2024molecularaspectsof pages 2-3)
* Staphylococcal mastitis was estimated to cost the global dairy industry **US$20–33 billion annually**, highlighting the real-world relevance of animal-pathogen mechanisms; the estimate cited in the 2023 review originates from 2011 and is not a current-year economic estimate. (cheung2023virulencemechanismsof pages 1-2)
* Reported MRSA prevalence averages in bovine bulk and individual-farm milk samples were approximately **2.9% and 4.5%**, although some studies reached approximately 50% and geographic variation was substantial. (cheung2023virulencemechanismsof pages 7-9)

## 6. Claims that should not yet be curated as general TraitMech edges

1. **“T3SS or T6SS causes animal pathogenicity.”** These systems are important in particular lineages but absent from many animal pathogens. Curate system-specific effector edges only where direct evidence exists.
2. **“Capsule promotes adhesion/biofilm.”** Capsule effects are bidirectional. Capsules may promote persistence yet mask adhesins and reduce initial in-vitro attachment; increased in-vitro adhesion may not predict colonization in animals. (gao2024bacterialcapsulesoccurrence pages 5-7, gao2024bacterialcapsulesoccurrence pages 3-5)
3. **“Biofilm is required for animal pathogenicity.”** Biofilms strongly support chronicity and device/environmental persistence but are dispensable in many acute infections.
4. **“QS genes imply virulence.”** Gene presence and PCR correlation do not establish functional signaling or disease causation. In *S. pseudintermedius*, Agr activates toxin transcription, but its necessity in skin disease is explicitly unknown. (cheung2023virulencemechanismsof pages 9-10)
5. **“RTX toxin promotes Acinetobacter virulence.”** T1SS-dependent secretion is supported, but RTX function has not been evaluated in Acinetobacter. (lucidi2024pathogenicityandvirulence pages 5-7)
6. **“Every siderophore promotes pathogenicity.”** Siderophores can be produced by commensals, and microbiota can redistribute siderophores. In one 2023 study, commensal XusB shielded enterobactin from lipocalin-2 and enabled its reacquisition by *Salmonella*, demonstrating that community context can reverse simple host–pathogen assumptions. (spiga2023ironacquisitionby pages 1-3)
7. **“Environmental resistance equals animal pathogenicity.”** Desiccation, antibiotic resistance, and hospital persistence raise exposure probability but do not alone demonstrate infection capacity.
8. **Species-wide host labels.** Host restriction can be lineage-, allele-, receptor-, and assay-dependent; attach host taxon and strain provenance to evidence.
9. **Invertebrate-surrogate lethality as definitive mammalian evidence.** *Galleria* results are valuable screening evidence but should remain assay-specific unless supported in the relevant natural host.
10. **Host damage as universally required.** Persistent or subclinical infections may satisfy the pathogen trait without conspicuous toxin-mediated pathology.

## 7. DOI-first bibliography

1. Barber MF, Fitzgerald JR. **Mechanisms of host adaptation by bacterial pathogens.** *FEMS Microbiology Reviews*. Published 13 July 2024. https://doi.org/10.1093/femsre/fuae019. (barber2024mechanismsofhost pages 1-2)
2. Gao S, et al. **Bacterial capsules: occurrence, mechanism, and function.** *npj Biofilms and Microbiomes*. March 2024. https://doi.org/10.1038/s41522-024-00497-6. (gao2024bacterialcapsulesoccurrence pages 1-3)
3. Lucidi M, et al. **Pathogenicity and virulence of Acinetobacter baumannii: factors contributing to fitness in healthcare settings and the infected host.** *Virulence*. 2024. https://doi.org/10.1080/21505594.2023.2289769. (lucidi2024pathogenicityandvirulence pages 5-7)
4. Yang A, Tian Y, Li X. **Unveiling the hidden arsenal: new insights into Proteus mirabilis virulence in UTIs.** *Frontiers in Cellular and Infection Microbiology*. November 2024. https://doi.org/10.3389/fcimb.2024.1465460. (yang2024unveilingthehidden pages 2-4)
5. Juszczuk-Kubiak E. **Molecular aspects of pathogenic bacterial biofilm based on quorum sensing and non-antibiotic strategies.** *International Journal of Molecular Sciences*. February 2024. https://doi.org/10.3390/ijms25052655. (juszczukkubiak2024molecularaspectsof pages 5-7)
6. Araújo D, et al. **Emerging approaches for mitigating biofilm-formation-associated infections in farm, wild, and companion animals.** *Pathogens*. April 2024. https://doi.org/10.3390/pathogens13040320. (araujo2024emergingapproachesfor pages 5-7)
7. Eidaroos NH, et al. **Impact of quorum sensing and biofilm formation on antimicrobial resistance and virulence of XDR/MDR Pseudomonas aeruginosa in laying chickens.** *Iranian Journal of Veterinary Research*. Accepted 18 May 2024. https://doi.org/10.22099/IJVR.2024.47975.6969. (eidaroos2024theimpactof pages 1-2)
8. Spiga L, et al. **Iron acquisition by a commensal bacterium modifies host nutritional immunity during Salmonella infection.** *Cell Host & Microbe*. Published 11 October 2023. https://doi.org/10.1016/j.chom.2023.08.018. (spiga2023ironacquisitionby pages 1-3)
9. Ullah I, Lang M. **Key players in regulation of iron homeostasis at the host–pathogen interface.** *Frontiers in Immunology*. Published 24 October 2023. https://doi.org/10.3389/fimmu.2023.1279826. (ullah2023keyplayersin pages 1-2)
10. Stelitano G, et al. **Iron acquisition and metabolism as a promising target for antimicrobials.** *International Journal of Molecular Sciences*. March 2023. https://doi.org/10.3390/ijms24076181. (stelitano2023ironacquisitionand pages 2-4)
11. Cheung GYC, Otto M. **Virulence mechanisms of staphylococcal animal pathogens.** *International Journal of Molecular Sciences*. Published 26 September 2023. https://doi.org/10.3390/ijms241914587. (cheung2023virulencemechanismsof pages 1-2)
12. Shahoumi LA, Saleh MHA, Meghil MM. **Virulence factors of periodontal pathogens.** *Microorganisms*. January 2023. https://doi.org/10.3390/microorganisms11010115. (shahoumi2023virulencefactorsof pages 1-2)

## Bottom line for `animal_pathogen.yaml`

Curate broad functional nodes for **adhesion, nutrient acquisition, immune evasion, persistence, secretion, and host damage**, but instantiate named genes and molecular interactions in taxon-specific branches. The most defensible new general edges are adhesin→attachment, siderophore/host-receptor systems→nutrient acquisition, capsule/complement-regulator recruitment→reduced immune clearance, toxin/effector delivery→host manipulation or damage, and biofilm→persistence. Urease, individual secretion systems, Agr/Las signaling, specific leukocidins, and host-specific receptors should not be promoted to universal requirements of METPO:1004002.

References

1. (barber2024mechanismsofhost pages 1-2): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

2. (barber2024mechanismsofhost pages 3-5): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

3. (barber2024mechanismsofhost pages 5-6): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

4. (lucidi2024pathogenicityandvirulence pages 4-5): Massimiliano Lucidi, Daniela Visaggio, Antonella Migliaccio, Giulia Capecchi, Paolo Visca, Francesco Imperi, and Raffaele Zarrilli. Pathogenicity and virulence of acinetobacter baumannii: factors contributing to the fitness in healthcare settings and the infected host. Virulence, Dec 2024. URL: https://doi.org/10.1080/21505594.2023.2289769, doi:10.1080/21505594.2023.2289769. This article has 138 citations and is from a peer-reviewed journal.

5. (barber2024mechanismsofhost pages 7-8): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

6. (lucidi2024pathogenicityandvirulence pages 5-7): Massimiliano Lucidi, Daniela Visaggio, Antonella Migliaccio, Giulia Capecchi, Paolo Visca, Francesco Imperi, and Raffaele Zarrilli. Pathogenicity and virulence of acinetobacter baumannii: factors contributing to the fitness in healthcare settings and the infected host. Virulence, Dec 2024. URL: https://doi.org/10.1080/21505594.2023.2289769, doi:10.1080/21505594.2023.2289769. This article has 138 citations and is from a peer-reviewed journal.

7. (barber2024mechanismsofhost pages 10-11): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

8. (eidaroos2024theimpactof pages 1-2): N. Eidaroos, H. I. Eid, S. Nasef, G. H. Mansour, and R. El-Tarabili. The impact of quorum sensing and biofilm formation on antimicrobial resistance and virulence of xdr and mdr pseudomonas aeruginosa in laying chickens. Iranian Journal of Veterinary Research, 25:125-134, 2024. URL: https://doi.org/10.22099/ijvr.2024.47975.6969, doi:10.22099/ijvr.2024.47975.6969. This article has 2 citations and is from a peer-reviewed journal.

9. (yang2024unveilingthehidden pages 2-4): Aoyu Yang, Yuchong Tian, and Xiancheng Li. Unveiling the hidden arsenal: new insights into proteus mirabilis virulence in utis. Frontiers in Cellular and Infection Microbiology, Nov 2024. URL: https://doi.org/10.3389/fcimb.2024.1465460, doi:10.3389/fcimb.2024.1465460. This article has 28 citations.

10. (barber2024mechanismsofhost pages 8-10): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

11. (gao2024bacterialcapsulesoccurrence pages 5-7): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, Li Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. NPJ Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 118 citations and is from a peer-reviewed journal.

12. (gao2024bacterialcapsulesoccurrence pages 3-5): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, Li Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. NPJ Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 118 citations and is from a peer-reviewed journal.

13. (ullah2023keyplayersin pages 1-2): Inam Ullah and Minglin Lang. Key players in the regulation of iron homeostasis at the host-pathogen interface. Frontiers in Immunology, Oct 2023. URL: https://doi.org/10.3389/fimmu.2023.1279826, doi:10.3389/fimmu.2023.1279826. This article has 80 citations and is from a peer-reviewed journal.

14. (stelitano2023ironacquisitionand pages 2-4): Giovanni Stelitano, Mario Cocorullo, Matteo Mori, Stefania Villa, Fiorella Meneghetti, and Laurent Roberto Chiarelli. Iron acquisition and metabolism as a promising target for antimicrobials (bottlenecks and opportunities): where do we stand? International Journal of Molecular Sciences, 24:6181, Mar 2023. URL: https://doi.org/10.3390/ijms24076181, doi:10.3390/ijms24076181. This article has 30 citations.

15. (juszczukkubiak2024molecularaspectsof pages 2-3): Edyta Juszczuk-Kubiak. Molecular aspects of the functioning of pathogenic bacteria biofilm based on quorum sensing (qs) signal-response system and innovative non-antibiotic strategies for their elimination. International Journal of Molecular Sciences, 25:2655, Feb 2024. URL: https://doi.org/10.3390/ijms25052655, doi:10.3390/ijms25052655. This article has 152 citations.

16. (juszczukkubiak2024molecularaspectsof pages 5-7): Edyta Juszczuk-Kubiak. Molecular aspects of the functioning of pathogenic bacteria biofilm based on quorum sensing (qs) signal-response system and innovative non-antibiotic strategies for their elimination. International Journal of Molecular Sciences, 25:2655, Feb 2024. URL: https://doi.org/10.3390/ijms25052655, doi:10.3390/ijms25052655. This article has 152 citations.

17. (barber2024mechanismsofhost pages 6-7): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

18. (cheung2023virulencemechanismsof pages 1-2): Gordon Y. C. Cheung and Michael Otto. Virulence mechanisms of staphylococcal animal pathogens. International Journal of Molecular Sciences, 24:14587, Sep 2023. URL: https://doi.org/10.3390/ijms241914587, doi:10.3390/ijms241914587. This article has 40 citations.

19. (cheung2023virulencemechanismsof pages 9-10): Gordon Y. C. Cheung and Michael Otto. Virulence mechanisms of staphylococcal animal pathogens. International Journal of Molecular Sciences, 24:14587, Sep 2023. URL: https://doi.org/10.3390/ijms241914587, doi:10.3390/ijms241914587. This article has 40 citations.

20. (spiga2023ironacquisitionby pages 1-3): Luisella Spiga, Ryan T. Fansler, Yasiru R. Perera, Nicolas G. Shealy, Matthew J. Munneke, Holly E. David, Teresa P. Torres, Andrew Lemoff, Xinchun Ran, Katrina L. Richardson, Nicholas Pudlo, Eric C. Martens, Ewa Folta-Stogniew, Zhongyue J. Yang, Eric P. Skaar, Mariana X. Byndloss, Walter J. Chazin, and Wenhan Zhu. Iron acquisition by a commensal bacterium modifies host nutritional immunity during salmonella infection. Cell Host &amp; Microbe, 31:1639-1654.e10, Oct 2023. URL: https://doi.org/10.1016/j.chom.2023.08.018, doi:10.1016/j.chom.2023.08.018. This article has 73 citations and is from a highest quality peer-reviewed journal.

21. (barber2024mechanismsofhost pages 11-12): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

22. (cheung2023virulencemechanismsof pages 7-9): Gordon Y. C. Cheung and Michael Otto. Virulence mechanisms of staphylococcal animal pathogens. International Journal of Molecular Sciences, 24:14587, Sep 2023. URL: https://doi.org/10.3390/ijms241914587, doi:10.3390/ijms241914587. This article has 40 citations.

23. (gao2024bacterialcapsulesoccurrence pages 1-3): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, Li Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. NPJ Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 118 citations and is from a peer-reviewed journal.

24. (araujo2024emergingapproachesfor pages 5-7): Daniela Araújo, Ana Rita Silva, Rúben Fernandes, Patrícia Serra, Maria Margarida Barros, Ana Maria Campos, Ricardo Oliveira, Sónia Silva, Carina Almeida, and Joana Castro. Emerging approaches for mitigating biofilm-formation-associated infections in farm, wild, and companion animals. Pathogens, 13:320, Apr 2024. URL: https://doi.org/10.3390/pathogens13040320, doi:10.3390/pathogens13040320. This article has 47 citations.

25. (shahoumi2023virulencefactorsof pages 1-2): Linah A. Shahoumi, Muhammad H. A. Saleh, and Mohamed M. Meghil. Virulence factors of the periodontal pathogens: tools to evade the host immune response and promote carcinogenesis. Microorganisms, 11:115, Jan 2023. URL: https://doi.org/10.3390/microorganisms11010115, doi:10.3390/microorganisms11010115. This article has 63 citations.