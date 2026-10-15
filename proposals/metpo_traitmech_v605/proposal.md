# Cellular Contraction

## Scope

Propose `METPO:1068200`, **cell body or cytoplasmic projection contraction**,
for `traitmech:000729` (`PHYSIOLOGY`, `CLASS`, `PROPOSED`).

Definition: A physiological phenotype in which a microbial cell actively
contracts its body or a cytoplasmic projection, reducing its length or extension.

Scope A contains one new class and two coupled child-parent repairs. Scopes B
and C contain no predicates or schema-enum lifts. This is an observable
microbial phenotype, not a protein, sequence feature, organelle or assay row.
No exact synonyms, xrefs, SSSOM mapping, canonical taxa or causal graph are added.

## Hierarchy

The new class is below active phenotype `METPO:1000059`, whose parent is quality
`METPO:1000188`. Motility `METPO:1000701` and motile `METPO:1000702` concern
locomotion, which need not establish shortening. Require a body or cytoplasmic
projection endpoint: extracellular pilus retraction, injection-system contraction,
contractile-vacuole cycling, cytokinetic constriction alone, passive osmotic
shrinkage, death-associated shortening and static small-cell morphology do not
establish it. Generic force production or isometric contractility is broader;
the label is qualified and no exact generic-contractility synonym is asserted.

The same branch refines the direct parents of two accepted narrower phenotypes:

| Child | Historical Placeholder | Emitted Additional Upstream Axiom |
|---|---|---|
| rapid axopodial contraction, `traitmech:000682` | v558 `METPO:1063500` | `METPO:1063500 rdfs:subClassOf METPO:1068200` |
| cell-body contraction, `traitmech:000728` | v604 `METPO:1068100` | `METPO:1068100 rdfs:subClassOf METPO:1068200` |

These are definition-based subclass inferences, not new experiments. Historical
cohorts remain byte-preserved. Following v501, this cohort repeats each existing
child ID with the refined parent, retaining its historical label, definition,
definition-source annotations and other identity cells. The three-row template
emits both child axioms together with the new parent. No child identifier is
minted again; phenotype remains an ancestor of both children. The broader
historical phenotype assertions are compatible with the more specific axioms.

Both child definitions, excerpts and prior curation events are retained. Their
historical parent-discussion rationales remain intact. The axopodial discussion
also asked about comparable time-resolved assays: that question is carried into
the new OPEN `axopodial-contraction-assay-comparability` discussion, explicitly
linked from the resolution. Its Khan source URL is qualified with `SRC:MED`.
Independent provenance and mechanism questions remain OPEN. Stalk contraction
is a future discovery lead, not a third child allocation on this branch.

## Evidence

1. [Katoh and Naitoh 1994](https://doi.org/10.1242/jeb.189.1.163),
   `PMID:9317557`: definition authority. Scientific Abstract item 3 distinguishes
   living-cell body shrinkage from stalk coiling. The 19-word clause directly
   matches a namespace-qualified MED abstract; native `VERIFIED`. Other abstract
   items use Triton-extracted preparations. Full Methods and figures were not
   accessible after publisher 403 responses. The parent definition is a curator
   synthesis, not a verbatim quotation or universal calcium mechanism.
2. [Khan et al. 2003](https://doi.org/10.2108/zsj.20.1367), `PMID:14624035`:
   scientific Abstract opening sentence supports stimulated axopodial contraction.
   The 15-word excerpt directly matches the qualified MED abstract; native
   `VERIFIED`. Calcium dependence and reported speed remain assay-specific.
   Full Methods and figures were not accessed. Publisher HTTP 200 contained an
   access challenge, not readable paper text; non-detection of filaments is not
   proof of biological absence.
3. [Febvre-Chevalier and Febvre 1992](https://doi.org/10.1083/jcb.118.3.585),
   `PMID:1639845`, `PMCID:PMC2289557`: primary Results, printed page 588,
   Kinetics of the Contraction. The 15-word excerpt reports shortening, not
   merely data collection. Native `NOT_IN_ABSTRACT` is preserved; extracted PDF
   text and the actual typeset passage were checked. The primary PDF was obtained
   from a [Semantic Scholar mirror](https://pdfs.semanticscholar.org/20fc/996490bf001a841702e28a552eee5f6e50e7.pdf)
   after official retrieval attempts failed. Actual Figure 1 and Figures 3-6
   show specimen states and recording traces. Length was measured from head top
   to stalk base; graph axes say stalk length, not isolated cell-body length.
   Natural-seawater and artificially slowed responses remain separate. The
   percentage and initial-length sample are not universal thresholds or proof
   of independent contraction replication. Microtubule disassembly accompanies
   shortening; the study explicitly does not establish force production.

Only Katoh and the local curation record annotate the new parent definition.
Khan and Febvre provide supporting phenotype evidence, not extra definition
annotations. Source-specific calcium, speed, ATP, protein and ecological-role
claims are not generalized. Study names are not canonical taxon assertions.
Floyd 2023 was inspected as corroborating context but is not an additional
counted parent citation or a new quote here. No common sequence-derived
mechanism is asserted.

Repeated child rows retain their historical definition annotations: Khan 2003
and `DOI:10.1111/j.1550-7408.2001.tb00187.x` for rapid axopodial contraction,
and `DOI:10.1126/sciadv.add6550` for cell-body contraction. These are not added
as parent evidence or counted as new parent citations.

The [verification sidecar](../../research/traits/physiology/cellular_contraction-source-verification.json)
retains hashes, source URLs, selected sections and actual native outcomes.
Inspected MED/Crossref metadata did not expose a linked correction in the
checked fields; publisher failures preclude comprehensive notice clearance.
Full-text matching does not upgrade an abstract verdict.

## Identity And Allocation

Accepted at `2026-10-14T22:35:09Z` on clean main
`ab8be94cd147cc60bf7c5d3795abef1b3171e91a`. Reserve `traitmech:000729`,
`metpo_traitmech_v605`, and the entire **1068200-1068299** block; only
`METPO:1068200` is populated. Subset: `metpo_traitmech_2026_10`.

External review in PR #1940 prompted two bounded refinements: #1941 adds the
machine-readable child axioms, and #1942 replaces the parenthetical label with
the direct qualified phrase above. The allocation receipt retains the label at
initial acceptance; the biological definition and scope are unchanged. Existing
child IDs remain owned by their historical blocks, not by 1068200-1068299.

Ignored and hidden files were included in 199 known locations. The refreshed
reservation/bare-contraction scan checked 149 retained heads, 25,093 TraitMech
and 6,745 CommunityMech regular-file blobs with positive regex controls. Its
catalogue was stable and rechecked before allocation. The earlier novelty
history run failed its live catalogue guard during concurrent CommunityMech
work; its pinned outputs were recovered and compared with original native
receipts, not relabeled as a successful original run.

Semantic assessment covered the 1,722 unique original lexical variants at
maintained-owner level, the remote match groups, and new bare-word contexts.
Existing matches concern the two narrower children, cell size/division,
extracellular pili, vacuoles, unrelated response endpoints, taxon names,
metazoan contraction, passive water loss, lanthanide radius, tocolytic chemicals,
growth intervals or software contracts. There is no additional exact curated
parent, synonym or causal-node migration in this bounded search.

Fresh remote contents covered 13 open/draft PRs: TraitMech #1938, #1937,
#1936, #973 and draft #924; CommunityMech #2006 and draft #935; METPO #644,
#643, #641, #640, #638 and #629. All 849 nonremoved changed-file blobs and
587 selected upstream owners were checked. Main, PR heads/descriptions/draft
states and upstream heads were rechecked before allocation.

Structured numeric inspection identified two embedding components
`1.1068203`/`0.1068264` in draft #924 and a `1068235` pymongo wheel byte size
in METPO lockfiles, not term reservations. Overlapping intervals denote the
broad `1000000-1999999` editor envelope or its documentation. Full-content
proposal and remote checks, including wrapped ranges and gzip decoding,
covered 52,939 owner contexts and 2,637 unique contents without a competing
narrower reservation.

Structured RDF assessment covered the pinned/current METPO releases and
hash-verified editor conversion; no active exact shortening class was found.
Deprecated Motility `METPO:0000006`/`METPO:000006` leads to `METPO:1000701`;
deprecated Motile `METPO:0000087`/`METPO:000088` leads to `METPO:1000702`.
These related locomotion classes are not exact replacements, revived IDs or
xrefs. The ontology pin is unchanged.

Checks are bounded, not atomic reservation or literature exhaustion. Lost
ignored/untracked history, symlink targets, arbitrary archives and unchanged
PR files were not reconstructed. Refresh reservations before publication.

## Verification And Upstream Path

The three-row template uses the canonical 11-column headers checked at
KG-Microbe `b4b4cee330768083494f6f7e556314b25d75f2b6`. Run the maintained
proposal verifier and ROBOT/ELK wrapper, then inspect the emitted RDF for the
actual `https://w3id.org/metpo/` parent IRIs, both child subclass axioms and
unchanged child definition annotations. This
narrative does not claim that unrun validation or review gates passed.

After review, submit this parent-and-child template to METPO.
The placeholders are not released identifiers. On upstream acceptance and
release, separately review exact scope, update the ontology pin, re-seed and
migrate local identifiers while retaining their old spellings for traceability.
No upstream PR or human scientific sign-off is implied here.
