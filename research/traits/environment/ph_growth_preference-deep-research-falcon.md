---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:34:00.362600'
end_time: '2026-08-04T02:42:21.027427'
duration_seconds: 500.66
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH growth preference
  trait_identifier: METPO:1003000
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_growth_preference
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that describes how the rate and extent of population growth
    are affected by environmental pH.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro2549: external pH values that are outside
    the cytoplasmic pH range (Supports environmental pH as a growth-relevant condition
    requiring pH homeostasis.)'
  causal_graph_summary: 'ph_growth_preference_homeostasis: 12 nodes, 12 edges'
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
- **Trait label:** pH growth preference
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003000
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes how the rate and extent of population growth are affected by environmental pH.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH values that are outside the cytoplasmic pH range (Supports environmental pH as a growth-relevant condition requiring pH homeostasis.)
- **Existing causal graph summary:** ph_growth_preference_homeostasis: 12 nodes, 12 edges

## Research Objective

Research the microbial trait **pH growth preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_growth_preference.yaml`.

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
- **Trait label:** pH growth preference
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003000
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes how the rate and extent of population growth are affected by environmental pH.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH values that are outside the cytoplasmic pH range (Supports environmental pH as a growth-relevant condition requiring pH homeostasis.)
- **Existing causal graph summary:** ph_growth_preference_homeostasis: 12 nodes, 12 edges

## Research Objective

Research the microbial trait **pH growth preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_growth_preference.yaml`.

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


# Curation report: microbial pH growth preference

## Executive summary

**Target trait:** pH growth preference  
**Identifier:** **METPO:1003000**  
**Category/kind:** ENVIRONMENT / CLASS  
**Parent:** METPO:1000059  
**Working definition:** the reaction norm describing how controlled extracellular pH affects the rate and extent of microbial population growth.

The most defensible TraitMech graph should connect **external pH** to **cytoplasmic-pH and bioenergetic perturbations**, then to compensating transport, metabolism, membrane structure, and extracellular-pH modification, and ultimately to growth. It should not equate pH growth preference with acid survival, pH tolerance limits, intracellular pH, or environmental relative-abundance optima.

Recent research substantially strengthens this distinction. Ramoneda et al. define environmental pH preference as a **realized niche**—the pH of maximal relative abundance in nature—which can differ from the pH optimum measured in culture because of biotic and abiotic constraints. Their 2023 analysis covered 1,470 soil/freshwater samples spanning pH 3–10, 250,275 ASVs, and 38 bacterial phyla, but could conservatively infer preference for only 0.5–4.9% of ASVs per dataset. Thus, ecological preference is informative but is not a direct substitute for the assay-defined trait (ramoneda2023buildingagenomebased pages 1-2).

## 1. Trait scope and boundaries

### 1.1 Included phenotype

The trait should represent a quantitative growth response across a defined extracellular-pH series. Suitable observables include:

- maximum specific growth rate;
- lag duration;
- biomass or optical-density yield;
- colony-forming-unit increase;
- biofilm biomass or viable-cell accumulation;
- an explicitly fitted optimum pH and lower/upper growth limits.

The preferred graph endpoint is therefore **population growth rate/extent**, not merely expression of a stress gene or maintenance of intracellular pH.

### 1.2 Distinct nearby traits

| Nearby concept | Distinction from METPO:1003000 |
|---|---|
| **Growth optimum** | A summary point on the full pH–growth reaction norm; depends on medium, temperature, aeration, and measurement endpoint. |
| **Growth range/tolerance** | The pH interval permitting detectable net growth; it does not identify the preferred or optimal pH. |
| **Survival/acid resistance** | Persistence without net population growth. Foundational literature explicitly defines survival as subsequent growth after return to permissive pH (krulwich2011molecularaspectsof pages 1-3). |
| **Cytoplasmic pH homeostasis** | A causal capacity that can enable growth at external pH extremes, not the growth phenotype itself. Many bacterial cytoplasms are maintained around pH 7.0–7.5 (poolman2023physicochemicalhomeostasisin pages 1-2). |
| **Acid/alkaline stress response** | Molecular or transcriptional response following pH challenge; it may support survival, repair, or growth but does not itself establish preference. |
| **Environmental pH preference** | Realized ecological niche inferred from maximal relative abundance; it integrates competition and other environmental covariates and can differ from culture optimum (ramoneda2023buildingagenomebased pages 1-2). |
| **Extracellular pH modification** | An organism-driven environmental process that can feed back on growth; it is upstream of, rather than synonymous with, preference. |

A useful quantitative boundary case is *Bacillus pseudofirmus* OF4: it maintains cytoplasmic pH near 7.5 at external pH 7.5–9.5, grows optimally near external pH 10.5 with internal pH about 8.3, and can survive at pH ≥11 even when its cytoplasm reaches ≥9.5. These are three separable phenotypes—homeostasis, optimum growth, and survival (krulwich2011molecularaspectsof pages 12-14).

### 1.3 Assay factors that must be represented as context

Buffer concentration, buffer chemistry, carbon and nitrogen sources, sodium and potassium availability, temperature, oxygen/aeration, inoculum state, planktonic versus biofilm growth, and sampling time can alter the observed curve. In *Bacillus subtilis*, active pH regulation was visible in 1 mM MOPS but masked in standard 100 mM MOPS medium, demonstrating that buffering can remove the causal feedback being assayed (tran2024activephregulation pages 2-5, tran2024activephregulation pages 7-9).

## 2. Candidate nodes grouped by type

### Environmental and experimental nodes

- extracellular pH;
- acidic, neutral, and alkaline extracellular conditions;
- buffer capacity and buffer identity;
- oxygen availability/aeration;
- temperature;
- sodium and potassium availability;
- nutrient composition, especially amino acids and urea;
- planktonic or biofilm growth mode;
- growth rate, lag time, yield, viable-cell count, and fitted optimum pH.

### Cellular compartments and physicochemical states

- cytoplasm — **GO:0005737**;
- plasma/cytoplasmic membrane — **GO:0005886**;
- periplasm, cell wall, S-layer, and biofilm extracellular matrix—retain label-only unless the target ontology is selected;
- intracellular pH;
- transmembrane pH gradient, membrane potential, and proton-motive force;
- passive proton permeability;
- cytoplasmic buffering capacity.

Poolman notes that a roughly 1-fL bacterial cell at pH 7.2 contains only about **10 free protons**, making buffering and regulated proton transport essential; *Lactococcus lactis* has approximately 100 mM organic/inorganic phosphate buffering capacity (poolman2023physicochemicalhomeostasisin pages 1-2).

### Transporters, enzymes, and complexes

- Mrp-family Na⁺/H⁺ antiporter;
- NhaA and other Na⁺/H⁺ antiporters;
- K⁺/H⁺ antiporters;
- KdpACD potassium-transport system;
- F₀F₁ ATP synthase;
- respiratory-chain proton pumps;
- amino-acid decarboxylases and coupled amino-acid/product antiporters;
- glutamate decarboxylase GadB;
- urease, UreI, and ureide/urea transporters;
- acid and alkaline phosphatases;
- AckA/AcsA-associated acetate metabolism;
- AlsS/AlsD acetoin-biosynthesis pathway;
- hydrogenase maturation/quality-control proteins HypCD, HycI, and HupF;
- membrane-bound cytochrome *c* with an Asn-rich segment in *Evansella clarkii*—provisional.

Relevant process-level grounding includes proton transmembrane transporter activity (**GO:0015078**), proton-motive-force-driven ATP synthesis (**GO:0015986**), and potassium-ion transport (**GO:0006813**). Organism-specific proteins should receive UniProt identifiers only after a strain is fixed; family labels should not be assigned a single species-specific accession.

### Chemicals and metabolites

- hydron/proton — **CHEBI:15378**;
- sodium(1+) — **CHEBI:29101**;
- potassium(1+) — **CHEBI:29103**;
- urea — **CHEBI:16199**;
- ammonia — **CHEBI:16134**;
- acetate — **CHEBI:30089**;
- acetoin — **CHEBI:15688**;
- 4-aminobutanoate/GABA — **CHEBI:16865**;
- glutamate, citrate, lactate, CO₂, NH₄⁺, ATP, and ADP—verify the desired protonation-state-specific ChEBI records during implementation.

### Structural and process nodes

- tetraether-rich archaeal membrane;
- GDGT/GDNT lipids and cyclopentane-ring remodeling;
- acidic secondary cell-wall polymers;
- protein folding/quality control;
- proton-consuming decarboxylation;
- ammonia production from urea;
- acetate-driven extracellular acidification;
- acetoin-associated extracellular alkalinization;
- maintenance of cytoplasmic pH;
- ATP synthesis and nutrient transport;
- population growth.

## 3. Candidate causal edges

The following compact table separates perturbation-supported edges from correlations and hypotheses.

| subject | predicate | object | taxon/context | evidence strength | DOI |
|---|---|---|---|---|---|
| external environmental pH | affects growth rate/extent of | microbial populations | Trait scope across bacteria/archaea; growth phenotype is measured against extracellular pH, distinct from internal pH homeostasis and survival-only states (krulwich2011molecularaspectsof pages 1-3, ramoneda2023buildingagenomebased pages 1-2) | Broad foundational review + comparative ecology | 10.1038/nrmicro2549; 10.1126/sciadv.adf8998 |
| cytoplasmic pH homeostasis | enables growth under non-cytoplasmic external pH | pH growth preference phenotype | General bacteria; many cells keep internal pH near neutral while growing across different external pH values (krulwich2011molecularaspectsof pages 3-5, poolman2023physicochemicalhomeostasisin pages 1-2) | Broad mechanistic review | 10.1038/nrmicro2549; 10.1093/femsre/fuad033 |
| Mrp Na+/H+ antiporter | is required for | alkaline pH homeostasis and alkaliphilic growth | Bacillus pseudofirmus OF4 and related alkaliphiles; mutant evidence summarized in review (krulwich2011molecularaspectsof pages 12-14) | Strong, mutant/perturbation-supported but taxon-specific | 10.1038/nrmicro2549 |
| F1Fo-ATP synthase proton uptake/activity | contributes to | alkaline pH homeostasis | Alkaliphilic Bacillus; motif mutations reduce activity and impair alkaline homeostasis capacity (krulwich2011molecularaspectsof pages 12-14) | Strong, mutant/perturbation-supported but taxon-specific | 10.1038/nrmicro2549 |
| Kdp K+ transport system | is associated with preference for | lower pH conditions | Comparative genomics across soil and freshwater taxa; KdpACD overrepresented in low-pH-preferring taxa (ramoneda2023buildingagenomebased pages 3-5) | Correlation-only genomic association | 10.1126/sciadv.adf8998 |
| amino-acid decarboxylation pathways | consume | cytoplasmic protons | General bacterial acid-stress/homeostasis mechanism; supports low-pH growth by buffering cytoplasm (krulwich2011molecularaspectsof pages 5-6, poolman2023physicochemicalhomeostasisin pages 1-2) | Mechanistic review; causal at pathway level, not trait-specific perturbation here | 10.1038/nrmicro2549; 10.1093/femsre/fuad033 |
| decarboxylase / amino-acid transporter / carboxylate transporter genes | are associated with preference for | lower pH conditions | Comparative genomics across habitats (ramoneda2023buildingagenomebased pages 3-5) | Correlation-only genomic association | 10.1126/sciadv.adf8998 |
| urease + urea transport/periplasmic buffering system | buffers acidity and supports | acid acclimation/growth at low external pH | Helicobacter pylori; membrane-bound urease activity increases at low pH, with pH-responsive regulation (krulwich2011molecularaspectsof pages 11-12) | Strong mechanistic evidence, species-specific | 10.1038/nrmicro2549 |
| urease / ureide permease genes | are associated with preference for | lower pH conditions | Comparative genomics across soil/freshwater bacteria (ramoneda2023buildingagenomebased pages 3-5) | Correlation-only genomic association | 10.1126/sciadv.adf8998 |
| archaeal bipolar tetraether membrane lipids (GDNT/GDGT-rich) | reduce passive proton permeability and help maintain | near-neutral intracellular pH in acidic growth conditions | Thermoacidophilic archaea such as Sulfolobus; membrane composition varies with pH and temperature (chong2024archaeamembranesin pages 1-2) | Strong biophysical/mechanistic review, taxon group-specific | 10.3389/frbis.2023.1338019 |
| acetate biosynthesis | causes | extracellular acidification | Bacillus subtilis biofilms in minimally buffered medium; ΔackAΔacsA shows 48% reduced acidification rate (tran2024activephregulation pages 5-7, tran2024activephregulation pages 2-5) | Strong, mutant/perturbation-supported | 10.1128/mbio.03387-23 |
| acetoin biosynthesis (alsS/alsD pathway) | causes | extracellular alkalinization toward neutrophile range | Bacillus subtilis biofilms; ΔalsS/ΔalsD lose alkalinization phase and buffering-deficient biofilms are developmentally impaired in minimally buffered media (tran2024activephregulation pages 5-7, tran2024activephregulation pages 7-9) | Strong, mutant/perturbation-supported | 10.1128/mbio.03387-23 |
| active extracellular pH regulation | facilitates | biofilm development under minimally buffered conditions | Bacillus subtilis biofilms; phenotype masked in fully buffered media (tran2024activephregulation pages 2-5, tran2024activephregulation pages 7-9) | Strong, assay-specific perturbation evidence | 10.1128/mbio.03387-23 |
| acidic secondary cell-wall components / S-layer acidity | attract/retain | protons at the cell surface | Alkaliphilic Bacillaceae; lowers effective surface pH and supports high-pH growth (goto2022differencesinbioenergetic pages 1-2, coker2019recentadvancesin pages 1-2) | Mechanistic review; some supporting mutant phenotype for surface layer, taxon-specific | 10.3389/fmicb.2022.842785; 10.12688/f1000research.20765.1 |
| membrane-bound cytochrome c with Asn-rich segment | may form | outer-surface H+ capacitor network | Evansella clarkii under low aeration at high pH; cytochrome c abundance 2.5–6.3-fold higher under low aeration (goto2022differencesinbioenergetic pages 1-2) | Uncertain/hypothesis-supported, taxon-specific | 10.3389/fmicb.2022.842785 |
| Na+/H+ antiporter genes (e.g., PhaGF, MnhG, MrpF, YufB) | are associated with preference for | higher pH conditions | Comparative genomics across soil/freshwater bacteria (ramoneda2023buildingagenomebased pages 3-5) | Correlation-only genomic association | 10.1126/sciadv.adf8998 |


*Table: This table compiles the strongest candidate causal edges for microbial pH growth preference, separating perturbation-supported mechanisms from comparative genomic correlations. It is useful for deciding which nodes and edges are ready for TraitMech curation versus which should remain provisional.*

A more curation-oriented evidence table follows. Quoted text is kept short; notes delimit the taxon and inference level.

| Subject–predicate–object | Reference | Supporting snippet | Curation note |
|---|---|---|---|
| External pH **alters** ΔpH and Δψ contributions to PMF | 10.1038/nrmicro2549 | “pH homeostatic demands determine the relative magnitudes” of PMF components | Broad mechanistic edge; PMF mediates effects on ATP production and transport (krulwich2011molecularaspectsof pages 3-5). |
| Cytoplasmic-pH homeostasis **supports** growth outside the cytoplasmic pH range | 10.1038/nrmicro2549 | Neutralophiles maintain approximately pH 7.5–7.7 while growing over external pH 5.5–9.0 | Strong conceptual edge, but represent growth and homeostasis as separate nodes (krulwich2011molecularaspectsof pages 1-3). |
| Mrp Na⁺/H⁺ antiporter **is required for** alkaline homeostasis/growth | 10.1038/nrmicro2549 | “Mutations in mrpA cause loss of alkaliphilic phenotype” | Strong, perturbation-supported, *B. pseudofirmus* OF4/alkaliphile-specific (krulwich2011molecularaspectsof pages 12-14). |
| F₀F₁ ATP synthase proton uptake **contributes to** alkaline pH homeostasis | 10.1038/nrmicro2549 | Motif mutations reduce activity and cause loss of homeostasis during alkaline shifts | Strong but taxon-specific; distinguish ATP synthesis from proton-leak effects (krulwich2011molecularaspectsof pages 12-14). |
| Na⁺/H⁺ or K⁺/H⁺ antiport **imports H⁺ and lowers** excessive cytoplasmic pH | 10.1038/nrmicro2549; 10.1093/femsre/fuad033 | Antiporters “acidify the cytoplasm by exporting K⁺ or Na⁺ in exchange for protons” | Broad mechanistic edge; ion availability determines which antiporter dominates (krulwich2011molecularaspectsof pages 5-6, poolman2023physicochemicalhomeostasisin pages 1-2). |
| Amino-acid decarboxylation **consumes** cytoplasmic H⁺ | 10.1038/nrmicro2549 | GadB “consumes cytoplasmic protons and generates GABA” | Mechanistically strong for acid resistance/homeostasis; direct effect on optimum growth pH may be taxon- and medium-specific (krulwich2011molecularaspectsof pages 5-6). |
| Urease hydrolysis of urea **produces** ammonia and buffers acidic periplasm | 10.1038/nrmicro2549 | Membrane-bound urease activity was twofold greater at pH 4.5 than at pH 7.4 | Strong for *Helicobacter pylori* acid acclimation; UreI/TCS context should accompany the edge (krulwich2011molecularaspectsof pages 11-12). |
| KdpACD presence **is associated with** lower environmental pH preference | 10.1126/sciadv.adf8998 | “overrepresented in taxa with low pH preference in all habitats” | Do **not** encode as causal without perturbation; comparative presence/absence association (ramoneda2023buildingagenomebased pages 3-5). |
| PhaGF/MnhG/MrpF/YufB presence **is associated with** higher environmental pH preference | 10.1126/sciadv.adf8998 | Na⁺/H⁺ antiporters were “overrepresented in taxa with preferences for higher pH” | Provisional association, not a universal gene-to-trait edge (ramoneda2023buildingagenomebased pages 3-5). |
| Tetraether-lipid remodeling **reduces** passive proton permeability | 10.3389/frbis.2023.1338019 | Adjustments permit “a low passive proton permeability and a near neutral intracellular pH” | Plausible group-level mechanism in thermoacidophilic archaea; review wording is partly inferential (“likely”) (chong2024archaeamembranesin pages 1-2). |
| Acetate metabolism **acidifies** the biofilm environment | 10.1128/mbio.03387-23 | ΔackAΔacsA showed “48% reduced acidification rates” | Strong mutant evidence in minimally buffered *B. subtilis* biofilms (tran2024activephregulation pages 5-7, tran2024activephregulation pages 2-5). |
| AlsS/AlsD acetoin biosynthesis **drives** extracellular alkalinization | 10.1128/mbio.03387-23 | ΔalsS and ΔalsD “lose alkalinization phase entirely” | Strong, taxon- and biofilm-specific mutant evidence (tran2024activephregulation pages 5-7). |
| Acetoin-dependent pH regulation **facilitates** biofilm growth/development | 10.1128/mbio.03387-23 | ΔalsS had lower cell counts and lost wrinkles only in minimally buffered medium | Strong assay-specific edge; buffered media eliminate the phenotype (tran2024activephregulation pages 5-7, tran2024activephregulation pages 7-9). |
| Acidic cell-surface polymers **retain** protons near the membrane | 10.3389/fmicb.2022.842785 | Negative charge “will attract H⁺ around the cell surface” | Mechanistically plausible in alkaliphilic Bacillaceae; S-layer-deficient mutants grow more slowly, especially at low Na⁺ (goto2022differencesinbioenergetic pages 1-2). |
| Low aeration **increases** membrane-bound cytochrome *c* | 10.3389/fmicb.2022.842785 | abundance was “2.5–6.3-fold higher” under low aeration | Observed association in *E. clarkii*; the downstream “H⁺ capacitor” remains a proposed model, not a settled causal edge (goto2022differencesinbioenergetic pages 1-2). |

## 4. Recent developments and quantitative evidence

### Genome-based inference of pH preference

Ramoneda et al. identified **332 gene types** with a consistent significant association in at least two datasets and **56** with the same directional association in at least three datasets across soil and freshwater; **30 of the 56** had prior links to pH adaptation. No gene was significant in every dataset, emphasizing habitat and taxonomic contingency. The authors explicitly state that the associations cannot confirm adaptation or causation (ramoneda2023buildingagenomebased pages 3-5).

This study is valuable for candidate-node discovery but not for direct causal curation. It found all four commonly discussed acid-response modules among associated genes: proton-consuming reactions, basic-compound production, proton efflux/ion transport, and membrane/protein protection (ramoneda2023buildingagenomebased pages 3-5).

### Biofilm-driven environmental pH regulation

In minimally buffered *B. subtilis* biofilms, pH initially fell to **5.5** at **0.06 ± 0.0008 pH units h⁻¹** for **15.0 ± 0.3 h**, then rose to **6.9** at **0.03 ± 0.0005 pH units h⁻¹** over **31.2 ± 0.5 h**. A planktonic ΔsinI mutant lacked the alkalinization phase. The ΔalsS mutant downregulated **16 of 18** extracellular-matrix-associated genes under minimally buffered conditions, linking pH regulation to community development rather than only single-cell homeostasis (tran2024activephregulation pages 2-5, tran2024activephregulation pages 7-9).

### Current understanding of bacterial physicochemical homeostasis

A 2023 expert review identifies Na⁺/H⁺ and K⁺/H⁺ antiporters, respiratory proton pumps, F₀F₁ ATPase, and metabolite decarboxylation as principal regulators. Depending on species, F₀F₁ ATP synthase uses approximately **three to five protons per ATP**. The review stresses that internal pH and energy status are coupled; a graph that ends at “cytoplasmic pH” misses downstream ATP synthesis, transport, macromolecular function, and growth (poolman2023physicochemicalhomeostasisin pages 1-2).

### Archaeal membrane biophysics

Thermoacidophiles inhabiting pH ≤4 and temperatures ≥65°C are enriched in bipolar tetraether lipids. Environmental pH can alter cyclopentane rings, GDNT:GDGT ratio, tetraether:diether ratio, and head-group glycosylation. These changes alter packing and hydrogen-bond networks and are proposed to maintain low proton permeability and near-neutral intracellular pH (chong2024archaeamembranesin pages 1-2).

## 5. Applications and real-world implementation

1. **Cultivation and isolate recovery.** Genome-informed preference models can prioritize pH conditions for uncultivated taxa, but ecological preference predictions should be experimentally validated because they estimate realized rather than fundamental niches (ramoneda2023buildingagenomebased pages 1-2, ramoneda2023buildingagenomebased pages 3-5).
2. **Microbial inoculant and community design.** pH-associated genomic features can help select taxa for soils, freshwater systems, probiotics, or engineered consortia, while acknowledging that taxonomy alone is a poor predictor (ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 1-2).
3. **Biofilm control.** The *B. subtilis* acetate–acetoin circuit suggests targets for preventing biofilm development in weakly buffered environments. Strong laboratory buffering may conceal relevant intervention phenotypes (tran2024activephregulation pages 1-2, tran2024activephregulation pages 7-9).
4. **High-pH biotechnology.** Alkaliphile antiporters, ATP synthases, acidic surface polymers, and proton-retention strategies support growth and catalysis under alkaline industrial conditions. Their performance can depend strongly on sodium and aeration (krulwich2011molecularaspectsof pages 12-14, goto2022differencesinbioenergetic pages 1-2).
5. **Acidic bioprocesses and biomining.** Proton-impermeable archaeal membranes, decarboxylation systems, and urease-mediated buffering provide engineering targets for low-pH production or survival, although growth preference must be measured separately from short-term acid tolerance (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 11-12, chong2024archaeamembranesin pages 1-2).

## 6. Recommended graph architecture

A compact cross-taxon backbone is:

**external pH → transmembrane ΔpH / proton flux → cytoplasmic pH + PMF → enzyme, membrane, ATP-synthesis and transport performance → population growth rate/extent → METPO:1003000**.

Taxon-specific branches can then be attached:

- **acid branch:** proton entry → decarboxylation, respiratory/F₀F₁ proton export, urea–urease buffering, K⁺ uptake/reversed Δψ, low-permeability membranes;
- **alkaline branch:** proton scarcity/cytoplasmic alkalinization → Na⁺/H⁺ or K⁺/H⁺ antiport, Mrp, F₀F₁ proton capture, acidic cell surface, localized proton retention;
- **environment-modification branch:** overflow acetate → extracellular acidification; AlsS/AlsD acetoin production → alkalinization → biofilm development.

This architecture avoids asserting that one mechanism universally determines preference. It also allows an edge to carry taxon, strain, medium, aeration, and evidence-strength qualifiers.

## 7. Claims not yet suitable for TraitMech curation

- **Do not curate gene–preference associations from Ramoneda et al. as causal.** They are cross-genome associations with possible pleiotropy, phylogenetic structure, and habitat dependence; no gene was significant in every dataset (ramoneda2023buildingagenomebased pages 3-5).
- **Do not equate realized environmental preference with optimum growth pH.** Relative abundance includes competition and other abiotic effects (ramoneda2023buildingagenomebased pages 1-2).
- **Do not generalize alkaliphile mechanisms to all bacteria or archaea.** Mrp dependence, surface polymers, and ATP-synthase adaptations are often strain- or lineage-specific (krulwich2011molecularaspectsof pages 12-14, goto2022differencesinbioenergetic pages 1-2).
- **Do not curate the *E. clarkii* cytochrome-*c* “H⁺ capacitor” as established causation.** Increased cytochrome abundance is measured, but capacitor formation is proposed (“may influence”) (goto2022differencesinbioenergetic pages 1-2).
- **Do not infer growth preference from survival-only acid-challenge assays.** Recovery after stress establishes resistance, not net growth under that pH (krulwich2011molecularaspectsof pages 1-3).
- **Do not omit assay buffering.** The *B. subtilis* mechanism disappears phenotypically in strongly buffered medium (tran2024activephregulation pages 2-5, tran2024activephregulation pages 7-9).
- **Do not assign universal UniProt, KEGG, or EC identifiers to family-level nodes without fixing organism and reaction.** Mrp subunit nomenclature and ion specificity vary.
- **Treat archaeal lipid remodeling as provisional unless linked to direct perturbation and growth measurements.** Current review-level synthesis uses qualified language and combines pH with temperature and growth-rate effects (chong2024archaeamembranesin pages 1-2).

## 8. DOI-first bibliography

1. Ramoneda J. et al. **Building a genome-based understanding of bacterial pH preferences.** *Science Advances* 9, eadf8998. Published **28 April 2023**. DOI: [10.1126/sciadv.adf8998](https://doi.org/10.1126/sciadv.adf8998). (ramoneda2023buildingagenomebased pages 1-2, ramoneda2023buildingagenomebased pages 3-5)
2. Poolman B. **Physicochemical homeostasis in bacteria.** *FEMS Microbiology Reviews* 47. Published online **19 June 2023**. DOI: [10.1093/femsre/fuad033](https://doi.org/10.1093/femsre/fuad033). (poolman2023physicochemicalhomeostasisin pages 1-2)
3. Tran P., Lander S.M., Prindle A. **Active pH regulation facilitates Bacillus subtilis biofilm development in a minimally buffered environment.** *mBio* 15. Published **March 2024**. DOI: [10.1128/mbio.03387-23](https://doi.org/10.1128/mbio.03387-23). (tran2024activephregulation pages 5-7, tran2024activephregulation pages 2-5, tran2024activephregulation pages 7-9)
4. Chong P.L.-G. **Archaea membranes in response to extreme acidic environments.** *Frontiers in Biophysics* 1:1338019. Published **4 January 2024**. DOI: [10.3389/frbis.2023.1338019](https://doi.org/10.3389/frbis.2023.1338019). (chong2024archaeamembranesin pages 1-2)
5. Goto T. et al. **Differences in Bioenergetic Metabolism of Obligately Alkaliphilic Bacillaceae Under High pH Depend on the Aeration Conditions.** *Frontiers in Microbiology* 13:842785. Published **18 March 2022**. DOI: [10.3389/fmicb.2022.842785](https://doi.org/10.3389/fmicb.2022.842785). (goto2022differencesinbioenergetic pages 1-2)
6. Krulwich T.A., Sachs G., Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology* 9:330–343. Published **May 2011**. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 1-3)
7. Coker J.A. **Recent advances in understanding extremophiles.** *F1000Research* 8:1917. Published **November 2019**. DOI: [10.12688/f1000research.20765.1](https://doi.org/10.12688/f1000research.20765.1). (coker2019recentadvancesin pages 1-2)

## Curation recommendation

For `ph_growth_preference.yaml`, curate the general backbone plus only the strongest experimentally supported branches—Mrp/alkaline homeostasis, F₀F₁ proton transport, urease-mediated acid buffering, and the *B. subtilis* acetate–acetoin biofilm circuit—with explicit taxon and assay qualifiers. Store the 2023 comparative-genomic gene associations, archaeal lipid remodeling, and *E. clarkii* H⁺-capacitor model as provisional evidence rather than unqualified causal edges.

References

1. (ramoneda2023buildingagenomebased pages 1-2): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

3. (poolman2023physicochemicalhomeostasisin pages 1-2): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 46 citations and is from a domain leading peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

5. (tran2024activephregulation pages 2-5): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. mBio, Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 33 citations and is from a domain leading peer-reviewed journal.

6. (tran2024activephregulation pages 7-9): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. mBio, Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 33 citations and is from a domain leading peer-reviewed journal.

7. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

8. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

9. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

10. (krulwich2011molecularaspectsof pages 11-12): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

11. (chong2024archaeamembranesin pages 1-2): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

12. (tran2024activephregulation pages 5-7): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. mBio, Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 33 citations and is from a domain leading peer-reviewed journal.

13. (goto2022differencesinbioenergetic pages 1-2): Toshitaka Goto, Shinichi Ogami, Kazuaki Yoshimume, and Isao Yumoto. Differences in bioenergetic metabolism of obligately alkaliphilic bacillaceae under high ph depend on the aeration conditions. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.842785, doi:10.3389/fmicb.2022.842785. This article has 6 citations and is from a peer-reviewed journal.

14. (coker2019recentadvancesin pages 1-2): James A Coker. Recent advances in understanding extremophiles. F1000Research, 8:1917, Nov 2019. URL: https://doi.org/10.12688/f1000research.20765.1, doi:10.12688/f1000research.20765.1. This article has 108 citations and is from a peer-reviewed journal.

15. (tran2024activephregulation pages 1-2): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. mBio, Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 33 citations and is from a domain leading peer-reviewed journal.