---
name: add-uniprot-protein-examples
description: Audit and add source-backed UniProt protein examples on TraitMech GENE_OR_PROTEIN
  causal nodes, preserving taxon-agnostic identities and the guarded writer.
---

# TraitMech UniProt protein examples

Read [grounding policy](../../../docs/GROUNDING_POLICY.md),
[the schema](../../../src/traitmech/schema/traitmech.yaml),
[exclusions](../../../DO_NOT_WORK.md), and the existing target's entire graph.
Do not touch excluded records. Inventory `data/traits/**/*.yaml`, including every
`causal_graphs[].nodes[]` with `node_type: GENE_OR_PROTEIN`.
Preserve justified `NONMECHANISTIC` graph scopes and reviewed label-only
dispositions; contextual families do not need token protein examples.

Keep node `grounding` taxon-agnostic (GO/InterPro/NCBIfam/complex). Store organism
instances only in `protein_examples`; never replace the node grounding with
UniProtKB. Follow the current `ProteinExample` class: `uniprot_id`,
`protein_label`, `taxon_id`, `taxon_label`, `entry_status`, quoted `retrieved_on`,
`role` and primary `evidence` are required. Evidence needs reference, exact
snippet and notes. Use the schema's reviewed/unreviewed enum spelling. Verify
entry/sequence versions when supplied. An unreviewed exact example needs a
live-verifiable `proteome_id` under the grounding policy. The protein's source
taxon need not be a canonical trait exemplar. Explain a subunit role rather than
presenting one accession as an entire complex. Preserve existing justified
examples and their ordering; do not duplicate accessions.

Write a narrowly scoped identity-asserting mutator using
`traitmech.curate.curation_event.record_curation_event` and
`traitmech.validation.write_validated.write_validated_trait`; append actual
repository history through `just new-history`. Inspect the result and run
`just validate-strict <record-path>`, `just validate-history`,
`just validate-products`, `just audit-writers`, relevant graph/snippet checks and
`just qc`. Run `just audit-uniprot` for accession, taxon, versions, proteome and
inactive-entry checks. For a non-clobbering audit output, inspect
`scripts/audit_uniprot_grounding.py --help`; its `--out` chooses a session-specific
report and `--traits-dir` selects a directory, not a single-record flag.
Regenerate current required page/stat outputs through the local workflow.
## Protein identity and evidence

Inspect live UniProt entry metadata or a release-pinned, provenance-verifiable
native snapshot. Check primary accession and active/merged/deleted state,
organism and strain, sequence/isoform, gene/locus mapping and source identity.
Prefer an exact assayed protein over a convenient ortholog. A named gene alone
is not a unique protein match. Keep family, whole complex, individual subunit,
native protein and experimental construct distinct. UniProt identity metadata
supports identity; primary role evidence supports participation in the record's
mechanism. Retain the original accession and an explicit mapping rationale when
resolving a changed identifier. Do not silently substitute species or isoforms.
## Scope and completion

For one target, read the whole maintained record and its generated projection or
components. For a corpus goal, first freeze an inventory of record IDs, paths,
input hashes and applicable graph/protein elements; resume that ledger after an
interruption. Include hidden and ignored inputs when establishing absence.
Classify each target as checked, changed, evidence-limited, excluded, not
applicable or blocked, with reasons and inspected sources. A sample, a provider
report and a validator pass do not establish whole-corpus scientific completion.

Use [curate-yaml-record](../curate-yaml-record/SKILL.md) for the local evidence,
write, history and status contract; this adapter does not replace its managed
method. Record actual agent identity. Preserve scientific status rules and
unrelated edits. Use inspected primary evidence for mechanistic claims and exact
active identifiers for instances; never infer causality from association or
coverage from an empty query. A quotation is source text; interpretation belongs
in the native notes/explanation field.

Save final scientific assessments through
[review-yaml-record](../review-yaml-record/SKILL.md),
[record reviews](../../../docs/record-reviews.md), and the
[local profile](../../../docs/record-review-profile.md), including their native
persistence exceptions. Keep coverage/checkpoint accounting even when a clean
review should not produce a bundle. Unavailable prerequisites remain blocked;
a skipped target is not a completed enrichment. This skill authorizes no paid
provider call by itself.

After a completed goal, follow the user's authorized commit, push/PR,
adversarial review, issue/fix, merge and branch-cleanup sequence under the current
repository guidance. Carry forward existing authorization without asking again.
Use fresh required checks and native merge-queue rules. Verify actual merge and
landed content before deleting that feature branch or starting the next goal.
Only genuine review findings become issues; a no-diff goal needs a documented
no-op receipt rather than an artificial commit.
