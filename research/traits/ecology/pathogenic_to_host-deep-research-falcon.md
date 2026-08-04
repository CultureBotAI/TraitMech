---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:35:09.222646'
end_time: '2026-08-03T23:47:02.173815'
duration_seconds: 712.95
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pathogenic to host
  trait_identifier: METPO:1004000
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: pathogenic_to_host
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype where a microbe is a pathogen of some host organism.
  parent_traits: METPO:1000059
  synonyms: General.keywords, Safety information.risk assessment
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162938: virulence factors
    (Virulence-factor review supports the encoding of dedicated virulence factors
    as the molecular basis of host pathogenicity.) | DOI:10.1038/nrmicro1592: secretion
    systems (Secretion-systems review supports protein secretion machineries as central
    effectors of host pathogenicity across kingdoms.)'
  causal_graph_summary: 'pathogenic_to_host_virulence_factor_program: 14 nodes, 12
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pathogenic to host
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1004000
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype where a microbe is a pathogen of some host organism.
- **Parent traits:** METPO:1000059
- **Synonyms:** General.keywords, Safety information.risk assessment
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the encoding of dedicated virulence factors as the molecular basis of host pathogenicity.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports protein secretion machineries as central effectors of host pathogenicity across kingdoms.)
- **Existing causal graph summary:** pathogenic_to_host_virulence_factor_program: 14 nodes, 12 edges

## Research Objective

Research the microbial trait **pathogenic to host** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/pathogenic_to_host.yaml`.

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
- **Trait label:** pathogenic to host
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1004000
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype where a microbe is a pathogen of some host organism.
- **Parent traits:** METPO:1000059
- **Synonyms:** General.keywords, Safety information.risk assessment
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the encoding of dedicated virulence factors as the molecular basis of host pathogenicity.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports protein secretion machineries as central effectors of host pathogenicity across kingdoms.)
- **Existing causal graph summary:** pathogenic_to_host_virulence_factor_program: 14 nodes, 12 edges

## Research Objective

Research the microbial trait **pathogenic to host** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/pathogenic_to_host.yaml`.

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


# Curation-focused research report: microbial trait “pathogenic to host”

## 1. Scope summary

**Trait record**

- **Trait label:** pathogenic to host
- **Trait identifier:** `METPO:1004000`
- **Category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** “A phenotype where a microbe is a pathogen of some host organism.”
- **Parent:** `METPO:1000059`

### Operational interpretation

For TraitMech, `METPO:1004000` should represent a **relational, context-dependent capacity of a microbial strain or lineage to cause host damage or disease in at least one susceptible host**. It is not adequately represented by a single universal molecular marker. Current expert models treat disease as an outcome of microbial functions interacting with host susceptibility, tissue site, microbiota, dose, and environment. Accordingly, a causal graph should terminate in demonstrated host damage, disease, or reduced host fitness—not merely detection of a microbe or virulence-associated gene. Recent host-adaptation work identifies colonization, nutrient acquisition, and immune evasion as major stages, while emphasizing that even small sequence changes can alter host tropism (barber2024mechanismsofhost pages 1-2).

### Boundaries and nearby concepts

- **Colonization:** establishment or persistence at a host site without necessarily causing damage. Adhesion and colonization are upstream enabling processes, not equivalent to pathogenicity.
- **Infection:** entry and multiplication in a host. Infection may remain asymptomatic; therefore, infection alone does not always establish the terminal “pathogenic to host” phenotype.
- **Disease/pathology:** measurable host damage or dysfunction. This is the strongest endpoint for curating pathogenicity.
- **Virulence:** the degree or quantitative expression of pathogenicity under specified conditions. “Pathogenic” is principally categorical; virulence is comparative or continuous.
- **Commensal:** an organism that can inhabit a host without ordinarily causing damage. A commensal can acquire virulence determinants or become harmful in a changed context.
- **Opportunistic pathogen/pathobiont:** pathogenic behavior is conditional on immune impairment, barrier disruption, dysbiosis, altered tissue location, medical devices, or other ecological changes. Enterococci, for example, are normal gut residents that become consequential pathogens in immunocompromised hosts (sangiorgio2024theimpactof pages 7-9).
- **Antimicrobial resistance:** resistance affects treatment survival and clinical outcome but is neither necessary nor sufficient for pathogenicity. It should be modeled as a modifier of persistence/treatment failure, not as a direct synonym of `METPO:1004000`.
- **Virulence-gene carriage:** genomic potential is weaker evidence than expression, mutant phenotype, host-cell damage, or an animal/plant disease model.
- **Polymicrobial disease:** community interactions may generate disease even when no individual isolate reproduces the complete phenotype. Such edges should be represented as community- or context-specific rather than assigned unconditionally to every member.

## 2. Recommended causal architecture

The graph should be modular rather than implying that every pathogen uses every mechanism:

1. **Host/environment sensing and virulence regulation**
2. **Access, adhesion, and colonization**
3. **Nutrient acquisition and in-host fitness**
4. **Secretion and effector delivery**
5. **Invasion, immune evasion, and persistence**
6. **Direct or inflammation-mediated host damage**
7. **Disease/pathogenic-to-host endpoint**

| Module/branch | Representative causal chain | Evidence strength | Scope | Curation recommendation |
|---|---|---|---|---|
| General virulence backbone | adhesins/fimbriae → host adherence/colonization; flagella/motility → access to host surfaces; secretion systems (especially T3SS/T4SS) → effector delivery → host-cell manipulation; toxins/proteases → host damage; siderophores/nutrient acquisition → in-host fitness; capsule/LPS/biofilm/antigenic variation → immune evasion or persistence; quorum sensing/regulators → virulence-gene expression → pathogenicity (lazar2023resistancetolerancevirulence pages 10-11, sangiorgio2024theimpactof pages 7-9, barber2024mechanismsofhost pages 1-2) | High for broad backbone; mixed for any single factor as universally necessary | Cross-taxon generalization across many bacterial pathogens, but not a universal required set | Curate as modular backbone with generic nodes and edges; avoid asserting necessity of every module for all taxa |
| *Pseudomonas aeruginosa* ExoU-SpcU branch | T3SS apparatus → ExoU secretion into host cells → cytotoxicity/virulence; functional SpcU chaperone → enables ExoU secretion/cytotoxicity; exoU deletion → attenuated cytotoxicity and in vivo virulence; complementation restores virulence (wu2024thetypeiii pages 1-2) | High | Taxon-specific; clinical isolate and murine bloodstream model | Curate as high-confidence taxon-specific branch, explicitly marked *P. aeruginosa*-specific and model-supported |
| *Proteus mirabilis* urea-UreR-Ynt-urease-ammonia/pH-stones branch | urinary tract urea → activates UreR → induces urease genes and Ynt nickel transporter → mature urease activity; urease hydrolyzes urea → ammonia production/local alkalinity → ion precipitation → struvite/apatite stones; urease-null mutants → cannot induce stones and show fitness defects/attenuation in murine UTI (fitzgerald2024proteusmirabilisurer pages 1-2, fitzgerald2024proteusmirabilisurer pages 2-5) | High | Taxon-specific; urinary tract/CAUTI niche, murine UTI support | Curate as high-priority specific branch linking environmental substrate, regulation, metal acquisition, enzyme maturation, and disease-promoting niche construction |
| Microbiota colonization resistance / environment branch | intact microbiota colonization resistance → limits pathogen establishment; inflammation- or microbiota-shaped metabolites/electron acceptors/nutrient depletion → alter virulence expression and pathogen expansion; host compromise, antibiotics, barrier disruption, and devices → increased opportunity for pathogenicity (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30, vonaesch2018pathogensmicrobiomeand pages 14-16, wang2024distributionpatternsand pages 1-2) | Moderate to high, but context-dependent | Host- and environment-dependent; strong for gut and device-associated settings, not a microbe-intrinsic determinant alone | Curate as environmental/external modulators of trait expression, not as intrinsic defining nodes of pathogenicity |
| HGT / pathogenicity island branch | mobile genetic elements/pathogenicity islands → acquisition of virulence determinants and secretion/toxin modules → emergence or enhancement of pathogenic capacity; small genetic changes or gene gain/loss can shift host adaptation/pathogenic behavior (lazar2023resistancetolerancevirulence pages 10-11, barber2024mechanismsofhost pages 1-2) | Moderate to high | Broad evolutionary mechanism; often lineage-specific and indirect relative to immediate phenotype | Curate as enabling/evolutionary edges (acquires virulence program), but avoid overclaiming that MGE presence alone proves pathogenic to host |


*Table: This table prioritizes the strongest curation branches for METPO:1004000 and distinguishes broadly reusable pathogenicity modules from taxon- and context-specific mechanisms. It is useful for deciding what to curate now versus what should remain qualified as environmental or evolutionary support.*

## 3. Candidate nodes grouped by type

Ontology assignments below are deliberately conservative. Label-only nodes are preferable to uncertain or invented CURIEs.

### A. Trait and organism-context nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| pathogenic to host | `METPO:1004000` | Terminal trait node. Preserve the identifier verbatim. |
| host organism | NCBITaxon identifier for the tested host | Host taxon should be recorded whenever evidence is species-specific. |
| microbial strain/lineage | NCBITaxon plus strain metadata | Pathogenicity often varies below species level. |
| host colonization | `GO:0044406` | Upstream enabling process; not equivalent to disease. |
| pathogenesis | `GO:0009405` | Broad process candidate connecting mechanisms to disease. |
| symbiont process | `GO:0044403` | Broad parent-level process; use only if compatible with schema conventions. |
| host-cell killing | `GO:0031640` | Appropriate for directly demonstrated microbial killing of host cells. |

### B. Adhesion, motility, and invasion

| Candidate node | Grounding | Role |
|---|---|---|
| adhesin activity | `GO:0044406` may capture colonization; specific adhesin nodes may remain label-only | Attachment to host receptors or extracellular matrix. |
| fimbriae/pili | Label-only unless a specific complex or protein is known | Promote attachment and tissue colonization. |
| FimH adhesin | UniProt accession should be strain-specific | Mannose-sensitive attachment; host-specific substitutions can alter tropism. |
| aggregation substance, Esp, epa polysaccharide | Label-only or strain-specific UniProt entries | Enterococcal adherence and epithelial translocation (sangiorgio2024theimpactof pages 7-9). |
| bacterial-type flagellum-dependent motility | `GO:0071973` | Enables access to host surfaces and, in some taxa, mucus traversal. |
| chemotaxis | `GO:0006935` | Environmental sensing and directed movement. |
| invasion of host cell | `GO:0044409` | Use only where internalization is experimentally shown. |

### C. Secretion machinery and effectors

| Candidate node | Suggested grounding | Role |
|---|---|---|
| type III protein secretion system | `GO:0030257` | Injects effectors into eukaryotic cells. |
| type IV secretion system | Label-only unless ontology mapping is verified | Transfers proteins and/or nucleic acids; some systems are virulence machines, others mediate conjugation. |
| type VI secretion system | Label-only unless mapping is verified | Can target host cells or microbial competitors. Its presence alone does not prove pathogenicity. |
| type V secretion proteins | Label-only/specific UniProt | Includes adhesins and other surface-exposed virulence proteins; some are licensed vaccine antigens. |
| bacterial effector delivery into host cell | `GO:0035635` | Useful mechanistic edge between secretion apparatus and intracellular manipulation. |
| ExoU | Strain-specific UniProt; label-only pending strain selection | Cytotoxic T3SS effector in *Pseudomonas aeruginosa*. |
| SpcU | Strain-specific UniProt; label-only pending strain selection | ExoU-specific chaperone required for secretion/cytotoxicity. |
| CagA | Strain-specific UniProt | *Helicobacter pylori* T4SS effector; retain as a taxon-specific branch. |

### D. Toxins, enzymes, and host-damage processes

| Candidate node | Suggested grounding | Role |
|---|---|---|
| cytolysin/pore-forming toxin | Label-only or specific protein identifier | Direct host-cell lysis; enterococcal cytolysin is one example (sangiorgio2024theimpactof pages 7-9). |
| extracellular protease | `GO:0008233` for peptidase activity, with specific protein identifier | Matrix degradation, barrier disruption, or immune-component cleavage. |
| urease | `EC:3.5.1.5`; `GO:0009039` | Urea hydrolysis; a demonstrated virulence mechanism in *P. mirabilis*. |
| UreR | Strain-specific UniProt or label-only | Urea-responsive transcriptional regulator. |
| Ynt nickel transporter | Strain-specific protein/complex identifiers or label-only | Supplies nickel required for mature urease. |
| urea | `CHEBI:16199` | Environmental substrate and UreR signal. |
| ammonia | `CHEBI:16134` | Urease product and weak base. |
| nickel(2+) | `CHEBI:28112` | Urease cofactor. |
| increased local pH/alkalinity | Label-only process/quality | Drives mineral precipitation in urine. |
| struvite | `CHEBI:63036` | Urinary-stone mineral; verify schema compatibility before use. |
| apatite urinary stone | Label-only pending exact mineral form | Disease-associated mineral outcome. |

### E. Nutrient acquisition and metabolism

| Candidate node | Suggested grounding | Role |
|---|---|---|
| siderophore-mediated iron uptake | `GO:0015891` | Counteracts host nutritional immunity and supports in-host growth. |
| iron ion | `CHEBI:24875` | Nutrient constrained by host sequestration. |
| salmochelin | `CHEBI:91398` if confirmed during implementation | Lipocalin-2-resistant siderophore used by *Salmonella*. |
| amino-acid biosynthesis | Appropriate pathway-specific GO/KEGG/MetaCyc term | Can overcome microbiota-mediated nutrient depletion. |
| nitrate respiration | Pathway-specific GO/KEGG/MetaCyc term | Inflammation-derived nitrate can support enteric pathogen expansion. |
| tetrathionate respiration | Pathway-specific GO/KEGG/MetaCyc term | Inflammation-associated respiratory advantage in *Salmonella*. |
| phosphotransferase system | KEGG module or component-specific identifiers | Supports nutrient acquisition and adaptation in enterococci (sangiorgio2024theimpactof pages 7-9). |

### F. Immune evasion and persistence

| Candidate node | Suggested grounding | Role |
|---|---|---|
| capsule/capsular polysaccharide | Specific biosynthetic locus or chemical entity | Can inhibit complement and phagocytosis. |
| lipopolysaccharide | `CHEBI:16412` | Context-dependent surface molecule; specific structures may alter innate recognition. |
| antigenic variation | `GO:0020033` | Reduces recognition by adaptive immunity. |
| biofilm formation | `GO:0042710` | Promotes persistence, device colonization, and protection from immune or antimicrobial clearance. |
| evasion of host immune response | `GO:0052170` | General process; use narrower descendants where mechanism is known. |
| intracellular persistence | Label-only or appropriate GO descendant | Survival in macrophages or other host cells. |
| inhibition of phagolysosomal fusion | Label-only pending verified GO mapping | Specific intracellular-survival mechanism. |

### G. Regulation, evolution, and external modifiers

| Candidate node | Suggested grounding | Role |
|---|---|---|
| quorum sensing | `GO:0009372` | Coordinates density-dependent virulence and biofilm programs. |
| two-component regulatory system | `GO:0000160` | Environmental sensing and virulence transcription. |
| pathogenicity island | SO term only after identifier verification | Mobile or chromosomal cluster encoding virulence functions. |
| plasmid | `GO:0005727` for plasmid cellular component, where appropriate | Can transfer virulence and resistance genes. |
| horizontal gene transfer | `GO:0044027` | Acquisition/spread of virulence modules. |
| host immune compromise | Label-only environmental/host-state node | Increases opportunity for conditional pathogens. |
| epithelial barrier disruption | Label-only or verified GO term | Permits translocation and ectopic colonization. |
| indwelling urinary catheter | `NCIT:C50444` may be considered after verification | Abiotic colonization surface and route bypassing micturition. |
| antibiotic exposure | Specific `CHEBI` drug identifier plus exposure relation | Can disrupt microbiota and select resistance; effect on virulence is drug-, dose-, and taxon-specific. |
| microbiota-mediated colonization resistance | Label-only process | Inhibits pathogen establishment through competition, metabolites, and host stimulation. |

## 4. Candidate evidence-backed causal edges

Predicates are phrased for later normalization to TraitMech’s relation vocabulary. “High” means supported by direct genetic or biochemical evidence; “moderate” generally denotes synthesis across taxa or context-dependent evidence.

| # | Subject–predicate–object triple | Reference | Supporting snippet | Strength, scope, and curation note |
|---:|---|---|---|---|
| 1 | adhesins/fimbriae — **promote** → host adherence and colonization | DOI [10.3390/pathogens12050746](https://doi.org/10.3390/pathogens12050746), 22 May 2023 | “Adhesins (pili, fimbriae, EPS) enable host adherence and colonization.” | **Moderate–high; cross-taxon.** Curate as a general enabling edge, not a sufficient cause of disease (lazar2023resistancetolerancevirulence pages 10-11). |
| 2 | bacterial flagellar/twitching motility — **promotes** → substrate colonization and movement across mucosal barriers | Same as above | “Flagellar and twitching motility facilitate substrate colonization and movement across mucosal barriers.” | **Moderate; cross-taxon but non-universal.** Flagella can also provoke immunity; do not encode a universally positive effect (lazar2023resistancetolerancevirulence pages 10-11). |
| 3 | T3SS/T6SS — **delivers** → effector proteins | Same as above | “Type III and Type VI secretion systems … deliver effectors for host manipulation.” | **High as machinery function; mixed endpoint.** For T6SS, distinguish host-directed effectors from interbacterial competition (lazar2023resistancetolerancevirulence pages 10-11). |
| 4 | T3SS-delivered effectors — **manipulate** → host-cell functions | DOI [10.1128/mmbr.00034-23](https://doi.org/10.1128/mmbr.00034-23), September 2023 | T3SS effectors “manipulate specific eukaryotic cell functions to benefit pathogen survival within the host.” | **High; Gram-negative/Chlamydia-centered.** Suitable general mechanism with taxonomic restrictions. |
| 5 | T6SS-mediated competitor elimination — **opens** → host ecological niche | DOI [10.1038/s41579-022-00833-7](https://doi.org/10.1038/s41579-022-00833-7), published online December 2022; journal issue 2023 | “T6SS systems enabling direct elimination of competitors to open ecological niches.” | **Moderate; indirect ecological path.** Curate as niche competition → colonization, not direct host damage (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30). |
| 6 | siderophore/high-affinity metal uptake — **overcomes** → host metal sequestration | Same as above | “Acquisition of iron through evolved siderophores and high-affinity transporters … to overcome host metal sequestration.” | **High for supported taxa.** Connect to in-host fitness before pathogenicity (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30). |
| 7 | de novo amino-acid synthesis — **overcomes** → microbiota-driven nutrient depletion | Same as above | “De novo amino acid synthesis by pathogens to overcome microbiota-driven nutrient depletion.” | **Moderate; enteric context.** Pathway- and taxon-specific evidence should accompany implementation (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30). |
| 8 | inflammation-derived tetrathionate/nitrate — **serves as** → respiratory electron acceptor for pathogen growth | Same as above | Pathogens use “inflammatory byproducts (tetrathionate, nitrate, ROS/RNS) as respiratory electron acceptors fueling pathogen growth.” | **Moderate–high; enteric taxa.** This is a host-response feedback edge, not universal microbial metabolism (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30). |
| 9 | microbiota-derived succinate — **activates via Cra** → EHEC T3SS | DOI [10.1093/femsre/fuy003](https://doi.org/10.1093/femsre/fuy003), 1 May 2018 | “Succinate produced by *B. thetaiotaomicron* activates EHEC T3SS via Cra transcription factor.” | **Moderate; highly taxon/context-specific.** Curate only in an EHEC intestinal branch (vonaesch2018pathogensmicrobiomeand pages 14-16). |
| 10 | propionate — **inhibits via HilD modification** → *Salmonella* SPI-1 | Same as above | “Propionate inhibits Salmonella pathogenicity island 1 through posttranslational modification of HilD.” | **Moderate; taxon-specific negative edge.** Useful evidence that metabolite effects can suppress, not only promote, virulence (vonaesch2018pathogensmicrobiomeand pages 14-16). |
| 11 | salmochelin — **resists** → lipocalin-2-mediated iron restriction | Same as above | “*Salmonella* Typhimurium uses Salmochelin resistant to Lipocalin2.” | **Moderate–high; *Salmonella*-specific.** Connect to iron acquisition and competitive fitness (vonaesch2018pathogensmicrobiomeand pages 14-16). |
| 12 | cytolysin/pore-forming toxin — **causes** → eukaryotic-cell lysis | DOI [10.3390/pathogens13050409](https://doi.org/10.3390/pathogens13050409), 16 May 2024 | “Cytolysin lysates eukaryotic cells.” | **High mechanism, Enterococcus example.** Prefer a specific toxin–host-cell edge rather than generic toxin presence (sangiorgio2024theimpactof pages 7-9). |
| 13 | aggregation substance — **promotes** → eukaryotic-cell adherence | Same as above | “Aggregation substance (Agg) promotes eukaryotic cell adherence.” | **Moderate–high; Enterococcus-specific.** Upstream colonization edge (sangiorgio2024theimpactof pages 7-9). |
| 14 | Esp/epa — **enable** → epithelial translocation | Same as above | “Esp and polysaccharide antigen (epa) enable epithelial translocation.” | **Moderate; Enterococcus-specific.** Validate protein/locus identifiers at strain level (sangiorgio2024theimpactof pages 7-9). |
| 15 | Gsr quorum-sensing system — **regulates** → gelatinase expression | Same as above | “Quorum sensing (Gsr system) regulates gelatinase expression.” | **Moderate–high; Enterococcus-specific.** Connect gelatinase separately to tissue effects where direct evidence is available (sangiorgio2024theimpactof pages 7-9). |
| 16 | biofilm formation — **promotes** → immune evasion and persistence | Same as above | Biofilm factors “enable immune evasion and persistence.” | **Moderate; context-dependent.** Biofilm should not directly imply disease without host/model evidence (sangiorgio2024theimpactof pages 7-9). |
| 17 | functional SpcU — **is required for** → ExoU secretion and cytotoxicity | DOI [10.1128/spectrum.02224-23](https://doi.org/10.1128/spectrum.02224-23), 9 January 2024 | “A functional downstream SpcU protein is required for both ExoU secretion and cytotoxicity.” | **High; *P. aeruginosa* clinical-isolate branch.** Direct functional evidence (wu2024thetypeiii pages 1-2). |
| 18 | ExoU — **promotes** → mammalian-cell cytotoxicity | Same as above | “Deletion of exoU resulted in significantly attenuated cytotoxicity.” | **High; strain/model-specific.** Complementation supports causality (wu2024thetypeiii pages 1-2). |
| 19 | ExoU — **promotes** → virulence in murine bloodstream infection | Same as above | ExoU deletion “reduced virulence in vivo,” and complementation “restored virulence.” | **High; murine bloodstream model.** One of the strongest edges for immediate curation (wu2024thetypeiii pages 1-2). |
| 20 | urea — **binds/activates** → UreR | DOI [10.1128/jb.00031-24](https://doi.org/10.1128/jb.00031-24), 27 March 2024 | “When urea is present, UreR directly binds this metabolite and forms a dimer.” | **High; *P. mirabilis*.** Environmental-sensing edge (fitzgerald2024proteusmirabilisurer pages 1-2). |
| 21 | activated UreR — **activates transcription of** → `ureDABCEFG` | Same as above | “Activated UreR dimers then bind two sites within the shared promoter, activating transcription.” | **High; direct regulatory mechanism** (fitzgerald2024proteusmirabilisurer pages 1-2). |
| 22 | UreR — **induces/directly regulates** → Ynt nickel transporter | Same as above | “UreR induces expression of both nickel transporters and directly regulates expression of nickel transporter Ynt.” | **High for regulation.** Keep Ynt strain-specific (fitzgerald2024proteusmirabilisurer pages 2-5). |
| 23 | Ynt-mediated nickel import — **enables maturation of** → active urease | Same as above | “Nickel must be transported into the cell before its delivery to the intracellular urease”; Ynt has higher nickel affinity and is used during experimental UTI. | **High biochemical chain; *P. mirabilis*.** Model as transport → cofactor incorporation → active enzyme (fitzgerald2024proteusmirabilisurer pages 1-2, fitzgerald2024proteusmirabilisurer pages 2-5). |
| 24 | urease — **hydrolyzes** → urea to ammonia and carbon dioxide | Same as above | “Urease … hydrolyzes urea to form ammonia and carbon dioxide.” | **High; biochemical reaction.** EC/Rhea grounding can be added after reaction verification (fitzgerald2024proteusmirabilisurer pages 2-5). |
| 25 | urease-derived ammonia — **raises** → local urinary pH | Same as above | Ammonia is a “weak base that raises the local pH.” | **High; biochemical/physiological** (fitzgerald2024proteusmirabilisurer pages 1-2). |
| 26 | urinary alkalinity — **induces** → polyvalent-ion precipitation and struvite/apatite stones | Same as above | “The resulting alkalinity induces the precipitation of polyvalent ions that crystalize into struvite and apatite urinary stones.” | **High; urinary-tract-specific** (fitzgerald2024proteusmirabilisurer pages 1-2). |
| 27 | urease activity — **promotes** → urinary-stone formation and *P. mirabilis* uropathogenesis | Same as above | “Urease-null *P. mirabilis* mutants cannot induce stones and exhibit significant fitness defects in a murine UTI model.” | **High; direct mutant evidence.** Strong curation endpoint branch (fitzgerald2024proteusmirabilisurer pages 1-2). |
| 28 | urinary stone/crystalline biofilm — **shelters** → *P. mirabilis* from immunity and antibiotics | Same as above | “Stones can complicate CAUTI treatment by sheltering *P. mirabilis* from the immune system and antibiotic treatment.” | **Moderate–high; device/urinary context** (fitzgerald2024proteusmirabilisurer pages 1-2). |
| 29 | catheter surface — **facilitates** → bladder access/colonization | Same as above | Microbes “access the bladder by traversing the abiotic catheter surface”; this route “evades natural host defenses such as micturition.” | **Moderate–high; device-associated context.** Model the catheter as an external enabling factor (fitzgerald2024proteusmirabilisurer pages 1-2). |
| 30 | mobile genetic elements/pathogenicity islands — **mediate acquisition of** → virulence programs | DOI [10.1093/femsre/fuae019](https://doi.org/10.1093/femsre/fuae019), July 2024; DOI [10.3390/pathogens12050746](https://doi.org/10.3390/pathogens12050746), May 2023 | Host adaptation includes “gene acquisitions/deletions … and horizontal gene transfer,” while virulence plasmids can transmit virulence genes. | **Moderate–high evolutionary edge.** MGE carriage predicts potential, not expressed pathogenicity (lazar2023resistancetolerancevirulence pages 10-11, barber2024mechanismsofhost pages 1-2). |

## 5. Recent developments and expert analysis

### Host adaptation is genetically fine-grained

A 2024 FEMS review emphasizes that host range can change through single-nucleotide substitutions, gene gain/loss, rearrangement, and horizontal transfer. Examples include host-associated `fimH` variation in *Salmonella* and substitutions in *Listeria monocytogenes* InlA that alter E-cadherin affinity. The curation implication is that pathogenicity should ordinarily be attached to a **strain–host pair**, not indiscriminately propagated to an entire species (barber2024mechanismsofhost pages 1-2).

### Ecological context is mechanistically active

Modern pathogenicity models incorporate the microbiota as a causal component. Colonization resistance can deny nutrients, stimulate host defenses, and directly inhibit competitors. Conversely, pathogens can deploy secretion systems, specialized siderophores, amino-acid biosynthesis, or inflammation-associated respiration to overcome that resistance. Microbiota metabolites can either induce or suppress virulence systems, demonstrating that “environmental factor → pathogenicity” is often signed and conditional rather than uniformly positive (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30, vonaesch2018pathogensmicrobiomeand pages 14-16).

### Direct genotype-to-phenotype validation remains decisive

The 2024 ExoU study provides a particularly curatable molecular-Koch-style chain: deleting `exoU` attenuated cytotoxicity and murine virulence; complementation restored virulence; and functional SpcU was necessary for ExoU secretion. This is stronger than gene-association evidence because perturbation, phenotype, and rescue are connected in one experimental system (wu2024thetypeiii pages 1-2).

The 2024 *P. mirabilis* work similarly links environmental sensing to pathology: urea activates UreR; UreR coordinates urease expression and nickel import; urease produces ammonia; ammonia raises pH; and alkalinity precipitates urinary-stone minerals. Urease-null mutants cannot form stones and are attenuated in murine UTI. This branch is an excellent model for the desired TraitMech granularity (fitzgerald2024proteusmirabilisurer pages 1-2, fitzgerald2024proteusmirabilisurer pages 2-5).

## 6. Current applications and real-world implementations

### Diagnostics and surveillance

Virulence loci are already used in molecular typing and risk assessment, but their interpretation must distinguish potential from demonstrated disease. Whole-genome surveillance can jointly profile virulence, resistance, mobile elements, and high-risk clones. In wound-infection surveillance from Jiaxing, 461 patients yielded 549 isolates; 58 were MDROs. A clinical MDRO prediction model incorporating host and care factors achieved sensitivity 0.627, specificity 0.933, and AUC 0.838, illustrating how microbial data and host context are combined operationally rather than treating pathogenicity as a genome-only property (wang2024distributionpatternsand pages 1-2).

### Vaccines targeting virulence machinery

Type V secretion system proteins are not merely experimental targets. Pertactin and filamentous haemagglutinin are components of licensed *Bordetella pertussis* vaccines, while NadA is included in a licensed meningococcal vaccine. These antigens can elicit antibodies that neutralize function, promote opsonophagocytosis, or activate complement. This is strong real-world evidence that surface-exposed virulence machinery can be translated into preventive interventions (costa2024type5secretion pages 1-2, costa2024type5secretion pages 2-4).

### Anti-virulence development

T3SSs, quorum sensing, adhesins, toxins, siderophore uptake, and biofilm formation are active anti-virulence targets. The therapeutic concept is to disarm host damage or colonization without necessarily killing the organism, potentially reducing conventional antibiotic selection pressure. However, most such approaches remain preclinical or pathogen-specific; their effectiveness depends on whether the targeted module is required in the relevant infection site and strain. The ExoU–SpcU dependency identifies a concrete *P. aeruginosa* target axis, whereas broad secretion-system inhibition requires careful selectivity because homologous systems also mediate commensal interactions or bacterial competition (lazar2023resistancetolerancevirulence pages 10-11, wu2024thetypeiii pages 1-2).

### Device-associated infection control

The *P. mirabilis* urease pathway is directly relevant to CAUTI management. Catheters provide a surface that bypasses urinary clearance; urease then drives crystalline biofilm, blockage, and stones that act as protected reservoirs. Interventions could target catheter colonization, UreR signaling, nickel import, urease activity, or mineral precipitation, but the graph should keep these as distinct intervention points (fitzgerald2024proteusmirabilisurer pages 1-2).

## 7. Recent statistics and burden data

- A 2024 systematic review included **322 studies and 90,672 patients** with antibiotic-resistant bloodstream infections. Overall 28/30-day mortality was **32.0%**; antibiotic-resistant *A. baumannii* had the highest species-level estimate at **54.2%**. The genomic analysis included **9,289 genomes** and identified **613 resistance-gene subtypes** across the six leading species (zhao2024mortalityandgenetic pages 1-2).
- In the 2024 Jiaxing wound cohort, **549 pathogens** were isolated from **461 patients**. *E. coli* amoxicillin resistance was **85.4%**, and *A. baumannii* resistance to advanced cephalosporins and carbapenems was **65.8–68.4%**. These figures quantify clinical severity and treatment complexity, but resistance must not be encoded as the molecular cause of pathogenicity itself (wang2024distributionpatternsand pages 1-2).
- The 2024 *P. mirabilis* study reports that CAUTIs account for **up to 40% of nosocomial infections globally**; more than **500,000 CAUTIs** occur annually in the United States, with estimated yearly costs up to **$1.7 billion**. It further notes that **15–25%** of hospital patients are catheterized during their stay (fitzgerald2024proteusmirabilisurer pages 1-2).
- A 2024 vaccine review reports **4.95 million deaths associated with AMR in 2019** and notes that Pertactin, FHA, and NadA are already used in licensed vaccines, supporting virulence-factor targeting as a practical public-health strategy (costa2024type5secretion pages 1-2).

These burden estimates concern infection and resistance, not a prevalence estimate for the ontology trait itself. They should therefore appear as application/context metadata rather than graph edges defining `METPO:1004000`.

## 8. Recommended YAML curation strategy

### High-priority additions

1. Retain the existing generic virulence-factor/secretion backbone.
2. Add explicit intermediate processes: adhesion, colonization, effector delivery, immune evasion, nutrient acquisition, persistence, and host damage.
3. Add the **ExoU–SpcU taxon-specific branch** with deletion and complementation evidence.
4. Add the **urea–UreR–Ynt–nickel–urease–ammonia–alkalinity–stone** branch for *P. mirabilis*.
5. Represent host state, microbiota, tissue chemistry, and devices as **context modifiers**, not intrinsic microbial traits.
6. Attach taxon, strain, host, tissue, and assay/model qualifiers to every specific edge where the schema permits.
7. Distinguish evidence levels such as `direct_mutant`, `complementation`, `biochemical`, `animal_model`, `clinical_association`, and `review_synthesis`.

### Predicate recommendations

Prefer mechanistically explicit predicates such as:

- `activates_expression_of`
- `requires_cofactor`
- `transports`
- `enables_maturation_of`
- `secretes`
- `delivers_into_host_cell`
- `promotes_colonization`
- `inhibits_host_process`
- `causes_host_cell_damage`
- `increases_in_host_fitness`
- `confers_resistance_to_host_defense`
- `enables_persistence`
- `contributes_to`

Reserve `causes` for direct biochemical or perturbational evidence. Use `contributes_to` for multifactorial virulence programs.

## 9. Warnings: claims not yet suitable for unconditional TraitMech curation

1. **Do not infer pathogenicity from a virulence gene alone.** Gene expression, functional integrity, secretion competence, and host context matter; intact `exoU`, for example, was insufficient when SpcU function was impaired (wu2024thetypeiii pages 1-2).
2. **Do not propagate strain-level findings to an entire species.** Host tropism and disease severity can change through small sequence differences (barber2024mechanismsofhost pages 1-2).
3. **Do not equate colonization with disease.** Adhesins, motility, and biofilm are enabling functions that also occur in commensals.
4. **Do not equate AMR with pathogenicity.** AMR modifies treatment outcome and persistence. The high mortality of resistant bloodstream infections does not demonstrate that resistance created the original host-damaging capacity (zhao2024mortalityandgenetic pages 1-2).
5. **Do not curate T6SS presence as direct host pathogenicity without substrate/target evidence.** Many T6SS effects are interbacterial and only indirectly facilitate host colonization (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30).
6. **Do not treat capsule, LPS, biofilm, or quorum sensing as universally virulence-enhancing.** Effects vary by structure, niche, expression level, and host response.
7. **Do not generalize metabolite effects across taxa.** Succinate, propionate, acetate, butyrate, and lactate can have different or opposing effects depending on the regulatory network (vonaesch2018pathogensmicrobiomeand pages 14-16).
8. **Keep animal-model outcomes qualified.** ExoU bloodstream virulence and urease-dependent UTI attenuation are strong evidence, but remain model- and route-specific (wu2024thetypeiii pages 1-2, fitzgerald2024proteusmirabilisurer pages 1-2).
9. **Community-driven/pathobiont disease needs contextual representation.** A taxon may be harmless in one community and damaging after dysbiosis, immune compromise, or ectopic translocation.
10. **Verify all ontology identifiers during implementation.** Where a stable, exact mapping has not been confirmed, retain a label-only node rather than assigning a broad or invented CURIE.

## 10. DOI-first bibliography

1. Barber MF, Fitzgerald JR. **Mechanisms of host adaptation by bacterial pathogens.** *FEMS Microbiology Reviews.* Published July 2024. DOI: [10.1093/femsre/fuae019](https://doi.org/10.1093/femsre/fuae019) (barber2024mechanismsofhost pages 1-2).
2. Wu T, et al. **The type III secretion system facilitates systemic infections of *Pseudomonas aeruginosa* in the clinic.** *Microbiology Spectrum.* Published 9 January 2024. DOI: [10.1128/spectrum.02224-23](https://doi.org/10.1128/spectrum.02224-23) (wu2024thetypeiii pages 1-2).
3. Fitzgerald MJ, Pearson MM, Mobley HLT. ***Proteus mirabilis* UreR coordinates cellular functions required for urease activity.** *Journal of Bacteriology.* Published 27 March 2024. DOI: [10.1128/jb.00031-24](https://doi.org/10.1128/jb.00031-24) (fitzgerald2024proteusmirabilisurer pages 1-2, fitzgerald2024proteusmirabilisurer pages 2-5).
4. Da Costa RM, et al. **Type 5 secretion system antigens as vaccines against Gram-negative bacterial infections.** *npj Vaccines.* Published September 2024. DOI: [10.1038/s41541-024-00953-6](https://doi.org/10.1038/s41541-024-00953-6) (costa2024type5secretion pages 1-2, costa2024type5secretion pages 2-4).
5. Sangiorgio G, et al. **The impact of *Enterococcus* spp. in the immunocompromised host: a comprehensive review.** *Pathogens.* Published 16 May 2024. DOI: [10.3390/pathogens13050409](https://doi.org/10.3390/pathogens13050409) (sangiorgio2024theimpactof pages 7-9).
6. Zhao H, et al. **Mortality and genetic diversity of antibiotic-resistant bacteria associated with bloodstream infections: a systematic review and genomic analysis.** *BMC Infectious Diseases.* Published December 2024. DOI: [10.1186/s12879-024-10274-7](https://doi.org/10.1186/s12879-024-10274-7) (zhao2024mortalityandgenetic pages 1-2).
7. Wang C, et al. **Distribution patterns and antibiotic resistance profiles of bacterial pathogens among patients with wound infections in the Jiaxing region from 2021 to 2023.** *Infection and Drug Resistance.* Published 9 July 2024. DOI: [10.2147/IDR.S470401](https://doi.org/10.2147/IDR.S470401) (wang2024distributionpatternsand pages 1-2).
8. Caballero-Flores G, Pickard JM, Núñez G. **Microbiota-mediated colonization resistance: mechanisms and regulation.** *Nature Reviews Microbiology.* Volume 21, 2023; published online December 2022. DOI: [10.1038/s41579-022-00833-7](https://doi.org/10.1038/s41579-022-00833-7) (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30).
9. Lazar V, Oprea E, Ditu L-M. **Resistance, tolerance, virulence and bacterial pathogen fitness—current state and envisioned solutions for the near future.** *Pathogens.* Published 22 May 2023. DOI: [10.3390/pathogens12050746](https://doi.org/10.3390/pathogens12050746) (lazar2023resistancetolerancevirulence pages 10-11).
10. Vonaesch P, Anderson M, Sansonetti PJ. **Pathogens, microbiome and the host: emergence of the ecological Koch’s postulates.** *FEMS Microbiology Reviews.* Published 1 May 2018. DOI: [10.1093/femsre/fuy003](https://doi.org/10.1093/femsre/fuy003) (vonaesch2018pathogensmicrobiomeand pages 14-16).

**Overall curation judgment:** the existing 14-node virulence-factor program is directionally sound but should be expanded into a modular, context-aware graph. The strongest immediate additions are the experimentally validated ExoU–SpcU and *P. mirabilis* urease branches. Broad modules such as adhesion, secretion, nutrient acquisition, immune evasion, and biofilm should be retained as contributory—not universally necessary or sufficient—causes of `METPO:1004000`.

References

1. (barber2024mechanismsofhost pages 1-2): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

2. (sangiorgio2024theimpactof pages 7-9): Giuseppe Sangiorgio, Maddalena Calvo, Giuseppe Migliorisi, Floriana Campanile, and Stefania Stefani. The impact of enterococcus spp. in the immunocompromised host: a comprehensive review. Pathogens, 13:409, May 2024. URL: https://doi.org/10.3390/pathogens13050409, doi:10.3390/pathogens13050409. This article has 65 citations.

3. (lazar2023resistancetolerancevirulence pages 10-11): Veronica Lazar, Eliza Oprea, and Lia-Mara Ditu. Resistance, tolerance, virulence and bacterial pathogen fitness—current state and envisioned solutions for the near future. Pathogens, 12:746, May 2023. URL: https://doi.org/10.3390/pathogens12050746, doi:10.3390/pathogens12050746. This article has 68 citations.

4. (wu2024thetypeiii pages 1-2): Tiantian Wu, Zhenchuan Zhang, Tong Li, Xu Dong, Dan Wu, Lixia Zhu, Kaijin Xu, and Ying Zhang. The type iii secretion system facilitates systemic infections of <i>pseudomonas aeruginosa</i> in the clinic. Jan 2024. URL: https://doi.org/10.1128/spectrum.02224-23, doi:10.1128/spectrum.02224-23. This article has 21 citations and is from a domain leading peer-reviewed journal.

5. (fitzgerald2024proteusmirabilisurer pages 1-2): Madison J. Fitzgerald, Melanie M. Pearson, and Harry L. T. Mobley. <i>proteus mirabilis</i> urer coordinates cellular functions required for urease activity. Journal of Bacteriology, Apr 2024. URL: https://doi.org/10.1128/jb.00031-24, doi:10.1128/jb.00031-24. This article has 24 citations and is from a peer-reviewed journal.

6. (fitzgerald2024proteusmirabilisurer pages 2-5): Madison J. Fitzgerald, Melanie M. Pearson, and Harry L. T. Mobley. <i>proteus mirabilis</i> urer coordinates cellular functions required for urease activity. Journal of Bacteriology, Apr 2024. URL: https://doi.org/10.1128/jb.00031-24, doi:10.1128/jb.00031-24. This article has 24 citations and is from a peer-reviewed journal.

7. (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30): Gustavo Caballero-Flores, Joseph M. Pickard, and Gabriel Núñez. Microbiota-mediated colonization resistance: mechanisms and regulation. Nature Reviews Microbiology, 21:347-360, Dec 2023. URL: https://doi.org/10.1038/s41579-022-00833-7, doi:10.1038/s41579-022-00833-7. This article has 532 citations and is from a highest quality peer-reviewed journal.

8. (vonaesch2018pathogensmicrobiomeand pages 14-16): Pascale Vonaesch, Mark Anderson, and Philippe J Sansonetti. Pathogens, microbiome and the host: emergence of the ecological koch's postulates. FEMS Microbiology Reviews, 42:273–292, May 2018. URL: https://doi.org/10.1093/femsre/fuy003, doi:10.1093/femsre/fuy003. This article has 182 citations and is from a domain leading peer-reviewed journal.

9. (wang2024distributionpatternsand pages 1-2): Chun Wang, Xiaoqin Niu, Siwen Bao, Weifeng Shen, and Chaoyue Jiang. Distribution patterns and antibiotic resistance profiles of bacterial pathogens among patients with wound infections in the jiaxing region from 2021 to 2023. Infection and Drug Resistance, 17:2883-2896, Jul 2024. URL: https://doi.org/10.2147/idr.s470401, doi:10.2147/idr.s470401. This article has 57 citations and is from a peer-reviewed journal.

10. (costa2024type5secretion pages 1-2): Rochelle M. Da Costa, Jessica L. Rooke, Timothy J. Wells, Adam F. Cunningham, and Ian R. Henderson. Type 5 secretion system antigens as vaccines against gram-negative bacterial infections. NPJ Vaccines, Sep 2024. URL: https://doi.org/10.1038/s41541-024-00953-6, doi:10.1038/s41541-024-00953-6. This article has 22 citations and is from a peer-reviewed journal.

11. (costa2024type5secretion pages 2-4): Rochelle M. Da Costa, Jessica L. Rooke, Timothy J. Wells, Adam F. Cunningham, and Ian R. Henderson. Type 5 secretion system antigens as vaccines against gram-negative bacterial infections. NPJ Vaccines, Sep 2024. URL: https://doi.org/10.1038/s41541-024-00953-6, doi:10.1038/s41541-024-00953-6. This article has 22 citations and is from a peer-reviewed journal.

12. (zhao2024mortalityandgenetic pages 1-2): Haitao Zhao, Mengyue Liu, Jie Wu, Shuaiyin Chen, Haiyan Yang, Jinzhao Long, and Guangcai Duan. Mortality and genetic diversity of antibiotic-resistant bacteria associated with bloodstream infections: a systemic review and genomic analysis. BMC Infectious Diseases, Dec 2024. URL: https://doi.org/10.1186/s12879-024-10274-7, doi:10.1186/s12879-024-10274-7. This article has 12 citations and is from a peer-reviewed journal.