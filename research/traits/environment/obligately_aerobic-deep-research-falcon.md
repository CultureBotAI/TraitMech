---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:06:16.681656'
end_time: '2026-08-04T02:14:26.329279'
duration_seconds: 489.65
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: obligately aerobic
  trait_identifier: METPO:1000606
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: obligately_aerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference that requires molecular oxygen (O\u2082) for growth."
  parent_traits: METPO:1000601
  synonyms: obligate aerobe, obligate aerobic
  evidence_summary: 'https://www.ncbi.nlm.nih.gov/books/NBK482349/: require oxygen
    as a terminal electron acceptor (Supports the requirement for oxygen in obligately
    aerobic organisms.) | PMID:27203084: M. tuberculosis is an obligate aerobe (Organism
    example: Mycobacterium tuberculosis is described as obligately aerobic.)'
  causal_graph_summary: 'obligate_aerobe_oxygen_respiration: 12 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately aerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000606
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that requires molecular oxygen (O₂) for growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** obligate aerobe, obligate aerobic
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: require oxygen as a terminal electron acceptor (Supports the requirement for oxygen in obligately aerobic organisms.) | PMID:27203084: M. tuberculosis is an obligate aerobe (Organism example: Mycobacterium tuberculosis is described as obligately aerobic.)
- **Existing causal graph summary:** obligate_aerobe_oxygen_respiration: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **obligately aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_aerobic.yaml`.

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
- **Trait label:** obligately aerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000606
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that requires molecular oxygen (O₂) for growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** obligate aerobe, obligate aerobic
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: require oxygen as a terminal electron acceptor (Supports the requirement for oxygen in obligately aerobic organisms.) | PMID:27203084: M. tuberculosis is an obligate aerobe (Organism example: Mycobacterium tuberculosis is described as obligately aerobic.)
- **Existing causal graph summary:** obligate_aerobe_oxygen_respiration: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **obligately aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_aerobic.yaml`.

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


# Curation Research Report: Obligately Aerobic

**Trait:** obligately aerobic  
**Identifier:** `METPO:1000606`  
**Category / term kind / status:** ENVIRONMENT / CLASS / REVIEWED  
**Definition supplied:** “An oxygen preference that requires molecular oxygen (O₂) for growth.”  
**Parent:** `METPO:1000601`

## 1. Scope summary

`METPO:1000606` should denote an **assay-observed growth phenotype**: reproducible growth requires molecular oxygen. In the strongest mechanistic form, the organism uses O₂ as its sole terminal respiratory electron acceptor, so removal of O₂ prevents sustained energy conservation and cell multiplication. The 2024 *Bordetella* study provides an unusually direct modern example: *B. pertussis* and *B. bronchiseptica* are described as obligate aerobes that use “only oxygen as the terminal electron acceptor” for electron-transport-coupled oxidative phosphorylation. (mckay2024cytochromeoxidaserequirements pages 1-2)

This term should not imply that an organism requires atmospheric 21% O₂. *B. bronchiseptica* grew at both 5% and 2% O₂, although more slowly than in ambient air; thus an obligate aerobe can persist and grow under hypoxia if trace O₂ remains available. (s.2024adaptationofbordetella pages 122-126, mckay2024cytochromeoxidaserequirements pages 18-20)

### Boundary cases

- **Facultative anaerobe:** grows with or without O₂ by switching to anaerobic respiration or fermentation. This excludes it from `METPO:1000606`; the defining contrast is not oxygen tolerance but anaerobic growth capacity. (andre2021theselectiveadvantage pages 2-4)
- **Microaerophile:** requires or preferentially grows at O₂ below atmospheric concentration. A microaerophile may also be obligately oxygen-dependent, so “microaerophilic” and “obligately aerobic” can overlap along different axes: optimum concentration versus absolute requirement.
- **Aerotolerant anaerobe:** tolerates O₂ but does not use it as the required terminal acceptor and generally obtains energy fermentatively. Oxygen tolerance alone does not support this trait.
- **Obligate aerobe surviving anoxia without growth:** dormancy, persistence, or maintenance viability under anoxia does not disprove the trait. Curators should use demonstrated cell multiplication—not CFU persistence alone—as the endpoint.
- **Oxygen-dependent biosynthesis without obligate aerobiosis:** an O₂-requiring enzyme or biosynthetic reaction does not establish the whole-organism phenotype if an anaerobic bypass or nutrient salvage route exists.
- ***Pseudomonas aeruginosa*:** should not be used as a canonical obligate aerobe. It can support anaerobic growth by denitrification and, under some conditions, fermentation; older descriptions as “obligately aerobic” are therefore misleading.

## 2. Current mechanistic model

The most defensible trait-wide causal chain is:

**environmental O₂ availability → terminal oxygen reductase activity → four-electron reduction of O₂ to water → respiratory electron flow/electrochemical gradient → ATP synthase activity → ATP supply sufficient for growth → obligately aerobic growth phenotype.**

Bacterial terminal oxygen reductases include heme-copper oxidases, such as aa₃-type enzymes, alternative oxidases, and cytochrome-bd-family oxidases. They accept electrons through carriers such as quinol or cytochrome *c* and reduce dioxygen to water. (andre2021theselectiveadvantage pages 2-4)

This is a **minimal mechanistic backbone**, not a universal gene signature. Respiratory chains are branched and taxon-specific. In *B. bronchiseptica*, no individual oxidase was necessary in ambient air: strains retaining only Cyd1, Cta1, or Cyo1 had approximately wild-type growth, demonstrating functional redundancy. (mckay2024cytochromeoxidaserequirements pages 8-10) The three oxidases conserved in *B. pertussis*—`cydAB1`, `ctaCDFGE1`, and `cyoABCD1`—were sufficient for ambient-air and low-O₂ growth, while CyoABCD1 alone supported wild-type-level murine burden. (mckay2024cytochromeoxidaserequirements pages 18-20, mckay2024cytochromeoxidaserequirements pages 1-2)

## 3. Candidate nodes grouped by type

### Trait and environmental nodes

- obligately aerobic — `METPO:1000606`
- oxygen preference — parent `METPO:1000601`
- molecular oxygen — **CHEBI:15379**
- oxic environment — candidate ENVO term; verify the exact release-specific CURIE before insertion
- hypoxic/low-oxygen environment — label-only pending ENVO verification
- anoxic condition — label-only pending ENVO verification
- oxygen concentration / oxygen partial pressure
- ambient air, 21% O₂
- experimental low oxygen, 5% O₂ and 2% O₂

### Chemicals and energetic products

- water — **CHEBI:15377**
- proton — **CHEBI:15378**
- ATP — **CHEBI:15422**
- ADP — **CHEBI:16761**
- phosphate — **CHEBI:18367**
- ubiquinone/ubiquinol pool — ground to the exact quinone species only where experimentally known
- cytochrome *c*
- superoxide anion radical — **CHEBI:18421**
- hydrogen peroxide — **CHEBI:16240**
- reactive oxygen species — **CHEBI:26523**
- bedaquiline — use ChEBI/drug identifier only after release verification

### Processes and molecular functions

- aerobic respiration — **GO:0009060**
- respiratory electron transport chain — **GO:0022904**
- oxidative phosphorylation — **GO:0006119**
- proton motive force generation — label or a verified GO electrochemical-gradient term
- ATP synthesis coupled proton transport — **GO:0015986**
- oxygen reduction to water
- response to oxidative stress — **GO:0006979**
- cellular response to hypoxia — use only if the relevant microbial annotation is semantically appropriate
- growth / cell population growth — verify the desired GO/METPO representation

### Complexes, proteins, and enzymes

- terminal oxygen reductase / cytochrome oxidase
- heme-copper oxygen reductase
- aa₃-type cytochrome *c* oxidase
- bo₃-type quinol oxidase, CyoABCD
- cytochrome bd ubiquinol oxidase, CydAB
- cytochrome bcc-aa₃ respiratory supercomplex in mycobacteria
- F₁F₀ ATP synthase — **GO:0000276** is a suitable complex candidate
- superoxide dismutase — **EC 1.15.1.1**
- catalase — **EC 1.11.1.6**
- peroxidases — ground to the experimentally identified enzyme
- oxygen-dependent dihydroorotate dehydrogenase
- ribonucleotide reductase; distinguish oxygen-dependent and anaerobic classes
- acetate kinase — **EC 2.7.2.1**

### Taxon-specific gene candidates

- *Bordetella*: `cydAB1`, `ctaCDFGE1`, `cyoABCD1`; additional *B. bronchiseptica* oxidase loci should remain taxon-scoped.
- *Mycobacterium tuberculosis*: `cydAB`/cytochrome bd, cytochrome bcc-aa₃ system, and F₁F₀ ATP-synthase subunits.
- *Pseudomonas putida* KT2440 engineering: heterologous `ackA`, class-I dihydroorotate-dehydrogenase genes, and class-III ribonucleotide-reductase genes. The retrieved study reports that this combined design enabled microoxic growth, whereas acetate kinase alone did not improve anoxic survival over 18 days. (kampers2020microbiallifestyleengineering pages 103-107)

Taxon-specific proteins should be grounded to UniProt accessions only after strain and sequence are fixed; gene symbols alone are not globally unique.

## 4. Candidate causal edges

The following compact table distinguishes core edges from scoped examples and rejected claims.

| candidate subject | predicate | object | evidence strength | taxon scope | key reference DOI |
|---|---|---|---|---|---|
| molecular oxygen (O2) | is required for growth of | obligately aerobic phenotype | High | trait-wide definition | 10.1111/cmi.13338 (andre2021theselectiveadvantage pages 2-4) |
| obligately aerobic Bordetella spp. | uses terminal electron acceptor | molecular oxygen (O2) only | High | *Bordetella pertussis*, *B. bronchiseptica* | 10.1371/journal.ppat.1012084 (mckay2024cytochromeoxidaserequirements pages 1-2) |
| terminal oxygen reductases / cytochrome oxidases | reduces | O2 to H2O | High | broad aerobic bacteria | 10.1111/cmi.13338 (andre2021theselectiveadvantage pages 2-4) |
| aerobic respiratory chain | generates | proton motive force | Medium | broad aerobic bacteria | 10.1371/journal.ppat.1012084 (mckay2024cytochromeoxidaserequirements pages 8-10) |
| proton motive force | drives | ATP synthase-dependent ATP production | Medium | broad aerobic bacteria | 10.1371/journal.ppat.1012084 (mckay2024cytochromeoxidaserequirements pages 8-10) |
| cytochrome oxidase repertoire | enables growth in | ambient air and low-O2 conditions | High | *Bordetella* spp. | 10.1371/journal.ppat.1012084 (mckay2024cytochromeoxidaserequirements pages 1-2) |
| individual cytochrome oxidase (cyd1+/cta1+/cyo1+) | is sufficient for growth in | ambient air | High | *Bordetella bronchiseptica* | 10.1371/journal.ppat.1012084 (mckay2024cytochromeoxidaserequirements pages 8-10) |
| growth in 5% and 2% O2 | is compatible with | obligately aerobic growth, but slower than ambient air | Medium | *Bordetella bronchiseptica* | 10.1371/journal.ppat.1012084 (mckay2024cytochromeoxidaserequirements pages 18-20) |
| ROS detoxification enzymes (SOD/catalase/peroxidases) | mitigates | endogenous ROS from aerobic metabolism | Medium | broad aerobes; common but non-definitional | 10.1371/journal.pone.0309988 (harrison2024remissionspectroscopyresolves pages 27-29) |
| oxygen-dependent biosynthetic enzymes | permits biosynthesis in | O2-containing environments | Medium | broad prokaryotes; common but non-definitional | 10.1002/1873-3468.14906 (harrison2024remissionspectroscopyresolves pages 27-29) |
| strictly aerobic *Pseudomonas putida* | lacks anoxic growth because of | deficient ATP generation, redox imbalance, and essential-metabolite limitations | Medium | *P. putida* KT2440 | 10.1186/s12934-019-1227-5, 10.18174/516082 (kampers2020microbiallifestyleengineering pages 103-107) |
| acetate kinase + class I dihydroorotate dehydrogenase + class III ribonucleotide triphosphate reductase engineering | enables | micro-oxic growth | Medium | engineered *Pseudomonas putida* KT2440 | 10.1186/s12934-019-1227-5, 10.18174/516082 (kampers2020microbiallifestyleengineering pages 103-107) |
| bedaquiline | inhibits | mycobacterial F-ATP synthase | High | *Mycobacterium tuberculosis* complex / mycobacteria | 10.3390/antibiotics13121169, 10.1101/2024.12.03.626386 (harrison2024remissionspectroscopyresolves pages 27-29) |
| bedaquiline exposure | redirects electron flux to | cytochrome bd oxidase | Medium | mycobacteria | 10.1101/2024.12.03.626386 (harrison2024remissionspectroscopyresolves pages 27-29) |
| *Pseudomonas aeruginosa* | grows anaerobically via | denitrification and fermentative pathways | High | *P. aeruginosa* | 10.2217/fmb.10.16 |
| *Pseudomonas aeruginosa* | should be rejected as example of | obligately aerobic trait | High | counterexample / misclassification warning | 10.2217/fmb.10.16 |


*Table: This table summarizes compact candidate causal edges for the obligately aerobic TraitMech graph, separating core definitional mechanisms from taxon-specific observations, engineering cases, drug-response edges, and a rejected counterexample. It is useful for deciding which edges are safe to curate broadly versus only under explicit taxonomic scope.*

A more detailed curation assessment follows.

| Subject | Predicate | Object | Supporting snippet | Reference | Curation note |
|---|---|---|---|---|---|
| molecular oxygen | required_for | obligately aerobic growth | “Strict aerobes require oxygen to grow” | André et al., 2021, DOI [10.1111/cmi.13338](https://doi.org/10.1111/cmi.13338), Apr 2021 (andre2021theselectiveadvantage pages 2-4) | **Core/definitional.** Use the supplied METPO definition as primary ontology authority. |
| obligately aerobic *Bordetella* | uses_as_terminal_electron_acceptor | molecular oxygen | “use only oxygen as the terminal electron acceptor” | McKay et al., 2024, DOI [10.1371/journal.ppat.1012084](https://doi.org/10.1371/journal.ppat.1012084), Jul 2024 (mckay2024cytochromeoxidaserequirements pages 1-2) | **Strong but taxon-specific.** Supports the canonical mechanistic chain. |
| terminal oxygen reductase | reduces | O₂ to H₂O | Terminal reductases conduct a “four-electron reduction of dioxygen to water” | André et al., 2021 (andre2021theselectiveadvantage pages 2-4) | **Broad mechanism.** Do not assert that every obligate aerobe has every oxidase family. |
| respiratory electron transport | generates | electrochemical/proton-motive force | *Bordetella* oxidase-retaining strains maintained proton motive force | McKay et al., 2024 (mckay2024cytochromeoxidaserequirements pages 8-10) | **Mechanistically strong**, but the retrieved direct comparison is taxon-specific. |
| proton motive force | drives | ATP synthesis | Oxidase-retaining strains generated ATP at least comparable to wild type | McKay et al., 2024 (mckay2024cytochromeoxidaserequirements pages 8-10) | Curate through ATP synthase; avoid implying PMF is used only for ATP synthesis. |
| ATP supply | enables | growth | In *P. putida*, oxygen dependence was attributed partly to deficient ATP production without O₂ | Kampers et al., DOI [10.1186/s12934-019-1227-5](https://doi.org/10.1186/s12934-019-1227-5), Oct 2019; thesis evidence (kampers2020microbiallifestyleengineering pages 103-107) | **Taxon-specific support** for a general physiological link. |
| `cydAB1`, `ctaCDFGE1`, `cyoABCD1` oxidases | collectively enable | low-O₂ growth | The three *B. pertussis*-conserved oxidases were sufficient for ambient and low-O₂ growth | McKay et al., 2024 (mckay2024cytochromeoxidaserequirements pages 1-2) | **Taxon-specific.** Suitable under a *Bordetella* context node. |
| Cyd1 OR Cta1 OR Cyo1 | sufficient_for | ambient-air growth | Each single-oxidase strain showed growth comparable to wild type | McKay et al., 2024 (mckay2024cytochromeoxidaserequirements pages 8-10) | Encode alternatives, not a conjunction. This demonstrates redundancy. |
| residual O₂ at 2–5% | permits | slower growth | “Growth in 5% and 2% O₂ was possible but slower” | McKay et al., 2024 (mckay2024cytochromeoxidaserequirements pages 18-20) | Supports low-O₂ tolerance, not microaerophilic optimum. |
| CyoABCD1 | sufficient_for | wild-type-level murine respiratory burden | Cyo1-only bacteria maintained wild-type burdens through day 14 | McKay et al., 2024 (mckay2024cytochromeoxidaserequirements pages 18-20) | **Infection-model-specific**; do not generalize to trait definition. |
| aerobic metabolism | produces | superoxide and H₂O₂ | Aerobic organisms “continuously generate internal superoxide and hydrogen peroxide” | Sirithanakorn & Imlay, DOI [10.1371/journal.pone.0309988](https://doi.org/10.1371/journal.pone.0309988), Oct 2024 | **Common consequence, not defining cause.** Evidence was retrieved bibliographically rather than as a standalone context passage; retain source-level qualification. |
| SOD/catalase/peroxidases | detoxify | endogenous ROS | Cells maintain “high levels of superoxide dismutases, catalases, and peroxidases” | Sirithanakorn & Imlay, 2024 | Curate enzyme-specific reactions rather than one undifferentiated edge where possible. Absence of one enzyme does not exclude obligate aerobiosis. |
| oxygen-dependent enzymes | enable | oxygen-compatible essential biosynthesis | 365 O₂-dependent reactions mapped to 792 protein families; pathways include NAD⁺, pyridoxal, thiamine, ubiquinone, cobalamin, heme, and chlorophyll biosynthesis | Mrnjavac et al., DOI [10.1002/1873-3468.14906](https://doi.org/10.1002/1873-3468.14906), May 2024 | **Contextual, not trait-defining.** Add only a reaction demonstrated essential in the focal taxon. |
| heterologous acetate kinase + class-I DHODH + class-III RNR | enables | microoxic growth of *P. putida* KT2440 | The combined construct “successfully enabled growth under micro-oxic conditions” | Kampers evidence (kampers2020microbiallifestyleengineering pages 103-107) | **Engineered/taxon-specific.** Useful mechanistic decomposition of oxygen dependency. |
| acetate kinase alone | does_not_enable | prolonged anoxic survival | No significant improvement versus controls during an 18-day experiment | Kampers evidence (kampers2020microbiallifestyleengineering pages 103-107) | Negative edge; valuable warning against a single-cause ATP model. |
| bedaquiline | inhibits | mycobacterial F₁F₀ ATP synthase | 2024 work describes bedaquiline as an ATP-synthase inhibitor | Harrison et al., DOI [10.1101/2024.12.03.626386](https://doi.org/10.1101/2024.12.03.626386), Dec 2024 (preprint) (harrison2024remissionspectroscopyresolves pages 27-29) | **Drug/taxon-specific.** Not part of the generic trait graph unless inhibitors are in scope. |
| bedaquiline | redirects_electron_flux_to | cytochrome bd oxidase | Sub-second electron-flux redirection to Cyd was reported | Harrison et al., 2024 (harrison2024remissionspectroscopyresolves pages 27-29) | **Uncertain pending peer review** in the retrieved version. |

## 5. Recent developments and quantitative findings

### Respiratory-pathogen physiology

The strongest 2024 primary study found marked oxidase redundancy in obligately aerobic *Bordetella*. *B. bronchiseptica* has eight cytochrome-oxidase loci, whereas host-restricted *B. pertussis* retains three functional loci. No individual oxidase was essential in ambient air, and the retained three were sufficient in low O₂. CyoABCD1 alone supported wild-type-level infection burden through 14 days in mice. (mckay2024cytochromeoxidaserequirements pages 8-10, mckay2024cytochromeoxidaserequirements pages 18-20, mckay2024cytochromeoxidaserequirements pages 1-2)

Expert interpretation: obligate aerobiosis is best curated at the **functional-module level**—oxygen-terminating respiration—rather than as dependence on a single conserved oxidase. Oxidase identity and affinity determine niche performance, but redundancy prevents a universal gene-level definition.

### Oxygen-dependent enzyme evolution

A 2024 evolutionary analysis mapped **365 O₂-dependent prokaryotic reactions to 792 protein families**. Its central conclusion was that oxygen’s impact extends beyond energy conservation: O₂-dependent alternatives entered essential cofactor-biosynthetic pathways, including those for NAD⁺, pyridoxal, thiamine, ubiquinone, cobalamin, heme, and chlorophyll. DOI: [10.1002/1873-3468.14906](https://doi.org/10.1002/1873-3468.14906), published May 2024.

For TraitMech, this argues against reducing obligate aerobiosis to “oxygen is the terminal acceptor.” In some taxa, anaerobic failure can also result from one or more indispensable oxygen-dependent biosynthetic steps. Nevertheless, those steps require taxon-specific knockout, rescue, or metabolic evidence before curation.

### ROS physiology

Recent work confirms that aerobic cells continuously form superoxide and hydrogen peroxide and depend on basal scavenging by SODs, catalases, and peroxidases. In *E. coli*, fatty-acid catabolism increased intracellular peroxide formation in a FadE-dependent manner, illustrating that ROS burden depends on active metabolic flux rather than oxygen exposure alone. DOI: [10.1371/journal.pone.0309988](https://doi.org/10.1371/journal.pone.0309988), published October 2024.

ROS defenses should therefore be represented as **enabling/tolerance modules**, not necessary-and-sufficient determinants of the obligately aerobic phenotype. Aerotolerant anaerobes also possess ROS defenses, while some aerobes lack canonical forms and use alternatives.

### Respiratory-chain inhibitors

Mycobacterial oxidative phosphorylation remains a major antimicrobial target. The 2024 spectroscopy preprint reported rapid redirection of electron flux toward cytochrome bd after bedaquiline inhibition of ATP synthase, providing a mechanistic explanation for respiratory compensation and combination-drug strategies. (harrison2024remissionspectroscopyresolves pages 27-29) Because the retrieved Harrison source was a December 2024 bioRxiv preprint, this particular flux-redirection edge should be marked provisional.

## 6. Applications and real-world implementation

1. **Clinical antimicrobial development.** ATP synthase and terminal oxidases are actionable vulnerabilities in oxygen-dependent pathogens. Bedaquiline validates oxidative phosphorylation as an anti-tuberculosis target, while oxidase redundancy suggests that dual-terminal-oxidase inhibition may be more robust than targeting one branch. (harrison2024remissionspectroscopyresolves pages 27-29)
2. **Respiratory infection models.** The *Bordetella* findings show that low-affinity bo₃-type oxidase can be sufficient in the murine respiratory tract. Oxygen concentration, CO₂, anatomical site, and infection duration should therefore be encoded as experimental context rather than inferred from atmospheric-growth assays. (mckay2024cytochromeoxidaserequirements pages 18-20)
3. **Industrial biotechnology.** Oxygen transfer is a scale-up constraint for strictly aerobic chassis such as *P. putida*. Engineering ATP generation and oxygen-independent biosynthesis can extend growth into microoxic reactor regions, but the failure of acetate kinase alone shows that energy, redox balance, and essential-metabolite synthesis must be addressed together. (kampers2020microbiallifestyleengineering pages 103-107)
4. **Phenotyping and cultivation.** Suitable evidence includes matched oxic/anoxic growth curves, colony formation, biomass or cell-number increase, controlled dissolved-O₂ measurements, and oxygen-gradient cultures. Resazurin can report redox/oxygen consumption but is not, by itself, proof of growth or of obligate aerobiosis.
5. **Ecology and bioprocess control.** Obligate aerobes can consume oxygen and create hypoxic or anoxic microniches for other community members. Consequently, bulk dissolved O₂ may not represent the local exposure experienced in biofilms or particles.

## 7. Recommended graph architecture

### Safe core for `obligately_aerobic.yaml`

1. `molecular oxygen` **enables** `terminal oxygen reductase activity`
2. `terminal oxygen reductase activity` **reduces** `molecular oxygen` **to** `water`
3. `terminal oxygen reductase activity` **supports** `respiratory electron transport`
4. `respiratory electron transport` **generates** `proton motive force`
5. `proton motive force` **drives** `F1Fo ATP synthase`
6. `F1Fo ATP synthase` **produces** `ATP`
7. `ATP availability` **enables** `cell growth`
8. `absence of molecular oxygen` **prevents** `oxygen-terminating respiration`
9. `failure of energy conservation under anoxia` **prevents** `growth`
10. `growth only in oxygen-containing conditions` **manifests_as** `METPO:1000606`

Edges 8–9 need wording that allows dormancy and avoids claiming immediate cell death.

### Optional modules

- **ROS module:** aerobic metabolism → ROS; SOD/catalase/peroxidases → ROS detoxification → maintenance of macromolecular function.
- **O₂-dependent biosynthesis module:** include only for a specified organism and experimentally essential reaction.
- **Low-O₂ oxidase switching:** high-affinity bd/cbb₃-family systems may support hypoxic respiration, but exact oxidase usage is taxon-specific.
- **Inhibitor module:** bedaquiline → ATP-synthase inhibition → energetic stress; alternative oxidase flux as a scoped compensatory response.

## 8. Claims not yet suitable for TraitMech curation

- **Do not assert that catalase or SOD is universally required for obligate aerobiosis.** These are common defenses, not defining markers.
- **Do not use presence of cytochrome oxidase genes alone as phenotype proof.** Facultative organisms also possess them, and genomic presence does not establish expression or essentiality.
- **Do not make `cytochrome bd → obligately aerobic` a universal edge.** Cytochrome bd occurs in facultative organisms and can serve stress, virulence, or low-O₂ functions.
- **Do not classify growth at 2–5% O₂ as microaerophily without an optimum-growth comparison.** It demonstrates hypoxic growth capacity only. (mckay2024cytochromeoxidaserequirements pages 18-20)
- **Do not equate anoxic survival with anoxic growth.** Persistence and dormancy are compatible with obligate aerobiosis.
- **Do not curate *P. aeruginosa* as an obligate-aerobe example.** Its denitrifying and fermentative capacities make it a counterexample to historical shorthand.
- **Do not generalize the *Bordetella* oxidase repertoire.** Eight versus three loci and Cyo1 sufficiency are lineage- and assay-specific. (mckay2024cytochromeoxidaserequirements pages 8-10, mckay2024cytochromeoxidaserequirements pages 1-2)
- **Do not treat bedaquiline-induced flux redirection as trait-defining.** It is a drug response, and the retrieved 2024 study was a preprint. (harrison2024remissionspectroscopyresolves pages 27-29)
- **Do not insert unverified UniProt, Rhea, KEGG, MetaCyc, or ENVO identifiers.** Exact strain, reaction direction, cofactor, and ontology release must first be checked.
- **Do not interpret resazurin reduction as synonymous with growth.** It is an indirect redox/metabolic readout affected by oxygen concentration and assay chemistry.

## 9. DOI-first bibliography

1. **McKay LS et al.** “Cytochrome oxidase requirements in *Bordetella* reveal insights into evolution towards life in the mammalian respiratory tract.” *PLOS Pathogens* 20:e1012084. **Published July 2024.** DOI: [10.1371/journal.ppat.1012084](https://doi.org/10.1371/journal.ppat.1012084). (mckay2024cytochromeoxidaserequirements pages 8-10, mckay2024cytochromeoxidaserequirements pages 18-20, mckay2024cytochromeoxidaserequirements pages 1-2)
2. **Mrnjavac N et al.** “The radical impact of oxygen on prokaryotic evolution—enzyme inhibition first, uninhibited essential biosyntheses second, aerobic respiration third.” *FEBS Letters* 598:1692–1714. **Published May 2024.** DOI: [10.1002/1873-3468.14906](https://doi.org/10.1002/1873-3468.14906).
3. **Sirithanakorn C, Imlay JA.** “Evidence for endogenous hydrogen peroxide production by *E. coli* fatty acyl-CoA dehydrogenase.” *PLOS ONE* 19:e0309988. **Published October 2024.** DOI: [10.1371/journal.pone.0309988](https://doi.org/10.1371/journal.pone.0309988).
4. **Harrison SH et al.** “Remission spectroscopy resolves the mode of action of bedaquiline within living mycobacteria.” *bioRxiv*. **Posted December 2024.** DOI: [10.1101/2024.12.03.626386](https://doi.org/10.1101/2024.12.03.626386). Preprint. (harrison2024remissionspectroscopyresolves pages 27-29)
5. **Harikishore A, Grüber G.** “*Mycobacterium tuberculosis* F-ATP Synthase Inhibitors and Targets.” *Antibiotics* 13:1169. **Published December 2024.** DOI: [10.3390/antibiotics13121169](https://doi.org/10.3390/antibiotics13121169).
6. **Maslovska O et al.** “Oxidative stress and protection against it in bacteria.” *Studia Biologica* 17:153–172. **Published June 2023.** DOI: [10.30970/sbi.1702.716](https://doi.org/10.30970/sbi.1702.716).
7. **André AC et al.** “The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection.” *Cellular Microbiology* 23. **Published April 2021.** DOI: [10.1111/cmi.13338](https://doi.org/10.1111/cmi.13338). (andre2021theselectiveadvantage pages 2-4)
8. **Kampers LFC et al.** “In silico-guided engineering of *Pseudomonas putida* towards growth under micro-oxic conditions.” *Microbial Cell Factories* 18. **Published October 2019.** DOI: [10.1186/s12934-019-1227-5](https://doi.org/10.1186/s12934-019-1227-5). Related retrieved thesis evidence: [10.18174/516082](https://doi.org/10.18174/516082). (kampers2020microbiallifestyleengineering pages 103-107)
9. **Schobert M, Tielen P.** “Contribution of oxygen-limiting conditions to persistent infection of *Pseudomonas aeruginosa*.” *Future Microbiology* 5:603–621. **Published March 2010.** DOI: [10.2217/fmb.10.16](https://doi.org/10.2217/fmb.10.16).

## Curation conclusion

The existing 12-node/10-edge graph has the correct likely backbone if it connects O₂ to terminal reduction, respiratory energy conservation, ATP production, and growth. The principal revision should be to separate: **(i)** universally defensible phenotype-level edges, **(ii)** common but non-definitional ROS and biosynthesis modules, and **(iii)** explicitly taxon-scoped oxidase, engineering, infection, and inhibitor edges. The 2024 *Bordetella* evidence particularly supports representing **functional redundancy and low-O₂ growth without anaerobic growth**, rather than encoding a single terminal oxidase as the cause of `METPO:1000606`. (mckay2024cytochromeoxidaserequirements pages 8-10, mckay2024cytochromeoxidaserequirements pages 18-20, mckay2024cytochromeoxidaserequirements pages 1-2)

References

1. (mckay2024cytochromeoxidaserequirements pages 1-2): Liliana S. McKay, Alexa R. Spandrio, Richard M. Johnson, M. Ashley Sobran, Sara A. Marlatt, Katlyn B. Mote, Margaret R. Dedloff, Zachary M. Nash, Steven M. Julio, and Peggy A. Cotter. Cytochrome oxidase requirements in bordetella reveal insights into evolution towards life in the mammalian respiratory tract. PLOS Pathogens, 20:e1012084, Jul 2024. URL: https://doi.org/10.1371/journal.ppat.1012084, doi:10.1371/journal.ppat.1012084. This article has 10 citations and is from a highest quality peer-reviewed journal.

2. (s.2024adaptationofbordetella pages 122-126): ADAPTATION OF BORDETELLA BRONCHISEPTICA TO SURVIVAL WITHIN THE MAMMALIAN RESPIRATORY TRACT This article has 0 citations and is from a peer-reviewed journal.

3. (mckay2024cytochromeoxidaserequirements pages 18-20): Liliana S. McKay, Alexa R. Spandrio, Richard M. Johnson, M. Ashley Sobran, Sara A. Marlatt, Katlyn B. Mote, Margaret R. Dedloff, Zachary M. Nash, Steven M. Julio, and Peggy A. Cotter. Cytochrome oxidase requirements in bordetella reveal insights into evolution towards life in the mammalian respiratory tract. PLOS Pathogens, 20:e1012084, Jul 2024. URL: https://doi.org/10.1371/journal.ppat.1012084, doi:10.1371/journal.ppat.1012084. This article has 10 citations and is from a highest quality peer-reviewed journal.

4. (andre2021theselectiveadvantage pages 2-4): Antonin C. André, Lorine Debande, and Benoit S. Marteyn. The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection. Cellular Microbiology, Apr 2021. URL: https://doi.org/10.1111/cmi.13338, doi:10.1111/cmi.13338. This article has 110 citations and is from a peer-reviewed journal.

5. (mckay2024cytochromeoxidaserequirements pages 8-10): Liliana S. McKay, Alexa R. Spandrio, Richard M. Johnson, M. Ashley Sobran, Sara A. Marlatt, Katlyn B. Mote, Margaret R. Dedloff, Zachary M. Nash, Steven M. Julio, and Peggy A. Cotter. Cytochrome oxidase requirements in bordetella reveal insights into evolution towards life in the mammalian respiratory tract. PLOS Pathogens, 20:e1012084, Jul 2024. URL: https://doi.org/10.1371/journal.ppat.1012084, doi:10.1371/journal.ppat.1012084. This article has 10 citations and is from a highest quality peer-reviewed journal.

6. (kampers2020microbiallifestyleengineering pages 103-107): Linde F.C. Kampers. Microbial lifestyle engineering. ArXiv, 2020. URL: https://doi.org/10.18174/516082, doi:10.18174/516082. This article has 0 citations.

7. (harrison2024remissionspectroscopyresolves pages 27-29): Suzanna H. Harrison, Rowan C Walters, Chen-Yi Cheung, Roger J Springett, Gregory M. Cook, Morwan M. Osman, and J. N. Blaza. Remission spectroscopy resolves the mode of action of bedaquiline within living mycobacteria. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.03.626386, doi:10.1101/2024.12.03.626386. This article has 1 citations.