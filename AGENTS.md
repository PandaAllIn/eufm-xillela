# Contributor Guide for Agents (Monitor A focus)

## What to work on
- Primary folder: `/agents/monitor/`.
- Source of truth for tasks: `/wbs/wbs.yaml` and `/wbs/milestones.yaml`.
- Compliance rules live in `/agents/monitor/rules/*.yaml`.

## How to validate changes
- Run `python -m pytest agents/monitor/tests -q` (tests must pass).
- Run `ruff check . && ruff format --check .` for lint/format.
- `python agents/monitor/monitor.py --dry-run` should:
  - Render a summary table per WP (GAR flags).
  - Print next 14‑day deadlines and any blockers.

## PR instructions
- Title: `[monitor] <concise change>`
- Include: before/after monitor output snippet and links to related issues.

## Monitor A contract
- Must not change WBS files unless the PR includes a matching rationale in `/docs/plan_overview.md`.
- Must attach a `compliance_score` (0‑100) to each run based on rules.
