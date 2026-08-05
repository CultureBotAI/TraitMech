---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:49:02.801397'
end_time: '2026-08-04T02:59:01.204230'
duration_seconds: 598.4
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range high
  trait_identifier: METPO:1000464
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH range phenotype in which the growth-supporting external pH range\
    \ spans approximately 10\u201314, characteristic of extreme-alkaliphile physiology."
  parent_traits: METPO:1000332
  synonyms: Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, 10_to_14
  evidence_summary: 'DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review
    supports extreme-alkaliphile physiology growing at external pH above 10.) | DOI:10.1016/j.tim.2007.02.005:
    proton motive force (pH-homeostasis review supports robust Na+/H+ antiporter activity
    as the extreme-alkaliphile mechanism sustaining the proton motive force above
    pH 10.)'
  causal_graph_summary: 'ph_range_high_extreme_alkaliphile: 12 nodes, 10 edges'
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
- **Trait label:** pH range high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000464
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 10–14, characteristic of extreme-alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, 10_to_14
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports extreme-alkaliphile physiology growing at external pH above 10.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports robust Na+/H+ antiporter activity as the extreme-alkaliphile mechanism sustaining the proton motive force above pH 10.)
- **Existing causal graph summary:** ph_range_high_extreme_alkaliphile: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **pH range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_high.yaml`.

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
- **Trait label:** pH range high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000464
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 10–14, characteristic of extreme-alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, 10_to_14
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports extreme-alkaliphile physiology growing at external pH above 10.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports robust Na+/H+ antiporter activity as the extreme-alkaliphile mechanism sustaining the proton motive force above pH 10.)
- **Existing causal graph summary:** ph_range_high_extreme_alkaliphile: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **pH range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_high.yaml`.

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


# Curation report: microbial trait **pH range high**

## Executive assessment

**Trait label:** pH range high  
**Trait identifier:** **METPO:1000464**  
**Category:** ENVIRONMENT  
**Parent:** METPO:1000332  
**Recommended interpretation:** a demonstrated growth phenotype whose external growth-supporting pH range extends into approximately pH 10–14. The best-supported mechanistic graph is not “alkaline resistance” in general, but a coupled system of respiratory proton translocation, unusually negative membrane potential, Na+/H+ cycling, cytoplasmic pH homeostasis, proton-coupled ATP synthesis, and cell-surface adaptations.

The strongest model is *Bacillus pseudofirmus* OF4: at external pH 10.5 it maintains cytoplasmic pH near 8.3; near the upper growth boundary, ≥pH 11.2, cytoplasmic pH rises to about 9.5. Thus, extreme alkaliphily does not imply a neutral cytoplasm under every condition; it includes the capacity to remain metabolically functional at unusually alkaline intracellular pH when homeostasis becomes incomplete. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 1-3, preiss2015alkaliphilicbacteriawith pages 5-7)

## 1. Trait scope and boundaries

### 1.1 What the trait represents

For TraitMech, **METPO:1000464** should denote an **assay-observed growth range**, not merely:

- survival after brief alkaline exposure;
- an alkaline optimum without evidence that growth spans the specified interval;
- enzyme activity at alkaline pH;
- environmental recovery from a soda lake;
- transcriptomic induction after alkaline shock; or
- alkali tolerance in a neutralophile.

Recent terminology remains inconsistent. A 2024 study describes alkali-tolerant organisms as having optima around pH 7–9 and generally not growing above 9.5; alkaliphiles have optima around pH 10–12. It further distinguishes facultative alkaliphiles, which also grow near neutrality, from obligate alkaliphiles that grow optimally above pH 10 and fail below approximately pH 9. These are useful operational distinctions, but they should not replace a recorded strain-specific growth curve. (maksimova2024metabolicandmorphological pages 1-2)

### 1.2 Boundary cases

1. **Alkali tolerance versus alkaliphily.** *Bacillus subtilis* ordinarily replicates around pH 6–9 and may withstand or grow near pH 10, but alkaline-shock responses in this species do not establish a pH 10–14 growth range. (mitchell2024penicillinbindingproteinredundancy pages 1-2)
2. **Optimal pH versus range.** An optimum at pH 10 does not prove growth to pH 12–14.
3. **Shock versus sustained growth.** A 30-minute NaOH exposure followed by an enzyme-activity assay is mechanistically informative but is not evidence for sustained extreme-alkaliphile growth. (mitchell2024penicillinbindingproteinredundancy pages 10-12)
4. **Haloalkaliphily.** High pH and high sodium/salinity frequently co-occur in soda lakes, but salinity tolerance is a separate trait. Sodium can nevertheless be mechanistically required for Na+/H+ cycling.
5. **The upper value 14.** The literature retrieved here strongly supports growth above pH 10 and in model strains to approximately 11–13, but not a general ability to grow at pH 14. The ontology definition should therefore be interpreted as an approximate bin, not evidence that every positive organism grows throughout all values from 10 to 14.
6. **Activity without growth.** In the 2024 *B. aequororis* study, metabolic activity was measured after exposure as high as pH 13, whereas prior growth evidence was at pH 11. Exposure activity should not be converted automatically into a pH-13 growth edge. (maksimova2024metabolicandmorphological pages 1-2, maksimova2024metabolicandmorphological pages 5-6)

### 1.3 Recommended phenotype assay model

A defensible annotation should record: strain, medium composition and buffering, initial and terminal pH, Na+ concentration, temperature, oxygen regime, inoculum history, incubation time, and evidence of replication (growth rate, viable counts, or serial propagation). Cytoplasmic pH, ATP, membrane potential, antiporter activity, or proteomics are mechanistic assays, not substitutes for replication.

## 2. Current mechanistic understanding

At high external pH, the bulk proton concentration is low and the transmembrane ΔpH is reversed: the cytoplasm is more acidic than the exterior. This chemical gradient opposes inward proton-driven work. Extreme alkaliphiles compensate partly through a large inside-negative electrical potential and use electrogenic Na+/H+ antiporters to import H+ while exporting Na+. Na+ then re-enters through solute symporters, sodium channels, and—in motile taxa—Na+-coupled flagellar systems, completing a sodium cycle. Respiratory complexes expel protons and generate the electrochemical driving force, while adapted F1Fo ATP synthase captures inward-moving H+ for ATP synthesis. Acidic cell-wall polymers and S-layers may retard loss of surface-associated protons into the alkaline bulk phase. (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6)

This is a distributed physiological system rather than a single “alkaliphile gene.” The most curatable causal backbone is:

**respiratory electron transport → proton extrusion/ΔΨ → Mrp Na+/H+ antiport → lower pH_in → macromolecular function and high-pH growth**, with a parallel energy branch **respiratory proton translocation → adapted F1Fo ATP synthase → ATP → growth**.

## 3. Candidate nodes grouped by type

### 3.1 Trait and environmental nodes

- **pH range high** — **METPO:1000464**
- external pH approximately 10–14 — label-only range node unless the project has a standard pH-bin ontology pattern
- alkaline environment — label-only pending selection of an appropriate ENVO class
- extracellular Na+ concentration
- oxygen availability / aeration
- low-proton-availability external milieu
- high salinity — separate environmental covariate, not part of the trait itself

### 3.2 Chemicals and energetic quantities

- hydron/proton — **CHEBI:15378**
- sodium cation — **CHEBI:29101**
- ATP — **CHEBI:15422**
- ADP — **CHEBI:16761**
- phosphate — **CHEBI:43474**
- oxygen — use a verified ChEBI identifier during implementation
- membrane potential, ΔΨ — label-only physical quantity
- proton motive force — label-only unless the curation framework has a verified identifier
- sodium motive force — label-only
- acetate — candidate only for the recent low-O2 hypothesis

### 3.3 Complexes, proteins, and genes

**Core candidates**

- Mrp/Sha multisubunit Na+/H+ antiporter, **mrpABCDEFG** — label-only complex unless mapped to strain-specific protein records
- MrpA, MrpB, MrpD and other Mrp subunits
- proton-pumping respiratory-chain complexes
- F1Fo ATP synthase
- ATP synthase subunit a and c-ring subunits; alkaliphile-specific c-subunit motifs **AxAxAVA** and **PxxExxP**
- Na+/solute symporters
- NavBP voltage-gated sodium channel
- MotPS sodium-coupled flagellar stator
- acidic secondary cell-wall polymers: teichuronic acid and teichuronopeptide
- S-layer proteins such as SlpA/SlaA

**Recent or conditional candidates**

- cytochrome aa3 oxidase
- cytochrome ba3 oxidase
- cytochrome bb3 oxidase and cytochrome bd oxidase—predicted under very low O2 but not detected in the 2024 proteomics study
- sodium:acetate exporter—hypothetical functional substitute for Mrp under oxygen limitation
- PBPH, PBP4/PbpD, PBP1a/PBP1b/PonA, PBP2a/PbpA, PBP2b, PBP3, and PBP5—alkaline-shock envelope-maintenance candidates, not yet core extreme-alkaliphile determinants
- BpOF4_01690—promising strain-specific candidate from prior deletion work, but insufficient full-text evidence was recovered here for an edge-level quotation

### 3.4 Processes and locations

- sodium ion transport — **GO:0006814**
- proton transmembrane transporter activity — **GO:0015078**
- proton-transporting ATP synthase activity, rotational mechanism — **GO:0046933**
- plasma membrane — **GO:0005886**
- cytoplasmic pH homeostasis — retain label-only unless verified against the current GO release
- oxidative phosphorylation
- respiratory electron transport
- peptidoglycan biosynthesis
- flagellum-dependent motility
- proton retention near the cell surface

### 3.5 Taxa

- *Bacillus subtilis* — **NCBITaxon:1423**, boundary/alkaline-shock model
- *Escherichia coli* — **NCBITaxon:562**, electrophysiology comparison rather than extreme alkaliphile
- *B. pseudofirmus* OF4, *B. halodurans* C-125, *Caldalkalibacillus thermarum* TA2.A1, *Evansella clarkii*, and *B. aequororis* 5-DB — retain taxon labels until their current accepted NCBITaxon identifiers and strain mappings are verified

## 4. Candidate causal edges

The following table is the compact curation set. “Direct” means a perturbation or functional assay supports causality; “association” means abundance or physiology covaries with the condition; “review-supported” means the cited review synthesizes earlier primary experiments.

| candidate subject | predicate | object | evidence tier | taxon/context | DOI |
|---|---|---|---|---|---|
| external pH ~10–14 | challenges | cytoplasmic pH homeostasis | review-supported physiology (growth at external pH above 10–11 requires maintained lower pH\_in) (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 1-3) | extreme alkaliphilic Bacillus spp.; e.g., *Bacillus pseudofirmus* OF4 at pH 10.5 with pH\_in ~8.3, and upward creep to ~9.5 near upper growth limit (krulwich2011molecularaspectsof pages 12-14, preiss2015alkaliphilicbacteriawith pages 5-7) | [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549); [10.3389/fbioe.2015.00075](https://doi.org/10.3389/fbioe.2015.00075) |
| respiratory proton-pumping chain | generates | membrane potential / proton motive force | review-supported bioenergetics (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 1-3) | alkaliphilic Bacillus bioenergetics; proton-pumping respiratory complexes support active proton uptake by antiport and ATP synthesis (krulwich2011molecularaspectsof pages 27-28) | [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549) |
| high membrane potential (ΔΨ) | drives | Na+/H+ antiport by Mrp | review-supported + physiological synthesis (krulwich2011molecularaspectsof pages 27-28, goto2022differencesinbioenergetic pages 1-2, krulwich2011molecularaspectsof pages 5-6) | obligate alkaliphilic Bacillaceae; ΔΨ about -170 mV at high aeration and ~-140 mV at low aeration in *Evansella clarkii* synthesis/review (goto2022differencesinbioenergetic pages 1-2) | [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549); [10.3389/fmicb.2022.842785](https://doi.org/10.3389/fmicb.2022.842785) |
| Mrp Na+/H+ antiporter complex | imports H+ in exchange for exporting Na+ | lower cytoplasmic pH / pH homeostasis | direct loss-of-function + review-supported mechanism (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 22-23, krulwich2011molecularaspectsof pages 20-22) | alkaliphilic *Bacillus* spp.; mrpA mutation abolishes alkaliphilic phenotype and Na+/H+ antiport per cited primary studies summarized in review (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 20-22) | [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549) |
| Mrp Na+/H+ antiporter complex | enables | growth at high external pH | direct loss-of-function (review-summarized) (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 20-22) | *B. pseudofirmus* OF4 / *B. halodurans* C-125 genetic evidence summarized in review | [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549) |
| Na+-coupled solute uptake / Na+ re-entry pathways | sustain | Mrp-dependent Na+/H+ cycling | review-supported, partially taxon-specific (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 22-23) | alkaliphilic Bacillus; Na+ re-entry via Na+/solute symporters, NavBP, and MotPS supports antiport cycle | [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549) |
| NavBP sodium channel | contributes to | cytoplasmic pH homeostasis / Na+ re-entry | review-supported, taxon-specific (krulwich2011molecularaspectsof pages 22-23, preiss2015alkaliphilicbacteriawith pages 5-7) | *B. pseudofirmus* OF4; high-pH-potentiated sodium channel with roles in chemotaxis and pH homeostasis | [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549); [10.3389/fbioe.2015.00075](https://doi.org/10.3389/fbioe.2015.00075) |
| MotPS Na+-driven flagellar stator / motility-associated Na+ entry | contributes to | Na+ re-entry supporting pH homeostasis cycle | review-supported, taxon-specific (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 22-23) | alkaliphilic Bacillus; role linked to sodium cycling as summarized in review | [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549) |
| F1Fo ATP synthase | uses inward H+ flow to synthesize | ATP | review-supported + classic biochemical evidence summarized in review (krulwich2011molecularaspectsof pages 27-28, preiss2015alkaliphilicbacteriawith pages 5-7) | non-fermentative alkaliphilic Bacillus spp. and *Caldalkalibacillus thermarum* | [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549); [10.3389/fbioe.2015.00075](https://doi.org/10.3389/fbioe.2015.00075) |
| alkaliphile-specific ATP synthase a/c-subunit motifs | enable | oxidative phosphorylation / ATP synthase function at pH 10.5 | direct sequence-function substitution evidence summarized in review (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 22-23) | extreme alkaliphilic Bacillus ATP synthase; replacing motifs with consensus Bacillus sequences impairs growth and oxidative phosphorylation at pH 10.5 | [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549) |
| acidic secondary cell-wall polymers / teichuronopeptide / teichuronic-acid-rich wall | promotes | alkaliphily / proton retention near cell surface | review-supported with mutation-backed literature synthesis (krulwich2011molecularaspectsof pages 5-6, preiss2015alkaliphilicbacteriawith pages 12-13) | *B. halodurans* C-125 and related alkaliphiles; loss of negatively charged SCWPs reduces alkaliphilic capacity | [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549); [10.3389/fbioe.2015.00075](https://doi.org/10.3389/fbioe.2015.00075) |
| S-layer protein (e.g., SlpA/SlaA) | promotes | alkaliphily | review-supported with prior mutational literature synthesis (krulwich2011molecularaspectsof pages 5-6, preiss2015alkaliphilicbacteriawith pages 12-13) | *B. pseudofirmus* OF4 and other alkaliphiles; surface acidic proteins proposed to retain protons and support high-pH growth | [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549); [10.3389/fbioe.2015.00075](https://doi.org/10.3389/fbioe.2015.00075) |
| oxygen availability | regulates abundance of | cytochrome aa3 and ba3 oxidases | proteomic association (2024) (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals pages 6-8) | *Caldalkalibacillus thermarum* TA2.A1 chemostats, 0.25–4.2% O2; aa3 highest at 4.2% O2, ba3 enriched at lower O2 until decline below 0.42% O2 | [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929) |
| low oxygen availability | downregulates | Mrp Na+/H+ antiporter abundance | proteomic association (2024) (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals pages 6-8) | *C. thermarum* TA2.A1 chemostats; authors note Mrp is significantly downregulated at lower O2 | [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929) |
| sodium:acetate exporter | may partially replace | Mrp requirement under low O2 | hypothetical / author inference (2024) (jong2024quantitativeproteomicsreveals pages 6-8) | *C. thermarum* TA2.A1 low-O2 chemostats; proposed explanation for reduced Mrp abundance | [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929) |
| alkaline shock (~pH 10–10.5 exposure) | inactivates or shifts activity of | specific PBPs (PBPH, PBP4, PBP1a→PBP1b) | direct assay-specific in vivo enzyme-activity evidence (2024) (mitchell2024penicillinbindingproteinredundancy pages 4-6, mitchell2024penicillinbindingproteinredundancy pages 1-2) | *Bacillus subtilis* whole-cell Bocillin-FL assay after NaOH treatment; not an extreme alkaliphile trait-defining experiment | [10.1128/aem.00548-23](https://doi.org/10.1128/aem.00548-23) |
| alkaline-active PBPs (PBP2a, PBP2b, PBP3, PBP5) | support | replication/growth during alkaline shock | direct assay-specific mutant inference (2024) (mitchell2024penicillinbindingproteinredundancy pages 1-2, mitchell2024penicillinbindingproteinredundancy pages 10-12) | *B. subtilis*; relevant as boundary/nearby mechanism, not yet core extreme-alkaliphile edge | [10.1128/aem.00548-23](https://doi.org/10.1128/aem.00548-23) |
| external pH and Na+ concentration | increase | ΔpH across the membrane via Na+/H+ antiport activity | direct physiological association, non-model facultative alkaliphile (2024) (maksimova2024metabolicandmorphological pages 5-6, maksimova2024metabolicandmorphological pages 9-10) | *Bacillus aequororis* 5-DB; maximum ΔpH observed at pH 11 and 50 g/L NaCl | [10.1155/2024/3087296](https://doi.org/10.1155/2024/3087296) |
| high aeration / high ΔΨ or low aeration / cytochrome-c-enriched surface | supports | ATP production under alkaline conditions | review-supported / partially hypothetical model (goto2022differencesinbioenergetic pages 1-2) | obligate alkaliphilic Bacillaceae; high ΔΨ under high aeration, H+-capacitor model under low aeration | [10.3389/fmicb.2022.842785](https://doi.org/10.3389/fmicb.2022.842785) |


*Table: This table compiles compact candidate causal edges for extreme alkaliphile high-pH growth, marking which claims are direct, review-supported, proteomic, assay-specific, or hypothetical. It is designed to help prioritize what is safe to curate into a TraitMech graph and what should remain provisional.*

### 4.1 Highest-priority YAML backbone

The following edges are the safest additions or refinements:

1. **external high pH — negatively regulates → cytoplasmic pH homeostasis**. High external pH creates an inwardly unfavorable proton gradient; at pH 10.5, *B. pseudofirmus* OF4 nevertheless holds pH_in near 8.3. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 1-3)
2. **respiratory proton-pumping complexes — generate → membrane potential/proton electrochemical potential**. This supplies energy for antiport and proton-coupled ATP synthesis. (krulwich2011molecularaspectsof pages 27-28)
3. **membrane potential — drives → Mrp Na+/H+ antiporter**. The large inside-negative ΔΨ is especially important because reversed ΔpH lowers bulk PMF. (goto2022differencesinbioenergetic pages 1-2, krulwich2011molecularaspectsof pages 5-6)
4. **Mrp Na+/H+ antiporter — imports → H+** and **exports → Na+**. Mrp is the dominant alkaliphile pH-homeostasis system; mutation or loss of function impairs antiport and alkaliphilic growth. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 22-23)
5. **Mrp-mediated H+ uptake — promotes → cytoplasmic pH homeostasis**, which in turn **enables → METPO:1000464**. This is the central trait edge. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 20-22)
6. **Na+/solute symporters/NavBP/MotPS — import → Na+**, sustaining the Na+ cycle that powers repeated Mrp exchange. This should be taxon-qualified. (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 22-23)
7. **F1Fo ATP synthase — catalyzes → ATP synthesis**, using inward H+ despite low bulk PMF. Alkaliphile-specific a/c-subunit features support function at pH 10.5. (krulwich2011molecularaspectsof pages 22-23, preiss2015alkaliphilicbacteriawith pages 5-7)
8. **ATP production — promotes → growth at high pH**. This edge is generic but mechanistically necessary.
9. **acidic secondary cell-wall polymers/S-layer — promotes → alkaliphily**, probably by increasing negatively charged surface character and retarding proton equilibration. Keep the proton-trapping subedge qualified because the physical mechanism remains partly modeled. (krulwich2011molecularaspectsof pages 5-6, preiss2015alkaliphilicbacteriawith pages 12-13)

### 4.2 Recent 2023–2024 developments

**Oxygen-dependent respiratory remodeling.** In October 2024, *C. thermarum* TA2.A1 was grown in chemostats from 0.25% to 4.2% inlet O2. Type I and II NADH dehydrogenases were constitutively detected. Cytochrome aa3 was most abundant at 4.2% O2, while ba3 predominated at most lower levels and declined below 0.42% O2. Mrp abundance also decreased under lower O2. These findings establish regulatory associations, not that any oxidase or Mrp change caused high-pH growth. The proposed replacement of part of Mrp’s role by sodium-coupled acetate export lacks direct transport measurements. (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals pages 6-8)

**Quantitative bioenergetic context.** In obligately alkaliphilic Bacillaceae, reported ΔΨ values are approximately −170 mV under high aeration and −140 mV under low aeration. Low aeration was associated with a 2.5–6.3-fold increase in membrane-bound cytochrome c in *E. clarkii*, supporting an aeration-dependent bioenergetic model. The proposed Asn-rich cytochrome-c “H+ capacitor” is plausible but remains less secure than Mrp-mediated homeostasis. (goto2022differencesinbioenergetic pages 1-2)

**Physiology across pH and salinity.** A July 2024 study found that *B. aequororis* 5-DB grows at pH 11 and 50 g/L NaCl and retained broader metabolic activity than *B. subtilis* ATCC 6633. The greatest measured ΔpH occurred at external pH 11 with 50 g/L NaCl. However, the authors’ statement that this condition “activates” Na+/H+ antiport is an interpretation; antiporter flux or genetics were not directly assayed. (maksimova2024metabolicandmorphological pages 1-2, maksimova2024metabolicandmorphological pages 9-10)

**Cell-wall enzyme specialization during alkaline shock.** Published online 21 December 2023 and appearing in the January 2024 issue, whole-cell activity-based profiling showed that *B. subtilis* PBP4 becomes inactive near pH 10, while PBP1 activity shifts from PBP1a to PBP1b near pH 10.5. PBP4 and PBPH inactivation occurred within about 5 minutes; the PBP1a→PBP1b transition took about 10 minutes. These observations support environment-specific redundancy among envelope enzymes, but the 30-minute shock assay in a neutralophile does not establish extreme-alkaliphile growth. (mitchell2024penicillinbindingproteinredundancy pages 4-6, mitchell2024penicillinbindingproteinredundancy pages 1-2)

**Broader electrophysiology.** A November 2024 single-cell/modeling study in *E. coli* found that reducing PMF impairs pH maintenance and that collapsing PMF depolarizes cells. Its model predicts NhaA-like antiport is the least costly strategy around external pH 9–12. This strengthens the general connection among PMF, antiport, and pH homeostasis, but it should not be used as direct evidence for an extreme-alkaliphile-specific edge. (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9)

## 5. Applications and real-world implementations

Alkaliphile-derived enzymes are used or investigated where alkaline processing would denature ordinary enzymes: alkaline proteases in detergents and hide dehairing; amylases and debranching enzymes in laundry; keratinases for feather waste; and cyclomaltodextrin glucanotransferases for cyclodextrin production in food, pharmaceutical, and chemical applications. Whole-cell implementations include traditional indigo fermentation, sulfide oxidation in haloalkaline gas-desulfurization systems, alkaline wastewater treatment, dye degradation, and microbial fuel cells. (preiss2015alkaliphilicbacteriawith pages 2-3)

Soda lakes provide naturally buffered, sodium-carbonate-rich high-pH systems and contain organisms mediating carbon, nitrogen, and sulfur cycles. South Siberian soda lakes described in the literature span approximately 50–400 g/L salinity, illustrating why alkaliphily and osmoadaptation often need to be modeled as interacting but separate traits. (sorokin2014microbialdiversityand pages 3-5)

For TraitMech, application evidence should be kept outside the core causal graph unless the graph explicitly models consequences of the trait. A suitable downstream relation is **METPO:1000464 — enables organismal activity in → alkaline industrial process**, not **industrial use — causes → high-pH growth**.

## 6. Expert analysis and curation recommendations

Authoritative reviews converge on Mrp-dependent pH homeostasis as the most secure central mechanism. They also emphasize that high-pH ATP synthesis remains a bioenergetic challenge: the larger ΔΨ does not fully compensate for reversed ΔpH in bulk-PMF calculations. Local proton retention, membrane organization, acidic surface layers, and proximity of respiratory complexes to ATP synthase are therefore credible contributors, but they do not all have equally strong causal evidence. (krulwich2011molecularaspectsof pages 5-6, preiss2015alkaliphilicbacteriawith pages 12-13, preiss2015alkaliphilicbacteriawith pages 5-7)

**Recommended graph architecture:**

- Keep **pH homeostasis** and **energy conservation** as two interacting branches.
- Use **Mrp complex**, rather than a single generic antiporter, for the principal model-Bacillus edge.
- Represent Na+ as both the exported Mrp substrate and a re-entering coupling ion.
- Keep respiratory-chain oxidase choice conditional on oxygen and taxon.
- Put S-layer/SCWP upstream of a provisional “surface proton retention” process, then connect that process to PMF/ATP synthesis with uncertainty.
- Do not generalize PBP alkaline-shock edges from *B. subtilis* to all extreme alkaliphiles.

## 7. Warnings: claims not yet ready for TraitMech

1. **Do not curate “growth at pH 14” as a universal consequence.** The retrieved evidence does not establish that endpoint broadly.
2. **Do not equate pH-13 metabolic signal with growth.** The 2024 *B. aequororis* experiment measured post-exposure metabolism, not necessarily replication at pH 13. (maksimova2024metabolicandmorphological pages 5-6)
3. **Do not curate low O2 → sodium:acetate export → replacement of Mrp as established.** It is explicitly a hypothesis without in vivo or in vitro acetate-transport data. (jong2024quantitativeproteomicsreveals pages 6-8)
4. **Do not curate cytochrome bb3 or bd induction below 0.25% O2 from the 2024 study.** Neither complex was detected. (jong2024quantitativeproteomicsreveals pages 6-8)
5. **Do not make the H+-capacitor model a high-confidence core edge.** Cytochrome-c enrichment is measured, but directed proton transfer to ATP synthase remains hypothetical. (goto2022differencesinbioenergetic pages 1-2)
6. **Do not generalize PBP1b, PBP2a, or PBP4 as extreme-alkaliphile determinants.** Evidence is from alkaline shock in *B. subtilis*. (mitchell2024penicillinbindingproteinredundancy pages 4-6, mitchell2024penicillinbindingproteinredundancy pages 10-12)
7. **Do not merge halotolerance with METPO:1000464.** Na+ is mechanistically important, but resistance to high osmolarity requires separate compatible-solute, K+, and envelope pathways.
8. **Do not assign strain-specific UniProt, KEGG, Rhea, or EC identifiers without checking the exact organism and reaction.** Label-only nodes are preferable to incorrect cross-strain grounding.

## 8. DOI-first bibliography

1. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology*. Published May 2011. https://doi.org/10.1038/nrmicro2549. (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 12-14)
2. Preiss L, Hicks DB, Suzuki S, Meier T, Krulwich TA. **Alkaliphilic Bacteria with Impact on Industrial Applications, Concepts of Early Life Forms, and Bioenergetics of ATP Synthesis.** *Frontiers in Bioengineering and Biotechnology*. Published June 2015. https://doi.org/10.3389/fbioe.2015.00075. (preiss2015alkaliphilicbacteriawith pages 12-13, preiss2015alkaliphilicbacteriawith pages 5-7, preiss2015alkaliphilicbacteriawith pages 2-3)
3. Goto T, Ogami S, Yoshimune K, Yumoto I. **Differences in Bioenergetic Metabolism of Obligately Alkaliphilic Bacillaceae Under High pH Depend on the Aeration Conditions.** *Frontiers in Microbiology*. Published March 2022. https://doi.org/10.3389/fmicb.2022.842785. (goto2022differencesinbioenergetic pages 1-2)
4. Mitchell SL, Kearns DB, Carlson EE. **Penicillin-binding protein redundancy in Bacillus subtilis enables growth during alkaline shock.** *Applied and Environmental Microbiology*. Published online 21 December 2023; January 2024 issue. https://doi.org/10.1128/aem.00548-23. (mitchell2024penicillinbindingproteinredundancy pages 4-6, mitchell2024penicillinbindingproteinredundancy pages 1-2)
5. Maksimova YG, Eliseeva A, Maksimov A. **Metabolic and Morphological Aspects of Adaptation of Alkaliphilic Bacillus aequororis 5-DB and Alkali-Tolerant Bacillus subtilis ATCC 6633 to Changes in pH and Mineralization.** *International Journal of Microbiology*. Accepted 10 July 2024. https://doi.org/10.1155/2024/3087296. (maksimova2024metabolicandmorphological pages 1-2, maksimova2024metabolicandmorphological pages 9-10)
6. de Jong SI et al. **Quantitative proteomics reveals oxygen-induced adaptations in Caldalkalibacillus thermarum TA2.A1 microaerobic chemostat cultures.** *Frontiers in Microbiology*. Published 28 October 2024. https://doi.org/10.3389/fmicb.2024.1468929. (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals pages 6-8)
7. Terradot G, Krasnopeeva E, Swain PS, Pilizota T. **Escherichia coli Maintains pH via the Membrane Potential.** *PRX Life*. Published 27 November 2024. https://doi.org/10.1103/PRXLife.2.043015. (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9)
8. Xu N et al. **The Lysine 299 Residue Endows the Multisubunit Mrp1 Antiporter with Dominant Roles in Na+ Resistance and pH Homeostasis in Corynebacterium glutamicum.** *Applied and Environmental Microbiology*. Published May 2018. https://doi.org/10.1128/aem.00110-18. This is strong antiporter structure–function evidence but only at pH 8–9 and is therefore supporting, not trait-defining, evidence. (xu2018thelysine299 pages 13-15, xu2018thelysine299 pages 20-22)
9. Sorokin DY et al. **Microbial diversity and biogeochemical cycling in soda lakes.** *Extremophiles*. Published August 2014. https://doi.org/10.1007/s00792-014-0670-9. (sorokin2014microbialdiversityand pages 3-5)

**Bottom line:** the existing 12-node/10-edge graph should be expanded conservatively around the Mrp–ΔΨ–Na+ cycle, adapted F1Fo ATP synthase, and acidic surface structures. The 2024 studies add valuable conditional regulation and envelope physiology, but most of those newer edges require taxon, oxygen, salinity, or assay qualifiers and should not displace the foundational direct evidence for extreme-alkaliphile pH homeostasis.

References

1. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

3. (preiss2015alkaliphilicbacteriawith pages 5-7): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 194 citations.

4. (maksimova2024metabolicandmorphological pages 1-2): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

5. (mitchell2024penicillinbindingproteinredundancy pages 1-2): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

6. (mitchell2024penicillinbindingproteinredundancy pages 10-12): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

7. (maksimova2024metabolicandmorphological pages 5-6): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

8. (krulwich2011molecularaspectsof pages 27-28): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

9. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

10. (goto2022differencesinbioenergetic pages 1-2): Toshitaka Goto, Shinichi Ogami, Kazuaki Yoshimume, and Isao Yumoto. Differences in bioenergetic metabolism of obligately alkaliphilic bacillaceae under high ph depend on the aeration conditions. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.842785, doi:10.3389/fmicb.2022.842785. This article has 6 citations and is from a peer-reviewed journal.

11. (krulwich2011molecularaspectsof pages 22-23): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

12. (krulwich2011molecularaspectsof pages 20-22): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

13. (preiss2015alkaliphilicbacteriawith pages 12-13): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 194 citations.

14. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

15. (jong2024quantitativeproteomicsreveals pages 6-8): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

16. (mitchell2024penicillinbindingproteinredundancy pages 4-6): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

17. (maksimova2024metabolicandmorphological pages 9-10): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

18. (terradot2024escherichiacolimaintains pages 1-2): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.

19. (terradot2024escherichiacolimaintains pages 8-9): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.

20. (preiss2015alkaliphilicbacteriawith pages 2-3): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 194 citations.

21. (sorokin2014microbialdiversityand pages 3-5): Dimitry Y. Sorokin, Tom Berben, Emily Denise Melton, Lex Overmars, Charlotte D. Vavourakis, and Gerard Muyzer. Microbial diversity and biogeochemical cycling in soda lakes. Extremophiles, 18:791-809, Aug 2014. URL: https://doi.org/10.1007/s00792-014-0670-9, doi:10.1007/s00792-014-0670-9. This article has 438 citations and is from a peer-reviewed journal.

22. (xu2018thelysine299 pages 13-15): Ning Xu, Yingying Zheng, Xiaochen Wang, Terry A. Krulwich, Yanhe Ma, and Jun Liu. The lysine 299 residue endows the multisubunit mrp1 antiporter with dominant roles in na <sup>+</sup> resistance and ph homeostasis in corynebacterium glutamicum. Applied and Environmental Microbiology, May 2018. URL: https://doi.org/10.1128/aem.00110-18, doi:10.1128/aem.00110-18. This article has 24 citations and is from a peer-reviewed journal.

23. (xu2018thelysine299 pages 20-22): Ning Xu, Yingying Zheng, Xiaochen Wang, Terry A. Krulwich, Yanhe Ma, and Jun Liu. The lysine 299 residue endows the multisubunit mrp1 antiporter with dominant roles in na <sup>+</sup> resistance and ph homeostasis in corynebacterium glutamicum. Applied and Environmental Microbiology, May 2018. URL: https://doi.org/10.1128/aem.00110-18, doi:10.1128/aem.00110-18. This article has 24 citations and is from a peer-reviewed journal.