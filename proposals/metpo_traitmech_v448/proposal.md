# METPO Proposal v448: Long Lamassu System

## Context and Scope

One Scope-A class lifts `traitmech:000571`, an organism-level possession
trait for the long-LmuB structural family. Scope B and C have zero rows.
The new record closes the long-family gap on the existing Lamassu parent.
This is neither an isolated protein nor a detector-specific feature row.

## Evidence and Hierarchy

[Haudiquet et al.](https://doi.org/10.1073/pnas.2519643122) distinguish
long and short families through LmuB phylogeny and coiled-coil structure.
The approximate 800-residue LmuB length is descriptive, not a threshold.
Their strain-qualified B. cereus B4077 example belongs to the long family;
the species anchor `NCBITaxon:1396` was independently resolved at NCBI.
No assembly, species-wide possession or native-host phenotype is inferred.

[Dataset S1](https://pmc-oa-opendata.s3.amazonaws.com/PMC12663957.1/pnas.2519643122.sd01.xlsx),
sheet `S3_Lamassu_Detection`, rows 58-60, records a complete computational
Cap4-system call with long LmuB, LmuC and LmuA. The quoted A:C cells were
read in column order with `openpyxl`. Column C is the actual `gene_name`;
column L is a model's `hit_gene_ref`, which can name the long slot even
when an exchangeable short profile matched. This dataset supports locus
architecture, not an experimentally verified phenotype or a sufficient
family-classification rule. The two citation URLs are distinct artifacts
from the same study, not two independent studies.

The class is a sibling of short Lamassu (`traitmech:000570`, v447
`METPO:1052400`) under Lamassu (`traitmech:000232`, v109
`METPO:1018600`). Hydrolase-Protease spans both families, and the legacy
FMO record's table-defined scope and SMEK's exception require separate
reconciliation. None of those whole records is reparented here. No
historical proposal row or identifier changes. Type II is not an exact
synonym; component-number classifications remain discovery leads.

The short Vc-Cap4 mechanism is not generalized to this family. No universal
effector chemistry, LmuC requirement, zinc-hook count or stoichiometry is
asserted. There is no new causal graph or exact external mapping, and no
SSSOM file is needed. The older Millman experimental paper was a research
lead, but its full text could not be retrieved in this session; no new
quote or independent verification claim is attributed to it.

## ID Space and Files

Reserve `METPO:1052500` in the next unused hundred block after v447's
`METPO:1052400`, with subset `metpo_traitmech_2026_10`. Ignored-and-hidden
searches found no collision with local records, METPO or earlier proposals.

| Artifact | Scope | Rows |
|---|---|---:|
| `metpo_proposal_classes_robot.tsv` | A | 1 |
| Property template | B, not applicable | 0 |
| SSSOM mappings | No exact mapping asserted | 0 |

Novelty searches included ignored and hidden files, research, history and
generated artifacts. Existing long-family mentions were evidence or open
discussions, not an exact record. A fresh METPO seed comparison produced
55 exact-ID leads already classified as 17 duplicates and 38 supporting
properties; no missing exact METPO family term was found.

## Verification and Upstream Path

The writer is dry-run-first, validates before writing, and rejects parent,
target or proposal drift. Its parent update preserves unrelated fields
and appends history. Test dry runs, idempotence, scope and drift refusal;
validate the record, both source spans, spreadsheet cells, NCBI identity,
repository history and generated artifacts; run proposal verification,
ROBOT/ELK, full tests and QC before merge.

Submit with [the existing upstream tracker](https://github.com/berkeleybop/metpo/issues/535).
After human review and minting, refresh METPO, replace the temporary local
identifier with the assigned one, and retain the old identifier's provenance.
Bot review does not promote the record from `PROPOSED` to `REVIEWED`.

## Change Log

- v448, 2026-10-03: propose the long-LmuB family with source-exact evidence
  and explicit phenotype, detector and sibling-scope limitations.
