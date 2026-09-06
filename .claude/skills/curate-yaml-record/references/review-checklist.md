# TraitRecord review checklist

Use this checklist for one trait. It is not a requirement to populate every
optional slot or to invent a causal graph.

## Evidence standard

- Definition, example, relation, and causal-edge evidence are distinct claims;
  attach sources to the narrowest supported object.
- Confirm each DOI/PMID/CURIE and inspect enough source text to establish
  support for the exact trait and scope.
- Snippets are short verbatim text; curator interpretation belongs in notes.
- Prediction and association do not establish mechanism or causality.
- Preserve conflicts and report bounded negative searches as “not found.”

## Field-by-field audit

| Area | Verify | Complete enough when |
|---|---|---|
| Identity | ID, label, synonyms, polarity, and term kind denote one trait concept. | The record is not an organism, protein, cell structure, assay, or observation. |
| Definition | Text is non-circular, source-backed, and scoped to what the trait means. | `definition_source` resolves and the wording does not overgeneralize. |
| Hierarchy | Every parent is strictly broader; replacements and xrefs have correct semantics. | Related, correlated, and opposite traits are not encoded as is-a. |
| Category/model | Trait category, domain, range, priority, and subset agree with the concept. | Enumerated values do not force a misleading representation. |
| Examples | Organism/protein example, taxon, role, source version, and evidence agree. | Examples are record-specific and do not imply universality. |
| Evidence | Reference, snippet, source type, and notes support the nearest claim. | Database and literature provenance remain distinguishable. |
| Causal graph | Scope, node identity/type, edge direction/predicate, and edge evidence agree. | Every edge is supported and nonmechanistic records do not carry invented mechanisms. |
| Discussions/datasets | Each item is relevant, durable, and actionable. | No placeholder question or bibliography dump remains. |
| Status/audit | Mapping status, per-record event, and repository history match the review performed. | REVIEWED has human sign-off; LLM assistance and unresolved gaps are explicit. |
