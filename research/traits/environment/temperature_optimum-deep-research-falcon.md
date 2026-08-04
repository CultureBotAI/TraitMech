---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:41:15.498613'
end_time: '2026-08-04T04:06:55.681460'
duration_seconds: 1540.18
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum
  trait_identifier: METPO:1000304
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A temperature phenotype with numerical limits that represents the ambient-temperature
    conditions at which an organism exhibits the most efficient growth and reproduction.
  parent_traits: METPO:1000533, METPO:1000536
  synonyms: ''
  evidence_summary: 'DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of
    high temperature (Thermophile-adaptation review supports the ambient temperature
    at which membrane and enzyme function are best maintained as the operational definition
    of temperature optimum.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated
    fatty acids (Membrane-adaptation review supports homoviscous membrane composition
    as a key mechanism setting the temperature optimum.)'
  causal_graph_summary: 'temperature_optimum_balanced_adaptation: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000304
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits that represents the ambient-temperature conditions at which an organism exhibits the most efficient growth and reproduction.
- **Parent traits:** METPO:1000533, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the ambient temperature at which membrane and enzyme function are best maintained as the operational definition of temperature optimum.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous membrane composition as a key mechanism setting the temperature optimum.)
- **Existing causal graph summary:** temperature_optimum_balanced_adaptation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum.yaml`.

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
- **Trait label:** temperature optimum
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000304
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits that represents the ambient-temperature conditions at which an organism exhibits the most efficient growth and reproduction.
- **Parent traits:** METPO:1000533, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the ambient temperature at which membrane and enzyme function are best maintained as the operational definition of temperature optimum.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous membrane composition as a key mechanism setting the temperature optimum.)
- **Existing causal graph summary:** temperature_optimum_balanced_adaptation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum.yaml`.

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


# Curation report: microbial temperature optimum

## Trait record and scope

- **Trait:** temperature optimum
- **Trait identifier:** **`METPO:1000304`**
- **Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED
- **Provided definition:** “A temperature phenotype with numerical limits that represents the ambient-temperature conditions at which an organism exhibits the most efficient growth and reproduction.”
- **Parents:** `METPO:1000533`, `METPO:1000536`

### Operational interpretation

For microbial curation, temperature optimum—often **optimal growth temperature (OGT or Topt)**—should mean the incubation temperature at which a defined organism, strain, and culture system exhibits its **maximum measured growth rate**. It is therefore a property of an organism–assay combination, not simply the temperature from which an isolate was recovered. Recent OGT datasets explicitly distinguish optimum temperature from any permissive cultivation temperature and from minimum or maximum growth temperatures. Reported optima are sensitive to the temperatures sampled and their spacing, so medium, pH, salinity, atmosphere, pressure, growth-rate endpoint, and temperature grid should be retained as evidence metadata. Available prokaryotic records span approximately 2–114°C, illustrating the breadth of the trait but not a universal physiological scale. (colette2025machinelearningfor pages 1-4, colette2025machinelearningfor pages 4-7)

### Boundary cases

1. **Growth range, Tmin, and Tmax:** Tmin and Tmax delimit detectable growth; Topt identifies the maximum of the growth-rate reaction norm. They must not be represented as synonyms or direct values of `METPO:1000304`. For example, *Psychromonas ingrahamii* can grow at −12°C but has a reported Topt near 5°C. (siliakus2017adaptationsofarchaeal pages 8-10)
2. **Thermophile/psychrophile classes:** conventional categories—psychrophile below approximately 15°C, mesophile 15–45°C, thermophile 45–80°C, and hyperthermophile above 80°C—are classifications based on OGT, but their boundaries are not fixed. Psychrotrophy and facultative thermophily describe breadth or tolerance rather than the optimum itself. (colette2025machinelearningfor pages 1-4)
3. **Heat- or cold-shock survival:** survival after an acute exposure is a stress-resistance phenotype. It can evolve without improving high-temperature growth and therefore is not evidence of an OGT shift. (liang2024interactionsbetweenchaperone pages 16-17)
4. **Enzyme optimal temperature and protein melting temperature:** these are molecular properties, not organismal OGT. They may correlate with OGT, but should be separate nodes or traits. A recent synthesis reports a correlation of about *r*=0.76 between OGT and enzyme catalytic optimum, which is strong but not identity. (colette2025machinelearningfor pages 1-4)
5. **Environmental preference:** an organism’s realized habitat temperature integrates competition, dispersal, pressure, nutrients, and other stresses. It is not necessarily its laboratory OGT.
6. **Stationary biomass or endpoint yield:** unless maximum exponential growth rate was measured, an endpoint optimum should be labeled assay-specific rather than treated as an unqualified OGT.

## Current mechanistic understanding

OGT is best represented as an emergent, polygenic systems phenotype. Temperature changes reaction kinetics and the physical states of membranes, proteins, and nucleic acids. Efficient growth occurs where metabolic throughput is high but the costs of maintaining membrane function, translation, proteostasis, and macromolecular repair remain manageable. No single universal “thermophile gene” determines the optimum.

### 1. Membrane homeoviscous adaptation

Cooling orders the lipid bilayer and can impair permeability, transport, bioenergetics, and membrane-protein function. Microbes compensate by increasing unsaturated fatty acids or lipids with analogous disordering properties. The authoritative membrane-sensing review states that bacteria incorporate “proportionally more unsaturated fatty acids … as growth temperature decreases,” thereby disrupting bilayer order and optimizing cellular processes at the new temperature. (mendoza2014temperaturesensingby pages 1-2)

The strongest curation-ready circuit is the *Bacillus subtilis* **DesK–DesR–des** system. A temperature downshift from 37°C to 20°C induces `des`, which encodes a Δ5 fatty-acid desaturase. Reduced membrane fluidity shifts DesK toward kinase activity; DesK autophosphorylation at His-188 transfers phosphate to DesR Asp-54; DesR-P activates `des`; and increased unsaturated-fatty-acid synthesis restores fluidity. Importantly, isoleucine limitation or `lipA` perturbation activates this pathway at a constant 37°C, demonstrating that membrane physical state—not temperature alone—is the sensed proximal signal. (mendoza2014temperaturesensingby pages 5-6)

This mechanism should not be universalized without taxon qualification. At high temperature, bacteria can instead increase saturated, longer-chain, or iso-branched fatty acids, whereas archaea use ether-linked and, in many thermophiles, tetraether lipids with temperature-dependent cyclization. The relative roles of branching and unsaturation vary by taxon and pressure; deep-sea pressure and low temperature can produce overlapping lipid signatures. (siliakus2017adaptationsofarchaeal pages 8-10)

### 2. Metabolic organization within the non-stress range

A major recent development is the separation of **ordinary thermal growth physiology** from classical heat/cold-shock biology. In *Escherichia coli*, growth in an approximately 23–37°C Arrhenius range had an activation energy near 13 kcal mol⁻¹, with roughly 10–15 kcal mol⁻¹ across strains. Adaptation after an upshift took about 1.5 doublings and was attributed chiefly to metabolome rearrangement rather than large transcriptional, translational, or membrane-composition changes. Similar Arrhenius behavior was observed across multiple *E. coli* strains, *Bacillus subtilis*, and fission yeast. The precise metabolic constraints setting the optimum and upper/lower limits remain unresolved. (knapp2025metabolicrearrangementenables pages 1-2)

This supports a graph module `ambient temperature → reaction/metabolic-rate changes → metabolome rearrangement → growth-rate adaptation`, but the individual metabolites and enzymes should not yet be asserted as universal causal nodes.

### 3. Protein folding and proteome allocation

Above the optimum, protein denaturation and aggregation increase demands on DnaK/DnaJ, GroEL/GroES, ClpB, HtpG, proteases, and related quality-control systems. Heat also activates RNA thermometers and envelope-stress pathways. In *E. coli*, heat-generated unfolded periplasmic proteins activate DegS-mediated RseA proteolysis, releasing RpoE; RpoE then induces periplasmic proteases, folding factors, and envelope-biogenesis genes. RpoH is controlled by an RNA thermometer, DnaK sequestration, and FtsH/ClpXP turnover. (moon2023temperaturemattersbacterial pages 3-5)

These pathways are mechanistically real but usually explain **thermal stress survival or the decline above OGT**, not the optimum value directly. In evolved *Legionella pneumophila*, mutations in DnaJ/DnaK/HtpG enhanced survival during 55–59°C shocks, but the study did not establish an OGT shift. Mutation accumulation correlated with tolerance in two lineages (*r*²=0.916 and 0.618), emphasizing that survival and growth optimum require separate graph endpoints. (liang2024interactionsbetweenchaperone pages 16-17)

### 4. RNA structure, translation, and tRNA modification

Cooling stabilizes RNA secondary and tertiary structure, which can terminate transcription prematurely, alter RNA turnover, and obstruct ribosome binding. In *E. coli*, CspA binds RNA and promotes single-stranded conformations; after cold shock it accounts for approximately 15% of newly synthesized protein. CspA, the CsdA RNA helicase, and RNase R participate in cold RNA remodeling. (moon2023temperaturemattersbacterial pages 3-5)

In the hyperthermophile *Pyrococcus furiosus*, heat shock triggers Phr-governed transcriptome reprogramming, whereas 4°C cold shock produces distinct short- and long-term responses, ribosomal-protein upregulation, and enrichment of 5′-leadered transcripts. These responses prioritize energy provision, translation, and survival after deviation from optimal conditions; they are not direct evidence that the named genes set OGT. (grunberger2023uncoveringthetemporal pages 1-2, grunberger2023uncoveringthetemporal pages 23-24)

A 2024 Bacillales comparison found strong temperature dependence of tRNA modification in thermophilic *Geobacillus stearothermophilus*: Ψ55-positive tRNA clusters increased from 9 at 40°C to 21 at 55°C and 29 at 70°C; D17 increased 1→12→13 and D20 increased 6→18→19. s4U8 was much more prevalent than in the psychrophilic and mesophilic comparators, while Ψ38 was unique to the two psychrophiles examined. These are plausible RNA-stability/flexibility mechanisms, but without perturbation of the modifying enzymes they remain associations rather than proven OGT determinants. (hoffmann2024temperaturedependenttrnamodifications pages 13-14, hoffmann2024temperaturedependenttrnamodifications pages 9-10, hoffmann2024temperaturedependenttrnamodifications pages 17-19)

## Candidate nodes for `temperature_optimum.yaml`

### Trait and assay nodes

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| temperature optimum | Trait | `METPO:1000304` | Central phenotype; quote CURIE verbatim. |
| ambient temperature | Environmental factor | label; ENVO grounding should be verified locally | Numerical value and unit required. |
| maximum specific growth rate | Assay endpoint | label-only candidate | Preferred operational endpoint for OGT. |
| cultivation medium / pH / salinity / atmosphere / pressure | Experimental context | labels; use established ontology terms only after validation | Necessary because OGT is conditional. |
| growth temperature range | Nearby phenotype | label-only candidate | Not equivalent to OGT. |
| heat-shock survival / thermotolerance | Nearby phenotype | label-only candidate | Must terminate in a survival/tolerance node, not OGT. |
| enzyme catalytic temperature optimum | Molecular trait | label-only candidate | Correlated but distinct. |
| protein melting temperature | Molecular trait | label-only candidate | Distinct from organismal OGT. |

### Cellular structures and processes

| Candidate node | Type | Suggested grounding |
|---|---|---|
| cytoplasmic membrane | Cellular component | `GO:0005886` |
| membrane fluidity / lipid order | Biophysical property | label-only candidate; do not force an unsuitable GO term |
| homeoviscous adaptation | Biological process | label-only candidate |
| unsaturated-fatty-acid biosynthesis | Biological process | `GO:0006636` |
| protein folding | Biological process | `GO:0006457` |
| translation | Biological process | `GO:0006412` |
| response to temperature stimulus | Biological process | `GO:0009266` |
| metabolic rearrangement | Biological process | label-only candidate |
| RNA secondary-structure remodeling | Biological process | label-only candidate |

### Genes, proteins, and complexes

| Candidate node | Type | Grounding recommendation | Scope |
|---|---|---|---|
| DesK | Membrane histidine kinase/thermosensor | label plus organism-specific UniProt ID after verification | *B. subtilis*-specific direct mechanism |
| DesR | Response regulator | label plus organism-specific UniProt ID after verification | *B. subtilis*-specific direct mechanism |
| `des` / Δ5-Des | Fatty-acid desaturase | label; verify UniProt and EC assignment before YAML insertion | *B. subtilis* |
| DnaK, DnaJ, ClpB, GroEL/GroES, HtpG | Chaperones/disaggregases | labels plus taxon-specific UniProt IDs | Primarily stress/proteostasis context |
| DegS, RseA, RseP, RpoE | Envelope-stress signaling proteins | labels plus taxon-specific UniProt IDs | *E. coli* heat-stress module |
| RpoH, FtsH, ClpXP | Heat-shock regulator/proteases | labels plus taxon-specific UniProt IDs | *E. coli* heat-stress module |
| CspA, CsdA, RNase R | RNA chaperone/helicase/exoribonuclease | labels plus taxon-specific UniProt IDs | Cold-response module |
| Phr, TRAM-domain proteins | Transcriptional regulator/RNA-binding proteins | labels plus *P. furiosus* accessions after verification | Archaeal stress module; not universal |
| tRNA modification enzymes | Enzyme class | label-only until the relevant enzyme is experimentally identified | Current evidence concerns modified bases, not causal enzymes |

### Chemicals and molecular states

| Candidate node | Type | Suggested grounding / warning |
|---|---|---|
| unsaturated fatty acid | Chemical class | `CHEBI:27208` should be locally validated before release |
| saturated fatty acid | Chemical class | use a verified ChEBI class in implementation |
| branched-chain fatty acid | Chemical class | label-only until exact chain/class is specified |
| plasmalogen | Lipid class | label-only candidate; molecular species not specified in the ALE study |
| dihydrouridine, 4-thiouridine, pseudouridine | Modified nucleosides | use verified ChEBI records only after identifier validation |
| ATP | Metabolite/energy donor | `CHEBI:15422` |
| phospho-DesR | Protein state | represent as a stateful protein node or post-translational modification edge |

## Evidence-backed causal edges

The following table separates direct mechanisms from associations and boundary evidence.

| Evidence Tier | Subject | Predicate | Object | Taxon / Assay | DOI / Citation | Short Snippet | Curation Note |
|---|---|---|---|---|---|---|---|
| Direct Mechanistic | Membrane lipid order (fluidity decrease) | activates | DesK/DesR two-component system | *Bacillus subtilis* (Isotope/mutant perturbation) | 10.1146/annurev-micro-091313-103612 (mendoza2014temperaturesensingby pages 5-6) | "reducing isoleucine-derived fatty acids activates des transcription through DesK/DesR-dependent mechanism" | Direct causal link mapping physical membrane state (proxy for temperature) to homeoviscous adaptation sensing. |
| Direct Mechanistic | DesK/DesR two-component system | increases expression of | des (Δ5-Des desaturase) | *Bacillus subtilis* (Molecular assay) | 10.1146/annurev-micro-091313-103612 (mendoza2014temperaturesensingby pages 5-6) | "autophosphorylation of DesK at His-188 transfers phosphate to DesR at Asp-54, with phosphorylated DesR-P being the active transcriptional activator" | Completes the established mechanistic circuit to restore fluidity via unsaturated fatty acids. |
| Direct Mechanistic | Ambient temperature (Arrhenius range 23-37°C) | causes | Metabolic rearrangement | *Escherichia coli* (Growth rate profiling) | 10.1038/s41564-024-01841-4 (knapp2025metabolicrearrangementenables pages 1-2) | "temperature adaptation occurs via metabolome rearrangement rather than transcriptional, translational, or membrane fluidity changes" | Shifts paradigm for optimal growth range (as opposed to stress ranges) toward metabolic flux regulation. |
| Direct Mechanistic | Metabolic rearrangement | enables | Growth rate adaptation | *Escherichia coli* (Growth kinetics) | 10.1038/s41564-024-01841-4 (knapp2025metabolicrearrangementenables pages 1-2) | "Growth rate responds gradually to temperature upshifts over ~1.5 doublings at the new temperature" | Directly links metabolome changes to growth rate adjustments within the optimal temperature range. |
| Association / Uncertain | Serial transfer at 45°C (suboptimal temperature) | associated with | OGT shift from 66°C to 60°C | *Thermoanaerobacter kivui* (Adaptive Laboratory Evolution) | 10.3389/fmicb.2023.1265216 (lehmann2023adaptivelaboratoryevolution pages 1-2) | "adapted strain Adpt45_67 did not grow better at 45°C, but a shift in the TOPT to 60°C was observed... 67 SNPs" | Demonstrates OGT is evolvable alongside lipid changes (plasmalogens), but specific causal mutations driving OGT shift remain unresolved. |
| Association | Optimal growth temperature | correlated with | tRNA modifications (s4U8, Ψ55) | *Geobacillus stearothermophilus* (RNA sequencing) | 10.3390/ijms25168823 (hoffmann2024temperaturedependenttrnamodifications pages 13-14, hoffmann2024temperaturedependenttrnamodifications pages 1-2) | "elevated levels of s4U8 and Ψ55 modifications compared to non-thermophilic bacteria, suggesting temperature-dependent regulation" | Thermophile correlation only; adaptive strategy for structural stability, but causality via knockouts not established here. |
| Boundary / Context | Extreme temperature shift (heat/cold shock) | activates | Survival stress responses | *Pyrococcus furiosus* (Multi-omics) | 10.1128/mbio.02174-23 (grunberger2023uncoveringthetemporal pages 1-2, grunberger2023uncoveringthetemporal pages 23-24) | "Stress responses prioritize immediate survival (energy/translation) over growth" | Context only: Stress responses (chaperones, RNA stabilizers) are explicitly distinct from optimal growth state mechanisms. |
| Boundary / Negative | DnaJ/DnaK chaperone mutations | increases | Heat-shock survival | *Legionella pneumophila* (Adaptive Laboratory Evolution) | 10.7717/peerj.17197 (liang2024interactionsbetweenchaperone pages 16-17) | "suggesting these mutations enhance heat stress tolerance/survival rather than shifting optimal growth temperature" | Do not curate as OGT modifiers; mutations increase survival at 55-59°C but do not change the organism's baseline OGT. |


*Table: A curation-ready table extracting candidate causal triples, associations, and boundary cases for microbial optimal growth temperature, structured for direct graph curation and highlighting mechanistic certainties versus associative/survival traits.*

### Additional recommended triples

| Subject | Predicate | Object | Evidence and supporting snippet | Curation decision |
|---|---|---|---|---|
| decreasing ambient temperature | decreases | membrane fluidity | “At low temperatures membrane bilayers undergo a reversible change … from a fluid … to a nonfluid … array.” (mendoza2014temperaturesensingby pages 1-2) | **Curate**, general biophysical edge. |
| decreasing ambient temperature | increases | membrane unsaturated-fatty-acid proportion | “proportionally more unsaturated fatty acids … as growth temperature decreases.” (mendoza2014temperaturesensingby pages 1-2) | **Curate** as adaptive response; qualify organismal scope. |
| increased unsaturated-fatty-acid proportion | decreases | lipid-bilayer order | The review states that incorporation is “suited to disrupt the order of the lipid bilayer.” (mendoza2014temperaturesensingby pages 1-2) | **Curate**. |
| restored membrane fluidity | supports | membrane-dependent physiological processes | Homeoviscous adaptation “optimizes the performance of a large array of cellular physiological processes.” (mendoza2014temperaturesensingby pages 1-2) | **Curate cautiously**; object is broad. Do not directly assert an OGT shift. |
| heat-denatured periplasmic proteins | activates | DegS–RseA–RpoE pathway | DegS recognizes denatured proteins; RseA proteolysis releases RpoE. (moon2023temperaturemattersbacterial pages 3-5) | **Curate only in a heat-stress subgraph**, not as a universal OGT edge. |
| cold temperature | increases | stable RNA secondary structure | Stabilized RNA alters transcription, turnover, and ribosome binding. (moon2023temperaturemattersbacterial pages 3-5) | **Curate** as a general cold-stress biophysical edge. |
| CspA RNA binding | promotes | single-stranded RNA | CspA promotes single-stranded RNA “by unwinding or capturing transiently unwound bases.” (moon2023temperaturemattersbacterial pages 3-5) | **Curate** for *E. coli* cold adaptation; uncertain effect on OGT. |
| thermal ALE at 45°C | associated_with | reduction of Topt from 66°C to 60°C | *T. kivui* shifted after 67 transfers/~180 generations. (lehmann2023adaptivelaboratoryevolution pages 1-2) | **Curate as experiment→phenotype**, not mutation→phenotype. |
| higher OGT | positively_correlates_with | aromatic/hydrophobic proteome residues | Proteins contain more aromatic and hydrophobic residues at higher temperature. (barnum2024predictingmicrobialgrowth pages 1-3) | **Association only**; phylogeny and proteome composition confound causality. |
| higher OGT | positively_correlates_with | glutamate frequency | Spearman ρ=0.39. (barnum2024predictingmicrobialgrowth pages 3-6) | **Association only**. |

## Recent developments and quantitative results, 2023–2024

### Direct evolution of an optimum

Lehmann and colleagues evolved *Thermoanaerobacter kivui*, whose ancestral Topt was 66°C, through 67 transfers—approximately 180 generations—at 45°C. The evolved lineage did not improve at 45°C but its measured Topt moved to 60°C. It also had 67 SNPs, altered morphology, increased plasmalogens, and temperature-dependent short-chain-fatty-acid changes. This is unusually direct evidence that an organismal optimum is evolvable, but the authors explicitly leave its molecular basis unresolved. (lehmann2023adaptivelaboratoryevolution pages 1-2)

### Genome-based OGT prediction

A 2024 preprint trained family-held-out models on 15,596 bacterial and archaeal genomes. Its OGT model obtained cross-validation *R*²=0.73 and RMSE=6.53°C; test performance was *R*²=0.72 and RMSE=7.42°C. The final temperature dataset included 1,722 organisms spanning 4–105°C. Performance was substantially poorer below 15°C, with RMSE around 14°C. The models can guide cultivation, but they infer OGT from compositional associations rather than causal genes. (barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 6-9, barnum2024predictingmicrobialgrowth pages 22-24)

### RNA adaptation

The 2024 Bacillales study provides fine-grained evidence that modification profiles vary with both lineage and assay temperature. Its strongest pattern—large increases in Ψ55, D17, and D20 in thermophilic *G. stearothermophilus*—supports an RNA-structure module but still needs knockout, complementation, or enzyme-manipulation experiments before a modification→OGT edge is justified. (hoffmann2024temperaturedependenttrnamodifications pages 13-14, hoffmann2024temperaturedependenttrnamodifications pages 9-10)

### Distinguishing tolerance from optimum

Recent adaptive-evolution work in *L. pneumophila* found repeated chaperone-system mutations during selection at 55–59°C. This is valuable for understanding failed hot-water pasteurization, but its endpoint was transient heat survival. It therefore demonstrates why tolerance evidence cannot automatically populate an OGT graph. (liang2024interactionsbetweenchaperone pages 16-17)

## Applications and real-world implementations

1. **Cultivation of uncultured microbes:** genome-composition models can prioritize incubation temperatures when physiological records are absent. Their family-level validation is useful for novel taxa, but predictions should remain evidence-qualified, especially for psychrophiles. (barnum2024predictingmicrobialgrowth pages 6-9, barnum2024predictingmicrobialgrowth pages 22-24)
2. **Bioprocess strain design:** shifting the thermal reaction norm can support fermentation at temperatures that reduce cooling costs or contamination. ALE of *T. kivui* demonstrates an experimentally movable Topt, although its causal mutations remain unknown. (lehmann2023adaptivelaboratoryevolution pages 1-2)
3. **Public-health water management:** repeated sublethal heating can select *Legionella* with greater heat-shock survival through chaperone and energy-storage networks. This informs superheat-and-flush protocols but should not be interpreted as proof of higher OGT. (liang2024interactionsbetweenchaperone pages 16-17)
4. **Environmental and climate modeling:** OGT and thermal growth curves can help forecast community turnover, but mechanistic models must distinguish routine Arrhenius-range growth from acute thermal stress. (knapp2025metabolicrearrangementenables pages 1-2)
5. **Enzyme discovery and protein engineering:** microbial OGT is useful as a prior for protein thermostability and catalytic-temperature searches, but the organismal and protein optima are not interchangeable. (colette2025machinelearningfor pages 1-4)

## Recommended minimal TraitMech graph

A conservative first revision could retain a balanced-adaptation topology while separating direct mechanisms from contextual branches:

1. `ambient temperature decrease → decreases → membrane fluidity`
2. `decreased membrane fluidity → activates → DesK kinase activity` **[*B. subtilis*]**
3. `DesK kinase activity → increases → DesR phosphorylation` **[*B. subtilis*]**
4. `phospho-DesR → activates transcription of → des` **[*B. subtilis*]**
5. `Δ5-Des activity → increases → unsaturated-fatty-acid proportion` **[*B. subtilis*]**
6. `unsaturated-fatty-acid proportion → increases → membrane fluidity`
7. `ambient temperature in Arrhenius range → changes → metabolic reaction rates`
8. `changed metabolic reaction rates → induces → metabolome rearrangement`
9. `metabolome rearrangement → enables → growth-rate adaptation`
10. `balanced membrane function + metabolic throughput + proteostasis + translation → supports → maximal specific growth rate`
11. `maximal specific growth rate at measured temperature → realizes → METPO:1000304`

Edges 1–6 and 7–9 have comparatively strong mechanistic support, although the first module is taxon-specific and the second does not yet identify universal molecular mediators. Edge 10 is a synthesis node and should be marked **inferred** rather than represented as a single experimentally proven interaction. (knapp2025metabolicrearrangementenables pages 1-2, mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 1-2)

## Claims not yet ready for TraitMech curation

- **Do not curate individual *T. kivui* SNPs, plasmalogens, or cAMP-regulator mutations as causes of the 66→60°C Topt shift.** They co-occurred after ALE, but causality was not resolved. (lehmann2023adaptivelaboratoryevolution pages 1-2)
- **Do not map DnaJ/DnaK/HtpG mutations directly to increased OGT in *Legionella*.** The demonstrated endpoint was heat-shock survival. (liang2024interactionsbetweenchaperone pages 16-17)
- **Do not treat heat/cold-shock induction as the normal optimum state.** *P. furiosus* stress programs prioritize survival and recovery outside optimal conditions. (grunberger2023uncoveringthetemporal pages 1-2, grunberger2023uncoveringthetemporal pages 23-24)
- **Do not infer causality from proteome amino-acid composition.** The 2024 model is predictive and phylogenetically structured; glutamate frequency (ρ=0.39), hydrophobicity, and aromatic residues are associations. (barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 3-6)
- **Do not curate tRNA modifications as OGT setters without perturbational validation.** Temperature-dependent s4U8, Ψ55, and D patterns are compelling but comparative. (hoffmann2024temperaturedependenttrnamodifications pages 13-14, hoffmann2024temperaturedependenttrnamodifications pages 9-10)
- **Do not universalize bacterial ester-lipid mechanisms to archaea.** Archaeal ether/tetraether lipids use distinct adaptive chemistry. (siliakus2017adaptationsofarchaeal pages 8-10)
- **Do not merge OGT with enzyme optimum, protein Tm, habitat temperature, isolation temperature, Tmax, or acute tolerance.** (colette2025machinelearningfor pages 1-4, colette2025machinelearningfor pages 4-7)
- **Do not assign unverified CURIEs.** Taxon-specific proteins should remain label-only until UniProt accessions are checked against the exact strain; modified-nucleoside ChEBI records and enzyme EC assignments likewise require registry validation.

## DOI-first bibliography

1. Knapp BD et al. **Metabolic rearrangement enables adaptation of microbial growth rate to temperature shifts.** *Nature Microbiology* 10, 185–201. Online DOI record dated 2024; issue publication 2025. DOI: [10.1038/s41564-024-01841-4](https://doi.org/10.1038/s41564-024-01841-4). (knapp2025metabolicrearrangementenables pages 1-2)
2. Hoffmann A et al. **Temperature-Dependent tRNA Modifications in Bacillales.** *International Journal of Molecular Sciences* 25. August 2024. DOI: [10.3390/ijms25168823](https://doi.org/10.3390/ijms25168823). (hoffmann2024temperaturedependenttrnamodifications pages 13-14, hoffmann2024temperaturedependenttrnamodifications pages 9-10)
3. Barnum TP et al. **Predicting microbial growth conditions from amino acid composition.** bioRxiv. March 2024, preprint. DOI: [10.1101/2024.03.22.586313](https://doi.org/10.1101/2024.03.22.586313). (barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 22-24)
4. Liang J, Faucher S. **Interactions between chaperone and energy storage networks during the evolution of *Legionella pneumophila* under heat shock.** *PeerJ* 12. April 2024. DOI: [10.7717/peerj.17197](https://doi.org/10.7717/peerj.17197). (liang2024interactionsbetweenchaperone pages 16-17)
5. Lehmann M et al. **Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.** *Frontiers in Microbiology* 14. October 2023. DOI: [10.3389/fmicb.2023.1265216](https://doi.org/10.3389/fmicb.2023.1265216). (lehmann2023adaptivelaboratoryevolution pages 1-2)
6. Grünberger F et al. **Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics.** *mBio* 14. December 2023. DOI: [10.1128/mbio.02174-23](https://doi.org/10.1128/mbio.02174-23). (grunberger2023uncoveringthetemporal pages 1-2, grunberger2023uncoveringthetemporal pages 23-24)
7. Moon S et al. **Temperature Matters: Bacterial Response to Temperature Change.** *Journal of Microbiology* 61, 343–357. March 2023. DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x). (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5)
8. Siliakus MF, van der Oost J, Kengen SWM. **Adaptations of archaeal and bacterial membranes to variations in temperature, pH and pressure.** *Extremophiles* 21, 651–670. May 2017. DOI: [10.1007/s00792-017-0939-x](https://doi.org/10.1007/s00792-017-0939-x). (siliakus2017adaptationsofarchaeal pages 8-10)
9. Ernst R, Ejsing CS, Antonny B. **Homeoviscous Adaptation and the Regulation of Membrane Lipids.** *Journal of Molecular Biology* 428, 4776–4791. December 2016. DOI: [10.1016/j.jmb.2016.08.013](https://doi.org/10.1016/j.jmb.2016.08.013). (ernst2016homeoviscousadaptationand pages 1-2)
10. de Mendoza D. **Temperature Sensing by Membranes.** *Annual Review of Microbiology* 68, 101–116. September 2014. DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612). (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 1-2)

**Overall curation judgment:** the most defensible additions to the existing nine-node graph are the taxon-qualified DesK/DesR/des homeoviscous circuit and a separate Arrhenius-range metabolic-rearrangement module. Recent ALE and RNA-modification results should enter as evidence annotations or uncertain association edges—not as universal molecular causes of `METPO:1000304`.

References

1. (colette2025machinelearningfor pages 1-4): Sophie Colette, Jaldert François, Bart De Moor, and Vera van Noort. Machine learning for optimal growth temperature prediction of prokaryotes using amino acid descriptors. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.03.03.640802, doi:10.1101/2025.03.03.640802. This article has 5 citations.

2. (colette2025machinelearningfor pages 4-7): Sophie Colette, Jaldert François, Bart De Moor, and Vera van Noort. Machine learning for optimal growth temperature prediction of prokaryotes using amino acid descriptors. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.03.03.640802, doi:10.1101/2025.03.03.640802. This article has 5 citations.

3. (siliakus2017adaptationsofarchaeal pages 8-10): Melvin F. Siliakus, John van der Oost, and Servé W. M. Kengen. Adaptations of archaeal and bacterial membranes to variations in temperature, ph and pressure. Extremophiles, 21:651-670, May 2017. URL: https://doi.org/10.1007/s00792-017-0939-x, doi:10.1007/s00792-017-0939-x. This article has 551 citations and is from a peer-reviewed journal.

4. (liang2024interactionsbetweenchaperone pages 16-17): Jeffrey Liang and Sebastien Faucher. Interactions between chaperone and energy storage networks during the evolution of legionella pneumophila under heat shock. PeerJ, Apr 2024. URL: https://doi.org/10.7717/peerj.17197, doi:10.7717/peerj.17197. This article has 2 citations and is from a peer-reviewed journal.

5. (mendoza2014temperaturesensingby pages 1-2): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

6. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

7. (knapp2025metabolicrearrangementenables pages 1-2): Benjamin D. Knapp, Lisa Willis, Carlos Gonzalez, Harsh Vashistha, Joanna Jammal-Touma, Mikhail Tikhonov, Jeffrey Ram, Hanna Salman, Josh E. Elias, and Kerwyn Casey Huang. Metabolic rearrangement enables adaptation of microbial growth rate to temperature shifts. Nature microbiology, 10:185-201, Dec 2025. URL: https://doi.org/10.1038/s41564-024-01841-4, doi:10.1038/s41564-024-01841-4. This article has 47 citations and is from a highest quality peer-reviewed journal.

8. (moon2023temperaturemattersbacterial pages 3-5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

9. (grunberger2023uncoveringthetemporal pages 1-2): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 23 citations and is from a domain leading peer-reviewed journal.

10. (grunberger2023uncoveringthetemporal pages 23-24): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 23 citations and is from a domain leading peer-reviewed journal.

11. (hoffmann2024temperaturedependenttrnamodifications pages 13-14): Anne Hoffmann, Christian Lorenz, Jörg Fallmann, Philippe Wolff, Antony Lechner, Heike Betat, Mario Mörl, and Peter Florian Stadler. Temperature-dependent trna modifications in bacillales. International Journal of Molecular Sciences, Aug 2024. URL: https://doi.org/10.3390/ijms25168823, doi:10.3390/ijms25168823. This article has 6 citations.

12. (hoffmann2024temperaturedependenttrnamodifications pages 9-10): Anne Hoffmann, Christian Lorenz, Jörg Fallmann, Philippe Wolff, Antony Lechner, Heike Betat, Mario Mörl, and Peter Florian Stadler. Temperature-dependent trna modifications in bacillales. International Journal of Molecular Sciences, Aug 2024. URL: https://doi.org/10.3390/ijms25168823, doi:10.3390/ijms25168823. This article has 6 citations.

13. (hoffmann2024temperaturedependenttrnamodifications pages 17-19): Anne Hoffmann, Christian Lorenz, Jörg Fallmann, Philippe Wolff, Antony Lechner, Heike Betat, Mario Mörl, and Peter Florian Stadler. Temperature-dependent trna modifications in bacillales. International Journal of Molecular Sciences, Aug 2024. URL: https://doi.org/10.3390/ijms25168823, doi:10.3390/ijms25168823. This article has 6 citations.

14. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

15. (hoffmann2024temperaturedependenttrnamodifications pages 1-2): Anne Hoffmann, Christian Lorenz, Jörg Fallmann, Philippe Wolff, Antony Lechner, Heike Betat, Mario Mörl, and Peter Florian Stadler. Temperature-dependent trna modifications in bacillales. International Journal of Molecular Sciences, Aug 2024. URL: https://doi.org/10.3390/ijms25168823, doi:10.3390/ijms25168823. This article has 6 citations.

16. (barnum2024predictingmicrobialgrowth pages 1-3): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

17. (barnum2024predictingmicrobialgrowth pages 3-6): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

18. (barnum2024predictingmicrobialgrowth pages 6-9): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

19. (barnum2024predictingmicrobialgrowth pages 22-24): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

20. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

21. (ernst2016homeoviscousadaptationand pages 1-2): Robert Ernst, Christer S. Ejsing, and Bruno Antonny. Homeoviscous adaptation and the regulation of membrane lipids. Journal of molecular biology, 428 24 Pt A:4776-4791, Dec 2016. URL: https://doi.org/10.1016/j.jmb.2016.08.013, doi:10.1016/j.jmb.2016.08.013. This article has 614 citations and is from a domain leading peer-reviewed journal.