# Causal-graph protein and taxon review plan

Date: 2026-08-23

## Objective

Review every TraitMech causal graph and its gene/protein grounding. Every
retained mechanistic graph should contain at least one source-backed protein
node, at least one cited canonical taxon, and at least one UniProt protein
example whose organism matches that canonical taxon.

Taxon-agnostic graph nodes must retain semantic groundings such as GO,
InterPro, or NCBIfam. A UniProt accession represents an organism-specific
protein instance and must therefore be stored as a taxon-paired example, not
as the generic node grounding.

## Baseline

The 2026-08-23 corpus inventory found 353 causal graphs in 353 TraitRecords.

| Cohort | Graphs |
|---|---:|
| Protein node and canonical taxon already present | 199 |
| Protein present; canonical taxon needed | 73 |
| Canonical taxon present; protein needed | 38 |
| Protein and canonical taxon both needed | 43 |

The graphs contain 818 `GENE_OR_PROTEIN` nodes representing 664 distinct
labels. Of those nodes, 81 are GO-grounded, 54 are InterPro-grounded, and 683
are label-only. No generic graph node remains grounded directly to UniProt.

All 353 graph records have tracked Falcon reports. The legacy reports do not
have separate citation sidecars, so reports are discovery inputs rather than
primary evidence. Every claim must be checked against its DOI source. The 331
existing canonical examples all carry references.

## Data model

Add an optional `protein_examples` list to `CausalNode`. Each example should
record:

- a `UniProtKB:` primary accession;
- the current protein label and optional gene symbol;
- `NCBITaxon:` identifier and taxon label;
- reviewed/unreviewed entry status;
- retrieval date and UniProt entry/sequence versions when available;
- the protein's role or complex-component role; and
- evidence containing `reference`, `snippet`, and `notes`.

The declared taxon must equal UniProt's `organism.taxonId` and must occur in
the owning TraitRecord's `canonical_examples`. Reviewed Swiss-Prot entries are
preferred. An unreviewed reference-proteome entry is permitted only when the
identity is exact, the mechanistic source supports that protein in that taxon,
and version/retrieval metadata make the example auditable.

Multi-subunit complex nodes must use a taxon-agnostic complex grounding where
available. Their protein examples must identify explicit components and must
not imply that one subunit accession denotes the whole complex.

## Scope rule

Do not add a token protein merely to pass a coverage check. For every graph
without a protein, first decide whether the record represents a biological
mechanism. If literature supports a protein-mediated mechanism, add the
specific protein and evidence-backed edges. If the graph represents an upper
ontology class, measurement descriptor, numerical bin, hazard classification,
or another nonmechanistic context, remove the causal graph or record an
explicit nonmechanism disposition while preserving the TraitRecord. This work
does not require deprecating the record.

The invariant is therefore: every retained causal mechanism graph has a
protein. Nonmechanistic records should not carry invented mechanism graphs.

## Execution phases

### 1. Preserve the remediation baseline

Validate and commit the completed removal of organism-specific UniProt
groundings, its mapping decisions, tests, reports, and generated pages. Rebase
onto the current `origin/main` before starting the new schema work.

### 2. Add schema, audits, and rendering

Implement `protein_examples` and generated model updates. Extend the trait
page renderer to show the protein accession, taxon, entry status, and evidence.

Add a graph-level coverage audit that reports, for every graph:

- protein-node count;
- semantic-grounding count;
- canonical-example count;
- taxon-paired UniProt-example count;
- scope disposition; and
- the exact unmet requirement.

Extend the UniProt audit to resolve protein examples and verify primary
accession status, entry type, protein name, taxon equality, entry version, and
deletion/merge state. Add a hard invariant that generic `grounding` fields
cannot contain `UniProtKB:` values.

### 3. Run a metabolism pilot

Curate a focused batch of ten metabolism records. Metabolism has 49 graphs and
only six minimum-coverage gaps, so it provides strong enzyme and complex cases
for testing the model before broad rollout. Include single-chain enzymes,
multi-subunit complexes, reviewed and carefully justified unreviewed examples,
and at least one graph requiring node refinement.

### 4. Close graph-level coverage gaps

Work in batches of 5-15 records, reusing shared protein-family and taxon
research while preserving record-specific evidence. Process categories in
this order:

1. metabolism;
2. physiology;
3. morphology;
4. environment;
5. ecology;
6. genomics; and
7. upper/nonmechanism dispositions.

Within each category, process the 73 add-taxon records first, the 38
add-protein records second, and the 43 records needing both last. The latter
cohort receives scope review before any graph enrichment.

### 5. Review every protein node

Review all 818 current protein nodes, not only the minimum one-per-graph
examples. Each node must end with one of these dispositions:

- exact GO molecular-function grounding;
- exact GO cellular-component complex grounding;
- exact InterPro/NCBIfam protein-family grounding;
- an evidence-backed split or rename to a more specific entity; or
- explicit reviewed label-only status with the reason no exact semantic term
  is available.

Broad labels such as `terminal oxidase`, `hydrogenase`, `methyltransferase`,
and `quorum-quenching enzyme` should be split only when the graph's cited
mechanism identifies the concrete class. No automated top hit may write
directly to the corpus.

### 6. Source and identifier verification

Use existing Falcon reports to locate candidate claims. Prefer primary DOI
sources and use PMID only when no DOI exists. Verify ontology definitions,
not only labels, against current GO, InterPro, NCBIfam, Complex Portal, and
UniProt records. Use targeted Falcon or literature searches only when the
tracked report cannot distinguish the protein family, complex, or taxon.

Every new or changed causal edge must include evidence with `reference`,
`snippet`, and `notes`. UniProt resolution proves identity and taxonomy; it
does not by itself prove the causal role.

### 7. Publish and verify

Regenerate node-grounding residuals, UniProt and coverage reports, and all
affected trait pages after each batch. The completed corpus must satisfy:

- every retained graph has at least one `GENE_OR_PROTEIN` node;
- every retained graph has at least one referenced canonical taxon;
- every retained graph has at least one taxon-matched UniProt protein example;
- every protein node has a semantic grounding or reviewed label-only
  disposition;
- no generic node grounding contains a UniProt instance;
- every protein accession resolves and its UniProt taxon matches the declared
  `NCBITaxon` identifier; and
- all evidence and generated-artifact audits pass.

Run the final gates:

```bash
just validate-all
just test
just audit-graphs
just audit-snippets
just audit-canonical-examples
just audit-uniprot
just gen-pages
just audit-derived-reports
```

