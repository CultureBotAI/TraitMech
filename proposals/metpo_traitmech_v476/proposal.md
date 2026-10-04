# Gravitropism: METPO Proposal v476

## Context

TraitMech adds `traitmech:000599 gravitropism`, a PROPOSED PHYSIOLOGY
class for gravity-directed growth, distinct from swimming orientation,
propulsion-speed change, passive displacement and growth rate alone.

A fresh temporary seed emitted 399 identifiers: 344 present and 55 absent
from the pre-change 993-record corpus. Joining the frozen release review
identifies the absences as 38 supporting-field terms and 17 duplicates;
all 38 former no-demand classes are now represented. That seed is not a
missing-work queue. Structured review of the pinned 12,617-triple OWL
found no exact gravity-directed growth term.

Whole-repository searches included ignored and hidden files, labels,
synonyms, slugs, citations, research, history and proposals. No prior exact
record, node or proposal was found. Gravitaxis, gravikinesis and phototropism
were inspected as distinct neighbors; none needs an older-record repair.
An all-state upstream METPO issue search found no gravitropism/geotropism
proposal, and open TraitMech PRs did not overlap this work.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One record uses the local identity. No gene, domain, protein, source column,
chemical-use pair or workflow enum is promoted to a trait.

## Hierarchy And Boundaries

The pinned ontology resolves phenotype at `https://w3id.org/metpo/1000059`
under `METPO:1000188 quality`. Growth reorientation does not require
locomotion, so motile is not the parent. The definition is polarity-neutral:
it does not require both response directions in any one organism.
The fungal evidence here supports negative gravitropism only.

No unverified synonyms, xrefs, SSSOM mappings or causal graph are added.
Two OPEN discussions retain scope/mapping and mechanistic-grounding work.
Human signoff is needed to promote the record from PROPOSED.

## Evidence And Access

- DOI:10.4161/cib.22291 (PMID:23650568; PMC3642927): fungal growth
  evidence. Full article XML and all three figure images inspected through
  the official Europe PMC service. Figure 1 shows stage I bending after
  tilting, but does not name the wild-type strain. Intracellular changes
  may accompany development, and Figure 3 is a touch experiment.
- DOI:10.1078/0176-1617-01082 (PMID:15266721): primary fungal
  clinostat-centrifuge experiment, authoritative abstract inspected.
  The named NRRL1555 wild-type polar-angle threshold is not the mutant
  or aiming-error threshold and is not made universal. Subscription full
  text and figures were not inspected.
- DOI:10.1007/s004250050744 (PMID:10550622): primary Chara abstract
  explicitly distinguishes positive rhizoid and negative protonematal
  growth. It supports terminology only; no algal mechanism or positive
  fungal response is inferred. Full text and figures were not inspected.

All three snippets exact-match contiguous source spans. The first is from
the body, not the abstract; the others are abstract passages. Europe PMC
indexes the 2013 article with `hasSuppl=N`: its supplementaryFiles download
contains ordinary figure assets, not additional experiments. Publisher PDF
access returned 403, and PMC browser access presented a verification page;
neither is counted as successful full-text retrieval. The independent
[official XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3642927/fullTextXML)
and figure service supplied the inspected material.

Canonical `NCBITaxon:763407` resolves at NCBI to
`Phycomyces blakesleeanus NRRL 1555(-)`, rank strain, parent 4837.
It is tied to the 2004 assay, not the unnamed 2013 wild type.
Natural-isolate provenance was independently checked in Materials and
Methods of DOI:10.1128/EC.00203-13 (PMID:24243797; PMC3910969), which
distinguishes NRRL1555 from backcrossed A56. That provenance is retained
in the example note, not counted as independent gravitropism evidence.

## ID Space And Files

Reserve `METPO:1055300` in the fresh 1055300-1055399 block after v475's
1055200-1055299 block, disjoint from CommunityMech v1. Ignored-and-hidden
collision searches found only an unrelated matplotlib decimal. The live
identity remains `traitmech:000599`; the placeholder is not a released
METPO term. Subset: `metpo_traitmech_2026_10`.

| File | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus 2 header rows |
| proposal.md | Reviewer narrative |

Property and SSSOM files are omitted. The 11-column header matches the live
upstream class template, including its three trailing directive cells.
Use the local ROBOT wrapper's correct w3id METPO prefix, not the legacy
OBO prefix still shown in the upstream skill.

## Verification

Seven focused writer tests pass, covering growth scope, qualified sources,
natural strain assignment, proposal parity, dry-run/replay, independent
record/proposal drift refusal, and schema rejection without partial writes.
All three snippets independently exact-matched the retrieved sources. The
maintained resolver reports two VERIFIED abstracts and one NOT_IN_ABSTRACT
body quote, which was separately verified against full-text XML.

Strict validation covers 994 records without errors; history validation
covers 1,032 records, including the append-only correction below. Products,
per-cohort proposal, Biolink and research
artifact checks pass. ROBOT/ELK adds four lines without unsatisfiable
classes; structured RDF checks confirm the real phenotype/quality chain
and absence of legacy OBO-prefix METPO stubs. The canonical audit resolves
708 examples across 523 records: zero errors and 24 existing label warnings,
none on the new example.

Browser checks at 1440px and 390px pass for the new trait and QC dashboard:
three evidence entries, one canonical example, correct local identifier
link, loaded coverage image, no page errors or document overflow. Screenshots
were inspected. All 993 older trait pages were compared: 992 change only
the corpus-count footer; phenotype also gains its 116th child. No older
source YAML changes. Both configured embedding source paths are absent,
so embedding artifacts were not regenerated. Shared generators used an
isolated reviewed claw source, verified against all 139 source files in
the pinned archive.

Full QC passes with no new blocking findings and two existing ENIGMA
license warnings. All 1,995 tests pass with two dependency deprecation
warnings; all 45 focused artifact tests also pass. Ordinary whitespace
checks pass except for the exact upstream-required three trailing ROBOT
header cells; all non-header TSV lines are clean.
After the provenance-only review correction, all 106 focused writer,
history and skill-frontmatter tests pass. The original history file,
TraitRecord, implementation/tests and generated artifacts are unchanged.

## Upstream And Round Trip

After review, submit the TSV through berkeleybop/metpo or the KG-Microbe
proposal pipeline. After acceptance, refresh the pinned ontology, seed a
temporary tree, migrate to the accepted CURIE, preserve local-ID traceability,
and reconcile references and proposal status in a reviewed change. No separate
upstream issue was opened for this branch.

## Change Log

- v476, 2026-10-04: add gravity-directed growth with source-qualified
  fungal observations, a natural strain exemplar and explicit causal limits.
  Independent review identified incorrect section attribution in the first
  repository history record (#1674): it listed a deferred causal graph and
  omitted discussions. An append-only AUDIT corrects that attribution without
  changing the TraitRecord or rewriting the original history. The add-trait
  scaffold now requires the actual touched sections and explains this
  provenance-only correction workflow. The review's article-type and quote
  location questions were resolved against authoritative full-text XML:
  a brief-report/Short Communication with original microscopy, and the
  quoted sentence under the section already cited in the record.
