# Stub for seeding GitHub issues from /wbs/*.yaml
# Usage: python scripts/seed_backlog.py --dry-run
import argparse, yaml, pathlib, json

ROOT = pathlib.Path(__file__).resolve().parents[1]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    w = yaml.safe_load(open(ROOT / "wbs" / "wbs.yaml", encoding="utf-8"))
    owners = yaml.safe_load(open(ROOT / "wbs" / "owners.yaml", encoding="utf-8"))
    out = []
    for wp, items in (w.get("wbs") or {}).items():
        for it in items:
            out.append({
                "title": f"[{wp}] {it['id']} — {it['title']}",
                "labels": [wp],
                "assignee": owners.get(it.get("owner",""), ""),
                "due": it.get("due"),
                "body": f"WBS ID: {it['id']}\nDue: {it.get('due')}\nOwner: {it.get('owner')}"
            })
    if args.dry_run:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print("Non-dry-run mode not implemented yet.")
if __name__ == "__main__":
    main()
