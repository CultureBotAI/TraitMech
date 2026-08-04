# Deep-research curation review: `cellulolysis` (`traitmech:000111`)

**Audit date:** 2026-07-30  
**Scope reviewed:** `data/traits/metabolism/cellulolysis.yaml`, especially
`causal_graphs`; `docs/GROUNDING_POLICY.md`;
`src/traitmech/schema/traitmech.yaml`; and the locally imported METPO OWL.

## Executive assessment

The graph contains a recognizable hydrolytic core, and most of its individual
enzyme claims are directionally correct. It is not yet a faithful general
mechanism for microbial cellulolysis, however.

The highest-impact defects are:

1. `cellulosome` is a protein complex, not a cellular localization. Its
   `GO:0043263` grounding is valid, but its local `node_type` should be
   `GENE_OR_PROTEIN` under the repository's current policy for complexes.
2. `cellulolysis_trait -> produces -> glucose` turns a capability/class into an
   occurring process and implies glucose is the universal immediate product.
   Many anaerobic cellulolytic bacteria instead import cellodextrins and cleave
   them intracellularly by phosphorolysis.
3. The graph omits cellulose-active LPMOs, CBM-mediated targeting, chain-end
   creation and endo/exo synergy, crystallinity/accessibility, transport,
   intracellular phosphorylases, and product inhibition.
4. The cellulosome and CCR components are disconnected from the catalytic
   cascade. Three of ten edges describe cohesin/dockerin architecture, although
   cellulosomes are only one taxonomically restricted strategy.
5. The generic CCR edge is overgeneralized. Its cited review discusses
   lignocellulose-catabolic regulation across disparate organisms, whereas the
   strongest direct cellulolysis evidence is a taxon-specific CRE-dependent
   repression of the *Clostridium cellulolyticum* `cip-cel` operon.

The report below separates broadly conserved mechanism from taxon-specific
branches. “Label-only, grounding uncertain” is deliberate wherever a suitable
identifier was not verified.

# 1. CORRECTNESS

## 1.1 Schema and grounding-policy constraints

The current schema permits the following relevant types: `TRAIT`,
`GENE_OR_PROTEIN`, `CHEMICAL`, `CELLULAR_LOCALIZATION`,
`MOLECULAR_FUNCTION`, `BIOLOGICAL_PROCESS`, `STATE`, and `QUALITY`.
`GENE_OR_PROTEIN` explicitly includes a protein complex. Nodes may remain
label-only. Every edge must have one or more evidence items, although an
evidence `snippet` is not currently mandatory.

The repository grounding policy requires:

- taxon-agnostic enzymatic functions → GO molecular function;
- taxon-agnostic protein complexes → GO cellular component;
- protein families/domains → InterPro/Pfam/NCBIfam;
- organism-specific protein instances → reviewed UniProt plus a taxon;
- broad functional classes → label-only or decomposed, not an arbitrary
  protein accession.

The schema's CURIE regex would syntactically accept `EC:3.2.1.4`, but `EC` is
not declared in the current LinkML prefix map. Since EC identifiers are useful
and specifically requested here, the prefix should be added and validated
before EC CURIEs are committed. Until then, the corresponding verified GO MF
can be the primary grounding and EC can be retained in the description or a
pending xref.

## 1.2 Requested CURIE-resolution audit

| CURIE | Resolved label/type | Verdict |
|---|---|---|
| `traitmech:000111` | Local record `cellulolysis` | **Correct and live.** The node label matches the local trait. |
| [`CHEBI:17234`](https://www.ebi.ac.uk/chebi/CHEBI:17234) | `glucose` | **Correct.** The graph's label and chemical semantics match. |
| [`CHEBI:18246`](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=18246) | `(1→4)-beta-D-glucan`; `cellulose` is a synonym | **Resolvable and semantically acceptable, but not an exact label match.** Either relabel the node with the primary ChEBI label and retain “cellulose” as display text, or document the synonym use. It represents the polymer, not specifically crystalline cellulose. |
| [`GO:0008422`](https://www.ebi.ac.uk/QuickGO/term/GO:0008422) | `beta-glucosidase activity`, molecular function | **Correct and live.** It grounds an activity, so a `MOLECULAR_FUNCTION` node would be semantically cleaner than a generic protein node. It is broader than cellobiose-only activity. |
| [`GO:0043263`](https://www.ebi.ac.uk/QuickGO/term/GO:0043263) | `cellulosome`, cellular component; an extracellular multi-enzyme complex | **Correct and live.** The grounding is appropriate for a taxon-agnostic complex; the local `node_type`, not the GO term, is wrong. |
| [`RO:0002327`](https://www.ebi.ac.uk/ols4/ontologies/ro/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FRO_0002327) | `enables` | **Correct and live.** Direction is bearer/gene product → function or process enabled. The current subject, an aggregate “cellulase systems,” makes the assertion less precise than the predicate. |
| [`METPO:2000202`](https://w3id.org/metpo/2000202) | `produces`, object property | **Correct and live in the imported METPO OWL.** The current problem is the trait-class subject, not this predicate. |
| [`METPO:2000007`](https://w3id.org/metpo/2000007) | `degrades`, object property | **Correct and live.** Broad but compatible with enzyme/system → cellulose. |
| [`METPO:2000013`](https://w3id.org/metpo/2000013) | `hydrolyzes`, object property | **Correct and live.** Compatible with activity/enzyme → chemical substrate. |

Also add the verified [`CHEBI:17057`](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=17057)
grounding to the existing `cellobiose` node.

## 1.3 Existing-node audit

| Node | Current type/grounding | Literature and semantic verdict | Recommended disposition |
|---|---|---|---|
| `cellulolysis_trait` | `TRAIT`; `traitmech:000111` | **Supported.** This is the correct graph anchor. Its description should emphasize capacity to depolymerize cellulose, not require release of free glucose. | Keep. |
| `cellulase` (“cellulase systems”) | `GENE_OR_PROTEIN`; label-only | **Partly supported, under-specified.** Cellulase systems are coordinated mixtures or complexes, not one gene/protein. Lynd et al. explicitly distinguish noncomplexed and cellulosomal systems ([DOI](https://doi.org/10.1128/MMBR.66.3.506-577.2002)). | Prefer `cellulase activity` as `MOLECULAR_FUNCTION`, `GO:0008810`, or retain a label-only “cellulase system” only as a high-level grouping node. Do not ground it to one accession. |
| `glucose` | `CHEMICAL`; `CHEBI:17234` | **Correct entity.** It is one possible soluble product and a downstream hydrolytic product, but not the universal extracellular intermediate. | Keep, with branch-specific edges. |
| `cellulose` | `CHEMICAL`; `CHEBI:18246` | **Semantically correct with a label caveat.** The CURIE's primary label is `(1→4)-beta-D-glucan`. It does not encode crystallinity. | Keep and document synonym; add distinct amorphous/crystalline nodes only where needed. |
| `endoglucanase` | `GENE_OR_PROTEIN`; label-only | **Supported but type/grounding mix function and bearer.** Endoglucanases cleave internal cellulose-chain bonds, especially accessible/noncrystalline regions. | Prefer `MOLECULAR_FUNCTION` + [`GO:0008810`](https://www.ebi.ac.uk/QuickGO/term/GO:0008810) (`cellulase activity`; EC 3.2.1.4) if the node denotes activity. Keep label-only only if it denotes the protein class. |
| `cellobiohydrolase` | `GENE_OR_PROTEIN`; label-only | **Supported but over-collapsed.** Reducing- and non-reducing-end activities have different EC entries, and “exoglucanase” is not a perfectly interchangeable family name. Processivity is common but enzyme-specific. | Split into non-reducing-end `EC:3.2.1.91` and reducing-end `EC:3.2.1.176` activity nodes after the EC prefix is declared. |
| `beta_glucosidase` | `GENE_OR_PROTEIN`; `GO:0008422` | **Claim supported; semantic typing is mixed.** GO grounds the molecular activity, not a protein family. Beta-glucosidases can accept substrates other than cellobiose, so the cellobiose edge is narrower than the GO term. | Change node type to `MOLECULAR_FUNCTION`, or split activity from enzyme bearer. Keep GO term. Add EC 3.2.1.21 as xref after prefix support. |
| `cellobiose` | `CHEMICAL`; label-only | **Correct and central, but ungrounded.** Cellobiose is a frequent product/intermediate and inhibitor. It is not the only cellodextrin. | Ground to `CHEBI:17057`; add a broader label-only `cellodextrin` node. |
| `cellulosome` | `CELLULAR_LOCALIZATION`; `GO:0043263` | **Type is wrong.** A cellulosome is an extracellular multi-enzyme macromolecular complex, not a location. The GO CC grounding is correct under the policy for complexes. | Change to `GENE_OR_PROTEIN`; keep `GO:0043263`. |
| `scaffoldin` | `GENE_OR_PROTEIN`; label-only | **Correct.** It is a noncatalytic backbone protein, though some scaffoldins can also contain catalytic domains; the description should not imply every scaffoldin is strictly noncatalytic. | Keep. A family-level InterPro grounding needs curator verification; do not use a single UniProt. |
| `cohesin_domain` | `GENE_OR_PROTEIN`; label-only | **Correct broad type.** It is a domain/family, not a whole enzyme. | Keep; candidate InterPro family should be independently checked before commit. |
| `dockerin_domain` | `GENE_OR_PROTEIN`; label-only | **Correct broad type.** It is a protein interaction module. Bacterial and fungal dockerins are not one interchangeable family. | Keep label-only or split bacterial/fungal families after verified domain grounding. |
| `ccr` | `BIOLOGICAL_PROCESS`; label-only | **Reasonable type, but description is too glucose-specific and universal.** Preferred soluble carbon sources and CCR circuitry vary among cellulolytic organisms. | Keep only in a taxon-qualified regulatory branch; label “CRE-dependent CCR” where that is the evidence. |
| `cellulolytic_genes` | `GENE_OR_PROTEIN`; label-only | **Semantically weak.** A plural gene set/operon is not a gene product. The schema has no `GENE_SET` type. The label also expands to lignocellulose genes, exceeding this trait. | Replace with a specific operon/regulon node (e.g. *C. cellulolyticum* `cip-cel` operon) and document the schema compromise, or add a gene-set type in a future schema change. |

## 1.4 Existing-edge audit

| # | Existing subject–predicate–object | Verdict | Evidence/citation assessment and correction |
|---:|---|---|---|
| 1 | `cellulase systems —enables→ cellulolysis` (`RO:0002327`) | **Directionally supported, but underspecified.** | Lynd et al. support coordinated cellulase systems as the machinery for cellulose utilization ([DOI](https://doi.org/10.1128/MMBR.66.3.506-577.2002); PMID [12209002](https://pubmed.ncbi.nlm.nih.gov/12209002/)). The edge is acceptable as a summary edge if `cellulase systems` remains a system-level label. For tighter RO semantics, use concrete cellulase protein/activity nodes. The description “hydrolyze extracellularly” is not universal: cell-surface hydrolysis and intracellular fate matter. |
| 2 | `cellulolysis —produces→ glucose` (`METPO:2000202`) | **Over-specified and ontologically awkward.** | Cragg et al. review deconstruction strategies but are weak direct evidence for this binary edge ([DOI](https://doi.org/10.1016/j.cbpa.2015.10.018)). A `TRAIT` is a capability/class, not an occurring reaction. More importantly, glucose is not always the immediate extracellular product; many anaerobes assimilate cellodextrins and use phosphorylases. Replace with the explicit substrate/product cascade and branch-specific edges. |
| 3 | `endoglucanase —degrades→ cellulose` (`METPO:2000007`) | **Supported but too broad.** | The cited review describes internal cleavage and concerted action ([DOI](https://doi.org/10.1093/jambio/lxac002)). Direction and predicate are sound. Add the mechanistic result—new chain ends/shorter cellodextrins—and qualify preference for accessible/amorphous regions rather than implying exclusive specificity. |
| 4 | `cellobiohydrolase —degrades→ cellulose` (`METPO:2000007`) | **Supported but too broad.** | The same review supports the participation of cellobiohydrolases. Split reducing- and non-reducing-end activities, add cellobiose as product, and retain processivity only for the applicable enzymes. |
| 5 | `beta-glucosidase —hydrolyzes→ cellobiose` (`METPO:2000013`) | **Supported.** | The cited paper directly describes conversion of cellobiose to glucose ([DOI](https://doi.org/10.1186/s13568-023-01658-0)). It is a primary *Neurospora crassa* enzyme study with a generic introductory claim, so it supports the chemistry, not universality of extracellular location. |
| 6 | `beta-glucosidase —produces→ glucose` (`METPO:2000202`) | **Supported, with context missing.** | Same citation supports two glucose molecules per hydrolyzed cellobiose. This is one fate branch, not the universal anaerobic route. A reaction intermediate or linked substrate edge would make the causal path unambiguous. |
| 7 | `cellulosome —has backbone component→ scaffoldin` | **Supported; predicate ungrounded.** | The cited review supports scaffoldin-built complexes ([DOI](https://doi.org/10.1093/jambio/lxac002)). Change the subject node type. Prefer a standard `has part`/component predicate if one is selected and verified; otherwise the label-only predicate is schema-valid. |
| 8 | `scaffoldin —contains→ cohesin domain` | **Supported, but evidence is narrower than the generic claim.** | The cited comparative study supports cohesin-bearing scaffoldins in the examined *Ruminiclostridium* systems ([DOI](https://doi.org/10.3389/fmicb.2023.1288286)). The general claim is well established, but a broader cellulosome review would be better evidence. “Contains” should become a verified part relation. |
| 9 | `dockerin domain —binds to→ cohesin domain` | **Supported and correctly directed.** | The cited review supports canonical cohesin–dockerin assembly ([DOI](https://doi.org/10.1093/jambio/lxac002)). The physical interaction is symmetric for graph traversal, but this direction is not wrong. Qualify compatibility/type specificity; not every dockerin binds every cohesin. |
| 10 | `CCR —represses→ cellulolytic/lignocellulose-catabolic genes` | **Overgeneralized and insufficiently cellulose-specific.** | The cited review discusses CcpA/CRE regulation in a broad lignocellulose context ([DOI](https://doi.org/10.1093/jambio/lxac002)); it does not justify a universal microbial edge. Direct evidence supports soluble-sugar/CRE-dependent repression of the *C. cellulolyticum* `cip-cel` operon ([DOI](https://doi.org/10.1128/JB.01160-07); PMID [18156277](https://pubmed.ncbi.nlm.nih.gov/18156277/)). Replace with that taxon-specific edge or explicitly mark the generic assertion uncertain. |

## 1.5 Citation-by-citation audit

- **Lynd et al. 2002, DOI 10.1128/MMBR.66.3.506-577.2002:** strongly
  supports the high-level cellulase-system edge, free versus complexed
  strategies, cellodextrin transport, alternative intracellular fates, and
  cellulosome organization. It does not support the graph's implication that
  every cellulolysis event simply ends in extracellular glucose.
- **Cragg et al. 2015, DOI 10.1016/j.cbpa.2015.10.018:** supports diversity of
  microbial lignocellulose-deconstruction strategies, including oxidative
  enzymes and cellulosomes. It is too indirect for the exact
  `trait -> produces -> glucose` edge.
- **Jayasekara & Ratnayake 2022, DOI 10.1093/jambio/lxac002:** supports the
  concerted endoglucanase/cellobiohydrolase/beta-glucosidase model and
  canonical cellulosome assembly. Its regulation discussion is a review-level
  synthesis and is not adequate evidence for universal CCR of a broad gene
  class.
- **Kameshwar et al. 2023, DOI 10.1186/s13568-023-01658-0:** supports the
  beta-glucosidase chemistry. The experimental organism is *N. crassa*; the
  edge should not inherit a bacterial intracellular/extracellular location
  from it.
- **Artzi et al. 2023, DOI 10.3389/fmicb.2023.1288286:** supports scaffoldin
  and cohesin architecture in the systems examined. It is not evidence that
  all cellulolytic organisms possess cellulosomes.
- **Abdou et al. 2008, DOI 10.1128/JB.01160-07:** not currently cited but is a
  much better replacement for the CCR edge. Its scope is explicitly
  *C. cellulolyticum*.

# 2. COMPLETENESS

The proposal below uses activity nodes where the mechanism is an activity,
complex nodes for complexes, and label-only nodes where no identifier was
verified. Each proposed edge has edge-level evidence. Quoted snippets are
short fragments from the linked source and should be stored once per edge in
the YAML evidence item.

## 2.1 LPMOs (AA9/AA10) and oxidative cleavage — **belongs in the core graph**

Hydrolysis-only is no longer an adequate representation of aerobic microbial
cellulose deconstruction. Cellulose-active LPMOs oxidatively cleave glycosidic
bonds and create new entry sites for hydrolases. AA9 is prominent in fungi and
AA10 in bacteria, but neither AA family is exclusively cellulose-active; a
family node must therefore be qualified as “cellulose-active.”

**Proposed nodes**

| Node | Type | Grounding |
|---|---|---|
| `cellulose_active_lpmo` | `GENE_OR_PROTEIN` | label-only, grounding uncertain; split AA9 and AA10 family/domain identifiers only after InterPro/Pfam verification |
| `oxidized_cellulose_chain_ends` | `CHEMICAL` | label-only, grounding uncertain |

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `cellulose_active_lpmo —oxidatively cleaves→ cellulose` | [DOI 10.1073/pnas.1402771111](https://doi.org/10.1073/pnas.1402771111), PMID [24912171](https://pubmed.ncbi.nlm.nih.gov/24912171/): “cleaves glycosidic bonds by oxidation of the C1 carbon” |
| `cellulose_active_lpmo —produces→ oxidized_cellulose_chain_ends` | [DOI 10.1073/pnas.1402771111](https://doi.org/10.1073/pnas.1402771111), PMID [24912171](https://pubmed.ncbi.nlm.nih.gov/24912171/): “can oxidize both C1 and C4” |
| `oxidized_cellulose_chain_ends —increases access for→ cellulase_activity` | [DOI 10.1038/srep40262](https://doi.org/10.1038/srep40262): “formation of new initiation sites for conventional cellulases” |

The need for an external electron donor/reductant and oxygen or peroxide is
important LPMO chemistry, but the preferred cosubstrate is enzyme- and
condition-dependent. Add that branch only with an explicitly scoped source.

## 2.2 CBMs and substrate targeting — **belongs in the core graph**

CBMs are noncatalytic targeting modules. They increase the local concentration
of appended enzymes at insoluble cellulose and can target distinct surface
regions. CBM families have different ligand specificities; “CBM” should not be
given one family identifier.

**Proposed nodes**

| Node | Type | Grounding |
|---|---|---|
| `cellulose_binding_module` | `GENE_OR_PROTEIN` | label-only, grounding uncertain because many CBM families bind cellulose |
| `cellulase_cellulose_association` | `STATE` | label-only, grounding uncertain |

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `cellulose_binding_module —binds→ cellulose` | [DOI 10.1042/BJ20040892](https://doi.org/10.1042/BJ20040892), PMID [15214846](https://pubmed.ncbi.nlm.nih.gov/15214846/): “CBMs promote the association of the enzyme with the substrate.” |
| `cellulose_binding_module —promotes→ cellulase_cellulose_association` | [DOI 10.1042/BJ20040892](https://doi.org/10.1042/BJ20040892), PMID [15214846](https://pubmed.ncbi.nlm.nih.gov/15214846/): “CBMs promote the association of the enzyme with the substrate.” |
| `cellulase_cellulose_association —promotes→ cellulose_hydrolysis` | [DOI 10.1128/JB.185.2.504-512.2003](https://doi.org/10.1128/JB.185.2.504-512.2003), PMID [12511497](https://pubmed.ncbi.nlm.nih.gov/12511497/): “decreased the catalytic activity toward bacterial microcrystalline cellulose to 1%” |

The last snippet describes a particular modular enzyme experiment and should
be marked assay-specific, not a universal quantitative effect.

## 2.3 Crystallinity and amorphous versus crystalline cellulose — **belongs as a substrate-quality modifier**

Crystallinity/accessibility is a major kinetic factor, not a separate microbial
trait. It should modify the hydrolysis branch. Crystallinity, accessible
surface area, porosity, and pretreatment are correlated, so a universal
deterministic edge would be too strong.

**Proposed nodes**

| Node | Type | Grounding |
|---|---|---|
| `cellulose_crystallinity` | `QUALITY` | label-only, grounding uncertain |
| `amorphous_cellulose` | `CHEMICAL` | `CHEBI:62967` |
| `crystalline_cellulose` | `CHEMICAL` | `CHEBI:62968` appears in the official ChEBI hierarchy; re-resolve directly before commit |

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `cellulose_crystallinity —decreases rate of→ cellulose_hydrolysis` | [DOI 10.1111/j.1742-4658.2010.07585.x](https://doi.org/10.1111/j.1742-4658.2010.07585.x): “decrease in rate as crystallinity increases.” |
| `amorphous_cellulose —is more susceptible to→ cellulase_activity` | [DOI 10.1111/j.1742-4658.2010.07585.x](https://doi.org/10.1111/j.1742-4658.2010.07585.x): “amorphous sample is hydrolyzed much faster” |

These are *T. reesei* cellulases acting on controlled Avicel preparations.
Mark the edges assay/substrate-specific and interpret crystallinity together
with accessibility.

## 2.4 Cellodextrin transport and intracellular phosphorolysis — **essential core branch**

This is the largest mechanistic omission. The current graph treats
beta-glucosidase hydrolysis to glucose as the only downstream fate. In
*Acetivibrio thermocellus* (formerly *Clostridium thermocellum*) and several
other anaerobes, cellodextrins are taken up by ATP-dependent transport and
phosphorolyzed intracellularly. Cellobiose and cellodextrin phosphorylases
conserve energy by forming glucose-1-phosphate. Hydrolytic and phosphorolytic
routes coexist and their relative importance varies by organism and growth
condition.

**Proposed nodes**

| Node | Type | Grounding |
|---|---|---|
| `cellodextrin` | `CHEMICAL` | label-only, grounding uncertain; it denotes a DP distribution, not one molecule |
| `cellodextrin_abc_transporter` | `GENE_OR_PROTEIN` | label-only, grounding uncertain; a taxon-agnostic transporter class, not one UniProt |
| `cytoplasm` | `CELLULAR_LOCALIZATION` | `GO:0005737` |
| `cellodextrin_phosphorylase_activity` | `MOLECULAR_FUNCTION` | `EC:2.4.1.49` after declaring/verifying the EC prefix |
| `cellobiose_phosphorylase_activity` | `MOLECULAR_FUNCTION` | `EC:2.4.1.20` after declaring/verifying the EC prefix |
| `glucose_1_phosphate` | `CHEMICAL` | label-only, grounding uncertain |

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `cellodextrin_abc_transporter —transports→ cellodextrin` | [DOI 10.1128/MMBR.66.3.506-577.2002](https://doi.org/10.1128/MMBR.66.3.506-577.2002), PMID [12209002](https://pubmed.ncbi.nlm.nih.gov/12209002/): “cellodextrin transport via an ATP-binding cassette protein” |
| `cellodextrin —is transported to→ cytoplasm` | [DOI 10.1073/pnas.0408734102](https://doi.org/10.1073/pnas.0408734102), PMID [15883376](https://pubmed.ncbi.nlm.nih.gov/15883376/): “substrate transport via an adenosine-binding cassette system” |
| `cellodextrin_phosphorylase_activity —phosphorolyzes→ cellodextrin` | [DOI 10.1128/AEM.70.3.1563-1569.2004](https://doi.org/10.1128/AEM.70.3.1563-1569.2004): “phosphorolytic cleavage greatly exceeds that of hydrolytic cleavage” |
| `cellodextrin_phosphorylase_activity —produces→ glucose_1_phosphate` | [DOI 10.1128/AEM.70.3.1563-1569.2004](https://doi.org/10.1128/AEM.70.3.1563-1569.2004): “glucose and glucose-1-phosphate” |
| `cellobiose_phosphorylase_activity —phosphorolyzes→ cellobiose` | [DOI 10.1271/bbb.110954](https://doi.org/10.1271/bbb.110954), PMID [22484959](https://pubmed.ncbi.nlm.nih.gov/22484959/): “phosphorolyzed only cellobiose efficiently” |
| `cellobiose_phosphorylase_activity —produces→ glucose_1_phosphate` | [DOI 10.1271/bbb.110954](https://doi.org/10.1271/bbb.110954), PMID [22484959](https://pubmed.ncbi.nlm.nih.gov/22484959/): “produce α-D-glucopyranosyl phosphate” |
| `cellobiose_phosphorylase_activity —produces→ glucose` | [DOI 10.1271/bbb.110954](https://doi.org/10.1271/bbb.110954), PMID [22484959](https://pubmed.ncbi.nlm.nih.gov/22484959/): “and D-glucose” |

These edges need a scope note such as “demonstrated in cellulolytic anaerobes;
not the universal fate of extracellular cellobiose.” A recent primary study
further indicates that transporter B is the major/sole cellodextrin system in
the tested *A. thermocellus* strain, refining earlier five-transporter
annotations ([DOI 10.1128/mbio.01476-22](https://doi.org/10.1128/mbio.01476-22)).

## 2.5 Product inhibition — **belongs as an enzyme-kinetic branch**

Cellobiose inhibits many cellobiohydrolases/cellulase mixtures, while glucose
inhibits many beta-glucosidases. These are not universal categorical effects:
glucose-tolerant beta-glucosidases exist, and inhibition constants vary.

**Proposed nodes:** reuse `cellobiose`, `glucose`, `cellobiohydrolase_activity`,
and `beta_glucosidase_activity`; optionally add `cellulase_product_inhibition`
as `STATE`, label-only.

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `cellobiose —inhibits→ cellobiohydrolase_activity` | [DOI 10.1360/02yc0163](https://doi.org/10.1360/02yc0163), PMID [15382672](https://pubmed.ncbi.nlm.nih.gov/15382672/): “cellobiose can strongly inhibit hydrolysis reaction of cellulase” |
| `glucose —inhibits→ beta_glucosidase_activity` | [DOI 10.1186/1754-6834-6-105](https://doi.org/10.1186/1754-6834-6-105), PMID [23883540](https://pubmed.ncbi.nlm.nih.gov/23883540/): “BG inhibition by glucose will eventually lead to the accumulation of cellobiose” |
| `beta_glucosidase_activity —relieves inhibition of→ cellobiohydrolase_activity` | [DOI 10.1186/1754-6834-6-105](https://doi.org/10.1186/1754-6834-6-105), PMID [23883540](https://pubmed.ncbi.nlm.nih.gov/23883540/): “thereby relieving the product inhibition of cellobiohydrolases” |

All three are enzyme/assay-specific trends and should be marked as such.

## 2.6 GH families and EC activities — **activity nodes belong; family membership is annotation/context**

The current graph should distinguish catalytic activity from CAZy family.
GH family does not map one-to-one to biochemical function:

- GH5 and GH9 include endoglucanases and processive enzymes, among other
  functions.
- GH6 commonly contains non-reducing-end cellobiohydrolases.
- fungal GH7 and bacterial GH48 commonly include reducing-end
  cellobiohydrolases, but family membership alone is not proof of that activity.
- beta-glucosidases occur in multiple families, notably GH1 and GH3.

**Proposed activity nodes**

| Node | Type | Grounding |
|---|---|---|
| `endoglucanase_activity` | `MOLECULAR_FUNCTION` | `GO:0008810`; pending xref `EC:3.2.1.4` |
| `nonreducing_end_cellobiohydrolase_activity` | `MOLECULAR_FUNCTION` | pending `EC:3.2.1.91`; GO candidate `GO:0016162` should be curator-reviewed for exact end semantics |
| `reducing_end_cellobiohydrolase_activity` | `MOLECULAR_FUNCTION` | pending `EC:3.2.1.176` |
| `beta_glucosidase_activity` | `MOLECULAR_FUNCTION` | `GO:0008422`; pending xref `EC:3.2.1.21` |
| `GH5`, `GH6`, `GH7`, `GH9`, `GH48` | `GENE_OR_PROTEIN` only if retained as family nodes | label-only, grounding uncertain until the exact InterPro/Pfam family record is verified |

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `endoglucanase_activity —hydrolyzes internal bonds of→ cellulose` | [DOI 10.1111/j.1742-4658.2010.07585.x](https://doi.org/10.1111/j.1742-4658.2010.07585.x): “break down cellulose chains at random positions” |
| `nonreducing_end_cellobiohydrolase_activity —produces→ cellobiose` | [DOI 10.1111/j.1742-4658.2010.07585.x](https://doi.org/10.1111/j.1742-4658.2010.07585.x): “cleave off cellobiose” |
| `reducing_end_cellobiohydrolase_activity —produces→ cellobiose` | [DOI 10.1107/S2053230X15015915](https://doi.org/10.1107/S2053230X15015915): “releases cellobiose as the major product.” |
| `beta_glucosidase_activity —hydrolyzes→ cellobiose` | [DOI 10.1186/s13568-023-01658-0](https://doi.org/10.1186/s13568-023-01658-0): “hydrolysis of cellobiose into two glucose molecules” |

The authoritative ENZYME entries confirm
[`EC 3.2.1.4`](https://enzyme.expasy.org/EC/3.2.1.4),
[`EC 3.2.1.91`](https://enzyme.expasy.org/EC/3.2.1.91),
[`EC 3.2.1.21`](https://enzyme.expasy.org/EC/3.2.1.21), and
[`EC 3.2.1.176`](https://enzyme.expasy.org/EC/3.2.1.176). In particular,
3.2.1.176 is the reducing-end activity and is distinct from non-reducing-end
3.2.1.91. Do not adopt the erroneous/obsolete 3.2.1.174 occasionally repeated
in secondary sources.

For the requested family coverage, Co and Hug's classification table maps
cellulase activities across GH5, GH6, GH7, GH9, and GH48, but also warns that
“sequence similarity does not necessarily indicate shared function”
([DOI 10.1128/AEM.01928-20](https://doi.org/10.1128/AEM.01928-20)). This is
why the activity nodes above should carry the causal edges, while GH family
membership remains a verified family annotation rather than a claimed
activity.

## 2.7 Cell-surface anchoring — **belongs only as taxon-specific cellulosome branches**

SLH-mediated noncovalent S-layer/cell-wall attachment in
*A. thermocellus* and sortase-mediated covalent attachment in
*Ruminococcus flavefaciens* are different mechanisms. Neither should become a
generic mandatory cellulosome edge.

**Proposed nodes**

| Node | Type | Grounding |
|---|---|---|
| `SLH_domain_anchor_protein` | `GENE_OR_PROTEIN` | label-only, grounding uncertain |
| `sortase_anchored_ScaE` | `GENE_OR_PROTEIN` | label-only, grounding uncertain; taxon-specific |
| `bacterial_cell_surface` | `CELLULAR_LOCALIZATION` | label-only, grounding uncertain |

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `SLH_domain_anchor_protein —attaches to→ bacterial_cell_surface` | [DOI 10.1128/MMBR.69.1.124-154.2005](https://doi.org/10.1128/MMBR.69.1.124-154.2005): “noncovalent attachment of the protein to peptidoglycan” |
| `SLH_domain_anchor_protein —anchors→ cellulosome` | [DOI 10.1128/MMBR.69.1.124-154.2005](https://doi.org/10.1128/MMBR.69.1.124-154.2005): “anchor cellulosomes or free enzymes” |
| `sortase_anchored_ScaE —anchors→ cellulosome` | [DOI 10.1128/JB.187.22.7569-7578.2005](https://doi.org/10.1128/JB.187.22.7569-7578.2005): “ScaE appears to play a role in anchoring the cellulosomal complex” |
| `sortase_anchored_ScaE —attaches to→ bacterial_cell_surface` | [DOI 10.1128/JB.187.22.7569-7578.2005](https://doi.org/10.1128/JB.187.22.7569-7578.2005): “sortase-mediated attachment to the bacterial cell wall.” |

Add taxon notes to every such edge. A generic node called “cell-surface
anchoring” would obscure rather than clarify these alternatives.

## 2.8 Adhesion and biofilm formation on cellulose — **optional, strategy-specific branch**

Direct attachment can improve substrate access and retention of enzymes and
hydrolysis products. It is important in several cellulolytic bacteria, but it
is not required for all microbial cellulolysis; some aerobic organisms
degrade cellulose without obligate contact.

**Proposed nodes**

| Node | Type | Grounding |
|---|---|---|
| `adhesion_to_cellulose` | `BIOLOGICAL_PROCESS` | label-only, grounding uncertain |
| `cellulose_associated_biofilm` | `BIOLOGICAL_PROCESS` | label-only, grounding uncertain |

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `adhesion_to_cellulose —promotes→ cellulose_associated_biofilm` | [DOI 10.1186/2191-0855-1-30](https://doi.org/10.1186/2191-0855-1-30): “degradation of either regenerated or natural cellulose was synchronized with biofilm formation” |
| `cellulose_associated_biofilm —promotes→ cellulolysis_trait` | [DOI 10.1186/2191-0855-1-30](https://doi.org/10.1186/2191-0855-1-30): “only the areas of cellulose surface colonized … were significantly degraded” |

These observations concern *Caldicellulosiruptor obsidiansis* and
*C. thermocellum* and should be marked taxon/assay-specific. The branch should
not be inserted into the mandatory shortest path from cellulose to products.

## 2.9 Regulation beyond CcpA/CRE — **belongs as explicit taxon-specific branches**

### RsgI/alternative sigma-I sensing in *A. thermocellus*

**Proposed nodes**

| Node | Type | Grounding |
|---|---|---|
| `RsgI_anti_sigma_sensor` | `GENE_OR_PROTEIN` | label-only, grounding uncertain; taxon-specific family |
| `sigma_I_factor` | `GENE_OR_PROTEIN` | label-only, grounding uncertain |
| `celS` | `GENE_OR_PROTEIN` | a taxon-specific gene; do not assign a taxon-agnostic UniProt |

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `cellulose —induces expression of→ sigma_I_factor` | [DOI 10.1073/pnas.1012175107](https://doi.org/10.1073/pnas.1012175107): “in the presence of cellulose and xylan” |
| `RsgI_anti_sigma_sensor —regulates availability of→ sigma_I_factor` | [DOI 10.1073/pnas.1012175107](https://doi.org/10.1073/pnas.1012175107): “anti-σI factors to their corresponding σ factors” |
| `sigma_I_factor —activates transcription of→ celS` | [DOI 10.1073/pnas.1012175107](https://doi.org/10.1073/pnas.1012175107): “promoter of celS” |

The complete signal-transduction sequence (substrate binding causing RsgI–SigI
dissociation) is a mechanistic model with experimental support for individual
parts; mark the release step **inferred**, not directly observed as a universal
event. The earlier RsgI-domain work also found this architecture to be highly
restricted among the genomes examined
([DOI 10.1111/j.1574-6968.2010.01997.x](https://doi.org/10.1111/j.1574-6968.2010.01997.x)).

### Cellobiose-responsive two-/three-component sensing in
*Ruminiclostridium cellulolyticum*

**Proposed nodes:** `CuaD_cellobiose_binding_protein`,
`CuaSR_two_component_system`, and `cuaABC_cbpA_genes`, all
`GENE_OR_PROTEIN`, label-only, taxon-specific.

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `cellobiose —binds→ CuaD_cellobiose_binding_protein` | [DOI 10.3390/microorganisms11071732](https://doi.org/10.3390/microorganisms11071732), PMID [37512904](https://pubmed.ncbi.nlm.nih.gov/37512904/): “CuaD … specifically binds to cellobiose” |
| `CuaD_cellobiose_binding_protein —signals through→ CuaSR_two_component_system` | [DOI 10.3390/microorganisms11071732](https://doi.org/10.3390/microorganisms11071732), PMID [37512904](https://pubmed.ncbi.nlm.nih.gov/37512904/): “forms a three-component system with CuaS and CuaR” |
| `CuaSR_two_component_system —activates→ cuaABC_cbpA_genes` | [DOI 10.3390/microorganisms11071732](https://doi.org/10.3390/microorganisms11071732), PMID [37512904](https://pubmed.ncbi.nlm.nih.gov/37512904/): “triggers the expression of the cuaABC-cbpA genes” |

This paper supports **cellobiose** sensing, not direct sensing of crystalline
cellulose. The proposed receptor-complex geometry is partly in silico, so do
not turn that structural model into an unqualified edge.

## 2.10 Downstream glycolysis, fermentation, and cross-feeding — **glycolytic entry belongs; products and ecology are optional context**

The core trait graph should reach assimilable intracellular hexose/hexose
phosphate and optionally glycolysis. Specific fermentation end products depend
on taxon, redox state, pH, growth rate, and culture conditions. Community
cross-feeding belongs in an ecological context branch rather than the defining
cellulolysis path.

**Proposed nodes**

| Node | Type | Grounding |
|---|---|---|
| `glycolysis` | `PATHWAY` | `GO:0006096` |
| `phosphoglucomutase_activity` | `MOLECULAR_FUNCTION` | pending `EC:5.4.2.2` after EC-prefix support |
| `glucose_6_phosphate` | `CHEMICAL` | label-only, grounding uncertain |
| `fermentation_products` | `CHEMICAL` or separate concrete chemicals | label-only as a grouping node; concrete ChEBI IDs should be verified individually |
| `noncellulolytic_rumen_bacteria` | no clean current schema type | label-only context node would require curator judgment; a taxon/community node type is absent |
| `cross_feeding` | `BIOLOGICAL_PROCESS` | label-only, grounding uncertain |

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `phosphoglucomutase_activity —converts→ glucose_1_phosphate` | [DOI 10.1186/s13068-016-0697-5](https://doi.org/10.1186/s13068-016-0697-5): “Glucose-1-phosphate is further converted” |
| `phosphoglucomutase_activity —produces→ glucose_6_phosphate` | [DOI 10.1186/s13068-016-0697-5](https://doi.org/10.1186/s13068-016-0697-5): “to the glycolytic intermediate glucose-6-phosphate” |
| `glucose_6_phosphate —feeds into→ glycolysis` | [DOI 10.1186/s13068-016-0697-5](https://doi.org/10.1186/s13068-016-0697-5): “glycolytic intermediate glucose-6-phosphate” |
| `glycolysis —produces through fermentation→ ethanol_acetate_lactate` | [DOI 10.1128/AEM.70.3.1563-1569.2004](https://doi.org/10.1128/AEM.70.3.1563-1569.2004): “ethanol, acetic acid, and lactic acid as products” |
| `cellodextrin —supports cross-feeding of→ noncellulolytic_rumen_bacteria` | [DOI 10.1128/aem.49.3.572-576.1985](https://doi.org/10.1128/aem.49.3.572-576.1985), PMID [3994365](https://pubmed.ncbi.nlm.nih.gov/3994365/): “increase the possibility that cross-feeding occurs in the rumen” |

The fermentation edge is *A. thermocellus* culture-specific. The cross-feeding
edge is rumen-specific. Neither should define cellulolysis across fungi,
aerobic bacteria, and anaerobes.

## 2.11 Fungal versus bacterial and free-enzyme versus cellulosomal strategies — **belongs as alternative strategy branches**

The graph description mentions free enzymes, but its structure only represents
cellulosomes. At minimum it should have two alternative strategy nodes.

**Proposed nodes**

| Node | Type | Grounding |
|---|---|---|
| `noncomplexed_secreted_cellulase_system` | `GENE_OR_PROTEIN` | label-only; system-level concept |
| `cellulosomal_cellulase_system` | `GENE_OR_PROTEIN` | `GO:0043263` applies to the complex, not the strategy as a whole |
| `aerobic_fungal_bacterial_strategy` | `BIOLOGICAL_PROCESS` | label-only |
| `anaerobic_cellulosomal_strategy` | `BIOLOGICAL_PROCESS` | label-only |

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `noncomplexed_secreted_cellulase_system —enables→ cellulolysis_trait` | [DOI 10.1128/MMBR.66.3.506-577.2002](https://doi.org/10.1128/MMBR.66.3.506-577.2002), PMID [12209002](https://pubmed.ncbi.nlm.nih.gov/12209002/): “‘free’ cellulases” |
| `cellulosomal_cellulase_system —enables→ cellulolysis_trait` | [DOI 10.1128/MMBR.66.3.506-577.2002](https://doi.org/10.1128/MMBR.66.3.506-577.2002), PMID [12209002](https://pubmed.ncbi.nlm.nih.gov/12209002/): “complexed cellulase systems” |

Do not encode “aerobic = always free” or “anaerobic = always cellulosomal.”
The review presents predominant strategies and exceptions. Some anaerobic
fungi have cellulosome-like complexes, and some bacteria combine free and
tethered enzymes.

## 2.12 Enzyme synergy and processivity — **belongs in the core catalytic cascade**

Endoglucanases create accessible chain ends; processive exo-acting enzymes
then release cellobiose. Their combined activity can exceed additive
expectations. Processivity is an enzyme property, not a synonym for every
cellobiohydrolase.

**Proposed nodes**

| Node | Type | Grounding |
|---|---|---|
| `new_cellulose_chain_ends` | `STATE` | label-only, grounding uncertain |
| `endo_exo_synergy` | `BIOLOGICAL_PROCESS` | label-only, grounding uncertain |
| `cellobiohydrolase_processivity` | `QUALITY` | label-only, grounding uncertain |

**Proposed edges**

| Subject–predicate–object | Evidence |
|---|---|
| `endoglucanase_activity —produces→ new_cellulose_chain_ends` | [DOI 10.1128/AEM.02706-13](https://doi.org/10.1128/AEM.02706-13), PMID [24162578](https://pubmed.ncbi.nlm.nih.gov/24162578/): “synergistic activities of enzymes with complementary properties” |
| `new_cellulose_chain_ends —increase substrate for→ cellobiohydrolase_activity` | [DOI 10.1021/acscatal.2c02377](https://doi.org/10.1021/acscatal.2c02377): “enhanced local density of accessible chain ends brought about by endolytic activity” |
| `endoglucanase_activity —participates in→ endo_exo_synergy` | [DOI 10.1128/AEM.02706-13](https://doi.org/10.1128/AEM.02706-13), PMID [24162578](https://pubmed.ncbi.nlm.nih.gov/24162578/): “synergism between a processive endocellulase … and an exocellulase” |
| `cellobiohydrolase_activity —participates in→ endo_exo_synergy` | [DOI 10.1128/AEM.02706-13](https://doi.org/10.1128/AEM.02706-13), PMID [24162578](https://pubmed.ncbi.nlm.nih.gov/24162578/): “synergism between a processive endocellulase … and an exocellulase” |
| `endo_exo_synergy —promotes→ cellulose_hydrolysis` | [DOI 10.1021/acscatal.2c02377](https://doi.org/10.1021/acscatal.2c02377): “spatiotemporally coordinated activity of endo- and exoenzymes” |

The *Thermobifida fusca* GH9/GH48 result is taxon- and enzyme-pair-specific,
but the general endo/exo synergy is supported across systems. Retain the
specific experiment in evidence notes.

# 3. RELEVANCE / SCOPE

## 3.1 What belongs here versus parent or sibling traits

Keep in `cellulolysis`:

- cleavage of beta-1,4-glucan/cellulose;
- cellulose-active endoglucanase, cellobiohydrolase, beta-glucosidase, and
  LPMO activities;
- cellulose-targeting CBMs;
- cellulolysis-specific transport and intracellular fate of cellodextrins;
- cellulose/cellobiose-responsive regulation when taxon-qualified;
- substrate crystallinity/accessibility as a kinetic modifier;
- alternative free-enzyme, surface-associated, and cellulosomal strategies.

Move or link rather than duplicate:

- Generic “lignocellulose-catabolic genes,” generic plant-cell-wall
  deconstruction, and nonspecific secretome regulation belong on
  `traitmech:000110` (biopolymer degradation) or a lignocellulose-level parent.
- Xylanases, xylan-responsive regulons, hemicellulose removal, and
  xylan-specific dockerin-bearing enzymes belong in `xylan_degradation`,
  although a cellulolysis record may cite them as contextual accessibility
  factors.
- Laccases, lignin peroxidases, manganese peroxidases, and lignin removal
  belong in `lignin_degradation`. Lignin-mediated nonproductive cellulase
  adsorption is relevant as context, but lignin chemistry should not expand
  this graph into a whole lignocellulose graph.
- Fermentation end products and community cross-feeding are downstream context,
  not defining steps. A short link to glycolytic entry is useful; a complete
  fermentation network should live elsewhere.

Cellulosomes can contain xylanases and other plant-polysaccharide enzymes.
Therefore “is in a cellulosome” is not by itself evidence that an enzyme belongs
in the cellulolysis graph.

## 3.2 The current CCR edge

`carbon catabolite repression -> represses ->
cellulolytic/lignocellulose-catabolic genes` is not sufficiently specific.
Three problems coincide:

1. The object label conflates cellulose-specific and broader lignocellulose
   regulons.
2. The mechanism and preferred signal differ among organisms.
3. The cited source is review-level and its wording is broader than the graph's
   claimed microbial generality.

The high-confidence replacement is:

`CRE-dependent carbon catabolite repression —represses→
C. cellulolyticum cip-cel operon`

Evidence: [DOI 10.1128/JB.01160-07](https://doi.org/10.1128/JB.01160-07),
PMID [18156277](https://pubmed.ncbi.nlm.nih.gov/18156277/): “completely
abolished the catabolite repression.”

Connect the operon to the mechanism:

`C. cellulolyticum cip-cel operon —encodes→ scaffoldin and major cellulases`

Same evidence: “major cellulase Cel48F.”

Both edges must be taxon-specific. If the project wants a cross-taxon
regulatory summary, it should be represented as an uncertain generalization
supported by multiple independent taxa, not by this one edge.

## 3.3 Balance

The graph is unbalanced. Three of ten edges (30%) describe
scaffoldin/cohesin/dockerin architecture, while the graph has:

- no cellodextrin product edge from endo/exo catalysis;
- no edge producing cellobiose from a cellobiohydrolase;
- no transport;
- no phosphorolysis;
- no LPMO;
- no CBM targeting;
- no inhibition;
- no chain-end/synergy representation.

Cellulosomes are a well-studied but phylogenetically restricted solution.
Lynd et al. explicitly distinguish noncomplexed systems of aerobic fungi and
actinomycetes from complexed systems of several anaerobic lineages
([DOI](https://doi.org/10.1128/MMBR.66.3.506-577.2002)). The graph should not
use the depth of architectural knowledge as a proxy for prevalence.

A balanced compact graph would devote most core edges to substrate
deconstruction and soluble-product fate, then represent cellulosomes and free
enzymes as parallel implementation branches. Cohesin/dockerin detail can remain
in a nested strategy subgraph, but should not dominate the only graph.

## 3.4 Dangling subgraphs and connecting edges

The dangling clusters are a material curation problem, not merely a rendering
issue. They cannot contribute to a causal path from cellulose to the trait or
products.

### Connect the cellulosome cluster

| Proposed edge | Evidence |
|---|---|
| `cellulosome —has catalytic component→ cellulase_activity` | [DOI 10.1128/MMBR.66.3.506-577.2002](https://doi.org/10.1128/MMBR.66.3.506-577.2002): “cellulases presented on the cellulosome” |
| `cellulosome —enables→ cellulolysis_trait` | [DOI 10.1128/MMBR.66.3.506-577.2002](https://doi.org/10.1128/MMBR.66.3.506-577.2002): “hydrolyzing microcrystalline cellulose” |
| `cellulosomal_CBMs —bind→ cellulose` | [DOI 10.1107/S174430911301614X](https://doi.org/10.1107/S174430911301614X): “binding of the cellulosome enzyme complex to the substrate cellulose” |

The first two are the minimum necessary. The third explains physical targeting.

### Connect the regulation cluster

Use one or both explicitly scoped branches:

| Proposed edge | Evidence |
|---|---|
| `CRE-dependent_CCR —represses→ C._cellulolyticum_cip-cel_operon` | [DOI 10.1128/JB.01160-07](https://doi.org/10.1128/JB.01160-07): “carbon catabolite repression mechanism” |
| `C._cellulolyticum_cip-cel_operon —encodes→ scaffoldin_and_cellulases` | [DOI 10.1128/JB.01160-07](https://doi.org/10.1128/JB.01160-07): “major cellulase Cel48F” |
| `A._thermocellus_sigma-I —activates transcription of→ celS_GH48_cellulase` | [DOI 10.1073/pnas.1012175107](https://doi.org/10.1073/pnas.1012175107): “promoter of celS” |
| `celS_GH48_cellulase —participates in→ cellulosome` | [DOI 10.1128/MMBR.69.1.124-154.2005](https://doi.org/10.1128/MMBR.69.1.124-154.2005): “major component of the cellulosome complex” |

Do not connect CCR directly to the generic trait with a negative edge; connect
it to the specific genes/operon whose expression is measured.

# 4. PRIORITIZED RECOMMENDATIONS

## High-confidence changes

1. **Fix the cellulosome node type immediately.** Change
   `CELLULAR_LOCALIZATION` to `GENE_OR_PROTEIN`; retain `GO:0043263`. This is a
   clear schema/policy correction.
2. **Replace the trait-to-glucose shortcut.** Remove or deprecate
   `cellulolysis_trait —produces→ glucose`. Represent cellulose → shorter
   cellodextrins/cellobiose → either hydrolytic glucose or transport plus
   phosphorolysis. This corrects both trait/process semantics and anaerobic
   biology.
3. **Ground cellobiose.** Add `CHEBI:17057`.
4. **Retype activity-grounded enzyme nodes.** If `GO:0008422` and
   `GO:0008810` are the intended groundings, use `MOLECULAR_FUNCTION` nodes.
   If proteins are intended, keep separate protein/family nodes with
   InterPro/Pfam groundings.
5. **Split cellobiohydrolase activity by chain end.** Add EC 3.2.1.91
   (non-reducing) and EC 3.2.1.176 (reducing), with a schema prefix change
   before committing EC CURIEs. Add cellobiose product edges.
6. **Add the missing anaerobic product-fate branch.** Cellodextrin ABC
   transport, cellodextrin phosphorylase, cellobiose phosphorylase, and
   glucose-1-phosphate are essential for a representative microbial graph.
7. **Connect the cellulosome to catalysis.** At minimum add
   `cellulosome —has catalytic component→ cellulase activity` and
   `cellulosome —enables→ cellulolysis`.
8. **Replace generic CCR with taxon-specific evidence.** Use CRE-dependent
   repression of the *C. cellulolyticum* `cip-cel` operon, and connect that
   operon to scaffoldin/Cel48F. Drop “lignocellulose-catabolic genes” from this
   cellulose-specific graph.
9. **Add LPMO and CBM branches.** These are central to contemporary mechanisms,
   especially aerobic free-enzyme systems. Keep AA9/AA10 and CBM grounding
   label-only until family identifiers are verified.
10. **Add chain-end generation, endo/exo synergy, and product inhibition.**
    These turn a list of enzymes into a causal catalytic cascade.

## High-confidence moves or reductions

11. **Reduce architectural over-weighting.** Retain scaffoldin,
    cohesin/dockerin binding, and one anchoring path, but move detailed
    architecture to a cellulosomal-strategy subgraph if the graph must remain
    compact.
12. **Move broad lignocellulose regulation and chemistry.** Generic
    lignocellulose genes belong at the parent level; xylan and lignin chemistry
    belong in sibling traits.
13. **Keep fermentation and cross-feeding contextual.** Link to glycolytic
    entry in the core; place specific products and rumen/gut cross-feeding in
    taxon/environment subgraphs.

## Changes needing curator judgment

14. **Choose whether nodes represent activities or enzyme families.** A fully
    normalized activity-centered graph is ontologically cleaner, but it may
    differ from conventions elsewhere in TraitMech. Do not mix GO MF groundings
    with protein-family semantics in one node.
15. **Decide whether to extend the schema.** A `PROTEIN_COMPLEX` and
    `GENE_SET/OPERON` type would avoid forcing cellulosomes and operons into
    `GENE_OR_PROTEIN`. Under the current schema, the grounding policy already
    makes `GENE_OR_PROTEIN` the correct choice for a complex.
16. **Decide how much taxon-specific regulation belongs in the generic graph.**
    RsgI/SigI, CuaDSR, CRE/CCR, SLH anchors, and sortase/ScaE are well supported
    but not universal. They should be visibly marked as alternative
    taxon-specific branches, or split into exemplar-specific graphs.
17. **Treat crystallinity as a qualified modifier.** Add it if the graph is
    intended to include rate controls; keep the assay/substrate caveat because
    crystallinity and accessibility are not cleanly separable in all studies.
18. **Verify family/domain CURIEs in a dedicated pass.** Do not guess one
    InterPro/Pfam identifier for generic CBMs, bacterial/fungal dockerins, AA9,
    AA10, or the diverse GH families. Family-level nodes are less important
    than getting the verified GO/EC activities and chemistry correct.

## Suggested minimal revised backbone

The shortest balanced causal backbone would be:

`cellulose`
→ *(endoglucanase and/or cellulose-active LPMO; CBM targeting)*
→ `new/oxidized chain ends and cellodextrins`
→ *(reducing- and non-reducing-end cellobiohydrolases)*
→ `cellobiose`
→ either:

- `beta-glucosidase activity → glucose`, or
- `ABC transport → cytoplasm → cellobiose/cellodextrin phosphorylase →
  glucose + glucose-1-phosphate`.

Both `noncomplexed secreted cellulase system` and `cellulosome` should connect
to this backbone as alternative implementations. Product inhibition,
crystallinity/accessibility, surface adhesion, and taxon-specific regulation
should enter as modifiers rather than replace the core path.

## Source-quality note

Primary experiments were preferred for causal edges; major reviews were used
for cross-taxon architecture and strategy claims. Every proposed edge above
has a DOI and, where available, a PMID plus a short verbatim support fragment.
Taxon-specific, assay-specific, and inferred statements are explicitly marked.
No repository file was modified for this audit.
