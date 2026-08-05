---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T14:53:57.273579'
end_time: '2026-08-04T15:04:01.506831'
duration_seconds: 604.23
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range
  trait_identifier: METPO:1000332
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH phenotype with numerical limits that bounds the minimum and maximum
    external pH supporting growth of an organism.
  parent_traits: METPO:1000531, METPO:1000535
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports the bounded external-pH span over which cytoplasmic pH homeostasis sustains
    growth as the basis of the pH-range phenotype.) | DOI:10.1016/j.tim.2007.02.005:
    highly impermeable cell membranes (pH-homeostasis review supports envelope-based
    proton barriers as the mechanism extending growth into acidic and alkaline extremes.)'
  causal_graph_summary: 'ph_range_bounded_homeostasis: 11 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000332
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits that bounds the minimum and maximum external pH supporting growth of an organism.
- **Parent traits:** METPO:1000531, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the bounded external-pH span over which cytoplasmic pH homeostasis sustains growth as the basis of the pH-range phenotype.) | DOI:10.1016/j.tim.2007.02.005: highly impermeable cell membranes (pH-homeostasis review supports envelope-based proton barriers as the mechanism extending growth into acidic and alkaline extremes.)
- **Existing causal graph summary:** ph_range_bounded_homeostasis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **pH range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range.yaml`.

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
- **Trait label:** pH range
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000332
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits that bounds the minimum and maximum external pH supporting growth of an organism.
- **Parent traits:** METPO:1000531, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the bounded external-pH span over which cytoplasmic pH homeostasis sustains growth as the basis of the pH-range phenotype.) | DOI:10.1016/j.tim.2007.02.005: highly impermeable cell membranes (pH-homeostasis review supports envelope-based proton barriers as the mechanism extending growth into acidic and alkaline extremes.)
- **Existing causal graph summary:** ph_range_bounded_homeostasis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **pH range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range.yaml`.

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


# Curation report: microbial pH range

## Executive summary

**Target trait:** `METPO:1000332` — **pH range**  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED.

The trait should represent the **closed or experimentally bounded interval of external pH values over which an organism exhibits net growth under stated conditions**. It is not the optimum pH, intracellular pH, transient survival after acid/alkali challenge, or the pH measured in an organism’s habitat. Mechanistically, range boundaries arise when envelope proton permeability, ion transport, proton motive force (PMF), metabolism, buffering, and macromolecular function can no longer maintain a growth-compatible cytoplasm.

A useful high-level graph is:

> external pH challenge → transmembrane proton/electrical disequilibrium → pH-sensing and homeostatic effectors → cytoplasmic/periplasmic pH homeostasis and preserved bioenergetics → growth at that external pH → bounded pH range.

Foundational syntheses place typical neutralophile growth around external pH 5.5–9.0 with cytoplasmic pH approximately 7.5–7.7, whereas acidophiles and alkaliphiles can grow at approximately pH 1–3 and 10–13, respectively. These are ecological classes, not universal annotation thresholds. *Escherichia coli*, for example, may survive environments in which it does not grow, illustrating why challenge survival cannot establish `METPO:1000332` boundaries. (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 1-3)

## 1. Trait scope and boundary cases

### Operational definition

Curate `METPO:1000332` only when a study reports or supports:

1. an external-pH series or explicit lower/upper external-pH limit;
2. **growth**, preferably by growth rate, biomass increase, colony formation after sustained incubation, or serial propagation;
3. controlled temperature, medium, ionic composition, gas phase, and buffering;
4. a taxonomically resolved strain or population; and
5. enough duration to distinguish growth from maintenance or transient survival.

The range is assay-dependent. Weak organic acids can enter cells in their uncharged forms and impose effects not reproduced by mineral-acid adjustment at the same pH. Sodium concentration, carbonate/bicarbonate, aeration, energy source, buffering capacity, inoculum history, biofilm state, and adaptation can all move an apparent boundary.

### Nearby traits that must remain separate

- **Optimal pH:** the pH maximizing growth rate or yield; a point or narrow optimum, not the lower-to-upper interval.
- **Acid/alkali tolerance or resistance:** continued viability after challenge. The 2024 *S. aureus* study, for example, separately used growth assays at pH 4.5–5.5 and survival assays at pH 2.5; those outcomes should not be merged. (beetham2024histidinetransportis pages 7-8, beetham2024histidinetransportis pages 17-18)
- **Cytoplasmic pH homeostasis:** an intermediate mechanism or physiological state, not the external-pH range itself.
- **Environmental occurrence:** isolation from an acidic or alkaline site does not prove growth at the site’s measured pH.
- **Acid or alkali production:** modification of extracellular pH may support range indirectly, but is a separate metabolic phenotype.
- **Community-level pH robustness:** activated sludge and biofilm behavior can reflect species sorting, matrix effects, and metabolite exchange rather than the intrinsic range of one organism.

## 2. Current mechanistic understanding

The most defensible interpretation is that pH range is an **emergent systems phenotype**, not the output of one universal pathway. The proximate causal bottleneck is retention of a growth-compatible intracellular physicochemical state.

At low external pH, relevant strategies include low envelope proton permeability, outward proton pumping, PMF management, amino-acid decarboxylation, ammonia-generating reactions, macromolecular repair, and alteration of cell-wall or membrane charge/composition. At high external pH, organisms must generally promote proton entry or retention, often through Na+/H+ or K+/H+ antiport, while preserving membrane potential and ATP synthesis despite an outwardly directed ΔpH. The balance of membrane potential, ΔpH, and ion gradients—not ΔpH alone—therefore determines the usable pH interval. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 3-5)

A quantitative example is *Bacillus pseudofirmus* OF4: it maintains cytoplasmic pH near 7.5 across external pH 7.5–9.5, grows optimally near external pH 10.5 with internal pH about 8.3, and can survive at still higher pH with substantially more alkaline cytoplasm. These values show both the value and limitation of homeostasis: internal pH is regulated, but not invariant, and survival beyond the growth optimum does not itself extend the growth range. (krulwich2011molecularaspectsof pages 12-14)

## 3. Candidate causal-graph nodes

Identifiers below are conservative. Where a stable, exact identifier was not verified from the retrieved sources, a label-only node is preferable to an invented CURIE.

### Trait and environmental nodes

- **pH range:** `METPO:1000332`
- **External pH:** label-only environmental/experimental variable
- **Acidic external environment:** candidate `ENVO` term; verify the exact class before curation
- **Alkaline external environment:** candidate `ENVO` term; verify the exact class before curation
- **Growth at specified external pH:** label-only assay outcome
- **Buffer capacity**, **organic-acid identity/concentration**, **temperature**, **aeration**, **ionic strength**, **Na+ concentration**, **biofilm versus planktonic state:** experimental-context nodes

### Chemicals and electrochemical variables

- proton: `CHEBI:15378`
- sodium cation: `CHEBI:29101`
- potassium cation: `CHEBI:29103`
- ammonia: `CHEBI:16134`
- ammonium: `CHEBI:28938`
- carbon dioxide: `CHEBI:16526`
- hydrogencarbonate/bicarbonate: `CHEBI:17544`
- L-glutamate: `CHEBI:29985`
- 4-aminobutanoate/GABA: `CHEBI:16865`
- putrescine: `CHEBI:17148`
- acetate: `CHEBI:30089`
- acetoin: `CHEBI:15688`
- histidine: use the appropriate protonation-specific ChEBI class only after checking assay convention
- **membrane potential**, **transmembrane pH gradient**, **proton motive force**, **cytoplasmic pH**, **periplasmic pH:** label-only physicochemical nodes unless the target schema has approved ontology terms

### Molecular functions and processes

- proton transmembrane transport: `GO:1902600`
- pH homeostasis: `GO:0045851`
- monovalent cation:proton antiporter activity: use the appropriate child of `GO:0015299` after confirming ion and stoichiometry
- ATP synthesis coupled proton transport: `GO:0015986`
- cellular response to acidic pH: verify the current GO term before use
- amino-acid decarboxylation, urease activity, aerobic respiration, cell-wall organization, histidine transport, extracellular-pH regulation, biofilm development: verify exact GO/EC grounding per organism

### Genes, proteins, and complexes

- **F1Fo-ATP synthase / F0F1-ATPase**
- **respiratory-chain proton pumps** and cytochrome oxidases
- **NhaA, NhaB**, and **MrpABCDEFG** cation/proton antiport systems
- **ClcA-like H+/Cl− antiporter**
- **GadB/glutamate decarboxylase** and associated glutamate/GABA antiport
- lysine- and arginine-dependent decarboxylase systems
- ***H. pylori* UreI, urease, HP0165–HP0166, and HP0244**
- ***S. aureus* SAUSA300_0846**, the experimentally supported major histidine transporter
- ***S. aureus* SrrA and QoxA/QoxB**, implicated in low-pH growth through respiratory functions
- ***S. aureus* cell-wall assembly/maintenance genes**, including the **dlt**-dependent teichoic-acid charge mechanism as a candidate module
- ***B. subtilis* acetate- and acetoin-biosynthesis modules**
- **Pal/Rim–PacC fungal alkaline-response pathway:** biologically plausible candidate, but no sufficiently specific causal evidence was recovered here for inclusion in the core graph

### Cellular structures/localizations

- cytoplasm
- cytoplasmic membrane
- periplasm, for diderm bacteria
- cell wall and teichoic acids
- outer membrane, for diderm bacteria
- extracellular polymeric matrix and biofilm microenvironment

## 4. Evidence-backed candidate edges

The following table summarizes the strongest edges. “Direct” means perturbation or measurement evidence in the cited taxon; it does not imply universality.

| subject | predicate | object | organism/context | evidence strength/status | DOI |
|---|---|---|---|---|---|
| proton motive force (PMF) | enables maintenance of | cytoplasmic pH homeostasis | *Escherichia coli*; single-cell measurements plus modeling; reduced PMF impaired pH maintenance | **Strong, direct, taxon-specific; partly model-integrated** (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9) | https://doi.org/10.1103/PRXLife.2.043015 |
| proton-ion antiporters (NhaA/NhaB/ClcA-like) | generate/support | membrane potential and PMF | *E. coli* electrophysiology model constrained by experimental PMF/pHi data | **Moderate, model-derived, taxon-specific** (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9) | https://doi.org/10.1103/PRXLife.2.043015 |
| Mrp Na+/H+ antiporter complex | required for | alkaline pH homeostasis and alkaliphilic growth | *Bacillus* alkaliphiles; review synthesis notes mrpA mutations abolish alkaliphilicity/homeostasis | **Moderate, review-backed, taxon-specific** (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 27-28) | https://doi.org/10.1038/nrmicro2549 |
| F1Fo-ATPase / F0F1-ATPase | mediates | proton transport contributing to pH homeostasis | Broad bacteria; acid stress and alkaliphily contexts; includes *S. mutans*, bifidobacteria, LAB | **Moderate, mixed direct+review evidence; taxon-specific/generalized with caution** (krulwich2011molecularaspectsof pages 5-6, atasoy2024exploitationofmicrobial pages 3-4) | https://doi.org/10.1038/nrmicro2549; https://doi.org/10.1093/femsre/fuad062 |
| amino-acid decarboxylation systems (e.g., glutamate/lysine/arginine) | consume | intracellular protons | Broad bacteria under acid stress; acid tolerance/homeostasis rather than direct range assay | **Moderate, review-backed, indirect for trait range** (beetham2024histidinetransportis pages 1-2, atasoy2024exploitationofmicrobial pages 3-4) | https://doi.org/10.1371/journal.ppat.1011927; https://doi.org/10.1093/femsre/fuad062 |
| urease + UreI | buffer/maintain | periplasmic pH near ~6.1 during acid acclimation | *Helicobacter pylori*; acid acclimation system | **Strong, review-backed mechanistic, taxon-specific** (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 11-12) | https://doi.org/10.1038/nrmicro2549 |
| SAUSA300_0846 histidine transporter | supports | cytosolic pH maintenance | *Staphylococcus aureus* under acid stress; mutant had reduced capacity to maintain cytosolic pH | **Strong, direct genetics, taxon-specific** (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 17-18) | https://doi.org/10.1371/journal.ppat.1011927 |
| SAUSA300_0846 histidine transporter | required for | low-pH growth | *S. aureus*; growth at pH 4.3–4.5 impaired in transporter mutant | **Strong, direct genetics, taxon-specific** (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 17-18) | https://doi.org/10.1371/journal.ppat.1011927 |
| cell-wall assembly/maintenance functions | promote | low-pH growth | *S. aureus*; many Tn-Seq hits for growth at pH 4.5 were cell-wall related | **Strong, direct screen-level, taxon-specific** (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 7-8) | https://doi.org/10.1371/journal.ppat.1011927 |
| acetate/acetoin metabolic interplay | buffers/modulates | extracellular pH | *Bacillus subtilis* biofilms in minimally buffered medium | **Strong, direct but community/biofilm-specific** (tran2024activephregulation pages 1-2) | https://doi.org/10.1128/mbio.03387-23 |
| extracellular pH buffering by acetate/acetoin metabolism | facilitates | biofilm development | *B. subtilis* biofilms; buffering-deficient biofilms showed dysregulated development | **Strong, direct but community/biofilm-specific** (tran2024activephregulation pages 1-2) | https://doi.org/10.1128/mbio.03387-23 |
| exogenous putrescine | enhances | glutamate-based acid resistance and GABA pathway | biofilm-based activated sludge under acidic stress | **Moderate, community-level, indirect for species trait curation** (jiang2024exogenousputrescineplays pages 1-2) | https://doi.org/10.1128/aem.00569-24 |
| exogenous putrescine | stimulates | ATPase expression / H+ transmembrane transport | biofilm-based activated sludge under acidic stress | **Moderate, community-level, indirect for species trait curation** (jiang2024exogenousputrescineplays pages 1-2) | https://doi.org/10.1128/aem.00569-24 |


*Table: This table compiles the strongest mechanistic candidate edges for curating microbial pH range (METPO:1000332). It highlights which edges are direct versus model-derived, and flags taxon-specific or community-level evidence that should be curated cautiously.*

### Additional edge-level evidence and snippets

| Proposed subject–predicate–object triple | Reference | Supporting source wording | Curation note |
|---|---|---|---|
| **Reduced PMF → impairs → cytoplasmic-pH maintenance** | Terradot et al., 2024, DOI: [10.1103/PRXLife.2.043015](https://doi.org/10.1103/PRXLife.2.043015) | “decreasing the PMF’s strength impairs the cells’ ability to maintain pH” | Strong experimental edge in *E. coli*. It supports a homeostasis intermediate; direct extension of the measured growth range was not tested. (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9) |
| **Proton-ion antiporter activity → supports → membrane potential/PMF** | Terradot et al., 2024 | Cells “build a membrane potential using proton-ion antiporters”; predicted optimal regimes were ClcA-like at approximately pHe 2–5, NhaB-like at 5–9, and NhaA-like at 9–12. | **Uncertain/model-derived.** Regime boundaries are optimization predictions, not measured growth limits or direct expression measurements in this study. (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9) |
| **Mrp antiporter function → enables → alkaliphilicity and alkaline pH homeostasis** | Krulwich et al., 2011, DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549) | Review synthesis: *mrpA* mutations cause “loss of alkaliphilicity and pH homeostasis” in *Bacillus halodurans*. | Strong candidate but based here on a review’s synthesis. Retrieve and cite the primary mutation paper before final YAML curation if required by policy. (krulwich2011molecularaspectsof pages 12-14) |
| **F1Fo-ATPase hydrolysis → exports → intracellular protons under acid stress** | Krulwich et al., 2011 | *S. mutans* increases hydrolytic F1Fo activity for H+ extrusion under acidic conditions. | Taxon- and energetic-state-specific. In alkaliphiles, ATP synthase can instead import protons during ATP synthesis; do not encode a universal fixed direction. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14) |
| **Amino-acid decarboxylation → consumes → cytoplasmic proton** | Atasoy et al., 2024, DOI: [10.1093/femsre/fuad062](https://doi.org/10.1093/femsre/fuad062) | Decarboxylation produces a biogenic amine and CO2 while “consuming a proton,” contributing to intracellular-pH maintenance and low-pH survival. | Mechanistically strong, but the retrieved evidence emphasizes survival. Require growth-range assays before connecting directly to `METPO:1000332`. (atasoy2024exploitationofmicrobial pages 3-4) |
| **UreI-recruited urease/urea hydrolysis → buffers → *H. pylori* periplasm** | Krulwich et al., 2011 | Urea hydrolysis produces CO2, NH3, and NH4+, maintaining periplasmic pH at approximately 6.1 during acid acclimation. | Strong, taxon-specific mechanism. Connect to acid acclimation/homeostasis first, then to growth only with direct growth evidence. (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 11-12) |
| **SAUSA300_0846-mediated histidine uptake → supports → low-pH growth** | Beetham et al., published 16 Jan 2024, DOI: [10.1371/journal.ppat.1011927](https://doi.org/10.1371/journal.ppat.1011927) | Wild type could not grow in defined medium at pH 4.3 without histidine; the transporter mutant could not grow at pH 4.3 regardless of added histidine. | One of the best direct growth-boundary edges. Restrict to *S. aureus* and the tested defined medium. (beetham2024histidinetransportis pages 17-18) |
| **SAUSA300_0846-mediated histidine uptake → supports → cytosolic-pH maintenance** | Beetham et al., 2024 | The mutant had “a reduced capacity to maintain its cytosolic pH during acid stress conditions.” | Direct mechanistic intermediate. Histidine abundance was maintained by induced biosynthesis, showing that uptake route—not total histidine alone—matters. (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 17-18) |
| **Cell-wall assembly and maintenance → support → growth at pH 4.5** | Beetham et al., 2024 | Of 31 genes essential for growth at pH 4.5, many encoded cell-wall assembly/maintenance functions. | Strong screen-level association; individual gene-level edges need mutant confirmation. The study confirmed 15 of 20 investigated candidates. (beetham2024histidinetransportis pages 7-8, beetham2024histidinetransportis pages 1-2) |
| **D-alanylation of teichoic acids → reduces/controls → acid susceptibility** | Beetham et al., 2024, introduction and cited prior work | Addition of positively charged D-alanine by the **dlt** operon to teichoic acids is described as important for growth and survival at low pH. | Plausible envelope-charge edge, but this passage summarizes prior work. Retrieve primary evidence before creating a gene-specific TraitMech edge. (beetham2024histidinetransportis pages 1-2) |
| **Acetate–acetoin metabolic switching → buffers → extracellular biofilm pH** | Tran et al., published 13 Feb 2024, DOI: [10.1128/mbio.03387-23](https://doi.org/10.1128/mbio.03387-23) | *B. subtilis* biofilms modulated extracellular pH toward the preferred neutrophile range from acidic or alkaline initial conditions; planktonic cells could not. | Strong community-state edge. It describes niche construction, not necessarily a cell-autonomous pH range. (tran2024activephregulation pages 1-2) |
| **Extracellular-pH regulation → facilitates → biofilm development** | Tran et al., 2024 | “buffering-deficient biofilms exhibit dysregulated biofilm development” in minimally buffered conditions. | Direct biofilm-development phenotype; include assay context because standard buffered MSgg can mask the mechanism. (tran2024activephregulation pages 1-2) |
| **Protonated putrescine → enhances → glutamate/GABA acid-resistance metabolism** | Jiang et al., published 25 Jun 2024, DOI: [10.1128/aem.00569-24](https://doi.org/10.1128/aem.00569-24) | Putrescine “consumed intracellular H+ by enhancing the glutamate-based acid resistance strategy and the γ-aminobutyric acid metabolic pathway.” | Community-level activated-sludge evidence. Putrescine had the opposite ecological effect under alkaline conditions; do not generalize it as universally range-expanding. (jiang2024exogenousputrescineplays pages 1-2) |
| **H+-ATPase activation → causes → intermittent proton efflux** | Gao et al., published Jan 2024, DOI: [10.1039/D3SC06238D](https://doi.org/10.1039/D3SC06238D) | Single *Lactiplantibacillus plantarum* cells exhibited proton bursts lasting several seconds, attributed to H+-ATPase activation compensating transient depolarization. | Novel direct single-cell physiology, but not a growth-range experiment. The attribution is mechanistic inference from the perturbation framework. (gao2024intermittentprotonbursts pages 1-2) |

## 5. Recent developments, applications, and quantitative findings

### 2024 advances

1. **Integrated electrophysiology:** Terradot and colleagues reframed pH homeostasis as inseparable from PMF and membrane potential. Experimentally weakening PMF impaired pHi maintenance, while their model proposed antiporter selection across different external-pH regimes. This is an important conceptual advance, but the predicted antiporter regimes must not be encoded as observed pH-range limits. (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9)

2. **Genome-scale low-pH growth genetics:** The *S. aureus* Tn-Seq study found **31 genes required at pH 4.5 versus five at pH 5.5**. Fifteen of 20 individually investigated candidates were confirmed as important for low-pH growth. Histidine transport emerged as a specific link between nutrient acquisition, cytosolic-pH maintenance, and growth at pH 4.3–4.5. (beetham2024histidinetransportis pages 7-8, beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 17-18)

3. **Biofilm niche construction:** *B. subtilis* biofilms—but not planktonic populations—actively returned extracellular pH toward a neutrophilic range through acetate/acetoin metabolic dynamics. The result demonstrates that measured range can depend on multicellular state and buffering. (tran2024activephregulation pages 1-2)

4. **Single-cell proton dynamics:** *L. plantarum* did not release protons only continuously; it also displayed stochastic bursts on a timescale of several seconds, linking H+-ATPase activity to transient membrane-potential homeostasis. (gao2024intermittentprotonbursts pages 1-2)

5. **Engineered community robustness:** In activated-sludge biofilms, exogenous putrescine promoted biofilm formation under acidic conditions but inhibited it under alkaline conditions. The pH-dependent sign reversal illustrates why chemical modifiers require conditional edges rather than a simple “increases pH range” relation. (jiang2024exogenousputrescineplays pages 1-2)

### Real-world implementation

- **Fermentation and organic-acid production:** Selecting or engineering strains that preserve growth while organic acids accumulate can improve productivity and reduce neutralizing-base requirements. Acid-resistance pathways are therefore engineering targets, although survival gains do not automatically imply higher production rates. (atasoy2024exploitationofmicrobial pages 3-4)
- **Probiotics and fermented foods:** Preadaptation at sublethal pH 4.5 or 5.0 has improved refrigerated-yogurt viability of *Lactobacillus rhamnosus* GG and *Bifidobacterium animalis* subsp. *lactis* BB12 in prior work summarized by a 2024 review. The response includes F1Fo-ATPase activity, membrane remodeling, decarboxylation, and stress proteins. Preadaptation can also alter aroma chemistry and biogenic-amine risk. (atasoy2024exploitationofmicrobial pages 3-4)
- **Food safety:** Acid adaptation of pathogens or spoilage organisms can undermine acid-based preservation; conversely, low pH and plasma-activated water can contribute to decontamination. Food matrices and weak-acid chemistry must be represented as context, not merely as pH values. (atasoy2024exploitationofmicrobial pages 3-4)
- **Biofilm control:** Disrupting acetate/acetoin pH regulation may control unwanted *B. subtilis* biofilms in minimally buffered settings. Standard buffered media can conceal this vulnerability. (tran2024activephregulation pages 1-2)
- **Wastewater engineering:** Putrescine-mediated community manipulation may stabilize acidic biofilms, but its inhibitory alkaline effect and taxonomic redistribution make it unsuitable as a universal intervention. (jiang2024exogenousputrescineplays pages 1-2)
- **Pathogenesis:** Histidine uptake, cell-wall maintenance, respiration, and urease-mediated buffering are potential anti-virulence targets in organisms encountering acidic skin, phagosomes, or stomach environments. (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 11-12, beetham2024histidinetransportis pages 1-2)

## 6. Recommended graph architecture

For `data/traits/environment/ph_range.yaml`, avoid connecting every stress-response component directly to `METPO:1000332`. Use layered causality:

1. **Environmental layer:** external pH, buffer capacity, organic acid, Na+/K+ availability, oxygen, temperature, growth medium.
2. **Perturbation layer:** proton influx/leak, altered ΔpH, altered membrane potential, protein/DNA damage, changed nutrient speciation.
3. **Mechanism layer:** envelope barrier, F1Fo-ATPase, respiratory proton pumping, cation/proton antiport, decarboxylation, urease, nutrient transport, cell-wall remodeling, extracellular-pH modification.
4. **State layer:** cytoplasmic/periplasmic pH homeostasis, maintained PMF, ATP production, enzyme function, redox homeostasis.
5. **Outcome layer:** positive growth rate at external pH.
6. **Trait layer:** lower and upper external-pH limits jointly define `METPO:1000332`.

A direct **mechanism → pH range** edge should be reserved for perturbations that shift a measured growth boundary. Most retrieved studies support the safer pattern **mechanism → homeostatic state → growth under specified pH**, with the final range effect still requiring a multi-pH assay.

## 7. Warnings: claims not ready for TraitMech curation

1. **Do not use pH 2–2.5 survival as evidence of growth range.** Several acid-resistance systems were studied in lethal challenge assays.
2. **Do not treat cytoplasmic-pH maintenance as synonymous with growth.** Maintenance may persist transiently after biosynthesis or division has stopped.
3. **Do not encode Terradot et al.’s pHe 2–5, 5–9, and 9–12 antiporter regimes as observed biological ranges.** They are model-optimal regimes. (terradot2024escherichiacolimaintains pages 8-9)
4. **Do not universalize transporter direction.** F1Fo-ATPase and antiporters can operate differently with organism, external pH, PMF, and energetic state.
5. **Do not generalize SAUSA300_0846 beyond *S. aureus*.** Its low-pH histidine-transport role is direct, whereas a reported alkaline-pH K+/H+ antiporter annotation came from separate preprint evidence discussed by the authors. (beetham2024histidinetransportis pages 17-18)
6. **Do not infer intrinsic species pH range from biofilm or activated-sludge behavior.** Community sorting, matrix diffusion, cross-feeding, and extracellular-pH modification can generate emergent tolerance. (tran2024activephregulation pages 1-2, jiang2024exogenousputrescineplays pages 1-2)
7. **Do not add membrane impermeability or Donnan-potential edges solely from the supplied 2007 review citation without retrieving the exact primary evidence.** These mechanisms are credible, but the present search did not recover sufficiently specific quotations from that paper.
8. **Do not ground uncertain nodes with guessed CURIEs.** Label-only nodes are preferable until the exact GO, ENVO, EC, UniProt, Rhea, or pathway record is verified.
9. **Do not assume that a gene required at one pH shifts the full range boundary.** A pH 4.5 screen identifies conditional fitness determinants; a range shift requires comparison across multiple pH values.

## DOI-first bibliography

1. **Terradot G, Krasnopeeva E, Swain PS, Pilizota T.** “*Escherichia coli* Maintains pH via the Membrane Potential.” *PRX Life*. Published **27 November 2024**. DOI: [10.1103/PRXLife.2.043015](https://doi.org/10.1103/PRXLife.2.043015). (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9)
2. **Beetham CM et al.** “Histidine transport is essential for the growth of *Staphylococcus aureus* at low pH.” *PLOS Pathogens* 20:e1011927. Published **16 January 2024**. DOI: [10.1371/journal.ppat.1011927](https://doi.org/10.1371/journal.ppat.1011927). (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 17-18)
3. **Tran P, Lander SM, Prindle A.** “Active pH regulation facilitates *Bacillus subtilis* biofilm development in a minimally buffered environment.” *mBio* 15. Published **13 February 2024**. DOI: [10.1128/mbio.03387-23](https://doi.org/10.1128/mbio.03387-23). (tran2024activephregulation pages 1-2)
4. **Jiang G et al.** “Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge.” *Applied and Environmental Microbiology* 90. Published **25 June 2024**. DOI: [10.1128/AEM.00569-24](https://doi.org/10.1128/AEM.00569-24). (jiang2024exogenousputrescineplays pages 1-2)
5. **Gao J et al.** “Intermittent proton bursts of single lactic acid bacteria.” *Chemical Science* 15:3516–3523. Published **2024**; accepted 23 January 2024. DOI: [10.1039/D3SC06238D](https://doi.org/10.1039/D3SC06238D). (gao2024intermittentprotonbursts pages 1-2)
6. **Atasoy M et al.** “Exploitation of microbial activities at low pH to enhance planetary health.” *FEMS Microbiology Reviews* 48. Published **2024**. DOI: [10.1093/femsre/fuad062](https://doi.org/10.1093/femsre/fuad062). (atasoy2024exploitationofmicrobial pages 3-4)
7. **Krulwich TA, Sachs G, Padan E.** “Molecular aspects of bacterial pH sensing and homeostasis.” *Nature Reviews Microbiology* 9:330–343. Published **May 2011**. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 1-3)
8. **Baker-Austin C, Dopson M.** “Life in acid: pH homeostasis in acidophiles.” *Trends in Microbiology* 15:165–171. Published **April 2007**. DOI: [10.1016/j.tim.2007.02.005](https://doi.org/10.1016/j.tim.2007.02.005). The paper is foundational for proton-impermeable-envelope concepts, but its full text was not retrieved in this evidence set; use it only after source-level verification.

References

1. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

3. (beetham2024histidinetransportis pages 7-8): Catrin M. Beetham, Christopher F. Schuster, Igor Kviatkovski, Marina Santiago, Suzanne Walker, and Angelika Gründling. Histidine transport is essential for the growth of staphylococcus aureus at low ph. PLOS Pathogens, 20:e1011927, Jan 2024. URL: https://doi.org/10.1371/journal.ppat.1011927, doi:10.1371/journal.ppat.1011927. This article has 28 citations and is from a highest quality peer-reviewed journal.

4. (beetham2024histidinetransportis pages 17-18): Catrin M. Beetham, Christopher F. Schuster, Igor Kviatkovski, Marina Santiago, Suzanne Walker, and Angelika Gründling. Histidine transport is essential for the growth of staphylococcus aureus at low ph. PLOS Pathogens, 20:e1011927, Jan 2024. URL: https://doi.org/10.1371/journal.ppat.1011927, doi:10.1371/journal.ppat.1011927. This article has 28 citations and is from a highest quality peer-reviewed journal.

5. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

6. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

7. (terradot2024escherichiacolimaintains pages 1-2): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.

8. (terradot2024escherichiacolimaintains pages 8-9): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.

9. (krulwich2011molecularaspectsof pages 27-28): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

10. (atasoy2024exploitationofmicrobial pages 3-4): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 104 citations and is from a domain leading peer-reviewed journal.

11. (beetham2024histidinetransportis pages 1-2): Catrin M. Beetham, Christopher F. Schuster, Igor Kviatkovski, Marina Santiago, Suzanne Walker, and Angelika Gründling. Histidine transport is essential for the growth of staphylococcus aureus at low ph. PLOS Pathogens, 20:e1011927, Jan 2024. URL: https://doi.org/10.1371/journal.ppat.1011927, doi:10.1371/journal.ppat.1011927. This article has 28 citations and is from a highest quality peer-reviewed journal.

12. (krulwich2011molecularaspectsof pages 11-12): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

13. (tran2024activephregulation pages 1-2): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 33 citations and is from a domain leading peer-reviewed journal.

14. (jiang2024exogenousputrescineplays pages 1-2): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

15. (gao2024intermittentprotonbursts pages 1-2): Jia Gao, Kai Zhou, Haoran Li, Yaohua Li, Kairong Yang, and Wei Wang. Intermittent proton bursts of single lactic acid bacteria. Chemical Science, 15:3516-3523, Jan 2024. URL: https://doi.org/10.1039/d3sc06238d, doi:10.1039/d3sc06238d. This article has 10 citations and is from a highest quality peer-reviewed journal.