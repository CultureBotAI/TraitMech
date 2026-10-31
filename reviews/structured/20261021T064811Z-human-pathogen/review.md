# Identity, source and representation review of human pathogen (METPO:1004004)

- Review: 20261021T064811Z-human-pathogen
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T06:43:51Z
- Finished UTC: 2026-10-21T06:48:11Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The active METPO identity, parent, three GO identifiers and two species examples are supported. All thirteen nodes and twelve edges were inspected for source scope and representation. Three major findings concern mischaracterized citations, eight external relation/endpoint conflicts and source uncertainty lost in categorical wording. Three minor findings concern a provisional relation’s local meaning, overstrong alias provenance and a missing human-acceptance link. Detailed pathogen mechanisms are not certified or reconstructed; unverified source support is explicit. The review proposes documentary and conceptual corrections only.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Eighth target in batch002, selected in lexicographic path order from the validated inventory union; one entire previously uncovered TraitRecord.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f25e2af0b38a8303b13f627a9a5c33b36af4b3d2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1004004 | data/traits/ecology/human_pathogen.yaml | maintained | human pathogen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1004004 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1004004 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1004004 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1004004 | 1276 history records checked, zero invalid links; integrity does not establish scientific correctness or human sign-off. |
| Initial full-product validation | failed | False | METPO:1004004 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1004004 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1004004 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | METPO:1004004 | The selected record validates. |
| Focused strict validation | passed | True | METPO:1004004 | One file scanned; zero strict errors. |
| Focused source snippet verification | passed | True | METPO:1004004 | Six occurrences across two references: four NOT_IN_ABSTRACT and two UNRESOLVED. These are inconclusive source-access results, not six verified quotations. Publisher and bibliographic checks separately establish citation-identity concerns. |
| Expression-module applicability | not_applicable | False | METPO:1004004 | The record does not assign a strain/locus-specific expression assertion to a generic graph node. Expression modules would not establish this host-defined pathogenicity class, and no unrelated module or new molecular target is introduced. |

## Scientific And Domain Assessments

### Native checklist: identifier, definition identity, polarity and kind

identity: supported. Targets: METPO:1004004.

The active METPO class exactly matches the target and its human-host distinction. The local class definition remains identifiable despite the mismatched literature citation. Disease capability is not automatically host exclusivity.

### Native checklist: definition-source suitability

evidence: concern. Targets: METPO:1004004.

The ontology supports the class wording, but the designated literature source is a narrow E. coli review. The source has been characterized more broadly than the inspected publication supports.

### Native checklist: broader parent

consistency: supported. Targets: METPO:1004004.

Pathogenic to host is strictly broader than its human-host subclass; both identifiers are active in the captured ontology.

### Native checklist: ecology class and nonmechanistic scope

representation: supported. Targets: METPO:1004004.

The ecological class and declared NONMECHANISTIC scope are coherent. The generic reviewed protein aggregate need not be given a token accession or expanded into a universal mechanism.

### Native checklist: related source alias and citation

provenance: concern. Targets: METPO:1004004.

The related alias and official citation are suitable. The accompanying unversioned exact-set/union-only rationale exceeds what was established from the inspected source metadata; historical source bytes remain unknown.

### Native checklist: both generic examples and exact taxa

evidence: supported. Targets: METPO:1004004.

Both taxonomy identities and the narrow species/disease assertions are supported directly by source abstracts. This does not extend their mechanistic results to the whole class.

### Native checklist: all citation identities and six snippets

evidence: concern. Targets: METPO:1004004.

Nine citation identities were accounted for, including the related-alias citation. One DOI is the wrong publication type/topic and another is narrower than claimed. None of the six short snippet occurrences was verified by the native checker; inspected surfaces do not establish their full-text exactness or the attached broad claims.

### Native checklist: all thirteen nodes and twelve edges

graph: concern. Targets: METPO:1004004.

All nodes and endpoints were inspected for conceptual representation. Grounded GO identities match. Eight external RO edges conflict with endpoint meanings, and one provisional local relation is used outside its stated subject meaning. The source review establishes framing and uncertainty, not a verified mechanistic model.

Zero-based ledger: node0 is the trait; nodes1 and5 are protein aggregates/complexes, with node5’s GO cellular-component grounding appropriate. Nodes2–4 and6–11 are described as processes; node12 is explicitly a trait/disposition. Nodes7 and11 have matching GO process identifiers. Edge0 has compatible external endpoint types but the attached broad citation claim is not established. Edges1 and2 use process subjects with material-executor enables; their original citations also need correction. Edge3 uses the provisional microorganism-state relation for host pathology. Edge4 has compatible endpoint types and abstract-level topical context only. Edges5,6,8 and9 use process subjects with enables. Edge7 uses a process-to-protein shape with material-to-process contributes to. Edge10 fits the documented provisional confers shape, but detailed source support is unverified. Edge11 uses a disposition as the enables executor. Edge9’s categorical source interpretation loses the abstract’s qualifications. This ledger provides no corrected biological route, targets or experimental steps.

### Native checklist: discussion and dataset slots

completeness: supported. Targets: METPO:1004004.

No discussion placeholders or asserted dataset accessions require resolution. These optional slots need not be invented to review the ecological classification.

### Native checklist: native REVIEWED and history

provenance: concern. Targets: METPO:1004004.

The history is explicit about assistance and scripted imports, but does not identify human scientific acceptance in the inspected target-specific materials. Saved review validation and PR publication do not supply such sign-off.

## Findings

### citation-identity-and-scope: Foundational citations are mischaracterized

major / open / confirmed; issue key: human-pathogen-citation-identity-and-scope.

The purported secretion-systems review DOI resolves to the editorial In this issue. The definition DOI resolves to a narrow E. coli review rather than the general source characterized by the record. The inspected text does not support the attached broad definition/graph assertions. The two-word snippets do not remedy those source mismatches, and their absence from inspected surfaces is not a claim that all inaccessible full text was searched.

### external-relation-endpoints: Eight edges conflict with inherited RO endpoint semantics

major / open / confirmed; issue key: human-pathogen-external-relation-endpoints.

Edges1,2,5,6,8 and9 have process subjects under RO enables; edge11 has a trait/disposition subject. Edge7 is process-to-protein under RO contributes to, which inherits material-entity-to-process semantics. The historical explanation based on a similarly named Biolink relation does not verify the selected RO identifier. This is semantic analysis, not a reported reasoner or YAML-validation failure.

### conditional-outcome-overstated: Categorical outcome wording drops source uncertainty

major / open / confirmed; issue key: human-pathogen-conditional-outcome-overstated.

Edge9 states an outcome categorically, whereas the cited review abstract uses conditional language and discusses context-dependent outcomes and trade-offs. The record’s own evidence note uses can, exposing the stronger edge description. Retaining those qualifications is necessary; this finding does not infer a uniform opposite outcome or supply a replacement mechanism.

### provisional-manifestation-meaning: The provisional manifestation relation is used for a different subject meaning

minor / open / confirmed; issue key: human-pathogen-provisional-manifestation-meaning.

The local v2 definition concerns a microorganism’s physiological/molecular state, while edge3 describes pathology in the human host. The wildcard mapping allows the shape but does not establish this meaning. This is a bounded local proposal consistency issue, not a claim that an active upstream relation failed formal typing.

### alias-equivalence-provenance: Alias rationale overstates source-group equivalence

minor / open / confirmed; issue key: human-pathogen-alias-equivalence-provenance.

The RELATED_SYNONYM slot is appropriate. Its writer/history rationale nevertheless describes an exact same set and a union-only construction without pinning a release. Current official FAPROTAX1.2.12 has group inclusions plus direct entries and does not establish exhaustive equivalence to the biological class. This does not prove which database bytes historical microbedecoder used or disprove its reported occurrence count.

### reviewed-signoff-not-documented: The inspected REVIEWED provenance lacks a human-acceptance link

minor / open / confirmed; issue key: human-pathogen-reviewed-signoff-not-documented.

The fifteen AI-assisted events and two scripted import events do not identify human scientific acceptance. The native checklist requires it for REVIEWED. This bounded local documentation finding does not establish absence of private or remote approval.

## Recommended Actions And Acceptance Checks

### reconcile-source-identities

Correct citation characterization and evidence placement in a separately authorized curation pass.

- Confirm exact publication identity and claim scope before retaining a reference.
- Do not treat generic two-word matches as proof of a detailed assertion; preserve inaccessible-text limitations.
- Limit follow-up to source fidelity and class definition; no new pathogen mechanism, molecular target or experimental route is proposed.

### align-relation-meaning

Reconcile ontology and local-proposal meanings with the existing endpoint concepts.

- Check the actual selected identifier, inherited constraints and local proposal definition rather than relying on a similarly named relation.
- Preserve microorganism-versus-host entity distinctions; do not invent biological intermediates or retype entities to fit a preferred ID.
- Any shared mapping change requires separate scope review; authorized curation retains guarded writes, appended history and applicable validation/qc gates.

### preserve-source-certainty

Align the strength of the statement with the cited conditional source.

- Keep source context, uncertainty and the record’s own qualifying evidence note consistent.
- Do not replace an overstated universal with an opposite universal or an operational biological recommendation.

### clarify-alias-provenance

Retain the related alias and clarify the maintained source-mapping rationale.

- Record a versioned group locator and retain RELATED_SYNONYM rather than asserting exhaustive equality.
- Preserve historical events; append a clarification during authorized curation instead of rewriting the old history.
- Keep the historical source version and occurrence count unverified unless the original input is recovered.

### document-human-acceptance

Locate and document the status basis or retain the question as unresolved.

- Neither automated validation, scripted import nor an AI-authored review establishes a human approver.
- Any status change requires separate curation authorization and a new history event.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; metadata validate-history.json | context_only | 1276 history records checked, zero invalid links; integrity does not establish scientific correctness or human sign-off. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-human_pathogen-validate | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/human_pathogen-validate.log; Executed 2026-10-21T06:44:15Z through 2026-10-21T06:44:16Z; metadata human_pathogen-validate.json | context_only | The selected record validates. |
| check-human_pathogen-strict | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/human_pathogen-strict.log; Executed 2026-10-21T06:44:15Z through 2026-10-21T06:44:17Z; metadata human_pathogen-strict.json | context_only | One file scanned; zero strict errors. |
| check-human_pathogen-snippets | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/human_pathogen-snippets.log; Executed 2026-10-21T06:44:19Z through 2026-10-21T06:44:22Z; metadata human_pathogen-snippets.json | context_only | Six occurrences across two references: four NOT_IN_ABSTRACT and two UNRESOLVED. These are inconclusive source-access results, not six verified quotations. Publisher and bibliographic checks separately establish citation-identity concerns. |
| record | data/traits/ecology/human_pathogen.yaml; Entire target, including thirteen nodes, twelve edges, two examples and seventeen history events | partial | The definition specifies host species. The NONMECHANISTIC declaration does not make every contextual molecular claim a class-defining requirement. Source identity, certainty and relation semantics require correction. |
| identity | data/raw/metpo.owl; Complete captured RDF and exact target/parent entities; provisional predicate searches | supports | METPO:1004004 is active human pathogen with the record’s definition; its active parent METPO:1004000 is pathogenic to host. Neither METPO:2007400 nor METPO:2007700 occurs in the complete captured release; local v2/v8 proposals document their provisional status. |
| parent | data/traits/ecology/pathogenic_to_host.yaml; Identifier, definition and parent relation | supports | Pathogenicity to a host is broader than the stated human-host subclass. This contextual inspection does not review the parent’s entire graph. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0043684%2CGO%3A0009292%2CGO%3A0042710; Exact live GO term identities, aspects and obsolete flags | supports | All three IDs are active and match their stated node identities. GO:0043684 is a cellular component compatible with a protein complex, while GO:0009292 and GO:0042710 are biological processes. This validates identity/type compatibility, not the biological graph claims. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1280,1773&amp;retmode=xml; Exact live species identities | supports | NCBITaxon:1280 and NCBITaxon:1773 resolve to Staphylococcus aureus and Mycobacterium tuberculosis, respectively. |
| relations | Cached authoritative RO database; RO enables and contributes to with recursive superproperty definitions and domains/ranges | refutes | The actual RO identifiers inherit material-executor-to-process semantics. Process/disposition subjects and the process-to-protein edge do not match those meanings. The historical use of a Biolink description does not establish the meaning of the selected RO identifier. |
| proposals | proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv; proposals/metpo_traitmech_v8/proposal.md; v2 manifests-as row3; v8 distinction from manifests-as and confers scope | partial | The v2 relation concerns a physiological/molecular state of a microorganism and its phenotype. Current host pathology is a different subject meaning. The v8 confers relation explicitly accommodates process-to-trait context. These are local proposal semantics, not active upstream identity claims. |
| bibliography | https://www.ebi.ac.uk/europepmc/webservices/rest/search; https://api.crossref.org/works/; Eight non-alias citations plus separately checked FAPROTAX citation | partial | All nine citation identities were accounted for. Seven current non-alias items resolve through PubMed; the remaining DOI is identified through Crossref and the publisher as an editorial. Identifier resolution does not prove that the record characterizes a source correctly. |
| definition-source | https://www.annualreviews.org/content/journals/10.1146/annurev.micro.62.081307.162938; Publisher title and abstract; indexed abstract PMID18785838 | partial | The DOI identifies Regulation and Function of Ag43 (Flu), a narrow E. coli review encompassing pathogenic and commensal isolates. The inspected abstract does not establish the broad human-pathogen definition or the general source characterization used by the record. The two-word snippet is absent from the inspected title/abstract; its full-text occurrence remains unverified. |
| editorial | https://www.nature.com/articles/nrmicro1592; Publisher heading and two displayed editorial paragraphs; matching Crossref metadata | refutes | The source is In this issue, Nature Reviews Microbiology5:1 (2007), with displayed ecological editorial text. It is not the secretion-systems review claimed by the record. The supplied two-word phrase does not occur in the inspected preview. The local shell200 response was a challenge, and a later browser reaccess also failed; neither is presented as successful full-text access. |
| editorial-metadata | https://api.crossref.org/works/10.1038%2Fnrmicro1592; Exact work title, publication and DOI | supports | Crossref independently identifies the short editorial under the cited DOI. |
| example-saureus | https://pubmed.ncbi.nlm.nih.gov/30209034/; Indexed abstract opening sentence | supports | The source explicitly supports S. aureus as a major human pathogen. Its narrower review focus does not invalidate that generic species-level statement; no additional mechanism is inferred. |
| example-mtb | https://pubmed.ncbi.nlm.nih.gov/40588584/; Indexed abstract disease association | supports | The abstract supports the generic association between M. tuberculosis and human tuberculosis. No strain-specific or mechanistic assertion is added. |
| context-t4 | https://doi.org/10.1038/s41579-023-00974-3; Indexed abstract, PMID37814112 | partial | The source identity and broad bacterial review context are established. That scope is not human-exclusive, and the abstract does not certify every detailed edge in the record. |
| context-hgt | https://doi.org/10.1093/femsre/fuae019; Indexed abstract, PMID39003250 | partial | The review concerns bacterial pathogens of humans and related mammals. Topical suitability is established; the detailed mechanism assertions are not independently certified by this abstract-level check. |
| context-evolution | https://doi.org/10.1146/annurev-pathmechdis-051122-111408; Indexed abstract, PMID37832940; conditional wording and scope | partial | The abstract presents context-dependent outcomes and trade-offs using conditional language. The current categorical outcome statement drops that uncertainty. This does not establish an opposite universal effect and supplies no corrective biological mechanism. |
| context-biofilm | https://doi.org/10.3389/fmicb.2024.1370818; Indexed abstract, PMID38444801 | partial | The citation identifies a general bacterial pathogenicity review. Its abstract does not independently substantiate the detailed treatment-related note. Full-paper support remains unverified, not disproved. |
| alias | https://pages.uoregon.edu/slouca/LoucaLab/archive/FAPROTAX/; Official FAPROTAX1.2.12 human_pathogens_all group lines5418–5689; format lines57–65; official citation page | partial | The source group combines six group inclusions with direct entries. The official citation page and Crossref support DOI10.1126/science.aaf4507. RELATED_SYNONYM is appropriate as a lookup mapping; the unversioned writer/history rationale does not establish an exhaustive exact-set equivalence. Current metadata cannot reconstruct the original microbedecoder input or validate its historical occurrence count. |
| owners | scripts/add_faprotax_synonyms.py; scripts/migrate_enables_range_edges.py; mappings/predicate_grounding.tsv; Target-specific alias rationale, historical endpoint corrections and current mapping assignments | partial | The maintained alias writer and companion history preserve a stronger equivalence rationale than the related-synonym slot requires. Predicate history addresses selected earlier object-type problems but does not establish the remaining RO subject semantics. Future scientific corrections require guarded writes and new history. |
| model | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, claim-specific source scope, graph grounding and human-sign-off requirements | partial | NONMECHANISTIC classification and reviewed generic aggregates do not require new molecular examples or invented steps. Evidence must support the nearest claim, and automated checks do not establish human acceptance. |
| graph-shape | Read-only graph ledger; Thirteen nodes and twelve edges | supports | All endpoints resolve and local shape is valid. This is distinct from external predicate semantics and scientific evidence strength. |
| search | Local repository identity/owner/provenance search; Ignored-inclusive target identifier, label and slug search | partial | The target has fifteen AI-assisted events and two named import-script events. Neither kind identifies human scientific acceptance. No target-specific acceptance link was found in the inspected local material; remote/private approval remains unknown. |

## Limits And Additional Notes

- The review inspects the whole record for identity, evidence framing, ontology and provenance. Detailed pathogen mechanisms are not reconstructed, optimized or independently certified from abstract-level evidence.
- Seven non-alias sources were inspected through indexed abstracts. The editorial identity and displayed preview were inspected through publisher/Crossref surfaces; inaccessible subscription text was not exhaustively searched.
- The six snippet occurrences yielded four NOT_IN_ABSTRACT and two UNRESOLVED results. Those statuses are inconclusive, and no full-text quotation exactness is claimed.
- Nature shell200 was a challenge and later browser access failed. Successful preview inspection occurred within06:44:37–06:45:22UTC; the evidence timestamp records that window’s endpoint, not a fabricated exact request time.
- Detailed source support for several contextual graph edges remains unverified. Bibliographic/topic matches and ontology type compatibility are not treated as experimental confirmation.
- The current FAPROTAX release is1.2.12. Historical source release and residual-count input were not identified; the current source cannot reconstruct them.
- The v2/v8 predicate identifiers remain documented proposals in the captured ontology context. Upstream acceptance is not inferred.
- Earlier full-corpus diagnostics retain their actual timestamps, baseline findings, superseded failures and product-adapter skips at the unchanged scientific base.
- No human scientific sign-off, native status promotion or scientific record change is performed.
- An initial native inspect failed because a guessed parent filename was wrong. Exact ignored-inclusive identifier search resolved pathogenic_to_host.yaml; the successful35-input capture preceded judgment. This was an inspection setup error, not a review-validation failure.
- Independent read-only citation, alias and ontology inspections informed the final manual assessment. Source summaries are not treated as primary evidence in place of the identified source surfaces.
- Only this new immutable review bundle is saved. No pathogen mechanism, experimental protocol or enhancement recommendation is added to the repository.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T064811Z-human-pathogen
kind: record
repository: CultureBotAI/TraitMech
title: Identity, source and representation review of human pathogen (METPO:1004004)
started_at: '2026-10-21T06:43:51Z'
finished_at: '2026-10-21T06:48:11Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Current review session did not author or change the captured
    trait. Supporting agents inspected sources and prepared draft observations; root
    reviewer integrates and validates the final review. Historical Codex/Claude curation
    events are disclosed and are not human sign-off.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The active METPO identity, parent, three GO identifiers and two species examples
  are supported. All thirteen nodes and twelve edges were inspected for source scope
  and representation. Three major findings concern mischaracterized citations, eight
  external relation/endpoint conflicts and source uncertainty lost in categorical
  wording. Three minor findings concern a provisional relation’s local meaning, overstrong
  alias provenance and a missing human-acceptance link. Detailed pathogen mechanisms
  are not certified or reconstructed; unverified source support is explicit. The review
  proposes documentary and conceptual corrections only.
source:
  git_revision: f25e2af0b38a8303b13f627a9a5c33b36af4b3d2
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
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/ecology/human_pathogen.yaml
    sha256: 104a578c4be34231855c6e1ec0e963f58eb89f52cc70152fe4b004ce80ceae43
    role: target
  - path: data/traits/ecology/pathogenic_to_host.yaml
    sha256: 6086ef781d3871684a8a21c77330be972673657b83b5fa0d4ba9c52e376ca451
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
  - path: history/infrastructure/add_faprotax_synonyms/2026-08-20T025913Z-claude-code-d035e0.yaml
    sha256: 0867403cd78fb6c7f28dd972c508a6843bee40da456d5b32c6d02f82ac6ef104
    role: context
  - path: mappings/node_grounding.tsv
    sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
    role: context
  - path: mappings/predicate_grounding.tsv
    sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
    role: context
  - path: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv
    sha256: 4ab5ca37ff8595210254b1099563b4425ecd737ed375dc5a932b44e2ad5c332e
    role: context
  - path: proposals/metpo_traitmech_v2/proposal.md
    sha256: fe0601356b120ef9babc6f90a417f860bf02aa628c46af661517f168e01bc48f
    role: context
  - path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
    role: context
  - path: proposals/metpo_traitmech_v5/proposal.md
    sha256: 5d54623dd00ac80a8d67a0eab7b70385f7f57b36daa205c28aa1f9d6f9be6167
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
  - path: scripts/add_faprotax_synonyms.py
    sha256: f0fdee608949555ee009bb8fe97abb1093de2d6d6c924be37f658635ff3b63df
    role: context
  - path: scripts/audit_causal_graphs.py
    sha256: e0c26506c9de712700317284f142097e7bf69334806b8010db5d6517e905e834
    role: context
  - path: scripts/curate_knowledge_gaps.py
    sha256: 9e0fb7e01a901d84189a28f1912a2552f28d2da8733c113589e4947359d48c73
    role: context
  - path: scripts/migrate_enables_range_edges.py
    sha256: 3d0d1bddcaa76baef5833973e2e979e4fee1f834c67d1abcc69a8d866ecb8f32
    role: context
  - path: scripts/migrate_enables_trait_edges.py
    sha256: a5e7965ee4f6b6ba5bae3a06bced2a83cbf755f3b9b150ce6acc0cd808cb1d88
    role: context
  - path: scripts/migrate_microbe_domain_edges.py
    sha256: 5187ccfb2897d415b243792a27afd6002c0eea4b167068639ff5be73ed583bb6
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
- target_id: METPO:1004004
  path: data/traits/ecology/human_pathogen.yaml
  label: human pathogen
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/human_pathogen.yaml
    role: Maintained scientific record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_faprotax_synonyms.py
    role: Maintained source-alias writer
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Eighth target in batch002, selected in lexicographic path order from
    the validated inventory union; one entire previously uncovered TraitRecord.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1004004
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1004004
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1004004
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1004004
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1004004
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1276 history records checked, zero invalid links; integrity does not establish
    scientific correctness or human sign-off.
  evidence_ids:
  - check-validate-history
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1004004
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1004004
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1004004
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: human_pathogen-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - METPO:1004004
  command: just validate data/traits/ecology/human_pathogen.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The selected record validates.
  evidence_ids:
  - check-human_pathogen-validate
- check_id: human_pathogen-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1004004
  command: just validate-strict data/traits/ecology/human_pathogen.yaml --out /private/tmp/traitmech-record-sweep-002.mdt7dqwk/human_pathogen-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero strict errors.
  evidence_ids:
  - check-human_pathogen-strict
- check_id: human_pathogen-snippets
  name: Focused source snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1004004
  command: just verify-snippets --record data/traits/ecology/human_pathogen.yaml --out
    /private/tmp/traitmech-record-sweep-002.mdt7dqwk/human_pathogen-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Six occurrences across two references: four NOT_IN_ABSTRACT and two UNRESOLVED.
    These are inconclusive source-access results, not six verified quotations. Publisher
    and bibliographic checks separately establish citation-identity concerns.'
  evidence_ids:
  - check-human_pathogen-snippets
- check_id: expression-applicability
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1004004
  summary: The record does not assign a strain/locus-specific expression assertion
    to a generic graph node. Expression modules would not establish this host-defined
    pathogenicity class, and no unrelated module or new molecular target is introduced.
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T06:48:11Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T06:48:11Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T06:48:11Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; metadata validate-history.json
  accessed_at: '2026-10-21T06:48:11Z'
  support: context_only
  summary: 1276 history records checked, zero invalid links; integrity does not establish
    scientific correctness or human sign-off.
  snapshot_sha256: 1fc48f1203fbfcd27b1243e4e147afb367aebfc592b496b352201058c6ee85d2
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T06:48:11Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T06:48:11Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T06:48:11Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-human_pathogen-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/human_pathogen-validate.log
  locator: Executed 2026-10-21T06:44:15Z through 2026-10-21T06:44:16Z; metadata human_pathogen-validate.json
  accessed_at: '2026-10-21T06:48:11Z'
  support: context_only
  summary: The selected record validates.
  snapshot_sha256: 00b0ff77db549481fbcb2fa4ccf34601fe87eb02c1cb646b5c7b5789d32b9f41
- evidence_id: check-human_pathogen-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/human_pathogen-strict.log
  locator: Executed 2026-10-21T06:44:15Z through 2026-10-21T06:44:17Z; metadata human_pathogen-strict.json
  accessed_at: '2026-10-21T06:48:11Z'
  support: context_only
  summary: One file scanned; zero strict errors.
  snapshot_sha256: b3acc3e5ad3ef3992a6a0cebf752ac00ef787391c3e99e205661fdf95c203f4e
- evidence_id: check-human_pathogen-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/human_pathogen-snippets.log
  locator: Executed 2026-10-21T06:44:19Z through 2026-10-21T06:44:22Z; metadata human_pathogen-snippets.json
  accessed_at: '2026-10-21T06:48:11Z'
  support: context_only
  summary: 'Six occurrences across two references: four NOT_IN_ABSTRACT and two UNRESOLVED.
    These are inconclusive source-access results, not six verified quotations. Publisher
    and bibliographic checks separately establish citation-identity concerns.'
  snapshot_sha256: d0c0673e5158408929808a6a78980e4a06ea5a18bdad9e77a72ee6fee8fca513
- evidence_id: record
  kind: record_content
  reference: data/traits/ecology/human_pathogen.yaml
  locator: Entire target, including thirteen nodes, twelve edges, two examples and
    seventeen history events
  accessed_at: '2026-10-21T06:48:11Z'
  support: partial
  summary: The definition specifies host species. The NONMECHANISTIC declaration does
    not make every contextual molecular claim a class-defining requirement. Source
    identity, certainty and relation semantics require correction.
  snapshot_sha256: 104a578c4be34231855c6e1ec0e963f58eb89f52cc70152fe4b004ce80ceae43
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl
  locator: Complete captured RDF and exact target/parent entities; provisional predicate
    searches
  accessed_at: '2026-10-21T06:44:18Z'
  support: supports
  summary: METPO:1004004 is active human pathogen with the record’s definition; its
    active parent METPO:1004000 is pathogenic to host. Neither METPO:2007400 nor METPO:2007700
    occurs in the complete captured release; local v2/v8 proposals document their
    provisional status.
  snapshot_sha256: d19f11ea8fdc24c0f0ac888e0afd2f1c414243103b3f0d2ac89828b794cd5122
- evidence_id: parent
  kind: record_content
  reference: data/traits/ecology/pathogenic_to_host.yaml
  locator: Identifier, definition and parent relation
  accessed_at: '2026-10-21T06:48:11Z'
  support: supports
  summary: Pathogenicity to a host is broader than the stated human-host subclass.
    This contextual inspection does not review the parent’s entire graph.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0043684%2CGO%3A0009292%2CGO%3A0042710
  locator: Exact live GO term identities, aspects and obsolete flags
  accessed_at: '2026-10-21T06:44:32Z'
  support: supports
  summary: All three IDs are active and match their stated node identities. GO:0043684
    is a cellular component compatible with a protein complex, while GO:0009292 and
    GO:0042710 are biological processes. This validates identity/type compatibility,
    not the biological graph claims.
  snapshot_sha256: 864977f4820bdc4e7c93f8ffd0f417b88477dad61cd2b353723f26f7dd57aa31
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1280,1773&retmode=xml
  locator: Exact live species identities
  accessed_at: '2026-10-21T06:44:32Z'
  support: supports
  summary: NCBITaxon:1280 and NCBITaxon:1773 resolve to Staphylococcus aureus and
    Mycobacterium tuberculosis, respectively.
  snapshot_sha256: 50d105f7c3bf92ca57b0661983f76e734e85ea0896c1d6768eb36df92c300ada
- evidence_id: relations
  kind: authority
  reference: Cached authoritative RO database
  locator: RO enables and contributes to with recursive superproperty definitions
    and domains/ranges
  accessed_at: '2026-10-21T06:44:18Z'
  support: refutes
  summary: The actual RO identifiers inherit material-executor-to-process semantics.
    Process/disposition subjects and the process-to-protein edge do not match those
    meanings. The historical use of a Biolink description does not establish the meaning
    of the selected RO identifier.
  snapshot_sha256: bc2dbc0094b443d7ad724ad7371850331436dd630c133b3922da578fe2fe5f85
- evidence_id: proposals
  kind: record_content
  reference: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv; proposals/metpo_traitmech_v8/proposal.md
  locator: v2 manifests-as row3; v8 distinction from manifests-as and confers scope
  accessed_at: '2026-10-21T06:48:11Z'
  support: partial
  summary: The v2 relation concerns a physiological/molecular state of a microorganism
    and its phenotype. Current host pathology is a different subject meaning. The
    v8 confers relation explicitly accommodates process-to-trait context. These are
    local proposal semantics, not active upstream identity claims.
- evidence_id: bibliography
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search; https://api.crossref.org/works/
  locator: Eight non-alias citations plus separately checked FAPROTAX citation
  accessed_at: '2026-10-21T06:45:22Z'
  support: partial
  summary: All nine citation identities were accounted for. Seven current non-alias
    items resolve through PubMed; the remaining DOI is identified through Crossref
    and the publisher as an editorial. Identifier resolution does not prove that the
    record characterizes a source correctly.
  snapshot_sha256: 22f1a34c65f1ad309dc99b47366ff54c0932d6b42540d7a8c00d5a12cc2ae599
- evidence_id: definition-source
  kind: primary_source
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev.micro.62.081307.162938
  locator: Publisher title and abstract; indexed abstract PMID18785838
  accessed_at: '2026-10-21T06:44:10Z'
  support: partial
  summary: The DOI identifies Regulation and Function of Ag43 (Flu), a narrow E. coli
    review encompassing pathogenic and commensal isolates. The inspected abstract
    does not establish the broad human-pathogen definition or the general source characterization
    used by the record. The two-word snippet is absent from the inspected title/abstract;
    its full-text occurrence remains unverified.
  snapshot_sha256: 3ac9bf7cc5e3640ff3d1e0a7401d46eea30b470ecf86a4a5b43ae69d46418013
- evidence_id: editorial
  kind: primary_source
  reference: https://www.nature.com/articles/nrmicro1592
  locator: Publisher heading and two displayed editorial paragraphs; matching Crossref
    metadata
  accessed_at: '2026-10-21T06:45:22Z'
  support: refutes
  summary: The source is In this issue, Nature Reviews Microbiology5:1 (2007), with
    displayed ecological editorial text. It is not the secretion-systems review claimed
    by the record. The supplied two-word phrase does not occur in the inspected preview.
    The local shell200 response was a challenge, and a later browser reaccess also
    failed; neither is presented as successful full-text access.
- evidence_id: editorial-metadata
  kind: database
  reference: https://api.crossref.org/works/10.1038%2Fnrmicro1592
  locator: Exact work title, publication and DOI
  accessed_at: '2026-10-21T06:44:41Z'
  support: supports
  summary: Crossref independently identifies the short editorial under the cited DOI.
  snapshot_sha256: 3f1e1c7a624cb8dc2befe101212b0b7d1620576412afe10710170cae73315dae
- evidence_id: example-saureus
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/30209034/
  locator: Indexed abstract opening sentence
  accessed_at: '2026-10-21T06:44:10Z'
  support: supports
  summary: The source explicitly supports S. aureus as a major human pathogen. Its
    narrower review focus does not invalidate that generic species-level statement;
    no additional mechanism is inferred.
  snapshot_sha256: 6cb7607f3e70ffb9fbdfa6eb45a79ea5ac81dd5566a0aa43f63e902e3ba9045b
- evidence_id: example-mtb
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/40588584/
  locator: Indexed abstract disease association
  accessed_at: '2026-10-21T06:44:10Z'
  support: supports
  summary: The abstract supports the generic association between M. tuberculosis and
    human tuberculosis. No strain-specific or mechanistic assertion is added.
  snapshot_sha256: 20786c9852c82dc547644834476fd7be39d08449cb445541c5cb7801aa3e92ba
- evidence_id: context-t4
  kind: primary_source
  reference: https://doi.org/10.1038/s41579-023-00974-3
  locator: Indexed abstract, PMID37814112
  accessed_at: '2026-10-21T06:44:10Z'
  support: partial
  summary: The source identity and broad bacterial review context are established.
    That scope is not human-exclusive, and the abstract does not certify every detailed
    edge in the record.
  snapshot_sha256: 1a52db86672c9e1c640449ad33471df4535bef53f0f8f3563cbbfe1902956717
- evidence_id: context-hgt
  kind: primary_source
  reference: https://doi.org/10.1093/femsre/fuae019
  locator: Indexed abstract, PMID39003250
  accessed_at: '2026-10-21T06:44:10Z'
  support: partial
  summary: The review concerns bacterial pathogens of humans and related mammals.
    Topical suitability is established; the detailed mechanism assertions are not
    independently certified by this abstract-level check.
  snapshot_sha256: 3fcc332b6a09b2b5be7029f400fefe32d9c2d43c6d5f70e2b0fdbfd3a92aaf8c
- evidence_id: context-evolution
  kind: primary_source
  reference: https://doi.org/10.1146/annurev-pathmechdis-051122-111408
  locator: Indexed abstract, PMID37832940; conditional wording and scope
  accessed_at: '2026-10-21T06:44:10Z'
  support: partial
  summary: The abstract presents context-dependent outcomes and trade-offs using conditional
    language. The current categorical outcome statement drops that uncertainty. This
    does not establish an opposite universal effect and supplies no corrective biological
    mechanism.
  snapshot_sha256: f2cec619e48ab398673fa401ec608226b8d355eac107196500cadd8936656317
- evidence_id: context-biofilm
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2024.1370818
  locator: Indexed abstract, PMID38444801
  accessed_at: '2026-10-21T06:44:10Z'
  support: partial
  summary: The citation identifies a general bacterial pathogenicity review. Its abstract
    does not independently substantiate the detailed treatment-related note. Full-paper
    support remains unverified, not disproved.
  snapshot_sha256: f4c71a64bdae89344133b0e69734904209439d3042634924a0152eeac047acd7
- evidence_id: alias
  kind: database
  reference: https://pages.uoregon.edu/slouca/LoucaLab/archive/FAPROTAX/
  locator: Official FAPROTAX1.2.12 human_pathogens_all group lines5418–5689; format
    lines57–65; official citation page
  accessed_at: '2026-10-21T06:45:58Z'
  support: partial
  summary: The source group combines six group inclusions with direct entries. The
    official citation page and Crossref support DOI10.1126/science.aaf4507. RELATED_SYNONYM
    is appropriate as a lookup mapping; the unversioned writer/history rationale does
    not establish an exhaustive exact-set equivalence. Current metadata cannot reconstruct
    the original microbedecoder input or validate its historical occurrence count.
  snapshot_sha256: 7b9fbbd6c1dcb88d8220dec1e061cebbca1f446ea42525df6713ba2cf03639dc
- evidence_id: owners
  kind: record_content
  reference: scripts/add_faprotax_synonyms.py; scripts/migrate_enables_range_edges.py;
    mappings/predicate_grounding.tsv
  locator: Target-specific alias rationale, historical endpoint corrections and current
    mapping assignments
  accessed_at: '2026-10-21T06:48:11Z'
  support: partial
  summary: The maintained alias writer and companion history preserve a stronger equivalence
    rationale than the related-synonym slot requires. Predicate history addresses
    selected earlier object-type problems but does not establish the remaining RO
    subject semantics. Future scientific corrections require guarded writes and new
    history.
- evidence_id: model
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, claim-specific source scope, graph grounding and human-sign-off
    requirements
  accessed_at: '2026-10-21T06:48:11Z'
  support: partial
  summary: NONMECHANISTIC classification and reviewed generic aggregates do not require
    new molecular examples or invented steps. Evidence must support the nearest claim,
    and automated checks do not establish human acceptance.
- evidence_id: graph-shape
  kind: validation
  reference: Read-only graph ledger
  locator: Thirteen nodes and twelve edges
  accessed_at: '2026-10-21T06:46:09Z'
  support: supports
  summary: All endpoints resolve and local shape is valid. This is distinct from external
    predicate semantics and scientific evidence strength.
  snapshot_sha256: d7ab4ce73b87393ab9aaadd1092aaf5099f5f21368798d239781ca304e99c6f6
- evidence_id: search
  kind: search
  reference: Local repository identity/owner/provenance search
  locator: Ignored-inclusive target identifier, label and slug search
  accessed_at: '2026-10-21T06:44:54Z'
  support: partial
  summary: The target has fifteen AI-assisted events and two named import-script events.
    Neither kind identifies human scientific acceptance. No target-specific acceptance
    link was found in the inspected local material; remote/private approval remains
    unknown.
  snapshot_sha256: ca189434fbb1716b64ddac00836af53da527ef8c55706b6881b2f479c8d41cdc
  search_scope: rg --no-ignore --hidden in the target and maintained scripts/history/docs/reviews/mappings/proposals/conf/DO_NOT_WORK.md;
    complete captured METPO RDF inspected separately. Ignored files included. The
    parent was resolved by exact identifier search to pathogenic_to_host.yaml after
    an initial wrong-filename inspection attempt; no judgment preceded the successful
    native capture. Human-acceptance finding is bounded to inspected target-specific
    provenance.
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, definition identity, polarity and kind'
  outcome: supported
  target_ids:
  - METPO:1004004
  summary: The active METPO class exactly matches the target and its human-host distinction.
    The local class definition remains identifiable despite the mismatched literature
    citation. Disease capability is not automatically host exclusivity.
  evidence_ids:
  - record
  - identity
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: definition-source suitability'
  outcome: concern
  target_ids:
  - METPO:1004004
  summary: The ontology supports the class wording, but the designated literature
    source is a narrow E. coli review. The source has been characterized more broadly
    than the inspected publication supports.
  evidence_ids:
  - record
  - identity
  - definition-source
- assessment_id: hierarchy
  area: consistency
  topic: 'Native checklist: broader parent'
  outcome: supported
  target_ids:
  - METPO:1004004
  summary: Pathogenic to host is strictly broader than its human-host subclass; both
    identifiers are active in the captured ontology.
  evidence_ids:
  - record
  - parent
  - identity
- assessment_id: category
  area: representation
  topic: 'Native checklist: ecology class and nonmechanistic scope'
  outcome: supported
  target_ids:
  - METPO:1004004
  summary: The ecological class and declared NONMECHANISTIC scope are coherent. The
    generic reviewed protein aggregate need not be given a token accession or expanded
    into a universal mechanism.
  evidence_ids:
  - record
  - model
- assessment_id: alias
  area: provenance
  topic: 'Native checklist: related source alias and citation'
  outcome: concern
  target_ids:
  - METPO:1004004
  summary: The related alias and official citation are suitable. The accompanying
    unversioned exact-set/union-only rationale exceeds what was established from the
    inspected source metadata; historical source bytes remain unknown.
  evidence_ids:
  - record
  - alias
  - owners
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: both generic examples and exact taxa'
  outcome: supported
  target_ids:
  - METPO:1004004
  summary: Both taxonomy identities and the narrow species/disease assertions are
    supported directly by source abstracts. This does not extend their mechanistic
    results to the whole class.
  evidence_ids:
  - record
  - taxa
  - example-saureus
  - example-mtb
- assessment_id: evidence
  area: evidence
  topic: 'Native checklist: all citation identities and six snippets'
  outcome: concern
  target_ids:
  - METPO:1004004
  summary: Nine citation identities were accounted for, including the related-alias
    citation. One DOI is the wrong publication type/topic and another is narrower
    than claimed. None of the six short snippet occurrences was verified by the native
    checker; inspected surfaces do not establish their full-text exactness or the
    attached broad claims.
  evidence_ids:
  - bibliography
  - definition-source
  - editorial
  - editorial-metadata
  - alias
  - check-human_pathogen-snippets
- assessment_id: graph
  area: graph
  topic: 'Native checklist: all thirteen nodes and twelve edges'
  outcome: concern
  target_ids:
  - METPO:1004004
  summary: All nodes and endpoints were inspected for conceptual representation. Grounded
    GO identities match. Eight external RO edges conflict with endpoint meanings,
    and one provisional local relation is used outside its stated subject meaning.
    The source review establishes framing and uncertainty, not a verified mechanistic
    model.
  evidence_ids:
  - record
  - identity
  - go
  - relations
  - proposals
  - graph-shape
  - definition-source
  - editorial
  - context-t4
  - context-hgt
  - context-evolution
  - context-biofilm
  - model
  details: 'Zero-based ledger: node0 is the trait; nodes1 and5 are protein aggregates/complexes,
    with node5’s GO cellular-component grounding appropriate. Nodes2–4 and6–11 are
    described as processes; node12 is explicitly a trait/disposition. Nodes7 and11
    have matching GO process identifiers. Edge0 has compatible external endpoint types
    but the attached broad citation claim is not established. Edges1 and2 use process
    subjects with material-executor enables; their original citations also need correction.
    Edge3 uses the provisional microorganism-state relation for host pathology. Edge4
    has compatible endpoint types and abstract-level topical context only. Edges5,6,8
    and9 use process subjects with enables. Edge7 uses a process-to-protein shape
    with material-to-process contributes to. Edge10 fits the documented provisional
    confers shape, but detailed source support is unverified. Edge11 uses a disposition
    as the enables executor. Edge9’s categorical source interpretation loses the abstract’s
    qualifications. This ledger provides no corrected biological route, targets or
    experimental steps.'
- assessment_id: discussion
  area: completeness
  topic: 'Native checklist: discussion and dataset slots'
  outcome: supported
  target_ids:
  - METPO:1004004
  summary: No discussion placeholders or asserted dataset accessions require resolution.
    These optional slots need not be invented to review the ecological classification.
  evidence_ids:
  - record
  - model
- assessment_id: status
  area: provenance
  topic: 'Native checklist: native REVIEWED and history'
  outcome: concern
  target_ids:
  - METPO:1004004
  summary: The history is explicit about assistance and scripted imports, but does
    not identify human scientific acceptance in the inspected target-specific materials.
    Saved review validation and PR publication do not supply such sign-off.
  evidence_ids:
  - record
  - owners
  - search
  - model
  - check-validate-history
findings:
- finding_id: citation-identity-and-scope
  issue_key: human-pathogen-citation-identity-and-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Foundational citations are mischaracterized
  description: The purported secretion-systems review DOI resolves to the editorial
    In this issue. The definition DOI resolves to a narrow E. coli review rather than
    the general source characterized by the record. The inspected text does not support
    the attached broad definition/graph assertions. The two-word snippets do not remedy
    those source mismatches, and their absence from inspected surfaces is not a claim
    that all inaccessible full text was searched.
  target_ids:
  - METPO:1004004
  field_paths:
  - definition_source
  - evidence
  - causal_graphs[0].edges[0].evidence
  - causal_graphs[0].edges[1].evidence
  - causal_graphs[0].edges[2].evidence
  - causal_graphs[0].edges[3].evidence
  evidence_ids:
  - record
  - definition-source
  - editorial
  - editorial-metadata
  - check-human_pathogen-snippets
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/human_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: external-relation-endpoints
  issue_key: human-pathogen-external-relation-endpoints
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Eight edges conflict with inherited RO endpoint semantics
  description: Edges1,2,5,6,8 and9 have process subjects under RO enables; edge11
    has a trait/disposition subject. Edge7 is process-to-protein under RO contributes
    to, which inherits material-entity-to-process semantics. The historical explanation
    based on a similarly named Biolink relation does not verify the selected RO identifier.
    This is semantic analysis, not a reported reasoner or YAML-validation failure.
  target_ids:
  - METPO:1004004
  field_paths:
  - causal_graphs[0].edges[1].predicate_id
  - causal_graphs[0].edges[2].predicate_id
  - causal_graphs[0].edges[5].predicate_id
  - causal_graphs[0].edges[6].predicate_id
  - causal_graphs[0].edges[7].predicate_id
  - causal_graphs[0].edges[8].predicate_id
  - causal_graphs[0].edges[9].predicate_id
  - causal_graphs[0].edges[11].predicate_id
  evidence_ids:
  - record
  - relations
  - owners
  - graph-shape
  - model
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/human_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping; separate scope review required for future mapping
      changes
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: conditional-outcome-overstated
  issue_key: human-pathogen-conditional-outcome-overstated
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Categorical outcome wording drops source uncertainty
  description: Edge9 states an outcome categorically, whereas the cited review abstract
    uses conditional language and discusses context-dependent outcomes and trade-offs.
    The record’s own evidence note uses can, exposing the stronger edge description.
    Retaining those qualifications is necessary; this finding does not infer a uniform
    opposite outcome or supply a replacement mechanism.
  target_ids:
  - METPO:1004004
  field_paths:
  - causal_graphs[0].edges[9].description
  - causal_graphs[0].edges[9].evidence
  - causal_graphs[0].nodes[10].description
  evidence_ids:
  - record
  - context-evolution
  - model
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/human_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: provisional-manifestation-meaning
  issue_key: human-pathogen-provisional-manifestation-meaning
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The provisional manifestation relation is used for a different subject meaning
  description: The local v2 definition concerns a microorganism’s physiological/molecular
    state, while edge3 describes pathology in the human host. The wildcard mapping
    allows the shape but does not establish this meaning. This is a bounded local
    proposal consistency issue, not a claim that an active upstream relation failed
    formal typing.
  target_ids:
  - METPO:1004004
  field_paths:
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].nodes[4]
  evidence_ids:
  - record
  - proposals
  - identity
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/human_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping; separate scope review required for future mapping
      changes
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: alias-equivalence-provenance
  issue_key: human-pathogen-alias-equivalence-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Alias rationale overstates source-group equivalence
  description: The RELATED_SYNONYM slot is appropriate. Its writer/history rationale
    nevertheless describes an exact same set and a union-only construction without
    pinning a release. Current official FAPROTAX1.2.12 has group inclusions plus direct
    entries and does not establish exhaustive equivalence to the biological class.
    This does not prove which database bytes historical microbedecoder used or disprove
    its reported occurrence count.
  target_ids:
  - METPO:1004004
  field_paths:
  - synonyms[0]
  - curation_history[15].changes
  evidence_ids:
  - record
  - alias
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/human_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/add_faprotax_synonyms.py
    role: Maintained source-alias rationale and guarded writer
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: reviewed-signoff-not-documented
  issue_key: human-pathogen-reviewed-signoff-not-documented
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The inspected REVIEWED provenance lacks a human-acceptance link
  description: The fifteen AI-assisted events and two scripted import events do not
    identify human scientific acceptance. The native checklist requires it for REVIEWED.
    This bounded local documentation finding does not establish absence of private
    or remote approval.
  target_ids:
  - METPO:1004004
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - record
  - search
  - model
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/human_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-source-identities
  description: Correct citation characterization and evidence placement in a separately
    authorized curation pass.
  finding_ids:
  - citation-identity-and-scope
  target_ids:
  - METPO:1004004
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/human_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Confirm exact publication identity and claim scope before retaining a reference.
  - Do not treat generic two-word matches as proof of a detailed assertion; preserve
    inaccessible-text limitations.
  - Limit follow-up to source fidelity and class definition; no new pathogen mechanism,
    molecular target or experimental route is proposed.
- action_id: align-relation-meaning
  description: Reconcile ontology and local-proposal meanings with the existing endpoint
    concepts.
  finding_ids:
  - external-relation-endpoints
  - provisional-manifestation-meaning
  target_ids:
  - METPO:1004004
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/human_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping; separate scope review required for future mapping
      changes
  acceptance_checks:
  - Check the actual selected identifier, inherited constraints and local proposal
    definition rather than relying on a similarly named relation.
  - Preserve microorganism-versus-host entity distinctions; do not invent biological
    intermediates or retype entities to fit a preferred ID.
  - Any shared mapping change requires separate scope review; authorized curation
    retains guarded writes, appended history and applicable validation/qc gates.
- action_id: preserve-source-certainty
  description: Align the strength of the statement with the cited conditional source.
  finding_ids:
  - conditional-outcome-overstated
  target_ids:
  - METPO:1004004
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/human_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Keep source context, uncertainty and the record’s own qualifying evidence note
    consistent.
  - Do not replace an overstated universal with an opposite universal or an operational
    biological recommendation.
- action_id: clarify-alias-provenance
  description: Retain the related alias and clarify the maintained source-mapping
    rationale.
  finding_ids:
  - alias-equivalence-provenance
  target_ids:
  - METPO:1004004
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/human_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/add_faprotax_synonyms.py
    role: Maintained source-alias rationale and guarded writer
  acceptance_checks:
  - Record a versioned group locator and retain RELATED_SYNONYM rather than asserting
    exhaustive equality.
  - Preserve historical events; append a clarification during authorized curation
    instead of rewriting the old history.
  - Keep the historical source version and occurrence count unverified unless the
    original input is recovered.
- action_id: document-human-acceptance
  description: Locate and document the status basis or retain the question as unresolved.
  finding_ids:
  - reviewed-signoff-not-documented
  target_ids:
  - METPO:1004004
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/human_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Neither automated validation, scripted import nor an AI-authored review establishes
    a human approver.
  - Any status change requires separate curation authorization and a new history event.
limitations:
- The review inspects the whole record for identity, evidence framing, ontology and
  provenance. Detailed pathogen mechanisms are not reconstructed, optimized or independently
  certified from abstract-level evidence.
- Seven non-alias sources were inspected through indexed abstracts. The editorial
  identity and displayed preview were inspected through publisher/Crossref surfaces;
  inaccessible subscription text was not exhaustively searched.
- The six snippet occurrences yielded four NOT_IN_ABSTRACT and two UNRESOLVED results.
  Those statuses are inconclusive, and no full-text quotation exactness is claimed.
- Nature shell200 was a challenge and later browser access failed. Successful preview
  inspection occurred within06:44:37–06:45:22UTC; the evidence timestamp records that
  window’s endpoint, not a fabricated exact request time.
- Detailed source support for several contextual graph edges remains unverified. Bibliographic/topic
  matches and ontology type compatibility are not treated as experimental confirmation.
- The current FAPROTAX release is1.2.12. Historical source release and residual-count
  input were not identified; the current source cannot reconstruct them.
- The v2/v8 predicate identifiers remain documented proposals in the captured ontology
  context. Upstream acceptance is not inferred.
- Earlier full-corpus diagnostics retain their actual timestamps, baseline findings,
  superseded failures and product-adapter skips at the unchanged scientific base.
- No human scientific sign-off, native status promotion or scientific record change
  is performed.
notes:
- An initial native inspect failed because a guessed parent filename was wrong. Exact
  ignored-inclusive identifier search resolved pathogenic_to_host.yaml; the successful35-input
  capture preceded judgment. This was an inspection setup error, not a review-validation
  failure.
- Independent read-only citation, alias and ontology inspections informed the final
  manual assessment. Source summaries are not treated as primary evidence in place
  of the identified source surfaces.
- Only this new immutable review bundle is saved. No pathogen mechanism, experimental
  protocol or enhancement recommendation is added to the repository.
tags:
- record-review
- human-pathogen
- ecology
- needs-curation
```
