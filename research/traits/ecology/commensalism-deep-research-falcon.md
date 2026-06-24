---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:01:53.127490'
end_time: '2026-06-17T20:18:25.260265'
duration_seconds: 992.13
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
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
  causal_graph_summary: 'commensalism_neutral_host: 3 nodes, 2 edges'
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
- **Trait label:** commensalism
- **METPO identifier:** traitmech:000042
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism benefits from the association (e.g. resources, shelter, transport) while the host's fitness remains essentially unaffected.
- **Parent traits:** traitmech:000040
- **Synonyms:** commensal
- **Existing evidence:** DOI:10.1038/s41579-021-00550-7:  (Drew et al. place commensalism on the parasite-mutualist continuum as a near-neutral host interaction.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support commensal colonization as a major class of host-associated microbial lifestyles.)
- **Existing causal graph summary:** commensalism_neutral_host: 3 nodes, 2 edges

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
- **METPO identifier:** traitmech:000042
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism benefits from the association (e.g. resources, shelter, transport) while the host's fitness remains essentially unaffected.
- **Parent traits:** traitmech:000040
- **Synonyms:** commensal
- **Existing evidence:** DOI:10.1038/s41579-021-00550-7:  (Drew et al. place commensalism on the parasite-mutualist continuum as a near-neutral host interaction.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support commensal colonization as a major class of host-associated microbial lifestyles.)
- **Existing causal graph summary:** commensalism_neutral_host: 3 nodes, 2 edges

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


## Microbial Trait Causal Graph Curation Report: Commensalism (traitmech:000042)

### Scope summary (trait scope and boundary cases)
**Trait definition (curation target).** Commensalism (METPO: traitmech:000042) is a symbiosis in which the microorganism benefits from association with the host (resources, shelter, transport) while the host experiences **no detectable fitness cost** (i.e., host fitness remains essentially unaffected). This “no detectable cost” framing is important operationally because many interactions sit on a **parasite–mutualist continuum** and can shift with context; thus, commensalism can reflect limits of measurement rather than true absence of effects. Drew et al. explicitly place commensals at the center of a continuum and define them as those that “benefit … but do not cause a detectable cost.” (drew2021microbialevolutionand pages 1-2)

**Boundary cases.**
- **Balanced-costs-and-benefits commensalism:** A net-zero host effect may mask simultaneous harms and benefits. Srinivasan et al. describe “no-effects commensalism” vs “balanced-costs-and-benefits commensalism,” cautioning that commensalism is not always unambiguous. (srinivasan2024modelingmicrobialcommunity pages 1-2)
- **Context/genotype dependence:** Dziuba et al. highlight that costs/benefits depend on environment and host genotype; commensal-like outcomes can shift when stressors change. (dziuba2024phylogenymorphologyvirulence pages 1-2)
- **Neutralism vs commensalism:** Lengrand et al. distinguish commensalism (“beneficial for one agent and safe for another”) from neutralism (“no influence on either partner”), which can be useful for node/edge semantics. (lengrand2024bacterialendophytomesources pages 2-3)

**Operationalization for curation.** Empirically, commensalism should be curated when (i) the microbe’s fitness increases in association with the host and (ii) **host fitness assays** (e.g., survival, reproduction) show no significant effect, ideally across relevant contexts. Dziuba et al. describe fitness and pathology (gut damage) as operational measures to classify outcomes. (dziuba2024phylogenymorphologyvirulence pages 1-2)

### Current understanding: key mechanistic themes that enable “microbe benefits / host neutral” outcomes
Recent synthesis emphasizes that commensalism in hosts is often stabilized by **host control mechanisms**—a conceptualization summarized as an “ecosystem on a leash.” Wilde et al. review how hosts shape microbial ecology through immunity, barrier function, physiology, and transit, promoting tolerated colonizers while suppressing harmful behaviors. (wilde2024hostcontrolof pages 1-5, wilde2024hostcontrolof media 71921141, wilde2024hostcontrolof media 5f8baa46, wilde2024hostcontrolof media 2b156c6b)

Core mechanistic themes supported in recent sources include:
1. **Mucus- and mucin-mediated niches and resources.** Hosts provide mucus layers and mucin glycans that can selectively feed mucin-degrading taxa (e.g., Bacteroidaceae, Akkermansia), enabling microbes to benefit from host resources while remaining spatially segregated from epithelium. (wilde2024hostcontrolof pages 15-17, wilde2024hostcontrolof pages 24-26)
2. **IgA as both constraint and facilitator.** Secretory IgA can agglutinate/“enchain” microbes for clearance, but can also facilitate colonization of the mucus layer and protect microbes from stressors such as bile acids and bacteriophages—illustrating how host immunity can simultaneously permit colonization and limit harm. (wilde2024hostcontrolof pages 8-10)
3. **Host-imposed physicochemical constraints select for low-damage lifestyles.** Oxygen limitation favors fermentative metabolism in the gut, and host antimicrobial peptides/lectins maintain spatial segregation. These factors can select microbes that persist without invasive growth. (wilde2024hostcontrolof pages 5-8, wilde2024hostcontrolof pages 8-10)
4. **Resource limitation as harm-prevention.** Host molecules like lipocalin 2 can sequester siderophores, limiting microbial iron acquisition and potentially preventing overgrowth or virulence expression. (wilde2024hostcontrolof pages 15-17, wilde2024hostcontrolof pages 26-28)

### Recent developments (prioritizing 2023–2024)
#### 1) Host control as a central framework (Science 2024)
Wilde, Slack, and Foster synthesize host mechanisms that regulate microbiome composition and behavior (“partner choice” and “partner manipulation”), emphasizing that host processes such as mucus, IgA, antimicrobial peptides, transit, and nutrient constraints shape microbial evolution toward tolerated states. (wilde2024hostcontrolof pages 1-5, wilde2024hostcontrolof media 71921141, wilde2024hostcontrolof media 5f8baa46, wilde2024hostcontrolof media 2b156c6b)

#### 2) Updated views of commensalism classification and measurement (Microbial Ecology 2024)
Srinivasan et al. emphasize that interaction types (positive/negative/neutral) require careful operationalization with co-cultures, conditioned media, and quantitative modeling. Their distinction between “no-effects” and “balanced-costs-and-benefits” commensalism is directly relevant to curating commensalism nodes/edges without over-claiming neutrality. (srinivasan2024modelingmicrobialcommunity pages 1-2, srinivasan2024modelingmicrobialcommunity pages 2-3)

#### 3) IgA-centric mucosal mechanisms extended across contexts (Frontiers in Immunology 2024)
Carreto-Binaghi et al. summarize pathways supporting IgA induction/maintenance (e.g., BAFF/APRIL) and describe cytokine-driven links to mucus and IgA coating of bacteria (e.g., ILC2-derived IL-13 → mucus; IL-5 → IgA coating of stomach bacteria in mice). (carretobinaghi2024roleofcellular pages 9-10)

#### 4) Fungal commensalism highlighted as underappreciated but immunologically potent (Gut Microbes 2024)
Huang et al. note that fungi comprise only **0.01%–0.1%** of the human gut microbiome, yet can have outsized immunoregulatory roles. They describe epithelial/immune regulation of **Candida albicans commensal state** via IL-22–linked induction of secretory IgA and β-defensins, and they highlight antibiotic-driven dysbiosis leading to Candida overgrowth (penicillin/clindamycin/vancomycin examples). (huang2024themycobiomeas pages 1-2)

#### 5) Quantitative, real-world colonization resistance as a commensal community function (bioRxiv 2024)
Ambat et al. (preprint) discuss commensal gut bacteria as contributors to resilience against pathogen invasion. They cite **75–90% efficacy** for fecal microbiota transplantation (FMT) in recurrent *Clostridioides difficile* infection, and report asymptomatic *C. difficile* colonization prevalence of about **5% in adults** and **15–70% in infants** (illustrating that “colonization” can occur without overt disease). They propose metabolic mechanisms (fructooligosaccharide metabolism, vitamin B3 biosynthesis, competition for Stickland metabolism precursors) and highlight that a Bacteroides:Escherichia ratio may outperform alpha diversity as a discriminator of colonization resistance. (ambat2024emergentmetabolicinteractions pages 1-2)

### Current applications and real-world implementations
1. **Microbiome engineering/therapeutics via host control principles.** Wilde et al. argue that understanding host control provides therapeutic targets to reshape microbiota for health, framing interventions as leveraging evolved “leash” mechanisms rather than only adding microbes. (wilde2024hostcontrolof pages 1-5)
2. **FMT and defined consortia for colonization resistance.** The high FMT efficacy (75–90%) reported in Ambat et al. motivates rational design of bacteriotherapies (synthetic communities) based on identified metabolic interactions. (ambat2024emergentmetabolicinteractions pages 1-2)
3. **Oral health and biofilm management.** Bloch et al. describe oral streptococci as early biofilm colonizers whose adhesion to salivary pellicle and EPS matrix formation enable stable commensal biofilms, while noting ambivalence (some streptococci are also pathogens). These mechanisms are relevant to designing interventions that maintain commensal biofilms while preventing pathogenic transitions. (bloch2024oralstreptococcimodulators pages 2-3)

### Expert opinions and analysis (authoritative synthesis)
- **“Ecosystem on a leash” perspective:** Wilde et al. emphasize that microbiomes are shaped by ongoing tension between host control and symbiont evolution, and that commensal persistence is often a product of host mechanisms that constrain harm while permitting colonization. (wilde2024hostcontrolof pages 1-5, wilde2024hostcontrolof media 71921141)
- **Commensalism is often provisional:** Drew et al. explicitly define commensals by lack of detectable host costs and highlight context dependence on the parasite–mutualist continuum; Srinivasan et al. reinforce that neutrality may reflect measurement limits or balanced effects. These are key cautions for TraitMech curation. (drew2021microbialevolutionand pages 1-2, srinivasan2024modelingmicrobialcommunity pages 1-2)

### Candidate nodes (grouped by type) and ontology grounding
A candidate node inventory with suggested grounding is provided below.

| Node label | Node type | Suggested grounding | Brief rationale and supporting source citation id |
|---|---|---|---|
| secretory IgA | Host factor | GO:0002455 | Central host effector that can both agglutinate microbes for clearance and help bacteria colonize mucus, making it a key node for tolerated commensal persistence (wilde2024hostcontrolof pages 8-10) |
| dimeric IgA | Host factor | unresolved | Specifically described as the secreted mucosal IgA form that enchains/agglutinates microbes; useful if graph needs the more specific molecular form rather than generic IgA (wilde2024hostcontrolof pages 8-10) |
| polymeric immunoglobulin receptor (pIgR) | Host factor | GO:0005887 | Required for secretion of dimeric IgA onto epithelial surfaces, linking host epithelial transport to mucosal commensal control (wilde2024hostcontrolof pages 8-10) |
| mucus layer | Host factor | GO:0070701 | Major host barrier/niche that spatially separates microbes from epithelia while permitting colonization by adapted symbionts (wilde2024hostcontrolof pages 8-10, wilde2024hostcontrolof pages 5-8) |
| mucin | Host factor | GO:0001533 | Host glycoprotein substrate/resource and attachment surface for mucus-associated commensals; central to mucin foraging and adhesion (wilde2024hostcontrolof pages 15-17, wilde2024hostcontrolof pages 26-28) |
| MUC2 | Host factor | UniProt:P98088 | Named mucus component implicated in host-microbe boundary maintenance; good grounded node for intestinal mucus secretion/barrier context (wilde2024hostcontrolof pages 24-26) |
| antimicrobial peptides | Host factor | GO:0006950 | Broad host control mechanism limiting epithelial encroachment and selecting tolerated colonizers; should remain generic unless specific peptide is supported (wilde2024hostcontrolof pages 8-10) |
| RegIIIγ | Host factor | UniProt:Q9Z0M4 | Specific host antimicrobial lectin/peptide cited as maintaining spatial segregation from epithelium; useful high-specificity node (wilde2024hostcontrolof pages 8-10) |
| lipocalin 2 | Host factor | UniProt:P80188 | Host iron-withholding factor that sequesters siderophores and constrains microbial overgrowth/iron acquisition (wilde2024hostcontrolof pages 15-17) |
| Lypd8 | Host factor | UniProt:Q8N7G0 | Host factor that binds flagella and inhibits swimming, supporting neutrality by preventing microbial encroachment (wilde2024hostcontrolof pages 15-17) |
| C-type lectins | Host factor | GO:0030246 | Host secreted aggregating molecules that protect or spatially manage resident symbionts; useful generic node where specific lectin identity is not fixed (wilde2024hostcontrolof pages 8-10, wilde2024hostcontrolof pages 26-28) |
| IL-13 | Host factor | UniProt:P35225 | ILC2-derived cytokine stimulating epithelial mucus production, indirectly supporting commensal colonization niches (carretobinaghi2024roleofcellular pages 9-10) |
| IL-5 | Host factor | UniProt:P05113 | ILC2-derived cytokine that increases IgA production and bacterial coating in stomach models (carretobinaghi2024roleofcellular pages 9-10) |
| IL-22 | Host factor | UniProt:Q9GZX6 | Cited in fungal commensal-state regulation through induction of sIgA and β-defensins (huang2024themycobiomeas pages 1-2) |
| BAFF | Host factor | UniProt:Q9Y275 | Local factor promoting IgA class switching and maintenance of IgA+ plasma cells, supporting mucosal commensal control (carretobinaghi2024roleofcellular pages 9-10) |
| APRIL | Host factor | UniProt:O75888 | Partner to BAFF in promoting IgA CSR and persistence; relevant to host tolerance circuitry (carretobinaghi2024roleofcellular pages 9-10) |
| β-defensins | Host factor | GO:0042742 | Host antimicrobial effectors induced in fungal commensal-state control; useful but taxon/site-specific (huang2024themycobiomeas pages 1-2) |
| epithelial cell | Host factor | GO:0005911 | Recurrently described as active regulator of commensal state through mucus, IgA transport, and immune signaling (carretobinaghi2024roleofcellular pages 9-10, huang2024themycobiomeas pages 1-2) |
| mucosal barrier | Host factor | GO:0006959 | Useful abstract node for host structures that limit direct host damage while permitting metabolite exchange and colonization (wilde2024hostcontrolof pages 5-8) |
| glycan-binding proteins | Microbial factor | GO:0005539 | Bacterial proteins mediating attachment to mucin; important candidate node even if specific genes are unresolved (wilde2024hostcontrolof pages 15-17) |
| mucin-foraging capacity | Microbial factor | GO:0005975 | Broad microbial trait enabling access to host-derived glycans and persistence in mucus-associated niches (wilde2024hostcontrolof pages 15-17, wilde2024hostcontrolof pages 24-26) |
| mucin degradation | Process | GO:0005975 | Community/ecological process by which microbes consume mucin glycans; central mechanism for commensal benefit from host association (wilde2024hostcontrolof pages 15-17, wilde2024hostcontrolof pages 24-26) |
| adhesion to salivary pellicle | Process | GO:0044406 | Oral commensal colonization mechanism highlighted for streptococci as pioneer colonizers (bloch2024oralstreptococcimodulators pages 2-3) |
| extracellular polymeric substance matrix | Microbial factor | GO:0019439 | Biofilm matrix that protects colonizers from shear and antimicrobials; persistence mechanism for oral commensals and pathobionts alike (bloch2024oralstreptococcimodulators pages 2-3) |
| extracellular glucan | Chemical | CHEBI:15986 | Product of streptococcal sucrose metabolism that builds EPS/biofilm and supports persistence (bloch2024oralstreptococcimodulators pages 2-3) |
| biofilm formation | Process | GO:0042710 | Frequently implicated persistence mechanism in oral commensals; may support neutral colonization but also disease depending on context (bloch2024oralstreptococcimodulators pages 2-3) |
| flagellum | Microbial factor | GO:0009288 | Target of host Lypd8; useful node for motility-linked persistence versus epithelial encroachment tradeoff (wilde2024hostcontrolof pages 15-17, wilde2024hostcontrolof pages 26-28) |
| swimming motility | Process | GO:0033293 | Persistence trait allowing resistance to expulsion, but one that can increase inflammatory potential; boundary-case node (wilde2024hostcontrolof pages 26-28) |
| siderophore | Chemical | CHEBI:26672 | Iron-chelating microbial factor countered by host lipocalin 2; relevant to resource acquisition under host control (wilde2024hostcontrolof pages 15-17, wilde2024hostcontrolof pages 26-28) |
| fermentation | Process | GO:0006113 | Selected by low-oxygen host environments and associated with tolerated gut commensals (wilde2024hostcontrolof pages 15-17, wilde2024hostcontrolof pages 5-8) |
| fructooligosaccharide metabolism | Process | unresolved | Community metabolic function linked to commensal-mediated colonization resistance; adjacent to commensal ecology (ambat2024emergentmetabolicinteractions pages 1-2) |
| vitamin B3 biosynthesis | Process | GO:0006761 | Identified as a community metabolic feature contributing to pathogen suppression in commensal communities (ambat2024emergentmetabolicinteractions pages 1-2) |
| Stickland metabolism precursor competition | Process | unresolved | Specific ecological mechanism by which commensal communities suppress invasion; likely too community-specific for direct curation without caution (ambat2024emergentmetabolicinteractions pages 1-2) |
| oxygen consumption | Process | GO:0016491 | Oral streptococci consume oxygen and create anaerobe-permissive microenvironments, shaping commensal community assembly (bloch2024oralstreptococcimodulators pages 2-3) |
| acid production | Process | GO:0019244 | Oral streptococcal carbohydrate metabolism acidifies the niche; persistence mechanism but can cross into pathogenic ecology (bloch2024oralstreptococcimodulators pages 2-3) |
| acid tolerance (aciduric phenotype) | Microbial factor | GO:0009268 | Stress-resistance trait allowing persistence in acidified oral biofilms; relevant but not uniquely commensal (bloch2024oralstreptococcimodulators pages 2-3) |
| Akkermansia muciniphila | Microbial factor | NCBITaxon:239935 | Explicit example of mucin-foraging commensal taxon in host-control review; useful exemplar node but taxon-specific (wilde2024hostcontrolof pages 15-17, wilde2024hostcontrolof pages 24-26) |
| Bacteroidaceae | Microbial factor | NCBITaxon:815 | Family-level example of mucin-degrading taxa enriched by host mucin glycans (wilde2024hostcontrolof pages 15-17) |
| Candida albicans | Microbial factor | NCBITaxon:5476 | Canonical fungal commensal/pathobiont boundary case; strongly useful for warnings and transition logic (huang2024themycobiomeas pages 1-2) |
| oral streptococci | Microbial factor | NCBITaxon:1301 | Pioneer oral commensals with clear adhesion/EPS/oxygen-modulation mechanisms supporting host-associated persistence (bloch2024oralstreptococcimodulators pages 2-3) |
| bile acids | Chemical | CHEBI:3098 | Host chemical stressor from which IgA can protect bacteria; also shapes colonization outcomes more broadly (wilde2024hostcontrolof pages 8-10) |
| butyrate | Chemical | CHEBI:17968 | Host-usable fermentation product in low-oxygen gut systems; may indicate shift toward mutualism rather than strict commensalism (wilde2024hostcontrolof pages 15-17) |
| fructooligosaccharide | Chemical | CHEBI:28731 | Substrate implicated in community metabolic interactions associated with colonization resistance (ambat2024emergentmetabolicinteractions pages 1-2) |
| mucin glycans | Chemical | CHEBI:18154 | Host-derived carbohydrate pool feeding mucin degraders and supporting commensal benefit (wilde2024hostcontrolof pages 15-17) |
| taurine | Chemical | CHEBI:15891 | Mentioned among host molecules influencing microbial metabolism/community dynamics; likely adjacent rather than core commensal node (wilde2024hostcontrolof pages 15-17) |
| oxygen-limited gut environment | Environment | ENVO:01001071 | Host physiological condition favoring fermentative commensals and constraining aerobically expanding invaders (wilde2024hostcontrolof pages 5-8, wilde2024hostcontrolof pages 26-28) |
| gut mucosa | Environment | UBERON:0002405 | Core anatomical environment for many cited commensal mechanisms including IgA, mucus, and transit (wilde2024hostcontrolof pages 5-8, wilde2024hostcontrolof pages 8-10) |
| oral cavity | Environment | UBERON:0000165 | Important host niche for commensal streptococcal colonization mechanisms (bloch2024oralstreptococcimodulators pages 2-3) |
| salivary pellicle | Environment | unresolved | Specific oral surface used by pioneer colonizers; good niche node though grounding is unclear (bloch2024oralstreptococcimodulators pages 2-3) |
| antibiotic exposure | Environment | CHEBI:33229 | Perturbation that can disrupt commensal equilibrium and drive fungal overgrowth, useful as experimental/context node (huang2024themycobiomeas pages 1-2) |
| host fitness neutrality | Assay | unresolved | Core assay concept: commensalism requires no detectable host cost, often measured through survival/reproduction/pathology (dziuba2024phylogenymorphologyvirulence pages 1-2, drew2021microbialevolutionand pages 1-2) |
| survival assay | Assay | OBI:0000070 | Operational measure used to determine whether host suffers detectable cost in boundary-case systems (dziuba2024phylogenymorphologyvirulence pages 1-2) |
| reproduction assay | Assay | OBI:0001927 | Paired with survival to operationalize net host fitness impact in context-dependent symbioses (dziuba2024phylogenymorphologyvirulence pages 1-2) |
| pathology / tissue damage assay | Assay | GO:0001894 | Useful for distinguishing low-virulence commensal-like associations from pathogenic interactions (dziuba2024phylogenymorphologyvirulence pages 1-2) |
| co-culture assay | Assay | OBI:0000639 | Recommended operational framework for distinguishing commensal, mutualistic, and parasitic interactions in microbial systems (srinivasan2024modelingmicrobialcommunity pages 1-2, srinivasan2024modelingmicrobialcommunity pages 2-3) |
| conditioned-media assay | Assay | unresolved | Useful assay for separating diffusible cross-feeding/commensal effects from contact-dependent ones (srinivasan2024modelingmicrobialcommunity pages 2-3) |
| metagenomics | Assay | OBI:0002117 | Recommended recent method for context-dependent classification and functional profiling of commensal systems (srinivasan2024modelingmicrobialcommunity pages 1-2, lengrand2024bacterialendophytomesources pages 2-3) |
| metabolomics | Assay | OBI:0000366 | Important for detecting exchanged metabolites and mechanisms behind one-way benefit/commensal interactions (srinivasan2024modelingmicrobialcommunity pages 1-2, srinivasan2024modelingmicrobialcommunity pages 2-3) |
| mutualism–parasitism continuum placement | Assay | unresolved | Conceptual classification dimension for determining whether a candidate trait instance is commensal, mutualist, or parasitic (drew2021microbialevolutionand pages 1-2, lengrand2024bacterialendophytomesources pages 2-3) |


*Table: This table lists candidate nodes for a TraitMech causal graph of microbial commensalism, grouped across host, microbial, environmental, process, chemical, and assay categories. It emphasizes evidence-backed entities from recent 2023–2024 literature while flagging unresolved grounding and boundary-case nodes that need cautious curation.*

### Evidence-backed candidate causal edges (triples)
The following table lists candidate subject–predicate–object edges with short supporting snippets and curation notes.

| Edge (triple) | Evidence snippet (short quote) | Source (citation id) | DOI | Publication date | Notes/uncertainty |
|---|---|---|---|---|---|
| secretory IgA — promotes colonization of → bacteria in mucus layer | “IgA can act as a carrot as well as a stick, for example, by helping bacteria to colonize the mucus layer” | (wilde2024hostcontrolof pages 8-10) | https://doi.org/10.1126/science.adi3338 | Jul 2024 | Strong mechanistic support for host-mediated persistence of commensals; not specific to one taxon, but host-specific to mucosal systems. |
| secretory IgA — protects from → bile acids | “protect them from bile acids and bacteriophages” | (wilde2024hostcontrolof pages 8-10) | https://doi.org/10.1126/science.adi3338 | Jul 2024 | Supports host factor enabling microbial benefit with limited host harm; likely context-dependent across gut taxa. |
| dimeric IgA — agglutinates/enchains → microbes | “dimeric IgA agglutinates and enchains microbes for clearance” | (wilde2024hostcontrolof pages 8-10) | https://doi.org/10.1126/science.adi3338 | Jul 2024 | Bidirectional control edge; may constrain overgrowth rather than promote commensalism per se. Curate as host-control context node. |
| mucus/mucins — provide niche/resources for → mucin-foraging taxa | “mucin glycan availability selectively feed mucin-degrading taxa (e.g., Bacteroidaceae, Akkermansia)” | (wilde2024hostcontrolof pages 15-17) | https://doi.org/10.1126/science.adi3338 | Jul 2024 | Good candidate edge for host-derived resource enabling commensal persistence; taxon examples given, broader generalization inferred. |
| bacterial glycan-binding proteins — mediate attachment to → mucin | “bacteria attach to mucin via glycan-binding proteins” | (wilde2024hostcontrolof pages 15-17) | https://doi.org/10.1126/science.adi3338 | Jul 2024 | Mechanistic but generic; grounding of the specific proteins may be unclear without primary studies. |
| Lypd8 — inhibits swimming of → flagellated bacteria | “Lypd8 binds flagella to inhibit swimming” | (wilde2024hostcontrolof pages 15-17) | https://doi.org/10.1126/science.adi3338 | Jul 2024 | Host-control edge limiting epithelial encroachment; relevant to maintaining near-neutral host impact. Host-specific, not a microbial trait node. |
| lipocalin 2 — sequesters → siderophores | “lipocalin 2 sequesters siderophores (limiting iron uptake)” | (wilde2024hostcontrolof pages 15-17) | https://doi.org/10.1126/science.adi3338 | Jul 2024 | Important host pressure selecting low-damage colonizers; indirect edge to commensalism via nutrient limitation. |
| oxygen limitation — favors → fermentation | “oxygen limitation… promotes fermentation-favoring microbes” | (wilde2024hostcontrolof pages 5-8) | https://doi.org/10.1126/science.adi3338 | Jul 2024 | Environmental edge relevant to gut commensals; general and host-niche dependent. |
| fermentation-favoring microbes — produce → butyrate/beneficial metabolites | “forces fermentation, producing host-usable metabolites (butyrate)” | (wilde2024hostcontrolof pages 15-17) | https://doi.org/10.1126/science.adi3338 | Jul 2024 | This may cross into mutualism rather than strict commensalism; curate cautiously as nearby mechanism. |
| ILC2-derived IL-13 — stimulates → epithelial mucus production | “ILC2 produce IL-13 that stimulates epithelial cells to produce mucus” | (carretobinaghi2024roleofcellular pages 9-10) | https://doi.org/10.3389/fimmu.2024.1446072 | Sep 2024 | Host immune pathway supporting tolerated colonization; indirect edge to commensalism. |
| ILC2-derived IL-5 — increases → IgA coating of stomach bacteria | “ILC2-derived IL-5 increases IgA production that ‘coated stomach bacteria’” | (carretobinaghi2024roleofcellular pages 9-10) | https://doi.org/10.3389/fimmu.2024.1446072 | Sep 2024 | Mouse/model-system evidence; host-specific and indirect, but useful for IgA-mediated commensal persistence. |
| epithelial cells/IL-22 axis — induces → secretory IgA and β-defensins | “Epithelial cells regulate its commensal state by recruiting immune cells and inducing IL-22 to produce secretory IgA (sIgA) and β-defensins” | (huang2024themycobiomeas pages 1-2) | https://doi.org/10.1080/19490976.2024.2440111 | Dec 2024 | Candida-specific fungal commensalism mechanism; taxon-specific and host-site specific. |
| antibiotics (penicillin/clindamycin/vancomycin) — promote overgrowth of → Candida albicans | “penicillin, clindamycin, and vancomycin promote Candida albicans overgrowth in the gut” | (huang2024themycobiomeas pages 1-2) | https://doi.org/10.1080/19490976.2024.2440111 | Dec 2024 | Boundary-case edge showing disruption of commensalism toward dysbiosis/pathobiosis; not a positive commensal mechanism. |
| streptococcal adhesion to salivary pellicle — enables → early oral colonization | “streptococci are predominant initial adherents to the salivary pellicle” | (bloch2024oralstreptococcimodulators pages 2-3) | https://doi.org/10.3389/fcimb.2024.1357631 | Feb 2024 | Strong colonization mechanism for oral commensals; does not by itself prove neutral host effect. |
| extracellular glucan/EPS production — builds → biofilm matrix | “synthesis of extracellular glucans… builds the EPS biofilm matrix” | (bloch2024oralstreptococcimodulators pages 2-3) | https://doi.org/10.3389/fcimb.2024.1357631 | Feb 2024 | Supports persistence in a host niche; can also contribute to disease in some streptococci, so context-dependent. |
| EPS biofilm matrix — protects cells from → shear forces and antimicrobials | “protects cells from shear forces and confers resistance to antimicrobials” | (bloch2024oralstreptococcimodulators pages 2-3) | https://doi.org/10.3389/fcimb.2024.1357631 | Feb 2024 | Good persistence edge; not uniquely commensal, may also support pathogenic lifestyles. |
| streptococcal oxygen consumption — creates microenvironment for → strict anaerobes | “consume oxygen, creating microenvironments permissive for strict anaerobes” | (bloch2024oralstreptococcimodulators pages 2-3) | https://doi.org/10.3389/fcimb.2024.1357631 | Feb 2024 | Community-assembly edge; supports commensal community structure rather than host neutrality directly. |
| fructooligosaccharide metabolism — contributes to → suppression of C. difficile invasion | “fructooligosaccharide metabolism… contribute to suppression” | (ambat2024emergentmetabolicinteractions pages 1-2) | https://doi.org/10.1101/2024.08.29.610284 | Aug 2024 | Preprint; mechanism is community-level colonization resistance, closer to mutualistic host protection than strict commensalism. |
| vitamin B3 biosynthesis — contributes to → suppression of C. difficile invasion | “vitamin B3 biosynthesis… contribute to suppression” | (ambat2024emergentmetabolicinteractions pages 1-2) | https://doi.org/10.1101/2024.08.29.610284 | Aug 2024 | Preprint; same caution as above. Useful as neighboring ecology trait edge. |
| competition for Stickland metabolism precursors — suppresses → C. difficile | “competition for Stickland metabolism precursors contribute to suppression” | (ambat2024emergentmetabolicinteractions pages 1-2) | https://doi.org/10.1101/2024.08.29.610284 | Aug 2024 | Preprint; strong ecological mechanism but about pathogen exclusion, not direct commensal neutrality. |
| low virulence / no detectable host cost — operationalizes → commensalism | “commensals… benefit from the interaction with hosts, but do not cause a detectable cost” | (drew2021microbialevolutionand pages 1-2) | https://doi.org/10.1038/s41579-021-00550-7 | Apr 2021 | Foundational scope edge for curation; conceptual rather than molecular. |
| host fitness assays (survival, reproduction, pathology) — classify → commensal vs parasitic interaction | “commensalism can be identified empirically as no detectable net fitness effect in assays of survival/reproduction and pathology” | (dziuba2024phylogenymorphologyvirulence pages 1-2) | https://doi.org/10.1128/mbio.00582-24 | Jun 2024 | Important assay/experimental-factor edge; Daphnia microsporidian system, host-specific and operational. |
| balanced costs and benefits — can appear as → commensalism | “balanced-costs-and-benefits commensalism” | (srinivasan2024modelingmicrobialcommunity pages 1-2) | https://doi.org/10.1007/s00248-024-02370-7 | Apr 2024 | Important warning edge: apparent neutrality may mask opposing effects; conceptual, not mechanistic. |
| one partner benefits while other is unaffected — defines → commensalism | “commensalism… beneficial for one agent and safe for another” | (lengrand2024bacterialendophytomesources pages 2-3) | https://doi.org/10.3389/fsufs.2024.1378436 | Mar 2024 | Scope/definition edge only; suitable for trait metadata, not causal graph mechanism node. |


*Table: This table lists evidence-backed candidate subject–predicate–object edges relevant to microbial commensalism, emphasizing host control, colonization, and context-dependent neutrality. It is useful as a first-pass curation aid for deciding which mechanisms are strong enough to include in a TraitMech causal graph and which should remain flagged as uncertain or adjacent to mutualism/pathobiosis.*

### Statistics and quantitative data from recent studies (2023–2024)
- **Fungal abundance in human gut microbiome:** fungi constitute **0.01%–0.1%** of the human gut microbiome. (huang2024themycobiomeas pages 1-2)
- **FMT efficacy for recurrent *C. difficile* infection:** **75–90%** (as summarized in Ambat et al., preprint). (ambat2024emergentmetabolicinteractions pages 1-2)
- **Asymptomatic *C. difficile* colonization prevalence:** about **5% in adults** and **15–70% in infants** (Ambat et al., preprint). (ambat2024emergentmetabolicinteractions pages 1-2)

### Warnings / claims that should not yet be curated (or should be curated as uncertain)
1. **Commensalism vs mutualism:** Edges involving host-usable metabolites (e.g., butyrate production) may indicate mutualistic benefit, not strict commensalism; curate as adjacent mechanisms unless host fitness neutrality is explicitly shown. (wilde2024hostcontrolof pages 15-17)
2. **Preprint evidence:** The Ambat et al. colonization resistance mechanisms are mechanistically detailed but are from bioRxiv; edges from that work should be flagged as **uncertain** until peer review. (ambat2024emergentmetabolicinteractions pages 1-2)
3. **Taxon- and niche-specificity:** Candida commensal regulation (IL-22 → sIgA/β-defensins) is valuable but taxon-specific; oral streptococcal EPS/biofilm mechanisms also apply to disease-associated states. Curate with explicit host-site context nodes (gut mucosa vs oral cavity) and uncertainty tags. (huang2024themycobiomeas pages 1-2, bloch2024oralstreptococcimodulators pages 2-3)
4. **“No detectable cost” depends on assay sensitivity:** Because commensalism can reflect detection limits or balanced effects, curations should include assay nodes (survival/reproduction/pathology; co-culture/omics methods) where possible. (srinivasan2024modelingmicrobialcommunity pages 1-2, dziuba2024phylogenymorphologyvirulence pages 1-2, drew2021microbialevolutionand pages 1-2)

---

## DOI-first bibliography (with URLs and publication dates)
1. Wilde J, Slack E, Foster KR. **Host control of the microbiome: Mechanisms, evolution, and disease.** *Science*. Jul 2024. DOI: 10.1126/science.adi3338. URL: https://doi.org/10.1126/science.adi3338 (wilde2024hostcontrolof pages 1-5)
2. Srinivasan S, Jnana A, Murali TS. **Modeling Microbial Community Networks: Methods and Tools for Studying Microbial Interactions.** *Microbial Ecology*. Apr 2024. DOI: 10.1007/s00248-024-02370-7. URL: https://doi.org/10.1007/s00248-024-02370-7 (srinivasan2024modelingmicrobialcommunity pages 1-2)
3. Carreto-Binaghi LE, Sztein MB, Booth JS. **Role of cellular effectors in the induction and maintenance of IgA responses leading to protective immunity against enteric bacterial pathogens.** *Frontiers in Immunology*. Sep 2024. DOI: 10.3389/fimmu.2024.1446072. URL: https://doi.org/10.3389/fimmu.2024.1446072 (carretobinaghi2024roleofcellular pages 9-10)
4. Huang H, Wang Q, Yang Y, et al. **The mycobiome as integral part of the gut microbiome: crucial role of symbiotic fungi in health and disease.** *Gut Microbes*. Dec 2024. DOI: 10.1080/19490976.2024.2440111. URL: https://doi.org/10.1080/19490976.2024.2440111 (huang2024themycobiomeas pages 1-2)
5. Dziuba MK, McIntire KM, Seto K, et al. **Phylogeny, morphology, virulence, ecology, and host range of *Ordospora pajunii* (Ordosporidae), a microsporidian symbiont of *Daphnia* spp.** *mBio*. Jun 2024. DOI: 10.1128/mbio.00582-24. URL: https://doi.org/10.1128/mbio.00582-24 (dziuba2024phylogenymorphologyvirulence pages 1-2)
6. Bloch S, Hager-Mair FF, Andrukhov O, Schäffer C. **Oral streptococci: modulators of health and disease.** *Frontiers in Cellular and Infection Microbiology*. Feb 2024. DOI: 10.3389/fcimb.2024.1357631. URL: https://doi.org/10.3389/fcimb.2024.1357631 (bloch2024oralstreptococcimodulators pages 2-3)
7. Ambat A, van den Berg NI, Zorrilla F, et al. **Emergent metabolic interactions in resistance to *Clostridioides difficile* invasion.** *bioRxiv* (preprint). Aug 2024. DOI: 10.1101/2024.08.29.610284. URL: https://doi.org/10.1101/2024.08.29.610284 (ambat2024emergentmetabolicinteractions pages 1-2)
8. Lengrand S, Pesenti L, Bragard C, Legrève A. **Bacterial endophytome sources, profile and dynamics—a conceptual framework.** *Frontiers in Sustainable Food Systems*. Mar 2024. DOI: 10.3389/fsufs.2024.1378436. URL: https://doi.org/10.3389/fsufs.2024.1378436 (lengrand2024bacterialendophytomesources pages 2-3)
9. Drew GC, Stevens EJ, King KC. **Microbial evolution and transitions along the parasite–mutualist continuum.** *Nature Reviews Microbiology*. Apr 2021. DOI: 10.1038/s41579-021-00550-7. URL: https://doi.org/10.1038/s41579-021-00550-7 (drew2021microbialevolutionand pages 1-2)


References

1. (drew2021microbialevolutionand pages 1-2): Georgia C. Drew, Emily J. Stevens, and Kayla C. King. Microbial evolution and transitions along the parasite–mutualist continuum. Nature Reviews. Microbiology, 19:623-638, Apr 2021. URL: https://doi.org/10.1038/s41579-021-00550-7, doi:10.1038/s41579-021-00550-7. This article has 396 citations.

2. (srinivasan2024modelingmicrobialcommunity pages 1-2): Shanchana Srinivasan, Apoorva Jnana, and Thokur Sreepathy Murali. Modeling microbial community networks: methods and tools for studying microbial interactions. Microbial Ecology, Apr 2024. URL: https://doi.org/10.1007/s00248-024-02370-7, doi:10.1007/s00248-024-02370-7. This article has 80 citations and is from a domain leading peer-reviewed journal.

3. (dziuba2024phylogenymorphologyvirulence pages 1-2): Marcin K. Dziuba, Kristina M. McIntire, Kensuke Seto, Elizabeth S. Davenport, Mary A. Rogalski, Camden D. Gowler, Emma Baird, Megan Vaandrager, Cristian Huerta, Riley Jaye, Fiona E. Corcoran, Alicia Withrow, Steven Ahrendt, Asaf Salamov, Matt Nolan, Sravanthi Tejomurthula, Kerrie Barry, Igor V. Grigoriev, Timothy Y. James, and Meghan A. Duffy. Phylogeny, morphology, virulence, ecology, and host range of <i>ordospora pajunii</i> (ordosporidae), a microsporidian symbiont of <i>daphnia</i> spp. Jun 2024. URL: https://doi.org/10.1128/mbio.00582-24, doi:10.1128/mbio.00582-24. This article has 9 citations and is from a domain leading peer-reviewed journal.

4. (lengrand2024bacterialendophytomesources pages 2-3): Salomé Lengrand, Lena Pesenti, Claude Bragard, and Anne Legrève. Bacterial endophytome sources, profile and dynamics—a conceptual framework. Frontiers in Sustainable Food Systems, Mar 2024. URL: https://doi.org/10.3389/fsufs.2024.1378436, doi:10.3389/fsufs.2024.1378436. This article has 27 citations and is from a peer-reviewed journal.

5. (wilde2024hostcontrolof pages 1-5): Jacob Wilde, Emma Slack, and Kevin R. Foster. Host control of the microbiome: mechanisms, evolution, and disease. Science, Jul 2024. URL: https://doi.org/10.1126/science.adi3338, doi:10.1126/science.adi3338. This article has 154 citations and is from a highest quality peer-reviewed journal.

6. (wilde2024hostcontrolof media 71921141): Jacob Wilde, Emma Slack, and Kevin R. Foster. Host control of the microbiome: mechanisms, evolution, and disease. Science, Jul 2024. URL: https://doi.org/10.1126/science.adi3338, doi:10.1126/science.adi3338. This article has 154 citations and is from a highest quality peer-reviewed journal.

7. (wilde2024hostcontrolof media 5f8baa46): Jacob Wilde, Emma Slack, and Kevin R. Foster. Host control of the microbiome: mechanisms, evolution, and disease. Science, Jul 2024. URL: https://doi.org/10.1126/science.adi3338, doi:10.1126/science.adi3338. This article has 154 citations and is from a highest quality peer-reviewed journal.

8. (wilde2024hostcontrolof media 2b156c6b): Jacob Wilde, Emma Slack, and Kevin R. Foster. Host control of the microbiome: mechanisms, evolution, and disease. Science, Jul 2024. URL: https://doi.org/10.1126/science.adi3338, doi:10.1126/science.adi3338. This article has 154 citations and is from a highest quality peer-reviewed journal.

9. (wilde2024hostcontrolof pages 15-17): Jacob Wilde, Emma Slack, and Kevin R. Foster. Host control of the microbiome: mechanisms, evolution, and disease. Science, Jul 2024. URL: https://doi.org/10.1126/science.adi3338, doi:10.1126/science.adi3338. This article has 154 citations and is from a highest quality peer-reviewed journal.

10. (wilde2024hostcontrolof pages 24-26): Jacob Wilde, Emma Slack, and Kevin R. Foster. Host control of the microbiome: mechanisms, evolution, and disease. Science, Jul 2024. URL: https://doi.org/10.1126/science.adi3338, doi:10.1126/science.adi3338. This article has 154 citations and is from a highest quality peer-reviewed journal.

11. (wilde2024hostcontrolof pages 8-10): Jacob Wilde, Emma Slack, and Kevin R. Foster. Host control of the microbiome: mechanisms, evolution, and disease. Science, Jul 2024. URL: https://doi.org/10.1126/science.adi3338, doi:10.1126/science.adi3338. This article has 154 citations and is from a highest quality peer-reviewed journal.

12. (wilde2024hostcontrolof pages 5-8): Jacob Wilde, Emma Slack, and Kevin R. Foster. Host control of the microbiome: mechanisms, evolution, and disease. Science, Jul 2024. URL: https://doi.org/10.1126/science.adi3338, doi:10.1126/science.adi3338. This article has 154 citations and is from a highest quality peer-reviewed journal.

13. (wilde2024hostcontrolof pages 26-28): Jacob Wilde, Emma Slack, and Kevin R. Foster. Host control of the microbiome: mechanisms, evolution, and disease. Science, Jul 2024. URL: https://doi.org/10.1126/science.adi3338, doi:10.1126/science.adi3338. This article has 154 citations and is from a highest quality peer-reviewed journal.

14. (srinivasan2024modelingmicrobialcommunity pages 2-3): Shanchana Srinivasan, Apoorva Jnana, and Thokur Sreepathy Murali. Modeling microbial community networks: methods and tools for studying microbial interactions. Microbial Ecology, Apr 2024. URL: https://doi.org/10.1007/s00248-024-02370-7, doi:10.1007/s00248-024-02370-7. This article has 80 citations and is from a domain leading peer-reviewed journal.

15. (carretobinaghi2024roleofcellular pages 9-10): Laura E. Carreto-Binaghi, Marcelo B. Sztein, and Jayaum S. Booth. Role of cellular effectors in the induction and maintenance of iga responses leading to protective immunity against enteric bacterial pathogens. Frontiers in Immunology, Sep 2024. URL: https://doi.org/10.3389/fimmu.2024.1446072, doi:10.3389/fimmu.2024.1446072. This article has 28 citations and is from a peer-reviewed journal.

16. (huang2024themycobiomeas pages 1-2): Hui Huang, Qiurong Wang, Ying Yang, Wei Zhong, Feng He, and Jun Li. The mycobiome as integral part of the gut microbiome: crucial role of symbiotic fungi in health and disease. Gut Microbes, Dec 2024. URL: https://doi.org/10.1080/19490976.2024.2440111, doi:10.1080/19490976.2024.2440111. This article has 53 citations and is from a peer-reviewed journal.

17. (ambat2024emergentmetabolicinteractions pages 1-2): Achuthan Ambat, Naomi Iris van den Berg, Francisco Zorrilla, Shruti Menon, Abhijit Maji, Arianna Basile, Sudeep Ghimire, Lajos Kalmar, Kiran R. Patil, and Joy Scaria. Emergent metabolic interactions in resistance to clostridioides difficile invasion. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.29.610284, doi:10.1101/2024.08.29.610284. This article has 1 citations.

18. (bloch2024oralstreptococcimodulators pages 2-3): Susanne Bloch, Fiona F. Hager-Mair, Oleh Andrukhov, and Christina Schäffer. Oral streptococci: modulators of health and disease. Frontiers in Cellular and Infection Microbiology, Feb 2024. URL: https://doi.org/10.3389/fcimb.2024.1357631, doi:10.3389/fcimb.2024.1357631. This article has 120 citations.