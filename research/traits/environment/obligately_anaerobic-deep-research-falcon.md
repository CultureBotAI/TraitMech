---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:08:29.937596'
end_time: '2026-08-04T02:20:51.163549'
duration_seconds: 741.23
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: obligately anaerobic
  trait_identifier: METPO:1000607
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: obligately_anaerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference in which molecular oxygen (O\u2082) inhibits or\
    \ prevents growth."
  parent_traits: METPO:1000601
  synonyms: obligate anaerobe, obligate anaerobic
  evidence_summary: 'https://www.ncbi.nlm.nih.gov/books/NBK482349/: Oxygen is toxic
    to anaerobes (Supports oxygen inhibition/toxicity for obligately anaerobic organisms.)
    | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides
    fragilis is described as an obligate anaerobe.)'
  causal_graph_summary: 'obligate_anaerobe_oxygen_toxicity: 14 nodes, 12 edges'
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
- **Trait label:** obligately anaerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000607
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which molecular oxygen (O₂) inhibits or prevents growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** obligate anaerobe, obligate anaerobic
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: Oxygen is toxic to anaerobes (Supports oxygen inhibition/toxicity for obligately anaerobic organisms.) | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides fragilis is described as an obligate anaerobe.)
- **Existing causal graph summary:** obligate_anaerobe_oxygen_toxicity: 14 nodes, 12 edges

## Research Objective

Research the microbial trait **obligately anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_anaerobic.yaml`.

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
- **Trait label:** obligately anaerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000607
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which molecular oxygen (O₂) inhibits or prevents growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** obligate anaerobe, obligate anaerobic
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: Oxygen is toxic to anaerobes (Supports oxygen inhibition/toxicity for obligately anaerobic organisms.) | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides fragilis is described as an obligate anaerobe.)
- **Existing causal graph summary:** obligate_anaerobe_oxygen_toxicity: 14 nodes, 12 edges

## Research Objective

Research the microbial trait **obligately anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_anaerobic.yaml`.

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


# Curation Report: Obligately Anaerobic

## Trait record and scope

- **Trait label:** obligately anaerobic
- **Trait identifier:** **METPO:1000607**
- **Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED
- **Definition:** an oxygen preference in which molecular oxygen (O₂) inhibits or prevents growth.
- **Parent:** METPO:1000601
- **Synonyms:** obligate anaerobe; obligate anaerobic

### Scope summary

For TraitMech, **METPO:1000607 should be interpreted as an assay-observed growth phenotype**: O₂ at the tested concentration blocks or substantially inhibits vegetative growth. It should not be interpreted as absolute inability to encounter, consume, or transiently survive O₂. The authoritative synthesis by Lu and Imlay emphasizes that the operational definition obscures a broad continuum of oxygen tolerance: obligate anaerobes may possess substantial ROS defenses, consume low concentrations of O₂, remain metabolically active during transient exposure, or survive air without being able to grow aerobically. Their defining feature remains O₂-dependent growth arrest. (lu2021whenanaerobesencounter pages 1-3, lu2021whenanaerobesencounter pages 3-4)

The best-supported mechanistic model is therefore not simply “absence of catalase or superoxide dismutase.” Rather, obligate anaerobiosis commonly reflects a conflict between highly efficient anaerobic metabolism—using glycyl radicals, low-potential electron carriers, and exposed metal centers—and O₂. O₂ directly poisons some enzymes and also accepts adventitious electrons to form superoxide and H₂O₂; damage to several essential metabolic nodes then arrests growth. Antioxidant and O₂-scavenging systems determine the exposure that can be tolerated but need not convert the organism into a facultative anaerobe. (khademian2020doreactiveoxygen pages 1-2, lu2021whenanaerobesencounter pages 9-11, lu2021whenanaerobesencounter pages 6-8)

### Boundary cases

1. **Facultative anaerobe:** can grow both without O₂ and with O₂, generally switching to aerobic respiration when O₂ is available. This should not receive METPO:1000607 if reproducible aerobic growth occurs.
2. **Aerotolerant anaerobe:** does not use O₂ as the principal terminal electron acceptor but tolerates exposure and may grow fermentatively in its presence. Aerotolerance is distinct from transient survival by an obligate anaerobe.
3. **Microaerophile:** requires or grows optimally at O₂ below atmospheric concentration. Growth at a defined low-O₂ optimum distinguishes this state from an obligate anaerobe whose growth is progressively inhibited by O₂.
4. **Extremely oxygen-sensitive organism:** a quantitative survival category, not automatically synonymous with obligate anaerobiosis. Conversely, an obligate anaerobe can be relatively aerotolerant.
5. **O₂ consumption without aerobic growth:** flavodiiron proteins and reverse rubrerythrins may reduce O₂ to water for detoxification. This is compatible with METPO:1000607 because detoxifying O₂ reduction is not necessarily energy-conserving aerobic respiration. *Clostridioides difficile* provides a clear 2024 example. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5)
6. **Spore survival:** an aerotolerant spore does not demonstrate aerobic growth of vegetative cells. Sporulation and vegetative obligate anaerobiosis should be represented separately.
7. **Assay dependence:** O₂ percentage, exposure duration, medium redox potential, inoculum, growth versus survival endpoint, carbon source, cysteine/reductant content, and strain identity must accompany phenotype assertions. The wide strain variation in *Faecalibacterium* illustrates why a species-level categorical assignment can conceal important variation. (botin2023thetoleranceof pages 1-2, botin2023thetoleranceof pages 2-5)

## Current mechanistic understanding

### 1. Direct molecular-oxygen toxicity

O₂ attacks chemical features that are especially useful in anaerobic metabolism:

- **Pyruvate formate-lyase (PFL; EC 2.3.1.54):** O₂ reacts with its glycyl radical, leading to radical chemistry and polypeptide cleavage. Inactivation can occur within seconds at low O₂ concentrations. (lu2021whenanaerobesencounter pages 6-8, lu2021whenanaerobesencounter pages 17-19)
- **Pyruvate:ferredoxin oxidoreductase (PFOR; EC 1.2.7.1):** in *Bacteroides thetaiotaomicron*, PFOR loses activity during aeration even when superoxide and peroxide levels are altered, supporting direct O₂ poisoning. The inability to repair PFOR amplifies the metabolic effect. (khademian2020doreactiveoxygen pages 1-2)
- **Low-potential metal centers and [4Fe–4S] proteins:** O₂ oxidizes catalytic metal centers into nonfunctional states. In the representative aconitase reaction, [4Fe–4S]²⁺ becomes [4Fe–4S]³⁺ and then inactive [3Fe–4S]⁺, with an approximately 30-minute half-time under the cited conditions. Hydrogenases, nitrogenase, and methyl-coenzyme-M reductase are additional plausible direct targets, although their relevance is pathway- and taxon-specific. (lu2021whenanaerobesencounter pages 6-8)

### 2. ROS-mediated toxicity

Reduced flavins, ferredoxins, and metal centers can transfer electrons adventitiously to O₂, producing superoxide and H₂O₂. *B. thetaiotaomicron* was reported to generate H₂O₂ approximately ten times faster than *Escherichia coli* during aeration. Superoxide and peroxide then damage exposed iron cofactors; superoxide-mediated inactivation of fumarase is a particularly well-supported metabolic lesion. (lu2021whenanaerobesencounter pages 9-11, lu2021whenanaerobesencounter pages 22-27)

The causal chain most suitable for the core graph is:

> O₂ exposure → direct PFL/PFOR damage plus endogenous superoxide/H₂O₂ formation → inactivation of fumarase and other metal-dependent enzymes → impaired pyruvate dissimilation and central metabolism → growth arrest.

This is a multi-target model: no single damaged enzyme should be represented as a universal cause of obligate anaerobiosis across all taxa. (khademian2020doreactiveoxygen pages 1-2, lu2021whenanaerobesencounter pages 22-27)

### 3. Defense and tolerance modules

Obligate anaerobes frequently encode defenses comparable to, or distinct from, those of aerobes:

- **Superoxide reductase (SOR)** reduces superoxide to H₂O₂, avoiding O₂ production by the SOD reaction.
- **Superoxide dismutase (SOD)** occurs in some anaerobes and converts superoxide to O₂ plus H₂O₂.
- **Catalase, peroxiredoxins, alkyl-hydroperoxide reductase AhpCF, rubrerythrins, and other peroxidases** remove H₂O₂ or organic peroxides.
- **Flavodiiron proteins and reverse rubrerythrins** reductively scavenge O₂, commonly yielding water.
- **Repair/replacement systems** can restore oxidized metal centers or replace damaged proteins, although PFOR repair is limited in the experimentally characterized *B. thetaiotaomicron* system. (khademian2020doreactiveoxygen pages 1-2, botin2023thetoleranceof pages 1-2, botin2023thetoleranceof pages 2-5)

The 2023 *Faecalibacterium* study found marked strain differences in FDP, reverse-rubrerythrin, SOR, and alkyl-peroxidase repertoires. A strain with multiple FDP/SOR genes retained **0.15% survival after 20 minutes in air**, whereas a strain with only two identified detoxification genes reached **100% mortality after five minutes**. This is useful comparative evidence, but gene count and tolerance were correlated rather than reduced to a single causal locus. (botin2023thetoleranceof pages 2-5)

## Candidate nodes

### Trait, environmental, and assay nodes

- obligately anaerobic — **METPO:1000607**
- molecular oxygen — **CHEBI:15379**
- superoxide — **CHEBI:18421**
- hydrogen peroxide — **CHEBI:16240**
- cysteine — **CHEBI:17561**
- low oxygen tension; atmospheric oxygen/air; anoxic environment; redox potential; aeration duration; oxygen exposure assay — retain as label-only unless a verified ENVO or assay ontology term is selected during curation
- vegetative growth, growth arrest, survival after oxygen exposure, recovery/generation time — process or measurement nodes requiring explicit endpoint annotation

### Enzymes, proteins, and regulators

- pyruvate formate-lyase — **EC 2.3.1.54**
- pyruvate:ferredoxin oxidoreductase — **EC 1.2.7.1**
- fumarase/fumarate hydratase — **EC 4.2.1.2**
- aconitase — enzyme-class node; choose the taxon-appropriate EC/UniProt record during organism-specific curation
- anaerobic ribonucleotide reductase NrdD; hydrogenase; nitrogenase; methyl-coenzyme-M reductase — label-only candidates until a specific taxon/pathway is selected
- superoxide reductase, superoxide dismutase, catalase, peroxiredoxin, rubrerythrin, reverse rubrerythrin, flavodiiron protein, AhpC/AhpF — ground to taxon-specific UniProt accessions where possible rather than assigning one universal protein identifier
- *C. difficile* FdpA/CD1157, FdpF/CD1623, revRbr1/CD1474, revRbr2/CD1524, σA, σB, OseR, and Rex — taxon-specific label candidates pending verified strain-specific identifiers
- *B. thetaiotaomicron* RhaR, Rbr2, KatE, AhpCF, Sod, PFL, and PFOR — taxon-specific nodes pending UniProt/locus-tag verification

### Cofactors, functions, and processes

- [4Fe–4S] cluster binding — **GO:0051539** as a candidate molecular-function grounding
- glycyl-radical chemistry; low-potential electron transfer; O₂ reduction to water; superoxide reduction; peroxide detoxification; Fe–S-cluster oxidation; oxidative protein damage; central carbon metabolism; pyruvate dissimilation; fermentation; oxidative-stress response; transcriptional regulation — select verified GO, Rhea, KEGG, or MetaCyc terms only during YAML implementation
- NADH and NAD⁺; reduced ferredoxin; flavin cofactors; water; pyruvate; formate; acetyl-CoA — chemically ground with ChEBI during implementation after reaction direction and protonation state are fixed

### Taxa useful as evidence contexts

- *Bacteroides thetaiotaomicron* — primary model for direct O₂ versus ROS toxicity
- *Bacteroides fragilis* — established obligate-anaerobe example with substantial aerotolerance
- *Clostridioides difficile* — 2024 primary model for oxygen-reductase specialization across O₂ gradients
- *Faecalibacterium* spp., especially *F. longum* L2-6 — 2023 model for strain-dependent oxidative tolerance and cysteine protection
- *Fusobacterium nucleatum* — emerging model for O₂ scavenging coupled to butyryl-CoA metabolism

## Candidate causal edges

The following curation table contains the principal graph candidates. Taxon-specific regulatory and tolerance edges should be placed in organism-qualified subgraphs rather than asserted as universal properties of METPO:1000607.

| # | subject node (CURIE if safe) | predicate | object node (CURIE if safe) | evidence reference (DOI, year) | supporting snippet / quantitative result | scope / uncertainty |
|---|---|---|---|---|---|---|
| 1 | molecular oxygen (CHEBI:15379) | directly inactivates | pyruvate formate-lyase / PFL (EC 2.3.1.54) | Lu & Imlay, 10.1038/s41579-021-00583-y (2021) | “PFL, a glycyl-radical enzyme, is inactivated by O2 within seconds at low concentrations in vitro and in vivo.” (lu2021whenanaerobesencounter pages 6-8) | Broad mechanism for obligate anaerobes; strong review-backed edge. |
| 2 | molecular oxygen (CHEBI:15379) | directly inactivates | pyruvate:ferredoxin oxidoreductase / PFOR (EC 1.2.7.1) | Khademian & Imlay, 10.1111/mmi.14516 (2020) | “PFOR damage was unaffected by the level of superoxide or peroxide, showing that molecular oxygen itself is the culprit… The cell cannot repair PFOR.” (khademian2020doreactiveoxygen pages 1-2) | Strong primary evidence, but organism tested was *Bacteroides thetaiotaomicron*; taxon-specific exemplar for a broader mechanism. |
| 3 | molecular oxygen (CHEBI:15379) | oxidatively damages | [4Fe-4S] enzyme/cofactor-containing enzymes (GO:0051539) | Lu & Imlay, 10.1038/s41579-021-00583-y (2021) | “O2 oxidizes low-potential metal centres in anaerobic enzymes… The [4Fe-4S]2+ cluster of aconitase oxidizes to [4Fe-4S]3+ and degrades to inactive [3Fe-4S]+ with a half-time of ~30 minutes.” (lu2021whenanaerobesencounter pages 6-8) | Broad mechanistic edge; representative [4Fe-4S] example is aconitase, not all enzymes equally supported. |
| 4 | molecular oxygen (CHEBI:15379) | promotes formation of | superoxide (CHEBI:18421) | Lu & Imlay, 10.1038/s41579-021-00583-y (2021) | “molecular O2 oxidizes flavins and metal centers in redox enzymes, producing O2− and H2O2.” (lu2021whenanaerobesencounter pages 9-11) | Broad mechanism; source enzymes vary by taxon and condition. |
| 5 | molecular oxygen (CHEBI:15379) | promotes formation of | hydrogen peroxide (CHEBI:16240) | Lu & Imlay, 10.1038/s41579-021-00583-y (2021) | “molecular O2 oxidizes flavins and metal centers in redox enzymes, producing O2− and H2O2”; “B. thetaiotaomicron generates H2O2 approximately 10-fold faster than E. coli.” (lu2021whenanaerobesencounter pages 9-11) | Broad mechanism with quantitative exemplar from *B. thetaiotaomicron*. |
| 6 | superoxide (CHEBI:18421) | inactivates | fumarase (EC 4.2.1.2) | Lu & Imlay, 10.1038/s41579-021-00583-y (2021) | “endogenous superoxide (O2−) inactivating fumarase specifically.” (lu2021whenanaerobesencounter pages 22-27) | Strong mechanism; enzyme isoform/context may vary. |
| 7 | direct O2 damage to PFL/PFOR plus ROS damage to fumarase | causes | central metabolic bottleneck in pyruvate dissimilation / central metabolism | Khademian & Imlay, 10.1111/mmi.14516 (2020); Lu & Imlay, 10.1038/s41579-021-00583-y (2021) | “Pyruvate dissimilation was shown to depend upon… PFL and PFOR, that lose activity upon aeration.” (khademian2020doreactiveoxygen pages 1-2); “These inactivations create metabolic bottlenecks sufficient to prohibit growth.” (lu2021whenanaerobesencounter pages 22-27) | Composite mechanistic edge synthesized across sources; curate with note that multiple damaged targets jointly contribute. |
| 8 | central metabolic bottleneck under O2/ROS stress | causes | growth arrest / obligately anaerobic growth phenotype (METPO:1000607) | Lu & Imlay, 10.1038/s41579-021-00583-y (2021) | “The defining trait of obligate anaerobes is that oxygen blocks their growth”; oxygen-sensitive targets “prohibit growth.” (lu2021whenanaerobesencounter pages 1-3, lu2021whenanaerobesencounter pages 22-27) | Trait-level inferred integration from authoritative review; suitable high-level edge. |
| 9 | revRbr2 / reverse rubrerythrin 2 (label-only candidate; *C. difficile* CD1524) | reduces | molecular oxygen (CHEBI:15379) | Caulat et al., 10.1128/mbio.01591-24 (2024) | “revRbr2 is specific to low O2 tensions (<0.4%).” “All four purified enzymes possess O2-reductase activity in vitro.” (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5) | Taxon-specific: *Clostridioides difficile*; O2-reduction product to water is described at study level. |
| 10 | FdpA / flavodiiron protein A (label-only candidate; *C. difficile* CD1157) | reduces | molecular oxygen (CHEBI:15379) | Caulat et al., 10.1128/mbio.01591-24 (2024) | “FdpA to low and intermediate O2 tensions (0.4%–1%).” “All four purified enzymes possess O2-reductase activity in vitro.” (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5) | Taxon-specific: *C. difficile*. |
| 11 | revRbr1 / reverse rubrerythrin 1 (label-only candidate; *C. difficile* CD1474) | reduces | molecular oxygen (CHEBI:15379) | Caulat et al., 10.1128/mbio.01591-24 (2024) | “revRbr1 has a wider spectrum of activity (0.1%–4%).” (caulat2024physiologicalroleand pages 1-2) | Taxon-specific: *C. difficile*. |
| 12 | FdpF / flavodiiron protein F (label-only candidate; *C. difficile* CD1623) | reduces | molecular oxygen (CHEBI:15379) | Caulat et al., 10.1128/mbio.01591-24 (2024) | “FdpF is more specific to tensions > 4% and air”; “FdpF is identified as the fastest and most efficient O2-reducing enzyme overall.” (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 13-15) | Taxon-specific: *C. difficile*; stronger at high O2 than other reductases. |
| 13 | O2-reductase activity of FdpA/FdpF/revRbr1/revRbr2 | protects against | oxygen stress tolerance in *C. difficile* | Caulat et al., 10.1128/mbio.01591-24 (2024) | “These four enzymes have different spectra of action and protect the vegetative cells over a large range of O2 tensions.” Double revrbr mutants were “nearly unable to grow at 0.1-0.4% O2.” (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5) | Taxon-specific, strong experimental support. |
| 14 | superoxide reductase / SOR (GO:0016721 candidate) | reduces | superoxide (CHEBI:18421) | Botin et al., 10.1128/aem.00606-23 (2023) | “SORs reduce superoxide anion to H2O2.” (botin2023thetoleranceof pages 2-5) | Mechanistic enzyme-class edge; demonstrated in *Faecalibacterium* genome/phenotype context. |
| 15 | flavodiiron proteins / reverse rubrerythrins | reduce | molecular oxygen (CHEBI:15379) to water | Botin et al., 10.1128/aem.00606-23 (2023) | “FDPs and revRbrs reduce O2 to H2O.” (botin2023thetoleranceof pages 2-5) | Gene-class edge from *Faecalibacterium* study; likely broader but curate as supported enzyme-class statement. |
| 16 | rubrerythrin / peroxiredoxin / peroxidases | scavenges | hydrogen peroxide (CHEBI:16240) | Lotoux et al., 10.1128/mbio.03753-24 (2025) | “Rbr… together with the peroxiredoxin, Bcp, plays a central role in the detoxification of H2O2 and promotes the survival of C. difficile in the presence of not only H2O2 but also air or 4% O2.” (from abstract in search results) | Strong but 2025 source; taxon-specific. Consider secondary priority if restricting to ≤2024-only curation. |
| 17 | cysteine (CHEBI:17561) | limits production of | extracellular superoxide (CHEBI:18421) | Botin et al., 10.1128/aem.00606-23 (2023) | “cysteine… limited the production of extracellular O2•− and improved the survival of *Faecalibacterium longum* L2-6 under high O2 tension.” (botin2023thetoleranceof pages 1-2) | Taxon- and assay-specific; useful environmental/modifier edge. |
| 18 | cysteine (CHEBI:17561) | improves | survival under high O2 tension | Botin et al., 10.1128/aem.00606-23 (2023) | Same snippet: cysteine “improved the survival of *Faecalibacterium longum* L2-6 under high O2 tension.” (botin2023thetoleranceof pages 1-2) | Taxon- and assay-specific; likely not universal. |
| 19 | sigma factor σB (label-only candidate) | positively regulates | fdpA / fdpF / revRbr1 / revRbr2 expression | Caulat et al., 10.1128/mbio.01591-24 (2024) | “All genes (fdpA, fdpF, revrbr1, revrbr2) are controlled by sigma factor σB for general stress response.” (caulat2024physiologicalroleand pages 13-15) | Taxon-specific regulatory edge in *C. difficile*. |
| 20 | sigma factor σA (label-only candidate) | positively regulates | fdpA and revRbr2 expression | Caulat et al., 10.1128/mbio.01591-24 (2024) | “fdpA and revrbr2 also possess σA-dependent promoters.” (caulat2024physiologicalroleand pages 13-15) | Taxon-specific. |
| 21 | OseR (Spx-family regulator; label-only candidate) | represses under anaerobiosis | fdp and revrbr genes | Caulat et al., 10.1128/mbio.01591-24 (2024) | “OseR… acts as a transcriptional repressor of fdp and revrbr genes under anaerobiosis, with this repression released upon long-term 1% O2 exposure.” (caulat2024physiologicalroleand pages 13-15) | Taxon-specific and regulatory-context dependent. |
| 22 | Rex (label-only candidate) | represses | fdpF expression | Caulat et al., 10.1128/mbio.01591-24 (2024) | “fdpF is uniquely controlled by Rex, a redox regulator sensing NADH/NAD+ ratio.” (caulat2024physiologicalroleand pages 13-15) | Taxon-specific. |
| 23 | RhaR (label-only candidate) | downregulates | PFOR expression (EC 1.2.7.1) | Xie et al., 10.3389/fmicb.2024.1505218 (2024) | “RhaR overexpression reduced PFOR transcription to 0.24-fold relative to glucose-control.” (xie2024bacteroidesthetaiotaomicronenhances pages 6-8) | Taxon-specific: *B. thetaiotaomicron*; mechanism may be indirect. |
| 24 | RhaR (label-only candidate) | decreases | hydrogen peroxide / ROS production | Xie et al., 10.3389/fmicb.2024.1505218 (2024) | “H2O2 production decreased from 16.5 nM/min… to 11 nM/min…” and “RhaR overexpression reduced hydrogen peroxide production.” (xie2024bacteroidesthetaiotaomicronenhances pages 6-8, xie2024bacteroidesthetaiotaomicronenhances pages 1-2) | Taxon-specific; extracellular H2O2 used as proxy for intracellular ROS. |
| 25 | RhaR (label-only candidate) | improves | oxygen survival / oxidative stress tolerance | Xie et al., 10.3389/fmicb.2024.1505218 (2024) | “rhamnose-grown Bt-prhaR cells showed 64.8% survival after 6-hour aeration versus 22% for glucose-grown cells.” (xie2024bacteroidesthetaiotaomicronenhances pages 6-8) | Taxon-specific; depends on rhamnose condition and engineered overexpression context. |
| 26 | detoxification gene repertoire abundance (FDP/SOR/revRbr/AhpC/AhpF etc.) | positively correlates with | oxidative/O2 tolerance | Botin et al., 10.1128/aem.00606-23 (2023) | “presence and number of these detoxification systems varied greatly among faecalibacteria”; strain with multiple FDP/SOR genes had “0.15% survival at 20 min,” whereas strain with only two detoxifying genes reached “100% mortality after 5 min air exposure.” (botin2023thetoleranceof pages 1-2, botin2023thetoleranceof pages 2-5) | Correlative, strain-comparative, not single-gene causal proof; mark uncertain if curated as direct edge. |


*Table: This table compiles curation-ready candidate causal edges for obligate anaerobiosis (METPO:1000607), linking oxygen and ROS damage, metabolic bottlenecks, and known protective/regulatory mechanisms. It is designed to support TraitMech graph curation while clearly flagging taxon-specific and inferred claims.*

## Priority recommendations for `obligately_anaerobic.yaml`

### High-confidence core edges

1. **CHEBI:15379 molecular oxygen — directly_inactivates → PFL (EC 2.3.1.54).**
2. **CHEBI:15379 molecular oxygen — directly_inactivates → PFOR (EC 1.2.7.1)**, qualified to *B. thetaiotaomicron*.
3. **CHEBI:15379 molecular oxygen — promotes_formation_of → CHEBI:18421 superoxide.**
4. **CHEBI:15379 molecular oxygen — promotes_formation_of → CHEBI:16240 hydrogen peroxide.**
5. **CHEBI:18421 superoxide — inactivates → fumarase (EC 4.2.1.2).**
6. **PFL/PFOR/fumarase inactivation — disrupts → central anaerobic metabolism.**
7. **Disrupted central anaerobic metabolism — causes → oxygen-dependent growth arrest / METPO:1000607.**

Edges 6–7 are mechanistic integrations rather than single-experiment molecular reactions and should be marked as higher-level causal summaries. (khademian2020doreactiveoxygen pages 1-2, lu2021whenanaerobesencounter pages 9-11, lu2021whenanaerobesencounter pages 22-27)

### Strong taxon-qualified extension

For *C. difficile*, curate FdpA, FdpF, revRbr1, and revRbr2 as O₂-reducing protective enzymes, with their measured operating ranges preserved as edge metadata:

- revRbr2: **<0.4% O₂**;
- FdpA: **0.4–1% O₂**;
- revRbr1: **0.1–4% O₂**;
- FdpF: predominantly **>4% O₂ through air (21%)**.

Double-reverse-rubrerythrin mutants were nearly unable to grow at 0.1–0.4% O₂; revRbr1 was especially important at 1% O₂, revRbr1 and FdpF at 4%, and FdpF was the main reductase in air. These data provide unusually strong support for representing O₂ tolerance as a layered, concentration-dependent network. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5, caulat2024physiologicalroleand pages 5-7)

The accompanying regulatory subgraph can include σB activation of all four genes, σA-dependent transcription of `fdpA` and `revrbr2`, OseR repression under anaerobiosis with derepression during O₂ exposure, and Rex-dependent repression of `fdpF` according to NADH/NAD⁺ status. These claims must remain *C. difficile*-specific. (caulat2024physiologicalroleand pages 11-13, caulat2024physiologicalroleand pages 13-15)

### Conditional metabolic-modifier extension

The 2024 *B. thetaiotaomicron* study supports a provisional chain:

> rhamnose/RhaR activation → lower PFOR expression → lower measured H₂O₂/ROS → improved survival after aeration.

RhaR overexpression reduced PFOR transcription to **0.24-fold**, H₂O₂ production from **16.5 to 11 nM min⁻¹**, and was associated with **64.8% survival after six hours of aeration**, compared with **22%** for the glucose-grown comparison. Nevertheless, PFOR was not the principal intracellular ROS source, extracellular H₂O₂ was partly used as a proxy, and direct RhaR binding to the `pfor` promoter was not established. This branch should be marked **uncertain, taxon-specific, carbon-source-dependent, and partly inferred**. (xie2024bacteroidesthetaiotaomicronenhances pages 8-9, xie2024bacteroidesthetaiotaomicronenhances pages 11-12, xie2024bacteroidesthetaiotaomicronenhances pages 6-8)

## Recent developments, 2023–2024

### 2023: strain-resolved defenses in a next-generation probiotic genus

Botin and colleagues showed that oxidative tolerance in *Faecalibacterium* is strongly strain dependent and linked to heterogeneous repertoires of FDPs, rubrerythrins, reverse rubrerythrins, SORs, and alkyl peroxidases. In *F. longum* L2-6, cysteine limited extracellular superoxide and increased survival at high O₂; O₂ and H₂O₂ also induced detoxification genes in condition-specific patterns. The result is important for both trait curation and probiotic development: oxygen phenotype should not be inferred solely from genus identity or one reference genome. (botin2023thetoleranceof pages 1-2, botin2023thetoleranceof pages 2-5)

### 2024: oxygen-reductase specialization in a strict anaerobe

Caulat and colleagues established that four purified *C. difficile* enzymes all possess O₂-reductase activity but protect distinct portions of the physiologically relevant O₂ gradient. FdpF directly accepts electrons from NADH, whereas the electron donors to FdpA and the reverse rubrerythrins remain unidentified. The work replaces a simple “has/does not have oxygen defense” model with a quantitatively regulated network spanning <0.4% O₂ to air. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5)

### 2024: nutrient-dependent oxidative tolerance

Xie and colleagues found that rhamnose and RhaR alter oxidative tolerance in *B. thetaiotaomicron*, partly through reduced PFOR expression and lower H₂O₂ production. This demonstrates that oxygen sensitivity is not solely genomic; nutrient identity and metabolic flux can move the measured phenotype substantially. The incomplete regulatory mechanism means this result is best used as a contextual branch rather than part of the universal core graph. (xie2024bacteroidesthetaiotaomicronenhances pages 1-2, xie2024bacteroidesthetaiotaomicronenhances pages 9-11, xie2024bacteroidesthetaiotaomicronenhances pages 6-8)

## Current applications and real-world relevance

### Gut ecology and disease

The healthy colon maintains low luminal O₂, favoring obligate anaerobic fermenters. Inflammation and altered epithelial metabolism can increase O₂/ROS, suppressing oxygen-sensitive butyrate producers while favoring facultative or aerotolerant organisms. Mechanistically grounded oxygen-tolerance traits are therefore useful for interpreting dysbiosis, inflammatory bowel disease, pathogen expansion, and recovery of community fermentation. The large strain differences observed in *Faecalibacterium* caution against treating every obligate anaerobe as equally susceptible. (botin2023thetoleranceof pages 1-2, botin2023thetoleranceof pages 2-5)

### Next-generation probiotics and live biotherapeutics

*Faecalibacterium* and other health-associated obligate anaerobes are being developed as next-generation probiotics because of their metabolic and immunological functions. Oxygen sensitivity complicates biomass production, quality control, storage, and oral delivery, creating demand for anaerobic manufacturing, reducing excipients, lyophilization, oxygen-impermeable packaging, and encapsulation. Mechanistic markers such as FDP/SOR/rubrerythrin repertoire, inducibility, and cysteine responsiveness could aid strain selection, but genomic presence alone is not yet a validated predictor of product stability. (botin2023thetoleranceof pages 1-2, yaekob2026currentadvancementsof pages 6-6, yaekob2026currentadvancementsof pages 6-7)

### Anaerobic digestion and biogas

Industrial anaerobic digestion depends on fermentative, syntrophic, and methanogenic communities whose terminal stages are O₂-sensitive. Reactor design separates acidogenic and methanogenic niches, controls temperature and redox conditions, and increasingly uses metagenomics to identify keystone populations and optimize methane production. O₂ can inhibit methanogenic activity, although controlled microaeration may benefit selected upstream operations; therefore, process-level “anaerobic” conditions should not be conflated with the phenotype of every community member. (ostos2024ametagenomicapproach pages 9-10, ostos2024ametagenomicapproach pages 22-22)

### Cultivation and diagnostics

Clinical and research recovery of obligate anaerobes requires rapid oxygen-limited transport, pre-reduced media, anaerobic chambers or gas systems, and redox indicators. TraitMech should represent these as experimental modifiers rather than intrinsic molecular causes: a negative aerobic plate result can establish growth inhibition, whereas loss of viability during collection can produce a false-negative culture.

## Expert interpretation

The strongest expert conclusion is that **obligate anaerobiosis is an emergent metabolic vulnerability, not a simple antioxidant-enzyme deficiency**. Lu and Imlay argue that anaerobic pathways gain energetic or biosynthetic advantages from radical chemistry and low-potential cofactors, while those same features create direct O₂ targets and high ROS flux. Thus, “anaerobic excellence and oxygen sensitivity” are mechanistically linked. (lu2021whenanaerobesencounter pages 1-3, khademian2020doreactiveoxygen pages 1-2)

A second conclusion is that **oxygen tolerance is quantitative and modular**. The *C. difficile* reductases divide labor by O₂ concentration, whereas *Faecalibacterium* strains differ greatly in both gene repertoire and survival. A binary graph should therefore preserve O₂ concentration, duration, strain, medium, and endpoint as evidence qualifiers. (botin2023thetoleranceof pages 2-5, caulat2024physiologicalroleand pages 1-2)

A third conclusion is that **tolerance does not negate the trait**. An obligate anaerobe can scavenge O₂, induce stress genes, or survive temporary exposure yet remain unable to sustain growth when O₂ rises. Curating detoxification nodes as negative regulators of toxicity—rather than as evidence against METPO:1000607—best reflects current understanding. (lu2021whenanaerobesencounter pages 3-4, caulat2024physiologicalroleand pages 1-2)

## Warnings: claims not yet ready for unqualified curation

1. **Do not curate “lack of catalase/SOD causes obligate anaerobiosis” as a universal edge.** Many obligate anaerobes possess these or alternative defenses. (khademian2020doreactiveoxygen pages 1-2)
2. **Do not generalize the complete PFL–PFOR–fumarase chain to every obligate anaerobe.** Individual taxa use different central pathways and oxygen-sensitive targets.
3. **Do not equate survival with growth.** Air-survival assays establish aerotolerance, not aerobic growth capacity.
4. **Do not infer phenotype from detoxification-gene counts alone.** The 2023 *Faecalibacterium* relationship is comparative and correlational. (botin2023thetoleranceof pages 2-5)
5. **Do not universalize *C. difficile* regulators or O₂ thresholds.** FdpA/FdpF/revRbr/OseR/Rex findings are species-, strain-, medium-, and assay-specific. (caulat2024physiologicalroleand pages 11-13, caulat2024physiologicalroleand pages 13-15)
6. **Do not curate RhaR as a direct `pfor` repressor without an uncertainty flag.** Direct promoter binding was not established, and PFOR explains only part of the ROS phenotype. (xie2024bacteroidesthetaiotaomicronenhances pages 8-9, xie2024bacteroidesthetaiotaomicronenhances pages 11-12)
7. **Do not assign unverified ontology identifiers.** Use label-only nodes until taxon-specific UniProt accessions, exact GO terms, and reaction identifiers have been checked.
8. **Do not treat oxygen percentage alone as transferable across assays.** Dissolved O₂, gas-phase O₂, medium composition, reducing agents, culture geometry, exposure duration, and inoculum all affect effective dose.
9. **Do not encode host inflammation → oxygen increase → loss of obligate anaerobes as a universal direct molecular edge** without an ecological-context qualifier; it is a community-level relationship with host and spatial intermediates.

## DOI-first bibliography

1. **Caulat LC et al.** “Physiological role and complex regulation of O₂-reducing enzymes in the obligate anaerobe *Clostridioides difficile*.” *mBio* 15, October 2024. DOI: [10.1128/mbio.01591-24](https://doi.org/10.1128/mbio.01591-24). (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5)
2. **Xie S, Ma J, Lu Z.** “*Bacteroides thetaiotaomicron* enhances oxidative stress tolerance through rhamnose-dependent mechanisms.” *Frontiers in Microbiology* 15, December 2024. DOI: [10.3389/fmicb.2024.1505218](https://doi.org/10.3389/fmicb.2024.1505218). (xie2024bacteroidesthetaiotaomicronenhances pages 8-9, xie2024bacteroidesthetaiotaomicronenhances pages 6-8)
3. **Ostos I, Flórez-Pardo LM, Camargo C.** “A metagenomic approach to demystify the anaerobic digestion black box and achieve higher biogas yield: a review.” *Frontiers in Microbiology* 15, October 2024. DOI: [10.3389/fmicb.2024.1437098](https://doi.org/10.3389/fmicb.2024.1437098). (ostos2024ametagenomicapproach pages 9-10)
4. **Botin T et al.** “The tolerance of gut commensal *Faecalibacterium* to oxidative stress is strain dependent and relies on detoxifying enzymes.” *Applied and Environmental Microbiology* 89, July 2023. DOI: [10.1128/aem.00606-23](https://doi.org/10.1128/aem.00606-23). (botin2023thetoleranceof pages 1-2, botin2023thetoleranceof pages 2-5)
5. **Lu Z, Imlay JA.** “When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence.” *Nature Reviews Microbiology* 19:774–785, June 2021. DOI: [10.1038/s41579-021-00583-y](https://doi.org/10.1038/s41579-021-00583-y). (lu2021whenanaerobesencounter pages 1-3, lu2021whenanaerobesencounter pages 9-11, lu2021whenanaerobesencounter pages 6-8)
6. **Khademian M, Imlay JA.** “Do reactive oxygen species or does oxygen itself confer obligate anaerobiosis? The case of *Bacteroides thetaiotaomicron*.” *Molecular Microbiology* 114:333–347, May 2020. DOI: [10.1111/mmi.14516](https://doi.org/10.1111/mmi.14516). (khademian2020doreactiveoxygen pages 1-2)
7. **Mishra S, Imlay JA.** “An anaerobic bacterium, *Bacteroides thetaiotaomicron*, uses a consortium of enzymes to scavenge hydrogen peroxide.” *Molecular Microbiology* 90:1356–1371, December 2013. DOI: [10.1111/mmi.12438](https://doi.org/10.1111/mmi.12438).
8. **Smalley D, Rocha ER, Smith CJ.** “Aerobic-type ribonucleotide reductase in the anaerobe *Bacteroides fragilis*.” *Journal of Bacteriology* 184:895–903, February 2002. DOI: [10.1128/JB.184.4.895-903.2002](https://doi.org/10.1128/JB.184.4.895-903.2002).

## Curation conclusion

The existing 14-node/12-edge oxygen-toxicity graph has the correct core theme but should be expanded into three qualified modules: **(i) direct O₂ poisoning of radical and low-potential enzymes, (ii) endogenous ROS formation and Fe–S-enzyme damage, and (iii) concentration-dependent O₂/ROS defense and regulation**. The first two modules support the trait-level causal endpoint; the third explains variable aerotolerance without contradicting **METPO:1000607**. Organism-specific branches for *B. thetaiotaomicron*, *C. difficile*, and *Faecalibacterium* should remain explicitly qualified rather than merged into a universal obligate-anaerobe mechanism.

References

1. (lu2021whenanaerobesencounter pages 1-3): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

2. (lu2021whenanaerobesencounter pages 3-4): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

3. (khademian2020doreactiveoxygen pages 1-2): Maryam Khademian and James A. Imlay. Do reactive oxygen species or does oxygen itself confer obligate anaerobiosis? the case of <i>bacteroides thetaiotaomicron</i>. May 2020. URL: https://doi.org/10.1111/mmi.14516, doi:10.1111/mmi.14516. This article has 42 citations and is from a domain leading peer-reviewed journal.

4. (lu2021whenanaerobesencounter pages 9-11): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

5. (lu2021whenanaerobesencounter pages 6-8): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

6. (caulat2024physiologicalroleand pages 1-2): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

7. (caulat2024physiologicalroleand pages 2-5): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

8. (botin2023thetoleranceof pages 1-2): Tatiana Botin, Luis Ramirez-Chamorro, Jasmina Vidic, Philippe Langella, Isabelle Martin-Verstraete, Jean-Marc Chatel, and Sandrine Auger. The tolerance of gut commensal <i>faecalibacterium</i> to oxidative stress is strain dependent and relies on detoxifying enzymes. Applied and Environmental Microbiology, Jul 2023. URL: https://doi.org/10.1128/aem.00606-23, doi:10.1128/aem.00606-23. This article has 20 citations and is from a peer-reviewed journal.

9. (botin2023thetoleranceof pages 2-5): Tatiana Botin, Luis Ramirez-Chamorro, Jasmina Vidic, Philippe Langella, Isabelle Martin-Verstraete, Jean-Marc Chatel, and Sandrine Auger. The tolerance of gut commensal <i>faecalibacterium</i> to oxidative stress is strain dependent and relies on detoxifying enzymes. Applied and Environmental Microbiology, Jul 2023. URL: https://doi.org/10.1128/aem.00606-23, doi:10.1128/aem.00606-23. This article has 20 citations and is from a peer-reviewed journal.

10. (lu2021whenanaerobesencounter pages 17-19): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

11. (lu2021whenanaerobesencounter pages 22-27): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

12. (caulat2024physiologicalroleand pages 13-15): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

13. (xie2024bacteroidesthetaiotaomicronenhances pages 6-8): Shuo Xie, Junze Ma, and Zheng Lu. Bacteroides thetaiotaomicron enhances oxidative stress tolerance through rhamnose-dependent mechanisms. Frontiers in Microbiology, Dec 2024. URL: https://doi.org/10.3389/fmicb.2024.1505218, doi:10.3389/fmicb.2024.1505218. This article has 22 citations and is from a peer-reviewed journal.

14. (xie2024bacteroidesthetaiotaomicronenhances pages 1-2): Shuo Xie, Junze Ma, and Zheng Lu. Bacteroides thetaiotaomicron enhances oxidative stress tolerance through rhamnose-dependent mechanisms. Frontiers in Microbiology, Dec 2024. URL: https://doi.org/10.3389/fmicb.2024.1505218, doi:10.3389/fmicb.2024.1505218. This article has 22 citations and is from a peer-reviewed journal.

15. (caulat2024physiologicalroleand pages 5-7): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

16. (caulat2024physiologicalroleand pages 11-13): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

17. (xie2024bacteroidesthetaiotaomicronenhances pages 8-9): Shuo Xie, Junze Ma, and Zheng Lu. Bacteroides thetaiotaomicron enhances oxidative stress tolerance through rhamnose-dependent mechanisms. Frontiers in Microbiology, Dec 2024. URL: https://doi.org/10.3389/fmicb.2024.1505218, doi:10.3389/fmicb.2024.1505218. This article has 22 citations and is from a peer-reviewed journal.

18. (xie2024bacteroidesthetaiotaomicronenhances pages 11-12): Shuo Xie, Junze Ma, and Zheng Lu. Bacteroides thetaiotaomicron enhances oxidative stress tolerance through rhamnose-dependent mechanisms. Frontiers in Microbiology, Dec 2024. URL: https://doi.org/10.3389/fmicb.2024.1505218, doi:10.3389/fmicb.2024.1505218. This article has 22 citations and is from a peer-reviewed journal.

19. (xie2024bacteroidesthetaiotaomicronenhances pages 9-11): Shuo Xie, Junze Ma, and Zheng Lu. Bacteroides thetaiotaomicron enhances oxidative stress tolerance through rhamnose-dependent mechanisms. Frontiers in Microbiology, Dec 2024. URL: https://doi.org/10.3389/fmicb.2024.1505218, doi:10.3389/fmicb.2024.1505218. This article has 22 citations and is from a peer-reviewed journal.

20. (yaekob2026currentadvancementsof pages 6-6): Ashenafi Teklay Yaekob, Gebremedhin Gebreslassie, Etsay Mesele, and Tesfakiros Semere. Current advancements of probiotic foods and their role in sustainable food security. Food Bioengineering, 5:105-123, Feb 2026. URL: https://doi.org/10.1002/fbe2.70046, doi:10.1002/fbe2.70046. This article has 3 citations.

21. (yaekob2026currentadvancementsof pages 6-7): Ashenafi Teklay Yaekob, Gebremedhin Gebreslassie, Etsay Mesele, and Tesfakiros Semere. Current advancements of probiotic foods and their role in sustainable food security. Food Bioengineering, 5:105-123, Feb 2026. URL: https://doi.org/10.1002/fbe2.70046, doi:10.1002/fbe2.70046. This article has 3 citations.

22. (ostos2024ametagenomicapproach pages 9-10): Iván Ostos, Luz Marina Flórez-Pardo, and Carolina Camargo. A metagenomic approach to demystify the anaerobic digestion black box and achieve higher biogas yield: a review. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1437098, doi:10.3389/fmicb.2024.1437098. This article has 22 citations and is from a peer-reviewed journal.

23. (ostos2024ametagenomicapproach pages 22-22): Iván Ostos, Luz Marina Flórez-Pardo, and Carolina Camargo. A metagenomic approach to demystify the anaerobic digestion black box and achieve higher biogas yield: a review. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1437098, doi:10.3389/fmicb.2024.1437098. This article has 22 citations and is from a peer-reviewed journal.