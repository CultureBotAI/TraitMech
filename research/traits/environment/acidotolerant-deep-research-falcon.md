---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:51:37.134806'
end_time: '2026-08-04T00:00:12.633084'
duration_seconds: 515.5
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: acidotolerant
  trait_identifier: METPO:1003008
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: acidotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference characterized by the ability to tolerate acidic
    environments (typically pH below 5.5) while maintaining optimal growth near neutral
    pH.
  parent_traits: METPO:1003000
  synonyms: aciduric
  evidence_summary: 'DOI:10.1038/nrmicro2549: tolerate and grow at external pH values
    (Supports acidotolerance as growth or survival under otherwise stressful external
    pH conditions.)'
  causal_graph_summary: 'acidotolerant_acid_stress_homeostasis: 9 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** acidotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003008
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by the ability to tolerate acidic environments (typically pH below 5.5) while maintaining optimal growth near neutral pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** aciduric
- **Existing evidence:** DOI:10.1038/nrmicro2549: tolerate and grow at external pH values (Supports acidotolerance as growth or survival under otherwise stressful external pH conditions.)
- **Existing causal graph summary:** acidotolerant_acid_stress_homeostasis: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **acidotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/acidotolerant.yaml`.

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
- **Trait label:** acidotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003008
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by the ability to tolerate acidic environments (typically pH below 5.5) while maintaining optimal growth near neutral pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** aciduric
- **Existing evidence:** DOI:10.1038/nrmicro2549: tolerate and grow at external pH values (Supports acidotolerance as growth or survival under otherwise stressful external pH conditions.)
- **Existing causal graph summary:** acidotolerant_acid_stress_homeostasis: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **acidotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/acidotolerant.yaml`.

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


# Curation-focused research report: microbial acidotolerance

## Executive summary

**Target:** `METPO:1003008` — **acidotolerant** (synonym: *aciduric*); category **ENVIRONMENT**; term kind **CLASS**; mapping **REVIEWED**; parent `METPO:1003000`.

For TraitMech, the safest interpretation is: **a microorganism whose growth optimum is near neutral pH but that can maintain growth at acidic external pH, commonly below approximately 5.5**. This is a growth-preference/capacity phenotype, not merely survival after a short lethal challenge. Neutralophilic bacteria generally keep cytoplasmic pH near 7.2–7.8 over an external range near pH 5.5–9.0; acidotolerance extends function toward the acidic edge by limiting proton entry, exporting or consuming protons, producing alkali, and repairing acid damage (rebelo2023unravelingtherole pages 18-20).

The strongest generic graph backbone is:

**low external pH / membrane-permeant weak acid → increased cytoplasmic proton load → pH-homeostasis modules (proton extrusion, proton-consuming decarboxylation, ammonia production, membrane remodeling) → maintained intracellular pH → growth or survival under acid stress.** Weak organic acids deserve an explicit branch because their undissociated forms cross membranes and then dissociate in the cytoplasm, imposing both proton and anion stress (lund2014copingwithlow pages 1-2).

Recent work emphasizes that “acid tolerance” is not one conserved pathway. A 2023 *E. coli* Ribo-seq/RNA-seq study found sharply condition-dependent responses at pH 5.8 versus 4.4 and 18 previously unannotated acid-induced small ORFs; a 2023 *Alicyclobacillus* study connected acid response to amino-acid metabolism, urea hydrolysis, energy supply and lipid remodeling; and a 2024 *Salmonella* knockout study showed that PhoP/PhoQ chiefly affected acid-induced cross-protection rather than being indispensable for acid tolerance itself (liu2023molecularmechanismof pages 12-15, gao2024theeffectof pages 13-14, schumacher2023ribosomeprofilingreveals pages 21-23, schumacher2023ribosomeprofilingreveals pages 1-2).

## 1. Trait scope and boundaries

### In scope

1. **Growth under acidic conditions:** demonstrated biomass increase, colony formation, growth rate or yield below the organism’s optimal pH.
2. **Maintenance of physiological function at low pH:** intracellular-pH regulation, ATP generation, membrane integrity and macromolecular function causally linked to growth.
3. **Acid survival as a supporting assay:** survival after a defined low-pH exposure can support a mechanism, but should not by itself establish the growth-preference trait.
4. **Constitutive or inducible mechanisms:** both may contribute, provided the terminal graph phenotype is acid growth/tolerance rather than only expression induction.

### Nearby traits that should remain distinct

- **Acidophile:** optimal growth occurs at acidic pH. Acidotolerant organisms retain an optimum closer to neutral. Therefore, *Alicyclobacillus acidoterrestris*, described as strongly acidophilic, is mechanistically informative but not an ideal taxonomic exemplar of this METPO class.
- **Acid resistance:** often operationally means survival of a severe, short challenge—such as pH 2–3—without requiring growth.
- **Acid-tolerance response/adaptation:** increased resistance following prior exposure to a milder acidic condition. This is a regulated state transition, not identical to the baseline trait.
- **Organic-acid tolerance:** overlaps with acidotolerance but adds acid-specific anion toxicity and depends on acid pKa, concentration and lipophilicity; equal extracellular pH values are not equivalent exposures (lund2014copingwithlow pages 1-2).
- **Acid production:** production of lactic, acetic or other acids does not prove tolerance to the resulting pH.
- **Gastric survival, biofilm formation or cross-protection:** useful application phenotypes, but not synonyms for acidotolerant.

**Recommended phenotype endpoint:** `maintained microbial growth under external pH <5.5 relative to a near-neutral control`, annotated with medium, buffering capacity, acidulant, temperature, oxygen, growth phase and exposure duration. A binary acidotolerant call should not be inferred solely from gene presence.

## 2. Candidate nodes, grouped by type

### Trait and phenotype nodes

- acidotolerant — `METPO:1003008`
- growth under acidic conditions — label-only pending METPO alignment
- acid survival — label-only; supporting phenotype, not equivalent to the trait
- acid-tolerance response — label-only regulated process
- intracellular-pH homeostasis — candidate process node; validate the current GO identifier before YAML insertion
- acid-induced cross-protection — label-only and preferably a separate subgraph

### Environmental and experimental nodes

- acidic environment / low external pH
- extracellular proton activity; proton — candidate `CHEBI:15378`
- weak organic acid, undissociated weak organic acid and conjugate-base anion
- acetic acid — candidate `CHEBI:15366`
- lactic acid — use the stereochemically appropriate ChEBI term after checking the assay
- benzoic, sorbic and propionic acids as acid-specific challenge nodes
- mild acid adaptation versus severe acid challenge
- pH, exposure time, acidulant, buffer capacity and growth phase as experimental-factor nodes

### Compartments and structures

- extracellular space
- cytoplasm/cytosol — candidate `GO:0005737`
- plasma membrane — candidate `GO:0005886`
- periplasmic space — candidate `GO:0042597`, Gram-negative only
- outer membrane and lipopolysaccharide, Gram-negative only
- peptidoglycan/cell wall
- biofilm matrix — contextual rather than a universal core node

### Transport and bioenergetic modules

- F-type H+-transporting ATPase/F1F0-ATPase
- proton transmembrane transport — candidate `GO:1902600`
- Na+/H+ antiporter NhaB; NhaA as a separate, pH-dependent paralog
- porins OmpC/OmpF, which can affect amino-acid entry in *E. coli*
- ATP and proton-motive force

### Amino-acid-dependent acid-resistance modules

- **Gad system:** GadA/GadB glutamate decarboxylase and GadC glutamate/GABA antiporter
- glutamate; γ-aminobutyrate/GABA
- **Adi system:** AdiA arginine decarboxylase and AdiC arginine/agmatine antiporter
- arginine; agmatine
- **Cad system:** CadA lysine decarboxylase and CadB lysine/cadaverine antiporter
- lysine; cadaverine
- ornithine decarboxylase system where experimentally supported
- pyridoxal 5′-phosphate as the decarboxylase cofactor

These systems couple import of a substrate to intracellular decarboxylation that consumes a proton and export of the product. *E. coli* has four canonical amino-acid decarboxylase systems—Gad, Adi, Cad and Orn—but their presence and dominance are taxon- and condition-specific (schumacher2023ribosomeprofilingreveals pages 1-2).

### Alkali-generating metabolic modules

- arginine deiminase pathway
- urease complex
- urea
- ammonia/ammonium
- arginine metabolism and associated ATP production

The immediate chemistry should be represented carefully: ammonia can accept a proton to form ammonium, thereby buffering cytoplasmic acidification. ADI and urease occur only in subsets of organisms and should never be inferred from the acidotolerant phenotype alone (liu2023molecularmechanismof pages 9-12, lund2014copingwithlow pages 6-6).

### Envelope and repair modules

- saturated/unsaturated-fatty-acid ratio
- cyclopropane fatty-acid synthesis
- membrane proton permeability
- LPS charge modification, Gram-negative only
- HdeA and HdeB periplasmic acid chaperones; HdeA is most active around pH 1–3 and HdeB around pH 3–5 in *E. coli*
- DnaK, GroEL/GroES, DegP and Clp proteostasis systems
- DNA depurination and strand breaks
- RecA, nucleotide-excision, mismatch and base-excision repair processes

Recent *A. acidoterrestris* proteomics reported 1.54-fold and 1.81-fold increases in TesA and YciA, respectively, alongside enrichment of unsaturated-fatty-acid biosynthesis; this is useful evidence for a membrane-remodeling branch but remains species- and assay-specific (pH 2.5, 15 min) (liu2023molecularmechanismof pages 12-15).

### Sensors and regulators

- YdeO, GadE, GadX and GadW in enteric Gad regulation
- MhpR and IscR as recent *E. coli* candidates
- PhoP/PhoQ in *Salmonella* acid-induced multistress adaptation
- OmpR/EnvZ
- RpoS/general stress response
- DsrA–Hfq post-transcriptional regulation
- acid-induced small ORFs: candidate nodes only, not yet graph-ready

## 3. Candidate evidence-backed causal edges

| Proposed subject–predicate–object triple | Reference and supporting snippet | Evidence and curation note |
|---|---|---|
| low external pH → increases → inward proton pressure/cytoplasmic acidification | Lund et al., DOI **10.1111/1574-6976.12076**: acidic niches range from pH 5–6 to stomach pH 1.5–3.5; neutralophiles must cope with the resulting proton stress (lund2014copingwithlow pages 1-2). | **High confidence, generic process.** Phrase as physicochemical pressure, not guaranteed cytoplasmic collapse. |
| undissociated weak organic acid → crosses → plasma membrane | Same review: weak acids are effective at low pH because they enter in unionized form (lund2014copingwithlow pages 1-2). | **High confidence.** Acid identity, pKa and membrane permeability must be recorded. |
| intracellular weak-acid dissociation → increases → cytoplasmic proton load | “Subsequently dissociating and lowering intracellular pH” (lund2014copingwithlow pages 1-2). | **High confidence.** Also creates an anion burden; do not model the effect as proton-only. |
| cytoplasmic pH homeostasis → enables → microbial growth under acidic conditions | Neutralophiles maintain cytoplasmic pH near 7.2–7.8 despite external pH around 5.5–9.0 (rebelo2023unravelingtherole pages 18-20). | **High-confidence conceptual edge.** This is the preferred terminal mechanism-to-trait edge. |
| F1F0-ATPase → exports → cytoplasmic protons | Recent synthesis lists the F1–F0 ATPase proton pump among active acid-tolerance mechanisms (rebelo2023unravelingtherole pages 18-20). | **High confidence but context-dependent.** Verify organism-specific direction and energetic state before gene-level curation. |
| GadA/GadB glutamate decarboxylase → consumes → cytoplasmic proton | The GDAR system converts glutamate to GABA and provides robust protection from extreme acid stress (rebelo2023unravelingtherole pages 18-20). | **High confidence; enteric and selected Gram-positive taxa.** Curate the enzyme reaction separately from its phenotype effect. |
| GadC antiporter → imports glutamate and exports GABA → sustains Gad proton-consumption cycle | GadA/B act with the GadC antiporter (rebelo2023unravelingtherole pages 18-20). | **High confidence, taxon-limited.** Avoid asserting universal occurrence. |
| Gad cycle → increases → intracellular-pH homeostasis/acid survival | Recent *E. coli* profiling retained Gad as a major pH-dependent defense system (schumacher2023ribosomeprofilingreveals pages 21-23, schumacher2023ribosomeprofilingreveals pages 1-2). | **High confidence in *E. coli*.** Survival evidence is stronger than continuous-growth evidence. |
| AdiA arginine decarboxylase → consumes → cytoplasmic proton | ADAR is identified as an arginine-dependent neutralization system (rebelo2023unravelingtherole pages 18-20, schumacher2023ribosomeprofilingreveals pages 1-2). | **High confidence for enterics.** |
| AdiC antiporter → sustains → arginine/agmatine decarboxylase cycle | The Adi system consists of a proton-consuming enzyme and antiporter (schumacher2023ribosomeprofilingreveals pages 1-2). | **High confidence at module level.** Reaction stoichiometry should be checked against Rhea before YAML entry. |
| CadA/CadB lysine decarboxylase cycle → increases → acid survival | LDAR is reported alongside GDAR and ADAR (rebelo2023unravelingtherole pages 18-20, schumacher2023ribosomeprofilingreveals pages 1-2). | **Medium-high confidence, enteric-specific.** |
| arginine deiminase pathway → produces → ammonia | ADI-mediated ammonia generation is described as an acid-neutralizing route (liu2023molecularmechanismof pages 9-12, lund2014copingwithlow pages 6-6). | **High biochemical confidence; distribution limited.** |
| urease → hydrolyzes urea to produce → ammonia | Urea hydrolysis is reported as part of intracellular-pH maintenance in *A. acidoterrestris* and established acid-defense literature (liu2023molecularmechanismof pages 9-12, lund2014copingwithlow pages 6-6). | **High biochemical confidence, taxon-specific.** |
| ammonia + cytoplasmic proton → forms ammonium and increases → intracellular pH | “NH3 combining with cytoplasmic protons to raise internal pH” (liu2023molecularmechanismof pages 9-12). | **High chemical plausibility; mechanism-level edge.** |
| increased unsaturated/cyclopropane membrane lipids → decreases → proton permeability | Recent *E. coli* review and *Alicyclobacillus* proteomics connect lipid remodeling with reduced permeability and pH maintenance (liu2023molecularmechanismof pages 12-15, li2024responseofescherichia pages 5-7). | **Medium-high confidence at process level.** Exact lipid change can differ among taxa; avoid one universal direction for saturation ratio. |
| HdeA/HdeB → protects → periplasmic proteins during acid stress | HdeA is active at pH 1–3 and HdeB at pH 3–5 and functions without ATP (li2024responseofescherichia pages 5-7). | **High confidence in Gram-negative enterics.** Not applicable to organisms lacking a periplasm. |
| cytoplasmic acidification → causes → DNA depurination/strand damage | Acid-induced protonation, depurination and DNA damage are described across reviews and recent studies (liu2023molecularmechanismof pages 12-15, li2024responseofescherichia pages 5-7, lund2014copingwithlow pages 6-6). | **High confidence.** |
| DNA-repair processes → mitigate → acid-induced DNA damage | NER, MMR, BER and RecA pathways are implicated (li2024responseofescherichia pages 5-7, lund2014copingwithlow pages 6-6). | **Medium confidence as a generic process.** Avoid specific gene edges without perturbation data. |
| YdeO → coordinates/activates → Gad and Adi systems | 2023 *E. coli* Ribo-seq/RNA-seq analysis reports coordinated regulation of both systems by YdeO (schumacher2023ribosomeprofilingreveals pages 21-23). | **Medium-high confidence, *E. coli*-specific.** Regulatory analysis, not a universal bacterial edge. |
| pH 5.8 or pH 4.4 acute exposure → differentially regulates → acid-defense programs | *E. coli* K-12 was shifted from pH 7.6 to pH 5.8 or 4.4 and sampled after 15 min; responses included 18 novel acid-induced sORFs (schumacher2023ribosomeprofilingreveals pages 21-23, schumacher2023ribosomeprofilingreveals pages 1-2). | **Strong condition-response evidence, not yet mechanism for novel genes.** Curate the exposure edge; defer sORF causal edges. |
| NhaB upregulation → associates with → acid adaptation | *A. acidoterrestris* NhaB was rapidly upregulated within 15 min at pH 2.5 (liu2023molecularmechanismof pages 9-12). | **Uncertain.** Omics association from an acidophilic organism; not direct transport or knockout evidence. |
| mild-acid adaptation → increases → subsequent lethal-acid, heat and osmotic survival | *S. Typhimurium* adapted at pH 5.4 for 90 min gained resistance to lethal acid, 55 °C heat and 8% hypertonic stress (gao2024theeffectof pages 13-14). | **High confidence for cross-protection, not baseline acidotolerance.** Keep in a separate adaptation subgraph. |
| PhoP deletion → decreases → acid-induced heat/CAMP cross-protection | ΔphoP reduced heat tolerance and increased polymyxin-B sensitivity after adaptation, but acid tolerance persisted (gao2024theeffectof pages 13-14). | **Direct knockout evidence. Do not curate PhoP/PhoQ as necessary for acidotolerance.** |
| engineered quorum-sensing DsrA–Hfq circuit → increases → low-pH growth/productivity robustness | Industrial *E. coli* achieved comparable lysine productivity and higher yield at pH 5.5 relative to the parent operated at pH 6.8 (DOI **10.1186/s12934-024-02524-9**) (yan2024engineeringquorumsensingbased pages 10-10). | **Application evidence only.** Put in an engineering extension, not the native causal graph. |

A concise prioritization matrix is provided below.

| priority | causal module | representative subject-predicate-object edge | strongest evidence type | taxon/assay scope | curation decision |
|---|---|---|---|---|---|
| High | Weak-acid proton loading | weak organic acid --causes--> cytoplasmic acidification | Core review synthesis on neutralophiles under low pH; mechanism is chemically general (lund2014copingwithlow pages 1-2) | Broad bacterial scope; especially relevant when external pH is below organic-acid pKa and acids are membrane permeable | Curate as core generic edge |
| High | F1F0 ATPase proton extrusion | F-type H+-transporting ATPase --exports--> proton | Repeated foundational review support across bacteria; recent reviews retain it as a canonical acid-homeostasis module (rebelo2023unravelingtherole pages 18-20, lund2014copingwithlow pages 1-2, li2024responseofescherichia pages 5-7) | Broad but directionality and net effect can vary by taxon/energetic state | Curate as core generic edge, with note that activity is context-dependent |
| High | Glutamate decarboxylase cycle | glutamate decarboxylase system (GadA/GadB + GadC) --increases--> intracellular pH homeostasis | Strong biochemical/review consensus; recent E. coli profiling confirms Gad system prominence under acid stress (rebelo2023unravelingtherole pages 18-20, schumacher2023ribosomeprofilingreveals pages 21-23, schumacher2023ribosomeprofilingreveals pages 1-2) | Best supported in enteric bacteria; also reported in some Gram-positives | Curate as core but gene-level instantiation should be taxon-specific |
| High | Arginine decarboxylase cycle | arginine decarboxylase system (AdiA + AdiC) --increases--> acid survival/homeostasis | Strong review support plus recent transcriptional evidence in E. coli/Salmonella contexts (rebelo2023unravelingtherole pages 18-20, gao2024theeffectof pages 13-14, schumacher2023ribosomeprofilingreveals pages 1-2) | Enteric/pathogen-enriched; not universal | Curate as common but not universal module |
| Medium | Lysine decarboxylase cycle | lysine decarboxylase system (CadA + CadB) --increases--> acid survival/homeostasis | Review-backed; recent E. coli overview keeps Cad among canonical AR systems (rebelo2023unravelingtherole pages 18-20, schumacher2023ribosomeprofilingreveals pages 1-2) | Mainly described in enteric bacteria | Curate as taxon-specific common edge |
| High | ADI / ammonia generation | arginine deiminase pathway --produces--> ammonia | Strong mechanistic review support; recent Alicyclobacillus proteomics points to ADI-linked ammonia generation under acid stress (lund2014copingwithlow pages 1-2, liu2023molecularmechanismof pages 9-12, lund2014copingwithlow pages 6-6) | Broad but uneven distribution; strong in LAB and some Gram-positives | Curate as common but taxon-limited module |
| High | Urease / ammonia generation | urease --produces--> ammonia | Strong mechanistic review support; recent Alicyclobacillus work includes urea hydrolysis as pHi-homeostasis mechanism (liu2023molecularmechanismof pages 9-12, lund2014copingwithlow pages 6-6) | Discrete subset of bacteria; not generic for all acidotolerant taxa | Curate as taxon-specific edge only where urease is present |
| High | Membrane remodeling | unsaturated/cyclopropane fatty acid remodeling --decreases--> membrane proton permeability | Review-backed and supported by 2023-2024 transcriptome/proteome synthesis in E. coli and Alicyclobacillus (liu2023molecularmechanismof pages 12-15, li2024responseofescherichia pages 5-7) | Broad stress module, but exact lipid chemistry varies by lineage | Curate as core generic process-level edge |
| Medium | Na+/H+ antiport | Na+/H+ antiporter NhaB --increases--> intracellular pH homeostasis | Recent species-specific proteomic association under sublethal acid stress (liu2023molecularmechanismof pages 9-12) | A. acidoterrestris pH 2.5 short-term response; broader generalization uncertain | Curate only as uncertain/taxon-specific edge |
| Medium | Periplasmic acid chaperones | HdeA/HdeB --protects--> periplasmic proteins from acid damage | Strong mechanistic review support with pH-range specificity retained in recent review (li2024responseofescherichia pages 5-7, li2024responseofescherichia pages 12-12) | Best established in Gram-negative enterics, especially E. coli | Curate as taxon-specific edge, not generic to all bacteria |
| Medium | DNA repair | acid stress --causes--> DNA damage | Strong review support and recent multi-omics support in Alicyclobacillus/E. coli (liu2023molecularmechanismof pages 12-15, li2024responseofescherichia pages 5-7, lund2014copingwithlow pages 6-6) | Broad bacterial consequence of cytoplasmic acidification | Curate as core stress-damage edge |
| Medium | DNA repair response | DNA repair systems --mitigates--> acid-induced DNA damage | Review-backed; recent omics show repair pathway involvement but intervention evidence limited in current set (li2024responseofescherichia pages 5-7, lund2014copingwithlow pages 6-6) | Broad, but exact repair proteins differ by taxon | Curate at process level only; avoid over-specific gene edges without direct perturbation |
| Low-Medium | Regulator YdeO | YdeO --activates--> Gad and Adi systems | Recent E. coli ribosome profiling/regulatory analysis (schumacher2023ribosomeprofilingreveals pages 21-23) | E. coli, 15 min response to pH 5.8 and 4.4 | Curate as taxon-specific regulatory edge; mark as not generic |
| Low-Medium | PhoP/PhoQ cross-protection | PhoP/PhoQ --increases--> heat/CAMP cross-protection after acid adaptation | Knockout evidence in Salmonella; acid tolerance itself persisted in ΔphoP (gao2024theeffectof pages 13-14) | S. Typhimurium, mild-acid adaptation at pH 5.4 followed by lethal acid/heat/osmotic/CAMP assays | Do not curate as core acidotolerance edge; reserve for cross-protection subgraph |
| Low | Engineered DsrA-Hfq circuit | engineered DsrA-Hfq module --increases--> low-pH growth/productivity robustness | Synthetic-biology intervention in industrial E. coli (yan2024engineeringquorumsensingbased pages 10-10) | Industrial strain engineering under mild low-pH fermentation | Do not curate into native TraitMech core graph; keep as application note |
| Low | Omics-only novel factors | acid stress --induces--> novel sORFs / MhpR / IscR candidates | Discovery-level omics association without direct causal validation (schumacher2023ribosomeprofilingreveals pages 21-23) | E. coli acute pH-shift assays | Do not curate yet; await functional perturbation evidence |


*Table: This table prioritizes candidate causal modules for curating the microbial acidotolerant trait METPO:1003008. It distinguishes broadly supported core mechanisms from taxon-specific regulators and engineering-only findings that should be handled cautiously.*

## 4. Recent developments and quantitative findings, 2023–2024

### Acute responses are graded, not binary

Schumacher et al. compared *E. coli* K-12 at pH 7.6, 5.8 and 4.4 after 15 min using RNA-seq and ribosome profiling. Beyond established Gad/Adi/Cad/Orn systems, the study implicated siderophore production, glycerol-3-phosphate conversion, copper and multidrug export, nucleotide biosynthesis, MhpR, IscR and **18 novel acid-induced sORFs**. Many H+-coupled transporters were downregulated. These are valuable discovery candidates, but expression changes alone do not establish causal acidotolerance edges (schumacher2023ribosomeprofilingreveals pages 21-23, schumacher2023ribosomeprofilingreveals pages 1-2).

### Multi-omics is resolving lineage-specific solutions

At pH 2.5 for 15 min, *A. acidoterrestris* proteomics identified **325 differentially expressed proteins: 83 increased and 242 decreased**. TesA and YciA increased **1.54-fold and 1.81-fold**, respectively, and unsaturated-fatty-acid biosynthesis was enriched. The same work associated NhaB, amino-acid metabolism, ADI/urease and DNA repair with the response. Because the organism is acidophilic, these findings should inform mechanism nodes but not define the acidotolerant taxon class (liu2023molecularmechanismof pages 12-15, liu2023molecularmechanismof pages 9-12).

A related pH 3.0, 1-h transcriptome/metabolome study reported **63 differential metabolites**, chiefly in amino-acid, nucleotide and energy metabolism, and concluded that amino-acid decarboxylation, urea hydrolysis and energy supply supported pHi homeostasis. This remains systems-level association unless individual components are experimentally perturbed.

### Cross-protection creates food-safety concerns

In *S. Typhimurium* ATCC 14028, adaptation for **90 min at pH 5.4** increased viability during lethal acid, **55 °C heat** and **8% osmotic stress**. Increased polymyxin-B resistance reportedly remained detectable for **21 days at 4 °C** in meat-extract medium. The ΔphoP result is particularly important for graph interpretation: PhoP/PhoQ influenced heat and antimicrobial cross-protection, whereas acid tolerance remained, implying redundant or parallel acid-defense pathways (gao2024theeffectof pages 13-14).

### Synthetic regulation is moving toward industrial implementation

A 2024 study used an Esa-type quorum-sensing circuit to dynamically control a DsrA–Hfq acid-resistance module. The engineered industrial *E. coli* produced lysine at pH 5.5 with productivity comparable to the parent strain at pH 6.8 and improved yield, illustrating “just-in-time/just-enough” deployment of defense rather than constitutive burden (yan2024engineeringquorumsensingbased pages 10-10).

Separately, adaptive evolution and metabolic engineering of *Yarrowia lipolytica* produced **112.54 g/L succinic acid at low pH**, with **0.67 g/g glucose yield** and **2.08 g/L/h productivity** (DOI **10.1186/s12934-024-02565-0**, October 2024). This demonstrates the economic value of acid robustness, but yeast mechanisms and organic-acid product tolerance should not be merged uncritically into a bacterial graph.

## 5. Applications and real-world relevance

1. **Low-pH biomanufacturing.** Acid-tolerant production strains reduce neutralizer demand, salt formation and wastewater, while maintaining organic-acid or amino-acid productivity. Dynamic circuits, adaptive laboratory evolution and membrane engineering are current implementation strategies (yan2024engineeringquorumsensingbased pages 10-10).
2. **Food fermentation.** Aciduric lactic and acetic-acid bacteria support starter-culture persistence, vinegar production, silage and fermented beverages. However, acid production and acid tolerance must be measured separately.
3. **Food safety and spoilage control.** Acid adaptation can protect *Salmonella* from heat, osmotic stress and cationic antimicrobials; *A. acidoterrestris* is a pasteurized acidic-juice spoilage target. Process validation should therefore test acid-adapted cells, not only neutral-grown cultures (liu2023molecularmechanismof pages 12-15, gao2024theeffectof pages 13-14).
4. **Probiotic selection.** Gastric and food-matrix survival depend on pH, acid type, bile, growth phase and formulation. Hde chaperones, membrane remodeling and proton-consuming metabolism can be useful markers, but gene presence is not a substitute for survival and growth assays (li2024responseofescherichia pages 5-7).
5. **Wastewater biofilms.** A 2024 activated-sludge study found that protonated exogenous putrescine promoted acidic-pH biofilm formation and was associated with Gad/GABA metabolism and ATPase activity. Because this was a mixed community with concentration- and pH-dependent effects, it is better retained as contextual evidence rather than a species-level core edge.
6. **Pathogenesis.** Acid-defense systems support passage through the stomach and intracellular acidic compartments; suppressing Gad, urease or pH-homeostasis pathways may sensitize selected pathogens. Therapeutic generalization is limited by pathway redundancy and taxonomic differences.

## 6. Expert synthesis and recommended graph architecture

Authoritative reviews converge on four functional requirements: **maintain pHi, preserve membrane integrity, regulate metabolism, and repair macromolecules**. Recent omics adds regulators and small proteins but does not overturn that framework (lund2014copingwithlow pages 1-2, li2024responseofescherichia pages 5-7, lund2014copingwithlow pages 6-6).

A robust TraitMech graph should use a **small conserved process-level core** with optional taxon modules:

1. **Exposure layer:** low external pH; weak organic acid; adaptation history.
2. **Primary perturbation:** proton influx, weak-acid dissociation, cytoplasmic acidification, membrane/protein/DNA damage.
3. **Defense modules:** proton extrusion; decarboxylase/antiporter cycles; ADI/urease alkali generation; envelope remodeling; chaperones and repair.
4. **Integrated state:** intracellular-pH homeostasis plus preserved membrane and macromolecular function.
5. **Trait endpoint:** maintained growth under acidic conditions.
6. **Optional context modules:** taxon-specific regulators, biofilm, gastric survival, acid-induced cross-protection and engineered circuits.

This architecture avoids treating Gad, urease, PhoP/PhoQ or any other single module as necessary or sufficient across all acidotolerant microbes.

## 7. Ontology-grounding recommendations

Use the following only after validation against the project’s ontology versions:

- Trait: **`METPO:1003008`** exactly as supplied.
- Proton: candidate `CHEBI:15378`.
- Acetic acid: candidate `CHEBI:15366`.
- Cytosol: candidate `GO:0005737`.
- Plasma membrane: candidate `GO:0005886`.
- Periplasmic space: candidate `GO:0042597`.
- Proton transmembrane transport: candidate `GO:1902600`.
- DNA repair: candidate `GO:0006281`.
- Protein folding: candidate `GO:0006457`.
- Biofilm formation: candidate `GO:0042710`.

**Keep label-only pending database verification:** acidic environment, acid challenge, acid adaptation, acid growth, intracellular-pH homeostasis, F-type ATPase complex, Gad/Adi/Cad systems, ADI pathway, urease pathway, membrane proton permeability, acid-induced cross-protection and DsrA–Hfq engineering module. For enzymes and transporters, use strain-specific UniProt accessions only after selecting a taxon/strain; do not assign one *E. coli* protein accession to a generic microbial node. Validate enzyme reactions against Rhea and EC, and use stereochemically explicit ChEBI metabolites.

## 8. Claims that should not yet be curated

- **Do not equate survival with growth.** A pH 2 challenge assay establishes acid resistance unless growth is demonstrated.
- **Do not label acidophiles as acidotolerant solely from low-pH growth.** Their optimum is itself acidic.
- **Do not infer phenotype from Gad, urease, ATPase or antiporter gene presence alone.** Expression, substrate availability and pathway integrity matter.
- **Do not make PhoP/PhoQ a necessary acidotolerance node.** ΔphoP retained acid tolerance in the retrieved *Salmonella* experiment (gao2024theeffectof pages 13-14).
- **Do not curate MhpR, IscR or the 18 novel sORFs as causal yet.** Present evidence is acute omics/regulatory association without phenotype rescue or knockout validation (schumacher2023ribosomeprofilingreveals pages 21-23).
- **Do not curate NhaB as a generic acid-response sensor.** Current evidence here is short-term proteomic association in an acidophile (liu2023molecularmechanismof pages 9-12).
- **Do not generalize HdeA/HdeB to Gram-positive organisms.** They are periplasmic enterobacterial chaperones.
- **Do not force a universal membrane-saturation direction.** Different organisms remodel lipids differently; use the process-level node until causal lipid-species data are available.
- **Do not merge organic-acid tolerance, acid production, biofilm formation, antibiotic tolerance or cross-protection into the trait endpoint.** Model them as exposure-specific or downstream/contextual branches.
- **Do not treat mixed-community putrescine results as a species-autonomous mechanism.** Community composition and adsorption effects confound the proposed intracellular route.
- **Do not place engineered circuits in the native core graph.** They belong in an application/engineering extension.

## DOI-first bibliography

1. Li Z, Huang Z, Gu P. “Response of *Escherichia coli* to Acid Stress: Mechanisms and Applications—A Narrative Review.” *Microorganisms*. **August 2024**. DOI: [10.3390/microorganisms12091774](https://doi.org/10.3390/microorganisms12091774) (li2024responseofescherichia pages 5-7).
2. Gao X et al. “The Effect of the PhoP/PhoQ System on the Regulation of Multi-Stress Adaptation Induced by Acid Stress in *Salmonella Typhimurium*.” *Foods*. **May 2024**. DOI: [10.3390/foods13101533](https://doi.org/10.3390/foods13101533) (gao2024theeffectof pages 13-14).
3. Yan X et al. “Engineering quorum sensing-based genetic circuits enhances growth and productivity robustness of industrial *E. coli* at low pH.” *Microbial Cell Factories*. **September 2024**. DOI: [10.1186/s12934-024-02524-9](https://doi.org/10.1186/s12934-024-02524-9) (yan2024engineeringquorumsensingbased pages 10-10).
4. Zhong Y et al. “Boosting succinic acid production of *Yarrowia lipolytica* at low pH through enhancing product tolerance and glucose metabolism.” *Microbial Cell Factories*. **October 2024**. DOI: [10.1186/s12934-024-02565-0](https://doi.org/10.1186/s12934-024-02565-0).
5. Schumacher K et al. “Ribosome profiling reveals the fine-tuned response of *Escherichia coli* to mild and severe acid stress.” *mSystems*. **December 2023**. DOI: [10.1128/msystems.01037-23](https://doi.org/10.1128/msystems.01037-23) (schumacher2023ribosomeprofilingreveals pages 21-23, schumacher2023ribosomeprofilingreveals pages 1-2).
6. Xu J et al. “Transcriptomic and Metabolomic Profiling Uncovers Response Mechanisms of *Alicyclobacillus acidoterrestris* DSM 3922T to Acid Stress.” *Microbiology Spectrum*. **August 2023**. DOI: [10.1128/spectrum.00022-23](https://doi.org/10.1128/spectrum.00022-23).
7. Liu X et al. “Molecular mechanism of acid stress response of *A. acidoterrestris* DSM 3922T under sublethal pH environment.” bioRxiv preprint. **July 2023**. DOI: [10.1101/2023.07.13.548807](https://doi.org/10.1101/2023.07.13.548807) (liu2023molecularmechanismof pages 12-15, liu2023molecularmechanismof pages 9-12). A peer-reviewed 2024 version was reported as DOI [10.1016/j.lwt.2024.115760](https://doi.org/10.1016/j.lwt.2024.115760); verify correspondence before transferring quotations.
8. Rebelo A et al. “Unraveling the Role of Metals and Organic Acids in Bacterial Antimicrobial Resistance in the Food Chain.” *Antibiotics*. **September 2023**. DOI: [10.3390/antibiotics12091474](https://doi.org/10.3390/antibiotics12091474) (rebelo2023unravelingtherole pages 18-20).
9. Lund P, Tramonti A, De Biase D. “Coping with low pH: molecular strategies in neutralophilic bacteria.” *FEMS Microbiology Reviews*. **November 2014**. DOI: [10.1111/1574-6976.12076](https://doi.org/10.1111/1574-6976.12076) (lund2014copingwithlow pages 1-2, lund2014copingwithlow pages 6-6).
10. Krulwich TA, Sachs G, Padan E. “Molecular aspects of bacterial pH sensing and homeostasis.” *Nature Reviews Microbiology*. **May 2011**. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). This is the supplied foundational evidence and supports the broad link between pH sensing/homeostasis and growth outside the normal cytoplasmic-pH range.
11. De Biase D, Pennacchietti E. “Glutamate decarboxylase-dependent acid resistance in orally acquired bacteria.” *Molecular Microbiology*. **November 2012**. DOI: [10.1111/mmi.12020](https://doi.org/10.1111/mmi.12020).
12. Cotter PD, Hill C. “Surviving the Acid Test: Responses of Gram-Positive Bacteria to Low pH.” *Microbiology and Molecular Biology Reviews*. **September 2003**. DOI: [10.1128/MMBR.67.3.429-453.2003](https://doi.org/10.1128/MMBR.67.3.429-453.2003) (cotter2003survivingtheacid pages 13-14).

References

1. (rebelo2023unravelingtherole pages 18-20): Andreia Rebelo, Agostinho Almeida, Luísa Peixe, Patrícia Antunes, and Carla Novais. Unraveling the role of metals and organic acids in bacterial antimicrobial resistance in the food chain. Antibiotics, 12:1474, Sep 2023. URL: https://doi.org/10.3390/antibiotics12091474, doi:10.3390/antibiotics12091474. This article has 35 citations.

2. (lund2014copingwithlow pages 1-2): Peter Lund, Angela Tramonti, and Daniela De Biase. Coping with low ph: molecular strategies in neutralophilic bacteria. FEMS microbiology reviews, 38 6:1091-125, Nov 2014. URL: https://doi.org/10.1111/1574-6976.12076, doi:10.1111/1574-6976.12076. This article has 655 citations and is from a domain leading peer-reviewed journal.

3. (liu2023molecularmechanismof pages 12-15): Xiaoxue Liu, Youzhi Wu, Lingxia Jiao, Junjian Ran, Linjun Sun, Fuzhou Ye, Xin-hong Liang, and Ruixiang Zhao. Molecular mechanism of acid stress response of a. acidoterrestris dsm 3922t under sublethal ph environment. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.13.548807, doi:10.1101/2023.07.13.548807. This article has 0 citations.

4. (gao2024theeffectof pages 13-14): Xu Gao, Jina Han, Lixian Zhu, George-John E. Nychas, Yanwei Mao, Xiaoyin Yang, Yunge Liu, Xueqing Jiang, Yimin Zhang, and Pengcheng Dong. The effect of the phop/phoq system on the regulation of multi-stress adaptation induced by acid stress in salmonella typhimurium. Foods, 13:1533, May 2024. URL: https://doi.org/10.3390/foods13101533, doi:10.3390/foods13101533. This article has 18 citations.

5. (schumacher2023ribosomeprofilingreveals pages 21-23): Kilian Schumacher, Rick Gelhausen, Willow Kion-Crosby, Lars Barquist, Rolf Backofen, and Kirsten Jung. Ribosome profiling reveals the fine-tuned response of <i>escherichia coli</i> to mild and severe acid stress. Dec 2023. URL: https://doi.org/10.1128/msystems.01037-23, doi:10.1128/msystems.01037-23. This article has 24 citations and is from a peer-reviewed journal.

6. (schumacher2023ribosomeprofilingreveals pages 1-2): Kilian Schumacher, Rick Gelhausen, Willow Kion-Crosby, Lars Barquist, Rolf Backofen, and Kirsten Jung. Ribosome profiling reveals the fine-tuned response of <i>escherichia coli</i> to mild and severe acid stress. Dec 2023. URL: https://doi.org/10.1128/msystems.01037-23, doi:10.1128/msystems.01037-23. This article has 24 citations and is from a peer-reviewed journal.

7. (liu2023molecularmechanismof pages 9-12): Xiaoxue Liu, Youzhi Wu, Lingxia Jiao, Junjian Ran, Linjun Sun, Fuzhou Ye, Xin-hong Liang, and Ruixiang Zhao. Molecular mechanism of acid stress response of a. acidoterrestris dsm 3922t under sublethal ph environment. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.13.548807, doi:10.1101/2023.07.13.548807. This article has 0 citations.

8. (lund2014copingwithlow pages 6-6): Peter Lund, Angela Tramonti, and Daniela De Biase. Coping with low ph: molecular strategies in neutralophilic bacteria. FEMS microbiology reviews, 38 6:1091-125, Nov 2014. URL: https://doi.org/10.1111/1574-6976.12076, doi:10.1111/1574-6976.12076. This article has 655 citations and is from a domain leading peer-reviewed journal.

9. (li2024responseofescherichia pages 5-7): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 41 citations.

10. (yan2024engineeringquorumsensingbased pages 10-10): Xiaofang Yan, Anqi Bu, Yanfei Yuan, Xin Zhang, Zhanglin Lin, and Xiaofeng Yang. Engineering quorum sensing-based genetic circuits enhances growth and productivity robustness of industrial e. coli at low ph. Microbial Cell Factories, Sep 2024. URL: https://doi.org/10.1186/s12934-024-02524-9, doi:10.1186/s12934-024-02524-9. This article has 15 citations and is from a peer-reviewed journal.

11. (li2024responseofescherichia pages 12-12): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 41 citations.

12. (cotter2003survivingtheacid pages 13-14): Paul D. Cotter and Colin Hill. Surviving the acid test: responses of gram-positive bacteria to low ph. Microbiology and Molecular Biology Reviews, 67:429-453, Sep 2003. URL: https://doi.org/10.1128/mmbr.67.3.429-453.2003, doi:10.1128/mmbr.67.3.429-453.2003. This article has 1740 citations and is from a domain leading peer-reviewed journal.