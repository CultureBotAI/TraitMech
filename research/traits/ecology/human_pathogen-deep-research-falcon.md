---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:25:27.174287'
end_time: '2026-06-17T20:44:07.341610'
duration_seconds: 1120.17
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
  causal_graph_summary: 'human_pathogen_anthropoid_adaptation: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
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
- **Existing causal graph summary:** human_pathogen_anthropoid_adaptation: 5 nodes, 4 edges

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
- **Existing causal graph summary:** human_pathogen_anthropoid_adaptation: 5 nodes, 4 edges

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


# Microbial Trait Causal Graph Curation Report: **human pathogen** (METPO:1004004)

## 0) Scope summary (curation-oriented)
The trait **human pathogen** (METPO:1004004) denotes a microbe that can **infect Homo sapiens** and cause a disease state (or a clinically recognized infection), typically by executing a sequence of steps including **contact → colonization → invasion → immune evasion → infection** (and, in many cases, persistence and transmission). (soni2024understandingbacterialpathogenicity pages 4-5)

**Boundary cases to distinguish during curation**:
- **Commensal ↔ opportunistic pathogen continuum**: several microbes can colonize humans without causing disease, and disease may occur mainly when host defenses are compromised (e.g., trauma, underlying illness, immunocompromise). Thus, “human pathogen” should not be treated as an intrinsic binary property for all taxa; it is often **context-dependent**. (soni2024understandingbacterialpathogenicity pages 2-4)
- **Host tropism / host restriction**: host range spans from **human-restricted** pathogens to broad-host-range generalists. Spillover from other hosts can occur; establishment in humans can require genetic/functional adaptation to human anatomy, immunity, and nutrients. (barber2024mechanismsofhost pages 1-2)
- **Zoonosis vs established human pathogen**: spillover events are a boundary; curate “human pathogen” edges preferentially when the mechanism supports **infection in humans** (or a compelling human-relevant model) rather than only animal infection. (barber2024mechanismsofhost pages 1-2)

## 1) Key concepts & definitions (current understanding)
### 1.1 Pathogenicity vs virulence vs infection state
- **Pathogenic bacteria** are described as a subset of bacteria capable of causing **disease in humans**, whereas many bacteria are harmless or beneficial. Infection is often enabled when host defenses are compromised. (soni2024understandingbacterialpathogenicity pages 2-4)
- **Virulence** is the degree/severity of disease and is tied to **virulence factors** such as toxins, surface coats/capsules, secretion systems and immune-evasion mechanisms. (soni2024understandingbacterialpathogenicity pages 2-4, soni2024understandingbacterialpathogenicity pages 4-5)

### 1.2 Mechanistic steps that define “human pathogen” as a functional capacity
A practical (curation-friendly) decomposition of “human pathogen” capacity supported by recent reviews includes:
- **Colonization** initiated at human epithelial barriers and/or after barrier disruption (wounds). (barber2024mechanismsofhost pages 3-5)
- **Attachment/adhesion** mediated by bacterial adhesins binding host receptors and extracellular matrix components. (barber2024mechanismsofhost pages 3-5)
- **Nutrient acquisition** tuned to host niches (e.g., metal/heme scavenging; carbohydrate utilization). (barber2024mechanismsofhost pages 6-7)
- **Immune evasion / host manipulation** via surface modifications, secreted effectors, and modulation of inflammation/cell death. (barber2024mechanismsofhost pages 6-7, zhou2024typeiiisecretion pages 1-2)
- **Genome plasticity and within-host evolution** enabling rapid adaptation, persistence and resistance. (dekker2024withinhostevolutionof pages 2-4)

## 2) Recent developments and latest research (prioritized 2023–2024)
### 2.1 Host adaptation mechanisms (2024)
A 2024 synthesis of bacterial host adaptation emphasizes that host tropism and successful infection depend on compatibility with host receptors (adhesion), host nutrient landscapes (metal/heme acquisition, carbon sources), and immune defenses; adaptation can arise from both point mutations and mobile genetic elements/HGT. (barber2024mechanismsofhost pages 1-2, barber2024mechanismsofhost pages 2-3, barber2024mechanismsofhost pages 6-7)

Notable human-specific mechanisms in this evidence set include:
- **CEACAM-binding adhesins** (e.g., HopQ/Opa/UspA1) mediating human-specific colonization by selective binding to human CEACAM1. (barber2024mechanismsofhost pages 3-5)
- **Human-specific nutrient receptor binding**, including transferrin-binding (TbpA/TdfH) and hemoglobin-heme scavenging (IsdB). (barber2024mechanismsofhost pages 6-7)

### 2.2 Secretion systems as major mechanistic modules (2024)
- **Type III secretion system (T3SS)**: syringe-like complexes that deliver effectors directly into host cells and can be decisive virulence determinants in clinical isolates. In *Pseudomonas aeruginosa*, ExoU is highlighted as the main determinant of pathogenicity in a highly virulent bloodstream isolate; deleting **exoU** attenuated cytotoxicity and virulence. (wu2024thetypeiii pages 1-2)
- **Effector targeting of host cell death pathways**: the 2024 study on *Edwardsiella piscicida* shows a T3SS effector (**YfiD**) can suppress host PARP1 activity, reducing inflammatory responses and cell death while promoting in vivo colonization and virulence. (zhou2024typeiiisecretion pages 1-2)
- **Immune evasion via lipid mediator suppression**: a 2024 *Yersinia pestis* study demonstrates leukocytes recognize the T3SS and trigger leukotriene B4 (LTB4), but Yop effectors secreted through the T3SS inhibit this response; exogenous LTB4 limits bacterial proliferation, linking suppression to immune evasion. (brady2024type3secretion pages 1-2)
- **Type IV secretion systems (T4SSs)**: a 2024 Nature Reviews Microbiology review frames T4SSs as nanomachines mediating DNA transfer (conjugation) and protein effector translocation, central to antimicrobial-resistance spread and infection; it details substrate recruitment by VirD4/type IV coupling proteins and host-interaction adaptations (e.g., immune modulation by the *H. pylori* Cag system). (costa2024structuralandfunctional pages 1-5, costa2024structuralandfunctional pages 9-11)

**Visual evidence**: The cited T4SS review includes schematics showing T4SS architecture and the functional split between conjugation and effector translocation (costa2024structuralandfunctional media d77bae5c, costa2024structuralandfunctional media 3d928bb8).

### 2.3 Within-host evolution and genome plasticity (2024)
A 2024 Annual Review of Pathology synthesis emphasizes that within-host evolution is enabled by large bacterial population sizes, short generation times, baseline mutation rates (~10−10 per position per generation), and diversity-amplifying mechanisms including hypermutation and mobile genetic element insertions; these changes can increase pathogenicity, persistence, and antimicrobial resistance. (dekker2024withinhostevolutionof pages 2-4)

## 3) Current applications and real-world implementations
### 3.1 Antivirulence strategies and quorum sensing interference
A 2023 Nature Reviews Microbiology review of *Staphylococcus aureus* host interactions highlights **agr quorum sensing** as a central regulatory node: agr activity controls PSM expression linked to inflammation, and microbial interactions can inhibit agr, supporting the feasibility of antivirulence strategies that suppress virulence regulation rather than kill bacteria outright. (howden2023staphylococcusaureushost pages 1-5)

### 3.2 Phages as precision tools for AMR pathogens
A 2023 review on enterococcal phages discusses bacteriophages as a “precision tool” for controlling bacterial populations, including potential use against AMR enterococci that have emerged as major hospital-acquired pathogens. (rodriguezlucas2023enterococcalphagesfood pages 1-2)

### 3.3 Clinical genomics and surveillance of virulence determinants
The 2024 *P. aeruginosa* clinical study motivates diagnostic/therapeutic stratification based on decisive virulence genes (e.g., **exoU**) and notes insertion sequences adjacent to exoU suggesting potential transfer (inference), aligning with genomic surveillance approaches. (wu2024thetypeiii pages 1-2)

## 4) Expert opinions & authoritative synthesis (what experts emphasize)
Authoritative reviews in 2023–2024 converge on a few principles that are directly useful for TraitMech graph design:
1. **Host adaptation is multi-step** (colonization, nutrient acquisition, immune evasion) rather than a single gene effect. (barber2024mechanismsofhost pages 1-2)
2. **Secretion systems are modular “delivery platforms”** for host manipulation and are simultaneously targets for intervention and key determinants of disease phenotypes. (wu2024thetypeiii pages 1-2, costa2024structuralandfunctional pages 1-5)
3. **Genome plasticity** (HGT, phages/PICIs, IS elements; hypermutation via proofreading/MMR defects) is a central enabler of emergence/persistence of human pathogenic lineages. (barber2024mechanismsofhost pages 2-3, dekker2024withinhostevolutionof pages 2-4)

## 5) Statistics and recent quantitative data
Although “human pathogen” is a mechanistic trait, recent sources provide relevant burden statistics to motivate curation priorities:
- A 2023 review summarizing global AMR burden reports **4.95 million deaths associated with bacterial resistance in 2019**, including **1.27 million deaths directly due to AMR**, and notes >1.5 million AMR-related deaths from lower respiratory infections. (lazar2023resistancetolerancevirulence pages 1-2)
- The same review states MRSA caused **>100,000 deaths in 2019** and highlights WHO priority pathogens. (lazar2023resistancetolerancevirulence pages 1-2)
- A 2023 enterococcal phage review reports in Europe **up to 133,000 deaths in 2019 attributable to AMR infections** and annual health-service costs exceeding **EUR 1,000 million**. (rodriguezlucas2023enterococcalphagesfood pages 1-2)

These statistics are best treated as **context nodes** (disease burden) rather than direct mechanistic edges for “human pathogen.” (lazar2023resistancetolerancevirulence pages 1-2, rodriguezlucas2023enterococcalphagesfood pages 1-2)

---

## 6) Candidate causal-graph nodes (grouped by type)

### 6.1 Microbial genes/proteins and systems (examples in evidence)
- **Adhesins / invasion factors**: HopQ, Opa, UspA1 (CEACAM-binding); InlA (E-cadherin-binding). (barber2024mechanismsofhost pages 3-5, barber2024mechanismsofhost pages 2-3)
- **Secreted effectors**: ExoU (T3SS effector); YfiD (T3SS effector). (wu2024thetypeiii pages 1-2, zhou2024typeiiisecretion pages 1-2)
- **Secretion systems**: T3SS; T4SS; type IV coupling protein VirD4/T4CP; OMCC/IMC subcomplexes. (wu2024thetypeiii pages 1-2, costa2024structuralandfunctional pages 1-5, costa2024structuralandfunctional pages 9-11)
- **Immune-evasion / surface modification**: dltB (cell wall/lipoteichoic acid decoration → AMP resistance). (barber2024mechanismsofhost pages 2-3)
- **Nutrient acquisition receptors**: TbpA/TdfH (transferrin/calprotectin); IsdB (hemoglobin/heme). (barber2024mechanismsofhost pages 6-7)
- **Regulatory modules**: agr quorum sensing (S. aureus), PSM expression. (howden2023staphylococcusaureushost pages 1-5)

### 6.2 Mobile genetic elements & evolutionary mechanisms
- **Temperate phages**, **PICIs**, **plasmids**, **transposons**, **insertion sequences**. (barber2024mechanismsofhost pages 2-3, dekker2024withinhostevolutionof pages 2-4)
- **Hypermutation mechanisms**: proofreading defects (dnaQ/mutD), mismatch repair defects (MutS/MutL/MutH), SOS response. (dekker2024withinhostevolutionof pages 2-4)

### 6.3 Host/environmental factors (context nodes; not microbial mechanisms)
- Host receptors/targets: CEACAM1, E-cadherin, PARP1. (barber2024mechanismsofhost pages 3-5, barber2024mechanismsofhost pages 2-3, zhou2024typeiiisecretion pages 1-2)
- Host nutrients: transferrin, hemoglobin/heme; carbohydrate availability. (barber2024mechanismsofhost pages 6-7)
- Host immune pathways: inflammasomes recognizing flagellin/T3SS proteins; GBP1 recognition of LPS. (barber2024mechanismsofhost pages 6-7)
- Host compromise/conditions: barrier disruption (wounds), immunocompromise; metabolic states such as hyperglycemia/diabetes affecting neutrophil response and virulence. (barber2024mechanismsofhost pages 3-5, barber2024mechanismsofhost pages 6-7, soni2024understandingbacterialpathogenicity pages 2-4)

---

## 7) Evidence-backed candidate causal edges (curation-ready)
The following table consolidates candidate triples, snippets, DOI-first references, and curation cautions.

| Edge (subject–predicate–object) | Entity types | Suggested ontology grounding (CURIEs where available) | Evidence snippet/quote | Reference (DOI + URL + publication month/year) | Curation notes (strength, uncertainty, taxon-specific) |
|---|---|---|---|---|---|
| CEACAM-binding adhesin — mediates attachment to epithelial CEACAM1 — host colonization | protein/receptor/process | GO:0046813 cell surface binding; GO:0044406 adhesion of symbiont to host; label-only: CEACAM-binding adhesin, CEACAM1 | “Human-specific Helicobacter, Neisseria, and Moraxella spp. encode surface adhesins (HopQ, Opa, and UspA1, respectively) with selectivity for human CEACAM1… Binding of bacterial adhesins to epithelial CEACAM subsequently mediates host colonization.” (barber2024mechanismsofhost pages 3-5) | 10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · Jul 2024 | Strong for specific adhesins and human-adapted colonization; taxon-specific; suitable as exemplars rather than universal edge. |
| InlA — binds human E-cadherin — host cell invasion/colonization | protein/protein/process | label-only: InlA; UniProt not asserted; label-only: E-cadherin; GO:0044406 | “InlA binds to human and guinea pig E-cadherin protein, but does not recognize the mouse or rat orthologs… a single amino acid mutation at position 16 in E-cadherin is sufficient to determine host species tropism.” (barber2024mechanismsofhost pages 2-3) | 10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · Jul 2024 | Strong, but clearly Listeria-specific and host-receptor-specific; curate as host-tropism mechanism, not generic for all human pathogens. |
| Type III secretion system — delivers ExoU effector into host cytoplasm — cytotoxicity/virulence | secretion system/protein/process | GO:0030257 type III protein secretion system complex; label-only: ExoU; GO:0052040 modulation by symbiont of host cell process | “T3SSs are multiprotein complexes that form syringe-like structures… allowing effector proteins to be delivered directly… ExoU… is considered the major T3SS cytotoxin… associated with severe acute lung injury, sepsis… Deletion of exoU showed significantly attenuated cytotoxicity and virulence in vivo.” (wu2024thetypeiii pages 1-2) | 10.1128/spectrum.02224-23 · https://doi.org/10.1128/spectrum.02224-23 · Jan 2024 | Strong primary evidence; Pseudomonas aeruginosa-specific; good direct virulence edge. |
| SpcU chaperone — enables ExoU secretion — ExoU-dependent cytotoxicity | protein/protein/process | label-only: SpcU; label-only: ExoU; GO:0030257 | “intact exoU is not sufficient for cytotoxicity, but a functional downstream SpcU is required for ExoU secretion and cytotoxicity.” (wu2024thetypeiii pages 1-2) | 10.1128/spectrum.02224-23 · https://doi.org/10.1128/spectrum.02224-23 · Jan 2024 | Strong but very taxon/gene specific; useful mechanistic sub-edge under T3SS-mediated virulence. |
| T3SS effector YfiD — binds/inhibits PARP1 ART domain — reduced inflammatory cell death and increased colonization/virulence | protein/protein/process | label-only: YfiD; UniProt:D0ZD05; PARP1 UniProt:P09874; GO:0016241 regulation of macroautophagy not appropriate; label-only: PARylation inhibition | “YfiD… binds to the ADP-ribosyl transferase (ART) domain of PARP1 to suppress its PARylation ability… YfiD impairs the inflammatory response and cell death in macrophages and promotes in vivo colonization and virulence.” (zhou2024typeiiisecretion pages 1-2) | 10.1038/s42003-024-05852-z · https://doi.org/10.1038/s42003-024-05852-z · Feb 2024 | Strong primary evidence; Edwardsiella-specific, but clear effector→host-target→virulence chain. |
| Yersinia T3SS/Yop effectors — inhibit leukotriene B4 synthesis — early immune evasion/enhanced infection | secretion system/proteins/chemical/process | GO:0030257; CHEBI:15639 leukotriene B4; label-only: Yop effectors | “Leukocytes recognize the T3SS and that recognition normally triggers rapid synthesis of leukotriene B4 (LTB4)… several Yop effectors secreted through the T3SS effectively inhibit this host response… exogenous administration of LTB4 prior to infection limited bacterial proliferation.” (brady2024type3secretion pages 1-2) | 10.1371/journal.ppat.1011280 · https://doi.org/10.1371/journal.ppat.1011280 · Jan 2024 | Strong primary evidence; suitable as secretion-system-mediated immune evasion edge; taxon-specific to Y. pestis. |
| dltB / Dlt pathway — decorates wall and lipoteichoic acids — resistance to antimicrobial peptides | gene/pathway/cell-envelope property | label-only: dltB; GO:0047496 D-alanyl-lipoteichoic acid biosynthetic process (candidate); CHEBI:antimicrobial peptide label-only | “dltB is part of an operon that decorates wall and lipoteichoic acids on the bacterial cell surface, promoting resistance to antimicrobial peptides.” (barber2024mechanismsofhost pages 2-3) | 10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · Jul 2024 | Strong for S. aureus host adaptation example; may be curatable as AMP-resistance contributes to host adaptation/human pathogenicity, but not universal. |
| TbpA — binds transferrin — iron acquisition supporting host-specific colonization | receptor protein/protein/nutrient acquisition | label-only: TbpA; label-only: transferrin; CHEBI:18248 iron(3+) | “transferrin… rapidly evolving regions of the protein match closely with the binding surface of transferrin-binding protein A (TbpA)” and “Surface receptors (TbpA and TdfH)… exhibit narrow host specificity for metal-binding proteins… from humans” (barber2024mechanismsofhost pages 3-5, barber2024mechanismsofhost pages 6-7) | 10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · Jul 2024 | Strong for host-specific nutrient acquisition; mostly Neisseria-focused in evidence. |
| IsdB — scavenges heme from human hemoglobin — iron/heme acquisition supporting host specificity | receptor protein/protein/nutrient acquisition | label-only: IsdB; CHEBI:60344 heme; label-only: hemoglobin | “The hemoglobin receptor IsdB from S. aureus selectively scavenges heme from human hemoglobin relative to NHPs and rodents.” (barber2024mechanismsofhost pages 6-7) | 10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · Jul 2024 | Strong; S. aureus-specific example of host-adapted nutrient acquisition. |
| Enhanced lactose utilization — increases fitness in bovine mammary gland — host adaptation via carbohydrate acquisition | metabolic capacity/nutrient/process | CHEBI:17716 lactose; GO:0005989 lactose metabolic process | “bovine mastitis isolates exhibit enhanced utilization of lactose… These results indicate that bovine-associated S. aureus lineages have undergone genetic attenuations to enhance nutrient acquisition.” (barber2024mechanismsofhost pages 6-7) | 10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · Jul 2024 | Good host-adaptation edge, but not specifically human-pathogen positive; probably warning/avoid direct curation for human pathogen unless used as comparative adaptation mechanism. |
| Pathogen attachment to fibrinogen/extracellular matrix — promotes biofilm or abscess formation — exacerbated pathology | protein interaction/process/pathology | label-only: fibrinogen; GO:0042710 biofilm formation; label-only: abscess formation | “attachment further promotes biofilm or abscess formation, exacerbating disease pathology and complicating treatment.” (barber2024mechanismsofhost pages 3-5) | 10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · Jul 2024 | Moderate; broad mechanism but examples mainly staphylococci/streptococci. |
| Type IV secretion system — translocates protein effectors/toxins — host cell manipulation and infection | secretion system/process/process | GO:0030254 protein secretion by the type IV secretion system; GO:0052040 | “T4SSs… function… as protein effector translocators… many have acquired new functionalities relating to translocation of effector proteins or toxins… viewed as viable targets for therapeutic intervention to thwart… infection by pathogens.” (costa2024structuralandfunctional pages 1-5) | 10.1038/s41579-023-00974-3 · https://doi.org/10.1038/s41579-023-00974-3 · Oct 2024 | Strong review-level evidence; broad but not specific to a single human pathogen trait edge unless represented as generic virulence module. |
| VirD4/T4CP — recruits substrates to T4SS — effector translocation | ATPase/complex/process | label-only: VirD4; GO:0030254 | “VirD4-like ATPases… are responsible for substrate recruitment… provide the energy for early-stage substrate processing… The AAD sits at the base of the hexamer, optimally positioned for docking of secretion substrates.” (costa2024structuralandfunctional pages 9-11) | 10.1038/s41579-023-00974-3 · https://doi.org/10.1038/s41579-023-00974-3 · Oct 2024 | Mechanistic sub-edge for secretion system function; not itself a direct human-pathogen determinant. |
| CagY extracellular domain — binds TLR5 sites / regulates host immune responses — persistent infection | protein/receptor/process | label-only: CagY; label-only: TLR5; GO:0050776 regulation of immune response | “the extracellular domain of the CagY subunit… contains multiple binding sites for Toll-like receptor 5 (TLR5) and functions in regulating immune responses of the host… rearrangements… regulate T4SSCag function… to maximize persistent infection.” (costa2024structuralandfunctional pages 9-11) | 10.1038/s41579-023-00974-3 · https://doi.org/10.1038/s41579-023-00974-3 · Oct 2024 | Strong but Helicobacter pylori-specific; good direct host-interaction edge. |
| Inflammasome detection of flagellin/T3SS proteins — activates pyroptosis/inflammatory cytokines — restricts infection | host process/MAMP/process | GO:0061702 inflammasome complex; GO:0006954 inflammatory response; label-only: flagellin; GO:0030257 | “One of the best studied examples involves inflammasome activation by bacterial flagellin and type-3 secretion system (T3SS) proteins.” (barber2024mechanismsofhost pages 6-7) | 10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · Jul 2024 | Host-side edge, valuable context node; not a microbial trait edge by itself. Mark as host factor in graph. |
| GBP1 — recognizes bacterial LPS — cell-autonomous immunity restricting intracellular pathogens | host protein/chemical/process | label-only: GBP1; CHEBI:16412 lipopolysaccharide; GO:0006955 immune response | “mammalian GBP1 contributes to defense against cytoplasmic Gram-negative bacteria by directly recognizing bacterial LPS.” (barber2024mechanismsofhost pages 6-7) | 10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · Jul 2024 | Host-side factor only; include as context node, not as microbial mechanism causing human pathogenicity. |
| Temperate phages / PICIs — carry virulence and immune-modulating genes — altered host tropism/pathogenicity | mobile genetic element/genes/process | label-only: temperate phage; label-only: PICI; SO-like grounding not asserted | “S. aureus genomes carry temperate phages that encode host-specific immune modulators… PICIs encode host-specific immune modulators, mediators of coagulation, and biofilm formation.” (barber2024mechanismsofhost pages 2-3) | 10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · Jul 2024 | Strong review evidence for MGE contribution; indirect trait mechanism, often taxon-specific. |
| IS elements / plasmids / transposons / bacteriophages — mediate horizontal gene transfer — gain of virulence or host-adaptation genes | mobile genetic elements/process/trait | label-only: IS element; plasmid; transposon; bacteriophage | “Horizontal gene transfer… can occur via conjugation (plasmids), transduction (bacteriophages), transposons, insertion sequence (IS) elements…” and acquisition “can be associated with the gain of one or multiple genes that facilitate changes in host species tropism, including virulence factors.” (barber2024mechanismsofhost pages 2-3) | 10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · Jul 2024 | Strong general mechanism; suitable as higher-level causal edge enabling emergence of human-pathogenic lineages. |
| IS element insertion / genome rearrangement / hypermutation — generates genetic diversity — within-host adaptation and chronic infection | genome process/process/trait | label-only: insertion sequence; GO:0006259 DNA metabolic process; label-only: hypermutation | “secondary mechanisms… include generalized… hypermutation… structural variation; and mobile genetic element and phage insertions” and these can “increase pathogenicity… facilitate long-term persistence” (dekker2024withinhostevolutionof pages 2-4, dekker2024withinhostevolutionof pages 1-2) | 10.1146/annurev-pathmechdis-051122-111408 · https://doi.org/10.1146/annurev-pathmechdis-051122-111408 · Jan 2024 | Strong for adaptation process; indirect for trait, but important background graph module. |
| exoU-adjacent insertion sequences — facilitate transfer potential — spread of virulence determinant | mobile element/gene/process | label-only: insertion sequence; label-only: exoU | “BSI_S5 harbored two types of insertion sequences adjacent to exoU, suggesting the potential of exoU to be transferred to other strains.” (wu2024thetypeiii pages 1-2) | 10.1128/spectrum.02224-23 · https://doi.org/10.1128/spectrum.02224-23 · Jan 2024 | Moderate; inference about transfer potential, not direct demonstration. Mark uncertain. |
| agr quorum sensing activity — controls PSM expression/inflammation — invasive virulence state | regulatory system/process/process | label-only: agr quorum sensing; label-only: PSM; GO:0009372 quorum sensing | “Agr quorum sensing (QS) is repeatedly implicated as a central regulatory node: agr activity controls PSM expression (linked to inflammation)… loss of agr function often accompanies transition from commensal to invasive states.” (howden2023staphylococcusaureushost pages 1-5) | 10.1038/s41579-023-00852-y · https://doi.org/10.1038/s41579-023-00852-y · Jan 2023 | Moderate-to-strong review evidence; S. aureus-specific and state-dependent; useful as regulatory module, but not universal. |
| Commensal inhibition of agr quorum sensing — reduces colonization/virulence traits — colonization resistance | microbe–microbe interaction/regulation/process | label-only: lugdunin; fengycins; agr quorum sensing | “Bacillus subtilis… produces fengycins that quench S. aureus agr quorum sensing and prevent gut colonisation… Lactobacillus reuteri interferes with S. aureus Agr.” (howden2023staphylococcusaureushost pages 1-5) | 10.1038/s41579-023-00852-y · https://doi.org/10.1038/s41579-023-00852-y · Jan 2023 | Useful ecological counter-edge; should not be curated as positive cause of human pathogen trait. |
| Biofilm formation — increases treatment resistance/persistence — infection severity | biological process/phenotype/trait | GO:0042710 biofilm formation | “These bacteria can form biofilms, making them resistant to treatment” and ESKAPE pathogens “are biofilm formers” (soni2024understandingbacterialpathogenicity pages 2-4, lazar2023resistancetolerancevirulence pages 1-2) | 10.3389/fmicb.2024.1370818 · https://doi.org/10.3389/fmicb.2024.1370818 · Feb 2024; 10.3390/pathogens12050746 · https://doi.org/10.3390/pathogens12050746 · May 2023 | Broad but somewhat generic; may need more direct mechanistic evidence for specific pathogens before curation. |
| HGT of resistance genes — increases AMR — contributes to infection-associated mortality | process/trait/outcome | label-only: horizontal gene transfer; label-only: AMR | “One of the most important mechanisms of the spread of AR is horizontal gene transfer (HGT)” and AMR was associated with “4.95 million deaths… including 1.27 million deaths directly due to bacterial AMR.” (lazar2023resistancetolerancevirulence pages 1-2) | 10.3390/pathogens12050746 · https://doi.org/10.3390/pathogens12050746 · May 2023 | Indirect for human pathogen trait; important public-health context but should be flagged not to over-interpret as causal for pathogenicity itself. |
| AMR bacterial infections — increase mortality burden — public-health significance of human pathogens | trait/outcome/population statistic | label-only: antimicrobial resistance | “4.95 million deaths were associated with bacterial resistance in 2019, including 1.27 million deaths directly due to bacterial AMR.” (lazar2023resistancetolerancevirulence pages 1-2) | 10.3390/pathogens12050746 · https://doi.org/10.3390/pathogens12050746 · May 2023 | Epidemiologic context only; not a mechanistic TraitMech edge. |
| Opportunity/host-compromise — permits infection by opportunistic pathogens — human disease | environmental/host factor/trait | label-only: compromised host defense; label-only: opportunistic pathogen | “Infections usually occur when the body’s defense are compromised, due to factors like trauma or underlying diseases.” (soni2024understandingbacterialpathogenicity pages 2-4) | 10.3389/fmicb.2024.1370818 · https://doi.org/10.3389/fmicb.2024.1370818 · Feb 2024 | Useful scope/boundary edge; host/environmental factor rather than intrinsic microbial mechanism. |


*Table: This table compiles candidate causal edges for curating the microbial trait 'human pathogen' using only the provided evidence contexts. It emphasizes mechanistic links, suggested grounding, and curation cautions about taxon specificity, indirectness, and host-side factors.*

---

## 8) Warnings / non-curation notes (important for TraitMech)
1. **Taxon-specific mechanisms**: many strong edges (e.g., ExoU, YfiD–PARP1, CEACAM-binding adhesins) are compelling but **not universal**; curate them as exemplars for subclasses of human pathogens rather than as defining edges for all bacteria. (barber2024mechanismsofhost pages 3-5, wu2024thetypeiii pages 1-2, zhou2024typeiiisecretion pages 1-2)
2. **Host-side immunity nodes** (inflammasomes, GBP1) are essential context but should be encoded as **host factors** rather than microbial mechanistic determinants. (barber2024mechanismsofhost pages 6-7)
3. **AMR burden statistics** should not be encoded as “virulence” edges; they are **outcome context**. Mechanistic links like HGT → AMR are valid, but AMR ≠ pathogenicity. (lazar2023resistancetolerancevirulence pages 1-2)
4. **Transfer potential inferences** (e.g., IS adjacent to exoU “suggesting potential transfer”) should be flagged as **uncertain** unless supported by direct mobility assays or epidemiologic transfer evidence. (wu2024thetypeiii pages 1-2)

---

## 9) DOI-first bibliography (with URLs and publication dates)
- Barber MF, Fitzgerald JR. **Mechanisms of host adaptation by bacterial pathogens**. *FEMS Microbiology Reviews*. **Jul 2024**. DOI: **10.1093/femsre/fuae019**. https://doi.org/10.1093/femsre/fuae019 (barber2024mechanismsofhost pages 1-2)
- Costa TRD, Patkowski JB, Macé K, Christie PJ, Waksman G. **Structural and functional diversity of type IV secretion systems**. *Nature Reviews Microbiology*. **Oct 2024**. DOI: **10.1038/s41579-023-00974-3**. https://doi.org/10.1038/s41579-023-00974-3 (costa2024structuralandfunctional pages 1-5)
- Howden BP, Giulieri SG, Lung TWF, et al. **Staphylococcus aureus host interactions and adaptation**. *Nature Reviews Microbiology*. **Jan 2023**. DOI: **10.1038/s41579-023-00852-y**. https://doi.org/10.1038/s41579-023-00852-y (howden2023staphylococcusaureushost pages 1-5)
- Wu T, Zhang Z, Li T, et al. **The type III secretion system facilitates systemic infections of Pseudomonas aeruginosa in the clinic**. *Microbiology Spectrum*. **Jan 2024** (published online Dec 13, 2023). DOI: **10.1128/spectrum.02224-23**. https://doi.org/10.1128/spectrum.02224-23 (wu2024thetypeiii pages 1-2)
- Brady A, Sheneman KR, Pulsifer AR, et al. **Type 3 secretion system induced leukotriene B4 synthesis by leukocytes is actively inhibited by Yersinia pestis to evade early immune recognition**. *PLOS Pathogens*. **Jan 2024**. DOI: **10.1371/journal.ppat.1011280**. https://doi.org/10.1371/journal.ppat.1011280 (brady2024type3secretion pages 1-2)
- Zhou M, Liu Y, Zhang Y, et al. **Type III secretion system effector YfiD inhibits the activation of host poly(ADP-ribose) polymerase-1 to promote bacterial infection**. *Communications Biology*. **Feb 2024**. DOI: **10.1038/s42003-024-05852-z**. https://doi.org/10.1038/s42003-024-05852-z (zhou2024typeiiisecretion pages 1-2)
- Dekker JP. **Within-Host Evolution of Bacterial Pathogens in Acute and Chronic Infection**. *Annual Review of Pathology: Mechanisms of Disease*. **Jan 2024**. DOI: **10.1146/annurev-pathmechdis-051122-111408**. https://doi.org/10.1146/annurev-pathmechdis-051122-111408 (dekker2024withinhostevolutionof pages 2-4)
- Lazar V, Oprea E, Ditu L-M. **Resistance, Tolerance, Virulence and Bacterial Pathogen Fitness—Current State and Envisioned Solutions for the Near Future**. *Pathogens*. **May 2023**. DOI: **10.3390/pathogens12050746**. https://doi.org/10.3390/pathogens12050746 (lazar2023resistancetolerancevirulence pages 1-2)
- Rodríguez-Lucas C, Ladero V. **Enterococcal Phages: Food and Health Applications**. *Antibiotics*. **May 2023**. DOI: **10.3390/antibiotics12050842**. https://doi.org/10.3390/antibiotics12050842 (rodriguezlucas2023enterococcalphagesfood pages 1-2)
- Soni J, Sinha S, Pandey R. **Understanding bacterial pathogenicity: a closer look at the journey of harmful microbes**. *Frontiers in Microbiology*. **Feb 2024**. DOI: **10.3389/fmicb.2024.1370818**. https://doi.org/10.3389/fmicb.2024.1370818 (soni2024understandingbacterialpathogenicity pages 2-4)


References

1. (soni2024understandingbacterialpathogenicity pages 4-5): Jyoti Soni, Sristi Sinha, and Rajesh Pandey. Understanding bacterial pathogenicity: a closer look at the journey of harmful microbes. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1370818, doi:10.3389/fmicb.2024.1370818. This article has 200 citations and is from a peer-reviewed journal.

2. (soni2024understandingbacterialpathogenicity pages 2-4): Jyoti Soni, Sristi Sinha, and Rajesh Pandey. Understanding bacterial pathogenicity: a closer look at the journey of harmful microbes. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1370818, doi:10.3389/fmicb.2024.1370818. This article has 200 citations and is from a peer-reviewed journal.

3. (barber2024mechanismsofhost pages 1-2): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 46 citations and is from a domain leading peer-reviewed journal.

4. (barber2024mechanismsofhost pages 3-5): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 46 citations and is from a domain leading peer-reviewed journal.

5. (barber2024mechanismsofhost pages 6-7): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 46 citations and is from a domain leading peer-reviewed journal.

6. (zhou2024typeiiisecretion pages 1-2): Mengqing Zhou, Yabo Liu, Yibei Zhang, Yue Ma, Yuanxing Zhang, Sang Ho Choi, Shuai Shao, and Qiyao Wang. Type iii secretion system effector yfid inhibits the activation of host poly(adp-ribose) polymerase-1 to promote bacterial infection. Communications Biology, Feb 2024. URL: https://doi.org/10.1038/s42003-024-05852-z, doi:10.1038/s42003-024-05852-z. This article has 10 citations and is from a peer-reviewed journal.

7. (dekker2024withinhostevolutionof pages 2-4): John P. Dekker. Within-host evolution of bacterial pathogens in acute and chronic infection. Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-111408, doi:10.1146/annurev-pathmechdis-051122-111408. This article has 28 citations and is from a domain leading peer-reviewed journal.

8. (barber2024mechanismsofhost pages 2-3): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 46 citations and is from a domain leading peer-reviewed journal.

9. (wu2024thetypeiii pages 1-2): Tiantian Wu, Zhenchuan Zhang, Tong Li, Xu Dong, Dan Wu, Lixia Zhu, Kaijin Xu, and Ying Zhang. The type iii secretion system facilitates systemic infections of <i>pseudomonas aeruginosa</i> in the clinic. Jan 2024. URL: https://doi.org/10.1128/spectrum.02224-23, doi:10.1128/spectrum.02224-23. This article has 20 citations and is from a domain leading peer-reviewed journal.

10. (brady2024type3secretion pages 1-2): Amanda Brady, Katelyn R. Sheneman, Amanda R. Pulsifer, Sarah L. Price, Taylor M. Garrison, Krishna Rao Maddipati, Sobha R. Bodduluri, Jianmin Pan, Nolan L. Boyd, Jing-Juan Zheng, Shesh N. Rai, Jason Hellmann, Bodduluri Haribabu, Silvia M. Uriarte, and Matthew B. Lawrenz. Type 3 secretion system induced leukotriene b4 synthesis by leukocytes is actively inhibited by yersinia pestis to evade early immune recognition. PLOS Pathogens, 20:e1011280, Jan 2024. URL: https://doi.org/10.1371/journal.ppat.1011280, doi:10.1371/journal.ppat.1011280. This article has 11 citations and is from a highest quality peer-reviewed journal.

11. (costa2024structuralandfunctional pages 1-5): Tiago R. D. Costa, Jonasz B. Patkowski, Kévin Macé, Peter J. Christie, and Gabriel Waksman. Structural and functional diversity of type iv secretion systems. Nature reviews. Microbiology, 22:170-185, Oct 2024. URL: https://doi.org/10.1038/s41579-023-00974-3, doi:10.1038/s41579-023-00974-3. This article has 130 citations.

12. (costa2024structuralandfunctional pages 9-11): Tiago R. D. Costa, Jonasz B. Patkowski, Kévin Macé, Peter J. Christie, and Gabriel Waksman. Structural and functional diversity of type iv secretion systems. Nature reviews. Microbiology, 22:170-185, Oct 2024. URL: https://doi.org/10.1038/s41579-023-00974-3, doi:10.1038/s41579-023-00974-3. This article has 130 citations.

13. (costa2024structuralandfunctional media d77bae5c): Tiago R. D. Costa, Jonasz B. Patkowski, Kévin Macé, Peter J. Christie, and Gabriel Waksman. Structural and functional diversity of type iv secretion systems. Nature reviews. Microbiology, 22:170-185, Oct 2024. URL: https://doi.org/10.1038/s41579-023-00974-3, doi:10.1038/s41579-023-00974-3. This article has 130 citations.

14. (costa2024structuralandfunctional media 3d928bb8): Tiago R. D. Costa, Jonasz B. Patkowski, Kévin Macé, Peter J. Christie, and Gabriel Waksman. Structural and functional diversity of type iv secretion systems. Nature reviews. Microbiology, 22:170-185, Oct 2024. URL: https://doi.org/10.1038/s41579-023-00974-3, doi:10.1038/s41579-023-00974-3. This article has 130 citations.

15. (howden2023staphylococcusaureushost pages 1-5): Benjamin P. Howden, Stefano G. Giulieri, Tania Wong Fok Lung, Sarah L. Baines, Liam K. Sharkey, Jean Y. H. Lee, Abderrahman Hachani, Ian R. Monk, and Timothy P. Stinear. Staphylococcus aureus host interactions and adaptation. Nature Reviews. Microbiology, 21:380-395, Jan 2023. URL: https://doi.org/10.1038/s41579-023-00852-y, doi:10.1038/s41579-023-00852-y. This article has 849 citations.

16. (rodriguezlucas2023enterococcalphagesfood pages 1-2): Carlos Rodríguez-Lucas and Victor Ladero. Enterococcal phages: food and health applications. Antibiotics, 12:842, May 2023. URL: https://doi.org/10.3390/antibiotics12050842, doi:10.3390/antibiotics12050842. This article has 27 citations.

17. (lazar2023resistancetolerancevirulence pages 1-2): Veronica Lazar, Eliza Oprea, and Lia-Mara Ditu. Resistance, tolerance, virulence and bacterial pathogen fitness—current state and envisioned solutions for the near future. Pathogens, 12:746, May 2023. URL: https://doi.org/10.3390/pathogens12050746, doi:10.3390/pathogens12050746. This article has 58 citations.

18. (dekker2024withinhostevolutionof pages 1-2): John P. Dekker. Within-host evolution of bacterial pathogens in acute and chronic infection. Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-111408, doi:10.1146/annurev-pathmechdis-051122-111408. This article has 28 citations and is from a domain leading peer-reviewed journal.