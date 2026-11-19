# Identity, source attribution and scope review of extremely halophilic

- Review: 20261021T100056Z-extremely-halophilic
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T09:48:14Z
- Finished UTC: 2026-10-21T10:00:56Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One major finding identifies two acidic-proteome evidence entries assigned to the wrong DOI: both authentic snippets belong to a separately verified halophilic-enzyme review. Two minor findings concern the canonical note’s added near-saturation requirement and the bounded missing local human-acceptance link. The active METPO identity, retained broader parent, named species/strains and all current node/relation roles are supported. All eleven nodes, eleven edges, eight publications and fourteen citation placements were assessed. Four snippets are exact at their assigned publications; two are exact but misattributed. Precise numerical-definition publication support remains explicitly unverified.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: One entire maintained TraitRecord, read before native capture. All eleven nodes, eleven edges, one canonical example, eight publications, fourteen citation placements, six snippets and fourteen history events are included. Contextual sources, ontology, parent, proposals and writers are not additional review targets; the excluded spore-germination record remains untouched.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000628 | data/traits/environment/extremely_halophilic.yaml | maintained | extremely halophilic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000628 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000628 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000628 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1000628 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000628 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000628 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000628 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | METPO:1000628 | Passed09:49:37–38Z. Structural validation does not establish publication attribution or biological source support. |
| Focused strict validation | passed | True | METPO:1000628 | Passed09:49:37–39Z with zero strict errors; current ontology roles were independently reviewed. |
| Focused abstract snippet check | passed | True | METPO:1000628 | Passed09:49:40–47Z: three VERIFIED and three NOT_IN_ABSTRACT. Actual body inspection verifies the salt-in phrase; the other two phrases are exact in a different publication, establishing a citation-attribution error rather than three equivalent abstract failures. |
| Reused native full-corpus QC | passed | True | METPO:1000628 | Actual B4 execution09:19:10–09:21:17Z passed. B5 byte comparison supports reuse for unchanged scientific/common-check inputs. Original baselines and warnings remain; this is not a fresh B5 execution or semantic certification. |
| Live UniProt instance audit | not_applicable | False | METPO:1000628 | No UniProt instance is asserted; two reviewed-label-only aggregates remain contextual. No unrelated accession/version failure imported. |
| Structured-source runner discovery | unavailable | False | METPO:1000628 | Documented hash-verified reuse of bounded discovery; official catalog fallback inspected. |
| Canonical-organism dataset applicability | not_applicable | False | METPO:1000628 | No canonical species/strain dataset in the inspected catalog; no replacement organism or module query. |

## Scientific And Domain Assessments

### Native checklist: identifier, label, polarity, synonym and term kind

identity: supported. Targets: METPO:1000628.

The exact active METPO class and retained RELATED_SYNONYM match. This is a positive environmental growth-preference class, not an organism or assay event. Removal of a synonym duplicating the preferred label loses no distinct meaning.

### Native checklist: noncircular quantitative definition and source scope

evidence: unknown. Targets: METPO:1000628.

The numerical clause matches pinned METPO, and the retained local wording is documented. PMID11790755 verifies its organism terminology but the inspected abstract does not establish the precise15–30%/12% criteria. Its unavailable body leaves publication attribution unverified, not a false-definition finding.

### Native checklist: strictly broader parent and retained release choice

identity: supported. Targets: METPO:1000628.

Halophily preference remains an upstream ancestor through halophilic. The local direct parent and introductory definition phrase were expressly retained by release disposition; direct-parent drift alone does not establish an incorrect hierarchy or warrant blind refresh.

### Native checklist: canonical species, named strains and salt-requirement note

evidence: concern. Targets: METPO:1000628.

Official identities and the cited genome paper support Halobacterium salinarum and the NRC-1/R1 twin strains. The near-saturating requirement is not directly established in that nearest complete main body. Preserve the valid model example while narrowing or directly supporting its added physiological assertion.

### Native checklist: environment category, graph scope and optional fields

representation: supported. Targets: METPO:1000628.

ENVIRONMENT/CLASS and contextual NONMECHANISTIC scope are coherent. Two protein aggregates have explicit reviewed-label-only rationale. Optional token protein instances, pathways, domain/range, priority/subset, discussion and expression datasets are not mandatory completeness targets.

### Native checklist: all eleven node identities and proposal status

grounding: supported. Targets: METPO:1000628.

Potassium identity is exact and response to osmotic stress matches its explicit response-process description. Salt-in and causal proposals retain local status. Node8 quality wording and free-text accumulation shorthand are bounded precision questions rather than automatic external-ontology failures.

### Native checklist: all eleven edge roles and directions

consistency: supported. Targets: METPO:1000628.

Current assigned Biolink/local relations fit their represented roles and no current RO relation is present. Historical removed groundings are not current findings. Source support is assessed separately from the permitted relation shape.

### Native checklist: eight publications and fourteen nearest placements

evidence: concern. Targets: METPO:1000628.

The DOI at edges3–4 identifies a different-topic publication; both snippets have an independently verified exact origin in the halophilic-enzyme review. Other placements have positive contextual support with their organism and evidence-tier bounds. The near-saturation note and numerical-definition attribution retain their distinct limitations.

### Native checklist: six snippets and exact source attribution

evidence: concern. Targets: METPO:1000628.

Four snippets are exact at their assigned publications: the organism phrase, two salinity phrases and the body salt-in phrase. Two further strings are exact in the separately identified halophilic-enzyme abstract but assigned to the therapeutic-bacteria DOI. Correct attribution is required even though their words are authentic.

### Native checklist: whole-record coverage and contextual source breadth

completeness: supported. Targets: METPO:1000628.

All eleven nodes and edges were reviewed. Existing source context supports alternative osmoadaptation routes, qualified general responses and named-organism glycosylation findings. No universal pathway, token accession, new molecular target or experimental demonstration is demanded merely by the broad graph.

### Native checklist: optional structured-source applicability

evidence: supported. Targets: METPO:1000628.

The inspected catalog lacks the canonical species and named strains. Bounded runner discovery is explicitly reused, not fresh; no alternative organism query or negative biological inference follows.

### Native checklist: history, imported authorship, acceptance, owners and checks

provenance: concern. Targets: METPO:1000628.

Thirteen AI-assisted events and one automated seed are disclosed. Upstream created_by and release retention are not local acceptance of this revision. No human-acceptance link emerged from the declared ignored-inclusive search. Native checks passed within their focused or unchanged-input reuse scope.

## Findings

### acidic-proteome-citation-attribution: Two acidic-proteome claims cite the wrong publication

major / open / confirmed; issue key: extremely-halophilic-acidic-proteome-citation-attribution.

Edges3–4 attach DOI:10.1016/j.copbio.2015.05.004 to acidic-proteome claims and two snippets. EPMC and independent Crossref identify that DOI as Engineered bacteria as therapeutic agents. Both snippets instead occur verbatim in the actual abstract of Halophiles and their enzymes: negativity put to good use, PMID26066288, DOI:10.1016/j.mib.2015.05.009. This is a confirmed source-attribution mismatch covering two placements, not merely an abstract-search miss. Preserve the positive underlying biology supported by the exact-origin abstract and the separately cited haloarchaeal review; no new pathway or therapeutic-bacteria mechanism is needed to correct the bibliography.

### canonical-growth-requirement-source: The canonical citation does not establish the added salt requirement

minor / open / confirmed; issue key: extremely-halophilic-canonical-growth-requirement-source.

The cited complete genome-comparison paper establishes Halobacterium salinarum and its twin laboratory strains NRC-1/R1, but the inspected main-body text does not establish the note’s requiring-near-saturating-NaCl assertion. That stronger physiological wording needs a directly supporting source or narrower wording. Preserve the correct species/strain identities and general extreme-halophile model context; this gap does not demonstrate that the organism’s phenotype is false.

### human-acceptance-link: Human scientific acceptance is not linked locally

minor / open / confirmed; issue key: extremely-halophilic-human-acceptance-link.

The fourteen history events comprise thirteen disclosed AI-assisted events and an automated seed. The created_by name is copied upstream authorship, and retained release dispositions do not identify a human accepting this record revision. The ignored-inclusive local search and review target-list inspection found no explicit human-acceptance link. This documentary gap does not establish that no private or remote human review occurred.

## Recommended Actions And Acceptance Checks

### repair-source-attribution

In separately authorized curation, align both acidic-proteome evidence entries with their verified quotation source.

- The reference and exact snippet at each affected placement resolve together to the actually inspected source; PMID26066288/DOI10.1016/j.mib.2015.05.009 is the verified origin of both current strings.
- Preserve the supported existing biological explanation and distinguish source identity correction from mechanism expansion; no pathogen-route investigation or experimental recommendation is required.
- Check both nearest placements and source notes, not only a top-level bibliography entry.
- After authorized edits use guarded writes, append-only history, focused strict/snippet/term/graph checks, just qc and maintained derived-product regeneration.

### bound-canonical-requirement

Retain the valid model/strain example while directly supporting or narrowing its near-saturation requirement wording.

- The cited genome paper continues to support the twin-strain identity/history for NRC-1 and R1.
- Any retained physiological requirement has an actual inspected source passage, with growth requirement distinguished from habitat, tested condition and optimum.
- Do not replace the species or strains merely because the nearest reference is genomic, and do not infer that the phenotype is false.

### link-acceptance

Locate and link existing human scientific acceptance or obtain it through the established process, preserving history and reassessing status if needed.

- Acceptance identifies the reviewed revision and scientific scope.
- Imported created_by, AI disclosures, release-retention reports, structural checks and this review are not substituted for human scientific acceptance; retain append-only history.

### clarify-definition-attribution

Keep ontology authority and unresolved numerical publication support distinct during any later bibliographic curation.

- The15–30% optimum and approximately12% boundary retain their ontology provenance; PMID11790755 is not claimed verified for those numbers solely because it uses extremely-halophilic terminology.
- Actual accessible source text is required before asserting a contradiction or changing numerical criteria.
- No new organism optimization, protocol or biological mechanism is proposed; preserve the valid broader-ancestor relation and recorded release disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep-005.klfwsp1f/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-extremely-halophilic-validate | /private/tmp/traitmech-record-sweep-005.klfwsp1f/extremely-halophilic-validate.log; Executed 2026-10-21T09:49:37Z through 2026-10-21T09:49:38Z; metadata extremely-halophilic-validate.json | context_only | Passed09:49:37–38Z. Structural validation does not establish publication attribution or biological source support. |
| check-extremely-halophilic-strict | /private/tmp/traitmech-record-sweep-005.klfwsp1f/extremely-halophilic-strict.log; Executed 2026-10-21T09:49:37Z through 2026-10-21T09:49:39Z; metadata extremely-halophilic-strict.json | context_only | Passed09:49:37–39Z with zero strict errors; current ontology roles were independently reviewed. |
| check-extremely-halophilic-snippets | /private/tmp/traitmech-record-sweep-005.klfwsp1f/extremely-halophilic-snippets.log; Executed 2026-10-21T09:49:40Z through 2026-10-21T09:49:47Z; metadata extremely-halophilic-snippets.json | context_only | Passed09:49:40–47Z: three VERIFIED and three NOT_IN_ABSTRACT. Actual body inspection verifies the salt-in phrase; the other two phrases are exact in a different publication, establishing a citation-attribution error rather than three equivalent abstract failures. |
| check-batch004-qc | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/batch004-qc.log; Executed 2026-10-21T09:19:10Z through 2026-10-21T09:21:17Z; metadata batch004-qc.json | context_only | Actual B4 execution09:19:10–09:21:17Z passed. B5 byte comparison supports reuse for unchanged scientific/common-check inputs. Original baselines and warnings remain; this is not a fresh B5 execution or semantic certification. |
| reuse | B5 common-input byte comparison and original execution receipts; 1130 trait files, history and common-check inputs versus B4; unchanged8eee scientific base | supports | Original f25 diagnostics and B3 history validation retain their execution dates, failed product attempts and adapter skips. B4 QC retains its actual execution time. Reuse on unchanged inputs does not certify newer external ontology releases. |
| reuse-independent | Independent B5 setup/reuse inspection; Original diagnostics and unchanged-input basis | supports | Independent inspection confirmed original counts, failures and limits without rerunning scientific validators or external release checks. |
| capture | Native selected-record inspection; 59 inputs captured09:48:14–16Z after whole-target read | supports | The native snapshot includes target, parent, schema, ontology, review rules, proposals, mappings, writers, release-disposition reports and research lead. Grounding review subsequently verified every captured hash. Provider content is a lead, not primary scientific proof. |
| record | data/traits/environment/extremely_halophilic.yaml; Entire identity, quantitative definition, graph, example and history | partial | The record denotes a very-high-salt growth preference and contains an archaeal salt-in contextual graph. NONMECHANISTIC scope and two reviewed-label-only protein aggregates do not themselves require token UniProt instances. |
| identity | Pinned METPO active/deprecated declarations; METPO:1000628 label/synonym; quantitative clause; ancestor chain1000628→1000620→1000629 | supports | The active exact class and related synonym match. The quantitative clause matches pinned METPO, while the local opening phrase and parent retain a documented earlier choice. The selected parent1000629 is still a strictly broader upstream ancestor. Ontology agreement establishes identity/meaning, not independent publication support for numerical limits. |
| local-authority | Native schema/checklist; v2/v7/v8 proposals; curation status rule; Salt-in process, selects-for and confers proposal roles; reviewed-label-only scope; human-acceptance gate | supports | The maintained local proposals fit the represented roles and retain their unminted status. Confers admits protein or process subjects with a trait object. The native schema permits contextual label-only aggregates and optional ungrounded predicates. REVIEWED status requires human scientific acceptance distinct from automated curation. |
| authority | Official QuickGO, ChEBI and NCBI Taxonomy responses; GO:0006970; CHEBI:29103; species2242 and strains64091/478009 | supports | Response to osmotic stress is an active biological process matching the node description. Potassium(1+) is exact. Halobacterium salinarum and the named NRC-1/R1 strains have matching current identities and species lineage. These checks do not establish salinity growth boundaries. |
| authority-receipts | Actual official identity acquisition receipts; Successful retries09:55:26.714577–09:55:27.441811Z | supports | All three official requests succeeded and preserve raw-response hashes, URLs and actual times. Initial sandbox DNS failures at09:55:04Z remain separately recorded and are not presented as biological or identifier failures. |
| authority-failures | Retained initial official identity attempts; Sandbox DNS errors09:55:04.230608–09:55:04.296997Z | context_only | The initial requests failed before source content was available. Successful retries supersede access failure, while the original attempts remain visible. |
| biolink | Pinned Biolink Model4.4.0 causes and inherited slots; Broad named-thing endpoint roles | supports | Causes permits the represented environmental condition and response-process roles. No RO predicate is asserted in the current graph. Free-text induction/accumulation shorthand is not assigned an invented external process-only restriction. |
| ledger | Independent complete node/edge, identity and owner ledger; Eleven nodes, eleven edges, two protein aggregates, zero protein instances; all59 native hashes match | supports | Every current node and edge role was assessed and no formal grounding finding was identified. Shortened osmotic-stress wording is resolved by the explicit response description. Historical removed RO/UniProt assertions are not treated as current defects. |
| node-edges | Complete independent node/edge ledger; All eleven nodes and eleven edges, zero-based | supports | Current process, quality, protein and ion roles are coherent within the native model. No new pathway step, target or assay is required to justify the contextual classification. |
| owners | Maintained node/predicate mappings, writers, proposals and release finalizer; Existing-ID skips; salt-in, potassium, response and causal mappings; retained semantic choices | supports | Mappings fit the current represented roles; no erroneous identifier recurrence was identified. The release finalizer and disposition reports explicitly retain local definition phrasing and hierarchy. The record remains the owner of the two incorrect citation placements; no unsupported mapping repair is proposed. |
| provenance | Whole history, ignored-inclusive target search and release disposition review; Search09:49:33.939956–09:49:34.035175Z;146 matches,67 review YAML files, no target-specific acceptance link | partial | Fourteen events comprise thirteen disclosed AI-assisted events and one automated seed. created_by is an upstream IAO_0000117 annotation copied by the seeder, not local human acceptance. Release-retention reports preserve semantics but do not identify a human accepting this revision. Private/remote acceptance remains unknown. |
| expression | https://imodulondb.org/api/datasets; Original catalog07:36:12.732638–07:36:12.858149Z; hash-verified canonical applicability inspection | context_only | The20-organism,28-dataset catalog has no matching Halobacterium salinarum, NRC-1 or R1 entry. No replacement Haloferax or other organism was queried. Catalog noncoverage is not negative phenotype/function evidence and does not require a token dataset or scope change. |
| runner | Structured-source runner discovery reuse; Original PATH/B5 discovery09:27:57.380287–09:27:57.542053Z; earlier external bounds08:17:15; reuse09:49:33Z | context_only | The retained bounded discovery found no runner. This target reused verified discovery/catalog files rather than executing a fresh search or network query. Original external search bounds and dates remain explicit. |
| bibliography | Complete source, quotation and acquisition ledger; Eight record publications, fourteen placements, six snippets and all eleven edge claims | partial | Five cited article bodies are local. Four snippets are exact at their assigned publications; two are exact in a different, independently identified publication. The canonical query was corrected without declaring the valid URL broken. Quantitative-definition attribution and the near-saturation requirement retain their distinct access/support limits. |
| source-receipts | Actual public XML and citation-registry acquisition receipts; Requests09:53:22.465460–09:53:34.385222Z | supports | Five XML bodies, corrected canonical metadata and independent Crossref identity were obtained with timestamps and hashes. Definition XML returned500 and is an error response, not an article. Earlier root metadata and prior salinity-browser access retain original times and hash-verified reuse. |
| source-reuse | Root metadata and prior salinity-browser receipt reuse; Metadata original09:48:51.951466–09:48:54.181656Z; salinity actual opening PDF09:29:16–17Z | context_only | Ten copied files were hash-verified. The salinity body evidence is limited to previously inspected opening pages353–355 and retains subsequent access errors; no successful local PDF hash or new whole-body read is fabricated. |
| definition-source | https://pubmed.ncbi.nlm.nih.gov/11790755/; DOI10.1128/JB.184.3.840-845.2002; actual indexed abstract opening sentence | partial | The paper exactly describes Haloferax volcanii as extremely halophilic, verifying the quotation and its organism terminology. Its inspected abstract does not establish15–30% optimal salinity or an approximately12% lower boundary. Body access failed, so those numerical attributions remain unverified rather than false; the independently matching pinned ontology is a separate authority. |
| canonical-source | https://pmc.ncbi.nlm.nih.gov/articles/PMC10264941/; PMID37379421; DOI10.1002/mbo3.1365; Abstract; Introduction/mbo31365-sec-0010/body3–6 | partial | Genome comparison directly establishes NRC-1 and R1 as the twin laboratory strains and supports their Halobacterium salinarum identity/model context. The complete main-body paragraphs do not establish a near-saturating-NaCl growth requirement. This is a bounded nearest-evidence gap for an ancillary physiological claim, not proof that the species is wrongly classified. |
| canonical-query | Corrected Europe PMC canonical-source query; PMC10264941 direct query; initial EXT_ID/SRC combination retained as failed query | supports | The corrected response identifies a valid2023 genome-comparison publication. The original zero-hit query reflects its search construction, not invalid publication identity. |
| salinity-source | https://doi.org/10.1093/femsre/fuy009; PMID29529204; complete indexed abstract, first sentence and KCl/model-organism passages | supports | Both assigned snippets are exact. The source directly supports habitats up to salt saturation, KCl accumulation in many haloarchaea and the Halobacterium salinarum model while distinguishing alternative strategies. The existing often qualification is appropriate; generic graph context does not mean every extreme halophile must use the same route. |
| salt-in-source | https://doi.org/10.1038/srep25642; PMID27231230; PMC4882750; Introduction/body0; results/discussion/body19–20,25–27 | supports | The exact Salt-in strategy phrase occurs in the introduction. Haloarcula marismortui RR12 results and review background support intracellular-ion osmoadaptation with condition-dependent responses. This supports the existing route without extending the same ion response to every species or salinity change. |
| wrong-source | https://doi.org/10.1016/j.copbio.2015.05.004; PMID26070111; actual indexed title/authors/abstract | refutes | The DOI identifies Engineered bacteria as therapeutic agents by Piñero-Lambea, Ruano-Gallego and Fernández. Its documentary scope conflicts with the acidic-proteome source represented at edges3–4. No detailed therapeutic/pathogen mechanisms were investigated; the positive identification of another exact quotation source establishes the attribution error. |
| wrong-source-registry | Publisher-deposited Crossref registration for DOI10.1016/j.copbio.2015.05.004; Exact registered title and authors | supports | An independent registry response confirms the therapeutic-bacteria publication identity. The major finding is not based solely on a search-result snippet or an abstract miss. |
| quote-origin | https://doi.org/10.1016/j.mib.2015.05.009; PMID26066288; PMC4729366; DasSarma and DasSarma, Halophiles and their enzymes: negativity put to good use; abstract sentence2 | supports | Both existing acidic-protein snippets occur verbatim in this actual indexed abstract. It provides positive support for the existing biological explanation and a concrete correct attribution for separately authorized bibliographic curation. This is supplemental source verification, not a newly introduced mechanism or an inferred search-only match. |
| quote-origin-receipt | Actual exact-quotation-origin acquisition receipt; 09:55:08.310432–09:55:09.127838Z; SHA256cd355f5328ee06a50505dd7e9184ade83945ad65e9212a7693fa65715b18080b | supports | The search hit was only a lead; a successful independent source-abstract response was downloaded and checked for both literal strings. The primary-browser challenge is retained and is not misrepresented as body access. |
| stress-source | https://doi.org/10.1186/s12934-024-02358-5; PMID38519954; PMC10960403; Abstract Results; Background/Sec1/body0–2 | supports | The source directly reports osmotic stress after salt shock in Halomonas elongata. Background/body2 expressly describes rapid potassium uptake as an emergency response in many microorganisms. This supports the current contextual claims while retaining dynamic-shock and organism scope; it is not proof of the full extreme-halophile threshold definition. |
| adaptation-source | https://doi.org/10.3390/microorganisms12081738; PMID39203580; PMC11357113; Osmotic Adaptation/sec2dot1/body4–5,9,11–12 | supports | The review directly supports sodium exclusion with antiporters and the link between acidic proteomes and solubility in high salt. It provides separate positive support for the wrongly cited branches. Retain usually/typically language and alternatives; the exact-origin abstract further supports existing residue-level wording without requiring an all-organism mechanism claim. |
| glycosylation-source | https://doi.org/10.3390/v15071469; PMID37515157; PMC10384203; Introduction/sec1/body1; Discussion/sec4/body34 | supports | The introduction supports haloarchaeal glycosylation/stability context. The discussion includes a second low-salt pathway in Haloferax volcanii as background and stability/adaptability findings in the paper’s own Halorubrum lacusprofundi study. Those named-organism limits support the existing contextual edges without assigning the same two pathways to every haloarchaeon. No viral engineering or host-range mechanism is reconstructed. |

## Limits And Additional Notes

- The definition’s numerical clause agrees with pinned METPO, but PMID11790755 was available only as an indexed abstract. Its exact organism terminology is verified;15–30% and approximately12% publication attribution remain unverified, not demonstrated false.
- The canonical paper directly supports species/strain identity and twin-strain history. Its complete main body does not establish the near-saturating requirement. This bounded source gap is not a negative growth result or false-classification finding.
- Five cited full texts are local; relevant existing claims were inspected, without an exhaustive methods, supplements or all-cited-references audit. The salinity review has fresh abstract support and retained prior opening-PDF inspection only.
- The therapeutic-bacteria source was assessed only for documentary metadata/abstract scope. Both misattributed strings were verified in the actual different-source abstract; no detailed therapeutic or pathogen mechanism was investigated.
- Source contexts include a specific Haloarcula strain, a Halomonas shock study, general haloarchaeal reviews and named-organism glycosylation background. These do not establish every extreme halophile using an identical pathway. The graph’s generic scope and existing often qualifier are preserved.
- No formal grounding defect was found. Short response labels are interpreted using their descriptions; maintained proposal identifiers remain provisional, and historical removed accessions/relations are not current assertions.
- Common checks and B4 QC retain their original execution times, failed attempts, adapter skips, baselines and warnings and are reused only on documented unchanged inputs. No new full-corpus run or newer-ontology certification is implied.
- Initial official authority DNS failures are retained beside successful retries. Actual timestamps and raw-response hashes remain distinguishable from later ledger/assessment times.
- There are no protein instances to audit. Catalog noncoverage and reused bounded runner discovery do not imply absent phenotype or function, and no alternative organism was substituted.
- Human acceptance beyond the ignored-inclusive local search remains unknown. Imported upstream authorship and this review do not confer local human scientific sign-off.
- No record, mapping, history or generated product was edited. No paid provider call, new pathway, molecular target, protocol or experiment was proposed.
- All node, edge and extracted body-paragraph indices are zero-based.
- Native capture retained59 inputs09:48:14–16Z; independent grounding inspection confirmed every hash. Fourteen history events comprise thirteen AI-assisted events plus an automated seed.
- One major and two minor findings. Initial abstract misses are superseded only by actual body text or independently verified exact quotation origin, with original access receipts retained.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T100056Z-extremely-halophilic
kind: record
repository: CultureBotAI/TraitMech
title: Identity, source attribution and scope review of extremely halophilic
started_at: '2026-10-21T09:48:14Z'
finished_at: '2026-10-21T10:00:56Z'
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
summary: 'One major finding identifies two acidic-proteome evidence entries assigned
  to the wrong DOI: both authentic snippets belong to a separately verified halophilic-enzyme
  review. Two minor findings concern the canonical note’s added near-saturation requirement
  and the bounded missing local human-acceptance link. The active METPO identity,
  retained broader parent, named species/strains and all current node/relation roles
  are supported. All eleven nodes, eleven edges, eight publications and fourteen citation
  placements were assessed. Four snippets are exact at their assigned publications;
  two are exact but misattributed. Precise numerical-definition publication support
  remains explicitly unverified.'
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
  - path: data/traits/environment/extremely_halophilic.yaml
    sha256: 15bf8267ffc4b393d3db1a13fa0738240dc94f5f017cce8322783f297f35d0f0
    role: target
  - path: data/traits/environment/halophily_preference.yaml
    sha256: d9d43dfaca09069195f27bdf5ceee8aa3465909f862e4ecff07dd22252b2c5dc
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
  - path: research/traits/environment/extremely_halophilic-deep-research-falcon.md
    sha256: 945bd08b3b501de2b1b25e735ed16ed6f0dcab38b2e72c9b143a8b8ed648e709
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
- target_id: METPO:1000628
  path: data/traits/environment/extremely_halophilic.yaml
  label: extremely halophilic
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/extremely_halophilic.yaml
    role: Maintained TraitRecord; scientific changes require guarded curation
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Maintained seeder for ontology-backed identity and hierarchy
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: One entire maintained TraitRecord, read before native capture. All eleven
    nodes, eleven edges, one canonical example, eight publications, fourteen citation
    placements, six snippets and fourteen history events are included. Contextual
    sources, ontology, parent, proposals and writers are not additional review targets;
    the excluded spore-germination record remains untouched.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000628
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000628
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000628
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000628
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000628
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000628
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000628
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000628
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: extremely-halophilic-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - METPO:1000628
  command: just validate data/traits/environment/extremely_halophilic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed09:49:37–38Z. Structural validation does not establish publication
    attribution or biological source support.
  evidence_ids:
  - check-extremely-halophilic-validate
- check_id: extremely-halophilic-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000628
  command: just validate-strict data/traits/environment/extremely_halophilic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed09:49:37–39Z with zero strict errors; current ontology roles were
    independently reviewed.
  evidence_ids:
  - check-extremely-halophilic-strict
- check_id: extremely-halophilic-snippets
  name: Focused abstract snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000628
  command: just verify-snippets --record data/traits/environment/extremely_halophilic.yaml
    --out /private/tmp/traitmech-record-sweep-005.klfwsp1f/extremely-halophilic-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed09:49:40–47Z: three VERIFIED and three NOT_IN_ABSTRACT. Actual body
    inspection verifies the salt-in phrase; the other two phrases are exact in a different
    publication, establishing a citation-attribution error rather than three equivalent
    abstract failures.'
  evidence_ids:
  - check-extremely-halophilic-snippets
- check_id: batch004-qc
  name: Reused native full-corpus QC
  status: passed
  required: true
  target_ids:
  - METPO:1000628
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual B4 execution09:19:10–09:21:17Z passed. B5 byte comparison supports
    reuse for unchanged scientific/common-check inputs. Original baselines and warnings
    remain; this is not a fresh B5 execution or semantic certification.
  evidence_ids:
  - check-batch004-qc
- check_id: live-uniprot
  name: Live UniProt instance audit
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000628
  summary: No UniProt instance is asserted; two reviewed-label-only aggregates remain
    contextual. No unrelated accession/version failure imported.
  evidence_ids:
  - record
  - ledger
- check_id: structured-source-runner
  name: Structured-source runner discovery
  status: unavailable
  required: false
  target_ids:
  - METPO:1000628
  summary: Documented hash-verified reuse of bounded discovery; official catalog fallback
    inspected.
  evidence_ids:
  - runner
- check_id: expression-context
  name: Canonical-organism dataset applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000628
  summary: No canonical species/strain dataset in the inspected catalog; no replacement
    organism or module query.
  evidence_ids:
  - expression
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T10:00:56Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T10:00:56Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T10:00:56Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-005.klfwsp1f/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T10:00:56Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T10:00:56Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T10:00:56Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T10:00:56Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-extremely-halophilic-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-005.klfwsp1f/extremely-halophilic-validate.log
  locator: Executed 2026-10-21T09:49:37Z through 2026-10-21T09:49:38Z; metadata extremely-halophilic-validate.json
  accessed_at: '2026-10-21T10:00:56Z'
  support: context_only
  summary: Passed09:49:37–38Z. Structural validation does not establish publication
    attribution or biological source support.
  snapshot_sha256: 442f2cd507bf1119be4163cc1ff6a236aa389f1cf6fb53b377bced2092573385
- evidence_id: check-extremely-halophilic-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-005.klfwsp1f/extremely-halophilic-strict.log
  locator: Executed 2026-10-21T09:49:37Z through 2026-10-21T09:49:39Z; metadata extremely-halophilic-strict.json
  accessed_at: '2026-10-21T10:00:56Z'
  support: context_only
  summary: Passed09:49:37–39Z with zero strict errors; current ontology roles were
    independently reviewed.
  snapshot_sha256: e271c103d4c5d06cc5c38a2a5b9ecacde1f2c7180d504326b19ec63618a6a586
- evidence_id: check-extremely-halophilic-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-005.klfwsp1f/extremely-halophilic-snippets.log
  locator: Executed 2026-10-21T09:49:40Z through 2026-10-21T09:49:47Z; metadata extremely-halophilic-snippets.json
  accessed_at: '2026-10-21T10:00:56Z'
  support: context_only
  summary: 'Passed09:49:40–47Z: three VERIFIED and three NOT_IN_ABSTRACT. Actual body
    inspection verifies the salt-in phrase; the other two phrases are exact in a different
    publication, establishing a citation-attribution error rather than three equivalent
    abstract failures.'
  snapshot_sha256: c410ae18895073bfc5f07acb6faf18395c56845b057c259626cdafa82d6b0837
- evidence_id: check-batch004-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/batch004-qc.log
  locator: Executed 2026-10-21T09:19:10Z through 2026-10-21T09:21:17Z; metadata batch004-qc.json
  accessed_at: '2026-10-21T10:00:56Z'
  support: context_only
  summary: Actual B4 execution09:19:10–09:21:17Z passed. B5 byte comparison supports
    reuse for unchanged scientific/common-check inputs. Original baselines and warnings
    remain; this is not a fresh B5 execution or semantic certification.
  snapshot_sha256: 41a3fbd2beadf60e039992274e868de70b6ade8cf4b5d6028d6df932e0cfb2e5
- evidence_id: reuse
  kind: validation
  reference: B5 common-input byte comparison and original execution receipts
  locator: 1130 trait files, history and common-check inputs versus B4; unchanged8eee
    scientific base
  accessed_at: '2026-10-21T10:00:56Z'
  support: supports
  summary: Original f25 diagnostics and B3 history validation retain their execution
    dates, failed product attempts and adapter skips. B4 QC retains its actual execution
    time. Reuse on unchanged inputs does not certify newer external ontology releases.
  snapshot_sha256: ce111d70655cdee3528b3c85ca4a71468c47d96e84ff4b28c0932389aee61313
- evidence_id: reuse-independent
  kind: validation
  reference: Independent B5 setup/reuse inspection
  locator: Original diagnostics and unchanged-input basis
  accessed_at: '2026-10-21T09:25:47.749251Z'
  support: supports
  summary: Independent inspection confirmed original counts, failures and limits without
    rerunning scientific validators or external release checks.
  snapshot_sha256: 4279ad9f488f187dd2f118a9b6274a60e5f79019225d24b33ce8b25f4ea2ca9f
- evidence_id: capture
  kind: validation
  reference: Native selected-record inspection
  locator: 59 inputs captured09:48:14–16Z after whole-target read
  accessed_at: '2026-10-21T09:48:16Z'
  support: supports
  summary: The native snapshot includes target, parent, schema, ontology, review rules,
    proposals, mappings, writers, release-disposition reports and research lead. Grounding
    review subsequently verified every captured hash. Provider content is a lead,
    not primary scientific proof.
  snapshot_sha256: 6d4b3543e8804348ed2ed11207c625656c84ecc6f5f82d6c184bd21a5bc1f3f0
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/extremely_halophilic.yaml
  locator: Entire identity, quantitative definition, graph, example and history
  accessed_at: '2026-10-21T09:48:14Z'
  support: partial
  summary: The record denotes a very-high-salt growth preference and contains an archaeal
    salt-in contextual graph. NONMECHANISTIC scope and two reviewed-label-only protein
    aggregates do not themselves require token UniProt instances.
  snapshot_sha256: 15bf8267ffc4b393d3db1a13fa0738240dc94f5f017cce8322783f297f35d0f0
- evidence_id: identity
  kind: authority
  reference: Pinned METPO active/deprecated declarations
  locator: METPO:1000628 label/synonym; quantitative clause; ancestor chain1000628→1000620→1000629
  accessed_at: '2026-10-21T09:57:32.712724Z'
  support: supports
  summary: The active exact class and related synonym match. The quantitative clause
    matches pinned METPO, while the local opening phrase and parent retain a documented
    earlier choice. The selected parent1000629 is still a strictly broader upstream
    ancestor. Ontology agreement establishes identity/meaning, not independent publication
    support for numerical limits.
  snapshot_sha256: 7061dc1847b17fc5d9db856a791c570b881d9e87c0d293eeead1e8d010786fcb
- evidence_id: local-authority
  kind: authority
  reference: Native schema/checklist; v2/v7/v8 proposals; curation status rule
  locator: Salt-in process, selects-for and confers proposal roles; reviewed-label-only
    scope; human-acceptance gate
  accessed_at: '2026-10-21T09:57:32.861008Z'
  support: supports
  summary: The maintained local proposals fit the represented roles and retain their
    unminted status. Confers admits protein or process subjects with a trait object.
    The native schema permits contextual label-only aggregates and optional ungrounded
    predicates. REVIEWED status requires human scientific acceptance distinct from
    automated curation.
  snapshot_sha256: 33411dd8e3e2e50350cec1898b5298a0b43e0a345f769506abf6398810b2f84d
- evidence_id: authority
  kind: database
  reference: Official QuickGO, ChEBI and NCBI Taxonomy responses
  locator: GO:0006970; CHEBI:29103; species2242 and strains64091/478009
  accessed_at: '2026-10-21T09:57:32.715014Z'
  support: supports
  summary: Response to osmotic stress is an active biological process matching the
    node description. Potassium(1+) is exact. Halobacterium salinarum and the named
    NRC-1/R1 strains have matching current identities and species lineage. These checks
    do not establish salinity growth boundaries.
  snapshot_sha256: 64892484fccb9b8db0c441ee65e05b4a738e798814396500b2b3f77197a929f5
- evidence_id: authority-receipts
  kind: database
  reference: Actual official identity acquisition receipts
  locator: Successful retries09:55:26.714577–09:55:27.441811Z
  accessed_at: '2026-10-21T09:55:27.441811Z'
  support: supports
  summary: All three official requests succeeded and preserve raw-response hashes,
    URLs and actual times. Initial sandbox DNS failures at09:55:04Z remain separately
    recorded and are not presented as biological or identifier failures.
  snapshot_sha256: 2b0333f5d6300bc7c70be8398947b6a80f10304d07779c368b88ce64e1079b33
- evidence_id: authority-failures
  kind: database
  reference: Retained initial official identity attempts
  locator: Sandbox DNS errors09:55:04.230608–09:55:04.296997Z
  accessed_at: '2026-10-21T09:55:04.296997Z'
  support: context_only
  summary: The initial requests failed before source content was available. Successful
    retries supersede access failure, while the original attempts remain visible.
  snapshot_sha256: de4958b948ee26d4c73ed20acf50a3801ec72831cf8dbf24740288ea6bb0123b
- evidence_id: biolink
  kind: authority
  reference: Pinned Biolink Model4.4.0 causes and inherited slots
  locator: Broad named-thing endpoint roles
  accessed_at: '2026-10-21T09:57:32.975784Z'
  support: supports
  summary: Causes permits the represented environmental condition and response-process
    roles. No RO predicate is asserted in the current graph. Free-text induction/accumulation
    shorthand is not assigned an invented external process-only restriction.
  snapshot_sha256: 206fad763a77a514ab85f84837cac76813d1ba87247bea7ddd58bad4c36b65dd
- evidence_id: ledger
  kind: validation
  reference: Independent complete node/edge, identity and owner ledger
  locator: Eleven nodes, eleven edges, two protein aggregates, zero protein instances;
    all59 native hashes match
  accessed_at: '2026-10-21T09:57:32.978641Z'
  support: supports
  summary: Every current node and edge role was assessed and no formal grounding finding
    was identified. Shortened osmotic-stress wording is resolved by the explicit response
    description. Historical removed RO/UniProt assertions are not treated as current
    defects.
  snapshot_sha256: ed623bbb3ba1b22be04e5e79ad7e70c43df4ff3785210813d93ce7d31316adbf
- evidence_id: node-edges
  kind: validation
  reference: Complete independent node/edge ledger
  locator: All eleven nodes and eleven edges, zero-based
  accessed_at: '2026-10-21T09:57:32.976378Z'
  support: supports
  summary: Current process, quality, protein and ion roles are coherent within the
    native model. No new pathway step, target or assay is required to justify the
    contextual classification.
  snapshot_sha256: afde2644277d0afd47f232928051f8ab0b4411a4bc3ee07e62449effea230ec1
- evidence_id: owners
  kind: search
  reference: Maintained node/predicate mappings, writers, proposals and release finalizer
  locator: Existing-ID skips; salt-in, potassium, response and causal mappings; retained
    semantic choices
  accessed_at: '2026-10-21T09:57:32.978265Z'
  support: supports
  summary: Mappings fit the current represented roles; no erroneous identifier recurrence
    was identified. The release finalizer and disposition reports explicitly retain
    local definition phrasing and hierarchy. The record remains the owner of the two
    incorrect citation placements; no unsupported mapping repair is proposed.
  snapshot_sha256: 20006ace118e11ae0b18ff04541e934f42ea49676dd59b5041f7971f1ba5cae1
  search_scope: Bounded ignored-inclusive mappings/scripts/proposals owner search,
    plus exact mapping lookups; static inspection only, no writer execution or global
    absence claim.
- evidence_id: provenance
  kind: search
  reference: Whole history, ignored-inclusive target search and release disposition
    review
  locator: Search09:49:33.939956–09:49:34.035175Z;146 matches,67 review YAML files,
    no target-specific acceptance link
  accessed_at: '2026-10-21T09:50:24.144034Z'
  support: partial
  summary: Fourteen events comprise thirteen disclosed AI-assisted events and one
    automated seed. created_by is an upstream IAO_0000117 annotation copied by the
    seeder, not local human acceptance. Release-retention reports preserve semantics
    but do not identify a human accepting this revision. Private/remote acceptance
    remains unknown.
  snapshot_sha256: 4749b19a3710a3f0f01ea13518227548218996188f81b132b0d76a7981fd9d0c
  search_scope: Bounded rg --no-ignore --hidden target ID/label/slug search within
    history, mappings, scripts, reviews/structured, and reports; matching history
    and exact review target lists plus retained release owners were inspected. Git
    metadata and virtual environments are outside these roots. No repository-wide,
    private or remote absence claim.
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Original catalog07:36:12.732638–07:36:12.858149Z; hash-verified canonical
    applicability inspection
  accessed_at: '2026-10-21T09:50:24.145605Z'
  support: context_only
  summary: The20-organism,28-dataset catalog has no matching Halobacterium salinarum,
    NRC-1 or R1 entry. No replacement Haloferax or other organism was queried. Catalog
    noncoverage is not negative phenotype/function evidence and does not require a
    token dataset or scope change.
  snapshot_sha256: b9da01c15c980d66cceda003cbb3f0f9a925d7918a86ea185cc0e331850e3b90
- evidence_id: runner
  kind: search
  reference: Structured-source runner discovery reuse
  locator: Original PATH/B5 discovery09:27:57.380287–09:27:57.542053Z; earlier external
    bounds08:17:15; reuse09:49:33Z
  accessed_at: '2026-10-21T09:49:33.939797Z'
  support: context_only
  summary: The retained bounded discovery found no runner. This target reused verified
    discovery/catalog files rather than executing a fresh search or network query.
    Original external search bounds and dates remain explicit.
  snapshot_sha256: 2a439a7838619dba6004a42d3cef60bd687e788c95987e5a3d62dfffb051d95d
  search_scope: Retained B5 search includes ignored, hidden and virtual-environment
    contents, excluding Git internals; external roots retain original bounded discovery.
    No whole-filesystem absence claim.
- evidence_id: bibliography
  kind: database
  reference: Complete source, quotation and acquisition ledger
  locator: Eight record publications, fourteen placements, six snippets and all eleven
    edge claims
  accessed_at: '2026-10-21T09:56:40.721180Z'
  support: partial
  summary: Five cited article bodies are local. Four snippets are exact at their assigned
    publications; two are exact in a different, independently identified publication.
    The canonical query was corrected without declaring the valid URL broken. Quantitative-definition
    attribution and the near-saturation requirement retain their distinct access/support
    limits.
  snapshot_sha256: 0c5cd556801beb10a1d61c01a6b85403cebf3c4f094698dc6c1af3d7188f8a5d
- evidence_id: source-receipts
  kind: primary_source
  reference: Actual public XML and citation-registry acquisition receipts
  locator: Requests09:53:22.465460–09:53:34.385222Z
  accessed_at: '2026-10-21T09:53:34.385222Z'
  support: supports
  summary: Five XML bodies, corrected canonical metadata and independent Crossref
    identity were obtained with timestamps and hashes. Definition XML returned500
    and is an error response, not an article. Earlier root metadata and prior salinity-browser
    access retain original times and hash-verified reuse.
  snapshot_sha256: c3be3ede9e487e3c6a71fcac119c4652a8f70e162ef07240b3549f1861ce2bce
- evidence_id: source-reuse
  kind: primary_source
  reference: Root metadata and prior salinity-browser receipt reuse
  locator: Metadata original09:48:51.951466–09:48:54.181656Z; salinity actual opening
    PDF09:29:16–17Z
  accessed_at: '2026-10-21T10:00:56Z'
  support: context_only
  summary: Ten copied files were hash-verified. The salinity body evidence is limited
    to previously inspected opening pages353–355 and retains subsequent access errors;
    no successful local PDF hash or new whole-body read is fabricated.
  snapshot_sha256: dd9bfe00b1443c7be66ab3cb2ca29851ebaa3a7cd8db63aa0e848894adb122bf
- evidence_id: definition-source
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/11790755/
  locator: DOI10.1128/JB.184.3.840-845.2002; actual indexed abstract opening sentence
  accessed_at: '2026-10-21T09:48:52.589777Z'
  support: partial
  summary: The paper exactly describes Haloferax volcanii as extremely halophilic,
    verifying the quotation and its organism terminology. Its inspected abstract does
    not establish15–30% optimal salinity or an approximately12% lower boundary. Body
    access failed, so those numerical attributions remain unverified rather than false;
    the independently matching pinned ontology is a separate authority.
  snapshot_sha256: e57a6f6a45e400bd7e8e846e169f78e612b2cba7f94db7911caf7b33f84f4a97
- evidence_id: canonical-source
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10264941/
  locator: PMID37379421; DOI10.1002/mbo3.1365; Abstract; Introduction/mbo31365-sec-0010/body3–6
  accessed_at: '2026-10-21T09:53:34.385222Z'
  support: partial
  summary: Genome comparison directly establishes NRC-1 and R1 as the twin laboratory
    strains and supports their Halobacterium salinarum identity/model context. The
    complete main-body paragraphs do not establish a near-saturating-NaCl growth requirement.
    This is a bounded nearest-evidence gap for an ancillary physiological claim, not
    proof that the species is wrongly classified.
  snapshot_sha256: 56c79fff2383c60e85cbe224b2ae4371d7011cba7dcc82f85fc9d33dd22a467b
- evidence_id: canonical-query
  kind: database
  reference: Corrected Europe PMC canonical-source query
  locator: PMC10264941 direct query; initial EXT_ID/SRC combination retained as failed
    query
  accessed_at: '2026-10-21T09:53:27.577837Z'
  support: supports
  summary: The corrected response identifies a valid2023 genome-comparison publication.
    The original zero-hit query reflects its search construction, not invalid publication
    identity.
  snapshot_sha256: 9b437095d7d8c6ab3cff843b43f71e21fbd728f67529dca4cd787a6f579d50d0
- evidence_id: salinity-source
  kind: primary_source
  reference: https://doi.org/10.1093/femsre/fuy009
  locator: PMID29529204; complete indexed abstract, first sentence and KCl/model-organism
    passages
  accessed_at: '2026-10-21T09:48:53.101390Z'
  support: supports
  summary: Both assigned snippets are exact. The source directly supports habitats
    up to salt saturation, KCl accumulation in many haloarchaea and the Halobacterium
    salinarum model while distinguishing alternative strategies. The existing often
    qualification is appropriate; generic graph context does not mean every extreme
    halophile must use the same route.
  snapshot_sha256: bc6a10ee6244e1ba4efb4ccb9abd95a51aa3d9482ff4c9ee3d1eb79a140e5064
- evidence_id: salt-in-source
  kind: primary_source
  reference: https://doi.org/10.1038/srep25642
  locator: PMID27231230; PMC4882750; Introduction/body0; results/discussion/body19–20,25–27
  accessed_at: '2026-10-21T09:53:23.571064Z'
  support: supports
  summary: The exact Salt-in strategy phrase occurs in the introduction. Haloarcula
    marismortui RR12 results and review background support intracellular-ion osmoadaptation
    with condition-dependent responses. This supports the existing route without extending
    the same ion response to every species or salinity change.
  snapshot_sha256: 02f91e6efd59c81b6498f6321e25d17c5668a6b796f8beecfc21b586c0befa47
- evidence_id: wrong-source
  kind: primary_source
  reference: https://doi.org/10.1016/j.copbio.2015.05.004
  locator: PMID26070111; actual indexed title/authors/abstract
  accessed_at: '2026-10-21T09:48:53.596251Z'
  support: refutes
  summary: The DOI identifies Engineered bacteria as therapeutic agents by Piñero-Lambea,
    Ruano-Gallego and Fernández. Its documentary scope conflicts with the acidic-proteome
    source represented at edges3–4. No detailed therapeutic/pathogen mechanisms were
    investigated; the positive identification of another exact quotation source establishes
    the attribution error.
  snapshot_sha256: 11784a177ba242c4e0b374ae7eacf54732569492178b4b3ebb3b0ee7a16fe6c2
- evidence_id: wrong-source-registry
  kind: database
  reference: Publisher-deposited Crossref registration for DOI10.1016/j.copbio.2015.05.004
  locator: Exact registered title and authors
  accessed_at: '2026-10-21T09:53:26.895318Z'
  support: supports
  summary: An independent registry response confirms the therapeutic-bacteria publication
    identity. The major finding is not based solely on a search-result snippet or
    an abstract miss.
  snapshot_sha256: e9120d4e084df647b09dbe2b3e4163fa268d7659e121015fb210d7c1fe73a130
- evidence_id: quote-origin
  kind: primary_source
  reference: https://doi.org/10.1016/j.mib.2015.05.009
  locator: 'PMID26066288; PMC4729366; DasSarma and DasSarma, Halophiles and their
    enzymes: negativity put to good use; abstract sentence2'
  accessed_at: '2026-10-21T09:55:09.127838Z'
  support: supports
  summary: Both existing acidic-protein snippets occur verbatim in this actual indexed
    abstract. It provides positive support for the existing biological explanation
    and a concrete correct attribution for separately authorized bibliographic curation.
    This is supplemental source verification, not a newly introduced mechanism or
    an inferred search-only match.
  snapshot_sha256: cd355f5328ee06a50505dd7e9184ade83945ad65e9212a7693fa65715b18080b
- evidence_id: quote-origin-receipt
  kind: database
  reference: Actual exact-quotation-origin acquisition receipt
  locator: 09:55:08.310432–09:55:09.127838Z; SHA256cd355f5328ee06a50505dd7e9184ade83945ad65e9212a7693fa65715b18080b
  accessed_at: '2026-10-21T09:55:09.127838Z'
  support: supports
  summary: The search hit was only a lead; a successful independent source-abstract
    response was downloaded and checked for both literal strings. The primary-browser
    challenge is retained and is not misrepresented as body access.
  snapshot_sha256: 89a0c25bee370a453144a83d5407e1dc751cab93ef764fdbd69310b36eea5604
- evidence_id: stress-source
  kind: primary_source
  reference: https://doi.org/10.1186/s12934-024-02358-5
  locator: PMID38519954; PMC10960403; Abstract Results; Background/Sec1/body0–2
  accessed_at: '2026-10-21T09:53:26.615260Z'
  support: supports
  summary: The source directly reports osmotic stress after salt shock in Halomonas
    elongata. Background/body2 expressly describes rapid potassium uptake as an emergency
    response in many microorganisms. This supports the current contextual claims while
    retaining dynamic-shock and organism scope; it is not proof of the full extreme-halophile
    threshold definition.
  snapshot_sha256: 36a0044a22088353f40c19bd23a6c602accba71676cf26127b6988a84efebb24
- evidence_id: adaptation-source
  kind: primary_source
  reference: https://doi.org/10.3390/microorganisms12081738
  locator: PMID39203580; PMC11357113; Osmotic Adaptation/sec2dot1/body4–5,9,11–12
  accessed_at: '2026-10-21T09:53:24.754143Z'
  support: supports
  summary: The review directly supports sodium exclusion with antiporters and the
    link between acidic proteomes and solubility in high salt. It provides separate
    positive support for the wrongly cited branches. Retain usually/typically language
    and alternatives; the exact-origin abstract further supports existing residue-level
    wording without requiring an all-organism mechanism claim.
  snapshot_sha256: 3de972ab3172b1b54a5b13f905abe236c42cdba1c22f6ec0ebd5dc7a5897d06c
- evidence_id: glycosylation-source
  kind: primary_source
  reference: https://doi.org/10.3390/v15071469
  locator: PMID37515157; PMC10384203; Introduction/sec1/body1; Discussion/sec4/body34
  accessed_at: '2026-10-21T09:53:26.092328Z'
  support: supports
  summary: The introduction supports haloarchaeal glycosylation/stability context.
    The discussion includes a second low-salt pathway in Haloferax volcanii as background
    and stability/adaptability findings in the paper’s own Halorubrum lacusprofundi
    study. Those named-organism limits support the existing contextual edges without
    assigning the same two pathways to every haloarchaeon. No viral engineering or
    host-range mechanism is reconstructed.
  snapshot_sha256: 2c7ed6860fe2dfc67fe6be4bb9937cccae7fd52cf3d5cc8d99c8f20f8794eafa
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, label, polarity, synonym and term kind'
  outcome: supported
  target_ids:
  - METPO:1000628
  summary: The exact active METPO class and retained RELATED_SYNONYM match. This is
    a positive environmental growth-preference class, not an organism or assay event.
    Removal of a synonym duplicating the preferred label loses no distinct meaning.
  evidence_ids:
  - identity
  - record
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: noncircular quantitative definition and source scope'
  outcome: unknown
  target_ids:
  - METPO:1000628
  summary: The numerical clause matches pinned METPO, and the retained local wording
    is documented. PMID11790755 verifies its organism terminology but the inspected
    abstract does not establish the precise15–30%/12% criteria. Its unavailable body
    leaves publication attribution unverified, not a false-definition finding.
  evidence_ids:
  - identity
  - definition-source
  - owners
  - bibliography
- assessment_id: hierarchy
  area: identity
  topic: 'Native checklist: strictly broader parent and retained release choice'
  outcome: supported
  target_ids:
  - METPO:1000628
  summary: Halophily preference remains an upstream ancestor through halophilic. The
    local direct parent and introductory definition phrase were expressly retained
    by release disposition; direct-parent drift alone does not establish an incorrect
    hierarchy or warrant blind refresh.
  evidence_ids:
  - identity
  - owners
  - provenance
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: canonical species, named strains and salt-requirement
    note'
  outcome: concern
  target_ids:
  - METPO:1000628
  summary: Official identities and the cited genome paper support Halobacterium salinarum
    and the NRC-1/R1 twin strains. The near-saturating requirement is not directly
    established in that nearest complete main body. Preserve the valid model example
    while narrowing or directly supporting its added physiological assertion.
  evidence_ids:
  - authority
  - canonical-source
  - canonical-query
  - salinity-source
- assessment_id: model
  area: representation
  topic: 'Native checklist: environment category, graph scope and optional fields'
  outcome: supported
  target_ids:
  - METPO:1000628
  summary: ENVIRONMENT/CLASS and contextual NONMECHANISTIC scope are coherent. Two
    protein aggregates have explicit reviewed-label-only rationale. Optional token
    protein instances, pathways, domain/range, priority/subset, discussion and expression
    datasets are not mandatory completeness targets.
  evidence_ids:
  - record
  - local-authority
  - ledger
- assessment_id: grounding
  area: grounding
  topic: 'Native checklist: all eleven node identities and proposal status'
  outcome: supported
  target_ids:
  - METPO:1000628
  summary: Potassium identity is exact and response to osmotic stress matches its
    explicit response-process description. Salt-in and causal proposals retain local
    status. Node8 quality wording and free-text accumulation shorthand are bounded
    precision questions rather than automatic external-ontology failures.
  evidence_ids:
  - authority
  - identity
  - node-edges
  - owners
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all eleven edge roles and directions'
  outcome: supported
  target_ids:
  - METPO:1000628
  summary: Current assigned Biolink/local relations fit their represented roles and
    no current RO relation is present. Historical removed groundings are not current
    findings. Source support is assessed separately from the permitted relation shape.
  evidence_ids:
  - biolink
  - local-authority
  - node-edges
  - ledger
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: eight publications and fourteen nearest placements'
  outcome: concern
  target_ids:
  - METPO:1000628
  summary: The DOI at edges3–4 identifies a different-topic publication; both snippets
    have an independently verified exact origin in the halophilic-enzyme review. Other
    placements have positive contextual support with their organism and evidence-tier
    bounds. The near-saturation note and numerical-definition attribution retain their
    distinct limitations.
  evidence_ids:
  - bibliography
  - wrong-source
  - wrong-source-registry
  - quote-origin
  - definition-source
  - canonical-source
  - salt-in-source
  - stress-source
  - adaptation-source
  - glycosylation-source
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: six snippets and exact source attribution'
  outcome: concern
  target_ids:
  - METPO:1000628
  summary: 'Four snippets are exact at their assigned publications: the organism phrase,
    two salinity phrases and the body salt-in phrase. Two further strings are exact
    in the separately identified halophilic-enzyme abstract but assigned to the therapeutic-bacteria
    DOI. Correct attribution is required even though their words are authentic.'
  evidence_ids:
  - check-extremely-halophilic-snippets
  - definition-source
  - salinity-source
  - salt-in-source
  - quote-origin
  - wrong-source
  - bibliography
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: whole-record coverage and contextual source breadth'
  outcome: supported
  target_ids:
  - METPO:1000628
  summary: All eleven nodes and edges were reviewed. Existing source context supports
    alternative osmoadaptation routes, qualified general responses and named-organism
    glycosylation findings. No universal pathway, token accession, new molecular target
    or experimental demonstration is demanded merely by the broad graph.
  evidence_ids:
  - ledger
  - node-edges
  - bibliography
  - adaptation-source
  - glycosylation-source
- assessment_id: datasets
  area: evidence
  topic: 'Native checklist: optional structured-source applicability'
  outcome: supported
  target_ids:
  - METPO:1000628
  summary: The inspected catalog lacks the canonical species and named strains. Bounded
    runner discovery is explicitly reused, not fresh; no alternative organism query
    or negative biological inference follows.
  evidence_ids:
  - expression
  - runner
- assessment_id: audit
  area: provenance
  topic: 'Native checklist: history, imported authorship, acceptance, owners and checks'
  outcome: concern
  target_ids:
  - METPO:1000628
  summary: Thirteen AI-assisted events and one automated seed are disclosed. Upstream
    created_by and release retention are not local acceptance of this revision. No
    human-acceptance link emerged from the declared ignored-inclusive search. Native
    checks passed within their focused or unchanged-input reuse scope.
  evidence_ids:
  - provenance
  - local-authority
  - owners
  - capture
  - reuse
  - reuse-independent
  - ledger
  - check-batch004-qc
findings:
- finding_id: acidic-proteome-citation-attribution
  issue_key: extremely-halophilic-acidic-proteome-citation-attribution
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Two acidic-proteome claims cite the wrong publication
  description: 'Edges3–4 attach DOI:10.1016/j.copbio.2015.05.004 to acidic-proteome
    claims and two snippets. EPMC and independent Crossref identify that DOI as Engineered
    bacteria as therapeutic agents. Both snippets instead occur verbatim in the actual
    abstract of Halophiles and their enzymes: negativity put to good use, PMID26066288,
    DOI:10.1016/j.mib.2015.05.009. This is a confirmed source-attribution mismatch
    covering two placements, not merely an abstract-search miss. Preserve the positive
    underlying biology supported by the exact-origin abstract and the separately cited
    haloarchaeal review; no new pathway or therapeutic-bacteria mechanism is needed
    to correct the bibliography.'
  target_ids:
  - METPO:1000628
  field_paths:
  - causal_graphs[0].edges[3].evidence[0].reference
  - causal_graphs[0].edges[3].evidence[0].snippet
  - causal_graphs[0].edges[4].evidence[0].reference
  - causal_graphs[0].edges[4].evidence[0].snippet
  evidence_ids:
  - wrong-source
  - wrong-source-registry
  - quote-origin
  - quote-origin-receipt
  - adaptation-source
  - bibliography
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/extremely_halophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: canonical-growth-requirement-source
  issue_key: extremely-halophilic-canonical-growth-requirement-source
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The canonical citation does not establish the added salt requirement
  description: The cited complete genome-comparison paper establishes Halobacterium
    salinarum and its twin laboratory strains NRC-1/R1, but the inspected main-body
    text does not establish the note’s requiring-near-saturating-NaCl assertion. That
    stronger physiological wording needs a directly supporting source or narrower
    wording. Preserve the correct species/strain identities and general extreme-halophile
    model context; this gap does not demonstrate that the organism’s phenotype is
    false.
  target_ids:
  - METPO:1000628
  field_paths:
  - canonical_examples[0].note
  - canonical_examples[0].reference
  evidence_ids:
  - canonical-source
  - authority
  - salinity-source
  - bibliography
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/extremely_halophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: extremely-halophilic-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human scientific acceptance is not linked locally
  description: The fourteen history events comprise thirteen disclosed AI-assisted
    events and an automated seed. The created_by name is copied upstream authorship,
    and retained release dispositions do not identify a human accepting this record
    revision. The ignored-inclusive local search and review target-list inspection
    found no explicit human-acceptance link. This documentary gap does not establish
    that no private or remote human review occurred.
  target_ids:
  - METPO:1000628
  field_paths:
  - mapping_status
  - created_by
  - curation_history
  evidence_ids:
  - provenance
  - local-authority
  - ledger
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/extremely_halophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: repair-source-attribution
  description: In separately authorized curation, align both acidic-proteome evidence
    entries with their verified quotation source.
  finding_ids:
  - acidic-proteome-citation-attribution
  target_ids:
  - METPO:1000628
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/extremely_halophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The reference and exact snippet at each affected placement resolve together to
    the actually inspected source; PMID26066288/DOI10.1016/j.mib.2015.05.009 is the
    verified origin of both current strings.
  - Preserve the supported existing biological explanation and distinguish source
    identity correction from mechanism expansion; no pathogen-route investigation
    or experimental recommendation is required.
  - Check both nearest placements and source notes, not only a top-level bibliography
    entry.
  - After authorized edits use guarded writes, append-only history, focused strict/snippet/term/graph
    checks, just qc and maintained derived-product regeneration.
- action_id: bound-canonical-requirement
  description: Retain the valid model/strain example while directly supporting or
    narrowing its near-saturation requirement wording.
  finding_ids:
  - canonical-growth-requirement-source
  target_ids:
  - METPO:1000628
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/extremely_halophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The cited genome paper continues to support the twin-strain identity/history for
    NRC-1 and R1.
  - Any retained physiological requirement has an actual inspected source passage,
    with growth requirement distinguished from habitat, tested condition and optimum.
  - Do not replace the species or strains merely because the nearest reference is
    genomic, and do not infer that the phenotype is false.
- action_id: link-acceptance
  description: Locate and link existing human scientific acceptance or obtain it through
    the established process, preserving history and reassessing status if needed.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000628
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/extremely_halophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies the reviewed revision and scientific scope.
  - Imported created_by, AI disclosures, release-retention reports, structural checks
    and this review are not substituted for human scientific acceptance; retain append-only
    history.
- action_id: clarify-definition-attribution
  description: Keep ontology authority and unresolved numerical publication support
    distinct during any later bibliographic curation.
  finding_ids: []
  target_ids:
  - METPO:1000628
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/extremely_halophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/finalize_metpo_2026_06_12_review.py
    role: Retained semantic-choice owner; do not blindly overwrite local hierarchy/definition
  acceptance_checks:
  - The15–30% optimum and approximately12% boundary retain their ontology provenance;
    PMID11790755 is not claimed verified for those numbers solely because it uses
    extremely-halophilic terminology.
  - Actual accessible source text is required before asserting a contradiction or
    changing numerical criteria.
  - No new organism optimization, protocol or biological mechanism is proposed; preserve
    the valid broader-ancestor relation and recorded release disposition.
limitations:
- The definition’s numerical clause agrees with pinned METPO, but PMID11790755 was
  available only as an indexed abstract. Its exact organism terminology is verified;15–30%
  and approximately12% publication attribution remain unverified, not demonstrated
  false.
- The canonical paper directly supports species/strain identity and twin-strain history.
  Its complete main body does not establish the near-saturating requirement. This
  bounded source gap is not a negative growth result or false-classification finding.
- Five cited full texts are local; relevant existing claims were inspected, without
  an exhaustive methods, supplements or all-cited-references audit. The salinity review
  has fresh abstract support and retained prior opening-PDF inspection only.
- The therapeutic-bacteria source was assessed only for documentary metadata/abstract
  scope. Both misattributed strings were verified in the actual different-source abstract;
  no detailed therapeutic or pathogen mechanism was investigated.
- Source contexts include a specific Haloarcula strain, a Halomonas shock study, general
  haloarchaeal reviews and named-organism glycosylation background. These do not establish
  every extreme halophile using an identical pathway. The graph’s generic scope and
  existing often qualifier are preserved.
- No formal grounding defect was found. Short response labels are interpreted using
  their descriptions; maintained proposal identifiers remain provisional, and historical
  removed accessions/relations are not current assertions.
- Common checks and B4 QC retain their original execution times, failed attempts,
  adapter skips, baselines and warnings and are reused only on documented unchanged
  inputs. No new full-corpus run or newer-ontology certification is implied.
- Initial official authority DNS failures are retained beside successful retries.
  Actual timestamps and raw-response hashes remain distinguishable from later ledger/assessment
  times.
- There are no protein instances to audit. Catalog noncoverage and reused bounded
  runner discovery do not imply absent phenotype or function, and no alternative organism
  was substituted.
- Human acceptance beyond the ignored-inclusive local search remains unknown. Imported
  upstream authorship and this review do not confer local human scientific sign-off.
- No record, mapping, history or generated product was edited. No paid provider call,
  new pathway, molecular target, protocol or experiment was proposed.
notes:
- All node, edge and extracted body-paragraph indices are zero-based.
- Native capture retained59 inputs09:48:14–16Z; independent grounding inspection confirmed
  every hash. Fourteen history events comprise thirteen AI-assisted events plus an
  automated seed.
- One major and two minor findings. Initial abstract misses are superseded only by
  actual body text or independently verified exact quotation origin, with original
  access receipts retained.
tags:
- record-review
- extremely-halophilic
- environment
- needs-curation
```
