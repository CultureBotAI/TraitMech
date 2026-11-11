# Whole-record review of mercury tolerant

- Review: 20261021T114525Z-mercury-tolerant
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T11:35:55.640194Z
- Finished UTC: 2026-10-21T11:45:25Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Accepted local identity, contextual definition, scoped organism examples and current/archived protein metadata are supported. Two major findings concern neutral-atom grounding on the Hg(II) node and a material protein assigned a process-regulation relation. Two minors concern a nonliteral protein-anchor snippet and bounded human-acceptance attribution. All nine nodes and eight edges are covered. Seven literal references supply sixteen placements; two snippet fields are exact and one is a supported paraphrase. Positive native CH34 evidence and exact-isoform limits are retained; detailed pathogen-related regulatory biology remains unassessed.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: One entire maintained environmental TraitRecord, fully read. The 59-input capture covers nine nodes, eight edges, three label-only protein classes, one taxon-paired protein instance, three canonical examples and seven explicit AI events. Seven literal references occur in sixteen placements with three snippet fields. Parent, proposal, writer and provider inputs are context, not additional targets. Existing environmental claims receive bounded documentary review. Detailed pathogen-related regulator and engineered biosensor biology remains UNASSESSED_SCOPE; no new mechanism, molecular target, exposure condition, experimental procedure or optimization is supplied.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000016 | data/traits/environment/mercury_tolerant.yaml | maintained | mercury tolerant |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000016 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000016 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000016 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | traitmech:000016 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | traitmech:000016 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000016 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000016 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | traitmech:000016 | Actual execution at 11:36:12–13Z passed. Structural acceptance does not establish scientific support. |
| Focused strict validation | passed | True | traitmech:000016 | Actual execution at 11:36:12–14Z passed. Native validity is separate from source and imported semantic assessment. |
| Initial focused snippet invocation | failed | False | traitmech:000016 | Actual execution at 11:36:26–48Z failed with DNS errors, exit 2. No source-falsity inference follows; superseded by the successful required network retry. |
| Focused snippet network retry | passed | True | traitmech:000016 | Actual execution at 11:37:20–25Z passed: two VERIFIED and one NOT_IN_ABSTRACT. Manual full-text review identifies the third as a meaning-supported nonliteral paraphrase. |
| Reused corpus protein/taxon audit | passed | True | traitmech:000016 | B4 execution at 08:55:04–10Z passed: 719 graphs, 129 PASS, 589 NONMECHANISTIC, one protected, zero gaps and zero errors. The current target row passes with three label-only classes and one taxon-matched instance. |
| Reused corpus UniProt audit | failed | False | traitmech:000016 | Optional outside-target corpus diagnostic: B4 execution at 08:55:08–08:56:53Z exited 1 for other corpus rows. Preserve that actual failed status. The Q1L9Z3 target row at TSV line 8 has matching primary accession, status, taxon, version 124, sequence 1 and proteome; it is not a target failure. |
| Reused full-corpus QC | passed | True | traitmech:000016 | B5 actual execution at 10:21:03–10:23:38Z passed. B6 input comparison and environment readiness support scoped historical reuse, not a new B6 corpus run. |
| Current target protein metadata and archive assessment | passed | True | traitmech:000016 | Fresh official Q1L9Z3, UniSave124/history and taxonomy observations match the declared instance; retained reference-proteome identity is compatible. This documentary check is separate from the failed historical corpus command and from experimental proof. |

## Scientific And Domain Assessments

### Native checklist: local identifier, hierarchy and synonym

identity: supported. Targets: traitmech:000016.

Accepted local 000016 has no exact mercury-specific active/deprecated match in the pin. V5 child 1007615 and parent 1007611 remain proposals; broad active metal tolerance overlaps the deliberately retained parent. Parent typical efflux wording does not require every child to use efflux. RELATED_SYNONYM mercury resistant is source-backed.

### Native checklist: complete existing definition

evidence: supported. Targets: traitmech:000016.

The actual definition abstract supports inorganic/organic mercury resistance and the stated typical MerA conversion. Initial DOI-search failure is resolved by matching title, PMID and registry identity. Typical wording is not an exclusive universal mechanism or a new quantitative tolerance threshold.

### Native checklist: all three organism examples

evidence: supported. Targets: traitmech:000016.

Official taxa match species and strain labels. Native CH34 phenotype supports the Cupriavidus species/strain examples within source limits, without transferring derivative results. P. putida evidence is SP1, not all strains or catalog KT2440. Species and strain examples are distinct scopes, not automatic duplicates.

### Native checklist: all nine current nodes

grounding: concern. Targets: traitmech:000016.

Node 1 intends Hg(II) but CHEBI25195 denotes a neutral mercury atom with zero charge. Native CHEMICAL type is appropriate; the assigned identity is the error. CHEBI16170 matches elemental mercury. Other protein, process and chemical-class facets are coherent; the legacy mer_operon ID does not override its present protein label.

Node 0: local trait. Node 1: mismatched ionic ground. Nodes 2/5/7: three material protein classes. Nodes 3/8: biological processes. Node 4: supported elemental chemical identity. Node 6: optional ungrounded organomercurial class.

### Native checklist: single taxon-paired protein instance and generic class

grounding: supported. Targets: traitmech:000016.

Q1L9Z3 is the current primary MerA entry for CH34 with matching status, reference proteome, entry version 124 and sequence version 1. Archive timing agrees with stored retrieval metadata. Unreviewed computational annotation is allowed but not direct experimental proof. Three label-only classes do not require instances on every contextual branch.

### Native checklist: experimental anchor and exact entry scope

evidence: unknown. Targets: traitmech:000016.

The primary paper positively supports native CH34 resistance and a probable MerA band. A unique Q1L9Z3 assay is not established in acquired main text, but the record does not expressly claim one. Preserve the branch with that evidence-tier limitation; no additional formal finding or negative-function claim follows. The nonliteral snippet is separately assessed.

### Native checklist: all eight relation roles

consistency: concern. Targets: traitmech:000016.

Edge 7 RO2213 requires a process subject, while its subject denotes a material protein; the process object fits. Edge 1 RO2327 has compatible material-executor roles. Local challenges, mitigates and produces fit current endpoint kinds; free-text cleaves/senses need no mandatory IDs. The wrong chemical ground is one shared node finding.

Edges 0/2: local stressor/mitigation roles. Edge 1: material executor to process. Edges 3/5: local material-protein to chemical production. Edges 4/6: free-text substrate/sensing roles. Edge 7: imported process-subject mismatch, independently of unassessed detailed biology.

### Native checklist: all eight nearest-source assertions

evidence: supported. Targets: traitmech:000016.

Existing generic environmental statements have contextual support in actual abstracts, BMC introduction and official preprint pages 2–3. Nies is broad metal context; its unseen mercury-specific body wording remains unknown. Detailed edge 7 pathogen-related regulator biology is UNASSESSED_SCOPE, not validated or declared false. Formal-role assessment is separate.

Supported outcome applies to documented source identity and the stated generic context, not blanket biological certification of every edge. No new route or engineering repair is supplied.

### Native checklist: three snippets and additional notes quotation

evidence: concern. Targets: traitmech:000016.

Two snippet fields and the quoted notes phrase match actual abstracts. The protein-anchor phrase is a meaning-supported paraphrase rather than a contiguous excerpt from acquired full JATS. Its absence from the abstract alone was inconclusive; full-text comparison supports the bounded quotation-fidelity finding.

### Native checklist: seven literal references, sixteen placements and version status

evidence: supported. Targets: traitmech:000016.

All seven cited identities resolve, comprising six journal publications and one explicit preprint. The apparent preprint/journal correspondence is inferred from primary text and identity overlap, not a confirmed version link or independent replication. Current status fields and access surfaces have explicit bounds.

### Native checklist: chemical state and scope of quantitative claims

quantity: concern. Targets: traitmech:000016.

The present material distinction is Hg(II) versus neutral/elemental mercury; the wrong ground obscures that distinction. The record does not require a newly imposed dose or universal threshold. Comparative derivative and bulk-removal outcomes are not transferred to a unique native protein or every strain.

### Native checklist: whole-record and branch scope

completeness: supported. Targets: traitmech:000016.

Nine nodes, eight edges, three canonical examples, one protein instance, seven literal references, sixteen placements, three snippets and seven events are covered. One MECHANISTIC component has a taxon-paired anchor with explicit evidence limits. No token instance on every contextual branch or graph reconstruction is required.

### Native checklist: canonical species versus dataset strain

evidence: not_applicable. Targets: traitmech:000016.

Cupriavidus/CH34 have no catalog entry. P. putida has a species match, but the dataset is KT2440 and the source example SP1. No matching represented experimental strain is established, so downstream expression queries were not applied. No phenotype absence or mandatory dataset defect is inferred.

### Native checklist: current values and maintained recurrence

ownership: concern. Targets: traitmech:000016.

The wrong chemical ground is owned by the current record and retained by existing-value skipping, with no exact assignment found in captured mappings/bounded searches. Wildcard activates and the predicate writer own recurrence of the RO mismatch. Correct elemental mapping, local produces migration, protein metadata and parent retention are preserved.

### Native checklist: REVIEWED and local attribution

provenance: concern. Targets: traitmech:000016.

Seven explicit AI events document proposal, graph curation, grounding, migration and protein-instance provenance. Ignored-inclusive bounded searches do not identify current-target human acceptance. Prefix-search false positives were refined; private and remote decisions remain unassessed.

### Native checklist: actual checks, failed corpus status and focused metadata

schema: supported. Targets: traitmech:000016.

Focused validation and strict checks passed. The DNS snippet failure is retained before its successful required retry. Historical corpus UniProt exit 1 remains failed as an optional outside-target diagnostic; the target row and separate required current-target official metadata assessment match, so no target version defect or unrelated corpus-repair requirement follows. Other reused checks preserve original dates, failures, retry and skips.

## Findings

### ionic-mercury-ground: The Hg(II) node is grounded to a neutral mercury atom

major / open / confirmed; issue key: mercury-tolerant-ionic-mercury-ground.

Node 1 names mercury(2+) ion and describes reactive ionic mercury, but current CHEBI25195 denotes the neutral mercury atom with zero charge. This changes the chemical identity represented across its incident edges. The native CHEMICAL type is valid; preserve the intended ionic meaning while reconciling the identifier. Correct elemental mercury grounding on node 4 remains separate, and no new replacement chemistry is prescribed.

### regulation-subject: RO positive regulation assigns a process role to a material protein

major / open / confirmed; issue key: mercury-tolerant-regulation-subject.

Edge 7 assigns RO:0002213 to a material regulator protein as subject. The relation inherits process-to-process regulation; its transcription-process object fits, but its protein subject does not become a process because the text describes regulatory activity. This is an external semantic conflict, not native validation failure or a claim that the detailed biology is false. That biology remains UNASSESSED_SCOPE; no replacement mechanism is supplied.

### protein-quote-fidelity: The protein-anchor snippet is a supported paraphrase rather than a literal excerpt

minor / open / confirmed; issue key: mercury-tolerant-protein-quote-fidelity.

The protein-example snippet is not a contiguous quotation in the acquired main JATS, although native CH34 mercury resistance and a probable MerA band are positively supported. The comparison covers that complete acquired text, not inaccessible supplements or all versions. Treat this as bounded quotation fidelity, not fabricated biology or a disproven protein function; retain the positive evidence and exact-entry limitations.

### human-acceptance-link: Inspected local provenance does not attribute human scientific acceptance

minor / open / confirmed; issue key: mercury-tolerant-human-acceptance-link.

REVIEWED accompanies seven explicit AI maintenance events. The bounded ignored-inclusive searches and inspected provenance do not identify a human acceptance decision for this target. Maintenance history remains positive evidence. Private or remote decisions are unassessed; this is not a claim that no human review ever occurred.

## Recommended Actions And Acceptance Checks

### reconcile-chemical-identity

Reconcile the assigned ground with the existing Hg(II) meaning.

- Any retained identifier denotes the stated ionic species and agrees with label, description and incident existing claims. Preserve the separate valid elemental-mercury ground.
- Review existing-value preservation without adding new chemical routes, experimental conditions or arbitrary replacements.
- After separately authorized curation, use guarded writes, append-only record/repository history, focused validation/strict/source and applicable protein audits, maintained QC and generated-output recipes. This review makes no scientific mutation.

### reconcile-regulation-role

Reconcile the imported relation with the represented protein/process endpoint meanings.

- Any retained RO identifier meets inherited domain/range meaning. Preserve the legitimate material protein and process object rather than forcing a retype.
- Bound the change to semantic annotation and recurrence; detailed pathogen-related regulator biology remains unassessed and no mechanism reconstruction or optimization is requested.
- After separately authorized curation, use guarded writes, append-only record/repository history, focused validation/strict/source and applicable protein audits, maintained QC and generated-output recipes. This review makes no scientific mutation.

### separate-quote-and-interpretation

Use literal evidence wording or clearly label the existing supported paraphrase.

- The snippet is a verifiable contiguous source excerpt, or the existing paraphrase is moved to interpretive notes. Preserve native CH34 phenotype and probable-band support.
- Do not transfer derivative results or imply unique Q1L9Z3 isolation; retain current accurate strain/status/version metadata.
- After separately authorized curation, use guarded writes, append-only record/repository history, focused validation/strict/source and applicable protein audits, maintained QC and generated-output recipes. This review makes no scientific mutation.

### attribute-human-acceptance

Link existing human scientific acceptance or obtain it through the established process.

- Acceptance identifies revision and scope, including source-tier limits, unassessed detailed biology and semantic concerns. Preserve all seven AI events.
- Automated validation and this review do not substitute for human acceptance; reassess status if necessary.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep-006.nq5qngor/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-mercury-validate | /private/tmp/traitmech-record-sweep-006.nq5qngor/mercury-validate.log; Executed 2026-10-21T11:36:12Z through 2026-10-21T11:36:13Z; metadata mercury-validate.json | context_only | Actual execution at 11:36:12–13Z passed. Structural acceptance does not establish scientific support. |
| check-mercury-strict | /private/tmp/traitmech-record-sweep-006.nq5qngor/mercury-strict.log; Executed 2026-10-21T11:36:12Z through 2026-10-21T11:36:14Z; metadata mercury-strict.json | context_only | Actual execution at 11:36:12–14Z passed. Native validity is separate from source and imported semantic assessment. |
| check-mercury-snippets | /private/tmp/traitmech-record-sweep-006.nq5qngor/mercury-snippets.log; Executed 2026-10-21T11:36:26Z through 2026-10-21T11:36:48Z; metadata mercury-snippets.json | context_only | Actual execution at 11:36:26–48Z failed with DNS errors, exit 2. No source-falsity inference follows; superseded by the successful required network retry. |
| check-mercury-snippets-network-retry | /private/tmp/traitmech-record-sweep-006.nq5qngor/mercury-snippets-network-retry.log; Executed 2026-10-21T11:37:20Z through 2026-10-21T11:37:25Z; metadata mercury-snippets-network-retry.json | context_only | Actual execution at 11:37:20–25Z passed: two VERIFIED and one NOT_IN_ABSTRACT. Manual full-text review identifies the third as a meaning-supported nonliteral paraphrase. |
| check-corpus-protein-taxa | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log; Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json | context_only | B4 execution at 08:55:04–10Z passed: 719 graphs, 129 PASS, 589 NONMECHANISTIC, one protected, zero gaps and zero errors. The current target row passes with three label-only classes and one taxon-matched instance. |
| check-corpus-uniprot | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-uniprot.log; Executed 2026-10-21T08:55:08Z through 2026-10-21T08:56:53Z; metadata corpus-uniprot.json | context_only | Optional outside-target corpus diagnostic: B4 execution at 08:55:08–08:56:53Z exited 1 for other corpus rows. Preserve that actual failed status. The Q1L9Z3 target row at TSV line 8 has matching primary accession, status, taxon, version 124, sequence 1 and proteome; it is not a target failure. |
| check-batch005-qc | /private/tmp/traitmech-record-sweep-005.klfwsp1f/batch005-qc.log; Executed 2026-10-21T10:21:03Z through 2026-10-21T10:23:38Z; metadata batch005-qc.json | context_only | B5 actual execution at 10:21:03–10:23:38Z passed. B6 input comparison and environment readiness support scoped historical reuse, not a new B6 corpus run. |
| capture | Native selected-record capture; 59 inputs at 11:35:55.640194–11:35:57.320860Z | supports | All current captured hashes match. No additional target or uncaptured history is adopted. |
| preparation | Whole-target factual preparation; Nine nodes, eight edges, three label-only classes, one instance and seven AI events | context_only | All current fields were read. Historical target audit rows are retained separately from whole-corpus command status; parent/provider inputs are not newly claimed fully read by this preparation. |
| record | data/traits/environment/mercury_tolerant.yaml; Whole current record and all seven explicit AI events | partial | The graph has MECHANISTIC scope with a qualified, strain-paired anchor. The legacy mer_operon node ID currently labels and describes a MerA protein; it is not an operon-as-protein assertion. |
| native-policy | Native field-by-field review checklist; Identity, source scope, quoted evidence, completeness and acceptance attribution | supports | Meaning, source support and traceable human acceptance require review. Optional instances on every branch and mandatory dataset assignments are not native completeness requirements. |
| protein-policy | Native grounding policy; Lines 174–195, generic protein classes and strain-paired examples | supports | The generic label-only node and particular protein instance are separate. Unreviewed reference-proteome entries can carry required metadata; database identity does not itself prove an accession-specific experiment. |
| snippet-policy | Native curation playbook; Lines 649–650 and 673–676, contiguous verbatim snippets and interpretation | supports | A meaning-supported paraphrase belongs in interpretive notes unless replaced by an actual contiguous source excerpt. Quotation fidelity is separate from biological falsity. |
| reuse | B6 common-input comparison; Original verification 10:14:46.298715Z | supports | 1130 traits, 1278 history files and 19 common inputs match the preceding batch. Actual B5 final QC is recorded separately from this earlier comparison. |
| reuse-supplement | B5 checks and B6 readiness supplement; Original supplement 10:28:10.859819Z; B5 QC 10:21:03–10:23:38Z | supports | Original check/log hashes, failures, retry, adapter skips and environment readiness retain distinct scopes and dates. No new focused scientific certificate is implied. |
| identity | Pinned METPO and accepted local identity; Local 000016; v5 rows 14/18; active-review row 41 and release-delta row 1182 | supports | Complete pinned active/deprecated scanning found no exact mercury-specific term. The local child and proposed 1007615 remain distinct from broader METPO1007074 and the deliberately retained parent 000012. The literature-sourced RELATED_SYNONYM is conservative. |
| db-chebi25195 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/25195/; Actual official request 2026-10-21T11:36:33.820467+00:00 through 2026-10-21T11:36:34.509763+00:00 | context_only | Retained official identity/version response; interpretation is explicitly separated in the grounding and protein assessments. This is not evidence of a new biological assay. |
| db-chebi16170 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/16170/; Actual official request 2026-10-21T11:36:33.824685+00:00 through 2026-10-21T11:36:34.547425+00:00 | context_only | Retained official identity/version response; interpretation is explicitly separated in the grounding and protein assessments. This is not evidence of a new biological assay. |
| db-uniprotQ1L9Z3 | https://rest.uniprot.org/uniprotkb/Q1L9Z3.json; Actual official request 2026-10-21T11:36:33.825423+00:00 through 2026-10-21T11:36:34.509112+00:00 | context_only | Retained official identity/version response; interpretation is explicitly separated in the grounding and protein assessments. This is not evidence of a new biological assay. |
| db-uniprotQ1L9Z3-v124 | https://rest.uniprot.org/unisave/Q1L9Z3?format=txt&amp;versions=124; Actual official request 2026-10-21T11:36:34.509556+00:00 through 2026-10-21T11:36:35.423624+00:00 | context_only | Retained official identity/version response; interpretation is explicitly separated in the grounding and protein assessments. This is not evidence of a new biological assay. |
| db-uniprotQ1L9Z3-history | https://rest.uniprot.org/unisave/Q1L9Z3?format=json; Actual official request 2026-10-21T11:36:34.510064+00:00 through 2026-10-21T11:36:35.432015+00:00 | context_only | Retained official identity/version response; interpretation is explicitly separated in the grounding and protein assessments. This is not evidence of a new biological assay. |
| db-taxa119219-303-266264 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=119219,303,266264&amp;retmode=xml; Actual official request 2026-10-21T11:36:34.547761+00:00 through 2026-10-21T11:36:34.845702+00:00 | context_only | Retained official identity/version response; interpretation is explicitly separated in the grounding and protein assessments. This is not evidence of a new biological assay. |
| proteome | https://rest.uniprot.org/proteomes/UP000002429; Original access 08:55:33.028575–08:55:33.650655Z | supports | The retained CH34 reference proteome matches the declared instance and organism. Copying at 11:37Z is not a new proteome acquisition or experimental validation. |
| protein-assessment | Current and archived protein metadata assessment; Q1L9Z3 current entry and UniSave124; sequence version 1 | supports | Primary accession, MerA name, strain, unreviewed status, reference proteome and declared versions match current and historical metadata. Release timing is compatible with the stored retrieval date. Functional annotation is computational/inferred; exact isoform-specific primary experiment remains separate. |
| predicate-authority | Recursive RO semantics; Original RO2211/2213 08:04:46.869674Z and RO2327 09:52:45.989262Z; integration 11:40:27.180441Z | supports | RO2213 inherits process-to-process regulation from RO2211; a material regulator protein is not that process. The transcription object fits. RO2327 material MerA executor to reduction process is compatible. Native validity is distinct from these meanings; no OWL reasoner was run. |
| local-authority | Maintained mappings, proposal properties and writer guards; Node row 185; predicate rows 2/9/38–39/64; v2 rows 9–10; v9 row 3 | supports | The correct elemental-mercury map, local challenges/mitigates/produces roles and protein metadata allowance remain intact. Wildcard activates can recreate the RO conflict. No maintained mapping was found for the wrong ionic-mercury assignment within the captured table and bounded searches. |
| authority-reuse | Authority, catalog and proteome reuse chain; Hash verification 11:37:39.025741Z | supports | Original RO, catalog, runner, reference-proteome and KT2440 dataset times/hashes are retained. Fresh chemical, current protein/archive and taxonomy responses are separate. |
| ground-ledger | Complete documentary grounding assessment; Nine nodes, eight edges, one component and 59 matching inputs | partial | Two external semantic problems are confirmed: neutral-atom grounding on the intended Hg(II) node and a material regulator subject on a process-regulation relation. Protein metadata, other node facets and local relation roles remain supported. |
| node-edges | Complete current node and edge ledger; nodes[0–8], edges[0–7], zero-based | partial | Every endpoint resolves. The three protein classes may remain label-only; the legacy node ID is not an entity-type error. Elemental mercury grounding is valid. Formal endpoint coverage does not imply validation of detailed pathogen-related biology on edge 7. |
| owners | Maintained owner and recurrence assessment; Wrong-ground current record; node guard 156–174; predicate guard 152–176 and mapping row 64 | supports | Existing-ID skips preserve current assignments. Wildcard activates is a recurrence owner; the wrong Hg(II) identifier has no matching captured node-mapping row. Prior microbe-domain produces assignments were already replaced and are not current defects. |
| provenance | Bounded ignored-inclusive target and protein provenance; Primary search 11:37:39.039909–11:38:03.254471Z; exact refinement through 11:38:23.086330Z | partial | Seven explicit AI events document maintenance. Inspected local material does not attribute human acceptance. Initial prefix taxon matches were refined to full identifiers and did not establish other-script ownership; no targeted local saved review or repository history was identified within the bounds. |
| expression | Canonical catalog and dataset strain applicability; Catalog original 07:36:12.732638–07:36:12.858149Z; dataset metadata 08:54:17.518957–08:54:18.018420Z | context_only | Cupriavidus/CH34 have no retained catalog match. P. putida has a species entry, but its precise321 dataset is KT2440 while the canonical source is SP1. No strain transfer or downstream module query is justified; noncoverage/mismatch is not negative phenotype evidence. |
| runner | Historical bounded structured-runner discovery; Original B5 PATH/project 09:27:57.380287–09:27:57.542053Z; external 08:17:15.206671–08:17:15.338052Z | context_only | Prior discovery and the official catalog fallback are reused with original bounds. No fresh B6 or whole-machine absence claim is made. |
| source-ledger | Final source assessment; Seven literal records, sixteen placements and three snippets; finalized 11:39:48.617848Z | partial | Definition and canonical classifications have positive scoped support. Two snippet fields and an additional notes quote are literal; the protein-anchor snippet is a meaning-supported paraphrase. The accession-specific evidence limit is retained without an additional formal finding under parent adjudication. |
| placements | Complete citation-placement ledger; All sixteen placements, including synonym and protein-instance evidence | partial | Native CH34 and derivative results remain distinct; P. putida support is SP1-specific. Broad metal context is not a newly verified mercury-specific body claim. Detailed edge 7 biology remains UNASSESSED_SCOPE. |
| snippets | Complete quotation ledger; Three snippet fields plus additional quoted phrase in evidence[0].notes | partial | Two fields and the notes phrase are exact. The protein-anchor phrase is absent as a contiguous quotation from the acquired main JATS despite positive native CH34 evidence. The search covers that entire acquired text, not inaccessible supplements or all versions. |
| edge-sources | Complete eight-edge source ledger; Existing environmental claims and explicit edge 7 biology boundary | partial | Generic existing conversion and background statements have source support with study/taxon limits. Frontiers identity and generic framing are verified; detailed pathogen-related regulatory biology is not assessed or repaired. |
| protein-source-limit | Primary protein-evidence scope assessment; Native CH34 phenotype and probable band versus unique accession proof | partial | The acquired JATS supports native CH34 resistance and a probable MerA band. It does not uniquely identify or assay Q1L9Z3 in its inspected main text. The record does not expressly claim such an isolated assay, so preserve this as a scoped limitation, not an additional source-tier finding. |
| adjudication | Independent parent final adjudication; Four findings adopted at 11:40:59.100946Z after complete ledger and primary-window reading | context_only | Two grounding majors, the nonliteral protein snippet minor and bounded human-acceptance minor are adopted. Positive CH34 evidence, exact isoform limits and unassessed detailed regulator biology remain explicit; no additional evidence-tier or version finding is assigned. |
| meta-0 | DOI:10.1016/S0168-6445(03)00046-9; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Bacterial%20mercury%20resistance%20from%20atoms%20to%20ecosystems%22&amp;format=json&amp;resultType=core; actual indexed metadata/abstract | supports | Bacterial mercury resistance from atoms to ecosystems. Access scope: Actual indexed abstract plus Crossref identity. Initial DOI query0 resolved by exact-title search to PMID12829275. Publisher PDF403 and browserredirect failure; body uninspected. |
| meta-1 | PMID:12829273; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12829273+AND+SRC%3AMED&amp;format=json&amp;resultType=core; actual indexed metadata/abstract | supports | Efflux-mediated heavy metal resistance in prokaryotes. Access scope: Actual indexed abstract; general metal-efflux context. No new body acquisition claimed. |
| meta-2 | PMID:21423734; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21423734+AND+SRC%3AMED&amp;format=json&amp;resultType=core; actual indexed metadata/abstract | supports | Characterization of the metabolically modified heavy metal-resistant Cupriavidus metallidurans strain MSR33 generated for mercury bioremediation. Access scope: Actual primary JATS; introduction, native CH34 comparisons and protein-identification certainty inspected. Incidental pathogen-specific mechanisms and operational optimization unassessed. |
| meta-3 | PMID:21751007; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21751007+AND+SRC%3AMED&amp;format=json&amp;resultType=core; actual indexed metadata/abstract | supports | Characterization of a marine-isolated mercury-resistant Pseudomonas putida strain SP1 and its potential application in marine mercury reduction. Access scope: Actual indexed title/abstract for SP1 identity and mercury-resistant classification only. Virulence, stress/fitness optimization and numerical operating conditions unassessed. |
| meta-4 | DOI:10.1186/s12866-024-03391-5; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1186%2Fs12866-024-03391-5&amp;format=json&amp;resultType=core; actual indexed metadata/abstract | supports | Horizontal gene transfer of the Mer operon is associated with large effects on the transcriptome and increased tolerance to mercury in nitrogen-fixing bacteria. Access scope: Actual primary JATS; generic introduction claims and evidence type inspected. |
| meta-5 | DOI:10.21203/rs.3.rs-3854515/v1; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.21203%2Frs.3.rs-3854515%2Fv1&amp;format=json&amp;resultType=core; actual indexed metadata/abstract | supports | Adaptation to mercury stress by nitrogen-fixing bacteria is driven by horizontal gene transfer and enhanced gene expression of the Mer operon Access scope: Actual official Research Square v1 PDF, pages1–3, abstract and introductory source claims inspected. Landing and staticHTML403 retained. |
| meta-6 | DOI:10.3389/fbioe.2023.1178680; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3389%2Ffbioe.2023.1178680&amp;format=json&amp;resultType=core; actual indexed metadata/abstract | supports | Synthetic bacteria for the detection and bioremediation of heavy metals. Access scope: Actual primary JATS acquired, but assessed only documentary/general regulator framing. Detailed engineered pathogen biosensor routes UNASSESSED_SCOPE. |
| ch34-primary | PMID:21423734; Introduction paragraph 3; body 20–22, 27 and 29; Fig. 3 caption; actual 2026-10-21T11:36:44.920667+00:00 through 2026-10-21T11:36:50.163740+00:00 | partial | Native CH34 phenotype and a probable MerA band are positive evidence. Derivative results and assay-specific outcomes are not transferred; exact-entry isolation is not established. |
| bmc-primary | DOI:10.1186/s12866-024-03391-5; Introduction paragraph 1; actual 2026-10-21T11:36:44.921254+00:00 through 2026-10-21T11:36:52.240969+00:00 | partial | Existing generic conversion claims are supported background, not new all-taxon isolated-enzyme measurements. |
| preprint-primary | DOI:10.21203/rs.3.rs-3854515/v1; Official v1 PDF printed pages 1–3, especially introductory pages 2–3; actual 2026-10-21T11:38:03.595888+00:00 through 2026-10-21T11:38:06.191021+00:00 | partial | The cited existing introductory claims and preprint identity are present. No engineering route, optimization or independent replication is inferred. |
| frontiers-primary | DOI:10.3389/fbioe.2023.1178680; Documentary identity and generic framing only; body 25, caption 27 and context 30; actual 2026-10-21T11:36:44.921440+00:00 through 2026-10-21T11:36:47.030084+00:00 | partial | The review provides generic family/promoter framing. Detailed engineered pathogen biosensor and regulator-to-transcription biology is UNASSESSED_SCOPE; full XML acquisition does not imply full biological verification. |
| source-access | Actual source access boundaries; Three JATS bodies, official preprint PDF, three abstract-only works and retained failed requests | context_only | Initial definition DOI query returned zero but title/registry resolution succeeded. Definition PDF and Research Square landing/static HTML returned 403; actual PDF subsequently succeeded. Browser failures remain distinct from primary text inspected. |
| versions | Preprint and journal relationship assessment; Official PDF date/version, BMC date, overlapping authors/text and empty registry relation fields | context_only | The corresponding-study relationship is strongly inferred, not confirmed by an explicit primary version link. Preserve seven literal references and sixteen placements, but do not count the apparent versions as independent replication. Preprint status is not retraction or invalidity. |
| publication-status | Bounded current publication-status inspection; Seven indexed records and three Crossref relation/update fields | context_only | Preprint status is explicit. No corrective relation occurred in the inspected fields; this is not a globally exhaustive absence claim. Empty relationship fields neither confirm nor refute the inferred version relationship. |
| root-ch34 | Independent primary CH34 window read; Actual paragraphs 1–3, 20–21 and 27; recorded 11:37:59.186263Z | supports | Root read the retained source body and verified its hash, preserving native versus derivative and probable-band versus unique-entry distinctions. |
| root-source-read | Independent actual abstract and BMC window reads; Definition, Nies and SP1 abstracts; BMC body 0–2; recorded 11:38:57.513403Z | supports | Actual text supports the bounded definition, quotations, species/strain classification and generic background. OUP failure and unassessed pathogen/optimization content remain separate. |
| root-preprint | Independent final preprint source read; Printed page 2 and opening page 3; recorded 11:40:34.677434Z | supports | Root read actual PDF-derived primary context and verified PDF/text hashes. Existing source claims are supported; the publication-version relationship remains inferred rather than an explicit primary link. |

## Limits And Additional Notes

- Local 000016 and v5 proposal 1007615 remain distinct from the deliberately retained broad metal-tolerance parent. No forced parent migration or universal efflux requirement is inferred.
- The definition review is abstract-only but positively supports the existing typical mechanism and quotations. Initial DOI query zero was resolved by exact-title/registry identity. Nies provides broad metal context; absence of mercury in its abstract does not prove body absence.
- Native CH34 resistance and a probable MerA band are supported. Derivative MSR33 and assay-specific results remain separate; acquired main text does not uniquely identify or assay Q1L9Z3. The record does not expressly claim such an isolated assay, so no additional source-tier defect is assigned.
- Current and archived Q1L9Z3 metadata both match entry 124/sequence 1, with compatible retrieval timing and reference-proteome taxon. Computational/unreviewed annotation is not unique experimental proof, but its status alone is not a schema or anchor defect.
- P. putida classification is source-strain SP1. Its catalog species match has KT2440 data, which are not transferred to SP1 or CH34. Cupriavidus noncoverage and strain mismatch are not negative phenotype evidence; no downstream module query was performed.
- The preprint and BMC paper are strongly inferred corresponding versions, not confirmed by an explicit primary relation link. Retain seven literal references and sixteen placements without counting apparent versions as independent replication. Preprint status is not invalidity or retraction.
- The official preprint PDF pages 1–3 and BMC generic introduction support existing contextual statements. They are not new all-taxon assays. Source wording relatively inert is contextual chemistry, not a health-safety conclusion.
- Frontiers detailed engineered-pathogen biosensor and regulator biology is UNASSESSED_SCOPE. Its identity and generic framing are documented; formal RO role review neither validates nor repairs that biological route.
- Legacy mer_operon is a node identifier, while the present label/description denote a protein and operon/gene fields are metadata. Three label-only classes and one instance do not require artificial examples on all contextual branches.
- The wrong ionic chemical identifier is separate from valid CHEMICAL type and compatible local relation roles. RO2327 material-executor roles fit; only the stated RO2213 assignment has the imported process-subject conflict. No OWL reasoner execution or new mechanism is claimed.
- Two snippet fields and one additional notes quote are literal. The protein-anchor phrase is a supported paraphrase in the acquired main JATS; inaccessible supplements and every possible version were not exhaustively searched.
- Source bodies, abstract-only access, official PDF success, landing/PDF 403 and browser failures retain actual scopes and times. Acquiring a complete XML does not imply inspection or validation of all detailed biology. Publication-status fields are bounded, not a global notice-absence certificate.
- Seven AI events and ignored-inclusive local searches document maintenance but not attributed human acceptance. Initial prefix taxon matches were false positives resolved by exact refinement; private/remote decisions remain unassessed.
- The historical corpus UniProt exit 1 remains failed and optional for outside-target rows. The matching target row and fresh required current-target metadata assessment are separate; unrelated corpus repair is not required for this review. Snippet DNS failure and successful retry, B4/B5/B3/OLD dates, product failures/retry, baselines and skips remain distinct; no native corpus rerun or environment mutation occurred.
- No scientific record, mapping, history, generated output, Git or state was changed. No paid research, new molecular target, experiment, exposure condition, biological intervention or optimization is supplied.
- Four findings: two major and two minor. All indices are zero-based.
- All 59 captured hashes match; nine nodes, eight edges, three label-only protein classes, one instance, three canonical examples and seven explicit AI events are covered.
- Final source ledger 11:39:48.617848Z; grounding 11:40:27.192178Z; parent adjudication 11:40:59.100946Z. Acquisition, reuse and integration remain distinct.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T114525Z-mercury-tolerant
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of mercury tolerant
started_at: '2026-10-21T11:35:55.640194Z'
finished_at: '2026-10-21T11:45:25Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: This session did not author or modify the captured record. Separate
    agents supplied complete source and grounding ledgers. The parent read the target,
    parent context, critical primary windows and final ledgers, and reviews this builder
    before execution. AI maintenance and this review are distinct from human scientific
    acceptance.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Accepted local identity, contextual definition, scoped organism examples
  and current/archived protein metadata are supported. Two major findings concern
  neutral-atom grounding on the Hg(II) node and a material protein assigned a process-regulation
  relation. Two minors concern a nonliteral protein-anchor snippet and bounded human-acceptance
  attribution. All nine nodes and eight edges are covered. Seven literal references
  supply sixteen placements; two snippet fields are exact and one is a supported paraphrase.
  Positive native CH34 evidence and exact-isoform limits are retained; detailed pathogen-related
  regulatory biology remains unassessed.
source:
  git_revision: 8eee04a8c65609fbaff6df7c54597dcaf1b9d282
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
    role: context
  - path: .claude/skills/manage-identifiers/SKILL.md
    sha256: a5c5aaa10943ee6d15423a5878ed2189e4e0b28a5c6e09fda80ba299ab779ebb
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: bb03efa3bbd3748ee1dccf57612a6ce8fcc861f20eb57c33eb16e3ac1dd728bd
    role: context
  - path: CLAUDE.md
    sha256: 4d328127022388e1affe9b71be24bc93944a971636d0d0ea902f6511e0b405c5
    role: context
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: conf/evidence_snippet_baseline.tsv
    sha256: cbe5c82379e796446366b292f15194d80625b928119b482a67d857a379ab31a7
    role: context
  - path: data/raw/biolink-model.yaml
    sha256: 4955709e1cac1d26fd657f7a0c29d6c8390f42e41f9ebfab859c82b102f2bebb
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/environment/mercury_tolerant.yaml
    sha256: d479ef78e58a331a1a3efef7f2adc3697872fa9bbc6679f4b68d89505d4ed372
    role: target
  - path: data/traits/environment/metal_tolerant.yaml
    sha256: 907f78048e48c547d03e3b2b073216a32007a0c0608fb361fba976a3812710c5
    role: context
  - path: docs/CURATION_PLAYBOOK.md
    sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
    role: context
  - path: docs/GROUNDING_POLICY.md
    sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
    role: context
  - path: docs/PATHWAY_LINKS.md
    sha256: 800492750fb3c025dfdf7164813e7a00b3bd72dc8cc6f8e754e2aed5d7bbf414
    role: context
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 008643042a721e84f647be6beda104ae02fe616361ff9b34fc608643a7526ee2
    role: context
  - path: mappings/node_grounding.tsv
    sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
    role: context
  - path: mappings/predicate_grounding.tsv
    sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
    role: context
  - path: mappings/trait_exact_match_review.tsv
    sha256: 7728593d526d9a723716e5daad64beb7e1ab5c2e4221ae8d43dd9480cd02f62b
    role: context
  - path: mappings/uniprot_regrounding_candidates.tsv
    sha256: c36d8e038886d137d5a1ae609240e59ce74b6aeee17ae24f21b6c4a0d7407391
    role: context
  - path: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv
    sha256: 4ab5ca37ff8595210254b1099563b4425ecd737ed375dc5a932b44e2ad5c332e
    role: context
  - path: proposals/metpo_traitmech_v2/proposal.md
    sha256: fe0601356b120ef9babc6f90a417f860bf02aa628c46af661517f168e01bc48f
    role: context
  - path: proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv
    sha256: 1a1cc789782cfae195c1fc81ddaf848d06d162c7434d94cceb66838de98ab6fa
    role: context
  - path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
    role: context
  - path: proposals/metpo_traitmech_v5/proposal.md
    sha256: 5d54623dd00ac80a8d67a0eab7b70385f7f57b36daa205c28aa1f9d6f9be6167
    role: context
  - path: proposals/metpo_traitmech_v6/metpo_proposal_properties_robot.tsv
    sha256: ed877efe2d59f43c51898e2dc85440188711455dcc5c882af2dc1384fc38fc19
    role: context
  - path: proposals/metpo_traitmech_v6/proposal.md
    sha256: aecbd48fd73712ccab57619d753b6084a7fa2fbf616f80623f63ce15b65871ae
    role: context
  - path: proposals/metpo_traitmech_v7/metpo_proposal_classes_robot.tsv
    sha256: 99e779afa894363b32966bd15415417035d246970aab02931ce896f37c910a73
    role: context
  - path: proposals/metpo_traitmech_v7/proposal.md
    sha256: bc6ea10ebc4bec0f446cee92578602889ec464295ce5ecce27fed76eb06528ce
    role: context
  - path: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
    role: context
  - path: proposals/metpo_traitmech_v8/proposal.md
    sha256: 119d51e7b7194890514a9e313505212bab92aeba607f7c1b8f9d9d2edeef67e7
    role: context
  - path: proposals/metpo_traitmech_v9/metpo_proposal_properties_robot.tsv
    sha256: 5ae84dd1351a4bec39adf7bcd5b3a8982af2e95fbccd0b53c0efa3efbfc89b0e
    role: context
  - path: proposals/metpo_traitmech_v9/proposal.md
    sha256: 85fde22f4733863188b437cfcf7552a31fea07ad1d32c0400cf493295c1e1156
    role: context
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/ontology_snapshot_manifest.tsv
    sha256: 4a157279a8c4e3fc2afb5382a45c31961991bbd1f330f26d0061b0cfd0b4d213
    role: context
  - path: research/traits/environment/mercury_tolerant-deep-research-falcon.md
    sha256: a977f36798ccc1fdbf5de072cac06d98e63f0997693aea8a4f4a9858d0085c73
    role: context
  - path: scripts/audit_causal_graphs.py
    sha256: e0c26506c9de712700317284f142097e7bf69334806b8010db5d6517e905e834
    role: context
  - path: scripts/audit_graph_protein_taxa.py
    sha256: d3375861829c612483b3545dd0f5e2b79872a4576b626edc08714a09fbd9a24d
    role: context
  - path: scripts/audit_uniprot_grounding.py
    sha256: 91eb2165c69b3a4fcb53154dc8c835ac1070577f88065a43dfc881284d3d1052
    role: context
  - path: scripts/backfill_canonical_examples_444.py
    sha256: 18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c
    role: context
  - path: scripts/curate_knowledge_gaps.py
    sha256: 9e0fb7e01a901d84189a28f1912a2552f28d2da8733c113589e4947359d48c73
    role: context
  - path: scripts/finalize_metpo_2026_06_12_review.py
    sha256: b850b386183b2d86647dada43f7f157059017dbb881f7e1fb2e220ae697d3bea
    role: context
  - path: scripts/ground_causal_nodes.py
    sha256: 204ce4162544154b1752b65da2136538847ea25ced26a52f5708eadff08f5d42
    role: context
  - path: scripts/ground_causal_predicates.py
    sha256: 5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381
    role: context
  - path: scripts/migrate_disposition_typing.py
    sha256: ebafdd145fc0729d32f3b8a45f570d97a8e001838afadd698e2b246cb8950714
    role: context
  - path: scripts/migrate_enables_trait_edges.py
    sha256: a5e7965ee4f6b6ba5bae3a06bced2a83cbf755f3b9b150ce6acc0cd808cb1d88
    role: context
  - path: scripts/migrate_microbe_domain_edges.py
    sha256: 5187ccfb2897d415b243792a27afd6002c0eea4b167068639ff5be73ed583bb6
    role: context
  - path: scripts/migrate_name_match_groundings.py
    sha256: 9b3ea1153839b9b260638cef95eba2d1ccc6d7b3825e7352c33cceb21bfe4dd4
    role: context
  - path: scripts/migrate_oxygen_senses.py
    sha256: 372e977a58ec6e17cdd45021c5849895142c67187eb29b995b8c39f0e899d2f3
    role: context
  - path: scripts/migrate_pathway_vs_process.py
    sha256: f236de7183048732e9001b7fac4367affff58d8b7a7d5c63286e6b058a4b38c2
    role: context
  - path: scripts/migrate_process_quality_consistency.py
    sha256: 1a83ad3dba79ed0c958b875a6fcc4b9e562259af26da2f248d32d5cf7784f80a
    role: context
  - path: scripts/migrate_protein_vs_activity.py
    sha256: 0b183248ff22d3d8aa66b35aece40c53b516684ca499cf73b7714206031dad49
    role: context
  - path: scripts/migrate_uniprot_instance_groundings.py
    sha256: 07d2a5405cff5857239757e0a3791f411b1d25709a5760c1e49553eed066993d
    role: context
  - path: scripts/seed_from_metpo.py
    sha256: 0fb9c9f7ea6a8f137eecd5c319775b511c398dba6158c81b1fbfb94210f7d851
    role: context
  - path: scripts/verify_metpo_proposal.py
    sha256: f58355151f7d6a807bb50dc8b732184994b0d6145d3c57f54e29fd0bb76268b6
    role: context
  - path: src/traitmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: src/traitmech/validation/write_validated.py
    sha256: 68cfeb876a60d67fd72d5a2800cd29e41b5cf563be5a27b698398a5bb3e67231
    role: context
targets:
- target_id: traitmech:000016
  path: data/traits/environment/mercury_tolerant.yaml
  label: mercury tolerant
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/mercury_tolerant.yaml
    role: Maintained accepted synthetic TraitRecord; scientific changes require guarded
      curation
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: One entire maintained environmental TraitRecord, fully read. The 59-input
    capture covers nine nodes, eight edges, three label-only protein classes, one
    taxon-paired protein instance, three canonical examples and seven explicit AI
    events. Seven literal references occur in sixteen placements with three snippet
    fields. Parent, proposal, writer and provider inputs are context, not additional
    targets. Existing environmental claims receive bounded documentary review. Detailed
    pathogen-related regulator and engineered biosensor biology remains UNASSESSED_SCOPE;
    no new mechanism, molecular target, exposure condition, experimental procedure
    or optimization is supplied.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000016
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000016
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - traitmech:000016
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - traitmech:000016
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - traitmech:000016
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - traitmech:000016
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - traitmech:000016
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - traitmech:000016
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: mercury-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - traitmech:000016
  command: just validate data/traits/environment/mercury_tolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual execution at 11:36:12–13Z passed. Structural acceptance does not
    establish scientific support.
  evidence_ids:
  - check-mercury-validate
- check_id: mercury-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000016
  command: just validate-strict data/traits/environment/mercury_tolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual execution at 11:36:12–14Z passed. Native validity is separate from
    source and imported semantic assessment.
  evidence_ids:
  - check-mercury-strict
- check_id: mercury-snippets
  name: Initial focused snippet invocation
  status: failed
  required: false
  target_ids:
  - traitmech:000016
  command: just verify-snippets --record data/traits/environment/mercury_tolerant.yaml
    --out /private/tmp/traitmech-record-sweep-006.nq5qngor/mercury-snippets.tsv
  exit_code: 2
  expected_exit_code: 0
  summary: Actual execution at 11:36:26–48Z failed with DNS errors, exit 2. No source-falsity
    inference follows; superseded by the successful required network retry.
  evidence_ids:
  - check-mercury-snippets
- check_id: mercury-snippets-network-retry
  name: Focused snippet network retry
  status: passed
  required: true
  target_ids:
  - traitmech:000016
  command: just verify-snippets --record data/traits/environment/mercury_tolerant.yaml
    --out /private/tmp/traitmech-record-sweep-006.nq5qngor/mercury-snippets-network.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual execution at 11:37:20–25Z passed: two VERIFIED and one NOT_IN_ABSTRACT.
    Manual full-text review identifies the third as a meaning-supported nonliteral
    paraphrase.'
  evidence_ids:
  - check-mercury-snippets-network-retry
- check_id: corpus-protein-taxa
  name: Reused corpus protein/taxon audit
  status: passed
  required: true
  target_ids:
  - traitmech:000016
  command: just audit-graph-protein-taxa --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'B4 execution at 08:55:04–10Z passed: 719 graphs, 129 PASS, 589 NONMECHANISTIC,
    one protected, zero gaps and zero errors. The current target row passes with three
    label-only classes and one taxon-matched instance.'
  evidence_ids:
  - check-corpus-protein-taxa
  scope_note: Historical target row is corpus-protein-taxa.tsv line 59. Same scientific
    input bytes support reuse; this is not a new focused biological experiment or
    proof of every contextual branch.
- check_id: corpus-uniprot
  name: Reused corpus UniProt audit
  status: failed
  required: false
  target_ids:
  - traitmech:000016
  command: just audit-uniprot --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-uniprot.tsv
  exit_code: 1
  expected_exit_code: 0
  summary: 'Optional outside-target corpus diagnostic: B4 execution at 08:55:08–08:56:53Z
    exited 1 for other corpus rows. Preserve that actual failed status. The Q1L9Z3
    target row at TSV line 8 has matching primary accession, status, taxon, version
    124, sequence 1 and proteome; it is not a target failure.'
  evidence_ids:
  - check-corpus-uniprot
  scope_note: The historical whole-corpus command remains failed and optional because
    its unresolved rows are outside this target. Fresh current-entry, UniSave, taxonomy
    and retained proteome assessment is the separate required current-target check.
    Do not relabel the corpus command passed or infer a target version defect; unrelated
    corpus repair is outside this review.
- check_id: batch005-qc
  name: Reused full-corpus QC
  status: passed
  required: true
  target_ids:
  - traitmech:000016
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: B5 actual execution at 10:21:03–10:23:38Z passed. B6 input comparison and
    environment readiness support scoped historical reuse, not a new B6 corpus run.
  evidence_ids:
  - check-batch005-qc
  scope_note: 1130 traits, 1278 history files and 19 common inputs match. B3 validated
    1277 history records; OLD failed attempts, network retry, baselines and skips
    remain separate.
- check_id: target-protein-metadata
  name: Current target protein metadata and archive assessment
  status: passed
  required: true
  target_ids:
  - traitmech:000016
  summary: Fresh official Q1L9Z3, UniSave124/history and taxonomy observations match
    the declared instance; retained reference-proteome identity is compatible. This
    documentary check is separate from the failed historical corpus command and from
    experimental proof.
  evidence_ids:
  - protein-assessment
  - db-uniprotQ1L9Z3
  - db-uniprotQ1L9Z3-v124
  - db-uniprotQ1L9Z3-history
  - db-taxa119219-303-266264
  - proteome
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-mercury-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/mercury-validate.log
  locator: Executed 2026-10-21T11:36:12Z through 2026-10-21T11:36:13Z; metadata mercury-validate.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: Actual execution at 11:36:12–13Z passed. Structural acceptance does not
    establish scientific support.
  snapshot_sha256: ff6fbaa538fe53259af826c286b764ab5b3649addc44d2e856ec70d0e75b59e5
- evidence_id: check-mercury-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/mercury-strict.log
  locator: Executed 2026-10-21T11:36:12Z through 2026-10-21T11:36:14Z; metadata mercury-strict.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: Actual execution at 11:36:12–14Z passed. Native validity is separate from
    source and imported semantic assessment.
  snapshot_sha256: da5d6cc5a2759f1c2bce27e5c407f5f4296277279c5a80c6e537d25486ac687b
- evidence_id: check-mercury-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/mercury-snippets.log
  locator: Executed 2026-10-21T11:36:26Z through 2026-10-21T11:36:48Z; metadata mercury-snippets.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: Actual execution at 11:36:26–48Z failed with DNS errors, exit 2. No source-falsity
    inference follows; superseded by the successful required network retry.
  snapshot_sha256: 02332c5e8151d3a1c7ada2df3deb63e2acdd11376966855c3371c1a408a68e13
- evidence_id: check-mercury-snippets-network-retry
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/mercury-snippets-network-retry.log
  locator: Executed 2026-10-21T11:37:20Z through 2026-10-21T11:37:25Z; metadata mercury-snippets-network-retry.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: 'Actual execution at 11:37:20–25Z passed: two VERIFIED and one NOT_IN_ABSTRACT.
    Manual full-text review identifies the third as a meaning-supported nonliteral
    paraphrase.'
  snapshot_sha256: 529abf3000b7ae963f58be6e56b37992f0a6bffea1df1f131e726727b16bcf42
- evidence_id: check-corpus-protein-taxa
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log
  locator: Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: 'B4 execution at 08:55:04–10Z passed: 719 graphs, 129 PASS, 589 NONMECHANISTIC,
    one protected, zero gaps and zero errors. The current target row passes with three
    label-only classes and one taxon-matched instance.'
  snapshot_sha256: f5f1a6be7789f2b3e487fcbc354361f8f1f0d0d0f90a9ba59864d26ed7ac49ef
- evidence_id: check-corpus-uniprot
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-uniprot.log
  locator: Executed 2026-10-21T08:55:08Z through 2026-10-21T08:56:53Z; metadata corpus-uniprot.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: 'Optional outside-target corpus diagnostic: B4 execution at 08:55:08–08:56:53Z
    exited 1 for other corpus rows. Preserve that actual failed status. The Q1L9Z3
    target row at TSV line 8 has matching primary accession, status, taxon, version
    124, sequence 1 and proteome; it is not a target failure.'
  snapshot_sha256: 6ad9ec31ef33837fb5f0d72d8c306af0ec862745d08c88240437e2e5012607b6
- evidence_id: check-batch005-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-005.klfwsp1f/batch005-qc.log
  locator: Executed 2026-10-21T10:21:03Z through 2026-10-21T10:23:38Z; metadata batch005-qc.json
  accessed_at: '2026-10-21T11:45:25Z'
  support: context_only
  summary: B5 actual execution at 10:21:03–10:23:38Z passed. B6 input comparison and
    environment readiness support scoped historical reuse, not a new B6 corpus run.
  snapshot_sha256: 206638ef702eef1ea64f13c4be3ef11180f9659383be68d1e492a9760c8f79be
- evidence_id: capture
  kind: validation
  reference: Native selected-record capture
  locator: 59 inputs at 11:35:55.640194–11:35:57.320860Z
  accessed_at: '2026-10-21T11:35:57.320860Z'
  support: supports
  summary: All current captured hashes match. No additional target or uncaptured history
    is adopted.
  snapshot_sha256: c72609e387f7dd58e5e7ab5c958aff306e39d08e1e27ccdb1d3bb2cf80fee74a
- evidence_id: preparation
  kind: validation
  reference: Whole-target factual preparation
  locator: Nine nodes, eight edges, three label-only classes, one instance and seven
    AI events
  accessed_at: '2026-10-21T11:40:50.077304Z'
  support: context_only
  summary: All current fields were read. Historical target audit rows are retained
    separately from whole-corpus command status; parent/provider inputs are not newly
    claimed fully read by this preparation.
  snapshot_sha256: 14a42563ba6ba84c7b15310decb08667568ab5ab49d471e19115fb952a58b015
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/mercury_tolerant.yaml
  locator: Whole current record and all seven explicit AI events
  accessed_at: '2026-10-21T11:40:27.192178Z'
  support: partial
  summary: The graph has MECHANISTIC scope with a qualified, strain-paired anchor.
    The legacy mer_operon node ID currently labels and describes a MerA protein; it
    is not an operon-as-protein assertion.
  snapshot_sha256: d479ef78e58a331a1a3efef7f2adc3697872fa9bbc6679f4b68d89505d4ed372
- evidence_id: native-policy
  kind: authority
  reference: Native field-by-field review checklist
  locator: Identity, source scope, quoted evidence, completeness and acceptance attribution
  accessed_at: '2026-10-21T11:40:27.192178Z'
  support: supports
  summary: Meaning, source support and traceable human acceptance require review.
    Optional instances on every branch and mandatory dataset assignments are not native
    completeness requirements.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: protein-policy
  kind: authority
  reference: Native grounding policy
  locator: Lines 174–195, generic protein classes and strain-paired examples
  accessed_at: '2026-10-21T11:40:27.192178Z'
  support: supports
  summary: The generic label-only node and particular protein instance are separate.
    Unreviewed reference-proteome entries can carry required metadata; database identity
    does not itself prove an accession-specific experiment.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: snippet-policy
  kind: authority
  reference: Native curation playbook
  locator: Lines 649–650 and 673–676, contiguous verbatim snippets and interpretation
  accessed_at: '2026-10-21T11:40:27.192178Z'
  support: supports
  summary: A meaning-supported paraphrase belongs in interpretive notes unless replaced
    by an actual contiguous source excerpt. Quotation fidelity is separate from biological
    falsity.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: reuse
  kind: validation
  reference: B6 common-input comparison
  locator: Original verification 10:14:46.298715Z
  accessed_at: '2026-10-21T10:14:46.298715Z'
  support: supports
  summary: 1130 traits, 1278 history files and 19 common inputs match the preceding
    batch. Actual B5 final QC is recorded separately from this earlier comparison.
  snapshot_sha256: 91de0fcd8f598a37b867033da1a4d732eaf5676848023a41dd6963612a78aa44
- evidence_id: reuse-supplement
  kind: validation
  reference: B5 checks and B6 readiness supplement
  locator: Original supplement 10:28:10.859819Z; B5 QC 10:21:03–10:23:38Z
  accessed_at: '2026-10-21T10:28:10.859819Z'
  support: supports
  summary: Original check/log hashes, failures, retry, adapter skips and environment
    readiness retain distinct scopes and dates. No new focused scientific certificate
    is implied.
  snapshot_sha256: f5e234e9de85ff4dbd486c2f4e4c9c8df915a767fb67afa4da204ab28f57a7f4
- evidence_id: identity
  kind: authority
  reference: Pinned METPO and accepted local identity
  locator: Local 000016; v5 rows 14/18; active-review row 41 and release-delta row
    1182
  accessed_at: '2026-10-21T11:40:27.179584Z'
  support: supports
  summary: Complete pinned active/deprecated scanning found no exact mercury-specific
    term. The local child and proposed 1007615 remain distinct from broader METPO1007074
    and the deliberately retained parent 000012. The literature-sourced RELATED_SYNONYM
    is conservative.
  snapshot_sha256: 2c8f92151a859d3bdd5625627bb6248f2bd89694c7833b7d7718fdff4b741c55
- evidence_id: db-chebi25195
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/25195/
  locator: Actual official request 2026-10-21T11:36:33.820467+00:00 through 2026-10-21T11:36:34.509763+00:00
  accessed_at: '2026-10-21T11:36:34.509763Z'
  support: context_only
  summary: Retained official identity/version response; interpretation is explicitly
    separated in the grounding and protein assessments. This is not evidence of a
    new biological assay.
  snapshot_sha256: 49ffd46f34b79d5621ca4e8ad7c64462b7b181fbae1fface1783516d4363d2d1
- evidence_id: db-chebi16170
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/16170/
  locator: Actual official request 2026-10-21T11:36:33.824685+00:00 through 2026-10-21T11:36:34.547425+00:00
  accessed_at: '2026-10-21T11:36:34.547425Z'
  support: context_only
  summary: Retained official identity/version response; interpretation is explicitly
    separated in the grounding and protein assessments. This is not evidence of a
    new biological assay.
  snapshot_sha256: e41e1fb314950e070f58d4d75ff7b94295ddd76f4cb6eff661f15563149dbcde
- evidence_id: db-uniprotQ1L9Z3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q1L9Z3.json
  locator: Actual official request 2026-10-21T11:36:33.825423+00:00 through 2026-10-21T11:36:34.509112+00:00
  accessed_at: '2026-10-21T11:36:34.509112Z'
  support: context_only
  summary: Retained official identity/version response; interpretation is explicitly
    separated in the grounding and protein assessments. This is not evidence of a
    new biological assay.
  snapshot_sha256: 075469f07ee589625b8f43b7c09bae36bac12a7d0d869fb466c80c10f41bade3
- evidence_id: db-uniprotQ1L9Z3-v124
  kind: database
  reference: https://rest.uniprot.org/unisave/Q1L9Z3?format=txt&versions=124
  locator: Actual official request 2026-10-21T11:36:34.509556+00:00 through 2026-10-21T11:36:35.423624+00:00
  accessed_at: '2026-10-21T11:36:35.423624Z'
  support: context_only
  summary: Retained official identity/version response; interpretation is explicitly
    separated in the grounding and protein assessments. This is not evidence of a
    new biological assay.
  snapshot_sha256: 0234222ab41d043cde9e54f0cfc18eaa0bb441a305ce451b4317f613320b2cfb
- evidence_id: db-uniprotQ1L9Z3-history
  kind: database
  reference: https://rest.uniprot.org/unisave/Q1L9Z3?format=json
  locator: Actual official request 2026-10-21T11:36:34.510064+00:00 through 2026-10-21T11:36:35.432015+00:00
  accessed_at: '2026-10-21T11:36:35.432015Z'
  support: context_only
  summary: Retained official identity/version response; interpretation is explicitly
    separated in the grounding and protein assessments. This is not evidence of a
    new biological assay.
  snapshot_sha256: d92bdfc08e87720d4e65909cd25e49c572eb6bdbe8a4e4561165cb1a649d591f
- evidence_id: db-taxa119219-303-266264
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=119219,303,266264&retmode=xml
  locator: Actual official request 2026-10-21T11:36:34.547761+00:00 through 2026-10-21T11:36:34.845702+00:00
  accessed_at: '2026-10-21T11:36:34.845702Z'
  support: context_only
  summary: Retained official identity/version response; interpretation is explicitly
    separated in the grounding and protein assessments. This is not evidence of a
    new biological assay.
  snapshot_sha256: 0c892ed9811561679f663813500550dfe1a0b839dd0cf720dc9590c8495bc7d6
- evidence_id: proteome
  kind: database
  reference: https://rest.uniprot.org/proteomes/UP000002429
  locator: Original access 08:55:33.028575–08:55:33.650655Z
  accessed_at: '2026-10-21T08:55:33.650655Z'
  support: supports
  summary: The retained CH34 reference proteome matches the declared instance and
    organism. Copying at 11:37Z is not a new proteome acquisition or experimental
    validation.
  snapshot_sha256: 86b9e50c441eb40769103dc3aa23d5687a6536722586060e9ed5f74d4f86db8f
- evidence_id: protein-assessment
  kind: validation
  reference: Current and archived protein metadata assessment
  locator: Q1L9Z3 current entry and UniSave124; sequence version 1
  accessed_at: '2026-10-21T11:40:27.184022Z'
  support: supports
  summary: Primary accession, MerA name, strain, unreviewed status, reference proteome
    and declared versions match current and historical metadata. Release timing is
    compatible with the stored retrieval date. Functional annotation is computational/inferred;
    exact isoform-specific primary experiment remains separate.
  snapshot_sha256: 647b890c80590ad4b3c97b768b88808a0e37a49abab5146e021f74fc5bbd367c
- evidence_id: predicate-authority
  kind: authority
  reference: Recursive RO semantics
  locator: Original RO2211/2213 08:04:46.869674Z and RO2327 09:52:45.989262Z; integration
    11:40:27.180441Z
  accessed_at: '2026-10-21T11:40:27.180441Z'
  support: supports
  summary: RO2213 inherits process-to-process regulation from RO2211; a material regulator
    protein is not that process. The transcription object fits. RO2327 material MerA
    executor to reduction process is compatible. Native validity is distinct from
    these meanings; no OWL reasoner was run.
  snapshot_sha256: 7605310c198f61cc16d15fd5b9db0b581cff4e2627a2c68b77a9f42d3aad733a
- evidence_id: local-authority
  kind: authority
  reference: Maintained mappings, proposal properties and writer guards
  locator: Node row 185; predicate rows 2/9/38–39/64; v2 rows 9–10; v9 row 3
  accessed_at: '2026-10-21T11:40:27.190257Z'
  support: supports
  summary: The correct elemental-mercury map, local challenges/mitigates/produces
    roles and protein metadata allowance remain intact. Wildcard activates can recreate
    the RO conflict. No maintained mapping was found for the wrong ionic-mercury assignment
    within the captured table and bounded searches.
  snapshot_sha256: 1aaeef3c3d92379970eaee6a8daf4123dec930b1da8196a1a4acf650a8be0ce2
- evidence_id: authority-reuse
  kind: validation
  reference: Authority, catalog and proteome reuse chain
  locator: Hash verification 11:37:39.025741Z
  accessed_at: '2026-10-21T11:37:39.025741Z'
  support: supports
  summary: Original RO, catalog, runner, reference-proteome and KT2440 dataset times/hashes
    are retained. Fresh chemical, current protein/archive and taxonomy responses are
    separate.
  snapshot_sha256: 8477966f3f608278ce0d4db594636d8bcebf6c2218c78738debc80c5408d925c
- evidence_id: ground-ledger
  kind: validation
  reference: Complete documentary grounding assessment
  locator: Nine nodes, eight edges, one component and 59 matching inputs
  accessed_at: '2026-10-21T11:40:27.192178Z'
  support: partial
  summary: 'Two external semantic problems are confirmed: neutral-atom grounding on
    the intended Hg(II) node and a material regulator subject on a process-regulation
    relation. Protein metadata, other node facets and local relation roles remain
    supported.'
  snapshot_sha256: dabe01f65d3b744a2e1079d95cc0918986f84db375b2ff9b7e1fcbe640dd6596
- evidence_id: node-edges
  kind: validation
  reference: Complete current node and edge ledger
  locator: nodes[0–8], edges[0–7], zero-based
  accessed_at: '2026-10-21T11:40:27.184289Z'
  support: partial
  summary: Every endpoint resolves. The three protein classes may remain label-only;
    the legacy node ID is not an entity-type error. Elemental mercury grounding is
    valid. Formal endpoint coverage does not imply validation of detailed pathogen-related
    biology on edge 7.
  snapshot_sha256: eb18daaf2788be94cd54b9c7425a8827e40d91ff9c35f8bd164dcb49743125fb
- evidence_id: owners
  kind: authority
  reference: Maintained owner and recurrence assessment
  locator: Wrong-ground current record; node guard 156–174; predicate guard 152–176
    and mapping row 64
  accessed_at: '2026-10-21T11:40:27.185334Z'
  support: supports
  summary: Existing-ID skips preserve current assignments. Wildcard activates is a
    recurrence owner; the wrong Hg(II) identifier has no matching captured node-mapping
    row. Prior microbe-domain produces assignments were already replaced and are not
    current defects.
  snapshot_sha256: 04d1cdd17c81517ac3375a9cfcfbd0dc182d3e2dfdbc4fbeecd3d9b5ec70632b
- evidence_id: provenance
  kind: search
  reference: Bounded ignored-inclusive target and protein provenance
  locator: Primary search 11:37:39.039909–11:38:03.254471Z; exact refinement through
    11:38:23.086330Z
  accessed_at: '2026-10-21T11:40:27.184802Z'
  support: partial
  summary: Seven explicit AI events document maintenance. Inspected local material
    does not attribute human acceptance. Initial prefix taxon matches were refined
    to full identifiers and did not establish other-script ownership; no targeted
    local saved review or repository history was identified within the bounds.
  snapshot_sha256: 147269fc384776e1a3f44406d12e3238dc5154b9c97e4abff93bfef62cd7c725
  search_scope: Own B6 target ID/label/slug/graph/protein search included hidden and
    ignored files, excluding .git and .venv. Exact node/protein searches covered history;
    wrong-ID and label searches covered scripts, mappings and history; full-word taxon/PMID/accession
    refinement covered history and scripts. The 172 matching files do not cover private
    or remote material.
- evidence_id: expression
  kind: validation
  reference: Canonical catalog and dataset strain applicability
  locator: Catalog original 07:36:12.732638–07:36:12.858149Z; dataset metadata 08:54:17.518957–08:54:18.018420Z
  accessed_at: '2026-10-21T11:40:27.191299Z'
  support: context_only
  summary: Cupriavidus/CH34 have no retained catalog match. P. putida has a species
    entry, but its precise321 dataset is KT2440 while the canonical source is SP1.
    No strain transfer or downstream module query is justified; noncoverage/mismatch
    is not negative phenotype evidence.
  snapshot_sha256: 04323e58828653dcf01cc18cd7a1dbf982aa685a0585a0083b0c2e894ad06773
- evidence_id: runner
  kind: search
  reference: Historical bounded structured-runner discovery
  locator: Original B5 PATH/project 09:27:57.380287–09:27:57.542053Z; external 08:17:15.206671–08:17:15.338052Z
  accessed_at: '2026-10-21T09:27:57.542053Z'
  support: context_only
  summary: Prior discovery and the official catalog fallback are reused with original
    bounds. No fresh B6 or whole-machine absence claim is made.
  snapshot_sha256: 43597ec8b007fc605fabf9069534281f331a33bda5615b9ce9c473facf744179
  search_scope: Original B5 PATH and ignored-inclusive project search plus the earlier
    separately retained bounded installation search; exact roots/exclusions remain
    in those receipts. No fresh global discovery or biological query was run.
- evidence_id: source-ledger
  kind: validation
  reference: Final source assessment
  locator: Seven literal records, sixteen placements and three snippets; finalized
    11:39:48.617848Z
  accessed_at: '2026-10-21T11:39:48.617848Z'
  support: partial
  summary: Definition and canonical classifications have positive scoped support.
    Two snippet fields and an additional notes quote are literal; the protein-anchor
    snippet is a meaning-supported paraphrase. The accession-specific evidence limit
    is retained without an additional formal finding under parent adjudication.
  snapshot_sha256: c221a15a25e18966d9eca2c8d45e4d373d942ae97efee6f99cd99a4c9c7d749f
- evidence_id: placements
  kind: validation
  reference: Complete citation-placement ledger
  locator: All sixteen placements, including synonym and protein-instance evidence
  accessed_at: '2026-10-21T11:39:48.617437Z'
  support: partial
  summary: Native CH34 and derivative results remain distinct; P. putida support is
    SP1-specific. Broad metal context is not a newly verified mercury-specific body
    claim. Detailed edge 7 biology remains UNASSESSED_SCOPE.
  snapshot_sha256: ae981eda23fc10ca1144b032d37be5dddf48aab25283aa512b2d809a427ec973
- evidence_id: snippets
  kind: validation
  reference: Complete quotation ledger
  locator: Three snippet fields plus additional quoted phrase in evidence[0].notes
  accessed_at: '2026-10-21T11:39:48.616718Z'
  support: partial
  summary: Two fields and the notes phrase are exact. The protein-anchor phrase is
    absent as a contiguous quotation from the acquired main JATS despite positive
    native CH34 evidence. The search covers that entire acquired text, not inaccessible
    supplements or all versions.
  snapshot_sha256: d4b4c26c84bd2d9fce5f6e7318e091207971328f309d41aae3792076f358ac9e
- evidence_id: edge-sources
  kind: validation
  reference: Complete eight-edge source ledger
  locator: Existing environmental claims and explicit edge 7 biology boundary
  accessed_at: '2026-10-21T11:39:48.617159Z'
  support: partial
  summary: Generic existing conversion and background statements have source support
    with study/taxon limits. Frontiers identity and generic framing are verified;
    detailed pathogen-related regulatory biology is not assessed or repaired.
  snapshot_sha256: 1e4e604136aa49db5ba50932bbc64472ce385547b5503124ddc92b1d7fc555f5
- evidence_id: protein-source-limit
  kind: validation
  reference: Primary protein-evidence scope assessment
  locator: Native CH34 phenotype and probable band versus unique accession proof
  accessed_at: '2026-10-21T11:39:48.617848Z'
  support: partial
  summary: The acquired JATS supports native CH34 resistance and a probable MerA band.
    It does not uniquely identify or assay Q1L9Z3 in its inspected main text. The
    record does not expressly claim such an isolated assay, so preserve this as a
    scoped limitation, not an additional source-tier finding.
  snapshot_sha256: c128da97d42ca8775e30fddd2ddfb22eec1c9721448fee09bd042f3a8c6a154c
- evidence_id: adjudication
  kind: validation
  reference: Independent parent final adjudication
  locator: Four findings adopted at 11:40:59.100946Z after complete ledger and primary-window
    reading
  accessed_at: '2026-10-21T11:40:59.100946Z'
  support: context_only
  summary: Two grounding majors, the nonliteral protein snippet minor and bounded
    human-acceptance minor are adopted. Positive CH34 evidence, exact isoform limits
    and unassessed detailed regulator biology remain explicit; no additional evidence-tier
    or version finding is assigned.
  snapshot_sha256: b4c5b23120e5714b56b547b68475354753535205d0fa77c5894ee8a1cc050905
- evidence_id: meta-0
  kind: database
  reference: DOI:10.1016/S0168-6445(03)00046-9
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Bacterial%20mercury%20resistance%20from%20atoms%20to%20ecosystems%22&format=json&resultType=core;
    actual indexed metadata/abstract
  accessed_at: '2026-10-21T11:37:30.919104Z'
  support: supports
  summary: 'Bacterial mercury resistance from atoms to ecosystems. Access scope: Actual
    indexed abstract plus Crossref identity. Initial DOI query0 resolved by exact-title
    search to PMID12829275. Publisher PDF403 and browserredirect failure; body uninspected.'
  snapshot_sha256: 6429298a87da000cbf112a84d79f35aacf1db47187407b0165d855b412f33e70
- evidence_id: meta-1
  kind: database
  reference: PMID:12829273
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12829273+AND+SRC%3AMED&format=json&resultType=core;
    actual indexed metadata/abstract
  accessed_at: '2026-10-21T11:36:22.792606Z'
  support: supports
  summary: 'Efflux-mediated heavy metal resistance in prokaryotes. Access scope: Actual
    indexed abstract; general metal-efflux context. No new body acquisition claimed.'
  snapshot_sha256: ab66a791a5245cbb2bd7274916dba2349cf69ed1b105f965af95e8f3d6279302
- evidence_id: meta-2
  kind: database
  reference: PMID:21423734
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21423734+AND+SRC%3AMED&format=json&resultType=core;
    actual indexed metadata/abstract
  accessed_at: '2026-10-21T11:36:22.833553Z'
  support: supports
  summary: 'Characterization of the metabolically modified heavy metal-resistant Cupriavidus
    metallidurans strain MSR33 generated for mercury bioremediation. Access scope:
    Actual primary JATS; introduction, native CH34 comparisons and protein-identification
    certainty inspected. Incidental pathogen-specific mechanisms and operational optimization
    unassessed.'
  snapshot_sha256: c6037bd90270925fe812039cc96a251a37a0a399a2fd7d11d42943ea169879e5
- evidence_id: meta-3
  kind: database
  reference: PMID:21751007
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21751007+AND+SRC%3AMED&format=json&resultType=core;
    actual indexed metadata/abstract
  accessed_at: '2026-10-21T11:36:22.827280Z'
  support: supports
  summary: 'Characterization of a marine-isolated mercury-resistant Pseudomonas putida
    strain SP1 and its potential application in marine mercury reduction. Access scope:
    Actual indexed title/abstract for SP1 identity and mercury-resistant classification
    only. Virulence, stress/fitness optimization and numerical operating conditions
    unassessed.'
  snapshot_sha256: 639bc90c4127c55abd6e2e9e03ef4777512107fe7cf80f2b6092c52a8b21a301
- evidence_id: meta-4
  kind: database
  reference: DOI:10.1186/s12866-024-03391-5
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1186%2Fs12866-024-03391-5&format=json&resultType=core;
    actual indexed metadata/abstract
  accessed_at: '2026-10-21T11:36:23.527890Z'
  support: supports
  summary: 'Horizontal gene transfer of the Mer operon is associated with large effects
    on the transcriptome and increased tolerance to mercury in nitrogen-fixing bacteria.
    Access scope: Actual primary JATS; generic introduction claims and evidence type
    inspected.'
  snapshot_sha256: b180fd7fa5549c3ae7ff9d326f1981aa57d3605bbe2b118bece17278fbefe70e
- evidence_id: meta-5
  kind: database
  reference: DOI:10.21203/rs.3.rs-3854515/v1
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.21203%2Frs.3.rs-3854515%2Fv1&format=json&resultType=core;
    actual indexed metadata/abstract
  accessed_at: '2026-10-21T11:36:23.544957Z'
  support: supports
  summary: 'Adaptation to mercury stress by nitrogen-fixing bacteria is driven by
    horizontal gene transfer and enhanced gene expression of the Mer operon Access
    scope: Actual official Research Square v1 PDF, pages1–3, abstract and introductory
    source claims inspected. Landing and staticHTML403 retained.'
  snapshot_sha256: de6ca10b60ad4fb822b541bebf42ce8b81194f36e9bf09508230b6906d768366
- evidence_id: meta-6
  kind: database
  reference: DOI:10.3389/fbioe.2023.1178680
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3389%2Ffbioe.2023.1178680&format=json&resultType=core;
    actual indexed metadata/abstract
  accessed_at: '2026-10-21T11:36:23.512883Z'
  support: supports
  summary: 'Synthetic bacteria for the detection and bioremediation of heavy metals.
    Access scope: Actual primary JATS acquired, but assessed only documentary/general
    regulator framing. Detailed engineered pathogen biosensor routes UNASSESSED_SCOPE.'
  snapshot_sha256: 3576ec84fd286c544d3944e5f63c63ec4705a0caa8bce8a23002113bc1ef81db
- evidence_id: ch34-primary
  kind: primary_source
  reference: PMID:21423734
  locator: Introduction paragraph 3; body 20–22, 27 and 29; Fig. 3 caption; actual
    2026-10-21T11:36:44.920667+00:00 through 2026-10-21T11:36:50.163740+00:00
  accessed_at: '2026-10-21T11:36:50.163740Z'
  support: partial
  summary: Native CH34 phenotype and a probable MerA band are positive evidence. Derivative
    results and assay-specific outcomes are not transferred; exact-entry isolation
    is not established.
  snapshot_sha256: a53bb68fc308ad35f92d7c0f8b3fa796af60505f69d50581dd9c546d4e517978
- evidence_id: bmc-primary
  kind: primary_source
  reference: DOI:10.1186/s12866-024-03391-5
  locator: Introduction paragraph 1; actual 2026-10-21T11:36:44.921254+00:00 through
    2026-10-21T11:36:52.240969+00:00
  accessed_at: '2026-10-21T11:36:52.240969Z'
  support: partial
  summary: Existing generic conversion claims are supported background, not new all-taxon
    isolated-enzyme measurements.
  snapshot_sha256: 300bb741defa575b3ccf497e5ec27b03b6ab30d2e69a91323327dd77062a0917
- evidence_id: preprint-primary
  kind: primary_source
  reference: DOI:10.21203/rs.3.rs-3854515/v1
  locator: Official v1 PDF printed pages 1–3, especially introductory pages 2–3; actual
    2026-10-21T11:38:03.595888+00:00 through 2026-10-21T11:38:06.191021+00:00
  accessed_at: '2026-10-21T11:38:06.191021Z'
  support: partial
  summary: The cited existing introductory claims and preprint identity are present.
    No engineering route, optimization or independent replication is inferred.
  snapshot_sha256: 58fa2f6969de404b079a2723890ec25344b10820a96f10f2463560af95adad93
- evidence_id: frontiers-primary
  kind: primary_source
  reference: DOI:10.3389/fbioe.2023.1178680
  locator: Documentary identity and generic framing only; body 25, caption 27 and
    context 30; actual 2026-10-21T11:36:44.921440+00:00 through 2026-10-21T11:36:47.030084+00:00
  accessed_at: '2026-10-21T11:36:47.030084Z'
  support: partial
  summary: The review provides generic family/promoter framing. Detailed engineered
    pathogen biosensor and regulator-to-transcription biology is UNASSESSED_SCOPE;
    full XML acquisition does not imply full biological verification.
  snapshot_sha256: c07d9a39e29e1f68b8b4f9bb0f160ec68c941a8048e78efccc89b26ad35b8a09
- evidence_id: source-access
  kind: validation
  reference: Actual source access boundaries
  locator: Three JATS bodies, official preprint PDF, three abstract-only works and
    retained failed requests
  accessed_at: '2026-10-21T11:39:48.617717Z'
  support: context_only
  summary: Initial definition DOI query returned zero but title/registry resolution
    succeeded. Definition PDF and Research Square landing/static HTML returned 403;
    actual PDF subsequently succeeded. Browser failures remain distinct from primary
    text inspected.
  snapshot_sha256: 96a64af2810be1a1ec2d68774dc3cdb6fe914c16d6cc03d751ba09f8678e6ebc
- evidence_id: versions
  kind: validation
  reference: Preprint and journal relationship assessment
  locator: Official PDF date/version, BMC date, overlapping authors/text and empty
    registry relation fields
  accessed_at: '2026-10-21T11:39:48.614806Z'
  support: context_only
  summary: The corresponding-study relationship is strongly inferred, not confirmed
    by an explicit primary version link. Preserve seven literal references and sixteen
    placements, but do not count the apparent versions as independent replication.
    Preprint status is not retraction or invalidity.
  snapshot_sha256: 929e73c89f4b48f21d71c6c90235060f4cf0f0723648171bbf389e5afeac08b6
- evidence_id: publication-status
  kind: validation
  reference: Bounded current publication-status inspection
  locator: Seven indexed records and three Crossref relation/update fields
  accessed_at: '2026-10-21T11:39:48.614423Z'
  support: context_only
  summary: Preprint status is explicit. No corrective relation occurred in the inspected
    fields; this is not a globally exhaustive absence claim. Empty relationship fields
    neither confirm nor refute the inferred version relationship.
  snapshot_sha256: 2bb53e4a470161f778f2d28e29b3c336abc96706022904f2e1e5800a071cdd37
- evidence_id: root-ch34
  kind: validation
  reference: Independent primary CH34 window read
  locator: Actual paragraphs 1–3, 20–21 and 27; recorded 11:37:59.186263Z
  accessed_at: '2026-10-21T11:37:59.186263Z'
  support: supports
  summary: Root read the retained source body and verified its hash, preserving native
    versus derivative and probable-band versus unique-entry distinctions.
  snapshot_sha256: a09367ca074563719bf2dd2212fbc365238406fcb1eb6f0ccbab7396bba3023d
- evidence_id: root-source-read
  kind: validation
  reference: Independent actual abstract and BMC window reads
  locator: Definition, Nies and SP1 abstracts; BMC body 0–2; recorded 11:38:57.513403Z
  accessed_at: '2026-10-21T11:38:57.513403Z'
  support: supports
  summary: Actual text supports the bounded definition, quotations, species/strain
    classification and generic background. OUP failure and unassessed pathogen/optimization
    content remain separate.
  snapshot_sha256: afa1a0301013fca5f95f0381199873a8d2ee7f091f8290ef3e399b76875e6895
- evidence_id: root-preprint
  kind: validation
  reference: Independent final preprint source read
  locator: Printed page 2 and opening page 3; recorded 11:40:34.677434Z
  accessed_at: '2026-10-21T11:40:34.677434Z'
  support: supports
  summary: Root read actual PDF-derived primary context and verified PDF/text hashes.
    Existing source claims are supported; the publication-version relationship remains
    inferred rather than an explicit primary link.
  snapshot_sha256: 2ada195d0472f797f9a5f5e818507762554523d14a959c0ecbdb38edd850e981
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: local identifier, hierarchy and synonym'
  outcome: supported
  target_ids:
  - traitmech:000016
  summary: Accepted local 000016 has no exact mercury-specific active/deprecated match
    in the pin. V5 child 1007615 and parent 1007611 remain proposals; broad active
    metal tolerance overlaps the deliberately retained parent. Parent typical efflux
    wording does not require every child to use efflux. RELATED_SYNONYM mercury resistant
    is source-backed.
  evidence_ids:
  - identity
  - local-authority
  - placements
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: complete existing definition'
  outcome: supported
  target_ids:
  - traitmech:000016
  summary: The actual definition abstract supports inorganic/organic mercury resistance
    and the stated typical MerA conversion. Initial DOI-search failure is resolved
    by matching title, PMID and registry identity. Typical wording is not an exclusive
    universal mechanism or a new quantitative tolerance threshold.
  evidence_ids:
  - meta-0
  - placements
  - root-source-read
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: all three organism examples'
  outcome: supported
  target_ids:
  - traitmech:000016
  summary: Official taxa match species and strain labels. Native CH34 phenotype supports
    the Cupriavidus species/strain examples within source limits, without transferring
    derivative results. P. putida evidence is SP1, not all strains or catalog KT2440.
    Species and strain examples are distinct scopes, not automatic duplicates.
  evidence_ids:
  - db-taxa119219-303-266264
  - ch34-primary
  - meta-3
  - placements
  - root-ch34
- assessment_id: nodes
  area: grounding
  topic: 'Native checklist: all nine current nodes'
  outcome: concern
  target_ids:
  - traitmech:000016
  summary: Node 1 intends Hg(II) but CHEBI25195 denotes a neutral mercury atom with
    zero charge. Native CHEMICAL type is appropriate; the assigned identity is the
    error. CHEBI16170 matches elemental mercury. Other protein, process and chemical-class
    facets are coherent; the legacy mer_operon ID does not override its present protein
    label.
  evidence_ids:
  - db-chebi25195
  - db-chebi16170
  - node-edges
  - record
  - local-authority
  details: 'Node 0: local trait. Node 1: mismatched ionic ground. Nodes 2/5/7: three
    material protein classes. Nodes 3/8: biological processes. Node 4: supported elemental
    chemical identity. Node 6: optional ungrounded organomercurial class.'
- assessment_id: protein
  area: grounding
  topic: 'Native checklist: single taxon-paired protein instance and generic class'
  outcome: supported
  target_ids:
  - traitmech:000016
  summary: Q1L9Z3 is the current primary MerA entry for CH34 with matching status,
    reference proteome, entry version 124 and sequence version 1. Archive timing agrees
    with stored retrieval metadata. Unreviewed computational annotation is allowed
    but not direct experimental proof. Three label-only classes do not require instances
    on every contextual branch.
  evidence_ids:
  - protein-assessment
  - db-uniprotQ1L9Z3
  - db-uniprotQ1L9Z3-v124
  - db-uniprotQ1L9Z3-history
  - proteome
  - protein-policy
- assessment_id: protein-evidence
  area: evidence
  topic: 'Native checklist: experimental anchor and exact entry scope'
  outcome: unknown
  target_ids:
  - traitmech:000016
  summary: The primary paper positively supports native CH34 resistance and a probable
    MerA band. A unique Q1L9Z3 assay is not established in acquired main text, but
    the record does not expressly claim one. Preserve the branch with that evidence-tier
    limitation; no additional formal finding or negative-function claim follows. The
    nonliteral snippet is separately assessed.
  evidence_ids:
  - ch34-primary
  - protein-source-limit
  - protein-assessment
  - root-ch34
  - adjudication
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all eight relation roles'
  outcome: concern
  target_ids:
  - traitmech:000016
  summary: Edge 7 RO2213 requires a process subject, while its subject denotes a material
    protein; the process object fits. Edge 1 RO2327 has compatible material-executor
    roles. Local challenges, mitigates and produces fit current endpoint kinds; free-text
    cleaves/senses need no mandatory IDs. The wrong chemical ground is one shared
    node finding.
  evidence_ids:
  - predicate-authority
  - local-authority
  - node-edges
  - owners
  details: 'Edges 0/2: local stressor/mitigation roles. Edge 1: material executor
    to process. Edges 3/5: local material-protein to chemical production. Edges 4/6:
    free-text substrate/sensing roles. Edge 7: imported process-subject mismatch,
    independently of unassessed detailed biology.'
- assessment_id: edge-evidence
  area: evidence
  topic: 'Native checklist: all eight nearest-source assertions'
  outcome: supported
  target_ids:
  - traitmech:000016
  summary: Existing generic environmental statements have contextual support in actual
    abstracts, BMC introduction and official preprint pages 2–3. Nies is broad metal
    context; its unseen mercury-specific body wording remains unknown. Detailed edge
    7 pathogen-related regulator biology is UNASSESSED_SCOPE, not validated or declared
    false. Formal-role assessment is separate.
  evidence_ids:
  - edge-sources
  - placements
  - meta-0
  - meta-1
  - bmc-primary
  - preprint-primary
  - frontiers-primary
  - root-preprint
  details: Supported outcome applies to documented source identity and the stated
    generic context, not blanket biological certification of every edge. No new route
    or engineering repair is supplied.
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: three snippets and additional notes quotation'
  outcome: concern
  target_ids:
  - traitmech:000016
  summary: Two snippet fields and the quoted notes phrase match actual abstracts.
    The protein-anchor phrase is a meaning-supported paraphrase rather than a contiguous
    excerpt from acquired full JATS. Its absence from the abstract alone was inconclusive;
    full-text comparison supports the bounded quotation-fidelity finding.
  evidence_ids:
  - snippets
  - snippet-policy
  - ch34-primary
  - check-mercury-snippets-network-retry
- assessment_id: bibliography
  area: evidence
  topic: 'Native checklist: seven literal references, sixteen placements and version
    status'
  outcome: supported
  target_ids:
  - traitmech:000016
  summary: All seven cited identities resolve, comprising six journal publications
    and one explicit preprint. The apparent preprint/journal correspondence is inferred
    from primary text and identity overlap, not a confirmed version link or independent
    replication. Current status fields and access surfaces have explicit bounds.
  evidence_ids:
  - source-ledger
  - placements
  - versions
  - publication-status
  - source-access
- assessment_id: quantity
  area: quantity
  topic: 'Native checklist: chemical state and scope of quantitative claims'
  outcome: concern
  target_ids:
  - traitmech:000016
  summary: The present material distinction is Hg(II) versus neutral/elemental mercury;
    the wrong ground obscures that distinction. The record does not require a newly
    imposed dose or universal threshold. Comparative derivative and bulk-removal outcomes
    are not transferred to a unique native protein or every strain.
  evidence_ids:
  - db-chebi25195
  - db-chebi16170
  - protein-source-limit
  - placements
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: whole-record and branch scope'
  outcome: supported
  target_ids:
  - traitmech:000016
  summary: Nine nodes, eight edges, three canonical examples, one protein instance,
    seven literal references, sixteen placements, three snippets and seven events
    are covered. One MECHANISTIC component has a taxon-paired anchor with explicit
    evidence limits. No token instance on every contextual branch or graph reconstruction
    is required.
  evidence_ids:
  - capture
  - node-edges
  - protein-policy
  - placements
  - adjudication
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: canonical species versus dataset strain'
  outcome: not_applicable
  target_ids:
  - traitmech:000016
  summary: Cupriavidus/CH34 have no catalog entry. P. putida has a species match,
    but the dataset is KT2440 and the source example SP1. No matching represented
    experimental strain is established, so downstream expression queries were not
    applied. No phenotype absence or mandatory dataset defect is inferred.
  evidence_ids:
  - expression
  - runner
  - authority-reuse
- assessment_id: ownership
  area: ownership
  topic: 'Native checklist: current values and maintained recurrence'
  outcome: concern
  target_ids:
  - traitmech:000016
  summary: The wrong chemical ground is owned by the current record and retained by
    existing-value skipping, with no exact assignment found in captured mappings/bounded
    searches. Wildcard activates and the predicate writer own recurrence of the RO
    mismatch. Correct elemental mapping, local produces migration, protein metadata
    and parent retention are preserved.
  evidence_ids:
  - owners
  - local-authority
  - provenance
  - identity
- assessment_id: human-acceptance
  area: provenance
  topic: 'Native checklist: REVIEWED and local attribution'
  outcome: concern
  target_ids:
  - traitmech:000016
  summary: Seven explicit AI events document proposal, graph curation, grounding,
    migration and protein-instance provenance. Ignored-inclusive bounded searches
    do not identify current-target human acceptance. Prefix-search false positives
    were refined; private and remote decisions remain unassessed.
  evidence_ids:
  - provenance
  - record
  - native-policy
- assessment_id: checks
  area: schema
  topic: 'Native checklist: actual checks, failed corpus status and focused metadata'
  outcome: supported
  target_ids:
  - traitmech:000016
  summary: Focused validation and strict checks passed. The DNS snippet failure is
    retained before its successful required retry. Historical corpus UniProt exit
    1 remains failed as an optional outside-target diagnostic; the target row and
    separate required current-target official metadata assessment match, so no target
    version defect or unrelated corpus-repair requirement follows. Other reused checks
    preserve original dates, failures, retry and skips.
  evidence_ids:
  - check-mercury-validate
  - check-mercury-strict
  - check-mercury-snippets
  - check-mercury-snippets-network-retry
  - check-corpus-protein-taxa
  - check-corpus-uniprot
  - check-batch005-qc
  - protein-assessment
  - reuse
  - reuse-supplement
findings:
- finding_id: ionic-mercury-ground
  issue_key: mercury-tolerant-ionic-mercury-ground
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The Hg(II) node is grounded to a neutral mercury atom
  description: Node 1 names mercury(2+) ion and describes reactive ionic mercury,
    but current CHEBI25195 denotes the neutral mercury atom with zero charge. This
    changes the chemical identity represented across its incident edges. The native
    CHEMICAL type is valid; preserve the intended ionic meaning while reconciling
    the identifier. Correct elemental mercury grounding on node 4 remains separate,
    and no new replacement chemistry is prescribed.
  target_ids:
  - traitmech:000016
  field_paths:
  - causal_graphs[0].nodes[1].grounding
  evidence_ids:
  - db-chebi25195
  - db-chebi16170
  - node-edges
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/mercury_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_nodes.py
    role: Existing-grounding guard retains the current record value; no exact wrong
      assignment exists in the captured mapping table
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: regulation-subject
  issue_key: mercury-tolerant-regulation-subject
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: RO positive regulation assigns a process role to a material protein
  description: Edge 7 assigns RO:0002213 to a material regulator protein as subject.
    The relation inherits process-to-process regulation; its transcription-process
    object fits, but its protein subject does not become a process because the text
    describes regulatory activity. This is an external semantic conflict, not native
    validation failure or a claim that the detailed biology is false. That biology
    remains UNASSESSED_SCOPE; no replacement mechanism is supplied.
  target_ids:
  - traitmech:000016
  field_paths:
  - causal_graphs[0].edges[7].predicate_id
  evidence_ids:
  - predicate-authority
  - node-edges
  - local-authority
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/mercury_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard activates mapping row 64
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Existing-ID preservation and declared type gates
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: protein-quote-fidelity
  issue_key: mercury-tolerant-protein-quote-fidelity
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The protein-anchor snippet is a supported paraphrase rather than a literal
    excerpt
  description: The protein-example snippet is not a contiguous quotation in the acquired
    main JATS, although native CH34 mercury resistance and a probable MerA band are
    positively supported. The comparison covers that complete acquired text, not inaccessible
    supplements or all versions. Treat this as bounded quotation fidelity, not fabricated
    biology or a disproven protein function; retain the positive evidence and exact-entry
    limitations.
  target_ids:
  - traitmech:000016
  field_paths:
  - causal_graphs[0].nodes[2].protein_examples[0].evidence[0].snippet
  evidence_ids:
  - snippets
  - ch34-primary
  - snippet-policy
  - protein-source-limit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/mercury_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: mercury-tolerant-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Inspected local provenance does not attribute human scientific acceptance
  description: REVIEWED accompanies seven explicit AI maintenance events. The bounded
    ignored-inclusive searches and inspected provenance do not identify a human acceptance
    decision for this target. Maintenance history remains positive evidence. Private
    or remote decisions are unassessed; this is not a claim that no human review ever
    occurred.
  target_ids:
  - traitmech:000016
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - record
  - native-policy
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/mercury_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-chemical-identity
  description: Reconcile the assigned ground with the existing Hg(II) meaning.
  finding_ids:
  - ionic-mercury-ground
  target_ids:
  - traitmech:000016
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/mercury_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_nodes.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Any retained identifier denotes the stated ionic species and agrees with label,
    description and incident existing claims. Preserve the separate valid elemental-mercury
    ground.
  - Review existing-value preservation without adding new chemical routes, experimental
    conditions or arbitrary replacements.
  - After separately authorized curation, use guarded writes, append-only record/repository
    history, focused validation/strict/source and applicable protein audits, maintained
    QC and generated-output recipes. This review makes no scientific mutation.
- action_id: reconcile-regulation-role
  description: Reconcile the imported relation with the represented protein/process
    endpoint meanings.
  finding_ids:
  - regulation-subject
  target_ids:
  - traitmech:000016
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/mercury_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Any retained RO identifier meets inherited domain/range meaning. Preserve the
    legitimate material protein and process object rather than forcing a retype.
  - Bound the change to semantic annotation and recurrence; detailed pathogen-related
    regulator biology remains unassessed and no mechanism reconstruction or optimization
    is requested.
  - After separately authorized curation, use guarded writes, append-only record/repository
    history, focused validation/strict/source and applicable protein audits, maintained
    QC and generated-output recipes. This review makes no scientific mutation.
- action_id: separate-quote-and-interpretation
  description: Use literal evidence wording or clearly label the existing supported
    paraphrase.
  finding_ids:
  - protein-quote-fidelity
  target_ids:
  - traitmech:000016
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/mercury_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The snippet is a verifiable contiguous source excerpt, or the existing paraphrase
    is moved to interpretive notes. Preserve native CH34 phenotype and probable-band
    support.
  - Do not transfer derivative results or imply unique Q1L9Z3 isolation; retain current
    accurate strain/status/version metadata.
  - After separately authorized curation, use guarded writes, append-only record/repository
    history, focused validation/strict/source and applicable protein audits, maintained
    QC and generated-output recipes. This review makes no scientific mutation.
- action_id: attribute-human-acceptance
  description: Link existing human scientific acceptance or obtain it through the
    established process.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - traitmech:000016
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/mercury_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies revision and scope, including source-tier limits, unassessed
    detailed biology and semantic concerns. Preserve all seven AI events.
  - Automated validation and this review do not substitute for human acceptance; reassess
    status if necessary.
limitations:
- Local 000016 and v5 proposal 1007615 remain distinct from the deliberately retained
  broad metal-tolerance parent. No forced parent migration or universal efflux requirement
  is inferred.
- The definition review is abstract-only but positively supports the existing typical
  mechanism and quotations. Initial DOI query zero was resolved by exact-title/registry
  identity. Nies provides broad metal context; absence of mercury in its abstract
  does not prove body absence.
- Native CH34 resistance and a probable MerA band are supported. Derivative MSR33
  and assay-specific results remain separate; acquired main text does not uniquely
  identify or assay Q1L9Z3. The record does not expressly claim such an isolated assay,
  so no additional source-tier defect is assigned.
- Current and archived Q1L9Z3 metadata both match entry 124/sequence 1, with compatible
  retrieval timing and reference-proteome taxon. Computational/unreviewed annotation
  is not unique experimental proof, but its status alone is not a schema or anchor
  defect.
- P. putida classification is source-strain SP1. Its catalog species match has KT2440
  data, which are not transferred to SP1 or CH34. Cupriavidus noncoverage and strain
  mismatch are not negative phenotype evidence; no downstream module query was performed.
- The preprint and BMC paper are strongly inferred corresponding versions, not confirmed
  by an explicit primary relation link. Retain seven literal references and sixteen
  placements without counting apparent versions as independent replication. Preprint
  status is not invalidity or retraction.
- The official preprint PDF pages 1–3 and BMC generic introduction support existing
  contextual statements. They are not new all-taxon assays. Source wording relatively
  inert is contextual chemistry, not a health-safety conclusion.
- Frontiers detailed engineered-pathogen biosensor and regulator biology is UNASSESSED_SCOPE.
  Its identity and generic framing are documented; formal RO role review neither validates
  nor repairs that biological route.
- Legacy mer_operon is a node identifier, while the present label/description denote
  a protein and operon/gene fields are metadata. Three label-only classes and one
  instance do not require artificial examples on all contextual branches.
- The wrong ionic chemical identifier is separate from valid CHEMICAL type and compatible
  local relation roles. RO2327 material-executor roles fit; only the stated RO2213
  assignment has the imported process-subject conflict. No OWL reasoner execution
  or new mechanism is claimed.
- Two snippet fields and one additional notes quote are literal. The protein-anchor
  phrase is a supported paraphrase in the acquired main JATS; inaccessible supplements
  and every possible version were not exhaustively searched.
- Source bodies, abstract-only access, official PDF success, landing/PDF 403 and browser
  failures retain actual scopes and times. Acquiring a complete XML does not imply
  inspection or validation of all detailed biology. Publication-status fields are
  bounded, not a global notice-absence certificate.
- Seven AI events and ignored-inclusive local searches document maintenance but not
  attributed human acceptance. Initial prefix taxon matches were false positives resolved
  by exact refinement; private/remote decisions remain unassessed.
- The historical corpus UniProt exit 1 remains failed and optional for outside-target
  rows. The matching target row and fresh required current-target metadata assessment
  are separate; unrelated corpus repair is not required for this review. Snippet DNS
  failure and successful retry, B4/B5/B3/OLD dates, product failures/retry, baselines
  and skips remain distinct; no native corpus rerun or environment mutation occurred.
- No scientific record, mapping, history, generated output, Git or state was changed.
  No paid research, new molecular target, experiment, exposure condition, biological
  intervention or optimization is supplied.
notes:
- 'Four findings: two major and two minor. All indices are zero-based.'
- All 59 captured hashes match; nine nodes, eight edges, three label-only protein
  classes, one instance, three canonical examples and seven explicit AI events are
  covered.
- Final source ledger 11:39:48.617848Z; grounding 11:40:27.192178Z; parent adjudication
  11:40:59.100946Z. Acquisition, reuse and integration remain distinct.
tags:
- record-review
- mercury-tolerant
- environment
- needs-curation
```
