---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:57:06.102215'
end_time: '2026-08-04T08:03:34.562834'
duration_seconds: 388.46
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: coccobacillus shaped
  trait_identifier: METPO:1000688
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: coccobacillus_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape intermediate between spherical cocci and elongated bacilli,
    typically appearing as short or plump rods.
  parent_traits: METPO:1000666
  synonyms: coccobacillus
  evidence_summary: 'DOI:10.1128/JB.187.1.54-64.2005: changes shape, from a rod to
    coccobacillus (Supports coccobacillus morphology as a short-rod state associated
    with cell-shape control in representative bacteria.)'
  causal_graph_summary: 'coccobacillus_shaped_short_rod_morphogenesis: 11 nodes, 10
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** coccobacillus shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000688
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape intermediate between spherical cocci and elongated bacilli, typically appearing as short or plump rods.
- **Parent traits:** METPO:1000666
- **Synonyms:** coccobacillus
- **Existing evidence:** DOI:10.1128/JB.187.1.54-64.2005: changes shape, from a rod to coccobacillus (Supports coccobacillus morphology as a short-rod state associated with cell-shape control in representative bacteria.)
- **Existing causal graph summary:** coccobacillus_shaped_short_rod_morphogenesis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **coccobacillus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/coccobacillus_shaped.yaml`.

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
- **Trait label:** coccobacillus shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000688
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape intermediate between spherical cocci and elongated bacilli, typically appearing as short or plump rods.
- **Parent traits:** METPO:1000666
- **Synonyms:** coccobacillus
- **Existing evidence:** DOI:10.1128/JB.187.1.54-64.2005: changes shape, from a rod to coccobacillus (Supports coccobacillus morphology as a short-rod state associated with cell-shape control in representative bacteria.)
- **Existing causal graph summary:** coccobacillus_shaped_short_rod_morphogenesis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **coccobacillus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/coccobacillus_shaped.yaml`.

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


# Curation report: coccobacillus-shaped morphology

## Executive summary

**Target:** **coccobacillus shaped** (`METPO:1000688`), morphology class, reviewed; parent `METPO:1000666`.

The trait denotes a cell whose longitudinal axis remains discernible but is only modestly longer than its width—a short, squat, or plump rod intermediate between a bacillus and a coccus. It is a geometric phenotype, not a single conserved pathway. The strongest mechanistic evidence supports at least three context-specific routes:

1. **Physiological remodeling:** *Rhodobacter sphaeroides* changes from rods during aerobic growth to coccobacilli during photoheterotrophic growth; lower light increases the spherical character.
2. **Maintenance of an intrinsic short-rod state:** in *Acinetobacter baumannii*, zinc-stabilized PBP2 and the RodA–PBP2 elongasome maintain the characteristic short, squat rod. Loss of this machinery moves cells beyond the target state toward spheres.
3. **Evolutionary reduction of elongation:** stepwise loss of `yacF` and elongasome genes can drive rod/coccobacillus-to-coccus transitions in Neisseriaceae and Moraxellaceae.

Accordingly, the best TraitMech model should represent **balanced lateral peptidoglycan elongation relative to septal growth** as the proximal shape mechanism, while keeping physiological, genetic, and evolutionary branches taxon-scoped. Peptidoglycan principally determines cell shape, and RodA/PBP2 extend the longitudinal axis by inserting lateral-wall material. (slovak2005localizationofmreb pages 1-2, micelli2023aconservedzincbinding pages 1-2)

## 1. Trait scope and boundaries

### Operational definition

Curate `METPO:1000688` when microscopy or an authoritative taxonomic description identifies cells as **coccobacilli, short rods, squat rods, or plump rods**, ideally with images or length/width measurements. The phenotype may be constitutive or conditional. In *A. baumannii*, the experimentally described wild-type state is “short, squat rods”; in *R. sphaeroides*, photoheterotrophic cells are expressly “coccobacillus shaped.” (slovak2005localizationofmreb pages 1-2, micelli2023aconservedzincbinding pages 4-6)

### Boundary cases

- **Coccus/spherical:** no sustained long axis. The spherical Δ`pbp2` phenotype in *A. baumannii* is an **out-of-class endpoint**, useful as loss-of-trait evidence but not as a positive instance of `METPO:1000688`. (micelli2023aconservedzincbinding pages 4-6)
- **Ordinary bacillus/rod:** clearly elongated cells with a larger aspect ratio. Aerobic *R. sphaeroides* is the contrasting rod state. (slovak2005localizationofmreb pages 1-2)
- **Filament:** excessive length or failed septation; not coccobacillary. Piperacillin–tazobactam-associated filamentation should not be mapped to this trait. (micelli2023aconservedzincbinding pages 4-6)
- **Localized bulging/swelling:** amdinocillin produces mid-cell bulges in *R. sphaeroides*. This is evidence about PBP2-directed side-wall elongation, but it is not itself evidence for a uniform coccobacillus phenotype. (slovak2005localizationofmreb pages 7-10)
- **Pleomorphism:** a heterogeneous population should receive the coccobacillus trait only if that state is explicitly observed and its frequency or growth condition is recorded.
- **Taxonomic label versus measured state:** calling a genus “coccobacillary” does not prove that every strain or growth condition has the same morphology.

### Recommended assay representation

Record growth phase, medium, oxygen regime, illumination, temperature, perturbation, imaging method, cell count, median length, median width, and aspect-ratio distribution. “Short rod” without measurements is acceptable but weaker. A universal numerical aspect-ratio cutoff is not supported by the retrieved literature and should not be invented.

## 2. Candidate graph nodes

### Trait and phenotype nodes

- **coccobacillus shaped** — `METPO:1000688`
- short/squat rod — label-only synonym or narrower assay description
- rod-shaped cell — label-only unless an approved METPO identifier is verified
- spherical/coccal cell — label-only contrasting phenotype
- increased cell width — label-only quantitative phenotype
- bacterial cell morphogenesis — `GO:0000902`

### Taxa

- *Acinetobacter baumannii* — `NCBITaxon:470`
- *Rhodobacter sphaeroides* — `NCBITaxon:1063`
- *Neisseria elongata* — use label-only until the intended strain-level taxon is verified
- Neisseriaceae and Moraxellaceae — label-only unless exact taxonomic CURIEs are validated during YAML curation

### Genes, proteins, and complexes

- `pbp2` / penicillin-binding protein 2 (PBP2; class-B PBP transpeptidase) — label-only; use a strain-specific UniProt identifier only after sequence verification
- `rodA` / RodA, SEDS-family peptidoglycan glycosyltransferase — label-only
- RodA–PBP2 complex — label-only complex
- elongasome/rod system — label-only cellular machinery
- `mreB`, `mreC`, `mreD`, `rodZ` — label-only
- `yacF` / ZapD — label-only; note nomenclature and taxon dependence
- `pbpC` — label-only because gene naming can be taxon-specific
- divisome, PBP3/FtsI, FtsZ ring — label-only supporting nodes

### Chemicals and perturbations

- zinc(2+) — `CHEBI:29105`
- TPEN zinc chelator — label-only pending exact ChEBI verification
- amdinocillin/mecillinam — label-only pending exact ChEBI verification
- carbapenems — label-only drug class
- sulbactam and piperacillin–tazobactam — label-only; relevant chiefly to antibiotic susceptibility or septal-PG stress, not positive trait induction
- D350A, D365A, H371A, C384A PBP2 variants — label-only experimental alleles
- `pbp2` deletion and wild-type complementation — experimental-factor nodes

### Processes and cellular locations

- peptidoglycan biosynthetic process — `GO:0009252`
- lateral peptidoglycan insertion/side-wall elongation — label-only
- peptidoglycan transglycosylation — label-only unless the precise GO/Rhea term is verified
- peptidoglycan transpeptidation/cross-linking — label-only
- septal/polar peptidoglycan synthesis — label-only
- lateral cell wall, mid-cell, septation site, periplasm — label-only candidate locations
- cytoplasmic-membrane invagination/photosynthetic membrane formation — label-only

### Environmental and growth-state nodes

- aerobic growth
- photoheterotrophic growth
- low-light condition
- zinc deprivation
- logarithmic growth phase

These should remain label-only experimental/environmental nodes unless exact ENVO or condition-ontology terms are verified.

## 3. Evidence-backed candidate edges

The strongest concise edge set is summarized below.

| Subject | Predicate | Object | Taxon/context | Evidence strength |
|---|---|---|---|---|
| Photoheterotrophic growth | promotes | coccobacillus shape | *Rhodobacter sphaeroides*; switch from aerobic to photoheterotrophic growth (slovak2005localizationofmreb pages 1-2) | Direct phenotype observation |
| Low light | increases | spherical character of coccobacillus morphology | *R. sphaeroides* photoheterotrophic growth; light-dependent extent of shape change (slovak2005localizationofmreb pages 1-2) | Associative/context-dependent |
| Functional PBP2 zinc coordination | enables | short-rod/coccobacillary morphology | *Acinetobacter baumannii* PBP2-dependent elongasome function in vivo (micelli2023aconservedzincbinding pages 4-6, micelli2023aconservedzincbinding pages 6-7) | Direct genetic/biochemical |
| `pbp2` deletion | causes | spherical widened cells | *A. baumannii* Δ`pbp2`; ~30% median width increase (micelli2023aconservedzincbinding pages 4-6) | Direct genetic |
| WT `pbp2` complementation | restores | short-rod shape | *A. baumannii* Δ`pbp2` + PBP2-WT plasmid (micelli2023aconservedzincbinding pages 4-6) | Direct complementation |
| PBP2 D350A/D365A/H371A/C384A variants | fails to restore | short-rod shape | *A. baumannii* Δ`pbp2` expressing zinc-site mutants (micelli2023aconservedzincbinding pages 4-6, micelli2023aconservedzincbinding pages 6-7) | Direct complementation failure |
| TPEN zinc chelation | causes | round morphology | *A. baumannii* grown with zinc chelator TPEN (micelli2023aconservedzincbinding pages 7-8) | Direct perturbation |
| RodA–PBP2 complex | catalyzes | lateral peptidoglycan elongation | Rod-shaped bacteria including *A. baumannii* elongasome; dispersed lateral wall insertion (micelli2023aconservedzincbinding pages 1-2, slovak2005localizationofmreb pages 1-2) | Direct for process; trait link inferred |
| Stepwise loss of `yacF` then `mreBCD`/`pbpC`/`rodA`/`rodZ` | causes | rod/coccobacillus-to-coccus transition | Neisseriaceae/Moraxellaceae evolutionary and in vitro deletion context (caccamo2018themolecularbasis pages 7-9) | Direct in vitro + comparative evolutionary |
| Amdinocillin (PBP2 inhibitor) | causes | mid-cell swelling with MreB-localized bulges | *R. sphaeroides*; identifies PBP2-linked elongation sites rather than coccobacillus state itself (slovak2005localizationofmreb pages 7-10, slovak2005localizationofmreb pages 1-2) | Direct but indirect to target trait |


*Table: This table summarizes the strongest curation-ready and near-curation-ready causal edges linked to coccobacillus-shaped morphology across key taxa. It distinguishes direct experimental evidence from associative or inferred links so curators can prioritize robust TraitMech entries.*

### Expanded evidence table

| Proposed subject–predicate–object | Reference | Supporting source text | Curation interpretation |
|---|---|---|---|
| photoheterotrophic growth **promotes** `METPO:1000688` | Slovak et al., 2005 | “*Rhodobacter sphaeroides changes shape, from a rod to coccobacillus … when it switches from aerobic to photoheterotrophic growth*.” | **Strong, direct, taxon-specific.** Best positive trait edge from the supplied evidence. The paper establishes the condition-dependent transition but not the complete signaling pathway. (slovak2005localizationofmreb pages 1-2) |
| low light **increases spherical character of** coccobacillus morphology | Slovak et al., 2005 | “*The extent of the coccobacillus morphology is dependent on the available light, with low light levels producing a more pronounced spherical shape*.” | **Moderate.** Direct observational condition–phenotype relation; use “increases” rather than asserting a molecular mechanism. Low light may move cells toward the coccus boundary. (slovak2005localizationofmreb pages 1-2) |
| photoheterotrophic growth **is associated with** cytoplasmic-membrane invagination | Slovak et al., 2005 | Photoheterotrophic cells undergo extensive membrane invagination supporting the photosynthetic apparatus. | **Association only.** Do not state that invagination causes coccobacillary shape; both accompany the metabolic switch. (slovak2005localizationofmreb pages 1-2) |
| RodA–PBP2 complex **catalyzes** lateral peptidoglycan synthesis | Micelli et al., 2023 | “*RodA catalyzes PG transglycosylation in concert with the PG cross-linking activity of PBP2*”; elongasomes insert PG at dispersed lateral-wall sites. | **Strong process edge.** Provides the proximal cell-wall mechanism, but coccobacillary geometry arises from the balance of elongation and division rather than this reaction alone. (micelli2023aconservedzincbinding pages 1-2) |
| PBP2 zinc coordination **enables** elongasome-supported short-rod morphology | Micelli et al., 2023 | The PBP2 structure revealed an intrinsic zinc site required for stability; zinc-site mutations caused loss of rod shape. | **Strong, direct, *A. baumannii*-specific.** Suitable for a positive maintenance branch: zinc → stable/functional PBP2 → PG elongation → short-rod state. (micelli2023aconservedzincbinding pages 1-2, micelli2023aconservedzincbinding pages 6-7) |
| `pbp2` deletion **causes** spherical widened cells | Micelli et al., 2023 | Δ`pbp2` cells were spherical and had an approximately **30% median increase in maximal width**. | **Strong direct genetic evidence**, but the object is loss of the target trait, not acquisition. Represent as `pbp2` loss → decreased lateral elongation → spherical morphology, or functional PBP2 → maintains target. (micelli2023aconservedzincbinding pages 4-6) |
| wild-type `pbp2` complementation **restores** short-rod morphology | Micelli et al., 2023 | Plasmid-borne wild-type PBP2 “*restored a short-rod shape and reduced cell width to that seen with the WT strain*.” | **Strong rescue evidence.** This is the cleanest causal support for PBP2 maintaining the native coccobacillary/short-rod state. (micelli2023aconservedzincbinding pages 4-6) |
| PBP2 D350A/D365A/H371A/C384A **prevents restoration of** short-rod morphology | Micelli et al., 2023 | None of the four zinc-impaired variants reverted the spherical, widened Δ`pbp2` phenotype, despite robust expression. | **Strong structure–function evidence.** Encode each mutation separately only if TraitMech supports allele nodes; otherwise group as “PBP2 zinc-site disruption.” (micelli2023aconservedzincbinding pages 4-6) |
| PBP2 zinc-site disruption **decreases** zinc binding and protein stability | Micelli et al., 2023 | Zn:PBP2 molar ratios were WT **1.03**, D350A **0.58**, D365A **0.42**, H371A **0.29**, and C384A **0.06**; ΔTm values were −12.00, −8.07, −14.78, and −17.90 °C, respectively. | **Strong biochemical intermediate.** Supports zinc coordination → PBP2 stability/function. Bocillin binding remained detectable, so complete catalytic unfolding should not be inferred. (micelli2023aconservedzincbinding pages 6-7, micelli2023aconservedzincbinding pages 4-6) |
| zinc deprivation/TPEN **promotes** round morphology | Micelli et al., 2023 | Carbapenem exposure or zinc-deprived growth causes a rod-to-sphere transition; TPEN-treated cultures showed round morphology. | **Direct perturbation but endpoint is spherical.** Useful for a loss-of-trait branch and antimicrobial mechanism, not as a positive coccobacillus edge. TPEN may have effects beyond PBP2. (micelli2023aconservedzincbinding pages 7-8, micelli2023aconservedzincbinding pages 1-2) |
| carbapenem-mediated PBP2 inhibition **promotes** rod-to-sphere transition | Micelli et al., 2023 | Carbapenems preferentially acylate PBP2 and block RodA–PBP2 transpeptidase function; exposure causes rod-to-sphere transition. | **Strong but pharmacological and taxon-specific.** Curate only if inhibitory edges and out-of-trait endpoints belong in the graph. (micelli2023aconservedzincbinding pages 1-2) |
| MreB **participates in** control of peptidoglycan deposition/cell width | Slovak et al., 2005 | GFP–MreB perturbation yielded ~**20%** increased width in mildly abnormal cells and ~**33%** increased width plus ~**23%** increased length in severely abnormal cells. | **Moderate.** Fusion-induced abnormalities and inability to delete `mreB` support functional importance, but do not prove that MreB localization causes the physiological rod-to-coccobacillus switch. (slovak2005localizationofmreb pages 7-10, slovak2005localizationofmreb pages 1-2) |
| amdinocillin inhibition of PBP2 **causes** mid-cell bulging | Slovak et al., 2005 | Wild-type and GFP–MreB cells “*bulged at mid-cell in the presence of amdinocillin*”; MreB remained localized at the swellings. | **Direct but indirect to target.** Supports PBP2-mediated side-wall elongation and MreB-associated PG control, not coccobacillary morphology per se. (slovak2005localizationofmreb pages 7-10) |
| loss of `yacF`, then `mreBCD`/`pbpC`/`rodA`/`rodZ` **drives** rod/coccobacillus-to-coccus transition | Caccamo & Brun, 2018, summarizing deletion and comparative-genomic evidence | The phenotype was duplicated in rod-shaped *N. elongata* by stepwise deletion; related lineages show convergent loss leading to “*coccobacillus-to-coccus shape*.” | **Moderate-to-strong but secondary-source and lineage-specific.** Valuable as an evolutionary branch; retrieve and curate the original primary study before committing individual gene-loss edges. (caccamo2018themolecularbasis pages 7-9) |
| reduced lateral PG / enriched septal-polar PG **is associated with** coccal transition | Caccamo & Brun, 2018 | Rod-to-coccus evolution showed increased pentapeptide-rich septal/polar PG and decreased tetrapeptide-rich lateral PG. | **Moderate association.** Do not generalize pentapeptide/tetrapeptide ratios to all coccobacilli without direct muropeptide measurements. (caccamo2018themolecularbasis pages 7-9) |

## 4. Recommended minimal TraitMech graph

A conservative graph can fit the existing 11-node/10-edge scale:

1. zinc(2+) (`CHEBI:29105`)
2. PBP2 zinc coordination
3. stable/functional PBP2
4. RodA–PBP2 elongasome
5. lateral peptidoglycan synthesis (`GO:0009252`, broader process)
6. longitudinal cell-wall elongation
7. balanced elongation relative to septal growth
8. coccobacillus shaped (`METPO:1000688`)
9. photoheterotrophic growth
10. low-light condition
11. spherical/coccal morphology

Recommended core edges:

- zinc(2+) → **enables** → PBP2 zinc coordination
- PBP2 zinc coordination → **stabilizes** → PBP2
- stable PBP2 + RodA → **enables** → elongasome-directed lateral PG synthesis
- lateral PG synthesis → **promotes** → longitudinal wall elongation
- limited/balanced longitudinal elongation relative to division → **produces/maintains** → `METPO:1000688` **[mechanistic synthesis; uncertain as a universal edge]**
- `pbp2` deletion or zinc-site disruption → **decreases** → functional lateral elongation
- decreased lateral elongation → **promotes** → spherical morphology
- photoheterotrophic growth → **promotes** → `METPO:1000688` in *R. sphaeroides*
- low light → **increases** → spherical character under photoheterotrophic growth

Keep the *R. sphaeroides* environmental branch and *A. baumannii* PBP2–zinc branch explicitly taxon-scoped; the available evidence does not show that photoheterotrophic remodeling acts through PBP2 zinc coordination.

## 5. Recent developments, applications, and expert interpretation

### 2023 advance

Micelli et al. supplied the principal recent mechanistic advance: a 2.65-Å PBP2 structure revealed a previously unrecognized zinc site connecting metal homeostasis to elongasome-dependent shape. Four coordinating-residue substitutions progressively reduced zinc occupancy, destabilized PBP2, failed morphological complementation, and increased β-lactam susceptibility. Morphometry used at least **154 cells per group**, with mutant-versus-WT-complement differences at **P < 0.0001**. The authors found the motif across all **72 validly named Acinetobacter species** examined and in many β- and γ-proteobacterial PBP2 orthologs, although sequence-based conservation is not direct functional proof outside tested *A. baumannii*. (micelli2023aconservedzincbinding pages 1-2, micelli2023aconservedzincbinding pages 6-7, micelli2023aconservedzincbinding pages 4-6)

### 2024 literature assessment

The retrieved 2024 literature did not add a comparably direct molecular mechanism for the target trait. A 2024 confined-community study treated bacillary and rounder coccobacillary shapes as experimentally distinct morphologies affecting spatial organization, illustrating an ecological application of shape phenotypes, but it does not establish a molecular cause of `METPO:1000688`. It should therefore not supply core mechanistic edges.

### Real-world relevance

- **Antimicrobial pharmacology:** PBP2 is a β-lactam target. Zinc-site disruption phenocopied loss of shape function and sensitized cells to divisome-targeting β-lactams, suggesting combined interference with zinc-dependent PG synthesis and β-lactam-resistance machinery as a possible strategy. This remains a research direction, not a validated clinical implementation. (micelli2023aconservedzincbinding pages 1-2, micelli2023aconservedzincbinding pages 6-7, micelli2023aconservedzincbinding pages 4-6)
- **Host nutritional immunity:** host-imposed zinc limitation can stress bacterial PG homeostasis, making metal availability a biologically relevant environmental input rather than merely a laboratory perturbation. The precise contribution of PBP2 to morphology in vivo still requires testing. (micelli2023aconservedzincbinding pages 6-7)
- **Phenotypic susceptibility testing:** rod-to-round transitions can report elongasome/PBP2 inhibition, whereas filamentation reports septal-PBP stress. Morphology can therefore help discriminate cell-wall drug effects, but it is not alone target-specific. (micelli2023aconservedzincbinding pages 1-2, micelli2023aconservedzincbinding pages 4-6)
- **Ecophysiological adaptation:** *R. sphaeroides* couples photosynthetic membrane development and coccobacillary morphology to photoheterotrophic conditions and light availability. The causal mediator between illumination and altered geometry remains unresolved. (slovak2005localizationofmreb pages 1-2)
- **Comparative genomics:** recurrent loss of elongasome components can identify evolutionary transitions toward coccal forms, but comparative correlation should be paired with deletion/rescue evidence before graph curation. (caccamo2018themolecularbasis pages 7-9)

The expert synthesis is that bacterial shape is an emergent output of spatially partitioned PG synthesis and remodeling. No universal “coccobacillus gene” exists: similar geometry can result from a naturally short elongation program, environmentally regulated remodeling, partial reduction of elongasome output, or an evolutionary intermediate toward cocci. The review literature explicitly cautions that adaptive explanations for shape require direct observation of selection rather than genomic correlation alone. (caccamo2018themolecularbasis pages 7-9)

## 6. Warnings: claims not yet ready for TraitMech

1. **Do not curate “MreB localization causes coccobacillus shape.”** MreB remained at mid-cell in both long aerobic and shorter photoheterotrophic cells; the localization pattern did not explain the transition. (slovak2005localizationofmreb pages 1-2, slovak2005localizationofmreb pages 7-10)
2. **Do not equate spheres with coccobacilli.** Δ`pbp2`, carbapenem, TPEN, and severe elongasome-loss endpoints are spherical/coccal and represent loss or overshoot of the target state. (micelli2023aconservedzincbinding pages 7-8, micelli2023aconservedzincbinding pages 1-2, micelli2023aconservedzincbinding pages 4-6)
3. **Do not claim membrane invagination causes shape change.** It is concurrent with photoheterotrophic growth, with no intervention separating the two effects. (slovak2005localizationofmreb pages 1-2)
4. **Do not generalize the PBP2 zinc mechanism to all bacteria.** Conservation suggests broader relevance, but direct functional tests were in *A. baumannii*; Moraxella and Psychrobacter even show motif substitutions predicted to prevent coordination. (micelli2023aconservedzincbinding pages 6-7, micelli2023aconservedzincbinding pages 4-6)
5. **Do not make TPEN synonymous with selective PBP2 inhibition.** Chelation perturbs many zinc-dependent proteins and pathways.
6. **Do not curate individual Neisseriaceae gene-loss edges solely from the review.** Obtain the cited primary deletion/comparative study and identify which deletion produces rod-to-coccobacillus versus coccobacillus-to-coccus transitions. (caccamo2018themolecularbasis pages 7-9)
7. **Do not universalize PG pentapeptide/tetrapeptide composition.** The reported enrichment describes particular evolutionary lineages and transitions, not a diagnostic chemical definition of all coccobacilli. (caccamo2018themolecularbasis pages 7-9)
8. **Do not assign unverified UniProt, EC, Rhea, KEGG, MetaCyc, ChEBI, ENVO, or taxon CURIEs.** Strain-specific proteins and exact chemical forms require database validation.
9. **Do not infer adaptive benefit from morphology alone.** Shape-associated niche patterns and mechanical sorting are hypotheses or context-dependent observations, not proof that coccobacillary shape was selected for a particular function. (caccamo2018themolecularbasis pages 7-9)

## DOI-first bibliography

1. **Micelli C, Dai Y, Raustad N, et al.** “A conserved zinc-binding site in *Acinetobacter baumannii* PBP2 required for elongasome-directed bacterial cell shape.” *Proceedings of the National Academy of Sciences* 120(8), e2215237120. **Published February 14, 2023.** DOI: [10.1073/pnas.2215237120](https://doi.org/10.1073/pnas.2215237120). Primary structural, biochemical, genetic-complementation, microscopy, and susceptibility evidence. (micelli2023aconservedzincbinding pages 1-2, micelli2023aconservedzincbinding pages 6-7, micelli2023aconservedzincbinding pages 4-6)
2. **Slovak PM, Wadhams GH, Armitage JP.** “Localization of MreB in *Rhodobacter sphaeroides* under conditions causing changes in cell shape and membrane structure.” *Journal of Bacteriology* 187(1):54–64. **Published January 2005.** DOI: [10.1128/JB.187.1.54-64.2005](https://doi.org/10.1128/JB.187.1.54-64.2005). Primary evidence for aerobic rod-to-photoheterotrophic coccobacillus plasticity and MreB/PBP2 perturbation phenotypes. (slovak2005localizationofmreb pages 7-10, slovak2005localizationofmreb pages 1-2)
3. **Caccamo PD, Brun YV.** “The Molecular Basis of Noncanonical Bacterial Morphology.” *Trends in Microbiology* 26(3):191–208. **Published March 2018.** DOI: [10.1016/j.tim.2017.09.012](https://doi.org/10.1016/j.tim.2017.09.012). Authoritative review synthesizing elongasome-gene loss, PG composition, and evolutionary morphology evidence; primary sources should be recovered before final edge-level curation. (caccamo2018themolecularbasis pages 7-9)

## Curation priority

**Curate now:** the taxon-qualified *R. sphaeroides* photoheterotrophic-growth → coccobacillus edge; the *A. baumannii* zinc coordination → stable PBP2 → RodA–PBP2 lateral PG synthesis → maintenance of short-rod morphology branch; and explicit loss-of-trait edges for Δ`pbp2` and zinc-site variants.

**Curate after primary-source retrieval:** individual `yacF`, `mreBCD`, `pbpC`, `rodA`, and `rodZ` evolutionary-loss edges and corresponding muropeptide changes.

**Retain as uncertain:** a universal “balanced elongation/division → coccobacillus” abstraction. It is biologically coherent and useful as a graph hub, but the exact balance and geometry are taxon- and condition-dependent.

References

1. (slovak2005localizationofmreb pages 1-2): Peter M. Slovak, George H. Wadhams, and Judith P. Armitage. Localization of mreb in rhodobacter sphaeroides under conditions causing changes in cell shape and membrane structure. Journal of Bacteriology, 187:54-64, Jan 2005. URL: https://doi.org/10.1128/jb.187.1.54-64.2005, doi:10.1128/jb.187.1.54-64.2005. This article has 107 citations and is from a peer-reviewed journal.

2. (micelli2023aconservedzincbinding pages 1-2): Carmina Micelli, Yunfei Dai, Nicole Raustad, Ralph R. Isberg, Christopher G. Dowson, Adrian J. Lloyd, Edward Geisinger, Allister Crow, and David I. Roper. A conserved zinc-binding site in acinetobacter baumannii pbp2 required for elongasome-directed bacterial cell shape. Proceedings of the National Academy of Sciences of the United States of America, Feb 2023. URL: https://doi.org/10.1073/pnas.2215237120, doi:10.1073/pnas.2215237120. This article has 23 citations and is from a highest quality peer-reviewed journal.

3. (micelli2023aconservedzincbinding pages 4-6): Carmina Micelli, Yunfei Dai, Nicole Raustad, Ralph R. Isberg, Christopher G. Dowson, Adrian J. Lloyd, Edward Geisinger, Allister Crow, and David I. Roper. A conserved zinc-binding site in acinetobacter baumannii pbp2 required for elongasome-directed bacterial cell shape. Proceedings of the National Academy of Sciences of the United States of America, Feb 2023. URL: https://doi.org/10.1073/pnas.2215237120, doi:10.1073/pnas.2215237120. This article has 23 citations and is from a highest quality peer-reviewed journal.

4. (slovak2005localizationofmreb pages 7-10): Peter M. Slovak, George H. Wadhams, and Judith P. Armitage. Localization of mreb in rhodobacter sphaeroides under conditions causing changes in cell shape and membrane structure. Journal of Bacteriology, 187:54-64, Jan 2005. URL: https://doi.org/10.1128/jb.187.1.54-64.2005, doi:10.1128/jb.187.1.54-64.2005. This article has 107 citations and is from a peer-reviewed journal.

5. (micelli2023aconservedzincbinding pages 6-7): Carmina Micelli, Yunfei Dai, Nicole Raustad, Ralph R. Isberg, Christopher G. Dowson, Adrian J. Lloyd, Edward Geisinger, Allister Crow, and David I. Roper. A conserved zinc-binding site in acinetobacter baumannii pbp2 required for elongasome-directed bacterial cell shape. Proceedings of the National Academy of Sciences of the United States of America, Feb 2023. URL: https://doi.org/10.1073/pnas.2215237120, doi:10.1073/pnas.2215237120. This article has 23 citations and is from a highest quality peer-reviewed journal.

6. (micelli2023aconservedzincbinding pages 7-8): Carmina Micelli, Yunfei Dai, Nicole Raustad, Ralph R. Isberg, Christopher G. Dowson, Adrian J. Lloyd, Edward Geisinger, Allister Crow, and David I. Roper. A conserved zinc-binding site in acinetobacter baumannii pbp2 required for elongasome-directed bacterial cell shape. Proceedings of the National Academy of Sciences of the United States of America, Feb 2023. URL: https://doi.org/10.1073/pnas.2215237120, doi:10.1073/pnas.2215237120. This article has 23 citations and is from a highest quality peer-reviewed journal.

7. (caccamo2018themolecularbasis pages 7-9): Paul D. Caccamo and Yves V. Brun. The molecular basis of noncanonical bacterial morphology. Mar 2018. URL: https://doi.org/10.1016/j.tim.2017.09.012, doi:10.1016/j.tim.2017.09.012. This article has 80 citations and is from a domain leading peer-reviewed journal.