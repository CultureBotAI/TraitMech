---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:01:25.284029'
end_time: '2026-08-04T02:08:26.088164'
duration_seconds: 420.8
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: non halophilic
  trait_identifier: METPO:1000624
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: non_halophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A halophily preference in which an organism does not require or prefer
    elevated salt concentrations for growth.
  parent_traits: METPO:1000629
  synonyms: non-halophilic
  evidence_summary: 'DOI:10.1128/AEM.01934-12: B. subtilis can attain cellular protection
    (Supports salt-stress protection mechanisms in a non-halophilic bacterial model.)
    | PMID:11583854: Vibrio cholerae non-O1, a non-halophilic bacterium (Organism
    example: Vibrio cholerae non-O1 is described as non-halophilic.)'
  causal_graph_summary: 'non_halophilic_salt_stress_response: 12 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** non halophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000624
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism does not require or prefer elevated salt concentrations for growth.
- **Parent traits:** METPO:1000629
- **Synonyms:** non-halophilic
- **Existing evidence:** DOI:10.1128/AEM.01934-12: B. subtilis can attain cellular protection (Supports salt-stress protection mechanisms in a non-halophilic bacterial model.) | PMID:11583854: Vibrio cholerae non-O1, a non-halophilic bacterium (Organism example: Vibrio cholerae non-O1 is described as non-halophilic.)
- **Existing causal graph summary:** non_halophilic_salt_stress_response: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **non halophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/non_halophilic.yaml`.

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
- **Trait label:** non halophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000624
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism does not require or prefer elevated salt concentrations for growth.
- **Parent traits:** METPO:1000629
- **Synonyms:** non-halophilic
- **Existing evidence:** DOI:10.1128/AEM.01934-12: B. subtilis can attain cellular protection (Supports salt-stress protection mechanisms in a non-halophilic bacterial model.) | PMID:11583854: Vibrio cholerae non-O1, a non-halophilic bacterium (Organism example: Vibrio cholerae non-O1 is described as non-halophilic.)
- **Existing causal graph summary:** non_halophilic_salt_stress_response: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **non halophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/non_halophilic.yaml`.

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


# TraitMech curation report: non-halophilic

## 1. Scope summary

**Trait:** non halophilic  
**Identifier:** **METPO:1000624**  
**Parent:** METPO:1000629  
**Definition supplied:** “A halophily preference in which an organism does not require or prefer elevated salt concentrations for growth.”

This trait should represent an **ecological/growth preference**, not merely survival under salt exposure. A non-halophile grows optimally without elevated salt, although it may possess substantial osmotic-stress defenses. Consequently:

- **Non-halophilic is not equivalent to salt-sensitive.** *Bacillus subtilis* is a non-halophilic model yet uses K⁺ accumulation, compatible-solute synthesis/import, stress-regulated transcription, and mechanosensitive channels to survive osmotic excursions. Reviews distinguish the requirement for salt from tolerance of salt. (hoffmann2016managementofosmotic pages 4-5, bremer2019responsesofmicroorganisms pages 3-5)
- **Halotolerant is a boundary case:** an organism may prefer low salt but tolerate high salt. Such an organism can remain non-halophilic under the supplied definition, provided the growth optimum—not merely the maximum tolerated concentration—is low.
- **Halophilic requires preference or requirement for elevated salt.** Salt-tolerance assays alone cannot establish that classification.
- **Salt stress and osmotic stress overlap but are not identical.** NaCl creates both hyperosmotic stress and ion-specific effects; sucrose or other nonionic osmolytes can test the osmotic component separately. The curated assay context should therefore record solute identity, concentration or water activity, medium, temperature, growth metric, and strain.
- Avoid treating a universal numerical cutoff as definitional unless TraitMech adopts a specific classification authority. Published cutoffs vary with medium and taxonomy; the most defensible annotation is based on a measured growth optimum across a salinity gradient.

## 2. Mechanistic interpretation

Non-halophily is best represented as a **composite phenotype graph** rather than as the output of one dedicated pathway. The central causal model is:

1. Elevated external NaCl increases extracellular osmolality.
2. Water exits the cell, reducing hydration and turgor and increasing macromolecular crowding.
3. A rapid emergency response transiently increases intracellular K⁺.
4. Sustained adaptation replaces excessive inorganic-ion accumulation with compatible solutes synthesized internally or imported from the environment.
5. Upon sudden osmotic downshift, mechanosensitive channels release solutes and reduce lysis risk.
6. These systems permit a non-halophile to tolerate temporary salinity without changing its low-salt growth preference. (hoffmann2016managementofosmotic pages 4-5, bremer2019responsesofmicroorganisms pages 3-5)

This is principally a **salt-out/compatible-solute strategy**, unlike obligate extreme halophiles whose proteomes and physiology can depend on sustained high intracellular salt.

## 3. Candidate nodes

### Trait, taxon, and environmental nodes

| Node | Suggested grounding | Curation note |
|---|---|---|
| non-halophilic | **METPO:1000624** | Target trait; preserve identifier verbatim. |
| *Bacillus subtilis* | **NCBITaxon:1423** | Strong model taxon, but strain should be recorded for gene/protein grounding. |
| elevated extracellular NaCl | **CHEBI:26710** | Environmental perturbation; attach concentration and medium to evidence. |
| hyperosmotic stress | **GO:0006970** for response to osmotic stress | GO term represents biological response, not the environmental condition itself. |
| osmotic upshift | Label-only candidate | Experimental process/event. |
| osmotic downshift | Label-only candidate | Distinct event activating mechanosensitive release. |
| low-salt growth optimum | Label-only candidate | Proximal assay phenotype establishing non-halophily. |

### Chemicals and physiological state nodes

| Node | Suggested grounding | Role |
|---|---|---|
| water | CHEBI identifier should be registry-validated during YAML preparation | Efflux during hyperosmotic shock; influx during downshift. |
| potassium ion | **CHEBI:29103** | Rapid emergency osmolyte/ion-homeostasis response. |
| L-proline | **CHEBI:26271** | Major synthesized/imported compatible solute in *B. subtilis*. |
| glycine betaine | **CHEBI:17750** | Imported compatible solute. |
| dimethylglycine | Label-only pending identifier validation | Imported stress protectant examined experimentally in *B. subtilis*. |
| cytoplasmic hydration | Label-only candidate | Falls after osmotic upshift. |
| turgor pressure | Label-only candidate | Perturbed by water flux; essential for growth. |
| macromolecular crowding | Label-only candidate | Increases following water loss. |
| intracellular compatible-solute pool | Label-only candidate | Mechanistically closer to protection than external solute concentration. |
| osmotic-stress tolerance | GO process can be linked through GO:0006970 | Distinguish from halophilic preference. |

### Genes, proteins, transporters, and pathways

| Node | Type | Proposed role | Grounding caution |
|---|---|---|---|
| ProJ–ProA–ProH pathway | Metabolic module | Osmoadaptive proline synthesis | Keep as a pathway/module or ground each strain-specific protein after UniProt verification. |
| **proJ, proA, proH** | Genes | Encode osmoadaptive proline-biosynthetic route | Gene labels are taxon-specific; do not assign generic UniProt IDs. |
| OpuE | Transporter | Proline uptake; osmotically regulated | Direct primary source should be attached before asserting exact regulatory architecture. |
| OpuA | ABC transporter system | Glycine-betaine/compatible-solute import | Substrate scope and subunits require strain-specific validation. |
| OpuC | ABC transporter system | Broad compatible-solute uptake | Candidate node; do not infer every substrate. |
| OpuD | Transporter | Glycine-betaine uptake | Supported through the primary-literature chain summarized by Bashir et al. (bashir2014dimethylglycineprovidessalt pages 11-12) |
| BusR | Transcriptional repressor | Ionic-strength-responsive control associated with opuA | Review-supported; primary regulatory evidence preferred. |
| SigA and SigB | Sigma factors | Components of opuE transcriptional control | Context-dependent; avoid encoding SigB as the sole regulator. |
| MscL, MscS-family proteins, YkuT | Mechanosensitive channels | Solute release during hypoosmotic downshift | Separate gene expression under upshift from channel opening under downshift. |
| AhrC | Transcriptional regulator | Suppressor mutations redirect arginine metabolism | Evolved-mutant-specific mechanism. |
| RocR/RocD/RocDEF | Regulator/enzyme/operon | Redirect ornithine metabolism toward a proline precursor | Suppressor-background evidence only. |
| argCJBD-carAB-argF | Biosynthetic operon/module | Increased arginine/ornithine pathway flux in suppressors | Do not generalize beyond the experimental suppressors. |

## 4. Candidate causal edges

The compact curation matrix below separates direct primary evidence from review-derived mechanisms.

| Triple | Evidence strength | Taxon | Reference DOI | Caveat |
|---|---|---|---|---|
| hyperosmotic/salt shock -> causes -> water efflux and increased cytoplasmic crowding (hoffmann2016managementofosmotic pages 4-5, bremer2019responsesofmicroorganisms pages 3-5) | Strong review-backed | *Bacillus subtilis* / non-halophilic bacteria generally | 10.1002/9781119004813.ch63; 10.1146/annurev-micro-020518-115504 | Mechanism is broadly established, but gathered evidence here is mainly review synthesis rather than a single primary experiment. |
| transient intracellular K+ increase -> limits -> water loss during early osmotic upshift (hoffmann2016managementofosmotic pages 4-5, bremer2019responsesofmicroorganisms pages 3-5) | Moderate | *Bacillus subtilis* / non-halophilic bacteria generally | 10.1002/9781119004813.ch63; 10.1146/annurev-micro-020518-115504 | Emergency-response framing is well supported in reviews; exact transporters/quantitation were not extracted in the gathered evidence. |
| compatible-solute synthesis or import -> enables -> sustained osmoadaptation under high salinity/osmolarity (bremer2019responsesofmicroorganisms pages 3-5, bashir2014dimethylglycineprovidessalt pages 11-12) | Strong | non-halophilic bacteria, including *Bacillus subtilis* | 10.1146/annurev-micro-020518-115504; 10.1128/AEM.00078-14 | General principle is strong; specific solute/species dependence should be curated taxon-by-taxon. |
| disruption of ProJ-ProA-ProH proline biosynthesis -> causes -> osmotic sensitivity (stecker2022lprolinesynthesismutants pages 8-9) | Strong primary | *Bacillus subtilis* | 10.3389/fmicb.2022.908304 | Specific to *B. subtilis* proline-biosynthesis mutants; not a universal rule for all non-halophiles. |
| altered arginine/ornithine metabolism (suppressor adaptation) -> restores -> osmostress tolerance at 0.8 M NaCl despite defective proline synthesis (stecker2022lprolinesynthesismutants pages 8-9) | Strong primary | *Bacillus subtilis* | 10.3389/fmicb.2022.908304 | Rescue occurs in evolved/suppressor backgrounds and is not a baseline trait mechanism for all strains. |
| high osmolarity -> regulates -> opuE expression (hoffmann2016managementofosmotic pages 4-5, bashir2014dimethylglycineprovidessalt pages 11-12) | Moderate | *Bacillus subtilis* | 10.1002/9781119004813.ch63; 10.1128/AEM.00078-14 | Evidence in gathered context includes review summary and citation trail; direct assay details were not fully extracted here. |
| high osmolarity / ionic strength -> regulates -> opuA operon expression (hoffmann2016managementofosmotic pages 4-5, bremer2019responsesofmicroorganisms pages 3-5) | Moderate | *Bacillus subtilis* | 10.1002/9781119004813.ch63; 10.1146/annurev-micro-020518-115504 | Regulatory details involve BusR according to gathered reviews, but exact primary experimental conditions were not captured. |
| OpuD / Opu-family transporters -> mediate uptake of -> glycine betaine and other compatible solutes (bashir2014dimethylglycineprovidessalt pages 11-12) | Moderate | *Bacillus subtilis* | 10.1128/AEM.00078-14 | Gathered evidence supports transporter role through cited primary literature, but substrate specificity by individual transporter should be checked before hard curation. |
| mechanosensitive channels (MscL, MscS-family, YkuT) -> mediate release of -> ions/organic solutes during osmotic downshift (hoffmann2016managementofosmotic pages 4-5) | Moderate | *Bacillus subtilis* | 10.1002/9781119004813.ch63 | Downshift-release role is summarized in review context; direct primary citations should be added before final TraitMech curation. |


*Table: This table compiles compact, curation-oriented causal edges relevant to METPO:1000624 using only the gathered evidence. It highlights which edges are directly supported versus review-derived and flags where taxon specificity or missing primary details warrant caution.*

### Additional evidence notes and usable snippets

1. **Proline synthesis is causally required for normal osmotic resistance in *B. subtilis*.** Stecker et al. state that proline accumulation through synthesis is a “cornerstone” of defense and that genetic disruption causes osmotic sensitivity. This supports `ProJ–ProA–ProH pathway —positively_regulates→ osmotic-stress tolerance` and `pathway disruption —causes→ osmotic sensitivity`. (stecker2022lprolinesynthesismutants pages 8-9)

2. **Alternative metabolism can rescue a proline-defective mutant.** First-generation suppressors involving `rocDEF` or RocR were still inadequate at **0.8 M NaCl**, whereas second-generation suppressors selected on 0.8 M NaCl regained tolerance. The paper attributes rescue to repurposed arginine/ornithine metabolism feeding γ-glutamate-semialdehyde/Δ¹-pyrroline-5-carboxylate into proline synthesis. This is strong causal evidence, but only for evolved mutant backgrounds. (stecker2022lprolinesynthesismutants pages 8-9)

3. **Compatible solutes mediate sustained adaptation.** The authoritative synthesis by Bremer and Krämer describes transient K⁺ accumulation as an emergency response and compatible-solute synthesis/import as the sustained salt-out response. Relevant solutes include proline, glycine betaine, and carnitine. (bremer2019responsesofmicroorganisms pages 3-5)

4. **Opu transport systems are experimentally linked to solute uptake.** The Bashir et al. primary paper and its cited experimental literature identify OpuD with glycine-betaine uptake, OpuE with high-osmolarity-regulated proline uptake, and Opu-family systems with compatible-solute transport. Because the retrieved excerpt contains part of the citation trail rather than all underlying assays, exact transporter–substrate edges should be checked in the original primary articles before release. (bashir2014dimethylglycineprovidessalt pages 11-12)

5. **Biophysical edges are appropriate graph components.** Salt shock causes water efflux, increased cytoplasmic solute concentration, and crowding; transient K⁺ changes and compatible-solute accumulation counter these effects. These edges are strongly accepted but currently supported here by reviews rather than one defining mutant experiment. (hoffmann2016managementofosmotic pages 4-5, bremer2019responsesofmicroorganisms pages 3-5)

## 5. Recommended minimal graph for initial curation

A conservative initial graph could contain the following 12 nodes:

1. **METPO:1000624** non-halophilic
2. elevated extracellular NaCl
3. increased extracellular osmolality
4. water efflux
5. reduced cytoplasmic hydration/increased crowding
6. transient intracellular K⁺ accumulation
7. ProJ–ProA–ProH pathway
8. intracellular proline pool
9. Opu compatible-solute uptake systems
10. intracellular glycine-betaine/compatible-solute pool
11. restored turgor and hydration
12. growth under transient salt stress

Recommended core edges are:

- elevated extracellular NaCl → increases → extracellular osmolality
- increased extracellular osmolality → causes → water efflux
- water efflux → decreases → cytoplasmic hydration
- water efflux → increases → macromolecular crowding
- osmotic upshift → causes → transient K⁺ accumulation
- ProJ–ProA–ProH pathway → produces → proline
- Opu systems → import → compatible solutes
- intracellular compatible-solute pool → promotes → osmotic adjustment
- osmotic adjustment → restores → hydration/turgor
- restored hydration/turgor → enables → growth during salt exposure
- growth optimum remaining at low salt → supports classification as → **METPO:1000624**

The last edge is an **assay-to-trait evidence edge**, not a biochemical causal edge. It should be represented distinctly if the schema supports evidence or phenotype-observation relations.

## 6. Recent developments and applications

The strongest directly relevant recent mechanistic paper retrieved was the 2022 suppressor-evolution study, which demonstrates metabolic plasticity: defects in canonical proline synthesis can be bypassed by regulatory changes linking arginine synthesis, ornithine degradation, and the terminal proline-biosynthetic step. This argues against encoding non-halophilic osmoadaptation as a rigid linear pathway. (stecker2022lprolinesynthesismutants pages 8-9)

Research published in 2023–2024 increasingly uses compatible-solute pathways for metabolic engineering, including ectoine, proline, and GABA production, and examines hybrid salt-in/salt-out strategies. However, much of this work uses *Halomonas* or extreme halophiles. It is valuable for selecting candidate mechanisms and biotechnology applications but should **not** be used as direct evidence for **METPO:1000624** without an independent low-salt growth-optimum assay.

Current application areas include:

- engineering non-halophilic hosts to produce compatible solutes such as ectoine;
- improving fermentation robustness under osmotic stress;
- designing salt-resilient microbial cell factories;
- deploying plant-growth-promoting bacteria in saline agriculture;
- interpreting microbial community transitions along salinity gradients.

These applications exploit **salt tolerance**, not necessarily non-halophilic preference. The distinction should remain explicit in TraitMech.

## 7. Curation warnings

1. **Do not curate “tolerates X% NaCl” as proof of non-halophily.** Maximum tolerated salinity does not identify the growth optimum.
2. **Do not infer non-halophily from taxonomy alone.** Phenotypes vary by species and strain.
3. **Do not import edges from *Halomonas elongata*, *Natranaerobius thermophilus*, or haloarchaea as direct evidence.** Those organisms are halophilic and their salt-dependent proteomes can differ fundamentally.
4. **Do not equate salt stress with generic osmotic stress.** Record whether NaCl, KCl, sucrose, or another agent was used.
5. **Do not make Opu substrate specificity broader than the assay demonstrates.** Individual Opu systems overlap but are not interchangeable.
6. **Do not encode suppressor mutations as the wild-type pathway.** AhrC/RocR/RocD/arginine-pathway rescue is an evolved, mutant-specific bypass.
7. **Do not assign strain-independent UniProt identifiers.** Resolve the exact *B. subtilis* strain and protein accession first.
8. **Treat mechanosensitive-channel edges carefully.** Osmotic upshift can regulate channel genes, whereas channel opening and solute release principally protect during downshift.
9. **The supplied *Vibrio cholerae* non-O1 evidence is organism-description evidence, not a mechanistic edge.** Retain it as trait occurrence unless full growth-optimum data and mechanism are recovered.
10. **The 2023–2024 literature retrieved is primarily comparative/application-oriented.** It should inform interpretation but not replace direct phenotype and mutant evidence in the target taxon.

## 8. DOI-first bibliography

1. Stecker D, Hoffmann T, Link H, Commichau FM, Bremer E. **L-Proline Synthesis Mutants of *Bacillus subtilis* Overcome Osmotic Sensitivity by Genetically Adapting L-Arginine Metabolism.** *Frontiers in Microbiology*. Published June 2022. DOI: [10.3389/fmicb.2022.908304](https://doi.org/10.3389/fmicb.2022.908304). Primary genetic, selection, protection-assay, and metabolomic evidence. (stecker2022lprolinesynthesismutants pages 8-9)

2. Bashir A, Hoffmann T, Smits SHJ, Bremer E. **Dimethylglycine Provides Salt and Temperature Stress Protection to *Bacillus subtilis*.** *Applied and Environmental Microbiology*. Published May 2014;80:2773–2785. DOI: [10.1128/AEM.00078-14](https://doi.org/10.1128/AEM.00078-14). Primary compatible-solute study and transporter evidence trail. (bashir2014dimethylglycineprovidessalt pages 11-12)

3. Bremer E, Krämer R. **Responses of Microorganisms to Osmotic Stress.** *Annual Review of Microbiology*. Published September 2019;73:313–334. DOI: [10.1146/annurev-micro-020518-115504](https://doi.org/10.1146/annurev-micro-020518-115504). Authoritative mechanistic review of water flux, K⁺ response, compatible solutes, turgor, and osmotic regulation. (bremer2019responsesofmicroorganisms pages 3-5)

4. Hoffmann T, Bremer E. **Management of Osmotic Stress by *Bacillus subtilis*: Genetics and Physiology.** Published August 2016, pp. 657–676. DOI: [10.1002/9781119004813.ch63](https://doi.org/10.1002/9781119004813.ch63). Detailed model-organism synthesis covering Opu systems, regulation, K⁺, and mechanosensitive channels. (hoffmann2016managementofosmotic pages 4-5)

5. Hoffmann T et al. **Osmotic Control of opuA Expression in *Bacillus subtilis* and Its Modulation in Response to Intracellular Glycine Betaine and Proline Pools.** *Journal of Bacteriology*. Published 2013;195:510–522. DOI: [10.1128/JB.01505-12](https://doi.org/10.1128/JB.01505-12). Relevant primary source for future direct verification of the opuA regulatory edge.

## Curation recommendation

**Proceed with curation**, but frame the graph as a *B. subtilis-centered mechanism enabling a non-halophilic organism to withstand transient salt stress*, not as a universal molecular definition of non-halophily. The highest-confidence direct edges are the dependence of osmotic resistance on ProJ–ProA–ProH-mediated proline synthesis and the evolved metabolic rescue demonstrated at **0.8 M NaCl**. Biophysical, K⁺, Opu, and mechanosensitive-channel edges are appropriate but should retain review-derived or verification-needed qualifiers until their original primary experiments are attached. (hoffmann2016managementofosmotic pages 4-5, bremer2019responsesofmicroorganisms pages 3-5, bashir2014dimethylglycineprovidessalt pages 11-12, stecker2022lprolinesynthesismutants pages 8-9)

References

1. (hoffmann2016managementofosmotic pages 4-5): Tamara Hoffmann and Erhard Bremer. Management of osmotic stress by bacillus subtilis: genetics and physiology. ArXiv, pages 657-676, Aug 2016. URL: https://doi.org/10.1002/9781119004813.ch63, doi:10.1002/9781119004813.ch63. This article has 53 citations.

2. (bremer2019responsesofmicroorganisms pages 3-5): Erhard Bremer and Reinhard Krämer. Responses of microorganisms to osmotic stress. Annual review of microbiology, 73:313-334, Sep 2019. URL: https://doi.org/10.1146/annurev-micro-020518-115504, doi:10.1146/annurev-micro-020518-115504. This article has 531 citations and is from a peer-reviewed journal.

3. (bashir2014dimethylglycineprovidessalt pages 11-12): Abdallah Bashir, Tamara Hoffmann, Sander H. J. Smits, and Erhard Bremer. Dimethylglycine provides salt and temperature stress protection to bacillus subtilis. Applied and Environmental Microbiology, 80:2773-2785, May 2014. URL: https://doi.org/10.1128/aem.00078-14, doi:10.1128/aem.00078-14. This article has 54 citations and is from a peer-reviewed journal.

4. (stecker2022lprolinesynthesismutants pages 8-9): Daniela Stecker, Tamara Hoffmann, Hannes Link, Fabian M. Commichau, and Erhard Bremer. L-proline synthesis mutants of bacillus subtilis overcome osmotic sensitivity by genetically adapting l-arginine metabolism. Frontiers in Microbiology, Jun 2022. URL: https://doi.org/10.3389/fmicb.2022.908304, doi:10.3389/fmicb.2022.908304. This article has 28 citations and is from a peer-reviewed journal.