"""Keep the published QC dashboard counts aligned with the live corpus."""

from html.parser import HTMLParser
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent


class Dashboard(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows = []
        self.values = []
        self.row = None
        self.cell = None
        self.value = None

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.row = []
        elif tag == "td":
            self.cell = []
        elif tag == "div" and "value" in dict(attrs).get("class", "").split():
            self.value = []

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)
        if self.value is not None:
            self.value.append(data)

    def handle_endtag(self, tag):
        if tag == "td" and self.cell is not None:
            self.row.append("".join(self.cell).strip())
            self.cell = None
        elif tag == "tr" and self.row:
            self.rows.append(self.row)
            self.row = None
        elif tag == "div" and self.value is not None:
            self.values.append("".join(self.value).strip())
            self.value = None


def test_published_dashboard_counts_match_corpus():
    config_path = ROOT / "conf" / "qc_config.yaml"
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    records = [
        yaml.safe_load(path.read_text(encoding="utf-8"))
        for path in (config_path.parent / config["yaml_dir"]).rglob(config["pattern"])
    ]
    page = Dashboard()
    page.feed((ROOT / "dashboard" / "index.html").read_text(encoding="utf-8"))
    assert page.values[0] == f"{len(records):,}", "Run just gen-qc-dashboard"
    assert [row[0] for row in page.rows] == [slot["path"] for slot in config["slots"]]
    for row in page.rows:
        populated = 0
        for record in records:
            value = record
            for part in row[0].split("."):
                value = value.get(part) if isinstance(value, dict) else None
            populated += value is not None and not (
                isinstance(value, (str, list, dict, tuple, set)) and not value
            )
        assert row[1] == f"{populated:,} / {len(records):,}", row[0]
