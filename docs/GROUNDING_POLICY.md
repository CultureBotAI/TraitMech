# Grounding policy for causal-graph gene/protein nodes

Status: **partly applied.** The retraction and the strict re-grounding pass
in §7 have been run against `data/traits/`. The remaining schema changes in
§4 are still proposals.

This document covers `CausalNode` entries typed `GENE_OR_PROTEIN`, and the
exemplar taxon / genome layer that mechanism claims should hang off. It
combines an audit of the current corpus (reproducible via
`scripts/audit_uniprot_grounding.py`) with a literature/primary-source
review of how comparable resources ground protein entities.

## 1. What the audit found

817 `GENE_OR_PROTEIN` nodes across 353 causal graphs, 663 distinct labels.

| | count | share |
|---|---:|---:|
| Ungrounded (label only) | 596 | 73% |
| Grounded to `UniProtKB:` | 221 | 27% |
| — of which the accession is **deleted from UniProt** | **162** | **73% of grounded** |
| — unreviewed (TrEMBL), still live | 58 | 26% of grounded |
| — reviewed (Swiss-Prot) | 1 | 0.5% of grounded |

Of the 138 distinct accessions in use, **99 are `Inactive`/DELETED** in
UniProt today. 101 trait files contain at least one dead accession.

Two further defects:

- **Accession reuse across unrelated traits.** 37 accessions appear in more
  than one trait file; `UniProtKB:A0A068T423` ("Na+/H+ antiporter") is used
  in 8 halophily/alkaliphily files. One organism's protein was made to stand
  in for a taxon-agnostic family node.
- **The live ones are arbitrary instances.** "nitrogenase" resolves to a
  *Paenibacillus durus* TrEMBL entry, "FtsZ" to *Lacticaseibacillus casei*.
  The mechanism claim is not about those organisms.

The dead accessions are **not automatically recoverable**. UniProt ID-mapping
returns `obsoleteCount: 1` with no replacement, and while UniParc retains the
sequence (e.g. `A0A068T423` → `UPI0004A5079E`) it carries zero active
cross-references. Each affected node must be re-derived from its label.

### Why this happened, and why it will happen again

These groundings came from an automated token-match against a UniProt dump,
picking a representative per label. The root cause is not the matching
heuristic — it is grounding a *family/function* node to a *protein instance*
identifier, then picking that instance from the unreviewed pool.

A re-run of the same idea against current APIs reproduces the failure. Over
all 663 labels, the GO top-hit does not even contain the node label as a
substring in **72%** of cases:

| label | GO top-hit | |
|---|---|---|
| acetate kinase | GO:0008776 acetate kinase activity | correct |
| ATP synthase | GO:1905273 *positive regulation of* proton-transporting ATP synthase activity | wrong |
| catalase | GO:1902553 *positive regulation of* catalase activity | wrong |
| bacterial adhesins | GO:0097347 TAM protein secretion complex | wrong |
| ars operon | GO:0010239 chloroplast mRNA processing | wrong |

**Automated grounding must therefore generate candidates for curator review,
never write directly to the corpus.**

## 2. Policy: match the identifier type to the node's semantics

The core rule from the source review: do not force every `GENE_OR_PROTEIN`
node onto a protein accession. Decide what the node *is* first.

| Node names… | Ground to | Example |
|---|---|---|
| An enzymatic **function**, taxon-agnostic | GO Molecular Function `…activity` | acetate kinase → `GO:0008776` |
| A **multi-subunit complex**, taxon-agnostic | GO Cellular Component `…complex` | nitrogenase complex → `GO:0016610` |
| A **protein family / domain** | InterPro / Pfam / NCBIfam | reverse gyrase → `IPR005736` |
| A specific **complex instance** in one organism | Complex Portal `CPX-…` | E. coli complexes only, in practice |
| A specific **protein instance** in one organism | UniProtKB **reviewed** accession, paired with a taxon | *B. subtilis* DesK → `UniProtKB:O34757` |
| A functional **class** ("virulence factors") | Do not ground to a protein at all — use a GO BP term, or split into concrete nodes | — |

Supporting points from the source review, all verified 3-0 by adversarial
check:

- Only the **primary (citable)** UniProt accession is stable. Accessions get
  demoted to secondary on merge/demerge and deleted outright; a grounding
  slot must be reconcilable against `sec_ac.txt` and the `delac_*` lists.
- **TrEMBL is unsuitable as a canonical anchor.** It carries no per-entry
  curation and is subject to bulk removal — ~50M records purged in 2015, and
  a 2025 policy limiting TrEMBL to reference-proteome sequences is projected
  to cut UniProtKB from ~253M to ~141M entries, executing across releases
  2025_04 → ~2026_02. Deleted TrEMBL entries usually have no forwarding.
  (Note: the `A0A` prefix means accession-space exhaustion, *not* unreviewed
  status — classify by the `entryType` field.)
- GO Consortium policy explicitly hosts **species-agnostic** complexes and
  separates the structural `…complex` CC term from the `…activity` MF term.
  Species-specific complexes belong in Complex Portal or PRO.
- A complex node takes a **complex-level** identifier, never one arbitrary
  subunit's accession.
- **UniRef is not a stable CURIE.** UniProt's own answer to "Are UniRef
  cluster identifiers permanent?" is "No" — the ID derives from the
  representative member, which can change on recomputation.

### The subunit trap

Both candidate routes land on a **subunit** when the node names a complex,
and the returned name is close enough that it reads as correct. Verified
during this audit:

| node label | top hit | what it actually is |
|---|---|---|
| ATP synthase | `IPR000131` | ATP synthase, F1 complex, **gamma subunit** |
| methyl-coenzyme M reductase | `IPR003178` | MCR, **gamma subunit** |
| nitrogenase | `IPR000510` | Nitrogenase/oxidoreductase, component 1 (**domain**) |
| Na+/H+ antiporter | `UniProtKB:Q4L4W4` | Na+/H+-antiporter, **MnhD subunit** |
| catalase | `UniProtKB:P14412` | Catalase-**peroxidase** (bifunctional KatG) |

For these, use the GO CC complex term instead — all verified live and
non-obsolete: nitrogenase complex `GO:0016610`, proton-transporting ATP
synthase complex `GO:0045259`, type III protein secretion system complex
`GO:0030257`. Reserve InterPro for labels that genuinely name a single
protein family (`IPR005736` reverse gyrase, `IPR017402` proteorhodopsin).

Practical caveat: Complex Portal covers ~28 mostly model organisms, with
*E. coli* K-12 the only substantial bacterium. Most TraitMech complexes
(nitrogenase, T3SS variants) have no `CPX` entry and should fall back to a
GO CC complex term or an InterPro/NCBIfam family.

## 3. Exemplar taxa and genomes

The exemplar-taxon slot is `canonical_examples` (`NCBITaxon` CURIE + label)
and it **is** populated: 312 exemplar taxa across 225 of 477 trait files. The
gap is genomes — **no trait file contains a `GCF_`/`GCA_` assembly accession**,
and the schema has no slot for one.

The reproducible anchor is **NCBITaxon ID + a versioned assembly accession**.
The full chain is machine-resolvable today:

```
UP000000625                    UniProt reference proteome (E. coli K-12)
  → taxonId 83333              NCBITaxon
  → GCA_000005845.2            genomeAssembly.assemblyId (ENA/GenBank)
  → GCF_000005845.2            NCBI Datasets `paired_accession` (RefSeq)
```

UniProt surfaces the **GCA_** (GenBank) accession, so reaching a RefSeq
**GCF_** requires the extra NCBI Datasets step. Store the version suffix —
`GCA_000005845.2`, not `GCA_000005845`.

**Do not use GTDB lineage as the identifier.** GTDB reassigns taxa between
releases, and the single best-studied bacterial genome demonstrates it:

| GTDB release | species assigned to `GCF_000005845.2` |
|---|---|
| R80 – R86.2 | `s__Escherichia coli` |
| R89 – R202 | `s__Escherichia flexneri` |
| R207 – R226 | `s__Escherichia coli` |
| **R232** | **`s__G047199095 sp047199095`** |

Across all of that, `NCBITaxon:511145` ("Escherichia coli str. K-12 substr.
MG1655") did not move. If a GTDB lineage is recorded at all it must be
release-pinned and treated as commentary, not as the anchor.

## 4. Proposed schema changes

None of these are applied yet.

1. **Split family-level from instance-level grounding.** The single
   `grounding` slot conflates them. Suggested: keep `grounding` for the
   taxon-agnostic term (GO / InterPro), and add an optional
   `exemplar_protein` group carrying a reviewed `UniProtKB` accession plus
   the `NCBITaxon` it came from — so an instance can never be recorded
   without its organism.
2. **Constrain the prefix.** `grounding` is currently any CURIE-shaped
   string. Restrict `GENE_OR_PROTEIN` groundings to the prefixes above and
   forbid bare TrEMBL accessions.
3. **Add a genome slot** to `canonical_examples`: versioned `GCF_`/`GCA_`
   accession, optional UniProt `UP…` proteome ID, optional release-pinned
   GTDB lineage.
4. **Add a resolvability check** to CI (`scripts/audit_uniprot_grounding.py`
   exits non-zero on deleted accessions) so this cannot silently rot again.

## 5. Suggested remediation sequence

1. **Retract the 162 dead groundings** — demote to label-only rather than
   leaving CURIEs that resolve to nothing. Affects 101 files. *Needs
   approval: it edits curated records.*
2. **Re-ground from `mappings/uniprot_regrounding_candidates.tsv`**, which
   has one row per distinct label with a proposed route and a blank
   `curator_decision` column. Current distribution:

   | proposed route | labels |
   |---|---:|
   | `NO_CANDIDATE` — manual curation needed | 342 |
   | `CLASS_NODE_DO_NOT_GROUND` | 95 |
   | `InterPro_family` | 92 |
   | `REVIEW_GO_SUSPECT` — top-hit failed the substring check | 77 |
   | `SwissProt_exemplar` | 45 |
   | `GO_term` | 12 |

   121 of the 138 currently-grounded labels have a candidate replacement;
   the rest need manual work.
3. **Add genome accessions** to the 312 existing `canonical_examples`
   entries, via the UniProt → NCBI chain in §3.

Only step 2's `SwissProt_exemplar` and `InterPro_family` rows are close to
mechanical, and even those want a curator eye. The 342 `NO_CANDIDATE` labels
are the real work and are not automatable.

## 6. APIs for a batch pass

All verified working during the audit:

- **UniProt REST** — `rest.uniprot.org/uniprotkb/{acc}.json`; deleted entries
  return `entryType: "Inactive"`. `rest.uniprot.org/proteomes/{UP…}.json`
  gives taxon + assembly.
- **UniProt ID-mapping** — async job endpoint; reports `obsoleteCount` but
  does **not** resolve deleted TrEMBL accessions to replacements.
- **OLS4** (`ebi.ac.uk/ols4/api/search?ontology=go`) — usable for GO
  candidates, low top-hit precision (see §1).
- **InterPro** (`ebi.ac.uk/interpro/api/entry/interpro/?search=`).
- **NCBI Datasets v2alpha** — `genome/accession/{GCA}/dataset_report` returns
  `paired_accession` for the GCA→GCF hop.
- **GTDB** (`gtdb-api.ecogenomic.org`) — `/genome/{acc}/taxon-history` gives
  the per-release lineage used in §3.

Serial querying of three APIs across 663 labels takes ~4 hours; at 8-way
concurrency it is ~4 minutes, with no rate-limiting observed. Pin the UniProt
release in any re-grounding run and re-check resolvability afterwards, since
the TrEMBL reduction is executing now.

## 7. What has been applied

Two passes have been run against `data/traits/`. Full corpus validation
(`just validate-strict`, 477 files) and the structural graph audit
(`just audit-graphs`) both report zero errors afterwards.

**Pass 1 — retraction** (`scripts/retract_dead_uniprot_groundings.py --apply`).
Removed 162 `grounding` values whose accessions UniProt reports as `Inactive`,
across 101 files, demoting those nodes to label-only. Each file gained one
`RETRACT_DEAD_UNIPROT_GROUNDINGS` curation event. Verified mechanically that
nothing else changed: for all 101 files, the only semantic differences are the
grounding removals plus the single appended event.

**Pass 2 — strict re-grounding** (`scripts/ground_causal_nodes.py --apply`).
`mappings/node_grounding.tsv` was first rebuilt, because it was the source of
the bad data and still contained every dead accession — re-running the grounder
against it would have restored exactly what pass 1 removed:

| change to `mappings/node_grounding.tsv` | rows |
|---|---:|
| dead accession replaced by a taxon-agnostic GO/InterPro term | 40 |
| dead accession dropped, no replacement available | 68 |
| new GO/InterPro rows for previously unmapped labels | 29 |
| live UniProtKB rows left untouched | 30 |

That grounded 91 nodes across 65 files (71 GO, 20 InterPro).

Net effect on the 817 `GENE_OR_PROTEIN` nodes:

| | before | after |
|---|---:|---:|
| Grounded to something that resolves | 59 | 150 |
| Grounded to a deleted accession | 162 | **0** |
| Ungrounded (label only) | 596 | 667 |

Ungrounded went *up*, which is the intended outcome: 162 nodes that falsely
appeared grounded are now honestly unlabelled, and 91 gained a real term.

### Candidate gate

Only exact matches were applied — an ontology term's own label had to equal the
node label (or the label plus `activity`/`complex`), with hits naming a part
(subunit, domain, conserved site) rejected. That admitted 74 of 666 labels.
Manual inspection of all 74 still caught four errors the automation missed,
which is the argument for keeping the gate strict:

- `rhodopsin` → `IPR000732` is the **animal visual opsin**; overridden to
  `IPR001425` (archaeal/bacterial/fungal rhodopsins).
- `hydrogenase` matched the over-specific `GO:0102220` *hydrogenase activity
  (NAD+, ferredoxin)* only because the normalizer stripped the term's
  parenthetical; normalization is now asymmetric and the match is gone.
- `chemoreceptor`, `cytochrome c`, `ferredoxin` resolved to UBERON/CHEBI/PR
  terms because OLS4 does not reliably honour `ontology=go`; non-GO CURIEs are
  now dropped.
- `NADH dehydrogenase (complex I)` and `methyl-accepting chemotaxis protein
  (MCP)` are ambiguous between an activity and a complex, and are excluded
  pending curation.

The remaining 667 ungrounded nodes are the real curation backlog. Roughly 95
of them are functional classes ("virulence factors", "osmolyte transport and
synthesis genes") that should never receive a protein accession at all — see
§2 — and the rest need a curator, not another automated pass.
