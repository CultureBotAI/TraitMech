---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:13:26.741115'
end_time: '2026-08-03T23:21:03.238860'
duration_seconds: 456.5
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: endosymbiosis
  trait_identifier: traitmech:000045
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: endosymbiosis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A symbiosis in which the microorganism lives inside the cells or tissues
    of its host. Obligate intracellular endosymbionts (e.g. of insects) frequently
    undergo extreme genome reduction.
  parent_traits: traitmech:000040
  synonyms: endosymbiont
  evidence_summary: 'DOI:10.1038/nrmicro2670:  (McCutcheon & Moran, "Extreme genome
    reduction in symbiotic bacteria", characterize intracellular endosymbionts and
    their diminished genomes.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe
    rhizobia as plant-cell endosymbionts within root nodules, an example of the endosymbiotic
    lifestyle.)'
  causal_graph_summary: 'endosymbiosis_intracellular_genome_reduction: 10 nodes, 7
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** endosymbiosis
- **METPO identifier:** traitmech:000045
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism lives inside the cells or tissues of its host. Obligate intracellular endosymbionts (e.g. of insects) frequently undergo extreme genome reduction.
- **Parent traits:** traitmech:000040
- **Synonyms:** endosymbiont
- **Existing evidence:** DOI:10.1038/nrmicro2670:  (McCutcheon & Moran, "Extreme genome reduction in symbiotic bacteria", characterize intracellular endosymbionts and their diminished genomes.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia as plant-cell endosymbionts within root nodules, an example of the endosymbiotic lifestyle.)
- **Existing causal graph summary:** endosymbiosis_intracellular_genome_reduction: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **endosymbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/endosymbiosis.yaml`.

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
- **Trait label:** endosymbiosis
- **METPO identifier:** traitmech:000045
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism lives inside the cells or tissues of its host. Obligate intracellular endosymbionts (e.g. of insects) frequently undergo extreme genome reduction.
- **Parent traits:** traitmech:000040
- **Synonyms:** endosymbiont
- **Existing evidence:** DOI:10.1038/nrmicro2670:  (McCutcheon & Moran, "Extreme genome reduction in symbiotic bacteria", characterize intracellular endosymbionts and their diminished genomes.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia as plant-cell endosymbionts within root nodules, an example of the endosymbiotic lifestyle.)
- **Existing causal graph summary:** endosymbiosis_intracellular_genome_reduction: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **endosymbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/endosymbiosis.yaml`.

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


# Curation report: microbial endosymbiosis

## 1. Scope and current understanding

**Target:** `traitmech:000045` — endosymbiosis; ecology class; reviewed mapping.

For TraitMech, the defensible core phenotype is **persistent residence of a microorganism inside host cells or tissues**. The trait describes spatial and ecological integration, not the sign of the fitness interaction. Endosymbionts range from parasitic through commensal to mutualistic; therefore, host benefit, obligacy, vertical transmission, bacteriocyte residence, and genome reduction are common associated properties but are **not individually necessary defining criteria**. Recent expert analysis specifically recommends measuring fitness effects rather than assigning organisms to simplistic “manipulator” or mutualist categories. Newly acquired associations may initially be costly, while vertical transmission can favor—but does not guarantee—evolution toward mutualism or host dependence (hoffmann2024describingendosymbiont–hostinteractions pages 1-2).

### Boundary cases

- **Include:** bacteria or fungi maintained inside host cells; rhizobia enclosed as bacteroids within plant-derived symbiosomes; microbes intracellular in specialized bacteriocytes; and intracellular associates transmitted through ovaries or eggs.
- **Do not equate with obligate intracellular lifestyle:** facultative endosymbionts qualify when intracellular, whereas obligacy is a separate dependence phenotype.
- **Do not require mutualism:** reproductive parasites and mildly pathogenic intracellular symbionts remain endosymbionts.
- **Exclude extracellular symbioses:** gut-lumen, cuticle, rhizosphere, and extracellular tissue associations are not sufficient unless intracellular localization is demonstrated.
- **Distinguish transient intracellular infection:** invasion alone is insufficient; evidence should indicate persistence, replication, developmental continuity, or transmission.
- **Treat organelles separately:** mitochondria and plastids arose through endosymbiosis but are normally curated as organelles rather than extant microbial endosymbionts.
- **Genome reduction is a consequence, not a diagnostic requirement.** The newly described *Symbiodolus* has eroding, transposon-rich genomes but retains substantial functional capacity, illustrating an intermediate-stage association (wierz2024intracellularsymbiontsymbiodolus pages 1-2, wierz2024intracellularsymbiontsymbiodolus pages 9-10).

## 2. Recommended graph architecture

A single universal molecular pathway does not cause all endosymbioses. The YAML should therefore use a modular graph:

1. **Host-cell entry and intracellular persistence**
2. **Host-derived compartmentalization**
3. **Immune accommodation and density control**
4. **Vertical or mixed transmission**
5. **Bidirectional nutrient and metabolite exchange**
6. **Host developmental and reproductive effects**
7. **Population bottlenecks, gene loss, and dependence**

Taxon-specific branches should be retained rather than collapsing insect bacteriocytes, legume symbiosomes, and intracellular fungi into one supposedly universal mechanism.

## 3. Candidate nodes grouped by type

### Trait and processes

- Endosymbiosis — `METPO:traitmech:000045`
- Intracellular localization — candidate `GO:0043656` (“intracellular region of host”); verify ontology version before committing
- Symbiont transmission / transovarial transmission — label-first
- Host-cell entry; intracellular persistence; immune accommodation; symbiont-density control — label-first
- Nutrient exchange and metabolic complementarity — label-first
- Genome reduction; gene loss; pseudogenization; genetic drift; transmission bottleneck — label-first
- Symbiotic nitrogen fixation — `GO:0009399`
- DNA mismatch repair — `GO:0006298`
- TOR signaling — `GO:0031929`

### Host structures and localizations

- Bacteriocyte — specialized insect cell containing endosymbionts; label-first
- Bacteriome — organ composed of bacteriocytes; label-first
- Female ovary, germ line, egg cytoplasm — use GO/Uberon terms only after host-specific review
- Symbiosome and symbiosome membrane — plant-derived compartment containing rhizobial bacteroids; label-first because ontology coverage varies
- Bacteroid — differentiated intracellular rhizobium; label-first
- Insect fat body — host tissue occupied by the fungal *Ophiocordyceps* endosymbiont

### Microbial taxa

- *“Candidatus Tremblaya phenacola”* PSOL
- *Phenacoccus solenopsis* host
- *Symbiodolus clandestinus* and genus *Symbiodolus*
- *Buchnera*, *Serratia*, *Hamiltonella*, and *Arsenophonus*
- *Sodalis pierantonius*
- Rhizobia associated with *Medicago truncatula* and *Lotus japonicus*
- *Ophiocordyceps* endosymbiont of *Parthenolecanium corni*

NCBITaxon identifiers should be resolved directly against the current taxonomy database during YAML curation; provisional or recently named taxa should not be assigned guessed CURIEs.

### Genes, proteins, and complexes

- Host miR-3024
- Host MRP4/ABCC-family membrane transporter
- Host mTOR complex/pathway
- Bacterial MutH, MutL, and MutS mismatch-repair proteins
- Host MtVTL8 vacuolar-iron-transporter-like protein
- Host LjFtsH4 mitochondrial metalloprotease
- Bacterial type III and type VI secretion systems, intimin–Tir-associated machinery, phospholipase effectors, and toxin–antitoxin systems
- Nodule-specific cysteine-rich peptides, including NCR247
- Nitrogenase — `EC:1.18.6.1`; corresponding nif genes should be represented only in the rhizobial branch

### Chemicals and metabolites

- Pyridoxine/vitamin B6 — `CHEBI:16709` for pyridoxine; distinguish the measured B6 vitamer before curation
- L-amino acids and essential amino acids — ground individual compounds rather than using one ambiguous aggregate node
- Ferrous iron — `CHEBI:29033`
- Heme — `CHEBI:30413`
- Dinitrogen — `CHEBI:17997`
- Ammonia/ammonium — `CHEBI:16134` / `CHEBI:28938`; distinguish chemical species
- 2-oxoglutarate and C4-dicarboxylates — ground the exact transported metabolite if experimentally identified
- Acetoacetate — `CHEBI:13705`
- Acetyl-CoA — `CHEBI:15351`

## 4. Candidate causal edges

The following table is a compact candidate set. “Strong” denotes intervention, localization plus transmission evidence, or direct functional genetics; “moderate” denotes convergent functional evidence with some mechanistic steps unresolved; “uncertain” denotes genomic prediction or evolutionary interpretation.

| subject | predicate | object | system/taxon | evidence strength | DOI/year |
|---|---|---|---|---|---|
| intracellular localization across host life stages | supports | persistent vertical transmission | *Symbiodolus clandestinus* in insects | moderate | 10.1093/ismejo/wrae099 (2024) (wierz2024intracellularsymbiontsymbiodolus pages 1-2, wierz2024intracellularsymbiontsymbiodolus pages 10-11) |
| ovarian tropism / high abundance in female ovaries | enables | transovarial vertical transmission | *Symbiodolus clandestinus* in multiple insect hosts | strong | 10.1093/ismejo/wrae099 (2024) (wierz2024intracellularsymbiontsymbiodolus pages 1-2, wierz2024intracellularsymbiontsymbiodolus pages 9-10) |
| secretion systems, effectors, toxin-antitoxin modules | facilitates | host-cell entry and host interaction | *Symbiodolus clandestinus* | uncertain | 10.1093/ismejo/wrae099 (2024) (wierz2024intracellularsymbiontsymbiodolus pages 1-2, wierz2024intracellularsymbiontsymbiodolus pages 9-10) |
| T3SS/T6SS-associated factors | promotes | host-cell invasion | *Symbiodolus clandestinus* | uncertain | 10.1093/ismejo/wrae099 (2024) (wierz2024intracellularsymbiontsymbiodolus pages 9-10) |
| bacteriocyte compartmentalization | houses | intracellular endosymbionts for nutrient exchange | aphid / mealybug endosymbioses | moderate | 10.1073/pnas.2406925121 (2024); 10.1093/ismejo/wrae052 (2024) (bai2024endosymbionttremblayaphenacola pages 1-2, shang2024micrornamaintainsnutrient pages 8-9) |
| symbiosome formation (plant-derived membrane compartment) | compartmentalizes | rhizobial bacteroids | legume-rhizobium symbiosis | moderate | 10.3389/fpls.2023.1306491 (2024) (cai2024expressionandmutagenesis pages 15-16) |
| endosymbiont essential-amino-acid synthesis | activates | host mTOR signaling | *Tremblaya phenacola*–*Phenacoccus solenopsis* | strong | 10.1093/ismejo/wrae052 (2024) (bai2024endosymbionttremblayaphenacola pages 1-2) |
| host mTOR signaling | increases | host fecundity / reproduction | *Tremblaya phenacola*–*Phenacoccus solenopsis* | strong | 10.1093/ismejo/wrae052 (2024) (bai2024endosymbionttremblayaphenacola pages 1-2) |
| miR-3024 | inhibits | MRP4 transporter expression | aphid-endosymbiont system | strong | 10.1073/pnas.2406925121 (2024) (shang2024micrornamaintainsnutrient pages 8-9) |
| MRP4 transporter | mediates transport of | endosymbiont-derived vitamin B6 to host | aphid-endosymbiont system | strong | 10.1073/pnas.2406925121 (2024) (shang2024micrornamaintainsnutrient pages 8-9) |
| MutH (facultative symbiont) + MutL/MutS (obligate symbiont) complementation | restores | complete DNA repair capacity | aphid endosymbionts (*Serratia* + *Buchnera*) | moderate | 10.1073/pnas.2415651121 (2024) (ling2024acompletedna pages 10-11) |
| restored cross-symbiont DNA repair | enhances | host bacteriocyte heat tolerance / thermostability | aphid endosymbiosis | moderate | 10.1073/pnas.2415651121 (2024) (ling2024acompletedna pages 10-11) |
| MtVTL8-mediated Fe2+ transport across symbiosome membrane | supports | bacteroid survival and symbiotic nitrogen fixation | *Medicago truncatula*–rhizobium | moderate | 10.3389/fpls.2023.1306491 (2024) (cai2024expressionandmutagenesis pages 15-16) |
| symbiosome membrane integrity | required for | effective symbiotic nitrogen fixation | *Lotus japonicus* nodules | moderate | 10.1038/s41598-024-78295-5 (2024) (cai2024expressionandmutagenesis pages 15-16) |
| long-term intracellular persistence with transmission bottlenecks / genetic drift | drives | genome erosion and gene loss | endosymbiotic bacteria broadly; louse *Sodalis* model | moderate | 10.1038/s41467-024-48784-2 (2024); 10.1016/S0168-9525(01)02447-7 (2001) (cai2024expressionandmutagenesis pages 15-16) |
| shift from entomopathogen to endosymbiont | accompanied by | 524 gene loss events | *Ophiocordyceps* endosymbiont of *Parthenolecanium corni* | strong | 10.1093/gbe/evae251 (2024) (ward2024adaptationduringthe pages 1-2) |
| vertical transmission | favors coevolution toward | mutualism / host dependence | arthropod endosymbionts broadly | uncertain | 10.1002/ece3.11705 (2024) (hoffmann2024describingendosymbiont–hostinteractions pages 1-2) |


*Table: This table summarizes curation-ready candidate causal edges for the microbial trait endosymbiosis, emphasizing experimentally supported mechanisms and explicitly marking uncertain, taxon-specific, or hypothesis-level links.*

### Supporting snippets and curation notes

1. **Ovarian tropism → transovarial transmission.** Wierz et al. report intracellular presence “in all host life stages and across tissues,” with “high abundance in female ovaries, indicating transovarial vertical transmission.” FISH supplies direct spatial evidence. This is strong for *Symbiodolus*, not a universal requirement of endosymbiosis (wierz2024intracellularsymbiontsymbiodolus pages 1-2).

2. **Secretion systems/effectors → host-cell entry.** *Symbiodolus* genomes encode “multiple secretion systems, alongside effectors and toxin-antitoxin systems, which likely facilitate host-cell entry.” Because “likely” reflects inference from gene content rather than direct knockout evidence, curate this edge as `uncertain: true`. More specific T3SS/T6SS links should remain taxon-specific (wierz2024intracellularsymbiontsymbiodolus pages 1-2, wierz2024intracellularsymbiontsymbiodolus pages 9-10).

3. **Metabolic complementarity → host reproduction.** The *Tremblaya phenacola* genome is only **221.1 kb**, and pathway reconstruction showed host–symbiont complementarity for amino-acid metabolism. Antibiotic elimination significantly decreased mealybug fecundity, while changing symbiont abundance activated host mTOR signaling. These results support a causal nutritional-symbiont → amino-acid status → mTOR → reproduction branch, although antibiotic off-target effects mean the pathway should retain system-specific qualification (bai2024endosymbionttremblayaphenacola pages 1-2).

4. **miR-3024 ⊣ MRP4 → vitamin-B6 transfer.** In aphids, low miR-3024 permits MRP4-mediated movement of endosymbiont-derived vitamin B6 from bacteriocytes to host tissues. Increased miR-3024 suppresses MRP4, reduces transfer, and lowers host fitness or causes mortality; stress-associated miR-3024 downregulation restores transport capacity. This is among the strongest molecularly resolved nutrient-transfer edges currently available (shang2024micrornamaintainsnutrient pages 8-9).

5. **Complementary DNA-repair genes → heat tolerance.** In aphids, MutH retained by *Serratia* complements MutL/MutS components in *Buchnera*, assembling repair capacity across two endosymbionts. Protein-localization and imaging evidence support trafficking between bacteriocyte compartments, and the reconstructed system improves *Buchnera* genome integrity and bacteriocyte thermostability. This is compelling but applies to a dual-symbiont aphid system, not endosymbiosis generally (ling2024acompletedna pages 10-11).

6. **MtVTL8 Fe²⁺ transport → bacteroid survival and nitrogen fixation.** MtVTL8 operates at the *Medicago truncatula* symbiosome membrane and is required for bacterial survival and effective symbiotic nitrogen fixation. The proposed Fe²⁺-driving mechanism involving NCR247, heme sequestration, and the symbiosome electrochemical environment remains partly hypothetical and should not be curated as a settled mechanistic chain (cai2024expressionandmutagenesis pages 15-16).

7. **Pathogen-to-endosymbiont transition → gene loss.** The intracellular *Ophiocordyceps* lineage residing transgenerationally in scale-insect fat tissue showed **524 inferred gene-loss events** relative to free-living pathogenic relatives. Lost functions included hyphal growth, cell-wall integrity, metabolism, regulation, and toxin production. Positive/intensified selection in three adjacent enzymes converting acetoacetate to acetyl-CoA suggests adaptation to the lipid-rich host environment, but the transition itself is comparative-historical rather than experimentally induced (ward2024adaptationduringthe pages 1-2).

8. **Intracellular persistence and transmission bottlenecks → genome erosion.** Recent *Symbiodolus* genomes are eroding and transposon-rich, while ancient obligate systems commonly lose redundant or host-supplied functions. This should be represented as a probabilistic evolutionary branch—not a deterministic direct edge—because losses differ among lineages and intermediate symbionts may retain large functional repertoires (wierz2024intracellularsymbiontsymbiodolus pages 1-2, wierz2024intracellularsymbiontsymbiodolus pages 9-10).

9. **Vertical transmission → mutualism/dependence.** Evolutionary theory predicts that aligning symbiont transmission with host reproduction can favor reduced harm and host benefit, but interactions remain environmentally contingent and “host addiction” can evolve without net fitness improvement. Curate only as an uncertain, higher-level evolutionary relationship (hoffmann2024describingendosymbiont–hostinteractions pages 1-2).

## 5. Recent developments and quantitative findings

- **Widespread intracellular lineage:** *Symbiodolus* occurs across at least **six insect orders**. FISH detected it intracellularly through host development, particularly in ovaries. Genomes from **16 host taxa** retained secretion systems and candidate amino-acid and B-vitamin biosynthetic pathways. Lack of strict host–symbiont cospeciation supports occasional horizontal transmission alongside vertical transmission (wierz2024intracellularsymbiontsymbiodolus pages 1-2, wierz2024intracellularsymbiontsymbiodolus pages 9-10).
- **Minimal nutritional symbiont genome:** *T. phenacola* PSOL has a **221.1-kb**, seven-contig genome. Antibiotic elimination reduced *P. solenopsis* fecundity, and symbiont abundance was linked experimentally to amino-acid-sensitive mTOR signaling (bai2024endosymbionttremblayaphenacola pages 1-2).
- **Genome remodeling during lifestyle transition:** the scale-insect fungal endosymbiont experienced **524 gene-loss events**, with lineage-specific selection concentrated partly in fatty-acid metabolism (ward2024adaptationduringthe pages 1-2).
- **Transport-level nutrient control:** the 2024 aphid study resolved an miRNA–transporter circuit regulating vitamin-B6 export from endosymbiont-containing bacteriocytes. The same pathway was tested as a pest-control target using miR-3024-expressing transgenic tobacco (shang2024micrornamaintainsnutrient pages 8-9).
- **Distributed functions across co-symbionts:** complementation of mismatch-repair components between *Buchnera* and *Serratia* restored a complete repair system and improved heat tolerance, showing that the relevant functional unit may be the multi-partner symbiotic consortium rather than one genome (ling2024acompletedna pages 10-11).

## 6. Applications and real-world relevance

1. **Crop-pest control:** disrupting endosymbiont nutrient transfer is a plausible control strategy. miR-3024 suppression of MRP4 reduced vitamin-B6 delivery and host survival, and transgenic tobacco expressing the miRNA produced sustained aphid resistance in the reported experiments. Deployment would nevertheless require ecological, resistance, and non-target assessment (shang2024micrornamaintainsnutrient pages 8-9).
2. **Improved biological nitrogen fixation:** symbiosome iron delivery, membrane maintenance, and host control of bacteroid differentiation are actionable targets for legume breeding or inoculant optimization. MtVTL8 is functionally required for bacteroid survival and nitrogen fixation in *M. truncatula*, but extrapolation to other legumes requires validation (cai2024expressionandmutagenesis pages 15-16).
3. **Thermal resilience of crop pests and beneficial insects:** cross-symbiont DNA repair can stabilize obligate symbioses under heat stress. This mechanism may inform predictions of insect responses to warming, although it is presently demonstrated in a specific aphid consortium (ling2024acompletedna pages 10-11).
4. **Discovery of controllable symbiont chassis:** *Symbiodolus* combines broad host range, mixed transmission, intracellular persistence, and a genome less reduced than those of ancient obligates. The authors view this as useful for studying establishment mechanisms, but culturability, genetic tractability, and host benefit remain unproven (wierz2024intracellularsymbiontsymbiodolus pages 10-11).

## 7. Expert interpretation

The strongest cross-system conclusion is that endosymbiosis is an **ecological state assembled from multiple mechanisms**, not a single conserved pathway. Entry and transmission machinery dominate early associations; host-derived compartments and regulated exchange stabilize mature associations; repeated bottlenecks, relaxed selection on dispensable functions, and metabolic complementation can then produce genome reduction and dependence. However, recent comparative work cautions that deterministic retention of host-beneficial functions coexists with stochastic gene loss, so genome content alone cannot establish the interaction’s fitness sign.

For TraitMech, the safest backbone is therefore:

`host-cell entry → intracellular localization → persistent host compartment residence → transmission and/or within-host maintenance`

with separate, optional branches for:

- `metabolite provisioning → host signaling/fitness`,
- `host transport/control → symbiont persistence or nitrogen fixation`, and
- `long-term intracellular transmission → bottlenecks/drift + relaxed selection → gene loss → metabolic dependence`.

## 8. Claims that should not yet be curated as firm edges

- **T3SS/T6SS causes *Symbiodolus* entry:** presently inferred principally from genome content; require mutational or infection assays.
- **All endosymbionts benefit hosts:** false; the interaction spans parasitism to mutualism (hoffmann2024describingendosymbiont–hostinteractions pages 1-2).
- **Vertical transmission necessarily produces mutualism:** theoretical tendency, not a rule.
- **Genome reduction defines endosymbiosis:** false; it is lineage- and age-dependent.
- **Presence of amino-acid or vitamin pathways proves metabolite transfer:** genomic potential alone is insufficient. For *Symbiodolus*, actual transfer and fitness benefit remain unresolved (wierz2024intracellularsymbiontsymbiodolus pages 10-11).
- **Antibiotic curing alone proves a specific nutrient mechanism:** microbiome disturbance and direct host toxicity must be excluded.
- **NCR247-driven Fe²⁺ energetics are established:** parts of the proposed transport mechanism await direct structural and transport validation (cai2024expressionandmutagenesis pages 15-16).
- **The 524 fungal gene losses are universally required for endosymbiosis:** they document one independent pathogen-to-endosymbiont transition (ward2024adaptationduringthe pages 1-2).
- **Symbiosome and bacteriocyte mechanisms are interchangeable:** these are analogous host compartments but are developmentally and evolutionarily distinct.

## 9. DOI-first bibliography

1. Wierz JC et al. “Intracellular symbiont *Symbiodolus* is vertically transmitted and widespread across insect orders.” *The ISME Journal*. Published January 2024. https://doi.org/10.1093/ismejo/wrae099 (wierz2024intracellularsymbiontsymbiodolus pages 1-2, wierz2024intracellularsymbiontsymbiodolus pages 9-10)
2. Bai J et al. “Endosymbiont *Tremblaya phenacola* influences the reproduction of cotton mealybugs by regulating the mechanistic target of rapamycin pathway.” *The ISME Journal*. Published January 2024. https://doi.org/10.1093/ismejo/wrae052 (bai2024endosymbionttremblayaphenacola pages 1-2)
3. Shang F et al. “microRNA maintains nutrient homeostasis in the symbiont–host interaction.” *Proceedings of the National Academy of Sciences*. Published August 2024. https://doi.org/10.1073/pnas.2406925121 (shang2024micrornamaintainsnutrient pages 8-9)
4. Ling X et al. “A complete DNA repair system assembled by two endosymbionts restores heat tolerance of the insect host.” *Proceedings of the National Academy of Sciences*. Published December 2024. https://doi.org/10.1073/pnas.2415651121 (ling2024acompletedna pages 10-11)
5. Ward CM, Onetto CA, Borneman AR. “Adaptation During the Shift from Entomopathogen to Endosymbiont Is Accompanied by Gene Loss and Intensified Selection.” *Genome Biology and Evolution*. Published November 2024. https://doi.org/10.1093/gbe/evae251 (ward2024adaptationduringthe pages 1-2)
6. Hoffmann AA, Cooper BS. “Describing endosymbiont–host interactions within the parasitism–mutualism continuum.” *Ecology and Evolution*. Published July 2024. https://doi.org/10.1002/ece3.11705 (hoffmann2024describingendosymbiont–hostinteractions pages 1-2)
7. Cai J, Longo A, Dickstein R. “Expression and mutagenesis studies in the *Medicago truncatula* iron transporter MtVTL8 confirm its role in symbiotic nitrogen fixation and reveal amino acids essential for transport.” *Frontiers in Plant Science*. Published January 2024. https://doi.org/10.3389/fpls.2023.1306491 (cai2024expressionandmutagenesis pages 15-16)
8. McCutcheon JP, Moran NA. “Extreme genome reduction in symbiotic bacteria.” *Nature Reviews Microbiology*. Published November 2011 online; 2012 volume. https://doi.org/10.1038/nrmicro2670. Foundational source supplied in the trait record; use for background rather than as the sole support for particular taxon-specific edges.

References

1. (hoffmann2024describingendosymbiont–hostinteractions pages 1-2): Ary A. Hoffmann and Brandon S. Cooper. Describing endosymbiont–host interactions within the parasitism–mutualism continuum. Ecology and Evolution, Jul 2024. URL: https://doi.org/10.1002/ece3.11705, doi:10.1002/ece3.11705. This article has 29 citations and is from a peer-reviewed journal.

2. (wierz2024intracellularsymbiontsymbiodolus pages 1-2): Jürgen C Wierz, Philipp Dirksen, Roy Kirsch, Ronja Krüsemer, Benjamin Weiss, Yannick Pauchet, Tobias Engl, and Martin Kaltenpoth. Intracellular symbiont symbiodolus is vertically transmitted and widespread across insect orders. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae099, doi:10.1093/ismejo/wrae099. This article has 20 citations.

3. (wierz2024intracellularsymbiontsymbiodolus pages 9-10): Jürgen C Wierz, Philipp Dirksen, Roy Kirsch, Ronja Krüsemer, Benjamin Weiss, Yannick Pauchet, Tobias Engl, and Martin Kaltenpoth. Intracellular symbiont symbiodolus is vertically transmitted and widespread across insect orders. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae099, doi:10.1093/ismejo/wrae099. This article has 20 citations.

4. (wierz2024intracellularsymbiontsymbiodolus pages 10-11): Jürgen C Wierz, Philipp Dirksen, Roy Kirsch, Ronja Krüsemer, Benjamin Weiss, Yannick Pauchet, Tobias Engl, and Martin Kaltenpoth. Intracellular symbiont symbiodolus is vertically transmitted and widespread across insect orders. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae099, doi:10.1093/ismejo/wrae099. This article has 20 citations.

5. (bai2024endosymbionttremblayaphenacola pages 1-2): Jianyang Bai, Zhangqi Zuo, Haonan DuanMu, Meizhen Li, Haojie Tong, Yang Mei, Yiqi Xiao, Kang He, Mingxing Jiang, Shuping Wang, and Fei Li. Endosymbiont tremblaya phenacola influences the reproduction of cotton mealybugs by regulating the mechanistic target of rapamycin pathway. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae052, doi:10.1093/ismejo/wrae052. This article has 10 citations.

6. (shang2024micrornamaintainsnutrient pages 8-9): Feng Shang, Bi-Yue Ding, Jinzhi Niu, Jin-Ming Lu, Xiu-Cheng Xie, Chuan-Zhen Li, Wei Zhang, Deng Pan, Rui-Xu Jiang, and Jin-Jun Wang. Microrna maintains nutrient homeostasis in the symbiont–host interaction. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2406925121, doi:10.1073/pnas.2406925121. This article has 12 citations and is from a highest quality peer-reviewed journal.

7. (cai2024expressionandmutagenesis pages 15-16): Jingya Cai, Antonella Longo, and Rebecca Dickstein. Expression and mutagenesis studies in the medicago truncatula iron transporter mtvtl8 confirm its role in symbiotic nitrogen fixation and reveal amino acids essential for transport. Frontiers in Plant Science, Jan 2024. URL: https://doi.org/10.3389/fpls.2023.1306491, doi:10.3389/fpls.2023.1306491. This article has 5 citations.

8. (ling2024acompletedna pages 10-11): Xiaoyu Ling, Huijuan Guo, Jian Di, Liqiang Xie, Keyan Zhu-Salzman, Feng Ge, Zihua Zhao, and Yucheng Sun. A complete dna repair system assembled by two endosymbionts restores heat tolerance of the insect host. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2415651121, doi:10.1073/pnas.2415651121. This article has 14 citations and is from a highest quality peer-reviewed journal.

9. (ward2024adaptationduringthe pages 1-2): Christopher M. Ward, Cristobal A. Onetto, and Anthony R Borneman. Adaptation during the shift from entomopathogen to endosymbiont is accompanied by gene loss and intensified selection. Genome Biology and Evolution, Nov 2024. URL: https://doi.org/10.1093/gbe/evae251, doi:10.1093/gbe/evae251. This article has 5 citations and is from a domain leading peer-reviewed journal.