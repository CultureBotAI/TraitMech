---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:15:58.908048'
end_time: '2026-08-04T06:25:44.839194'
duration_seconds: 585.93
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: fermentative hydrogen production
  trait_identifier: traitmech:000109
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: fermentative_hydrogen_production
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A fermentation in which an organism disposes of excess reducing equivalents
    by producing molecular hydrogen (H2), typically via hydrogenases acting on reduced
    ferredoxin or formate.
  parent_traits: METPO:1002005
  synonyms: biohydrogen production
  evidence_summary: 'DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy
    conservation supports H2 production as a redox-balancing fermentation output via
    hydrogenases.) | DOI:10.1016/S0360-3199(02)00131-3:  (Hallenbeck & Benemann review
    biological hydrogen production, including dark fermentative H2 generation.)'
  causal_graph_summary: 'fermentative_h2_production: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 58
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** fermentative hydrogen production
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000109
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which an organism disposes of excess reducing equivalents by producing molecular hydrogen (H2), typically via hydrogenases acting on reduced ferredoxin or formate.
- **Parent traits:** METPO:1002005
- **Synonyms:** biohydrogen production
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports H2 production as a redox-balancing fermentation output via hydrogenases.) | DOI:10.1016/S0360-3199(02)00131-3:  (Hallenbeck & Benemann review biological hydrogen production, including dark fermentative H2 generation.)
- **Existing causal graph summary:** fermentative_h2_production: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **fermentative hydrogen production** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/fermentative_hydrogen_production.yaml`.

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
- **Trait label:** fermentative hydrogen production
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000109
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which an organism disposes of excess reducing equivalents by producing molecular hydrogen (H2), typically via hydrogenases acting on reduced ferredoxin or formate.
- **Parent traits:** METPO:1002005
- **Synonyms:** biohydrogen production
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports H2 production as a redox-balancing fermentation output via hydrogenases.) | DOI:10.1016/S0360-3199(02)00131-3:  (Hallenbeck & Benemann review biological hydrogen production, including dark fermentative H2 generation.)
- **Existing causal graph summary:** fermentative_h2_production: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **fermentative hydrogen production** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/fermentative_hydrogen_production.yaml`.

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


# Curation report: fermentative hydrogen production

## Trait record and scope

- **Trait label:** fermentative hydrogen production
- **Trait identifier:** `traitmech:000109`
- **Category / term kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `METPO:1002005`
- **Synonym:** biohydrogen production

### Recommended operational definition

This trait is the **cellular capacity to evolve molecular hydrogen during fermentation**, thereby disposing of reducing equivalents generated by anaerobic organic-substrate catabolism. Two principal mechanistic realizations should be admitted:

1. **Ferredoxin/cofactor branch:** substrate oxidation generates reduced ferredoxin, sometimes together with NADH; a proton-reducing hydrogenase reoxidizes these carriers and evolves H2.
2. **Formate branch:** pyruvate-formate lyase produces formate, which a formate-hydrogenlyase complex disproportionates to H2 and CO2.

A current fermentation definition explicitly allows protons to serve as electron acceptors, producing H2, while requiring an organic electron donor such as glucose. The 2024 synthesis examined 8,300 prokaryotes, found 55 fermentation end products in nearly 300 combinations, and mapped 123 reactions, 127 enzymes, and 97 metabolites, underscoring that H2 evolution is a branch of a diverse fermentation network rather than a single universal pathway. (hackmann2024thevastlandscape pages 2-3, hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 5-6)

### Boundaries

**Include:** anaerobic or oxygen-limited H2 evolution causally coupled to fermentation of carbohydrates, amino acids, pyruvate, formate, or related organic substrates; whole-cell phenotypes measured as H2 accumulation; and genetically or biochemically supported hydrogenase/FHL mechanisms.

**Exclude as neighboring traits:**

- oxygenic or anoxygenic **photobiological H2 production**, where light supplies energy;
- **microbial electrolysis**, where an electrode and applied potential are causal;
- respiratory H2 metabolism involving an external terminal acceptor;
- hydrogenotrophic methanogenesis, acetogenesis, sulfate reduction, or other **H2 consumption**;
- abiotic H2 generation and isolated-enzyme activity lacking evidence of a fermentative cellular phenotype.

H2 consumption may nevertheless be represented as an environmental/community modifier because it changes H2 partial pressure and therefore fermentative thermodynamics. Conversely, H2 can be a secondary electron donor in some fermentation definitions, but that is not the phenotype represented by this trait. (hackmann2024thevastlandscape pages 2-3, hackmann2024thevastlandscape pages 1-2)

## Candidate nodes grouped by type

### Pathways and biological processes

- fermentative hydrogen production — `traitmech:000109`
- fermentation — ontology grounding should use the project-approved METPO term; do not infer a child CURIE from `METPO:1002005`
- carbohydrate/glucose fermentation
- acetate-type fermentation
- butyrate-type fermentation
- mixed-acid fermentation
- pyruvate oxidation through PFOR
- formate-dependent H2 evolution
- flavin-based electron bifurcation/confurcation
- substrate-level phosphorylation
- redox-cofactor regeneration
- methanogenic H2 consumption — contextual node, not part of the intrinsic trait

### Chemicals and electron carriers

High-confidence ChEBI candidates include molecular hydrogen (`CHEBI:18276`), proton (`CHEBI:15378`), carbon dioxide (`CHEBI:16526`), formate (`CHEBI:15740`), pyruvate (`CHEBI:15361`), acetyl-CoA (`CHEBI:15351`), glucose (`CHEBI:17234`), NAD+ (`CHEBI:57540`), and NADH (`CHEBI:57945`). Candidate labels requiring curator verification include reduced/oxidized ferredoxin, acetate, butyrate, lactate, ethanol, FAD, FMN, Fe–S clusters, nickel, cobalt, and carbon monoxide. Use molecular H2—not generic elemental hydrogen—as the graph product.

### Enzymes, proteins, complexes, and regulators

- pyruvate:ferredoxin oxidoreductase, **PFOR/POR** — `EC:1.2.7.1`
- pyruvate-formate lyase, **PflB/PFL** — `EC:2.3.1.54`
- hydrogenase (NAD+, ferredoxin), a bifurcating/confurcating class — `EC:1.12.1.4`
- monomeric ferredoxin-dependent [FeFe]-hydrogenase — label-only until a taxon-specific enzyme is selected
- electron-bifurcating [FeFe]-hydrogenase **HydABC** — complex node; subunits should be grounded to strain-specific UniProt records only when the organism is specified
- formate-hydrogenlyase **FHL-1/FHL-2**
- fermentative formate dehydrogenase H, **Fdh-H/FdhF**
- hydrogenase 3, **Hyd-3/Hyc**
- formate channel **FocA**
- transcriptional activator **FhlA** and repressor **HycA**
- [FeFe]-hydrogenase maturation proteins **HydE/HydF/HydG** — plausible enabling nodes, but no edge should be added here without direct phenotype evidence
- Rnf ferredoxin:NAD oxidoreductase and Nfn transhydrogenase — redox-allocation nodes, not automatically H2-producing enzymes

Buckel’s review supports reduced ferredoxin generation by oxidative decarboxylation of 2-oxoacids and flavin-based electron bifurcation, and describes Rnf-mediated ion-gradient formation. These systems affect electron allocation, but Rnf should not be represented as directly producing H2. (buckel2021energyconservationin pages 1-2, buckel2021energyconservationin pages 3-4, buckel2021energyconservationin pages 4-6)

### Cellular locations and structures

- cytoplasm — PFOR, soluble hydrogenases, PFL, and regulatory steps in many bacteria
- cytoplasmic membrane — FocA and membrane-associated FHL in *Escherichia coli*
- H-cluster of [FeFe]-hydrogenase
- iron–sulfur electron-transfer chain
- FMN-containing bifurcation site in HydB

Locations are architecture- and taxon-dependent; they should not be generalized from *E. coli* FHL to soluble clostridial hydrogenases.

### Organisms and communities

Useful taxon exemplars are *Clostridium* spp., *Thermotoga* spp., *Caldicellulosiruptor saccharolyticus*, *Clostridium thermocellum*, enterobacteria including *Escherichia coli*, and hydrogenase-positive gut butyrogens such as *Roseburia intestinalis* and *Eubacterium rectale*. *Faecalibacterium prausnitzii* is a useful negative comparator in the 2023 H2-feedback study because the tested strain lacked hydrogenase and did not respond to H2 or CO. *Methanobrevibacter smithii* is an H2-consuming community modifier, not a positive exemplar of the trait. (campbell2023h2generatedby pages 1-2, campbell2023h2generatedby pages 7-9)

## Candidate causal edges

The table below is the recommended starting set for YAML curation. It deliberately separates intrinsic mechanisms from environmental and community modifiers.

| Subject | Predicate | Object | Evidence DOI/date | Supporting snippet | Scope/confidence |
|---|---|---|---|---|---|
| carbohydrate/glucose fermentation | produces | pyruvate + reduced cofactors/end products including H2 branches | 10.1093/femsre/fuae016 (May 2024) | “carbohydrates and pyruvate are the most commonly used fermentation substrates” and fermentation releases “more than 50 metabolic end products”; H2 is included because “Protons can be another electron acceptor, forming hydrogen (H2)” (hackmann2024thevastlandscape pages 2-3, hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 5-6) | Broad trait scope; high confidence for fermentation context, moderate for graph edge abstraction |
| pyruvate | is oxidized by | pyruvate:ferredoxin oxidoreductase (PFOR) | 10.3389/fmicb.2021.703525 (Sep 2021) | “pyruvate oxidation using ferredoxin (Fd) reduction” is described in anaerobic fermentation (buckel2021energyconservationin pages 11-12) | Broad in strict anaerobes; moderate confidence because excerpt summarizes reaction rather than naming all taxa |
| pyruvate oxidation by PFOR | produces | acetyl-CoA + CO2 + reduced ferredoxin | 10.3389/fmicb.2021.703525 (Sep 2021) | “pyruvate oxidation using ferredoxin (Fd) reduction, producing reduced ferredoxin (Fd−) alongside acetyl-CoA and CO2” (buckel2021energyconservationin pages 11-12) | Core mechanistic edge; high confidence |
| reduced ferredoxin | donates electrons to | proton-reducing hydrogenase | 10.3389/fmicb.2021.703525 (Sep 2021); 10.1093/femsre/fuae016 (May 2024) | Reduced ferredoxin is a central fermentation electron carrier, and “Hydrogenase (NAD+, ferredoxin) (EC 1.12.1.4) … catalyz[es] H2 production from 2 H+ to 1 H2” while balancing ferredoxin/NAD pools (buckel2021energyconservationin pages 1-2, hackmann2024thevastlandscape pages 12-13) | Core edge; moderate-high confidence, enzyme class broad rather than single protein |
| proton-reducing hydrogenase | produces | H2 | 10.1093/femsre/fuae016 (May 2024) | “Hydrogenase (NAD+, ferredoxin) (EC 1.12.1.4) is the enzyme catalyzing H2 production from 2 H+ to 1 H2” (hackmann2024thevastlandscape pages 12-13) | Core edge; high confidence |
| pyruvate | is cleaved by pyruvate-formate lyase (PFL) to produce | formate + acetyl-CoA | 10.4061/2011/532536 (May 2011); 10.1128/jb.00502-24 (Feb 2025) | “PFL system converts pyruvate to formate and acetyl-CoA”; “Pyruvate formate-lyase (PflB) cleaves pyruvate to produce formate” (crable2011formateformationand pages 2-3, sawers2025howfocafacilitates pages 1-3) | Strong but taxon-enriched for enterobacteria/facultative anaerobes; high confidence |
| FocA | transports | formate across the cytoplasmic membrane | 10.1128/jb.00502-24 (Feb 2025) | “FocA pentameric membrane transporter facilitates bidirectional formate translocation” (sawers2025howfocafacilitates pages 1-3) | **E. coli-specific / enterobacterial**; high confidence, not universal |
| formate | activates | FhlA | 10.1128/jb.00502-24 (Feb 2025) | “formate re-imported into the cytoplasm is sensed by the transcriptional regulator FhlA” and formate accumulation activates FhlA (sawers2025howfocafacilitates pages 1-3, sawers2025howfocafacilitates pages 3-5) | **E. coli-specific**; high confidence |
| FhlA | induces | formate hydrogenlyase (FHL) genes/complex | 10.1128/jb.00502-24 (Feb 2025); 10.4061/2011/532536 (May 2011) | FhlA induces the “formate regulon” encoding enzymes “necessary to assemble the formate hydrogenlyase complex”; engineering increasing fhlA strongly enhanced H2 production (sawers2025howfocafacilitates pages 1-3, sawers2025howfocafacilitates pages 3-5, crable2011formateformationand pages 4-6) | **E. coli-specific** regulatory edge; high confidence |
| formate hydrogenlyase (FHL) | converts | formate to H2 + CO2 | 10.1023/b:biry.0000009129.18714.a4 (Nov 2003); 10.4061/2011/532536 (May 2011); 10.1128/jb.00502-24 (Feb 2025) | FHL “catalyzes oxidation of formic acid to CO2 and H2”; FDH-H transfers electrons to Hyd-3, which “subsequently produces hydrogen gas” (bagramyan2003structuralandfunctional pages 1-3, crable2011formateformationand pages 2-3, sawers2025howfocafacilitates pages 1-3) | **Mixed-acid fermentation / E. coli-focused**; high confidence |
| elevated H2 partial pressure | shifts fermentation away from net H2 evolution toward | butyrate/lactate/formate production and away from acetate | 10.1186/s40168-023-01565-3 (Jun 2023) | High H2 “increased production of butyrate, lactate, and formate” and shifted fermentation “away from acetate”; effects were dose-dependent up to 3 atm H2 (campbell2023h2generatedby pages 1-2, campbell2023h2generatedby pages 7-9, campbell2023h2generatedby pages 2-4) | Strong causal evidence but **gut butyrogen assay-specific**; do not overgeneralize to all taxa |
| carbon monoxide / hydrogenase inhibition | mimics | high-H2 product shift | 10.1186/s40168-023-01565-3 (Jun 2023) | “Carbon monoxide, a ferredoxin hydrogenase inhibitor, produced identical fermentation shifts” (campbell2023h2generatedby pages 7-9) | Strong causal support for hydrogenase-mediated feedback; assay-specific |
| methanogen H2 consumption (Methanobrevibacter smithii) | lowers | H2 concentration | 10.1186/s40168-023-01565-3 (Jun 2023) | Addition of M. smithii “consumed H2 and decreased its concentration” (campbell2023h2generatedby pages 9-11) | Strong but community-context specific |
| methanogen H2 consumption | decreases/changes | butyrate production and butyrate-producer fitness | 10.1186/s40168-023-01565-3 (Jun 2023) | M. smithii “decreased both H2 concentration and butyrate production” and altered competitive fitness (campbell2023h2generatedby pages 1-2, campbell2023h2generatedby pages 9-11, campbell2023h2generatedby pages 11-12) | Strong community-level causal edge; not intrinsic single-organism trait |
| acidic pH (~5.5–6.0) | enriches / selectively favors | Clostridium spp. and suppresses methanogens | 10.3390/su162310755 (Dec 2024) | “Acidic pH (5.5–6.0) selectively enriched Clostridium spp. while inhibiting methanogens” (jalil2024impactofsubstrates pages 10-11, jalil2024impactofsubstrates pages 1-2) | Process/meta-analysis level; moderate confidence, partly aggregated across studies |
| acetate fermentation branch | associates with theoretical yield of | 4 mol H2/mol glucose | 10.3390/su162310755 (Dec 2024) | “the acetate pathway yields 4 moles H2/mole glucose” (jalil2024impactofsubstrates pages 5-7) | Canonical stoichiometric association; high confidence |
| butyrate fermentation branch | associates with theoretical yield of | 2 mol H2/mol glucose | 10.3390/su162310755 (Dec 2024); 10.3390/methane3030029 (Sep 2024) | “butyrate yields 2 moles H2/mole glucose”; review snippet notes “2 mol of bioH2 per mol of glucose” (jalil2024impactofsubstrates pages 5-7) | Canonical stoichiometric association; high confidence |
| thermophilic dark fermentation on lignocellulose/industrial residues | enables | real-world biohydrogen production implementations | 10.3390/ijms25147685 (Jul 2024) | C. saccharolyticus produced “2.9–3.4 moles of hydrogen per mole of hexose”; cassava pulp gave “760 mL/L at 60°C”; membrane bioreactors improved C. thermocellum yields (gallo2024theundeniablepotential pages 5-7, gallo2024theundeniablepotential pages 4-5, gallo2024theundeniablepotential pages 3-4) | Application/process evidence; high confidence for implementation, not direct graph edge |
| HydABC ([FeFe]-hydrogenase complex) | experimentally catalyzes | H2 oxidation coupled to NAD(P)+ and ferredoxin reduction | 10.1021/jacs.2c11683 (Feb 2023) | HydABC “oxidizes H2 gas to reduce both NAD(P)+ and low-potential ferredoxins” and catalyzes electron bifurcation from H2 to Fd and NAD(P)+ (katsyv2023molecularbasisof pages 1-2, katsyv2023molecularbasisof pages 2-3, katsyv2023molecularbasisof pages 3-4) | **Caveat / do-not-overcurate**: direct 2023 evidence is reverse direction, so do not assert generic H2-production edge from HydABC without organism-specific physiological support |


*Table: This table summarizes curator-ready candidate causal edges for fermentative hydrogen production (traitmech:000109), including core metabolic steps, regulatory and environmental modifiers, and explicit caveats for taxon-specific or reverse-direction evidence.*

## Mechanistic interpretation

### Core ferredoxin route

PFOR oxidizes pyruvate and produces acetyl-CoA, CO2, and reduced ferredoxin; the reported standard free-energy change for the pyruvate oxidation step is −13 kJ/mol. Reduced ferredoxin can then supply low-potential electrons to a proton-reducing hydrogenase, regenerating oxidized ferredoxin while evolving H2. This is the cleanest generic causal backbone for strict anaerobes. (buckel2021energyconservationin pages 11-12, hackmann2024thevastlandscape pages 12-13)

For bifurcating/confurcating enzymes, directionality must be represented explicitly. The 2023 HydABC structural study directly measured **H2 oxidation**, not physiological H2 production: HydABC from *Acetobacterium woodii* and *Thermoanaerobacter kivui* reduced NAD(P)+ and low-potential ferredoxin (E0′ approximately −450 mV). Activities were 4.1 ± 0.7 and 20.5 ± 2.8 U mg−1, respectively. Reduction of a nearby Fe–S cluster increased NAD(P)+ affinity about 15-fold, from Kd 69.6 to 4.6 µM, while redox-driven conformational gating limited electron backflow. These findings establish reversibility-capable molecular machinery but do not, by themselves, justify an edge `HydABC produces H2` in either organism. (katsyv2023molecularbasisof pages 5-7, katsyv2023molecularbasisof pages 1-2, katsyv2023molecularbasisof pages 2-3)

### Formate route

In mixed-acid fermentation, PFL cleaves pyruvate to acetyl-CoA and formate. In *E. coli*, FocA mediates bidirectional formate transport; accumulated/re-imported formate activates FhlA, which induces the formate regulon. Fdh-H oxidizes formate, transfers electrons through FHL to Hyd-3 or the alternative Hyd-4 architecture, and proton reduction produces H2. The net transformation is formate/formic acid → CO2 + H2. (sawers2025howfocafacilitates pages 1-3, bagramyan2003structuralandfunctional pages 1-3, crable2011formateformationand pages 2-3)

This branch has unusually strong engineering evidence: deletion of H2-oxidizing hydrogenase genes `hyaB` and `hybC`, deletion of the FHL repressor `hycA`, and increased `fhlA` expression produced a reported 141-fold increase over wild-type formate-dependent H2 production in bench experiments; the mutations themselves accounted for an 80-fold increase in production rate. This is compelling evidence for the FHL regulatory module but remains *E. coli*-specific. (crable2011formateformationand pages 4-6)

## Environmental and experimental modifiers

- **H2 partial pressure:** elevated H2 opposes net H2 evolution and redirects reducing equivalents. In *R. intestinalis* and *E. rectale*, effects were dose-dependent up to 3 atm and shifted metabolism away from acetate toward butyrate, lactate, and formate; CO inhibition phenocopied high H2. A hydrogenase-negative *F. prausnitzii* strain did not respond, strengthening causal attribution to hydrogenase. (campbell2023h2generatedby pages 7-9, campbell2023h2generatedby pages 2-4)
- **Hydrogenotrophs:** adding *M. smithii* consumed H2 and reduced butyrate in synthetic gut communities. Vigorous shaking, which removed local H2 disequilibrium, abolished the effect. In vivo relevance is plausible because measured dissolved gut H2 can be 3–100 times higher than headspace-equilibrium predictions. (campbell2023h2generatedby pages 9-11)
- **Anaerobiosis/electron acceptors:** the *E. coli* FHL pathway is induced under anaerobic fermentative conditions; H2 evolution stops on addition of O2 or nitrate. Thus oxygen and nitrate are strong negative context edges for this branch, but their effects are architecture-specific. (sawers2025howfocafacilitates pages 3-5)
- **pH:** recent aggregate analysis identifies pH 5.5–6.0 as favorable for many dark-fermentation systems, enriching clostridia and suppressing methanogens. However, individual components can respond differently; *E. coli* FHL-1 production increases below pH 6.5 even though isolated FDH-H activity was reported to decline from pH 7.5 to 6.0. Curate pH against the whole phenotype only with organism and assay specified. (sawers2025howfocafacilitates pages 5-7, bagramyan2003structuralandfunctional pages 1-3, jalil2024impactofsubstrates pages 10-11)
- **Temperature:** thermophilic operation can favor *Thermotoga* and suppress methanogens. A 2024 meta-analysis associated temperature strongly with H2 production (p=0.001, r=0.82) and reported approximately 25% higher output above 65°C than in mesophilic systems, but these are aggregate, not universal causal effects. (jalil2024impactofsubstrates pages 10-11)
- **Product branches:** canonical stoichiometry is 4 mol H2/mol glucose for acetate-type fermentation and 2 mol H2/mol glucose for butyrate-type fermentation. Lactate, ethanol, and other reduced products divert reducing equivalents away from H2; nevertheless, VFA abundance is an observational process marker rather than a universally causal activator. (jalil2024impactofsubstrates pages 5-7)

## Recent research, applications, and quantitative evidence

### 2023–2024 developments

1. **Molecular mechanism:** the 2023 HydABC study resolved how FMN and multiple Fe–S clusters couple an exergonic NAD(P)+ branch to an endergonic ferredoxin branch. The complex is a `(HydABC)2` dimer, with reported masses of 306 kDa in *A. woodii* and 348 kDa in *T. kivui*. This advances enzyme-level understanding but chiefly characterizes H2 oxidation. (katsyv2023molecularbasisof pages 1-2, katsyv2023molecularbasisof pages 2-3)
2. **Ecological feedback:** Campbell et al. established that H2 is not merely an end product; its concentration feeds back through hydrogenase to control carbon and reducing-equivalent allocation in gut fermenters. Under high H2, *E. rectale* lost approximately half its ATP formation per glucose when metabolism shifted toward lactate. (campbell2023h2generatedby pages 11-12)
3. **Systems-scale fermentation diversity:** Hackmann’s 2024 review formalized proton reduction to H2 within fermentation and documented the breadth of prokaryotic fermentation chemistry. (hackmann2024thevastlandscape pages 2-3, hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 5-6)
4. **Process meta-analysis:** Jalil and Yu reported a cross-study mean of 168.57 ± 52.09 mL H2/g substrate. Substrate-specific means were 205 mL/g for food waste, 191.8 mL/g for glucose, and 108.90 mL/g for mixed food waste; substrate effects were significant, `F(2,5)=15.32`, p<0.05. Acetate and butyrate correlated with H2 yield at r=0.75 and r=0.68, respectively (both p<0.01). These data combine heterogeneous configurations and some microbial-electrolysis observations, so they should inform process context, not intrinsic single-organism edges. (jalil2024impactofsubstrates pages 1-2, jalil2024impactofsubstrates pages 16-18, jalil2024impactofsubstrates pages 5-7)

### Current implementations

Thermophilic dark fermentation is being implemented experimentally with lignocellulose, food-industry residues, and waste effluents. *C. saccharolyticus* produced 2.9–3.4 mol H2/mol hexose from cellulose, corresponding to 74–85% of the four-mole theoretical maximum. Untreated cassava pulp yielded 760 mL H2/L at 60°C. For *C. thermocellum*, membrane-bioreactor operation increased cumulative H2 from 25.8 to 42.1 mmol on cellobiose and from 46.8 to 74.6 mmol on Avicel. Nickel-ferrite nanoparticles were reported to improve yield by approximately 28.3%. (gallo2024theundeniablepotential pages 5-7, gallo2024theundeniablepotential pages 4-5, gallo2024theundeniablepotential pages 3-4)

The authoritative 2024 assessment remains cautious: high-temperature reactors require specialized designs, yields and stability still need improvement, and commercial-scale deployment is incomplete. Accordingly, “industrial biohydrogen production” should be described as an application target or pilot/laboratory implementation, not an established widespread commercial phenotype. (gallo2024theundeniablepotential pages 5-7)

## Recommended minimal graph

For a compact first revision beyond the existing seven-node/six-edge graph, prioritize:

1. `pyruvate` → **oxidized by PFOR to produce** → `acetyl-CoA + CO2 + reduced ferredoxin`
2. `reduced ferredoxin` → **donates electrons to** → `proton-reducing hydrogenase`
3. `proton-reducing hydrogenase` → **reduces protons to produce** → `molecular hydrogen`
4. `pyruvate` → **cleaved by PFL to produce** → `acetyl-CoA + formate`
5. `formate-hydrogenlyase` → **converts formate to** → `molecular hydrogen + CO2`
6. `elevated H2 partial pressure` → **inhibits net** → `fermentative hydrogen production`
7. `anaerobic conditions` → **enable** → `fermentative hydrogen production`

Represent the PFOR/hydrogenase and PFL/FHL routes as alternatives rather than requiring every positive organism to possess both. Place FocA/FhlA/HycA under an *E. coli* taxon restriction. Keep methanogen removal of H2, pH, temperature, reactor architecture, and substrate pretreatment in an optional contextual layer.

## Warnings: claims not ready for TraitMech curation

1. **Do not curate HydABC generically as H2-producing from the 2023 structural paper.** Its direct reaction was H2 oxidation to reduced ferredoxin and NAD(P)H. Reverse/confurcating H2 evolution requires organism-specific physiological evidence. (katsyv2023molecularbasisof pages 1-2, katsyv2023molecularbasisof pages 3-4)
2. **Do not treat all hydrogenase genes as sufficient for the phenotype.** Directionality, maturation, electron donors, expression, H2 partial pressure, and competing sinks matter.
3. **Do not universalize FocA–FhlA–FHL regulation.** This is a well-supported *E. coli*/enterobacterial module, not the generic clostridial mechanism. (sawers2025howfocafacilitates pages 1-3, sawers2025howfocafacilitates pages 3-5)
4. **Do not curate acetate or butyrate concentration as a direct activator based only on meta-analysis.** Their positive correlations with H2 are process associations and partly reflect pathway stoichiometry. (jalil2024impactofsubstrates pages 1-2, jalil2024impactofsubstrates pages 16-18)
5. **Do not import the reported 25% benefit from methanogen inhibitors as a dark-fermentation edge.** The cited aggregate explicitly includes microbial electrolysis systems. (jalil2024impactofsubstrates pages 1-2)
6. **Do not encode a universal optimal pH or temperature.** Values around pH 5.5–6.0 and 65–75°C are process-level optima for selected communities and thermophiles, not defining properties of the trait. (jalil2024impactofsubstrates pages 10-11, jalil2024impactofsubstrates pages 15-16)
7. **Do not infer phenotype from `hydA` alone.** [FeFe]-hydrogenases require maturation machinery and may operate in uptake or evolution directions depending on context.
8. **Avoid composite CURIE invention.** Multi-subunit complexes, organism-specific protein records, pathway variants, and reduced-ferredoxin states may remain label-only until verified against UniProt, Rhea, GO, or the project’s preferred ontology release.

## DOI-first bibliography

1. Hackmann TJ. “The vast landscape of carbohydrate fermentation in prokaryotes.” *FEMS Microbiology Reviews*. Published May 2024. DOI: [10.1093/femsre/fuae016](https://doi.org/10.1093/femsre/fuae016). (hackmann2024thevastlandscape pages 1-2)
2. Jalil A, Yu Z. “Impact of Substrates, Volatile Fatty Acids, and Microbial Communities on Biohydrogen Production: A Systematic Review and Meta-Analysis.” *Sustainability* 16:10755. Published December 2024. DOI: [10.3390/su162310755](https://doi.org/10.3390/su162310755). (jalil2024impactofsubstrates pages 1-2)
3. Gallo G, Imbimbo P, Aulitto M. “The Undeniable Potential of Thermophiles in Industrial Processes.” *International Journal of Molecular Sciences* 25:7685. Published July 2024. DOI: [10.3390/ijms25147685](https://doi.org/10.3390/ijms25147685). (gallo2024theundeniablepotential pages 5-7)
4. Albuquerque MM et al. “Biohydrogen Produced via Dark Fermentation: A Review.” *Methane* 3:500–532. Published September 2024. DOI: [10.3390/methane3030029](https://doi.org/10.3390/methane3030029).
5. Katsyv A et al. “Molecular Basis of the Electron Bifurcation Mechanism in the [FeFe]-Hydrogenase Complex HydABC.” *Journal of the American Chemical Society* 145:5696–5709. Published February 2023. DOI: [10.1021/jacs.2c11683](https://doi.org/10.1021/jacs.2c11683). (katsyv2023molecularbasisof pages 5-7, katsyv2023molecularbasisof pages 2-3)
6. Campbell A et al. “H2 generated by fermentation in the human gut microbiome influences metabolism and competitive fitness of gut butyrate producers.” *Microbiome* 11. Published June 2023. DOI: [10.1186/s40168-023-01565-3](https://doi.org/10.1186/s40168-023-01565-3). (campbell2023h2generatedby pages 1-2)
7. Buckel W. “Energy Conservation in Fermentations of Anaerobic Bacteria.” *Frontiers in Microbiology* 12. Published September 2021. DOI: [10.3389/fmicb.2021.703525](https://doi.org/10.3389/fmicb.2021.703525). (buckel2021energyconservationin pages 1-2)
8. Crable BR et al. “Formate Formation and Formate Conversion in Biological Fuels Production.” *Enzyme Research* 2011:532536. Published May 2011. DOI: [10.4061/2011/532536](https://doi.org/10.4061/2011/532536). (crable2011formateformationand pages 2-3, crable2011formateformationand pages 4-6)
9. Bagramyan K, Trchounian A. “Structural and Functional Features of Formate Hydrogen Lyase, an Enzyme of Mixed-Acid Fermentation from *Escherichia coli*.” *Biochemistry (Moscow)* 68:1159–1170. Published November 2003. DOI: [10.1023/B:BIRY.0000009129.18714.A4](https://doi.org/10.1023/B:BIRY.0000009129.18714.A4). (bagramyan2003structuralandfunctional pages 1-3)
10. Hallenbeck PC, Benemann JR. “Biological hydrogen production; fundamentals and limiting processes.” *International Journal of Hydrogen Energy*. Published 2002. DOI: [10.1016/S0360-3199(02)00131-3](https://doi.org/10.1016/S0360-3199(02)00131-3).

References

1. (hackmann2024thevastlandscape pages 2-3): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 27 citations and is from a domain leading peer-reviewed journal.

2. (hackmann2024thevastlandscape pages 1-2): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 27 citations and is from a domain leading peer-reviewed journal.

3. (hackmann2024thevastlandscape pages 5-6): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 27 citations and is from a domain leading peer-reviewed journal.

4. (buckel2021energyconservationin pages 1-2): Wolfgang Buckel. Energy conservation in fermentations of anaerobic bacteria. Frontiers in Microbiology, Sep 2021. URL: https://doi.org/10.3389/fmicb.2021.703525, doi:10.3389/fmicb.2021.703525. This article has 139 citations and is from a peer-reviewed journal.

5. (buckel2021energyconservationin pages 3-4): Wolfgang Buckel. Energy conservation in fermentations of anaerobic bacteria. Frontiers in Microbiology, Sep 2021. URL: https://doi.org/10.3389/fmicb.2021.703525, doi:10.3389/fmicb.2021.703525. This article has 139 citations and is from a peer-reviewed journal.

6. (buckel2021energyconservationin pages 4-6): Wolfgang Buckel. Energy conservation in fermentations of anaerobic bacteria. Frontiers in Microbiology, Sep 2021. URL: https://doi.org/10.3389/fmicb.2021.703525, doi:10.3389/fmicb.2021.703525. This article has 139 citations and is from a peer-reviewed journal.

7. (campbell2023h2generatedby pages 1-2): Austin Campbell, Kristi Gdanetz, Alexander W. Schmidt, and Thomas M. Schmidt. H2 generated by fermentation in the human gut microbiome influences metabolism and competitive fitness of gut butyrate producers. Microbiome, Jun 2023. URL: https://doi.org/10.1186/s40168-023-01565-3, doi:10.1186/s40168-023-01565-3. This article has 87 citations and is from a highest quality peer-reviewed journal.

8. (campbell2023h2generatedby pages 7-9): Austin Campbell, Kristi Gdanetz, Alexander W. Schmidt, and Thomas M. Schmidt. H2 generated by fermentation in the human gut microbiome influences metabolism and competitive fitness of gut butyrate producers. Microbiome, Jun 2023. URL: https://doi.org/10.1186/s40168-023-01565-3, doi:10.1186/s40168-023-01565-3. This article has 87 citations and is from a highest quality peer-reviewed journal.

9. (buckel2021energyconservationin pages 11-12): Wolfgang Buckel. Energy conservation in fermentations of anaerobic bacteria. Frontiers in Microbiology, Sep 2021. URL: https://doi.org/10.3389/fmicb.2021.703525, doi:10.3389/fmicb.2021.703525. This article has 139 citations and is from a peer-reviewed journal.

10. (hackmann2024thevastlandscape pages 12-13): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 27 citations and is from a domain leading peer-reviewed journal.

11. (crable2011formateformationand pages 2-3): Bryan R. Crable, Caroline M. Plugge, Michael J. McInerney, and Alfons J. M. Stams. Formate formation and formate conversion in biological fuels production. Enzyme Research, 2011:1-8, May 2011. URL: https://doi.org/10.4061/2011/532536, doi:10.4061/2011/532536. This article has 103 citations.

12. (sawers2025howfocafacilitates pages 1-3): R. Gary Sawers. How foca facilitates fermentation and respiration of formate by <i>escherichia coli</i>. Feb 2025. URL: https://doi.org/10.1128/jb.00502-24, doi:10.1128/jb.00502-24. This article has 18 citations and is from a peer-reviewed journal.

13. (sawers2025howfocafacilitates pages 3-5): R. Gary Sawers. How foca facilitates fermentation and respiration of formate by <i>escherichia coli</i>. Feb 2025. URL: https://doi.org/10.1128/jb.00502-24, doi:10.1128/jb.00502-24. This article has 18 citations and is from a peer-reviewed journal.

14. (crable2011formateformationand pages 4-6): Bryan R. Crable, Caroline M. Plugge, Michael J. McInerney, and Alfons J. M. Stams. Formate formation and formate conversion in biological fuels production. Enzyme Research, 2011:1-8, May 2011. URL: https://doi.org/10.4061/2011/532536, doi:10.4061/2011/532536. This article has 103 citations.

15. (bagramyan2003structuralandfunctional pages 1-3): K. Bagramyan and A. Trchounian. Structural and functional features of formate hydrogen lyase, an enzyme of mixed-acid fermentation from escherichia coli. Biochemistry (Moscow), 68:1159-1170, Nov 2003. URL: https://doi.org/10.1023/b:biry.0000009129.18714.a4, doi:10.1023/b:biry.0000009129.18714.a4. This article has 162 citations.

16. (campbell2023h2generatedby pages 2-4): Austin Campbell, Kristi Gdanetz, Alexander W. Schmidt, and Thomas M. Schmidt. H2 generated by fermentation in the human gut microbiome influences metabolism and competitive fitness of gut butyrate producers. Microbiome, Jun 2023. URL: https://doi.org/10.1186/s40168-023-01565-3, doi:10.1186/s40168-023-01565-3. This article has 87 citations and is from a highest quality peer-reviewed journal.

17. (campbell2023h2generatedby pages 9-11): Austin Campbell, Kristi Gdanetz, Alexander W. Schmidt, and Thomas M. Schmidt. H2 generated by fermentation in the human gut microbiome influences metabolism and competitive fitness of gut butyrate producers. Microbiome, Jun 2023. URL: https://doi.org/10.1186/s40168-023-01565-3, doi:10.1186/s40168-023-01565-3. This article has 87 citations and is from a highest quality peer-reviewed journal.

18. (campbell2023h2generatedby pages 11-12): Austin Campbell, Kristi Gdanetz, Alexander W. Schmidt, and Thomas M. Schmidt. H2 generated by fermentation in the human gut microbiome influences metabolism and competitive fitness of gut butyrate producers. Microbiome, Jun 2023. URL: https://doi.org/10.1186/s40168-023-01565-3, doi:10.1186/s40168-023-01565-3. This article has 87 citations and is from a highest quality peer-reviewed journal.

19. (jalil2024impactofsubstrates pages 10-11): Anam Jalil and Zhisheng Yu. Impact of substrates, volatile fatty acids, and microbial communities on biohydrogen production: a systematic review and meta-analysis. Sustainability, 16:10755, Dec 2024. URL: https://doi.org/10.3390/su162310755, doi:10.3390/su162310755. This article has 35 citations.

20. (jalil2024impactofsubstrates pages 1-2): Anam Jalil and Zhisheng Yu. Impact of substrates, volatile fatty acids, and microbial communities on biohydrogen production: a systematic review and meta-analysis. Sustainability, 16:10755, Dec 2024. URL: https://doi.org/10.3390/su162310755, doi:10.3390/su162310755. This article has 35 citations.

21. (jalil2024impactofsubstrates pages 5-7): Anam Jalil and Zhisheng Yu. Impact of substrates, volatile fatty acids, and microbial communities on biohydrogen production: a systematic review and meta-analysis. Sustainability, 16:10755, Dec 2024. URL: https://doi.org/10.3390/su162310755, doi:10.3390/su162310755. This article has 35 citations.

22. (gallo2024theundeniablepotential pages 5-7): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 26 citations.

23. (gallo2024theundeniablepotential pages 4-5): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 26 citations.

24. (gallo2024theundeniablepotential pages 3-4): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 26 citations.

25. (katsyv2023molecularbasisof pages 1-2): Alexander Katsyv, Anuj Kumar, Patricia Saura, Maximilian C. Pöverlein, Sven A. Freibert, Sven T. Stripp, Surbhi Jain, Ana P. Gamiz-Hernandez, Ville R. I. Kaila, Volker Müller, and Jan M. Schuller. Molecular basis of the electron bifurcation mechanism in the [fefe]-hydrogenase complex hydabc. Journal of the American Chemical Society, 145:5696-5709, Feb 2023. URL: https://doi.org/10.1021/jacs.2c11683, doi:10.1021/jacs.2c11683. This article has 78 citations and is from a highest quality peer-reviewed journal.

26. (katsyv2023molecularbasisof pages 2-3): Alexander Katsyv, Anuj Kumar, Patricia Saura, Maximilian C. Pöverlein, Sven A. Freibert, Sven T. Stripp, Surbhi Jain, Ana P. Gamiz-Hernandez, Ville R. I. Kaila, Volker Müller, and Jan M. Schuller. Molecular basis of the electron bifurcation mechanism in the [fefe]-hydrogenase complex hydabc. Journal of the American Chemical Society, 145:5696-5709, Feb 2023. URL: https://doi.org/10.1021/jacs.2c11683, doi:10.1021/jacs.2c11683. This article has 78 citations and is from a highest quality peer-reviewed journal.

27. (katsyv2023molecularbasisof pages 3-4): Alexander Katsyv, Anuj Kumar, Patricia Saura, Maximilian C. Pöverlein, Sven A. Freibert, Sven T. Stripp, Surbhi Jain, Ana P. Gamiz-Hernandez, Ville R. I. Kaila, Volker Müller, and Jan M. Schuller. Molecular basis of the electron bifurcation mechanism in the [fefe]-hydrogenase complex hydabc. Journal of the American Chemical Society, 145:5696-5709, Feb 2023. URL: https://doi.org/10.1021/jacs.2c11683, doi:10.1021/jacs.2c11683. This article has 78 citations and is from a highest quality peer-reviewed journal.

28. (katsyv2023molecularbasisof pages 5-7): Alexander Katsyv, Anuj Kumar, Patricia Saura, Maximilian C. Pöverlein, Sven A. Freibert, Sven T. Stripp, Surbhi Jain, Ana P. Gamiz-Hernandez, Ville R. I. Kaila, Volker Müller, and Jan M. Schuller. Molecular basis of the electron bifurcation mechanism in the [fefe]-hydrogenase complex hydabc. Journal of the American Chemical Society, 145:5696-5709, Feb 2023. URL: https://doi.org/10.1021/jacs.2c11683, doi:10.1021/jacs.2c11683. This article has 78 citations and is from a highest quality peer-reviewed journal.

29. (sawers2025howfocafacilitates pages 5-7): R. Gary Sawers. How foca facilitates fermentation and respiration of formate by <i>escherichia coli</i>. Feb 2025. URL: https://doi.org/10.1128/jb.00502-24, doi:10.1128/jb.00502-24. This article has 18 citations and is from a peer-reviewed journal.

30. (jalil2024impactofsubstrates pages 16-18): Anam Jalil and Zhisheng Yu. Impact of substrates, volatile fatty acids, and microbial communities on biohydrogen production: a systematic review and meta-analysis. Sustainability, 16:10755, Dec 2024. URL: https://doi.org/10.3390/su162310755, doi:10.3390/su162310755. This article has 35 citations.

31. (jalil2024impactofsubstrates pages 15-16): Anam Jalil and Zhisheng Yu. Impact of substrates, volatile fatty acids, and microbial communities on biohydrogen production: a systematic review and meta-analysis. Sustainability, 16:10755, Dec 2024. URL: https://doi.org/10.3390/su162310755, doi:10.3390/su162310755. This article has 35 citations.