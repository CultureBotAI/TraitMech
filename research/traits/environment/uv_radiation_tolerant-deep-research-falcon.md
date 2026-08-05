---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:32:13.622515'
end_time: '2026-08-04T04:39:57.404306'
duration_seconds: 463.78
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: UV radiation tolerant
  trait_identifier: traitmech:000009
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: uv_radiation_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An environmental tolerance in which an organism survives high doses
    of ultraviolet radiation, typically via photoreactivation and nucleotide-excision
    repair of cyclobutane pyrimidine dimers and 6-4 photoproducts.
  parent_traits: traitmech:000007
  synonyms: UV resistant
  evidence_summary: "DOI:10.3390/genes14091803: Deinococcus radiodurans R1 demonstrates\
    \ a significantly higher radiation resistance with D10 values exceeding 12 kGy\
    \ for gamma radiation and 700 J/m2 for UV-C radiation (Organism example: Deinococcus\
    \ radiodurans tolerates UV-C radiation D10 doses of 700 J/m2.) | DOI:10.1101/cshperspect.a012765:\
    \ The bacterium Deinococcus radiodurans is a champion of extreme radiation resistance\
    \ (Review support \u2014 Deinococcus radiodurans is the reference organism for\
    \ extreme UV and ionizing radiation resistance.)"
  causal_graph_summary: 'uv_tolerance_excision_repair: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** UV radiation tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000009
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives high doses of ultraviolet radiation, typically via photoreactivation and nucleotide-excision repair of cyclobutane pyrimidine dimers and 6-4 photoproducts.
- **Parent traits:** traitmech:000007
- **Synonyms:** UV resistant
- **Existing evidence:** DOI:10.3390/genes14091803: Deinococcus radiodurans R1 demonstrates a significantly higher radiation resistance with D10 values exceeding 12 kGy for gamma radiation and 700 J/m2 for UV-C radiation (Organism example: Deinococcus radiodurans tolerates UV-C radiation D10 doses of 700 J/m2.) | DOI:10.1101/cshperspect.a012765: The bacterium Deinococcus radiodurans is a champion of extreme radiation resistance (Review support — Deinococcus radiodurans is the reference organism for extreme UV and ionizing radiation resistance.)
- **Existing causal graph summary:** uv_tolerance_excision_repair: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **UV radiation tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/uv_radiation_tolerant.yaml`.

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
- **Trait label:** UV radiation tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000009
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives high doses of ultraviolet radiation, typically via photoreactivation and nucleotide-excision repair of cyclobutane pyrimidine dimers and 6-4 photoproducts.
- **Parent traits:** traitmech:000007
- **Synonyms:** UV resistant
- **Existing evidence:** DOI:10.3390/genes14091803: Deinococcus radiodurans R1 demonstrates a significantly higher radiation resistance with D10 values exceeding 12 kGy for gamma radiation and 700 J/m2 for UV-C radiation (Organism example: Deinococcus radiodurans tolerates UV-C radiation D10 doses of 700 J/m2.) | DOI:10.1101/cshperspect.a012765: The bacterium Deinococcus radiodurans is a champion of extreme radiation resistance (Review support — Deinococcus radiodurans is the reference organism for extreme UV and ionizing radiation resistance.)
- **Existing causal graph summary:** uv_tolerance_excision_repair: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **UV radiation tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/uv_radiation_tolerant.yaml`.

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


# Curation report: microbial UV-radiation tolerance

## Trait record and recommendation

- **Trait label:** UV radiation tolerant
- **Trait identifier:** `traitmech:000009`
- **Category / term kind / status:** ENVIRONMENT / CLASS / REVIEWED
- **Parent:** `traitmech:000007`
- **Synonym:** UV resistant

**Recommended scope.** This trait should denote a reproducible capacity of a microorganism to retain viability or reproductive capacity after a defined ultraviolet exposure. A valid phenotype record should specify wavelength or band, fluence in J m⁻², dose rate where known, physiological state, medium, shielding conditions, and whether recovery occurred in photoreactivating light or darkness. These variables are mechanistically decisive: haloarchaeal survival was measured at 254-nm UV-C and 0–144 J m⁻² under light versus dark recovery, whereas a *Pseudomonas syringae* study used solar UV-B at 4.5 kJ m⁻² over 290–320 nm. The resulting values are not directly interchangeable. (gunasekera2006roleofnucleotide pages 1-2, nag2023genomicanalysisof pages 2-4)

The supplied definition is substantially correct but too narrow if interpreted as universal. Photoreactivation and nucleotide-excision repair (NER) are the best-supported core mechanisms, but auxiliary recombinational, DNA-end-protection, antioxidant, pigment, sporulation, biofilm, and physical-shielding mechanisms can contribute in particular taxa or assays. The graph should therefore represent photoreactivation and NER as the conserved core while placing *Deinococcus*-specific and lineage-specific systems in qualified extensions.

## 1. Trait scope and boundary cases

### Included phenotype

A strain is UV-radiation tolerant when its survival curve, D-value, surviving fraction at a specified fluence, or post-exposure growth is substantially greater than an appropriate comparator under the same conditions. For example, *Deinococcus radiodurans* survives doses up to approximately 750 J m⁻² in the cited experiment, compared with about 30 J m⁻² for *E. coli* B/r; 500 J m⁻² generated approximately 5,000 thymine-containing pyrimidine dimers per *D. radiodurans* genome, or about one lesion per 640 bp. (selvam2013ddraddrdand pages 1-2)

The phenotype may include:

1. **Intrinsic damage prevention**, such as molecular absorption or quenching, when experimentally linked to cellular survival.
2. **Direct reversal**, principally visible-light-dependent photoreactivation.
3. **Damage excision and resynthesis**, principally UvrABC-dependent NER.
4. **Damage tolerance and genome restoration**, including recombination, stress regulation, and taxon-specific DNA-protection proteins.
5. **Community- or structure-mediated protection**, such as spores, aggregates, extracellular matrix, or pigments, but only when the curated subject is explicitly the corresponding structured state rather than an unshielded vegetative cell.

### Exclusions and nearby traits

- **Ionizing-radiation resistance is not equivalent.** Gamma/X-ray resistance involves extensive oxidative damage and double-strand breaks; overlap with UV tolerance does not justify transferring a gamma-radiation D10 value into this trait.
- **Desiccation tolerance is distinct.** Shared protein-protection and DNA-repair systems may create correlated phenotypes, especially in *Deinococcus*, but desiccation survival is not evidence of UV survival by itself.
- **UV avoidance is not cellular tolerance.** Burial, motility away from light, host-tissue protection, mineral shielding, and self-shading reduce received dose. Curate these as exposure modifiers unless survival of directly irradiated cells is demonstrated.
- **Inactivation is not necessarily death.** Loss of colony formation, membrane damage, delayed growth, and inability to infect are different endpoints.
- **Gene presence is not phenotype evidence.** A predicted photolyase, NER operon, pigment cluster, or antioxidant gene supports mechanistic potential, not the trait, without a survival assay or functional perturbation.
- **Photoreactivation must be separated from dark repair.** Light after exposure can strongly increase apparent resistance; studies that do not control post-irradiation illumination may conflate damage induction with recovery capacity.

## 2. Current mechanistic model

UV-B and UV-C induce bulky DNA photolesions, especially cyclobutane pyrimidine dimers (CPDs) and 6-4 photoproducts. These lesions impede replication and transcription and may produce mutagenesis or loss of viability. In the best-supported graph, lesion removal branches into two routes:

1. **Photoreactivation:** lesion-specific photolyases bind CPDs or 6-4 photoproducts and use photoreactivating light to reverse the lesion.
2. **Dark repair:** UvrA/UvrB recognize damaged DNA, UvrC incises it, and downstream excision, synthesis, and ligation restore the duplex.

The routes can be strongly complementary. In *P. syringae*, either a `phr` or `uvrA` mutation reduced survival by approximately 10²-fold, whereas the double mutant was reduced by more than 10⁶-fold under solar UV-B. The same study observed a faster and stronger RecA-mediated SOS response in repair mutants, consistent with accumulation of unrepaired lesions; this supports an edge from damage accumulation to SOS induction, but not by itself a direct edge from SOS induction to tolerance. (gunasekera2006roleofnucleotide pages 1-2)

In marine *Synechococcus* RS9916, photoreactivation accounted for most recovery, and multiple photolyases collectively supported exceptional survival. At 1,000 J m⁻² UV-B and 250 J m⁻² UV-C, survival differences relative to *E. coli* were reported on the order of one million-fold and 100,000-fold, respectively. However, assignments of Phr2/Phr3 as CPD photolyases and Phr4/Phr5 as a 6-4 photolyase remain sequence/structure-based predictions pending direct biochemical substrate assays. (haney2022multiplephotolyasesprotect pages 12-13, haney2022multiplephotolyasesprotect pages 4-7)

## 3. Candidate nodes

### Environmental and assay nodes

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| ultraviolet radiation | Environmental factor | **ENVO term to be resolved**; label-only until verified | Record UV-A, UV-B, or UV-C as assay qualifiers rather than treating them as equivalent. |
| UV-B radiation | Experimental/environmental factor | Label-only candidate | Solar study: 290–320 nm, 4.5 kJ m⁻². (gunasekera2006roleofnucleotide pages 1-2) |
| UV-C radiation | Experimental factor | Label-only candidate | Haloarchaeal study: 254 nm, 0–144 J m⁻². (nag2023genomicanalysisof pages 2-4) |
| UV fluence | Measurement/assay attribute | Unit: J m⁻² | Mandatory quantitative qualifier when available. |
| photoreactivating light | Experimental factor | Label-only candidate | Enables photolyase-dependent recovery; spectrum and duration should be recorded. |
| dark recovery | Experimental condition | Label-only candidate | Operationally separates light-independent repair from photoreactivation. |
| surviving fraction / CFU | Phenotype measurement | Label-only candidate | Prefer raw survival curve or D10 over an unqualified “resistant” label. |

### Damage and chemical nodes

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| cyclobutane pyrimidine dimer | DNA lesion | Label-only candidate; resolve CHEBI identifier before YAML entry | Primary UV-B photoproduct in the *Pseudomonas* study. (gunasekera2006roleofnucleotide pages 1-2) |
| 6-4 photoproduct | DNA lesion | Label-only candidate; resolve CHEBI identifier | UV-C produces a higher 6-4:CPD ratio than UV-B in the cited interpretation. (haney2022multiplephotolyasesprotect pages 12-13) |
| reactive oxygen species | Chemical class | `CHEBI:26523` | Secondary UV damage is plausible, but trait-level causal edges require direct survival evidence. |
| hydrogen peroxide | Chemical | `CHEBI:16240` | Relevant to oxidative-stress studies; not a universal UV-lesion intermediate. |

### Processes and pathways

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| DNA photoreactivation | Biological process | `GO:0000719` | Core pathway; verify ontology release before committing. |
| nucleotide-excision repair | Biological process | `GO:0006289` | Core light-independent pathway. |
| transcription-coupled NER | Biological process | Label-only candidate | Mechanistically relevant via Mfd, but insufficient trait-specific survival evidence was retrieved for a core edge. |
| homologous recombination | Biological process | `GO:0035825` | Important in genome restoration; UV-tolerance contribution is taxon- and lesion-context-dependent. |
| SOS response | Biological process | `GO:0009432` | Better curated downstream of persistent DNA damage than directly upstream of tolerance. |
| DNA ligation | Biological process | `GO:0006266` | PprA stimulates ligation in *D. radiodurans*. (selvam2013ddraddrdand pages 6-7) |
| response to UV | Biological process | `GO:0009411` | Broad response term; not equivalent to the survival trait. |

### Genes, proteins, and complexes

| Candidate node | Type | Grounding recommendation | Role/evidence status |
|---|---|---|---|
| CPD photolyase / `phr` | Enzyme/gene | `GO:0003904` for photolyase activity; use taxon-specific UniProt only after sequence resolution | Directly supported by deletion phenotypes in *Pseudomonas*, *Synechococcus*, and haloarchaea. (gunasekera2006roleofnucleotide pages 1-2, nag2023genomicanalysisof pages 2-4) |
| Phr2 | Protein | Taxon-specific label; add verified UniProt per strain | Required for photorepair in *Halobacterium* NRC-1; Phr1 was not required. (nag2023genomicanalysisof pages 2-4) |
| Phr2/Phr3 | Proteins | *Synechococcus* strain-specific labels | Survival roles are direct; CPD substrate assignments remain predicted. (haney2022multiplephotolyasesprotect pages 12-13) |
| Phr4/Phr5 system | Protein system | *Synechococcus* strain-specific label | UV-C survival role is direct; 6-4 substrate assignment remains predicted. (haney2022multiplephotolyasesprotect pages 12-13) |
| UvrA–UvrB–UvrC excinuclease | Protein complex | Use individual verified UniProt accessions plus `GO:0006289` | Core NER module; `uvrA` or `uvrC` deletion greatly reduced haloarchaeal dark repair. (nag2023genomicanalysisof pages 2-4) |
| UvrD, DNA polymerase, DNA ligase | Downstream NER factors | Resolve per taxon | Mechanistically expected, but do not add trait edges without source-specific evidence. |
| Mfd | Transcription-repair coupling factor | Resolve taxon-specific UniProt | Candidate extension, not yet justified as a core tolerance node by the gathered survival evidence. |
| RecA | Recombinase/regulator | Resolve taxon-specific UniProt; `GO:0003697` may describe ssDNA binding but is not protein identity | Persistent lesions induce RecA/SOS; direct survival contribution must be supported per organism. (gunasekera2006roleofnucleotide pages 1-2) |
| PprA | DNA repair protein | *D. radiodurans*-specific UniProt to resolve | Deletion reduced UV survival up to eightfold; binds DNA ends and promotes ligation. (selvam2013ddraddrdand pages 1-2, selvam2013ddraddrdand pages 6-7) |
| DdrA | DNA end-protection protein | *D. radiodurans*-specific UniProt to resolve | Protects 3′ ssDNA ends; strong synthetic UV phenotype with `pprA`. (selvam2013ddraddrdand pages 6-7) |
| DdrD | Damage-response protein | *D. radiodurans*-specific UniProt to resolve | Function remains unclear; strong synthetic phenotype with `pprA`. (selvam2013ddraddrdand pages 1-2) |
| IrrE–DdrO regulatory module | Regulatory module | Label-only until taxon-specific IDs are verified | Appropriate only in a *Deinococcus*-specific extension. |
| catalase / superoxide dismutase | Antioxidant enzymes | EC and UniProt IDs must be taxon-specific | UV-induced expression and genomic association are supportive but generally weaker than repair-gene perturbations. (kurth2015genomicandproteomic pages 1-2) |

### Organism-context nodes

Use verified NCBITaxon identifiers during implementation rather than inferring them from species names. High-value organism contexts are *Deinococcus radiodurans* R1, *Halobacterium* sp. NRC-1, *Pseudomonas syringae* pv. *syringae* B728a, and marine *Synechococcus* RS9916. The 2023 haloarchaeal comparison is especially useful because it tested nine strains from high-irradiance surface environments, cold lakes, and ancient subsurface halite rather than assuming UV tolerance is uniform across Haloarchaea. (nag2023genomicanalysisof pages 2-4, nag2023genomicanalysisof pages 1-2)

## 4. Candidate causal edges

The following table is the recommended evidence ledger. “Core” means suitable for the principal TraitMech graph; “taxon-specific extension” means suitable only with an organism qualifier; and “uncertain” means retain as a research note rather than a YAML causal assertion.

| Proposed subject–predicate–object edge | Evidence class | Taxon/assay context | DOI and publication date | Short supporting snippet paraphrased closely from retrieved evidence | Curation decision |
|---|---|---|---|---|---|
| UV-C exposure → causes → cyclobutane pyrimidine dimers (CPDs) and 6-4 photoproducts | biochemical/general | General microbial UV damage context; haloarchaea review/experiment context | 10.3390/microorganisms11030607 (Feb 2023) | The study states that UV-C causes thymine dimers and 6-4 photoproducts; CPDs are the dominant lesions discussed across repair pathways (nag2023genomicanalysisof pages 1-2, nag2023genomicanalysisof pages 2-4) | core |
| UV-B / solar UVB exposure → causes → CPD accumulation | direct perturbation | *Pseudomonas syringae* pv. *syringae* B728a; solar UVB 4.5 kJ m−2, 290–320 nm | 10.1111/j.1365-2672.2006.02841.x (May 2006) | Insertional *phr* and *uvrA* mutants were used to test solar UVB survival, and CPDs were identified as the primary UVB photoproducts accumulating during exposure (gunasekera2006roleofnucleotide pages 1-2) | core |
| Photoreactivating light → enables → photolyase-mediated photorepair | direct perturbation | Haloarchaea UV-C assays at 254 nm, 0–144 J/m²; light vs dark recovery | 10.3390/microorganisms11030607 (Feb 2023) | CFU survival was compared after UV-C with plates exposed either to photoreactivating light or kept dark; strains with light recovery showed markedly better survival, including complete survival at 144 J/m² for top strains (nag2023genomicanalysisof pages 2-4, nag2023genomicanalysisof pages 4-6) | core |
| Photolyase (Phr2) → mediates → direct photorepair of UV lesions | direct perturbation | *Halobacterium* sp. NRC-1 and related haloarchaea; UV-C 254 nm | 10.3390/microorganisms11030607 (Feb 2023) | Knockout evidence in NRC-1 showed Phr2 is essential for photorepair, whereas Phr1 is not; superior photorepair correlates with conserved *phr2* in tolerant strains (nag2023genomicanalysisof pages 2-4, nag2023genomicanalysisof pages 13-15) | core |
| UvrABCD excinuclease / UvrA / UvrC → mediates → dark repair of UV damage | direct perturbation | *Halobacterium* sp. NRC-1 and related haloarchaea; dark recovery after UV-C | 10.3390/microorganisms11030607 (Feb 2023) | The paper reports dark repair is mediated by bacterial-type nucleotide excision repair, and deletion of *uvrA* or *uvrC* greatly diminished dark repair (nag2023genomicanalysisof pages 2-4) | core |
| Photolyase (*phr*) loss → decreases → UV survival | direct perturbation | *Pseudomonas aeruginosa* / *P. syringae* photolyase mutants under UV-B with photoreactivation | 10.1128/AEM.67.4.1405-1411.2001 (Apr 2001) | The mutant analysis directly tested contribution of photoreactivation, nucleotide excision repair, and mutagenic repair to survival after UV-B; *phr* mutants were less UV-B tolerant (gunasekera2006roleofnucleotide pages 1-2) | core |
| UvrA-dependent nucleotide excision repair → increases → solar UVB survival | direct perturbation | *Pseudomonas syringae* pv. *syringae* B728a; solar UVB 4.5 kJ m−2 | 10.1111/j.1365-2672.2006.02841.x (May 2006) | Single mutants in *uvrA* or *phr* each showed about 10²-fold survival reduction, while the *uvrA phr* double mutant showed >10⁶-fold reduction, indicating both repair routes are essential (gunasekera2006roleofnucleotide pages 1-2) | core |
| Photoreactivation + nucleotide excision repair → jointly increase → UV survival | direct perturbation | *Pseudomonas syringae* pv. *syringae* B728a; solar UVB assay | 10.1111/j.1365-2672.2006.02841.x (May 2006) | The double-mutant result (>10⁶-fold drop) was far more severe than either single mutant (~10²-fold), supporting additive or complementary roles for photolyase and NER during solar UV exposure (gunasekera2006roleofnucleotide pages 1-2) | core |
| RecA / SOS response → is induced by → UV damage accumulation | direct perturbation | *Pseudomonas syringae* pv. *syringae* B728a; solar UVB | 10.1111/j.1365-2672.2006.02841.x (May 2006) | RecA-mediated SOS response was more rapid and intense in repair mutants, consistent with increased unrepaired UV lesions; this supports a damage-response edge more than a tolerance-conferring edge (gunasekera2006roleofnucleotide pages 1-2) | taxon-specific extension |
| Phr2 and Phr3 → repair/predominantly protect against → CPD-associated UV damage | direct perturbation for survival; predicted substrate assignment | Marine *Synechococcus* RS9916; UV-B and UV-C survival with white-light photoreactivation | 10.1128/mBio.01511-22 (Aug 2022) | Loss of Phr2 or Phr3 significantly reduced survival after UV-B; authors interpret these as CPD photolyases, but exact biochemical substrate specificity is inferred from sequence/structure and needs in vitro confirmation (haney2022multiplephotolyasesprotect pages 12-13, haney2022multiplephotolyasesprotect pages 4-7) | taxon-specific extension |
| Phr4/Phr5 → repair/predominantly protect against → 6-4 photoproduct-associated UV damage | direct perturbation for survival; predicted substrate assignment | Marine *Synechococcus* RS9916; UV-C survival with white-light photoreactivation | 10.1128/mBio.01511-22 (Aug 2022) | Loss of the Phr4/Phr5 system reduced survival after UV-C, matching the higher 6-4:CPD lesion ratio under UV-C; however, the 6-4 photolyase assignment is predicted rather than directly biochemically verified (haney2022multiplephotolyasesprotect pages 12-13) | taxon-specific extension |
| Multiple photolyases → confer → exceptional UV tolerance | direct perturbation | Marine *Synechococcus* RS9916; UV-B 1,000 J m⁻² and UV-C 250 J m⁻² | 10.1128/mBio.01511-22 (Aug 2022) | *Synechococcus* survived UV-B and UV-C at rates vastly higher than *E. coli*—about million-fold and 100,000-fold differences respectively—and survival depended on photoreactivating light (haney2022multiplephotolyasesprotect pages 4-7) | taxon-specific extension |
| PprA deletion → decreases → UV resistance | direct perturbation | *Deinococcus radiodurans* R1; UV-C from germicidal lamp at 25 J m⁻² s⁻¹ | 10.1371/journal.pone.0069007 (Jul 2013) | Deleting *pprA* sensitized cells up to eightfold relative to wild type; at 1000 J m⁻², double mutants with *ddrA* or *ddrD* became 100- to 1000-fold more sensitive than the *pprA* single mutant (selvam2013ddraddrdand pages 1-2, selvam2013ddraddrdand pages 6-7) | taxon-specific extension |
| DdrA + PprA → jointly support → UV tolerance | direct perturbation | *Deinococcus radiodurans* R1; 1000 J m⁻² UV | 10.1371/journal.pone.0069007 (Jul 2013) | The Δ*ddrA* Δ*pprA* strain was 100-fold more UV sensitive than the *pprA* mutant alone, supporting a complementary tolerance role outside classic excision repair or homologous recombination (selvam2013ddraddrdand pages 1-2, selvam2013ddraddrdand pages 6-7) | taxon-specific extension |
| DdrD + PprA → jointly support → UV tolerance | direct perturbation | *Deinococcus radiodurans* R1; 1000 J m⁻² UV | 10.1371/journal.pone.0069007 (Jul 2013) | The Δ*ddrD* Δ*pprA* strain was 1000-fold more UV sensitive than the *pprA* single mutant, indicating a strong complementary role in UV tolerance (selvam2013ddraddrdand pages 1-2) | taxon-specific extension |
| Surface high-irradiance origin / conserved *phr2* → correlates with → higher haloarchaeal UV tolerance | phenotype correlation | Diverse haloarchaea from surface brines vs subsurface halite; UV-C 254 nm 0–144 J/m² | 10.3390/microorganisms11030607 (Feb 2023) | Surface isolates with conserved *phr2* had higher UV survival and stronger photorepair; subsurface strains had divergent or absent *phr2* and poorer survival, but this is correlation across isolates rather than direct perturbation in each strain (nag2023genomicanalysisof pages 6-8, nag2023genomicanalysisof pages 1-2, nag2023genomicanalysisof pages 11-13) | uncertain/do not curate |
| Antioxidant/protein-protection systems → contribute to → UV tolerance | biochemical/general | General radiation-resistance literature, especially *Deinococcus* and polyextremophiles | 10.1128/MMBR.00015-10 (Mar 2011); 10.3389/fmicb.2015.00328 (Apr 2015) | Reviews and proteomics support oxidative-stress defense and catalase upregulation during UV exposure, but the retrieved conversation evidence is not as direct for UV-tolerance curation as for photolyase and NER edges (kurth2015genomicandproteomic pages 1-2) | uncertain/do not curate |


*Table: This table compiles candidate causal edges for microbial UV-radiation tolerance with evidence strength, assay context, and curation decisions. It is designed to separate core broadly curatable mechanisms from taxon-specific extensions and correlation-only claims.*

### Minimal recommended core graph

A conservative first revision could contain the following backbone:

1. `UV radiation —causes→ cyclobutane pyrimidine dimer`
2. `UV radiation —causes→ 6-4 photoproduct`
3. `cyclobutane pyrimidine dimer —decreases→ DNA replication/transcription integrity`
4. `6-4 photoproduct —decreases→ DNA replication/transcription integrity`
5. `photoreactivating light —enables→ photolyase activity`
6. `CPD photolyase —repairs→ cyclobutane pyrimidine dimer`
7. `6-4 photolyase —repairs→ 6-4 photoproduct`
8. `UvrABC nucleotide-excision repair —removes→ UV-induced DNA photolesion`
9. `DNA photolesion repair —increases→ post-UV survival`
10. `post-UV survival —realizes→ traitmech:000009`

Edges 1, 2, and 5–9 have direct or closely matched support in the gathered microbial studies. Edges 3–4 are biologically standard but should receive a lesion-specific source before final YAML insertion if the project requires every intermediate edge to have direct microbial evidence. The *Pseudomonas* double-mutant result provides particularly strong evidence that photoreactivation and NER are complementary rather than interchangeable. (gunasekera2006roleofnucleotide pages 1-2)

## 5. Recent developments, applications, and quantitative evidence

### 2023 haloarchaeal comparative study

Nag and colleagues tested nine haloarchaeal strains rather than generalizing from NRC-1. Surface isolates from high-solar-irradiance environments showed the highest survival and photorepair, whereas subsurface Permian-halite isolates were less tolerant and carried divergent or absent `phr2`. Some light-recovered strains survived the highest tested dose, 144 J m⁻², while most strains under dark recovery showed approximately 3–4 log killing at that dose. NRC-1 was reported as more than twice as tolerant as yeast, approximately fivefold more tolerant than *E. coli*, and approximately 50-fold more tolerant than human cells under the comparison used by the authors. (nag2023genomicanalysisof pages 2-4, nag2023genomicanalysisof pages 4-6)

The important expert-level interpretation is that UV tolerance is **not a uniform haloarchaeal character**. Conserved `phr2`, environmental origin, and measured photorepair covaried, but amino-acid substitutions and modeled DNA/FAD interactions were not directly validated biochemically. Those variant-level claims should therefore remain uncertain. (nag2023genomicanalysisof pages 6-8, nag2023genomicanalysisof pages 11-13)

### Multi-photolyase architecture in marine cyanobacteria

The *Synechococcus* work demonstrates that one organism can partition UV protection across several photolyases and that lesion spectrum matters: UV-B and UV-C do not generate identical lesion ratios. This argues against a graph containing a single undifferentiated “photolyase” node where lineage-specific substrate assignments are known. Nevertheless, because the Phr2/Phr3 and Phr4/Phr5 substrate labels were inferred rather than measured in vitro, the graph should distinguish **demonstrated survival function** from **predicted lesion specificity**. (haney2022multiplephotolyasesprotect pages 12-13)

### *Deinococcus* auxiliary survival systems

At 1,000 J m⁻², `ΔddrA ΔpprA` and `ΔddrD ΔpprA` strains were respectively 100- and 1,000-fold more sensitive than a strain lacking only `pprA`; deletion of `pprA` alone reduced viability by as much as eightfold. These results support complementary damage-tolerance functions, but the investigators found no evidence that DdrA, DdrD, or PprA directly performs excision repair or homologous recombination. They should be represented as enabling/protective extensions, not substituted for photolyase or NER. (selvam2013ddraddrdand pages 1-2, selvam2013ddraddrdand pages 6-7)

### Real-world implementation relevance

- **Water and surface disinfection:** Photoreactivation after UV treatment can restore culturability, so validation protocols should control post-treatment light and measure delayed regrowth. The trait graph can inform selection of challenge organisms and explain apparent treatment failure.
- **Agriculture and phyllosphere ecology:** The *P. syringae* data show that photoreactivation and NER operate during solar UV-B exposure relevant to leaf surfaces; repair capacity can influence persistence of both beneficial and pathogenic epiphytes. (gunasekera2006roleofnucleotide pages 1-2)
- **Marine primary production:** Multiple photolyases permit photosynthetic cyanobacteria to occupy the strongly irradiated photic zone, where light is simultaneously required for photosynthesis, damaging, and usable for photorepair. (haney2022multiplephotolyasesprotect pages 12-13)
- **Astrobiology and planetary protection:** Haloarchaeal variation is relevant to survival in surface brines, ancient halite, and Mars-like irradiation. It also cautions that taxonomic identity alone cannot predict persistence under spacecraft or planetary UV exposure. (nag2023genomicanalysisof pages 1-2)
- **Biotechnology:** Photolyases and extremophile DNA-protection systems are candidates for engineered UV robustness and post-exposure DNA repair. Such applications are plausible, but an application node should not be inserted into the causal trait graph unless engineering experiments demonstrate increased microbial survival.

## 6. Warnings: claims not yet ready for TraitMech curation

1. **Do not use the supplied 700 J m⁻² UV-C D10 statement without checking the primary methods and endpoint.** The gathered evidence supports exceptional *D. radiodurans* survival, but dose survived, D10, D37, and assay ceiling are not synonymous.
2. **Do not import the >12-kGy gamma-radiation D10 into this UV trait.** It supports a broader radiation-resistant phenotype, not the UV-specific causal graph.
3. **Do not assert that UvrABC is universally required.** In *D. radiodurans*, NER can be genetically redundant with a UV-endonuclease pathway, whereas it is strongly required in *Pseudomonas* and contributes to haloarchaeal dark repair. (selvam2013ddraddrdand pages 1-2, gunasekera2006roleofnucleotide pages 1-2)
4. **Do not curate `phr2` sequence conservation as causing tolerance across haloarchaeal isolates.** The cross-isolate result is correlation; only NRC-1 pathway perturbations provide direct functional support. (nag2023genomicanalysisof pages 2-4, nag2023genomicanalysisof pages 6-8)
5. **Do not curate predicted Phr2/Phr3 CPD or Phr4/Phr5 6-4 specificity as experimentally proven.** Survival phenotypes are direct, but substrate assignments need purified-enzyme or lesion-removal measurements. (haney2022multiplephotolyasesprotect pages 12-13)
6. **Do not infer UV tolerance from a genome alone.** Predicted photolyases, carotenoid clusters, mycosporine-like amino-acid pathways, catalases, or repair operons require phenotype and preferably perturbation evidence.
7. **Do not make pigments, biofilms, spores, or extracellular matrix core nodes yet.** They can reduce delivered dose, but no sufficiently direct causal survival evidence for these nodes was retrieved here.
8. **Do not place Mfd-mediated transcription-coupled repair in the core graph yet.** It is mechanistically credible, but the gathered material did not establish a direct microbial UV-survival effect comparable to the `phr` and `uvrA/uvrC` perturbations.
9. **Avoid unqualified ontology identifiers.** Resolve strain-specific UniProt and NCBITaxon CURIEs during implementation; label-only nodes are preferable to incorrect IDs.

## 7. DOI-first bibliography

1. **Nag S, et al.** “Genomic Analysis of Haloarchaea from Diverse Environments, including Permian Halite, Reveals Diversity of Ultraviolet Radiation Survival and DNA Photolyase Gene Variants.” *Microorganisms* 11:607. **February 2023.** DOI: [10.3390/microorganisms11030607](https://doi.org/10.3390/microorganisms11030607). (nag2023genomicanalysisof pages 2-4)
2. **Haney AM, et al.** “Multiple Photolyases Protect the Marine Cyanobacterium *Synechococcus* from Ultraviolet Radiation.” *mBio* 13. **August 2022.** DOI: [10.1128/mbio.01511-22](https://doi.org/10.1128/mbio.01511-22). (haney2022multiplephotolyasesprotect pages 12-13, haney2022multiplephotolyasesprotect pages 4-7)
3. **Selvam K, Duncan JR, Tanaka M, Battista JR.** “DdrA, DdrD, and PprA: Components of UV and Mitomycin C Resistance in *Deinococcus radiodurans* R1.” *PLoS ONE* 8:e69007. **July 2013.** DOI: [10.1371/journal.pone.0069007](https://doi.org/10.1371/journal.pone.0069007). (selvam2013ddraddrdand pages 1-2, selvam2013ddraddrdand pages 6-7)
4. **Gunasekera TS, Sundin GW.** “Role of nucleotide excision repair and photoreactivation in the solar UVB radiation survival of *Pseudomonas syringae* pv. *syringae* B728a.” *Journal of Applied Microbiology* 100:1073–1083. **May 2006.** DOI: [10.1111/j.1365-2672.2006.02841.x](https://doi.org/10.1111/j.1365-2672.2006.02841.x). (gunasekera2006roleofnucleotide pages 1-2)
5. **Kim JJ, Sundin GW.** “Construction and Analysis of Photolyase Mutants of *Pseudomonas aeruginosa* and *Pseudomonas syringae*.” *Applied and Environmental Microbiology* 67:1405–1411. **April 2001.** DOI: [10.1128/AEM.67.4.1405-1411.2001](https://doi.org/10.1128/AEM.67.4.1405-1411.2001).
6. **Kurth D, et al.** “Genomic and proteomic evidences unravel the UV-resistome of the poly-extremophile *Acinetobacter* sp. Ver3.” *Frontiers in Microbiology* 6:328. **April 2015.** DOI: [10.3389/fmicb.2015.00328](https://doi.org/10.3389/fmicb.2015.00328). Its catalase and proteomic findings should be treated as supportive rather than equivalent to gene-deletion evidence. (kurth2015genomicandproteomic pages 1-2)

## Curation conclusion

The strongest defensible TraitMech graph is a lesion-centered model in which UV-B/UV-C produce CPDs and 6-4 photoproducts; photoreactivating light enables lesion-specific photolyases; UvrABC provides complementary dark repair; and lesion removal increases post-exposure survival. Add PprA/DdrA/DdrD, individual photolyase paralogs, RecA/SOS, antioxidants, and environmental adaptation only as taxon-specific or uncertainty-qualified extensions. This approach preserves the mechanistic value of the existing 10-node/9-edge graph while preventing correlation, irradiation band, and recovery-condition differences from being encoded as universal causation.

References

1. (gunasekera2006roleofnucleotide pages 1-2): T.S. Gunasekera and G.W. Sundin. Role of nucleotide excision repair and photoreactivation in the solar uvb radiation survival of pseudomonas syringae pv. syringae b728a. Journal of Applied Microbiology, 100:1073-1083, May 2006. URL: https://doi.org/10.1111/j.1365-2672.2006.02841.x, doi:10.1111/j.1365-2672.2006.02841.x. This article has 44 citations and is from a peer-reviewed journal.

2. (nag2023genomicanalysisof pages 2-4): Sagorika Nag, Priya DasSarma, David J. Crowley, Rafael Hamawi, Samantha Tepper, Brian P. Anton, Daniel Guzmán, and Shiladitya DasSarma. Genomic analysis of haloarchaea from diverse environments, including permian halite, reveals diversity of ultraviolet radiation survival and dna photolyase gene variants. Microorganisms, 11:607, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030607, doi:10.3390/microorganisms11030607. This article has 10 citations.

3. (selvam2013ddraddrdand pages 1-2): Kathiresan Selvam, Jana R. Duncan, Masashi Tanaka, and John R. Battista. Ddra, ddrd, and ppra: components of uv and mitomycin c resistance in deinococcus radiodurans r1. PLoS ONE, 8:e69007, Jul 2013. URL: https://doi.org/10.1371/journal.pone.0069007, doi:10.1371/journal.pone.0069007. This article has 76 citations and is from a peer-reviewed journal.

4. (haney2022multiplephotolyasesprotect pages 12-13): Allissa M. Haney, Joseph E. Sanfilippo, Laurence Garczarek, Frédéric Partensky, and David M. Kehoe. Multiple photolyases protect the marine cyanobacterium <i>synechococcus</i> from ultraviolet radiation. Aug 2022. URL: https://doi.org/10.1128/mbio.01511-22, doi:10.1128/mbio.01511-22. This article has 12 citations and is from a domain leading peer-reviewed journal.

5. (haney2022multiplephotolyasesprotect pages 4-7): Allissa M. Haney, Joseph E. Sanfilippo, Laurence Garczarek, Frédéric Partensky, and David M. Kehoe. Multiple photolyases protect the marine cyanobacterium <i>synechococcus</i> from ultraviolet radiation. Aug 2022. URL: https://doi.org/10.1128/mbio.01511-22, doi:10.1128/mbio.01511-22. This article has 12 citations and is from a domain leading peer-reviewed journal.

6. (selvam2013ddraddrdand pages 6-7): Kathiresan Selvam, Jana R. Duncan, Masashi Tanaka, and John R. Battista. Ddra, ddrd, and ppra: components of uv and mitomycin c resistance in deinococcus radiodurans r1. PLoS ONE, 8:e69007, Jul 2013. URL: https://doi.org/10.1371/journal.pone.0069007, doi:10.1371/journal.pone.0069007. This article has 76 citations and is from a peer-reviewed journal.

7. (kurth2015genomicandproteomic pages 1-2): Daniel Kurth, Carolina Belfiore, Marta F. Gorriti, Néstor Cortez, María E. Farias, and Virginia H. Albarracín. Genomic and proteomic evidences unravel the uv-resistome of the poly-extremophile acinetobacter sp. ver3. Frontiers in Microbiology, Apr 2015. URL: https://doi.org/10.3389/fmicb.2015.00328, doi:10.3389/fmicb.2015.00328. This article has 73 citations and is from a peer-reviewed journal.

8. (nag2023genomicanalysisof pages 1-2): Sagorika Nag, Priya DasSarma, David J. Crowley, Rafael Hamawi, Samantha Tepper, Brian P. Anton, Daniel Guzmán, and Shiladitya DasSarma. Genomic analysis of haloarchaea from diverse environments, including permian halite, reveals diversity of ultraviolet radiation survival and dna photolyase gene variants. Microorganisms, 11:607, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030607, doi:10.3390/microorganisms11030607. This article has 10 citations.

9. (nag2023genomicanalysisof pages 4-6): Sagorika Nag, Priya DasSarma, David J. Crowley, Rafael Hamawi, Samantha Tepper, Brian P. Anton, Daniel Guzmán, and Shiladitya DasSarma. Genomic analysis of haloarchaea from diverse environments, including permian halite, reveals diversity of ultraviolet radiation survival and dna photolyase gene variants. Microorganisms, 11:607, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030607, doi:10.3390/microorganisms11030607. This article has 10 citations.

10. (nag2023genomicanalysisof pages 13-15): Sagorika Nag, Priya DasSarma, David J. Crowley, Rafael Hamawi, Samantha Tepper, Brian P. Anton, Daniel Guzmán, and Shiladitya DasSarma. Genomic analysis of haloarchaea from diverse environments, including permian halite, reveals diversity of ultraviolet radiation survival and dna photolyase gene variants. Microorganisms, 11:607, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030607, doi:10.3390/microorganisms11030607. This article has 10 citations.

11. (nag2023genomicanalysisof pages 6-8): Sagorika Nag, Priya DasSarma, David J. Crowley, Rafael Hamawi, Samantha Tepper, Brian P. Anton, Daniel Guzmán, and Shiladitya DasSarma. Genomic analysis of haloarchaea from diverse environments, including permian halite, reveals diversity of ultraviolet radiation survival and dna photolyase gene variants. Microorganisms, 11:607, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030607, doi:10.3390/microorganisms11030607. This article has 10 citations.

12. (nag2023genomicanalysisof pages 11-13): Sagorika Nag, Priya DasSarma, David J. Crowley, Rafael Hamawi, Samantha Tepper, Brian P. Anton, Daniel Guzmán, and Shiladitya DasSarma. Genomic analysis of haloarchaea from diverse environments, including permian halite, reveals diversity of ultraviolet radiation survival and dna photolyase gene variants. Microorganisms, 11:607, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030607, doi:10.3390/microorganisms11030607. This article has 10 citations.