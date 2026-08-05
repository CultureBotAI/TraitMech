---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:30:42.985905'
end_time: '2026-08-04T10:41:31.308462'
duration_seconds: 648.32
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: antibiotic resistance
  trait_identifier: traitmech:000088
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: antibiotic_resistance
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A physiological capacity to grow in the presence of antibiotic concentrations
    that inhibit susceptible cells, mediated by efflux, target modification, drug
    inactivation, or reduced permeability.
  parent_traits: METPO:1000059
  synonyms: antimicrobial resistance
  evidence_summary: 'DOI:10.1038/nrmicro3380:  (Blair et al. review the molecular
    mechanisms of antibiotic resistance (efflux, target alteration, drug inactivation,
    reduced uptake).) | DOI:10.1038/s41579-022-00820-y:  (Updated review revisits
    molecular mechanisms of antibiotic resistance.)'
  causal_graph_summary: 'antibiotic_resistance_mechanisms: 12 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** antibiotic resistance
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000088
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological capacity to grow in the presence of antibiotic concentrations that inhibit susceptible cells, mediated by efflux, target modification, drug inactivation, or reduced permeability.
- **Parent traits:** METPO:1000059
- **Synonyms:** antimicrobial resistance
- **Existing evidence:** DOI:10.1038/nrmicro3380:  (Blair et al. review the molecular mechanisms of antibiotic resistance (efflux, target alteration, drug inactivation, reduced uptake).) | DOI:10.1038/s41579-022-00820-y:  (Updated review revisits molecular mechanisms of antibiotic resistance.)
- **Existing causal graph summary:** antibiotic_resistance_mechanisms: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **antibiotic resistance** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/antibiotic_resistance.yaml`.

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
- **Trait label:** antibiotic resistance
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000088
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological capacity to grow in the presence of antibiotic concentrations that inhibit susceptible cells, mediated by efflux, target modification, drug inactivation, or reduced permeability.
- **Parent traits:** METPO:1000059
- **Synonyms:** antimicrobial resistance
- **Existing evidence:** DOI:10.1038/nrmicro3380:  (Blair et al. review the molecular mechanisms of antibiotic resistance (efflux, target alteration, drug inactivation, reduced uptake).) | DOI:10.1038/s41579-022-00820-y:  (Updated review revisits molecular mechanisms of antibiotic resistance.)
- **Existing causal graph summary:** antibiotic_resistance_mechanisms: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **antibiotic resistance** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/antibiotic_resistance.yaml`.

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


# TraitMech curation report: antibiotic resistance

## Record and scope summary

- **Trait:** antibiotic resistance
- **Identifier:** **`traitmech:000088`**
- **Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED
- **Parent:** `METPO:1000059`
- **Recommended operational meaning:** a microbial cell or population can **replicate at an antibiotic concentration that inhibits a defined susceptible comparator**, usually observed as an increased minimum inhibitory concentration (MIC) or categorical nonsusceptibility under a specified susceptibility-testing standard. MIC is the lowest concentration preventing visible replication; therefore, resistance is fundamentally a concentration-, medium-, incubation-, species-, and breakpoint-dependent phenotype rather than an unconditional property of a gene. (maeda2024laboratoryevolutionof pages 1-2)

The supplied definition—“a physiological capacity to grow in the presence of antibiotic concentrations that inhibit susceptible cells, mediated by efflux, target modification, drug inactivation, or reduced permeability”—is consistent with current mechanistic understanding. Canonical mechanisms additionally include **target replacement/protection** and **cell-envelope remodeling**. Resistance may be intrinsic or acquired by mutation or horizontal gene transfer. (maeda2024laboratoryevolutionof pages 1-2, zhu2022clinicalperspectiveof pages 4-5)

### Boundaries and nearby traits

1. **Tolerance is not resistance.** Tolerant populations survive longer exposure without necessarily having an increased MIC; time-kill measures are more appropriate than growth inhibition alone. (maeda2024laboratoryevolutionof pages 1-2, maeda2024laboratoryevolutionof pages 12-13)
2. **Persistence is not resistance.** Persistence is survival of a minority, typically non-growing or slow-growing subpopulation, without a stable population-wide MIC increase. It should be represented separately unless the graph explicitly models an evolutionary route from persistence to inherited resistance. (maeda2024laboratoryevolutionof pages 1-2, maeda2024laboratoryevolutionof pages 12-13)
3. **Heteroresistance is adjacent but distinct.** An isogenic population contains a resistant minority while the majority remains susceptible; routine MIC testing can report the isolate as susceptible. Population analysis profiling is the reference detection approach. Consequently, heteroresistance should not automatically instantiate the population-wide trait. (xu2025epidemiologymechanismsand pages 1-2)
4. **Multidrug resistance is a classification**, requiring resistance across multiple antimicrobial categories; it is not a separate molecular mechanism. A single resistance determinant can be narrow-spectrum or pleiotropic. (zhu2022clinicalperspectiveof pages 2-4)
5. **Biofilm-associated recalcitrance** can combine diffusion effects, altered physiology, tolerance, persistence, and inherited resistance. “Biofilm formation → antibiotic resistance” is too broad for unqualified curation.
6. **Antimicrobial resistance** is broader than antibiotic resistance because it includes antiviral, antifungal, and antiparasitic resistance. This graph should remain bacterial-antibiotic focused unless TraitMech intentionally uses the synonym broadly.

## Candidate nodes grouped by type

Identifiers below are deliberately conservative. Where an exact stable CURIE was not verified from the retrieved evidence, the node is left **label-only** rather than assigned a potentially incorrect identifier.

### Trait and assay nodes

- `traitmech:000088` — antibiotic resistance
- `METPO:1000059` — supplied parent trait
- minimum inhibitory concentration (MIC), label-only
- elevated MIC, label-only
- susceptible comparator, label-only
- antibiotic susceptibility testing, label-only
- clinical breakpoint, label-only
- population analysis profiling, label-only

### Environmental and experimental factors

- antibiotic exposure / selection pressure
- repeated antibiotic exposure
- subinhibitory antibiotic concentration
- inhibitory antibiotic concentration
- growth medium, inoculum, incubation time and temperature
- antibiotic combination or sequential/alternating treatment
- membrane permeabilizer
- metabolic inhibitor

Repeated exposure selects adaptive variants, whereas alternating drugs can slow evolution where collateral-sensitivity trade-offs apply. Laboratory evolution coupled to whole-genome sequencing and phenotyping is a current implementation for identifying such paths. (maeda2024laboratoryevolutionof pages 1-2, maeda2024laboratoryevolutionof pages 12-13, maeda2024laboratoryevolutionof pages 6-7)

### Genes, proteins, enzymes, transporters and complexes

- **Drug inactivation:** β-lactamases; ESBLs; AmpC; carbapenemases; NDM/VIM/IMP metallo-β-lactamases; OXA enzymes; aminoglycoside-modifying enzymes
- **Target replacement/remodeling:** `mecA`, `mecC`, PBP2a; `vanA`, `vanB`, `vanM`, VanHAX; D-Ala-D-Lac ligase
- **Target mutation/modification:** `gyrA`, `gyrB`, `parC`, `parE`; `erm`-family 23S-rRNA methyltransferases; 16S-rRNA methylases; `cfr`
- **Efflux:** AcrAB–TolC; AcrB; RND, MFS, MATE, SMR and ABC transporter families; `tetA`; `msrA`
- **Permeability:** OmpF; OprD/OprD2; porin loss or downregulation
- **Envelope remodeling:** `mcr-1`, `mcr-3`, `mcr-9`; MCR phosphoethanolamine transferases; EptA; PmrAB and PhoPQ regulatory systems
- **Evolution/dissemination:** plasmid, transposon and other mobile genetic element

### Chemicals, structures, cellular locations and processes

- β-lactam antibiotic; carbapenem; aminoglycoside; fluoroquinolone; macrolide; tetracycline; vancomycin; colistin/polymyxin
- β-lactam ring; D-Ala-D-Ala; D-Ala-D-Lac; 23S rRNA; 16S rRNA; lipid A; lipopolysaccharide
- periplasm, cytoplasmic membrane, outer membrane, cell envelope, cytosol, ribosome
- antibiotic hydrolysis; antibiotic covalent modification; active efflux; reduced influx; target alteration; target replacement; target protection; lipid-A phosphoethanolamine modification; horizontal gene transfer; mutation; selection

A useful compact overview is provided below.

| mechanism module | representative subject nodes | intermediate process | phenotype effect | primary scope/qualifier |
|---|---|---|---|---|
| β-lactamase-mediated drug inactivation | β-lactamases; ESBLs; metallo-β-lactamases; OXA enzymes | Hydrolysis of the β-lactam ring inactivates drug before target engagement | Increased resistance to β-lactam antibiotics, including cephalosporins/carbapenems depending on enzyme class (zhu2022clinicalperspectiveof pages 4-5, zhu2022clinicalperspectiveof pages 2-4) | Broad bacterial mechanism; enzyme class and spectrum are taxon/enzyme-specific |
| Target replacement by mecA/PBP2a | mecA; mecC; PBP2a | Acquisition/expression of a low-affinity penicillin-binding protein preserves cell-wall synthesis despite β-lactams | Methicillin/β-lactam resistance in MRSA and related staphylococci (zhu2022clinicalperspectiveof pages 4-5, gajic2025acomprehensiveoverview pages 6-8) | Strongly taxon-specific to staphylococci/MRSA context |
| Van operon remodeling of peptidoglycan precursors | vanA; vanB; vanM; VanHAX; D-Ala-D-Lac ligase activity | Replacement of D-Ala-D-Ala with D-Ala-D-Lac or D-Ala-D-Ser reduces glycopeptide binding | Vancomycin/glycopeptide resistance (gajic2025acomprehensiveoverview pages 6-8, zhu2022clinicalperspectiveof pages 2-4) | Best supported in Enterococcus; transferable to other taxa but should be curated with taxon qualifiers |
| Fluoroquinolone target alteration | gyrA; gyrB; parC; parE | Mutations alter DNA gyrase/topoisomerase IV quinolone-resistance determining regions | Reduced fluoroquinolone susceptibility/resistance (zhu2022clinicalperspectiveof pages 4-5, zhu2022clinicalperspectiveof pages 2-4) | Common across multiple taxa; specific mutation effects are taxon- and drug-dependent |
| Ribosomal target modification by erm | erm genes; 23S rRNA methyltransferase | Methylation of 23S rRNA alters antibiotic binding site on the ribosome | Macrolide/lincosamide/streptogramin resistance (nazir2025theglobalchallenge pages 1-2, gajic2025acomprehensiveoverview pages 6-8) | Gene-family broad; exact spectrum varies by erm allele and host taxon |
| Active multidrug efflux | AcrAB-TolC; RND efflux pumps | Energy-dependent export lowers intracellular antibiotic concentration | Multidrug resistance or elevated MICs to several classes (maeda2024laboratoryevolutionof pages 6-7, zhu2022clinicalperspectiveof pages 4-5) | Canonical Gram-negative module; AcrAB-TolC is especially representative for Enterobacterales/E. coli |
| Reduced outer-membrane permeability | OmpF; OprD/OprD2; porin loss/downregulation | Decreased porin abundance restricts antibiotic entry | Lower susceptibility, especially for β-lactams and some other hydrophilic drugs (zhu2022clinicalperspectiveof pages 4-5, nazir2025theglobalchallenge pages 1-2) | Strongly assay/taxon dependent; important in Gram-negative outer membrane context |
| Lipid A phosphoethanolamine modification | mcr-1; MCR family; EptA-like phosphoethanolamine transferases | Addition of phosphoethanolamine to lipid A reduces colistin binding to LPS | Colistin/polymyxin resistance or decreased susceptibility (gao2016disseminationandmechanism pages 8-10, gaballa2023morethanmcr pages 1-2, schumann2024siteselectivemodificationsby pages 17-18) | Strongest direct evidence from Enterobacteriaceae/heterologous expression systems; site-selective effects differ among PET family members |
| Horizontal gene transfer of resistance determinants | plasmids; transposons; mobile genetic elements carrying mcr or other AMR genes | Mobilization and transfer disseminate resistance genes between strains/species | Acquisition and spread of antibiotic resistance traits (nazir2025theglobalchallenge pages 1-2, gaballa2023morethanmcr pages 1-2) | Broad ecological mechanism; specific transferred determinants should be modeled separately |
| Antibiotic selection pressure | antibiotic exposure; repetitive antibiotic treatments; subinhibitory or inhibitory concentrations | Exposure selects resistant mutants/subpopulations and enriches acquired determinants | Evolution and maintenance of resistance phenotypes in populations (maeda2024laboratoryevolutionof pages 1-2, maeda2024laboratoryevolutionof pages 12-13) | Population/evolutionary process rather than a single molecular mechanism; context and regimen matter |
| Aminoglycoside enzymatic modification | aminoglycoside-modifying enzymes; 16S rRNA methylases | Drug modification and/or ribosomal target protection lowers effective binding | Aminoglycoside resistance (zhu2022clinicalperspectiveof pages 4-5, zhu2022clinicalperspectiveof pages 2-4) | Included as adjacent high-value module even if not one of the ten requested core rows; curate with class-specific scope |


*Table: This compact table summarizes curation-ready mechanism modules for traitmech:000088, linking representative nodes to intermediate processes and phenotype effects. It is useful as a quick companion to the fully cited report when selecting graph nodes and edge qualifiers.*

## Candidate evidence-backed causal edges

The snippets are concise evidence extracts or close source summaries generated from the retrieved full text. **High** means suitable for core curation with the stated qualifier; **moderate** means curate only with taxon, allele, drug, or assay context.

| # | Subject — predicate → object | Reference and supporting snippet | Curation notes |
|---:|---|---|---|
| 1 | antibiotic concentration — **is measured for growth inhibition by** → MIC | Maeda & Furusawa 2024: MIC is “the lowest antibiotic concentration inhibiting bacterial replication.” (maeda2024laboratoryevolutionof pages 1-2) | **High.** Use as an observation/assay edge, not as a molecular mechanism. Breakpoint and protocol must be contextual metadata. |
| 2 | repeated antibiotic exposure — **selects for** → elevated MIC / antibiotic resistance | Maeda & Furusawa 2024: with “repetitive antibiotic exposures, bacterial populations will adapt and eventually become tolerant and resistant.” (maeda2024laboratoryevolutionof pages 1-2) | **Moderate.** Population-level evolutionary edge; regimen-dependent and not deterministic. |
| 3 | horizontal gene transfer — **causes acquisition of** → resistance determinants | Maeda & Furusawa 2024 identifies resistance mechanisms arising from “de novo mutations or horizontal gene transfer.” (maeda2024laboratoryevolutionof pages 1-2) | **High as a general process**, but preferably instantiate determinant-specific transfer edges. |
| 4 | plasmid/transposon carrying a resistance gene — **transfers** → resistance gene | Current reviews identify dominant dissemination through “plasmids and transposons.” (nazir2025theglobalchallenge pages 1-2) | **High**, provided donor, recipient, mobile element and gene are recorded when known. |
| 5 | β-lactamase — **hydrolyzes** → β-lactam ring | Zhu et al. 2022: β-lactamases, including ESBLs, MBLs and OXAs, “destroy β-lactam rings.” (zhu2022clinicalperspectiveof pages 4-5, zhu2022clinicalperspectiveof pages 2-4) | **High.** Separate enzyme subclasses because substrate spectrum differs. |
| 6 | β-lactam hydrolysis — **inactivates** → β-lactam antibiotic | β-lactamases “hydrolyze the β-lactam ring, inactivating drug efficacy.” (zhu2022clinicalperspectiveof pages 2-4) | **High.** A clean intermediate edge linking enzymatic activity to phenotype. |
| 7 | `mecA` — **encodes** → PBP2a | Zhu et al. 2022: “mecA gene encoding low-affinity PBP2a.” (zhu2022clinicalperspectiveof pages 4-5) | **High; taxon-specific.** Principally staphylococci; `mecC` is a related but separate determinant. |
| 8 | PBP2a — **reduces binding/target inhibition by** → β-lactam antibiotics | PBP2a has reduced β-lactam affinity and is the primary basis of MRSA β-lactam resistance. (zhu2022clinicalperspectiveof pages 4-5, gajic2025acomprehensiveoverview pages 6-8) | **High in MRSA/staphylococci.** Do not generalize PBP2a to all β-lactam-resistant bacteria. |
| 9 | VanA/VanHAX pathway — **replaces** → D-Ala-D-Ala with D-Ala-D-Lac | Van genes modify the dipeptide target; D-Ala-D-Lac/D-Ala-D-Ser products reduce glycopeptide binding. (gajic2025acomprehensiveoverview pages 6-8, zhu2022clinicalperspectiveof pages 2-4) | **High in vancomycin-resistant enterococci; transferable but taxon-qualified elsewhere.** |
| 10 | D-Ala-D-Lac peptidoglycan precursor — **reduces binding of** → vancomycin | Target remodeling can reduce vancomycin-binding affinity by up to approximately 1000-fold. (zhu2022clinicalperspectiveof pages 2-4) | **High**, but the magnitude belongs in source-specific evidence, not as a universal constant. |
| 11 | `gyrA`/`parC` mutation — **alters** → DNA gyrase/topoisomerase IV antibiotic target | Fluoroquinolone resistance involves `gyrA/B` and `parC/E` mutations. (zhu2022clinicalperspectiveof pages 4-5, zhu2022clinicalperspectiveof pages 2-4) | **Moderate until allele grounded.** Individual substitutions have drug- and taxon-specific effects. |
| 12 | altered DNA gyrase/topoisomerase IV — **reduces susceptibility to** → fluoroquinolone | Same sources connect target mutations to fluoroquinolone resistance. (zhu2022clinicalperspectiveof pages 4-5, zhu2022clinicalperspectiveof pages 2-4) | **High at module level;** precise causal claims should identify substitution and organism. |
| 13 | `erm`-encoded methyltransferase — **methylates** → 23S rRNA | Reviews describe “ribosome methylation (erm)” as a macrolide resistance pathway. (gajic2025acomprehensiveoverview pages 6-8, nazir2025theglobalchallenge pages 1-2) | **High at family level.** Resistance spectrum varies among `erm` alleles and expression states. |
| 14 | 23S-rRNA methylation — **reduces antibiotic binding and causes** → macrolide/lincosamide/streptogramin resistance | The methylated ribosomal target is linked to macrolide-class resistance. (gajic2025acomprehensiveoverview pages 6-8, nazir2025theglobalchallenge pages 1-2) | **High**, with antibiotic-class qualifier. |
| 15 | aminoglycoside-modifying enzyme — **covalently modifies/inactivates** → aminoglycoside | Aminoglycoside resistance includes AMEs and target methylation. (zhu2022clinicalperspectiveof pages 4-5, zhu2022clinicalperspectiveof pages 2-4) | **Moderate as written.** Split into acetyltransferase, phosphotransferase and nucleotidyltransferase edges when enzyme identity is known. |
| 16 | AcrAB–TolC / RND efflux — **exports** → antibiotic | Efflux families confer resistance to multiple classes; laboratory evolution repeatedly implicated `acrB`. (maeda2024laboratoryevolutionof pages 6-7, zhu2022clinicalperspectiveof pages 4-5) | **High for direct export where substrate is demonstrated.** “Efflux causes MDR” requires substrate and expression evidence. |
| 17 | increased efflux — **decreases** → intracellular antibiotic concentration | Active efflux is a canonical drug-transport resistance mechanism. (maeda2024laboratoryevolutionof pages 1-2, zhu2022clinicalperspectiveof pages 4-5) | **High mechanistic intermediate.** Energy dependence and membrane localization can be added as contextual nodes. |
| 18 | OmpF/OprD loss or downregulation — **decreases** → outer-membrane antibiotic influx | Porin loss, including OprD2 defects, reduces susceptibility; laboratory evolution also implicates `ompF`. (maeda2024laboratoryevolutionof pages 6-7, zhu2022clinicalperspectiveof pages 4-5) | **High but Gram-negative and drug-specific.** OprD is especially relevant to selected carbapenems in *Pseudomonas*. |
| 19 | reduced antibiotic influx — **increases** → antibiotic resistance | Reduced permeability is a canonical mechanism, often synergizing with β-lactamase or efflux activity. (zhu2022clinicalperspectiveof pages 4-5, nazir2025theglobalchallenge pages 1-2) | **High as a module**, but avoid implying porin loss alone always crosses a clinical breakpoint. |
| 20 | `mcr-1` — **encodes** → MCR-1 phosphoethanolamine transferase | Gao et al. 2016 identifies MCR-1 as a plasmid-borne PEA lipid-A transferase; membrane region and substrate-binding motif are required. (gao2016disseminationandmechanism pages 8-10, gao2016disseminationandmechanism pages 1-2) | **High.** Direct mutagenesis/MIC evidence, principally heterologous *E. coli* and Enterobacterales. |
| 21 | MCR-1 — **adds phosphoethanolamine to** → lipid A | MCR proteins “modify lipid A by adding phosphoethanolamine.” (gaballa2023morethanmcr pages 1-2, gao2016disseminationandmechanism pages 1-2) | **High.** Periplasmic/cell-envelope localization can be represented separately. |
| 22 | phosphoethanolamine-modified lipid A — **reduces binding of** → colistin/polymyxin | Modification neutralizes negative membrane charge and reduces colistin binding/susceptibility. (gaballa2023morethanmcr pages 1-2, gao2016disseminationandmechanism pages 1-2) | **High for Gram-negative bacteria.** Avoid extending to organisms lacking lipid A/LPS. |
| 23 | MCR-1/MCR-3 modification of lipid-A 4′-phosphate — **lowers** → colistin susceptibility | Schumann et al. 2024: MCR-1 and MCR-3 selectively modify the 4′ phosphate, associated with lowered susceptibility and low fitness cost. (schumann2024siteselectivemodificationsby pages 17-18) | **High but assay- and taxon-specific:** isogenic expression in *E. coli*. MCR-9/EptA behavior differs. |
| 24 | antibiotic-resistance mutation — **causes** → collateral sensitivity to a second antibiotic | Laboratory evolution found 157 collateral-sensitivity and 336 cross-resistance drug pairs. (maeda2024laboratoryevolutionof pages 6-7) | **Uncertain for generic graph.** Curate only as mutation–drug-A–drug-B-specific edges; signs can reverse by background. |

## Recommended graph architecture

A robust YAML graph should avoid direct “gene → antibiotic resistance” shortcuts where mechanistic intermediates are known. A preferred pattern is:

**determinant or perturbation → molecular activity → altered drug/target/transport state → intracellular effective exposure or target engagement → elevated MIC/growth under antibiotic → `traitmech:000088`.**

For example:

`mcr-1` → MCR-1 enzyme → phosphoethanolamine-modified lipid A → reduced colistin binding → reduced colistin susceptibility → `traitmech:000088`.

This layered architecture supports reuse across taxa and drugs, makes negative or inhibitory edges explicit, and separates genotype from assay-observed phenotype.

## Recent developments, applications and expert analysis

### 2023–2024 mechanistic advances

- A 2023 comparative study found **69,814 mcr-like genes across 256 genera** and 125 putative novel plasmid-associated candidates. Crucially, sequence similarity alone could not reliably distinguish resistance-conferring MCR proteins from intrinsic phosphoethanolamine transferases. For curation, an MCR-like sequence should therefore not be asserted to cause resistance without functional or high-quality phenotype evidence. (gaballa2023morethanmcr pages 1-2)
- A December 2024 isogenic-expression study refined the MCR mechanism: MCR-1/MCR-3 preferentially modified lipid A’s 4′ phosphate and lowered colistin susceptibility with relatively low fitness costs, whereas MCR-9 and EptA modified a different phosphate and had different phenotypic effects. This argues for **allele-specific edges**, not one generic “PET → colistin resistance” assertion. (schumann2024siteselectivemodificationsby pages 17-18)
- Laboratory evolution studies now integrate serial exposure, phenotyping, genome sequencing and transcriptomics. Approximately **27% of implicated resistance mutations were loss-of-function mutations** in the reviewed experiments, and transport, porin and metabolic changes emerged repeatedly. (maeda2024laboratoryevolutionof pages 6-7)
- Quantified cross-resistance and collateral-sensitivity networks are being used to design alternating or combination regimens. Alternation can slow resistance evolution, but the interaction is genotype-, environment- and order-dependent, so these edges require unusually precise provenance. (maeda2024laboratoryevolutionof pages 12-13, maeda2024laboratoryevolutionof pages 6-7)

### Current real-world implementations

1. **Clinical susceptibility testing:** MIC, disk diffusion and automated growth assays remain the phenotype-level basis for treatment categorization. Genotype does not replace phenotype because expression, gene background, permeability, heteroresistance and breakpoint rules affect the result. (maeda2024laboratoryevolutionof pages 1-2, xu2025epidemiologymechanismsand pages 1-2)
2. **Genomic surveillance:** sequencing detects mobile determinants such as `mecA`, carbapenemases and `mcr`, tracks plasmid/transposon dissemination, and supports outbreak analysis. However, the MCR/PET study demonstrates why sequence-only functional assignment can overcall resistance. (gaballa2023morethanmcr pages 1-2)
3. **Combination treatment and adjuvants:** β-lactam/β-lactamase-inhibitor combinations directly inhibit a resistance mechanism; membrane permeabilizers, efflux inhibitors and metabolic inhibitors are mechanistically rational but organism- and toxicity-dependent. Laboratory evolution can identify combinations that exploit collateral sensitivity. (maeda2024laboratoryevolutionof pages 6-7)
4. **Heteroresistance detection:** population analysis profiling is the reference method because a minority resistant subpopulation can be missed by routine MIC testing. Reported examples include ceftazidime-avibactam heteroresistance in *K. pneumoniae* (11.55%), tigecycline heteroresistance up to 56% in *A. baumannii*, and fosfomycin heteroresistance around 10% in Enterobacterales; these are organism–drug-specific estimates, not global prevalence values. (xu2025epidemiologymechanismsand pages 1-2)
5. **Stewardship and infection prevention:** recent burden modeling supports improved care, antibiotic access, stewardship, vaccination and new Gram-negative drugs as complementary—not interchangeable—interventions. (naghavi2024globalburdenof pages 17-18, naghavi2024globalburdenof pages 2-3)

### Current burden

The September 2024 *Lancet* analysis used approximately **520 million records/isolates**, 19,513 study-location-years, 22 pathogens and 11 infectious syndromes across 204 countries. It estimated **1.14 million deaths attributable to bacterial AMR** and **4.71 million deaths associated with AMR in 2021**. Attributable mortality fell by more than 50% among children under five between 1990 and 2021 but rose by more than 80% among adults aged 70 years or older. MRSA-associated deaths increased from approximately 261,000 in 1990 to 550,000 in 2021, while carbapenem-resistant Gram-negative infections were associated with about 1.03 million deaths in 2021. (naghavi2024globalburdenof pages 1-2, naghavi2024globalburdenof pages 3-4)

Under the reference forecast, deaths directly attributable to AMR reach approximately **1.91 million in 2050**, with about **8.22 million associated deaths**. Modeled improvements in care and antibiotic access could avert 92.0 million deaths during 2025–2050, while a scenario with new Gram-negative-active drugs could avert 11.1 million. These are model-based counterfactual estimates, not observed effects. (naghavi2024globalburdenof pages 1-2, naghavi2024globalburdenof pages 17-18)

## Ontology-grounding recommendations

- Preserve the supplied trait CURIE exactly: **`traitmech:000088`**.
- Preserve the supplied parent exactly: **`METPO:1000059`**.
- Ground **chemicals** to ChEBI only after confirming the precise entity: antibiotic class versus individual active ingredient, protonation state and conjugate form can have different identifiers.
- Ground **processes/functions/localizations** to GO only after confirming whether the node denotes molecular function (e.g., transporter or hydrolase activity), biological process (drug export), or cellular component (outer membrane/periplasm).
- Ground **enzymes** to EC only where the reaction class is unambiguous; individual β-lactamase families and resistance proteins are better represented with UniProt or AMR-database accessions plus gene labels.
- Ground **reactions** to Rhea when a curated reaction exists, particularly β-lactam hydrolysis and phosphoethanolamine transfer to lipid A.
- Ground taxa with NCBITaxon at the strain/species level supported by each experiment. Do not attach an *E. coli* heterologous-expression result universally to Bacteria.
- Retain label-only nodes for MIC, clinical breakpoint, resistant subpopulation and elevated intracellular efflux until the project’s preferred assay/phenotype ontologies are confirmed.

## Warnings: claims not yet ready for unconditional TraitMech curation

1. **Presence of a resistance gene does not guarantee the trait.** Expression, promoter context, copy number, host background and epistasis matter.
2. **Do not curate every MCR-like sequence as colistin resistance.** Sequence similarity cannot reliably separate bona fide MCR from intrinsic PET enzymes; functional evidence is required. (gaballa2023morethanmcr pages 1-2)
3. **Do not collapse tolerance, persistence or heteroresistance into `traitmech:000088`.** They require separate phenotype nodes and assays. (maeda2024laboratoryevolutionof pages 1-2, xu2025epidemiologymechanismsand pages 1-2)
4. **Avoid universal porin-loss edges.** The effect depends on the porin, drug, organism and accompanying β-lactamase/efflux mechanisms.
5. **Avoid universal biofilm → resistance edges.** Much biofilm-associated survival is tolerance or spatial protection rather than inherited MIC elevation.
6. **Do not curate collateral sensitivity generically.** It must specify the selected drug, second drug, mutation/background, environment and direction of effect. (maeda2024laboratoryevolutionof pages 6-7)
7. **Do not use epidemiological association as a cell-level causal edge.** Burden, mortality and treatment-failure statistics motivate prioritization but do not establish molecular causality.
8. **Distinguish intrinsic and acquired resistance.** Chromosomal EptA/PmrAB/PhoPQ remodeling and plasmid-borne `mcr` may converge phenotypically but have different regulation and dissemination.
9. **Record assay context.** MIC medium, inoculum, incubation, drug concentration and interpretive standard can alter the resistant/susceptible label.
10. **Use taxon qualifiers aggressively.** PBP2a is principally a staphylococcal mechanism; D-Ala-D-Lac is best established in enterococci; OprD effects are prominent in *Pseudomonas*; lipid-A mechanisms apply to LPS-bearing Gram-negative bacteria.

## DOI-first bibliography

1. **Naghavi M, et al.** “Global burden of bacterial antimicrobial resistance 1990–2021: a systematic analysis with forecasts to 2050.” *The Lancet* 404, 1199–1226. Published September 2024. DOI: [10.1016/S0140-6736(24)01867-1](https://doi.org/10.1016/S0140-6736(24)01867-1). (naghavi2024globalburdenof pages 1-2)
2. **Maeda T, Furusawa C.** “Laboratory Evolution of Antimicrobial Resistance in Bacteria to Develop Rational Treatment Strategies.” *Antibiotics* 13, 94. Published January 2024. DOI: [10.3390/antibiotics13010094](https://doi.org/10.3390/antibiotics13010094). (maeda2024laboratoryevolutionof pages 1-2)
3. **Schumann A, et al.** “Site-selective modifications by lipid A phosphoethanolamine transferases linked to colistin resistance and bacterial fitness.” *mSphere* 9. Published December 2024. DOI: [10.1128/msphere.00731-24](https://doi.org/10.1128/msphere.00731-24). (schumann2024siteselectivemodificationsby pages 17-18)
4. **Gaballa A, Wiedmann M, Carroll LM.** “More than mcr: canonical plasmid- and transposon-encoded mobilized colistin resistance genes represent a subset of phosphoethanolamine transferases.” *Frontiers in Cellular and Infection Microbiology* 13. Published June 2023. DOI: [10.3389/fcimb.2023.1060519](https://doi.org/10.3389/fcimb.2023.1060519). (gaballa2023morethanmcr pages 1-2)
5. **Baran A, Kwiatkowska A, Potocki L.** “Antibiotics and Bacterial Resistance—A Short Story of an Endless Arms Race.” *International Journal of Molecular Sciences* 24, 5777. Published March 2023. DOI: [10.3390/ijms24065777](https://doi.org/10.3390/ijms24065777).
6. **Zhu Y, Huang WE, Yang Q.** “Clinical Perspective of Antimicrobial Resistance in Bacteria.” *Infection and Drug Resistance* 15, 735–746. Published March 2022. DOI: [10.2147/IDR.S345574](https://doi.org/10.2147/IDR.S345574). (zhu2022clinicalperspectiveof pages 4-5, zhu2022clinicalperspectiveof pages 2-4)
7. **Gao R, et al.** “Dissemination and Mechanism for the MCR-1 Colistin Resistance.” *PLOS Pathogens* 12, e1005957. Published November 2016. DOI: [10.1371/journal.ppat.1005957](https://doi.org/10.1371/journal.ppat.1005957). (gao2016disseminationandmechanism pages 8-10, gao2016disseminationandmechanism pages 1-2)
8. **Blair JMA, Webber MA, Baylay AJ, Ogbolu DO, Piddock LJV.** “Molecular mechanisms of antibiotic resistance.” *Nature Reviews Microbiology* 13, 42–51. Published December 2014 online / 2015 issue. DOI: [10.1038/nrmicro3380](https://doi.org/10.1038/nrmicro3380). Supplied existing evidence.
9. **Darby EM, et al.** Updated review of molecular antibiotic-resistance mechanisms. *Nature Reviews Microbiology*. Published 2023 issue cycle. DOI: [10.1038/s41579-022-00820-y](https://doi.org/10.1038/s41579-022-00820-y). Supplied existing evidence.

## Curation priority

For the existing 12-node/7-edge graph, the strongest expansion is to add four mechanistic modules with explicit intermediates: **(i) β-lactamase hydrolysis, (ii) PBP2a target replacement, (iii) VanA-mediated D-Ala-D-Lac remodeling, and (iv) MCR-mediated lipid-A phosphoethanolamine modification**. Efflux and permeability should then be represented as transport modules, followed by determinant-specific target mutations. Evolutionary selection, horizontal transfer, heteroresistance and collateral sensitivity are valuable secondary layers but should not replace the core cell-level mechanism graph.

References

1. (maeda2024laboratoryevolutionof pages 1-2): Tomoya Maeda and Chikara Furusawa. Laboratory evolution of antimicrobial resistance in bacteria to develop rational treatment strategies. Antibiotics, 13:94, Jan 2024. URL: https://doi.org/10.3390/antibiotics13010094, doi:10.3390/antibiotics13010094. This article has 46 citations.

2. (zhu2022clinicalperspectiveof pages 4-5): Ying Zhu, Wei E. Huang, and Qiwen Yang. Clinical perspective of antimicrobial resistance in bacteria. Infection and Drug Resistance, 15:735-746, Mar 2022. URL: https://doi.org/10.2147/idr.s345574, doi:10.2147/idr.s345574. This article has 235 citations and is from a peer-reviewed journal.

3. (maeda2024laboratoryevolutionof pages 12-13): Tomoya Maeda and Chikara Furusawa. Laboratory evolution of antimicrobial resistance in bacteria to develop rational treatment strategies. Antibiotics, 13:94, Jan 2024. URL: https://doi.org/10.3390/antibiotics13010094, doi:10.3390/antibiotics13010094. This article has 46 citations.

4. (xu2025epidemiologymechanismsand pages 1-2): Linna Xu, Xiaofen Mo, Hui Zhang, Fen Wan, Qixia Luo, and Yonghong Xiao. Epidemiology, mechanisms, and clinical impact of bacterial heteroresistance. npj Antimicrobials and Resistance, Jan 2025. URL: https://doi.org/10.1038/s44259-025-00076-5, doi:10.1038/s44259-025-00076-5. This article has 30 citations and is from a peer-reviewed journal.

5. (zhu2022clinicalperspectiveof pages 2-4): Ying Zhu, Wei E. Huang, and Qiwen Yang. Clinical perspective of antimicrobial resistance in bacteria. Infection and Drug Resistance, 15:735-746, Mar 2022. URL: https://doi.org/10.2147/idr.s345574, doi:10.2147/idr.s345574. This article has 235 citations and is from a peer-reviewed journal.

6. (maeda2024laboratoryevolutionof pages 6-7): Tomoya Maeda and Chikara Furusawa. Laboratory evolution of antimicrobial resistance in bacteria to develop rational treatment strategies. Antibiotics, 13:94, Jan 2024. URL: https://doi.org/10.3390/antibiotics13010094, doi:10.3390/antibiotics13010094. This article has 46 citations.

7. (gajic2025acomprehensiveoverview pages 6-8): Ina Gajic, Nina Tomic, Bojana Lukovic, Milos Jovicevic, Dusan Kekic, Milos Petrovic, Marko Jankovic, Anika Trudic, Dragana Mitic Culafic, Marina Milenkovic, and Natasa Opavski. A comprehensive overview of antibacterial agents for combating multidrug-resistant bacteria: the current landscape, development, future opportunities, and challenges. Antibiotics, 14:221, Feb 2025. URL: https://doi.org/10.3390/antibiotics14030221, doi:10.3390/antibiotics14030221. This article has 124 citations.

8. (nazir2025theglobalchallenge pages 1-2): Abubakar Nazir, Awais Nazir, Varisha Zuhair, Shafaq Aman, Safi Ur Rehman Sadiq, Abdul Haseeb Hasan, Maryam Tariq, Latif Ur Rehman, Mubarak Jolayemi Mustapha, and Deusdedith Boniphace Bulimbe. The global challenge of antimicrobial resistance: mechanisms, case studies, and mitigation approaches. Health Science Reports, Jul 2025. URL: https://doi.org/10.1002/hsr2.71077, doi:10.1002/hsr2.71077. This article has 138 citations and is from a peer-reviewed journal.

9. (gao2016disseminationandmechanism pages 8-10): Rongsui Gao, Yongfei Hu, Zhencui Li, Jian Sun, Qingjing Wang, Jingxia Lin, Huiyan Ye, Fei Liu, Swaminath Srinivas, Defeng Li, Baoli Zhu, Ya-Hong Liu, Guo-Bao Tian, and Youjun Feng. Dissemination and mechanism for the mcr-1 colistin resistance. PLOS Pathogens, 12:e1005957, Nov 2016. URL: https://doi.org/10.1371/journal.ppat.1005957, doi:10.1371/journal.ppat.1005957. This article has 349 citations and is from a highest quality peer-reviewed journal.

10. (gaballa2023morethanmcr pages 1-2): Ahmed Gaballa, Martin Wiedmann, and Laura M. Carroll. More than mcr: canonical plasmid- and transposon-encoded mobilized colistin resistance genes represent a subset of phosphoethanolamine transferases. Frontiers in Cellular and Infection Microbiology, Jun 2023. URL: https://doi.org/10.3389/fcimb.2023.1060519, doi:10.3389/fcimb.2023.1060519. This article has 24 citations.

11. (schumann2024siteselectivemodificationsby pages 17-18): Anna Schumann, Ahmed Gaballa, Hyojik Yang, Di Yu, Robert K. Ernst, and Martin Wiedmann. Site-selective modifications by lipid a phosphoethanolamine transferases linked to colistin resistance and bacterial fitness. Dec 2024. URL: https://doi.org/10.1128/msphere.00731-24, doi:10.1128/msphere.00731-24. This article has 12 citations and is from a peer-reviewed journal.

12. (gao2016disseminationandmechanism pages 1-2): Rongsui Gao, Yongfei Hu, Zhencui Li, Jian Sun, Qingjing Wang, Jingxia Lin, Huiyan Ye, Fei Liu, Swaminath Srinivas, Defeng Li, Baoli Zhu, Ya-Hong Liu, Guo-Bao Tian, and Youjun Feng. Dissemination and mechanism for the mcr-1 colistin resistance. PLOS Pathogens, 12:e1005957, Nov 2016. URL: https://doi.org/10.1371/journal.ppat.1005957, doi:10.1371/journal.ppat.1005957. This article has 349 citations and is from a highest quality peer-reviewed journal.

13. (naghavi2024globalburdenof pages 17-18): M. Naghavi, S. Vollset, K. Ikuta, Lucien R. Swetschinski, Authia Gray, Eve E Wool, G. Aguilar, T. Meštrović, Georgia Smith, Chieh Han, Rebecca L Hsu, Julian Chalek, Daniel T Araki, Erin Chung, Cat Raggi, A. Hayoon, N. Weaver, Paulina A Lindstedt, Amanda E Smith, Umut Altay, N. V. Bhattacharjee, Konstantinos Giannakis, F. Fell, Barney McManigal, N. Ekapirat, J. Mendes, Tilleye Runghien, Oraya Srimokla, A. Abdelkader, S. Abd-Elsalam, R. Aboagye, Hassan Abolhassani, Hasan Abualruz, U. Abubakar, Hana J. Abukhadijah, Salahdein Aburuz, Ahmed Abu-Zaid, Sureerak Achalapong, Isaac Yeboah Addo, Victor Adekanmbi, T. AdeyeOluwa, Q. Adnani, Leticia Akua Adzigbli, M. Afzal, Saira Afzal, A. Agodi, Austin J Ahlstrom, Aqeel Ahmad, Sajjad Ahmad, Tauseef Ahmad, Alireza Ahmadi, Ayman Ahmed, H. Ahmed, Ibrar Ahmed, Mohammed Ahmed, Saeed Ahmed, Syed Anees Ahmed, Mohammed Ahmed Akkaif, S. Awaidy, Yazan Al Thaher, Samer O. Alalalmeh, M. Albataineh, W. Aldhaleei, A. Al-Gheethi, N. Alhaji, Abid Ali, Liaqat Ali, Syed Shujait Shujait Ali, Waad Ali, K. Allel, Sabah Al-Marwani, Ahmad Alrawashdeh, Awais Altaf, Ala’a B. Al-Tammemi, J. Al-Tawfiq, K. Alzoubi, W. Al-Zyoud, B. Amos, J. Amuasi, R. Ancuceanu, J. R. Andrews, Abhishek Anil, Iyadunni A. Anuoluwa, Saeid Anvari, A. Anyasodor, G. L. Apostol, J. Arabloo, M. Arafat, A. Aravkin, D. Areda, A. Aremu, A. Artamonov, Elizabeth A. Ashley, M. Asika, S. Athari, M. Atout, T. Awoke, S. Azadnajafabad, James M Azam, Shahkaar Aziz, A. Azzam, Mahsa Babaei, François-Xavier Babin, Muhammad Badar, A. Baig, Milica Bajcetic, Stephen Baker, Mainak Bardhan, H. Barqawi, Z. Basharat, A. Basiru, M. Bastard, S. Basu, N. Bayleyegn, M. A. Belete, O. Bello, Apostolos Beloukas, J. Berkley, A. Bhagavathula, Sonu M M Bhaskar, S. Bhuyan, J. Bielicki, N. I. Briko, C. Brown, A. Browne, Danilo Buonsenso, Yasser K. Bustanji, Cristina G Carvalheiro, C. Castañeda-Orjuela, Muthia Cenderadewi, J. Chadwick, S. Chakraborty, R. Chandika, Sara Chandy, Vilada Chansamouth, Vijay Kumar Chattu, A. Chaudhary, Patrick R. Ching, Hitesh Chopra, F. Chowdhury, D. Chu, M. Chutiyami, N. Cruz-Martins, A. Silva, O. Dadras, X. Dai, S. Darcho, Saswati Das, F. D. L. Hoz, D. Dekker, K. Dhama, D. Díaz, B. Dickson, S. Djorie, Milad Dodangeh, Sushil Dohare, K. Dokova, Ojas Prakashbhai Doshi, Robert Kokou Dowou, H. Dsouza, S. Dunachie, Arkadiusz Marian Dziedzic, T. Eckmanns, Abdelaziz Ed-Dra, Aziz Eftekharimehrabad, T. Ekundayo, I. Sayed, Muhammed Elhadi, W. El‐Huneidi, Christelle Elias, Sally J Ellis, Randa Elsheikh, I. Elsohaby, Chadi Eltaha, B. Eshrati, M. Eslami, David W. Eyre, A. Fadaka, A. Fagbamigbe, A. Fahim, Aliasghar Fakhri-Demeshghieh, F. Fasina, M. Fasina, A. Fatehizadeh, N. Feasey, Alireza Feizkhah, G. Fekadu, Florian Fischer, Ida Fitriana, Karen M Forrest, C. Rodrigues, J. Fuller, M. Gadanya, Márió Gajdács, A. Gandhi, Esteban Garcia-Gallo, D. Garrett, R. Gautam, M. W. Gebregergis, Mesfin Gebrehiwot, T. G. Gebremeskel, Christine Geffers, Leonidas Georgalis, R. Ghazy, Mahaveer Golechha, Davide Golinelli, Melita A. Gordon, Snigdha Gulati, R. Gupta, Sapna Gupta, V. K. Gupta, A. D. Habteyohannes, Sebastian Haller, H. Harapan, Michelle L. Harrison, Ahmed I Hasaballah, Ikramul Hasan, R. Hasan, H. Hasani, A. Haselbeck, M. Hasnain, I. Hassan, Shoaib Hassan, Mahgol Sadat Hassan Zadeh Tabatabaei, Khezar Hayat, Jiawei He, Omar E. Hegazi, Mohammad Heidari, Kamal Hezam, Ramesh Holla, M. Holm, Heidi Hopkins, M. Hossain, M. Hosseinzadeh, S. Hostiuc, N. Hussein, Le Duc Huy, Elsa D. Ibáñez-Prada, A. Ikiroma, Irena Ilic, Sheikh Mohammed Shariful Islam, Faisal Ismail, N. Ismail, C. C. Iwu, C. Iwu-Jaja, A. Jafarzadeh, Fatoumatta Jaiteh, R. J. Yengejeh, R. Jamora, Javad Javidnia, Talha Jawaid, A. Jenney, H. Jeon, Mohammad Jokar, Dr. Nabi Jomehzadeh, Tamás Joó, Nitin Joseph, Zul Kamal, K. Kanmodi, Rami S. Kantar, J. Kapisi, I. Karaye, Yousef S. Khader, H. Khajuria, Nauman Khalid, F. Khamesipour, A. Khan, Mohammad Jobair Khan, Muhammad T. Khan, Vishnu Khanal, F. F. Khidri, J. Khubchandani, S. Khusuwan, M. Kim, A. Kisa, V. A. Korshunov, F. Krapp, R. Krumkamp, M. Kuddus, M. Kulimbet, Dewesh Kumar, E. Kumaran, Ambily Kuttikkattu, H. Kyu, I. Landires, B. Lawal, T. Le, I. Lederer, Munjae Lee, S. Lee, A. Lepape, T. L. Lerango, V. Ligade, C. Lim, Stephen S. Lim, Liknaw Workie Limenh, Chaojie Liu, Xiaofeng Liu, Xuefeng Liu, Michael J Loftus, H. I. M. Amin, Kelsey Lynn Maass, Sandeep B. Maharaj, M. Mahmoud, Panagiota Maikanti-Charalampous, O. Makram, Kashish Malhotra, A. Malik, Georgia D Mandilara, Florian Marks, B. Martínez-Guerra, Miquel Martorell, H. Masoumi-Asl, A. Mathioudakis, J. May, Theresa A. McHugh, J. Meiring, H. Meles, A. Melese, E. Melese, G. Minervini, N. Mohamed, S. Mohammed, Syam Mohan, A. Mokdad, L. Monasta, A. M. Ghalibaf, Catrin E Moore, Yousef Moradi, Elias Mossialos, Vincent Mougin, George Duke Mukoro, Francesk Mulita, B. Muller-Pebody, Efrén Murillo-Zamora, Sani Musa, P. Musicha, Lillian A Musila, S. Muthupandian, Ahamarshan Jayaraman Nagarajan, Pirouz Naghavi, F. Nainu, T. Nair, H. Najmuldeen, Z. Natto, J. Nauman, B. Nayak, G. T. Nchanji, P. Ndishimye, I. Negoi, R. Negoi, S. A. Nejadghaderi, QuynhAnh P Nguyen, E. Noman, Davis C. Nwakanma, Seamus O’Brien, Theresa J Ochoa, I. A. Odetokun, O. Ogundijo, Tolulope R. Ojo-Akosile, S. Okeke, Osaretin Christabel Okonji, A. Olagunju, A. Olivas-Martínez, A. Olorukooba, P. Olwoch, K. Onyedibe, Edgar Ortiz-Brizuela, O. Osuolale, P. Ounchanum, O. Oyeyemi, A. MaheshPadukudruP, J. Paredes, Romil R. Parikh, J. Patel, Shankargouda Patil, Shrikant Pawar, A. Peleg, Prince Peprah, João Perdigão, Carlo Perrone, I. Petcu, K. Phommasone, Z. Piracha, Dimitri Poddighe, A. Pollard, Ramesh Poluru, A. Ponce-de-León, J. Puvvula, F. Qamar, Nameer Hashim Qasim, Clotaire Donatien Rafai, P. Raghav, L. Rahbarnia, Fakher Rahim, V. Rahimi-Movaghar, Mosiur Rahman, Muhammad Aziz Rahman, H. Ramadan, S. Ramasamy, P. Ramesh, P. Ramteke, R. K. Rana, Usha Rani, M. Rashidi, D. Rathish, S. Rattanavong, S. Rawaf, E. Redwan, Luis Felipe Reyes, Tamalee Roberts, J. Robotham, V. D. Rosenthal, A. G. Ross, Nitai Roy, Kristina E. Rudd, C. Sabet, B. Saddik, M. Saeb, U. Saeed, S. Moghaddam, Weeravoot Saengchan, M. Safaei, A. Saghazadeh, N. Sharif-Askari, A. Sahebkar, S. S. Sahoo, Maitreyi Sahu, Morteza Saki, Nasir Salam, Z. Saleem, Mohamed Saleh, Y. Samodra, A. Samy, Aswini Saravanan, Maheswar Satpathy, Austin E. Schumacher, M. Sedighi, Samroeng Seekaew, Mahan Shafie, P. Shah, Samiah Shahid, M. Shahwan, S. Shakoor, Noga Shalev, M. A. Shamim, M. A. Shamshirgaran, Anas Shamsi, Amin Sharifan, R. P. Shastry, Mahabalesh Shetty, A. Shittu, Sunil Shrestha, E. Siddig, T. Sideroglou, J. Sifuentes-Osornio, Luís Manuel Lopes Rodrigues Silva, Eric A F Simões, Andrew J. H. Simpson, Amit Singh, Surjit Singh, R. Sinto, Sameh S. M. Soliman, Soroush Soraneh, N. Stoesser, Temenuga Stoeva, C. Swain, Lukasz Szarpak, Y. SreeSudhaT, S. Tabatabai, C. Tabche, Z. Taha, Ker-Kan Tan, Nidanuch Tasak, Nathan Y. Tat, Areerat Thaiprakong, P. Thangaraju, Caroline Tigoi, Krishna Tiwari, M. Tovani-Palone, Thang Tran, M. Tumurkhuu, Paul Turner, A. Udoakang, Arit Udoh, N. Ullah, Saeed Ullah, A. Vaithinathan, M. Valenti, T. Vos, Huong Thi Lan Vu, Yasir Waheed, A. S. Walker, J. Walson, T. Wangrangsimakul, K. Weerakoon, H. Wertheim, P. C. Williams, Asrat Wolde, and T. Wozniak. Global burden of bacterial antimicrobial resistance 1990–2021: a systematic analysis with forecasts to 2050. Lancet (London, England), 404:1199-1226, Sep 2024. URL: https://doi.org/10.1016/s0140-6736(24)01867-1, doi:10.1016/s0140-6736(24)01867-1. This article has 2640 citations.

14. (naghavi2024globalburdenof pages 2-3): M. Naghavi, S. Vollset, K. Ikuta, Lucien R. Swetschinski, Authia Gray, Eve E Wool, G. Aguilar, T. Meštrović, Georgia Smith, Chieh Han, Rebecca L Hsu, Julian Chalek, Daniel T Araki, Erin Chung, Cat Raggi, A. Hayoon, N. Weaver, Paulina A Lindstedt, Amanda E Smith, Umut Altay, N. V. Bhattacharjee, Konstantinos Giannakis, F. Fell, Barney McManigal, N. Ekapirat, J. Mendes, Tilleye Runghien, Oraya Srimokla, A. Abdelkader, S. Abd-Elsalam, R. Aboagye, Hassan Abolhassani, Hasan Abualruz, U. Abubakar, Hana J. Abukhadijah, Salahdein Aburuz, Ahmed Abu-Zaid, Sureerak Achalapong, Isaac Yeboah Addo, Victor Adekanmbi, T. AdeyeOluwa, Q. Adnani, Leticia Akua Adzigbli, M. Afzal, Saira Afzal, A. Agodi, Austin J Ahlstrom, Aqeel Ahmad, Sajjad Ahmad, Tauseef Ahmad, Alireza Ahmadi, Ayman Ahmed, H. Ahmed, Ibrar Ahmed, Mohammed Ahmed, Saeed Ahmed, Syed Anees Ahmed, Mohammed Ahmed Akkaif, S. Awaidy, Yazan Al Thaher, Samer O. Alalalmeh, M. Albataineh, W. Aldhaleei, A. Al-Gheethi, N. Alhaji, Abid Ali, Liaqat Ali, Syed Shujait Shujait Ali, Waad Ali, K. Allel, Sabah Al-Marwani, Ahmad Alrawashdeh, Awais Altaf, Ala’a B. Al-Tammemi, J. Al-Tawfiq, K. Alzoubi, W. Al-Zyoud, B. Amos, J. Amuasi, R. Ancuceanu, J. R. Andrews, Abhishek Anil, Iyadunni A. Anuoluwa, Saeid Anvari, A. Anyasodor, G. L. Apostol, J. Arabloo, M. Arafat, A. Aravkin, D. Areda, A. Aremu, A. Artamonov, Elizabeth A. Ashley, M. Asika, S. Athari, M. Atout, T. Awoke, S. Azadnajafabad, James M Azam, Shahkaar Aziz, A. Azzam, Mahsa Babaei, François-Xavier Babin, Muhammad Badar, A. Baig, Milica Bajcetic, Stephen Baker, Mainak Bardhan, H. Barqawi, Z. Basharat, A. Basiru, M. Bastard, S. Basu, N. Bayleyegn, M. A. Belete, O. Bello, Apostolos Beloukas, J. Berkley, A. Bhagavathula, Sonu M M Bhaskar, S. Bhuyan, J. Bielicki, N. I. Briko, C. Brown, A. Browne, Danilo Buonsenso, Yasser K. Bustanji, Cristina G Carvalheiro, C. Castañeda-Orjuela, Muthia Cenderadewi, J. Chadwick, S. Chakraborty, R. Chandika, Sara Chandy, Vilada Chansamouth, Vijay Kumar Chattu, A. Chaudhary, Patrick R. Ching, Hitesh Chopra, F. Chowdhury, D. Chu, M. Chutiyami, N. Cruz-Martins, A. Silva, O. Dadras, X. Dai, S. Darcho, Saswati Das, F. D. L. Hoz, D. Dekker, K. Dhama, D. Díaz, B. Dickson, S. Djorie, Milad Dodangeh, Sushil Dohare, K. Dokova, Ojas Prakashbhai Doshi, Robert Kokou Dowou, H. Dsouza, S. Dunachie, Arkadiusz Marian Dziedzic, T. Eckmanns, Abdelaziz Ed-Dra, Aziz Eftekharimehrabad, T. Ekundayo, I. Sayed, Muhammed Elhadi, W. El‐Huneidi, Christelle Elias, Sally J Ellis, Randa Elsheikh, I. Elsohaby, Chadi Eltaha, B. Eshrati, M. Eslami, David W. Eyre, A. Fadaka, A. Fagbamigbe, A. Fahim, Aliasghar Fakhri-Demeshghieh, F. Fasina, M. Fasina, A. Fatehizadeh, N. Feasey, Alireza Feizkhah, G. Fekadu, Florian Fischer, Ida Fitriana, Karen M Forrest, C. Rodrigues, J. Fuller, M. Gadanya, Márió Gajdács, A. Gandhi, Esteban Garcia-Gallo, D. Garrett, R. Gautam, M. W. Gebregergis, Mesfin Gebrehiwot, T. G. Gebremeskel, Christine Geffers, Leonidas Georgalis, R. Ghazy, Mahaveer Golechha, Davide Golinelli, Melita A. Gordon, Snigdha Gulati, R. Gupta, Sapna Gupta, V. K. Gupta, A. D. Habteyohannes, Sebastian Haller, H. Harapan, Michelle L. Harrison, Ahmed I Hasaballah, Ikramul Hasan, R. Hasan, H. Hasani, A. Haselbeck, M. Hasnain, I. Hassan, Shoaib Hassan, Mahgol Sadat Hassan Zadeh Tabatabaei, Khezar Hayat, Jiawei He, Omar E. Hegazi, Mohammad Heidari, Kamal Hezam, Ramesh Holla, M. Holm, Heidi Hopkins, M. Hossain, M. Hosseinzadeh, S. Hostiuc, N. Hussein, Le Duc Huy, Elsa D. Ibáñez-Prada, A. Ikiroma, Irena Ilic, Sheikh Mohammed Shariful Islam, Faisal Ismail, N. Ismail, C. C. Iwu, C. Iwu-Jaja, A. Jafarzadeh, Fatoumatta Jaiteh, R. J. Yengejeh, R. Jamora, Javad Javidnia, Talha Jawaid, A. Jenney, H. Jeon, Mohammad Jokar, Dr. Nabi Jomehzadeh, Tamás Joó, Nitin Joseph, Zul Kamal, K. Kanmodi, Rami S. Kantar, J. Kapisi, I. Karaye, Yousef S. Khader, H. Khajuria, Nauman Khalid, F. Khamesipour, A. Khan, Mohammad Jobair Khan, Muhammad T. Khan, Vishnu Khanal, F. F. Khidri, J. Khubchandani, S. Khusuwan, M. Kim, A. Kisa, V. A. Korshunov, F. Krapp, R. Krumkamp, M. Kuddus, M. Kulimbet, Dewesh Kumar, E. Kumaran, Ambily Kuttikkattu, H. Kyu, I. Landires, B. Lawal, T. Le, I. Lederer, Munjae Lee, S. Lee, A. Lepape, T. L. Lerango, V. Ligade, C. Lim, Stephen S. Lim, Liknaw Workie Limenh, Chaojie Liu, Xiaofeng Liu, Xuefeng Liu, Michael J Loftus, H. I. M. Amin, Kelsey Lynn Maass, Sandeep B. Maharaj, M. Mahmoud, Panagiota Maikanti-Charalampous, O. Makram, Kashish Malhotra, A. Malik, Georgia D Mandilara, Florian Marks, B. Martínez-Guerra, Miquel Martorell, H. Masoumi-Asl, A. Mathioudakis, J. May, Theresa A. McHugh, J. Meiring, H. Meles, A. Melese, E. Melese, G. Minervini, N. Mohamed, S. Mohammed, Syam Mohan, A. Mokdad, L. Monasta, A. M. Ghalibaf, Catrin E Moore, Yousef Moradi, Elias Mossialos, Vincent Mougin, George Duke Mukoro, Francesk Mulita, B. Muller-Pebody, Efrén Murillo-Zamora, Sani Musa, P. Musicha, Lillian A Musila, S. Muthupandian, Ahamarshan Jayaraman Nagarajan, Pirouz Naghavi, F. Nainu, T. Nair, H. Najmuldeen, Z. Natto, J. Nauman, B. Nayak, G. T. Nchanji, P. Ndishimye, I. Negoi, R. Negoi, S. A. Nejadghaderi, QuynhAnh P Nguyen, E. Noman, Davis C. Nwakanma, Seamus O’Brien, Theresa J Ochoa, I. A. Odetokun, O. Ogundijo, Tolulope R. Ojo-Akosile, S. Okeke, Osaretin Christabel Okonji, A. Olagunju, A. Olivas-Martínez, A. Olorukooba, P. Olwoch, K. Onyedibe, Edgar Ortiz-Brizuela, O. Osuolale, P. Ounchanum, O. Oyeyemi, A. MaheshPadukudruP, J. Paredes, Romil R. Parikh, J. Patel, Shankargouda Patil, Shrikant Pawar, A. Peleg, Prince Peprah, João Perdigão, Carlo Perrone, I. Petcu, K. Phommasone, Z. Piracha, Dimitri Poddighe, A. Pollard, Ramesh Poluru, A. Ponce-de-León, J. Puvvula, F. Qamar, Nameer Hashim Qasim, Clotaire Donatien Rafai, P. Raghav, L. Rahbarnia, Fakher Rahim, V. Rahimi-Movaghar, Mosiur Rahman, Muhammad Aziz Rahman, H. Ramadan, S. Ramasamy, P. Ramesh, P. Ramteke, R. K. Rana, Usha Rani, M. Rashidi, D. Rathish, S. Rattanavong, S. Rawaf, E. Redwan, Luis Felipe Reyes, Tamalee Roberts, J. Robotham, V. D. Rosenthal, A. G. Ross, Nitai Roy, Kristina E. Rudd, C. Sabet, B. Saddik, M. Saeb, U. Saeed, S. Moghaddam, Weeravoot Saengchan, M. Safaei, A. Saghazadeh, N. Sharif-Askari, A. Sahebkar, S. S. Sahoo, Maitreyi Sahu, Morteza Saki, Nasir Salam, Z. Saleem, Mohamed Saleh, Y. Samodra, A. Samy, Aswini Saravanan, Maheswar Satpathy, Austin E. Schumacher, M. Sedighi, Samroeng Seekaew, Mahan Shafie, P. Shah, Samiah Shahid, M. Shahwan, S. Shakoor, Noga Shalev, M. A. Shamim, M. A. Shamshirgaran, Anas Shamsi, Amin Sharifan, R. P. Shastry, Mahabalesh Shetty, A. Shittu, Sunil Shrestha, E. Siddig, T. Sideroglou, J. Sifuentes-Osornio, Luís Manuel Lopes Rodrigues Silva, Eric A F Simões, Andrew J. H. Simpson, Amit Singh, Surjit Singh, R. Sinto, Sameh S. M. Soliman, Soroush Soraneh, N. Stoesser, Temenuga Stoeva, C. Swain, Lukasz Szarpak, Y. SreeSudhaT, S. Tabatabai, C. Tabche, Z. Taha, Ker-Kan Tan, Nidanuch Tasak, Nathan Y. Tat, Areerat Thaiprakong, P. Thangaraju, Caroline Tigoi, Krishna Tiwari, M. Tovani-Palone, Thang Tran, M. Tumurkhuu, Paul Turner, A. Udoakang, Arit Udoh, N. Ullah, Saeed Ullah, A. Vaithinathan, M. Valenti, T. Vos, Huong Thi Lan Vu, Yasir Waheed, A. S. Walker, J. Walson, T. Wangrangsimakul, K. Weerakoon, H. Wertheim, P. C. Williams, Asrat Wolde, and T. Wozniak. Global burden of bacterial antimicrobial resistance 1990–2021: a systematic analysis with forecasts to 2050. Lancet (London, England), 404:1199-1226, Sep 2024. URL: https://doi.org/10.1016/s0140-6736(24)01867-1, doi:10.1016/s0140-6736(24)01867-1. This article has 2640 citations.

15. (naghavi2024globalburdenof pages 1-2): M. Naghavi, S. Vollset, K. Ikuta, Lucien R. Swetschinski, Authia Gray, Eve E Wool, G. Aguilar, T. Meštrović, Georgia Smith, Chieh Han, Rebecca L Hsu, Julian Chalek, Daniel T Araki, Erin Chung, Cat Raggi, A. Hayoon, N. Weaver, Paulina A Lindstedt, Amanda E Smith, Umut Altay, N. V. Bhattacharjee, Konstantinos Giannakis, F. Fell, Barney McManigal, N. Ekapirat, J. Mendes, Tilleye Runghien, Oraya Srimokla, A. Abdelkader, S. Abd-Elsalam, R. Aboagye, Hassan Abolhassani, Hasan Abualruz, U. Abubakar, Hana J. Abukhadijah, Salahdein Aburuz, Ahmed Abu-Zaid, Sureerak Achalapong, Isaac Yeboah Addo, Victor Adekanmbi, T. AdeyeOluwa, Q. Adnani, Leticia Akua Adzigbli, M. Afzal, Saira Afzal, A. Agodi, Austin J Ahlstrom, Aqeel Ahmad, Sajjad Ahmad, Tauseef Ahmad, Alireza Ahmadi, Ayman Ahmed, H. Ahmed, Ibrar Ahmed, Mohammed Ahmed, Saeed Ahmed, Syed Anees Ahmed, Mohammed Ahmed Akkaif, S. Awaidy, Yazan Al Thaher, Samer O. Alalalmeh, M. Albataineh, W. Aldhaleei, A. Al-Gheethi, N. Alhaji, Abid Ali, Liaqat Ali, Syed Shujait Shujait Ali, Waad Ali, K. Allel, Sabah Al-Marwani, Ahmad Alrawashdeh, Awais Altaf, Ala’a B. Al-Tammemi, J. Al-Tawfiq, K. Alzoubi, W. Al-Zyoud, B. Amos, J. Amuasi, R. Ancuceanu, J. R. Andrews, Abhishek Anil, Iyadunni A. Anuoluwa, Saeid Anvari, A. Anyasodor, G. L. Apostol, J. Arabloo, M. Arafat, A. Aravkin, D. Areda, A. Aremu, A. Artamonov, Elizabeth A. Ashley, M. Asika, S. Athari, M. Atout, T. Awoke, S. Azadnajafabad, James M Azam, Shahkaar Aziz, A. Azzam, Mahsa Babaei, François-Xavier Babin, Muhammad Badar, A. Baig, Milica Bajcetic, Stephen Baker, Mainak Bardhan, H. Barqawi, Z. Basharat, A. Basiru, M. Bastard, S. Basu, N. Bayleyegn, M. A. Belete, O. Bello, Apostolos Beloukas, J. Berkley, A. Bhagavathula, Sonu M M Bhaskar, S. Bhuyan, J. Bielicki, N. I. Briko, C. Brown, A. Browne, Danilo Buonsenso, Yasser K. Bustanji, Cristina G Carvalheiro, C. Castañeda-Orjuela, Muthia Cenderadewi, J. Chadwick, S. Chakraborty, R. Chandika, Sara Chandy, Vilada Chansamouth, Vijay Kumar Chattu, A. Chaudhary, Patrick R. Ching, Hitesh Chopra, F. Chowdhury, D. Chu, M. Chutiyami, N. Cruz-Martins, A. Silva, O. Dadras, X. Dai, S. Darcho, Saswati Das, F. D. L. Hoz, D. Dekker, K. Dhama, D. Díaz, B. Dickson, S. Djorie, Milad Dodangeh, Sushil Dohare, K. Dokova, Ojas Prakashbhai Doshi, Robert Kokou Dowou, H. Dsouza, S. Dunachie, Arkadiusz Marian Dziedzic, T. Eckmanns, Abdelaziz Ed-Dra, Aziz Eftekharimehrabad, T. Ekundayo, I. Sayed, Muhammed Elhadi, W. El‐Huneidi, Christelle Elias, Sally J Ellis, Randa Elsheikh, I. Elsohaby, Chadi Eltaha, B. Eshrati, M. Eslami, David W. Eyre, A. Fadaka, A. Fagbamigbe, A. Fahim, Aliasghar Fakhri-Demeshghieh, F. Fasina, M. Fasina, A. Fatehizadeh, N. Feasey, Alireza Feizkhah, G. Fekadu, Florian Fischer, Ida Fitriana, Karen M Forrest, C. Rodrigues, J. Fuller, M. Gadanya, Márió Gajdács, A. Gandhi, Esteban Garcia-Gallo, D. Garrett, R. Gautam, M. W. Gebregergis, Mesfin Gebrehiwot, T. G. Gebremeskel, Christine Geffers, Leonidas Georgalis, R. Ghazy, Mahaveer Golechha, Davide Golinelli, Melita A. Gordon, Snigdha Gulati, R. Gupta, Sapna Gupta, V. K. Gupta, A. D. Habteyohannes, Sebastian Haller, H. Harapan, Michelle L. Harrison, Ahmed I Hasaballah, Ikramul Hasan, R. Hasan, H. Hasani, A. Haselbeck, M. Hasnain, I. Hassan, Shoaib Hassan, Mahgol Sadat Hassan Zadeh Tabatabaei, Khezar Hayat, Jiawei He, Omar E. Hegazi, Mohammad Heidari, Kamal Hezam, Ramesh Holla, M. Holm, Heidi Hopkins, M. Hossain, M. Hosseinzadeh, S. Hostiuc, N. Hussein, Le Duc Huy, Elsa D. Ibáñez-Prada, A. Ikiroma, Irena Ilic, Sheikh Mohammed Shariful Islam, Faisal Ismail, N. Ismail, C. C. Iwu, C. Iwu-Jaja, A. Jafarzadeh, Fatoumatta Jaiteh, R. J. Yengejeh, R. Jamora, Javad Javidnia, Talha Jawaid, A. Jenney, H. Jeon, Mohammad Jokar, Dr. Nabi Jomehzadeh, Tamás Joó, Nitin Joseph, Zul Kamal, K. Kanmodi, Rami S. Kantar, J. Kapisi, I. Karaye, Yousef S. Khader, H. Khajuria, Nauman Khalid, F. Khamesipour, A. Khan, Mohammad Jobair Khan, Muhammad T. Khan, Vishnu Khanal, F. F. Khidri, J. Khubchandani, S. Khusuwan, M. Kim, A. Kisa, V. A. Korshunov, F. Krapp, R. Krumkamp, M. Kuddus, M. Kulimbet, Dewesh Kumar, E. Kumaran, Ambily Kuttikkattu, H. Kyu, I. Landires, B. Lawal, T. Le, I. Lederer, Munjae Lee, S. Lee, A. Lepape, T. L. Lerango, V. Ligade, C. Lim, Stephen S. Lim, Liknaw Workie Limenh, Chaojie Liu, Xiaofeng Liu, Xuefeng Liu, Michael J Loftus, H. I. M. Amin, Kelsey Lynn Maass, Sandeep B. Maharaj, M. Mahmoud, Panagiota Maikanti-Charalampous, O. Makram, Kashish Malhotra, A. Malik, Georgia D Mandilara, Florian Marks, B. Martínez-Guerra, Miquel Martorell, H. Masoumi-Asl, A. Mathioudakis, J. May, Theresa A. McHugh, J. Meiring, H. Meles, A. Melese, E. Melese, G. Minervini, N. Mohamed, S. Mohammed, Syam Mohan, A. Mokdad, L. Monasta, A. M. Ghalibaf, Catrin E Moore, Yousef Moradi, Elias Mossialos, Vincent Mougin, George Duke Mukoro, Francesk Mulita, B. Muller-Pebody, Efrén Murillo-Zamora, Sani Musa, P. Musicha, Lillian A Musila, S. Muthupandian, Ahamarshan Jayaraman Nagarajan, Pirouz Naghavi, F. Nainu, T. Nair, H. Najmuldeen, Z. Natto, J. Nauman, B. Nayak, G. T. Nchanji, P. Ndishimye, I. Negoi, R. Negoi, S. A. Nejadghaderi, QuynhAnh P Nguyen, E. Noman, Davis C. Nwakanma, Seamus O’Brien, Theresa J Ochoa, I. A. Odetokun, O. Ogundijo, Tolulope R. Ojo-Akosile, S. Okeke, Osaretin Christabel Okonji, A. Olagunju, A. Olivas-Martínez, A. Olorukooba, P. Olwoch, K. Onyedibe, Edgar Ortiz-Brizuela, O. Osuolale, P. Ounchanum, O. Oyeyemi, A. MaheshPadukudruP, J. Paredes, Romil R. Parikh, J. Patel, Shankargouda Patil, Shrikant Pawar, A. Peleg, Prince Peprah, João Perdigão, Carlo Perrone, I. Petcu, K. Phommasone, Z. Piracha, Dimitri Poddighe, A. Pollard, Ramesh Poluru, A. Ponce-de-León, J. Puvvula, F. Qamar, Nameer Hashim Qasim, Clotaire Donatien Rafai, P. Raghav, L. Rahbarnia, Fakher Rahim, V. Rahimi-Movaghar, Mosiur Rahman, Muhammad Aziz Rahman, H. Ramadan, S. Ramasamy, P. Ramesh, P. Ramteke, R. K. Rana, Usha Rani, M. Rashidi, D. Rathish, S. Rattanavong, S. Rawaf, E. Redwan, Luis Felipe Reyes, Tamalee Roberts, J. Robotham, V. D. Rosenthal, A. G. Ross, Nitai Roy, Kristina E. Rudd, C. Sabet, B. Saddik, M. Saeb, U. Saeed, S. Moghaddam, Weeravoot Saengchan, M. Safaei, A. Saghazadeh, N. Sharif-Askari, A. Sahebkar, S. S. Sahoo, Maitreyi Sahu, Morteza Saki, Nasir Salam, Z. Saleem, Mohamed Saleh, Y. Samodra, A. Samy, Aswini Saravanan, Maheswar Satpathy, Austin E. Schumacher, M. Sedighi, Samroeng Seekaew, Mahan Shafie, P. Shah, Samiah Shahid, M. Shahwan, S. Shakoor, Noga Shalev, M. A. Shamim, M. A. Shamshirgaran, Anas Shamsi, Amin Sharifan, R. P. Shastry, Mahabalesh Shetty, A. Shittu, Sunil Shrestha, E. Siddig, T. Sideroglou, J. Sifuentes-Osornio, Luís Manuel Lopes Rodrigues Silva, Eric A F Simões, Andrew J. H. Simpson, Amit Singh, Surjit Singh, R. Sinto, Sameh S. M. Soliman, Soroush Soraneh, N. Stoesser, Temenuga Stoeva, C. Swain, Lukasz Szarpak, Y. SreeSudhaT, S. Tabatabai, C. Tabche, Z. Taha, Ker-Kan Tan, Nidanuch Tasak, Nathan Y. Tat, Areerat Thaiprakong, P. Thangaraju, Caroline Tigoi, Krishna Tiwari, M. Tovani-Palone, Thang Tran, M. Tumurkhuu, Paul Turner, A. Udoakang, Arit Udoh, N. Ullah, Saeed Ullah, A. Vaithinathan, M. Valenti, T. Vos, Huong Thi Lan Vu, Yasir Waheed, A. S. Walker, J. Walson, T. Wangrangsimakul, K. Weerakoon, H. Wertheim, P. C. Williams, Asrat Wolde, and T. Wozniak. Global burden of bacterial antimicrobial resistance 1990–2021: a systematic analysis with forecasts to 2050. Lancet (London, England), 404:1199-1226, Sep 2024. URL: https://doi.org/10.1016/s0140-6736(24)01867-1, doi:10.1016/s0140-6736(24)01867-1. This article has 2640 citations.

16. (naghavi2024globalburdenof pages 3-4): M. Naghavi, S. Vollset, K. Ikuta, Lucien R. Swetschinski, Authia Gray, Eve E Wool, G. Aguilar, T. Meštrović, Georgia Smith, Chieh Han, Rebecca L Hsu, Julian Chalek, Daniel T Araki, Erin Chung, Cat Raggi, A. Hayoon, N. Weaver, Paulina A Lindstedt, Amanda E Smith, Umut Altay, N. V. Bhattacharjee, Konstantinos Giannakis, F. Fell, Barney McManigal, N. Ekapirat, J. Mendes, Tilleye Runghien, Oraya Srimokla, A. Abdelkader, S. Abd-Elsalam, R. Aboagye, Hassan Abolhassani, Hasan Abualruz, U. Abubakar, Hana J. Abukhadijah, Salahdein Aburuz, Ahmed Abu-Zaid, Sureerak Achalapong, Isaac Yeboah Addo, Victor Adekanmbi, T. AdeyeOluwa, Q. Adnani, Leticia Akua Adzigbli, M. Afzal, Saira Afzal, A. Agodi, Austin J Ahlstrom, Aqeel Ahmad, Sajjad Ahmad, Tauseef Ahmad, Alireza Ahmadi, Ayman Ahmed, H. Ahmed, Ibrar Ahmed, Mohammed Ahmed, Saeed Ahmed, Syed Anees Ahmed, Mohammed Ahmed Akkaif, S. Awaidy, Yazan Al Thaher, Samer O. Alalalmeh, M. Albataineh, W. Aldhaleei, A. Al-Gheethi, N. Alhaji, Abid Ali, Liaqat Ali, Syed Shujait Shujait Ali, Waad Ali, K. Allel, Sabah Al-Marwani, Ahmad Alrawashdeh, Awais Altaf, Ala’a B. Al-Tammemi, J. Al-Tawfiq, K. Alzoubi, W. Al-Zyoud, B. Amos, J. Amuasi, R. Ancuceanu, J. R. Andrews, Abhishek Anil, Iyadunni A. Anuoluwa, Saeid Anvari, A. Anyasodor, G. L. Apostol, J. Arabloo, M. Arafat, A. Aravkin, D. Areda, A. Aremu, A. Artamonov, Elizabeth A. Ashley, M. Asika, S. Athari, M. Atout, T. Awoke, S. Azadnajafabad, James M Azam, Shahkaar Aziz, A. Azzam, Mahsa Babaei, François-Xavier Babin, Muhammad Badar, A. Baig, Milica Bajcetic, Stephen Baker, Mainak Bardhan, H. Barqawi, Z. Basharat, A. Basiru, M. Bastard, S. Basu, N. Bayleyegn, M. A. Belete, O. Bello, Apostolos Beloukas, J. Berkley, A. Bhagavathula, Sonu M M Bhaskar, S. Bhuyan, J. Bielicki, N. I. Briko, C. Brown, A. Browne, Danilo Buonsenso, Yasser K. Bustanji, Cristina G Carvalheiro, C. Castañeda-Orjuela, Muthia Cenderadewi, J. Chadwick, S. Chakraborty, R. Chandika, Sara Chandy, Vilada Chansamouth, Vijay Kumar Chattu, A. Chaudhary, Patrick R. Ching, Hitesh Chopra, F. Chowdhury, D. Chu, M. Chutiyami, N. Cruz-Martins, A. Silva, O. Dadras, X. Dai, S. Darcho, Saswati Das, F. D. L. Hoz, D. Dekker, K. Dhama, D. Díaz, B. Dickson, S. Djorie, Milad Dodangeh, Sushil Dohare, K. Dokova, Ojas Prakashbhai Doshi, Robert Kokou Dowou, H. Dsouza, S. Dunachie, Arkadiusz Marian Dziedzic, T. Eckmanns, Abdelaziz Ed-Dra, Aziz Eftekharimehrabad, T. Ekundayo, I. Sayed, Muhammed Elhadi, W. El‐Huneidi, Christelle Elias, Sally J Ellis, Randa Elsheikh, I. Elsohaby, Chadi Eltaha, B. Eshrati, M. Eslami, David W. Eyre, A. Fadaka, A. Fagbamigbe, A. Fahim, Aliasghar Fakhri-Demeshghieh, F. Fasina, M. Fasina, A. Fatehizadeh, N. Feasey, Alireza Feizkhah, G. Fekadu, Florian Fischer, Ida Fitriana, Karen M Forrest, C. Rodrigues, J. Fuller, M. Gadanya, Márió Gajdács, A. Gandhi, Esteban Garcia-Gallo, D. Garrett, R. Gautam, M. W. Gebregergis, Mesfin Gebrehiwot, T. G. Gebremeskel, Christine Geffers, Leonidas Georgalis, R. Ghazy, Mahaveer Golechha, Davide Golinelli, Melita A. Gordon, Snigdha Gulati, R. Gupta, Sapna Gupta, V. K. Gupta, A. D. Habteyohannes, Sebastian Haller, H. Harapan, Michelle L. Harrison, Ahmed I Hasaballah, Ikramul Hasan, R. Hasan, H. Hasani, A. Haselbeck, M. Hasnain, I. Hassan, Shoaib Hassan, Mahgol Sadat Hassan Zadeh Tabatabaei, Khezar Hayat, Jiawei He, Omar E. Hegazi, Mohammad Heidari, Kamal Hezam, Ramesh Holla, M. Holm, Heidi Hopkins, M. Hossain, M. Hosseinzadeh, S. Hostiuc, N. Hussein, Le Duc Huy, Elsa D. Ibáñez-Prada, A. Ikiroma, Irena Ilic, Sheikh Mohammed Shariful Islam, Faisal Ismail, N. Ismail, C. C. Iwu, C. Iwu-Jaja, A. Jafarzadeh, Fatoumatta Jaiteh, R. J. Yengejeh, R. Jamora, Javad Javidnia, Talha Jawaid, A. Jenney, H. Jeon, Mohammad Jokar, Dr. Nabi Jomehzadeh, Tamás Joó, Nitin Joseph, Zul Kamal, K. Kanmodi, Rami S. Kantar, J. Kapisi, I. Karaye, Yousef S. Khader, H. Khajuria, Nauman Khalid, F. Khamesipour, A. Khan, Mohammad Jobair Khan, Muhammad T. Khan, Vishnu Khanal, F. F. Khidri, J. Khubchandani, S. Khusuwan, M. Kim, A. Kisa, V. A. Korshunov, F. Krapp, R. Krumkamp, M. Kuddus, M. Kulimbet, Dewesh Kumar, E. Kumaran, Ambily Kuttikkattu, H. Kyu, I. Landires, B. Lawal, T. Le, I. Lederer, Munjae Lee, S. Lee, A. Lepape, T. L. Lerango, V. Ligade, C. Lim, Stephen S. Lim, Liknaw Workie Limenh, Chaojie Liu, Xiaofeng Liu, Xuefeng Liu, Michael J Loftus, H. I. M. Amin, Kelsey Lynn Maass, Sandeep B. Maharaj, M. Mahmoud, Panagiota Maikanti-Charalampous, O. Makram, Kashish Malhotra, A. Malik, Georgia D Mandilara, Florian Marks, B. Martínez-Guerra, Miquel Martorell, H. Masoumi-Asl, A. Mathioudakis, J. May, Theresa A. McHugh, J. Meiring, H. Meles, A. Melese, E. Melese, G. Minervini, N. Mohamed, S. Mohammed, Syam Mohan, A. Mokdad, L. Monasta, A. M. Ghalibaf, Catrin E Moore, Yousef Moradi, Elias Mossialos, Vincent Mougin, George Duke Mukoro, Francesk Mulita, B. Muller-Pebody, Efrén Murillo-Zamora, Sani Musa, P. Musicha, Lillian A Musila, S. Muthupandian, Ahamarshan Jayaraman Nagarajan, Pirouz Naghavi, F. Nainu, T. Nair, H. Najmuldeen, Z. Natto, J. Nauman, B. Nayak, G. T. Nchanji, P. Ndishimye, I. Negoi, R. Negoi, S. A. Nejadghaderi, QuynhAnh P Nguyen, E. Noman, Davis C. Nwakanma, Seamus O’Brien, Theresa J Ochoa, I. A. Odetokun, O. Ogundijo, Tolulope R. Ojo-Akosile, S. Okeke, Osaretin Christabel Okonji, A. Olagunju, A. Olivas-Martínez, A. Olorukooba, P. Olwoch, K. Onyedibe, Edgar Ortiz-Brizuela, O. Osuolale, P. Ounchanum, O. Oyeyemi, A. MaheshPadukudruP, J. Paredes, Romil R. Parikh, J. Patel, Shankargouda Patil, Shrikant Pawar, A. Peleg, Prince Peprah, João Perdigão, Carlo Perrone, I. Petcu, K. Phommasone, Z. Piracha, Dimitri Poddighe, A. Pollard, Ramesh Poluru, A. Ponce-de-León, J. Puvvula, F. Qamar, Nameer Hashim Qasim, Clotaire Donatien Rafai, P. Raghav, L. Rahbarnia, Fakher Rahim, V. Rahimi-Movaghar, Mosiur Rahman, Muhammad Aziz Rahman, H. Ramadan, S. Ramasamy, P. Ramesh, P. Ramteke, R. K. Rana, Usha Rani, M. Rashidi, D. Rathish, S. Rattanavong, S. Rawaf, E. Redwan, Luis Felipe Reyes, Tamalee Roberts, J. Robotham, V. D. Rosenthal, A. G. Ross, Nitai Roy, Kristina E. Rudd, C. Sabet, B. Saddik, M. Saeb, U. Saeed, S. Moghaddam, Weeravoot Saengchan, M. Safaei, A. Saghazadeh, N. Sharif-Askari, A. Sahebkar, S. S. Sahoo, Maitreyi Sahu, Morteza Saki, Nasir Salam, Z. Saleem, Mohamed Saleh, Y. Samodra, A. Samy, Aswini Saravanan, Maheswar Satpathy, Austin E. Schumacher, M. Sedighi, Samroeng Seekaew, Mahan Shafie, P. Shah, Samiah Shahid, M. Shahwan, S. Shakoor, Noga Shalev, M. A. Shamim, M. A. Shamshirgaran, Anas Shamsi, Amin Sharifan, R. P. Shastry, Mahabalesh Shetty, A. Shittu, Sunil Shrestha, E. Siddig, T. Sideroglou, J. Sifuentes-Osornio, Luís Manuel Lopes Rodrigues Silva, Eric A F Simões, Andrew J. H. Simpson, Amit Singh, Surjit Singh, R. Sinto, Sameh S. M. Soliman, Soroush Soraneh, N. Stoesser, Temenuga Stoeva, C. Swain, Lukasz Szarpak, Y. SreeSudhaT, S. Tabatabai, C. Tabche, Z. Taha, Ker-Kan Tan, Nidanuch Tasak, Nathan Y. Tat, Areerat Thaiprakong, P. Thangaraju, Caroline Tigoi, Krishna Tiwari, M. Tovani-Palone, Thang Tran, M. Tumurkhuu, Paul Turner, A. Udoakang, Arit Udoh, N. Ullah, Saeed Ullah, A. Vaithinathan, M. Valenti, T. Vos, Huong Thi Lan Vu, Yasir Waheed, A. S. Walker, J. Walson, T. Wangrangsimakul, K. Weerakoon, H. Wertheim, P. C. Williams, Asrat Wolde, and T. Wozniak. Global burden of bacterial antimicrobial resistance 1990–2021: a systematic analysis with forecasts to 2050. Lancet (London, England), 404:1199-1226, Sep 2024. URL: https://doi.org/10.1016/s0140-6736(24)01867-1, doi:10.1016/s0140-6736(24)01867-1. This article has 2640 citations.