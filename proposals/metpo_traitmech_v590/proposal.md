# Behavioral Habituation

## Context And Scope

One Scope-A physiological CLASS, `traitmech:000714`, proposed as
`METPO:1066700`: **behavioral habituation**. Scope B and C each have zero
rows; no relation or workflow-enum lift is needed.

A physiological phenotype in which repeated stimulation produces an
experience-dependent decrease in a microbial organism's behavioral response
that is not attributable solely to sensory adaptation or motor fatigue.

This is a reusable organism-level behavioral phenotype, not a gene, receptor
model, assay column, one-off observation, or all learning and memory. The
record remains `PROPOSED`. No canonical taxa, causal graph, protein examples,
exact synonyms or external-equivalence mappings are asserted. No SSSOM file
is emitted. The pinned ontology and existing trait records are unchanged.

## Evidence And Limits

- [Boisseau et al. 2016](https://doi.org/10.1098/rspb.2016.0446),
  PMID:27122563, PMC4855389: cultured Physarum repellent-bridge experiments.
  The Results excerpt reports reduced aversive behavior after repeated
  exposures. Alternate-repellent tests and qualified recovery support the
  behavioral interpretation; latency, crossing time and shape are distinct.
- [Rajan and Marshall 2025](https://doi.org/10.1016/j.cub.2025.05.071),
  PMID:40562036, PMC13499368: experimental Stentor contraction responses in
  Figure 4F, not its adjacent simulation. Responses to stronger stimuli
  persist. The caption/control-cadence discrepancy remains unresolved.
- [Rajan et al. 2026](https://doi.org/10.1016/j.cub.2026.03.080),
  PMID:42025171, PMC13192338: drug-treated contraction assays, with dose,
  pretreatment, timing and off-target limitations. This shares a laboratory
  with the 2025 study, not an independent replication.
- [Rankin et al. 2009](https://doi.org/10.1016/j.nlm.2008.09.012),
  PMID:18854219, PMC2754195: a consensus review for operational terminology,
  not a microbial experiment or evidence of microbial nervous systems.

Four short contiguous snippets were matched directly to retained full text;
the native abstract resolver is a separate check. No abstract-verification
baseline exception is introduced. Source locators, hashes, versions,
acquisition receipts, source-reading scope and actual verifier outcomes are in
the [source sidecar](../../research/traits/physiology/behavioral_habituation-source-verification.json).

The public 2016/2009 PDFs and 2025/2026 PMC author manuscripts are not asserted
equivalent to current corrected publisher versions. Actual main figures and
relevant Methods were inspected, not all supplements or raw data. Supplement
requests returning HTML were not counted as PDFs. Bounded MED/Crossref checks
do not prove notice absence. Conditions and unresolved source discrepancies
remain beside each record excerpt. No raw-data or simulation reanalysis was
performed, and full articles are not redistributed.

## Identity And Hierarchy

`METPO:1000059` phenotype is the conservative parent; its exact identity,
definition and hierarchy are guarded by the writer. Chemotaxis is not a
parent of every behavioral assay. Carbon-source memory (`traitmech:000706`),
acquired stress-resistance memory (`traitmech:000712`), enhanced transcriptional
reactivation memory (`traitmech:000713`), anticipation, bet hedging and nutrient
adaptation have different defining endpoints. No existing record needs
reparenting or a synonym/causal-node migration for this scoped addition.

Repeated response decrement alone is not enough: assay-specific alternatives
include sensory adaptation, motor fatigue, injury, toxicity, selection and
depletion. Specificity and recovery are operational support, not a complete
mechanism. Rankin's neural framing and Rajan's cellular-adaptation terminology
are explicitly distinguished; the behavioral definition does not forbid
shared intracellular machinery. No universal curve, duration, complete
recovery, dishabituation, or demonstration of all ten hallmarks is imposed.
Response to a stronger stimulus is not itself dishabituation of the original
response. Cultured/selected cells are qualified evidence, not species-wide
natural canonical examples.

Pinned and current inspected METPO graphs contain deprecated neighbors
`METPO:1000004` adaptation, `METPO:1000005` adaptive trait, `METPO:0000248` and
`METPO:000249` Microbial Adaptation, below ObsoleteClass with OMO:0001000 and
no inspected replacement/consider annotations. Their original historical
scopes remain unresolved. [METPO #521](https://github.com/berkeleybop/metpo/issues/521)
disputes the mechanically assigned reasons. This phenotype is accepted
independently from primary evidence, not by reviving those terms, asserting
historical nonequivalence or inferring biological invalidity. Three OPEN
discussions preserve hierarchy, evidence/mechanism and historical-identity gaps.

## Novelty And Reservation

Post-audit confirmation: `2026-10-13T04:41:26Z`, against main
`1e4d8170d36324d781ac3d8c29897ff7d1376936`. A prior temporary note quoted a
pre-completion clock read at 04:38:50Z; that is not the allocation timestamp.

Ignored and hidden current files were included. Expanded lexical checks
covered 33 available local locations (22 registered paths and 11 independent
copies) and 908 pending/upstream full-file entries, with no matches or binary
limits. Prunable registrations are not claims of complete usable worktrees.
Earlier bounded tracked-history, PR-title/body, ontology-literal, six-template
and live 1,108-record semantic checks remain separate; 17 neighboring records
were read for scope. These are bounded absence checks, not universal novelty.

Paginated open/draft changes cover TraitMech #1782, #1476, #973 and draft #924;
CommunityMech draft #935; and METPO #644, #643, #641, #640, #638 and #629.
Full nonremoved blobs were checked against current head/blob identities and
SHA-256; gzip text was decompressed. Removed content, unchanged PR files and
unavailable ignored historical bytes are not reconstructed. Current upstream
METPO main was `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`; pinned RDF is unchanged.

The allocation audit checked 9,291 interval occurrences. Two bare-number hits
were explicitly adjudicated: `-1.1066754` is an embedding coordinate for
`METPO:1000609` in draft #924; `beilstein:1066722` is a chemical identifier in a
KG-Microbe mapping, not a METPO identifier. Ten `1000000-1999999` overlaps are
formal editor-namespace envelopes or prior documentation of those envelopes,
not competing block reservations. Narrower reserved and retired ranges stayed
checked. No conflicting reservation remained in the inspected scope.

Recheck current main and pending heads before publication. These checks do
not eliminate concurrent-allocation races. Symlink directories and arbitrary
archives were not expanded; historical Git trees omit unavailable ignored
and untracked material. Discovery remains active, not exhausted.

## ID Space And Files

- Local identifier: `traitmech:000714`.
- Cohort: `metpo_traitmech_v590`.
- Reserved block: `METPO:1066700`-`METPO:1066799`.
- Only populated placeholder: `METPO:1066700`, not a released identifier.
- Subset: `metpo_traitmech_2026_10`.

| Artifact | Rows |
| --- | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class plus two 11-column headers |
| `proposal.md` | Reviewer narrative |
| Property and SSSOM templates | Not emitted; zero proposed relations/mappings |

This block is separate from CommunityMech v1's 1007100-1007220 range. Required
blank trailing ROBOT cells are preserved. DOI citations and the TraitMech
record path are provenance, not external ontology alignments. Curator: codex.

## Verification And Upstream Path

Required before publication: strict/schema validation, record snippet check,
proposal verification, ROBOT/ELK with parsed RDF parent/IRI checks, generated
artifact freshness, repository QC, full tests, append-only histories and saved
adversarial review. Results must come from actual commands, not this checklist.

After curator sign-off, submit the TSV and evidence narrative to
berkeleybop/metpo or the KG-Microbe mapping workflow. If upstream adopts an
equivalent class, a separately reviewed pinned-release refresh and migration
must preserve local-ID provenance and incoming references while reseeding the
released METPO class. The placeholder is not permission to silently replace
the local ID, reinterpret its biology or promote mapping status.

## Change Log

- 2026-10-13, v590: one proposed behavioral-habituation class, guarded writer,
  qualified evidence and explicit reservation adjudication.
