---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:01:19.682191'
end_time: '2026-08-04T07:09:17.686705'
duration_seconds: 478.0
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: sulfur oxidation
  trait_identifier: traitmech:000106
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: sulfur_oxidation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which an organism oxidizes reduced inorganic sulfur
    compounds (sulfide, elemental sulfur, thiosulfate) to sulfate, conserving energy
    and often supporting chemolithotrophic growth.
  parent_traits: METPO:1000060
  synonyms: sulfide oxidation
  evidence_summary: 'DOI:10.1111/j.1574-6976.2009.00187.x:  (Ghosh & Dam review the
    biochemistry and molecular biology of lithotrophic sulfur oxidation across bacteria
    and archaea.) | DOI:10.1128/AEM.67.7.2873-2882.2001:  (Friedrich et al. describe
    a common mechanism for bacterial oxidation of reduced inorganic sulfur compounds
    (the Sox system).)'
  causal_graph_summary: 'sulfur_oxidation_sox: 13 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** sulfur oxidation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000106
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism oxidizes reduced inorganic sulfur compounds (sulfide, elemental sulfur, thiosulfate) to sulfate, conserving energy and often supporting chemolithotrophic growth.
- **Parent traits:** METPO:1000060
- **Synonyms:** sulfide oxidation
- **Existing evidence:** DOI:10.1111/j.1574-6976.2009.00187.x:  (Ghosh & Dam review the biochemistry and molecular biology of lithotrophic sulfur oxidation across bacteria and archaea.) | DOI:10.1128/AEM.67.7.2873-2882.2001:  (Friedrich et al. describe a common mechanism for bacterial oxidation of reduced inorganic sulfur compounds (the Sox system).)
- **Existing causal graph summary:** sulfur_oxidation_sox: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **sulfur oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/sulfur_oxidation.yaml`.

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
- **Trait label:** sulfur oxidation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000106
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism oxidizes reduced inorganic sulfur compounds (sulfide, elemental sulfur, thiosulfate) to sulfate, conserving energy and often supporting chemolithotrophic growth.
- **Parent traits:** METPO:1000060
- **Synonyms:** sulfide oxidation
- **Existing evidence:** DOI:10.1111/j.1574-6976.2009.00187.x:  (Ghosh & Dam review the biochemistry and molecular biology of lithotrophic sulfur oxidation across bacteria and archaea.) | DOI:10.1128/AEM.67.7.2873-2882.2001:  (Friedrich et al. describe a common mechanism for bacterial oxidation of reduced inorganic sulfur compounds (the Sox system).)
- **Existing causal graph summary:** sulfur_oxidation_sox: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **sulfur oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/sulfur_oxidation.yaml`.

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


# Curation report: microbial sulfur oxidation

## Trait record and recommended scope

- **Trait:** sulfur oxidation
- **Identifier:** `traitmech:000106`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `METPO:1000060`
- **Synonym:** sulfide oxidation

### Scope summary

For TraitMech, this trait should represent **dissimilatory oxidation of reduced inorganic sulfur compounds (RISCs)**—principally sulfide/H₂S, elemental sulfur or polysulfides, and thiosulfate, with tetrathionate and sulfite as additional pathway substrates or intermediates—where electron transfer contributes to energy conservation. It includes aerobic and anaerobic chemolithotrophy, mixotrophic sulfur oxidation, and anoxygenic phototrophic sulfur oxidation. A 2023 review explicitly separates this energy-yielding process from assimilatory sulfur metabolism and lists sulfides, polysulfides, elemental sulfur, tetrathionate, sulfite, and thiosulfate among the relevant substrates (nosalova2023coldsulfursprings—neglected pages 2-3).

The graph should not require carbon fixation: many sulfur oxidizers are facultative or mixotrophic. Nor should it require oxygen, because nitrate and, in particular organisms or environments, Fe(III) and Mn(IV) can receive electrons from sulfur oxidation (zhou2025diversityandecology pages 3-5, zhou2025diversityandecology pages 32-34).

### Boundary cases

1. **Assimilatory sulfate reduction is outside scope.** Its purpose is production of reduced sulfur for cysteine, homocysteine, and biomass rather than conservation of energy from RISC oxidation (zhou2025diversityandecology pages 7-9, nosalova2023coldsulfursprings—neglected pages 2-3).
2. **Sulfate/sulfite reduction is the opposite trait.** Presence of `dsrAB` alone cannot determine direction: Dsr systems occur in reductive and oxidative configurations, and some organisms may switch direction (zhang2023microbedrivenelementalcycling pages 10-12, zhou2025diversityandecology pages 7-9).
3. **Sulfur disproportionation is adjacent but not equivalent.** Disproportionation simultaneously generates oxidized and reduced products without an external electron acceptor. It should be represented separately unless experimental evidence shows that its oxidative branch is integrated into energy-conserving sulfur oxidation (nosalova2023coldsulfursprings—neglected pages 2-3).
4. **Organic-sulfur catabolism is normally outside scope.** Taurine, alkanesulfonate, methanesulfonate, and related pathways belong here only when they demonstrably supply sulfite, sulfide, or sulfane sulfur to the inorganic energy pathway (zhou2025diversityandecology pages 7-9).
5. **Detoxification is insufficient.** SQR-mediated sulfide removal may protect cells without supporting growth. Curate the trait only when oxidation is connected to respiratory or phototrophic electron transfer, energy conservation, growth, or a validated complete pathway.
6. **Tetrathionate formation is an incomplete endpoint.** TsdA-dependent thiosulfate-to-tetrathionate oxidation establishes a sulfur-oxidation reaction, but does not by itself establish complete oxidation to sulfate or chemolithotrophic growth (nosalova2023coldsulfursprings—neglected pages 5-6).

## Current mechanistic understanding

Three interoperable modules dominate present models: **(i)** SQR or FccAB initiates sulfide oxidation; **(ii)** rDsr or sHdr oxidizes stored or carrier-bound sulfane sulfur to sulfite; and **(iii)** the periplasmic Sox system oxidizes thiosulfate and related sulfur substrates, commonly to sulfate. Electrons enter quinone or cytochrome pools and ultimately support aerobic respiration, anaerobic respiration, or anoxygenic photosynthesis (zhou2025diversityandecology pages 3-5).

A complete Sox cycle uses SoxYZ as a covalent sulfur carrier, SoxAX for substrate loading, SoxCD for oxidation of carrier-bound sulfur, and SoxB for hydrolytic sulfate release. The complete cycle is reported to release **eight electrons per thiosulfate**, whereas TsdA oxidation of thiosulfate to tetrathionate releases **two electrons** (nosalova2023coldsulfursprings—neglected pages 5-6, zhou2025diversityandecology pages 3-5).

The following artifact gives the recommended compact mechanistic edge set.

| Subject | Predicate | Object | Pathway/context | Evidence strength | Key qualifier |
|---|---|---|---|---|---|
| Sulfide:quinone oxidoreductase (SQR) | oxidizes | sulfide to elemental sulfur / persulfidic sulfur | Initial sulfide oxidation in sulfur oxidizers | Strong review-backed | Broadly distributed; exact product handling varies by lineage (nosalova2023coldsulfursprings—neglected pages 5-6, zhou2025diversityandecology pages 3-5) |
| Flavocytochrome c sulfide dehydrogenase (FccAB) | oxidizes | sulfide | Periplasmic/cytochrome-linked sulfide oxidation | Moderate review-backed | Commonly emphasized in phototrophs and some chemotrophs; taxon-specific prevalence (nosalova2023coldsulfursprings—neglected pages 5-6, zhou2025diversityandecology pages 3-5) |
| SoxAX | transfers / loads sulfur onto | SoxYZ-bound carrier intermediate | Sox thiosulfate oxidation cycle | Moderate review-backed | Functional step is canonical but component-level evidence here is from review synthesis rather than a retrieved primary experiment (zhou2025diversityandecology pages 3-5) |
| SoxYZ | functions as | sulfur carrier | Sox pathway intermediate carrier | Strong review-backed | Carrier role is central across Sox systems, but downstream completion depends on presence/absence of SoxCD (nosalova2023coldsulfursprings—neglected pages 5-6, zhou2025diversityandecology pages 3-5) |
| SoxB | releases | sulfate from carrier-bound sulfur intermediate | Sox pathway | Strong review-backed | Often described as sulfate thiol esterase; biochemical wording differs across sources (nosalova2023coldsulfursprings—neglected pages 5-6, zhou2025diversityandecology pages 3-5) |
| SoxCD | oxidizes | carrier-bound sulfur to more oxidized state | Complete Sox pathway | Strong review-backed | Missing SoxCD can redirect metabolism toward stored sulfur intermediates in some taxa (nosalova2023coldsulfursprings—neglected pages 5-6, zhou2025diversityandecology pages 3-5) |
| Complete Sox system | yields | 8 electrons per thiosulfate oxidized | Complete periplasmic thiosulfate oxidation | Moderate review-backed | Electron yield reported in review context; should be curated as pathway-level stoichiometric claim, not single-enzyme edge (nosalova2023coldsulfursprings—neglected pages 5-6) |
| TsdA (thiosulfate dehydrogenase) | converts | thiosulfate to tetrathionate | Tetrathionate-forming branch of sulfur oxidation | Strong review-backed | Alternative branch, not universal sulfur oxidation mechanism (nosalova2023coldsulfursprings—neglected pages 5-6) |
| TsdA-mediated thiosulfate oxidation | yields | 2 electrons | Tetrathionate branch | Moderate review-backed | Stoichiometric summary from review; pathway-level, not necessarily sufficient for trait alone (nosalova2023coldsulfursprings—neglected pages 5-6) |
| Sulfur globules / stored elemental sulfur | feed into | reverse Dsr (rDsr) pathway | Cytoplasmic oxidation of stored sulfur | Moderate review-backed | Especially associated with sulfur-storing phototrophs and related sulfur oxidizers; taxon-specific (nosalova2023coldsulfursprings—neglected pages 5-6, zhou2025diversityandecology pages 3-5) |
| DsrEFH | transfers sulfur to | DsrC | rDsr sulfur relay | Strong review-backed | Mechanistic sulfur-transfer role is canonical in rDsr models; exact relay chemistry can be lineage-specific (zhou2025diversityandecology pages 3-5) |
| DsrABL | oxidizes sulfur intermediate to produce | sulfite | rDsr pathway | Moderate review-backed | Often represented as DsrAB with DsrL support in oxidative direction; exact subunit notation varies (zhou2025diversityandecology pages 3-5) |
| SoeABC | oxidizes | sulfite to sulfate | Terminal sulfite oxidation after rDsr | Moderate review-backed | Strongly associated with sulfur-globule oxidizers in review context; taxon-specific curation advised (nosalova2023coldsulfursprings—neglected pages 5-6) |
| SoxT1A | imports | sulfur into cytoplasm | Hyphomicrobium denitrificans SoxT/sHdr-linked pathway | Strong primary evidence | Taxon-specific primary evidence from 2024; transported sulfur species remains unresolved (li2024yeeelikebacterialsoxt pages 8-9, li2024yeeelikebacterialsoxt pages 7-8) |
| sHdr-LbpA system | oxidizes sulfur intermediate to produce | sulfite | Cytoplasmic sulfane sulfur oxidation | Moderate primary/review-backed | Mechanistically supported in Hyphomicrobium-linked model; exact substrate identity still uncertain (li2024yeeelikebacterialsoxt pages 8-9, li2024yeeelikebacterialsoxt pages 7-8, zhou2025diversityandecology pages 3-5) |
| Oxygen | serves as terminal electron acceptor for | sulfide/sulfur oxidation | Aerobic sulfur oxidation | Strong review-backed | Broad but not universal; many sulfur oxidizers can instead use alternative acceptors (zhou2025diversityandecology pages 3-5) |
| Nitrate | serves as terminal electron acceptor for | sulfide/sulfur oxidation | Anaerobic sulfur oxidation / sulfur-driven denitrification | Strong review-backed plus genomic/ecological support | Broad ecological support; exact coupling and enzymes are lineage-specific (zhang2023microbedrivenelementalcycling pages 10-12, zhou2025diversityandecology pages 3-5) |


*Table: This table summarizes a concise, curator-ready core edge set for microbial sulfur oxidation, emphasizing mechanistic steps and qualifiers needed for TraitMech curation. It highlights which claims are broadly supported versus taxon-specific or stoichiometric pathway summaries.*

## Candidate nodes grouped by type

### Trait and phenotype nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| sulfur oxidation | `traitmech:000106` | Root trait node; quote CURIE verbatim. |
| dissimilatory sulfur oxidation | Label-only unless a verified ontology term is selected | Preferred mechanistic scope. |
| chemolithotrophic growth on reduced sulfur | Label-only | Evidence endpoint stronger than gene presence. |
| anoxygenic phototrophic sulfur oxidation | Label-only | Valid trait implementation, but light supplies additional energy. |
| sulfur-autotrophic denitrification | Label-only | Application/process subtype coupling sulfur oxidation to nitrate reduction. |

### Chemicals and electron carriers

Use verified ChEBI records during implementation; useful label-level candidates are **hydrogen sulfide**, **sulfide**, **elemental sulfur**, **polysulfide**, **thiosulfate**, **tetrathionate**, **sulfite**, **sulfate**, **oxygen**, **nitrate**, **nitrite**, **quinone**, **quinol**, **c-type cytochrome**, **Fe(III)**, and **Mn(IV)**. Proton production should be included in acid-generating sulfur oxidation or bioleaching models only where reaction stoichiometry is explicitly supported.

Do not collapse H₂S and HS⁻ without a chemical-normalization policy: their relative abundance is pH-dependent, while many papers use “sulfide” operationally for total dissolved sulfide.

### Pathways and modules

- Complete periplasmic **Sox pathway**: SoxAX–SoxYZ–SoxB–SoxCD.
- Sox pathway lacking SoxCD, often associated with elemental-sulfur accumulation.
- **SQR-dependent sulfide oxidation**.
- **FccAB-dependent sulfide oxidation**.
- **Reverse Dsr pathway**: DsrEFH, DsrC, oxidative DsrAB/DsrL, with downstream sulfite oxidation.
- **sHdr–LbpA pathway** for cytoplasmic sulfane-sulfur oxidation.
- **SoeABC-dependent sulfite oxidation**.
- **TsdA-dependent tetrathionate-forming branch**.
- Sulfur-globule formation and mobilization.
- Respiratory electron-transfer chain and ATP generation—preferably represented downstream only when the organism-specific chain is known.

### Genes, proteins, enzymes, and complexes

| Node | Function recommended for graph | Qualification |
|---|---|---|
| `soxX`, `soxA` / SoxXA | c-type cytochrome complex loading substrate-derived sulfur onto SoxYZ | Component chemistry should be supported by a biochemical source. |
| `soxY`, `soxZ` / SoxYZ | sulfur-carrier complex | Strong core Sox marker, but not alone diagnostic of the complete phenotype. |
| `soxB` / SoxB | sulfate thiol esterase; sulfate release | Widely used functional marker. |
| `soxC`, `soxD` / SoxCD | sulfur dehydrogenase for carrier-bound sulfur | Absence changes pathway products and sulfur storage. |
| `sqr` / SQR | sulfide:quinone oxidoreductase | Can mediate detoxification as well as energy metabolism. |
| `fccA`, `fccB` / FccAB | flavocytochrome-c sulfide dehydrogenase | Distribution and physiological role are taxon-dependent. |
| `dsrE`, `dsrF`, `dsrH` / DsrEFH | sulfur transfer to DsrC | Oxidative-pathway context is essential. |
| `dsrC` / DsrC | persulfide/trisulfide carrier in Dsr chemistry | Also occurs in reduction; not direction-specific alone. |
| `dsrA`, `dsrB`, `dsrL` / DsrABL | oxidation of DsrC-bound sulfur toward sulfite | Treat notation and exact complex composition conservatively. |
| `soeA`, `soeB`, `soeC` / SoeABC | sulfite oxidation to sulfate | Taxon-specific terminal module. |
| `tsdA` / TsdA | thiosulfate oxidation to tetrathionate | Bifunctionality or reverse activity can complicate annotation. |
| `sgpA`, `sgpB`, `sgpC` | sulfur-globule envelope proteins | Evidence for storage architecture, not independently for oxidation. |
| `soxT1A` / SoxT1A | sulfur import into cytoplasm | Strong evidence in *Hyphomicrobium denitrificans*; substrate identity unresolved. |
| `soxT1B` / SoxT1B | sulfur-responsive signal-transduction module | Do not generalize as the mass transporter. |
| Rhd442, DsrE3C, LbpA, sHdr | sulfur relay and cytoplasmic sulfane-sulfur oxidation | Emerging, lineage-specific module. |

For enzyme grounding, assign **EC, Rhea, KEGG, MetaCyc, and UniProt identifiers only after checking the exact reaction and taxon-specific protein**. Gene symbols are not stable universal identifiers, and no unverified CURIE should be introduced.

### Cellular localization and structures

- **Periplasm/extracytoplasmic compartment:** canonical Sox reactions and many FccAB reactions.
- **Cytoplasmic membrane:** SQR and quinone-pool electron entry.
- **Cytoplasm:** rDsr and sHdr–LbpA downstream sulfur processing.
- **Intracellular or extracytoplasmic sulfur globule:** taxon-dependent storage intermediate.
- **Photosynthetic membrane/reaction center:** phototrophic coupling.

The 2024 SoxT study is important because it directly connects an initial extracytoplasmic process to downstream cytoplasmic oxidation. SoxT1A delivers sulfur to the cytoplasm, after which Rhd442/DsrE3C and sHdr–LbpA participate in processing; the chemical identity of the transported species remains unresolved (li2024yeeelikebacterialsoxt pages 8-9, li2024yeeelikebacterialsoxt pages 7-8).

### Environmental and experimental factors

Candidate context nodes include oxic–anoxic interface, oxygen minimum zone, euxinic water, hydrothermal vent, cold sulfur spring, marine sediment, deep-sea ferromanganese-nodule sediment, acid-mine drainage, sulfidic wastewater, low-C/N wastewater, acidic pH, alkaline pH, light, oxygen availability, nitrate availability, sulfide concentration, thiosulfate amendment, and molybdate inhibition. These are context or assay nodes rather than constitutive causes in every taxon.

## Evidence-backed causal edges

The snippets below are concise source-derived statements or faithful excerpt summaries. “Strong” denotes direct biochemical or genetic support; “moderate” denotes authoritative review synthesis; “uncertain” denotes taxon-specific, omics-inferred, or chemically unresolved interpretation.

| Subject–predicate–object triple | Reference | Supporting snippet | Curation notes |
|---|---|---|---|
| SQR — oxidizes — sulfide to elemental/persulfidic sulfur while reducing quinone | DOI: [10.1038/s41579-024-01104-3](https://doi.org/10.1038/s41579-024-01104-3) | “Sqr transforms hydrogen sulfide to elemental sulfur using electron-transfer quinones.” | Strong review consensus; distinguish energy coupling from detoxification (zhou2025diversityandecology pages 3-5). |
| FccAB — oxidizes — sulfide through c-type cytochrome electron transfer | DOI: [10.1038/s41579-024-01104-3](https://doi.org/10.1038/s41579-024-01104-3) | “Fcc oxidizes sulfide via c-type cytochromes.” | Moderate; organism-specific role and localization should be checked (zhou2025diversityandecology pages 3-5). |
| SoxYZ — carries — covalently bound sulfur intermediates | DOI: [10.3390/microorganisms11061436](https://doi.org/10.3390/microorganisms11061436) | “SoxYZ and SoxB catalyze thiosulfate oxidation.” | Strong pathway-level support; avoid claiming sufficiency (nosalova2023coldsulfursprings—neglected pages 5-6). |
| SoxAX — loads — substrate-derived sulfur onto SoxYZ | DOI: [10.1038/s41579-024-01104-3](https://doi.org/10.1038/s41579-024-01104-3) | “SoxXA functions as [a] heterodimeric c-type cytochrome, SoxYZ as sulfur carrier.” | Moderate review-derived component edge (zhou2025diversityandecology pages 3-5). |
| SoxCD — oxidizes — SoxY-cysteine persulfide | DOI: [10.3390/microorganisms11061436](https://doi.org/10.3390/microorganisms11061436) | “Sox(CD)₂ dehydrogenase oxidiz[es] SoxY-cysteine persulfide.” | Strong mechanistic edge in the complete Sox cycle (nosalova2023coldsulfursprings—neglected pages 5-6). |
| SoxB — releases — sulfate from SoxY-bound intermediate | DOI: [10.1038/s41579-024-01104-3](https://doi.org/10.1038/s41579-024-01104-3) | “SoxB [is a] sulfate thiol esterase releasing sulfate from cysteine S-thiosulfonate.” | Strong; terminology of the carrier intermediate varies (zhou2025diversityandecology pages 3-5). |
| Complete Sox cycle — generates — eight electrons per thiosulfate | DOI: [10.3390/microorganisms11061436](https://doi.org/10.3390/microorganisms11061436) | “completing a catalytic cycle yielding 8 electrons per mole thiosulfate.” | Curate as pathway stoichiometry, not as a single-enzyme edge (nosalova2023coldsulfursprings—neglected pages 5-6). |
| TsdA — converts — thiosulfate to tetrathionate | DOI: [10.3390/microorganisms11061436](https://doi.org/10.3390/microorganisms11061436) | “TsdA … catalyzes thiosulfate-to-tetrathionate conversion.” | Strong reaction; alternative branch and not universal (nosalova2023coldsulfursprings—neglected pages 5-6). |
| TsdA reaction — releases — two electrons | DOI: [10.3390/microorganisms11061436](https://doi.org/10.3390/microorganisms11061436) | “forming sulfur-sulfur bonds and yielding 2 electrons.” | Pathway-level stoichiometric edge (nosalova2023coldsulfursprings—neglected pages 5-6). |
| Sulfur globules — supply sulfur to — rDsr pathway | DOI: [10.3390/microorganisms11061436](https://doi.org/10.3390/microorganisms11061436) | “intracellular globule oxidation using dsr cluster enzymes (rDsr) producing sulfite.” | Moderate and taxon-specific, especially sulfur-storing phototrophs (nosalova2023coldsulfursprings—neglected pages 5-6). |
| DsrEFH — transfers sulfur to — DsrC | DOI: [10.1038/s41579-024-01104-3](https://doi.org/10.1038/s41579-024-01104-3) | Sulfur is transferred “via DsrEFH to DsrC forming trisulfide.” | Strong mechanistic model for oxidative Dsr systems (zhou2025diversityandecology pages 3-5). |
| DsrABL — oxidizes DsrC-bound sulfur to — sulfite | DOI: [10.1038/s41579-024-01104-3](https://doi.org/10.1038/s41579-024-01104-3) | “DsrABL catalyzes oxidation to sulfite.” | Moderate; verify oxidative phylogeny and `dsrL` context (zhou2025diversityandecology pages 3-5). |
| SoeABC — oxidizes — sulfite to sulfate | DOI: [10.3390/microorganisms11061436](https://doi.org/10.3390/microorganisms11061436) | Sulfite is “subsequently oxidized to sulfate by SoeABC.” | Moderate, taxon-specific terminal module (nosalova2023coldsulfursprings—neglected pages 5-6). |
| SoxT1A — imports — sulfur into the cytoplasm | DOI: [10.1038/s42003-024-07270-7](https://doi.org/10.1038/s42003-024-07270-7) | “SoxT1A delivers sulfur to the cytoplasm for its further oxidation.” | Strong knockout evidence in *H. denitrificans*; transported chemical is uncertain (li2024yeeelikebacterialsoxt pages 8-9). |
| SoxT1A-mediated import — supplies sulfur to — sHdr–LbpA | DOI: [10.1038/s42003-024-07270-7](https://doi.org/10.1038/s42003-024-07270-7) | SoxT1A “mediates sulfur import into the cytoplasm for further processing by the sHdr-LbpA system.” | Strong organism-specific model (li2024yeeelikebacterialsoxt pages 7-8). |
| SoxT1B — transduces sulfur availability to — SoxR-dependent transcription | DOI: [10.1038/s42003-024-07270-7](https://doi.org/10.1038/s42003-024-07270-7) | “SoxT1B serves as a signal transduction unit for the transcriptional repressor SoxR.” | Strong but taxon-specific; it should not be annotated simply as a sulfur importer (li2024yeeelikebacterialsoxt pages 8-9). |
| Oxygen — accepts electrons from — sulfur oxidation | DOI: [10.1038/s41579-024-01104-3](https://doi.org/10.1038/s41579-024-01104-3) | Sulfide oxidation couples to “oxygen, nitrate, iron, manganese.” | Broad context edge, not universal (zhou2025diversityandecology pages 3-5). |
| Nitrate — accepts electrons from — sulfide/sulfur oxidation | DOI: [10.1038/s41579-024-01104-3](https://doi.org/10.1038/s41579-024-01104-3) | Sulfide oxidation couples to “oxygen, nitrate, iron, manganese.” | Supports sulfur-driven denitrification; enzyme chain is lineage-specific (zhou2025diversityandecology pages 3-5). |
| `dsrL` plus `dsrEFH` — supports inference of — oxidative Dsr pathway | DOI: [10.1186/s40168-023-01601-2](https://doi.org/10.1186/s40168-023-01601-2) | Deep-sea MAGs contained “dsrL and dsrEFH genes” associated with rDsr sulfur oxidation. | **Uncertain if gene presence alone**; useful genomic evidence only in pathway context (zhang2023microbedrivenelementalcycling pages 10-12). |

## Recent developments, 2023–2024

### Discovery of sulfur import and signaling machinery

The clearest mechanistic advance is the November 2024 characterization of two YeeE-like proteins in *Hyphomicrobium denitrificans*. SoxT1A mutants were sulfur-oxidation negative despite high sulfur-pathway transcription, supporting an essential transport role. SoxT1B instead acts principally in signal transduction through SoxR. This separates high-capacity sulfur transport from low-copy regulatory sensing (li2024yeeelikebacterialsoxt pages 8-9, li2024yeeelikebacterialsoxt pages 7-8).

The same study reported residual thiosulfate-responsive transcription in a relevant double-deletion background: `shdrA` and `soxXA` increased **6.62-fold** and **2.92-fold**, respectively. These values support regulation by sulfur exposure, but they do not alone establish transport chemistry or flux (li2024yeeelikebacterialsoxt pages 7-8).

### Environmental genomics and pathway diversity

A 2023 study of seven ferromanganese-nodule sediment samples reconstructed **179 high-quality MAGs**, spanning 21 bacterial phyla and one archaeal phylum; **88.8%** remained unclassified at species level. The community was inferred to obtain energy from oxidation of sulfur and metals using oxygen or nitrate, and oxidative-Dsr markers included `dsrL` and `dsrEFH`. This demonstrates substantial uncultured trait diversity, but remains largely genomic inference rather than organism-level physiology (zhang2023microbedrivenelementalcycling pages 10-12).

A broader recent synthesis surveyed 127 bacterial phyla and 47 archaeal classes and found sulfur-metabolism functions in 102 bacterial and 26 archaeal lineages. This is evidence that sulfur metabolism is phylogenetically widespread, but the aggregate includes reduction, disproportionation, assimilation, and organic-sulfur transformations—not only the target trait (zhou2025diversityandecology pages 7-9).

Cold sulfur springs were highlighted in 2023 as an under-sampled habitat for mesophilic and psychrophilic chemolithoautotrophs. The authoritative interpretation is that pathway diversity reflects both the many oxidation states of sulfur and repeated ecological recruitment across bacteria and Sulfolobales; cultivation remains a major bottleneck (nosalova2023coldsulfursprings—neglected pages 5-6, nosalova2023coldsulfursprings—neglected pages 2-3).

## Applications and real-world implementations

### Wastewater nitrogen and sulfide removal

Sulfur-based autotrophic denitrification couples oxidation of sulfide, elemental sulfur, or thiosulfate to nitrate/nitrite reduction. It is used or piloted for low-organic-carbon wastewater because it can remove nitrate without dosing a conventional organic electron donor. The relevant graph should represent nitrate as a context-dependent terminal acceptor, not as part of the universal sulfur-oxidation definition (zhou2025diversityandecology pages 3-5, zhou2025diversityandecology pages 32-34).

Engineering implementations include packed sulfur/limestone filters, elemental-sulfur autotrophic denitrification reactors, sulfide-driven denitrification, and sulfur-driven partial denitrification coupled to anammox. Current expert assessments emphasize reduced external-carbon demand and sludge production, while warning about sulfate generation, acidity/alkalinity demand, slow startup, nitrite or N₂O accumulation, and community instability. Application-level performance should not be propagated into the basal microbial trait graph without organism- and reactor-specific evidence.

### Biomining and bioleaching

Acidophilic sulfur oxidizers regenerate sulfuric acid and oxidizing conditions during dissolution of metal sulfides. This supports commercial copper biomining and pretreatment of refractory gold ores, and is being explored for recovery of metals from tailings, electronic waste, and other secondary resources. Mechanistically, ore dissolution can be indirect and consortium-dependent; sulfur oxidation, iron oxidation, proton generation, and abiotic ferric-iron attack should therefore be separate graph modules. A sulfur-oxidation gene or acid-tolerance phenotype does not by itself prove bioleaching performance.

### Gas, odor, and water treatment

Biofilters, biotrickling filters, and microaerobic bioreactors exploit sulfide oxidation to remove H₂S from biogas, sewage gas, and industrial emissions. Operational control of oxygen-to-sulfide ratio can favor elemental-sulfur recovery rather than complete sulfate production. These are genuine implementations of the trait, but product selectivity is reactor-dependent and should be encoded as conditional.

### Environmental remediation and ecosystem services

Sulfur oxidizers constrain sulfide accumulation at sediment–water interfaces, oxygen-minimum zones, hydrothermal systems, springs, and wastewater environments. They can also connect sulfur flux to nitrate, manganese, iron, carbon fixation, and phototrophy. In dysoxic or euxinic waters, uncultivated lineages and pathway-sharing consortia remain prominent; expert reviews therefore recommend tailored sampling, cultivation, and activity measurements rather than gene inventories alone (zhou2025diversityandecology pages 32-34, zhou2025diversityandecology pages 3-5).

## Assays and evidence hierarchy for curation

A robust positive trait assignment should combine at least two evidence classes:

1. **Chemical flux:** disappearance of sulfide, thiosulfate, or elemental sulfur and formation of tetrathionate, sulfite, or sulfate, with sterile controls.
2. **Growth or energy conservation:** biomass increase, yield, ATP, membrane potential, oxygen consumption, nitrate reduction, or light-dependent growth linked to the sulfur donor.
3. **Genetic causality:** knockout/complementation, depletion, or inhibitor evidence for a specific component.
4. **Protein/activity evidence:** enzyme assay, proteomics, sulfur-carrier intermediate, or purified-complex biochemistry.
5. **Omics context:** a near-complete coherent module, expression under sulfur oxidation, and an appropriate electron-acceptor chain.

Recommended experimental-factor nodes include sulfur substrate and concentration, pH, oxygen tension, nitrate availability, light, carbon source, incubation time, and abiotic controls. Because sulfur compounds interconvert abiotically, analytical chemistry and mass balance are essential.

## Curation warnings

1. **Do not infer direction from `dsrAB` alone.** Oxidative and reductive Dsr systems are homologous; `dsrL`, `dsrEFH`, phylogeny, gene neighborhood, expression, and physiology are needed (zhang2023microbedrivenelementalcycling pages 10-12, zhou2025diversityandecology pages 7-9).
2. **Do not infer a complete Sox pathway from `soxB` or `soxYZ` alone.** Partial systems can produce stored sulfur or feed a second cytoplasmic pathway.
3. **Do not equate SQR with chemolithotrophic growth.** SQR can serve sulfide detoxification or biosynthetic redox homeostasis.
4. **Keep TsdA conditional.** It establishes thiosulfate oxidation to tetrathionate, not necessarily complete oxidation to sulfate (nosalova2023coldsulfursprings—neglected pages 5-6).
5. **Keep SoxT1A/SoxT1B edges taxon-specific.** Their roles were demonstrated in *H. denitrificans*, and the transported sulfur species remains unresolved (li2024yeeelikebacterialsoxt pages 8-9, li2024yeeelikebacterialsoxt pages 7-8).
6. **Treat Fe(III)- and Mn(IV)-coupled sulfur oxidation as context-specific.** Broad reviews support these acceptors, but organism-level mechanisms are less uniformly resolved than oxygen- or nitrate-coupled oxidation (zhou2025diversityandecology pages 3-5, zhou2025diversityandecology pages 32-34).
7. **Separate sulfur storage from sulfur oxidation.** Sgp proteins or sulfur globules indicate storage architecture but are not sufficient evidence of subsequent oxidation.
8. **Do not curate metagenomic potential as demonstrated phenotype.** The 2023 deep-sea study is valuable ecological evidence, but MAG pathway reconstruction does not show substrate turnover or growth for an individual organism (zhang2023microbedrivenelementalcycling pages 10-12).
9. **Do not merge acid production, metal dissolution, and sulfur oxidation into one edge.** In biomining, these may be mediated by different organisms and abiotic reactions.
10. **Avoid unverified ontology identifiers.** Retain label-only nodes until ChEBI, GO, EC, Rhea, KEGG, MetaCyc, UniProt, ENVO, and NCBITaxon records have been checked individually.

## Recommended YAML graph architecture

The existing `sulfur_oxidation_sox` graph of 13 nodes and 12 edges is best retained as one **Sox module**, then extended or linked to separate conditional modules:

- `sulfide_oxidation_sqr_fcc`
- `sulfur_globule_reverse_dsr`
- `sulfane_sulfur_shdr_lbpa`
- `thiosulfate_to_tetrathionate_tsda`
- `sulfite_to_sulfate_soeabc`
- `sulfur_oxidation_aerobic_respiration`
- `sulfur_oxidation_nitrate_respiration`
- `sulfur_oxidation_phototrophy`

This modular design avoids implying that every sulfur oxidizer possesses every pathway and permits taxon-, compartment-, and electron-acceptor-specific evidence.

## DOI-first bibliography

1. Dahl C, Li J, Göbel F, et al. **YeeE-like bacterial SoxT proteins mediate sulfur import for oxidation and signal transduction.** *Communications Biology*. Published November 2024. DOI: [10.1038/s42003-024-07270-7](https://doi.org/10.1038/s42003-024-07270-7) (li2024yeeelikebacterialsoxt pages 8-9, li2024yeeelikebacterialsoxt pages 7-8).
2. Zhou Z, Tran PQ, Cowley ES, Trembath-Reichert E, Anantharaman K. **Diversity and ecology of microbial sulfur metabolism.** *Nature Reviews Microbiology*. DOI published online in 2024; volume publication 2025. DOI: [10.1038/s41579-024-01104-3](https://doi.org/10.1038/s41579-024-01104-3) (zhou2025diversityandecology pages 3-5, zhou2025diversityandecology pages 32-34, zhou2025diversityandecology pages 7-9).
3. Zhang D, Li X, Wu Y, et al. **Microbe-driven elemental cycling enables microbial adaptation to deep-sea ferromanganese nodule sediment fields.** *Microbiome*. Published July 2023. DOI: [10.1186/s40168-023-01601-2](https://doi.org/10.1186/s40168-023-01601-2) (zhang2023microbedrivenelementalcycling pages 10-12).
4. Nosalova L, Piknova M, Kolesarova M, Pristas P. **Cold Sulfur Springs—Neglected Niche for Autotrophic Sulfur-Oxidizing Bacteria.** *Microorganisms*. Published May 2023. DOI: [10.3390/microorganisms11061436](https://doi.org/10.3390/microorganisms11061436) (nosalova2023coldsulfursprings—neglected pages 5-6, nosalova2023coldsulfursprings—neglected pages 2-3, nosalova2023coldsulfursprings—neglected pages 9-11).
5. Ghosh W, Dam B. **Biochemistry and molecular biology of lithotrophic sulfur oxidation by taxonomically and ecologically diverse bacteria and archaea.** *FEMS Microbiology Reviews*. 2009. DOI: [10.1111/j.1574-6976.2009.00187.x](https://doi.org/10.1111/j.1574-6976.2009.00187.x). Foundational source supplied in the trait record.
6. Friedrich CG, Rother D, Bardischewsky F, Quentmeier A, Fischer J. **Oxidation of reduced inorganic sulfur compounds by bacteria: emergence of a common mechanism?** *Applied and Environmental Microbiology*. Published July 2001. DOI: [10.1128/AEM.67.7.2873-2882.2001](https://doi.org/10.1128/AEM.67.7.2873-2882.2001). Foundational Sox source supplied in the trait record.

## Curatorial conclusion

The strongest immediate extension to `sulfur_oxidation.yaml` is a modular graph joining initial sulfide oxidation by SQR/FccAB, complete or partial Sox thiosulfate oxidation, rDsr or sHdr cytoplasmic sulfur processing, terminal sulfite oxidation, and conditional electron acceptors. The SoxT1A transport edge is a particularly valuable 2024 addition, but should remain explicitly taxon-specific and chemically unresolved. Claims based only on marker genes, MAGs, sulfur globules, or SQR presence should be recorded as mechanistic potential rather than a demonstrated sulfur-oxidation phenotype.

References

1. (nosalova2023coldsulfursprings—neglected pages 2-3): Lea Nosalova, Maria Piknova, Mariana Kolesarova, and Peter Pristas. Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria. Microorganisms, 11:1436, May 2023. URL: https://doi.org/10.3390/microorganisms11061436, doi:10.3390/microorganisms11061436. This article has 16 citations.

2. (zhou2025diversityandecology pages 3-5): Zhichao Zhou, Patricia Q. Tran, Elise S. Cowley, Elizabeth Trembath-Reichert, and Karthik Anantharaman. Diversity and ecology of microbial sulfur metabolism. Nature reviews. Microbiology, 23:122-140, Oct 2025. URL: https://doi.org/10.1038/s41579-024-01104-3, doi:10.1038/s41579-024-01104-3. This article has 240 citations.

3. (zhou2025diversityandecology pages 32-34): Zhichao Zhou, Patricia Q. Tran, Elise S. Cowley, Elizabeth Trembath-Reichert, and Karthik Anantharaman. Diversity and ecology of microbial sulfur metabolism. Nature reviews. Microbiology, 23:122-140, Oct 2025. URL: https://doi.org/10.1038/s41579-024-01104-3, doi:10.1038/s41579-024-01104-3. This article has 240 citations.

4. (zhou2025diversityandecology pages 7-9): Zhichao Zhou, Patricia Q. Tran, Elise S. Cowley, Elizabeth Trembath-Reichert, and Karthik Anantharaman. Diversity and ecology of microbial sulfur metabolism. Nature reviews. Microbiology, 23:122-140, Oct 2025. URL: https://doi.org/10.1038/s41579-024-01104-3, doi:10.1038/s41579-024-01104-3. This article has 240 citations.

5. (zhang2023microbedrivenelementalcycling pages 10-12): Dechao Zhang, Xudong Li, Yuehong Wu, Xuewei Xu, Yanxia Liu, Benze Shi, Yujie Peng, Dadong Dai, Zhongli Sha, and Jinshui Zheng. Microbe-driven elemental cycling enables microbial adaptation to deep-sea ferromanganese nodule sediment fields. Microbiome, Jul 2023. URL: https://doi.org/10.1186/s40168-023-01601-2, doi:10.1186/s40168-023-01601-2. This article has 68 citations and is from a highest quality peer-reviewed journal.

6. (nosalova2023coldsulfursprings—neglected pages 5-6): Lea Nosalova, Maria Piknova, Mariana Kolesarova, and Peter Pristas. Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria. Microorganisms, 11:1436, May 2023. URL: https://doi.org/10.3390/microorganisms11061436, doi:10.3390/microorganisms11061436. This article has 16 citations.

7. (li2024yeeelikebacterialsoxt pages 8-9): Christiane Dahl, Jingjing Li, Fabienne Göbel, Hsun Hsu, Julian Koch, Natalie Hager, Wanda Flegler, and Tomohisa Tanabe. Yeee-like bacterial soxt proteins mediate sulfur import for oxidation and signal transduction. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07270-7, doi:10.1038/s42003-024-07270-7. This article has 8 citations and is from a peer-reviewed journal.

8. (li2024yeeelikebacterialsoxt pages 7-8): Christiane Dahl, Jingjing Li, Fabienne Göbel, Hsun Hsu, Julian Koch, Natalie Hager, Wanda Flegler, and Tomohisa Tanabe. Yeee-like bacterial soxt proteins mediate sulfur import for oxidation and signal transduction. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07270-7, doi:10.1038/s42003-024-07270-7. This article has 8 citations and is from a peer-reviewed journal.

9. (nosalova2023coldsulfursprings—neglected pages 9-11): Lea Nosalova, Maria Piknova, Mariana Kolesarova, and Peter Pristas. Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria. Microorganisms, 11:1436, May 2023. URL: https://doi.org/10.3390/microorganisms11061436, doi:10.3390/microorganisms11061436. This article has 16 citations.