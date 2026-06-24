---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:36:19.830619'
end_time: '2026-06-18T12:44:25.733581'
duration_seconds: 485.9
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: urease activity
  trait_identifier: traitmech:000077
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: urease_activity
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A physiological enzyme-activity phenotype in which a cell produces urease,
    which hydrolyzes urea to ammonia and carbon dioxide, typically raising local pH;
    it is the basis of the diagnostic urease test.
  parent_traits: METPO:1000059
  synonyms: urease-positive
  evidence_summary: 'DOI:10.1128/mr.59.3.451-480.1995:  (Mobley, Island & Hausinger
    review the molecular biology of microbial ureases that hydrolyze urea to ammonia
    and carbon dioxide.) | DOI:10.1128/mr.53.1.85-108.1989:  (Mobley & Hausinger review
    the significance and regulation of microbial ureases.)'
  causal_graph_summary: 'urease_activity_urea_hydrolysis: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** urease activity
- **METPO identifier:** traitmech:000077
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological enzyme-activity phenotype in which a cell produces urease, which hydrolyzes urea to ammonia and carbon dioxide, typically raising local pH; it is the basis of the diagnostic urease test.
- **Parent traits:** METPO:1000059
- **Synonyms:** urease-positive
- **Existing evidence:** DOI:10.1128/mr.59.3.451-480.1995:  (Mobley, Island & Hausinger review the molecular biology of microbial ureases that hydrolyze urea to ammonia and carbon dioxide.) | DOI:10.1128/mr.53.1.85-108.1989:  (Mobley & Hausinger review the significance and regulation of microbial ureases.)
- **Existing causal graph summary:** urease_activity_urea_hydrolysis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **urease activity** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/urease_activity.yaml`.

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
- **Trait label:** urease activity
- **METPO identifier:** traitmech:000077
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological enzyme-activity phenotype in which a cell produces urease, which hydrolyzes urea to ammonia and carbon dioxide, typically raising local pH; it is the basis of the diagnostic urease test.
- **Parent traits:** METPO:1000059
- **Synonyms:** urease-positive
- **Existing evidence:** DOI:10.1128/mr.59.3.451-480.1995:  (Mobley, Island & Hausinger review the molecular biology of microbial ureases that hydrolyze urea to ammonia and carbon dioxide.) | DOI:10.1128/mr.53.1.85-108.1989:  (Mobley & Hausinger review the significance and regulation of microbial ureases.)
- **Existing causal graph summary:** urease_activity_urea_hydrolysis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **urease activity** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/urease_activity.yaml`.

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


# Research Report: Microbial Trait “Urease Activity” (METPO traitmech:000077)

## 1) Scope summary (trait definition and boundaries)
Urease activity is a physiological enzyme-activity phenotype in which a microbe produces functional urease (EC 3.5.1.5) that catalyzes urea hydrolysis, generating alkalinity (OH−) and nitrogen/carbon products (NH4+ and CO2), thereby typically raising local pH and enabling assay detection in urease tests (e.g., phenol red yellow→pink readout). The reaction is explicitly given as: “(NH2)2CO + 2H2O + urease → 2 NH4+ + 2 OH- + CO2 + urease”. (stabnikov2024microbialproducerof pages 1-3)

**Boundary cases / nearby traits**
- **Urea utilization vs. urease-positive phenotype:** Urease activity is about the enzymatic capacity to hydrolyze urea; downstream nitrogen assimilation/urea transport are separable processes and should not be conflated unless directly evidenced.
- **Carbonate precipitation without ureolysis:** Microbial-induced carbonate precipitation (MICP) can occur through non-ureolytic pathways; urease-mediated MICP is described as a common mechanism but is not synonymous with MICP in general. (saracho2024uncoveringthedynamics pages 9-13)
- **Acid-tolerant/acid-optimum ureases:** Some systems emphasize “acid urease” activity (optimum pH ~4.5–5.5), which is mechanistically still urease activity but affects where and how the phenotype is expressed and measured. (stabnikov2024microbialproducerof pages 1-3)

## 2) Key concepts and current understanding (mechanism-focused)
### 2.1 Core chemistry and pH effects
Ureolysis produces NH4+ and OH−, causing pH to increase; in a ureolytic bacterium system (Sporosarcina pasteurii), this alkalinization is described along with a physicochemical cap near pH 9.25 associated with the NH3 pKa (~9.24). (saracho2024uncoveringthedynamics pages 9-13)

### 2.2 Metal cofactor requirement and urease maturation (Ni-dependent activation)
In *Helicobacter pylori*, urease is described as a heterodimer of UreA and UreB and contains “two nickel ions at each active site,” and the urease cluster includes “seven accessory genes required for enzyme activation and nickel insertion.” (shaalan2024theeffectof pages 1-2)

Recent 2024 work emphasizing accessory-protein targeting in rumen microbiology summarizes the Ni-delivery chain and maturation logic: “nickel is transferred from UreE to UreG,” and “Ni-UreG delivers nickel to apo-urease” in the context of a maturation “supercomplex apo-urease/UreFHG in *Helicobacter pylori*,” with nickel insertion depending on UreG GTP hydrolysis and conformational change. (zhang2024epiberberineapotential pages 1-2)

### 2.3 Systems coupling: carbonic anhydrase (CA) and carbonate chemistry
In *S. pasteurii* under varying CO2(g), carbonic anhydrase is implicated in CO2 hydration to bicarbonate and buffering. The authors report: “Ur gene up-regulation coincides with an increase in [HCO3-] following the hydration of CO2 to HCO3- by CA,” and state “CA physiologically promotes buffering… [and] affects the phase of the CaCO3 mineral formed.” (saracho2024uncoveringthedynamics pages 5-9)

## 3) Recent developments and latest research (prioritizing 2023–2024)
### 3.1 Quantitative ureolysis kinetics under CO2 (CO2-trapping/MICP context; 2024)
Saracho & Marek (2024) quantified biomass-normalized ureolysis kinetics in *S. pasteurii* across headspace CO2. Reported first-order biomass-normalized rate constants (k′1) decreased as CO2 increased: 1.1×10−10, 1.9×10−11, and 3.3×10−12 L·h−1·CFU−1 at 0.04, 15, and 55 vol% CO2, respectively. They also specify assay definitions (e.g., “one Ur unit = hydrolysis of 1 µmol urea per min”) and that urease activity was assayed via ammonia release using the Berthelot method. (saracho2024uncoveringthedynamics pages 9-13, saracho2024uncoveringthedynamics pages 5-9)

### 3.2 Quantitative inhibitor effects on *H. pylori* urease and viability (2024)
A clinical-isolate study (49 *H. pylori* isolates) evaluated acetohydroxamic acid (AHA), baicalin, and ebselen using a phenol red urease assay and flow cytometry viability readouts. Key quantitative findings included:
- AHA at 2.5 mM produced “almost full urease inhibition (84% reduction).” (shaalan2024theeffectof pages 3-5)
- Baicalin produced a “50% reduction at 8 mM.” (shaalan2024theeffectof pages 3-5)
- Ebselen produced a “71% urease activity reduction even at 0.03 mM.” (shaalan2024theeffectof pages 3-5)
- Flow cytometry viability: AHA reduced viable cells to 21.9% vs 74.4% controls; baicalin and ebselen produced large viability decreases (~61.82% and 60.97%). (shaalan2024theeffectof pages 3-5)
The same paper provides mechanistic framing: AHA is described as a competitive inhibitor that complexes Ni at the urease metallocenter; baicalin as non-competitive interacting with a mobile flap cysteine; ebselen as competitive reacting with Ni ions and cysteine. (shaalan2024theeffectof pages 2-3)

Supporting visual evidence (Table/Figures) for inhibitor concentrations and outcome plots was retrieved (Table 1 and Figures 2–5; Table 3). (shaalan2024theeffectof media 1849fa05, shaalan2024theeffectof media 9e1ae2ae, shaalan2024theeffectof media 0d248d40, shaalan2024theeffectof media 66699e8f, shaalan2024theeffectof media bfb43865, shaalan2024theeffectof media d8c18288)

### 3.3 Targeting urease maturation (UreG) to reduce ruminal ammonia (2024)
Zhang et al. (2024) developed an inhibitor-screening strategy targeting UreG (an accessory GTPase required for Ni insertion/maturation). Epiberberine inhibited Ni association with UreG and was linked to decreased ammonia release in rumen fermentation experiments, with NH3 reductions reported as 13.1% and 15.6% (at tested doses). (zhang2024epiberberineapotential pages 5-7)

### 3.4 Multi-target botanical inhibition of *H. pylori* (2024)
Zhu et al. (2024) report Triphala has in vitro activity against *H. pylori* with MICs 80–320 μg/mL and downregulates urease-related genes “ureA, ureB, ureE, ureF,” alongside inhibition of urease activity and other virulence-associated phenotypes. (zhu2024preliminaryinvestigationof pages 11-12)

## 4) Current applications and real-world implementations
### 4.1 Clinical microbiology and pathogenesis: *H. pylori* survival in acid
Clinical/pathogenesis framing remains a primary application of urease activity as a trait: *H. pylori* urease creates a “neutral microenvironment” enabling survival in acidic gastric conditions. This physiological role underlies urease-based diagnostics and motivates urease inhibition as a therapeutic strategy. (shaalan2024theeffectof pages 1-2)

### 4.2 Geotechnical and environmental biotechnology: ureolysis-driven biocementation/MICP
Urease activity is central to ureolysis-driven biocementation because it generates alkalinity and carbonate chemistry that can precipitate minerals. A 2024 biocementation-focused article provides the ureolysis reaction and notes pH changes that support precipitation; it reports environmental pH in such processes can reach ~8.5–9.5 and provides application metrics (e.g., biocemented sand water permeability 2×10−5 m/s). (stabnikov2024microbialproducerof pages 1-3)

In CO2-trapping/MICP research, urease and carbonic anhydrase are treated as coupled biocatalysts influencing carbonate precipitation and mineral phase under controlled CO2 conditions. (saracho2024uncoveringthedynamics pages 5-9)

### 4.3 Agriculture/animal nutrition: reducing ammonia emissions from rumen ureolysis
Targeting urease accessory maturation via UreG inhibition is presented as an emerging route to reduce ruminal NH3 release and improve nitrogen utilization, with epiberberine proposed as a candidate feed additive. (zhang2024epiberberineapotential pages 5-7, zhang2024epiberberineapotential pages 1-2)

## 5) Candidate causal-graph nodes (grouped by type, with ontology grounding where possible)
### Phenotype node
- **Urease activity** (METPO: traitmech:000077; enzyme activity **EC:3.5.1.5**) (stabnikov2024microbialproducerof pages 1-3)

### Chemicals / metabolites / ions (CHEBI)
- **Urea** (CHEBI:16199) (stabnikov2024microbialproducerof pages 1-3)
- **Ammonium (NH4+)** (CHEBI:28938) (stabnikov2024microbialproducerof pages 1-3)
- **Hydroxide (OH−)** (CHEBI:16234) (stabnikov2024microbialproducerof pages 1-3)
- **Carbon dioxide (CO2)** (CHEBI:16526) (stabnikov2024microbialproducerof pages 1-3)
- **Bicarbonate (HCO3−)** (CHEBI:17544) (saracho2024uncoveringthedynamics pages 5-9)
- **Nickel(2+)** (CHEBI:49786) (shaalan2024theeffectof pages 1-2)
- **Calcium carbonate** (CHEBI:3311) (saracho2024uncoveringthedynamics pages 5-9)

### Enzymes / proteins / complexes
- **Urease structural subunits:** UreA, UreB (label-only; taxon-specific naming in *H. pylori*) (shaalan2024theeffectof pages 1-2)
- **Urease accessory maturation proteins:** UreE, UreG (label-only; Ni transfer/maturation) (zhang2024epiberberineapotential pages 1-2)
- **Accessory complex:** UreFHG supercomplex (label-only; *H. pylori* context) (zhang2024epiberberineapotential pages 1-2)
- **Carbonic anhydrase** (EC:4.2.1.1) (saracho2024uncoveringthedynamics pages 5-9)

### Genes (label-only unless curated to specific database IDs)
- **ureA, ureB** (*H. pylori*; expression measured by RT-qPCR) (shaalan2024theeffectof pages 2-3, shaalan2024theeffectof pages 3-5)
- **ureC** (*S. pasteurii* qPCR target for urease gene dynamics) (saracho2024uncoveringthedynamics pages 9-13)
- **ureE, ureF** (*H. pylori* downregulated by Triphala) (zhu2024preliminaryinvestigationof pages 11-12)

### Environmental / experimental factors
- **pH** (PATO:0000196) (saracho2024uncoveringthedynamics pages 9-13)
- **CO2(g) headspace concentration** (0.04–60 vol% tested) (saracho2024uncoveringthedynamics pages 5-9)
- **Assay context:** phenol red urease assay (OD570), Berthelot ammonia assay, flow cytometry viability, RT-qPCR (saracho2024uncoveringthedynamics pages 5-9, shaalan2024theeffectof pages 2-3, shaalan2024theeffectof pages 3-5)

### Inhibitors / interventions (CHEBI where available)
- **Acetohydroxamic acid (AHA)** (CHEBI:15699) (shaalan2024theeffectof pages 1-2)
- **Baicalin** (CHEBI:6391) (shaalan2024theeffectof pages 1-2)
- **Ebselen** (CHEBI:91488) (shaalan2024theeffectof pages 1-2)
- **Epiberberine** (CHEBI:140350; used as UreG-targeting inhibitor in rumen context) (zhang2024epiberberineapotential pages 5-7)
- **Triphala** (label-only mixture/extract) (zhu2024preliminaryinvestigationof pages 11-12)

## 6) Evidence-backed candidate causal edges (curation-oriented)
The table below compiles candidate edges as subject–predicate–object triples with direct snippets, DOI/URL/year, and curation notes.

| Subject node (CURIE) | Predicate | Object node (CURIE) | Evidence snippet | Reference (DOI / URL / year) | Notes |
|---|---|---|---|---|---|
| urea (CHEBI:16199) | is hydrolyzed by | urease activity (EC:3.5.1.5) | “(NH2)2CO + 2H2O + urease → 2 NH4+ + 2 OH- + CO2 + urease” | 10.24263/2304-974x-2024-13-2-10 / https://doi.org/10.24263/2304-974x-2024-13-2-10 / 2024 (stabnikov2024microbialproducerof pages 1-3) | Core reaction for the trait; directly supports urease-positive phenotype. |
| urease activity (EC:3.5.1.5) | produces | ammonium (CHEBI:28938) | “(NH2)2CO + 2H2O + urease → 2 NH4+ + 2 OH- + CO2 + urease” | 10.24263/2304-974x-2024-13-2-10 / https://doi.org/10.24263/2304-974x-2024-13-2-10 / 2024 (stabnikov2024microbialproducerof pages 1-3) | Product node should likely be ammonium rather than free ammonia under many assay conditions. |
| urease activity (EC:3.5.1.5) | produces | hydroxide (CHEBI:16234) | “(NH2)2CO + 2H2O + urease → 2 NH4+ + 2 OH- + CO2 + urease” | 10.24263/2304-974x-2024-13-2-10 / https://doi.org/10.24263/2304-974x-2024-13-2-10 / 2024 (stabnikov2024microbialproducerof pages 1-3) | Hydroxide production mechanistically explains alkalinization. |
| urease activity (EC:3.5.1.5) | produces | carbon dioxide (CHEBI:16526) | “(NH2)2CO + 2H2O + urease → 2 NH4+ + 2 OH- + CO2 + urease” | 10.24263/2304-974x-2024-13-2-10 / https://doi.org/10.24263/2304-974x-2024-13-2-10 / 2024 (stabnikov2024microbialproducerof pages 1-3) | CO2 product can feed carbonate chemistry and CA-linked processes. |
| urease activity (EC:3.5.1.5) | increases | pH (PATO:0000196) | “Urea hydrolysis produces NH4+ and OH−, causing a pH increase” | 10.1021/acs.est.3c06617 / https://doi.org/10.1021/acs.est.3c06617 / 2024 (saracho2024uncoveringthedynamics pages 9-13) | Generalizable to urease-positive phenotype; assay-visible via urease test color change. |
| urease activity (EC:3.5.1.5) | enables | neutral microenvironment [candidate] | “generating a neutral microenvironment that enables survival in the acidic gastric environment” | 10.3389/fmicb.2024.1464484 / https://doi.org/10.3389/fmicb.2024.1464484 / 2024 (shaalan2024theeffectof pages 1-2) | Taxon-specific to *H. pylori* gastric colonization context. |
| UreA/UreB urease structural complex [candidate] | has cofactor | nickel(2+) (CHEBI:49786) | “urease is a heterodimer of UreA and UreB with two nickel ions at each active site” | 10.3389/fmicb.2024.1464484 / https://doi.org/10.3389/fmicb.2024.1464484 / 2024 (shaalan2024theeffectof pages 1-2) | Strong support for Ni requirement in *H. pylori* urease; subunit naming is taxon-specific. |
| UreE (protein) | transfers | nickel(2+) (CHEBI:49786) to UreG (protein) | “nickel is transferred from UreE to UreG” | 10.1007/s00253-024-13131-4 / https://doi.org/10.1007/s00253-024-13131-4 / 2024 (zhang2024epiberberineapotential pages 1-2) | Supports accessory maturation step; organismal framing includes *H. pylori* literature and rumen urease context. |
| Ni-UreG (protein complex) | delivers | nickel(2+) (CHEBI:49786) to apo-urease [candidate] | “Ni-UreG delivers nickel to apo-urease during formation of a supercomplex apo-urease/UreFHG in Helicobacter pylori” | 10.1007/s00253-024-13131-4 / https://doi.org/10.1007/s00253-024-13131-4 / 2024 (zhang2024epiberberineapotential pages 1-2) | Strong but taxon-specific maturation mechanism; apo-urease node may remain label-only if no stable CURIE. |
| GTP hydrolysis (GO:0003924) by UreG | enables | nickel delivery to apo-urease [candidate] | “nickel insertion depends on GTP hydrolysis and conformational changes of UreG” | 10.1007/s00253-024-13131-4 / https://doi.org/10.1007/s00253-024-13131-4 / 2024 (zhang2024epiberberineapotential pages 1-2) | Causal edge for maturation; best modeled with UreG as mediator. |
| carbonic anhydrase activity (EC:4.2.1.1) | increases | bicarbonate (CHEBI:17544) | “Ur gene up-regulation coincides with an increase in [HCO3-] following the hydration of CO2 to HCO3- by CA” | 10.1021/acs.est.3c06617 / https://doi.org/10.1021/acs.est.3c06617 / 2024 (saracho2024uncoveringthedynamics pages 5-9) | Supports CA→bicarbonate edge in ureolytic systems. |
| increased bicarbonate (CHEBI:17544) | is associated with up-regulation of | ureC gene [candidate] | “Ur gene up-regulation coincides with an increase in [HCO3-]” | 10.1021/acs.est.3c06617 / https://doi.org/10.1021/acs.est.3c06617 / 2024 (saracho2024uncoveringthedynamics pages 5-9) | Association in *Sporosarcina pasteurii*; likely curate as uncertain/regulatory correlation rather than direct causation. |
| carbonic anhydrase activity (EC:4.2.1.1) | physiologically promotes | buffering [candidate] | “CA physiologically promotes buffering” | 10.1021/acs.est.3c06617 / https://doi.org/10.1021/acs.est.3c06617 / 2024 (saracho2024uncoveringthedynamics pages 5-9) | Useful environmental-process node; wording is source-direct. |
| carbonic anhydrase activity (EC:4.2.1.1) | affects | calcium carbonate precipitation (CHEBI:3311) | “CA physiologically promotes buffering, which enhances solubility trapping and affects the phase of the CaCO3 mineral formed” | 10.1021/acs.est.3c06617 / https://doi.org/10.1021/acs.est.3c06617 / 2024 (saracho2024uncoveringthedynamics pages 5-9) | Good edge for MICP context; phase effects are condition-dependent. |
| urease activity (EC:3.5.1.5) | drives | microbially induced carbonate precipitation [candidate] | “the urease enzyme generated by the bacteria catalyzes the hydrolysis of urea” in “the most common type of microbial-induced carbonate precipitation” | 10.1038/s41598-023-33070-w / https://doi.org/10.1038/s41598-023-33070-w / 2023 (saracho2024uncoveringthedynamics pages 9-13) | MICP edge is well supported but application-specific rather than universally trait-defining. |
| acetohydroxamic acid (CHEBI:15699) | inhibits | *Helicobacter pylori* urease activity (EC:3.5.1.5) | “AHA inhibited urease activity at 2.5 mM” | 10.3389/fmicb.2024.1464484 / https://doi.org/10.3389/fmicb.2024.1464484 / 2024 (shaalan2024theeffectof pages 1-2) | Assay-specific concentration from phenol red assay. |
| acetohydroxamic acid (CHEBI:15699) | reduces | *H. pylori* viability [candidate] | “All three inhibitors significantly reduced H. pylori viability” | 10.3389/fmicb.2024.1464484 / https://doi.org/10.3389/fmicb.2024.1464484 / 2024 (shaalan2024theeffectof pages 1-2) | Effect may be partially urease-dependent and assay-specific; avoid overgeneralization. |
| baicalin (CHEBI:6391) | inhibits | *Helicobacter pylori* urease activity (EC:3.5.1.5) | “Baicalin showed inhibition at lower concentrations but required major effects at 8 mM” | 10.3389/fmicb.2024.1464484 / https://doi.org/10.3389/fmicb.2024.1464484 / 2024 (shaalan2024theeffectof pages 1-2) | Strong assay support; concentration-dependent. |
| ebselen (CHEBI:91488) | inhibits | *Helicobacter pylori* urease activity (EC:3.5.1.5) | “Ebselen’s major inhibition occurred at 0.06 mM” | 10.3389/fmicb.2024.1464484 / https://doi.org/10.3389/fmicb.2024.1464484 / 2024 (shaalan2024theeffectof pages 1-2) | Assay-specific; potent relative to AHA/baicalin in this isolate set. |
| urease inhibition in *H. pylori* [candidate] | is associated with reduced | viability [candidate] | “All three inhibitors significantly reduced H. pylori viability” | 10.3389/fmicb.2024.1464484 / https://doi.org/10.3389/fmicb.2024.1464484 / 2024 (shaalan2024theeffectof pages 1-2) | Do not over-curate as direct universal causal edge; inhibitors may have off-target effects. |
| urease inhibitor exposure [candidate] | up-regulates | ureA gene [candidate] | “ureA and ureB were upregulated after inhibitor exposure” | 10.3389/fmicb.2024.1464484 / https://doi.org/10.3389/fmicb.2024.1464484 / 2024 (shaalan2024theeffectof pages 3-5) | Regulatory compensation in *H. pylori*; likely inhibitor- and assay-specific. |
| urease inhibitor exposure [candidate] | up-regulates | ureB gene [candidate] | “ureA and ureB were upregulated after inhibitor exposure” | 10.3389/fmicb.2024.1464484 / https://doi.org/10.3389/fmicb.2024.1464484 / 2024 (shaalan2024theeffectof pages 3-5) | Same caution as above. |
| epiberberine (CHEBI:140350) | inhibits | UreG GTPase activity [candidate] | “epiberberine exerted superior inhibition potential… based on GTPase activity study of UreG” | 10.1007/s00253-024-13131-4 / https://doi.org/10.1007/s00253-024-13131-4 / 2024 (zhang2024epiberberineapotential pages 9-10, zhang2024epiberberineapotential pages 1-2) | Best modeled against maturation rather than catalytic urease active site. |
| epiberberine (CHEBI:140350) | inhibits | nickel binding to UreG [candidate] | “epiberberine was… more effective than berberine chloride in inhibiting the combination of nickel towards UreG” | 10.1007/s00253-024-13131-4 / https://doi.org/10.1007/s00253-024-13131-4 / 2024 (zhang2024epiberberineapotential pages 5-7) | Supports accessory-protein inhibition mechanism. |
| epiberberine (CHEBI:140350) | decreases | ammonia release (CHEBI:16134) | “lowered NH3 release (decreases of 13.1% and 15.6% at tested doses)” | 10.1007/s00253-024-13131-4 / https://doi.org/10.1007/s00253-024-13131-4 / 2024 (zhang2024epiberberineapotential pages 5-7) | Rumen fermentation context; application-specific. |
| Triphala [candidate] | down-regulates | ureA gene [candidate] | “downregulating… urease-related genes (ureA, ureB, ureE, ureF)” | 10.3389/fphar.2024.1438193 / https://doi.org/10.3389/fphar.2024.1438193 / 2024 (zhu2024preliminaryinvestigationof pages 11-12) | Plant extract; multi-target effect, not urease-specific. |
| Triphala [candidate] | down-regulates | ureB gene [candidate] | “downregulating… urease-related genes (ureA, ureB, ureE, ureF)” | 10.3389/fphar.2024.1438193 / https://doi.org/10.3389/fphar.2024.1438193 / 2024 (zhu2024preliminaryinvestigationof pages 11-12) | Same caution. |
| Triphala [candidate] | down-regulates | ureE gene [candidate] | “downregulating… urease-related genes (ureA, ureB, ureE, ureF)” | 10.3389/fphar.2024.1438193 / https://doi.org/10.3389/fphar.2024.1438193 / 2024 (zhu2024preliminaryinvestigationof pages 11-12) | Accessory-gene regulation evidence in *H. pylori*. |
| Triphala [candidate] | down-regulates | ureF gene [candidate] | “downregulating… urease-related genes (ureA, ureB, ureE, ureF)” | 10.3389/fphar.2024.1438193 / https://doi.org/10.3389/fphar.2024.1438193 / 2024 (zhu2024preliminaryinvestigationof pages 11-12) | Accessory-gene regulation evidence in *H. pylori*. |
| Triphala [candidate] | inhibits | *Helicobacter pylori* urease activity (EC:3.5.1.5) | “Triphala has significant inhibitory effects on H. pylori urease activity” | 10.3389/fphar.2024.1438193 / https://doi.org/10.3389/fphar.2024.1438193 / 2024 (zhu2024preliminaryinvestigationof pages 11-12) | Useful application/inhibitor edge; extract is pleiotropic and not trait-defining. |


*Table: This table lists evidence-backed candidate causal graph edges for the microbial trait urease activity, including core chemistry, maturation, regulation, biomineralization, and inhibitor effects. It is useful for TraitMech curation because each row links a proposed edge to a direct literature snippet, DOI/URL, and curation notes about specificity or uncertainty.*

## 7) Statistics and data highlights (from recent studies)
- **Ureolysis kinetics under CO2:** k′1 decreased from 1.1×10−10 to 3.3×10−12 L·h−1·CFU−1 as CO2 increased from 0.04 to 55 vol% in *S. pasteurii*. (saracho2024uncoveringthedynamics pages 9-13)
- **pH behavior:** ureolysis-driven alkalinization noted with a cap near pH 9.25 (linked to NH3 pKa ≈ 9.24). (saracho2024uncoveringthedynamics pages 9-13)
- ***H. pylori* inhibitor outcomes (49 isolates):** AHA 2.5 mM (84% urease reduction); baicalin 8 mM (50% reduction); ebselen 0.03 mM (71% reduction); major viability reductions measured by flow cytometry. (shaalan2024theeffectof pages 3-5)
- **Rumen NH3 mitigation:** epiberberine associated with NH3 decreases of 13.1% and 15.6% in rumen fermentation experiments. (zhang2024epiberberineapotential pages 5-7)
- **Botanical MIC ranges:** Triphala MIC 80–320 μg/mL against standard and clinical *H. pylori* strains (in vitro). (zhu2024preliminaryinvestigationof pages 11-12)

## 8) Expert opinions / analysis (authoritative, source-linked)
- **Urease as a virulence/survival factor:** Shaalan et al. frame urease as central to *H. pylori* colonization in acid by generating a neutral microenvironment. (shaalan2024theeffectof pages 1-2)
- **Urease–CA coupling as “next-generation” CO2 trapping approach:** Saracho & Marek argue that understanding the role of CO2 hydration (CA) on ureolysis and CaCO3 precipitation is needed to develop “next-generation biocatalyzed CO2 trapping technologies,” implicitly positioning urease activity as part of an engineered biogeochemical module rather than a single-enzyme phenotype. (saracho2024uncoveringthedynamics pages 5-9)
- **Accessory-protein targeting as a modern inhibitor strategy:** Zhang et al. position UreG as “a new target for design of urease inhibitor” and emphasize maturation interference (Ni handling) as an alternative to active-site inhibitors. (zhang2024epiberberineapotential pages 1-2, zhang2024epiberberineapotential pages 5-7)

## 9) Curation warnings (claims that may be premature or should be marked uncertain)
1. **Do not overgeneralize *H. pylori* subunit naming (UreA/UreB) to all bacteria/archaea** without additional taxon-spanning evidence; retain gene/protein nodes as label-only or taxon-scoped. (shaalan2024theeffectof pages 1-2)
2. **Inhibitor→viability edges** should be curated with caution because inhibitors can have off-target effects; treat as “associated with” unless a mechanistic dependence on urease is demonstrated. (shaalan2024theeffectof pages 3-5)
3. **CA→urease gene regulation** in *S. pasteurii* is supported as a coincident/up-regulation relationship under specific CO2 regimes; it may be best curated as condition-dependent/uncertain causality rather than a universal regulatory edge. (saracho2024uncoveringthedynamics pages 5-9)
4. **UreI (urea channel) and other transporters** were mentioned in retrieved abstracts but were not supported by extracted evidence snippets here; avoid curating transporter edges until directly evidenced in full text. (chitas2024 abstract only; not cited)

## DOI-first bibliography (2023–2024; with publication month/year and URLs)
1. Shaalan H, Azrad M, Peretz A. *The effect of three urease inhibitors on H. pylori viability, urease activity and urease gene expression.* **Frontiers in Microbiology**. Nov 2024. DOI: **10.3389/fmicb.2024.1464484**. https://doi.org/10.3389/fmicb.2024.1464484 (shaalan2024theeffectof pages 1-2)
2. Saracho AC, Marek EJ. *Uncovering the dynamics of urease and carbonic anhydrase genes in ureolysis, carbon dioxide hydration, and calcium carbonate precipitation.* **Environmental Science & Technology**. Jan 2024. DOI: **10.1021/acs.est.3c06617**. https://doi.org/10.1021/acs.est.3c06617 (saracho2024uncoveringthedynamics pages 5-9)
3. Zhang X, Xiong Z, He Y, Zheng N, Zhao S, Wang J. *Epiberberine: a potential rumen microbial urease inhibitor to reduce ammonia release screened by targeting UreG.* **Applied Microbiology and Biotechnology**. Apr 2024. DOI: **10.1007/s00253-024-13131-4**. https://doi.org/10.1007/s00253-024-13131-4 (zhang2024epiberberineapotential pages 5-7)
4. Stabnikov V, Udymovych V, Kovshar I, Stabnikov D. *Microbial producer of acid urease for its application in biocementation.* **Ukrainian Food Journal**. Jun 2024. DOI: **10.24263/2304-974x-2024-13-2-10**. https://doi.org/10.24263/2304-974x-2024-13-2-10 (stabnikov2024microbialproducerof pages 1-3)
5. Zhu Z, Zou Y, Ou L, et al. *Preliminary investigation of the in vitro anti-Helicobacter pylori activity of Triphala.* **Frontiers in Pharmacology**. Nov 2024. DOI: **10.3389/fphar.2024.1438193**. https://doi.org/10.3389/fphar.2024.1438193 (zhu2024preliminaryinvestigationof pages 11-12)



References

1. (stabnikov2024microbialproducerof pages 1-3): Viktor Stabnikov, Viktor Udymovych, Iryna Kovshar, and Dmytro Stabnikov. Microbial producer of acid urease for its application in biocementation. Ukrainian Food Journal, 13:331-350, Jun 2024. URL: https://doi.org/10.24263/2304-974x-2024-13-2-10, doi:10.24263/2304-974x-2024-13-2-10. This article has 1 citations.

2. (saracho2024uncoveringthedynamics pages 9-13): Alexandra Clarà Saracho and Ewa J. Marek. Uncovering the dynamics of urease and carbonic anhydrase genes in ureolysis, carbon dioxide hydration, and calcium carbonate precipitation. Environmental science & technology, 58:1199-1210, Jan 2024. URL: https://doi.org/10.1021/acs.est.3c06617, doi:10.1021/acs.est.3c06617. This article has 48 citations and is from a domain leading peer-reviewed journal.

3. (shaalan2024theeffectof pages 1-2): Hanaa Shaalan, Maya Azrad, and Avi Peretz. The effect of three urease inhibitors on h. pylori viability, urease activity and urease gene expression. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1464484, doi:10.3389/fmicb.2024.1464484. This article has 26 citations and is from a peer-reviewed journal.

4. (zhang2024epiberberineapotential pages 1-2): Xiaoyin Zhang, Zhanbo Xiong, Yue He, Nan Zheng, Shengguo Zhao, and Jiaqi Wang. Epiberberine: a potential rumen microbial urease inhibitor to reduce ammonia release screened by targeting ureg. Applied Microbiology and Biotechnology, Apr 2024. URL: https://doi.org/10.1007/s00253-024-13131-4, doi:10.1007/s00253-024-13131-4. This article has 5 citations and is from a domain leading peer-reviewed journal.

5. (saracho2024uncoveringthedynamics pages 5-9): Alexandra Clarà Saracho and Ewa J. Marek. Uncovering the dynamics of urease and carbonic anhydrase genes in ureolysis, carbon dioxide hydration, and calcium carbonate precipitation. Environmental science & technology, 58:1199-1210, Jan 2024. URL: https://doi.org/10.1021/acs.est.3c06617, doi:10.1021/acs.est.3c06617. This article has 48 citations and is from a domain leading peer-reviewed journal.

6. (shaalan2024theeffectof pages 3-5): Hanaa Shaalan, Maya Azrad, and Avi Peretz. The effect of three urease inhibitors on h. pylori viability, urease activity and urease gene expression. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1464484, doi:10.3389/fmicb.2024.1464484. This article has 26 citations and is from a peer-reviewed journal.

7. (shaalan2024theeffectof pages 2-3): Hanaa Shaalan, Maya Azrad, and Avi Peretz. The effect of three urease inhibitors on h. pylori viability, urease activity and urease gene expression. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1464484, doi:10.3389/fmicb.2024.1464484. This article has 26 citations and is from a peer-reviewed journal.

8. (shaalan2024theeffectof media 1849fa05): Hanaa Shaalan, Maya Azrad, and Avi Peretz. The effect of three urease inhibitors on h. pylori viability, urease activity and urease gene expression. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1464484, doi:10.3389/fmicb.2024.1464484. This article has 26 citations and is from a peer-reviewed journal.

9. (shaalan2024theeffectof media 9e1ae2ae): Hanaa Shaalan, Maya Azrad, and Avi Peretz. The effect of three urease inhibitors on h. pylori viability, urease activity and urease gene expression. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1464484, doi:10.3389/fmicb.2024.1464484. This article has 26 citations and is from a peer-reviewed journal.

10. (shaalan2024theeffectof media 0d248d40): Hanaa Shaalan, Maya Azrad, and Avi Peretz. The effect of three urease inhibitors on h. pylori viability, urease activity and urease gene expression. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1464484, doi:10.3389/fmicb.2024.1464484. This article has 26 citations and is from a peer-reviewed journal.

11. (shaalan2024theeffectof media 66699e8f): Hanaa Shaalan, Maya Azrad, and Avi Peretz. The effect of three urease inhibitors on h. pylori viability, urease activity and urease gene expression. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1464484, doi:10.3389/fmicb.2024.1464484. This article has 26 citations and is from a peer-reviewed journal.

12. (shaalan2024theeffectof media bfb43865): Hanaa Shaalan, Maya Azrad, and Avi Peretz. The effect of three urease inhibitors on h. pylori viability, urease activity and urease gene expression. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1464484, doi:10.3389/fmicb.2024.1464484. This article has 26 citations and is from a peer-reviewed journal.

13. (shaalan2024theeffectof media d8c18288): Hanaa Shaalan, Maya Azrad, and Avi Peretz. The effect of three urease inhibitors on h. pylori viability, urease activity and urease gene expression. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1464484, doi:10.3389/fmicb.2024.1464484. This article has 26 citations and is from a peer-reviewed journal.

14. (zhang2024epiberberineapotential pages 5-7): Xiaoyin Zhang, Zhanbo Xiong, Yue He, Nan Zheng, Shengguo Zhao, and Jiaqi Wang. Epiberberine: a potential rumen microbial urease inhibitor to reduce ammonia release screened by targeting ureg. Applied Microbiology and Biotechnology, Apr 2024. URL: https://doi.org/10.1007/s00253-024-13131-4, doi:10.1007/s00253-024-13131-4. This article has 5 citations and is from a domain leading peer-reviewed journal.

15. (zhu2024preliminaryinvestigationof pages 11-12): Zhixiang Zhu, Yuanjing Zou, Ling Ou, Meiyun Chen, Yujiang Pang, Hui Li, Yajie Hao, Bingmei Su, Yuqian Lai, Liping Zhang, Junwei Jia, Ruixia Wei, Guimin Zhang, Meicun Yao, and Zhong Feng. Preliminary investigation of the in vitro anti-helicobacter pylori activity of triphala. Frontiers in Pharmacology, Nov 2024. URL: https://doi.org/10.3389/fphar.2024.1438193, doi:10.3389/fphar.2024.1438193. This article has 4 citations.

16. (zhang2024epiberberineapotential pages 9-10): Xiaoyin Zhang, Zhanbo Xiong, Yue He, Nan Zheng, Shengguo Zhao, and Jiaqi Wang. Epiberberine: a potential rumen microbial urease inhibitor to reduce ammonia release screened by targeting ureg. Applied Microbiology and Biotechnology, Apr 2024. URL: https://doi.org/10.1007/s00253-024-13131-4, doi:10.1007/s00253-024-13131-4. This article has 5 citations and is from a domain leading peer-reviewed journal.