---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:01:11.067510'
end_time: '2026-08-04T00:08:59.745475'
duration_seconds: 468.68
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: alkaphilic
  trait_identifier: METPO:1003002
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: alkaphilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference in which an organism grows optimally at pH values
    above 9.
  parent_traits: METPO:1003000
  synonyms: alkaliphile, alkaliphilic, alkalophile, alkalophilic
  evidence_summary: 'DOI:10.1038/nrmicro2549: external pH range of 9.5-11.0 (Supports
    alkaliphilic growth at strongly alkaline external pH.)'
  causal_graph_summary: 'alkaliphilic_na_cycle_homeostasis: 11 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** alkaphilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003002
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism grows optimally at pH values above 9.
- **Parent traits:** METPO:1003000
- **Synonyms:** alkaliphile, alkaliphilic, alkalophile, alkalophilic
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH range of 9.5-11.0 (Supports alkaliphilic growth at strongly alkaline external pH.)
- **Existing causal graph summary:** alkaliphilic_na_cycle_homeostasis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/alkaphilic.yaml`.

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
- **Trait label:** alkaphilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003002
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism grows optimally at pH values above 9.
- **Parent traits:** METPO:1003000
- **Synonyms:** alkaliphile, alkaliphilic, alkalophile, alkalophilic
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH range of 9.5-11.0 (Supports alkaliphilic growth at strongly alkaline external pH.)
- **Existing causal graph summary:** alkaliphilic_na_cycle_homeostasis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/alkaphilic.yaml`.

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


# Curation report: alkaphilic microbial trait

## Executive scope

**Trait:** alkaphilic  
**Identifier:** **METPO:1003002**  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED  
**Operational definition supplied for curation:** a pH-growth preference in which an organism grows optimally above pH 9.

The trait should represent a **strain-level growth optimum**, established from a growth-rate, biomass-yield, or comparable growth assay across a controlled pH series. Mere survival, detectable activity, isolation from an alkaline habitat, enrichment at high pH, or possession of pH-homeostasis genes is insufficient. Reviews variously use optimal pH ≥9 or >10, so the supplied METPO threshold should control TraitMech curation rather than imposing a stricter literature convention. One recent comparison, for example, defined facultative alkaliphiles as having optima at pH ≥10 and obligate alkaliphiles as additionally failing to grow below pH 9; that narrower convention should not replace the METPO definition. (maksimova2024metabolicandmorphological pages 1-2, matsuno2018formationofproton pages 1-2)

The core physiological problem is twofold. First, pH 10 contains approximately one-thousandth the extracellular proton concentration at pH 7. Second, maintaining a substantially more acidic cytoplasm reverses the ΔpH component of proton motive force. Alkaliphily therefore depends on coordinated proton acquisition, cation extrusion, cytoplasmic pH homeostasis, surface proton retention, and membrane bioenergetics rather than on one universal “alkaliphile gene.” (goto2022differencesinbioenergetic pages 1-2, matsuno2018formationofproton pages 1-2)

## Trait boundaries

### Include

- Organisms whose **measured optimum is >pH 9**, including facultative and obligate alkaliphiles.
- Aerobic, anaerobic, bacterial, archaeal, or microbial-eukaryotic instances when the phenotype is experimentally demonstrated.
- Haloalkaliphiles only when alkaline preference is independently supported; salinity is a second trait rather than part of the definition.

### Distinguish from

1. **Alkali tolerance:** growth or survival at high pH despite an optimum near neutrality. A recent Bacillus comparison contrasts an alkaliphile growing at pH 11 and 50 g/L NaCl with a weakly alkali-tolerant strain, illustrating that growth range and salt resistance do not by themselves establish the optimum. (maksimova2024metabolicandmorphological pages 1-2)
2. **Obligate alkaliphily:** a narrower subtype characterized by poor or absent growth near neutral pH.
3. **Haloalkaliphily, alkalithermophily, and polyextremophily:** compound phenotypes in which salinity or temperature mechanisms must not automatically be assigned to alkaliphily.
4. **Alkaline-shock resistance:** a transient stress response in a neutralophile is not equivalent to preferential growth above pH 9.
5. **Alkaline habitat association:** metagenomic occurrence in soda lakes or alkaline wastewater is ecological evidence, not a strain-level optimum.

## Mechanistic model and expert interpretation

The best-supported conserved module is a **respiration–ΔΨ–Na⁺/H⁺ antiport–pH-homeostasis cycle**. Respiratory electron transport generates a negative-inside membrane potential. Electrogenic Na⁺/H⁺ antiporters use that potential to export cytoplasmic Na⁺ while importing scarce extracellular H⁺, thereby acidifying the cytoplasm and supporting sodium homeostasis. The resulting sodium motive force can support transport and motility, while proton-coupled F₁F₀ ATP synthase retains a direct role in ATP formation. Mrp is important in many model alkaliphiles, but transporter redundancy and lineage-specific alternatives mean that Mrp should be represented as a common causal mechanism, not a defining or universally necessary marker. (yumoto2025h+capacitorandatp pages 2-3, patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5, cheng(程彬)2016alkalineresponseof pages 2-4, cheng(程彬)2016alkalineresponseof pages 1-2)

In obligately alkaliphilic Bacillaceae, high ΔΨ can compensate partly for the adverse bulk ΔpH. Reported values for *Evansella clarkii* are approximately −170 mV under high aeration and −140 mV under low aeration. Under oxygen limitation, membrane-bound cytochrome c increased 2.5–6.3-fold, supporting—but not proving—the proposed surface “H⁺ capacitor” model. The latter remains an expert hypothesis and should not be promoted to a universal mechanistic edge. (goto2022differencesinbioenergetic pages 1-2)

## Candidate nodes grouped by type

### Trait and environmental nodes

- **alkaphilic — METPO:1003002**
- Parent trait **METPO:1003000**
- External alkaline pH; growth optimum above pH 9
- Low extracellular proton availability
- Sodium concentration, potassium concentration, salinity, aeration/oxygen availability
- Cytoplasmic pH; transmembrane ΔpH; membrane electrical potential ΔΨ
- Proton motive force and sodium motive force

Environmental ontology grounding should be conservative. A generic “alkaline environment” ENVO term may be added only after identifier verification; soda lake, alkaline wastewater, and serpentinizing-fluid nodes should remain habitat-specific and should not be treated as synonyms for the phenotype.

### Genes, proteins, transporters, and complexes

- **MrpA–MrpG** and the hetero-oligomeric Mrp/CPA3 Na⁺/H⁺ antiporter complex
- NhaA, NhaB, NhaC, NhaD, NhaP, and other CPA-family antiporters where strain-specific evidence exists
- Na⁺/H⁺ antiporter activity — candidate **GO:0015385**, subject to release validation
- F-type H⁺-transporting ATP synthase; AtpA–AtpI subunits as appropriate
- Respiratory-chain complexes, including NADH dehydrogenases and terminal oxidases
- Membrane-bound cytochrome c and its taxon-specific Asn-rich extension
- SlpA/SlaA-type surface-layer proteins
- BpOF4_01690 as a *Bacillus pseudofirmus* OF4-specific candidate, not a universal node
- Glycine-betaine and ectoine uptake systems

Mrp complexes generally require MrpA–G for activity, and individual subunit deletion or mutation can disrupt antiport activity and complex assembly. Exceptions exist, however, and should be represented at the taxon level. (yumoto2025h+capacitorandatp pages 2-3, ito2017mrpantiportershave pages 10-11)

### Chemicals and metabolites

- Sodium(1+) — **CHEBI:29101**
- Proton/H⁺, potassium(1+), lithium(1+), hydroxide
- ATP, ADP, phosphate
- Glycine betaine, ectoine, glutamate, proline
- Acidic cell-wall polymers: teichuronic acid, teichuronopeptide, and poly-γ-glutamate where demonstrated
- Cardiolipin, squalene, and C40 isoprenoids as lineage-specific membrane candidates

Use verified CHEBI records in the YAML. Do not infer a metabolite’s role merely because a transporter or biosynthetic gene is present.

### Processes, functions, and localizations

- Cytoplasmic pH homeostasis
- Sodium-ion homeostasis and cation extrusion
- Proton transmembrane transport
- Oxidative phosphorylation
- Proton-motive-force-driven ATP synthesis — candidate **GO:0042777**, subject to release validation
- Solute uptake powered by sodium motive force
- Cell-surface proton retention and hydroxide exclusion
- Cytoplasmic membrane, cell wall, S-layer, extracellular membrane surface, and cytoplasm

### Taxon and assay-context nodes

High-value mechanistic models include *Alkalihalobacillus halodurans* C-125, *Alkalihalobacillus pseudofirmus* OF4, *Evansella clarkii*, *Halomonas* sp. Y2, and *Caldalkalibacillus thermarum* TA2.A1. Exact NCBITaxon and UniProt CURIEs should be inserted only after checking the strain and current taxonomic synonym in the relevant database.

## Candidate causal edges

The following table separates strong biochemical/genetic evidence from taxon-specific observations and explicit hypotheses.

| Subject | Predicate | Object | Reference DOI/date | Supporting quote/snippet | Curation note/strength |
|---|---|---|---|---|---|
| External alkaline pH (>9) | decreases availability of | protons outside cell | 10.3389/fmicb.2018.02331 (2018-10); 10.3389/fbioe.2015.00075 (2015-06) | “alkaliphiles thrive in environments with a H+ concentrations that are one-thousandth (ca. pH 10) the concentration required by neutralophiles”; “the pH gradient across the cytoplasmic membrane… is in the reverse of the productive orientation” (matsuno2018formationofproton pages 1-2) | Strong mechanistic background; direct for alkaline environments, not a gene-level edge. |
| METPO:1003002 alkaphilic | has growth optimum at | alkaline pH above 9 | 10.3389/fbioe.2015.00075 (2015-06); 10.1155/2024/3087296 (2024-01) | “Alkaliphilic bacteria typically grow well at pH 9”; “alkaliphilic bacteria as organisms with optimal growth above pH 10.0” (maksimova2024metabolicandmorphological pages 1-2) | Strong phenotype edge; note literature cutoffs vary (>9 vs >10). Use supplied METPO definition as primary. |
| Cytoplasmic pH homeostasis | maintains | cytoplasm more acidic than external alkaline medium | 10.3389/fbioe.2015.00075 (2015-06); 10.3389/fmicb.2022.842785 (2022-03) | “alkaliphiles must maintain a cytoplasmic pH that is significantly lower than the pH of the outside medium”; “intracellular pH ~8.1 while growing optimally above pH 9” (goto2022differencesinbioenergetic pages 1-2) | Strong, broad mechanism; phenotype-level process node. |
| Na+/H+ antiporters (GO:0015385) | import | H+ | 10.1074/jbc.m116.751016 (2016-12) | “Na+/H+ exchangers catalyze active proton transport, resulting in efflux of intracellular monovalent cations (Na+, K+, Li+) in exchange for external protons” (cheng(程彬)2016alkalineresponseof pages 2-4) | Strong direct transporter mechanism; taxon demonstrated in Halomonas sp. Y2, broadly consistent with alkaliphily literature. |
| Na+/H+ antiporters (GO:0015385) | export | CHEBI:29101 sodium(1+) | 10.1074/jbc.m116.751016 (2016-12); 10.3390/ijms23169156 (2022-08) | “efflux of intracellular monovalent cations (Na+, K+, Li+) in exchange for external protons”; “membrane-potential-driven Na+/H+ antiport activity” (cheng(程彬)2016alkalineresponseof pages 2-4, patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5) | Strong for sodium export; broad but transporter-family-general. |
| Na+/H+ antiporters (GO:0015385) | export | potassium(1+) / lithium(1+) | 10.1074/jbc.m116.751016 (2016-12) | “efflux of intracellular monovalent cations (Na+, K+, Li+) in exchange for external protons” (cheng(程彬)2016alkalineresponseof pages 2-4) | Moderate; direct in Halomonas sp. Y2 and some antiporters, but not universal for all Na+/H+ antiporters. |
| Mrp antiporter complex (MrpA-G) | contributes to | pH homeostasis in alkaline environment | 10.3389/fmicb.2017.02325 (2017-11) | “The functions of the Mrp antiporter include sodium tolerance and pH homeostasis in an alkaline environment” (yumoto2025h+capacitorandatp pages 2-3) | Strong review-supported edge; broad across bacteria/archaea, though extent is taxon-dependent. |
| Mrp antiporter complex (MrpA-G) | contributes to | sodium tolerance / sodium homeostasis | 10.3389/fmicb.2017.02325 (2017-11); 10.3389/fmicb.2022.842785 (2022-03) | “The functions of the Mrp antiporter include sodium tolerance”; “Mrp (Sha) is critical for Na+ cycle regulation” (yumoto2025h+capacitorandatp pages 2-3, goto2022differencesinbioenergetic pages 2-3) | Strong; direct and central for existing Na-cycle graph. |
| mrpA–G genes | are required for | Mrp antiporter activity/complex function | 10.3389/fmicb.2017.02325 (2017-11) | “Generally, all Mrp subunits, mrpA–G, are required for enzymatic activity” (yumoto2025h+capacitorandatp pages 2-3) | Strong but complex-assembly edge; suitable if graph includes gene-subunit decomposition. |
| Membrane potential (negative inside, high ΔΨ) | drives/supports | Na+/H+ antiport activity | 10.3390/ijms23169156 (2022-08) | “Both transporters are electrogenic and can be driven by the negative-inside membrane potential for Na+ extrusion”; “membrane-potential-driven Na+/H+ antiport activity” (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5) | Strong family-level mechanism; not specific to one alkaliphile. |
| Respiratory chain | generates | high membrane electrical potential (ΔΨ) | 10.3389/fmicb.2018.02331 (2018-10); 10.3389/fmicb.2022.842785 (2022-03) | “high membrane electrical potential (ΔΨ) generated for an attractive force for H+”; “Δψ ca. -170 mV under high aeration, ~-140 mV under low aeration” (matsuno2018formationofproton pages 1-2, goto2022differencesinbioenergetic pages 1-2) | Strong for obligate alkaliphilic Bacillaceae; quantitative and curation-useful. |
| High negative-inside ΔΨ | supports | ATP synthesis under alkaline conditions | 10.3389/fmicb.2018.02331 (2018-10); 10.3389/fmicb.2022.842785 (2022-03) | “enhanced F1Fo-ATPase driving force per H+ is derived from the high ΔΨ”; “enabling ATP synthesis despite H+-diluted environment” (matsuno2018formationofproton pages 1-2, goto2022differencesinbioenergetic pages 1-2) | Strong mechanistic edge; especially supported in obligate alkaliphilic Bacillaceae. |
| F1Fo-ATP synthase | uses | H+ for ATP synthesis | 10.1016/S0021-9258(17)30537-9 (1990-11); 10.3389/fbioe.2015.00075 (2015-06) | “Evidence that the enzyme translocates H+ but not Na+”; “use of proton-coupled ATP synthases for oxidative phosphorylation by non-fermentative alkaliphiles” (yumoto2025h+capacitorandatp pages 1-2) | Strong direct edge; foundational, broad in aerobic alkaliphilic Bacillus models. |
| Acidic secondary cell wall polymers / S-layer proteins | retain/attract | H+ at cell surface | 10.3389/fmicb.2022.842785 (2022-03); 10.3389/fmicb.2018.02331 (2018-10) | “possess acidic secondary cell walls… that attract and retain H+ at cell surface”; “SlpA protein and polyglutamic acid… attract H+” (goto2022differencesinbioenergetic pages 1-2, matsuno2018formationofproton pages 1-2) | Moderate-strong; direct but mostly Bacillaceae-specific, exact polymer identity varies by taxon. |
| Acidic cell-surface polymers / S-layer proteins | repel | OH− | 10.3389/fmicb.2018.02331 (2018-10); 10.3389/fmicb.2025.1637315 (2025-09) | “attract H⁺ and repel OH⁻ to protect intracellular pathways”; “cell-surface acidic polymers… repel OH− and protect cells” (matsuno2018formationofproton pages 1-2, yumoto2025h+capacitorandatp pages 2-3) | Moderate; mechanistically plausible and repeatedly stated, but curate as taxon-specific surface adaptation. |
| Membrane-bound cytochrome c with Asn-rich segment | may act as | H+ capacitor on outer membrane surface | 10.3389/fmicb.2018.02331 (2018-10); 10.3389/fmicb.2022.842785 (2022-03) | “propose a cytochrome c-associated ‘H+ capacitor mechanism’”; “This structure may influence the formation of an H+-bond network that accumulates H+” (matsuno2018formationofproton pages 1-2, goto2022differencesinbioenergetic pages 1-2) | Weak-to-moderate; explicitly hypothetical and taxon-specific to obligate alkaliphilic Bacillaceae. Mark uncertain. |
| Oxygen limitation / lower O2 | decreases abundance of | Mrp antiporter complex | 10.3389/fmicb.2024.1468929 (2024-10) | “the sodium-proton antiporter complex Mrp was downregulated under the lower oxygen levels” (jong2023membraneproteomeof pages 8-9) | Moderate direct proteomic evidence in Caldalkalibacillus thermarum; environmental-regulation edge, not universal trait mechanism. |
| Glycine betaine and ectoine importers | are expressed in | Caldalkalibacillus thermarum TA2.A1 membrane proteome | 10.3389/fmicb.2023.1228266 (2023-07) | “We also observed C. thermarum TA2.A1 expressing transporters for ectoine and glycine betaine” (jong2023membraneproteomeof pages 8-9) | Moderate association only; observed expression, but causal contribution to alkaliphily is inferred rather than directly tested. |
| Glycine betaine / ectoine uptake | may assist in maintaining | near-neutral internal pH under highly alkaline external pH | 10.3389/fmicb.2023.1228266 (2023-07) | “compounds that are known osmolytes that may assist in maintaining a near neutral internal pH when the external pH is highly alkaline” (jong2023membraneproteomeof pages 8-9) | Weak-to-moderate; speculative wording (“may assist”), keep as uncertain/inferred. |


*Table: This table lists curation-ready candidate causal edges for microbial alkaliphily (METPO:1003002), emphasizing direct mechanistic evidence, taxon specificity, and uncertainty where appropriate. It is designed to support TraitMech YAML drafting while avoiding over-curation of hypothesis-level claims.*

### Recommended minimal graph expansion

For the existing 11-node `alkaliphilic_na_cycle_homeostasis` graph, the safest additions are:

1. `external alkaline pH` **decreases** `extracellular proton availability`;
2. `respiratory chain` **generates** `negative-inside membrane potential`;
3. `negative-inside membrane potential` **drives** `Mrp/Na+/H+ antiport`;
4. `Mrp/Na+/H+ antiport` **imports** `H+`;
5. `Mrp/Na+/H+ antiport` **exports** `Na+`;
6. `H+ import` **promotes** `cytoplasmic pH homeostasis`;
7. `Na+ export` **promotes** `sodium homeostasis`;
8. `cytoplasmic pH homeostasis` **enables** `growth optimum above pH 9`;
9. `acidic cell-surface polymers` **retain** `H+ near the membrane`, restricted to supported Bacillaceae;
10. `F₁F₀ ATP synthase` **uses** `proton electrochemical potential` for ATP synthesis.

The direction of antiport is well supported: external H⁺ is exchanged for intracellular Na⁺, K⁺, or Li⁺. In *Halomonas* sp. Y2, eight transporters complemented an Na⁺-sensitive *E. coli* strain and four complemented a K⁺-uptake-deficient strain; Ha-NhaD2, Ha-Mrp, and Ha-NhaP showed distinct ion and pH specializations. These results support transporter-level edges but also demonstrate why all cation/proton exchangers should not be collapsed into one universal substrate profile. (cheng(程彬)2016alkalineresponseof pages 2-4, cheng(程彬)2016alkalineresponseof pages 1-2)

## Recent developments, 2023–2024

### Direct membrane-proteome evidence

A 2023 membrane-proteomics study of *C. thermarum* TA2.A1 detected 158 proteins containing at least one transmembrane helix and recovered a complete oxidative-phosphorylation pathway, alternative type-II NADH dehydrogenase, ba₃ terminal oxidase, ion-transport proteins, and glycine-betaine/ectoine importers. The transporter expression is direct proteomic evidence, but the proposed contribution of those osmolytes to near-neutral internal pH was not tested causally. (jong2023membraneproteomeof pages 8-9)

A 2024 chemostat study spanning 0.25–4.2% O₂ found constitutive type-I and type-II NADH dehydrogenases, oxygen-dependent terminal-oxidase abundance, and lower Mrp abundance at low oxygen. This establishes an oxygen→Mrp-abundance edge in that organism, not a universal alkaliphily rule.

### Improved phenotype discrimination

The 2024 comparison of alkaliphilic *Bacillus aequororis* 5-DB with weakly alkali-tolerant *B. subtilis* ATCC 6633 combined resazurin reduction, ATP bioluminescence, AFM, and intracellular-pH measurements. *B. aequororis* grew at pH 11 and 50 g/L NaCl and maintained ΔpH and metabolic activity over a broader stress range. This is useful assay design for TraitMech evidence, although the salt phenotype must remain separate. (maksimova2024metabolicandmorphological pages 1-2)

### Current interpretation

Recent work largely refines context dependence rather than replacing the established Na⁺/H⁺-homeostasis model. Proteomics shows that respiratory branches, Mrp abundance, and osmolyte transport vary with oxygen and co-stress. Consequently, causal graphs should include experimental context and taxon qualifiers instead of treating every detected adaptation as constitutive or universal. (jong2023membraneproteomeof pages 8-9)

## Applications and real-world relevance

Alkaliphiles and their extracellular enzymes are exploited because they remain active under process conditions that inhibit ordinary organisms. Established or developing applications include alkaline proteases, amylases, cellulases, lipases, xylanases, and pectinases for detergents, textiles, pulp and paper, leather processing, food manufacture, and pharmaceutical workflows. Alkaliphilic cells and consortia are also studied for treatment of alkaline textile wastewater, nitrate-rich effluent, bauxite residue/red mud, and other industrial alkaline wastes.

Mechanistically, these applications do not themselves support edges in an alkaliphily graph unless the production or remediation phenotype is experimentally linked to a homeostasis node. They are better represented as downstream use cases. The strongest engineering implication is that Mrp/CPA transport, respiratory-chain flexibility, membrane robustness, and extracellular-enzyme stability are candidate targets for developing high-pH chassis organisms, but transporter overexpression alone may disturb sodium balance and bioenergetics.

## Curation warnings

1. **Do not equate high-pH growth with a high-pH optimum.** Record the complete assay range, optimum, buffering system, temperature, salinity, carbon source, oxygen status, and growth metric.
2. **Do not infer alkaliphily from habitat metagenomes.** Soda-lake abundance, alkaline-soil occurrence, or recovery from pH >11 wastewater is ecological association.
3. **Do not infer causality from gene presence.** Mrp, Nha, F-type ATP synthase, and terminal oxidases also occur in neutralophiles and perform broader physiological functions. (yumoto2025h+capacitorandatp pages 2-3)
4. **Do not universalize Mrp necessity.** *Halomonas* sp. Y2 demonstrates functional redundancy among antiporters, while Mrp effects vary with ion and pH conditions. (cheng(程彬)2016alkalineresponseof pages 1-2)
5. **Do not collapse salinity mechanisms into alkaliphily.** Compatible-solute accumulation and K⁺ retention may primarily reflect salt stress.
6. **Keep the cytochrome-c “H⁺ capacitor” uncertain.** It is a plausible, quantitatively motivated model for selected obligately alkaliphilic Bacillaceae, but the literature explicitly presents it as proposed or hypothetical. (goto2022differencesinbioenergetic pages 1-2, matsuno2018formationofproton pages 1-2)
7. **Keep glycine-betaine/ectoine→pH-homeostasis uncertain.** Importer expression is measured, but causal rescue or knockout evidence is lacking. (jong2023membraneproteomeof pages 8-9)
8. **Restrict acidic-polymer edges by taxon and molecule.** Teichuronic acid, teichuronopeptide, polyglutamate, and S-layer proteins are not interchangeable.
9. **Avoid unverified ontology IDs.** Label-only nodes are preferable to guessed CURIEs; verify GO, CHEBI, NCBITaxon, UniProt, Rhea, and pathway records against current releases.
10. **The supplied synonym “alkaphilic” is nonstandard.** Preserve it as the requested label, but use “alkaliphilic” in literature searches and synonym mapping.

## DOI-first bibliography

- Maksimova YG, Eliseeva A, Maksimov A. “Metabolic and Morphological Aspects of Adaptation of Alkaliphilic *Bacillus aequororis* 5-DB and Alkali-Tolerant *Bacillus subtilis* ATCC 6633…” Published January 2024. https://doi.org/10.1155/2024/3087296. (maksimova2024metabolicandmorphological pages 1-2)
- de Jong SI et al. “Membrane proteome of the thermoalkaliphile *Caldalkalibacillus thermarum* TA2.A1.” Published July 2023. https://doi.org/10.3389/fmicb.2023.1228266. (jong2023membraneproteomeof pages 8-9)
- Goto T et al. “Differences in Bioenergetic Metabolism of Obligately Alkaliphilic Bacillaceae Under High pH Depend on the Aeration Conditions.” Published March 2022. https://doi.org/10.3389/fmicb.2022.842785. (goto2022differencesinbioenergetic pages 2-3, goto2022differencesinbioenergetic pages 1-2)
- Patiño-Ruiz M, Ganea C, Călinescu O. “Prokaryotic Na+/H+ Exchangers—Transport Mechanism and Essential Residues.” Published August 2022. https://doi.org/10.3390/ijms23169156. (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5)
- Matsuno T et al. “Formation of Proton Motive Force Under Low-Aeration Alkaline Conditions in Alkaliphilic Bacteria.” Published October 2018. https://doi.org/10.3389/fmicb.2018.02331. (matsuno2018formationofproton pages 1-2)
- Ito M, Morino M, Krulwich TA. “Mrp Antiporters Have Important Roles in Diverse Bacteria and Archaea.” Published November 2017. https://doi.org/10.3389/fmicb.2017.02325. (yumoto2025h+capacitorandatp pages 2-3, ito2017mrpantiportershave pages 10-11)
- Cheng B et al. “Alkaline Response of a Halotolerant Alkaliphilic *Halomonas* Strain and Functional Diversity of Its Na⁺(K⁺)/H⁺ Antiporters.” Published December 2016. https://doi.org/10.1074/jbc.M116.751016. (cheng(程彬)2016alkalineresponseof pages 2-4, cheng(程彬)2016alkalineresponseof pages 1-2)
- Hicks DB, Krulwich TA. “Purification and reconstitution of the F₁F₀-ATP synthase from alkaliphilic *Bacillus firmus* OF4: evidence that the enzyme translocates H⁺ but not Na⁺.” Published November 1990. https://doi.org/10.1016/S0021-9258(17)30537-9.

## Bottom-line curation recommendation

Retain the existing Na-cycle/homeostasis graph as the core of **METPO:1003002**, and add respiratory ΔΨ, explicit H⁺ import/Na⁺ export, cytoplasmic pH homeostasis, and proton-coupled ATP synthesis. Add acidic surface polymers only in taxon-qualified branches. Hold cytochrome-c proton capacitance, osmolyte-mediated pH control, specific lipid compositions, and oxygen-dependent Mrp regulation as uncertain or context-specific extensions until direct perturbation evidence supports their contribution to a growth optimum above pH 9.

References

1. (maksimova2024metabolicandmorphological pages 1-2): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

2. (matsuno2018formationofproton pages 1-2): Toshihide Matsuno, Toshitaka Goto, Shinichi Ogami, Hajime Morimoto, Koji Yamazaki, Norio Inoue, Hidetoshi Matsuyama, Kazuaki Yoshimune, and Isao Yumoto. Formation of proton motive force under low-aeration alkaline conditions in alkaliphilic bacteria. Frontiers in Microbiology, Oct 2018. URL: https://doi.org/10.3389/fmicb.2018.02331, doi:10.3389/fmicb.2018.02331. This article has 214 citations and is from a peer-reviewed journal.

3. (goto2022differencesinbioenergetic pages 1-2): Toshitaka Goto, Shinichi Ogami, Kazuaki Yoshimume, and Isao Yumoto. Differences in bioenergetic metabolism of obligately alkaliphilic bacillaceae under high ph depend on the aeration conditions. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.842785, doi:10.3389/fmicb.2022.842785. This article has 6 citations and is from a peer-reviewed journal.

4. (yumoto2025h+capacitorandatp pages 2-3): Isao Yumoto. H+-capacitor and atp production in obligate alkaliphilic bacillaceae: insights into cytochrome c and h+ transport mechanisms. Frontiers in Microbiology, Sep 2025. URL: https://doi.org/10.3389/fmicb.2025.1637315, doi:10.3389/fmicb.2025.1637315. This article has 1 citations and is from a peer-reviewed journal.

5. (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5): Miyer Patiño-Ruiz, Constanța Ganea, and Octavian Călinescu. Prokaryotic na+/h+ exchangers—transport mechanism and essential residues. International Journal of Molecular Sciences, 23:9156, Aug 2022. URL: https://doi.org/10.3390/ijms23169156, doi:10.3390/ijms23169156. This article has 28 citations.

6. (cheng(程彬)2016alkalineresponseof pages 2-4): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.

7. (cheng(程彬)2016alkalineresponseof pages 1-2): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.

8. (ito2017mrpantiportershave pages 10-11): Masahiro Ito, Masato Morino, and Terry A. Krulwich. Mrp antiporters have important roles in diverse bacteria and archaea. Frontiers in Microbiology, Nov 2017. URL: https://doi.org/10.3389/fmicb.2017.02325, doi:10.3389/fmicb.2017.02325. This article has 145 citations and is from a peer-reviewed journal.

9. (goto2022differencesinbioenergetic pages 2-3): Toshitaka Goto, Shinichi Ogami, Kazuaki Yoshimume, and Isao Yumoto. Differences in bioenergetic metabolism of obligately alkaliphilic bacillaceae under high ph depend on the aeration conditions. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.842785, doi:10.3389/fmicb.2022.842785. This article has 6 citations and is from a peer-reviewed journal.

10. (yumoto2025h+capacitorandatp pages 1-2): Isao Yumoto. H+-capacitor and atp production in obligate alkaliphilic bacillaceae: insights into cytochrome c and h+ transport mechanisms. Frontiers in Microbiology, Sep 2025. URL: https://doi.org/10.3389/fmicb.2025.1637315, doi:10.3389/fmicb.2025.1637315. This article has 1 citations and is from a peer-reviewed journal.

11. (jong2023membraneproteomeof pages 8-9): Samuel I. de Jong, Dimitry Y. Sorokin, Mark C. M. van Loosdrecht, Martin Pabst, and Duncan G. G. McMillan. Membrane proteome of the thermoalkaliphile caldalkalibacillus thermarum ta2.a1. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1228266, doi:10.3389/fmicb.2023.1228266. This article has 5 citations and is from a peer-reviewed journal.