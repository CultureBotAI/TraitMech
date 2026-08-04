---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T22:59:37.497428'
end_time: '2026-08-03T23:07:55.711227'
duration_seconds: 498.21
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
  causal_graph_summary: 'commensalism_neutral_host: 11 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
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
- **METPO identifier:** traitmech:000042
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


# TraitMech curation report: microbial commensalism

## Executive curation recommendation

**Trait:** commensalism (`traitmech:000042`; ECOLOGY; CLASS)

Commensalism should be represented as a **relational, context-indexed ecological outcome**, not as a single cell-autonomous pathway. The necessary phenotype is:

1. association increases microbial access to resources, shelter, transport, or persistence;
2. the microorganism establishes or maintains association with a specified host and anatomical site; and
3. host fitness is statistically indistinguishable from an appropriate uncolonized or alternative-colonization control over a defined interval.

The strongest mechanistic subgraph presently supported is **host glycan/IgA-supported mucosal persistence**, particularly in *Bacteroides fragilis*. However, most studies establish colonization or host benefit rather than directly demonstrating the defining neutral host-fitness term. Accordingly, the graph should distinguish `commensal association` from its enabling mechanisms and attach taxon, host, site, diet, immune status, and assay qualifiers to every terminal claim.

## 1. Scope and boundaries

Drew, Stevens and King place commensalism near the neutral point of a dynamic parasite–mutualist continuum: host effects can be neutral, harmful, or beneficial and can change with ecological or genetic context. Virulence is correspondingly framed as host damage, often measured as reduced fitness. Thus, “commensal” is not an immutable organismal label. (drew2021microbialevolutionand pages 2-3)

### Include

- Persistent or recurrent host association in which the microorganism obtains a measurable fitness benefit.
- Molecular mechanisms enabling low-damage attachment, spatial retention, nutrient acquisition, immune accommodation, and competition within an occupied niche.
- Assay-defined neutrality, provided the host endpoint, time window, and detection threshold are recorded.

### Exclude or distinguish

- **Colonization:** presence, abundance, adherence, or persistence alone. Colonization is an enabling process, not proof of host neutrality.
- **Mutualism:** both partners benefit. Colonization resistance, barrier reinforcement, or immunomodulation may move an interaction toward mutualism rather than demonstrate strict commensalism.
- **Parasitism/pathogenicity:** measurable host damage or fitness reduction.
- **Pathobiont:** an organism harmless in one context but disease-producing after environmental, host-genetic, or immune changes; this is a context transition rather than a separate permanent microbial essence. (caballeroflores2023microbiotamediatedcolonizationresistance pages 12-14)
- **Microbiota member/symbiont:** taxonomic occurrence or long-term association without a measured host-effect sign.
- **Probiotic:** an intervention category requiring demonstrated host benefit; it is not synonymous with commensal.

A suitable terminal graph pattern is therefore:

`host-derived resource or shelter → microbial acquisition/retention → increased microbial persistence`, together with a separately asserted assay result, `colonization → no detectable change in specified host-fitness endpoint`. The latter edge should not be inferred merely from absence of reported disease.

## 2. Candidate nodes grouped by type

### A. Trait and outcome nodes

- **Commensalism** — `METPO:traitmech:000042` as supplied.
- Host-associated microbial lifestyle.
- Mucosal colonization; stable mucosal colonization; single-strain stability.
- Epithelial or mucus adherence.
- Niche saturation; competitive exclusion; colonization resistance.
- Microbial fitness/abundance/persistence.
- Host fitness unchanged — retain as a label-only assay outcome until a suitable phenotype/statistical ontology term is verified.
- Host damage, inflammation, barrier permeability, and bacterial translocation as boundary/negative-outcome nodes.

### B. Microbial genes, proteins, and structures

- ***B. fragilis* `ccfA`** — taxon-specific regulator in the commensal colonization-factor system; retain as a label plus strain/locus accession until a verified UniProt or genome-feature identifier is selected.
- *B. fragilis* capsular polysaccharides **PSA, PSB, PSC** and their biosynthetic loci.
- *B. thetaiotaomicron* **CPS1–CPS8** repertoire.
- Polysaccharide-utilization loci; glycoside hydrolases; glycosyltransferases.
- Pili, exopolysaccharide, lipoteichoic acid, surface-layer proteins, and adhesins. Lactobacillus/Bifidobacterium colonization reviews identify acid/bile resistance, pili, EPS, LTA, and carbohydrate-active enzymes as strain-specific colonization determinants; approximately 14% of *Bifidobacterium* genes were reported to encode carbohydrate-metabolizing enzymes. These are broad candidate classes, not universal commensalism determinants. (xiao2021gutcolonizationmechanisms pages 3-5, xiao2021gutcolonizationmechanisms pages 5-6)
- **SpaC** as a *Lactobacillus rhamnosus* GG mucus-binding candidate; evidence is review-level in the retrieved corpus. (xiao2021gutcolonizationmechanisms pages 7-9)
- **ClfA, SraP, Fnbps** as skin-adherence comparators, but not commensalism nodes based on the retrieved *S. aureus* experiment. (costa2024thestaphylococcusaureus pages 1-2)

### C. Host molecules, cells, and pathways

- Secretory immunoglobulin A (**sIgA**); IgA coating/binding and IgA-mediated aggregation.
- **MUC2** and mucin-type O-linked glycans.
- **C1GalT1**, core-1 O-glycans; candidate core-2/core-3 glycosylation machinery.
- Intestinal epithelial cells, goblet cells, intestinal mucus, inner/outer colonic mucus layers.
- Group-3 innate lymphoid cells (**ILC3**), **HIF-1α**, **IL-22**, epithelial barrier integrity.
- B cells/adaptive immunity and anti-CD20 depletion as experimental factors.

### D. Chemicals and nutrients

Conservative identifiers that are well established and should still be checked against the project’s ontology release before serialization include:

- Oxygen — `CHEBI:15379`.
- Butyrate — `CHEBI:17968`.
- Acetate — `CHEBI:30089`.
- L-lactate — `CHEBI:422`.
- Fucose — `CHEBI:33984`.
- N-acetyl-D-galactosamine — `CHEBI:28037`.
- N-acetyl-D-glucosamine — `CHEBI:506227`.
- Mucin O-glycans, dietary fiber, fructan, amino acids, gluconate, iron, zinc, manganese, bile acids, and short-chain fatty acids as broader chemical or mixture nodes where exact composition is not specified.

### E. Environments and experimental contexts

- Mammalian gastrointestinal tract, intestinal lumen, colonic mucus, epithelial surface, physiological hypoxia.
- Germ-free and gnotobiotic mouse; monocolonization; horizontal-transmission/cohousing assay.
- `IgA−/−`, `Rag1−/−`, B-cell-depleted, and epithelial glycosyltransferase-knockout mice.
- High-fiber, low-fiber, and high-protein diets; antibiotic exposure; hyperbaric oxygen.
- Human skin surface, corneocyte-adhesion assay, and skin-like medium.

Taxa should be grounded using verified NCBITaxon records during YAML implementation. Priority taxa are *Bacteroides fragilis*, *Bacteroides thetaiotaomicron*, *Lactobacillus rhamnosus*, *Bifidobacterium* spp., *Escherichia coli*, *Citrobacter rodentium*, *Salmonella enterica* serovar Typhimurium, and *Clostridioides difficile*. Strain-level identifiers are preferable whenever the experiment used a defined strain.

## 3. Candidate causal edges

The following evidence matrix separates direct perturbation evidence from synthesis and identifies edges that should remain contextual or provisional.

| Proposed subject–predicate–object triple | Organism/context | Evidence type and strength | Exact short supporting snippet | DOI | Curation note/uncertainty |
|---|---|---|---|---|---|
| **Bacteroides fragilis ccfA** → **regulates expression of capsular polysaccharide loci (PSC↑ / PSA switch in vivo)** | *B. fragilis* gut monocolonization; RNA-seq and in vivo expression | **Direct experiment; strong; taxon-specific** | “**24 out of 25 genes mapped to the biosynthesis loci for capsular polysaccharides A and C (PSA and PSC)**” and “**ccf mutation decreased expression of PSC and increased expression of PSA in vivo**” (donaldson2018gutmicrobiotautilize pages 2-3) | https://doi.org/10.1126/science.aaq0926 | Directly supports a gene-regulatory edge in *B. fragilis*. Prefer capsule-locus-specific child nodes over generic “capsule” node. |
| **PSB/PSC capsule expression** → **increases IgA binding/coating** | *B. fragilis* feces from monocolonized mice | **Direct experiment; strong; taxon-specific** | “wild-type *B. fragilis* was highly coated with IgA, which was **significantly diminished in Δccf and ΔPSB/C strains**” (donaldson2018gutmicrobiotautilize pages 2-3) | https://doi.org/10.1126/science.aaq0926 | Mechanism is specific to CCF-regulated capsules in *B. fragilis*; not yet generalizable to all commensals. |
| **Secretory IgA** → **increases epithelial/mucus adherence of *B. fragilis*** | Tissue-culture epithelial cells; mucus-producing lines | **Direct experiment; strong; taxon-specific** | “**The addition of IgA** to in vivo-adapted, IgA-free bacteria **increased adherence of B. fragilis to intestinal epithelial cells**” and “**Cell lines known to produce more mucus exhibited a greater capacity for IgA-enhanced B. fragilis adherence**” (donaldson2018gutmicrobiotautilize pages 2-3) | https://doi.org/10.1126/science.aaq0926 | Supports an edge from host IgA to microbe adherence/mucosal association. Host factor, not microbe-encoded mechanism. |
| **Secretory IgA / B cell responses** → **promotes stable mucosal colonization / single-strain stability** | *B. fragilis* horizontal transmission assays; IgA−/−, Rag1−/−, anti-CD20 models | **Direct experiment; strong; taxon-specific** | “**IgA specifically contributes to single-strain stability**” and “lack of IgA allowed **co-colonization by challenge strains**” (donaldson2018gutmicrobiotautilize pages 3-4) | https://doi.org/10.1126/science.aaq0926 | Strong evidence for stable colonization, but this may be better modeled as “host IgA enables commensal mucosal persistence” rather than intrinsic commensalism. |
| **Mucin O-glycans** → **provide microbial binding sites** | Intestinal mucus; host–microbe interface | **Review-level; moderate** | “**Mucin glycans may also act as microbial binding sites, influencing intestinal colonization**” (fekete2023theroleof pages 1-5) | https://doi.org/10.1152/ajpgi.00261.2022 | Useful generic edge for host environment → colonization. Review language; no single microbe-specific causal perturbation in retrieved text. |
| **Mucin O-glycans** → **serve as nutrient source for microbes** | Intestinal commensals/pathogens in mucus habitat | **Review-level; moderate** | “**Mucin O-glycans and glycan-derived sugars may be degraded and utilized as a nutrient source**” (fekete2023theroleof pages 1-5) | https://doi.org/10.1152/ajpgi.00261.2022 | Good environmental/nutrient node for commensalism graph; should be marked broad and host-context dependent. |
| **C1GalT1 / core-1-derived O-glycans** → **maintains mucus integrity and limits bacterial translocation** | IEC-specific knockout mice | **Review summarizing direct genetics; moderate** | “loss of core 1-derived glycan structures… **resulted in development of spontaneous colitis**” and “showed **thin and discontinuous colonic mucus and translocation of bacteria into mucosal tissues**” (fekete2023theroleof pages 1-5) | https://doi.org/10.1152/ajpgi.00261.2022 | Strong biological plausibility for host-side gating of harmless colonization; source is secondary review, so curate cautiously unless primary knockout papers are added. |
| **Capsule repertoire (multiple CPS loci)** → **increases competitive fitness in mouse gut** | *Bacteroides thetaiotaomicron* long-term colonization and competition | **Direct experiment; strong; taxon-specific** | “**specific CPSs provide advantages in the gut environment**” and “the ability to dynamically express multiple CPSs **provides an advantage over any single CPS**” (porter2017asubsetof pages 2-4) | https://doi.org/10.1016/j.chom.2017.08.020 | Supports capsule diversity/repertoire as a colonization-fitness mechanism. Evidence is about competitive fitness, not host neutrality per se. |
| **Existing gut microbiota nutrient depletion/scavenging** → **excludes pathogen expansion** | Gut ecosystem colonization resistance | **Review-level; strong synthesis** | “the gut microorganisms **scavenge most available nutrients, keeping them at low levels at the steady state, which limits pathogen expansion**” (caballeroflores2023microbiotamediatedcolonizationresistance pages 3-4) | https://doi.org/10.1038/s41579-022-00833-7 | Important ecosystem-level edge; supports commensal communities maintaining occupancy. Not a microbe-intrinsic trait for one taxon. |
| **High-protein diet** → **increases *Citrobacter rodentium* colonization** | Conventionally raised mice | **Review summarizing direct screen; moderate** | “administration of a **high-protein diet** to conventionally raised mice **enhanced pathogen colonization by ~3 logs**” (caballeroflores2023microbiotamediatedcolonizationresistance pages 3-4) | https://doi.org/10.1038/s41579-022-00833-7 | Environmental modifier edge; relevant as a factor weakening commensal-mediated exclusion, not a direct commensalism mechanism. |
| **Oxygen-respiring commensals/facultative anaerobes** → **improve resistance to *Salmonella Typhimurium*** | Synthetic communities in mouse gut | **Review summarizing direct community experiments; moderate** | “**Three additional facultative anaerobes, which can respire oxygen, were able to improve resistance to S. Typhimurium** to levels similar to a complete microbiota” (caballeroflores2023microbiotamediatedcolonizationresistance pages 3-4) | https://doi.org/10.1038/s41579-022-00833-7 | Good edge for oxygen competition / electron acceptor occupancy. Community-level and pathogen-exclusion focused. |
| **Hyperbaric oxygen** → **reduces microbiota-derived SCFAs and worsens dysbiosis** | Mouse gut; HBO exposure before CDI | **Direct experiment; strong** | “daily treatment with hyperbaric oxygen **affects gut microbiome composition, worsening antibiotic-induced dysbiosis**” and “closely linked with **a decline in the level of microbiota-derived short-chain fatty acids (SCFAs)**” (fachi2024hyperbaricoxygenaugments pages 1-2) | https://doi.org/10.1080/19490976.2023.2297872 | Valuable negative environmental edge: oxygenation can destabilize anaerobe-associated commensal states. Disease-model context. |
| **Butyrate** → **improves HIF-1α–IL-22 ILC3 responses and epithelial barrier integrity** | HBO/CDI mouse model | **Direct experiment; strong** | “**Butyrate… mitigated HBO-induced susceptibility to CDI and increased epithelial barrier integrity by improving group 3 innate lymphoid cell (ILC3) responses**” and effects depended on “**HIF-1α-IL-22 axis**” (fachi2024hyperbaricoxygenaugments pages 1-2) | https://doi.org/10.1080/19490976.2023.2297872 | Strong host-response mechanism linking anaerobe metabolite production to a permissive, low-damage host interface; indirect support for commensalism maintenance. |
| **Acidic skin-like medium** → **upregulates adhesins (ClfA/SraP/Fnbps) and increases corneocyte adherence in *S. aureus*** | Human skin-like medium; pathogen colonization assay | **Direct experiment; strong, but off-scope warning** | “MRSA primed in SLM **adhered better to human corneocytes**” and “This improved adherence… was **dependent on both acidic pH and growth in SLM**” with roles for “**ClfA, SraP, and the fibronectin binding proteins (Fnbps)**” (costa2024thestaphylococcusaureus pages 1-2) | https://doi.org/10.1128/mbio.00453-24 | **Warning:** pathogen colonization mechanism, not evidence of commensalism. Useful only as a boundary-case comparator for host association and adhesion. |
| **Commensalism** → **is a near-neutral point on a parasite–mutualist continuum** | Conceptual scope across host–microbe symbioses | **Review-level definition; strong conceptual support** | “Symbiotic interactions can be **neutral, harmful or have beneficial effects** on the host organism” and transitions occur “**along the parasite–mutualist continuum**” (drew2021microbialevolutionand pages 2-3) | https://doi.org/10.1038/s41579-021-00550-7 | Use for scope/definition only, not as a mechanistic edge. Important warning that commensalism is context-dependent and can shift. |


*Table: This table compiles candidate causal edges and evidence for a TraitMech curation of microbial commensalism, separating direct experimental findings from review-level synthesis. It is useful for deciding which host, microbial, and environmental mechanisms are ready for graph curation and which require caution due to taxon specificity or off-scope pathogen contexts.*

### Highest-priority graph core

The most defensible initial graph is:

1. `B. fragilis ccfA → regulates → PSA/PSC capsule-locus expression`;
2. `CCF-regulated PSB/PSC capsules → increase → species-specific IgA coating`;
3. `secretory IgA coating → increases → epithelial/mucus adherence and aggregation`;
4. `IgA-supported mucosal association → increases → single-strain stability`;
5. `stable mucosal association + host-derived habitat/resources → benefits → microbial persistence`.

Donaldson et al. directly showed that 24 of 25 non-`ccf` genes regulated after `ccfA` overexpression mapped to PSA/PSC biosynthetic loci. `ccf` mutation reduced PSC and increased PSA expression in vivo. Wild-type bacteria were strongly IgA-coated, whereas coating was diminished in `Δccf` and `ΔPSB/C` strains. Added IgA increased epithelial adherence, especially in mucus-producing cell lines. IgA deficiency, adaptive-immune deficiency, or B-cell depletion disrupted mucosal aggregation and single-strain stability. These results support a coherent regulatory-to-ecological mechanism. (donaldson2018gutmicrobiotautilize pages 2-3, donaldson2018gutmicrobiotautilize pages 3-4)

**Critical qualification:** this pathway demonstrates host-supported stable association. It does not, by itself, show that host fitness is unchanged. Indeed, a host mechanism that selectively maintains beneficial organisms could represent mutualism.

## 4. Recent developments, 2023–2024

### Mucus is an active ecological interface

A 2023 synthesis describes MUC2 O-glycans as binding sites, nutrient substrates, barrier components, and determinants of microbial spatial distribution. MUC2 can be up to 80% O-linked glycans by weight/volume. Glycan fermentation generates SCFAs that influence immunity and goblet-cell activity. However, glycan structures can also act as decoys, and their degradation may weaken the barrier; the edge direction therefore depends on glycan structure, microbial enzyme repertoire, and anatomical site. (fekete2023theroleof pages 1-5)

Genetic evidence summarized in that review strengthens the host-side boundary mechanism. Intestinal epithelial loss of C1GalT1/core-1 glycans caused thin, discontinuous mucus, bacterial translocation, and spontaneous colitis; loss of core-2 or core-3 structures increased permeability and susceptibility in other models. These findings support `intact mucin glycosylation → spatially contained colonization`, but the primary knockout articles should be retrieved before this edge is treated as fully curated. (fekete2023theroleof pages 1-5)

### Nutrient and electron-acceptor occupancy are mechanistic

The 2023 Nature Reviews Microbiology synthesis emphasizes that filled nutrient niches stabilize gut communities and restrict invaders. Germ-free or antibiotic-treated mice contain more available sugars and amino acids and have less colonization resistance. A cited intervention increased *C. rodentium* colonization by approximately **three orders of magnitude** under a high-protein diet. Synthetic-community experiments further suggest that oxygen-respiring facultative anaerobes restore resistance to *S. Typhimurium*, making oxygen or alternative respiratory acceptors limiting ecological resources. (caballeroflores2023microbiotamediatedcolonizationresistance pages 3-4)

These are important ecosystem mechanisms, but they should be encoded as **community-mediated niche occupancy or pathogen exclusion**, not as evidence that an individual organism has the commensalism trait.

### Oxygen–SCFA–immune-axis evidence

Fachi et al. reported in 2024 that hyperbaric oxygen worsened antibiotic-associated dysbiosis and reduced microbiota-derived SCFAs. Butyrate supplementation improved epithelial integrity and ILC3 responses during *C. difficile* infection. Loss of HIF-1α in RORγt-positive cells abolished the protection, whereas stabilization of HIF-1 signaling through VHL deletion mitigated disease. This supports the causal sequence `oxygenation → loss of anaerobe-derived SCFAs → reduced HIF-1α/IL-22 ILC3 activity → impaired barrier`, with butyrate acting in the opposite direction. (fachi2024hyperbaricoxygenaugments pages 1-2)

The same paper notes that Firmicutes and Bacteroidetes together represent about **90% of the human gut microbiome** and are predominantly obligate anaerobes. This is useful ecological context, not a universal compositional constant across cohorts or methods. (fachi2024hyperbaricoxygenaugments pages 1-2)

### Improved host-like colonization assays

Costa et al. developed an open-source skin-like medium matching important features of healthy skin, including acidic pH. Human skin was reported at **pH 4.1–5.8**, and eccrine sweat production can reach **0.5–3.5 L/hour** across the body. Growth in this medium and acidic pH increased MRSA expression of adhesion/virulence functions and corneocyte adherence involving ClfA, SraP and Fnbps. *S. aureus* nasal carriage was estimated at **20–30%** of the population. (costa2024thestaphylococcusaureus pages 1-2)

This is a valuable real-world assay development, but it is a boundary example: improved adherence by a recognized pathogen is not evidence of commensalism and illustrates why adhesion must not be equated with a neutral host effect.

## 5. Quantitative evidence relevant to curation

- *B. thetaiotaomicron* monocolonization increased ex-vivo small-intestinal total IgA from **4.023 ± 0.660 μg/mL** in germ-free controls to **12.61 ± 1.068 μg/mL** at three weeks (`P=0.002`). Organism-specific IgA increased from OD405 **0.250 ± 0.008** to **0.718 ± 0.092** (`P=0.007`) and continued rising through week 12. These data establish a specific adaptive response to a colonizing commensal, but not host-effect neutrality. (joglekar2019intestinaligaregulates pages 3-4)
- In long-term *B. thetaiotaomicron* colonization, low-fiber feeding significantly reduced CPS2 (`P=0.0144`) and CPS4 (`P<0.0001`) expression and increased CPS6 (`P=0.0002`) during the first low-fiber period. CPS4 expression sometimes changed by as much as **62%**, demonstrating that capsule expression is dynamic and diet-dependent. (porter2017asubsetof pages 2-4)
- A 2024 colonization review reported *Lactobacillus delbrueckii* abundance of **11.3% versus 3.3%** with microbially enhanced soybean meal versus fish meal, illustrating diet-dependent abundance rather than proving a specific commensal mechanism. (lin2024areviewof pages 13-14)

## 6. Applications and real-world implementation

1. **Defined live biotherapeutics and probiotics.** Colonization determinants—capsules, adhesins, glycan-utilization systems, acid/bile resistance, and host-compatible nutrient niches—can improve strain persistence. Because persistence is strain-, diet-, immune-, and microbiome-dependent, personalized matching is more defensible than assigning a universal “commensal” program. (xiao2021gutcolonizationmechanisms pages 3-5, xiao2021gutcolonizationmechanisms pages 5-6)
2. **Prebiotic and dietary design.** Fiber and specific glycans can maintain mucus integrity and supply microbial substrates, but nutrient interventions can also favor pathogens or alter capsule expression. Dietary nodes should therefore be connected to defined organisms and measured outcomes rather than labeled generically beneficial. (lin2024areviewof pages 13-14, fekete2023theroleof pages 1-5, porter2017asubsetof pages 2-4)
3. **Microbiota-mediated infection prevention.** Rational communities can be assembled to saturate nutrient, oxygen, and trace-metal niches or produce inhibitory metabolites. This is an application of colonization resistance and is often mutualistically beneficial to the host, not strict commensalism. (caballeroflores2023microbiotamediatedcolonizationresistance pages 3-4)
4. **Mucosal therapeutics.** IgA coating, mucus glycosylation, and SCFA–HIF-1α–IL-22 signaling are potential levers for stabilizing spatially contained microbiota. Manipulation must preserve barrier separation and avoid selecting IgA-coated pathobionts. (donaldson2018gutmicrobiotautilize pages 3-4, fekete2023theroleof pages 1-5, fachi2024hyperbaricoxygenaugments pages 1-2)
5. **Host-mimetic assays.** Skin-like medium, mucus-producing epithelial systems, organoids, gnotobiotic models, and competitive transmission assays provide more realistic tests than nutrient-rich broth. A complete commensalism assay should add host-fitness endpoints to these colonization measurements. (donaldson2018gutmicrobiotautilize pages 2-3, costa2024thestaphylococcusaureus pages 1-2)

## 7. Expert interpretation and recommended YAML architecture

Authoritative reviews converge on three principles:

- **Interaction sign is continuous and dynamic.** Genetic changes, diet, age, inflammation, transmission mode, and community composition can move an association toward mutualism or parasitism. (drew2021microbialevolutionand pages 2-3)
- **Niche occupancy is multidimensional.** Nutrients, adhesion sites, oxygen/electron acceptors, immune factors, and spatial microenvironments jointly determine persistence. (caballeroflores2023microbiotamediatedcolonizationresistance pages 3-4)
- **Host containment is not simple immune ignorance.** IgA can actively foster association with some microbes while excluding or spatially restraining others. (donaldson2018gutmicrobiotautilize pages 2-3, donaldson2018gutmicrobiotautilize pages 3-4)

For `commensalism.yaml`, use a small conserved core and contextual branches:

- **Core outcome:** microbial benefit → stable host association; host-fitness effect ≈ 0.
- **Mucosal-retention branch:** `ccfA → capsules → IgA coating → mucus adherence/aggregation → stable colonization`.
- **Resource branch:** mucin/dietary glycans → uptake and catabolism → microbial growth/persistence.
- **Containment branch:** intact mucus glycosylation → spatial separation → low translocation/inflammation.
- **Community branch:** nutrient/electron-acceptor occupancy → exclusion of competitors/pathogens.
- **Context modifiers:** host genotype, immune state, diet, oxygen, antibiotics, anatomical site, microbial strain, and time.

Predicates should be explicit—`positively_regulates`, `enables`, `increases_adherence_to`, `increases_abundance_of`, `decreases_translocation_of`, or `associated_with`—rather than a vague `causes commensalism`. Add evidence codes or qualifiers for direct knockout/add-back, in-vitro assay, gnotobiotic animal, review synthesis, and inference.

## 8. Claims not yet ready for TraitMech curation

- **“A species is commensal” without host/site/context qualifiers.** The same strain may be neutral, beneficial, or pathogenic under different conditions.
- **Adhesion or colonization implies commensalism.** The *S. aureus* skin model directly demonstrates why this inference fails. (costa2024thestaphylococcusaureus pages 1-2)
- **IgA universally promotes commensal colonization.** It promoted *B. fragilis* and Rikenellaceae mucosal association but could reduce association of other taxa; the effect is antigen- and taxon-specific. (donaldson2018gutmicrobiotautilize pages 3-4)
- **Capsules are universally tolerance mechanisms.** Capsules may enhance competitive fitness, attract IgA, evade immunity, or contribute to virulence depending on structure and organism. (donaldson2018gutmicrobiotautilize pages 2-3, porter2017asubsetof pages 2-4)
- **SCFA production is evidence of strict commensalism.** Butyrate can benefit the host, which is more consistent with mutualism, and the strongest recent evidence came from an HBO/antibiotic/*C. difficile* disease model. (fachi2024hyperbaricoxygenaugments pages 1-2)
- **Colonization resistance is synonymous with commensalism.** It is a community function that benefits the host and may involve direct antagonism among microbes. (caballeroflores2023microbiotamediatedcolonizationresistance pages 3-4)
- **Host neutrality inferred from no reported pathology.** Curate only when an appropriately powered host-fitness or damage endpoint was measured and found equivalent within a stated margin.
- **Broad GO/CHEBI/ENVO mappings not verified against an ontology release.** Do not invent CURIEs. Label-only nodes are preferable to uncertain identifiers.

## DOI-first bibliography

1. **Lin Q, et al.** “A Review of the Mechanisms of Bacterial Colonization of the Mammal Gut.” *Microorganisms*. Published May 2024. https://doi.org/10.3390/microorganisms12051026 (lin2024areviewof pages 13-14)
2. **Fachi JL, et al.** “Hyperbaric oxygen augments susceptibility to *C. difficile* infection by impairing gut microbiota ability to stimulate the HIF-1α-IL-22 axis in ILC3.” *Gut Microbes*. Published 2024; accepted December 18, 2023. https://doi.org/10.1080/19490976.2023.2297872 (fachi2024hyperbaricoxygenaugments pages 1-2)
3. **Costa FG, et al.** “The *Staphylococcus aureus* regulatory program in a human skin-like environment.” *mBio*. Published March 28, 2024. https://doi.org/10.1128/mbio.00453-24 (costa2024thestaphylococcusaureus pages 1-2)
4. **Caballero-Flores G, Pickard JM, Núñez G.** “Microbiota-mediated colonization resistance: mechanisms and regulation.” *Nature Reviews Microbiology*. Volume 21, 347–360; issue publication 2023. https://doi.org/10.1038/s41579-022-00833-7 (caballeroflores2023microbiotamediatedcolonizationresistance pages 3-4)
5. **Fekete E, Buret AG.** “The role of mucin O-glycans in microbiota dysbiosis, intestinal homeostasis, and host-pathogen interactions.” *American Journal of Physiology—Gastrointestinal and Liver Physiology*. Published June 2023. https://doi.org/10.1152/ajpgi.00261.2022 (fekete2023theroleof pages 1-5)
6. **Drew GC, Stevens EJ, King KC.** “Microbial evolution and transitions along the parasite–mutualist continuum.” *Nature Reviews Microbiology*. Published 2021. https://doi.org/10.1038/s41579-021-00550-7 (drew2021microbialevolutionand pages 2-3)
7. **Xiao Y, et al.** “Gut Colonization Mechanisms of *Lactobacillus* and *Bifidobacterium*: An Argument for Personalized Designs.” *Annual Review of Food Science and Technology*. Published March 2021. https://doi.org/10.1146/annurev-food-061120-014739 (xiao2021gutcolonizationmechanisms pages 3-5, xiao2021gutcolonizationmechanisms pages 5-6)
8. **Joglekar P, et al.** “Intestinal IgA Regulates Expression of a Fructan Polysaccharide Utilization Locus in Colonizing Gut Commensal *Bacteroides thetaiotaomicron*.” *mBio*. Published November–December 2019. https://doi.org/10.1128/mbio.02324-19 (joglekar2019intestinaligaregulates pages 3-4)
9. **Donaldson GP, et al.** “Gut microbiota utilize immunoglobulin A for mucosal colonization.” *Science*. First released May 3, 2018. https://doi.org/10.1126/science.aaq0926 (donaldson2018gutmicrobiotautilize pages 2-3, donaldson2018gutmicrobiotautilize pages 3-4)
10. **Porter NT, et al.** “A Subset of Polysaccharide Capsules in the Human Symbiont *Bacteroides thetaiotaomicron* Promote Increased Competitive Fitness in the Mouse Gut.” *Cell Host & Microbe*. Published October 2017. https://doi.org/10.1016/j.chom.2017.08.020 (porter2017asubsetof pages 2-4)

**Bottom line:** curate the `ccfA–capsule–IgA–mucosal stability` chain as the best-supported mechanistic branch, but terminate it at **stable low-inflammatory host association**, not automatically at commensalism. The defining `host fitness essentially unaffected` edge remains an assay-level requirement that must be supplied by direct host-outcome evidence for each host–microbe–environment combination.

References

1. (drew2021microbialevolutionand pages 2-3): Georgia C. Drew, Emily J. Stevens, and Kayla C. King. Microbial evolution and transitions along the parasite–mutualist continuum. Nature Reviews. Microbiology, 19:623-638, Apr 2021. URL: https://doi.org/10.1038/s41579-021-00550-7, doi:10.1038/s41579-021-00550-7. This article has 405 citations.

2. (caballeroflores2023microbiotamediatedcolonizationresistance pages 12-14): Gustavo Caballero-Flores, Joseph M. Pickard, and Gabriel Núñez. Microbiota-mediated colonization resistance: mechanisms and regulation. Nature Reviews Microbiology, 21:347-360, Dec 2023. URL: https://doi.org/10.1038/s41579-022-00833-7, doi:10.1038/s41579-022-00833-7. This article has 532 citations and is from a highest quality peer-reviewed journal.

3. (xiao2021gutcolonizationmechanisms pages 3-5): Yue Xiao, Qixiao Zhai, Hao Zhang, Wei Chen, and Colin Hill. Gut colonization mechanisms of <i>lactobacillus</i> and <i>bifidobacterium</i>: an argument for personalized designs. Annual Review of Food Science and Technology, 12:213-233, Mar 2021. URL: https://doi.org/10.1146/annurev-food-061120-014739, doi:10.1146/annurev-food-061120-014739. This article has 136 citations and is from a domain leading peer-reviewed journal.

4. (xiao2021gutcolonizationmechanisms pages 5-6): Yue Xiao, Qixiao Zhai, Hao Zhang, Wei Chen, and Colin Hill. Gut colonization mechanisms of <i>lactobacillus</i> and <i>bifidobacterium</i>: an argument for personalized designs. Annual Review of Food Science and Technology, 12:213-233, Mar 2021. URL: https://doi.org/10.1146/annurev-food-061120-014739, doi:10.1146/annurev-food-061120-014739. This article has 136 citations and is from a domain leading peer-reviewed journal.

5. (xiao2021gutcolonizationmechanisms pages 7-9): Yue Xiao, Qixiao Zhai, Hao Zhang, Wei Chen, and Colin Hill. Gut colonization mechanisms of <i>lactobacillus</i> and <i>bifidobacterium</i>: an argument for personalized designs. Annual Review of Food Science and Technology, 12:213-233, Mar 2021. URL: https://doi.org/10.1146/annurev-food-061120-014739, doi:10.1146/annurev-food-061120-014739. This article has 136 citations and is from a domain leading peer-reviewed journal.

6. (costa2024thestaphylococcusaureus pages 1-2): Flavia G. Costa, Krista B. Mills, Heidi A. Crosby, and Alexander R. Horswill. The <i>staphylococcus aureus</i> regulatory program in a human skin-like environment. May 2024. URL: https://doi.org/10.1128/mbio.00453-24, doi:10.1128/mbio.00453-24. This article has 39 citations and is from a domain leading peer-reviewed journal.

7. (donaldson2018gutmicrobiotautilize pages 2-3): Gregory P. Donaldson, M. Ladinsky, Kristie B. Yu, Jon G. Sanders, Bryan B. Yoo, Wen-Chi Chou, M. Conner, A. Earl, Rob Knight, P. Bjorkman, and S. Mazmanian. Gut microbiota utilize immunoglobulin a for mucosal colonization. Science, 360:795-800, May 2018. URL: https://doi.org/10.1126/science.aaq0926, doi:10.1126/science.aaq0926. This article has 786 citations and is from a highest quality peer-reviewed journal.

8. (donaldson2018gutmicrobiotautilize pages 3-4): Gregory P. Donaldson, M. Ladinsky, Kristie B. Yu, Jon G. Sanders, Bryan B. Yoo, Wen-Chi Chou, M. Conner, A. Earl, Rob Knight, P. Bjorkman, and S. Mazmanian. Gut microbiota utilize immunoglobulin a for mucosal colonization. Science, 360:795-800, May 2018. URL: https://doi.org/10.1126/science.aaq0926, doi:10.1126/science.aaq0926. This article has 786 citations and is from a highest quality peer-reviewed journal.

9. (fekete2023theroleof pages 1-5): Elena Fekete and Andre G. Buret. The role of mucin <i>o</i>-glycans in microbiota dysbiosis, intestinal homeostasis, and host-pathogen interactions. Jun 2023. URL: https://doi.org/10.1152/ajpgi.00261.2022, doi:10.1152/ajpgi.00261.2022. This article has 68 citations.

10. (porter2017asubsetof pages 2-4): Nathan T. Porter, Pablo Canales, Daniel A. Peterson, and Eric C. Martens. A subset of polysaccharide capsules in the human symbiont bacteroides thetaiotaomicron promote increased competitive fitness in the mouse gut. Cell host & microbe, 22 4:494-506.e8, Oct 2017. URL: https://doi.org/10.1016/j.chom.2017.08.020, doi:10.1016/j.chom.2017.08.020. This article has 140 citations and is from a highest quality peer-reviewed journal.

11. (caballeroflores2023microbiotamediatedcolonizationresistance pages 3-4): Gustavo Caballero-Flores, Joseph M. Pickard, and Gabriel Núñez. Microbiota-mediated colonization resistance: mechanisms and regulation. Nature Reviews Microbiology, 21:347-360, Dec 2023. URL: https://doi.org/10.1038/s41579-022-00833-7, doi:10.1038/s41579-022-00833-7. This article has 532 citations and is from a highest quality peer-reviewed journal.

12. (fachi2024hyperbaricoxygenaugments pages 1-2): José L. Fachi, Laís. P. Pral, Helder C. Assis, Sarah Oliveira, Vinícius R. Rodovalho, Jefferson A. C. dos Santos, Mariane F. Fernandes, Valquíria A. Matheus, Renata Sesti-Costa, Paulo J. Basso, Marina Flóro e Silva, Niels O. S. Câmara, Selma Giorgio, Marco Colonna, and Marco A. R. Vinolo. Hyperbaric oxygen augments susceptibility to c. difficile infection by impairing gut microbiota ability to stimulate the hif-1α-il-22 axis in ilc3. Gut Microbes, Jan 2024. URL: https://doi.org/10.1080/19490976.2023.2297872, doi:10.1080/19490976.2023.2297872. This article has 29 citations and is from a peer-reviewed journal.

13. (joglekar2019intestinaligaregulates pages 3-4): Payal Joglekar, Hua Ding, Pablo Canales-Herrerias, Pankaj Jay Pasricha, Justin L. Sonnenburg, and Daniel A. Peterson. Intestinal iga regulates expression of a fructan polysaccharide utilization locus in colonizing gut commensal bacteroides thetaiotaomicron. Dec 2019. URL: https://doi.org/10.1128/mbio.02324-19, doi:10.1128/mbio.02324-19. This article has 48 citations and is from a domain leading peer-reviewed journal.

14. (lin2024areviewof pages 13-14): Qingjie Lin, Shiying Lin, Zitao Fan, Jing Liu, Dingcheng Ye, and Pingting Guo. A review of the mechanisms of bacterial colonization of the mammal gut. Microorganisms, 12:1026, May 2024. URL: https://doi.org/10.3390/microorganisms12051026, doi:10.3390/microorganisms12051026. This article has 43 citations.