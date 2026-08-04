---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T00:22:35.557891'
end_time: '2026-06-30T00:44:35.775508'
duration_seconds: 1320.22
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: obligately piezophilic
  trait_identifier: traitmech:000002
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: obligately_piezophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pressure growth preference in which an organism requires elevated
    hydrostatic pressure for growth and is unable to grow at atmospheric pressure
    (0.1 MPa).
  parent_traits: traitmech:000001
  synonyms: obligate piezophile
  evidence_summary: 'DOI:10.1038/srep27289: High hydrostatic pressure adaptive strategies
    in an obligate piezophile Pyrococcus yayanosii (Organism example: Pyrococcus yayanosii
    is an obligate piezophile that requires high hydrostatic pressure for growth.)
    | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at
    6 degrees C (Organism example: Colwellia marinimaniae MTCD1 grows only at high
    pressure (80-140 MPa) and does not grow near atmospheric pressure.)'
  causal_graph_summary: 'obligate_piezophily_high_pressure_requirement: 6 nodes, 6
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately piezophilic
- **METPO identifier:** traitmech:000002
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure growth preference in which an organism requires elevated hydrostatic pressure for growth and is unable to grow at atmospheric pressure (0.1 MPa).
- **Parent traits:** traitmech:000001
- **Synonyms:** obligate piezophile
- **Existing evidence:** DOI:10.1038/srep27289: High hydrostatic pressure adaptive strategies in an obligate piezophile Pyrococcus yayanosii (Organism example: Pyrococcus yayanosii is an obligate piezophile that requires high hydrostatic pressure for growth.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Organism example: Colwellia marinimaniae MTCD1 grows only at high pressure (80-140 MPa) and does not grow near atmospheric pressure.)
- **Existing causal graph summary:** obligate_piezophily_high_pressure_requirement: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **obligately piezophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_piezophilic.yaml`.

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
- **Trait label:** obligately piezophilic
- **METPO identifier:** traitmech:000002
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure growth preference in which an organism requires elevated hydrostatic pressure for growth and is unable to grow at atmospheric pressure (0.1 MPa).
- **Parent traits:** traitmech:000001
- **Synonyms:** obligate piezophile
- **Existing evidence:** DOI:10.1038/srep27289: High hydrostatic pressure adaptive strategies in an obligate piezophile Pyrococcus yayanosii (Organism example: Pyrococcus yayanosii is an obligate piezophile that requires high hydrostatic pressure for growth.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Organism example: Colwellia marinimaniae MTCD1 grows only at high pressure (80-140 MPa) and does not grow near atmospheric pressure.)
- **Existing causal graph summary:** obligate_piezophily_high_pressure_requirement: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **obligately piezophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_piezophilic.yaml`.

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


# Obligately Piezophilic Trait: Curation-Focused Research Report

**Trait:** obligately piezophilic (traitmech:000002)
**Category:** ENVIRONMENT | **Kind:** CLASS | **Status:** REVIEWED
**Definition:** A pressure growth preference in which an organism requires elevated hydrostatic pressure for growth and is unable to grow at atmospheric pressure (0.1 MPa).

---

## 1. Trait Scope Summary

Obligate piezophily (synonym: obligate piezophile, also termed hyperpiezophily) defines microorganisms that cannot grow at atmospheric pressure (0.1 MPa) and require elevated hydrostatic pressure (HHP) for cellular growth and division (scoma2021functionalgroupsin pages 1-2). This trait is distinguished from related categories along a pressure-preference continuum: *piezosensitive* organisms grow best at atmospheric pressure and are inhibited by HHP; *piezotolerant* organisms tolerate moderate HHP but grow optimally near atmospheric pressure; *facultative piezophiles* grow optimally above atmospheric pressure but can still grow at 0.1 MPa; and *obligate piezophiles* are absolutely unable to grow at 0.1 MPa (scoma2021functionalgroupsin pages 1-2, scoma2021functionalgroupsin pages 6-7).

Scoma (2021) proposed updated functional group definitions that subdivide piezophiles by temperature preference: piezopsychrophiles (T_opt ≤15°C), piezomesophiles (16 < T_opt < 49°C), and piezothermophiles (T_opt ≥50°C), reflecting the important cross-stress interplay between pressure and temperature (scoma2021functionalgroupsin pages 1-2, scoma2021functionalgroupsin pages 2-3). Competitive advantage of piezophiles over piezosensitive organisms consistently appears at pressures ≥20 MPa (scoma2021functionalgroupsin pages 6-7, scoma2021functionalgroupsin pages 5-6).

**Key model organisms for obligate piezophily:**
- *Pyrococcus yayanosii* CH1 — the only known obligate piezophilic hyperthermophilic archaeon, isolated from the Ashadze hydrothermal vent at 4,100 m depth, with optimal growth at 52 MPa and 98°C (michoud2016highhydrostaticpressure pages 1-2, michoud2016highhydrostaticpressure pages 2-3).
- *Colwellia marinimaniae* MTCD1 — a psychrophilic obligate piezophile with optimal growth at 120 MPa and 6°C, growth range 80–140 MPa; represents the most pressure-adapted bacterium known (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7).
- *Shewanella benthica* DB21MT-2/KT99 — obligately piezophilic bacteria isolated from hadal sediments, with well-studied respiratory chain adaptations (oger2010themanyways pages 5-6, peoples2020distinctivegeneand pages 5-7).

**Boundary cases:** The distinction between obligate and extreme facultative piezophily can be blurred by experimental conditions (temperature, media composition). Some organisms classified as obligate piezophiles may show marginal growth near atmospheric pressure under specific conditions. The inability to grow at 0.1 MPa must be confirmed under optimized conditions for all other variables.

---

## 2. Candidate Causal Graph Nodes

The following table lists candidate nodes grouped by type, with suggested ontology groundings where available.

| Node group | Node name | Type | Suggested CURIE | Brief description | Evidence |
|---|---|---|---|---|---|
| Environmental factor | high hydrostatic pressure (HHP) | environmental factor | ENVO:01000220 | Elevated pressure required for growth in obligate piezophiles; central external driver shaping membrane, protein, and respiratory adaptations. | (scoma2021functionalgroupsin pages 1-2, scoma2021functionalgroupsin pages 6-7) |
| Environmental factor | deep-sea hydrothermal vent | environmental factor | ENVO:01000017 | High-pressure seafloor vent habitat associated with hyperthermophilic obligate piezophiles such as *Pyrococcus yayanosii*. | (michoud2016highhydrostaticpressure pages 1-2, scoma2021functionalgroupsin pages 1-2) |
| Environmental factor | hadal trench | environmental factor | ENVO:01000020 | Extreme deep-ocean trench habitat selecting for psychrophilic obligate piezophiles such as hadal *Colwellia* and *Shewanella*. | (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9) |
| Gene/gene cluster | pfaABCD | gene cluster | label-only candidate | Polyunsaturated fatty acid synthase gene cluster for omega-3 PUFA production; supports membrane adaptation under pressure. | (tamby2023microbialmembranelipid pages 2-4, scheffer2023themysteryof pages 6-7) |
| Gene/gene cluster | nuoABCEFGHIJKLMN | gene cluster | KEGG:map00190 | NADH dehydrogenase I operon found in hadal piezophilic *Colwellia* but absent from piezosensitive comparators. | (peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 7-9) |
| Gene | ompH | gene | label-only candidate | Encodes pressure-responsive outer membrane porin upregulated under pressure in piezophilic bacteria. | (scheffer2023themysteryof pages 6-7, scheffer2023themysteryof pages 7-9) |
| Gene | toxR | gene | label-only candidate | Regulatory gene controlling ompH expression in pressure-responsive membrane adaptation. | (scheffer2023themysteryof pages 6-7) |
| Gene | delta-9 acyl-phospholipid desaturase | gene | EC:1.14.19.- | Introduces double bonds into phospholipid acyl chains, increasing membrane unsaturation in piezophilic *Colwellia*. | (scheffer2023themysteryof pages 6-7, peoples2020distinctivegeneand pages 5-7) |
| Gene/gene cluster | nqrABCDEF | gene cluster | KEGG:K05574 | Na+-translocating NADH:quinone reductase respiratory complex present across compared *Colwellia* strains. | (peoples2020distinctivegeneand pages 5-7) |
| Gene/gene cluster | rnfABCDGE | gene cluster | KEGG:K03616 | Membrane electron-transfer/ion-translocating complex used in *Colwellia* respiration. | (peoples2020distinctivegeneand pages 5-7) |
| Gene | ddl (d-alanine-D-alanine ligase) | gene | EC:6.3.2.4 | Piezophile-enriched peptidoglycan biosynthesis gene; extra copies found in piezophilic *Colwellia*. | (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9) |
| Gene | ald (alanine dehydrogenase) | gene | EC:1.4.1.1 | Candidate piezophile-specific gene implicated in pyruvate/alanine interconversion and NADH/NAD+ homeostasis. | (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9) |
| Gene/gene cluster | mbh/mbx hydrogenases | gene cluster | label-only candidate | Membrane-bound hydrogenase systems linked to ferredoxin oxidation, H2 formation, and energy conservation in Thermococcales. | (michoud2016highhydrostaticpressure pages 2-3, scheffer2023themysteryof pages 7-9) |
| Gene set | chemotaxis genes | gene set | GO:0006935 | Pressure-responsive motility/signaling genes upregulated in *P. yayanosii* under nonoptimal pressures. | (michoud2016highhydrostaticpressure pages 1-2, michoud2016highhydrostaticpressure pages 3-4) |
| Gene/gene cluster | CRISPR-Cas clusters | gene cluster | GO:0099048 | Defense-associated loci overrepresented or pressure-responsive in *P. yayanosii*; possible stress-linked regulatory role. | (michoud2016highhydrostaticpressure pages 1-2, michoud2016highhydrostaticpressure pages 4-6) |
| Gene/gene cluster | V-ATPase genes | gene cluster | GO:0015992 | Archaeal ATPase genes upregulated at high pressure in *P. yayanosii*, likely helping ion/proton homeostasis. | (michoud2016highhydrostaticpressure pages 2-3, michoud2016highhydrostaticpressure pages 4-6) |
| Protein/enzyme | PUFA synthase | protein complex | label-only candidate | Enzyme complex producing long-chain omega-3 PUFAs such as EPA/DHA for membrane adaptation. | (tamby2023microbialmembranelipid pages 2-4, scheffer2023themysteryof pages 6-7) |
| Protein/enzyme | NADH dehydrogenase I (Nuo) | protein complex | EC:7.1.1.2 | Proton-translocating respiratory complex enriched in hadal piezophilic *Colwellia*. | (peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 7-9) |
| Protein/enzyme | Na+-NQR complex | protein complex | EC:7.2.1.1 | Sodium-translocating respiratory enzyme complex contributing to energy metabolism in *Colwellia*. | (peoples2020distinctivegeneand pages 5-7) |
| Protein | OmpH porin | protein | label-only candidate | Pressure-induced outer membrane porin implicated in nutrient transport and pressure-resistant membrane function. | (scheffer2023themysteryof pages 6-7, scheffer2023themysteryof pages 7-9) |
| Protein/enzyme | quinol oxidase | protein complex | EC:7.1.1.- | High-pressure terminal oxidase used in pressure-dependent respiratory chain switching in *Shewanella*. | (oger2010themanyways pages 5-6, scheffer2023themysteryof pages 7-9) |
| Protein/enzyme | cytochrome c oxidase | protein complex | EC:7.1.1.9 | Low-pressure terminal oxidase replaced by quinol oxidase under high pressure in some piezophilic *Shewanella*. | (oger2010themanyways pages 5-6) |
| Protein/enzyme | cytochrome bd complex | protein complex | EC:7.1.1.- | Pressure-regulated terminal oxidase component detected in high-pressure respiratory remodeling. | (oger2010themanyways pages 5-6) |
| Protein | ToxR regulator | protein | label-only candidate | Transcriptional regulator controlling ompH and associated membrane-pressure response. | (scheffer2023themysteryof pages 6-7) |
| Protein/enzyme | formate dehydrogenase | protein/enzyme | EC:1.17.1.9 | Enzyme in formate metabolism coupled to hydrogen metabolism; pathway downregulated under pressure stress in *P. yayanosii*. | (michoud2016highhydrostaticpressure pages 4-6, scheffer2023themysteryof pages 7-9) |
| Protein/enzyme | membrane-bound [NiFe] hydrogenases | protein complex | EC:1.12.7.2 | Pressure-responsive hydrogenases involved in H2 metabolism and membrane energy conservation in Thermococcales. | (michoud2016highhydrostaticpressure pages 2-3, scheffer2023themysteryof pages 7-9) |
| Protein/enzyme | V-ATPase | protein complex | EC:7.2.2.1 | Ion-translocating ATPase implicated in pH balance and energetic adjustment at high pressure. | (michoud2016highhydrostaticpressure pages 2-3, michoud2016highhydrostaticpressure pages 4-6) |
| Protein/enzyme | SAM-dependent methyltransferase | protein/enzyme | pfam:PF13659 | Piezophile-biased enzyme candidate, possibly linked to tRNA modification and deep-sea adaptation. | (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9) |
| Protein/enzyme | superoxide dismutase | protein/enzyme | EC:1.15.1.1 | Oxidative stress defense enzyme commonly retained in piezophilic and piezosensitive deep-sea bacteria. | (peoples2020distinctivegeneand pages 7-9) |
| Chemical/metabolite | unsaturated fatty acids (MUFA, PUFA) | chemical class | CHEBI:32395 | Increased membrane unsaturation counteracts pressure-induced membrane ordering and rigidity. | (oger2010themanyways pages 4-5, tamby2023microbialmembranelipid pages 2-4) |
| Chemical/metabolite | eicosapentaenoic acid (EPA; C20:5) | chemical | CHEBI:25414 | Long-chain omega-3 PUFA associated with high-pressure membrane adaptation and cell division support. | (tamby2023microbialmembranelipid pages 2-4, tamby2023microbialmembranelipid pages 10-11) |
| Chemical/metabolite | docosahexaenoic acid (DHA; C22:6) | chemical | CHEBI:28125 | Long-chain omega-3 PUFA frequently associated with pressure-adapted membranes, though not universal. | (tamby2023microbialmembranelipid pages 2-4) |
| Chemical/metabolite | branched-chain fatty acids | chemical class | CHEBI:35819 | Membrane lipids that can increase fluidity under pressure in some taxa; not universal among piezophiles. | (tamby2023microbialmembranelipid pages 6-7, tamby2023microbialmembranelipid pages 1-2) |
| Chemical/metabolite | phosphatidylglycerides | chemical class | CHEBI:17517 | Phospholipid headgroup class reported to increase under high pressure in some piezophiles. | (scheffer2023themysteryof pages 9-10) |
| Chemical/metabolite | phosphatidylethanolamine | chemical class | CHEBI:16038 | Major membrane phospholipid class whose relative abundance can shift during high-pressure adaptation. | (scheffer2023themysteryof pages 9-10) |
| Chemical/metabolite | trimethylamine N-oxide (TMAO) | chemical | CHEBI:15724 | Acts as piezolyte and, in some taxa, respiratory substrate; protects proteins from pressure-induced water intrusion. | (scheffer2023themysteryof pages 9-10, yancey2020cellularresponsesin pages 9-11) |
| Chemical/metabolite | mannosyl-glycerate | chemical | CHEBI:63863 | Compatible solute in Thermococcales; accumulates under low-pressure stress and rigidifies proteins. | (scheffer2023themysteryof pages 9-10, cario2016molecularchaperoneaccumulation pages 4-5) |
| Chemical/metabolite | beta-hydroxybutyrate | chemical | CHEBI:15978 | Pressure-associated compatible solute reported in piezophilic systems. | (scheffer2023themysteryof pages 9-10, scheffer2023themysteryof pages 7-9) |
| Chemical/metabolite | glutamate | chemical | CHEBI:29985 | Common compatible solute/piezolyte contributing to preferential hydration and stress protection. | (scheffer2023themysteryof pages 9-10, scheffer2023themysteryof pages 7-9) |
| Chemical/metabolite | betaine | chemical | CHEBI:17750 | Compatible solute detected under high-pressure growth; contributes to protein protection. | (scheffer2023themysteryof pages 9-10, scheffer2023themysteryof pages 7-9) |
| Chemical/metabolite | formate | chemical | CHEBI:15740 | Central metabolite in Thermococcales formate/hydrogen metabolism affected by pressure. | (michoud2016highhydrostaticpressure pages 4-6, scheffer2023themysteryof pages 7-9) |
| Biological process | membrane fluidity maintenance | biological process | GO:0016042 | Adaptive remodeling of membrane lipids to preserve membrane function under compression. | (oger2010themanyways pages 4-5, tamby2023microbialmembranelipid pages 2-4) |
| Biological process | pressure-dependent respiratory chain regulation | biological process | label-only candidate | Switching among respiratory complexes and terminal oxidases as a function of growth pressure. | (oger2010themanyways pages 5-6, scheffer2023themysteryof pages 7-9) |
| Biological process | protein folding under pressure | biological process | GO:0006457 | Chaperone-assisted maintenance of protein structure/function under pressure stress. | (oger2010themanyways pages 2-4, oger2010themanyways pages 6-8) |
| Biological process | piezolyte accumulation | biological process | label-only candidate | Intracellular accumulation of compatible solutes that stabilize proteins by preferential hydration. | (scheffer2023themysteryof pages 9-10, scheffer2023themysteryof pages 7-9) |
| Biological process | chemotaxis | biological process | GO:0006935 | Directed motility/signaling response upregulated in *P. yayanosii* under suboptimal pressures. | (michoud2016highhydrostaticpressure pages 1-2, michoud2016highhydrostaticpressure pages 3-4) |
| Biological process | peptidoglycan biosynthesis | biological process | GO:0009252 | Cell wall strengthening/remodeling process linked to piezophile-enriched ddl genes. | (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9) |
| Biological process | DNA replication/repair | biological process | GO:0006260 / GO:0006281 | Replication and repair functions enriched or pressure-responsive in obligate piezophiles. | (peoples2020distinctivegeneand pages 1-2, michoud2016highhydrostaticpressure pages 4-6) |
| Molecular function | fatty acid desaturation | molecular function | GO:0004768 | Introduction of double bonds into fatty acyl chains to increase membrane fluidity under pressure. | (scheffer2023themysteryof pages 6-7, peoples2020distinctivegeneand pages 5-7) |
| Molecular function | NADH oxidation | molecular function | GO:0003954 | Electron transfer from NADH into respiratory chains via Nuo or Na+-NQR complexes. | (oger2010themanyways pages 5-6, peoples2020distinctivegeneand pages 5-7) |
| Molecular function | proton gradient generation | molecular function | GO:0015992 | Energy-conserving ion translocation by respiratory complexes, hydrogenases, and V-ATPase. | (michoud2016highhydrostaticpressure pages 2-3, oger2010themanyways pages 5-6) |
| Molecular function | compatible solute transport/protection | molecular function | label-only candidate | Functional contribution of piezolytes and associated systems to protein stabilization under pressure. | (scheffer2023themysteryof pages 9-10, yancey2020cellularresponsesin pages 9-11) |
| Molecular function | amino acid substitution pattern favoring basic/hydrophobic residues | molecular function | label-only candidate | Proteome-level compositional bias in obligate piezophiles that may stabilize proteins and modulate hydration/compressibility. | (scheffer2023themysteryof pages 10-12, peoples2020distinctivegeneand pages 5-7) |


*Table: This table lists candidate causal graph nodes for obligate piezophily, grouped by entity type and grounded to stable identifiers where possible. It is useful for TraitMech curation because it maps reported pressure-adaptation mechanisms to concrete graph-ready nodes with supporting evidence.*

---

## 3. Mechanistic Details Supporting Causal Edges

### 3.1 Membrane Lipid Adaptations

High hydrostatic pressure compresses lipid bilayers, decreasing membrane fluidity and permeability through altered lipid packing and conformational changes (oger2010themanyways pages 2-4, oger2010themanyways pages 4-5). Obligate piezophiles counteract this by increasing the proportion of mono- and polyunsaturated fatty acids in their membrane phospholipids, which introduces kinks in acyl chains and increases membrane disorder (oger2010themanyways pages 4-5, tamby2023microbialmembranelipid pages 2-4). A positive correlation exists between unsaturated fatty acid content and the depth of organism isolation (oger2010themanyways pages 4-5). Key biosynthetic components include the *pfaABCD* operon encoding the polyunsaturated fatty acid (PUFA) synthase complex for EPA and DHA production, present in all compared Colwellia strains (peoples2020distinctivegeneand pages 5-7), and the delta-9 acyl-phospholipid desaturase gene found specifically in piezophilic Colwellia, which introduces double bonds directly into membrane phospholipid saturated fatty acids (peoples2020distinctivegeneand pages 5-7, scheffer2023themysteryof pages 6-7). Notably, piezosensitive Colwellia possess a fatty acid cis/trans isomerase absent in piezophilic strains, suggesting different membrane regulation strategies (peoples2020distinctivegeneand pages 5-7). Branched-chain fatty acids (iso and anteiso forms) also contribute to membrane fluidity in some taxa but are not universal among piezophiles (tamby2023microbialmembranelipid pages 6-7, tamby2023microbialmembranelipid pages 1-2). Phospholipid headgroup composition, including shifts in phosphatidylglycerides and phosphatidylethanolamine ratios, may also be relevant but remains less well characterized (scheffer2023themysteryof pages 9-10, tamby2023microbialmembranelipid pages 6-7).

### 3.2 Respiratory Chain Remodeling

Piezophilic Shewanella species exhibit a striking pressure-dependent switch in respiratory chain components. At low pressure (0.1 MPa), the respiratory chain consists of NADH dehydrogenase, the bc1 complex, and terminal cytochrome c oxidase. At high pressure (28–70 MPa), the system switches to NADH dehydrogenase with membrane-bound cytochrome c-551 and quinol oxidase as the terminal oxidase (oger2010themanyways pages 5-6, scheffer2023themysteryof pages 7-9). Additionally, a cytochrome bd complex is expressed specifically under HHP conditions (oger2010themanyways pages 5-6). In piezophilic Colwellia, the NADH dehydrogenase I complex (nuoABCEFGHIJKLMN) is present only in the three hadal piezophilic strains and is absent from piezosensitive counterparts, while both groups utilize the rnf and Na+-NQR respiratory complexes (peoples2020distinctivegeneand pages 5-7). Alanine dehydrogenase genes, found specifically in piezophilic Colwellia, maintain NADH/NAD+ homeostasis under pressure (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9).

### 3.3 Protein and Proteome Adaptations

Obligate piezophiles display systematic proteome-level adaptations. Piezophilic Colwellia exhibit a more basic and hydrophobic proteome, enriched in tryptophan, tyrosine, leucine, phenylalanine, histidine, and methionine, which may help maintain protein structure by preventing water intrusion at high pressure (scheffer2023themysteryof pages 10-12, peoples2020distinctivegeneand pages 9-11, peoples2020distinctivegeneand pages 5-7). In archaeal piezophiles such as *Pyrococcus* species, amino acid composition shifts toward smaller residues (serine, glycine, valine, aspartic acid) with decreased tyrosine and glutamine (scheffer2023themysteryof pages 10-12, scheffer2023themysteryof pages 9-10). *P. yayanosii* has lost aromatic amino acid biosynthesis pathways including tryptophan synthesis, suggesting that de novo synthesis is energetically unfavorable under HHP (michoud2016highhydrostaticpressure pages 2-3, scheffer2023themysteryof pages 9-10).

Structural adaptations include increased internal cavity volumes in piezophilic enzymes (e.g., DHFR: 340 Å vs. 270 Å in non-piezophiles), providing greater compressibility (scheffer2023themysteryof pages 10-12, huang2016amolecularperspective pages 9-11). Piezophilic proteins exhibit greater flexibility at atmospheric pressure and lower stability, with catalytic activity rates 4–5 times higher than mesophilic counterparts to compensate for pressure-induced reductions (scheffer2023themysteryof pages 10-12, huang2016amolecularperspective pages 9-11). Makhatadze (2024) proposed that modulation of electrostatic interactions between charged residues represents a "cryptic" evolutionary mechanism for pressure adaptation across the Colwellia proteome (makhatadze2024modulationofelectrostatic pages 6-8, makhatadze2024modulationofelectrostatic pages 1-3). When piezophilic proteins are expressed at atmospheric pressure, they require chaperone assistance (DnaK, DnaJ, GroEL, HtpG), confirming their structural optimization for high-pressure conditions (oger2010themanyways pages 6-8).

### 3.4 Compatible Solutes and Piezolytes

Piezolytes are small organic molecules that protect proteins from pressure-induced denaturation through preferential hydration, displacing water molecules that would otherwise penetrate protein interiors (scheffer2023themysteryof pages 9-10, scheffer2023themysteryof pages 7-9). Key piezolytes include glutamate, betaine, and β-hydroxybutyrate, which accumulate in pressure-dependent fashion in *Photobacterium profundum* (scheffer2023themysteryof pages 9-10, scheffer2023themysteryof pages 7-9). TMAO (trimethylamine N-oxide) ranks as the most potent piezolyte, binding water molecules to prevent pressure-induced crowding around nonpolar protein surfaces (yancey2020cellularresponsesin pages 9-11). In the piezophilic archaeon *Thermococcus barophilus*, mannosyl-glycerate (MG) accumulates under low-pressure (suboptimal) conditions, increasing protein rigidity to compensate for excessive flexibility of the pressure-adapted proteome at atmospheric pressure; MG accumulation is reduced at supra-optimal pressures, confirming the structural adaptation of the proteome to HHP (cario2016molecularchaperoneaccumulation pages 4-5).

### 3.5 Energy Metabolism in *P. yayanosii*

Multi-omics analyses of *P. yayanosii* revealed that energy metabolism genes, including ATP/ADP synthase (V-ATPase), hydrogenases, and ferredoxin oxidoreductases, are constitutively highly expressed compared to non-obligate piezophilic *Pyrococcus* species (michoud2016highhydrostaticpressure pages 2-3). Under pressure stress (both sub- and supra-optimal), chemotaxis pathway genes are upregulated to enhance motility and nutrient searching, while hydrogenase and formate metabolism genes are downregulated (michoud2016highhydrostaticpressure pages 3-4, michoud2016highhydrostaticpressure pages 4-6, scheffer2023themysteryof pages 7-9). V-ATPase genes are upregulated at 80 MPa to regulate intracellular pH (michoud2016highhydrostaticpressure pages 4-6). The Mbx hydrogenase cluster and associated NSR and Pdo proteins suggest a pressure-induced energetic shift, while DNA replication genes including a bipolar DNA helicase and rad50 ATPase are translationally upregulated under high pressure stress (michoud2016highhydrostaticpressure pages 4-6). The organism possesses an overrepresented CRISPR-Cas system with two of four clusters unique to *P. yayanosii*, with differential regulation under pressure (michoud2016highhydrostaticpressure pages 2-3, michoud2016highhydrostaticpressure pages 4-6).

### 3.6 Cell Wall and Outer Membrane Adaptations

Piezophilic Colwellia carry extra copies of d-alanine-d-alanine ligase (EC 6.3.2.4), implicated in peptidoglycan biosynthesis and cell wall strengthening under pressure (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9). The outer membrane protein OmpH, regulated by the ToxR regulon, increases 10- to 100-fold under elevated pressure to enable transport of amino acids and sugars through the compressed membrane (scheffer2023themysteryof pages 6-7, scheffer2023themysteryof pages 7-9). A tad pilus operon for adhesion is found only in piezophilic Colwellia, alongside enriched glycosyltransferases for extracellular polysaccharide synthesis (peoples2020distinctivegeneand pages 5-7). Many piezophile-specific genes are located near genomic islands and transposases, strongly suggesting horizontal gene transfer as a mechanism for acquisition of deep-sea adaptations (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9).

---

## 4. Candidate Causal Edges

The following table presents evidence-backed causal edges as subject-predicate-object triples, with DOI references, supporting quotes, and confidence assessments.

| Subject | Predicate | Object | Reference (DOI) | Supporting snippet / quote | Notes | Confidence |
|---|---|---|---|---|---|---|
| high_hydrostatic_pressure | requires | obligate_piezophily | 10.1038/s41396-021-00930-0 | "Obligate piezophiles (or hyperpiezophiles) cannot grow at ambient pressure" (scoma2021functionalgroupsin pages 1-2) | Defining scope edge for the trait; maps trait to inability to grow at 0.1 MPa. | high |
| high_hydrostatic_pressure | decreases | membrane_fluidity | 10.1016/j.resmic.2010.09.017 | "lipid membranes... lose fluidity and permeability through altered lipid packing" under HHP (oger2010themanyways pages 2-4, oger2010themanyways pages 4-5) | General mechanistic pressure effect; broad across piezophile literature. | high |
| unsaturated_fatty_acids | increases | membrane_fluidity | 10.1016/j.resmic.2010.09.017 | "monounsaturated and polyunsaturated fatty acids... increase membrane fluidity and reduce pressure-dependent lipid packing" (oger2010themanyways pages 5-6, oger2010themanyways pages 4-5) | Strong comparative support across bacterial piezophiles. | high |
| pfaABCD_operon | produces | PUFA | 10.3389/fmolb.2022.1058381 | "all contain pfaABCD to produce polyunsaturated fatty acids" (tamby2023microbialmembranelipid pages 2-4, peoples2020distinctivegeneand pages 5-7) | Well supported for Colwellia and broader deep-sea bacteria; EPA/DHA may vary by taxon. | high |
| delta-9_desaturase | produces | unsaturated_fatty_acids | 10.1186/s12864-020-07102-y | "delta-9 acyl-phospholipid desaturase... promoting unsaturated fatty acid synthesis by introducing double bonds directly into membrane phospholipid saturated fatty acids" (peoples2020distinctivegeneand pages 5-7) | Direct gene-to-product mechanism. | high |
| membrane_fluidity_maintenance | enables | obligate_piezophily | 10.3389/fmolb.2022.1058381 | "Piezophiles... maintain membrane integrity through key adaptive strategies" and increased unsaturated/branched lipids (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 2-4) | Integrative process-level edge; mechanistically strong but not demonstrated as singly sufficient. | medium |
| high_hydrostatic_pressure | upregulates | ompH | 10.3390/microorganisms11071629 | "outer membrane protein OmpH... increases 10-100 fold under high pressure" (scheffer2023themysteryof pages 6-7, scheffer2023themysteryof pages 7-9) | Derived from piezophilic bacterial studies; likely taxon-specific. | medium |
| toxR | regulates | ompH | 10.3390/microorganisms11071629 | "ompH gene is regulated by the toxR regulon" (scheffer2023themysteryof pages 6-7) | Regulatory edge reported in review from primary studies. | medium |
| nuo_operon | enables | piezophilic_respiration | 10.1186/s12864-020-07102-y | "the NADH dehydrogenase I complex (nuoABCEF-GHIJKLMN) is only present in the three hadal piezophiles" (peoples2020distinctivegeneand pages 5-7) | Presence/absence suggests role in hadal piezophilic respiration; causality inferred, not experimentally validated. | medium |
| high_hydrostatic_pressure | switches | respiratory_chain | 10.1016/j.resmic.2010.09.017 | "At low pressure... cytochrome c oxidase. At high pressure... membrane-bound cytochrome c-551 and quinol oxidase" (oger2010themanyways pages 5-6) | Classic Shewanella pressure-dependent respiratory remodeling. | high |
| quinol_oxidase | replaces | cytochrome_c_oxidase | 10.1016/j.resmic.2010.09.017 | "At low pressure (0.1 MPa)... terminal cytochrome c oxidase. At high pressure (28-70 MPa)... quinol oxidase as the terminal oxidase" (oger2010themanyways pages 5-6) | Strong within Shewanella; not universal to all obligate piezophiles. | high |
| piezolytes | protects | proteins | 10.3390/microorganisms11071629 | "These compatible solutes function through a mechanism called 'preferential hydration'... displace water molecules bound to proteins" (scheffer2023themysteryof pages 9-10, scheffer2023themysteryof pages 7-9) | Strong general mechanism. | high |
| TMAO | counteracts | pressure_denaturation | 10.1002/jez.2354 | "TMAO... prevents hydrostatic pressure-induced crowding of water around nonpolar protein regions and blocks water penetration into protein interiors" (yancey2020cellularresponsesin pages 9-11) | Strong piezolyte mechanism; much evidence from animals but also cited for microbes. | medium |
| mannosyl-glycerate | stabilizes | proteome | 10.1038/srep29483 | "MG accumulation increases protein rigidity" and low pressure is perceived as stress in T. barophilus (cario2016molecularchaperoneaccumulation pages 4-5) | Strong for Thermococcales, especially archaeal piezophiles. | high |
| high_hydrostatic_pressure | upregulates | chemotaxis_genes | 10.1038/srep27289 | "chemotaxis pathway genes are upregulated" under stressful pressure conditions in P. yayanosii (michoud2016highhydrostaticpressure pages 3-4) | Directly supported in obligate piezophile P. yayanosii. | high |
| high_hydrostatic_pressure | upregulates | V-ATPase | 10.1038/srep27289 | "V-ATPase genes (PYCH_15710–60) are upregulated at 80 MPa" (michoud2016highhydrostaticpressure pages 4-6) | Directly supported in P. yayanosii. | high |
| mbh/mbx_hydrogenases | generates | proton_gradient | 10.1038/srep27289 | "mbh and mbx hydrogenases enable respiration by creating proton gradients across the membrane through electron acceptance from ferredoxin" (scheffer2023themysteryof pages 7-9, michoud2016highhydrostaticpressure pages 2-3) | Strong for Thermococcales energy metabolism. | high |
| formate_metabolism | downregulated_at | suboptimal_pressure | 10.1038/srep27289 | "The formate metabolism cluster shows downregulation at both low and high pressure" (michoud2016highhydrostaticpressure pages 4-6) | Specific to pressure stress relative to optimum in P. yayanosii. | high |
| amino_acid_composition_bias | enables | protein_pressure_stability | 10.3390/microorganisms11071629 | "more basic proteins and enriched hydrophobic residues... help maintain protein structure against water penetration at high pressure" (scheffer2023themysteryof pages 10-12, peoples2020distinctivegeneand pages 9-11) | Comparative/proteome-level inference across Colwellia and other piezophiles. | medium |
| loss_of_aromatic_AA_biosynthesis | associated_with | obligate_piezophily | 10.1038/srep27289 | "A notable adaptation is the loss of aromatic amino acid biosynthesis pathways" in P. yayanosii (michoud2016highhydrostaticpressure pages 2-3, scheffer2023themysteryof pages 9-10) | Association is strong in P. yayanosii but likely not universal; avoid overgeneralization. | medium |
| d-alanine-d-alanine_ligase | strengthens | peptidoglycan | 10.1186/s12864-020-07102-y | "d-alanine-d-alanine ligase... may be involved in peptidoglycan synthesis" (peoples2020distinctivegeneand pages 7-9) | Functional direction is biologically standard, but specific contribution to pressure adaptation is inferred. | medium |
| alanine_dehydrogenase | maintains | NADH/NAD+_homeostasis | 10.1186/s12864-020-07102-y | "alanine dehydrogenase for NADH/NAD+ homeostasis" (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9) | Strong comparative support from piezophilic Colwellia genomics. | high |
| horizontal_gene_transfer | facilitates | deep-sea_adaptation | 10.1186/s12864-020-07102-y | "Many of these piezophile-specific genes are in variable regions of the genome near genomic islands, transposases, and toxin-antitoxin systems" (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9) | Genomic context strongly suggests HGT-mediated adaptation. | high |
| protein_flexibility | enables | enzymatic_activity_at_HHP | 10.48550/arxiv.1603.06901 | "maintaining flexibility... is crucial for enzyme activity under pressure" and larger cavity volume makes proteins "more compressible" (huang2016amolecularperspective pages 9-11) | Mechanistically plausible and supported by comparative enzyme studies; some debate remains on packing vs cavities. | medium |
| electrostatic_modulation | enables | pressure_adapted_protein_stability | 10.1101/2024.07.28.605522 | "modulation of electrostatic interactions between charged residues appears to be a primary driver of evolutionary adaptation to high pressure" (makhatadze2024modulationofelectrostatic pages 1-3, makhatadze2024modulationofelectrostatic pages 6-8) | 2024 preprint; promising but not yet peer-reviewed. | uncertain |
| chaperones (dnaK, dnaJ, groEL) | maintains | protein_folding_at_HHP | 10.1016/j.resmic.2010.09.017 | piezophilic proteins "require chaperone assistance (htpG, dnaK, dnaJ, groEL) when expressed at atmospheric pressure" (oger2010themanyways pages 6-8) | Supports chaperone role in pressure-adapted folding/homeostasis, though often inferred from heterologous/low-pressure expression. | medium |


*Table: This table compiles candidate subject-predicate-object edges for a TraitMech-style obligate piezophily causal graph, with DOI-linked evidence, supporting snippets, and curation confidence. It is useful for identifying which mechanisms are strong enough to curate now versus those that remain taxon-specific or uncertain.*

---

## 5. Ontology Grounding Summary

Key suggested CURIEs for graph construction:
- **traitmech:000002** — obligately piezophilic trait
- **traitmech:000001** — parent trait (piezophilic)
- **ENVO:01000220** — high hydrostatic pressure environment
- **GO:0016042** — lipid catabolic process (proxy for membrane remodeling)
- **GO:0006935** — chemotaxis
- **GO:0009252** — peptidoglycan biosynthesis
- **GO:0006457** — protein folding
- **GO:0015992** — proton transmembrane transport
- **CHEBI:25414** — eicosapentaenoic acid (EPA)
- **CHEBI:28125** — docosahexaenoic acid (DHA)
- **CHEBI:15724** — trimethylamine N-oxide (TMAO)
- **CHEBI:63863** — mannosyl-glycerate
- **CHEBI:15978** — 3-hydroxybutyrate
- **EC:1.14.19.-** — acyl-lipid desaturases
- **EC:7.1.1.2** — NADH:ubiquinone oxidoreductase (Nuo complex)
- **EC:6.3.2.4** — d-alanine-d-alanine ligase
- **EC:1.4.1.1** — alanine dehydrogenase
- **NCBITaxon:298351** — *Pyrococcus yayanosii*
- **NCBITaxon:167879** — *Colwellia marinimaniae*

---

## 6. DOI-First Bibliography

1. Michoud, G. & Jebbar, M. (2016). High hydrostatic pressure adaptive strategies in an obligate piezophile *Pyrococcus yayanosii*. *Scientific Reports*, 6, 27289. DOI: 10.1038/srep27289
2. Peoples, L.M. et al. (2020). Distinctive gene and protein characteristics of extremely piezophilic *Colwellia*. *BMC Genomics*, 21, 692. DOI: 10.1186/s12864-020-07102-y
3. Oger, P.M. & Jebbar, M. (2010). The many ways of coping with pressure. *Research in Microbiology*, 161(10), 799–809. DOI: 10.1016/j.resmic.2010.09.017
4. Scheffer, G. & Gieg, L.M. (2023). The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. *Microorganisms*, 11(7), 1629. DOI: 10.3390/microorganisms11071629
5. Scoma, A. (2021). Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature. *The ISME Journal*, 15, 1871–1878. DOI: 10.1038/s41396-021-00930-0
6. Tamby, A. et al. (2023). Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. *Frontiers in Molecular Biosciences*, 9, 1058381. DOI: 10.3389/fmolb.2022.1058381
7. Cario, A. et al. (2016). Molecular chaperone accumulation as a function of stress evidences adaptation to high hydrostatic pressure in the piezophilic archaeon *Thermococcus barophilus*. *Scientific Reports*, 6, 29483. DOI: 10.1038/srep29483
8. Makhatadze, G.I. (2024). Modulation of electrostatic interactions as a mechanism of cryptic adaptation of *Colwellia* to high hydrostatic pressure. *bioRxiv*. DOI: 10.1101/2024.07.28.605522
9. Huang, Q. et al. (2016). A molecular perspective on the limits of life: enzymes under pressure. *arXiv*. DOI: 10.48550/arxiv.1603.06901
10. Yancey, P.H. (2020). Cellular responses in marine animals to hydrostatic pressure. *J. Exp. Zool. A*, 333(6), 398–420. DOI: 10.1002/jez.2354
11. Kusube, M. et al. (2017). *Colwellia marinimaniae* sp. nov., a hyperpiezophilic species isolated from an amphipod within the Challenger Deep, Mariana Trench. *Int. J. Syst. Evol. Microbiol.*, 67(4), 824–831. DOI: 10.1099/ijsem.0.001671

---

## 7. Curation Warnings

1. **Taxon-specificity:** Many mechanistic details are specific to particular model organisms. The respiratory chain switch (cytochrome c oxidase → quinol oxidase) is well established in *Shewanella* but has not been confirmed in archaeal piezophiles. Hydrogenase and formate metabolism edges are specific to Thermococcales. These should be annotated as taxon-specific in the YAML.

2. **Correlation vs. causation:** The loss of aromatic amino acid biosynthesis pathways in *P. yayanosii* is strongly associated with obligate piezophily but is not demonstrated to be causally required. Similar caution applies to amino acid composition biases across proteomes (scheffer2023themysteryof pages 9-10).

3. **Universal vs. non-universal mechanisms:** Membrane PUFA production via pfaABCD is widely distributed but some piezophilic taxa lack specific PUFAs (e.g., some lack EPA entirely), and branched-chain fatty acid responses are not universal (tamby2023microbialmembranelipid pages 6-7, tamby2023microbialmembranelipid pages 2-4).

4. **Preprint caution:** The electrostatic modulation mechanism (Makhatadze 2024) is from a bioRxiv preprint and should be marked as uncertain until peer review (makhatadze2024modulationofelectrostatic pages 6-8, makhatadze2024modulationofelectrostatic pages 1-3).

5. **Confounding with cold adaptation:** Many obligate piezophiles are also psychrophilic, and membrane lipid changes (PUFA enrichment, branched-chain FA) are shared adaptations to both cold and high pressure. Distinguishing pressure-specific from temperature-specific effects remains a challenge (tamby2023microbialmembranelipid pages 1-2).

6. **HGT-mediated edges:** The role of horizontal gene transfer in acquiring piezophile-specific genes (d-alanine-d-alanine ligase, alanine dehydrogenase, nuo operon, SAM methyltransferase) is supported by genomic context (proximity to genomic islands and transposases) but not by direct experimental demonstration (peoples2020distinctivegeneand pages 7-9).

7. **Existing graph expansion:** The existing causal graph has 6 nodes and 6 edges. The present report identifies approximately 50 candidate nodes and 26 candidate edges, representing a substantial expansion. Curators should prioritize edges marked as "high confidence" for initial inclusion and add "medium/uncertain" edges with appropriate caveats.

References

1. (scoma2021functionalgroupsin pages 1-2): Alberto Scoma. Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature. The ISME Journal, 15:1871-1878, Mar 2021. URL: https://doi.org/10.1038/s41396-021-00930-0, doi:10.1038/s41396-021-00930-0. This article has 18 citations.

2. (scoma2021functionalgroupsin pages 6-7): Alberto Scoma. Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature. The ISME Journal, 15:1871-1878, Mar 2021. URL: https://doi.org/10.1038/s41396-021-00930-0, doi:10.1038/s41396-021-00930-0. This article has 18 citations.

3. (scoma2021functionalgroupsin pages 2-3): Alberto Scoma. Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature. The ISME Journal, 15:1871-1878, Mar 2021. URL: https://doi.org/10.1038/s41396-021-00930-0, doi:10.1038/s41396-021-00930-0. This article has 18 citations.

4. (scoma2021functionalgroupsin pages 5-6): Alberto Scoma. Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature. The ISME Journal, 15:1871-1878, Mar 2021. URL: https://doi.org/10.1038/s41396-021-00930-0, doi:10.1038/s41396-021-00930-0. This article has 18 citations.

5. (michoud2016highhydrostaticpressure pages 1-2): Grégoire Michoud and Mohamed Jebbar. High hydrostatic pressure adaptive strategies in an obligate piezophile pyrococcus yayanosii. Scientific Reports, Jun 2016. URL: https://doi.org/10.1038/srep27289, doi:10.1038/srep27289. This article has 89 citations and is from a peer-reviewed journal.

6. (michoud2016highhydrostaticpressure pages 2-3): Grégoire Michoud and Mohamed Jebbar. High hydrostatic pressure adaptive strategies in an obligate piezophile pyrococcus yayanosii. Scientific Reports, Jun 2016. URL: https://doi.org/10.1038/srep27289, doi:10.1038/srep27289. This article has 89 citations and is from a peer-reviewed journal.

7. (peoples2020distinctivegeneand pages 1-2): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 56 citations and is from a peer-reviewed journal.

8. (peoples2020distinctivegeneand pages 5-7): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 56 citations and is from a peer-reviewed journal.

9. (oger2010themanyways pages 5-6): Philippe M. Oger and Mohamed Jebbar. The many ways of coping with pressure. Research in microbiology, 161 10:799-809, Dec 2010. URL: https://doi.org/10.1016/j.resmic.2010.09.017, doi:10.1016/j.resmic.2010.09.017. This article has 273 citations and is from a peer-reviewed journal.

10. (peoples2020distinctivegeneand pages 7-9): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 56 citations and is from a peer-reviewed journal.

11. (tamby2023microbialmembranelipid pages 2-4): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 49 citations.

12. (scheffer2023themysteryof pages 6-7): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 32 citations.

13. (scheffer2023themysteryof pages 7-9): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 32 citations.

14. (michoud2016highhydrostaticpressure pages 3-4): Grégoire Michoud and Mohamed Jebbar. High hydrostatic pressure adaptive strategies in an obligate piezophile pyrococcus yayanosii. Scientific Reports, Jun 2016. URL: https://doi.org/10.1038/srep27289, doi:10.1038/srep27289. This article has 89 citations and is from a peer-reviewed journal.

15. (michoud2016highhydrostaticpressure pages 4-6): Grégoire Michoud and Mohamed Jebbar. High hydrostatic pressure adaptive strategies in an obligate piezophile pyrococcus yayanosii. Scientific Reports, Jun 2016. URL: https://doi.org/10.1038/srep27289, doi:10.1038/srep27289. This article has 89 citations and is from a peer-reviewed journal.

16. (oger2010themanyways pages 4-5): Philippe M. Oger and Mohamed Jebbar. The many ways of coping with pressure. Research in microbiology, 161 10:799-809, Dec 2010. URL: https://doi.org/10.1016/j.resmic.2010.09.017, doi:10.1016/j.resmic.2010.09.017. This article has 273 citations and is from a peer-reviewed journal.

17. (tamby2023microbialmembranelipid pages 10-11): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 49 citations.

18. (tamby2023microbialmembranelipid pages 6-7): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 49 citations.

19. (tamby2023microbialmembranelipid pages 1-2): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 49 citations.

20. (scheffer2023themysteryof pages 9-10): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 32 citations.

21. (yancey2020cellularresponsesin pages 9-11): Paul H. Yancey. Cellular responses in marine animals to hydrostatic pressure. Journal of experimental zoology. Part A, Ecological and integrative physiology, 333:398-420, Feb 2020. URL: https://doi.org/10.1002/jez.2354, doi:10.1002/jez.2354. This article has 75 citations.

22. (cario2016molecularchaperoneaccumulation pages 4-5): Anaïs Cario, Mohamed Jebbar, Axel Thiel, Nelly Kervarec, and Phil M. Oger. Molecular chaperone accumulation as a function of stress evidences adaptation to high hydrostatic pressure in the piezophilic archaeon thermococcus barophilus. Scientific Reports, Jul 2016. URL: https://doi.org/10.1038/srep29483, doi:10.1038/srep29483. This article has 41 citations and is from a peer-reviewed journal.

23. (oger2010themanyways pages 2-4): Philippe M. Oger and Mohamed Jebbar. The many ways of coping with pressure. Research in microbiology, 161 10:799-809, Dec 2010. URL: https://doi.org/10.1016/j.resmic.2010.09.017, doi:10.1016/j.resmic.2010.09.017. This article has 273 citations and is from a peer-reviewed journal.

24. (oger2010themanyways pages 6-8): Philippe M. Oger and Mohamed Jebbar. The many ways of coping with pressure. Research in microbiology, 161 10:799-809, Dec 2010. URL: https://doi.org/10.1016/j.resmic.2010.09.017, doi:10.1016/j.resmic.2010.09.017. This article has 273 citations and is from a peer-reviewed journal.

25. (scheffer2023themysteryof pages 10-12): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 32 citations.

26. (peoples2020distinctivegeneand pages 9-11): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 56 citations and is from a peer-reviewed journal.

27. (huang2016amolecularperspective pages 9-11): Q. Huang, K. N. Tran, J. M. Rodgers, D. H. Bartlett, R. J. Hemley, and T. Ichiye. A molecular perspective on the limits of life: enzymes under pressure. Text, Jan 2016. URL: https://doi.org/10.48550/arxiv.1603.06901, doi:10.48550/arxiv.1603.06901. This article has 27 citations and is from a peer-reviewed journal.

28. (makhatadze2024modulationofelectrostatic pages 6-8): George I. Makhatadze. Modulation of electrostatic interactions as a mechanism of cryptic adaptation of colwellia to high hydrostatic pressure. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.28.605522, doi:10.1101/2024.07.28.605522. This article has 1 citations.

29. (makhatadze2024modulationofelectrostatic pages 1-3): George I. Makhatadze. Modulation of electrostatic interactions as a mechanism of cryptic adaptation of colwellia to high hydrostatic pressure. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.28.605522, doi:10.1101/2024.07.28.605522. This article has 1 citations.