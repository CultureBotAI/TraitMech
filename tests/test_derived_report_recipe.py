"""Regression tests for failure diagnostics in ``audit-derived-reports``."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def test_graph_protein_generator_failure_reaches_missing_report_diagnostic():
    """A crashing generator must not bypass the recipe's actionable error.

    ``set -e`` would otherwise stop immediately at the generator invocation,
    before the following file check can print the captured generator output.
    """
    justfile = (ROOT / "justfile").read_text()
    invocation = (
        'uv run python scripts/audit_graph_protein_taxa.py --out "$tmp/$gpt" \\\n'
        '      --fail-on none > "$tmp/gen.log" 2>&1 || true'
    )

    assert invocation in justfile
    assert 'if [ ! -s "$tmp/$gpt" ]; then' in justfile
    assert 'cat "$tmp/gen.log" >&2' in justfile
