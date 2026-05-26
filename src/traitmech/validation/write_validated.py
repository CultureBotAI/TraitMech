"""Write-time validation: dump a TraitRecord to YAML *only if* it passes
closed-schema LinkML validation.

audit-writers: library-helper

    This module is the canonical write-time YAML gate that CLI scripts
    route through. Curation-history append and write-safeguard
    (--dry-run/--apply) responsibilities live in the callers, not
    here. ``scripts/audit_writers.py`` recognizes the
    ``audit-writers: library-helper`` marker on this line and excludes
    this file from its CLI-writer audit.

This is the write-time gate that pairs the in-memory mutation step with
a schema check at the same call site, so a script can't accidentally
write a doc that drifted into an invalid shape between the mutation and
the disk write. The check is on the in-memory object (not a re-load of
the emitted YAML), which is the right granularity for catching missing
required fields, unknown fields, enum / pattern violations, etc. —
the failure modes the audit cares about.

Use::

    from traitmech.validation.write_validated import (
        write_validated_trait,
        ValidationFailedError,
    )

    try:
        write_validated_trait(doc, path)
    except ValidationFailedError as exc:
        # Bad doc refused; print categorized errors and abort.
        print(exc.summary())
        raise

The validator is shared across calls (LinkML schema parse + JSON-schema
emit is the slow part), so calling this in a tight migration loop is
cheap.

Ported from CultureMech's ``src/culturemech/validation/write_validated.py``
(by way of MediaIngredientMech's ``write_validated_ingredient``). The
TraitMech version is simpler: the schema has only one ``tree_root: true``
class (``TraitRecord``), so ``infer_target_class`` is a constant.
"""

from __future__ import annotations

from pathlib import Path
from threading import Lock
from typing import Any

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity, ValidationResult

DEFAULT_SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schema" / "traitmech.yaml"
DEFAULT_TARGET_CLASS = "TraitRecord"

_VALIDATORS: dict[Path, Validator] = {}
_VALIDATOR_LOCK = Lock()


class ValidationFailedError(Exception):
    """Raised when a TraitRecord fails closed-schema validation before write."""

    def __init__(self, path: Path | None, errors: list[ValidationResult]):
        self.path = path
        self.errors = errors
        super().__init__(self.summary())

    def summary(self) -> str:
        lines = [
            f"validation failed: {len(self.errors)} error(s)"
            + (f" for {self.path}" if self.path else "")
        ]
        for err in self.errors[:10]:
            lines.append(f"  - {err.message[:200]}")
        if len(self.errors) > 10:
            lines.append(f"  ... + {len(self.errors) - 10} more")
        return "\n".join(lines)


def _get_validator(schema_path: Path) -> Validator:
    """Cache validators keyed by resolved schema path so callers can mix
    schemas in the same process without silently reusing a stale instance."""
    key = Path(schema_path).resolve()
    with _VALIDATOR_LOCK:
        if key not in _VALIDATORS:
            _VALIDATORS[key] = Validator(
                schema=str(key),
                validation_plugins=[JsonschemaValidationPlugin(closed=True)],
            )
        return _VALIDATORS[key]


def validate_trait(
    doc: dict[str, Any],
    *,
    target_class: str = DEFAULT_TARGET_CLASS,
    schema_path: Path = DEFAULT_SCHEMA_PATH,
) -> list[ValidationResult]:
    """Return the list of ERROR-severity validation results (empty when clean)."""
    validator = _get_validator(schema_path)
    report = validator.validate(doc, target_class=target_class)
    return [r for r in report.results if r.severity == Severity.ERROR]


def write_validated_trait(
    doc: dict[str, Any],
    path: Path,
    *,
    target_class: str = DEFAULT_TARGET_CLASS,
    schema_path: Path = DEFAULT_SCHEMA_PATH,
    yaml_kwargs: dict[str, Any] | None = None,
) -> None:
    """Write ``doc`` to ``path`` as YAML, but only if validation passes.

    Raises :class:`ValidationFailedError` (without writing) when closed-schema
    validation finds any error. Use in place of
    ``path.write_text(yaml.safe_dump(doc, ...))`` inside mutating scripts.
    """
    errors = validate_trait(doc, target_class=target_class, schema_path=schema_path)
    if errors:
        raise ValidationFailedError(path, errors)
    # Match the repo's existing yaml emission convention so re-running the
    # helper over an existing file produces a byte-identical diff.
    opts = {
        "default_flow_style": False,
        "sort_keys": False,
        "allow_unicode": True,
        **(yaml_kwargs or {}),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(doc, **opts), encoding="utf-8")
