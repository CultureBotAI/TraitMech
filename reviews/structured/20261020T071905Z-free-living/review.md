# Scientific and source review of free-living (traitmech:000048)

- Review: 20261020T071905Z-free-living
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-20T07:08:08Z
- Finished UTC: 2026-10-20T07:19:05Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The ecological identity, broader parent and two canonical examples are supported at their documented scopes. All nine nodes, eight edges, two context links and the resolved discussion were assessed. Two major findings concern universal metabolic self-sufficiency and RO endpoint semantics. Two minor findings concern evidence placement and missing target-specific human sign-off in the inspected local provenance. Both experimental quotation occurrences match the full texts; source access and expression-dataset limitations remain explicit.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Fourth target in batch002, selected in lexicographic path order from the validated review inventory union. One whole previously uncovered TraitRecord.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f25e2af0b38a8303b13f627a9a5c33b36af4b3d2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000048 | data/traits/ecology/free_living.yaml | maintained | free-living |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000048 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000048 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000048 | The same-base full-corpus check passed 19 context links at pinned PathwayMech aa305727458c44ab05614901334540e2c87a9f3a, including this target’s two links. The pin, index and target-specific scope restrictions were also inspected. |
| Full-corpus history integrity | passed | True | traitmech:000048 | 1276 history records checked, zero invalid links; integrity does not establish scientific correctness or human sign-off. |
| Initial full-product validation | failed | False | traitmech:000048 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000048 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000048 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | traitmech:000048 | The selected record validates. |
| Focused strict validation | passed | True | traitmech:000048 | One file scanned; zero strict errors. |
| Focused source snippet verification | passed | True | traitmech:000048 | Two snippets across two references were NOT_IN_ABSTRACT, an inconclusive result. Both were subsequently matched exactly after normalizing existing whitespace in full-text paragraphs; automated outcomes are retained. |

## Scientific And Domain Assessments

### Native checklist: identifier, label, polarity and kind

identity: supported. Targets: traitmech:000048.

One ecological class is identified; the documented fallback remains appropriate to the captured ontology. Free-living does not require never associating with hosts.

### Native checklist: definition and scope

evidence: supported. Targets: traitmech:000048.

The host-independence boundary is coherent with the inspected ecological context and examples. The formal definition wording itself was not located in the accessible definition-source excerpt.

### Native checklist: parent and cross-record semantics

consistency: supported. Targets: traitmech:000048.

The parent is strictly broader. Both related-record links retain their pinned context-only and organism limitations.

### Native checklist: category, model and scope

representation: supported. Targets: traitmech:000048.

ECOLOGY and CLASS fit the concept. NONMECHANISTIC is appropriate for the broad class; contextual mechanism examples do not become universal merely by being drawn in the graph.

### Native checklist: both organism examples

evidence: supported. Targets: traitmech:000048.

Both examples have direct habitat/lifestyle support and current matching NCBI species labels. The papers’ studied strains bound the evidence; neither example asserts that every strain has every downstream graph property.

### Native checklist: all references, snippets and evidence roles

evidence: concern. Targets: traitmech:000048.

Active identities resolve, with arXiv checked outside Europe PMC. Two full-text quotations are exact. Comparative predictions, review-level ecology, experimental results, rejected scan provenance and expression-module context remain distinct. Edge1’s current evidence note supports a different claim.

### Native checklist: all nine nodes and eight edges

graph: concern. Targets: traitmech:000048.

Anchors and local trait identity resolve. The graph overstates complete metabolic capacity and uses incompatible external relation semantics on five edges. The late experimental edge has stronger evidence than the older comparative branches, within its stated organism context.

Zero-based ledger: edge0 is a conceptual habitat/classification bridge, not a sufficiency assay. Edge1 has a valid broad relation type but an evidence-placement gap. Edge2 makes an unsupported universal necessity claim. Edges3,4,5 and7 use pathway-process subjects with RO enables. Edge6 applies process-to-process positive regulation to a TRAIT object. Node3’s complete-capacity label/description is implicated in edge2. Nodes0–2 and4–8 retain identifiable conceptual meanings; the glycine-betaine and trehalose nodes aggregate synthesis/transport and must not be treated as one exact linked route. All node groundings and context links were accounted for.

### Native checklist: resolved question, preserved provenance and proposal scope

completeness: supported. Targets: traitmech:000048.

The resolved discussion has valid anchors and sources supporting its narrow counterexample to a categorical separation of roles. This does not demonstrate universal pathway redundancy, all-condition specificity or a general genotype-to-habitat prediction rule. Those remain limits of the interpretation; no experiment is redesigned here.

### Native checklist: scientific status and history

provenance: concern. Targets: traitmech:000048.

The record remains REVIEWED and its AI-assisted changes are explicit. The inspected target-specific history does not document the human sign-off required by the native checklist. This review does not supply it or change status.

## Findings

### universal-metabolic-self-sufficiency: Host independence is inflated into universal biosynthetic self-sufficiency

major / open / confirmed; issue key: free-living-universal-metabolic-self-sufficiency.

Node3 and edge2 require complete metabolic capacity across several nutrient classes for a free-living lifestyle. The cited lineage comparisons do not establish that universal condition. A primary study explicitly reports a free-living marine auxotroph, refuting the stronger requirement while leaving the target’s host-independence definition intact.

### external-relation-endpoint-semantics: Five edges use external predicates with incompatible endpoint meanings

major / open / confirmed; issue key: free-living-external-relation-endpoint-semantics.

Edges3,4,5 and7 use named pathway processes as the subjects of RO enables, whose executor is a material entity. Edge6 uses a disposition as the object of process-to-process positive regulation. NONMECHANISTIC scope and permissive local validation do not override those meanings.

### biogeography-evidence-placement: The biogeography edge’s evidence note supports a phase contrast

minor / open / confirmed; issue key: free-living-biogeography-evidence-placement.

Edge1 asserts environment-structured global distribution, but its attached note describes a free-living versus host-associated phase. The accessible Poole abstract supports that phase contrast. The already-cited Martiny abstract directly supports biogeographic patterning. The bounded defect is evidence placement; it is not a claim that the inaccessible Poole full text cannot discuss geography.

### reviewed-signoff-not-documented: The inspected REVIEWED provenance does not document human sign-off

minor / open / confirmed; issue key: free-living-reviewed-signoff-not-documented.

The native checklist requires human sign-off for REVIEWED. The target’s promotion and subsequent local history identify AI-assisted curation, with no explicit human acceptance in the target-specific materials found by the ignored-inclusive search. Private or remote approval may exist; the confirmed defect is the missing documentary link in these inspected inputs.

## Recommended Actions And Acceptance Checks

### bound-metabolic-claim

Separate host dependence from biosynthetic completeness and bound the retained comparative interpretation to its sources.

- The corrected conceptual claim must admit the inspected counterexample.
- Preserve source provenance and do not promote genomic predictions into experimentally established universal requirements.
- After separately authorized curation, use the guarded writer/history workflow and focused schema, strict, evidence, graph and applicable qc checks.

### align-relation-semantics

Reconcile the affected relations with the actual node meanings and external definitions.

- Check domain, range, direction and claim strength rather than selecting a similar predicate label.
- Do not retype a biological process as a material entity solely to satisfy an existing relation.
- Preserve the experimental support and context-link limitations; shared mapping changes require their own scoped audit.
- Re-run focused validation, strict validation, source checks and the native graph/product checks after separately authorized curation.

### align-edge-evidence

Attach the biogeographic support at the edge making that assertion.

- The nearest source must support distribution patterning at the stated scope.
- Retain the phase-contrast source where it actually supports the concept; no blanket bibliography deletion is warranted.

### document-status-basis

Locate and document the basis for human scientific acceptance, or retain the status question as unresolved.

- Do not invent an approver or treat an automated check as human review.
- Any later status or history change needs separate curation authorization; this observation does not promote or demote the record.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | Full-corpus diagnostic: 19 pinned context links pass, including two in this target. It is not a scientific certification of the pathway mechanisms. |
| check-validate-history | /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; metadata validate-history.json | context_only | 1276 history records checked, zero invalid links; integrity does not establish scientific correctness or human sign-off. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-free_living-validate | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/free_living-validate.log; Executed 2026-10-20T07:08:41Z through 2026-10-20T07:08:42Z; metadata free_living-validate.json | context_only | The selected record validates. |
| check-free_living-strict | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/free_living-strict.log; Executed 2026-10-20T07:08:41Z through 2026-10-20T07:08:42Z; metadata free_living-strict.json | context_only | One file scanned; zero strict errors. |
| check-free_living-snippets-network | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/free_living-snippets-network.log; Executed 2026-10-20T07:08:59Z through 2026-10-20T07:09:04Z; metadata free_living-snippets-network.json | context_only | Two snippets across two references were NOT_IN_ABSTRACT, an inconclusive result. Both were subsequently matched exactly after normalizing existing whitespace in full-text paragraphs; automated outcomes are retained. |
| record | data/traits/ecology/free_living.yaml; Entire TraitRecord: nine nodes, eight edges, two examples, two related-record links, history and resolved discussion | partial | The record defines freedom from obligatory host association, while its graph contains a stronger metabolic-necessity claim. NONMECHANISTIC scope and AI-assisted history are explicit. |
| identity | data/raw/metpo.owl; Complete captured METPO literal search; v5 free-living class and parent rows | supports | No normalized exact free-living label or synonym was found in the complete captured snapshot, including obsolete-label forms. v5 documents fallback traitmech:000048 and reservation METPO:1007647 under proposed habitat association. |
| hierarchy | data/traits/ecology/habitat_association.yaml; Parent identity and definition; v5 class rows | supports | Habitat association is broader than the free-living subtype. A facultative host-associated phase is compatible with the target’s non-obligate boundary. |
| ownership | scripts/connect_free_living_trehalose_osmotic.py; Entire targeted historical writer; per-record repository history and external-research provenance record | context_only | The writer owns the added final edge and records its bounded evidence and unresolved wider question. The earlier provider answer is explicitly documented as lacking resolvable citations and is not used as scientific evidence here. |
| bibliography | https://www.ebi.ac.uk/europepmc/webservices/rest/search; Exact DOI/PMID searches; actual per-request access times in free_living-sources/sources.json | supports | All nine PubMed-indexed active references and four historical PMIDs resolve. The arXiv DOI is absent from this adapter and was independently resolved at arXiv; that adapter miss is not a broken citation. |
| martiny | https://doi.org/10.1038/nrmicro1341; Publisher abstract and key points; Europe PMC PMID16415926 | partial | The review supports environmental and historical contributions to microbial biogeographic patterns. Accessible text supplies ecological context rather than a formal definition of host independence. |
| poole | https://doi.org/10.1038/nrmicro.2017.171; PubMed-indexed abstract; PMID29379215 | partial | The abstract supports a soil phase preceding legume symbiosis. It does not itself establish the graph’s global-distribution assertion. Full article access was not obtained; no paper-wide absence claim is made. |
| examples | https://pmc.ncbi.nlm.nih.gov/articles/PMC31192/; Caulobacter genome paper abstract and introduction; PMID11259647; comparison with the separately inspected PMID15560824 abstract | supports | The genome paper explicitly places its Caulobacter example in a nutrient-poor aquatic setting and identifies it as free-living. The second article supports environmental and facultative plant-associated life for KT2440. These are examples, not universal properties of every strain. |
| putida | https://pubmed.ncbi.nlm.nih.gov/15560824/; Abstract of the KT2440 genomic niche study | supports | The article supports the second example’s broad soil/environmental claim. Only the abstract was available for this review; its strain context is retained. |
| taxa | https://www.ncbi.nlm.nih.gov/taxonomy; Exact taxonomy records 155892, 303, 2746, 562 and KT2440 record 160488 | supports | Current retrieved NCBI records match the two species labels. Caulobacter crescentus is listed as a synonym of C. vibrioides. KT2440 remains under species 303 in this retrieved taxonomy. Context-link organism IDs also match their labels. |
| taxon-strain | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=160488; KT2440 strain record and species lineage | supports | The retrieved strain-to-species placement supports use of the current record’s species example; no speculative reclassification is imposed. |
| reversion | https://doi.org/10.1186/s12915-024-02013-w; Study abstract and introductory discussion of lifestyle transitions | partial | This lineage-focused phylogenomic study discusses metabolic losses and repeated lifestyle transitions. It does not establish a universal requirement for complete biosynthetic self-sufficiency in all free-living microbes. |
| fluviibacter | https://pmc.ncbi.nlm.nih.gov/articles/PMC10952467/; Abstract, significance and comparative metabolic discussion | partial | Comparative genomes support predicted nutritional dependence of a particular symbiont relative to its free-living relatives. That contrast does not prove the converse universal requirement asserted by edge2. |
| counterexample | https://doi.org/10.1111/j.1462-2920.2008.01758.x; Primary-study abstract, PMID19125817 | refutes | The study reports experimentally demonstrated amino-acid auxotrophy in a successful free-living marine bacterium. Host independence and complete biosynthetic independence are therefore different properties. |
| jaffe | https://arxiv.org/abs/2302.00582; Accepted-review preprint, section on physicochemical barriers, printed pages5–6; arXiv v1 identity | partial | The review discusses habitat-transition constraints and lineage-dependent adaptation. It supplies background for osmotic tolerance in particular environments, not a universal free-living mechanism. |
| paracoccus | https://doi.org/10.1371/journal.pone.0287947; Comparative-genomics secondary-metabolite/stress discussion, six type strains | partial | The article reports genomic inventories and interprets their possible ecological significance, with explicit uncertainty. This supports contextual plausibility; it is not direct functional verification of every generic graph branch. |
| experiment2021 | https://doi.org/10.1128/mBio.00390-21; Results on the named Bradyrhizobium background; exact record-snippet paragraph and specificity controls | supports | The experimental results support the bounded osmotic-role claim. Other tested stress responses remain distinguishable. The record quotation matches the full-text paragraph. |
| experiment2010 | https://doi.org/10.1128/AEM.02483-09; Abstract and results on physiological stress; exact record-snippet paragraph | supports | The independent study supports the bounded osmotic phenotype and preserves a different desiccation result. The record quotation matches the full-text paragraph; effects are not generalized to all stress conditions. |
| manual-snippets | Local downloaded primary-source text; Paragraph-wise inline-text reconstruction and existing-whitespace normalization | supports | Both record quotations match without changing their wording. This check does not independently establish the interpretation of either study. |
| historical | https://www.ebi.ac.uk/europepmc/webservices/rest/search; PMIDs41989588,42039802,41943163,42125129; source abstracts and preserved discussion snippets | context_only | The historical identifiers resolve and their quoted fragments are present in the indexed abstracts. They are preserved as rejected scan provenance rather than active evidence for the resolved question. |
| ro | http://purl.obolibrary.org/obo/ro.owl; RO:0002327 enables and RO:0002213 positively regulates, with inherited domain/range semantics | refutes | Enables takes an executing material entity, not a pathway process, as subject. Positively regulates is process-to-process; the free-living trait is a disposition rather than its process object. |
| biolink | https://w3id.org/biolink/biolink-model.yaml; Locally cached model, associated with slot and named-thing domain/range | supports | Associated with is a broad non-causal relation. Endpoint typing does not establish the asserted association. |
| graph-check | Local read-only target analysis; All node IDs, endpoint references and discussion anchors | supports | Nine distinct nodes and eight edges have resolving endpoints; all five discussion anchors resolve. Shape checks do not resolve the source or ontology concerns. |
| pathway-context | conf/pathway_context_links.yaml; This target’s two entries; pinned index and conf/pathwaymech_pin.yaml | supports | Both pathway references resolve in the exact pinned snapshot. Their basis text explicitly limits organism transfer and explains that the trehalose synthesis context does not cover transport. They are context links, not equivalence assertions. |
| model | src/traitmech/schema/traitmech.yaml; Native checklist, node types, grounding policy, predicate mappings and v8 confers reservation | partial | PATHWAY denotes a named multi-step route. Generic NONMECHANISTIC nodes and documented local predicate proposals are permitted, but source scope and external relation semantics still apply. The checklist requires human sign-off for REVIEWED. |
| structured-source | https://imodulondb.org/api/datasets/b_diazoefficiens/modulome/meta; Public catalogue, dataset metadata and searches for the record’s terms | context_only | The shared console runner was unavailable on PATH and bounded local checkout searches did not locate a runnable package. The public source API was used instead. The b_diazoefficiens/modulome dataset contains the matching gene key bll0322 for otsA; no matching iModulon name was returned. The dataset spans multiple strain labels and establishes no phenotype, causal edge or exact study replication. |
| search | Local repository at f25e2af0b38a8303b13f627a9a5c33b36af4b3d2; Ignored-and-hidden-inclusive identifier/owner searches; target-specific history and research sign-off keyword check | partial | The target and maintained owners resolve. The target-specific provenance records AI assistance but no explicit human sign-off. No claim is made about private or remote approvals. |

## Limits And Additional Notes

- Martiny and Poole full articles were not obtained; their abstracts and available publisher key points bound the corresponding assessments. The Pseudomonas example was checked at abstract level.
- Three Europe PMC full-text XML endpoints returned HTTP500; PMC HTML recovered Caulobacter, Fluviibacter and the 2010 study. The two native snippet results remain NOT_IN_ABSTRACT despite subsequent manual full-text confirmation.
- The arXiv DOI had no Europe PMC result; its own repository identity and PDF were inspected. Review and comparative-genomics evidence remain distinct from direct experimental support.
- The iModulonDB console adapter was unavailable in the bounded local search; the public source API was read instead. Gene-name hits supply context only, and no matching iModulon name was returned for the searched terms. This is not negative biological evidence.
- PathwayMech links were assessed against the declared pinned index and its hash-checked native gate, not treated as exact identity or source-organism transfer.
- External relation analysis is manual; no formal OWL reasoning run is claimed. RO cached evidence retains its actual earlier access time.
- Earlier unchanged-base full-corpus diagnostics retain all baselines, adapter skips and superseded failures. They are not focused scientific validation of this target.
- No new experiments, engineering changes, strain examples or mechanisms were designed. The review assesses representation, source fidelity and conceptual scope.
- No human sign-off is inferred from this AI review or from the existing REVIEWED value.
- The expanded native capture preserved every original input hash and added the inspected pathway pin/index.
- Only the new immutable bundle is written. Scientific records, scripts, history, proposals and generated artifacts remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T071905Z-free-living
kind: record
repository: CultureBotAI/TraitMech
title: Scientific and source review of free-living (traitmech:000048)
started_at: '2026-10-20T07:08:08Z'
finished_at: '2026-10-20T07:19:05Z'
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
summary: The ecological identity, broader parent and two canonical examples are supported
  at their documented scopes. All nine nodes, eight edges, two context links and the
  resolved discussion were assessed. Two major findings concern universal metabolic
  self-sufficiency and RO endpoint semantics. Two minor findings concern evidence
  placement and missing target-specific human sign-off in the inspected local provenance.
  Both experimental quotation occurrences match the full texts; source access and
  expression-dataset limitations remain explicit.
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
  - path: conf/pathway_context_links.yaml
    sha256: 067da370d4adacac209893e65cf369e16b79d30121bb596141b09f58e411d032
    role: context
  - path: conf/pathwaymech_index.json
    sha256: 83e698f179caa0ca058989326d58eda780ea70269990ae5fc91fd2c285cef5b6
    role: context
  - path: conf/pathwaymech_pin.yaml
    sha256: 5a8f6487d9b8e23d881d112cbe58b3c548133f9ca7c9fc80761793860204eb9c
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/ecology/free_living.yaml
    sha256: d42d23af7ac02e192ba7a8783aeb9f28335a818c35c552526361b29f2c0a8ea0
    role: target
  - path: data/traits/ecology/habitat_association.yaml
    sha256: 623d18cf295c01782024055b4dca534217f52d3ef18d46f086af27fe504bbd2a
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
  - path: history/other/free-living-trehalose-external-research/2026-08-31T203047Z-claude-code-47e2e8.yaml
    sha256: e250d11c361b6dcb5184d42a754b855ab8dc30028832a27ae914fee6c331a70f
    role: context
  - path: history/records/free_living/2026-08-31T204506Z-claude-code-ca81b1.yaml
    sha256: 0c2d8296d829bf97b806e44163c6138eac07431dbedc34e99a70bcbb191c7fe4
    role: context
  - path: mappings/predicate_grounding.tsv
    sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
    role: context
  - path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
    role: context
  - path: proposals/metpo_traitmech_v7/metpo_proposal_classes_robot.tsv
    sha256: 99e779afa894363b32966bd15415417035d246970aab02931ce896f37c910a73
    role: context
  - path: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
    role: context
  - path: scripts/audit_causal_graphs.py
    sha256: e0c26506c9de712700317284f142097e7bf69334806b8010db5d6517e905e834
    role: context
  - path: scripts/connect_free_living_trehalose_osmotic.py
    sha256: 7b39fbf6fdae76a319dd88115888ac66137c1cbc5e798d1aaaaa35692df26252
    role: context
  - path: scripts/curate_knowledge_gaps.py
    sha256: 9e0fb7e01a901d84189a28f1912a2552f28d2da8733c113589e4947359d48c73
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
- target_id: traitmech:000048
  path: data/traits/ecology/free_living.yaml
  label: free-living
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/free_living.yaml
    role: Maintained scientific record
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_free_living_trehalose_osmotic.py
    role: Historical targeted writer for the most recent experimental-evidence edge
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Fourth target in batch002, selected in lexicographic path order from
    the validated review inventory union. One whole previously uncovered TraitRecord.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000048
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000048
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
  - traitmech:000048
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
  - traitmech:000048
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: The same-base full-corpus check passed 19 context links at pinned PathwayMech
    aa305727458c44ab05614901334540e2c87a9f3a, including this target’s two links. The
    pin, index and target-specific scope restrictions were also inspected.
  evidence_ids:
  - check-check-pathway-links
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - traitmech:000048
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
  - traitmech:000048
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
  - traitmech:000048
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
  - traitmech:000048
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: free_living-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - traitmech:000048
  command: just validate data/traits/ecology/free_living.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The selected record validates.
  evidence_ids:
  - check-free_living-validate
- check_id: free_living-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000048
  command: just validate-strict data/traits/ecology/free_living.yaml --out /private/tmp/traitmech-record-sweep-002.mdt7dqwk/free_living-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero strict errors.
  evidence_ids:
  - check-free_living-strict
- check_id: free_living-snippets-network
  name: Focused source snippet verification
  status: passed
  required: true
  target_ids:
  - traitmech:000048
  command: just verify-snippets --record data/traits/ecology/free_living.yaml --out
    /private/tmp/traitmech-record-sweep-002.mdt7dqwk/free_living-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Two snippets across two references were NOT_IN_ABSTRACT, an inconclusive
    result. Both were subsequently matched exactly after normalizing existing whitespace
    in full-text paragraphs; automated outcomes are retained.
  evidence_ids:
  - check-free_living-snippets-network
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-20T07:19:05Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-20T07:19:05Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-20T07:19:05Z'
  support: context_only
  summary: 'Full-corpus diagnostic: 19 pinned context links pass, including two in
    this target. It is not a scientific certification of the pathway mechanisms.'
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; metadata validate-history.json
  accessed_at: '2026-10-20T07:19:05Z'
  support: context_only
  summary: 1276 history records checked, zero invalid links; integrity does not establish
    scientific correctness or human sign-off.
  snapshot_sha256: 1fc48f1203fbfcd27b1243e4e147afb367aebfc592b496b352201058c6ee85d2
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-20T07:19:05Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-20T07:19:05Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-20T07:19:05Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-free_living-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/free_living-validate.log
  locator: Executed 2026-10-20T07:08:41Z through 2026-10-20T07:08:42Z; metadata free_living-validate.json
  accessed_at: '2026-10-20T07:19:05Z'
  support: context_only
  summary: The selected record validates.
  snapshot_sha256: 16270f26cbb54ab0a74cc8b4c12e960b6dd140f9e4a01850f3687af8dd7fa88c
- evidence_id: check-free_living-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/free_living-strict.log
  locator: Executed 2026-10-20T07:08:41Z through 2026-10-20T07:08:42Z; metadata free_living-strict.json
  accessed_at: '2026-10-20T07:19:05Z'
  support: context_only
  summary: One file scanned; zero strict errors.
  snapshot_sha256: 26cca573a4888c1bf64555e29cd142f52609983f0302ef952dc38c17a238498d
- evidence_id: check-free_living-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/free_living-snippets-network.log
  locator: Executed 2026-10-20T07:08:59Z through 2026-10-20T07:09:04Z; metadata free_living-snippets-network.json
  accessed_at: '2026-10-20T07:19:05Z'
  support: context_only
  summary: Two snippets across two references were NOT_IN_ABSTRACT, an inconclusive
    result. Both were subsequently matched exactly after normalizing existing whitespace
    in full-text paragraphs; automated outcomes are retained.
  snapshot_sha256: fcd459d2a86716ea769f73e3d29e8979518a143a60db7071f8039cfcb8a57415
- evidence_id: record
  kind: record_content
  reference: data/traits/ecology/free_living.yaml
  locator: 'Entire TraitRecord: nine nodes, eight edges, two examples, two related-record
    links, history and resolved discussion'
  accessed_at: '2026-10-20T07:19:05Z'
  support: partial
  summary: The record defines freedom from obligatory host association, while its
    graph contains a stronger metabolic-necessity claim. NONMECHANISTIC scope and
    AI-assisted history are explicit.
  snapshot_sha256: d42d23af7ac02e192ba7a8783aeb9f28335a818c35c552526361b29f2c0a8ea0
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl
  locator: Complete captured METPO literal search; v5 free-living class and parent
    rows
  accessed_at: '2026-10-20T07:10:01Z'
  support: supports
  summary: No normalized exact free-living label or synonym was found in the complete
    captured snapshot, including obsolete-label forms. v5 documents fallback traitmech:000048
    and reservation METPO:1007647 under proposed habitat association.
  snapshot_sha256: 63e81d0814c50600e61c1063459be0ca7fa89614273ea3f112bbb084ae749c33
- evidence_id: hierarchy
  kind: record_content
  reference: data/traits/ecology/habitat_association.yaml
  locator: Parent identity and definition; v5 class rows
  accessed_at: '2026-10-20T07:19:05Z'
  support: supports
  summary: Habitat association is broader than the free-living subtype. A facultative
    host-associated phase is compatible with the target’s non-obligate boundary.
- evidence_id: ownership
  kind: record_content
  reference: scripts/connect_free_living_trehalose_osmotic.py
  locator: Entire targeted historical writer; per-record repository history and external-research
    provenance record
  accessed_at: '2026-10-20T07:19:05Z'
  support: context_only
  summary: The writer owns the added final edge and records its bounded evidence and
    unresolved wider question. The earlier provider answer is explicitly documented
    as lacking resolvable citations and is not used as scientific evidence here.
- evidence_id: bibliography
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search
  locator: Exact DOI/PMID searches; actual per-request access times in free_living-sources/sources.json
  accessed_at: '2026-10-20T07:19:05Z'
  support: supports
  summary: All nine PubMed-indexed active references and four historical PMIDs resolve.
    The arXiv DOI is absent from this adapter and was independently resolved at arXiv;
    that adapter miss is not a broken citation.
  snapshot_sha256: 8b3cb8c6653627156abcba06820088fb32d8fab39ff15e1bee7b84a27dabaa6e
- evidence_id: martiny
  kind: primary_source
  reference: https://doi.org/10.1038/nrmicro1341
  locator: Publisher abstract and key points; Europe PMC PMID16415926
  accessed_at: '2026-10-20T07:11:13Z'
  support: partial
  summary: The review supports environmental and historical contributions to microbial
    biogeographic patterns. Accessible text supplies ecological context rather than
    a formal definition of host independence.
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: poole
  kind: primary_source
  reference: https://doi.org/10.1038/nrmicro.2017.171
  locator: PubMed-indexed abstract; PMID29379215
  accessed_at: '2026-10-20T07:09:39Z'
  support: partial
  summary: The abstract supports a soil phase preceding legume symbiosis. It does
    not itself establish the graph’s global-distribution assertion. Full article access
    was not obtained; no paper-wide absence claim is made.
  snapshot_sha256: 4eafb8c598b4ac91de3526cbd97101dac6d112d0f8dc960c905fc4253fd4b90b
- evidence_id: examples
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC31192/
  locator: Caulobacter genome paper abstract and introduction; PMID11259647; comparison
    with the separately inspected PMID15560824 abstract
  accessed_at: '2026-10-20T07:09:53Z'
  support: supports
  summary: The genome paper explicitly places its Caulobacter example in a nutrient-poor
    aquatic setting and identifies it as free-living. The second article supports
    environmental and facultative plant-associated life for KT2440. These are examples,
    not universal properties of every strain.
  snapshot_sha256: 91ed6a19e044a7689a6e5ff30426efaaa3a9ff5b9f6349912787ff4c350b5c9f
- evidence_id: putida
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15560824/
  locator: Abstract of the KT2440 genomic niche study
  accessed_at: '2026-10-20T07:09:39Z'
  support: supports
  summary: The article supports the second example’s broad soil/environmental claim.
    Only the abstract was available for this review; its strain context is retained.
  snapshot_sha256: 47d26402615b43d80710eee69e673fef76d281f1a7e35ef75fa561b9d4ab5999
- evidence_id: taxa
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/taxonomy
  locator: Exact taxonomy records 155892, 303, 2746, 562 and KT2440 record 160488
  accessed_at: '2026-10-20T07:10:14Z'
  support: supports
  summary: Current retrieved NCBI records match the two species labels. Caulobacter
    crescentus is listed as a synonym of C. vibrioides. KT2440 remains under species
    303 in this retrieved taxonomy. Context-link organism IDs also match their labels.
  snapshot_sha256: 4f5f81acefb20274a5ac86d0e9bc4654a46a6081f18c21d72159d359a4567c95
- evidence_id: taxon-strain
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=160488
  locator: KT2440 strain record and species lineage
  accessed_at: '2026-10-20T07:11:13Z'
  support: supports
  summary: The retrieved strain-to-species placement supports use of the current record’s
    species example; no speculative reclassification is imposed.
  snapshot_sha256: c488474850621b344f1aa7766c97a0269bab3fb74783da9c859c19327e9e4424
- evidence_id: reversion
  kind: primary_source
  reference: https://doi.org/10.1186/s12915-024-02013-w
  locator: Study abstract and introductory discussion of lifestyle transitions
  accessed_at: '2026-10-20T07:09:41Z'
  support: partial
  summary: This lineage-focused phylogenomic study discusses metabolic losses and
    repeated lifestyle transitions. It does not establish a universal requirement
    for complete biosynthetic self-sufficiency in all free-living microbes.
  snapshot_sha256: 33becfb99965616135ad73b53f498948ee377c8c2bdf4daa138f74db73e6d2f2
- evidence_id: fluviibacter
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10952467/
  locator: Abstract, significance and comparative metabolic discussion
  accessed_at: '2026-10-20T07:09:43Z'
  support: partial
  summary: Comparative genomes support predicted nutritional dependence of a particular
    symbiont relative to its free-living relatives. That contrast does not prove the
    converse universal requirement asserted by edge2.
  snapshot_sha256: 21d61f02fb5c067fb842c116f045cd7e5e61257ab52d6054f301c5af2eeaad3e
- evidence_id: counterexample
  kind: primary_source
  reference: https://doi.org/10.1111/j.1462-2920.2008.01758.x
  locator: Primary-study abstract, PMID19125817
  accessed_at: '2026-10-20T07:16:01Z'
  support: refutes
  summary: The study reports experimentally demonstrated amino-acid auxotrophy in
    a successful free-living marine bacterium. Host independence and complete biosynthetic
    independence are therefore different properties.
  snapshot_sha256: 642226fc8f31be4c9cd3f783253f3dcc11227162a23b7eb5d06d708763a15dc1
- evidence_id: jaffe
  kind: primary_source
  reference: https://arxiv.org/abs/2302.00582
  locator: Accepted-review preprint, section on physicochemical barriers, printed
    pages5–6; arXiv v1 identity
  accessed_at: '2026-10-20T07:11:13Z'
  support: partial
  summary: The review discusses habitat-transition constraints and lineage-dependent
    adaptation. It supplies background for osmotic tolerance in particular environments,
    not a universal free-living mechanism.
  snapshot_sha256: 9f9da5add4a48ec5778ec75f569be1538f1d32c10f06cff541ccbeaa1431db46
- evidence_id: paracoccus
  kind: primary_source
  reference: https://doi.org/10.1371/journal.pone.0287947
  locator: Comparative-genomics secondary-metabolite/stress discussion, six type strains
  accessed_at: '2026-10-20T07:09:45Z'
  support: partial
  summary: The article reports genomic inventories and interprets their possible ecological
    significance, with explicit uncertainty. This supports contextual plausibility;
    it is not direct functional verification of every generic graph branch.
  snapshot_sha256: 54b07c89a29dfaf50fdbc8148f20b17de926e2ae0cf17dca2c35b67eb0e46d2f
- evidence_id: experiment2021
  kind: primary_source
  reference: https://doi.org/10.1128/mBio.00390-21
  locator: Results on the named Bradyrhizobium background; exact record-snippet paragraph
    and specificity controls
  accessed_at: '2026-10-20T07:09:45Z'
  support: supports
  summary: The experimental results support the bounded osmotic-role claim. Other
    tested stress responses remain distinguishable. The record quotation matches the
    full-text paragraph.
  snapshot_sha256: 2a275626e31ab82a33478f3075eb75747af0958a29bf9baf30e6ecd4bea4fbf5
- evidence_id: experiment2010
  kind: primary_source
  reference: https://doi.org/10.1128/AEM.02483-09
  locator: Abstract and results on physiological stress; exact record-snippet paragraph
  accessed_at: '2026-10-20T07:09:51Z'
  support: supports
  summary: The independent study supports the bounded osmotic phenotype and preserves
    a different desiccation result. The record quotation matches the full-text paragraph;
    effects are not generalized to all stress conditions.
  snapshot_sha256: 29c0ec89037a1ec68f29670b2238ef41a51021dd9a7dd87e2109a9067ffebc3d
- evidence_id: manual-snippets
  kind: validation
  reference: Local downloaded primary-source text
  locator: Paragraph-wise inline-text reconstruction and existing-whitespace normalization
  accessed_at: '2026-10-20T07:14:23Z'
  support: supports
  summary: Both record quotations match without changing their wording. This check
    does not independently establish the interpretation of either study.
  snapshot_sha256: 3791b9a831ef776a562cc3430e257f8ad7b2dd384f8605b6f8061d53ed0c7456
- evidence_id: historical
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search
  locator: PMIDs41989588,42039802,41943163,42125129; source abstracts and preserved
    discussion snippets
  accessed_at: '2026-10-20T07:19:05Z'
  support: context_only
  summary: The historical identifiers resolve and their quoted fragments are present
    in the indexed abstracts. They are preserved as rejected scan provenance rather
    than active evidence for the resolved question.
  snapshot_sha256: 8b3cb8c6653627156abcba06820088fb32d8fab39ff15e1bee7b84a27dabaa6e
- evidence_id: ro
  kind: authority
  reference: http://purl.obolibrary.org/obo/ro.owl
  locator: RO:0002327 enables and RO:0002213 positively regulates, with inherited
    domain/range semantics
  accessed_at: '2026-10-19T23:34:08Z'
  support: refutes
  summary: Enables takes an executing material entity, not a pathway process, as subject.
    Positively regulates is process-to-process; the free-living trait is a disposition
    rather than its process object.
  snapshot_sha256: 3120f8e09fcf819197ecf3b15f27d6633811b297e1f6a88aad8fd86d79b616bb
- evidence_id: biolink
  kind: authority
  reference: https://w3id.org/biolink/biolink-model.yaml
  locator: Locally cached model, associated with slot and named-thing domain/range
  accessed_at: '2026-10-20T07:19:05Z'
  support: supports
  summary: Associated with is a broad non-causal relation. Endpoint typing does not
    establish the asserted association.
  snapshot_sha256: 4955709e1cac1d26fd657f7a0c29d6c8390f42e41f9ebfab859c82b102f2bebb
- evidence_id: graph-check
  kind: validation
  reference: Local read-only target analysis
  locator: All node IDs, endpoint references and discussion anchors
  accessed_at: '2026-10-20T07:14:51Z'
  support: supports
  summary: Nine distinct nodes and eight edges have resolving endpoints; all five
    discussion anchors resolve. Shape checks do not resolve the source or ontology
    concerns.
  snapshot_sha256: c668030797969b904d9f74105d7e9a839a73f02ab9df379d04673375baa2fa8f
- evidence_id: pathway-context
  kind: record_content
  reference: conf/pathway_context_links.yaml
  locator: This target’s two entries; pinned index and conf/pathwaymech_pin.yaml
  accessed_at: '2026-10-20T07:19:05Z'
  support: supports
  summary: Both pathway references resolve in the exact pinned snapshot. Their basis
    text explicitly limits organism transfer and explains that the trehalose synthesis
    context does not cover transport. They are context links, not equivalence assertions.
- evidence_id: model
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Native checklist, node types, grounding policy, predicate mappings and
    v8 confers reservation
  accessed_at: '2026-10-20T07:19:05Z'
  support: partial
  summary: PATHWAY denotes a named multi-step route. Generic NONMECHANISTIC nodes
    and documented local predicate proposals are permitted, but source scope and external
    relation semantics still apply. The checklist requires human sign-off for REVIEWED.
- evidence_id: structured-source
  kind: database
  reference: https://imodulondb.org/api/datasets/b_diazoefficiens/modulome/meta
  locator: Public catalogue, dataset metadata and searches for the record’s terms
  accessed_at: '2026-10-20T07:12:35Z'
  support: context_only
  summary: The shared console runner was unavailable on PATH and bounded local checkout
    searches did not locate a runnable package. The public source API was used instead.
    The b_diazoefficiens/modulome dataset contains the matching gene key bll0322 for
    otsA; no matching iModulon name was returned. The dataset spans multiple strain
    labels and establishes no phenotype, causal edge or exact study replication.
  snapshot_sha256: f0d9feb25abb6d9084c8ca3460616f2bf20ca62fb42649760effb6c208ed8772
- evidence_id: search
  kind: search
  reference: Local repository at f25e2af0b38a8303b13f627a9a5c33b36af4b3d2
  locator: Ignored-and-hidden-inclusive identifier/owner searches; target-specific
    history and research sign-off keyword check
  accessed_at: '2026-10-20T07:16:11Z'
  support: partial
  summary: The target and maintained owners resolve. The target-specific provenance
    records AI assistance but no explicit human sign-off. No claim is made about private
    or remote approvals.
  snapshot_sha256: ac7c0464551d664965f009a6e360d4acf860f68dbcbc016076222a08a4585075
  search_scope: rg --no-ignore --hidden over data/traits, scripts, history, mappings,
    proposals, conf and DO_NOT_WORK.md for label, slug and traitmech:000048; additional
    ignored-inclusive history/reviews/research search followed by target-named-file
    inspection for human/sign-off language. No exclusion match was found. External
    approvals were not exhaustively searched.
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, label, polarity and kind'
  outcome: supported
  target_ids:
  - traitmech:000048
  summary: One ecological class is identified; the documented fallback remains appropriate
    to the captured ontology. Free-living does not require never associating with
    hosts.
  evidence_ids:
  - record
  - identity
  - hierarchy
  - poole
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: definition and scope'
  outcome: supported
  target_ids:
  - traitmech:000048
  summary: The host-independence boundary is coherent with the inspected ecological
    context and examples. The formal definition wording itself was not located in
    the accessible definition-source excerpt.
  evidence_ids:
  - record
  - martiny
  - poole
  - examples
  - putida
- assessment_id: hierarchy
  area: consistency
  topic: 'Native checklist: parent and cross-record semantics'
  outcome: supported
  target_ids:
  - traitmech:000048
  summary: The parent is strictly broader. Both related-record links retain their
    pinned context-only and organism limitations.
  evidence_ids:
  - record
  - hierarchy
  - pathway-context
  - check-check-pathway-links
- assessment_id: category
  area: representation
  topic: 'Native checklist: category, model and scope'
  outcome: supported
  target_ids:
  - traitmech:000048
  summary: ECOLOGY and CLASS fit the concept. NONMECHANISTIC is appropriate for the
    broad class; contextual mechanism examples do not become universal merely by being
    drawn in the graph.
  evidence_ids:
  - record
  - model
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: both organism examples'
  outcome: supported
  target_ids:
  - traitmech:000048
  summary: Both examples have direct habitat/lifestyle support and current matching
    NCBI species labels. The papers’ studied strains bound the evidence; neither example
    asserts that every strain has every downstream graph property.
  evidence_ids:
  - record
  - examples
  - putida
  - taxa
  - taxon-strain
- assessment_id: evidence
  area: evidence
  topic: 'Native checklist: all references, snippets and evidence roles'
  outcome: concern
  target_ids:
  - traitmech:000048
  summary: Active identities resolve, with arXiv checked outside Europe PMC. Two full-text
    quotations are exact. Comparative predictions, review-level ecology, experimental
    results, rejected scan provenance and expression-module context remain distinct.
    Edge1’s current evidence note supports a different claim.
  evidence_ids:
  - bibliography
  - martiny
  - poole
  - jaffe
  - paracoccus
  - manual-snippets
  - historical
  - structured-source
- assessment_id: graph
  area: graph
  topic: 'Native checklist: all nine nodes and eight edges'
  outcome: concern
  target_ids:
  - traitmech:000048
  summary: Anchors and local trait identity resolve. The graph overstates complete
    metabolic capacity and uses incompatible external relation semantics on five edges.
    The late experimental edge has stronger evidence than the older comparative branches,
    within its stated organism context.
  evidence_ids:
  - record
  - graph-check
  - ro
  - model
  - reversion
  - fluviibacter
  - counterexample
  - paracoccus
  - experiment2021
  - experiment2010
  details: 'Zero-based ledger: edge0 is a conceptual habitat/classification bridge,
    not a sufficiency assay. Edge1 has a valid broad relation type but an evidence-placement
    gap. Edge2 makes an unsupported universal necessity claim. Edges3,4,5 and7 use
    pathway-process subjects with RO enables. Edge6 applies process-to-process positive
    regulation to a TRAIT object. Node3’s complete-capacity label/description is implicated
    in edge2. Nodes0–2 and4–8 retain identifiable conceptual meanings; the glycine-betaine
    and trehalose nodes aggregate synthesis/transport and must not be treated as one
    exact linked route. All node groundings and context links were accounted for.'
- assessment_id: discussion
  area: completeness
  topic: 'Native checklist: resolved question, preserved provenance and proposal scope'
  outcome: supported
  target_ids:
  - traitmech:000048
  summary: The resolved discussion has valid anchors and sources supporting its narrow
    counterexample to a categorical separation of roles. This does not demonstrate
    universal pathway redundancy, all-condition specificity or a general genotype-to-habitat
    prediction rule. Those remain limits of the interpretation; no experiment is redesigned
    here.
  evidence_ids:
  - record
  - ownership
  - experiment2021
  - experiment2010
  - historical
  - graph-check
- assessment_id: status
  area: provenance
  topic: 'Native checklist: scientific status and history'
  outcome: concern
  target_ids:
  - traitmech:000048
  summary: The record remains REVIEWED and its AI-assisted changes are explicit. The
    inspected target-specific history does not document the human sign-off required
    by the native checklist. This review does not supply it or change status.
  evidence_ids:
  - record
  - ownership
  - model
  - search
  - check-validate-history
findings:
- finding_id: universal-metabolic-self-sufficiency
  issue_key: free-living-universal-metabolic-self-sufficiency
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Host independence is inflated into universal biosynthetic self-sufficiency
  description: Node3 and edge2 require complete metabolic capacity across several
    nutrient classes for a free-living lifestyle. The cited lineage comparisons do
    not establish that universal condition. A primary study explicitly reports a free-living
    marine auxotroph, refuting the stronger requirement while leaving the target’s
    host-independence definition intact.
  target_ids:
  - traitmech:000048
  field_paths:
  - causal_graphs[0].nodes[3]
  - causal_graphs[0].edges[2]
  evidence_ids:
  - record
  - reversion
  - fluviibacter
  - counterexample
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/free_living.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: external-relation-endpoint-semantics
  issue_key: free-living-external-relation-endpoint-semantics
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Five edges use external predicates with incompatible endpoint meanings
  description: Edges3,4,5 and7 use named pathway processes as the subjects of RO enables,
    whose executor is a material entity. Edge6 uses a disposition as the object of
    process-to-process positive regulation. NONMECHANISTIC scope and permissive local
    validation do not override those meanings.
  target_ids:
  - traitmech:000048
  field_paths:
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[4].predicate_id
  - causal_graphs[0].edges[5].predicate_id
  - causal_graphs[0].edges[6].predicate_id
  - causal_graphs[0].edges[7].predicate_id
  evidence_ids:
  - record
  - graph-check
  - ro
  - model
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/free_living.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_free_living_trehalose_osmotic.py
    role: Historical targeted writer containing the final edge; review its constants
      before separately authorized reuse
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained predicate mapping; any shared correction requires separately
      scoped corpus assessment
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: biogeography-evidence-placement
  issue_key: free-living-biogeography-evidence-placement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The biogeography edge’s evidence note supports a phase contrast
  description: Edge1 asserts environment-structured global distribution, but its attached
    note describes a free-living versus host-associated phase. The accessible Poole
    abstract supports that phase contrast. The already-cited Martiny abstract directly
    supports biogeographic patterning. The bounded defect is evidence placement; it
    is not a claim that the inaccessible Poole full text cannot discuss geography.
  target_ids:
  - traitmech:000048
  field_paths:
  - causal_graphs[0].edges[1].evidence
  evidence_ids:
  - record
  - martiny
  - poole
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/free_living.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: reviewed-signoff-not-documented
  issue_key: free-living-reviewed-signoff-not-documented
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The inspected REVIEWED provenance does not document human sign-off
  description: The native checklist requires human sign-off for REVIEWED. The target’s
    promotion and subsequent local history identify AI-assisted curation, with no
    explicit human acceptance in the target-specific materials found by the ignored-inclusive
    search. Private or remote approval may exist; the confirmed defect is the missing
    documentary link in these inspected inputs.
  target_ids:
  - traitmech:000048
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - record
  - ownership
  - model
  - search
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/free_living.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: history/records/free_living
    role: Target-specific immutable provenance; append a later event if separately
      authorized
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: bound-metabolic-claim
  description: Separate host dependence from biosynthetic completeness and bound the
    retained comparative interpretation to its sources.
  finding_ids:
  - universal-metabolic-self-sufficiency
  target_ids:
  - traitmech:000048
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/free_living.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The corrected conceptual claim must admit the inspected counterexample.
  - Preserve source provenance and do not promote genomic predictions into experimentally
    established universal requirements.
  - After separately authorized curation, use the guarded writer/history workflow
    and focused schema, strict, evidence, graph and applicable qc checks.
- action_id: align-relation-semantics
  description: Reconcile the affected relations with the actual node meanings and
    external definitions.
  finding_ids:
  - external-relation-endpoint-semantics
  target_ids:
  - traitmech:000048
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/free_living.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_free_living_trehalose_osmotic.py
    role: Historical targeted writer containing the final edge; review its constants
      before separately authorized reuse
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained predicate mapping; any shared correction requires separately
      scoped corpus assessment
  acceptance_checks:
  - Check domain, range, direction and claim strength rather than selecting a similar
    predicate label.
  - Do not retype a biological process as a material entity solely to satisfy an existing
    relation.
  - Preserve the experimental support and context-link limitations; shared mapping
    changes require their own scoped audit.
  - Re-run focused validation, strict validation, source checks and the native graph/product
    checks after separately authorized curation.
- action_id: align-edge-evidence
  description: Attach the biogeographic support at the edge making that assertion.
  finding_ids:
  - biogeography-evidence-placement
  target_ids:
  - traitmech:000048
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/free_living.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The nearest source must support distribution patterning at the stated scope.
  - Retain the phase-contrast source where it actually supports the concept; no blanket
    bibliography deletion is warranted.
- action_id: document-status-basis
  description: Locate and document the basis for human scientific acceptance, or retain
    the status question as unresolved.
  finding_ids:
  - reviewed-signoff-not-documented
  target_ids:
  - traitmech:000048
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/free_living.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: history/records/free_living
    role: Future appended provenance only
  acceptance_checks:
  - Do not invent an approver or treat an automated check as human review.
  - Any later status or history change needs separate curation authorization; this
    observation does not promote or demote the record.
limitations:
- Martiny and Poole full articles were not obtained; their abstracts and available
  publisher key points bound the corresponding assessments. The Pseudomonas example
  was checked at abstract level.
- Three Europe PMC full-text XML endpoints returned HTTP500; PMC HTML recovered Caulobacter,
  Fluviibacter and the 2010 study. The two native snippet results remain NOT_IN_ABSTRACT
  despite subsequent manual full-text confirmation.
- The arXiv DOI had no Europe PMC result; its own repository identity and PDF were
  inspected. Review and comparative-genomics evidence remain distinct from direct
  experimental support.
- The iModulonDB console adapter was unavailable in the bounded local search; the
  public source API was read instead. Gene-name hits supply context only, and no matching
  iModulon name was returned for the searched terms. This is not negative biological
  evidence.
- PathwayMech links were assessed against the declared pinned index and its hash-checked
  native gate, not treated as exact identity or source-organism transfer.
- External relation analysis is manual; no formal OWL reasoning run is claimed. RO
  cached evidence retains its actual earlier access time.
- Earlier unchanged-base full-corpus diagnostics retain all baselines, adapter skips
  and superseded failures. They are not focused scientific validation of this target.
- No new experiments, engineering changes, strain examples or mechanisms were designed.
  The review assesses representation, source fidelity and conceptual scope.
- No human sign-off is inferred from this AI review or from the existing REVIEWED
  value.
notes:
- The expanded native capture preserved every original input hash and added the inspected
  pathway pin/index.
- Only the new immutable bundle is written. Scientific records, scripts, history,
  proposals and generated artifacts remain unchanged.
tags:
- record-review
- free-living
- ecology
- needs-curation
```
