---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T14:46:57.119646'
end_time: '2026-08-04T14:55:16.876254'
duration_seconds: 499.76
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: commensalism
  trait_identifier: traitmech:000042
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: commensalism
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A symbiosis in which the microorganism benefits from the association
    (e.g. resources, shelter, transport) while the host's fitness remains essentially
    unaffected.
  parent_traits: traitmech:000040
  synonyms: commensal
  evidence_summary: 'DOI:10.1038/s41579-021-00550-7:  (Drew et al. place commensalism
    on the parasite-mutualist continuum as a near-neutral host interaction.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai
    et al. support commensal colonization as a major class of host-associated microbial
    lifestyles.)'
  causal_graph_summary: 'commensalism_neutral_host: 11 nodes, 10 edges'
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
- **Trait label:** commensalism
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000042
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism benefits from the association (e.g. resources, shelter, transport) while the host's fitness remains essentially unaffected.
- **Parent traits:** traitmech:000040
- **Synonyms:** commensal
- **Existing evidence:** DOI:10.1038/s41579-021-00550-7:  (Drew et al. place commensalism on the parasite-mutualist continuum as a near-neutral host interaction.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support commensal colonization as a major class of host-associated microbial lifestyles.)
- **Existing causal graph summary:** commensalism_neutral_host: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **commensalism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/commensalism.yaml`.

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
- **Trait label:** commensalism
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000042
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism benefits from the association (e.g. resources, shelter, transport) while the host's fitness remains essentially unaffected.
- **Parent traits:** traitmech:000040
- **Synonyms:** commensal
- **Existing evidence:** DOI:10.1038/s41579-021-00550-7:  (Drew et al. place commensalism on the parasite-mutualist continuum as a near-neutral host interaction.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support commensal colonization as a major class of host-associated microbial lifestyles.)
- **Existing causal graph summary:** commensalism_neutral_host: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **commensalism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/commensalism.yaml`.

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


# Curation report: microbial commensalism

## Trait record and scope

- **Trait:** commensalism
- **Identifier:** **`traitmech:000042`**
- **Category / kind / status:** ECOLOGY / CLASS / REVIEWED
- **Parent:** `traitmech:000040`
- **Operational definition:** a host-associated symbiosis in which the microorganism gains resources, shelter, transport, or reproductive fitness while the host experiences no detectable fitness cost.

Drew et al. place commensals at the center of the parasite–mutualist continuum: they “benefit from the interaction with hosts, but do not cause a detectable cost.” The relevant endpoint is therefore **microbial benefit plus approximately zero host-fitness effect**, not simply residence in or on a host. Symbiosis itself is broader and does not specify effects on either partner. Outcomes may also change with environment, host state, microbial evolution, or community composition. (drew2021microbialevolutionand pages 1-2)

### Boundaries

1. **Colonization is necessary but insufficient.** Adhesion, nutrient use, stress resistance, growth, and persistence establish host association and microbial benefit, but they do not demonstrate neutral host fitness.
2. **Mutualism:** a reproducible positive host-fitness effect moves the interaction toward mutualism. Butyrate-supported epithelial metabolism, pathogen exclusion, or immune development may therefore be neighboring mechanisms rather than defining edges of strict commensalism.
3. **Parasitism/pathogenicity:** epithelial invasion, tissue damage, inflammation that lowers fitness, toxin action, or resource extraction that harms the host moves the interaction toward parasitism.
4. **Neutralism:** neither partner measurably benefits. This differs from commensalism because the microbial benefit is absent.
5. **Pathobionts:** an organism can be commensal under homeostasis yet pathogenic after immune deficiency, dysbiosis, barrier disruption, altered oxygenation, or acquisition/expression of virulence determinants. *Candida albicans* illustrates this conditionality particularly clearly. (froismartins2024candidaalbicansvirulence pages 1-2, froismartins2024candidaalbicansvirulence pages 2-4)

**Recommended graph semantics:** represent `commensalism` as a composite ecological outcome requiring two terminal observations: **increased/maintained microbial fitness** and **no detectable change in host fitness under a specified context**. Mechanisms of colonization and containment should feed into those endpoints rather than be treated as synonymous with commensalism.

## Candidate nodes

### Ecological and phenotype nodes

- `commensalism` — `traitmech:000042`
- host-associated colonization
- stable colonization / persistence
- microbial fitness in host
- no detectable host-fitness cost
- host–microbe homeostasis
- colonization resistance
- cross-feeding / trophic network
- epithelial invasion; host-cell damage; inflammation — negative boundary nodes
- mutualism, parasitism, neutralism, pathobiont transition — neighboring outcome classes

### Environmental and anatomical nodes

- gastrointestinal tract; colon; outer mucus layer; inner mucus layer; intestinal lumen; epithelium
- anoxic or hypoxic colonic environment
- dietary complex polysaccharides/fiber
- host mucin glycans
- oxygen, bile salts, antimicrobial peptides, shear stress, pH, carbon dioxide, host immune status, antibiotic exposure, and dysbiosis

The colon contains approximately **10¹¹–10¹² bacteria per gram**, compared with roughly **10³–10⁷ per gram** from proximal to distal small intestine. This gradient accompanies oxygen, bile, antimicrobial, and nutrient habitat filters. (muramatsu2024nutrientacquisitionstrategies pages 2-4)

### Chemicals and metabolites

Confident candidate groundings include:

- oxygen — **CHEBI:15379**
- pyruvate — **CHEBI:15361**
- L-fucose — **CHEBI:2181**
- N-acetylneuraminic acid — **CHEBI:17012**
- butyrate — **CHEBI:17968**
- acetate — **CHEBI:30089**
- succinate — **CHEBI:30031**
- propionate — **CHEBI:17272**
- D-glucose — **CHEBI:17634**
- D-gluconate — **CHEBI:18391**
- fumarate — **CHEBI:29806**
- ammonia — **CHEBI:16134**

Additional label-only candidates pending identifier verification are mucin glycan, starch, mannooligosaccharide, 2,7-anhydro-Neu5Ac, N-acetylmannosamine, fuculose-1-phosphate, lactaldehyde, and 1,2-propanediol.

### Host proteins, pathways, and processes

- MUC2 mucin; mucus production and polymerization
- FUT2-mediated epithelial fucosylation
- LYPD8-mediated exclusion/anti-motility activity
- epithelial tight and adherens junctions
- colonocyte β-oxidation and oxygen consumption
- IgA, IgG, IL-17, IL-22, antimicrobial peptides, neutrophils
- pattern-recognition signaling involving TLR2, NOD1/2, MyD88, and TRIF
- nutritional immunity through lipocalin-2 and calprotectin

MUC2 forms the firm inner colonic mucus layer that prevents microbial penetration; LYPD8 helps separate microbes from epithelium, while junctional proteins restrict paracellular invasion. These are host-containment mechanisms compatible with low-damage residence, but they do not independently demonstrate host neutrality. (chen2024themicrobiotaa pages 3-5)

### Microbial genes, proteins, and modules

**Bacterial carbohydrate acquisition**

- Bacteroides starch-utilization system: **SusD, SusE, SusF** (binding), **SusG** (hydrolysis), **SusC–ExbB/ExbD/TonB** (outer-membrane import), and **SusA/SusB** (periplasmic hydrolysis)
- carbohydrate-active enzymes, glycoside hydrolases, polysaccharide lyases, ABC transporters, major-facilitator transporters, and phosphotransferase systems
- sialic-acid pathway: **NanT, NanA, NanK, NanE**; in *Ruminococcus gnavus*, intramolecular trans-sialidase and **NanOx**
- fucose-utilization operon **fucOAPIKR**, including **FucP, FucI, FucK, FucA, FucO**
- glycogen synthesis and mobilization pathway
- aspartase/aspartate ammonia-lyase and fumarate respiration

**Fungal boundary mechanisms**

- *C. albicans* yeast-to-hypha transition
- **Efg1** and **Eed1** morphogenesis regulators
- adhesins/invasins **Als3, Hwp1, Hyr1, Ssa1**
- secreted aspartyl proteases
- candidalysin
- β-glucan masking and complement inactivation

Taxon CURIE candidates include *Escherichia coli* **NCBITaxon:562**, *Bacteroides thetaiotaomicron* **NCBITaxon:818**, *Bacteroides fragilis* **NCBITaxon:817**, and *Candida albicans* **NCBITaxon:5476**. Strain-level CURIEs should be added only after checking the exact experimental strain.

## Candidate causal edges

The compact table below summarizes the principal graph candidates. The detailed evidence notes following it explain how each should be curated.

| subject | predicate | object | system/taxon | evidence strength | caveat |
|---|---|---|---|---|---|
| Host mucus/mucin glycans | serve as nutrient source for | gut microbiota via glycan degradation and cross-feeding | Mammalian gut microbiota; mucus layer | Strong review synthesis with mechanistic detail (doranga2024nutritionofescherichia pages 2-4, muramatsu2024nutrientacquisitionstrategies pages 6-7) | Supports microbial benefit/colonization, not by itself host-fitness neutrality; some mucus degradation can become pathogenic if barrier is breached (doranga2024nutritionofescherichia pages 2-4) |
| MUC2 mucin glycans | provide attachment sites for | bacterial adhesins | Mammalian colon microbiota | Strong review synthesis (doranga2024nutritionofescherichia pages 2-4) | Attachment/colonization edge only; adhesion to epithelium should not be inferred for commensal E. coli, which is described as dispersed in mucus and not attached to epithelium (doranga2024nutritionofescherichia pages 2-4) |
| SusD/SusE/SusF + SusG + SusC/SusA/SusB (SUS) | enable | starch capture, degradation, import, and fermentation to acetate/succinate/propionate | Bacteroides spp. in large intestine | Strong mechanistic review (muramatsu2024nutrientacquisitionstrategies pages 2-4) | Establishes carbohydrate utilization supporting colonization/homeostasis; host outcome may be neutral or beneficial depending on context |
| fucOAPIKR operon / FucP-FucI-FucK-FucA-FucO pathway | enables | L-fucose utilization | Commensal E. coli in mammalian intestine | Strong, with mutant evidence (muramatsu2024nutrientacquisitionstrategies pages 6-7) | Directly supports maintenance of colonization, not neutrality |
| Loss of fucK or fucAO | decreases | stable intestinal colonization over time | Murine intestine; E. coli mutants | Strong experimental evidence (muramatsu2024nutrientacquisitionstrategies pages 6-7) | Assay/model-specific; supports persistence rather than commensal host outcome |
| Commensal bacteria | induce | host Fut2 expression and epithelial fucosylation | Murine intestine | Moderate to strong (muramatsu2024nutrientacquisitionstrategies pages 6-7, chen2024themicrobiotaa pages 3-5) | This host-conditioning edge may reflect mutualistic/homeostatic interactions rather than strictly neutral commensalism |
| Butyrate | induces | colonocyte β-oxidation | Large intestine; host epithelium | Strong review synthesis (muramatsu2024nutrientacquisitionstrategies pages 2-4) | More indicative of beneficial host-microbiota homeostasis than strict neutrality |
| Colonocyte β-oxidation | creates | epithelial hypoxia/anoxic lumen | Large intestine | Strong review synthesis (muramatsu2024nutrientacquisitionstrategies pages 2-4) | Host environmental shaping edge, not microbe-intrinsic trait |
| Epithelial hypoxia/anoxic lumen | facilitates colonization by | obligate anaerobic Firmicutes and Bacteroides | Large intestine microbiota | Strong review synthesis (muramatsu2024nutrientacquisitionstrategies pages 2-4) | Supports habitat preference and colonization, not direct neutrality |
| MUC2 inner mucus layer | prevents penetration of | microorganisms to colonic epithelium | Mammalian large intestine | Strong review synthesis (chen2024themicrobiotaa pages 3-5) | Host containment mechanism; compatible with commensalism because it separates microbes from tissue rather than indicating benefit |
| Lypd8 | separates/restrains | intestinal microbes from the epithelium | Mammalian colon | Strong review synthesis (chen2024themicrobiotaa pages 3-5, wilde2024hostcontrolof pages 15-17) | Host containment edge; not specific to a commensal taxon |
| IgA | restrains | C. albicans hyphae / fungal virulence | Oral and gastrointestinal mucosa | Moderate to strong review evidence (froismartins2024candidaalbicansvirulence pages 2-4) | Fungal-specific and immunity-dependent; demonstrates host restraint of a pathobiont boundary case |
| IL-17 and IL-22 | prevent excessive growth of | C. albicans on epithelia via antimicrobial programs | Mucosal barriers | Moderate to strong review evidence (froismartins2024candidaalbicansvirulence pages 2-4) | Host-protective containment, not proof of neutral host effect |
| Yeast morphology / lack of filamentation and invasion | is associated with | C. albicans commensalism | Human mucosal C. albicans | Strong review synthesis (froismartins2024candidaalbicansvirulence pages 1-2, froismartins2024candidaalbicansvirulence pages 2-4) | Boundary marker rather than universal mechanism; some virulence traits can still support colonization |
| EFG1 induction | coordinates | yeast-to-hyphae transition | C. albicans | Strong mechanistic review (froismartins2024candidaalbicansvirulence pages 2-4) | Hyphal transition is a pathogenic-boundary edge, generally arguing against strict commensalism when sustained |
| Hyphae-associated candidalysin | causes | host membrane damage, pore formation, inflammation, and tissue invasion | C. albicans in susceptible hosts | Strong mechanistic review (froismartins2024candidaalbicansvirulence pages 2-4) | Negative boundary case; should not be curated as a positive commensalism mechanism except as a transition-away-from-commensalism warning |
| F18 18-strain commensal consortium | regulates | gluconate availability | Healthy-human-derived commensals in mouse gut | Strong 2024 Nature evidence (furuichi2024commensalconsortiadecolonize pages 1-2) | Therapeutic ecological-control result; demonstrates colonization resistance and inflammation reduction, trending toward beneficial/mutualistic host impact rather than neutrality |
| Gluconate regulation by F18-mix | suppresses | Enterobacteriaceae intestinal colonization/outgrowth | Mouse intestine; Klebsiella/Escherichia pathobionts | Strong 2024 Nature evidence (furuichi2024commensalconsortiadecolonize pages 1-2, furuichi2024commensalconsortiadecolonize pages 3-4) | Consortium-level ecological effect, not a generic single-microbe commensalism edge |
| Genes important for host colonization identified by TnSeq | comprise about | 5.7% of genome on average across 58 datasets | Diverse host-associated bacteria | Moderate quantitative review evidence (torres2024sheddinglighton pages 9-10) | Global statistic for colonization fitness only; not specific evidence of commensal host neutrality |
| Commensal E. coli in mucus layer | requires growth roughly every | 2 h to maintain ~10^8 CFU/g feces | Mammalian intestine | Moderate quantitative review evidence (doranga2024nutritionofescherichia pages 2-4) | Population-maintenance statistic; supports niche persistence, not neutrality |


*Table: This table summarizes the strongest curation-ready causal edges relevant to microbial commensalism, emphasizing which mechanisms directly support colonization or host containment. It also flags boundary cases where evidence points toward mutualism or pathogenic transition rather than strict host-neutral commensalism.*

### Detailed curation triples and evidence

| # | Subject–predicate–object | Reference and supporting snippet | Curation note |
|---|---|---|---|
| 1 | host mucin glycans **provide nutrient source for** gut microorganisms | Doranga et al. (2024): “Mucosal glycans…serve as a source of nutrients”; non-degraders rely on cross-feeding. DOI: [10.1128/ecosalplus.esp-0006-2023](https://doi.org/10.1128/ecosalplus.esp-0006-2023). (doranga2024nutritionofescherichia pages 2-4) | Strong colonization/resource edge; does not prove neutral host fitness. |
| 2 | mucin glycans **provide attachment sites for** bacterial adhesins | “Mucosal glycans, besides serving as attachment sites for bacterial adhesins…” (doranga2024nutritionofescherichia pages 2-4) | Strong general attachment edge. Do not infer epithelial attachment: commensal *E. coli* is reported dispersed in mucus but not attached to epithelium. |
| 3 | SusD/SusE/SusF → SusG → SusC/TonB → SusA/SusB **enable** starch capture, hydrolysis, import, and fermentation | Muramatsu & Winter (2024) describe sequential binding, SusG cleavage, SusC import, periplasmic hydrolysis, and fermentation to acetate, succinate, and propionate. DOI: [10.1016/j.chom.2024.05.011](https://doi.org/10.1016/j.chom.2024.05.011), published June 2024. (muramatsu2024nutrientacquisitionstrategies pages 2-4) | Mechanistically strong and suitable as a taxon-specific nutrient-acquisition module. Host outcome remains unspecified. |
| 4 | *R. torques* extracellular CAZymes **release** mucin oligosaccharides **that support growth of** *B. thetaiotaomicron* | Cross-feeding of *R. torques*-generated oligosaccharides facilitates *B. thetaiotaomicron* growth on mucin. (muramatsu2024nutrientacquisitionstrategies pages 6-7) | Strong community-level cross-feeding edge; source calls related examples mutualistic between bacteria, so it is not itself host–microbe commensalism. |
| 5 | NanT/NanA/NanK/NanE **convert** Neu5Ac **into intermediates entering** glycolysis | Neu5Ac is transported by NanT; NanA produces pyruvate and ManNAc; NanK and NanE channel it toward fructose-6-phosphate. (muramatsu2024nutrientacquisitionstrategies pages 6-7) | Suitable pathway edges for sialic-acid utilization. Evidence supports microbial nutrition, not neutral host impact. |
| 6 | fucOAPIKR pathway **enables** L-fucose utilization **required for** stable *E. coli* persistence | *fucK* and *fucAO* mutants initially colonized like wild type but failed to maintain colonization over time. (muramatsu2024nutrientacquisitionstrategies pages 6-7) | Strong murine, *E. coli*-specific persistence edge. Mark model-specific. |
| 7 | commensal bacteria **induce** FUT2 expression/fucosylation **creating** a fucose-rich niche | Commensals induce host Fut2, “leading to a fucose-rich niche” supporting fucotrophic bacteria. (muramatsu2024nutrientacquisitionstrategies pages 6-7) | Bidirectional host-conditioning edge. Because host glycans are protected and pathogen defense may improve, this may lie toward mutualism rather than strict neutrality. |
| 8 | microbial butyrate **induces** colonocyte β-oxidation **which lowers** oxygen diffusion | Colonocytes consume oxygen during β-oxidation; butyrate instructs this metabolism, creating a feedback loop. (muramatsu2024nutrientacquisitionstrategies pages 2-4) | Strong homeostatic mechanism, but likely host-beneficial; use as contextual support rather than a defining commensalism edge. |
| 9 | epithelial oxygen consumption **creates** an anoxic lumen **facilitating** obligate anaerobe colonization | Host oxygen consumption creates an anoxic environment facilitating anaerobic Firmicutes and *Bacteroides*. (muramatsu2024nutrientacquisitionstrategies pages 2-4) | Strong host-environment-to-colonization chain. Not microbe-intrinsic and not direct neutrality evidence. |
| 10 | MUC2 inner mucus layer **prevents** microbial contact with colonic epithelium | MUC2 “effectively prevents microorganisms from penetrating the colonic epithelium.” (chen2024themicrobiotaa pages 3-5) | Strong containment edge that helps explain non-damaging residence. |
| 11 | LYPD8 **restricts/separates** motile microbes from epithelium | LYPD8 efficiently separates intestinal microbes and epithelium; a complementary Science review describes flagellar binding and reduced breach. DOI: [10.1126/science.adi3338](https://doi.org/10.1126/science.adi3338), July 2024. (wilde2024hostcontrolof pages 15-17, chen2024themicrobiotaa pages 3-5) | Good host-control edge; not taxon-specific. |
| 12 | IL-17/IL-22 **prevent** excessive epithelial growth of *C. albicans* | These cytokines restrain fungal growth, probably through epithelial antimicrobial peptides. DOI: [10.1007/s40588-024-00235-8](https://doi.org/10.1007/s40588-024-00235-8), published 1 October 2024. (froismartins2024candidaalbicansvirulence pages 2-4) | Strong fungal homeostasis edge, but review-level and pathway wording is partly presumptive. |
| 13 | *C. albicans*-specific IgA **binds** hyphae **and restrains** fungal virulence | The review states that specific IgA binds hyphae and thereby restrains virulence. (froismartins2024candidaalbicansvirulence pages 2-4) | Useful host-control edge; fungal and mucosal-site specific. |
| 14 | yeast morphology/lack of filamentation and invasion **is associated with** *C. albicans* commensal state | Commensalism is generally associated with lack of filamentation, epithelial invasion, and host-cell damage. (froismartins2024candidaalbicansvirulence pages 1-2) | Curate as an association or state marker, not a universal causal mechanism. |
| 15 | EFG1 induction **drives** yeast-to-hypha transition; hypha-associated factors **increase** invasion and damage | Efg1 coordinates morphotype switching; Als3/Hwp1/Hyr1/Ssa1 support adhesion/invasion, and candidalysin causes membrane pores and calcium influx. (froismartins2024candidaalbicansvirulence pages 2-4) | Strong **transition-away-from-commensalism** boundary. Do not curate candidalysin as a generic positive commensal mechanism. |
| 16 | immune deficiency or dysbiosis **permits** *C. albicans* overgrowth/invasion **leading to** disease | Fungal disease occurs especially in immunodeficient individuals; antibiotic-associated dysbiosis predisposes to candidiasis. (froismartins2024candidaalbicansvirulence pages 1-2, froismartins2024candidaalbicansvirulence pages 2-4) | Strong context edge but broad; encode environmental qualifiers. |
| 17 | F18 18-strain consortium **regulates** gluconate availability **suppressing** Enterobacteriaceae | Furuichi et al. report an 18-strain healthy-human consortium that controlled niches through gluconate availability, restored colonization resistance, and reduced *Klebsiella*/*Escherichia*-driven inflammation in mice. DOI: [10.1038/s41586-024-07960-6](https://doi.org/10.1038/s41586-024-07960-6), published 18 September 2024. (furuichi2024commensalconsortiadecolonize pages 1-2) | Strong consortium-level application edge. Reduced inflammation is host-beneficial, so this is closer to mutualistic/therapeutic function than strict neutrality. The effect persisted in several immune-deficient mouse backgrounds, supporting ecological rather than canonical immune control. (furuichi2024commensalconsortiadecolonize pages 3-4) |
| 18 | glycogen storage/mobilization **supports** *E. coli* colonization during nutrient limitation | Glycogen-pathway knockouts had colonization defects; 2% gluconate in drinking water rescued them. (doranga2024nutritionofescherichia pages 6-8) | Strong experimental nutrient-buffering edge. Exact glycogen genes and original DOI should be recovered before gene-level YAML curation. |

## Recent research, methods, and applications

### Host control as an “ecosystem on a leash”

A 2024 *Science* review argues that microbiomes reflect continuing tension between host control and rapidly evolving symbionts. Mucus provisioning, oxygen restriction, barrier function, transit, and genotype-specific IgA can select microbial location and metabolism while constraining epithelial damage. This framing is highly relevant to commensalism: an apparently neutral interaction may be neutral **because host control suppresses its costs**, not because the microorganism lacks harmful potential. (wilde2024hostcontrolof pages 15-17, wilde2024hostcontrolof pages 21-24)

### Genome-scale discovery

TnSeq measures mutant abundance before and after host selection, thereby identifying loci whose disruption reduces colonization fitness. Across **58 host-colonization datasets**, an average **5.7% of the genome** contributed a fitness benefit: **7.2%** in animal-host studies and **3.8%** in plant-host studies. The proportion was similar between detrimental and non-detrimental interactions, showing that colonization-gene catalogs alone cannot classify an interaction as commensal. Comparability is limited by media, bottlenecks, cut-offs, and taxonomic bias toward genetically tractable Pseudomonadota. (torres2024sheddinglighton pages 3-5, torres2024sheddinglighton pages 9-10)

### Live biotherapeutics and ecological control

The F18 consortium demonstrates a 2024 real-world translational direction: rationally selected commensals can manipulate nutrient niches rather than kill pathogens directly. The study positions defined consortia as safer and more reproducible alternatives to variable fecal microbiota transplantation, although the evidence remains preclinical and mouse-based. (furuichi2024commensalconsortiadecolonize pages 1-2)

*E. coli* Nissle 1917 is already marketed as Mutaflor and has been used for gastrointestinal disease; the reviewed literature describes use of seven intestinal carbon sources. *E. coli* HS can reach approximately **10¹⁰ CFU/g feces without disease** and uses six identified carbon sources during colonization. These are useful organism-level exemplars, but absence of overt disease is not equivalent to a measured zero effect on lifetime host fitness. (doranga2024nutritionofescherichia pages 6-8)

### Quantitative niche observations

- Stable *E. coli* populations of about **10⁸ CFU/g feces** require division roughly every **2 hours**; strain BJ4 exhibited estimated mucus-layer generation times of **40–80 minutes**, increasing to **116–130 minutes** after conventionalization. (doranga2024nutritionofescherichia pages 2-4)
- More than **90% of free amino acids** measured across the proximal small intestine and colon were absorbed in the small intestine, illustrating why large-intestinal microbes depend heavily on fiber, mucus, cross-feeding, and endogenous secretions. (doranga2024nutritionofescherichia pages 2-4)
- Conventional germ-free mammals were reported in the foundational synthesis to require approximately **one-third more food** to maintain the same body mass, an observation demonstrating host benefit from microbiota generally—but therefore supporting mutualism rather than strict commensal neutrality. (mcfallngai2013animalsina pages 3-4)
- The *C. albicans* review reports roughly **1 billion fungal infections and ~4 million associated deaths annually**, with about one-quarter of fatal fungal infections caused by *Candida* spp. These values underscore the clinical importance of context-dependent transition from colonization to disease; they are not commensalism prevalence estimates. (froismartins2024candidaalbicansvirulence pages 1-2)

## Recommended minimal graph architecture

A conservative core for `commensalism_neutral_host` should be:

1. **host-associated niche** → `provides_resources_or_shelter_for` → **microorganism**
2. **microbial nutrient-acquisition / adhesion / stress-tolerance module** → `increases` → **microbial colonization fitness**
3. **host barrier and immune containment** → `decreases` → **epithelial contact / invasion / host damage**
4. **microbial colonization fitness** → `constitutes_microbe_benefit_in` → **`traitmech:000042`**
5. **host-fitness assay: no detectable effect** → `supports_classification_as` → **`traitmech:000042`**
6. **epithelial invasion or measurable damage** → `shifts_interaction_toward` → **parasitism/pathogenicity**
7. **measurable host-fitness benefit** → `shifts_interaction_toward` → **mutualism**

For implementation, store context qualifiers on every terminal assertion: host taxon, microbial strain, anatomical site, diet, community state, immune state, observation period, comparator, and fitness endpoint.

## Warnings: claims not yet suitable for TraitMech curation

1. **Do not assert “colonization causes commensalism.”** Colonization genes occur in pathogens, mutualists, and commensals; the TnSeq synthesis found similar genome fractions supporting detrimental and non-detrimental host interactions. (torres2024sheddinglighton pages 9-10)
2. **Do not infer host neutrality from “healthy donor,” “normal microbiota,” or absence of diagnosed disease.** Strict commensalism requires a powered host-fitness comparison with an explicit equivalence or non-inferiority margin.
3. **Do not curate SCFA production, immune maturation, or colonization resistance as strictly neutral.** These often confer host benefit and therefore support mutualism or homeostasis.
4. **Do not universalize taxon-specific modules.** SUS is characteristic of particular Bacteroides systems; fucose-mutant evidence is *E. coli*/mouse-specific; Candida morphogenesis is fungal and tissue-dependent.
5. **Do not treat all mucus degradation as benign.** Cross-feeding in the outer mucus layer can support stable communities, whereas Pic-mediated MUC2 degradation by enteroaggregative *E. coli* disrupts the barrier and promotes epithelial colonization—a virulence boundary. (doranga2024nutritionofescherichia pages 2-4)
6. **Do not equate gene expression with causal fitness.** TnSeq and RNA-seq are complementary because expression and mutant fitness correlate imperfectly; direct knockout, complementation, metabolite rescue, and host-fitness measurements are preferable. (torres2024sheddinglighton pages 3-5)
7. **Do not assign unverified CURIEs.** Retain label-only nodes for strain-specific proteins, complexes, and ecological processes until UniProt, GO, Rhea, MetaCyc, or KEGG records have been checked.
8. **Do not curate candidalysin as a positive commensalism determinant without primary evidence.** Although transient virulence-factor expression may help establish colonization and protective immunity, candidalysin directly damages host membranes; its safest placement is a context-dependent boundary or transition edge. (froismartins2024candidaalbicansvirulence pages 1-2, froismartins2024candidaalbicansvirulence pages 2-4)
9. **Neutrality is time-scale dependent.** Short assays may miss delayed immune, reproductive, survival, or transmission effects. Drew et al. emphasize that interactions can move along the continuum with ecological and evolutionary change. (drew2021microbialevolutionand pages 1-2, drew2021microbialevolutionand pages 3-4)

## DOI-first bibliography

1. Wilde J, Slack E, Foster KR. **Host control of the microbiome: mechanisms, evolution, and disease.** *Science*. Published July 2024. DOI: [10.1126/science.adi3338](https://doi.org/10.1126/science.adi3338). (wilde2024hostcontrolof pages 15-17, wilde2024hostcontrolof pages 21-24)
2. Furuichi M, et al. **Commensal consortia decolonize Enterobacteriaceae via ecological control.** *Nature*. Published 18 September 2024. DOI: [10.1038/s41586-024-07960-6](https://doi.org/10.1038/s41586-024-07960-6). (furuichi2024commensalconsortiadecolonize pages 3-4, furuichi2024commensalconsortiadecolonize pages 1-2)
3. Muramatsu MK, Winter SE. **Nutrient acquisition strategies by gut microbes.** *Cell Host & Microbe*. Published June 2024. DOI: [10.1016/j.chom.2024.05.011](https://doi.org/10.1016/j.chom.2024.05.011). (muramatsu2024nutrientacquisitionstrategies pages 6-7, muramatsu2024nutrientacquisitionstrategies pages 2-4)
4. Torres M, Paszti S, Eberl L. **Shedding light on bacteria–host interactions with the aid of TnSeq approaches.** *mBio*. Published June 2024. DOI: [10.1128/mbio.00390-24](https://doi.org/10.1128/mbio.00390-24). (torres2024sheddinglighton pages 3-5, torres2024sheddinglighton pages 9-10)
5. Doranga S, Krogfelt KA, Cohen PS, Conway T. **Nutrition of Escherichia coli within the intestinal microbiome.** *EcoSal Plus*. Published December 2024. DOI: [10.1128/ecosalplus.esp-0006-2023](https://doi.org/10.1128/ecosalplus.esp-0006-2023). (doranga2024nutritionofescherichia pages 2-4, doranga2024nutritionofescherichia pages 6-8)
6. Fróis-Martins R, Lagler J, LeibundGut-Landmann S. **Candida albicans Virulence Traits in Commensalism and Disease.** *Current Clinical Microbiology Reports*. Published online 1 October 2024. DOI: [10.1007/s40588-024-00235-8](https://doi.org/10.1007/s40588-024-00235-8). (froismartins2024candidaalbicansvirulence pages 1-2, froismartins2024candidaalbicansvirulence pages 2-4)
7. Chen Y, Xiao L, Zhou M, Zhang H. **The microbiota: a crucial mediator in gut homeostasis and colonization resistance.** *Frontiers in Microbiology*. Published August 2024. DOI: [10.3389/fmicb.2024.1417864](https://doi.org/10.3389/fmicb.2024.1417864). (chen2024themicrobiotaa pages 3-5)
8. Drew GC, Stevens EJ, King KC. **Microbial evolution and transitions along the parasite–mutualist continuum.** *Nature Reviews Microbiology*. Published April 2021; issue October 2021. DOI: [10.1038/s41579-021-00550-7](https://doi.org/10.1038/s41579-021-00550-7). (drew2021microbialevolutionand pages 1-2, drew2021microbialevolutionand pages 3-4)
9. McFall-Ngai M, et al. **Animals in a bacterial world, a new imperative for the life sciences.** *PNAS*. Published February 2013. DOI: [10.1073/pnas.1218525110](https://doi.org/10.1073/pnas.1218525110). (mcfallngai2013animalsina pages 3-4)

## Overall assessment

A TraitMech graph for commensalism is feasible, but the best-supported mechanistic literature primarily explains **how microorganisms persist** and **how hosts contain them**, not how host fitness is proven to be exactly neutral. The strongest defensible graph therefore combines resource acquisition and colonization modules with host barrier/immune restraint, then requires an explicit assay-derived “no detectable host-fitness cost” terminal node. Edges involving pathogen exclusion, butyrate-mediated epithelial metabolism, or immune development should be tagged as neighboring mutualistic/homeostatic mechanisms; invasion, candidalysin, barrier degradation, and dysbiosis-driven overgrowth should be represented as context-dependent transitions away from `traitmech:000042`.

References

1. (drew2021microbialevolutionand pages 1-2): Georgia C. Drew, Emily J. Stevens, and Kayla C. King. Microbial evolution and transitions along the parasite–mutualist continuum. Nature Reviews. Microbiology, 19:623-638, Apr 2021. URL: https://doi.org/10.1038/s41579-021-00550-7, doi:10.1038/s41579-021-00550-7. This article has 405 citations.

2. (froismartins2024candidaalbicansvirulence pages 1-2): Ricardo Fróis-Martins, Julia Lagler, and Salomé LeibundGut-Landmann. Candida albicans virulence traits in commensalism and disease. Current Clinical Microbiology Reports, 11:231-240, Oct 2024. URL: https://doi.org/10.1007/s40588-024-00235-8, doi:10.1007/s40588-024-00235-8. This article has 21 citations.

3. (froismartins2024candidaalbicansvirulence pages 2-4): Ricardo Fróis-Martins, Julia Lagler, and Salomé LeibundGut-Landmann. Candida albicans virulence traits in commensalism and disease. Current Clinical Microbiology Reports, 11:231-240, Oct 2024. URL: https://doi.org/10.1007/s40588-024-00235-8, doi:10.1007/s40588-024-00235-8. This article has 21 citations.

4. (muramatsu2024nutrientacquisitionstrategies pages 2-4): Matthew K. Muramatsu and Sebastian E. Winter. Nutrient acquisition strategies by gut microbes. Cell host & microbe, 32 6:863-874, Jun 2024. URL: https://doi.org/10.1016/j.chom.2024.05.011, doi:10.1016/j.chom.2024.05.011. This article has 49 citations and is from a highest quality peer-reviewed journal.

5. (chen2024themicrobiotaa pages 3-5): Yiding Chen, Ling Xiao, Min Zhou, and Hu Zhang. The microbiota: a crucial mediator in gut homeostasis and colonization resistance. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1417864, doi:10.3389/fmicb.2024.1417864. This article has 75 citations and is from a peer-reviewed journal.

6. (doranga2024nutritionofescherichia pages 2-4): Sudhir Doranga, Karen A. Krogfelt, Paul S. Cohen, and Tyrrell Conway. Nutrition of <i>escherichia coli</i> within the intestinal microbiome. Dec 2024. URL: https://doi.org/10.1128/ecosalplus.esp-0006-2023, doi:10.1128/ecosalplus.esp-0006-2023. This article has 23 citations.

7. (muramatsu2024nutrientacquisitionstrategies pages 6-7): Matthew K. Muramatsu and Sebastian E. Winter. Nutrient acquisition strategies by gut microbes. Cell host & microbe, 32 6:863-874, Jun 2024. URL: https://doi.org/10.1016/j.chom.2024.05.011, doi:10.1016/j.chom.2024.05.011. This article has 49 citations and is from a highest quality peer-reviewed journal.

8. (wilde2024hostcontrolof pages 15-17): Jacob Wilde, Emma Slack, and Kevin R. Foster. Host control of the microbiome: mechanisms, evolution, and disease. Science, Jul 2024. URL: https://doi.org/10.1126/science.adi3338, doi:10.1126/science.adi3338. This article has 169 citations and is from a highest quality peer-reviewed journal.

9. (furuichi2024commensalconsortiadecolonize pages 1-2): Munehiro Furuichi, Takaaki Kawaguchi, Marie-Madlen Pust, Keiko Yasuma-Mitobe, Damian R. Plichta, Naomi Hasegawa, Takashi Ohya, Shakti K. Bhattarai, Satoshi Sasajima, Yoshimasa Aoto, Timur Tuganbaev, Mizuki Yaginuma, Masahiro Ueda, Nobuyuki Okahashi, Kimiko Amafuji, Yuko Kiridoshi, Kayoko Sugita, Martin Stražar, Julian Avila-Pacheco, Kerry Pierce, Clary B. Clish, Ashwin N. Skelly, Masahira Hattori, Nobuhiro Nakamoto, Silvia Caballero, Jason M. Norman, Bernat Olle, Takeshi Tanoue, Wataru Suda, Makoto Arita, Vanni Bucci, Koji Atarashi, Ramnik J. Xavier, and Kenya Honda. Commensal consortia decolonize enterobacteriaceae via ecological control. Nature, 633:878-886, Sep 2024. URL: https://doi.org/10.1038/s41586-024-07960-6, doi:10.1038/s41586-024-07960-6. This article has 134 citations and is from a highest quality peer-reviewed journal.

10. (furuichi2024commensalconsortiadecolonize pages 3-4): Munehiro Furuichi, Takaaki Kawaguchi, Marie-Madlen Pust, Keiko Yasuma-Mitobe, Damian R. Plichta, Naomi Hasegawa, Takashi Ohya, Shakti K. Bhattarai, Satoshi Sasajima, Yoshimasa Aoto, Timur Tuganbaev, Mizuki Yaginuma, Masahiro Ueda, Nobuyuki Okahashi, Kimiko Amafuji, Yuko Kiridoshi, Kayoko Sugita, Martin Stražar, Julian Avila-Pacheco, Kerry Pierce, Clary B. Clish, Ashwin N. Skelly, Masahira Hattori, Nobuhiro Nakamoto, Silvia Caballero, Jason M. Norman, Bernat Olle, Takeshi Tanoue, Wataru Suda, Makoto Arita, Vanni Bucci, Koji Atarashi, Ramnik J. Xavier, and Kenya Honda. Commensal consortia decolonize enterobacteriaceae via ecological control. Nature, 633:878-886, Sep 2024. URL: https://doi.org/10.1038/s41586-024-07960-6, doi:10.1038/s41586-024-07960-6. This article has 134 citations and is from a highest quality peer-reviewed journal.

11. (torres2024sheddinglighton pages 9-10): Marta Torres, Sarah Paszti, and Leo Eberl. Shedding light on bacteria–host interactions with the aid of tnseq approaches. Jun 2024. URL: https://doi.org/10.1128/mbio.00390-24, doi:10.1128/mbio.00390-24. This article has 23 citations and is from a domain leading peer-reviewed journal.

12. (doranga2024nutritionofescherichia pages 6-8): Sudhir Doranga, Karen A. Krogfelt, Paul S. Cohen, and Tyrrell Conway. Nutrition of <i>escherichia coli</i> within the intestinal microbiome. Dec 2024. URL: https://doi.org/10.1128/ecosalplus.esp-0006-2023, doi:10.1128/ecosalplus.esp-0006-2023. This article has 23 citations.

13. (wilde2024hostcontrolof pages 21-24): Jacob Wilde, Emma Slack, and Kevin R. Foster. Host control of the microbiome: mechanisms, evolution, and disease. Science, Jul 2024. URL: https://doi.org/10.1126/science.adi3338, doi:10.1126/science.adi3338. This article has 169 citations and is from a highest quality peer-reviewed journal.

14. (torres2024sheddinglighton pages 3-5): Marta Torres, Sarah Paszti, and Leo Eberl. Shedding light on bacteria–host interactions with the aid of tnseq approaches. Jun 2024. URL: https://doi.org/10.1128/mbio.00390-24, doi:10.1128/mbio.00390-24. This article has 23 citations and is from a domain leading peer-reviewed journal.

15. (mcfallngai2013animalsina pages 3-4): Margaret McFall-Ngai, Michael G. Hadfield, Thomas C. G. Bosch, Hannah V. Carey, Tomislav Domazet-Lošo, Angela E. Douglas, Nicole Dubilier, Gerard Eberl, Tadashi Fukami, Scott F. Gilbert, Ute Hentschel, Nicole King, Staffan Kjelleberg, Andrew H. Knoll, Natacha Kremer, Sarkis K. Mazmanian, Jessica L. Metcalf, Kenneth Nealson, Naomi E. Pierce, John F. Rawls, Ann Reid, Edward G. Ruby, Mary Rumpho, Jon G. Sanders, Diethard Tautz, and Jennifer J. Wernegreen. Animals in a bacterial world, a new imperative for the life sciences. Proceedings of the National Academy of Sciences, 110:3229-3236, Feb 2013. URL: https://doi.org/10.1073/pnas.1218525110, doi:10.1073/pnas.1218525110. This article has 3293 citations and is from a highest quality peer-reviewed journal.

16. (drew2021microbialevolutionand pages 3-4): Georgia C. Drew, Emily J. Stevens, and Kayla C. King. Microbial evolution and transitions along the parasite–mutualist continuum. Nature Reviews. Microbiology, 19:623-638, Apr 2021. URL: https://doi.org/10.1038/s41579-021-00550-7, doi:10.1038/s41579-021-00550-7. This article has 405 citations.