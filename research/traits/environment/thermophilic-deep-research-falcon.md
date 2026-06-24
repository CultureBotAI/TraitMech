---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:38:38.039609'
end_time: '2026-06-18T02:55:01.676025'
duration_seconds: 983.64
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: thermophilic
  trait_identifier: METPO:1000616
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: thermophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature preference in which growth is favored at elevated temperatures,\
    \ typically \u226545 \xB0C."
  parent_traits: METPO:1000613
  synonyms: ''
  evidence_summary: 'DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of
    high temperature (Supports thermophilic growth as adaptation to elevated temperature.)
    | PMID:24058645: Geobacillus stearothermophilus is a gram-positive, thermophilic
    bacterium (Organism example: Geobacillus stearothermophilus is described as thermophilic.)'
  causal_graph_summary: 'thermophilic_heat_adaptation: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** thermophilic
- **METPO identifier:** METPO:1000616
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at elevated temperatures, typically ≥45 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Supports thermophilic growth as adaptation to elevated temperature.) | PMID:24058645: Geobacillus stearothermophilus is a gram-positive, thermophilic bacterium (Organism example: Geobacillus stearothermophilus is described as thermophilic.)
- **Existing causal graph summary:** thermophilic_heat_adaptation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **thermophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/thermophilic.yaml`.

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
- **Trait label:** thermophilic
- **METPO identifier:** METPO:1000616
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at elevated temperatures, typically ≥45 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Supports thermophilic growth as adaptation to elevated temperature.) | PMID:24058645: Geobacillus stearothermophilus is a gram-positive, thermophilic bacterium (Organism example: Geobacillus stearothermophilus is described as thermophilic.)
- **Existing causal graph summary:** thermophilic_heat_adaptation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **thermophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/thermophilic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **thermophilic** (METPO:1000616)

### Scope summary (trait meaning and boundaries)
**Thermophilic** denotes a growth-temperature preference in which an organism’s *optimal growth temperature* (TOPT) lies above ~45 °C, typically determined from a growth-rate (or yield) vs. temperature curve that yields the *cardinal temperatures* TMIN, TOPT, and TMAX. (lehmann2023adaptivelaboratoryevolution pages 1-2)

Operational categories used in recent literature include:
- **Thermophile**: TOPT > 45 °C (often with endurance roughly 45–75 °C in applied contexts). (lehmann2023adaptivelaboratoryevolution pages 1-2, gallo2024theundeniablepotential pages 1-3)
- **Moderate thermophile**: TOPT ~45–65 °C; **strict thermophile**: TOPT ~65–80 °C; **hyperthermophile**: growth above ~80 °C (some species tolerate >100 °C). (rekadwad2023extremophilesthespecies pages 2-4, takemata2024howdothermophiles pages 1-2)
- **Thermotolerant** (boundary case): organisms that can survive above ~45 °C but may not have TOPT > 45 °C (survival ≠ preference). (rekadwad2023extremophilesthespecies pages 2-4)

**Assay/measurement notes for curation**: the clearest curation criterion is TOPT > 45 °C measured by growth profiling across temperatures (cardinal temperature determination). This distinguishes “thermophilic” from “thermotolerant” (survival at heat) and from “hyperthermophilic” (TOPT and growth sustained above ~80 °C). (lehmann2023adaptivelaboratoryevolution pages 1-2, rekadwad2023extremophilesthespecies pages 2-4)

---

### Key concepts and mechanistic understanding (2023–2024 emphasis)
Thermophily is widely understood as a **multicomponent systems phenotype**: elevated temperature threatens protein folding, membrane integrity, and genome stability; thermophiles maintain function through coupled adaptations spanning protein homeostasis, membrane physicochemistry, and genome topology/organization. (lehmann2023adaptivelaboratoryevolution pages 2-3, takemata2024howdothermophiles pages 1-2)

#### 1) Protein homeostasis (proteostasis) at high temperature
In the thermophilic crenarchaeon *Sulfolobus acidocaldarius*, heat shock induces a coordinated chaperone system in which **small heat shock proteins (sHSPs)** and **prefoldin** bind denaturing proteins and deliver them to the **HSP60-type group II chaperonin (“thermosome”)** for ATP-dependent refolding. (baes2023transcriptionalandtranslational pages 1-2)

Recent biochemical work on crenarchaeal group II chaperonins further supports this central role: HSPα/HSPβ form large complexes that assist folding and protect proteins during thermal stress, with measurable thermostability across temperature ranges. (furr2024structuralstabilitycomparisons pages 1-2)

#### 2) DNA protection via topology and genome organization
A defining genomic/biochemical marker of many thermophiles—especially above ~65 °C—is **reverse gyrase**, a unique topoisomerase that introduces **positive supercoils**. Reverse gyrase is suggested to support genome integrity by limiting DNA melting and contributing to repair. (takemata2024howdothermophiles pages 1-2)

In *S. acidocaldarius*, heat shock is associated with increased positive supercoiling linked to increased **TopR1** activity (reverse gyrase paralog), connecting thermal stress to a measurable DNA-topology response. (baes2023transcriptionalandtranslational pages 1-2)

Genome stabilization is also associated with proteins and small molecules that shape DNA packaging and 3D organization, including **nucleoid-associated proteins (NAPs)**, **histones**, **SMC-family proteins**, and potentially **polyamines** (positively charged compounds) that may enhance DNA thermostability. (takemata2024howdothermophiles pages 4-5)

#### 3) Membrane lipid adaptation: ether lipids, tetraethers, and temperature-tuned modifications
Archaeal thermophiles/thermoacidophiles commonly use **ether-linked isoprenoid lipids** and **tetraether (membrane-spanning) lipids** (e.g., GDGT/GDNT), which provide enhanced chemical/thermal stability compared with ester lipids; membranes tune rigidity via cyclization and other structural changes. (chong2024archaeamembranesin pages 1-2)

A key recent advance (2024) is the experimental linkage of **GMGT (glycerol monoalkyl glycerol tetraether)** biosynthesis/modification to temperature:
- **Gms** (GMGT synthase; radical SAM enzyme) cross-links GDGT tails to form GMGTs.
- **Gmm** (GMGT methylase; radical SAM enzyme) methylates the GMGT hydrocarbon core.
- **GrsA/GrsB** catalyze cyclopentane ring formation in GDGTs, linking cyclization to tetraether lipid adaptation pathways. (garcia2024identificationoftwo pages 1-2, garcia2024identificationoftwo pages 2-2)

In cultures of thermophilic archaea, **GMGT abundance, methylation, and cyclization can increase with growth temperature**, with GMGTs dominating monolayer lipids at high temperature in some species. The temperature dependence is visualized in Garcia et al. (PNAS 2024) Figure 5. (garcia2024identificationoftwo pages 6-7, garcia2024identificationoftwo media b2e6804e)

**Curation warning**: temperature–GMGT relationships are not universal across taxa; a 2024 Nature Communications study notes that *Pyrococcus furiosus* showed decreased GMGT abundance with increasing temperature in prior culture work, so edges linking “temperature increase → GMGT increase” should be annotated as clade/taxon-conditional. (li2024biosynthesisofgmgt pages 1-2)

---

### Candidate nodes for `thermophilic.yaml` (grouped by type)
The following table provides curation-ready node candidates grounded to the available evidence.

| Node label | Node type | Role in thermophily | Evidence source(s) | Key citation context IDs | Suggested CURIE grounding | Notes on uncertainty/taxon-specificity |
|---|---|---|---|---|---|---|
| elevated temperature / heat shock | environmental factor | primary selecting stressor | Lehmann 2023; Baes 2023; Gallo 2024 | (lehmann2023adaptivelaboratoryevolution pages 1-2, baes2023transcriptionalandtranslational pages 1-2, gallo2024theundeniablepotential pages 1-3) | label-only | Central environmental driver; operationally measured via TOPT/TMIN/TMAX |
| geothermal habitat / hot spring | environmental factor | typical source environment | Gallo 2024; Rekadwad 2023 | (gallo2024theundeniablepotential pages 1-3, rekadwad2023extremophilesthespecies pages 2-4) | ENVO:00000446 hot spring | Broad environment node; not itself mechanistic |
| compost thermogenic phase (50–80 °C) | environmental factor | ecological selector for thermophiles | Finore 2023 | (finore2023thermophilicbacteriaand pages 5-7) | label-only | Specific to compost systems |
| high-temperature growth preference (thermophily) | phenotype | trait being explained | Lehmann 2023; Gallo 2024 | (lehmann2023adaptivelaboratoryevolution pages 1-2, gallo2024theundeniablepotential pages 1-3) | METPO:1000616 | Core trait node |
| hyperthermophily | phenotype | boundary case above thermophily | Lehmann 2023; Rekadwad 2023 | (lehmann2023adaptivelaboratoryevolution pages 1-2, rekadwad2023extremophilesthespecies pages 2-4) | label-only | Distinct nearby trait; generally >80 °C |
| thermotolerance | phenotype | survival at heat without strict preference | Rekadwad 2023 | (rekadwad2023extremophilesthespecies pages 2-4) | label-only | Boundary term; may not equal thermophily |
| growth temperature optimum (TOPT) | phenotype | operational assay descriptor | Lehmann 2023; Takemata 2024 | (lehmann2023adaptivelaboratoryevolution pages 1-2, takemata2024howdothermophiles pages 1-2) | label-only | Assay/property node rather than mechanism |
| heat shock response | process | acute response to temperature upshift | Baes 2023 | (baes2023transcriptionalandtranslational pages 1-2) | GO:0009408 | Acute stress response; not identical to constitutive thermophily |
| protein folding | process | preserves proteome function at heat | Baes 2023; Furr 2024 | (baes2023transcriptionalandtranslational pages 1-2, furr2024structuralstabilitycomparisons pages 1-2) | GO:0006457 | Strongly supported process |
| DNA topological change / positive supercoiling | process | stabilizes DNA at high temperature | Takemata 2024; Baes 2023 | (takemata2024howdothermophiles pages 1-2, baes2023transcriptionalandtranslational pages 1-2) | GO:0006265 | Especially supported in thermophilic archaea |
| DNA repair | process | protects genome integrity at heat | Takemata 2024 | (takemata2024howdothermophiles pages 1-2) | GO:0006281 | Mechanistic linkage often review-level |
| chromatin / nucleoid organization | process | compacts and protects genome | Takemata 2024; Baes 2023 | (takemata2024howdothermophiles pages 4-5, baes2023transcriptionalandtranslational pages 1-2) | GO:0006325 | Strong in archaeal models; factor-specific effects vary |
| membrane adaptation / homeoviscous adjustment | process | maintains membrane stability | Chong 2024; Rekadwad 2023 | (chong2024archaeamembranesin pages 1-2, rekadwad2023extremophilesthespecies pages 2-4) | label-only | Broad process label; composition depends on lineage |
| small heat shock proteins (sHSPs/HSP20) | gene/protein/complex | bind denaturing proteins | Baes 2023; Sato 2024 via review context | (baes2023transcriptionalandtranslational pages 1-2) | label-only | Strong for archaeal and thermotolerant systems; family-level node |
| prefoldin | gene/protein/complex | shuttles unfolded proteins | Baes 2023 | (baes2023transcriptionalandtranslational pages 1-2) | label-only | Best supported in Sulfolobales |
| thermosome / group II chaperonin | gene/protein/complex | ATP-dependent refolding cage | Baes 2023; Furr 2024 | (baes2023transcriptionalandtranslational pages 1-2, furr2024structuralstabilitycomparisons pages 1-2) | label-only | Archaeal complex; equivalent bacterial systems differ |
| HSPα | gene/protein/complex | thermostable chaperonin subunit | Furr 2024 | (furr2024structuralstabilitycomparisons pages 1-2) | label-only | Crenarchaeal, taxon-specific |
| HSPβ | gene/protein/complex | thermostable chaperonin subunit | Furr 2024 | (furr2024structuralstabilitycomparisons pages 1-2) | label-only | Crenarchaeal, taxon-specific |
| Thα / Thβ / Thγ thermosome subunits | gene/protein/complex | temperature-tuned chaperonin composition | Baes 2023 | (baes2023transcriptionalandtranslational pages 1-2) | label-only | Specific to Sulfolobales |
| reverse gyrase | gene/protein/complex | introduces positive supercoils | Takemata 2024; Baes 2023 | (takemata2024howdothermophiles pages 1-2, baes2023transcriptionalandtranslational pages 1-2) | EC:5.6.2.2 | Canonical thermophile marker, especially >65 °C |
| TopR1 | gene/protein/complex | heat-responsive reverse gyrase paralog | Baes 2023; Takemata 2024 | (baes2023transcriptionalandtranslational pages 1-2, takemata2024howdothermophiles pages 1-2) | label-only | Sulfolobus-specific naming |
| nucleoid-associated proteins (NAPs) | gene/protein/complex | reorganize and compact DNA | Takemata 2024; Baes 2023 | (takemata2024howdothermophiles pages 4-5, baes2023transcriptionalandtranslational pages 1-2) | label-only | Broad class node |
| Alba | gene/protein/complex | archaeal DNA-binding organizer | Takemata 2024 | (takemata2024howdothermophiles pages 4-5) | label-only | Archaeal/taxon-specific |
| Sul7 | gene/protein/complex | archaeal chromatin protein | Takemata 2024 | (takemata2024howdothermophiles pages 4-5) | label-only | Archaeal/taxon-specific |
| Cren7 | gene/protein/complex | archaeal chromatin protein | Takemata 2024 | (takemata2024howdothermophiles pages 4-5) | label-only | Archaeal/taxon-specific |
| TrmBL2 | gene/protein/complex | genome architectural factor | Takemata 2024 | (takemata2024howdothermophiles pages 4-5) | label-only | Archaeal/taxon-specific |
| histones (archaeal) | gene/protein/complex | DNA stabilization/compaction | Takemata 2024; Lehmann 2023 | (takemata2024howdothermophiles pages 4-5, lehmann2023adaptivelaboratoryevolution pages 2-3) | GO:0030527 structural constituent of chromatin | Not present in all thermophiles |
| SMC proteins / Arcadin-4 | gene/protein/complex | higher-order chromosome structuring | Takemata 2024 | (takemata2024howdothermophiles pages 4-5) | label-only | Best supported in archaeal genome-organization studies |
| Gms (GMGT synthase) | gene/protein/complex | cross-links GDGT tails to GMGT | Garcia 2024; Li 2024 | (garcia2024identificationoftwo pages 1-2, li2024biosynthesisofgmgt pages 1-2, garcia2024identificationoftwo pages 2-3) | label-only | Recently identified radical SAM enzyme |
| Gmm (GMGT methylase) | gene/protein/complex | methylates GMGT core lipids | Garcia 2024 | (garcia2024identificationoftwo pages 1-2, garcia2024identificationoftwo pages 3-4) | label-only | Recently identified; archaeal lipid modifier |
| GrsA | gene/protein/complex | forms GDGT cyclopentane rings | Garcia 2024; Li 2024 | (garcia2024identificationoftwo pages 2-2, li2024biosynthesisofgmgt pages 3-4) | label-only | Lipid-cyclization enzyme |
| GrsB | gene/protein/complex | forms additional GDGT rings | Garcia 2024; Li 2024 | (garcia2024identificationoftwo pages 2-2, li2024biosynthesisofgmgt pages 3-4) | label-only | Lipid-cyclization enzyme |
| Tes (tetraether synthase) | gene/protein/complex | forms GDGT backbone | Garcia 2024; Li 2024 | (garcia2024identificationoftwo pages 2-2, li2024biosynthesisofgmgt pages 3-4) | label-only | Relevant precursor pathway node |
| radical SAM enzyme family | gene/protein/complex | catalyzes unusual lipid C–C chemistry | Garcia 2024; Li 2024 | (garcia2024identificationoftwo pages 6-7, li2024biosynthesisofgmgt pages 1-2, li2024biosynthesisofgmgt pages 3-4) | label-only | Family-level node, not single gene |
| archaeal ether-linked isoprenoid lipids | lipid/metabolite/chemical | chemically stable membrane matrix | Chong 2024; Rekadwad 2023 | (chong2024archaeamembranesin pages 1-2, rekadwad2023extremophilesthespecies pages 2-4) | label-only | Strong for archaea; bacteria use different lipid strategies |
| GDGT | lipid/metabolite/chemical | core tetraether membrane lipid | Chong 2024; Garcia 2024 | (chong2024archaeamembranesin pages 1-2, garcia2024identificationoftwo pages 1-2) | label-only | Central archaeal lipid node |
| GDNT | lipid/metabolite/chemical | thermoacidophile membrane tetraether | Chong 2024 | (chong2024archaeamembranesin pages 1-2) | label-only | Especially relevant to thermoacidophiles |
| GMGT | lipid/metabolite/chemical | cross-linked monolayer lipid for heat adaptation | Garcia 2024; Li 2024 | (garcia2024identificationoftwo pages 6-7, garcia2024identificationoftwo pages 1-2, li2024biosynthesisofgmgt pages 1-2) | label-only | Strong in some thermophilic archaea; response can vary by taxon |
| methylated GMGT | lipid/metabolite/chemical | fine-tunes membrane properties | Garcia 2024 | (garcia2024identificationoftwo pages 6-7, garcia2024identificationoftwo pages 3-4) | label-only | Particularly supported in Vulcanisaeta distributa |
| cyclized GDGT/GMGT | lipid/metabolite/chemical | increases membrane rigidity | Chong 2024; Garcia 2024 | (chong2024archaeamembranesin pages 1-2, garcia2024identificationoftwo pages 6-7, garcia2024identificationoftwo media b2e6804e) | label-only | Ring-number effects best studied in archaea |
| cyclopentane rings | lipid/metabolite/chemical | condense tetraether membranes | Chong 2024; Garcia 2024 | (chong2024archaeamembranesin pages 1-2, garcia2024identificationoftwo pages 2-2) | CHEBI:30387 cyclopentane | Feature node rather than standalone metabolite |
| polyamines | lipid/metabolite/chemical | stabilize DNA at high temperature | Takemata 2024 | (takemata2024howdothermophiles pages 4-5) | CHEBI:17599 | Support is review-level and somewhat generalized |
| teichoic acid | lipid/metabolite/chemical | cell-wall composition linked to heat stability | Rekadwad 2023 | (rekadwad2023extremophilesthespecies pages 2-4) | CHEBI:26115 | Mainly bacterial cell-wall correlation, not universal |
| cytoplasmic membrane | cellular component | site of thermal stability adaptation | Baes 2023; Chong 2024 | (baes2023transcriptionalandtranslational pages 1-2, chong2024archaeamembranesin pages 1-2) | GO:0005886 | Universal component |
| archaeal monolayer membrane | cellular component | rigid high-temperature barrier | Chong 2024; Garcia 2024 | (chong2024archaeamembranesin pages 1-2, garcia2024identificationoftwo pages 6-7) | label-only | Best suited to archaeal thermophiles |
| chromosome / genome | cellular component | heat-sensitive information carrier | Takemata 2024 | (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 4-5) | GO:0005694 chromosome | Useful target node for DNA-protection edges |
| nucleoid / chromatin | cellular component | physical substrate for NAP action | Takemata 2024; Baes 2023 | (takemata2024howdothermophiles pages 4-5, baes2023transcriptionalandtranslational pages 1-2) | GO:0009295 nucleoid | Archaeal chromatin states vary |
| cell wall / peptidoglycan layer | cellular component | structural envelope adaptation | Rekadwad 2023 | (rekadwad2023extremophilesthespecies pages 2-4) | GO:0009273 peptidoglycan-based cell wall | Relevant mainly to bacterial thermophiles |
| thermophilic community in compost | phenotype | ecological assemblage favored by heat | Finore 2023 | (finore2023thermophilicbacteriaand pages 5-7) | label-only | Community-level node; useful for environment graph branches |
| thermophilic industrial biocatalysis | process | application enabled by thermal adaptation | Gallo 2024; Burkhardt 2024 | (gallo2024theundeniablepotential pages 7-8, burkhardt2024miningthermophilesfor pages 1-2) | label-only | Application/context node, not core intrinsic mechanism |
| PET degradation at 60 °C | process | high-temperature plastic depolymerization | Gallo 2024 | (gallo2024theundeniablepotential pages 7-8, gallo2024theundeniablepotential pages 5-7) | label-only | Downstream application; not curate as core trait mechanism unless needed |
| enzyme activity up to 120 °C | phenotype | practical extremozymes performance envelope | Burkhardt 2024 | (burkhardt2024miningthermophilesfor pages 1-2) | label-only | Application-screening statistic, not organism-level mechanism |


*Table: This table lists curation-ready candidate nodes for a thermophilic TraitMech causal graph, grouped by biological and environmental type. It is useful for selecting graph entities before adding evidence-backed edges and ontology grounding.*

---

### Evidence-backed candidate causal edges (triples)
The following table lists proposed subject–predicate–object edges suitable for a TraitMech/TraitGraph representation, including snippets, sources, and grounding suggestions.

| Edge (S–P–O) | Mechanistic category | Evidence snippet (short quote) | Source (first author year, journal) | DOI URL | Publication date | Notes/uncertainty | Suggested ontology grounding |
|---|---|---|---|---|---|---|---|
| Elevated temperature → induces → small heat shock proteins / prefoldin expression | protein | “heat shock induces robust chaperone activity: small HSPs and prefoldin bind denaturing proteins” (baes2023transcriptionalandtranslational pages 1-2) | Baes 2023, mBio | https://doi.org/10.1128/mbio.03593-22 | Oct 2023 | Strong for Sulfolobus acidocaldarius; likely broader in thermophilic archaea but taxon-specific evidence | GO:0009408 heat response; GO:0031072 heat shock protein binding; label-only: prefoldin |
| Small HSPs / prefoldin → deliver substrates to → thermosome (group II chaperonin) | protein | “small HSPs and prefoldin bind denaturing proteins and shuttle them to the HSP60-type group II chaperonin (thermosome)” (baes2023transcriptionalandtranslational pages 1-2) | Baes 2023, mBio | https://doi.org/10.1128/mbio.03593-22 | Oct 2023 | Strong mechanistic edge in Sulfolobales | GO:0044183 protein folding chaperone; GO:0006457 protein folding; label-only: thermosome |
| Thermosome (group II chaperonin) → refolds → denatured proteins | protein | “thermosome, which refolds proteins in an ATP-dependent manner” (baes2023transcriptionalandtranslational pages 1-2) | Baes 2023, mBio | https://doi.org/10.1128/mbio.03593-22 | Oct 2023 | Strong | GO:0006457 protein folding; GO:1903644 regulation of chaperone-mediated protein folding; label-only: thermosome |
| Group II chaperonins HSPα/HSPβ → prevent → protein aggregation/denaturation during thermal stress | protein | “assist in folding nascent proteins and protecting resident proteins during thermal stress” (furr2024structuralstabilitycomparisons pages 1-2) | Furr 2024, Microorganisms | https://doi.org/10.3390/microorganisms12112348 | Nov 2024 | Strong for crenarchaeal HSPα/HSPβ | GO:0006457 protein folding; label-only: HSPα; label-only: HSPβ |
| Elevated temperature / heat shock → increases activity of → reverse gyrase (TopR1) | DNA | “heat shock causes increased positive supercoiling mediated by enhanced reverse gyrase (TopR1) activity” (baes2023transcriptionalandtranslational pages 1-2) | Baes 2023, mBio | https://doi.org/10.1128/mbio.03593-22 | Oct 2023 | Strong for Sulfolobus acidocaldarius heat-shock response | GO:0006265 DNA topological change; label-only: reverse gyrase TopR1 |
| Reverse gyrase → introduces → positive DNA supercoils | DNA | “reverse gyrase introduces positive supercoils” (takemata2024howdothermophiles pages 1-2) | Takemata 2024, Microbes Environ. | https://doi.org/10.1264/jsme2.me23087 | Jun 2024 | Strong, broadly accepted in thermophile genomics | GO:0006265 DNA topological change; EC:5.6.2.2 |
| Positive DNA supercoiling → limits → DNA melting | DNA | “maintain the genome integrity of thermophiles by limiting DNA melting” (takemata2024howdothermophiles pages 1-2) | Takemata 2024, Microbes Environ. | https://doi.org/10.1264/jsme2.me23087 | Jun 2024 | Strong review-level support; mechanism generalized across thermophiles | GO:0006974 DNA damage response; label-only: positive DNA supercoiling |
| Reverse gyrase → mediates → DNA repair / genome integrity maintenance | DNA | “maintain the genome integrity of thermophiles by limiting DNA melting and mediating DNA repair” (takemata2024howdothermophiles pages 1-2) | Takemata 2024, Microbes Environ. | https://doi.org/10.1264/jsme2.me23087 | Jun 2024 | Strong review support, but exact downstream repair routes remain incomplete | GO:0006281 DNA repair; label-only: reverse gyrase |
| Nucleoid-associated proteins (e.g., Alba, Sul7, Cren7, TrmBL2) → alter → DNA organization/compaction during thermal response | DNA | “temperature-responsive DNA organization changes driven by nucleoid-associated proteins” (baes2023transcriptionalandtranslational pages 1-2); “roles for nucleoid-associated proteins (NAPs) ... in shaping thermophile 3D genome architecture” (takemata2024howdothermophiles pages 1-2) | Baes 2023, mBio; Takemata 2024, Microbes Environ. | https://doi.org/10.1128/mbio.03593-22 ; https://doi.org/10.1264/jsme2.me23087 | Oct 2023; Jun 2024 | Moderate: strong concept, but individual NAP effects are taxon-specific | GO:0006325 chromatin organization; label-only: Alba; label-only: Sul7; label-only: Cren7; label-only: TrmBL2 |
| Polyamines → enhance → DNA thermostability / genome stabilization | DNA | “polyamines are noted as ubiquitous positively charged compounds with potential roles in genome thermostability” (takemata2024howdothermophiles pages 4-5) | Takemata 2024, Microbes Environ. | https://doi.org/10.1264/jsme2.me23087 | Jun 2024 | Moderate; phrased as potential role, curate as uncertain | CHEBI:17599 polyamine; GO:1902275 regulation of chromatin organization |
| Ether-linked membrane lipids → confer → greater chemical and thermal stability than ester-linked lipids | membrane | “Ether-linked isoprenoid chains ... confer greater chemical and thermal stability than ester-linked lipids” (chong2024archaeamembranesin pages 1-2) | Chong 2024, Frontiers in Biophysics | https://doi.org/10.3389/frbis.2023.1338019 | Jan 2024 | Strong for archaeal membranes; not universal for bacteria | CHEBI:166828 ether lipid; label-only: archaeal ether-linked isoprenoid lipid |
| Increased cyclopentane ring number in tetraether lipids → increases → membrane condensation/rigidity | membrane | “cyclopentane ring cyclization ... increase membrane condensation, packing tightness, rigidity” (chong2024archaeamembranesin pages 1-2) | Chong 2024, Frontiers in Biophysics | https://doi.org/10.3389/frbis.2023.1338019 | Jan 2024 | Strong; applies especially to archaeal tetraether membranes | label-only: GDGT cyclization; GO:0016042 lipid catabolic process [not ideal, label-only preferred] |
| Higher growth temperature → increases → tetraether lipid cyclization in Sulfolobus acidocaldarius | membrane | “Sulfolobus acidocaldarius increases ring number from 3.4 to 4.8 between 65°C and 82°C” (chong2024archaeamembranesin pages 1-2) | Chong 2024, Frontiers in Biophysics | https://doi.org/10.3389/frbis.2023.1338019 | Jan 2024 | Strong quantitative association; species-specific example | NCBITaxon:2285; label-only: GDGT cyclization |
| GMGT synthase (Gms) → converts → GDGT to GMGT via covalent tail cross-linking | membrane | “Gms (a GMGT synthase that covalently cross-links GDGT hydrocarbon tails to form GMGTs)” (garcia2024identificationoftwo pages 1-2) | Garcia 2024, PNAS | https://doi.org/10.1073/pnas.2318761121 | Jun 2024 | Strong, experimentally validated by heterologous expression | label-only: Gms; label-only: GDGT; label-only: GMGT |
| GMGT methylase (Gmm) → methylates → GMGT hydrocarbon core | membrane | “Gmm (a GMGT methylase that methylates the hydrocarbon core)” (garcia2024identificationoftwo pages 1-2) | Garcia 2024, PNAS | https://doi.org/10.1073/pnas.2318761121 | Jun 2024 | Strong, experimentally validated | label-only: Gmm; label-only: methylated GMGT |
| Elevated growth temperature → increases → GMGT abundance | membrane | “GMGT abundance rises as temperature increases ... production is stimulated between 70–80 °C” (garcia2024identificationoftwo pages 6-7) | Garcia 2024, PNAS | https://doi.org/10.1073/pnas.2318761121 | Jun 2024 | Strong for Archaeoglobus/Vulcanisaeta examples; not universal because some taxa show opposite trend | label-only: GMGT; ENVO:00002009 geothermal feature [environmental context] |
| Elevated growth temperature → increases → GMGT methylation index | membrane | “MI from 0.09 ±0.01 at 85 °C to 0.34 ±0.01 at 99 °C” (garcia2024identificationoftwo pages 6-7) | Garcia 2024, PNAS | https://doi.org/10.1073/pnas.2318761121 | Jun 2024 | Strong quantitative example in V. distributa; taxon-specific | label-only: GMGT methylation index; label-only: methylated GMGT |
| Elevated growth temperature → increases → GMGT cyclization (5–6 rings) | membrane | “V. distributa produces highly cyclized GMGTs with 5–6 rings at 99 °C” (garcia2024identificationoftwo pages 6-7) | Garcia 2024, PNAS | https://doi.org/10.1073/pnas.2318761121 | Jun 2024 | Strong quantitative example; taxon-specific | label-only: cyclized GMGT; NCBITaxon:273116 |
| Gms and Gmm → are → radical SAM enzymes in archaeal lipid modification | membrane | “Gms and Gmm are radical SAM proteins” (garcia2024identificationoftwo pages 6-7); “Gms ... radical SAM enzyme” (li2024biosynthesisofgmgt pages 1-2) | Garcia 2024, PNAS; Li 2024, Nat. Commun. | https://doi.org/10.1073/pnas.2318761121 ; https://doi.org/10.1038/s41467-024-49650-x | Jun 2024; Jun 2024 | Strong | GO:0003676 nucleic acid binding [not specific]; label-only: radical SAM enzyme |
| GrsA/GrsB → catalyze → cyclopentane ring formation in GDGTs | membrane | “GrsA and GrsB ... form cyclopentane rings” (garcia2024identificationoftwo pages 2-2) | Garcia 2024, PNAS | https://doi.org/10.1073/pnas.2318761121 | Jun 2024 | Strong, but edge is for GDGT ring synthesis rather than direct thermophily phenotype | label-only: GrsA; label-only: GrsB; label-only: cyclized GDGT |
| Cell-wall/peptidoglycan composition changes → correlates with → thermal stability | cell wall | “temperature-dependent cell-wall and peptidoglycan changes ... correlate with thermal stability” (rekadwad2023extremophilesthespecies pages 2-4) | Rekadwad 2023, 3 Biotech | https://doi.org/10.1007/s13205-023-03733-6 | Aug 2023 | Moderate; broad review statement, not a single conserved mechanism | GO:0009273 peptidoglycan-based cell wall biogenesis; CHEBI:26115 teichoic acid |
| Thermogenic composting phase (50–80 °C) → selects for → thermophilic bacteria | community/process | “the composting thermogenic phase is reported at 50–80 °C” and “thermophile populations increase while mesophiles decline” (finore2023thermophilicbacteriaand pages 5-7) | Finore 2023, Chem. Biol. Technol. Agric. | https://doi.org/10.1186/s40538-023-00381-z | Jan 2023 | Strong ecological/process edge | ENVO:00002009 compost; METPO:1000616 thermophilic |
| Temperatures >60–70 °C in compost → support metabolic activity of → Bacillus/Thermus/Clostridium thermophiles | community/process | “Bacillus, Thermus and Clostridium ... have metabolic activity above 60 °C” and some “above 70 °C” (finore2023thermophilicbacteriaand pages 5-7) | Finore 2023, Chem. Biol. Technol. Agric. | https://doi.org/10.1186/s40538-023-00381-z | Jan 2023 | Strong for compost-associated taxa; environment-specific | NCBITaxon:1386 Bacillus; NCBITaxon:274 Thermus; NCBITaxon:1485 Clostridium |
| Thermophilic growth → enables → high-temperature industrial biocatalysis / polymer degradation | process | “>60% mass conversion of commercial PET films into soluble monomers within 14 days at 60 °C” (gallo2024theundeniablepotential pages 7-8) | Gallo 2024, Int. J. Mol. Sci. | https://doi.org/10.3390/ijms25147685 | Jul 2024 | Application edge rather than intrinsic mechanism; useful for trait context, not core TraitMech biology | CHEBI:53251 polyethylene terephthalate; label-only: PET hydrolase/LCC; NCBITaxon:1515 Clostridium thermocellum |


*Table: This table lists evidence-backed subject–predicate–object edges for a thermophilic microbial trait causal graph, spanning protein homeostasis, DNA topology and genome protection, membrane lipid adaptations, cell-wall effects, and ecological selection in composting. It is useful as a curation-ready starting point for selecting mechanistic nodes and edges with supporting citations and ontology grounding hints.*

---

### Recent developments and “what’s new” (2023–2024)
1. **Genome organization as a thermophily axis (2024)**: A focused 2024 review frames thermophily in terms of genome integrity under heat, highlighting reverse gyrase, NAPs/histones, SMC proteins, and polyamines as multi-scale genome stabilizers and emphasizing open questions about how these systems interact. (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 4-5)
2. **Mechanistic enzymology of GMGT modifications (2024)**: Identification and validation of **Gms** and **Gmm** as radical SAM enzymes establishes a concrete gene→lipid modification→thermal physiology link for archaeal membranes, and provides a route for ontology-grounded nodes/edges in a causal graph. (garcia2024identificationoftwo pages 1-2, garcia2024identificationoftwo pages 3-4)
3. **Quantified temperature-dependent lipid remodeling (2024, with figure evidence)**: GMGT dominance at high temperature (>90% of monolayer lipids at 90 °C in some cultures) and increased methylation index at higher temperature are reported, alongside highly cyclized GMGTs (5–6 rings) at 99 °C in *Vulcanisaeta distributa*. (garcia2024identificationoftwo pages 6-7, garcia2024identificationoftwo media b2e6804e)

---

### Current applications and real-world implementations (with quantitative data)
Thermophilic traits are exploited for **high-temperature bioprocessing**, where elevated temperatures can improve substrate solubility, reduce contamination risk, and enable thermostable catalysts.

Representative recent quantitative examples:
- **PET depolymerization at 60 °C**: A thermophilic *Clostridium thermocellum* whole-cell system expressing LCC achieved **>60% mass conversion of commercial PET films** into soluble monomers **within 14 days at 60 °C**. (gallo2024theundeniablepotential pages 7-8)
- **Thermophilic plastic degradation consortia**: Thermophilic consortia achieved **75% LDPE** and **60% HDPE degradation** over **120 days at 55 °C** (reported in a 2024 review). (gallo2024theundeniablepotential pages 7-8)
- **Composting thermogenic phase ecology**: Composting commonly features a **thermogenic phase at ~50–80 °C**, with metabolic activity of key thermophilic genera reported **above 60–70 °C** (e.g., *Bacillus*, *Thermus*, *Clostridium*), reflecting a clear temperature-selection implementation in waste processing. (finore2023thermophilicbacteriaand pages 5-7)
- **Extremozyme screening envelope (2024 review)**: Hot-spring thermophiles provide enzymes reported active **up to 120 °C**, with tolerance spanning **pH ~0.1–11**, **salt up to 30%**, and **solvents up to 99%**, illustrating the operational spaces exploited industrially (biocatalysis, polymer degradation, and harsh-reaction chemistry). (burkhardt2024miningthermophilesfor pages 1-2)

---

### Expert synthesis / analysis (authoritative source perspectives)
- A 2024 genome-focused synthesis emphasizes that high temperature increases DNA melting and damage, and positions reverse gyrase and chromatin/nucleoid organization factors as central thermophile solutions, while highlighting gaps in mechanistic integration across scales. (takemata2024howdothermophiles pages 1-2)
- A 2023 mBio study of *S. acidocaldarius* proposes that some thermophilic archaea may use ancient regulatory logic relying on temperature-responsive changes in DNA organization/compaction (NAP-driven) coupled to altered initiation factor recruitment, underscoring that thermophily includes *regulatory architecture* as well as macromolecular stability. (baes2023transcriptionalandtranslational pages 1-2)

---

## Statistics/data suitable for curation notes
- Thermophiles are commonly defined by **TOPT > 45 °C** and assessed via *TMIN/TOPT/TMAX* growth profiling. (lehmann2023adaptivelaboratoryevolution pages 1-2)
- Composting thermogenic phase typically spans **50–80 °C**; thermophilic activity is reported above **60–70 °C** for key genera. (finore2023thermophilicbacteriaand pages 5-7)
- In archaeal culture experiments, GMGTs can represent **>90%** of monolayer lipids at **90 °C**, and methylation index can rise from **0.09 ± 0.01 (85 °C)** to **0.34 ± 0.01 (99 °C)** in *V. distributa*; highly cyclized GMGTs (5–6 rings) occur at **99 °C**. (garcia2024identificationoftwo pages 6-7, garcia2024identificationoftwo media b2e6804e)

---

## Warnings / claims to treat as uncertain (do not curate as universal)
1. **GMGT response direction can be taxon-specific**: While multiple archaeal cultures show increased GMGT with temperature, prior *Pyrococcus furiosus* culture observations include the opposite trend (GMGT decreases with increasing temperature). Encode temperature→GMGT edges as conditional (species/clade-dependent) rather than universal. (li2024biosynthesisofgmgt pages 1-2)
2. **Polyamine roles are stated as “potential”** in the reviewed thermophile genome-organization literature; curate as a candidate node/edge with explicit uncertainty until primary experimental support is added. (takemata2024howdothermophiles pages 4-5)
3. **Preprint-only evidence**: A hot-spring metagenome preprint discusses reverse gyrase indispensability and abundant stress genes; treat as supporting context but prefer peer-reviewed sources for mechanistic edges when possible. (mondal2024aquificaeovercomescompetition pages 28-30)

---

## DOI-first bibliography (URLs and dates)
- Garcia AA et al. **Identification of two archaeal GDGT lipid–modifying proteins reveals diverse microbes capable of GMGT biosynthesis and modification.** *PNAS* (Jun 2024). https://doi.org/10.1073/pnas.2318761121 (garcia2024identificationoftwo pages 6-7, garcia2024identificationoftwo pages 1-2, garcia2024identificationoftwo pages 3-4, garcia2024identificationoftwo media b2e6804e)
- Li Y et al. **Biosynthesis of GMGT lipids by a radical SAM enzyme associated with anaerobic archaea and oxygen-deficient environments.** *Nature Communications* (Jun 2024). https://doi.org/10.1038/s41467-024-49650-x (li2024biosynthesisofgmgt pages 1-2, li2024biosynthesisofgmgt pages 3-4)
- Takemata N. **How Do Thermophiles Organize Their Genomes?** *Microbes and Environments* (Jun 2024). https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 4-5)
- Chong PL-G. **Archaea membranes in response to extreme acidic environments.** *Frontiers in Biophysics* (Jan 2024). https://doi.org/10.3389/frbis.2023.1338019 (chong2024archaeamembranesin pages 1-2)
- Gallo G et al. **The Undeniable Potential of Thermophiles in Industrial Processes.** *International Journal of Molecular Sciences* (Jul 2024). https://doi.org/10.3390/ijms25147685 (gallo2024theundeniablepotential pages 1-3, gallo2024theundeniablepotential pages 7-8, gallo2024theundeniablepotential pages 4-5, gallo2024theundeniablepotential pages 5-7)
- Burkhardt C et al. **Mining thermophiles for biotechnologically relevant enzymes: evaluating the potential of European and Caucasian hot springs.** *Extremophiles* (Nov 2024). https://doi.org/10.1007/s00792-023-01321-3 (burkhardt2024miningthermophilesfor pages 1-2)
- Furr M et al. **Structural Stability Comparisons Between Natural and Engineered Group II Chaperonins…** *Microorganisms* (Nov 2024). https://doi.org/10.3390/microorganisms12112348 (furr2024structuralstabilitycomparisons pages 1-2)
- Baes R et al. **Transcriptional and translational dynamics underlying heat shock response in the thermophilic crenarchaeon Sulfolobus acidocaldarius.** *mBio* (Oct 2023). https://doi.org/10.1128/mbio.03593-22 (baes2023transcriptionalandtranslational pages 1-2)
- Lehmann M et al. **Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.** *Frontiers in Microbiology* (Oct 2023). https://doi.org/10.3389/fmicb.2023.1265216 (lehmann2023adaptivelaboratoryevolution pages 1-2, lehmann2023adaptivelaboratoryevolution pages 2-3)
- Finore I et al. **Thermophilic bacteria and their thermozymes in composting processes: a review.** *Chemical and Biological Technologies in Agriculture* (Jan 2023). https://doi.org/10.1186/s40538-023-00381-z (finore2023thermophilicbacteriaand pages 5-7)
- Rekadwad BN et al. **Extremophiles: the species that evolve and survive under hostile conditions.** *3 Biotech* (Aug 2023). https://doi.org/10.1007/s13205-023-03733-6 (rekadwad2023extremophilesthespecies pages 2-4)
- Mondal N et al. **Aquificae overcomes competition…** *bioRxiv* (Jul 2023). https://doi.org/10.1101/2023.07.10.548480 (preprint) (mondal2024aquificaeovercomescompetition pages 28-30)


References

1. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

2. (gallo2024theundeniablepotential pages 1-3): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 21 citations.

3. (rekadwad2023extremophilesthespecies pages 2-4): Bhagwan Narayan Rekadwad, Wen-Jun Li, Juan M. Gonzalez, Rekha Punchappady Devasya, Arun Ananthapadmanabha Bhagwath, Ruchi Urana, and Khalid Parwez. Extremophiles: the species that evolve and survive under hostile conditions. 3 Biotech, Aug 2023. URL: https://doi.org/10.1007/s13205-023-03733-6, doi:10.1007/s13205-023-03733-6. This article has 49 citations and is from a peer-reviewed journal.

4. (takemata2024howdothermophiles pages 1-2): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.

5. (lehmann2023adaptivelaboratoryevolution pages 2-3): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

6. (baes2023transcriptionalandtranslational pages 1-2): Rani Baes, Felix Grünberger, Sébastien Pyr dit Ruys, Mohea Couturier, Sarah De Keulenaer, Sonja Skevin, Filip Van Nieuwerburgh, Didier Vertommen, Dina Grohmann, Sébastien Ferreira-Cerca, and Eveline Peeters. Transcriptional and translational dynamics underlying heat shock response in the thermophilic crenarchaeon <i>sulfolobus acidocaldarius</i>. Oct 2023. URL: https://doi.org/10.1128/mbio.03593-22, doi:10.1128/mbio.03593-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

7. (furr2024structuralstabilitycomparisons pages 1-2): Mercede Furr, Shadi A. Badiee, Sreenivasulu Basha, Shilpi Agrawal, Zeina Alraawi, Sobroney Heng, Carson Stacy, Yeasin Ahmed, Mahmoud Moradi, Thallapuranam K. S. Kumar, and Ruben Michael Ceballos. Structural stability comparisons between natural and engineered group ii chaperonins: are crenarchaeal “heat shock” proteins also “ph shock” resistant? Microorganisms, 12:2348, Nov 2024. URL: https://doi.org/10.3390/microorganisms12112348, doi:10.3390/microorganisms12112348. This article has 0 citations.

8. (takemata2024howdothermophiles pages 4-5): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.

9. (chong2024archaeamembranesin pages 1-2): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 9 citations.

10. (garcia2024identificationoftwo pages 1-2): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

11. (garcia2024identificationoftwo pages 2-2): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

12. (garcia2024identificationoftwo pages 6-7): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

13. (garcia2024identificationoftwo media b2e6804e): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

14. (li2024biosynthesisofgmgt pages 1-2): Yanan Li, Ting Yu, Xi Feng, Bo Zhao, Huahui Chen, Huan Yang, Xing Chen, Xiao-Hua Zhang, Hayden R. Anderson, Noah Z. Burns, Fuxing Zeng, Lizhi Tao, and Zhirui Zeng. Biosynthesis of gmgt lipids by a radical sam enzyme associated with anaerobic archaea and oxygen-deficient environments. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49650-x, doi:10.1038/s41467-024-49650-x. This article has 21 citations and is from a highest quality peer-reviewed journal.

15. (finore2023thermophilicbacteriaand pages 5-7): Ilaria Finore, Antonio Feola, Ludovica Russo, Andrea Cattaneo, Paola Di Donato, Barbara Nicolaus, Annarita Poli, and Ida Romano. Thermophilic bacteria and their thermozymes in composting processes: a review. Chemical and Biological Technologies in Agriculture, 10:1-22, Jan 2023. URL: https://doi.org/10.1186/s40538-023-00381-z, doi:10.1186/s40538-023-00381-z. This article has 209 citations and is from a peer-reviewed journal.

16. (garcia2024identificationoftwo pages 2-3): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

17. (garcia2024identificationoftwo pages 3-4): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

18. (li2024biosynthesisofgmgt pages 3-4): Yanan Li, Ting Yu, Xi Feng, Bo Zhao, Huahui Chen, Huan Yang, Xing Chen, Xiao-Hua Zhang, Hayden R. Anderson, Noah Z. Burns, Fuxing Zeng, Lizhi Tao, and Zhirui Zeng. Biosynthesis of gmgt lipids by a radical sam enzyme associated with anaerobic archaea and oxygen-deficient environments. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49650-x, doi:10.1038/s41467-024-49650-x. This article has 21 citations and is from a highest quality peer-reviewed journal.

19. (gallo2024theundeniablepotential pages 7-8): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 21 citations.

20. (burkhardt2024miningthermophilesfor pages 1-2): Christin Burkhardt, Leon Baruth, Neele Meyer-Heydecke, Barbara Klippel, Armine Margaryan, Ani Paloyan, Hovik H. Panosyan, and Garabed Antranikian. Mining thermophiles for biotechnologically relevant enzymes: evaluating the potential of european and caucasian hot springs. Extremophiles, Nov 2024. URL: https://doi.org/10.1007/s00792-023-01321-3, doi:10.1007/s00792-023-01321-3. This article has 38 citations and is from a peer-reviewed journal.

21. (gallo2024theundeniablepotential pages 5-7): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 21 citations.

22. (mondal2024aquificaeovercomescompetition pages 28-30): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. BioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.10.548480, doi:10.1101/2023.07.10.548480. This article has 0 citations.

23. (gallo2024theundeniablepotential pages 4-5): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 21 citations.