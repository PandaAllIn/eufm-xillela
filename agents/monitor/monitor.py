import argparse
import pathlib
import sys
from datetime import datetime

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]


def load_yaml(p):
    with open(p, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def gar_for_due(due_str):
    try:
        due = datetime.strptime(due_str, "%Y-%m-%d").date()
    except Exception:
        return "grey"
    today = datetime.utcnow().date()
    if due < today:
        return "red"
    if (due - today).days <= 14:
        return "amber"
    return "green"

def render_summary():
    w = load_yaml(ROOT / "wbs" / "wbs.yaml") or {}
    lines = ["# Monitor A — GAR Summary", ""]
    for wp, items in (w.get("wbs") or {}).items():
        lines.append(f"## {wp}")
        for it in items:
            due = it.get("due", "?")
            gar = gar_for_due(due)
            lines.append(f"- **{it.get('id','?')}** {it.get('title','')} — due {due} — GAR: **{gar.upper()}**")
        lines.append("")
    return "\n".join(lines)

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print summary to stdout")
    parser.add_argument("--emit-status", action="store_true", help="Alias of --dry-run for CI")
    parser.add_argument("--post-comments", action="store_true", help="(stub) would comment on PR")
    args = parser.parse_args(argv)

    summary = render_summary()
    print(summary)
    if args.post_comments:
        print("\n[post-comments stub] Use GITHUB_TOKEN to comment on the latest PR.", file=sys.stderr)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
