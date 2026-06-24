---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:30:57.175207'
end_time: '2026-06-17T20:48:45.039455'
duration_seconds: 1067.86
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
  causal_graph_summary: 'opportunistic_pathogen_context_dependent_virulence: 3 nodes,
    2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
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
- **Existing causal graph summary:** opportunistic_pathogen_context_dependent_virulence: 3 nodes, 2 edges

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
- **Existing causal graph summary:** opportunistic_pathogen_context_dependent_virulence: 3 nodes, 2 edges

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


## Microbial Trait Causal Graph Curation Report: Opportunistic pathogen (METPO traitmech:000046)

### Executive scope summary (TraitMech definition alignment)
The TraitMech trait **opportunistic pathogen** (traitmech:000046) is best curated as a *context-dependent host-association lifestyle* in which a microorganism that is commonly commensal or environmental causes disease primarily when **host defenses are compromised** and/or when it reaches a **normally sterile site**. This context dependence is explicitly reflected in clinical and ecological reviews describing opportunism as emerging under immunocompromise, barrier failure, dysbiosis, and resource changes that enable virulence programs. Evidence also supports key boundary conditions: (i) colonization is common but does not equal infection, and (ii) strains that behave commensally can retain pathogenic potential. (uberoi2024thewoundmicrobiota pages 1-2, jacobsen2023theroleof pages 1-2, froismartins2024candidaalbicansvirulence pages 1-2, sangiorgio2024theimpactof pages 9-10)

**Boundary cases to distinguish from nearby traits**
- **Commensal/colonizer ≠ opportunistic pathogen**: wounds are frequently colonized, but only a subset progress to infection, indicating that opportunism requires additional host and microbial conditions beyond mere presence. (uberoi2024thewoundmicrobiota pages 1-2)
- **Pathobiont framing (commensal with retained virulence capacity)**: *Candida albicans* commensal isolates from healthy individuals can still “retain the capacity to cause disease,” highlighting that opportunism is not simply loss/gain of virulence genes but regulated expression in context. (froismartins2024candidaalbicansvirulence pages 1-2)
- **Host susceptibility can dominate over microbial load**: opportunistic *Xanthomonas* disease in immunocompromised **rbohD** plants occurred without higher colonization, implying host defense status rather than pathogen abundance alone. (sebastian2024leafmicrobiomedysbiosis pages 3-4)

### Current understanding: key concepts and definitions

#### Core host-context drivers (generalizable across taxa)
1. **Immune compromise**: Opportunism is defined by disease emergence when “host defenses are compromised.” Reviews of *Enterococcus* in immunocompromised hosts explicitly frame commensals as opportunists in this context. (sangiorgio2024theimpactof pages 9-10, sangiorgio2024theimpactof pages 1-2)
2. **Barrier breach / access to sterile tissue**: In wounds, breach of the skin barrier “exposes sterile tissue to microbes,” creating a permissive niche for opportunistic infection and polymicrobial biofilms. (uberoi2024thewoundmicrobiota pages 1-2)
3. **Microbiome dysbiosis and antibiotic exposure**: Antibiotic treatment is described as a common risk factor enabling expansion of opportunists (e.g., candidiasis). Dysbiosis-oriented infection-control framing also links antimicrobial pressure to opportunist enrichment. (jacobsen2023theroleof pages 1-2, alsoubhi2024theecologyof pages 4-6)
4. **Nutritional immunity and resource limitation**: During infection, vertebrate hosts impose “nutritional immunity” through metal sequestration, creating iron limitation that triggers opportunist iron-acquisition programs (exemplified by *Pseudomonas aeruginosa*). (sanchez‐jimenez2023mechanismsofiron pages 1-2)

#### Core microbial mechanisms (curatable mechanistic node families)
- **Adhesion and invasion**: For *C. albicans*, “Adhesion, invasion, and tissue damage are critical steps” in transition from commensalism to disease, supported by adhesin-associated invasion pathways. (jacobsen2023theroleof pages 1-2)
- **Morphological switching and toxin-mediated damage**: *C. albicans* hyphae formation and candidalysin are highlighted as key virulence traits enabling invasion and damage, while their expression can also play roles in colonization that are restrained by host immunity. (froismartins2024candidaalbicansvirulence pages 1-2)
- **Biofilm formation**: Biofilms on host tissues or devices enable persistence, immune evasion, and antimicrobial tolerance; this is emphasized in opportunistic *Enterococcus* infections and wound microbiota reviews. (sangiorgio2024theimpactof pages 9-10, uberoi2024thewoundmicrobiota pages 1-2)
- **Secretion systems and tissue-degrading enzymes**: In a high-resolution plant model of opportunism, *Xanthomonas* **T2SS (Xps)** exported cell wall–degrading enzymes that caused tissue degradation and drove microbiome dysbiosis in immunocompromised hosts. (sebastian2024leafmicrobiomedysbiosis pages 3-4, sebastian2024leafmicrobiomedysbiosis pages 11-12, sebastian2024leafmicrobiomedysbiosis pages 2-3)
- **Iron acquisition and quorum sensing**: Under iron limitation, *P. aeruginosa* promotes high-affinity iron transport and siderophore production; the quorum-sensing signal **PQS** promotes transcription of virulence genes and also chelates iron, linking iron homeostasis to virulence regulation. (sanchez‐jimenez2023mechanismsofiron pages 1-2, sanchez‐jimenez2023mechanismsofiron pages 2-4, sanchez‐jimenez2023mechanismsofiron pages 5-7)

### Recent developments (prioritizing 2023–2024)

#### 2024: Primary causal demonstration of opportunism-driven dysbiosis (plant model)
Pfeilmeier et al. (Nature Microbiology, Jan 2024) provide unusually direct experimental causality for opportunism in an immunocompromised host context: loss of host NADPH oxidase **RBOHD** (immune component) enabled opportunistic *Xanthomonas* to cause disease and reshape the leaf community. The effect of adding *Xanthomonas* Leaf131 to a 137-member synthetic community substantially increased the host-genotype effect size (12.5%, P=0.0001), whereas removing Leaf131 largely eliminated dysbiosis (effect size 2.8%, P=0.71). (sebastian2024leafmicrobiomedysbiosis pages 2-3)

Mechanistically, the authors demonstrate secretion-mediated tissue degradation consistent with an edge chain: **T2SS-dependent enzyme secretion → tissue degradation → dysbiosis**, including evidence that “cell wall–degrading enzymes [are] secreted via T2SS Xps” and that “cell-free supernatants reproduce leaf degradation.” (sebastian2024leafmicrobiomedysbiosis pages 3-4, sebastian2024leafmicrobiomedysbiosis pages 11-12)

#### 2024: Updated immune-control view of commensal fungi as opportunistic pathogens
Jensen et al. (Infection and Immunity, Sep 2024) synthesize gut immune mechanisms that keep commensal fungi from becoming pathogenic, emphasizing that mucus, antimicrobial peptides, and IgA “regulate fungal colonization and inhibit pathogenic potential,” and that defects in epithelial biology and immunity can “permit expansion or epithelial colonization by normally excluded fungi.” This supports a curatable host-defense module (barrier + secreted effectors + immune control) that causally suppresses opportunistic disease. (jensen2024controllingcandida pages 1-2)

#### 2024: Candida virulence traits in commensalism and disease (paradigm shift)
Fróis‑Martins et al. (Current Clinical Microbiology Reports, Oct 2024) summarize evidence that traits classically labeled “virulence” (hyphae formation, candidalysin) can contribute to gut commensal colonization while adaptive immunity prevents excessive tissue damage, explicitly stating “Overt filamentation and tissue damage is in turn prevented by adaptive antifungal immunity.” This supports graph modeling where virulence traits are *not solely downstream of disease*, but are nodes that can support both commensal fitness and pathogenicity depending on regulation and host state. (froismartins2024candidaalbicansvirulence pages 1-2)

#### 2024: Opportunistic infection as a continuum in wounds
Uberoi et al. (Nature Reviews Microbiology, Apr 2024) emphasize that “Nearly all wounds are colonized but only some progress to infection,” supporting a boundary distinction between contamination/colonization and opportunistic infection, and highlighting context dependence (host susceptibility, microbial traits, priority effects, polymicrobial interactions). The review also reports a large health-system burden: **US wound care spending up to $96.8B annually** and **wound prevalence ~2% in the USA**. (uberoi2024thewoundmicrobiota pages 1-2)

#### 2023: Iron homeostasis and “nutritional immunity” as a mechanistic axis of opportunism
Sánchez‑Jiménez et al. (Microbial Biotechnology, Mar 2023) provide mechanistic edges linking host-imposed iron limitation to siderophore programs and QS-linked virulence. The review states that during infection, vertebrates induce “nutritional immunity” with metal sequestration, and that “Under iron limitation, the production of high-affinity iron transport systems is promoted.” It also states that siderophores “scavenge iron and form soluble Fe3+-complexes,” and notes PQS “promot[es] transcription … of several P. aeruginosa virulence genes.” (sanchez‐jimenez2023mechanismsofiron pages 1-2, sanchez‐jimenez2023mechanismsofiron pages 5-7)

### Trait scope for curation: what this trait represents

**Trait content (recommended TraitMech interpretation):**
- A *lifestyle capacity* combining (i) **context-triggered expression** of pathogenic programs and (ii) **fitness outside invasive disease** (commensal colonization or environmental persistence), such that disease is conditional on host/environmental perturbations.

**Out of scope / do-not-conflate:**
- Not equivalent to “pathogen” generally (obligate pathogens may not require host compromise).
- Not equivalent to “commensal” or “colonizer” (colonization can be frequent without disease progression). (uberoi2024thewoundmicrobiota pages 1-2)
- Not a single gene/pathway: opportunism is a *causal subgraph* spanning host state, ecological context, and regulated microbial mechanisms.

### Candidate causal graph nodes (grouped by type; ontology grounding where feasible)

#### A) Host/environmental context nodes
- **Immunocompromised host** (label-only; host state) (sangiorgio2024theimpactof pages 9-10)
- **Barrier breach / epithelial barrier disruption** (GO label-only; includes wound barrier breach) (uberoi2024thewoundmicrobiota pages 1-2)
- **Normally sterile site exposure** (label-only; “sterile tissue”) (uberoi2024thewoundmicrobiota pages 1-2)
- **Antibiotic exposure** (CHEBI label-only) → **dysbiosis** (community state) (jacobsen2023theroleof pages 1-2, alsoubhi2024theecologyof pages 4-6)
- **Nutritional immunity / iron limitation** (label-only; host-driven metal sequestration) (sanchez‐jimenez2023mechanismsofiron pages 1-2)

#### B) Microbial processes/modules
- **Adhesion** (GO:0007155) (jacobsen2023theroleof pages 1-2)
- **Invasion of host tissue** (label-only; can be split into induced endocytosis vs active penetration for fungi) (jacobsen2023theroleof pages 1-2)
- **Biofilm formation** (GO:0042710) (sangiorgio2024theimpactof pages 9-10, uberoi2024thewoundmicrobiota pages 1-2)
- **Secretion system activity: Type II secretion system (T2SS)** (GO label-only) (sebastian2024leafmicrobiomedysbiosis pages 3-4, sebastian2024leafmicrobiomedysbiosis pages 11-12)
- **Iron acquisition / siderophore biosynthesis and uptake** (label-only; may map to MetaCyc/KEGG in later curation) (sanchez‐jimenez2023mechanismsofiron pages 1-2, sanchez‐jimenez2023mechanismsofiron pages 2-4)
- **Quorum sensing (PQS system)** (label-only; pathway/regulatory module) (sanchez‐jimenez2023mechanismsofiron pages 5-7)

#### C) Genes/proteins/complexes (exemplars; taxon-specific)
- **Plant NADPH oxidase RBOHD** (gene label: RBOHD; Arabidopsis) (sebastian2024leafmicrobiomedysbiosis pages 1-2, sebastian2024leafmicrobiomedysbiosis pages 2-3)
- **Xanthomonas T2SS Xps** (system label) (sebastian2024leafmicrobiomedysbiosis pages 3-4)
- **Candida adhesin Als3** (protein label; UniProt grounding recommended during curation) (jacobsen2023theroleof pages 1-2)
- **Candida candidalysin** (toxin label) (froismartins2024candidaalbicansvirulence pages 1-2)
- **Pseudomonas Fur** (Ferric uptake regulator; bacterial TF) (sanchez‐jimenez2023mechanismsofiron pages 5-7)
- **Pseudomonas PqsR** (QS regulator) (sanchez‐jimenez2023mechanismsofiron pages 5-7)
- **Enterococcus Fsr locus** (QS locus controlling gelatinase/biofilm; label-only from review) (sangiorgio2024theimpactof pages 9-10)

#### D) Chemicals/metabolites
- **Siderophores (general class)** (CHEBI label-only) (sanchez‐jimenez2023mechanismsofiron pages 1-2)
- **Fe3+ (iron(III)) / Fe3+-complex** (CHEBI: iron(III) label) (sanchez‐jimenez2023mechanismsofiron pages 1-2)
- **PQS (Pseudomonas quinolone signal)** (CHEBI label-only) (sanchez‐jimenez2023mechanismsofiron pages 5-7)

### Evidence-backed candidate causal edges (curation table)
The following table is formatted for direct translation into a TraitMech YAML causal graph, with uncertainty and taxon-specificity explicitly annotated.

| Edge (subject–predicate–object) | Node types (S/O) | Suggested ontology grounding (subject ; object) | Evidence snippet (short quote) | Source (first author, journal, year) | DOI | URL | Notes/uncertainty |
|---|---|---|---|---|---|---|---|
| host defense compromise / immunocompromised host → increases susceptibility to → opportunistic pathogen disease | host condition → lifestyle/phenotype | label-only: immunocompromised host ; METPO:traitmech:000046 opportunistic pathogen | “when host defenses are compromised” (sangiorgio2024theimpactof pages 9-10, sangiorgio2024theimpactof pages 1-2) | Sangiorgio, *Pathogens*, 2024 | 10.3390/pathogens13050409 | https://doi.org/10.3390/pathogens13050409 | Broad trait-defining edge; review-level, cross-taxon framing but illustrated with *Enterococcus*. |
| barrier breach / sterile site access → enables → infection by opportunistic microbes | host process/site access → disease process | GO candidate: epithelial barrier maintenance/disruption (label-only) ; label-only: infection in normally sterile site | “barrier breach exposes sterile tissue to microbes” (uberoi2024thewoundmicrobiota pages 1-2) | Uberoi, *Nat Rev Microbiol*, 2024 | 10.1038/s41579-024-01035-z | https://doi.org/10.1038/s41579-024-01035-z | Generalizable ecological/clinical edge; not a single gene-level mechanism. |
| antibiotic treatment / prior antibiotic exposure → promotes → fungal expansion or overgrowth of opportunists | exposure → community state | CHEBI/label-only: antibiotics ; label-only: dysbiosis / opportunist overgrowth | “Antibiotic-driven fungal expansion is highlighted as a common risk factor for candidiasis” (jacobsen2023theroleof pages 1-2) | Jacobsen, *Curr Clin Microbiol Rep*, 2023 | 10.1007/s40588-023-00190-w | https://doi.org/10.1007/s40588-023-00190-w | Candida-focused; should likely be curated as antibiotic exposure → dysbiosis/overgrowth rather than direct universal pathogenicity. |
| antimicrobial-induced dysbiosis → increases colonization by → opportunists | community state → population expansion | label-only: dysbiosis ; label-only: opportunists / Enterococcus | “Dysbiosis increases colonization by opportunists (e.g., Enterococcus)” (alsoubhi2024theecologyof pages 4-6) | Alsoubhi, infection-control ecology review, 2024 | NA | NA | Useful high-level ecological edge; source is generic review with unclear journal metadata, so curate cautiously. |
| gut reservoir / gut colonization → risk factor for → systemic or disseminated candidiasis | anatomical reservoir → disease | UBERON candidate: gut ; label-only: disseminated candidiasis | “colonization of the gut is not only a risk factor for systemic candidiasis” (jacobsen2023theroleof pages 1-2) | Jacobsen, *Curr Clin Microbiol Rep*, 2023 | 10.1007/s40588-023-00190-w | https://doi.org/10.1007/s40588-023-00190-w | Strongly supports reservoir concept; Candida-specific. |
| adhesion (Candida) → enables → invasion / pathogenic transition | biological process → biological process | GO:0007155 cell adhesion ; GO candidate: invasion of host tissue (label-only) | “Adhesion, invasion, and tissue damage are critical steps in the infection process” (jacobsen2023theroleof pages 1-2) | Jacobsen, *Curr Clin Microbiol Rep*, 2023 | 10.1007/s40588-023-00190-w | https://doi.org/10.1007/s40588-023-00190-w | Mechanistically central but review-summarized. |
| Als3 adhesin → promotes → induced endocytosis / host invasion | protein → process | UniProt/label-only: Als3 ; label-only: induced endocytosis / invasion | “invasion via induced endocytosis (Als3/Ssa1 interactions with cadherins, EGFR, HER2)” (jacobsen2023theroleof pages 1-2) | Jacobsen, *Curr Clin Microbiol Rep*, 2023 | 10.1007/s40588-023-00190-w | https://doi.org/10.1007/s40588-023-00190-w | Candida-specific; receptor identities mentioned in review but not all individually quoted in excerpt. |
| hyphal morphogenesis / filamentation → promotes → tissue damage and pathogenic state | morphology/process → phenotype/process | GO candidate: filamentous growth ; label-only: tissue damage / pathogenic state | “filamentation-driven tissue damage” (jacobsen2023theroleof pages 1-2) | Jacobsen, *Curr Clin Microbiol Rep*, 2023 | 10.1007/s40588-023-00190-w | https://doi.org/10.1007/s40588-023-00190-w | Candida-specific; could be split into morphology → invasion and morphology → damage. |
| candidalysin production → causes → host cell damage | toxin/activity → phenotype | label-only: candidalysin ; GO candidate: host cell damage (label-only) | “hyphae formation and candidalysin production” and “epithelial invasion and host cell damage” (froismartins2024candidaalbicansvirulence pages 1-2) | Fróis-Martins, *Curr Clin Microbiol Rep*, 2024 | 10.1007/s40588-024-00235-8 | https://doi.org/10.1007/s40588-024-00235-8 | In excerpt, the causal linkage is summarized rather than a direct full-sentence quote; still strong review evidence. |
| adaptive antifungal immunity → limits → overt filamentation and tissue damage | host immune process → phenotype | GO/label-only: adaptive antifungal immunity ; label-only: overt filamentation and tissue damage | “Overt filamentation and tissue damage is in turn prevented by adaptive antifungal immunity” (froismartins2024candidaalbicansvirulence pages 1-2) | Fróis-Martins, *Curr Clin Microbiol Rep*, 2024 | 10.1007/s40588-024-00235-8 | https://doi.org/10.1007/s40588-024-00235-8 | Host-suppression edge; useful negative control in causal graph. |
| epithelial integrity / mucus / antimicrobial peptides / IgA → limits → fungal colonization or pathogenic potential | host defense ensemble → phenotype | GO/label-only: epithelial integrity + mucus + antimicrobial peptides + IgA ; label-only: fungal colonization/pathogenic potential | “mucus and antimicrobial peptides, regulate fungal colonization and inhibit pathogenic potential” (jensen2024controllingcandida pages 1-2) | Jensen, *Infect Immun*, 2024 | 10.1128/iai.00516-23 | https://doi.org/10.1128/iai.00516-23 | Composite host-defense node may need decomposition into separate nodes for curation. |
| defects in epithelial biology / mucus / AMP secretion / immune responses → permits → expansion or epithelial colonization by fungi | host defect → microbial expansion | label-only: barrier/immune defects ; label-only: expansion of commensal fungi | “permits expansion or epithelial colonization by normally excluded fungi” (jensen2024controllingcandida pages 1-2) | Jensen, *Infect Immun*, 2024 | 10.1128/iai.00516-23 | https://doi.org/10.1128/iai.00516-23 | Strong host-context edge; gut-fungi focused. |
| nutritional immunity / iron limitation → promotes → high-affinity iron transport and siderophore production | host-imposed nutrient limitation → process | GO/label-only: nutritional immunity / iron limitation ; label-only: siderophore production / high-affinity iron transport | “Under iron limitation, the production of high-affinity iron transport systems is promoted” (sanchez‐jimenez2023mechanismsofiron pages 1-2) | Sánchez-Jiménez, *Microb Biotechnol*, 2023 | 10.1111/1751-7915.14241 | https://doi.org/10.1111/1751-7915.14241 | Excellent mechanistic edge; Pseudomonas-specific exemplar of opportunist adaptation. |
| siderophores → scavenge → iron / Fe3+ complexes | metabolite → chemical process | CHEBI/label-only: siderophore ; CHEBI:iron(III) / Fe3+-complex | “scavenge iron and form soluble Fe3+-complexes” (sanchez‐jimenez2023mechanismsofiron pages 1-2) | Sánchez-Jiménez, *Microb Biotechnol*, 2023 | 10.1111/1751-7915.14241 | https://doi.org/10.1111/1751-7915.14241 | Core metabolic edge; general in siderophore biology though source is *P. aeruginosa*. |
| PQS quorum-sensing signal → promotes transcription of → virulence genes | small molecule / QS signal → gene expression program | CHEBI/label-only: Pseudomonas quinolone signal (PQS) ; label-only: virulence genes | “promoting transcription of the pqs biosynthesis operons and that of several P. aeruginosa virulence genes” (sanchez‐jimenez2023mechanismsofiron pages 5-7, sanchez‐jimenez2023mechanismsofiron pages 4-5) | Sánchez-Jiménez, *Microb Biotechnol*, 2023 | 10.1111/1751-7915.14241 | https://doi.org/10.1111/1751-7915.14241 | Strong mechanistic edge; taxon-specific to *P. aeruginosa*. |
| prior medical device insertion → promotes → Enterococcus biofilm-associated infection | exposure/device → process/phenotype | label-only: medical device insertion / central venous catheter ; GO:0042710 biofilm formation / label-only infection | “medical device insertion” and “biofilm formation (on mucosa and devices)” (sangiorgio2024theimpactof pages 9-10, sangiorgio2024theimpactof pages 1-2) | Sangiorgio, *Pathogens*, 2024 | 10.3390/pathogens13050409 | https://doi.org/10.3390/pathogens13050409 | Built from two exact phrases in same review; device → biofilm → infection path should be represented as two edges if stricter granularity desired. |
| Enterococcus biofilm formation → promotes → persistence and infection in immunocompromised hosts | process → phenotype | GO:0042710 biofilm formation ; label-only: persistence/infection | “biofilm formation (on mucosa and devices)” (sangiorgio2024theimpactof pages 9-10) | Sangiorgio, *Pathogens*, 2024 | 10.3390/pathogens13050409 | https://doi.org/10.3390/pathogens13050409 | Enterococcus-specific; persistence/infection outcome is inferred from surrounding excerpt context. |
| host RBOHD defect → enables → opportunistic Xanthomonas disease | host gene defect → phenotype | label-only: RBOHD defect ; label-only: Xanthomonas disease | “loss of the NADPH oxidase RBOHD” and “permits opportunistic Xanthomonas … to cause disease” (sebastian2024leafmicrobiomedysbiosis pages 1-2, sebastian2024leafmicrobiomedysbiosis pages 2-3) | Pfeilmeier, *Nat Microbiol*, 2024 | 10.1038/s41564-023-01555-z | https://doi.org/10.1038/s41564-023-01555-z | Plant-specific but conceptually valuable for opportunism under immune compromise. |
| Xanthomonas T2SS-dependent enzyme secretion → causes → tissue degradation | secretion system/process → phenotype | GO/label-only: type II secretion system (T2SS) ; label-only: tissue degradation | “cell wall-degrading enzymes secreted via T2SS Xps” and “cell-free supernatants reproduce leaf degradation” (sebastian2024leafmicrobiomedysbiosis pages 3-4, sebastian2024leafmicrobiomedysbiosis pages 11-12) | Pfeilmeier, *Nat Microbiol*, 2024 | 10.1038/s41564-023-01555-z | https://doi.org/10.1038/s41564-023-01555-z | Strong primary-study edge; plant-pathogen specific. |
| tissue degradation → triggers → leaf microbiome dysbiosis | phenotype → community state | label-only: tissue degradation ; label-only: microbiome dysbiosis | “Leaf microbiome dysbiosis triggered by t2ss-dependent enzyme secretion” (sebastian2024leafmicrobiomedysbiosis pages 11-12) | Pfeilmeier, *Nat Microbiol*, 2024 | 10.1038/s41564-023-01555-z | https://doi.org/10.1038/s41564-023-01555-z | Mechanism partially compressed from title and figure-supported narrative; still directly phrased. |
| wound colonization + host susceptibility factors → determines progression to → infection | community state/host factors → disease state | label-only: wound colonization + host susceptibility ; label-only: local/systemic infection | “Nearly all wounds are colonized but only some progress to infection” (uberoi2024thewoundmicrobiota pages 1-2) | Uberoi, *Nat Rev Microbiol*, 2024 | 10.1038/s41579-024-01035-z | https://doi.org/10.1038/s41579-024-01035-z | Good boundary-case edge emphasizing opportunism is context-dependent, not equivalent to colonization. |


*Table: This table lists curation-ready candidate causal edges for the opportunistic pathogen trait, grounded in 2023–2024 evidence across Candida, Enterococcus, Pseudomonas, Xanthomonas, wound microbiota, and dysbiosis ecology. It is useful for selecting which host-context and microbial-mechanism relationships are strong enough for TraitMech graph curation.*

### Current applications and real-world implementations (how these mechanisms are used)

1. **Clinical infection risk stratification / prevention**
   - Opportunistic infection risk is operationalized in clinical settings by identifying immunocompromised states (e.g., chemotherapy/HSCT) and device-associated exposure that predispose to opportunistic commensals like *Enterococcus*. (sangiorgio2024theimpactof pages 9-10, sangiorgio2024theimpactof pages 1-2)

2. **Wound management and biofilm-aware care**
   - The wound microbiota framework explicitly treats wound infection as a continuum from colonization to systemic infection, emphasizing biofilms and polymicrobial interactions as mechanisms of impaired healing and infection persistence. (uberoi2024thewoundmicrobiota pages 1-2)

3. **Microbiome-aware stewardship**
   - Antibiotic exposure and dysbiosis are repeatedly identified as upstream causal factors that enable opportunist expansion (Candida; Enterococcus; general ecology framing), supporting antimicrobial stewardship and microbiome-preserving strategies as real-world levers. (jacobsen2023theroleof pages 1-2, alsoubhi2024theecologyof pages 4-6, sangiorgio2024theimpactof pages 9-10)

4. **Anti-virulence and nutrient-targeting strategies (translational research axis)**
   - Iron homeostasis is explicitly presented as an exploitable vulnerability in *P. aeruginosa*, because iron limitation triggers iron-acquisition systems and QS-linked virulence gene regulation; thus iron chelators/mimics and disruption of siderophore uptake are conceptually aligned with targeting opportunist fitness in-host. (sanchez‐jimenez2023mechanismsofiron pages 1-2, sanchez‐jimenez2023mechanismsofiron pages 2-4, sanchez‐jimenez2023mechanismsofiron pages 5-7)

### Expert opinions and analysis (authoritative synthesis grounded in citations)

- **Opportunism is an interactional outcome, not an intrinsic label**: multiple reviews emphasize that host immunity, barrier function, and microbiota context set the boundary between commensalism and disease, with “Nearly all wounds … colonized but only some progress to infection” capturing this principle. (uberoi2024thewoundmicrobiota pages 1-2)
- **Virulence traits can support commensal fitness**: *C. albicans* literature argues that classic virulence determinants can be required for stable colonization and to elicit host-protective immunity, implying that causal graphs should include *bidirectional* host–microbe feedback (virulence → immunity → containment). (froismartins2024candidaalbicansvirulence pages 1-2)
- **Host genotype can enable opportunism independent of higher pathogen burden**: the *Xanthomonas* rbohD model demonstrates that immune failure can allow disease without increased colonization, sharpening the curation distinction between “growth advantage” vs “host tolerance failure.” (sebastian2024leafmicrobiomedysbiosis pages 3-4)

### Relevant statistics and data (recent sources)
- **Candida colonization prevalence**: gut colonization in **40–60%** of healthy individuals; oral carriage **~20–60%** depending on population. (jacobsen2023theroleof pages 1-2)
- **Wound burden (USA)**: wound prevalence **~2%**; spending **up to $96.8B annually**. (uberoi2024thewoundmicrobiota pages 1-2)
- **Fungal infection burden**: review reports **~1 billion fungal infections/year** and **~4 million deaths**, and states **invasive candidiasis accounts for about a million deaths annually** (noting this is a review-level global estimate). (froismartins2024candidaalbicansvirulence pages 1-2)
- **Enterococcus outcomes and AMR burden**: WHO-reported *Enterococcus* mortality **14.3–32.3%**, and substantial geographic variation in vancomycin-resistant *E. faecium* (some countries <1%, others ≥25%, some ≥50%). (sangiorgio2024theimpactof pages 1-2)
- **Quantitative causal evidence in plant opportunism**: dysbiosis effect size **12.5% (P=0.0001)** with *Xanthomonas* Leaf131 present vs **2.8% (P=0.71)** without Leaf131 in SynCom-137. (sebastian2024leafmicrobiomedysbiosis pages 2-3)

### Visual evidence (figure support)
Figure evidence from Pfeilmeier et al. supports the edge chain **host immune defect (rbohD) → opportunistic pathogen effect → community dysbiosis / disease phenotype**, which can be cited when curating host-context nodes and edges. (sebastian2024leafmicrobiomedysbiosis media 704e81b2)

### DOI-first bibliography (with dates and URLs)

1. **Pfeilmeier S**, et al. *Leaf microbiome dysbiosis triggered by T2SS-dependent enzyme secretion from opportunistic Xanthomonas pathogens*. **Nature Microbiology**. **Jan 2024**. DOI: **10.1038/s41564-023-01555-z**. URL: https://doi.org/10.1038/s41564-023-01555-z (sebastian2024leafmicrobiomedysbiosis pages 1-2, sebastian2024leafmicrobiomedysbiosis pages 3-4, sebastian2024leafmicrobiomedysbiosis pages 2-3, sebastian2024leafmicrobiomedysbiosis pages 11-12, sebastian2024leafmicrobiomedysbiosis media 704e81b2)
2. **Uberoi A**, McCready-Vangi A, Grice EA. *The wound microbiota: microbial mechanisms of impaired wound healing and infection.* **Nature Reviews Microbiology**. **Apr 2024**. DOI: **10.1038/s41579-024-01035-z**. URL: https://doi.org/10.1038/s41579-024-01035-z (uberoi2024thewoundmicrobiota pages 1-2)
3. **Jensen O**, et al. *Controlling Candida: immune regulation of commensal fungi in the gut.* **Infection and Immunity**. **Sep 2024**. DOI: **10.1128/iai.00516-23**. URL: https://doi.org/10.1128/iai.00516-23 (jensen2024controllingcandida pages 1-2)
4. **Fróis‑Martins R**, Lagler J, LeibundGut-Landmann S. *Candida albicans Virulence Traits in Commensalism and Disease.* **Current Clinical Microbiology Reports**. **Oct 2024**. DOI: **10.1007/s40588-024-00235-8**. URL: https://doi.org/10.1007/s40588-024-00235-8 (froismartins2024candidaalbicansvirulence pages 1-2)
5. **Sangiorgio G**, et al. *The Impact of Enterococcus spp. in the Immunocompromised Host: A Comprehensive Review.* **Pathogens**. **May 2024**. DOI: **10.3390/pathogens13050409**. URL: https://doi.org/10.3390/pathogens13050409 (sangiorgio2024theimpactof pages 9-10, sangiorgio2024theimpactof pages 1-2)
6. **Jacobsen ID**. *The Role of Host and Fungal Factors in the Commensal-to-Pathogen Transition of Candida albicans.* **Current Clinical Microbiology Reports**. **Mar 2023**. DOI: **10.1007/s40588-023-00190-w**. URL: https://doi.org/10.1007/s40588-023-00190-w (jacobsen2023theroleof pages 1-2)
7. **Sánchez‑Jiménez A**, Marcos‑Torres FJ, Llamas MA. *Mechanisms of iron homeostasis in Pseudomonas aeruginosa and emerging therapeutics directed to disrupt this vital process.* **Microbial Biotechnology**. **Mar 2023**. DOI: **10.1111/1751-7915.14241**. URL: https://doi.org/10.1111/1751-7915.14241 (sanchez‐jimenez2023mechanismsofiron pages 1-2, sanchez‐jimenez2023mechanismsofiron pages 2-4, sanchez‐jimenez2023mechanismsofiron pages 5-7)

### Warnings / curation cautions

1. **Avoid over-generalizing from single-taxon mechanisms**: T2SS (Xanthomonas), PQS (Pseudomonas), candidalysin (Candida), and RBOHD (plant immunity) are excellent mechanistic exemplars but should be curated either as taxon-scoped nodes/edges or as children under more general mechanistic parents (e.g., “secreted degradative enzymes,” “quorum sensing signal,” “toxins,” “ROS-mediated immunity”). (sebastian2024leafmicrobiomedysbiosis pages 3-4, sanchez‐jimenez2023mechanismsofiron pages 5-7, froismartins2024candidaalbicansvirulence pages 1-2)
2. **Composite host-defense nodes may need decomposition**: “mucus and antimicrobial peptides” and “epithelial integrity” are bundled in some reviews; for TraitMech, splitting into separable nodes (mucus layer, AMPs, IgA, epithelial junction integrity) will improve mechanistic precision. (jensen2024controllingcandida pages 1-2)
3. **Generic infection-control ecology review metadata is unclear**: edges derived from this source should be marked lower confidence until a peer-reviewed venue and stable DOI/URL are confirmed. (alsoubhi2024theecologyof pages 4-6)
4. **Burden estimates are review-level**: global death and incidence estimates (fungal infections, invasive candidiasis) should be tagged as “review estimate” and not treated as primary surveillance data in the graph. (froismartins2024candidaalbicansvirulence pages 1-2)


References

1. (uberoi2024thewoundmicrobiota pages 1-2): Aayushi Uberoi, Amelia McCready-Vangi, and Elizabeth A. Grice. The wound microbiota: microbial mechanisms of impaired wound healing and infection. Nature reviews. Microbiology, 22:507-521, Apr 2024. URL: https://doi.org/10.1038/s41579-024-01035-z, doi:10.1038/s41579-024-01035-z. This article has 804 citations.

2. (jacobsen2023theroleof pages 1-2): Ilse D. Jacobsen. The role of host and fungal factors in the commensal-to-pathogen transition of candida albicans. Current Clinical Microbiology Reports, 10:55-65, Mar 2023. URL: https://doi.org/10.1007/s40588-023-00190-w, doi:10.1007/s40588-023-00190-w. This article has 68 citations.

3. (froismartins2024candidaalbicansvirulence pages 1-2): Ricardo Fróis-Martins, Julia Lagler, and Salomé LeibundGut-Landmann. Candida albicans virulence traits in commensalism and disease. Current Clinical Microbiology Reports, 11:231-240, Oct 2024. URL: https://doi.org/10.1007/s40588-024-00235-8, doi:10.1007/s40588-024-00235-8. This article has 20 citations.

4. (sangiorgio2024theimpactof pages 9-10): Giuseppe Sangiorgio, Maddalena Calvo, Giuseppe Migliorisi, Floriana Campanile, and Stefania Stefani. The impact of enterococcus spp. in the immunocompromised host: a comprehensive review. Pathogens, 13:409, May 2024. URL: https://doi.org/10.3390/pathogens13050409, doi:10.3390/pathogens13050409. This article has 60 citations.

5. (sebastian2024leafmicrobiomedysbiosis pages 3-4): Sebastian Pfeilmeier, Anja Werz, Marine Ote, Miriam Bortfeld-Miller, Pascal Kirner, Andreas Keppler, Lucas Hemmerle, Christoph G. Gäbelein, Gabriella C. Petti, Sarah Wolf, Christine M. Pestalozzi, and Julia A. Vorholt. Leaf microbiome dysbiosis triggered by t2ss-dependent enzyme secretion from opportunistic xanthomonas pathogens. Nature Microbiology, 9:136-149, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01555-z, doi:10.1038/s41564-023-01555-z. This article has 71 citations and is from a highest quality peer-reviewed journal.

6. (sangiorgio2024theimpactof pages 1-2): Giuseppe Sangiorgio, Maddalena Calvo, Giuseppe Migliorisi, Floriana Campanile, and Stefania Stefani. The impact of enterococcus spp. in the immunocompromised host: a comprehensive review. Pathogens, 13:409, May 2024. URL: https://doi.org/10.3390/pathogens13050409, doi:10.3390/pathogens13050409. This article has 60 citations.

7. (alsoubhi2024theecologyof pages 4-6): NB Alsoubhi, AA Alsoubhi, and AH Alkhalifa. The ecology of infection control: balancing microbes, medicine, and management. Unknown journal, 2024.

8. (sanchez‐jimenez2023mechanismsofiron pages 1-2): Ana Sánchez‐Jiménez, Francisco J. Marcos‐Torres, and María A. Llamas. Mechanisms of iron homeostasis in pseudomonas aeruginosa and emerging therapeutics directed to disrupt this vital process. Microbial Biotechnology, 16:1475-1491, Mar 2023. URL: https://doi.org/10.1111/1751-7915.14241, doi:10.1111/1751-7915.14241. This article has 61 citations and is from a peer-reviewed journal.

9. (sebastian2024leafmicrobiomedysbiosis pages 11-12): Sebastian Pfeilmeier, Anja Werz, Marine Ote, Miriam Bortfeld-Miller, Pascal Kirner, Andreas Keppler, Lucas Hemmerle, Christoph G. Gäbelein, Gabriella C. Petti, Sarah Wolf, Christine M. Pestalozzi, and Julia A. Vorholt. Leaf microbiome dysbiosis triggered by t2ss-dependent enzyme secretion from opportunistic xanthomonas pathogens. Nature Microbiology, 9:136-149, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01555-z, doi:10.1038/s41564-023-01555-z. This article has 71 citations and is from a highest quality peer-reviewed journal.

10. (sebastian2024leafmicrobiomedysbiosis pages 2-3): Sebastian Pfeilmeier, Anja Werz, Marine Ote, Miriam Bortfeld-Miller, Pascal Kirner, Andreas Keppler, Lucas Hemmerle, Christoph G. Gäbelein, Gabriella C. Petti, Sarah Wolf, Christine M. Pestalozzi, and Julia A. Vorholt. Leaf microbiome dysbiosis triggered by t2ss-dependent enzyme secretion from opportunistic xanthomonas pathogens. Nature Microbiology, 9:136-149, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01555-z, doi:10.1038/s41564-023-01555-z. This article has 71 citations and is from a highest quality peer-reviewed journal.

11. (sanchez‐jimenez2023mechanismsofiron pages 2-4): Ana Sánchez‐Jiménez, Francisco J. Marcos‐Torres, and María A. Llamas. Mechanisms of iron homeostasis in pseudomonas aeruginosa and emerging therapeutics directed to disrupt this vital process. Microbial Biotechnology, 16:1475-1491, Mar 2023. URL: https://doi.org/10.1111/1751-7915.14241, doi:10.1111/1751-7915.14241. This article has 61 citations and is from a peer-reviewed journal.

12. (sanchez‐jimenez2023mechanismsofiron pages 5-7): Ana Sánchez‐Jiménez, Francisco J. Marcos‐Torres, and María A. Llamas. Mechanisms of iron homeostasis in pseudomonas aeruginosa and emerging therapeutics directed to disrupt this vital process. Microbial Biotechnology, 16:1475-1491, Mar 2023. URL: https://doi.org/10.1111/1751-7915.14241, doi:10.1111/1751-7915.14241. This article has 61 citations and is from a peer-reviewed journal.

13. (jensen2024controllingcandida pages 1-2): Owen Jensen, Emma Trujillo, Luke Hanson, and Kyla S. Ost. Controlling <i>candida</i> : immune regulation of commensal fungi in the gut. Infection and Immunity, Sep 2024. URL: https://doi.org/10.1128/iai.00516-23, doi:10.1128/iai.00516-23. This article has 19 citations and is from a peer-reviewed journal.

14. (sebastian2024leafmicrobiomedysbiosis pages 1-2): Sebastian Pfeilmeier, Anja Werz, Marine Ote, Miriam Bortfeld-Miller, Pascal Kirner, Andreas Keppler, Lucas Hemmerle, Christoph G. Gäbelein, Gabriella C. Petti, Sarah Wolf, Christine M. Pestalozzi, and Julia A. Vorholt. Leaf microbiome dysbiosis triggered by t2ss-dependent enzyme secretion from opportunistic xanthomonas pathogens. Nature Microbiology, 9:136-149, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01555-z, doi:10.1038/s41564-023-01555-z. This article has 71 citations and is from a highest quality peer-reviewed journal.

15. (sanchez‐jimenez2023mechanismsofiron pages 4-5): Ana Sánchez‐Jiménez, Francisco J. Marcos‐Torres, and María A. Llamas. Mechanisms of iron homeostasis in pseudomonas aeruginosa and emerging therapeutics directed to disrupt this vital process. Microbial Biotechnology, 16:1475-1491, Mar 2023. URL: https://doi.org/10.1111/1751-7915.14241, doi:10.1111/1751-7915.14241. This article has 61 citations and is from a peer-reviewed journal.

16. (sebastian2024leafmicrobiomedysbiosis media 704e81b2): Sebastian Pfeilmeier, Anja Werz, Marine Ote, Miriam Bortfeld-Miller, Pascal Kirner, Andreas Keppler, Lucas Hemmerle, Christoph G. Gäbelein, Gabriella C. Petti, Sarah Wolf, Christine M. Pestalozzi, and Julia A. Vorholt. Leaf microbiome dysbiosis triggered by t2ss-dependent enzyme secretion from opportunistic xanthomonas pathogens. Nature Microbiology, 9:136-149, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01555-z, doi:10.1038/s41564-023-01555-z. This article has 71 citations and is from a highest quality peer-reviewed journal.