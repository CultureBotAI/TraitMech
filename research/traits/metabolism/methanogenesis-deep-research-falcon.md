---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:33:30.875040'
end_time: '2026-08-04T06:43:52.755207'
duration_seconds: 621.88
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Methanogenesis
  trait_identifier: METPO:1000844
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: methanogenesis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which methane is produced as the primary end product
    through the reduction of carbon-containing compounds, formate, methanol, or acetate,
    exclusively performed by methanogenic archaea under strictly anaerobic conditions.
  parent_traits: METPO:1000060
  synonyms: Biological methanation, Biomethanation, Carbonate respiration
  evidence_summary: 'DOI:10.1146/annurev-micro-011720-122807: from CO2 and H2 to methane
    (Supports hydrogenotrophic methanogenesis as a methane-producing archaeal pathway.)
    | DOI:10.1021/acs.biochem.9b00164: catalyzes the reversible reduction of methyl-coenzyme
    M (Supports methyl-coenzyme M reductase as the terminal methane-forming enzyme.)'
  causal_graph_summary: 'methanogenesis_c1_reduction: 15 nodes, 11 edges'
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
- **Trait label:** Methanogenesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000844
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which methane is produced as the primary end product through the reduction of carbon-containing compounds, formate, methanol, or acetate, exclusively performed by methanogenic archaea under strictly anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** Biological methanation, Biomethanation, Carbonate respiration
- **Existing evidence:** DOI:10.1146/annurev-micro-011720-122807: from CO2 and H2 to methane (Supports hydrogenotrophic methanogenesis as a methane-producing archaeal pathway.) | DOI:10.1021/acs.biochem.9b00164: catalyzes the reversible reduction of methyl-coenzyme M (Supports methyl-coenzyme M reductase as the terminal methane-forming enzyme.)
- **Existing causal graph summary:** methanogenesis_c1_reduction: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **Methanogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/methanogenesis.yaml`.

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
- **Trait label:** Methanogenesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000844
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which methane is produced as the primary end product through the reduction of carbon-containing compounds, formate, methanol, or acetate, exclusively performed by methanogenic archaea under strictly anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** Biological methanation, Biomethanation, Carbonate respiration
- **Existing evidence:** DOI:10.1146/annurev-micro-011720-122807: from CO2 and H2 to methane (Supports hydrogenotrophic methanogenesis as a methane-producing archaeal pathway.) | DOI:10.1021/acs.biochem.9b00164: catalyzes the reversible reduction of methyl-coenzyme M (Supports methyl-coenzyme M reductase as the terminal methane-forming enzyme.)
- **Existing causal graph summary:** methanogenesis_c1_reduction: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **Methanogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/methanogenesis.yaml`.

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


# Methanogenesis (`METPO:1000844`): TraitMech curation report

## Executive summary

**Methanogenesis** is the net anaerobic biological production of methane by methanogenic archaea. For TraitMech, the class should cover hydrogenotrophic, acetoclastic/aceticlastic, methylotrophic, and H₂-dependent methyl-reducing routes. These routes differ in substrate entry and electron supply but converge on methyl-coenzyme M (methyl-S-CoM), whose reduction by methyl-coenzyme M reductase (MCR) is the terminal methane-forming reaction. The reviewed trait identifier should be retained verbatim as **`METPO:1000844`**, with parent **`METPO:1000060`** and category **METABOLISM**. (borrel2013phylogenomicdatasupport pages 1-2, thauer2019methyl(alkyl)coenzymem pages 1-2)

The recommended graph backbone is therefore:

**anaerobic environment + methanogenic archaeon + pathway-specific substrate/electron donor → methyl-S-CoM → MCR reaction → CH₄**, with heterodisulfide reductase recycling coenzymes M and B. Environmental controls such as H₂ availability, competing electron acceptors, temperature, substrate loading, and inhibitors should be represented as regulatory/contextual branches rather than defining reactions. (thauer2019methyl(alkyl)coenzymem pages 1-2, yang2022effectofbiochar pages 81-86, tveit2015fromthecover pages 1-2, mackie2024—invitedreview pages 1-2)

## 1. Trait scope and boundaries

### 1.1 Included phenotype

The trait denotes a **physiological capacity for net methane production**, not merely possession of a marker gene. Its direct assay-level readout is methane accumulation or production rate under anoxic conditions with an appropriate substrate and controls. Classical routes are:

1. **Hydrogenotrophic methanogenesis:** CO₂ is reduced through formyl-, methenyl-, methylene-, and methyl-level C1 intermediates; H₂ supplies reducing equivalents. Formate can also support this metabolism in organisms able to oxidize it to provide electrons and CO₂.
2. **Acetoclastic methanogenesis:** acetate is activated and cleaved; its methyl carbon is transferred through the methanogenic carrier system to methyl-S-CoM, while oxidation of the carboxyl carbon supplies reducing equivalents.
3. **Methylotrophic methanogenesis:** substrate-specific methyltransferases transfer methyl groups from methanol, methylamines, or methyl sulfides to CoM.
4. **H₂-dependent methyl-reducing methanogenesis:** external H₂ supplies the reducing equivalents for reduction of methyl compounds; this is characteristic of Methanomassiliicoccales and related organisms. (borrel2013phylogenomicdatasupport pages 1-2)

All four route classes converge on MCR. MCR is an α₂β₂γ₂-type complex built from McrA, McrB, and McrG subunits and uses nickel-containing coenzyme F₄₃₀. It reduces methyl-S-CoM with coenzyme B to methane and CoM-S-S-CoB; Hdr subsequently regenerates the free thiols. (thauer2019methyl(alkyl)coenzymem pages 1-2)

### 1.2 Boundary cases

- **Anaerobic methane oxidation (AOM) is not methanogenesis.** MCR homologues also catalyze the first step of methane oxidation in ANME archaea. Methanogen MCR can run in reverse in vitro, although the reported oxidation activity is only about 0.01% of its methane-formation rate; enzyme presence therefore does not determine net physiological direction. (dinh2024towardtheuse pages 2-4)
- **Alkyl-CoM reductase-mediated ethane, propane, or butane activation is not this trait.** Divergent ACRs are related to MCR but support anaerobic non-methane alkane metabolism. Claims that such enzymes produce alkanes remain partly prospective and should not be folded into `METPO:1000844`. (sarno2024beyondmethanenew pages 1-3)
- **Methanotrophy is distinct.** Methane-consuming bacteria or archaea should not be assigned the methanogenesis trait without independent evidence of net methane formation. mcrA can occur in methane oxidizers, and nitrate reduction or N₂ production alone does not prove methane-dependent metabolism. (ahmadi2024recentfindingsin pages 2-4)
- **Anaerobic digestion is broader than methanogenesis.** Hydrolysis, acidogenesis, acetogenesis, syntrophy, and fermentation furnish methanogenic substrates but are upstream community processes, not themselves instances of the trait.
- **Methane accumulation alone is not taxonomic proof.** Abiotic methane, carry-over methane, and methane produced by another consortium member must be excluded. Appropriate no-cell, killed, substrate-free, and inhibitor controls are needed.
- **“Exclusively Euryarchaeota” is historically useful but taxonomically outdated as a rigid graph constraint.** Recent phylogenomic work finds canonical and divergent MCR systems across broader archaeal lineages; curate the producer as Archaea/methanogenic archaeon and add narrower taxonomic scope only when the source demonstrates it. (sarno2024beyondmethanenew pages 1-3)

## 2. Candidate nodes grouped by type

### 2.1 Trait and pathway/process nodes

- Methanogenesis — **`METPO:1000844`**
- Hydrogenotrophic methanogenesis — label-only candidate
- Acetoclastic/aceticlastic methanogenesis — label-only candidate
- Methylotrophic methanogenesis — label-only candidate
- H₂-dependent methyl-reducing methanogenesis — label-only candidate
- CO₂ reduction to methyl-S-CoM — label-only candidate
- Terminal methane formation — label-only candidate
- CoM/CoB heterodisulfide recycling — label-only candidate
- Anaerobic digestion — contextual process, not synonymous with the trait
- Direct interspecies electron transfer — contextual process; curate only with system-specific evidence
- Anaerobic methane oxidation — explicit exclusion/contrast node

### 2.2 Chemicals and cofactors

Conservative candidate grounding includes methane **CHEBI:16183**, carbon dioxide **CHEBI:16526**, dihydrogen **CHEBI:18276**, acetate **CHEBI:30089**, methanol **CHEBI:17790**, and formate **CHEBI:15740**. Other important label-only candidates are methyl-S-CoM, coenzyme M/HS-CoM, coenzyme B/HS-CoB, CoM-S-S-CoB, methanofuran, tetrahydromethanopterin/H₄MPT, coenzyme F₄₂₀, coenzyme F₄₃₀, ferredoxin, methylamines, and dimethyl sulfide. Exact ChEBI records for protonation states and conjugates should be resolved during implementation rather than inferred from names.

### 2.3 Enzymes, genes, and complexes

- Methyl-coenzyme M reductase; genes **mcrA, mcrB, mcrG**; **EC:2.8.4.1**
- Heterodisulfide reductase, especially soluble **HdrABC**; label-only pending complex-specific grounding
- Formylmethanofuran dehydrogenase, **Fwd/Fmd**
- Formylmethanofuran:H₄MPT formyltransferase, **Ftr**
- Methenyl-H₄MPT cyclohydrolase, **Mch**
- F₄₂₀-dependent methylene-H₄MPT dehydrogenase, **Mtd**
- H₂-forming methylene-H₄MPT dehydrogenase, **Hmd**
- F₄₂₀-dependent methylene-H₄MPT reductase, **Mer**
- Methyl-H₄MPT:CoM methyltransferase, **Mtr** complex; **EC:2.1.1.86** is supported in the recent co-digestion study
- F₄₂₀-reducing hydrogenase, **Frh**; **EC:1.12.98.1**
- Mvh hydrogenase–Hdr electron-bifurcating complex
- Methanol methyltransferase **MtaABC**
- Monomethylamine system **MtmBC/MtbA**
- Dimethylamine system **MtbBC/MtbA**
- Trimethylamine system **MttBC/MtbA**
- Dimethyl-sulfide system **MtsA/MtsB** (thauer2019methyl(alkyl)coenzymem pages 1-2, borrel2013phylogenomicdatasupport pages 1-2)

The 2024 coal–straw study additionally reports enrichment of enzymes annotated as **EC:1.2.99.5**, **EC:2.1.1.86**, and **EC:1.12.98.1** in its methane-producing treatment. This supports context-specific pathway association, but abundance is not equivalent to catalytic flux. (khan2024coalstrawcodigestioninducedbiogenic pages 1-2)

### 2.4 Organisms and ecological participants

Candidate taxa include Methanobacteriaceae/Methanobrevibacter for hydrogenotrophic methanogenesis, Methanosarcinaceae/Methanosarcina for metabolically versatile and acetoclastic routes, and Methanomethylophilaceae/Methanomassiliicoccales for H₂-dependent methyl-reducing metabolism. In a 2024 catalogue of 998 ruminant-gut archaeal genomes, 67.03% belonged to Methanobacteriaceae and 19.84% to Methanomethylophilaceae; pathway dependencies varied by host and strain. (mi2024ametagenomiccatalogue pages 1-2)

Fermenters, syntrophic acetate/propionate oxidizers, Geobacteraceae, sulfate reducers, nitrate reducers, and homoacetogens are contextual community nodes. They influence substrate or electron flow but should not automatically inherit the methanogenesis trait.

### 2.5 Environmental and experimental factors

- Strictly anoxic/low-redox environment
- H₂ partial pressure and formate availability
- CO₂ availability, dissolved inorganic-carbon speciation, and pH
- Acetate and methyl-compound availability
- Temperature
- Competing electron acceptors: O₂, nitrate, sulfate, and Fe(III)
- Total solids, organic loading, inoculum-to-substrate ratio, and retention time
- Conductive materials/biochar, where DIET is experimentally supported
- 2-bromoethanesulfonate (BES), 3-nitrooxypropanol, and selected halogenated inhibitors
- Gas chromatography or automated methane-potential measurements
- Stable-carbon and clumped-isotope measurements, metagenomics, transcriptomics, mcrA quantification, and enzyme assays as supporting—not individually definitive—evidence

## 3. Evidence-backed candidate edges

The compact high-confidence subset is summarized below.

| subject | predicate | object | confidence/scope | primary DOI |
|---|---|---|---|---|
| Hydrogenotrophic methanogenesis | produces | methyl-coenzyme M | High; core pathway in methanogenic archaea from CO2 with electrons from external H2; pathway-level (borrel2013phylogenomicdatasupport pages 1-2) | 10.1093/gbe/evt128 |
| Acetoclastic methanogenesis | produces | methyl-coenzyme M | High; core pathway in methanogenic archaea via acetate cleavage and methyl transfer; pathway-level (borrel2013phylogenomicdatasupport pages 1-2) | 10.1093/gbe/evt128 |
| Methylotrophic methanogenesis | produces | methyl-coenzyme M | High; core pathway in methanogenic archaea using substrate-specific methyltransferases; pathway-level (borrel2013phylogenomicdatasupport pages 1-2) | 10.1093/gbe/evt128 |
| Methyl-coenzyme M reductase | catalyzes reduction of | methyl-coenzyme M + coenzyme B to methane + CoM-S-S-CoB | High; terminal methane-forming step of methanogenesis; enzyme-level (thauer2019methyl(alkyl)coenzymem pages 1-2) | 10.1021/acs.biochem.9b00164 |
| Heterodisulfide reductase | reduces | CoM-S-S-CoB to coenzyme M + coenzyme B | High; cofactor-recycling step coupled to methanogenesis; enzyme-level (thauer2019methyl(alkyl)coenzymem pages 1-2) | 10.1021/acs.biochem.9b00164 |
| Methanol methyltransferase complex MtaABC | transfers methyl group from | methanol to coenzyme M | High; substrate-specific methylotrophic entry step; pathway-specific (borrel2013phylogenomicdatasupport pages 1-2) | 10.1093/gbe/evt128 |
| Monomethylamine methyltransferase complex MtmBC/MtbA | transfers methyl group from | monomethylamine to coenzyme M | High; substrate-specific methylotrophic entry step; pathway-specific (borrel2013phylogenomicdatasupport pages 1-2) | 10.1093/gbe/evt128 |
| Dimethylamine methyltransferase complex MtbBC/MtbA | transfers methyl group from | dimethylamine to coenzyme M | High; substrate-specific methylotrophic entry step; pathway-specific (borrel2013phylogenomicdatasupport pages 1-2) | 10.1093/gbe/evt128 |
| Trimethylamine methyltransferase complex MttBC/MtbA | transfers methyl group from | trimethylamine to coenzyme M | High; substrate-specific methylotrophic entry step; pathway-specific (borrel2013phylogenomicdatasupport pages 1-2) | 10.1093/gbe/evt128 |
| Dimethyl sulfide methyltransferase complex MtsA/MtsB | transfers methyl group from | dimethyl sulfide to coenzyme M | High; substrate-specific methylotrophic entry step; pathway-specific (borrel2013phylogenomicdatasupport pages 1-2) | 10.1093/gbe/evt128 |
| Oxygen exposure | inactivates | methyl-coenzyme M reductase activity | High; MCR is highly oxygen-sensitive; enzyme-level, mechanistic (thauer2019methyl(alkyl)coenzymem pages 1-2) | 10.1021/acs.biochem.9b00164 |
| 2-bromoethanesulfonate (BES) | inhibits | methanogenesis | High; experimental inhibitor that immediately halts CH4 production in anoxic soil microcosms; assay/context-specific (yang2022effectofbiochar pages 81-86) | 10.15496/publikation-42776 |
| Hydrogen availability | positively regulates | hydrogenotrophic methanogenesis rate | High; kinetics and energetics strongly controlled by H2 supply; environmental control (mackie2024—invitedreview pages 1-2, tyne2023identifyingandunderstanding pages 3-4) | 10.5713/ab.23.0294 |
| Competing electron acceptors (for example oxygen, nitrate, sulfate, Fe(III)) | suppress | methanogenesis | High; they divert reducing equivalents and/or outcompete H2-consuming methanogens; environmental control across rumen and anoxic soils (yang2022effectofbiochar pages 81-86, mackie2024—invitedreview pages 1-2) | 10.5713/ab.23.0294 |


*Table: This table lists compact, high-confidence causal triples for methanogenesis suitable for graph curation. It emphasizes pathway convergence, terminal methane formation, cofactor recycling, substrate-specific entry steps, and major environmental or experimental controls.*

The following expanded table supplies curation snippets and qualifications.

| # | Proposed subject–predicate–object triple | Reference | Supporting snippet | Curation note |
|---|---|---|---|---|
| 1 | hydrogenotrophic methanogenesis — **reduces** → CO₂ to methyl-S-CoM using H₂-derived electrons | 10.1093/gbe/evt128 | “CO₂ is reduced via six enzymatic steps to methyl-S-CoM using electrons from external H₂.” | **High confidence**, pathway-level. Avoid implying every hydrogenotrophic species uses an identical isoenzyme set. (borrel2013phylogenomicdatasupport pages 1-2) |
| 2 | H₂ availability — **positively regulates** → hydrogenotrophic methanogenesis | 10.1021/acs.est.2c08652 | “hydrogen exert[s] large control over kinetics and energetics”; H₂ and CO₂ are consumed at a 4:1 molar ratio. | **High confidence concept**, but the magnitude is reservoir-specific. (tyne2023identifyingandunderstanding pages 3-4) |
| 3 | acetate cleavage — **supplies** → methyl group and reducing equivalents for acetoclastic methanogenesis | 10.1093/gbe/evt128 | “acetate is cleaved with its methyl group transferred to H₄MPT then HS-CoM, with electrons from acetate carboxyl oxidation.” | **High confidence**, pathway-level. (borrel2013phylogenomicdatasupport pages 1-2) |
| 4 | MtaABC — **transfers methyl group from** → methanol to CoM | 10.1093/gbe/evt128 | “substrate-specific methyltransferases: MtaABC (methanol).” | **High confidence**, methylotrophic entry module. (borrel2013phylogenomicdatasupport pages 1-2) |
| 5 | MtmBC/MtbA — **transfers methyl group from** → monomethylamine to CoM | 10.1093/gbe/evt128 | “MtmBC/MtbA (monomethylamine).” | **High confidence**, substrate-specific. (borrel2013phylogenomicdatasupport pages 1-2) |
| 6 | MtbBC/MtbA — **transfers methyl group from** → dimethylamine to CoM | 10.1093/gbe/evt128 | “MtbBC/MtbA (dimethylamine).” | **High confidence**, substrate-specific. (borrel2013phylogenomicdatasupport pages 1-2) |
| 7 | MttBC/MtbA — **transfers methyl group from** → trimethylamine to CoM | 10.1093/gbe/evt128 | “MttBC/MtbA (trimethylamine).” | **High confidence**, substrate-specific. (borrel2013phylogenomicdatasupport pages 1-2) |
| 8 | MtsA/MtsB — **transfers methyl group from** → dimethyl sulfide to CoM | 10.1093/gbe/evt128 | “MtsA/MtsB (dimethyl sulfide), producing methyl-S-CoM.” | **High confidence**, but taxonomic distribution should be separately curated. (borrel2013phylogenomicdatasupport pages 1-2) |
| 9 | MCR + methyl-S-CoM + HS-CoB — **produces** → CH₄ + CoM-S-S-CoB | 10.1021/acs.biochem.9b00164 | “reversible reduction of methyl-coenzyme M … with coenzyme B … to produce methane and the heterodisulfide.” | **Highest-confidence terminal edge**. Represent as a reaction node if the schema supports stoichiometry. (thauer2019methyl(alkyl)coenzymem pages 1-2) |
| 10 | Ni(I)-coenzyme F₄₃₀ — **is required for activity of** → MCR | 10.1021/acs.biochem.9b00164 | “MCR requires the Ni(I) form of coenzyme F-430 for activity.” | **High confidence**. Distinguish active Ni(I) from oxidized inactive forms. (thauer2019methyl(alkyl)coenzymem pages 1-2) |
| 11 | HdrABC — **reduces** → CoM-S-S-CoB to HS-CoM + HS-CoB | 10.1021/acs.biochem.9b00164 | “HdrABC … catalyzes reduction … back to HS-CoM and HS-CoB.” | **High confidence** cofactor-recycling edge. Other Hdr configurations are taxon-specific. (thauer2019methyl(alkyl)coenzymem pages 1-2) |
| 12 | oxygen/high redox potential — **inactivates** → MCR | 10.1021/acs.biochem.9b00164 | MCR is “highly oxygen-sensitive,” and Ni(I) can be oxidized to Ni(II) or Ni(III). | **High confidence** molecular mechanism. Do not reduce all oxygen effects to MCR alone. (thauer2019methyl(alkyl)coenzymem pages 1-2) |
| 13 | ATP-dependent MCR activation system — **reactivates** → oxidized MCR | 10.1021/acs.biochem.9b00164 | Methanogens possess an “ATP-dependent enzyme system for MCR reactivation.” | **Strong but incompletely grounded**; use a label-only activation-system node pending protein-level evidence. (thauer2019methyl(alkyl)coenzymem pages 1-2) |
| 14 | competing nitrate/sulfate/O₂ — **suppresses** → methanogenesis by diverting H₂/electrons | 10.5713/ab.23.0294 | Competing electron acceptors “outcompet[e] H₂-consuming methanogens for available H₂.” | **High-confidence ecological regulation**, but strength depends on ecosystem and donor supply. (mackie2024—invitedreview pages 1-2) |
| 15 | Fe(III) availability — **suppresses** → methanogenesis relative to Fe(III) reduction | 10.15496/publikation-42776 | Ferrihydrite favored Fe(III) reduction and suppressed methanogenesis. | **Assay- and soil-specific**; do not generalize as absolute inhibition. (yang2022effectofbiochar pages 81-86) |
| 16 | BES — **inhibits** → methane production | 10.15496/publikation-42776 | BES “immediately halts CH₄ production while preserving Fe(III) reduction.” | **Strong experimental control**, but specificity and dose must be recorded; not proof of direct MCR binding from this source alone. (yang2022effectofbiochar pages 81-86) |
| 17 | increased temperature from 4°C to 25°C — **increases** → Arctic-peat methane-production rate | 10.1073/pnas.1420797112 | Production at 4°C was “only 25%” of that at 25°C; a 7°C transition changed the limiting process. | **Strong ecosystem-specific edge**, not a universal monotonic rule. (tveit2015fromthecover pages 1-2) |
| 18 | conductive biochar — **facilitates** → interspecies electron transfer and methanogenesis | 10.15496/publikation-42776 | Biochar linked Geobacteraceae and Methanosarcina and stimulated methanogenesis “2.3-fold.” | **Uncertain/generalization warning**: paddy-soil microcosm evidence; particle size and surface chemistry matter. (yang2022effectofbiochar pages 1-9) |
| 19 | freeze–thaw pretreatment of cow manure — **increases** → methylotrophic pathway representation and methane yield | 10.1038/s41598-024-76392-z | Pretreatment “significantly enhanced the methylotrophic methanogenic pathway”; yields improved by 13–21% depending on solids. | **Application-specific association**; omics abundance does not by itself prove flux through the route. (abid2024enhancedanaerobicdigestion pages 1-2) |
| 20 | coal:wheat-straw co-digestion at 3:1 — **increases** → methane yield | 10.1038/s41598-024-75655-z | Methane yield increased “1246.05%” over control; Methanosarcinaceae and Methanobacteriaceae reached 51.14% and 39.90%. | **Strong treatment result but highly system-specific**; do not make it a core trait edge. (khan2024coalstrawcodigestioninducedbiogenic pages 1-2) |
| 21 | high organic loading — **inhibits** → methane yield in dairy-waste BMP assay | 10.3390/agronomy14112546 | Dairy waste reached only 24.8% biodegradability and 106.3 NmL CH₄/g VS because of organic-matter overloading. | **Assay-specific** process-control edge. Mechanistic intermediary should remain unspecified. (llanoslizcano2024evaluationofbiochemical pages 1-2) |
| 22 | dissolved/injected CO₂ plus available H₂ — **supports** → subsurface methanogenesis | 10.1021/acs.est.2c08652 | CO₂ availability and H₂ control kinetics; 13–19% of injected CO₂ was inferred to become CH₄ within 30 years at the Olla field. | **Field-context edge**; attribution combines sequencing and isotope evidence and should carry site provenance. (tyne2023identifyingandunderstanding pages 7-8, tyne2023identifyingandunderstanding pages 3-4) |

## 4. Recent research, applications, and quantitative evidence

### 4.1 Anaerobic digestion and waste-to-energy

Methanogenesis is implemented at scale as the terminal biogas-producing stage of anaerobic digestion in wastewater, manure, food-waste, and agricultural-residue treatment. A 2024 BMP study at 37°C over 30 days found brewery waste produced **462.3 ± 1.25 NmL CH₄ g⁻¹ VS** at **95.1% biodegradability**; food waste produced **391.3 NmL CH₄ g⁻¹ VS** at an inoculum:substrate ratio of 2, while overloaded dairy waste produced only **106.3 NmL CH₄ g⁻¹ VS**. The results illustrate that substrate identity and loading are causal process variables, not merely metadata. (llanoslizcano2024evaluationofbiochemical pages 1-2)

Two 2024 studies show how pretreatment and co-substrates can restructure pathway use. Freeze–thaw-pretreated cow manure yielded up to **487 mL CH₄ g⁻¹ VS** at 5% total solids and improved yields by **13%, 20%, and 21%** at 5%, 10%, and 15% solids, respectively. Coal–wheat-straw co-digestion reported a **1246.05%** methane-yield increase over coal-only control, alongside marked enrichment of Methanosarcinaceae and Methanobacteriaceae. These are promising engineering results, but neither treatment should be promoted to a universal methanogenesis mechanism. (khan2024coalstrawcodigestioninducedbiogenic pages 1-2, abid2024enhancedanaerobicdigestion pages 1-2)

### 4.2 Rumen methane and mitigation

Rumen methanogens consume fermentation-derived H₂ and formate, maintaining low reducing-equivalent pressure and supporting primary fermentation. This syntrophic benefit explains why methane inhibition can redirect electron flow unpredictably rather than simply causing stoichiometric H₂ accumulation. The 2024 invited review argues that interventions should therefore target the whole H₂/formate economy—including alternative sinks—not only methanogen abundance. (mackie2024—invitedreview pages 1-2, mackie2024—invitedreview pages 10-11)

Recent quantitative context is substantial: the review attributes approximately **80% of agricultural methane to livestock**, nearly **90% of that to enteric fermentation**, and projects livestock methane emissions to rise approximately **30% by 2050** under demand growth. It discusses 3-nitrooxypropanol, halogenated compounds, seaweeds, nitrate/sulfate competition, and diet-driven shifts toward propionate as mitigation approaches, while emphasizing unresolved electron balances and ecosystem responses. (mackie2024—invitedreview pages 1-2, mackie2024—invitedreview pages 10-11)

The 2024 ruminant archaeome catalogue recovered **998 genomes from 2,270 metagenomes spanning 10 ruminant species**. Hydrogenotrophic methanogenesis was estimated to account for **more than 80% of rumen methane**, while archaeal composition and pathway completeness varied with host, breed, and gut location. This supports strain- and context-aware graphs rather than a single “rumen methanogen” node. (mi2024ametagenomiccatalogue pages 1-2)

### 4.3 Geological CO₂ storage and subsurface conversion

Methanogenesis is increasingly treated as a material factor in carbon capture and storage. A 2023 ES&T review concluded that methanogenesis is possible across storage-target types but will often be constrained by H₂ generation. At the Olla field, integrated geochemical and microbiological analyses inferred conversion of **13–19% of injected CO₂ to methane within 30 years**. Because methane is less soluble and less reactive than CO₂, conversion may alter fluid mobility, storage capacity, and trapping mechanisms. The authors recommend baseline, spatial, and temporal biogeochemical monitoring rather than assuming supercritical CO₂ sterilizes a reservoir. (tyne2023identifyingandunderstanding pages 7-8, tyne2023identifyingandunderstanding pages 1-3, tyne2023identifyingandunderstanding pages 3-4)

### 4.4 MCR biotechnology

A 2024 authoritative perspective identifies MCR as both the terminal methane-forming catalyst and a prospective platform for methane-to-chemical bioconversion. However, its oxygen sensitivity, complex α₂β₂γ₂ assembly, post-translational modifications, F₄₃₀ maturation, and difficult in-vitro activation make a methanogenic host more realistic in the near term than an isolated-enzyme process. Methanosarcina acetivorans is highlighted as a genetically tractable host, but efficient reverse-direction biomanufacturing remains developmental rather than established industrial practice. (thauer2019methyl(alkyl)coenzymem pages 1-2, dinh2024towardtheuse pages 2-4)

## 5. Recommended YAML graph architecture

A conservative first implementation should preserve the existing reduction-centered graph and add modular branches:

1. **Context module:** anoxic environment, methanogenic archaeon, substrate/electron-donor availability.
2. **Hydrogenotrophic module:** H₂/formate → reduced carriers; CO₂ → formyl-MFR → methenyl/methylene/methyl-H₄MPT → methyl-S-CoM.
3. **Acetoclastic module:** acetate activation/cleavage → methyl-H₄MPT or pathway-equivalent methyl carrier → methyl-S-CoM.
4. **Methylotrophic module:** methanol/methylamine/methyl-sulfide-specific methyltransferases → methyl-S-CoM; add H₂ dependence only for the appropriate lineage.
5. **Terminal module:** methyl-S-CoM + HS-CoB —MCR/F₄₃₀→ CH₄ + CoM-S-S-CoB.
6. **Recycling/energy module:** Hdr-mediated CoM/CoB regeneration; add electron-bifurcation and membrane-ion-conservation edges only when supported by a source specific to the chosen taxon/complex.
7. **Regulation module:** oxygen/redox, H₂, competing acceptors, temperature, pH, loading, inhibitors, and conductive materials, each with provenance and scope qualifiers.
8. **Evidence module:** methane-production assay, isotope evidence, transcript/protein/enzyme evidence, and negative controls.

## 6. Claims not yet suitable for unqualified TraitMech curation

1. **Do not use `mcrA present → methanogenesis` as a sufficient edge.** mcrA/MCR occurs in reverse methanogenesis and related alkane pathways; direction and net flux require physiological evidence. (sarno2024beyondmethanenew pages 1-3, dinh2024towardtheuse pages 2-4, ahmadi2024recentfindingsin pages 2-4)
2. **Do not equate MCR reversibility with bidirectional physiology.** Methanogen MCR oxidizes methane in vitro at only about 0.01% of its formation rate, and direct in-vitro activity has not been established for ANME MCRs in the cited review. (dinh2024towardtheuse pages 2-4)
3. **Do not curate ACR-mediated ethane/propane/butane activation as methanogenesis.** Proposed reverse alkane production by divergent ACRs remains uncertain. (sarno2024beyondmethanenew pages 1-3)
4. **Do not make biochar/DIET a universal positive regulator.** The 2.3-fold stimulation is from a defined paddy-soil microcosm and depends on particle and community properties. (yang2022effectofbiochar pages 1-9)
5. **Do not generalize temperature coefficients.** The 4°C-versus-25°C effect and 7°C ecological transition are specific to Arctic peat communities. (tveit2015fromthecover pages 1-2)
6. **Do not infer pathway flux solely from metagenomic abundance.** Enzyme genes and taxon enrichment establish potential or association; methane measurements, isotopic tracing, expression, or enzyme activity are needed for causal flux claims.
7. **Do not treat BES as perfectly specific without concentration and matrix information.** It is a useful experimental inhibitor, but an observed methane decrease does not independently identify its molecular target in every system. (yang2022effectofbiochar pages 81-86)
8. **Do not curate coal–straw or freeze–thaw effects as core biology.** Retain them as treatment-specific evidence linked to substrate accessibility, community restructuring, and process conditions. (khan2024coalstrawcodigestioninducedbiogenic pages 1-2, abid2024enhancedanaerobicdigestion pages 1-2)
9. **Do not assign exact ontology identifiers to ambiguous protonation states, enzyme isoforms, or multisubunit complexes without database verification.** Label-only nodes are preferable to false precision.

## 7. DOI-first bibliography

- **Dinh, T.-A.; Allen, K. D.** “Toward the Use of Methyl-Coenzyme M Reductase for Methane Bioconversion Applications.” *Accounts of Chemical Research* 57, 2746–2757. Published August 2024. DOI: [10.1021/acs.accounts.4c00413](https://doi.org/10.1021/acs.accounts.4c00413). (dinh2024towardtheuse pages 2-4)
- **Mi, J. et al.** “A metagenomic catalogue of the ruminant gut archaeome.” *Nature Communications* 15. Published November 2024. DOI: [10.1038/s41467-024-54025-3](https://doi.org/10.1038/s41467-024-54025-3). (mi2024ametagenomiccatalogue pages 1-2)
- **Khan, S. et al.** “Coal-straw co-digestion-induced biogenic methane production.” *Scientific Reports* 14. Published November 2024. DOI: [10.1038/s41598-024-75655-z](https://doi.org/10.1038/s41598-024-75655-z). (khan2024coalstrawcodigestioninducedbiogenic pages 1-2)
- **Abid, M. et al.** “Enhanced anaerobic digestion of freezing and thawing pretreated cow manure.” *Scientific Reports* 14. Published October 2024. DOI: [10.1038/s41598-024-76392-z](https://doi.org/10.1038/s41598-024-76392-z). (abid2024enhancedanaerobicdigestion pages 1-2)
- **Llanos-Lizcano, R.; Senila, L.; Modoi, O. C.** “Evaluation of Biochemical Methane Potential and Kinetics of Organic Waste Streams.” *Agronomy* 14, 2546. Published October 2024. DOI: [10.3390/agronomy14112546](https://doi.org/10.3390/agronomy14112546). (llanoslizcano2024evaluationofbiochemical pages 1-2)
- **Sarno, N. et al.** “Beyond methane, new frontiers in anaerobic microbial hydrocarbon utilizing pathways.” *Microbial Biotechnology* 17. Published June 2024. DOI: [10.1111/1751-7915.14508](https://doi.org/10.1111/1751-7915.14508). (sarno2024beyondmethanenew pages 1-3)
- **Mackie, R. I. et al.** “Hydrogen production and hydrogen utilization in the rumen.” *Animal Bioscience* 37, 323–336. Published February 2024. DOI: [10.5713/ab.23.0294](https://doi.org/10.5713/ab.23.0294). (mackie2024—invitedreview pages 1-2, mackie2024—invitedreview pages 10-11)
- **Ahmadi, F.; Lackner, M.** “Recent findings in methanotrophs: genetics, molecular ecology, and biopotential.” *Applied Microbiology and Biotechnology* 108. Published January 2024. DOI: [10.1007/s00253-023-12978-3](https://doi.org/10.1007/s00253-023-12978-3). (ahmadi2024recentfindingsin pages 2-4)
- **Tyne, R. L. et al.** “Identifying and Understanding Microbial Methanogenesis in CO₂ Storage.” *Environmental Science & Technology* 57, 9459–9473. Published June 2023. DOI: [10.1021/acs.est.2c08652](https://doi.org/10.1021/acs.est.2c08652). (tyne2023identifyingandunderstanding pages 7-8, tyne2023identifyingandunderstanding pages 1-3, tyne2023identifyingandunderstanding pages 3-4)
- **Thauer, R. K.** “Methyl (Alkyl)-Coenzyme M Reductases.” *Biochemistry* 58, 5198–5220. Published April 2019. DOI: [10.1021/acs.biochem.9b00164](https://doi.org/10.1021/acs.biochem.9b00164). (thauer2019methyl(alkyl)coenzymem pages 1-2)
- **Tveit, A. T. et al.** “Metabolic and trophic interactions modulate methane production by Arctic peat microbiota in response to warming.” *PNAS* 112. Published May 2015. DOI: [10.1073/pnas.1420797112](https://doi.org/10.1073/pnas.1420797112). (tveit2015fromthecover pages 1-2)
- **Borrel, G. et al.** “Phylogenomic Data Support a Seventh Order of Methylotrophic Methanogens.” *Genome Biology and Evolution* 5, 1769–1780. Published August 2013. DOI: [10.1093/gbe/evt128](https://doi.org/10.1093/gbe/evt128). (borrel2013phylogenomicdatasupport pages 1-2, borrel2013phylogenomicdatasupport pages 12-12)

## Curation priority

The immediate high-value additions to `methanogenesis.yaml` are the three/four substrate-entry modules, their convergence on methyl-S-CoM, the explicit MCR/F₄₃₀ terminal reaction, Hdr-mediated cofactor recycling, and contextual edges for anoxia, H₂ supply, and competing electron acceptors. Taxon-specific pretreatments, conductive-material effects, CCS conversion estimates, and mitigation interventions should remain separately qualified evidence branches rather than components of the universal causal core.

References

1. (borrel2013phylogenomicdatasupport pages 1-2): Guillaume Borrel, Paul W. O’Toole, Hugh M.B. Harris, Pierre Peyret, Jean-François Brugère, and Simonetta Gribaldo. Phylogenomic data support a seventh order of methylotrophic methanogens and provide insights into the evolution of methanogenesis. Genome Biology and Evolution, 5:1769-1780, Aug 2013. URL: https://doi.org/10.1093/gbe/evt128, doi:10.1093/gbe/evt128. This article has 336 citations and is from a domain leading peer-reviewed journal.

2. (thauer2019methyl(alkyl)coenzymem pages 1-2): Rudolf K. Thauer. Methyl (alkyl)-coenzyme m reductases: nickel f-430-containing enzymes involved in anaerobic methane formation and in anaerobic oxidation of methane or of short chain alkanes. Biochemistry, 58:5198-5220, Apr 2019. URL: https://doi.org/10.1021/acs.biochem.9b00164, doi:10.1021/acs.biochem.9b00164. This article has 227 citations and is from a peer-reviewed journal.

3. (yang2022effectofbiochar pages 81-86): Effect of biochar as geobattery and geoconductor on microbial Fe(III) reduction and methanogenesis in a paddy soil This article has 1 citations.

4. (tveit2015fromthecover pages 1-2): Alexander Tøsdal Tveit, Tim Urich, Peter Frenzel, and Mette Marianne Svenning. From the cover: pnas plus: metabolic and trophic interactions modulate methane production by arctic peat microbiota in response to warming. Proceedings of the National Academy of Sciences of the United States of America, May 2015. URL: https://doi.org/10.1073/pnas.1420797112, doi:10.1073/pnas.1420797112. This article has 260 citations and is from a highest quality peer-reviewed journal.

5. (mackie2024—invitedreview pages 1-2): Roderick I. Mackie, Hyewon Kim, Na Kyung Kim, and Isaac Cann. — invited review — hydrogen production and hydrogen utilization in the rumen: key to mitigating enteric methane production. Animal Bioscience, 37:323-336, Feb 2024. URL: https://doi.org/10.5713/ab.23.0294, doi:10.5713/ab.23.0294. This article has 45 citations and is from a peer-reviewed journal.

6. (dinh2024towardtheuse pages 2-4): Thuc-Anh Dinh and Kylie D. Allen. Toward the use of methyl-coenzyme m reductase for methane bioconversion applications. Accounts of Chemical Research, 57:2746-2757, Aug 2024. URL: https://doi.org/10.1021/acs.accounts.4c00413, doi:10.1021/acs.accounts.4c00413. This article has 18 citations and is from a domain leading peer-reviewed journal.

7. (sarno2024beyondmethanenew pages 1-3): Natalie Sarno, Emily Hyde, Valerie De Anda, and Brett J. Baker. Beyond methane, new frontiers in anaerobic microbial hydrocarbon utilizing pathways. Microbial Biotechnology, Jun 2024. URL: https://doi.org/10.1111/1751-7915.14508, doi:10.1111/1751-7915.14508. This article has 2 citations and is from a peer-reviewed journal.

8. (ahmadi2024recentfindingsin pages 2-4): Fatemeh Ahmadi and Maximilian Lackner. Recent findings in methanotrophs: genetics, molecular ecology, and biopotential. Applied Microbiology and Biotechnology, 108:1-21, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12978-3, doi:10.1007/s00253-023-12978-3. This article has 37 citations and is from a domain leading peer-reviewed journal.

9. (khan2024coalstrawcodigestioninducedbiogenic pages 1-2): Sohail Khan, Ze Deng, Bobo Wang, and Zhisheng Yu. Coal-straw co-digestion-induced biogenic methane production: perspectives on microbial communities and associated metabolic pathways. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-75655-z, doi:10.1038/s41598-024-75655-z. This article has 12 citations and is from a peer-reviewed journal.

10. (mi2024ametagenomiccatalogue pages 1-2): Jiandui Mi, Xiaoping Jing, Chouxian Ma, Fuyu Shi, Ze Cao, Xin Yang, Yiwen Yang, Apurva Kakade, Weiwei Wang, and Ruijun Long. A metagenomic catalogue of the ruminant gut archaeome. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54025-3, doi:10.1038/s41467-024-54025-3. This article has 45 citations and is from a highest quality peer-reviewed journal.

11. (tyne2023identifyingandunderstanding pages 3-4): R. L. Tyne, P. H. Barry, M. Lawson, K. G. Lloyd, D. Giovannelli, Z. M. Summers, and C. J. Ballentine. Identifying and understanding microbial methanogenesis in co2 storage. Environmental science & technology, 57:9459-9473, Jun 2023. URL: https://doi.org/10.1021/acs.est.2c08652, doi:10.1021/acs.est.2c08652. This article has 38 citations and is from a domain leading peer-reviewed journal.

12. (yang2022effectofbiochar pages 1-9): Effect of biochar as geobattery and geoconductor on microbial Fe(III) reduction and methanogenesis in a paddy soil This article has 1 citations.

13. (abid2024enhancedanaerobicdigestion pages 1-2): Muhammad Abid, Jing Wu, Yan Yuanyuan, Zeeshan Ajmal, Tariq Mehmood, Syed Nabeel Husnain, and Xu Zhou. Enhanced anaerobic digestion of freezing and thawing pretreated cow manure with increasing solid content: kinetics and microbial community dynamics. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-76392-z, doi:10.1038/s41598-024-76392-z. This article has 11 citations and is from a peer-reviewed journal.

14. (llanoslizcano2024evaluationofbiochemical pages 1-2): Rodolfo Llanos-Lizcano, Lacrimioara Senila, and Oana Cristina Modoi. Evaluation of biochemical methane potential and kinetics of organic waste streams for enhanced biogas production. Agronomy, 14:2546, Oct 2024. URL: https://doi.org/10.3390/agronomy14112546, doi:10.3390/agronomy14112546. This article has 30 citations and is from a peer-reviewed journal.

15. (tyne2023identifyingandunderstanding pages 7-8): R. L. Tyne, P. H. Barry, M. Lawson, K. G. Lloyd, D. Giovannelli, Z. M. Summers, and C. J. Ballentine. Identifying and understanding microbial methanogenesis in co2 storage. Environmental science & technology, 57:9459-9473, Jun 2023. URL: https://doi.org/10.1021/acs.est.2c08652, doi:10.1021/acs.est.2c08652. This article has 38 citations and is from a domain leading peer-reviewed journal.

16. (mackie2024—invitedreview pages 10-11): Roderick I. Mackie, Hyewon Kim, Na Kyung Kim, and Isaac Cann. — invited review — hydrogen production and hydrogen utilization in the rumen: key to mitigating enteric methane production. Animal Bioscience, 37:323-336, Feb 2024. URL: https://doi.org/10.5713/ab.23.0294, doi:10.5713/ab.23.0294. This article has 45 citations and is from a peer-reviewed journal.

17. (tyne2023identifyingandunderstanding pages 1-3): R. L. Tyne, P. H. Barry, M. Lawson, K. G. Lloyd, D. Giovannelli, Z. M. Summers, and C. J. Ballentine. Identifying and understanding microbial methanogenesis in co2 storage. Environmental science & technology, 57:9459-9473, Jun 2023. URL: https://doi.org/10.1021/acs.est.2c08652, doi:10.1021/acs.est.2c08652. This article has 38 citations and is from a domain leading peer-reviewed journal.

18. (borrel2013phylogenomicdatasupport pages 12-12): Guillaume Borrel, Paul W. O’Toole, Hugh M.B. Harris, Pierre Peyret, Jean-François Brugère, and Simonetta Gribaldo. Phylogenomic data support a seventh order of methylotrophic methanogens and provide insights into the evolution of methanogenesis. Genome Biology and Evolution, 5:1769-1780, Aug 2013. URL: https://doi.org/10.1093/gbe/evt128, doi:10.1093/gbe/evt128. This article has 336 citations and is from a domain leading peer-reviewed journal.