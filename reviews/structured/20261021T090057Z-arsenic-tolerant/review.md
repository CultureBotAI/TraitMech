# Evidence, grounding and protein-anchor review of arsenic tolerance (traitmech:000017)

- Review: 20261021T090057Z-arsenic-tolerant
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T08:53:09Z
- Finished UTC: 2026-10-21T09:00:57Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Arsenic tolerance retains a justified traitmech identifier, appropriate hierarchy and supported environmental resistance context. Two major findings concern two mismatched node groundings and, provisionally, the stronger experimental certainty assigned to the Q1LRL1 anchor than the inspected accession/primary-source evidence establishes. Three minor findings concern an unverified quotation, nearest-edge citation placement and a bounded missing human-acceptance link. All thirteen nodes and twelve edges were inspected. The live UniProt audit fails on later version drift, while archived99 supports the historical metadata.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Sixth batch004 target in lexicographic path order. Entire target read before native capture; all thirteen nodes, twelve edges, three canonical examples and the single protein example are in scope.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000017 | data/traits/environment/arsenic_tolerant.yaml | maintained | arsenic tolerant |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000017 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000017 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000017 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | traitmech:000017 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | traitmech:000017 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000017 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000017 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | traitmech:000017 | Selected record validates. |
| Focused strict validation | passed | True | traitmech:000017 | One file scanned; zero strict errors. |
| Focused abstract snippet check | passed | True | traitmech:000017 | Three snippets across three references are NOT_IN_ABSTRACT. These misses are inconclusive; inspected full-text and quotation assessments are separate. |
| Initial narrower UniProt invocation | passed | False | traitmech:000017 | Exited0 but inspected zero nodes: the native implementation uses a category/file glob under the trait root. This execution establishes no target coverage and is superseded by the corpus invocation. |
| Native full-corpus protein/taxon coverage | passed | True | traitmech:000017 | 719graphs:129PASS,589NONMECHANISTIC,onePROTECTED,zero gaps/errors. The target passes with six reviewed label-only proteins, three cited canonical examples and one taxon-paired example. Coverage does not establish experimental source support. |
| Native full-corpus live UniProt audit | failed | True | traitmech:000017 | Exit1:146uses across115accessions,110findings all ENTRY_VERSION_MISMATCH. The target differs only at entry version99 versus current100; primary accession, taxon, status, sequence and proteome match. Archived99 supports the recorded retrieval-time snapshot, so current drift is not by itself an original curation defect. |
| Structured-source runner discovery | unavailable | False | traitmech:000017 | Bounded original discovery reused; official API fallback inspected. |
| KT2440 expression context and Cupriavidus applicability | passed | False | traitmech:000017 | Twelve fresh API GETs: dataset metadata, eight term searches, three selected gene memberships. Source strain matched; no directly matching module or positive inspected membership flag. No negative biological inference. |

## Scientific And Domain Assessments

### Native checklist: fallback, synonyms, polarity and hierarchy

identity: supported. Targets: traitmech:000017.

The accepted traitmech identifier is appropriate against the complete pinned METPO scan. Arsenic resistance is a related synonym, and the broader metal/metalloid-tolerance parent includes this narrower phenotype. The local proposal is not treated as a minted upstream identity.

### Native checklist: broad growth capability and typical mechanism

evidence: supported. Targets: traitmech:000017.

The definition is a reasonable synthesis of the cited resistance review. Typical ars-associated export is supported, while the graph and source preserve alternative exporters; neither a universal ArsB requirement nor an exact concentration threshold is asserted.

### Native checklist: three organism examples and one accession

evidence: concern. Targets: traitmech:000017.

CH34 supports a resistant member of C. metallidurans and a family/cluster-level reduction branch. KT2440 supplies the actual P. putida source context. Q1LRL1 identity is valid, but accession-specific experimental support is not established by the cited genome text and homology annotation alone.

### Native checklist: environmental class and MECHANISTIC evidence tier

representation: concern. Targets: traitmech:000017.

ENVIRONMENT/CLASS fits. The scoped graph does not claim every branch is universal, and the native taxon/protein coverage gate passes. Its stronger experimentally supported anchor wording nevertheless needs evidence that is distinguishable from family background and cluster annotation.

### Native checklist: all node identities and external terms

grounding: concern. Targets: traitmech:000017.

The arsenite charge-state label disagrees with its CHEBI term, and general metal-ion transport is not an exact grounding for arsenite export. Arsenate identity and all taxonomy match. No arbitrary protein accession replacement or inferred physiological protonation state is proposed.

### Native checklist: twelve edge directions and endpoint roles

consistency: supported. Targets: traitmech:000017.

Current RO executor/process and process/output pairs and proposed METPO challenge/mitigation/reduction pairs have compatible roles. Promoter is correctly typed as a genetic element; gene symbols and operon metadata do not make the protein-module node an operon-as-protein error.

### Native checklist: eight references, three excerpts and nearest support

evidence: concern. Targets: traitmech:000017.

Most existing family-level claims have direct review/background support. The CH34 anchor phrase is unverified as a quotation, and edge11 uses a gene-inventory citation where other already-cited passages explicitly state the reaction. The MIC value is correct as an inhibitory endpoint; the PeerJ study’s own data remain genomic rather than a cellular depletion assay.

### Native checklist: retrieval-time metadata versus current audit

provenance: supported. Targets: traitmech:000017.

Archived Q1LRL1 version99 matches the stored snapshot, including sequence1, primary accession, strain and proteome. The native live audit correctly reports later version100 drift. That result is retained as a failed freshness check without inventing an original metadata error or treating unreviewed status alone as forbidden.

### Native checklist: source-matched KT2440 computational context

evidence: supported. Targets: traitmech:000017.

The exact cited strain matches p_putida/precise321. Eight searches and three selected gene memberships supply bounded annotation context without a directly matching module or positive inspected membership. No absent-function inference or transfer to Cupriavidus follows.

### Native checklist: required structure and optional surfaces

completeness: supported. Targets: traitmech:000017.

All thirteen nodes and twelve edges resolve; the graph has an appropriately paired instance structurally. Optional datasets and additional protein examples are not automatically required. Existing research is a provenance lead, not independent evidence.

### Native checklist: nine AI events, human acceptance and ownership

provenance: concern. Targets: traitmech:000017.

All nine events explicitly disclose AI assistance. Human acceptance was not linked within the declared local bounds. The two node groundings need guarded record correction; the current mapping search does not establish an automatic recurrence owner.

## Findings

### node-grounding-semantics: Two node groundings do not denote their stated concepts

major / open / confirmed; issue key: arsenic-tolerant-node-grounding-semantics.

Node1 is labelled arsenite(3−), but CHEBI29242 currently denotes arsenite(1−). Node3 asserts arsenite transmembrane export while GO0030001 denotes general metal-ion transport. The GO term has the correct broad biological-process aspect, but is not an exact semantic grounding. Reconcile intended entities without guessing physiological speciation or minting an unsupported replacement.

### anchor-quotation: The protein-anchor snippet is not verified verbatim

minor / open / confirmed; issue key: arsenic-tolerant-anchor-quotation.

The recorded phrase does not occur in the complete retrieved CH34 article XML, including tables and references, although it is a plausible descriptive summary of the source. Move interpretation to notes or supply a short verified excerpt. The supplementary workbook was not exhaustively parsed, so this is not an absence claim across every supplement or the literature.

### nearest-reaction-evidence: The reduction edge cites gene-inventory evidence

minor / open / confirmed; issue key: arsenic-tolerant-nearest-reaction-evidence.

Edge11 cites the BS1 genome study with only a graph-wiring note. Its inspected nearest passage lists predicted arsenic-related genes; the represented reduction reaction is directly described by other sources already cited in the record. Attach direct reaction support to this edge while retaining genomic annotation in its proper role. This is evidence-placement precision, not false chemistry.

### human-acceptance-link: Human scientific acceptance is not linked locally

minor / open / confirmed; issue key: arsenic-tolerant-human-acceptance-link.

All nine record events disclose AI assistance, including the promotion to REVIEWED. No explicit human acceptance identifying this revision was found in the ignored-inclusive declared local scope. Private or remote acceptance remains unknown; native validation and this new agent review are not human sign-off.

### experimental-anchor-certainty: The claimed experimental protein anchor is not established by the cited evidence

major / open / provisional; issue key: arsenic-tolerant-experimental-anchor-certainty.

The scope note presents the taxon-paired Q1LRL1 example as anchoring an experimentally supported branch. The inspected genome paper supports ArsC-family reduction and explicitly marks a CH34 ars cluster containing C1 and C2 active, while the accession annotation is based on homology/genomic sequence. These sources do not identify the accession-specific experiment that would substantiate the stronger anchor wording. The concern is provisional and bounded to inspected evidence: CH34 functional support is present, the protein is not shown to be wrong or nonfunctional, and no literature-wide absence is asserted.

## Recommended Actions And Acceptance Checks

### repair-grounding

In separately authorized curation, reconcile the intended arsenite species and export concept with exact node labels/groundings.

- The arsenite label and selected ChEBI identity agree without assuming an unsupported protonation state.
- The transport grounding denotes the intended exact process; a nearby broader GO term is not presented as exact.
- The existing node writer skips populated IDs. Use guarded record correction and review the maintained mapping only if a supported reusable mapping is added.
- Run focused strict/term/graph checks and just qc, preserve native curation/history and regenerate affected products after authorized edits.

### repair-snippet

Replace the descriptive anchor phrase with a short verified quotation or move it into interpretation notes.

- The excerpt has an exact inspected source location and remains distinct from interpretation.
- Run the focused snippet check and manual full-text verification; abstract absence alone is inconclusive.

### place-reaction-evidence

Attach already-supported reaction evidence to edge11 and retain the BS1 genome reference only for the claim it establishes.

- The edge’s nearest evidence explicitly supports the represented reaction.
- Do not promote genome annotation into a new protein-specific experiment.
- Run focused record and evidence validation after authorized changes.

### link-acceptance

Locate and link existing human scientific acceptance or obtain it through the established process, preserving all AI provenance.

- Acceptance identifies this record revision and scientific scope.
- If acceptance remains unavailable, reassess native status without misrepresenting automated checks as sign-off.

### substantiate-or-qualify-anchor

Resolve the accession-specific evidence tier: link the experiment supporting the stated anchor if available, or qualify the scope and example to the family/cluster-level evidence actually established.

- The relationship between the named protein instance, source organism and claimed experimental branch is explicit and source-backed.
- Preserve the verified active CH34 cluster and family-level function; do not declare the protein nonfunctional or discard valid identity merely because its database status is unreviewed.
- A supported qualification is an acceptable resolution; no new experimental design or expanded mechanism is required.
- Reassess native graph scope only as warranted by the documented evidence, then run protein/taxon coverage, focused validation and just qc after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-arsenic_tolerant-validate | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/arsenic_tolerant-validate.log; Executed 2026-10-21T08:53:31Z through 2026-10-21T08:53:32Z; metadata arsenic_tolerant-validate.json | context_only | Selected record validates. |
| check-arsenic_tolerant-strict | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/arsenic_tolerant-strict.log; Executed 2026-10-21T08:53:31Z through 2026-10-21T08:53:33Z; metadata arsenic_tolerant-strict.json | context_only | One file scanned; zero strict errors. |
| check-arsenic_tolerant-snippets | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/arsenic_tolerant-snippets.log; Executed 2026-10-21T08:53:39Z through 2026-10-21T08:53:44Z; metadata arsenic_tolerant-snippets.json | context_only | Three snippets across three references are NOT_IN_ABSTRACT. These misses are inconclusive; inspected full-text and quotation assessments are separate. |
| check-environment-uniprot | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/environment-uniprot.log; Executed 2026-10-21T08:54:50Z through 2026-10-21T08:54:50Z; metadata environment-uniprot.json | context_only | Exited0 but inspected zero nodes: the native implementation uses a category/file glob under the trait root. This execution establishes no target coverage and is superseded by the corpus invocation. |
| check-corpus-protein-taxa | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log; Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json | context_only | 719graphs:129PASS,589NONMECHANISTIC,onePROTECTED,zero gaps/errors. The target passes with six reviewed label-only proteins, three cited canonical examples and one taxon-paired example. Coverage does not establish experimental source support. |
| check-corpus-uniprot | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-uniprot.log; Executed 2026-10-21T08:55:08Z through 2026-10-21T08:56:53Z; metadata corpus-uniprot.json | context_only | Exit1:146uses across115accessions,110findings all ENTRY_VERSION_MISMATCH. The target differs only at entry version99 versus current100; primary accession, taxon, status, sequence and proteome match. Archived99 supports the recorded retrieval-time snapshot, so current drift is not by itself an original curation defect. |
| record | data/traits/environment/arsenic_tolerant.yaml; Entire identity, evidence, graph, protein instance and history | partial | Environmental arsenic tolerance is the intended trait. The record presents one mechanistic branch anchored to a CH34 protein example; schema validity and taxon matching do not by themselves prove that branch experimentally. |
| shape | Whole graph and history inspection; Thirteen nodes, twelve edges, one protein example and nine events | supports | All endpoints resolve, all nine events disclose AI assistance, and no pathway-context link is asserted. |
| policy | docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml; Semantic grounding versus protein instances; protein version metadata | supports | A taxon-paired instance is distinct from a family node. Label-only family decisions are allowed; each experimental claim still needs appropriately scoped source evidence. Entry and sequence versions explicitly describe the retrieval-time snapshot, not a promise that the external database never changes. |
| provenance | Target events and bounded local history/mapping/writer/review search; Nine AI-assisted events; ignored-inclusive exact identifier/path/label search | partial | No explicit local link to human scientific acceptance was identified in the inspected scope. AI-assisted promotion to REVIEWED and subsequent automated integrity checks do not establish human acceptance; unsearched remote/private acceptance remains unknown. |
| status-rule | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md; Status/audit and human acceptance gate | supports | REVIEWED requires human scientific acceptance. An AI-authored history event and a valid review bundle do not supply it. |
| expression | https://imodulondb.org/api; p_putida/precise321; Official KT2440 dataset metadata; eight bounded searches and three selected gene-membership responses | context_only | The cited P. putida paper and dataset explicitly identify KT2440. No Cupriavidus dataset matches. Search results include annotations but no directly matching module; three selected genes each have zero positive membership flags across84returned rows. These computational observations do not establish absent expression/function, mechanism or tolerance. They are not transferred to CH34 or BS1. |
| runner | Structured-source runner discovery; Original ignored-inclusive08:17:15Z search, hash-verified reuse | context_only | The structured runner was unavailable within the original bounds; official API fallback supplied current KT2440 context. Original catalog07:36:12Z and runner receipts are retained without claiming fresh/global absence. |
| identity | Pinned data/raw/metpo.owl; proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv; parent traitmech000012; Complete pinned METPO scan and proposal rows19/14 | supports | No active exact arsenic-tolerance term was found in the pinned ontology, including the complete ignored-file-independent OWL inspection. The local v5 proposed1007616 is not minted upstream in that snapshot. Preserve the accepted traitmech fallback. Metal tolerance explicitly includes metalloids and is strictly broader. |
| live-grounding | Official ChEBI29242/29125; QuickGO GO0030001; NCBI taxa119219/303/266264; Live identity responses08:54:06–07Z | partial | CHEBI29242 is arsenite(1−), conflicting with the node’s arsenite(3−) label. CHEBI29125 agrees with arsenate(3−). GO0030001 denotes general metal-ion transport rather than exact arsenite export. All three current taxon labels match. GO is a valid biological process; its problem here is semantic specificity. |
| protein | https://rest.uniprot.org/uniprotkb/Q1LRL1.json; https://rest.uniprot.org/proteomes/UP000002429.json; Current primary accession08:54:07Z and reference proteome08:55:33Z | partial | Primary Q1LRL1, unreviewed status, arsC1/Rmet_0329, CH34 taxon266264 and proteomeUP000002429 all match. Current entry100/sequence1 is later than stored99/1. Protein existence is inferred from homology and the linked paper is large-scale genomic sequencing; metadata alone does not establish a protein-specific experiment. |
| archive | https://rest.uniprot.org/unisave/Q1LRL1?format=txt&amp;versions=99; UniSave version99, retrieved08:54:43–44Z | supports | Archived entry99 is dated08-OCT-2025 and matches primary accession, gene, strain, proteome, unreviewed status and sequence1. The current100 update occurred2026-09-02, after the record’s declared2026-08-25 retrieval. This is consistent with the historical metadata, without independently re-observing that past retrieval. |
| ledger | Complete independent grounding/endpoint ledger; All thirteen nodes and twelve edges | partial | Two node groundings conflict with their exact labels/concepts. No formal current relation endpoint conflict was confirmed. Promoter typing and gene/operon metadata are already appropriate; label-only family nodes and optional predicate IDs are allowed. |
| relations | RO0002327 and RO0002234; local v8/v9 proposal tables; Executor/process, process/output and proposed challenges/mitigates/reduces roles | supports | The current grounded relations fit their documented broad endpoint roles. RO enables authority is reused from07:58:06Z; has-output authority was inspected08:54:03Z. Historical microbe-domain defects have already been migrated and are not reported as current errors. |
| owners | mappings/node_grounding.tsv; scripts/ground_causal_nodes.py; scripts,src,proposals; Ignored-inclusive literal label/identifier search and populated-ID handling | partial | No current matching row/literal for the two problematic groundings was found in the declared owner-search bounds. The maintained writer skips populated IDs. Correct the target through guarded curation; there is no evidence that clearing an ID would regenerate the same value from the present table. This is not a claim that historical owners never existed. |
| bibliography | Primary-source identity and claim ledger; Eight references, twenty citation placements, three excerpts, all nodes/edges | partial | Eight identities resolve. Seven article bodies and one complete indexed abstract were inspected. One excerpt is exact, one differs only by micro-unit typography, and the protein-anchor phrase was not found in the retrieved complete article text. Seventeen access attempts produced sixteen hashed acquisitions including a supplement; publisher403 is not evidence. |
| review-source | https://doi.org/10.3389/fmicb.2018.02473; PMID30405552, PMC6205960; The ars Operons body4/9/11/12; Distribution19; Additional Genes24–25 | supports | The review supports the broad resistance synthesis, common ars systems, exact ArsB extrusion quotation and alternative exporters. It does not make ArsB universal. Its soil KT2440 context corroborates the canonical note; general resistance remains distinct from a numerical assay threshold. |
| bs1 | https://doi.org/10.3389/fmicb.2020.00047; PMID32117100, PMC7019866; ResultsS3.SS1/body11, Table1, S3.SS12/body41 | partial | BS1 arsenite MIC3.5mM is exact; the excerpt’s uM/μM typography does not change its value. MIC is an inhibitory endpoint, not demonstrated growth at that concentration or a measured intracellular pool. The later gene inventory supports ArsC annotation but does not directly state/test the reduction reaction at edge11. Other already-cited sources explicitly supply that reaction. |
| ars | https://doi.org/10.3390/antibiotics12091474; PMID37760770, PMC10525130; Section2.2 Arsenic/body30 | supports | The inspected review paragraph directly supports existing generic ArsR promoter binding, ArsC reduction and ArsB export claims. It is review-level support across configurations, not an assay of the named CH34 accession. An awkward neighboring regulatory sentence was not used to infer a new route or silently override the separately cited regulation source. |
| regulation | https://doi.org/10.3389/fmicb.2024.1494872; PMID39640857, PMC11617546; Section2/body4 | supports | The environmental bioreporter mini-review directly states the existing arsenite/ArsR conformational derepression claim in its background. The assessment verifies attribution only and supplies no design, optimization or universal operon configuration. |
| acr3 | https://doi.org/10.3390/microorganisms12010074; PMID38257901, PMC10820871; Section3.2/body18 | supports | The nearest review supports Acr3 as an alternative inorganic arsenic exporter in some microorganisms. The separately cited2018 review corroborates arsenite specificity. No universal exporter or specific protein instance is inferred. |
| arsm | https://doi.org/10.7717/peerj.18383; PMID39494289, PMC11531259; Introductionsec1/body3, Discussionsec16/body37, Conclusionssec17/body41 | partial | Source background supports the generic methylation/volatile-endpoint route. The agricultural-soil study proposes cooperation from metagenomic distributions; it did not measure intracellular depletion or individual-cell tolerance. This evidence-tier limit does not make the contextual route false or a universal assertion. |
| ch34 | https://doi.org/10.1371/journal.pone.0010433; PMID20463976, PMC2864759; Abstract, Results s2f/body52, Table5 arsPHC1BC2IRM row, ref94 | partial | The genome/manual-annotation study supports CH34 tolerance, family-level ArsC reduction/efflux and an explicitly active ars cluster. Those observations do not by themselves identify a Q1LRL1-specific experiment. The recorded anchor phrase is not verbatim text in the complete retrieved article XML, including tables/references; this is not a global literature-absence claim. |
| ch34-supplement | https://journals.plos.org/plosone/article/file?type=supplementary&amp;id=10.1371/journal.pone.0010433.s010; TableS2 caption and embedded spreadsheet cell strings | context_only | Downloaded TableS2 supplies gene-cluster annotation-comparison context. Embedded strings were inspected, but the workbook was not exhaustively parsed; no exhaustive quotation or experiment absence across all supplements is claimed. |
| putida | https://pubmed.ncbi.nlm.nih.gov/25646541/; DOI10.1111/1758-2229.12167; title and complete abstract | supports | The primary study identifies KT2440 and supports arsenite/arsenate tolerance, acknowledging strain differences. It establishes an example within P. putida, not equal resistance in every strain or every metal. The publisher body returned403; source use remains abstract-limited. |

## Limits And Additional Notes

- The experimental-anchor finding is provisional. The CH34 source explicitly supports an active ars cluster and family-level reduction/efflux; it does not by itself identify a Q1LRL1-specific experiment. This is not evidence that the protein is wrong/nonfunctional or that no such experiment exists elsewhere.
- The complete retrieved CH34 article XML was searched for the anchor phrase. The supplementary XLS was downloaded and embedded strings inspected, but the workbook was not exhaustively parsed; no all-supplement absence claim is made.
- The P. putida primary study was assessed through its complete abstract because publisher body access returned403. Its actual strain is KT2440; species-level exemplar naming does not establish equal tolerance in all strains.
- The BS1 value3.5mM is a correct MIC under the source assay. The record already identifies it as MIC; no separate growth-at-MIC falsehood finding is made. It is not a cytoplasmic concentration measurement.
- The PeerJ methylation route is supported as literature background. Its own metagenomic study proposes community cooperation and does not measure intracellular depletion; no new false-route finding is inferred from that limitation.
- The live UniProt command returned1 for110current entry-version mismatches across the corpus. This target differs at99versus100 only. Archived99 is consistent with the recorded retrieval snapshot and schema semantics; the historical retrieval itself was not re-observed.
- The initial category-directory UniProt invocation returned0while inspecting zero nodes because of its native category/file glob. It supplies no target coverage and is retained separately from the subsequent full-corpus audit.
- GO0030001 is a valid biological process. The finding concerns exact transport semantics, not an invalid aspect or a claimed reasoner failure. CHEBI charge reconciliation does not prescribe unsupported physiological speciation.
- Expression context covers one exact KT2440 dataset, eight bounded searches and three selected gene memberships. Zero positive membership flags are not evidence of absent expression, function or tolerance, and no result was transferred to Cupriavidus.
- Unreviewed protein instances are permitted by the native model; valid identity/status/proteome metadata do not substitute for primary experimental evidence.
- Common corpus checks retain original executions and reuse verification. Fresh protein/taxon and UniProt audits are reported with their actual broader scope, including failures.
- Human acceptance remains unknown outside the bounded ignored-inclusive local search.
- Existing provider research supplied provenance/leads only. No paid call, record/status/history/mapping/schema change, generated-page edit or experimental optimization was performed.
- Field indices are zero-based.
- Initial capture08:53:09–10Z retained53inputs; supplemental capture08:55:03–04Z retainedall53unchanged and addedtwo native audit implementation files.
- Review validation is separate from scientific/native-audit verdict: the UniProt freshness failure is retained rather than hidden.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T090057Z-arsenic-tolerant
kind: record
repository: CultureBotAI/TraitMech
title: Evidence, grounding and protein-anchor review of arsenic tolerance (traitmech:000017)
started_at: '2026-10-21T08:53:09Z'
finished_at: '2026-10-21T09:00:57Z'
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
summary: Arsenic tolerance retains a justified traitmech identifier, appropriate hierarchy
  and supported environmental resistance context. Two major findings concern two mismatched
  node groundings and, provisionally, the stronger experimental certainty assigned
  to the Q1LRL1 anchor than the inspected accession/primary-source evidence establishes.
  Three minor findings concern an unverified quotation, nearest-edge citation placement
  and a bounded missing human-acceptance link. All thirteen nodes and twelve edges
  were inspected. The live UniProt audit fails on later version drift, while archived99
  supports the historical metadata.
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
  - path: data/traits/environment/arsenic_tolerant.yaml
    sha256: b7c4c9ee1b352e7194421d11f8ed653d6ff01f58ea29bd934f069632071bb320
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
  - path: reports/ontology_snapshot_manifest.tsv
    sha256: 4a157279a8c4e3fc2afb5382a45c31961991bbd1f330f26d0061b0cfd0b4d213
    role: context
  - path: research/traits/environment/arsenic_tolerant-deep-research-falcon.md
    sha256: 34cac39ea026f302304bc4b2f12e183b730a703133c44244df039d1f9ebdb0eb
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
- target_id: traitmech:000017
  path: data/traits/environment/arsenic_tolerant.yaml
  label: arsenic tolerant
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/arsenic_tolerant.yaml
    role: Maintained TraitRecord; scientific changes require guarded curation
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: METPO-first identifier comparison; target was curator proposed
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Sixth batch004 target in lexicographic path order. Entire target read
    before native capture; all thirteen nodes, twelve edges, three canonical examples
    and the single protein example are in scope.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000017
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000017
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - traitmech:000017
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - traitmech:000017
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - traitmech:000017
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - traitmech:000017
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - traitmech:000017
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - traitmech:000017
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: arsenic_tolerant-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - traitmech:000017
  command: just validate data/traits/environment/arsenic_tolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Selected record validates.
  evidence_ids:
  - check-arsenic_tolerant-validate
- check_id: arsenic_tolerant-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000017
  command: just validate-strict data/traits/environment/arsenic_tolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero strict errors.
  evidence_ids:
  - check-arsenic_tolerant-strict
- check_id: arsenic_tolerant-snippets
  name: Focused abstract snippet check
  status: passed
  required: true
  target_ids:
  - traitmech:000017
  command: just verify-snippets --record data/traits/environment/arsenic_tolerant.yaml
    --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/arsenic_tolerant-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Three snippets across three references are NOT_IN_ABSTRACT. These misses
    are inconclusive; inspected full-text and quotation assessments are separate.
  evidence_ids:
  - check-arsenic_tolerant-snippets
- check_id: environment-uniprot
  name: Initial narrower UniProt invocation
  status: passed
  required: false
  target_ids:
  - traitmech:000017
  command: just audit-uniprot --traits-dir data/traits/environment --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/environment-uniprot.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Exited0 but inspected zero nodes: the native implementation uses a category/file
    glob under the trait root. This execution establishes no target coverage and is
    superseded by the corpus invocation.'
  evidence_ids:
  - check-environment-uniprot
- check_id: corpus-protein-taxa
  name: Native full-corpus protein/taxon coverage
  status: passed
  required: true
  target_ids:
  - traitmech:000017
  command: just audit-graph-protein-taxa --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 719graphs:129PASS,589NONMECHANISTIC,onePROTECTED,zero gaps/errors. The
    target passes with six reviewed label-only proteins, three cited canonical examples
    and one taxon-paired example. Coverage does not establish experimental source
    support.
  evidence_ids:
  - check-corpus-protein-taxa
- check_id: corpus-uniprot
  name: Native full-corpus live UniProt audit
  status: failed
  required: true
  target_ids:
  - traitmech:000017
  command: just audit-uniprot --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-uniprot.tsv
  exit_code: 1
  expected_exit_code: 0
  summary: Exit1:146uses across115accessions,110findings all ENTRY_VERSION_MISMATCH.
    The target differs only at entry version99 versus current100; primary accession,
    taxon, status, sequence and proteome match. Archived99 supports the recorded retrieval-time
    snapshot, so current drift is not by itself an original curation defect.
  evidence_ids:
  - check-corpus-uniprot
- check_id: structured-source-runner
  name: Structured-source runner discovery
  status: unavailable
  required: false
  target_ids:
  - traitmech:000017
  summary: Bounded original discovery reused; official API fallback inspected.
  evidence_ids:
  - runner
- check_id: expression-context
  name: KT2440 expression context and Cupriavidus applicability
  status: passed
  required: false
  target_ids:
  - traitmech:000017
  summary: 'Twelve fresh API GETs: dataset metadata, eight term searches, three selected
    gene memberships. Source strain matched; no directly matching module or positive
    inspected membership flag. No negative biological inference.'
  evidence_ids:
  - expression
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-arsenic_tolerant-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/arsenic_tolerant-validate.log
  locator: Executed 2026-10-21T08:53:31Z through 2026-10-21T08:53:32Z; metadata arsenic_tolerant-validate.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: Selected record validates.
  snapshot_sha256: 7b447de6ed364a33d62eb18b95f36c484152437f2532a547228da3a4711f75b9
- evidence_id: check-arsenic_tolerant-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/arsenic_tolerant-strict.log
  locator: Executed 2026-10-21T08:53:31Z through 2026-10-21T08:53:33Z; metadata arsenic_tolerant-strict.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: One file scanned; zero strict errors.
  snapshot_sha256: ca30713c13a6307905a049109165283dc35826f8c4f889809853ce2c46577181
- evidence_id: check-arsenic_tolerant-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/arsenic_tolerant-snippets.log
  locator: Executed 2026-10-21T08:53:39Z through 2026-10-21T08:53:44Z; metadata arsenic_tolerant-snippets.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: Three snippets across three references are NOT_IN_ABSTRACT. These misses
    are inconclusive; inspected full-text and quotation assessments are separate.
  snapshot_sha256: b13dd6d96c754d9d407f35b248cc2caced837189e8d10259c27711ffe47a8e54
- evidence_id: check-environment-uniprot
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/environment-uniprot.log
  locator: Executed 2026-10-21T08:54:50Z through 2026-10-21T08:54:50Z; metadata environment-uniprot.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: 'Exited0 but inspected zero nodes: the native implementation uses a category/file
    glob under the trait root. This execution establishes no target coverage and is
    superseded by the corpus invocation.'
  snapshot_sha256: 15050bd32ce990992e9e67c6425af0c84dc1bc4cd0d889a49ed6851bdbc095d6
- evidence_id: check-corpus-protein-taxa
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log
  locator: Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: 719graphs:129PASS,589NONMECHANISTIC,onePROTECTED,zero gaps/errors. The
    target passes with six reviewed label-only proteins, three cited canonical examples
    and one taxon-paired example. Coverage does not establish experimental source
    support.
  snapshot_sha256: f5f1a6be7789f2b3e487fcbc354361f8f1f0d0d0f90a9ba59864d26ed7ac49ef
- evidence_id: check-corpus-uniprot
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-uniprot.log
  locator: Executed 2026-10-21T08:55:08Z through 2026-10-21T08:56:53Z; metadata corpus-uniprot.json
  accessed_at: '2026-10-21T09:00:57Z'
  support: context_only
  summary: Exit1:146uses across115accessions,110findings all ENTRY_VERSION_MISMATCH.
    The target differs only at entry version99 versus current100; primary accession,
    taxon, status, sequence and proteome match. Archived99 supports the recorded retrieval-time
    snapshot, so current drift is not by itself an original curation defect.
  snapshot_sha256: 6ad9ec31ef33837fb5f0d72d8c306af0ec862745d08c88240437e2e5012607b6
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/arsenic_tolerant.yaml
  locator: Entire identity, evidence, graph, protein instance and history
  accessed_at: '2026-10-21T09:00:57Z'
  support: partial
  summary: Environmental arsenic tolerance is the intended trait. The record presents
    one mechanistic branch anchored to a CH34 protein example; schema validity and
    taxon matching do not by themselves prove that branch experimentally.
  snapshot_sha256: b7c4c9ee1b352e7194421d11f8ed653d6ff01f58ea29bd934f069632071bb320
- evidence_id: shape
  kind: validation
  reference: Whole graph and history inspection
  locator: Thirteen nodes, twelve edges, one protein example and nine events
  accessed_at: '2026-10-21T08:54:19Z'
  support: supports
  summary: All endpoints resolve, all nine events disclose AI assistance, and no pathway-context
    link is asserted.
  snapshot_sha256: a7da5c12f809df389f76ed4345a1f51a6c046fa2c7a6c2b165a73312a54bd7ae
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml
  locator: Semantic grounding versus protein instances; protein version metadata
  accessed_at: '2026-10-21T09:00:57Z'
  support: supports
  summary: A taxon-paired instance is distinct from a family node. Label-only family
    decisions are allowed; each experimental claim still needs appropriately scoped
    source evidence. Entry and sequence versions explicitly describe the retrieval-time
    snapshot, not a promise that the external database never changes.
- evidence_id: provenance
  kind: search
  reference: Target events and bounded local history/mapping/writer/review search
  locator: Nine AI-assisted events; ignored-inclusive exact identifier/path/label
    search
  accessed_at: '2026-10-21T08:54:19Z'
  support: partial
  summary: No explicit local link to human scientific acceptance was identified in
    the inspected scope. AI-assisted promotion to REVIEWED and subsequent automated
    integrity checks do not establish human acceptance; unsearched remote/private
    acceptance remains unknown.
  snapshot_sha256: 61ec9f8bab2dd77839a8b9725eaa1e8bba0e1f5dd5f9ccbfc0545dd01e32a21b
  search_scope: rg --no-ignore --hidden over history,mappings,scripts,reviews/structured
    for traitmech000017, exact path and arsenic_tolerant/arsenic tolerant; command
    and269matching lines retained. Whole target history read; remote/private sources
    remain outside scope.
- evidence_id: status-rule
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md
  locator: Status/audit and human acceptance gate
  accessed_at: '2026-10-21T09:00:57Z'
  support: supports
  summary: REVIEWED requires human scientific acceptance. An AI-authored history event
    and a valid review bundle do not supply it.
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api; p_putida/precise321
  locator: Official KT2440 dataset metadata; eight bounded searches and three selected
    gene-membership responses
  accessed_at: '2026-10-21T08:56:19Z'
  support: context_only
  summary: The cited P. putida paper and dataset explicitly identify KT2440. No Cupriavidus
    dataset matches. Search results include annotations but no directly matching module;
    three selected genes each have zero positive membership flags across84returned
    rows. These computational observations do not establish absent expression/function,
    mechanism or tolerance. They are not transferred to CH34 or BS1.
  snapshot_sha256: 23e7deada3fef845cdec178dc4773dd2bbebfdb9f98686bf85f25f55e445b1d2
- evidence_id: runner
  kind: search
  reference: Structured-source runner discovery
  locator: Original ignored-inclusive08:17:15Z search, hash-verified reuse
  accessed_at: '2026-10-21T08:17:15Z'
  support: context_only
  summary: The structured runner was unavailable within the original bounds; official
    API fallback supplied current KT2440 context. Original catalog07:36:12Z and runner
    receipts are retained without claiming fresh/global absence.
  snapshot_sha256: 39b52930f52e898f85ac3bbb88f11ac674a355967b5704e2b62f0bda259d404f
  search_scope: Original PATH/project/install/B4 roots, including hidden/ignored and
    virtual-environment contents, are specified in the receipt; only Git internals
    excluded. Unsearched directories remain unknown.
- evidence_id: identity
  kind: authority
  reference: Pinned data/raw/metpo.owl; proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv;
    parent traitmech000012
  locator: Complete pinned METPO scan and proposal rows19/14
  accessed_at: '2026-10-21T08:53:45Z'
  support: supports
  summary: No active exact arsenic-tolerance term was found in the pinned ontology,
    including the complete ignored-file-independent OWL inspection. The local v5 proposed1007616
    is not minted upstream in that snapshot. Preserve the accepted traitmech fallback.
    Metal tolerance explicitly includes metalloids and is strictly broader.
  snapshot_sha256: 384c55d51a1db2202ceaa8392b9a61616912c86f3c684111464e95d444dbb543
- evidence_id: live-grounding
  kind: authority
  reference: Official ChEBI29242/29125; QuickGO GO0030001; NCBI taxa119219/303/266264
  locator: Live identity responses08:54:06–07Z
  accessed_at: '2026-10-21T08:54:07Z'
  support: partial
  summary: CHEBI29242 is arsenite(1−), conflicting with the node’s arsenite(3−) label.
    CHEBI29125 agrees with arsenate(3−). GO0030001 denotes general metal-ion transport
    rather than exact arsenite export. All three current taxon labels match. GO is
    a valid biological process; its problem here is semantic specificity.
  snapshot_sha256: d412f68feda54fe4eb5cadcb5a71f9bbfbe62d562f7c161a419babccd6c1317b
- evidence_id: protein
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q1LRL1.json; https://rest.uniprot.org/proteomes/UP000002429.json
  locator: Current primary accession08:54:07Z and reference proteome08:55:33Z
  accessed_at: '2026-10-21T08:56:51Z'
  support: partial
  summary: Primary Q1LRL1, unreviewed status, arsC1/Rmet_0329, CH34 taxon266264 and
    proteomeUP000002429 all match. Current entry100/sequence1 is later than stored99/1.
    Protein existence is inferred from homology and the linked paper is large-scale
    genomic sequencing; metadata alone does not establish a protein-specific experiment.
  snapshot_sha256: b0d7a6fcd56571cb48ef4404f4cdb8b1822bfa5ee7a0d3973ac9a39510a88fca
- evidence_id: archive
  kind: database
  reference: https://rest.uniprot.org/unisave/Q1LRL1?format=txt&versions=99
  locator: UniSave version99, retrieved08:54:43–44Z
  accessed_at: '2026-10-21T08:54:44Z'
  support: supports
  summary: Archived entry99 is dated08-OCT-2025 and matches primary accession, gene,
    strain, proteome, unreviewed status and sequence1. The current100 update occurred2026-09-02,
    after the record’s declared2026-08-25 retrieval. This is consistent with the historical
    metadata, without independently re-observing that past retrieval.
  snapshot_sha256: 36470f62164551ec51001bf1ad5b9fa98f2ba87ff1abc68e4afdc9c3aa019ec3
- evidence_id: ledger
  kind: validation
  reference: Complete independent grounding/endpoint ledger
  locator: All thirteen nodes and twelve edges
  accessed_at: '2026-10-21T08:56:51Z'
  support: partial
  summary: Two node groundings conflict with their exact labels/concepts. No formal
    current relation endpoint conflict was confirmed. Promoter typing and gene/operon
    metadata are already appropriate; label-only family nodes and optional predicate
    IDs are allowed.
  snapshot_sha256: fe23bf62a38e9f5ac13b2f4953770e34341cd3bfe9f0d3305fced9f1d36e7ba7
- evidence_id: relations
  kind: authority
  reference: RO0002327 and RO0002234; local v8/v9 proposal tables
  locator: Executor/process, process/output and proposed challenges/mitigates/reduces
    roles
  accessed_at: '2026-10-21T08:54:03Z'
  support: supports
  summary: The current grounded relations fit their documented broad endpoint roles.
    RO enables authority is reused from07:58:06Z; has-output authority was inspected08:54:03Z.
    Historical microbe-domain defects have already been migrated and are not reported
    as current errors.
  snapshot_sha256: 5948effdcbb1dd9a5a86afc64f3721061b9a9a0c755d7f74ae2da635f1d8b388
- evidence_id: owners
  kind: search
  reference: mappings/node_grounding.tsv; scripts/ground_causal_nodes.py; scripts,src,proposals
  locator: Ignored-inclusive literal label/identifier search and populated-ID handling
  accessed_at: '2026-10-21T08:57:13Z'
  support: partial
  summary: No current matching row/literal for the two problematic groundings was
    found in the declared owner-search bounds. The maintained writer skips populated
    IDs. Correct the target through guarded curation; there is no evidence that clearing
    an ID would regenerate the same value from the present table. This is not a claim
    that historical owners never existed.
  snapshot_sha256: e3b56abf8a6da8fbf4c8b25e2dde86f3ca2fc045cfa3493ba59d54774ed94a77
  search_scope: Ignored-inclusive, hidden, case-insensitive literal searches across
    mappings,scripts,src,proposals for both problematic labels and IDs; exact commands/results
    retained. Earlier wider search also covered data/traits. Unsearched history is
    not declared absent.
- evidence_id: bibliography
  kind: database
  reference: Primary-source identity and claim ledger
  locator: Eight references, twenty citation placements, three excerpts, all nodes/edges
  accessed_at: '2026-10-21T08:58:38Z'
  support: partial
  summary: Eight identities resolve. Seven article bodies and one complete indexed
    abstract were inspected. One excerpt is exact, one differs only by micro-unit
    typography, and the protein-anchor phrase was not found in the retrieved complete
    article text. Seventeen access attempts produced sixteen hashed acquisitions including
    a supplement; publisher403 is not evidence.
  snapshot_sha256: da6c4644d5c36d92a86bb8db97e7426ec7221a6a1dd82c385c40eaead619c0d5
- evidence_id: review-source
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2018.02473
  locator: PMID30405552, PMC6205960; The ars Operons body4/9/11/12; Distribution19;
    Additional Genes24–25
  accessed_at: '2026-10-21T08:55:35Z'
  support: supports
  summary: The review supports the broad resistance synthesis, common ars systems,
    exact ArsB extrusion quotation and alternative exporters. It does not make ArsB
    universal. Its soil KT2440 context corroborates the canonical note; general resistance
    remains distinct from a numerical assay threshold.
  snapshot_sha256: 10e2f5cdf5c207f7e422a4af9a45159ac96621aa13235fa611c46ae9cdc1b926
- evidence_id: bs1
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2020.00047
  locator: PMID32117100, PMC7019866; ResultsS3.SS1/body11, Table1, S3.SS12/body41
  accessed_at: '2026-10-21T08:55:31Z'
  support: partial
  summary: BS1 arsenite MIC3.5mM is exact; the excerpt’s uM/μM typography does not
    change its value. MIC is an inhibitory endpoint, not demonstrated growth at that
    concentration or a measured intracellular pool. The later gene inventory supports
    ArsC annotation but does not directly state/test the reduction reaction at edge11.
    Other already-cited sources explicitly supply that reaction.
  snapshot_sha256: 64d52eb8778d5b00a469f8d82deeeeb5d3a0102de2faa89badc5d55f7e72db81
- evidence_id: ars
  kind: primary_source
  reference: https://doi.org/10.3390/antibiotics12091474
  locator: PMID37760770, PMC10525130; Section2.2 Arsenic/body30
  accessed_at: '2026-10-21T08:55:30Z'
  support: supports
  summary: The inspected review paragraph directly supports existing generic ArsR
    promoter binding, ArsC reduction and ArsB export claims. It is review-level support
    across configurations, not an assay of the named CH34 accession. An awkward neighboring
    regulatory sentence was not used to infer a new route or silently override the
    separately cited regulation source.
  snapshot_sha256: f06974481fe82e6cb9502f52488ad5204e2f710818efc25cab08743f993dcdfa
- evidence_id: regulation
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2024.1494872
  locator: PMID39640857, PMC11617546; Section2/body4
  accessed_at: '2026-10-21T08:55:30Z'
  support: supports
  summary: The environmental bioreporter mini-review directly states the existing
    arsenite/ArsR conformational derepression claim in its background. The assessment
    verifies attribution only and supplies no design, optimization or universal operon
    configuration.
  snapshot_sha256: c09b53f6ec72dc3e0266609c36164f272a96fba341b512668c6db2cf17aa7af5
- evidence_id: acr3
  kind: primary_source
  reference: https://doi.org/10.3390/microorganisms12010074
  locator: PMID38257901, PMC10820871; Section3.2/body18
  accessed_at: '2026-10-21T08:55:31Z'
  support: supports
  summary: The nearest review supports Acr3 as an alternative inorganic arsenic exporter
    in some microorganisms. The separately cited2018 review corroborates arsenite
    specificity. No universal exporter or specific protein instance is inferred.
  snapshot_sha256: 865ecd03285d453eefa5c05b1af9eb11fa2d92d594fb1b897d6e869c38b9192c
- evidence_id: arsm
  kind: primary_source
  reference: https://doi.org/10.7717/peerj.18383
  locator: PMID39494289, PMC11531259; Introductionsec1/body3, Discussionsec16/body37,
    Conclusionssec17/body41
  accessed_at: '2026-10-21T08:55:35Z'
  support: partial
  summary: Source background supports the generic methylation/volatile-endpoint route.
    The agricultural-soil study proposes cooperation from metagenomic distributions;
    it did not measure intracellular depletion or individual-cell tolerance. This
    evidence-tier limit does not make the contextual route false or a universal assertion.
  snapshot_sha256: e80b4e4a3d59afdc5c57c7240339f0ebac05a146daa9a950d1989b4bb4ee494f
- evidence_id: ch34
  kind: primary_source
  reference: https://doi.org/10.1371/journal.pone.0010433
  locator: PMID20463976, PMC2864759; Abstract, Results s2f/body52, Table5 arsPHC1BC2IRM
    row, ref94
  accessed_at: '2026-10-21T08:55:43Z'
  support: partial
  summary: The genome/manual-annotation study supports CH34 tolerance, family-level
    ArsC reduction/efflux and an explicitly active ars cluster. Those observations
    do not by themselves identify a Q1LRL1-specific experiment. The recorded anchor
    phrase is not verbatim text in the complete retrieved article XML, including tables/references;
    this is not a global literature-absence claim.
  snapshot_sha256: bc3ff60f3133a5ec3ac949d7f319d52401370ffaa038d9c498d330529cccd821
- evidence_id: ch34-supplement
  kind: primary_source
  reference: https://journals.plos.org/plosone/article/file?type=supplementary&id=10.1371/journal.pone.0010433.s010
  locator: TableS2 caption and embedded spreadsheet cell strings
  accessed_at: '2026-10-21T08:57:05Z'
  support: context_only
  summary: Downloaded TableS2 supplies gene-cluster annotation-comparison context.
    Embedded strings were inspected, but the workbook was not exhaustively parsed;
    no exhaustive quotation or experiment absence across all supplements is claimed.
  snapshot_sha256: 0b5a0ea997744698b749daa3373810ed9c998bff29175f31b2502c338a84f577
- evidence_id: putida
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/25646541/
  locator: DOI10.1111/1758-2229.12167; title and complete abstract
  accessed_at: '2026-10-21T08:55:28Z'
  support: supports
  summary: The primary study identifies KT2440 and supports arsenite/arsenate tolerance,
    acknowledging strain differences. It establishes an example within P. putida,
    not equal resistance in every strain or every metal. The publisher body returned403;
    source use remains abstract-limited.
  snapshot_sha256: 8098b05f99fcfd304e17e501c8b33e6ff6fe73559a8de30a3862a3287571387d
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: fallback, synonyms, polarity and hierarchy'
  outcome: supported
  target_ids:
  - traitmech:000017
  summary: The accepted traitmech identifier is appropriate against the complete pinned
    METPO scan. Arsenic resistance is a related synonym, and the broader metal/metalloid-tolerance
    parent includes this narrower phenotype. The local proposal is not treated as
    a minted upstream identity.
  evidence_ids:
  - identity
  - record
  - review-source
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: broad growth capability and typical mechanism'
  outcome: supported
  target_ids:
  - traitmech:000017
  summary: The definition is a reasonable synthesis of the cited resistance review.
    Typical ars-associated export is supported, while the graph and source preserve
    alternative exporters; neither a universal ArsB requirement nor an exact concentration
    threshold is asserted.
  evidence_ids:
  - review-source
  - record
  - acr3
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: three organism examples and one accession'
  outcome: concern
  target_ids:
  - traitmech:000017
  summary: CH34 supports a resistant member of C. metallidurans and a family/cluster-level
    reduction branch. KT2440 supplies the actual P. putida source context. Q1LRL1
    identity is valid, but accession-specific experimental support is not established
    by the cited genome text and homology annotation alone.
  evidence_ids:
  - ch34
  - putida
  - protein
  - archive
  - live-grounding
  - review-source
- assessment_id: model
  area: representation
  topic: 'Native checklist: environmental class and MECHANISTIC evidence tier'
  outcome: concern
  target_ids:
  - traitmech:000017
  summary: ENVIRONMENT/CLASS fits. The scoped graph does not claim every branch is
    universal, and the native taxon/protein coverage gate passes. Its stronger experimentally
    supported anchor wording nevertheless needs evidence that is distinguishable from
    family background and cluster annotation.
  evidence_ids:
  - record
  - policy
  - ch34
  - protein
  - check-corpus-protein-taxa
- assessment_id: grounding
  area: grounding
  topic: 'Native checklist: all node identities and external terms'
  outcome: concern
  target_ids:
  - traitmech:000017
  summary: The arsenite charge-state label disagrees with its CHEBI term, and general
    metal-ion transport is not an exact grounding for arsenite export. Arsenate identity
    and all taxonomy match. No arbitrary protein accession replacement or inferred
    physiological protonation state is proposed.
  evidence_ids:
  - live-grounding
  - ledger
  - identity
  - owners
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: twelve edge directions and endpoint roles'
  outcome: supported
  target_ids:
  - traitmech:000017
  summary: Current RO executor/process and process/output pairs and proposed METPO
    challenge/mitigation/reduction pairs have compatible roles. Promoter is correctly
    typed as a genetic element; gene symbols and operon metadata do not make the protein-module
    node an operon-as-protein error.
  evidence_ids:
  - relations
  - ledger
  - record
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: eight references, three excerpts and nearest support'
  outcome: concern
  target_ids:
  - traitmech:000017
  summary: Most existing family-level claims have direct review/background support.
    The CH34 anchor phrase is unverified as a quotation, and edge11 uses a gene-inventory
    citation where other already-cited passages explicitly state the reaction. The
    MIC value is correct as an inhibitory endpoint; the PeerJ study’s own data remain
    genomic rather than a cellular depletion assay.
  evidence_ids:
  - bibliography
  - review-source
  - bs1
  - ars
  - regulation
  - acr3
  - arsm
  - ch34
- assessment_id: protein-history
  area: provenance
  topic: 'Native checklist: retrieval-time metadata versus current audit'
  outcome: supported
  target_ids:
  - traitmech:000017
  summary: Archived Q1LRL1 version99 matches the stored snapshot, including sequence1,
    primary accession, strain and proteome. The native live audit correctly reports
    later version100 drift. That result is retained as a failed freshness check without
    inventing an original metadata error or treating unreviewed status alone as forbidden.
  evidence_ids:
  - archive
  - protein
  - policy
  - check-corpus-uniprot
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: source-matched KT2440 computational context'
  outcome: supported
  target_ids:
  - traitmech:000017
  summary: The exact cited strain matches p_putida/precise321. Eight searches and
    three selected gene memberships supply bounded annotation context without a directly
    matching module or positive inspected membership. No absent-function inference
    or transfer to Cupriavidus follows.
  evidence_ids:
  - expression
  - runner
  - putida
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: required structure and optional surfaces'
  outcome: supported
  target_ids:
  - traitmech:000017
  summary: All thirteen nodes and twelve edges resolve; the graph has an appropriately
    paired instance structurally. Optional datasets and additional protein examples
    are not automatically required. Existing research is a provenance lead, not independent
    evidence.
  evidence_ids:
  - shape
  - record
  - policy
  - check-corpus-protein-taxa
- assessment_id: audit
  area: provenance
  topic: 'Native checklist: nine AI events, human acceptance and ownership'
  outcome: concern
  target_ids:
  - traitmech:000017
  summary: All nine events explicitly disclose AI assistance. Human acceptance was
    not linked within the declared local bounds. The two node groundings need guarded
    record correction; the current mapping search does not establish an automatic
    recurrence owner.
  evidence_ids:
  - provenance
  - status-rule
  - owners
  - shape
findings:
- finding_id: node-grounding-semantics
  issue_key: arsenic-tolerant-node-grounding-semantics
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two node groundings do not denote their stated concepts
  description: Node1 is labelled arsenite(3−), but CHEBI29242 currently denotes arsenite(1−).
    Node3 asserts arsenite transmembrane export while GO0030001 denotes general metal-ion
    transport. The GO term has the correct broad biological-process aspect, but is
    not an exact semantic grounding. Reconcile intended entities without guessing
    physiological speciation or minting an unsupported replacement.
  target_ids:
  - traitmech:000017
  field_paths:
  - causal_graphs[0].nodes[1]
  - causal_graphs[0].nodes[3]
  evidence_ids:
  - live-grounding
  - ledger
  - owners
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/arsenic_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: anchor-quotation
  issue_key: arsenic-tolerant-anchor-quotation
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The protein-anchor snippet is not verified verbatim
  description: The recorded phrase does not occur in the complete retrieved CH34 article
    XML, including tables and references, although it is a plausible descriptive summary
    of the source. Move interpretation to notes or supply a short verified excerpt.
    The supplementary workbook was not exhaustively parsed, so this is not an absence
    claim across every supplement or the literature.
  target_ids:
  - traitmech:000017
  field_paths:
  - causal_graphs[0].nodes[7].protein_examples[0].evidence[0].snippet
  evidence_ids:
  - ch34
  - ch34-supplement
  - bibliography
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/arsenic_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: nearest-reaction-evidence
  issue_key: arsenic-tolerant-nearest-reaction-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The reduction edge cites gene-inventory evidence
  description: Edge11 cites the BS1 genome study with only a graph-wiring note. Its
    inspected nearest passage lists predicted arsenic-related genes; the represented
    reduction reaction is directly described by other sources already cited in the
    record. Attach direct reaction support to this edge while retaining genomic annotation
    in its proper role. This is evidence-placement precision, not false chemistry.
  target_ids:
  - traitmech:000017
  field_paths:
  - causal_graphs[0].edges[11].evidence
  evidence_ids:
  - bs1
  - ars
  - ch34
  - review-source
  - bibliography
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/arsenic_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: arsenic-tolerant-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human scientific acceptance is not linked locally
  description: All nine record events disclose AI assistance, including the promotion
    to REVIEWED. No explicit human acceptance identifying this revision was found
    in the ignored-inclusive declared local scope. Private or remote acceptance remains
    unknown; native validation and this new agent review are not human sign-off.
  target_ids:
  - traitmech:000017
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - status-rule
  - shape
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/arsenic_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: experimental-anchor-certainty
  issue_key: arsenic-tolerant-experimental-anchor-certainty
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: The claimed experimental protein anchor is not established by the cited evidence
  description: 'The scope note presents the taxon-paired Q1LRL1 example as anchoring
    an experimentally supported branch. The inspected genome paper supports ArsC-family
    reduction and explicitly marks a CH34 ars cluster containing C1 and C2 active,
    while the accession annotation is based on homology/genomic sequence. These sources
    do not identify the accession-specific experiment that would substantiate the
    stronger anchor wording. The concern is provisional and bounded to inspected evidence:
    CH34 functional support is present, the protein is not shown to be wrong or nonfunctional,
    and no literature-wide absence is asserted.'
  target_ids:
  - traitmech:000017
  field_paths:
  - causal_graphs[0].scope_notes
  - causal_graphs[0].nodes[7].protein_examples[0]
  evidence_ids:
  - ch34
  - ch34-supplement
  - protein
  - archive
  - policy
  - bibliography
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/arsenic_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major because the unresolved evidence tier affects the record’s
    explicit experimental justification for its mechanistic anchor; provisional because
    family/active-cluster support exists and uninspected experimental literature may
    resolve the accession-specific claim.
actions:
- action_id: repair-grounding
  description: In separately authorized curation, reconcile the intended arsenite
    species and export concept with exact node labels/groundings.
  finding_ids:
  - node-grounding-semantics
  target_ids:
  - traitmech:000017
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/arsenic_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The arsenite label and selected ChEBI identity agree without assuming an unsupported
    protonation state.
  - The transport grounding denotes the intended exact process; a nearby broader GO
    term is not presented as exact.
  - The existing node writer skips populated IDs. Use guarded record correction and
    review the maintained mapping only if a supported reusable mapping is added.
  - Run focused strict/term/graph checks and just qc, preserve native curation/history
    and regenerate affected products after authorized edits.
- action_id: repair-snippet
  description: Replace the descriptive anchor phrase with a short verified quotation
    or move it into interpretation notes.
  finding_ids:
  - anchor-quotation
  target_ids:
  - traitmech:000017
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/arsenic_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The excerpt has an exact inspected source location and remains distinct from interpretation.
  - Run the focused snippet check and manual full-text verification; abstract absence
    alone is inconclusive.
- action_id: place-reaction-evidence
  description: Attach already-supported reaction evidence to edge11 and retain the
    BS1 genome reference only for the claim it establishes.
  finding_ids:
  - nearest-reaction-evidence
  target_ids:
  - traitmech:000017
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/arsenic_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The edge’s nearest evidence explicitly supports the represented reaction.
  - Do not promote genome annotation into a new protein-specific experiment.
  - Run focused record and evidence validation after authorized changes.
- action_id: link-acceptance
  description: Locate and link existing human scientific acceptance or obtain it through
    the established process, preserving all AI provenance.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - traitmech:000017
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/arsenic_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies this record revision and scientific scope.
  - If acceptance remains unavailable, reassess native status without misrepresenting
    automated checks as sign-off.
- action_id: substantiate-or-qualify-anchor
  description: 'Resolve the accession-specific evidence tier: link the experiment
    supporting the stated anchor if available, or qualify the scope and example to
    the family/cluster-level evidence actually established.'
  finding_ids:
  - experimental-anchor-certainty
  target_ids:
  - traitmech:000017
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/arsenic_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The relationship between the named protein instance, source organism and claimed
    experimental branch is explicit and source-backed.
  - Preserve the verified active CH34 cluster and family-level function; do not declare
    the protein nonfunctional or discard valid identity merely because its database
    status is unreviewed.
  - A supported qualification is an acceptable resolution; no new experimental design
    or expanded mechanism is required.
  - Reassess native graph scope only as warranted by the documented evidence, then
    run protein/taxon coverage, focused validation and just qc after authorized curation.
limitations:
- The experimental-anchor finding is provisional. The CH34 source explicitly supports
  an active ars cluster and family-level reduction/efflux; it does not by itself identify
  a Q1LRL1-specific experiment. This is not evidence that the protein is wrong/nonfunctional
  or that no such experiment exists elsewhere.
- The complete retrieved CH34 article XML was searched for the anchor phrase. The
  supplementary XLS was downloaded and embedded strings inspected, but the workbook
  was not exhaustively parsed; no all-supplement absence claim is made.
- The P. putida primary study was assessed through its complete abstract because publisher
  body access returned403. Its actual strain is KT2440; species-level exemplar naming
  does not establish equal tolerance in all strains.
- The BS1 value3.5mM is a correct MIC under the source assay. The record already identifies
  it as MIC; no separate growth-at-MIC falsehood finding is made. It is not a cytoplasmic
  concentration measurement.
- The PeerJ methylation route is supported as literature background. Its own metagenomic
  study proposes community cooperation and does not measure intracellular depletion;
  no new false-route finding is inferred from that limitation.
- The live UniProt command returned1 for110current entry-version mismatches across
  the corpus. This target differs at99versus100 only. Archived99 is consistent with
  the recorded retrieval snapshot and schema semantics; the historical retrieval itself
  was not re-observed.
- The initial category-directory UniProt invocation returned0while inspecting zero
  nodes because of its native category/file glob. It supplies no target coverage and
  is retained separately from the subsequent full-corpus audit.
- GO0030001 is a valid biological process. The finding concerns exact transport semantics,
  not an invalid aspect or a claimed reasoner failure. CHEBI charge reconciliation
  does not prescribe unsupported physiological speciation.
- Expression context covers one exact KT2440 dataset, eight bounded searches and three
  selected gene memberships. Zero positive membership flags are not evidence of absent
  expression, function or tolerance, and no result was transferred to Cupriavidus.
- Unreviewed protein instances are permitted by the native model; valid identity/status/proteome
  metadata do not substitute for primary experimental evidence.
- Common corpus checks retain original executions and reuse verification. Fresh protein/taxon
  and UniProt audits are reported with their actual broader scope, including failures.
- Human acceptance remains unknown outside the bounded ignored-inclusive local search.
- Existing provider research supplied provenance/leads only. No paid call, record/status/history/mapping/schema
  change, generated-page edit or experimental optimization was performed.
notes:
- Field indices are zero-based.
- Initial capture08:53:09–10Z retained53inputs; supplemental capture08:55:03–04Z retainedall53unchanged
  and addedtwo native audit implementation files.
- 'Review validation is separate from scientific/native-audit verdict: the UniProt
  freshness failure is retained rather than hidden.'
tags:
- record-review
- arsenic-tolerant
- environment
- needs-curation
```
