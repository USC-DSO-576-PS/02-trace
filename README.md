# Marquee on Vine — box office

Marquee on Vine is a small live-events venue off Hollywood Boulevard. This is
the box office's working repo and the DSO-576 Module 2 repo.

The raw door-scanner feed is `ticket_scans.csv`, one row per gate scan before
anyone cleaned or reconciled it. `door_report.py` is the inherited program the
last analyst left behind. It cleans the amounts, keeps paid scans, flags large
orders, sorts the result, and prints the period's headline numbers.

Finance closes the same period at **$3,832**. The program reports **$3,876**.
Nobody has reconciled the **$44 difference** or decided which figure the venue
should quote.

## Files

| File | What it is |
|---|---|
| `trace_lab.py` | The ordered `# %%` lab. Predict each cell, run it, and inspect the result before moving on. |
| `door_report.py` | The inherited program you will read and investigate. |
| `ticket_scans.csv` | The raw feed: `scan_id`, `show`, `ticket_type`, `amount`, `scanned_at`. |
| `door_take_memo.md` | The one-file business deliverable you complete and upload to Brightspace. |
| `AGENTS.md` | Standing rules for coding agents working in this repo. |
| `tutor.md` | Instructions for asking your own agent to tutor you. |
| `pyproject.toml`, `uv.lock` | The pandas environment used by `uv run`. |

## Run the two Python files

Open the whole folder in VS Code. In `trace_lab.py`, put the cursor in a cell,
write down your prediction, and press **Shift+Enter** to run that cell. Read the
cells from top to bottom.

Run the inherited program from the terminal:

```text
uv run python door_report.py
```

The data has 120 rows from fourteen performances between September and
December 2025. Its grain is one row per scanner event—not one row per person,
ticket sold, or show.
