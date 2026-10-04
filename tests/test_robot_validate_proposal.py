"""Keep ROBOT proposals attached to the real METPO hierarchy (#1658)."""

import sys
from pathlib import Path

import pytest
import yaml
from rdflib import Graph, RDFS, URIRef

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import robot_validate_proposal as validator  # noqa: E402


def metpo_prefix():
    return next(value.removeprefix("METPO: ") for value in validator.PREFIXES
                if value.startswith("METPO: "))


def test_robot_prefix_matches_schema_and_labeled_ontology_parent():
    schema = yaml.safe_load((ROOT / "src/traitmech/schema/traitmech.yaml").read_text())
    assert metpo_prefix() == schema["prefixes"]["METPO"]
    ontology = Graph().parse(validator.DEFAULT_METPO)
    parent = URIRef(metpo_prefix() + "1000702")
    assert {str(label) for label in ontology.objects(parent, RDFS.label)} == {"motile"}
    assert list(ontology.objects(parent, RDFS.subClassOf))


@pytest.mark.parametrize("kinds", [("classes",), ("properties",), ("classes", "properties")])
def test_every_template_command_uses_canonical_namespace(tmp_path, monkeypatch, kinds):
    cohort = tmp_path / "cohort"
    cohort.mkdir()
    for kind in kinds:
        (cohort / f"metpo_proposal_{kind}_robot.tsv").write_text("fixture\n")
    out = tmp_path / "out"
    commands = []

    def run(command):
        commands.append(command)
        Path(command[command.index("--output") + 1]).write_text("fixture\n")

    monkeypatch.setattr(validator, "find_robot", lambda: "robot")
    monkeypatch.setattr(validator, "run", run)
    monkeypatch.setattr(sys, "argv", ["validator", str(cohort), "--out", str(out)])
    assert validator.main() == 0
    templates = [command for command in commands if command[1] == "template"]
    assert len(templates) == len(kinds)
    for command in templates:
        assert "METPO: https://w3id.org/metpo/" in command
        assert not any("purl.obolibrary.org/obo/METPO_" in arg for arg in command)
    merge, = [command for command in commands if command[1] == "merge"]
    assert str(validator.DEFAULT_METPO) in merge
    reason, = [command for command in commands if command[1] == "reason"]
    assert reason[reason.index("--reasoner") + 1] == "ELK"


def test_manual_skill_commands_use_same_namespace():
    guidance = (ROOT / ".claude/skills/metpo-proposal/reference/verification-and-pitfalls.md").read_text()
    commands = [line for line in guidance.splitlines() if '--prefix "METPO:' in line]
    assert len(commands) == 2
    assert all(f'METPO: {metpo_prefix()}"' in line for line in commands)
    assert metpo_prefix() == "https://w3id.org/metpo/"
