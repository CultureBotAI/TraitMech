---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T15:20:46.824629'
end_time: '2026-08-04T15:27:53.627339'
duration_seconds: 426.8
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: nitrogen-fixing symbiosis
  trait_identifier: traitmech:000044
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: nitrogen_fixing_symbiosis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A mutualistic symbiosis in which a diazotrophic bacterium fixes atmospheric\
    \ N2 for a host plant \u2014 classically rhizobia in legume root nodules \u2014\
    \ in exchange for photosynthate."
  parent_traits: traitmech:000041
  synonyms: nitrogen-fixing symbiont, root-nodule symbiosis
  evidence_summary: 'DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe the free-living-to-endosymbiont
    transition of rhizobia that forms N2-fixing legume root nodules.) | DOI:10.1038/nrmicro2990:  (Oldroyd,
    "Speak, friend, and enter", supports the symbiotic signalling that establishes
    beneficial nitrogen-fixing plant-microbe associations.)'
  causal_graph_summary: 'rhizobia_legume_n2_fixation: 11 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** nitrogen-fixing symbiosis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000044
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A mutualistic symbiosis in which a diazotrophic bacterium fixes atmospheric N2 for a host plant — classically rhizobia in legume root nodules — in exchange for photosynthate.
- **Parent traits:** traitmech:000041
- **Synonyms:** nitrogen-fixing symbiont, root-nodule symbiosis
- **Existing evidence:** DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe the free-living-to-endosymbiont transition of rhizobia that forms N2-fixing legume root nodules.) | DOI:10.1038/nrmicro2990:  (Oldroyd, "Speak, friend, and enter", supports the symbiotic signalling that establishes beneficial nitrogen-fixing plant-microbe associations.)
- **Existing causal graph summary:** rhizobia_legume_n2_fixation: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **nitrogen-fixing symbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/nitrogen_fixing_symbiosis.yaml`.

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
- **Trait label:** nitrogen-fixing symbiosis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000044
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A mutualistic symbiosis in which a diazotrophic bacterium fixes atmospheric N2 for a host plant — classically rhizobia in legume root nodules — in exchange for photosynthate.
- **Parent traits:** traitmech:000041
- **Synonyms:** nitrogen-fixing symbiont, root-nodule symbiosis
- **Existing evidence:** DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe the free-living-to-endosymbiont transition of rhizobia that forms N2-fixing legume root nodules.) | DOI:10.1038/nrmicro2990:  (Oldroyd, "Speak, friend, and enter", supports the symbiotic signalling that establishes beneficial nitrogen-fixing plant-microbe associations.)
- **Existing causal graph summary:** rhizobia_legume_n2_fixation: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **nitrogen-fixing symbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/nitrogen_fixing_symbiosis.yaml`.

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


# Curation report: nitrogen-fixing symbiosis

## Trait record and scope

- **Trait label:** nitrogen-fixing symbiosis
- **Trait identifier:** `traitmech:000044`
- **Category / kind / status:** ECOLOGY / CLASS / REVIEWED
- **Parent:** `traitmech:000041`
- **Synonyms:** nitrogen-fixing symbiont; root-nodule symbiosis

### Operational definition

This trait is an **emergent, reciprocal plant–microbe phenotype** in which a host accommodates diazotrophic bacteria, supplies carbon and a controlled low-oxygen niche, and receives bacterially fixed nitrogen. In the canonical rhizobium–legume case, recognition and infection produce a root nodule containing differentiated bacteroids; nitrogenase reduces atmospheric N₂ to ammonia, while plant photosynthate—principally delivered to bacteroids as C4-dicarboxylates—supports the large respiratory and energetic cost. The host subsequently assimilates transferred fixed N through GS/GOGAT metabolism (lepetit2023controlofthe pages 1-2, ledermann2021howrhizobiaadapt pages 4-6, ledermann2021howrhizobiaadapt pages 7-9).

The graph’s terminal phenotype should therefore require all of the following:

1. compatible host–microbe association;
2. a differentiated, host-supported diazotrophic state;
3. active N₂ reduction under an oxygen regime compatible with nitrogenase;
4. net fixed-N transfer or nutritional benefit to the host; and
5. reciprocal host carbon/energy provision.

### Boundaries

**Include:** classical rhizobial root or stem nodules, provided effective N₂ fixation and host N transfer are demonstrated. Actinorhizal–*Frankia* symbioses fit the broad biological definition but use substantially different recognition and developmental machinery; they should be represented by a separate mechanism branch rather than forced through the legume Nod-factor pathway.

**Exclude or distinguish:**

- **Free-living diazotrophy:** nitrogenase activity without a reciprocal host association.
- **Associative/endophytic BNF:** include only where host benefit and fixed-N transfer are demonstrated; root colonization alone is insufficient.
- **Nodulation:** nodules can be ineffective; nodule count is not equivalent to nitrogen-fixing symbiosis.
- **Nitrogen fixation:** biochemical N₂ reduction alone does not establish mutualism.
- **Plant growth promotion:** phytohormone production, phosphate solubilization, or improved biomass without demonstrated symbiotic N fixation is a nearby but separate trait.
- **Engineered cereal-associated diazotrophs:** these are emerging applications, usually not root-nodule symbioses and often not yet equivalent to the canonical phenotype.

## Current mechanistic understanding

Canonical Nod-dependent symbiosis begins when compatible root flavonoids bind rhizobial NodD regulators and induce `nod`, `nol`, and `noe` genes. The resulting lipo-chitooligosaccharide Nod factors are recognized by host LysM receptor-like kinases. In model legumes, this induces nuclear/perinuclear Ca²⁺ oscillations; CCaMK/DMI3 decodes the signal, phosphorylates CYCLOPS/IPD3, and activates NIN-associated infection and nodule-organogenesis programs (lima2024expandingagriculturalpotential pages 1-2, dong2020thesignificanceof pages 3-5, ma2021nitrogenandphosphorus pages 2-4, dong2020thesignificanceof pages 5-7).

Following infection-thread progression and bacterial release, rhizobia differentiate into bacteroids inside plant-derived symbiosome membranes. Mature bacteroids are generally growth-arrested but metabolically active. In hosts such as *Medicago truncatula*, hundreds of nodule-specific cysteine-rich peptides drive terminal differentiation, including endoreduplication and cell enlargement; this mechanism is not universal among legumes (ledermann2021howrhizobiaadapt pages 6-7).

The nodule solves an oxygen paradox: nitrogenase Fe–S clusters are oxygen-sensitive, but ATP generation requires respiration. The cortex restricts free oxygen to approximately **11 nM**, compared with about **255 μM** in air-equilibrated water. Bacteroid FixNOQP/cbb3 oxidase has an oxygen Km of approximately **4–7 nM**, supporting respiration in that niche. Leghemoglobin buffers free oxygen and facilitates oxygen delivery; it should not be represented merely as eliminating oxygen (ledermann2021howrhizobiaadapt pages 6-7, ledermann2021howrhizobiaadapt pages 4-6).

Plant-delivered malate and succinate are major bacteroid carbon substrates. Their oxidation supplies reductant and ATP for nitrogenase, although downstream routes differ among rhizobia. Nitrogenase reduces N₂ to ammonia; bacteroid GS/GOGAT is commonly downregulated, favoring release rather than microbial reassimilation. Ammonia is the principal reported transferred product, but alanine and aspartate have also been observed, so a universal dedicated “ammonia-exporter” edge would be premature (lepetit2023controlofthe pages 1-2, ledermann2021howrhizobiaadapt pages 7-9).

## Candidate nodes grouped by type

Identifiers below are proposed only where the correspondence is stable. Species-specific genes and proteins should receive NCBITaxon-qualified UniProt identifiers during implementation rather than an unqualified generic accession.

### Organisms and biological structures

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| rhizobia | NCBITaxon label/group; no single taxon CURIE | Polyphyletic functional group; do not assign one species identifier. |
| legume host | `NCBITaxon:3803` (Fabaceae) | Narrow to host species for experimental edges. |
| root nodule | `GO:0009878` (nodule morphogenesis) for process; anatomy ontology preferred for structure | Process and anatomical structure must remain distinct. |
| bacteroid | label-only candidate | Differentiated rhizobial state, not a taxon. |
| symbiosome | `GO:0043663` (host cell part) is too broad; label-only preferred | Plant-derived membrane compartment containing bacteroids. |
| symbiosome membrane | label-only candidate | Do not equate with bacterial membrane. |
| infection thread | `GO:0009860` where applicable | Canonical entry route, but not universal. |
| nodule fixation zone | label-only candidate | Particularly appropriate for indeterminate nodules. |

### Signals, regulators, and developmental processes

| Candidate node | Suggested grounding | Note |
|---|---|---|
| root flavonoid | `CHEBI:47916` (flavonoid) | Specific compounds such as genistein should be grounded separately. |
| NodD | label plus taxon-qualified UniProt | LysR-family rhizobial transcriptional regulator. |
| nod genes / Nod-factor biosynthesis | KEGG/MetaCyc pathway where species-specific | `nodABC` encodes the conserved synthesis core. |
| Nod factor | CHEBI class search/curation required | Structure and decorations are strain-specific. |
| NFR1/NFR5 or LYK3/NFP receptors | taxon-qualified UniProt | Model-specific names for LysM receptor kinases. |
| calcium oscillation | `GO:0055086` is general calcium homeostasis; label-only event preferred | Avoid grounding a dynamic oscillation to a static ion term. |
| CCaMK/DMI3 | taxon-qualified UniProt | Calcium/calmodulin-dependent kinase. |
| CYCLOPS/IPD3 | taxon-qualified UniProt | CCaMK substrate/transcriptional regulator. |
| NIN | taxon-qualified UniProt | Master nodulation transcription factor in model legumes. |
| nodule organogenesis | `GO:0009878` | Host developmental process. |
| NCR peptides | label-only or individual UniProt entries | Restricted to particular inverted-repeat-lacking-clade legumes. |
| bacteroid differentiation | `GO:0043934` (sporulation-related terms inappropriate); label-only preferred | A symbiotic cell-state transition, not sporulation. |

### Metabolic and respiratory components

| Candidate node | Suggested grounding | Note |
|---|---|---|
| atmospheric dinitrogen | `CHEBI:17997` | Nitrogenase substrate/electron acceptor in the overall reduction. |
| ammonia | `CHEBI:16134` | Distinguish from ammonium, `CHEBI:28938`, according to pH/context. |
| nitrogenase complex | `GO:0016163` (nitrogenase activity); `EC:1.18.6.1` | Represent NifH/NifDK separately when gene resolution is needed. |
| ATP | `CHEBI:15422` | Required by nitrogenase turnover. |
| reduced ferredoxin/flavodoxin | CHEBI/UniProt species-specific | Electron donor class; exact physiological donor varies. |
| oxygen | `CHEBI:15379` | Both respiratory substrate and nitrogenase inhibitor. |
| microoxic condition | ENVO term to be verified; label-only acceptable | Quantitative oxygen concentration is preferable in evidence annotations. |
| leghemoglobin | taxon-qualified UniProt | Host oxygen buffer/carrier. |
| FixNOQP/cbb3 oxidase | `GO:0004129`; `EC:7.1.1.9` for cytochrome-c oxidase family, verify exact mapping | High-affinity terminal oxidase. |
| malate | `CHEBI:6650` | C4-dicarboxylate supplied to bacteroids. |
| succinate | `CHEBI:30031` | C4-dicarboxylate supplied to bacteroids. |
| DctA | taxon-qualified UniProt; transporter classification | C4-dicarboxylate transporter; curate only with direct species evidence. |
| GS/GOGAT pathway | `GO:0006542` for glutamine biosynthesis plus enzyme terms | Separate bacterial downregulation from host assimilation. |
| glutamine synthetase | `EC:6.3.1.2`; `GO:0004356` | Host and bacterium require distinct nodes. |
| glutamate synthase | EC depends on electron donor | Host assimilation module. |
| photosynthate/sucrose | sucrose `CHEBI:17992` | Long-distance carbon supply to nodules. |

### Environmental and experimental factors

- mineral-nitrogen availability, especially nitrate (`CHEBI:17632`);
- phosphorus availability/phosphate (`CHEBI:18367` for phosphate, with protonation caveats);
- plant nitrogen demand or N satiety;
- carbon allocation and photosynthetic capacity;
- drought, temperature, acidity, salinity, and pesticide exposure;
- compatible versus incompatible host genotype;
- rhizobial inoculation and strain competition;
- ^15N isotope dilution, ^15N natural abundance, acetylene-reduction assay, and nitrogenase activity;
- nodule number/weight, shoot N, percentage N derived from atmosphere, and total N fixed.

## Conservative core causal graph

The following compact graph is suitable as the starting point for `data/traits/ecology/nitrogen_fixing_symbiosis.yaml`.

| module | subject | predicate | object | confidence/caveat |
|---|---|---|---|---|
| Signal initiation | root flavonoids | activate | rhizobial NodD and nod gene expression | High; core Nod-dependent pathway in many rhizobium-legume symbioses, but host-range chemistry is strain-specific and some bradyrhizobial systems are partially Nod-independent (dong2020thesignificanceof pages 3-5, dong2020thesignificanceof pages 5-7) |
| Signal initiation | nod genes | produce | Nod factors | High; canonical nodulation signal, review-supported rather than single experiment here (lima2024expandingagriculturalpotential pages 1-2, dong2020thesignificanceof pages 3-5) |
| Host perception | Nod factor receptor | activates | calcium oscillations in root epidermal cells | High in model legumes; receptor names vary by taxon (ma2021nitrogenandphosphorus pages 2-4) |
| Symbiotic signaling | calcium oscillations and CCaMK-CYCLOPS signaling | activate | NIN | High in model legumes; conserved pathway, though mostly grounded from review synthesis here (ma2021nitrogenandphosphorus pages 2-4) |
| Organogenesis/infection | NIN | promotes | rhizobial infection and nodule organogenesis | High; strongest support in model legumes, broader extrapolation should be cautious (ma2021nitrogenandphosphorus pages 2-4) |
| Intracellular accommodation | infection thread-mediated infection | produces | bacteroid-containing symbiosome | Medium-High; broadly supported for rhizobium-legume endosymbiosis, but details vary by host and rhizobium lineage (lepetit2023controlofthe pages 1-2, dong2020thesignificanceof pages 3-5) |
| Oxygen control | microoxic nodule environment plus leghemoglobin | permits | low-O2 bacteroid respiration compatible with nitrogenase function | High; leghemoglobin facilitates O2 diffusion/buffering rather than simply eliminating O2 (ledermann2021howrhizobiaadapt pages 6-7, ledermann2021howrhizobiaadapt pages 4-6) |
| Carbon exchange | plant-delivered C4-dicarboxylates | fuel | bacteroid respiration | High; malate/succinate are major bacteroid carbon sources, but downstream catabolic routes differ among taxa (lepetit2023controlofthe pages 1-2, ledermann2021howrhizobiaadapt pages 7-9) |
| Nitrogen fixation | nitrogenase | reduces | N2 to ammonia | High; defining biochemical step of the trait (lima2024expandingagriculturalpotential pages 1-2, lepetit2023controlofthe pages 1-2) |
| Fixed-N transfer | ammonia from bacteroids | transfers to / is assimilated by | plant GS/GOGAT pathway | Medium; transfer to plant is core, but exact exported N form can vary and alanine/aspartate have also been reported (lepetit2023controlofthe pages 1-2, ledermann2021howrhizobiaadapt pages 7-9) |
| Host support | plant photosynthate | supports | symbiotic nitrogen fixation | High; plant carbon supply is essential, often via sugar allocation and dicarboxylate provision (lepetit2023controlofthe pages 1-2) |
| Systemic regulation | mineral-N satiety | inhibits / activates | nodulation inhibition and nodule senescence | High; whole-plant nitrogen demand strongly regulates symbiosis, with mechanism not fully resolved (lepetit2023controlofthe pages 1-2, lima2024expandingagriculturalpotential pages 5-6, lima2024expandingagriculturalpotential pages 4-5) |


*Table: This table summarizes 12 conservative, source-backed edges for a TraitMech causal graph of nitrogen-fixing symbiosis. It emphasizes widely supported mechanisms while flagging important caveats such as Nod-dependent exceptions, taxon specificity, and uncertainty in fixed-nitrogen export chemistry.*

## Expanded evidence-backed edge proposals

Snippets are intentionally short and closely paraphrase or quote the retrieved source text. “High” means broadly supported, not necessarily universal across all nitrogen-fixing plant symbioses.

| Subject | Predicate | Object | Evidence and supporting snippet | Curation note |
|---|---|---|---|---|
| compatible root flavonoid | activates | NodD-dependent nod-gene transcription | Dong & Song 2020: flavonoids interact with NodD and regulate `nod` transcription; genistein is described as a strong selective inducer (dong2020thesignificanceof pages 5-7). | **High, canonical Nod-dependent branch.** Compound–strain specificity should be retained. |
| nod genes | produce | Nod factors | de Lima et al. 2024: flavonoid-activated regulators upregulate `nod/nol/noe` genes “encoding Nod Factors” (lima2024expandingagriculturalpotential pages 1-2). | Review-derived; `nodABC` is the synthesis core, while substitutions alter host range. |
| Nod factor | binds/activates | host LysM receptor complex | Ma & Chen 2021 identify NFR1/NFR5 in *Lotus* and LYK3/NFP in *Medicago* as Nod-factor receptors (ma2021nitrogenandphosphorus pages 2-4). | **High in model legumes;** receptor composition is host-specific. |
| activated Nod-factor receptor pathway | induces | nuclear/perinuclear Ca²⁺ oscillations | Ma & Chen 2021: perception leads to oscillations involving DMI1, CNGC15 channels, and MCA8 (ma2021nitrogenandphosphorus pages 2-4). | Keep channel-level edges model-qualified. |
| Ca²⁺ oscillations | activate | CCaMK/DMI3 | Ma & Chen 2021: Ca²⁺ spikes are sensed by CCaMK/DMI3 (ma2021nitrogenandphosphorus pages 2-4). | Strong model-legume edge. |
| CCaMK/DMI3 | phosphorylates | CYCLOPS/IPD3 | Ma & Chen 2021 explicitly describes CCaMK phosphorylation of CYCLOPS/IPD3 (ma2021nitrogenandphosphorus pages 2-4). | Strong model-legume edge. |
| CYCLOPS/NSP-associated signaling | activates | NIN expression | Ma & Chen 2021 links CYCLOPS and NSP complexes to NIN activation (ma2021nitrogenandphosphorus pages 2-4). | Exact promoter logic differs by host. |
| NIN | promotes | infection and nodule organogenesis | Ma & Chen 2021: NIN activates genes needed for infection and cortical nodule organogenesis (ma2021nitrogenandphosphorus pages 2-4). | Do not reduce NIN to a bacterial-trait node; it is a host regulator. |
| Nod-factor signaling | induces | root-hair curling and infection-thread formation | Dong & Song 2020 describes Nod-factor recognition followed by root-hair curling and infection-thread formation (dong2020thesignificanceof pages 3-5). | **Canonical but not universal.** Crack entry and Nod-independent infection are boundary cases. |
| intracellular accommodation | produces | symbiosome-contained bacteroid | Lepetit & Brouquisse describe infection-zone differentiation into bacteroids; mature nodule fixation occurs in the bacteroid state (lepetit2023controlofthe pages 1-2). | Broad rhizobial branch; exact release route differs. |
| NCR peptides | promote | terminal bacteroid differentiation | Ledermann et al. 2021: NCR peptides inhibit FtsZ/disrupt ribosomal functions and promote endoreduplication and swelling (ledermann2021howrhizobiaadapt pages 6-7). | **Taxon-specific; optional branch only.** About 700 variants are reported in *M. truncatula*. |
| nodule cortex oxygen barrier | reduces | free O₂ in fixation zone | Free O₂ is reported near 11 nM versus ~255 μM in air-equilibrated water (ledermann2021howrhizobiaadapt pages 4-6). | Quantitative, review-synthesized value; avoid treating it as universal. |
| oxygen exposure | inhibits/damages | nitrogenase | Nitrogenase Fe–S clusters are described as highly oxygen-sensitive (ledermann2021howrhizobiaadapt pages 4-6). | Core biochemical constraint. |
| leghemoglobin | buffers and delivers | O₂ to respiring symbiosomes | Ledermann et al. state that leghemoglobin buffers free O₂ and facilitates diffusion rather than simply lowering O₂ (ledermann2021howrhizobiaadapt pages 6-7). | Use “buffers/facilitates delivery,” not “removes oxygen.” |
| FixNOQP/cbb3 oxidase | enables | respiration at nanomolar O₂ | FixNOQP has an O₂ Km of 4–7 nM; *Bradyrhizobium japonicum* mutants show marginal nitrogenase activity (ledermann2021howrhizobiaadapt pages 6-7, ledermann2021howrhizobiaadapt pages 4-6). | Strong but mutant evidence is taxon-specific. |
| plant C4-dicarboxylates | fuel | bacteroid central metabolism and respiration | Malate and succinate are identified as major bacteroid carbon sources (lepetit2023controlofthe pages 1-2, ledermann2021howrhizobiaadapt pages 7-9). | Core exchange edge; downstream malic-enzyme versus PCK/PK routing varies among species. |
| bacteroid respiration | supplies | ATP/reductant for nitrogenase | Microoxic metabolism remains high because nitrogen fixation is energy intensive (ledermann2021howrhizobiaadapt pages 6-7, ledermann2021howrhizobiaadapt pages 4-6). | Add direct stoichiometry only from a biochemical source. |
| nitrogenase | reduces | N₂ to ammonia/ammonium | Recent and authoritative reviews identify nitrogenase-mediated conversion as the defining biochemical step (lima2024expandingagriculturalpotential pages 1-2, lepetit2023controlofthe pages 1-2). | Ground reaction to `EC:1.18.6.1`; maintain protonation conventions. |
| repression of bacteroid GS/GOGAT | favors | fixed-N release to host | Bacteroid GS/GOGAT is largely downregulated relative to free-living cells, consistent with redirecting N to export (ledermann2021howrhizobiaadapt pages 7-9). | **Mechanistic interpretation:** curate as “contributes to” rather than strictly “causes.” |
| bacteroid fixed-N product | transfers to | plant compartment | Ammonia is the principal secretion product, while alanine/aspartate have also been reported (ledermann2021howrhizobiaadapt pages 7-9). | **Uncertain chemical form and transport route.** |
| plant GS/GOGAT | assimilates | transferred ammonium into amino acids | Lepetit & Brouquisse describe plant assimilation of rhizobial NH₄⁺ into amino acids (lepetit2023controlofthe pages 1-2). | Strong pathway-level edge. |
| plant photosynthate allocation | supports | symbiotic N₂ fixation | Plants reciprocally supply photosynthate/dicarboxylic acids to fuel fixation (lepetit2023controlofthe pages 1-2). | Central reciprocity edge. |
| mineral-N satiety | inhibits | nodule formation | When mineral N satisfies demand, nodule formation is inhibited (lepetit2023controlofthe pages 1-2). | Whole-plant/systemic context is essential. |
| mineral-N satiety | activates | nodule senescence | Adequate mineral N activates senescence of existing nodules (lepetit2023controlofthe pages 1-2). | Mechanistic intermediates remain incompletely resolved. |
| plant N deficit | stimulates | compensatory symbiotic N foraging | N limitation can systemically stimulate symbiotic root foraging and is correlated with changes in nodule sugar allocation (lepetit2023controlofthe pages 1-2). | Represent as systemic regulation, not a direct bacterial sensing edge. |

## Recent developments, applications, and data

### Established implementation: legume inoculation

Commercial rhizobial seed/soil inoculation and co-inoculation are established in soybean, common bean, pea, peanut, and forage legumes. Recent synthesis reports improved nodulation, fixation, and yield from soybean co-inoculation with *Bradyrhizobium* and *Azospirillum*; one co-inoculation treatment involving *Bacillus megaterium* increased N uptake by **31%**. However, only **20%** of surveyed classical rhizobial isolates were effective in one common-bean assessment, illustrating that rhizobial presence or nodulation cannot substitute for effectiveness testing (lima2024expandingagriculturalpotential pages 5-6, lima2024expandingagriculturalpotential pages 4-5).

Applied mineral N can suppress the phenotype: the 2024 synthesis recommends not exceeding **20 kg N ha⁻¹** in the cited soybean context because higher input inhibits nodulation. This is useful graph evidence for a nitrate/mineral-N inhibitory edge but should not be encoded as a universal threshold (lima2024expandingagriculturalpotential pages 5-6, lima2024expandingagriculturalpotential pages 4-5).

In a 2024 greenhouse experiment, rhizobia-inoculated field pea received 0–1,600 kg ha⁻¹ Humalite. Relative to controls, amendment increased average nodule weight **11–91%**, atmospheric-N contribution **8–14%**, total shoot N fixed **48–80%**, shoot/root biomass **13–54%**, seed number **8–16%**, and seed N fixed **7–22%**. These are promising quantitative effects, but they are controlled-environment results and do not establish a universal causal edge from humic substances to symbiosis (rathor2024thebiostimulatoryeffect pages 1-2).

### Cropping systems and non-legume associations

Legume–cereal intercropping can improve cereal N acquisition and reduce external N requirements, but N transfer pathways and effect size depend on crop combination, soil, and management. Inoculant performance is limited by high temperature, drought, acidity, and competition from native rhizobia—the long-recognized “rhizobial competition problem” (wu2024naturalnitrogenboosters pages 7-8).

For non-legumes, recent synthesis reports that *Azospirillum brasilense* reduced fertilizer requirements by **25%** in cited maize/wheat applications and *Azospirillum* reduced N fertilization by **20%** in a *Brachiaria* pasture example. These systems are usually associative plant-growth-promotion rather than canonical root-nodule symbiosis; the numerical results therefore should support application notes, not the core graph for `traitmech:000044` (lima2024expandingagriculturalpotential pages 4-5).

### Engineering outlook

The current expert consensus is that transferring robust fixation to cereals requires more than inserting `nif` genes. A successful system must coordinate oxygen protection, high ATP/reductant supply, regulated ammonia release, host colonization, and ecological competitiveness. Accordingly, engineered cereal diazotrophs and synthetic host–microbe signaling are important 2023–2024 research directions, but they should be marked **emerging/engineered** rather than treated as established root-nodule symbiosis. The canonical graph is valuable precisely because it exposes these coupled constraints: recognition, accommodation, microoxia, carbon allocation, nitrogenase biochemistry, and host assimilation cannot be optimized independently.

## Expert synthesis for graph design

1. **Represent two organisms explicitly.** Host NIN, leghemoglobin, photosynthate, and GS/GOGAT must not be assigned to the bacterium; NodD, Nod-factor synthesis, FixNOQP, and nitrogenase are microbial.
2. **Separate establishment from function.** A signaling/infection subgraph should converge on intracellular bacteroids; an exchange/physiology subgraph should converge on net host N acquisition.
3. **Make oxygen a dual-role node.** Low O₂ permits high-affinity respiration, whereas excess O₂ damages nitrogenase. A single “oxygen promotes/inhibits symbiosis” edge is biologically misleading.
4. **Use context-qualified branches.** NCR-mediated terminal differentiation is appropriate for *Medicago* and related hosts, but not as a universal prerequisite. Likewise, Nod-factor signaling is canonical rather than universal.
5. **Do not use nodulation as the graph endpoint.** The endpoint should require active N₂ fixation and host fixed-N acquisition; ineffective nodules are a critical negative control.
6. **Retain systemic host regulation.** Recent expert analysis places mature nodule activity within whole-plant nitrogen demand and carbon-allocation control, although the intervening molecular circuits remain incompletely understood (lepetit2023controlofthe pages 1-2).

## Warnings: claims not ready for unconditional TraitMech curation

- **Do not require Nod factors universally.** Some bradyrhizobial and alternative entry systems can nodulate through noncanonical or partly Nod-independent mechanisms; mechanisms remain incompletely resolved (dong2020thesignificanceof pages 3-5, dong2020thesignificanceof pages 13-15).
- **Do not make NCR peptides universal.** Terminal NCR-driven enlargement/endoreduplication is host-clade-specific (ledermann2021howrhizobiaadapt pages 6-7).
- **Do not curate a universal fixed-N exporter yet.** Ammonia is the dominant reported product, but amino acids are also reported and the membrane-crossing mechanism is system-dependent (ledermann2021howrhizobiaadapt pages 7-9).
- **Do not equate increased nodule number with increased fixation.** Ineffective nodules and poorly effective strains are common; direct ^15N, nitrogen-balance, or validated nitrogenase measurements are preferable.
- **Treat acetylene reduction as assay evidence, not the phenotype itself.** It measures nitrogenase activity indirectly and does not by itself demonstrate net N transfer to the plant.
- **Do not universalize oxygen concentrations or fertilizer thresholds.** The ~11 nM O₂ and ≤20 kg N ha⁻¹ values are system/context observations, not ontology-level constants (ledermann2021howrhizobiaadapt pages 4-6, lima2024expandingagriculturalpotential pages 4-5).
- **Do not curate humic amendment as a core mechanism.** The large 2024 effects came from one rhizobia-inoculated pea greenhouse study and require multi-site field validation (rathor2024thebiostimulatoryeffect pages 1-2).
- **Keep cereal PGPR and engineered diazotroph evidence outside the canonical graph** unless reciprocal fixed-N transfer and the defining symbiotic state are directly shown.
- **Avoid unverified CURIEs.** In particular, symbiosome, bacteroid differentiation, Nod-factor structural classes, and microoxic nodule conditions should remain label-only until ontology lookup confirms exact semantics.

## DOI-first bibliography

1. **Lepetit M, Brouquisse R.** “Control of the rhizobium–legume symbiosis by the plant nitrogen demand is tightly integrated at the whole plant level and requires inter-organ systemic signaling.” *Frontiers in Plant Science* 14. **Published 9 March 2023.** DOI: [10.3389/fpls.2023.1114840](https://doi.org/10.3389/fpls.2023.1114840) (lepetit2023controlofthe pages 1-2).
2. **de Lima JD et al.** “Expanding agricultural potential through biological nitrogen fixation: Recent advances and diversity of diazotrophic bacteria.” *Australian Journal of Crop Science*, 324–333. **Published June 2024.** DOI: [10.21475/ajcs.24.18.06.p4104](https://doi.org/10.21475/ajcs.24.18.06.p4104) (lima2024expandingagriculturalpotential pages 1-2, lima2024expandingagriculturalpotential pages 5-6, lima2024expandingagriculturalpotential pages 4-5).
3. **Rathor P et al.** “The biostimulatory effect of humic-based soil amendment on plant growth, root nodulation, symbiotic nitrogen fixation and yield of field pea.” *Journal of Sustainable Agriculture and Environment* 3. **Published September 2024.** DOI: [10.1002/sae2.70001](https://doi.org/10.1002/sae2.70001) (rathor2024thebiostimulatoryeffect pages 1-2).
4. **Ledermann R, Schulte CCM, Poole PS.** “How Rhizobia Adapt to the Nodule Environment.” *Journal of Bacteriology* 203(12). **Published May 2021.** DOI: [10.1128/JB.00539-20](https://doi.org/10.1128/JB.00539-20) (ledermann2021howrhizobiaadapt pages 6-7, ledermann2021howrhizobiaadapt pages 4-6, ledermann2021howrhizobiaadapt pages 7-9).
5. **Ma Y, Chen R.** “Nitrogen and Phosphorus Signaling and Transport During Legume–Rhizobium Symbiosis.” *Frontiers in Plant Science* 12. **Published June 2021.** DOI: [10.3389/fpls.2021.683601](https://doi.org/10.3389/fpls.2021.683601) (ma2021nitrogenandphosphorus pages 2-4).
6. **Dong W, Song Y.** “The Significance of Flavonoids in the Process of Biological Nitrogen Fixation.” *International Journal of Molecular Sciences* 21:5926. **Published August 2020.** DOI: [10.3390/ijms21165926](https://doi.org/10.3390/ijms21165926) (dong2020thesignificanceof pages 3-5, dong2020thesignificanceof pages 5-7, dong2020thesignificanceof pages 13-15).
7. **Poole P, Ramachandran V, Terpolilli J.** “Rhizobia: from saprophytes to endosymbionts.” *Nature Reviews Microbiology* 16:291–303. **Published 2018.** DOI: [10.1038/nrmicro.2017.171](https://doi.org/10.1038/nrmicro.2017.171). Foundational source supplied in the trait record.
8. **Oldroyd GED.** “Speak, friend, and enter: signalling systems that promote beneficial symbiotic associations in plants.” *Nature Reviews Microbiology* 11:252–263. **Published 2013.** DOI: [10.1038/nrmicro2990](https://doi.org/10.1038/nrmicro2990). Foundational source supplied in the trait record.

## Recommended YAML-level graph policy

Use the 12-edge artifact as the **conservative core**. Add model-qualified expansions for Ca²⁺ channels, CCaMK–CYCLOPS–NIN, NCR peptides, FixNOQP, and individual transporters only when each edge carries host species, rhizobial strain, assay, and DOI provenance. Encode evidence strength and uncertainty directly, and require the graph endpoint to be **host acquisition of bacterially fixed nitrogen under reciprocal carbon exchange**, rather than nodulation or nitrogenase expression alone.

References

1. (lepetit2023controlofthe pages 1-2): Marc Lepetit and Renaud Brouquisse. Control of the rhizobium–legume symbiosis by the plant nitrogen demand is tightly integrated at the whole plant level and requires inter-organ systemic signaling. Frontiers in Plant Science, Mar 2023. URL: https://doi.org/10.3389/fpls.2023.1114840, doi:10.3389/fpls.2023.1114840. This article has 105 citations.

2. (ledermann2021howrhizobiaadapt pages 4-6): Raphael Ledermann, Carolin C. M. Schulte, and Philip S. Poole. How rhizobia adapt to the nodule environment. May 2021. URL: https://doi.org/10.1128/jb.00539-20, doi:10.1128/jb.00539-20. This article has 112 citations and is from a peer-reviewed journal.

3. (ledermann2021howrhizobiaadapt pages 7-9): Raphael Ledermann, Carolin C. M. Schulte, and Philip S. Poole. How rhizobia adapt to the nodule environment. May 2021. URL: https://doi.org/10.1128/jb.00539-20, doi:10.1128/jb.00539-20. This article has 112 citations and is from a peer-reviewed journal.

4. (lima2024expandingagriculturalpotential pages 1-2): Julliane Destro de Lima, Adijailton José de Souza, Amanda Letícia Pit Nunes, Wesley Ribeiro Rivadavea, Geovanna Cristina Zaro, and Glacy Jaqueline da Silva. Expanding agricultural potential through biological nitrogen fixation: recent advances and diversity of diazotrophic bacteria. Australian Journal of Crop Science, pages 324-333, Jun 2024. URL: https://doi.org/10.21475/ajcs.24.18.06.p4104, doi:10.21475/ajcs.24.18.06.p4104. This article has 17 citations and is from a peer-reviewed journal.

5. (dong2020thesignificanceof pages 3-5): Wei Dong and Yuguang Song. The significance of flavonoids in the process of biological nitrogen fixation. International Journal of Molecular Sciences, 21:5926, Aug 2020. URL: https://doi.org/10.3390/ijms21165926, doi:10.3390/ijms21165926. This article has 148 citations.

6. (ma2021nitrogenandphosphorus pages 2-4): Yanlin Ma and Rujin Chen. Nitrogen and phosphorus signaling and transport during legume–rhizobium symbiosis. Frontiers in Plant Science, Jun 2021. URL: https://doi.org/10.3389/fpls.2021.683601, doi:10.3389/fpls.2021.683601. This article has 51 citations.

7. (dong2020thesignificanceof pages 5-7): Wei Dong and Yuguang Song. The significance of flavonoids in the process of biological nitrogen fixation. International Journal of Molecular Sciences, 21:5926, Aug 2020. URL: https://doi.org/10.3390/ijms21165926, doi:10.3390/ijms21165926. This article has 148 citations.

8. (ledermann2021howrhizobiaadapt pages 6-7): Raphael Ledermann, Carolin C. M. Schulte, and Philip S. Poole. How rhizobia adapt to the nodule environment. May 2021. URL: https://doi.org/10.1128/jb.00539-20, doi:10.1128/jb.00539-20. This article has 112 citations and is from a peer-reviewed journal.

9. (lima2024expandingagriculturalpotential pages 5-6): Julliane Destro de Lima, Adijailton José de Souza, Amanda Letícia Pit Nunes, Wesley Ribeiro Rivadavea, Geovanna Cristina Zaro, and Glacy Jaqueline da Silva. Expanding agricultural potential through biological nitrogen fixation: recent advances and diversity of diazotrophic bacteria. Australian Journal of Crop Science, pages 324-333, Jun 2024. URL: https://doi.org/10.21475/ajcs.24.18.06.p4104, doi:10.21475/ajcs.24.18.06.p4104. This article has 17 citations and is from a peer-reviewed journal.

10. (lima2024expandingagriculturalpotential pages 4-5): Julliane Destro de Lima, Adijailton José de Souza, Amanda Letícia Pit Nunes, Wesley Ribeiro Rivadavea, Geovanna Cristina Zaro, and Glacy Jaqueline da Silva. Expanding agricultural potential through biological nitrogen fixation: recent advances and diversity of diazotrophic bacteria. Australian Journal of Crop Science, pages 324-333, Jun 2024. URL: https://doi.org/10.21475/ajcs.24.18.06.p4104, doi:10.21475/ajcs.24.18.06.p4104. This article has 17 citations and is from a peer-reviewed journal.

11. (rathor2024thebiostimulatoryeffect pages 1-2): Pramod Rathor, Punita Upadhyay, Aman Ullah, Thomas D. Warkentin, Linda Yuya Gorim, and Malinda S. Thilakarathna. The biostimulatory effect of humic‐based soil amendment on plant growth, root nodulation, symbiotic nitrogen fixation and yield of field pea (pisum sativum l.). Journal of Sustainable Agriculture and Environment, Sep 2024. URL: https://doi.org/10.1002/sae2.70001, doi:10.1002/sae2.70001. This article has 11 citations and is from a peer-reviewed journal.

12. (wu2024naturalnitrogenboosters pages 7-8): Jiayi Wu and Shudan Yan. Natural nitrogen boosters: the symbiotic relationship between legumes and rhizobia. Molecular Soil Biology, Jan 2024. URL: https://doi.org/10.5376/msb.2024.15.0009, doi:10.5376/msb.2024.15.0009. This article has 5 citations.

13. (dong2020thesignificanceof pages 13-15): Wei Dong and Yuguang Song. The significance of flavonoids in the process of biological nitrogen fixation. International Journal of Molecular Sciences, 21:5926, Aug 2020. URL: https://doi.org/10.3390/ijms21165926, doi:10.3390/ijms21165926. This article has 148 citations.