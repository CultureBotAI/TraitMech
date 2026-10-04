# Rheotropism: METPO Proposal v477

## Context

TraitMech adds `traitmech:000600 rheotropism`, a PROPOSED PHYSIOLOGY
class for flow-directed growth, distinct from locomotory rheotaxis.
The pre-change corpus contains 994 records. A fresh temporary METPO seed
emits 399 identifiers: 344 present and 55 absent. Joining the frozen
release-review table classifies those absences as 38 supporting-field
terms and 17 duplicates; all 38 former no-demand classes are now present.
The seed is not a missing-work queue.

Structured review of the pinned 12,617-triple ontology found no exact
flow-directed growth term. Whole-repository searches included ignored and
hidden files, candidate labels and variants, slugs, citations, research,
history and proposals. No exact record, proposal or unresolved mention
was found. Rheotaxis, chemotropism, thigmotropism, phototropism and
gravitropism were checked as distinct neighbors; no older record needs
repair. Open TraitMech PRs do not overlap this work, and an all-state
METPO issue search found no rheotropism or anemotropism proposal.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One record uses the local identity. No source column, sequence feature,
protein, pathway or chemical-use pair is promoted to a primary trait.

## Hierarchy And Boundaries

The parent resolves at `https://w3id.org/metpo/1000059`, phenotype,
under `METPO:1000188 quality`. Growth orientation does not require
locomotion, so `motile` is not the parent. The class is polarity-neutral
and covers liquid and gaseous flows without requiring all contexts in
one organism. Initial outgrowth localization and later tip reorientation
are separate readouts. Passive displacement and growth rate alone are
insufficient; the definition does not require a particular sensor.

No synonyms, xrefs, SSSOM mappings, canonical examples or causal graph
are asserted. Two OPEN discussions retain scope/mapping questions and
mechanism/strain-provenance gaps. Human curator signoff is required before
promotion from PROPOSED. The protected `spore_germination` record is unchanged.

## Evidence And Access

- DOI:10.1016/S0006-3495(65)86719-4 (PMID:19431336): downstream
  Botrytis growth evidence. The complete 19-page author-hosted
  [PDF](https://mterasaki.us/cellbio/lfjaffe/reprints/65bj2.pdf) was read;
  Figures 3 and 4 and Tables VI and VII were visually inspected.
  Molecular identity remains unresolved. SHA256:
  `34b4b52cc7f2ec846d09096a30cd70619434016277ff701e31228d7d064c8bae`.
- DOI:10.1016/S0168-1656(97)00147-8 (PMID:9470224): primary liquid-flow
  hyphal-growth study. Authoritative PubMed and Europe PMC abstracts
  inspected; full text and figures were not verified.
- DOI:10.1007/BF00397538 (PMID:24258181): primary wind-response study.
  Authoritative PubMed and Europe PMC abstracts inspected; full text and
  figures were not verified. Its ethylene experiment does not establish
  the mechanism of every rheotropic response.

All three snippets exact-match contiguous Europe PMC abstract passages
and contain at most 25 words per source. No natural-strain accession is
inferred from a species name or transferred from another study.
Publisher pages were inaccessible through the browsing tool, and the PMC
1965 article page showed browser verification; those attempts are not
counted as successful full-text access. The independent author-hosted PDF
was openly retrievable. Europe PMC metadata reports no supplements for
these records, not independent verification of subscription supplements.

## ID Space And Files

Reserve `METPO:1055400` in the fresh 1055400-1055499 block after v476's
1055300-1055399 block, disjoint from the CommunityMech reference cohort.
Ignored-and-hidden whole-repository collision searches returned no hits.
The actual identity remains `traitmech:000600`, not a released METPO ID.
Subset: `metpo_traitmech_2026_10`.

| File | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus 2 header rows |
| proposal.md | Reviewer narrative |

Properties and SSSOM files are omitted. Both 11-column header rows match
the live upstream class template, including the three required trailing
directive cells. Use the maintained local ROBOT wrapper with the correct
w3id METPO prefix, not the legacy OBO prefix shown upstream.

## Verification

Seven focused tests pass: scope and source limits, proposal parity,
dry-run/idempotent replay, independent target/proposal drift refusal,
and schema rejection before either output is written. All three snippets
were independently exact-matched against freshly retrieved authoritative
abstracts; the maintained resolver reports 3 VERIFIED.

Full QC passes with no new blocking findings and two existing ENIGMA
license warnings. All 2,002 tests pass with two dependency deprecation
warnings; all 45 focused README/priority/QC artifact tests also pass.
Strict validation covers 995 records without errors. History validation
covers 1,033 records, and the new history passes direct LinkML and link
checks. Products, per-cohort and cross-cohort proposal checks, Biolink
coverage and the local canonical-example audit pass.

ROBOT/ELK adds four lines without unsatisfiable classes. Structured RDF
inspection confirms the real w3id phenotype/quality parent chain and no
legacy OBO-prefix METPO stubs. Desktop/mobile browser checks at 1440px
and 390px pass for the new trait and QC dashboard: three evidence entries,
correct local identifier link, loaded chart, no page errors or document
overflow. Screenshots were inspected.

All 994 older trait pages were checked: 993 change only in corpus-count
and embedding-coverage footers; phenotype also gains its 117th child.
No older source YAML changes. Both configured embedding inputs are absent,
so embeddings were not regenerated. Shared generators match all 139 source
files in the reviewed claw archive. The QC chart was regenerated and is
byte-identical at its rendering precision; dashboard HTML carries the new
995-record and per-slot counts.

Staged whitespace checks pass except for the canonical ROBOT header's
three required trailing empty cells. All other files and non-header TSV
lines are clean. The history sections are exactly
`identity,evidence,discussions`, matching the actual record.

## Upstream And Round Trip

After review, submit the TSV through berkeleybop/metpo or the KG-Microbe
proposal pipeline. After acceptance, refresh the pinned ontology, seed
a temporary tree, migrate to the accepted CURIE, preserve local-ID
traceability, and reconcile references and proposal status in a reviewed
change. No separate upstream issue is used in place of this proposal.

## Change Log

- v477, 2026-10-04: add flow-directed growth with three primary studies,
  qualified source access and explicit mechanism and exemplar limits.
