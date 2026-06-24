---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:35:18.165303'
end_time: '2026-06-18T10:44:07.783244'
duration_seconds: 529.62
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: carboxydotrophic
  trait_identifier: METPO:1000633
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: carboxydotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism derives energy from the oxidation
    of carbon monoxide.
  parent_traits: METPO:1000631
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro1595: Carbon monoxide (CO) supports the growth
    and metabolism (Review supports aerobic CO oxidation as an energy-supporting metabolism.)
    | DOI:10.1111/j.1574-6968.1986.tb01858.x: presence of the enzyme CO dehydrogenase
    (Review supports CODH and CO-insensitive respiratory-chain features in aerobic
    carboxydotrophs.)'
  causal_graph_summary: 'carboxydotrophic_co_oxidation: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** carboxydotrophic
- **METPO identifier:** METPO:1000633
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism derives energy from the oxidation of carbon monoxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro1595: Carbon monoxide (CO) supports the growth and metabolism (Review supports aerobic CO oxidation as an energy-supporting metabolism.) | DOI:10.1111/j.1574-6968.1986.tb01858.x: presence of the enzyme CO dehydrogenase (Review supports CODH and CO-insensitive respiratory-chain features in aerobic carboxydotrophs.)
- **Existing causal graph summary:** carboxydotrophic_co_oxidation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **carboxydotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/carboxydotrophic.yaml`.

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
- **Trait label:** carboxydotrophic
- **METPO identifier:** METPO:1000633
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism derives energy from the oxidation of carbon monoxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro1595: Carbon monoxide (CO) supports the growth and metabolism (Review supports aerobic CO oxidation as an energy-supporting metabolism.) | DOI:10.1111/j.1574-6968.1986.tb01858.x: presence of the enzyme CO dehydrogenase (Review supports CODH and CO-insensitive respiratory-chain features in aerobic carboxydotrophs.)
- **Existing causal graph summary:** carboxydotrophic_co_oxidation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **carboxydotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/carboxydotrophic.yaml`.

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


## Microbial trait: **carboxydotrophic** (METPO:1000633)

### Scope summary (curation-focused)
**Carboxydotrophy** is a trophic/physiological capacity in which an organism conserves energy from the oxidation of carbon monoxide (CO) to carbon dioxide (CO2), with the released electrons feeding respiration or other energy-conserving reductive processes. The defining biochemical step is catalysis by **carbon monoxide dehydrogenase (CODH)**, which “catalyzes the reversible oxidation of CO to CO2” (dent2023carbonmonoxidesensingtranscription pages 1-3). Mechanistically, microbial CO oxidation spans both **aerobic** and **anaerobic** contexts, with the dominant boundary determined by oxygen sensitivity of the CODH class: **Ni,Fe-CODHs are oxygen sensitive** and associated with anaerobic carboxydotrophs (dent2023carbonmonoxidesensingtranscription pages 1-3), whereas **Cu,Mo-CODHs are O2-tolerant** and associated with aerobic CO metabolism (dent2023carbonmonoxidesensingtranscription pages 3-5).

#### What the trait *includes*
- **Aerobic carboxydotrophy / carboxydovory**: CO oxidation feeding the aerobic respiratory chain, often at trace/atmospheric concentrations; CO oxidation can support maintenance energy and survival during starvation (dent2023carbonmonoxidesensingtranscription pages 1-3, leung2024tracegasoxidation pages 1-2). 
- **Anaerobic carboxydotrophy**: CO oxidation coupled to reduction of alternative electron acceptors/sinks including **protons (H2 evolution; hydrogenogenesis)** and, in some taxa, **nitrate** (imaura2023isolationandgenomic pages 1-4, bahrle2023currentstatusof pages 8-9, imaura2023isolationgenomicsequence pages 2-4).

#### Boundary cases important for curation
- **CO utilization for biosynthesis without clear energy conservation**: In the human gut, many genomes encode putative Ni-CODH but lack “CO-oxidizing respiratory machinery” (e.g., energy-converting hydrogenases), suggesting CO use may favor fixation/biosynthesis rather than respiratory energy conservation (katayama2024phylogeneticdiversityofa pages 1-2). Such cases should be curated as *CO-utilization* rather than carboxydotrophy unless energy conservation is evidenced.
- **CO tolerance/protection systems** (e.g., CowN protecting nitrogenase from CO) are related but not sufficient to claim carboxydotrophy (dent2023carbonmonoxidesensingtranscription pages 7-9).
- **Genomic prediction alone** (e.g., MAGs) should be curated as *putative* unless activity/physiology is demonstrated (williams2024novelendolithicbacteria pages 1-2).


### Current understanding: key concepts and definitions
1. **Core reaction and energy conservation**
   - CODH-mediated CO oxidation provides electrons that can enter electron transport chains and ultimately support ATP synthesis: CO oxidizers “couple reversible CO oxidation to reduction of electron acceptors (O2, H+, NO3−, SO42−); reduction of these acceptors generates an ion motive force that drives ATP synthesis” (bahrle2023currentstatusof pages 4-5). 

2. **Two major CODH systems (key mechanistic fork)**
   - **Aerobic Mo,Cu-CODH system (cox)**: encoded by **cox operons** including **coxS, coxM, coxL** (dent2023carbonmonoxidesensingtranscription pages 3-5), with accessory genes **coxDEF, coxI, coxG** supporting active-site assembly/membrane anchoring (dent2023carbonmonoxidesensingtranscription pages 3-5). In membrane-associated systems, electrons from CODH can be “accepted by a cytochrome b complex or a quinone” (bahrle2023currentstatusof pages 5-8).
   - **Anaerobic Ni,Fe-CODH system (coo/cdh/acs)**: **coo operons** encode CODH plus accessory proteins for energy conservation (dent2023carbonmonoxidesensingtranscription pages 3-5). They include Ni/Fe-S assembly factors (CooC/T/J), electron-transfer protein **CooF**, and hydrogenase-associated modules for “hydrogen production (CooMKLXUH)” (dent2023carbonmonoxidesensingtranscription pages 3-5).

3. **Electron acceptors and outcomes**
   - Aerobic respiration: “In aerobic CO-oxidizing bacteria the terminal oxidant is most commonly molecular oxygen” (dent2023carbonmonoxidesensingtranscription pages 1-3), consistent with Mo-CODH-linked electron flow to terminal oxidases (leung2024tracegasoxidation pages 1-2).
   - Nitrate respiration: CO oxidation can also drive “dissimilatory nitrate reduction/denitrification” (dent2023carbonmonoxidesensingtranscription pages 1-3). In *Parageobacillus* G301, genomic reconstruction suggests “aerobic respiration and nitrate reduction utilize quinones” and that “CO-derived electrons from Mo-CODH may be received by the quinones” linking Mo-CODH to nitrate reduction (imaura2023isolationgenomicsequence pages 2-4).
   - Hydrogenogenesis: Ni,Fe-CODH can couple to **energy-converting hydrogenases (EcH/ECH)** such that electron flow is coupled “to proton reduction” producing H2 (bahrle2023currentstatusof pages 8-9).

4. **Regulation (CO-sensing transcription factors)**
   - Because CODH systems are complex and energetically costly, they are tightly regulated (dent2023carbonmonoxidesensingtranscription pages 1-3).
   - **CooA**: CO binding to Fe(II)-heme activates transcription (promoter binding and RNAP recruitment) (dent2023carbonmonoxidesensingtranscription pages 3-5). CooA homologs are genomically associated with **cooS** and hydrogenase genes (dent2023carbonmonoxidesensingtranscription pages 7-9), consistent with regulation of anaerobic/hydrogenogenic CO metabolism.
   - **RcoM**: heme-dependent **high-affinity CO sensor** that “regulates aerobic CO oxidation” and is found upstream of **coxMSL** genes (dent2023carbonmonoxidesensingtranscription pages 7-9). A mechanistic activation step is described where “Met104 is replaced by CO” to activate promoter binding upstream of coxM (dent2023carbonmonoxidesensingtranscription pages 7-9). Reported CO affinity is very high (“Kd = 4 nM”) (dent2023carbonmonoxidesensingtranscription pages 7-9), supporting sensitivity at low CO concentrations.


### Recent developments (prioritizing 2023–2024)
1. **Expanded regulatory and genomic-context synthesis (2023 review)**
   - Dent et al. (2023) consolidate evidence linking the genomic contexts of CooA vs RcoM to anaerobic vs aerobic CODH systems: “Genes associated with aerobic CO oxidation (cox) were not observed in the genomic context of CooA homologs” (dent2023carbonmonoxidesensingtranscription pages 7-9), while RcoM is commonly found adjacent to coxMSL (dent2023carbonmonoxidesensingtranscription pages 7-9). This provides curatable mechanistic edges between regulators and operons.

2. **A single isolate bridging aerobic and anaerobic CODH systems (2023 primary study)**
   - *Parageobacillus* sp. G301 is reported as “capable of both hydrogenogenic and aerobic carbon monoxide oxidation” (imaura2023isolationgenomicsequence pages 9-11), with both Ni-CODH and Mo-CODH functional (imaura2023isolationgenomicsequence pages 7-9). It provides a rare experimentally characterized example where CO oxidation can couple to: 
     - **H2 production (proton reduction)** via Ni-CODH/ECH (imaura2023isolationgenomicsequence pages 2-4, imaura2023isolationgenomicsequence pages 7-9)
     - **O2 reduction** (aerobic Mo-CODH path) (imaura2023isolationandgenomic pages 1-4)
     - **nitrate reduction** (anaerobic Mo-CODH path; inferred/assigned based on physiology and comparative tests) (imaura2023isolationgenomicsequence pages 7-9, imaura2023isolationgenomicsequence pages 2-4)

3. **Archaeal trace-gas carboxydotrophy and persistence physiology (2024 Nature Communications)**
   - Leung et al. (2024) provide high-impact evidence that a thermoacidophilic archaeon (*Acidianus brierleyi*) “constitutively consumes both H2 and CO to sub-atmospheric levels” (leung2024tracegasoxidation pages 1-2). The work explicitly frames atmospheric CO as a trace energy source (tropospheric CO “~0.09 ppmv (~0.086 nM)”) and notes oxidation “via high-affinity form I CO dehydrogenases” with electrons passed to terminal oxidases (leung2024tracegasoxidation pages 1-2). Trace-gas oxidation occurs across “10–70 °C” and can “enhance ATP production during starvation-induced persistence” (leung2024tracegasoxidation pages 1-2). This expands the trait’s phylogenetic and ecological scope to archaea.

4. **Atmospheric chemosynthesis in extreme deserts (2024 AEM)**
   - Williams et al. (2024) report that in Antarctic endolithic communities, “some MAGs encode the capacity to couple the energy generated from H2 and CO oxidation to support carbon fixation (atmospheric chemosynthesis)” (williams2024novelendolithicbacteria pages 1-2). This is **genomic inference** (not direct flux measurements) but supports candidate nodes/edges linking trace-gas oxidation to carbon fixation in oligotrophic environments.


### Current applications and real-world implementations
1. **Global CO biogeochemical sink (soil-atmosphere CO removal)**
   - Dent et al. (2023) summarize that “computational models estimate 145–163 Tg CO removed per year” by soils (dent2023carbonmonoxidesensingtranscription pages 1-3). This motivates ENVO habitat nodes (soil) and a higher-level ecological edge (soil microbial communities → atmospheric CO sink).

2. **Bioprocess/biotechnology interfaces via CODH catalysis (enzyme applications)**
   - Bährle et al. (2023) review CODH systems with emphasis on redox catalysis relevant to electrochemical applications, distinguishing O2-tolerant Mo,Cu-CODHs from O2-sensitive Ni,Fe-CODHs and explaining how acceptor reduction drives ion motive force and ATP synthesis (bahrle2023currentstatusof pages 4-5). While this review is oriented toward enzymatic CO2↔CO interconversion, it provides mechanistic grounding for implementing CODH-based electron flow in engineered systems.

3. **Versatile CO oxidation at oxic–anoxic interfaces (physiology-to-application bridge)**
   - The multi-mode CO oxidation of *Parageobacillus* G301 (H2-producing, O2-respiring, nitrate-respiring) suggests a chassis-like capacity to channel CO-derived electrons into distinct sinks depending on redox conditions (imaura2023isolationgenomicsequence pages 7-9, imaura2023isolationgenomicsequence pages 2-4). This supports curation of environmental-factor nodes (oxygen availability, nitrate availability) as modulators of which CO-oxidation branch is expressed/functional.


### Expert synthesis and analysis (authoritative-source interpretations)
- **Regulation is central to trait expression**: CODH pathways “require many accessory proteins” and are “energetically costly,” hence are “tightly regulated” (dent2023carbonmonoxidesensingtranscription pages 1-3). For TraitMech, this supports modeling regulatory edges (CO → sensor TF activation → operon transcription → CODH system assembly → CO oxidation → energy conservation).
- **Trait stratifies into mechanistic subtypes**: The CODH oxygen-sensitivity divide (Ni,Fe vs Mo,Cu) is not merely taxonomic—it creates different environmental feasibility regimes (anoxic vs oxic), different electron sinks (hydrogenogenesis vs respiration), and different regulators (CooA vs RcoM) (dent2023carbonmonoxidesensingtranscription pages 7-9, dent2023carbonmonoxidesensingtranscription pages 1-3).
- **Trace-gas carboxydotrophy is increasingly recognized as a persistence strategy**: Evidence that CO oxidation supports survival under carbon starvation and persistence in oligotrophic ecosystems (dent2023carbonmonoxidesensingtranscription pages 1-3, leung2024tracegasoxidation pages 1-2) motivates explicitly including low-CO concentration nodes (trace/atmospheric CO) and “starvation/persistence” outcomes as optional downstream phenotype nodes.


### Recent statistics and quantitative data (for curation)
- **Global soil CO sink**: 145–163 Tg CO/year removed (model estimate) (dent2023carbonmonoxidesensingtranscription pages 1-3).
- **Trace CO concentrations used by aerobic carboxydovores**: ambient aqueous CO approximately 0.1–25 nM (dent2023carbonmonoxidesensingtranscription pages 1-3).
- **Tropospheric CO concentration**: ~0.09 ppmv (~0.086 nM) (leung2024tracegasoxidation pages 1-2).
- **RcoM CO binding affinity**: Kd = 4 nM (dent2023carbonmonoxidesensingtranscription pages 7-9).
- **Trace-gas oxidation temperature span (archaeal example)**: 10–70 °C (leung2024tracegasoxidation pages 1-2).
- ***Parageobacillus* G301 stoichiometries**:
  - Hydrogenogenic: “molar ratio of consumed CO/H2 evolved…/CO2 evolved… = 1:1.03:0.47” (imaura2023isolationgenomicsequence pages 7-9)
  - Aerobic: “molar ratio… CO/consumed O2/CO2 = 1:0.95:0.60” (imaura2023isolationgenomicsequence pages 7-9)
  - Nitrate-coupled: “molar ratio… CO/consumed nitrate/CO2/nitrite = 1:1.79:0.60:1.63” (imaura2023isolationgenomicsequence pages 7-9)


## Candidate causal-graph nodes (grouped by type)
| Group | Label | Description | Suggested identifier(s) | Notes / uncertainty |
|---|---|---|---|---|
| Phenotype/trait | carboxydotrophic | Microbial capacity to conserve energy from oxidation of carbon monoxide (CO) to carbon dioxide (CO2); may support growth, persistence, or maintenance. | METPO:1000633 | Distinguish from CO tolerance or CO use only for biosynthesis without demonstrated energy conservation (dent2023carbonmonoxidesensingtranscription pages 1-3, katayama2024phylogeneticdiversityof pages 1-7) |
| Phenotype/trait | aerobic carboxydotrophy / carboxydovory | CO oxidation linked to aerobic respiration, often at trace or atmospheric CO concentrations. | label only | Boundary case: some literature uses “carboxydovore” for organisms that oxidize CO mainly for supplemental energy rather than autotrophic growth (dent2023carbonmonoxidesensingtranscription pages 1-3, leung2024tracegasoxidation pages 1-2) |
| Phenotype/trait | anaerobic carboxydotrophy | CO oxidation under anoxic conditions using O2-sensitive Ni,Fe-CODH and alternative electron sinks such as protons, nitrate, sulfate, or CO2. | label only | Includes hydrogenogenic and acetogenic variants; not all anaerobic CO users are proven energy conservers in every taxon (dent2023carbonmonoxidesensingtranscription pages 1-3, bahrle2023currentstatusof pages 4-5) |
| Enzymes/proteins/complexes | carbon monoxide dehydrogenase (CODH) | Core enzyme catalyzing reversible CO/CO2 interconversion. | EC:1.2.99.2; GO:0018492 | Central mechanistic node for trait; two main classes differ strongly in oxygen sensitivity and context (dent2023carbonmonoxidesensingtranscription pages 1-3, bahrle2023currentstatusof pages 4-5) |
| Enzymes/proteins/complexes | Mo,Cu-containing CODH | O2-tolerant aerobic CODH, typically heterotrimeric CoxL/CoxM/CoxS enzyme. | EC:1.2.99.2; GO:0018492 | Suitable for aerobic or microaerobic CO oxidation; can feed respiratory chain and in some taxa nitrate reduction (bahrle2023currentstatusof pages 4-5, bahrle2023currentstatusof pages 5-8, imaura2023isolationgenomicsequence pages 2-4) |
| Enzymes/proteins/complexes | Ni,Fe-containing CODH | O2-sensitive anaerobic CODH, catalytic subunit usually CooS/CdhA. | EC:1.2.99.2; GO:0018492 | Common in hydrogenogenic, acetogenic, and methanogenic CO metabolisms (dent2023carbonmonoxidesensingtranscription pages 1-3, katayama2024phylogeneticdiversityof pages 1-7, katayama2024phylogeneticdiversityofa pages 1-2) |
| Enzymes/proteins/complexes | CoxL | Large catalytic subunit of Mo-CODH. | label only | Form I coxL is associated with aerobic CO oxidation; exact stable protein-family identifier may vary by database (katayama2024phylogeneticdiversityof pages 1-7, imaura2023isolationgenomicsequence pages 2-4) |
| Enzymes/proteins/complexes | CoxM | Medium subunit of Mo-CODH. | label only | Usually encoded in coxMSL operons (dent2023carbonmonoxidesensingtranscription pages 3-5, dent2023carbonmonoxidesensingtranscription pages 7-9) |
| Enzymes/proteins/complexes | CoxS | Small subunit of Mo-CODH. | label only | Usually encoded in coxMSL operons (dent2023carbonmonoxidesensingtranscription pages 3-5, dent2023carbonmonoxidesensingtranscription pages 7-9) |
| Enzymes/proteins/complexes | CooS / CdhA | Catalytic subunit of Ni,Fe-CODH. | label only | Often used as genomic marker for anaerobic CO metabolism (katayama2024phylogeneticdiversityof pages 1-7, imaura2023isolationgenomicsequence pages 9-11) |
| Enzymes/proteins/complexes | CooF | Ferredoxin-like electron transfer protein associated with Ni,Fe-CODH. | label only | Supports electron transfer from CODH to downstream modules such as hydrogenases (katayama2024phylogeneticdiversityof pages 1-7, dent2023carbonmonoxidesensingtranscription pages 3-5) |
| Enzymes/proteins/complexes | energy-converting hydrogenase (ECH / EcH) | Membrane-associated hydrogenase coupling electron flow from CO oxidation to proton reduction and ion-motive-force generation. | label only | Important in hydrogenogenic carboxydotrophy; nomenclature varies across taxa (imaura2023isolationandgenomic pages 1-4, bahrle2023currentstatusof pages 8-9, imaura2023isolationgenomicsequence pages 2-4) |
| Enzymes/proteins/complexes | Rnf complex | Energy-conserving ferredoxin:NAD oxidoreductase linked to Wood–Ljungdahl metabolism in some acetogens. | label only | Relevant mainly for acetogenic/anaerobic carboxydotrophs; absent in some taxa such as Parageobacillus G301 (katayama2024phylogeneticdiversityof pages 1-7, bahrle2023currentstatusof pages 8-9, imaura2023isolationgenomicsequence pages 2-4) |
| Enzymes/proteins/complexes | cytochrome b complex / quinone-linked respiratory chain | Respiratory chain components receiving electrons from aerobic CODH. | GO:0022900 | Generic node for electron transport; exact complex identity can differ among taxa (bahrle2023currentstatusof pages 5-8, bahrle2023currentstatusof pages 8-9, imaura2023isolationgenomicsequence pages 2-4) |
| Enzymes/proteins/complexes | ATP synthase | Conserves energy from ion motive force generated during CO-linked respiration or hydrogenogenesis. | GO:0046933 | Broadly inferred from coupling statements rather than always directly assayed in each study (bahrle2023currentstatusof pages 4-5, bahrle2023currentstatusof pages 8-9) |
| Enzymes/proteins/complexes | nitrate reductase (Nar) | Terminal reductase enabling nitrate-coupled anaerobic respiration during CO oxidation in some taxa. | EC:1.7.99.4 | Taxon-specific for nitrate-respiring carboxydotrophs such as G301 (imaura2023isolationgenomicsequence pages 2-4, imaura2023isolationgenomicsequence pages 7-9) |
| Enzymes/proteins/complexes | terminal oxidase | O2-reducing respiratory oxidase receiving electrons ultimately derived from CO oxidation. | GO:0004129 | Generic term; exact oxidase type differs among organisms (leung2024tracegasoxidation pages 1-2, imaura2023isolationgenomicsequence pages 2-4) |
| Enzymes/proteins/complexes | CooA | Heme-dependent CO-sensing transcription factor regulating anaerobic CO metabolism genes. | label only | Strongly associated with coo operons and hydrogenogenic/anaerobic contexts (bahrle2023currentstatusof pages 8-9, dent2023carbonmonoxidesensingtranscription pages 3-5, dent2023carbonmonoxidesensingtranscription pages 7-9) |
| Enzymes/proteins/complexes | RcoM | Heme-dependent, high-affinity CO-sensing transcription factor regulating aerobic CO oxidation genes. | label only | Often associated with coxMSL; reported CO affinity in low nM range (dent2023carbonmonoxidesensingtranscription pages 7-9, dent2023carbonmonoxidesensingtranscription pages 9-11) |
| Enzymes/proteins/complexes | CorQ/CorR | CO-responsive two-component regulatory system linked to coo operons in some archaea. | label only | More taxon-specific than CooA/RcoM; curate cautiously (dent2023carbonmonoxidesensingtranscription pages 11-13) |
| Genes/operons | cox operon | Operon encoding aerobic Mo-CODH core and accessory factors. | label only | Typically includes coxS, coxM, coxL; accessory genes may include coxDEF, coxI, coxG (dent2023carbonmonoxidesensingtranscription pages 3-5, imaura2023isolationgenomicsequence pages 2-4) |
| Genes/operons | coxMSL / coxSML | Core structural genes for Mo-CODH. | label only | Operon order varies in literature; same functional module (dent2023carbonmonoxidesensingtranscription pages 3-5, dent2023carbonmonoxidesensingtranscription pages 7-9) |
| Genes/operons | coxDEF | Accessory genes for Mo-CODH active-site assembly. | label only | Support Mo-CODH maturation rather than catalysis directly (dent2023carbonmonoxidesensingtranscription pages 3-5, imaura2023isolationgenomicsequence pages 2-4) |
| Genes/operons | coxI | Accessory / membrane-anchoring gene linked to aerobic CODH systems. | label only | Presence and role can vary across taxa (dent2023carbonmonoxidesensingtranscription pages 3-5) |
| Genes/operons | coxG | Accessory electron-transfer component associated with aerobic CODH systems. | label only | Often included in genomic context of cox operons (dent2023carbonmonoxidesensingtranscription pages 3-5) |
| Genes/operons | coo operon | Operon encoding anaerobic Ni,Fe-CODH system and associated energy-conservation modules. | label only | Frequently regulated by CooA; often linked to hydrogenogenic metabolism (bahrle2023currentstatusof pages 8-9, dent2023carbonmonoxidesensingtranscription pages 3-5, dent2023carbonmonoxidesensingtranscription pages 7-9) |
| Genes/operons | cooS | Gene encoding catalytic Ni,Fe-CODH subunit. | label only | Widely used marker for anaerobic CO oxidation; disruption can abolish growth on CO in some taxa (imaura2023isolationgenomicsequence pages 9-11) |
| Genes/operons | cooC / cooT / cooJ | Ni-4Fe-4S assembly and maturation factors for Ni,Fe-CODH. | label only | Mechanistically important but not always all present in every operon (dent2023carbonmonoxidesensingtranscription pages 3-5) |
| Genes/operons | cooF | Electron transfer gene adjacent to cooS. | label only | Often bridges CODH to hydrogenase/electron-accepting modules (dent2023carbonmonoxidesensingtranscription pages 3-5, imaura2023isolationgenomicsequence pages 2-4) |
| Genes/operons | cooMKLXUH | Hydrogenase-associated gene cluster linked to CO oxidation and H2 production. | label only | Strong candidate module for hydrogenogenic carboxydotrophy (dent2023carbonmonoxidesensingtranscription pages 3-5, dent2023carbonmonoxidesensingtranscription pages 7-9) |
| Genes/operons | coo–ech gene cluster | Genomic module coupling Ni,Fe-CODH to energy-converting hydrogenase. | label only | Particularly relevant in thermophilic hydrogenogenic CO oxidizers (imaura2023isolationandgenomic pages 1-4, imaura2023isolationgenomicsequence pages 9-11, imaura2023isolationgenomicsequence pages 7-9) |
| Genes/operons | nar gene cluster | Nitrate reductase genes supporting nitrate-dependent CO oxidation. | label only | Supported in G301 genomic reconstruction; may be absent from many carboxydotrophs (imaura2023isolationgenomicsequence pages 2-4, imaura2023isolationgenomicsequence pages 7-9) |
| Genes/operons | cowN | CO protection gene for nitrogenase, under CooA/RcoM-responsive control in some taxa. | label only | Important boundary-case marker for CO tolerance/protection rather than carboxydotrophy per se (dent2023carbonmonoxidesensingtranscription pages 7-9, dent2023carbonmonoxidesensingtranscription pages 11-13) |
| Pathways/processes | CO oxidation | Biological oxidation of CO to CO2 with release of electrons for energy conservation. | GO:0018491 | Core process underlying trait (dent2023carbonmonoxidesensingtranscription pages 1-3) |
| Pathways/processes | aerobic respiration | O2-dependent respiratory process fueled by electrons from CO oxidation. | GO:0009060 | Canonical process for Mo-CODH-based carboxydotrophy (bahrle2023currentstatusof pages 5-8, dent2023carbonmonoxidesensingtranscription pages 1-3) |
| Pathways/processes | nitrate respiration / dissimilatory nitrate reduction | Anaerobic respiration using nitrate as terminal electron acceptor during CO oxidation. | GO:0009061 | Taxon-specific but experimentally supported in G301 (imaura2023isolationandgenomic pages 1-4, imaura2023isolationgenomicsequence pages 7-9) |
| Pathways/processes | hydrogenogenesis / proton reduction | Production of H2 from protons using electrons derived from CO oxidation. | GO:0018130 | Strongly associated with Ni,Fe-CODH plus ECH modules (imaura2023isolationandgenomic pages 1-4, bahrle2023currentstatusof pages 8-9, imaura2023isolationgenomicsequence pages 7-9) |
| Pathways/processes | Wood–Ljungdahl pathway | Acetyl-CoA pathway coupling CO/CO2 metabolism to carbon fixation and often energy conservation. | KEGG pathway map00720; MetaCyc: PWY-7254 | Common in anaerobic CO utilizers; in some communities/pathobionts may be incomplete or remodeled rather than trait-defining (katayama2024phylogeneticdiversityof pages 1-7, bahrle2023currentstatusof pages 8-9, katayama2024phylogeneticdiversityofa pages 1-2) |
| Pathways/processes | Calvin–Benson–Bassham cycle | CO2 fixation pathway used by some aerobic CO oxidizers. | KEGG pathway map00710 | Relevant to autotrophic aerobic carboxydotrophs, but not universal (dent2023carbonmonoxidesensingtranscription pages 1-3) |
| Pathways/processes | electron transport chain | Transfer of electrons from CODH to terminal acceptors via quinones/cytochromes. | GO:0022900 | Generic process node spanning aerobic and some anaerobic respiratory variants (bahrle2023currentstatusof pages 5-8, bahrle2023currentstatusof pages 8-9, imaura2023isolationgenomicsequence pages 2-4) |
| Pathways/processes | ATP synthesis driven by ion motive force | Energy conservation outcome of CO-linked respiration or hydrogenogenic modules. | GO:0006754 | Often inferred from known physiology and associated complexes (bahrle2023currentstatusof pages 4-5, bahrle2023currentstatusof pages 8-9) |
| Chemicals (CHEBI) | carbon monoxide | Electron donor and substrate for carboxydotrophy. | CHEBI:17245 | Core chemical defining the trait (dent2023carbonmonoxidesensingtranscription pages 1-3) |
| Chemicals (CHEBI) | carbon dioxide | Oxidation product of CO; also carbon-fixation substrate in linked pathways. | CHEBI:16526 | Product node for CODH reaction and substrate in WLP/CBB coupling (bahrle2023currentstatusof pages 4-5, katayama2024phylogeneticdiversityof pages 1-7) |
| Chemicals (CHEBI) | dioxygen | Terminal electron acceptor in aerobic carboxydotrophy. | CHEBI:15379 | Used with Mo-CODH-linked aerobic respiration (bahrle2023currentstatusof pages 5-8, imaura2023isolationgenomicsequence pages 7-9) |
| Chemicals (CHEBI) | nitrate | Terminal electron acceptor in some anaerobic CO oxidizers. | CHEBI:17632 | Supported for Parageobacillus G301 and broader reviews (imaura2023isolationandgenomic pages 1-4, imaura2023isolationgenomicsequence pages 2-4, dent2023carbonmonoxidesensingtranscription pages 1-3) |
| Chemicals (CHEBI) | nitrite | Product of nitrate reduction during nitrate-coupled CO oxidation. | CHEBI:16301 | Mainly relevant if nitrate respiration node is included (imaura2023isolationgenomicsequence pages 7-9) |
| Chemicals (CHEBI) | proton | Electron acceptor for hydrogenogenic CO oxidation. | CHEBI:15378 | Reduced to H2 by ECH/hydrogenase modules (imaura2023isolationandgenomic pages 1-4, bahrle2023currentstatusof pages 8-9) |
| Chemicals (CHEBI) | hydrogen | Product of proton reduction during hydrogenogenic carboxydotrophy. | CHEBI:18276 | Useful as output node in hydrogenogenic branch (imaura2023isolationgenomicsequence pages 7-9) |
| Chemicals (CHEBI) | water | Reactant in CODH-catalyzed CO oxidation and water–gas shift framing. | CHEBI:15377 | May be omitted if graph keeps reaction abstraction at process level (bahrle2023currentstatusof pages 5-8, bahrle2023currentstatusof pages 8-9) |
| Chemicals (CHEBI) | quinone | Respiratory electron carrier receiving CO-derived electrons in some aerobic/nitrate-respiring systems. | CHEBI:36141 | Specific quinone species often unresolved in trait-level evidence (bahrle2023currentstatusof pages 5-8, imaura2023isolationgenomicsequence pages 2-4) |
| Environmental factors/habitats (ENVO) | oxygen availability / oxic conditions | Environmental factor favoring Mo-CODH-based aerobic CO oxidation. | label only | Use as environmental condition node if no exact ontology term selected (dent2023carbonmonoxidesensingtranscription pages 1-3, bahrle2023currentstatusof pages 4-5) |
| Environmental factors/habitats (ENVO) | anoxic conditions | Environmental factor favoring Ni,Fe-CODH-based anaerobic CO oxidation. | label only | Closely tied to O2 sensitivity of Ni,Fe-CODH (dent2023carbonmonoxidesensingtranscription pages 1-3, katayama2024phylogeneticdiversityofa pages 1-2) |
| Environmental factors/habitats (ENVO) | trace / atmospheric CO | Low-concentration CO regime supporting maintenance metabolism and survival. | label only | Quantitatively reported near ~0.09 ppmv tropospheric CO and ~0.1–25 nM aqueous range for aerobic carboxydovores (dent2023carbonmonoxidesensingtranscription pages 1-3, leung2024tracegasoxidation pages 1-2) |
| Environmental factors/habitats (ENVO) | oligotrophic environment | Nutrient-poor setting where trace-gas oxidation can support persistence. | ENVO:01000408 | Common ecological context for atmospheric chemosynthesis and maintenance metabolism (dent2023carbonmonoxidesensingtranscription pages 1-3, leung2024tracegasoxidation pages 1-2, williams2024novelendolithicbacteria pages 1-2) |
| Environmental factors/habitats (ENVO) | soil | Major habitat for atmospheric CO consumption. | ENVO:00001998 | Global soil sink estimates are strong ecological evidence for trait significance (dent2023carbonmonoxidesensingtranscription pages 1-3) |
| Environmental factors/habitats (ENVO) | freshwater sediment | Habitat of Parageobacillus sp. G301 isolate. | ENVO:00002007 | Example habitat supporting facultative aerobic/anaerobic carboxydotrophy (imaura2023isolationandgenomic pages 1-4) |
| Environmental factors/habitats (ENVO) | hydrothermal vent | High-CO or reduced-gas habitat associated with anaerobic carboxydotrophs. | ENVO:00000215 | Relevant for extremophilic anaerobes (dent2023carbonmonoxidesensingtranscription pages 1-3) |
| Environmental factors/habitats (ENVO) | hot spring | Thermal habitat associated with CO-utilizing extremophiles. | ENVO:00000501 | Supports anaerobic and thermophilic CO metabolisms (dent2023carbonmonoxidesensingtranscription pages 1-3) |
| Environmental factors/habitats (ENVO) | Antarctic endolithic habitat | Rock-inhabiting hyperarid habitat where H2/CO oxidation may support atmospheric chemosynthesis. | label only | Genomic inference rather than direct physiological confirmation for many MAGs (williams2024novelendolithicbacteria pages 1-2) |
| Example taxa (NCBITaxon) | Parageobacillus sp. G301 | Facultative anaerobe encoding both Ni,Fe-CODH and Mo-CODH; oxidizes CO coupled to H2 production, O2 reduction, and nitrate reduction. | NCBITaxon:unresolved strain | Strong recent primary-study exemplar; strain-level taxon identifier may need manual confirmation (imaura2023isolationgenomicsequence pages 7-9) |
| Example taxa (NCBITaxon) | Acidianus brierleyi | Thermoacidophilic archaeon shown to consume CO and H2 to sub-atmospheric levels. | NCBITaxon:227 | Useful exemplar for archaeal trace-gas carboxydotrophy (leung2024tracegasoxidation pages 2-3, leung2024tracegasoxidation pages 1-2) |
| Example taxa (NCBITaxon) | Rhodospirillum rubrum | Model anaerobic CO metabolizer with CooA-regulated coo operons. | NCBITaxon:269796 | Classic regulatory exemplar; not a 2023–2024 isolate but heavily referenced in recent review (bahrle2023currentstatusof pages 8-9, dent2023carbonmonoxidesensingtranscription pages 7-9) |
| Example taxa (NCBITaxon) | Acetobacterium woodii | Acetogenic anaerobe linking CODH/WLP to Rnf-based energy conservation. | NCBITaxon:33952 | Good exemplar for WLP-coupled carboxydotrophy (bahrle2023currentstatusof pages 8-9) |
| Example taxa (NCBITaxon) | Oligotropha carboxidovorans | Canonical aerobic carboxydotroph using Mo-CODH for autotrophic growth. | NCBITaxon:40137 | Strong exemplar for aerobic branch of trait (bahrle2023currentstatusof pages 5-8) |
| Example taxa (NCBITaxon) | Carbonactinospora thermoautotrophica strain StC | Consortium keystone species inferred to exhibit carboxydotrophy in thermophilic oligotrophic system. | NCBITaxon:unresolved strain | Evidence is genomic/consortium-based rather than pure-culture trait proof (dent2023carbonmonoxidesensingtranscription pages 1-3) |
| Example taxa (NCBITaxon) | Chloroflexota endolithic MAGs | Novel Antarctic MAGs encoding predicted CO oxidation and atmospheric chemosynthesis functions. | NCBITaxon:multiple unresolved MAGs | Genomic inference only; curate as weak/tentative exemplars (williams2024novelendolithicbacteria pages 1-2) |


*Table: This table lists curation-ready candidate nodes for a TraitMech causal graph of microbial carboxydotrophy, grouped by biological type and annotated with suggested identifiers, evidence-based notes, and uncertainty flags. It is useful as a starting inventory for constructing `carboxydotrophic.yaml`.*


## Evidence-backed candidate causal edges (triples)
| Edge (Subject—Predicate—Object) | Node type(s) | Evidence snippet (verbatim, short) | Source (with DOI, year) | Notes/uncertainty and suggested ontology grounding |
|---|---|---|---|---|
| carbon monoxide — is oxidized by — carbon monoxide dehydrogenase (CODH) | chemical → enzyme | “CODH catalyzes the reversible oxidation of CO to CO2” (dent2023carbonmonoxidesensingtranscription pages 1-3) | Dent et al., *J Bacteriol* (2023), https://doi.org/10.1128/jb.00332-22 | Core defining edge for carboxydotrophy. Grounding: CHEBI:17245 CO; CHEBI:16526 CO2; EC:1.2.99.2; GO carbon monoxide dehydrogenase activity candidate. |
| Ni,Fe-CODH — has property — oxygen sensitive | enzyme class → quality/environmental constraint | “Ni,Fe-CODHs are noted as oxygen sensitive and associated with anaerobic carboxydotrophs” (dent2023carbonmonoxidesensingtranscription pages 1-3) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Supports anaerobic boundary of this CODH class. Grounding: label-only Ni,Fe-CODH; ENVO oxygenated vs anoxic environment candidate. |
| Cu,Mo-CODH (Mo-CODH) — has property — O2-tolerant | enzyme class → quality | “Cu,Mo-CODHs are O2-tolerant (aerobic CO metabolism)” (dent2023carbonmonoxidesensingtranscription pages 3-5) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Distinguishes aerobic carboxydotrophy. Grounding: label-only Cu,Mo-CODH / Mo-CODH. |
| cox operon — encodes — coxS/coxM/coxL Mo-CODH subunits | operon → genes/protein complex | “Mo-CODH is encoded in cox operons that include coxS, coxM, and coxL” (dent2023carbonmonoxidesensingtranscription pages 3-5) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Strong genomic edge for aerobic CO oxidation machinery. Grounding: gene labels coxS, coxM, coxL; GO/EC on complex if available. |
| cox accessory genes (coxDEF/coxI/coxG) — facilitate — Mo-CODH assembly and membrane anchoring | genes/accessory proteins → process/complex | “accessory genes coxDEF, coxI, and coxG facilitate CoxL active-site assembly and membrane anchoring” (dent2023carbonmonoxidesensingtranscription pages 3-5) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Useful mechanistic detail, but some components may be taxon-specific in organization. Grounding: gene labels only. |
| coo operon — encodes — Ni,Fe-CODH and accessory proteins for energy conservation | operon → enzyme complex/process | “coo operons specifically encode CODH plus accessory proteins for energy conservation” (dent2023carbonmonoxidesensingtranscription pages 3-5) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Core anaerobic carboxydotrophy architecture. Grounding: coo operon label; Ni,Fe-CODH label. |
| coo operon — includes — CooF electron transport protein | operon → electron transfer protein | “include factors for… electron transport (CooF)” (dent2023carbonmonoxidesensingtranscription pages 3-5) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Supports electron transfer node downstream of Ni-CODH. Grounding: CooF label; Fe-S protein label. |
| coo operon — includes — cooMKLXUH hydrogenase module | operon → complex | “include factors for… hydrogen production (CooMKLXUH)” (dent2023carbonmonoxidesensingtranscription pages 3-5) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Useful as gene-cluster edge; exact subunit nomenclature may vary among taxa. Grounding: cooMKLXUH label; energy-converting hydrogenase candidate. |
| Ni-CODH + ECH — drives — proton reduction to H2 | enzyme complex/module → chemical transformation | “electrons are transferred via ferredoxin-like carriers (and CooF iron–sulfur proteins) to EcH, which couples electron flow to proton reduction” (bahrle2023currentstatusof pages 8-9) | Bährle et al., *Bioresour Bioprocess* (2023), https://doi.org/10.1186/s40643-023-00705-9 | Strong mechanistic edge for hydrogenogenic carboxydotrophy. Grounding: CHEBI:15378 proton; CHEBI:18276 H2; energy-converting hydrogenase label. |
| hydrogenogenic CO oxidation — generates — ion motive force | process → bioenergetic process | “ECH-mediated proton reduction generates an ion motive force used by ATP synthase” (imaura2023isolationandgenomic pages 1-4) | Imaura et al., *bioRxiv* (2023), https://doi.org/10.1101/2023.01.17.524042 | Mechanistically important but based on inferred machinery in G301 and prior literature. Grounding: GO ion transmembrane transport coupled to electron transfer candidate. |
| ion motive force — powers — ATP synthase | bioenergetic state → enzyme complex | “generates an ion motive force that drives ATP synthesis” (bahrle2023currentstatusof pages 4-5) | Bährle et al. (2023), https://doi.org/10.1186/s40643-023-00705-9 | Generic energy-conservation edge applicable across CO respirers. Grounding: ATP synthase complex; GO ATP biosynthetic process. |
| membrane-bound Mo-CODH — transfers electrons to — cytochrome b complex or quinone | enzyme complex → electron carrier | “accepted by a cytochrome b complex or a quinone” (bahrle2023currentstatusof pages 5-8) | Bährle et al. (2023), https://doi.org/10.1186/s40643-023-00705-9 | Strong for aerobic/membrane-associated systems; may not apply to all cytoplasmic CODHs. Grounding: quinone CHEBI candidate; cytochrome b complex label. |
| CO-derived electrons from Mo-CODH — may be received by — quinones | electron flow/process → electron carrier | “CO-derived electrons from Mo-CODH may be received by the quinones” (imaura2023isolationgenomicsequence pages 2-4) | Imaura et al., *Appl Environ Microbiol* (2023), https://doi.org/10.1128/aem.00185-23 | More taxon-specific/inferred in *Parageobacillus* G301; mark as moderate-confidence. Grounding: quinone label/CHEBI candidate. |
| Mo-CODH-mediated CO oxidation — is coupled to — O2 reduction | process → electron acceptor | “Mo-CODH-mediated CO oxidation supports O2 reduction aerobically” (imaura2023isolationandgenomic pages 1-4) | Imaura et al. (2023), https://doi.org/10.1101/2023.01.17.524042 | Strong edge for aerobic carboxydotrophy. Grounding: CHEBI:15379 dioxygen; GO aerobic respiration candidate. |
| Mo-CODH-mediated CO oxidation — may be coupled to — nitrate reduction | process → electron acceptor/process | “nitrate reduction may be coupled with Mo-CODH-mediated CO oxidation” (imaura2023isolationgenomicsequence pages 2-4) | Imaura et al. (2023), https://doi.org/10.1128/aem.00185-23 | Taxon-specific to G301 and phrased inferentially; curate as uncertain. Grounding: CHEBI:17632 nitrate; EC:1.7.99.4 nitrate reductase candidate. |
| CODH/ACS complex — participates in — Wood–Ljungdahl pathway | enzyme complex → pathway | “The Wood–Ljungdahl (WL) pathway uses CODH/ACS to form acetyl‑CoA” (bahrle2023currentstatusof pages 8-9) | Bährle et al. (2023), https://doi.org/10.1186/s40643-023-00705-9 | Important for anaerobic CO-linked carbon fixation/acetogenesis; not all carboxydotrophs use WLP. Grounding: Wood–Ljungdahl pathway label; acetyl-CoA CHEBI candidate. |
| CO-derived carbon — is incorporated via — Calvin-Benson-Bassham cycle | chemical carbon source → pathway | “CO-derived carbon is incorporated via pathways such as… the Calvin-Benson-Bassham cycle (aerobes)” (dent2023carbonmonoxidesensingtranscription pages 1-3) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Review-level statement; pathway coupling may be taxon-dependent. Grounding: Calvin cycle label; GO carbon fixation candidate. |
| CooA — activates transcription of — coo operons | regulator → operon | “CooA activation is described mechanistically: CO binding to Fe(II)-heme allosterically activates promoter binding and RNAP recruitment” (dent2023carbonmonoxidesensingtranscription pages 3-5) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Strong regulatory edge for anaerobic CO metabolism. Grounding: CooA label; GO DNA-binding transcription activator activity candidate. |
| RcoM — regulates — aerobic coxMSL genes | regulator → operon/genes | “RcoM is described as a heme-dependent, high-affinity CO sensor that ‘regulates aerobic CO oxidation’ and was ‘originally identified upstream of coxMSL genes’” (dent2023carbonmonoxidesensingtranscription pages 7-9) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Strong regulatory edge for aerobic CO oxidation. Grounding: RcoM label; coxMSL gene labels. |
| RcoM — binds — CO with high affinity | regulator → chemical | “RcoM binds CO with very high affinity (‘Kd = 4 nM’)” (dent2023carbonmonoxidesensingtranscription pages 7-9) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Useful quantitative regulator edge; biochemical property, not phenotype-defining alone. Grounding: CHEBI:17245 CO. |
| atmospheric/trace CO oxidation — supports — microbial survival during carbon starvation | ecological process → biological process | “CO oxidation is widespread and supports survival of aerobic heterotrophic bacteria during carbon starvation” (dent2023carbonmonoxidesensingtranscription pages 1-3) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Good ecological edge for carboxydovory/trace-gas scavenging subset of carboxydotrophy. Grounding: atmospheric CO label; GO starvation response candidate. |
| soils — remove — atmospheric CO | habitat → ecological process | “computational models estimate 145–163 Tg CO removed per year” (dent2023carbonmonoxidesensingtranscription pages 1-3) | Dent et al. (2023), https://doi.org/10.1128/jb.00332-22 | Ecosystem-scale edge; not cell-mechanistic but useful environmental context. Grounding: ENVO:00001998 soil; atmospheric CO label. |
| Acidianus brierleyi trace-gas oxidation — enhances — ATP production during starvation-induced persistence | taxon-specific process → phenotype/process | “Trace-gas oxidation occurs across a broad temperature span (10–70 °C) and can enhance ATP production during starvation-induced persistence” (leung2024tracegasoxidation pages 1-2) | Leung et al., *Nat Commun* (2024), https://doi.org/10.1038/s41467-024-47324-2 | Taxon-specific but valuable recent evidence extending trait to archaea and sub-atmospheric CO use. Grounding: NCBITaxon:*Acidianus brierleyi*; GO ATP metabolic process candidate. |


*Table: This table compiles curation-ready causal edges for microbial carboxydotrophy, linking CODH types, operons, regulators, electron acceptors, energy conservation modules, and ecological trace-gas roles. It is designed to support TraitMech graph construction with short evidence snippets, recent sources, and suggested ontology grounding.*


## Ontology grounding notes (CURIE suggestions)
- **Chemicals (CHEBI)**: CO (CHEBI:17245), CO2 (CHEBI:16526), O2 (CHEBI:15379), nitrate (CHEBI:17632), nitrite (CHEBI:16301), proton (CHEBI:15378), H2 (CHEBI:18276), water (CHEBI:15377). (bahrle2023currentstatusof pages 4-5, bahrle2023currentstatusof pages 5-8, bahrle2023currentstatusof pages 8-9, leung2024tracegasoxidation pages 1-2, imaura2023isolationgenomicsequence pages 7-9, dent2023carbonmonoxidesensingtranscription pages 1-3)
- **Enzymes (EC)**: CODH (EC 1.2.99.2; generic CODH activity referenced across sources) (bahrle2023currentstatusof pages 4-5, dent2023carbonmonoxidesensingtranscription pages 1-3). Nitrate reductase Nar (EC 1.7.99.4) is suggested for nitrate respiration coupling in G301 (imaura2023isolationgenomicsequence pages 2-4).
- **Processes (GO; suggested, verify exact term IDs during curation)**: CO oxidation; aerobic respiration; nitrate respiration/dissimilatory nitrate reduction; proton reduction/hydrogenogenesis; electron transport chain; ATP synthesis via chemiosmotic gradient; carbon fixation (Calvin cycle; Wood–Ljungdahl pathway). These are mechanistically supported, but GO IDs should be verified in the ontology browser at curation time (bahrle2023currentstatusof pages 4-5, bahrle2023currentstatusof pages 8-9, leung2024tracegasoxidation pages 1-2, dent2023carbonmonoxidesensingtranscription pages 1-3).
- **Habitats (ENVO)**: soil (ENVO:00001998), oligotrophic environment (ENVO:01000408), hydrothermal vent (ENVO:00000215), hot spring (ENVO:00000501), freshwater sediment (ENVO:00002007). (imaura2023isolationandgenomic pages 1-4, dent2023carbonmonoxidesensingtranscription pages 1-3)


## Warnings / “do-not-curate-yet” items
1. **MAG-only predictions**: Endolithic Chloroflexota MAGs provide plausible capacity, but are not direct physiological demonstrations; edges involving “couple H2/CO oxidation to carbon fixation” should be marked *uncertain / inferred from genomics* unless activity is measured (williams2024novelendolithicbacteria pages 1-2).
2. **Nitrate-coupled CO oxidation generalization**: Evidence is strong for *Parageobacillus* G301, but broad generalization across taxa should be avoided; keep nitrate coupling as taxon-conditional or uncertain unless more sources are added (imaura2023isolationgenomicsequence pages 2-4, imaura2023isolationgenomicsequence pages 7-9).
3. **Human-gut CODH as carboxydotrophy**: Many gut CODH-bearing genomes appear to lack energy-conserving respiratory machinery; treat as CO utilization/biosynthesis rather than carboxydotrophy unless energy conservation is shown (katayama2024phylogeneticdiversityofa pages 1-2).


## DOI-first bibliography (with dates and URLs)
1. **Dent MR, Weaver BR, Roberts MG, Burstyn JN.** Carbon monoxide-sensing transcription factors: regulators of microbial carbon monoxide oxidation pathway gene expression. *Journal of Bacteriology*. **May 2023**. https://doi.org/10.1128/jb.00332-22 (dent2023carbonmonoxidesensingtranscription pages 1-3, dent2023carbonmonoxidesensingtranscription pages 3-5, dent2023carbonmonoxidesensingtranscription pages 7-9)
2. **Bährle R, Böhnke S, Englhard J, Bachmann J, Perner M.** Current status of carbon monoxide dehydrogenases (CODH) and their potential for electrochemical applications. *Bioresources and Bioprocessing*. **Nov 2023**. https://doi.org/10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 4-5, bahrle2023currentstatusof pages 5-8, bahrle2023currentstatusof pages 8-9)
3. **Imaura Y, Okamoto S, Hino T, et al.** Isolation, genomic sequence and physiological characterization of *Parageobacillus* sp. G301, an isolate capable of both hydrogenogenic and aerobic carbon monoxide oxidation. *Applied and Environmental Microbiology*. **Jun 2023**. https://doi.org/10.1128/aem.00185-23 (imaura2023isolationgenomicsequence pages 7-9, imaura2023isolationgenomicsequence pages 2-4, imaura2023isolationgenomicsequence pages 9-11)
4. **Leung PM, Grinter R, Tudor-Matthew E, et al.** Trace gas oxidation sustains energy needs of a thermophilic archaeon at suboptimal temperatures. *Nature Communications*. **Apr 2024**. https://doi.org/10.1038/s41467-024-47324-2 (leung2024tracegasoxidation pages 2-3, leung2024tracegasoxidation pages 1-2)
5. **Williams TJ, Allen MA, Ray AE, et al.** Novel endolithic bacteria of phylum Chloroflexota reveal a myriad of potential survival strategies in the Antarctic desert. *Applied and Environmental Microbiology*. **Feb 2024**. https://doi.org/10.1128/aem.02264-23 (williams2024novelendolithicbacteria pages 1-2)
6. **Katayama YA, Kamikawa R, Yoshida T.** Phylogenetic diversity of putative nickel-containing carbon monoxide dehydrogenase-encoding prokaryotes in the human gut microbiome. *Microbial Genomics*. **Aug 2024**. https://doi.org/10.1099/mgen.0.001285 (katayama2024phylogeneticdiversityofa pages 1-2)
7. **Katayama YA, Kamikawa R, Yoshida T.** Phylogenetic diversity of the carbon monoxide-utilizing prokaryotes and their divergent carbon monoxide metabolisms in the human gut microbiome. *bioRxiv*. **Mar 2024**. https://doi.org/10.1101/2023.10.23.563559 (katayama2024phylogeneticdiversityof pages 1-7)


---

### Deliverable alignment to `data/traits/physiology/carboxydotrophic.yaml`
The node inventory (artifact-01) and edge table (artifact-00) provide a concrete starting set of TraitMech entities and evidence-backed causal triples, emphasizing (i) CODH class, operon structure, and accessory assembly genes; (ii) electron acceptor/sink branching (O2 vs nitrate vs protons); and (iii) CO-sensing transcriptional regulation (CooA vs RcoM) that modulates trait expression under different redox and CO regimes. (dent2023carbonmonoxidesensingtranscription pages 3-5, imaura2023isolationgenomicsequence pages 2-4, dent2023carbonmonoxidesensingtranscription pages 7-9, dent2023carbonmonoxidesensingtranscription pages 1-3)

References

1. (dent2023carbonmonoxidesensingtranscription pages 1-3): Matthew R. Dent, Brian R. Weaver, Madeleine G. Roberts, and Judith N. Burstyn. Carbon monoxide-sensing transcription factors: regulators of microbial carbon monoxide oxidation pathway gene expression. Journal of Bacteriology, May 2023. URL: https://doi.org/10.1128/jb.00332-22, doi:10.1128/jb.00332-22. This article has 21 citations and is from a peer-reviewed journal.

2. (dent2023carbonmonoxidesensingtranscription pages 3-5): Matthew R. Dent, Brian R. Weaver, Madeleine G. Roberts, and Judith N. Burstyn. Carbon monoxide-sensing transcription factors: regulators of microbial carbon monoxide oxidation pathway gene expression. Journal of Bacteriology, May 2023. URL: https://doi.org/10.1128/jb.00332-22, doi:10.1128/jb.00332-22. This article has 21 citations and is from a peer-reviewed journal.

3. (leung2024tracegasoxidation pages 1-2): Pok Man Leung, Rhys Grinter, Eve Tudor-Matthew, James P. Lingford, Luis Jimenez, Han-Chung Lee, Michael Milton, Iresha Hanchapola, Erwin Tanuwidjaya, Ashleigh Kropp, Hanna A. Peach, Carlo R. Carere, Matthew B. Stott, Ralf B. Schittenhelm, and Chris Greening. Trace gas oxidation sustains energy needs of a thermophilic archaeon at suboptimal temperatures. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47324-2, doi:10.1038/s41467-024-47324-2. This article has 18 citations and is from a highest quality peer-reviewed journal.

4. (imaura2023isolationandgenomic pages 1-4): Yoshinari Imaura, Shunsuke Okamoto, Taiki Hino, Yusuke Ogami, Yuka Adachi Katayama, Ayumi Tanimura, Masao Inoue, Ryoma Kamikawa, Takashi Yoshida, and Yoshihiko Sako. Isolation and genomic and physiological characterization of parageobacillus sp. g301, the isolate capable of both hydrogenogenic and aerobic carbon monoxide oxidation. bioRxiv, Jan 2023. URL: https://doi.org/10.1101/2023.01.17.524042, doi:10.1101/2023.01.17.524042. This article has 0 citations.

5. (bahrle2023currentstatusof pages 8-9): Rebecca Bährle, Stefanie Böhnke, Jonas Englhard, Julien Bachmann, and Mirjam Perner. Current status of carbon monoxide dehydrogenases (codh) and their potential for electrochemical applications. Bioresources and Bioprocessing, Nov 2023. URL: https://doi.org/10.1186/s40643-023-00705-9, doi:10.1186/s40643-023-00705-9. This article has 27 citations and is from a peer-reviewed journal.

6. (imaura2023isolationgenomicsequence pages 2-4): Yoshinari Imaura, Shunsuke Okamoto, Taiki Hino, Yusuke Ogami, Yuka Adachi Katayama, Ayumi Tanimura, Masao Inoue, Ryoma Kamikawa, Takashi Yoshida, and Yoshihiko Sako. Isolation, genomic sequence and physiological characterization of <i>parageobacillus</i> sp. g301, an isolate capable of both hydrogenogenic and aerobic carbon monoxide oxidation. Applied and Environmental Microbiology, Jun 2023. URL: https://doi.org/10.1128/aem.00185-23, doi:10.1128/aem.00185-23. This article has 16 citations and is from a peer-reviewed journal.

7. (katayama2024phylogeneticdiversityofa pages 1-2): Yuka Adachi Katayama, Ryoma Kamikawa, and Takashi Yoshida. Phylogenetic diversity of putative nickel-containing carbon monoxide dehydrogenase-encoding prokaryotes in the human gut microbiome. Aug 2024. URL: https://doi.org/10.1099/mgen.0.001285, doi:10.1099/mgen.0.001285. This article has 10 citations and is from a peer-reviewed journal.

8. (dent2023carbonmonoxidesensingtranscription pages 7-9): Matthew R. Dent, Brian R. Weaver, Madeleine G. Roberts, and Judith N. Burstyn. Carbon monoxide-sensing transcription factors: regulators of microbial carbon monoxide oxidation pathway gene expression. Journal of Bacteriology, May 2023. URL: https://doi.org/10.1128/jb.00332-22, doi:10.1128/jb.00332-22. This article has 21 citations and is from a peer-reviewed journal.

9. (williams2024novelendolithicbacteria pages 1-2): Timothy J. Williams, Michelle A. Allen, Angelique E. Ray, Nicole Benaud, Devan S. Chelliah, Davide Albanese, Claudio Donati, Laura Selbmann, Claudia Coleine, and Belinda C. Ferrari. Novel endolithic bacteria of phylum chloroflexota reveal a myriad of potential survival strategies in the antarctic desert. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.02264-23, doi:10.1128/aem.02264-23. This article has 20 citations and is from a peer-reviewed journal.

10. (bahrle2023currentstatusof pages 4-5): Rebecca Bährle, Stefanie Böhnke, Jonas Englhard, Julien Bachmann, and Mirjam Perner. Current status of carbon monoxide dehydrogenases (codh) and their potential for electrochemical applications. Bioresources and Bioprocessing, Nov 2023. URL: https://doi.org/10.1186/s40643-023-00705-9, doi:10.1186/s40643-023-00705-9. This article has 27 citations and is from a peer-reviewed journal.

11. (bahrle2023currentstatusof pages 5-8): Rebecca Bährle, Stefanie Böhnke, Jonas Englhard, Julien Bachmann, and Mirjam Perner. Current status of carbon monoxide dehydrogenases (codh) and their potential for electrochemical applications. Bioresources and Bioprocessing, Nov 2023. URL: https://doi.org/10.1186/s40643-023-00705-9, doi:10.1186/s40643-023-00705-9. This article has 27 citations and is from a peer-reviewed journal.

12. (imaura2023isolationgenomicsequence pages 9-11): Yoshinari Imaura, Shunsuke Okamoto, Taiki Hino, Yusuke Ogami, Yuka Adachi Katayama, Ayumi Tanimura, Masao Inoue, Ryoma Kamikawa, Takashi Yoshida, and Yoshihiko Sako. Isolation, genomic sequence and physiological characterization of <i>parageobacillus</i> sp. g301, an isolate capable of both hydrogenogenic and aerobic carbon monoxide oxidation. Applied and Environmental Microbiology, Jun 2023. URL: https://doi.org/10.1128/aem.00185-23, doi:10.1128/aem.00185-23. This article has 16 citations and is from a peer-reviewed journal.

13. (imaura2023isolationgenomicsequence pages 7-9): Yoshinari Imaura, Shunsuke Okamoto, Taiki Hino, Yusuke Ogami, Yuka Adachi Katayama, Ayumi Tanimura, Masao Inoue, Ryoma Kamikawa, Takashi Yoshida, and Yoshihiko Sako. Isolation, genomic sequence and physiological characterization of <i>parageobacillus</i> sp. g301, an isolate capable of both hydrogenogenic and aerobic carbon monoxide oxidation. Applied and Environmental Microbiology, Jun 2023. URL: https://doi.org/10.1128/aem.00185-23, doi:10.1128/aem.00185-23. This article has 16 citations and is from a peer-reviewed journal.

14. (katayama2024phylogeneticdiversityof pages 1-7): Yuka Adachi Katayama, Ryoma Kamikawa, and Takashi Yoshida. Phylogenetic diversity of the carbon monoxide-utilizing prokaryotes and their divergent carbon monoxide metabolisms in the human gut microbiome. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2023.10.23.563559, doi:10.1101/2023.10.23.563559. This article has 1 citations.

15. (dent2023carbonmonoxidesensingtranscription pages 9-11): Matthew R. Dent, Brian R. Weaver, Madeleine G. Roberts, and Judith N. Burstyn. Carbon monoxide-sensing transcription factors: regulators of microbial carbon monoxide oxidation pathway gene expression. Journal of Bacteriology, May 2023. URL: https://doi.org/10.1128/jb.00332-22, doi:10.1128/jb.00332-22. This article has 21 citations and is from a peer-reviewed journal.

16. (dent2023carbonmonoxidesensingtranscription pages 11-13): Matthew R. Dent, Brian R. Weaver, Madeleine G. Roberts, and Judith N. Burstyn. Carbon monoxide-sensing transcription factors: regulators of microbial carbon monoxide oxidation pathway gene expression. Journal of Bacteriology, May 2023. URL: https://doi.org/10.1128/jb.00332-22, doi:10.1128/jb.00332-22. This article has 21 citations and is from a peer-reviewed journal.

17. (leung2024tracegasoxidation pages 2-3): Pok Man Leung, Rhys Grinter, Eve Tudor-Matthew, James P. Lingford, Luis Jimenez, Han-Chung Lee, Michael Milton, Iresha Hanchapola, Erwin Tanuwidjaya, Ashleigh Kropp, Hanna A. Peach, Carlo R. Carere, Matthew B. Stott, Ralf B. Schittenhelm, and Chris Greening. Trace gas oxidation sustains energy needs of a thermophilic archaeon at suboptimal temperatures. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47324-2, doi:10.1038/s41467-024-47324-2. This article has 18 citations and is from a highest quality peer-reviewed journal.