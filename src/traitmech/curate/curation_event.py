"""Standard helper for appending CurationEvent entries to a TraitRecord.

Every script that mutates a TraitRecord YAML should call
``record_curation_event`` to leave an audit trail. Centralizing here means:

* timestamps are ISO-8601 with UTC tz, consistently;
* the ``curation_history`` slot is created on demand;
* re-runs of idempotent migration scripts can short-circuit when the most
  recent event already matches (``skip_if_recent`` flag);
* the schema's ``CurationEvent`` field names (timestamp / curator / action /
  changes / llm_assisted) are honored, so future schema diffs only need
  to touch one file.

Drop-in usage::

    from traitmech.curate.curation_event import record_curation_event

    record_curation_event(
        doc,
        curator="claude",
        action="GROUND_CAUSAL_NODES",
        changes=f"Grounded {n} nodes via mappings/node_grounding.tsv",
        llm_assisted=True,
    )

Ported from CultureMech's ``src/culturemech/curate/curation_event.py``
(via MediaIngredientMech's ``record_curation_event``). The TraitMech
``CurationEvent`` schema does not define ``notes``, ``source``,
``previous_status``, ``new_status``, or ``llm_model`` — those keyword
arguments are intentionally absent here. Pass narrative detail in
``changes``.

The default timestamp format matches the in-repo convention used by
existing ``append_curation_event`` helpers (whole-second precision,
``Z`` suffix instead of ``+00:00``) so re-runs produce byte-identical
diffs.
"""

from __future__ import annotations

import datetime
from typing import Any

__all__ = ["record_curation_event", "now_iso"]


def now_iso() -> str:
    """Current UTC timestamp matching the repo's existing convention.

    Whole-second precision with a ``Z`` suffix
    (e.g. ``"2026-05-25T04:50:12Z"``). Mirrors the format produced by
    ``ground_causal_nodes.append_curation_event`` and siblings, so
    converting those scripts to this helper does not churn the YAML.
    """
    iso = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    return iso.replace("+00:00", "Z")


def record_curation_event(
    doc: dict[str, Any],
    *,
    curator: str,
    action: str,
    changes: str | None = None,
    llm_assisted: bool = False,
    timestamp: str | None = None,
    skip_if_recent: bool = False,
) -> dict[str, Any]:
    """Append a CurationEvent to ``doc['curation_history']``.

    Args:
        doc: The TraitRecord dict being mutated. Mutated in place.
        curator: Script / human identifier (e.g. ``"claude"``,
            ``"seed_from_metpo"``, ``"jane.smith"``). Required because
            the schema's ``CurationEvent.curator`` is required.
        action: SCREAMING_SNAKE_CASE action label
            (e.g. ``"GROUND_CAUSAL_NODES"``, ``"SEEDED_FROM_METPO"``).
            Required.
        changes: Optional human-readable description of what changed.
            Maps to ``CurationEvent.changes`` — also the right field
            for narrative notes since the schema has no separate
            ``notes`` slot.
        llm_assisted: True when an LLM produced this change. When True
            the field is emitted; when False the field is omitted so
            downstream consumers can distinguish "explicitly not LLM"
            from "older event written before this field existed".
        timestamp: Override the ISO-8601 timestamp (used for tests /
            deterministic snapshots). Defaults to current UTC.
        skip_if_recent: When True, do nothing if the most recent
            ``curation_history`` entry already matches the same
            ``(curator, action)`` pair. Useful when refactoring a script
            into the helper without producing duplicate trail entries
            during a re-run.

    Returns:
        The appended event dict (or the most recent matching one if
        ``skip_if_recent`` short-circuited).
    """
    history = doc.setdefault("curation_history", [])
    if history is None:
        doc["curation_history"] = history = []

    if skip_if_recent and history:
        last = history[-1]
        if (
            isinstance(last, dict)
            and last.get("curator") == curator
            and last.get("action") == action
        ):
            return last

    event: dict[str, Any] = {
        "timestamp": timestamp or now_iso(),
        "curator": curator,
        "action": action,
    }
    if changes is not None:
        event["changes"] = changes
    if llm_assisted:
        event["llm_assisted"] = True

    history.append(event)
    return event
