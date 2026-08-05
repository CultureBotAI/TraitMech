---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:05:58.370716'
end_time: '2026-08-04T05:15:17.631237'
duration_seconds: 559.26
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: plasmid carriage
  trait_identifier: traitmech:000090
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: plasmid_carriage
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A genomics trait describing possession of one or more plasmids \u2014\
    \ extrachromosomal, typically circular DNA replicons that carry accessory genes\
    \ such as resistance, virulence, or metabolic functions and can transfer by conjugation."
  parent_traits: traitmech:000089
  synonyms: plasmid-bearing
  evidence_summary: 'DOI:10.1128/MMBR.00020-10:  (Smillie et al. review plasmid mobility,
    classifying conjugative and mobilizable plasmids as key vectors of horizontal
    gene transfer.) | DOI:10.1038/nrmicro1235:  (Frost et al. include plasmids among
    the principal mobile genetic elements.)'
  causal_graph_summary: 'plasmid_conjugation_hgt: 11 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 69
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** plasmid carriage
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000090
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of one or more plasmids — extrachromosomal, typically circular DNA replicons that carry accessory genes such as resistance, virulence, or metabolic functions and can transfer by conjugation.
- **Parent traits:** traitmech:000089
- **Synonyms:** plasmid-bearing
- **Existing evidence:** DOI:10.1128/MMBR.00020-10:  (Smillie et al. review plasmid mobility, classifying conjugative and mobilizable plasmids as key vectors of horizontal gene transfer.) | DOI:10.1038/nrmicro1235:  (Frost et al. include plasmids among the principal mobile genetic elements.)
- **Existing causal graph summary:** plasmid_conjugation_hgt: 11 nodes, 8 edges

## Research Objective

Research the microbial trait **plasmid carriage** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/plasmid_carriage.yaml`.

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
- **Trait label:** plasmid carriage
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000090
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of one or more plasmids — extrachromosomal, typically circular DNA replicons that carry accessory genes such as resistance, virulence, or metabolic functions and can transfer by conjugation.
- **Parent traits:** traitmech:000089
- **Synonyms:** plasmid-bearing
- **Existing evidence:** DOI:10.1128/MMBR.00020-10:  (Smillie et al. review plasmid mobility, classifying conjugative and mobilizable plasmids as key vectors of horizontal gene transfer.) | DOI:10.1038/nrmicro1235:  (Frost et al. include plasmids among the principal mobile genetic elements.)
- **Existing causal graph summary:** plasmid_conjugation_hgt: 11 nodes, 8 edges

## Research Objective

Research the microbial trait **plasmid carriage** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/plasmid_carriage.yaml`.

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


# TraitMech curation report: plasmid carriage

**Trait:** `traitmech:000090`  
**Label:** plasmid carriage  
**Category:** GENOMICS | **Kind:** CLASS | **Status:** REVIEWED  
**Parent:** `traitmech:000089`

## 1. Scope summary

Plasmid carriage is the state in which a microbial cell possesses at least one **autonomously replicating, extrachromosomal DNA replicon**. Most plasmids are circular, but circularity should not be required because linear plasmids occur. Likewise, conjugative mobility, antimicrobial-resistance genes, virulence genes, and high copy number are optional properties rather than defining criteria. A 2023 survey describes plasmids as autonomously replicating mobile genetic elements and explicitly notes both circular and linear forms; only 22% of its identified *Salmonella* MOB-clusters were associated with a known resistance gene. Thus, “plasmid carriage” must not be made synonymous with AMR carriage (robertson2023aglobalsurvey pages 1-2).

The graph should represent two routes into and maintenance of the state:

1. **Acquisition/establishment:** conjugation or another DNA-transfer route → evasion of recipient defense → autonomous replication → plasmid carriage.
2. **Vertical maintenance:** replication/copy-number control + segregation/partition + multimer resolution and, in some plasmids, toxin–antitoxin systems → reduced plasmid loss → persistent carriage.

Host fitness, positive selection, compensatory evolution, cell-envelope properties, co-resident plasmids, and ecological context modify these routes. Contemporary plasmid ecology treats host fitness effects and horizontal transmission rate as the principal population-level controls; conjugation affects both initial acquisition and persistence by replenishing plasmid-bearing cells (dimitriu2024variousplasmidstrategies pages 1-2).

### Boundary cases

- **Include:** cells carrying one or more autonomous plasmids; low- or high-copy plasmids; circular or linear plasmids; conjugative, mobilizable, or non-mobilizable plasmids.
- **Exclude:** an integrative conjugative element residing only in the chromosome; a resistance gene integrated into the chromosome after leaving a plasmid; transient transferred DNA that never establishes autonomous replication; and naked plasmid DNA outside a cell.
- **Do not equate with:** plasmid persistence, conjugation, plasmid copy number, plasmid-borne AMR, virulence, or metabolic phenotypes. These are causes, modifiers, measurements, or consequences of carriage.
- **Assay caution:** short-read replicon calls and MOB-suite reconstructions are evidence for predicted carriage, not necessarily direct observation of an intact autonomous molecule. Long-read closure, plasmid extraction, copy-number measurements, or demonstrated transfer/stability provide stronger evidence.

## 2. Candidate nodes and ontology grounding

Identifiers below are restricted to high-confidence established terms. Family- or plasmid-specific entities are deliberately left label-only where a stable cross-database identifier was not verified.

### A. Trait and physical entities

- **plasmid carriage:** `traitmech:000090`
- **plasmid:** GO:0005727
- **plasmid DNA / extrachromosomal replicon:** label-only candidate if the data model distinguishes molecule from localization
- **plasmid replication origin (oriV):** label-only
- **plasmid multimer:** label-only
- **donor cell, recipient cell, transconjugant:** label-only role nodes
- **cytoplasm:** GO:0005737

### B. Processes and molecular functions

- **DNA replication:** GO:0006260
- **DNA-templated transcription:** GO:0006351
- **DNA recombination:** GO:0006310
- **conjugation:** GO:0000746
- **DNA-mediated transformation:** GO:0009294
- **DNA methylation:** GO:0006306
- **DNA binding:** GO:0003677
- **DNA-binding transcription-factor activity:** GO:0003700
- **endonuclease activity:** GO:0004519
- **transposase activity:** GO:0004803
- **biofilm formation:** GO:0042710
- **cell death:** GO:0008219
- **plasmid replication, plasmid partition, multimer resolution, post-segregational killing, plasmid loss, compensatory evolution, plasmid establishment, and plasmid incompatibility:** retain as label-only candidates unless the curation environment supplies verified ontology terms.

### C. Genes, proteins, RNAs, and complexes

**Core inheritance modules**

- Rep replication initiator and oriV
- ColE1 priming RNA (**RNA-p/RNA II**) and inhibitory antisense RNA (**RNA-i/RNA I**)
- **ParA–ParB** partition system and centromere-like **parS** site
- **KorB/ParB** of IncP-1 plasmids
- site-specific multimer-resolution machinery, such as Xer-like recombinases where demonstrated
- toxin–antitoxin/post-segregational-killing modules: **vapBC2ST**, **ccdABST**, and generic stable toxin–labile antitoxin pair

Direct *Salmonella* evidence shows that `parAB` is crucial for pSLT maintenance and that `vapBC2ST` contributes to stability; this supports separate partition and TA branches rather than one generic “stability gene” node (lobatomarquez2016stabilizationofthe pages 1-2). A plasmid-curing study also identifies controlled replication, active partitioning, multimer resolution, and post-segregational killing as distinct stable-inheritance mechanisms (lazdins2020potentiationofcuring pages 1-2).

**Horizontal transfer and defense**

- relaxase/relaxosome
- origin of transfer (**oriT**)
- mating-pair-formation/type IV secretion machinery
- restriction endonuclease and cognate DNA methyltransferase
- plasmid-encoded methylase
- anti-restriction protein
- CRISPR array, crRNA, and Cas interference complex
- bacterial capsule and conjugative pilus

**Host adaptation and regulatory crosstalk**

- **PFLU4242** and plasmid regulator **PQBR57_0059**—specific to *Pseudomonas fluorescens* SBW25–pQBR57 compensation
- **nsrR**, **ndh**, **ndhC**, **rppH**, and **fabI**—specific to triclosan-evolved *Klebsiella pneumoniae*
- pOXA-48-encoded **LysR-family regulator**
- chromosomal **pfp–ifp** operon in *Klebsiella/Citrobacter*
- **IS26**, integrons, and insertion sequences

The pOXA-48 LysR regulator experimentally causes plasmid–chromosome crosstalk, while overexpression of the chromosomal `pfp–ifp` operon benefits one plasmid-bearing MDR *K. pneumoniae* strain (toribiocelestino2024aplasmidchromosomecrosstalk pages 1-2). These should remain plasmid- and taxon-qualified rather than becoming universal carriage mechanisms.

### D. Chemicals and environmental factors

- **triclosan:** CHEBI:164200
- **antibiotic:** CHEBI:22582
- **mercury atom:** CHEBI:16170; use a more specific mercury species when the experiment identifies it
- nutrients/root exudates: label-only unless individually specified
- **biofilm:** ENVO:00002034
- **rhizosphere:** ENVO:00005801
- hospital sink/drain biofilm, wastewater plumbing, antibiotic exposure, disinfectant exposure, metal exposure, no-selection conditions: label-only experimental/environmental nodes

### E. Taxa with direct evidence

- *Escherichia coli*: NCBITaxon:562
- *Klebsiella pneumoniae*: NCBITaxon:573
- *Salmonella enterica*: NCBITaxon:28901
- *Pseudomonas fluorescens*: NCBITaxon:294
- *Staphylococcus epidermidis*: NCBITaxon:1282

## 3. Candidate evidence-backed edges

The following table is intended as a curation worksheet. “High” denotes direct experimental evidence or an established mechanism; “medium” usually denotes population-genomic association or an ecological extrapolation; “low–medium” denotes model-based support that should not yet be represented as a general causal edge.

| subject | predicate | object | evidence snippet (short direct quote) | DOI/year | confidence/context |
|---|---|---|---|---|---|
| plasmid copy number control | prevents | plasmid loss | "as the RNA production ratio kp/ki decreases, the number of plasmids inside each cell will approach 1 ... may lead to the catastrophic consequence of plasmid loss" (rouches2022aplasmidsystem pages 1-2) | 10.1038/s41467-022-31422-0 / 2022 | High; ColE1-based experimental/synthetic system, mechanistically general for copy-number dependence |
| low plasmid copy number | reduces | metabolic burden | "Few copies reduce metabolic burden but suppose a risk of plasmid loss during bacterial division" (lobatomarquez2016stabilizationofthe pages 1-2) | 10.3389/fmolb.2016.00066 / 2016 | High; Salmonella pSLT low-copy virulence plasmid, taxon/plasmid-specific example |
| parAB partition system | stabilizes | plasmid carriage | "we confirmed a crucial role of parAB in pSLT maintenance" (lobatomarquez2016stabilizationofthe pages 1-2) | 10.3389/fmolb.2016.00066 / 2016 | High; direct experimental evidence in Salmonella Typhimurium pSLT |
| active partitioning | contributes to stable inheritance of plasmids | plasmid carriage | "For stable inheritance, plasmids have evolved a variety of mechanisms: controlled replication, active partitioning, multimer resolution" (lazdins2020potentiationofcuring pages 1-2) | 10.1371/journal.pone.0225202 / 2020 | High; review/introduction framing, broad across plasmids |
| post-segregational killing systems (toxin-antitoxin/PSK) | stabilize | plasmid carriage | "For stable inheritance, plasmids have evolved ... 'addiction' or post-segregational killing (PSK) systems" (lazdins2020potentiationofcuring pages 1-2) | 10.1371/journal.pone.0225202 / 2020 | High; broad mechanism statement |
| unstable antitoxin + stable toxin | causes | death after plasmid loss | "the toxin becomes active in the cell after plasmid loss" (lazdins2020potentiationofcuring pages 1-2) | 10.1371/journal.pone.0225202 / 2020 | High; canonical PSK mechanism, broad |
| vapBC2ST toxin-antitoxin locus | contributes to | plasmid stability | "we also showed that vapBC2ST ... is important for plasmid stability" (lobatomarquez2016stabilizationofthe pages 1-2) | 10.3389/fmolb.2016.00066 / 2016 | High; Salmonella pSLT-specific |
| conjugation rate | impacts | plasmid persistence in populations | "Conjugation will impact not only a plasmid's ability to persist within a population" (dimitriu2024variousplasmidstrategies pages 1-2) | 10.1093/nar/gkae896 / 2024 | High; broad conceptual statement for conjugative plasmids |
| fitness cost of plasmid carriage | limits | plasmid persistence/transmission | "plasmid acquisition can produce physiological alterations in the bacterial host, leading to potential fitness costs" (toribiocelestino2024aplasmidchromosomecrosstalk pages 1-2); "plasmids impose a burden on the bacteria that carry them" (wright2024achromosomalmutation pages 1-2) | 10.1038/s41467-024-55169-y / 2024; 10.1371/journal.pbio.3002926 / 2024 | High; broad, with experimental backing in Enterobacteriaceae and Pseudomonas |
| chromosomal compensatory mutation | reduces | plasmid fitness cost | "Single CMs affecting either PFLU4242 or plasmid regulator PQBR57_0059 negate this cost" (wright2024achromosomalmutation pages 1-2) | 10.1371/journal.pbio.3002926 / 2024 | High; direct in Pseudomonas fluorescens SBW25-pQBR57 |
| chromosomal compensatory mutation | promotes long-term | plasmid persistence/dissemination | "compensated bacteria that can act as 'hubs' for plasmid accumulation and dissemination" (wright2024achromosomalmutation pages 1-2) | 10.1371/journal.pbio.3002926 / 2024 | Medium; ecological implication from experiments/model, taxon-specific base system |
| restriction-modification (RM) systems | restrict | plasmid establishment after conjugation | "RM systems ... act as a barrier against plasmids"; defence efficiency ranged "from none to 10^5-fold protection" (dimitriu2024variousplasmidstrategies pages 1-2) | 10.1093/nar/gkae896 / 2024 | High; E. coli with 10 RM systems and 13 natural AMR plasmids |
| number of RM recognition sites on plasmid | increases | RM-mediated defence against plasmids | "higher numbers of sites being associated with stronger defence" (dimitriu2024variousplasmidstrategies pages 1-2) | 10.1093/nar/gkae896 / 2024 | High; E. coli experimental panel |
| plasmid-encoded methylases | protect against | restriction activity | "some plasmids encode methylases that protect against restriction activity" (dimitriu2024variousplasmidstrategies pages 1-2) | 10.1093/nar/gkae896 / 2024 | High; direct experimental/genomic analysis |
| plasmid-encoded anti-restriction genes | reduce | RM barrier to conjugation | "a high number of plasmids ... encode anti-restriction genes" and RM systems "form only a weak barrier for plasmid transfer by conjugation" (dimitriu2024variousplasmidstrategies pages 1-2) | 10.1093/nar/gkae896 / 2024 | High; natural AMR plasmids in E. coli |
| CRISPR-Cas immunity | prevents acquisition of | conjugative plasmids | "CRISPR interference has been shown experimentally to prevent the acquisition of conjugative plasmids" (jiang2013dealingwiththe pages 1-2) | 10.1371/journal.pgen.1003844 / 2013 | High; broad statement with Staphylococcus epidermidis experiment |
| loss/inactivation of CRISPR-Cas locus | permits | plasmid carriage | "more than 10^-4 of the cells in CRISPR-Cas positive populations are defective or deleted for the CRISPR-Cas region and thereby able to receive and carry the plasmid" (jiang2013dealingwiththe pages 1-2) | 10.1371/journal.pgen.1003844 / 2013 | High; direct experimental evidence in S. epidermidis RP62a/pG0400 |
| capsule serotype/volume | modulates | conjugation efficiency | "Capsule types also influence conjugation efficiency in both donor and recipient cells" (haudiquet2024capsulesandtheir pages 1-2) | 10.1038/s41467-024-46147-5 / 2024 | High; direct in Klebsiella pneumoniae capsule-swap experiments |
| antibiotic selective pressure | selects for | AMR plasmid-carrying bacteria | "antibiotic pressure persistently selects for AMR plasmid-carrying bacteria" (toribiocelestino2024aplasmidchromosomecrosstalk pages 1-2); "plasmid-borne ... genes ... are spreading in clinical pathogens under antibiotics selective pressure" (wang2024interplasmidtransferof pages 1-2) | 10.1038/s41467-024-55169-y / 2024; 10.1093/ismejo/wrad032 / 2024 | High; clinical/ecological generalization |
| triclosan exposure | increases evolvability of | triclosan-resistant mutants | "TCS exposure increases the evolvability of K. pneumoniae to evolve TCS-resistant mutants" (yang2024evolutionoftriclosan pages 1-2) | 10.1038/s41467-024-48006-9 / 2024 | High; direct experimental evolution in K. pneumoniae |
| nsrR deletion | increases permissiveness to | AMR plasmid conjugation | "nsrR deletion increases conjugation permissiveness of K. pneumoniae to four AMR plasmids" (yang2024evolutionoftriclosan pages 1-2) | 10.1038/s41467-024-48006-9 / 2024 | High; direct, taxon-specific to K. pneumoniae |
| plasmid-encoded LysR regulator | causes | plasmid-chromosome crosstalk | "a pOXA-48-encoded LysR regulator is responsible for the plasmid-chromosome crosstalk" (toribiocelestino2024aplasmidchromosomecrosstalk pages 1-2) | 10.1038/s41467-024-55169-y / 2024 | High; direct in pOXA-48-carrying MDR enterobacteria |
| overexpression of chromosomal pfp-ifp operon | provides fitness benefit to | pOXA-48-carrying host | "the operon overexpression produces a fitness benefit in a pOXA-48-carrying MDR K. pneumoniae strain" (toribiocelestino2024aplasmidchromosomecrosstalk pages 1-2) | 10.1038/s41467-024-55169-y / 2024 | High; direct but strain-specific |
| compatible co-resident plasmids | facilitate | ARG transfer between plasmids | "over 88% of ARG transfers occurring between compatible plasmids" (wang2024interplasmidtransferof pages 1-2) | 10.1093/ismejo/wrad032 / 2024 | High; large-scale genomic inference with supporting experiment |
| IS26 | facilitates | inter-plasmid ARG transfer | "IS26 facilitates 63.1% of ARG transfer events among plasmids" (wang2024interplasmidtransferof pages 1-2) | 10.1093/ismejo/wrad032 / 2024 | High; large dataset plus in vitro validation |
| hospital drain biofilm/wastewater reservoir | supports | persistence and movement of AMR plasmids/genes | "Water system biofilms in sink drains and traps are a unique ecosystem" and "provides opportunities for AMR gene movement and sharing between bacteria via ... conjugative plasmids" (mathers2024developingaframework pages 1-2) | 10.1038/s44259-024-00069-w / 2024 | High; longitudinal environmental surveillance in hospital drains |
| blaKPC transposition among plasmids/chromosome | contributes to | persistent reservoir dynamics | "frequent transposition events of blaKPC from plasmids to other plasmids, as well as integration into the bacterial chromosome" (mathers2024developingaframework pages 1-2) | 10.1038/s44259-024-00069-w / 2024 | High; hospital drain system, gene-specific rather than generic plasmid carriage |
| rhizosphere environment | is hotspot for | conjugative HGT | "it has been indicated as a hotspot of HGT, especially via conjugation" (riva2024conjugalplasmidtransfer pages 1-2) | 10.3389/fmicb.2024.1457854 / 2024 | Medium; literature-backed environmental statement |
| broad-host-range plasmid pKJK5 | transfers in rhizosphere at frequency | 10^-3 | "Fluorescence stereomicroscopy revealed plasmid transfer at a frequency of 10−3" (riva2024conjugalplasmidtransfer pages 1-2) | 10.3389/fmicb.2024.1457854 / 2024 | High; direct in lettuce rhizosphere, donor Klebsiella variicola EEF15 |
| mobilizable/conjugative plasmid mobility class | associates with broader | host range/serovar spread | "non-mobilizable plasmids were associated with fewer serotypes compared to mobilizable or conjugative MOB-clusters" (robertson2023aglobalsurvey pages 1-2) | 10.1099/mgen.0.001002 / 2023 | Medium; population-genomic association in Salmonella, inferred ecological edge |
| mobilizable MOB-clusters | account for most | broad-host-range predictions | "mobilizable MOB-clusters accounting for 88.3% of the multi-phyla (broad-host-range) predictions" (robertson2023aglobalsurvey pages 1-2) | 10.1099/mgen.0.001002 / 2023 | Medium; prediction-based, not direct mechanism |
| biofilm contaminants (metals/antibiotics) | promote | plasmid persistence and conjugation | "contaminants like toxic metals and antibiotics promote plasmid persistence by favoring plasmid carriers and stimulating conjugation" (liu2024compensatoryevolutionof pages 10-11) | 10.1007/s11538-024-01289-x / 2024 | Low-Medium; modeling paper, inferred not directly curatable without primary experiment |


*Table: This table compiles compact, curation-ready candidate causal edges for plasmid carriage (traitmech:000090), with short evidence snippets, DOIs, and context/confidence notes. It is designed to support TraitMech graph construction while flagging taxon-specific and inferred/model-based claims.*

### Recommended minimal backbone for `plasmid_carriage.yaml`

The highest-confidence, least redundant backbone is:

1. `plasmid replication` **enables** `plasmid carriage`
2. `copy-number control` **regulates** `plasmid replication`
3. `active partitioning` **decreases** `segregational plasmid loss`
4. `multimer resolution` **decreases** `segregational plasmid loss`
5. `toxin–antitoxin/post-segregational killing` **decreases population frequency of** `plasmid-free segregants`
6. `conjugation` **increases** `plasmid acquisition`
7. `plasmid acquisition` **increases** `plasmid carriage`
8. `plasmid fitness cost` **decreases** `persistence of plasmid carriage`
9. `positive selection for plasmid-encoded function` **increases** `persistence of plasmid carriage`
10. `compensatory mutation` **decreases** `plasmid fitness cost`
11. `restriction–modification defense` **decreases** `plasmid establishment`
12. `CRISPR–Cas interference` **decreases** `plasmid acquisition/establishment`
13. `plasmid anti-restriction mechanism` **decreases** `RM-mediated restriction`

Importantly, post-segregational killing does not necessarily preserve a plasmid molecule inside the cell that lost it. It eliminates or arrests plasmid-free segregants and thereby stabilizes carriage at the lineage/population level. The object should therefore not simply be “cell retains plasmid” unless the TraitMech predicate semantics can express that distinction (lazdins2020potentiationofcuring pages 1-2).

## 4. Recent developments and quantitative evidence

### Host defense is a highly variable barrier

A 2024 *Nucleic Acids Research* study tested **10 restriction–modification systems against 13 natural AMR plasmids in *E. coli***. Protection ranged from none to **10^5-fold**. More recognition sites generally produced stronger defense, whereas plasmid methylases and anti-restriction genes weakened it. The authors consequently characterize RM as only a weak general barrier because plasmid countermeasures are common (published 16 October 2024; DOI [10.1093/nar/gkae896](https://doi.org/10.1093/nar/gkae896)) (dimitriu2024variousplasmidstrategies pages 1-2).

CRISPR–Cas provides a second establishment barrier. In a *Staphylococcus epidermidis*–pG0400 system, plasmid acquisition occurred through host loss or inactivation of targeting CRISPR immunity; more than **10^-4** of cells in nominally CRISPR-positive populations were defective/deleted and could carry the plasmid. This is strong evidence for `functional CRISPR-Cas → decreased acquisition`, but also shows that genotype presence alone does not guarantee the phenotype (published 26 September 2013; DOI [10.1371/journal.pgen.1003844](https://doi.org/10.1371/journal.pgen.1003844)) (jiang2013dealingwiththe pages 1-2).

### Host surface and environmental adaptation modify permissiveness

Capsule-locus swaps in *K. pneumoniae* demonstrated that capsule type affects conjugation in both donors and recipients; capsule volume and pilus structure help determine the effect. More permissive serotypes in the laboratory also corresponded to strains with more conjugative plasmids in nature. The causal edge should be “capsule properties modulate conjugation efficiency,” not a universal positive or negative direction (accepted 14 February 2024; DOI [10.1038/s41467-024-46147-5](https://doi.org/10.1038/s41467-024-46147-5)) (haudiquet2024capsulesandtheir pages 1-2).

Triclosan experimental evolution provides a recent example of chemical exposure changing host permissiveness. In *K. pneumoniae*, deletion of the stress regulator `nsrR` increased permissiveness to four AMR plasmids. The study also found ciprofloxacin MIC increasing from **0.5 to 8 mg/L**, with fourfold and 16-fold increases for cefotaxime and fosfomycin, respectively. These MIC effects describe evolved cross-resistance, however, and should not be represented as effects of plasmid carriage itself (accepted 17 April 2024; DOI [10.1038/s41467-024-48006-9](https://doi.org/10.1038/s41467-024-48006-9)) (yang2024evolutionoftriclosan pages 1-2).

### Compensatory evolution stabilizes costly associations

Current expert synthesis emphasizes that plasmid costs arise from metabolic burden, stress responses, gene-expression disruption, and direct conflicts between plasmid and chromosome machinery. Compensatory changes can occur in either replicon. In the *P. fluorescens* SBW25–pQBR57 system, mutations involving chromosomal `PFLU4242` or plasmid regulator `PQBR57_0059` eliminated a specific cost. Chromosomal compensation outperformed plasmid compensation experimentally and could create host “hubs” permissive to multiple plasmids, although the hub conclusion remains an ecological inference from a defined laboratory system (published December 2024; DOI [10.1371/journal.pbio.3002926](https://doi.org/10.1371/journal.pbio.3002926)) (wright2024achromosomalmutation pages 1-2, wright2024achromosomalmutation pages 14-15).

In MDR enterobacteria, a pOXA-48 LysR regulator induced `pfp–ifp`; operon overexpression provided a fitness benefit in one pOXA-48-bearing *K. pneumoniae* strain. Most transcriptional effects were nevertheless strain-specific. The correct graph pattern is therefore a qualified mechanistic subgraph, not `LysR regulation → plasmid carriage` across bacteria (accepted 3 December 2024; DOI [10.1038/s41467-024-55169-y](https://doi.org/10.1038/s41467-024-55169-y)) (toribiocelestino2024aplasmidchromosomecrosstalk pages 1-2).

### Co-resident plasmids create an ARG-recruitment network

Analysis of **2,420 complete clinical plasmid genomes** found that 87% of 8,229 plasmid-borne ARGs showed potential transfer among plasmids; more than 88% of inferred transfers occurred between compatible plasmids, and **IS26 accounted for 63.1%** of events. An *in vitro* experiment supported IS26-mediated transfer of `aacC1`. These data justify an `IS26 → inter-plasmid ARG movement` edge, but ARG recruitment is a consequence of co-carriage, not a mechanism required for basic plasmid carriage (published 10 January 2024; DOI [10.1093/ismejo/wrad032](https://doi.org/10.1093/ismejo/wrad032)) (wang2024interplasmidtransferof pages 1-2).

## 5. Applications and real-world implementation

### Genomic surveillance

A 2023 MOB-suite survey analyzed **150,767 *Salmonella* genomes**, reconstructing **183,017 plasmids** in 1,044 primary MOB-clusters plus 830 potentially novel clusters. Replicon typing identified 83.4%, relaxase typing 58%, and MOB-clustering 99.9%. Mobilizable plasmids represented 88.3% of predicted multi-phyla host-range clusters, while only 22% of MOB-clusters carried a known resistance gene. These results support mobility-aware plasmid surveillance while illustrating that predicted mobility, AMR association, and carriage are distinct traits (published 18 May 2023; DOI [10.1099/mgen.0.001002](https://doi.org/10.1099/mgen.0.001002)) (robertson2023aglobalsurvey pages 1-2).

### Hospital environmental reservoirs

Hybrid long/short-read surveillance across six hospital drains over five years recovered 82 analyzable isolates, 14 strains from 10 species, and **113 `blaKPC`-carrying plasmids spanning 16 replicon types**. Frequent transposition moved `blaKPC` between plasmids and into chromosomes. Hospital drain biofilms should therefore be modeled as environments supporting contact, persistence, and gene mobilization—not as direct molecular causes of carriage in every species (published December 2024; DOI [10.1038/s44259-024-00069-w](https://doi.org/10.1038/s44259-024-00069-w)) (mathers2024developingaframework pages 1-2).

### One Health/agri-food monitoring

A fluorescent pKJK5 system directly detected transfer from wastewater-derived *K. variicola* into the lettuce rhizosphere microbiome at a frequency of **10^-3**; the donor also entered the leaf endosphere seven days after administration. This is a real-world-like demonstration that plant-associated microbiomes can receive broad-host-range plasmids, but its numerical rate is specific to the constructed donor, marker plasmid, plant system, and assay (published 29 August 2024; DOI [10.3389/fmicb.2024.1457854](https://doi.org/10.3389/fmicb.2024.1457854)) (riva2024conjugalplasmidtransfer pages 1-2).

### Plasmid curing and synthetic biology

Replication interference, addiction-system neutralization, and incompatibility can be exploited to remove resistance plasmids. An IncP-1 curing vector required both elevated copy number and `korB`; it displaced targets in laboratory populations and showed activity in a mouse model, although in vivo spread was less efficient and required additional selection. This is proof of concept, not an established clinical treatment (published 15 January 2020; DOI [10.1371/journal.pone.0225202](https://doi.org/10.1371/journal.pone.0225202)) (lazdins2020potentiationofcuring pages 1-2).

Engineered ColE1 systems can tune copy number from **1 to 800 copies per cell**. In that platform, each additional plasmid imposed an estimated **0.063% linear metabolic burden**. Copy-number engineering is already important for gene expression and biosynthetic optimization, but this burden coefficient is system-specific and should not become a universal biological edge weight (published July 2022; DOI [10.1038/s41467-022-31422-0](https://doi.org/10.1038/s41467-022-31422-0)) (rouches2022aplasmidsystem pages 1-2).

## 6. Curation warnings

1. **Do not require circularity.** Linear plasmids are documented (robertson2023aglobalsurvey pages 1-2).
2. **Do not define carriage by AMR.** Most *Salmonella* MOB-clusters in the large 2023 survey lacked identified resistance genes (robertson2023aglobalsurvey pages 1-2).
3. **Do not merge carriage with persistence.** Carriage is a cell state; persistence is maintenance across time, divisions, or a population.
4. **Do not merge conjugation with carriage.** A non-mobilizable plasmid can be carried, and transferred DNA may fail to establish.
5. **Do not treat every accessory phenotype as caused by carriage generally.** Resistance, virulence, and metabolism depend on particular plasmid genes and expression contexts.
6. **Qualify taxon-specific edges.** `parAB/vapBC2ST` evidence concerns *Salmonella* pSLT; `nsrR` concerns experimental *K. pneumoniae*; `PFLU4242/PQBR57_0059` concerns *P. fluorescens*–pQBR57; and LysR–`pfp-ifp` concerns pOXA-48 and selected enterobacteria (yang2024evolutionoftriclosan pages 1-2, toribiocelestino2024aplasmidchromosomecrosstalk pages 1-2, lobatomarquez2016stabilizationofthe pages 1-2, wright2024achromosomalmutation pages 1-2).
7. **Represent capsule effects as “modulates.”** Direction varies with serotype, capsule volume, donor/recipient status, and pilus type (haudiquet2024capsulesandtheir pages 1-2).
8. **Do not curate modeled contaminant effects as general causal facts yet.** Predictions that antibiotics/metals promote persistence in biofilms require matching direct experiments and concentration-specific context.
9. **Separate DNA movement from plasmid movement.** IS26-mediated ARG transposition among plasmids changes plasmid content but does not itself establish a new plasmid replicon (wang2024interplasmidtransferof pages 1-2).
10. **Treat genomic reconstructions as assay observations.** MOB clusters, replicon calls, and host-range predictions are not equivalent to demonstrated autonomous replication or transfer (robertson2023aglobalsurvey pages 1-2).
11. **Avoid universal quantitative weights.** The 0.063% burden per plasmid, 10^-3 rhizosphere transfer rate, and up-to-10^5-fold RM protection are experimental-system estimates, not species-independent constants (riva2024conjugalplasmidtransfer pages 1-2, dimitriu2024variousplasmidstrategies pages 1-2, rouches2022aplasmidsystem pages 1-2).
12. **Do not assign unverified CURIEs.** Plasmid-family genes and specialized processes should remain label-only until identifiers are checked against the target ontology release.

## 7. DOI-first bibliography

1. Dimitriu T, Szczelkun MD, Westra ER. “Various plasmid strategies limit the effect of bacterial restriction–modification systems against conjugation.” *Nucleic Acids Research* 52, 12976–12986. Published 16 October 2024. [https://doi.org/10.1093/nar/gkae896](https://doi.org/10.1093/nar/gkae896) (dimitriu2024variousplasmidstrategies pages 1-2).
2. Wright RCT et al. “A chromosomal mutation is superior to a plasmid-encoded mutation for plasmid fitness cost compensation.” *PLOS Biology* 22:e3002926. Published December 2024. [https://doi.org/10.1371/journal.pbio.3002926](https://doi.org/10.1371/journal.pbio.3002926) (wright2024achromosomalmutation pages 1-2, wright2024achromosomalmutation pages 14-15).
3. Toribio-Celestino L et al. “A plasmid-chromosome crosstalk in multidrug resistant enterobacteria.” *Nature Communications* 15:10859. Accepted 3 December 2024. [https://doi.org/10.1038/s41467-024-55169-y](https://doi.org/10.1038/s41467-024-55169-y) (toribiocelestino2024aplasmidchromosomecrosstalk pages 1-2).
4. Yang QE et al. “Evolution of triclosan resistance modulates bacterial permissiveness to multidrug resistance plasmids and phages.” *Nature Communications* 15:3654. Accepted 17 April 2024. [https://doi.org/10.1038/s41467-024-48006-9](https://doi.org/10.1038/s41467-024-48006-9) (yang2024evolutionoftriclosan pages 1-2).
5. Haudiquet M et al. “Capsules and their traits shape phage susceptibility and plasmid conjugation efficiency.” *Nature Communications* 15:2032. Accepted 14 February 2024. [https://doi.org/10.1038/s41467-024-46147-5](https://doi.org/10.1038/s41467-024-46147-5) (haudiquet2024capsulesandtheir pages 1-2).
6. Wang X et al. “Inter-plasmid transfer of antibiotic resistance genes accelerates antibiotic resistance in bacterial pathogens.” *ISME Journal* 18:wrad032. Published 10 January 2024. [https://doi.org/10.1093/ismejo/wrad032](https://doi.org/10.1093/ismejo/wrad032) (wang2024interplasmidtransferof pages 1-2).
7. Mathers AJ et al. “Developing a framework for tracking antimicrobial resistance gene movement in a persistent environmental reservoir.” *npj Antimicrobials & Resistance* 2:50. Published December 2024. [https://doi.org/10.1038/s44259-024-00069-w](https://doi.org/10.1038/s44259-024-00069-w) (mathers2024developingaframework pages 1-2).
8. Riva F et al. “Conjugal plasmid transfer in the plant rhizosphere in the One Health context.” *Frontiers in Microbiology* 15:1457854. Published 29 August 2024. [https://doi.org/10.3389/fmicb.2024.1457854](https://doi.org/10.3389/fmicb.2024.1457854) (riva2024conjugalplasmidtransfer pages 1-2).
9. Liu Z et al. “Compensatory evolution of chromosomes and plasmids counteracts the plasmid fitness cost.” *Ecology and Evolution* 14. Published August 2024. [https://doi.org/10.1002/ece3.70121](https://doi.org/10.1002/ece3.70121) (liu2024compensatoryevolutionof pages 10-11).
10. Robertson J et al. “A global survey of *Salmonella* plasmids and their associations with antimicrobial resistance.” *Microbial Genomics* 9:001002. Published 18 May 2023. [https://doi.org/10.1099/mgen.0.001002](https://doi.org/10.1099/mgen.0.001002) (robertson2023aglobalsurvey pages 1-2).
11. Rouches MV et al. “A plasmid system with tunable copy number.” *Nature Communications* 13:3908. Published July 2022. [https://doi.org/10.1038/s41467-022-31422-0](https://doi.org/10.1038/s41467-022-31422-0) (rouches2022aplasmidsystem pages 1-2).
12. Lazdins A et al. “Potentiation of curing by a broad-host-range self-transmissible vector for displacing resistance plasmids to tackle AMR.” *PLOS ONE* 15:e0225202. Published 15 January 2020. [https://doi.org/10.1371/journal.pone.0225202](https://doi.org/10.1371/journal.pone.0225202) (lazdins2020potentiationofcuring pages 1-2).
13. Lobato-Márquez D et al. “Stabilization of the Virulence Plasmid pSLT of *Salmonella* Typhimurium by Three Maintenance Systems.” *Frontiers in Molecular Biosciences* 3:66. Published 17 October 2016. [https://doi.org/10.3389/fmolb.2016.00066](https://doi.org/10.3389/fmolb.2016.00066) (lobatomarquez2016stabilizationofthe pages 1-2).
14. Jiang W et al. “Dealing with the Evolutionary Downside of CRISPR Immunity: Bacteria and Beneficial Plasmids.” *PLOS Genetics* 9:e1003844. Published 26 September 2013. [https://doi.org/10.1371/journal.pgen.1003844](https://doi.org/10.1371/journal.pgen.1003844) (jiang2013dealingwiththe pages 1-2).

References

1. (robertson2023aglobalsurvey pages 1-2): James Robertson, Justin Schonfeld, Kyrylo Bessonov, Patrick Bastedo, and John H. E. Nash. A global survey of salmonella plasmids and their associations with antimicrobial resistance. May 2023. URL: https://doi.org/10.1099/mgen.0.001002, doi:10.1099/mgen.0.001002. This article has 25 citations and is from a peer-reviewed journal.

2. (dimitriu2024variousplasmidstrategies pages 1-2): Tatiana Dimitriu, Mark D Szczelkun, and Edze R Westra. Various plasmid strategies limit the effect of bacterial restriction–modification systems against conjugation. Oct 2024. URL: https://doi.org/10.1093/nar/gkae896, doi:10.1093/nar/gkae896. This article has 46 citations and is from a highest quality peer-reviewed journal.

3. (lobatomarquez2016stabilizationofthe pages 1-2): Damián Lobato-Márquez, Laura Molina-García, Inma Moreno-Córdoba, Francisco García-del Portillo, and Ramón Díaz-Orejas. Stabilization of the virulence plasmid pslt of salmonella typhimurium by three maintenance systems and its evaluation by using a new stability test. Frontiers in Molecular Biosciences, Oct 2016. URL: https://doi.org/10.3389/fmolb.2016.00066, doi:10.3389/fmolb.2016.00066. This article has 41 citations.

4. (lazdins2020potentiationofcuring pages 1-2): Alessandro Lazdins, Anand Prakash Maurya, Claire E. Miller, Muhammad Kamruzzaman, Shuting Liu, Elton R. Stephens, Georgina S. Lloyd, Mona Haratianfar, Melissa Chamberlain, Anthony S. Haines, Jan-Ulrich Kreft, Mark. A. Webber, Jonathan Iredell, and Christopher M. Thomas. Potentiation of curing by a broad-host-range self-transmissible vector for displacing resistance plasmids to tackle amr. PLoS ONE, 15:e0225202, Jan 2020. URL: https://doi.org/10.1371/journal.pone.0225202, doi:10.1371/journal.pone.0225202. This article has 23 citations and is from a peer-reviewed journal.

5. (toribiocelestino2024aplasmidchromosomecrosstalk pages 1-2): Laura Toribio-Celestino, Alicia Calvo-Villamañán, Cristina Herencias, Aida Alonso-del Valle, Jorge Sastre-Dominguez, Susana Quesada, Didier Mazel, Eduardo P. C. Rocha, Ariadna Fernández-Calvet, and Alvaro San Millan. A plasmid-chromosome crosstalk in multidrug resistant enterobacteria. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55169-y, doi:10.1038/s41467-024-55169-y. This article has 22 citations and is from a highest quality peer-reviewed journal.

6. (rouches2022aplasmidsystem pages 1-2): Miles V. Rouches, Yasu Xu, Louis Brian Georges Cortes, and Guillaume Lambert. A plasmid system with tunable copy number. Nature Communications, Jul 2022. URL: https://doi.org/10.1038/s41467-022-31422-0, doi:10.1038/s41467-022-31422-0. This article has 171 citations and is from a highest quality peer-reviewed journal.

7. (wright2024achromosomalmutation pages 1-2): Rosanna C. T. Wright, A. Jamie Wood, Michael J. Bottery, Katie J. Muddiman, Steve Paterson, Ellie Harrison, Michael A. Brockhurst, and James P. J. Hall. A chromosomal mutation is superior to a plasmid-encoded mutation for plasmid fitness cost compensation. PLOS Biology, 22:e3002926, Dec 2024. URL: https://doi.org/10.1371/journal.pbio.3002926, doi:10.1371/journal.pbio.3002926. This article has 24 citations and is from a highest quality peer-reviewed journal.

8. (jiang2013dealingwiththe pages 1-2): Wenyan Jiang, Inbal Maniv, Fawaz Arain, Yaying Wang, Bruce R. Levin, and Luciano A. Marraffini. Dealing with the evolutionary downside of crispr immunity: bacteria and beneficial plasmids. PLoS Genetics, 9:e1003844, Sep 2013. URL: https://doi.org/10.1371/journal.pgen.1003844, doi:10.1371/journal.pgen.1003844. This article has 304 citations and is from a domain leading peer-reviewed journal.

9. (haudiquet2024capsulesandtheir pages 1-2): Matthieu Haudiquet, Julie Le Bris, Amandine Nucci, Rémy A. Bonnin, Pilar Domingo-Calap, Eduardo P. C. Rocha, and Olaya Rendueles. Capsules and their traits shape phage susceptibility and plasmid conjugation efficiency. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46147-5, doi:10.1038/s41467-024-46147-5. This article has 79 citations and is from a highest quality peer-reviewed journal.

10. (wang2024interplasmidtransferof pages 1-2): Xiaolong Wang, Hanhui Zhang, Shenbo Yu, Donghang Li, Michael R Gillings, Hongqiang Ren, Daqing Mao, Jianhua Guo, and Yi Luo. Inter-plasmid transfer of antibiotic resistance genes accelerates antibiotic resistance in bacterial pathogens. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrad032, doi:10.1093/ismejo/wrad032. This article has 186 citations.

11. (yang2024evolutionoftriclosan pages 1-2): Qiu E. Yang, Xiaodan Ma, Minchun Li, Mengshi Zhao, Lingshuang Zeng, Minzhen He, Hui Deng, Hanpeng Liao, Christopher Rensing, Ville-Petri Friman, Shungui Zhou, and Timothy R. Walsh. Evolution of triclosan resistance modulates bacterial permissiveness to multidrug resistance plasmids and phages. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-48006-9, doi:10.1038/s41467-024-48006-9. This article has 78 citations and is from a highest quality peer-reviewed journal.

12. (mathers2024developingaframework pages 1-2): Amy J. Mathers, Thomas J. X. Li, Qijun He, Sharvari Narendra, Nicole Stoesser, David W. Eyre, A. Sarah Walker, Katie E. Barry, Salvador Castañeda-Barba, Fenix W. Huang, Hardik Parikh, Shireen Kotay, Derrick W. Crook, and Christian Reidys. Developing a framework for tracking antimicrobial resistance gene movement in a persistent environmental reservoir. npj Antimicrobials and Resistance, Dec 2024. URL: https://doi.org/10.1038/s44259-024-00069-w, doi:10.1038/s44259-024-00069-w. This article has 9 citations and is from a peer-reviewed journal.

13. (riva2024conjugalplasmidtransfer pages 1-2): Francesco Riva, Arnaud Dechesne, Ester M. Eckert, Valentina Riva, Sara Borin, Francesca Mapelli, Barth F. Smets, and Elena Crotti. Conjugal plasmid transfer in the plant rhizosphere in the one health context. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1457854, doi:10.3389/fmicb.2024.1457854. This article has 6 citations and is from a peer-reviewed journal.

14. (liu2024compensatoryevolutionof pages 10-11): Ziyi Liu, Qiuyun Zhao, Chenggang Xu, and Houhui Song. Compensatory evolution of chromosomes and plasmids counteracts the plasmid fitness cost. Ecology and Evolution, Aug 2024. URL: https://doi.org/10.1002/ece3.70121, doi:10.1002/ece3.70121. This article has 22 citations and is from a peer-reviewed journal.

15. (wright2024achromosomalmutation pages 14-15): Rosanna C. T. Wright, A. Jamie Wood, Michael J. Bottery, Katie J. Muddiman, Steve Paterson, Ellie Harrison, Michael A. Brockhurst, and James P. J. Hall. A chromosomal mutation is superior to a plasmid-encoded mutation for plasmid fitness cost compensation. PLOS Biology, 22:e3002926, Dec 2024. URL: https://doi.org/10.1371/journal.pbio.3002926, doi:10.1371/journal.pbio.3002926. This article has 24 citations and is from a highest quality peer-reviewed journal.