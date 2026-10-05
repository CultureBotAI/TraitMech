# Pseudohomothallism: METPO Proposal v489

## Context

Lift `traitmech:000612 pseudohomothallism`, a PROPOSED PHYSIOLOGY class.
Whole-repository novelty searches included ignored and hidden files, labels,
synonyms, citations, graph nodes, discussions, research, proposals, pages and
history. Existing homothallism describes this mechanism but has no exact
synonym or unresolved same-scope node. Heterokaryosis alone does not establish
sexual self-fertility. No exact record was found.

The pinned 12,617-triple METPO graph has no exact term. A fresh 399-record
seed compared with the 1,006-record pre-addition corpus has 344 present and
55 absent IDs. Both frozen release-review tables classify those 55 as
38 supporting-field rows and 17 duplicates, not missing primary traits.
An all-state upstream issue search for pseudohomothallism returned no results
on 2026-10-04. Current open local PRs reserve neither this trait nor its block.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

The local parent is `traitmech:000609 homothallism`: a single sexual spore
carrying compatible nuclei can establish a self-fertile heterokaryotic culture.
This is not heterothallism, mating-type switching, mere nuclear coexistence,
ploidy or MAT-gene content. Do not require exactly two nuclei at every stage,
four spores, a fixed nuclear ratio, one meiotic program, universal
self-fertility or absence of outcrossing.

The standalone template uses released `METPO:1000059 phenotype`, under
`METPO:1000188 quality`, in the pinned ontology's `https://w3id.org/metpo/`
namespace. It deliberately does not create an unlabeled stub for pending
homothallism `METPO:1056300` from v486. Reconcile this narrower parent after
upstream acceptance. This is the same standalone-parent policy used in v478;
the local and proposal parent identifiers are deliberately different.
PHYSIOLOGY is a filesystem category, not an ontology parent. The obsolete
reproduction-process and reproduction-structure classes are unsuitable.

Secondary homothallism and functional heterothallism require lexical review
before exact synonym assignment. No xrefs or SSSOM mappings are asserted.

## Evidence and Limitations

- `DOI:10.5598/imafungus.2015.06.01.13` (`PMID:26203424`, `PMC4500084`):
  terminology review, full section s2b read as raw XML. The 19-word clause
  supports the definition and homothallism parent, not experimental
  replication. Figure 1 remains uninspected. Its packaging description does
  not impose a fixed nuclear count through subsequent development.
- `DOI:10.1093/genetics/143.2.789` (`PMID:8725227`, `PMC1207337`): primary
  study, directly retrieved scientific-abstract opening clause. Self-fertile
  heterokaryons and occasional self-sterile outcrossing strains are distinct.
  Recombination suppression is an association, not the general definition.
  Full text, figures, supplements and original strain provenance remain unread.
- `DOI:10.1002/dvg.1020150111` (`PMID:8187347`): primary comparative cytology,
  directly retrieved scientific-abstract sentence. The abstract explicitly
  truncates at 400 words. First- and second-division programs differ across
  genera; germinating P. anserina spores retain three functional nuclei.
  Established and inferred crossover events are distinguished. Four-spored
  species in this study do not define a universal spore count. Full text,
  original methods, figures and strain provenance remain unread.
- `DOI:10.1371/journal.pgen.1000030` (`PMID:18369449`, `PMC2268244`): primary
  selfed-progeny study. Scientific abstract, Introduction, Results s2b/s2c,
  Methods s4a/s4c/s4d/s4e and actual Table 1 including footnotes were read.
  The snippet is a 16-word Methods s4d clause, not an abstract quote. The
  152 heterokaryotic sexual progeny of selfed P581 are a selected assay set,
  not the frequency among all spores. The separate 83-progeny N. crassa
  introgression experiment is not the native selfing assay. Figures,
  supplements, Discussion and other experimental sections remain uninspected.

The qualified natural canonical example is N. tetrasperma P581 from Lihue,
Hawaii. Table 1 and its Perkins-collection footnote establish provenance at
https://pmc.ncbi.nlm.nih.gov/articles/PMC2268244/; the selfed progeny supply
direct reproductive evidence. Methods s4a specifies synthetic cross medium
at 25 C. FGSC 2508/2509 are isolated homokaryotic components, not identifiers
for the heterokaryon. NCBI efetch resolves `NCBITaxon:40127` to the active
species name on 2026-10-04. No universal strain or life-stage claim is made.

Two CURATION_TODOs preserve lexical, external-mapping and native-protein gaps.
No causal graph is inferred. Keep actual abstract-resolver verdicts separate
from manual full-text matching. PROPOSED status awaits human curator signoff.

## ID Space and Subset

Reserve `METPO:1056600` in `1056600-1056699`, after v488's block.
Ignored-and-hidden searches across TraitMech and CommunityMech proposals,
including the fully read CommunityMech v1 narrative and templates, found no
collision before writing. Subset: `metpo_traitmech_2026_10`.
Local `traitmech:000612` remains the identifier pending acceptance and release.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Scope, evidence and migration |

No property or SSSOM template is needed. The 11-column class template follows
the upstream headers with three trailing empty directive cells. The upstream
contract and both templates were read at Knowledge-Graph-Hub/kg-microbe commit
`ea1c5f15e6c4dba6c72165367162b354e215f018`. Legacy OBO namespace examples
do not override the pinned ontology's w3id IRIs or local verification policy.

## Verification

```bash
just verify-proposal metpo_traitmech_v489
just robot-validate-proposal metpo_traitmech_v489
just audit-proposal-coverage
just qc
```

Check record/template label and definition parity, the deliberate parent
divergence above, and emitted OWL for the released w3id phenotype parent and
quality ancestor. ELK success against an unlabeled legacy stub is insufficient.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` following local
review. A reserved placeholder is not upstream acceptance.

## Round-Trip Plan

After acceptance and release, refresh the pinned ontology, reconcile the
homothallism parent and migrate to the accepted METPO CURIE. Preserve the local
identifier in an explicit migration artifact and append-only history,
regenerate dependent artifacts, and avoid a duplicate primary record.

## Change Log

- v489, 2026-10-04: propose pseudohomothallism with four DOI-backed snippets,
  a qualified natural P581 example and explicit developmental limits.
