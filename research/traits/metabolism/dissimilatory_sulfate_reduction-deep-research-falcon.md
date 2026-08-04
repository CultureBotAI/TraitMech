---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:04:46.677106'
end_time: '2026-08-04T06:16:15.850902'
duration_seconds: 689.17
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dissimilatory sulfate reduction
  trait_identifier: traitmech:000105
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: dissimilatory_sulfate_reduction
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An anaerobic respiratory metabolism in which an organism uses sulfate
    as the terminal electron acceptor, reducing it to hydrogen sulfide while oxidizing
    organic matter or hydrogen for energy.
  parent_traits: METPO:1000802
  synonyms: sulfate respiration
  evidence_summary: 'DOI:10.1038/nrmicro1892:  (Muyzer & Stams review sulfate-reducing
    bacteria, which respire sulfate to sulfide in anoxic habitats.) | DOI:10.3389/fmicb.2011.00081:  (Plugge
    et al. review the metabolic flexibility of sulfate-reducing bacteria.)'
  causal_graph_summary: 'sulfate_reduction_to_sulfide: 12 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory sulfate reduction
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000105
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism uses sulfate as the terminal electron acceptor, reducing it to hydrogen sulfide while oxidizing organic matter or hydrogen for energy.
- **Parent traits:** METPO:1000802
- **Synonyms:** sulfate respiration
- **Existing evidence:** DOI:10.1038/nrmicro1892:  (Muyzer & Stams review sulfate-reducing bacteria, which respire sulfate to sulfide in anoxic habitats.) | DOI:10.3389/fmicb.2011.00081:  (Plugge et al. review the metabolic flexibility of sulfate-reducing bacteria.)
- **Existing causal graph summary:** sulfate_reduction_to_sulfide: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **dissimilatory sulfate reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_sulfate_reduction.yaml`.

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
- **Trait label:** dissimilatory sulfate reduction
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000105
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism uses sulfate as the terminal electron acceptor, reducing it to hydrogen sulfide while oxidizing organic matter or hydrogen for energy.
- **Parent traits:** METPO:1000802
- **Synonyms:** sulfate respiration
- **Existing evidence:** DOI:10.1038/nrmicro1892:  (Muyzer & Stams review sulfate-reducing bacteria, which respire sulfate to sulfide in anoxic habitats.) | DOI:10.3389/fmicb.2011.00081:  (Plugge et al. review the metabolic flexibility of sulfate-reducing bacteria.)
- **Existing causal graph summary:** sulfate_reduction_to_sulfide: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **dissimilatory sulfate reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_sulfate_reduction.yaml`.

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


# Curation report: dissimilatory sulfate reduction

**Trait:** `traitmech:000105`  
**Category:** METABOLISM · **Kind:** CLASS · **Status:** REVIEWED  
**Parent:** `METPO:1000802`  
**Synonym:** sulfate respiration

## 1. Scope summary

Dissimilatory sulfate reduction is an anaerobic respiratory metabolism in which sulfate, sulfur oxidation state +VI, is used as the terminal electron acceptor and is reduced through APS and sulfite to predominantly sulfide, oxidation state −II. Electrons come from oxidation of organic substrates or H₂, and the pathway supports energy conservation rather than sulfur incorporation into biomass. In oxygen-depleted marine sediments, sulfate reduction accounts for more than half of organic-matter remineralization; a recent global synthesis estimates that one-third of the 260 Tmol organic carbon reaching the seabed annually is mineralized through sulfate reduction. Approximately 90% of the resulting sulfide is reoxidized, consuming about 25% of global sedimentary oxygen; in coastal sediments, sulfate reduction accounts for about 50% of organic-carbon mineralization. (sim2023whatcontrolsthe pages 1-2, diao2023globaldiversityand pages 1-2)

The canonical sequence is sulfate uptake → Sat-mediated activation to APS → AprAB-mediated APS reduction to sulfite → DsrAB/DsrC-mediated sulfite reduction → DsrMKJOP-dependent terminal reduction and sulfide release. QmoABC and DsrMKJOP deliver electrons to the APS- and sulfite-reduction modules, respectively. (klier2024evolutionaryhistoryand pages 1-2, sim2023whatcontrolsthe pages 1-2)

### Inclusion criteria

Curate the trait when there is physiological evidence for sulfate-dependent anaerobic growth or sulfate consumption with sulfide formation, or strong genomic evidence for both:

1. a sulfate-to-sulfite module—typically `sat`, `aprAB`, and `qmoABC`; and
2. a reductive Dsr module—`dsrAB`, `dsrC`, and usually `dsrMKJOP`, with pathway-direction evidence.

### Boundary cases

- **Sulfite respiration:** organisms that reduce supplied sulfite but cannot use sulfate lack the upstream sulfate-activation capability. `dsrAB` alone therefore supports dissimilatory **sulfite** reduction, not necessarily `traitmech:000105`. (klier2024evolutionaryhistoryand pages 1-2, neukirchen2023stepwisepathwayfor pages 2-3)
- **Assimilatory sulfate reduction:** sulfate is reduced for cysteine/methionine biosynthesis and sulfur is retained in biomass. Presence of Sat/Apr-like proteins is not by itself diagnostic; these proteins can have assimilatory functions. (neukirchen2023stepwisepathwayfor pages 8-9)
- **Dsr-mediated sulfur oxidation:** oxidative Dsr systems can share Sat, AprAB, QmoABC, DsrC, DsrAB, and DsrMKJOP with reducers. Direction must therefore be inferred from gene context, DsrAB type, `dsrD`, `dsrL` type, `dsrEFH`, physiology, and expression—not from `dsrAB` alone. Four phyla contain organisms with genomic potential for both directions. (diao2023globaldiversityand pages 1-2)
- **Sulfur disproportionation:** simultaneous production of sulfate and sulfide from elemental sulfur, sulfite, or thiosulfate is a separate trait. Dsr proteins of known disproportionators can be phylogenetically indistinguishable from reductive Dsr proteins, and the mechanism is incompletely resolved; genome content alone cannot reliably distinguish disproportionators from sulfate reducers. (neukirchen2023stepwisepathwayfor pages 8-9)
- **Alternative zero-valent sulfur output:** a 2023 study reported sulfate-to-zero-valent-sulfur conversion by sulfate-reducing microorganisms. This is an important branch or boundary phenotype, but it should not replace sulfide as the canonical product without organism- and condition-specific evidence.
- **Oxygen exposure:** the metabolism is anaerobic, but possession of the trait does not imply obligate intolerance of oxygen. Sulfate reducers can survive oxic transitions, and some can switch to oxygen respiration.

## 2. Candidate nodes

### Trait and process nodes

- dissimilatory sulfate reduction — `traitmech:000105`
- sulfate respiration — synonym of the target trait
- anaerobic respiration — GO grounding candidate; verify exact GO CURIE before YAML insertion
- sulfate transport — GO grounding candidate
- APS reduction
- dissimilatory sulfite reduction
- electron transport / energy conservation
- sulfur isotope fractionation
- sulfide biomineralization / metal-sulfide precipitation

### Chemicals and metabolites

Use ChEBI records after identifier validation during ingestion:

- sulfate (`SO4²⁻`)
- ATP
- adenosine 5′-phosphosulfate, APS
- pyrophosphate
- sulfite (`SO3²⁻`)
- sulfide / hydrogen sulfide / hydrosulfide—represent protonation states explicitly if the graph schema permits
- DsrC trisulfide
- reduced and oxidized menaquinone
- electron donors: H₂, lactate, acetate, glycerol, and other organic substrates
- elemental or zero-valent sulfur, S(0)—branch product/alternative acceptor, not canonical endpoint
- iron(II)/iron(III), pyrite, and metal sulfides—downstream environmental nodes

Modern seawater contains about 28 mM sulfate, whereas many freshwater environments contain approximately 10–300 μM; sulfate limitation changes pathway flux and isotopic expression. (sim2023whatcontrolsthe pages 3-5, diao2023globaldiversityand pages 1-2)

### Genes, proteins, enzymes, and complexes

- **Sulfate transporter:** SulP-family transporter; CysZ and CysP are taxon-dependent candidates. Transporter assignment remains uncertain because comparative genomics found multiple candidate families and no universal experimentally established transporter.
- **Sat / ATP sulfurylase:** EC 2.7.7.4; activates sulfate with ATP to form APS and pyrophosphate.
- **AprA/AprB / APS reductase:** EC 1.8.99.2; reduces APS to sulfite.
- **QmoABC:** membrane electron-transfer complex supplying reducing equivalents to AprAB.
- **DsrA/DsrB:** dissimilatory sulfite reductase catalytic subunits; reductive versus oxidative DsrAB type must be represented.
- **DsrC:** small sulfur-carrier/redox protein and substrate for terminal reduction; DsrC-trisulfide is the canonical pathway intermediate.
- **DsrD:** allosteric activator of DsrAB in several reductive and disproportionating systems; supportive rather than universally essential marker. (diao2023globaldiversityand pages 3-4, klier2024evolutionaryhistoryand pages 12-13)
- **DsrMKJOP:** membrane-bound terminal reductase complex in anaerobic sulfate respiration; link to DsrC recycling and energy conservation. (klier2024evolutionaryhistoryand pages 12-13, neukirchen2023stepwisepathwayfor pages 11-12)
- **DsrN:** siroheme-amide cofactor-modification protein important in many Dsr systems. (neukirchen2023stepwisepathwayfor pages 2-3)
- **DsrL, DsrEFH:** pathway-direction/context markers, especially for oxidative Dsr metabolism; not core reductive-trait nodes without taxon-specific evidence.
- **DsrT:** possible regulatory component; function remains insufficiently resolved for a strong mechanistic edge.

### Environmental and experimental nodes

- anoxic or oxygen-depleted environment
- sulfate availability
- electron-donor availability
- organic-carbon availability
- temperature
- pH / acidic mine water
- oxygen exposure and reactive-oxygen stress
- sulfate-reduction rate
- sulfur-isotope composition, including δ³⁴S
- metal(loid) concentration and metal-sulfide precipitation
- biofilm and metal surface for corrosion applications

## 3. Recommended core graph

The following compact representation can serve as the initial YAML checklist.

| subject node | predicate | object node | confidence | principal DOI |
|---|---|---|---|---|
| sulfate transporter (SulP/CysZ candidate) | imports | sulfate | uncertain — transporter identity varies across sulfate-reducing microorganisms; uptake is required but specific family assignment is not universal (sim2023whatcontrolsthe pages 1-2, sim2023whatcontrolsthe pages 3-5) | 10.3389/fmicb.2018.00309 |
| Sat (ATP sulfurylase) | converts sulfate + ATP to | APS | high (klier2024evolutionaryhistoryand pages 1-2, sim2023whatcontrolsthe pages 1-2) | 10.1093/ismejo/wrae167 |
| QmoABC | donates electrons to | AprAB | high (sim2023whatcontrolsthe pages 1-2, diao2023globaldiversityand pages 3-4) | 10.1021/acsenvironau.2c00059 |
| AprAB | reduces APS to | sulfite | high (klier2024evolutionaryhistoryand pages 1-2, sim2023whatcontrolsthe pages 1-2) | 10.1021/acsenvironau.2c00059 |
| DsrAB + DsrC | converts sulfite to | DsrC-trisulfide intermediate | medium — canonical model strongly supported, but detailed chemistry is not yet equally resolved across all taxa (neukirchen2023stepwisepathwayfor pages 8-9, klier2024evolutionaryhistoryand pages 12-13) | 10.1038/s41396-023-01477-y |
| DsrMKJOP | reduces/recycles | DsrC-trisulfide to release sulfide | medium-high — terminal reductase role strongly supported, with some subunit/function details still system-specific (klier2024evolutionaryhistoryand pages 12-13, neukirchen2023stepwisepathwayfor pages 11-12) | 10.1073/pnas.2313650121 |
| electron donor availability | increases flux through | dissimilatory sulfate reduction | high (sim2023whatcontrolsthe pages 1-2, liu2024enrichmentofacidtolerant pages 1-2, liu2024enrichmentofacidtolerant pages 2-3) | 10.3389/fmicb.2024.1475137 |
| anoxic conditions | permit | sulfate respiration | high (sim2023whatcontrolsthe pages 1-2, diao2023globaldiversityand pages 1-2) | 10.1021/acsenvironau.2c00059 |


*Table: This table summarizes recommended core causal edges for traitmech:000105 with confidence flags and one principal DOI per edge. It highlights the best-supported canonical sulfate-respiration steps while marking transport identity and DsrC intermediate chemistry as less universal.*

## 4. Evidence-backed candidate causal edges

| Subject | Predicate | Object | Evidence snippet | Reference | Curation note |
|---|---|---|---|---|---|
| anoxic conditions | permit | dissimilatory sulfate reduction | “sulfate serves as an electron acceptor…where oxygen is depleted” | Sim et al., 2023, DOI: [10.1021/acsenvironau.2c00059](https://doi.org/10.1021/acsenvironau.2c00059) | **Strong**, but oxygen exposure does not necessarily eliminate the organism or trait. (sim2023whatcontrolsthe pages 1-2) |
| sulfate transporter | imports | sulfate | “The enzymatic pathway…consists of four principle steps from sulfate uptake” | Sim et al., published 3 Jan 2023, DOI above | **Strong process edge**; **uncertain protein identity** across taxa. (sim2023whatcontrolsthe pages 3-5, sim2023whatcontrolsthe pages 1-2) |
| Sat | converts sulfate + ATP to | APS | Canonical pathway described as “Sat converts sulfate to APS.” | Klier et al., 2024, DOI: [10.1093/ismejo/wrae167](https://doi.org/10.1093/ismejo/wrae167) | **Strong** canonical biochemical edge. (klier2024evolutionaryhistoryand pages 1-2) |
| QmoABC | donates electrons to | APS-reduction module / AprAB | “QmoABC and DsrMKJOP donate electrons for the reduction of APS and sulfite, respectively.” | Sim et al., 2023, DOI above | **Strong** at complex/module level; donor chain upstream of Qmo can vary. (sim2023whatcontrolsthe pages 1-2) |
| AprAB | reduces | APS to sulfite | Pathway sequence: sulfate activation to APS followed by “reduction of APS to sulfite.” | Sim et al., 2023; Klier et al., 2024 | **Strong**. (sim2023whatcontrolsthe pages 6-7, klier2024evolutionaryhistoryand pages 1-2) |
| DsrAB + DsrC | converts sulfite sulfur into | DsrC-trisulfide | Recent synthesis states that “DsrAB produces a DsrC-trisulfide from sulfite.” | Neukirchen et al., July 2023, DOI: [10.1038/s41396-023-01477-y](https://doi.org/10.1038/s41396-023-01477-y) | **Medium-high** canonical model; avoid asserting identical intermediate handling in every lineage. (neukirchen2023stepwisepathwayfor pages 8-9) |
| DsrD | activates | DsrAB | “DsrD acts as an allosteric activator of DsrAB” in several reducer classes. | Diao et al., advance publication 5 Oct 2023, DOI: [10.1093/femsre/fuad058](https://doi.org/10.1093/femsre/fuad058) | **Taxon/context-dependent**; do not make universally required. (diao2023globaldiversityand pages 3-4) |
| DsrMKJOP | reduces and recycles | oxidized/trisulfide DsrC | Identified as “the terminal reductase complex in anaerobic sulfate respiration.” | Barbosa et al., 2024, DOI: [10.1073/pnas.2313650121](https://doi.org/10.1073/pnas.2313650121) | **Strong complex-level edge**; exact subunit-level electron/proton stoichiometry should be curated separately only from the primary paper. (klier2024evolutionaryhistoryand pages 12-13) |
| DsrC-trisulfide reduction | releases | sulfide | Review pathway places the trisulfide form of DsrC before reduction to sulfide and thiol-form DsrC. | Sim et al., 2023, DOI above | **Medium-high**; represent protonation state carefully. (sim2023whatcontrolsthe pages 1-2) |
| electron-donor availability | positively regulates | sulfate-reduction rate / sulfide production | “Glycerol stimulated dissimilatory sulfate reduction much faster than elemental sulfur alone,” indicating donor limitation. | Liu et al., Oct 2024, DOI: [10.3389/fmicb.2024.1475137](https://doi.org/10.3389/fmicb.2024.1475137) | **Strong but assay-specific**; glycerol is an experimental donor, not universal. (liu2024enrichmentofacidtolerant pages 1-2) |
| sulfate reduction | oxidizes | organic matter or H₂ | DSR requires an electron donor, “usually in the form of organic compounds”; marine sulfate respiration is commonly regulated by organic-substrate supply. | Sim et al., 2023 | **Strong general edge**; donor-specific edges require organism-level evidence. (sim2023whatcontrolsthe pages 3-5) |
| dissimilatory sulfate reduction | produces | ³⁴S-depleted sulfide | Sulfide can be depleted in ³⁴S relative to sulfate “by as much as 66‰.” | Sim et al., 2023 | **Strong phenotype/assay edge**, but magnitude is condition-dependent. (sim2023whatcontrolsthe pages 1-2) |
| electron-donor limitation | increases | sulfur-isotope fractionation | Limiting lactate increased fractionation from approximately 10‰ to >50‰ while lowering cell-specific reduction rates. | Sim et al., 2023 | **Strong experimental relationship**, not a fixed diagnostic threshold. (sim2023whatcontrolsthe pages 6-7) |
| sulfate limitation | decreases | sulfur-isotope fractionation | “Submillimolar sulfate concentrations…generally decrease” fractionation; terminal-acceptor depletion produces smaller effects. | Sim et al., 2023 | **Strong trend**, with environmental exceptions. (sim2023whatcontrolsthe pages 3-5) |
| sulfide | reacts with iron to form | insoluble iron sulfides / pyrite | DSR-derived sulfide “reacts with iron and forms insoluble pyrite.” | Sim et al., 2023 | Suitable **downstream environmental edge**, not part of the intracellular core. (sim2023whatcontrolsthe pages 1-2) |
| stimulated sulfate reduction | promotes | metal(loid) immobilization | Pit-lake strategy stimulated biosulfidogenesis to form low-solubility sulfide minerals. | Liu et al., 2024 | **Application edge**; mineral identity and removal efficiency require experiment-specific data. (liu2024enrichmentofacidtolerant pages 1-2, liu2024enrichmentofacidtolerant pages 2-3) |

## 5. Recent developments, applications, and quantitative evidence

### Expanded diversity and annotation rules

The 2023 FEMS synthesis screened **950** `dsrAB`-carrying genomes—902 bacterial and 48 archaeal—distributed across 27 bacterial and four archaeal phyla in the initial dataset. It concluded that uncharacterized sulfate/sulfite reducers occur in **19 of 23 bacterial** and **two of four archaeal** phyla evaluated. The updated database taxonomically resolved more than 60% of uncultured family-level lineages. These data strongly support replacing narrow taxonomic definitions such as “sulfate-reducing bacteria” with the function-based “sulfate-reducing microorganisms.” (diao2023globaldiversityand pages 3-4, diao2023globaldiversityand pages 1-2)

A major expert conclusion is that direction cannot safely be assigned from `dsrAB` presence alone. Combinations of reductive/oxidative DsrAB type, `dsrD`, and `dsrL` type provide better—but still inferential—guidance. Physiological sulfate-dependent growth, sulfur mass balance, transcript/protein expression, or isotope tracing remains preferable. (diao2023globaldiversityand pages 1-2)

### Environmental flexibility and oxygen

Recent work has overturned the simplistic equation “sulfate reducer = strictly oxygen-intolerant organism.” A 2023 genome-centric metatranscriptomic study demonstrated an acidobacterium switching from sulfate reduction under anoxia to oxygen respiration under oxic conditions; `sat`, `aprAB`, and `dsrC` were among the highly expressed genes under sulfate-reducing conditions. A 2024 bioreactor study further reported sulfate-reducing Desulfobacterota and Bacillota populations reaching **2.9% relative abundance** despite weekly exposure to **133 μM oxygen**, approximately 50% air saturation, over more than 200 days. These findings support separate graph nodes for the anaerobic activity and the organism’s oxygen-tolerance/defense phenotype.

### Acid-mine and metal-removal implementation

Liu et al. tested 5 mM glycerol, 5 g/L elemental sulfur, both amendments, and an unamended control in synthetic acidic pit-lake medium containing, among other metals, **15 mg/L As, 100 mg/L Zn, and 50 mg/L Al**. Glycerol accelerated sulfate reduction, and glycerol plus S(0) produced the most sulfide. *Desulfosporosinus acididurans* reached **76–96% relative abundance** with glycerol and **93–99%** with glycerol plus S(0). The result supports donor amendment → increased biosulfidogenesis → potential metal-sulfide precipitation, but the combined treatment also permits elemental-sulfur reduction; not all measured sulfide can automatically be attributed to sulfate reduction. (liu2024enrichmentofacidtolerant pages 1-2, liu2024enrichmentofacidtolerant pages 2-3)

### Corrosion and reservoir souring

Sulfide production and biofilm-associated electron transfer make sulfate-reducing microorganisms major contributors to microbiologically influenced corrosion, while sulfide accumulation causes oil-reservoir souring. These are real-world consequences of the trait, but corrosion is multi-mechanistic and community-dependent; sulfate reduction should not be asserted as the cause of a corrosion case without electrochemical, chemical, and microbiological evidence. The 2023 global review identifies steel corrosion and oil souring as major economic burdens. (diao2023globaldiversityand pages 1-2)

### Isotope-based detection and reconstruction

Sulfur isotope fractionation is widely used to detect DSR in cultures, sediments, and geologic archives. Modern models treat uptake, Sat, Apr, and Dsr reactions as partially reversible, with sulfate uptake or APS reduction often acting as a physiological bottleneck. Sulfate and donor availability, rather than phylogeny alone, are considered the primary controls. Thus δ³⁴S is an assay-observed downstream phenotype, not a constitutive organismal constant. (sim2023whatcontrolsthe pages 1-2, sim2023whatcontrolsthe pages 6-7, sim2023whatcontrolsthe pages 3-5)

## 6. Curation warnings

1. **Do not curate `dsrAB → dissimilatory sulfate reduction` as a sufficient edge.** `dsrAB` also occurs in sulfite reducers, sulfur oxidizers, and disproportionators.
2. **Do not infer sulfate respiration from `sat` and `aprAB` alone.** These proteins can occur in assimilation or sulfite detoxification/oxidation contexts. (neukirchen2023stepwisepathwayfor pages 8-9)
3. **Do not assign a universal sulfate transporter.** SulP, CysZ, and CysP remain taxon-dependent candidates; transporter homology is weaker evidence than uptake experiments.
4. **Do not make DsrD universally essential.** It is a useful reductive-pathway marker and allosteric activator in characterized systems, but it is absent from some bona fide reductive lineages. (diao2023globaldiversityand pages 3-4)
5. **Do not infer sulfur disproportionation from the reductive Dsr gene set.** Current phylogenetic and genomic information cannot reliably distinguish it from reduction. (neukirchen2023stepwisepathwayfor pages 8-9)
6. **Do not treat oxygen exposure as proof of pathway absence.** Separate active anaerobic respiration from survival, detoxification, or facultative aerobic respiration.
7. **Do not curate S(0) as the universal product.** The 2023 zero-valent-sulfur pathway is a condition- and organism-specific branch requiring independent confirmation.
8. **Do not use a fixed isotope-fractionation cutoff as diagnostic.** Values vary with sulfate/donor ratio, rate, reversibility, temperature, and nutrients. (sim2023whatcontrolsthe pages 6-7, sim2023whatcontrolsthe pages 3-5)
9. **Avoid universal donor edges.** H₂, lactate, acetate, glycerol, methane-derived reducing equivalents, and complex organic matter are organism- and community-specific.
10. **Keep downstream impacts outside the minimal intracellular graph.** Pyrite formation, metal immobilization, corrosion, souring, gut effects, and carbon mineralization are valuable extension modules but are not defining intracellular steps.

## 7. DOI-first bibliography

1. Diao M. et al. **Global diversity and inferred ecophysiology of microorganisms with the potential for dissimilatory sulfate/sulfite reduction.** *FEMS Microbiology Reviews* 47, 2023. Advance publication: **5 October 2023**. DOI: [10.1093/femsre/fuad058](https://doi.org/10.1093/femsre/fuad058). (diao2023globaldiversityand pages 1-2)
2. Neukirchen S., Pereira I.A.C., Sousa F.L. **Stepwise pathway for early evolutionary assembly of dissimilatory sulfite and sulfate reduction.** *The ISME Journal* 17:1680–1692. Published **July 2023**. DOI: [10.1038/s41396-023-01477-y](https://doi.org/10.1038/s41396-023-01477-y). (neukirchen2023stepwisepathwayfor pages 8-9)
3. Sim M.S. et al. **What Controls the Sulfur Isotope Fractionation during Dissimilatory Sulfate Reduction?** *ACS Environmental Au* 3:76–86. Published **3 January 2023**. DOI: [10.1021/acsenvironau.2c00059](https://doi.org/10.1021/acsenvironau.2c00059). (sim2023whatcontrolsthe pages 1-2)
4. Klier K.M. et al. **Evolutionary history and origins of Dsr-mediated sulfur oxidation.** *The ISME Journal* 18. Published **2024**. DOI: [10.1093/ismejo/wrae167](https://doi.org/10.1093/ismejo/wrae167). (klier2024evolutionaryhistoryand pages 1-2)
5. Barbosa A.C.C., Venceslau S.S., Pereira I.A.C. **DsrMKJOP is the terminal reductase complex in anaerobic sulfate respiration.** *Proceedings of the National Academy of Sciences* 121:e2313650121. Published **2024**. DOI: [10.1073/pnas.2313650121](https://doi.org/10.1073/pnas.2313650121). (klier2024evolutionaryhistoryand pages 12-13)
6. Liu Y. et al. **Enrichment of acid-tolerant sulfide-producing microbes from an acidic pit lake.** *Frontiers in Microbiology* 15. Published **October 2024**. DOI: [10.3389/fmicb.2024.1475137](https://doi.org/10.3389/fmicb.2024.1475137). (liu2024enrichmentofacidtolerant pages 1-2)
7. Wang S. et al. **Generation of zero-valent sulfur from dissimilatory sulfate reduction in sulfate-reducing microorganisms.** *PNAS* 120, 2023. DOI: [10.1073/pnas.2220725120](https://doi.org/10.1073/pnas.2220725120).
8. Dyksma S., Pester M. **Oxygen respiration and polysaccharide degradation by a sulfate-reducing acidobacterium.** *Nature Communications* 14, **October 2023**. DOI: [10.1038/s41467-023-42074-z](https://doi.org/10.1038/s41467-023-42074-z).
9. Dyksma S., Pester M. **Growth of sulfate-reducing Desulfobacterota and Bacillota at periodic oxygen stress of 50% air-O₂ saturation.** *Microbiome* 12, **October 2024**. DOI: [10.1186/s40168-024-01909-7](https://doi.org/10.1186/s40168-024-01909-7).
10. Marietou A. et al. **Sulfate Transporters in Dissimilatory Sulfate Reducing Microorganisms: A Comparative Genomics Analysis.** *Frontiers in Microbiology* 9, **March 2018**. DOI: [10.3389/fmicb.2018.00309](https://doi.org/10.3389/fmicb.2018.00309).
11. Hausmann B. et al. **Peatland Acidobacteria with a dissimilatory sulfur metabolism.** *The ISME Journal* 12:1729–1742, **2018**. DOI: [10.1038/s41396-018-0077-1](https://doi.org/10.1038/s41396-018-0077-1).
12. Muyzer G., Stams A.J.M. **The ecology and biotechnology of sulphate-reducing bacteria.** *Nature Reviews Microbiology* 6:441–454, **June 2008**. DOI: [10.1038/nrmicro1892](https://doi.org/10.1038/nrmicro1892).
13. Plugge C.M. et al. **Metabolic flexibility of sulfate-reducing bacteria.** *Frontiers in Microbiology* 2:81, **2011**. DOI: [10.3389/fmicb.2011.00081](https://doi.org/10.3389/fmicb.2011.00081).

References

1. (sim2023whatcontrolsthe pages 1-2): Min Sub Sim, Dong Kyun Woo, Bokyung Kim, Hyeonjeong Jeong, Young Ji Joo, Yeon Woo Hong, and Jy Young Choi. What controls the sulfur isotope fractionation during dissimilatory sulfate reduction? ACS Environmental Au, 3:76-86, Jan 2023. URL: https://doi.org/10.1021/acsenvironau.2c00059, doi:10.1021/acsenvironau.2c00059. This article has 46 citations and is from a peer-reviewed journal.

2. (diao2023globaldiversityand pages 1-2): Muhe Diao, Stefan Dyksma, Elif Koeksoy, David Kamanda Ngugi, Karthik Anantharaman, Alexander Loy, and Michael Pester. Global diversity and inferred ecophysiology of microorganisms with the potential for dissimilatory sulfate/sulfite reduction. FEMS Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1093/femsre/fuad058, doi:10.1093/femsre/fuad058. This article has 88 citations and is from a domain leading peer-reviewed journal.

3. (klier2024evolutionaryhistoryand pages 1-2): Katherine M. Klier, Cody Martin, Marguerite V. Langwig, and Karthik Anantharaman. Evolutionary history and origins of dsr-mediated sulfur oxidation. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae167, doi:10.1093/ismejo/wrae167. This article has 21 citations.

4. (neukirchen2023stepwisepathwayfor pages 2-3): Sinje Neukirchen, Inês A C Pereira, and Filipa L Sousa. Stepwise pathway for early evolutionary assembly of dissimilatory sulfite and sulfate reduction. The ISME Journal, 17:1680-1692, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01477-y, doi:10.1038/s41396-023-01477-y. This article has 74 citations.

5. (neukirchen2023stepwisepathwayfor pages 8-9): Sinje Neukirchen, Inês A C Pereira, and Filipa L Sousa. Stepwise pathway for early evolutionary assembly of dissimilatory sulfite and sulfate reduction. The ISME Journal, 17:1680-1692, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01477-y, doi:10.1038/s41396-023-01477-y. This article has 74 citations.

6. (sim2023whatcontrolsthe pages 3-5): Min Sub Sim, Dong Kyun Woo, Bokyung Kim, Hyeonjeong Jeong, Young Ji Joo, Yeon Woo Hong, and Jy Young Choi. What controls the sulfur isotope fractionation during dissimilatory sulfate reduction? ACS Environmental Au, 3:76-86, Jan 2023. URL: https://doi.org/10.1021/acsenvironau.2c00059, doi:10.1021/acsenvironau.2c00059. This article has 46 citations and is from a peer-reviewed journal.

7. (diao2023globaldiversityand pages 3-4): Muhe Diao, Stefan Dyksma, Elif Koeksoy, David Kamanda Ngugi, Karthik Anantharaman, Alexander Loy, and Michael Pester. Global diversity and inferred ecophysiology of microorganisms with the potential for dissimilatory sulfate/sulfite reduction. FEMS Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1093/femsre/fuad058, doi:10.1093/femsre/fuad058. This article has 88 citations and is from a domain leading peer-reviewed journal.

8. (klier2024evolutionaryhistoryand pages 12-13): Katherine M. Klier, Cody Martin, Marguerite V. Langwig, and Karthik Anantharaman. Evolutionary history and origins of dsr-mediated sulfur oxidation. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae167, doi:10.1093/ismejo/wrae167. This article has 21 citations.

9. (neukirchen2023stepwisepathwayfor pages 11-12): Sinje Neukirchen, Inês A C Pereira, and Filipa L Sousa. Stepwise pathway for early evolutionary assembly of dissimilatory sulfite and sulfate reduction. The ISME Journal, 17:1680-1692, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01477-y, doi:10.1038/s41396-023-01477-y. This article has 74 citations.

10. (liu2024enrichmentofacidtolerant pages 1-2): Yutong Liu, Jennifer L. Macalady, Javier Sánchez-España, and William D. Burgos. Enrichment of acid-tolerant sulfide-producing microbes from an acidic pit lake. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1475137, doi:10.3389/fmicb.2024.1475137. This article has 9 citations and is from a peer-reviewed journal.

11. (liu2024enrichmentofacidtolerant pages 2-3): Yutong Liu, Jennifer L. Macalady, Javier Sánchez-España, and William D. Burgos. Enrichment of acid-tolerant sulfide-producing microbes from an acidic pit lake. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1475137, doi:10.3389/fmicb.2024.1475137. This article has 9 citations and is from a peer-reviewed journal.

12. (sim2023whatcontrolsthe pages 6-7): Min Sub Sim, Dong Kyun Woo, Bokyung Kim, Hyeonjeong Jeong, Young Ji Joo, Yeon Woo Hong, and Jy Young Choi. What controls the sulfur isotope fractionation during dissimilatory sulfate reduction? ACS Environmental Au, 3:76-86, Jan 2023. URL: https://doi.org/10.1021/acsenvironau.2c00059, doi:10.1021/acsenvironau.2c00059. This article has 46 citations and is from a peer-reviewed journal.