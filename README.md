# Marquee on Vine — box office

**Marquee on Vine** is a small live-events venue off Hollywood Boulevard: music,
comedy, a Sunday open mic. Small staff, a scanner at the door, a season's worth
of shows a quarter. This is the box office's working repo, and the DSO-576
Module 2 repo.

The venue's reporting runs off a *show-level* table — one clean row per
performance, with tickets, price, and refunds already totalled. You are working
one level **underneath** that, at `ticket_scans.csv`: the **raw feed from the
door scanners**, one row per gate scan, before anyone cleaned it.

`door_report.py` is the script the last analyst left behind. It reads that feed
and prints the period's door take. Your manager inherited it and asked a fair
question: **what does it actually do?**

Finance closes the same period at **$1,151**. The script reports **$1,195**.
Nobody has worked out which figure the venue should be quoting.

## What's in this repo

| File | What it is |
|---|---|
| `README.md` | This file. |
| `ticket_scans.csv` | The data: the raw gate-scan feed. Columns: `scan_id`, `show`, `ticket_type` (GA / VIP / presale / comp), `amount` (as text — comps are logged as `comp`, `n/a`, or blank), `scanned_at`. |
| `door_report.py` | The inherited script. Cleans the amounts, keeps the paid scans, flags large orders, ranks them, and prints the period's door take. |
| `trace_filter.py` | One show's scans, pulled out of the feed. |
| `trace_derive.py` | Cleans `amount` and flags the large orders. |
| `trace_sort.py` | The earliest scans of the season, by timestamp. |
| `trace_copy.py` | Open Mic amounts, raw and cleaned side by side. |
| `trace_chain.py` | The season's VIP scans, earliest first — one chained line. |
| `trace_function.py` | `gate_fee` — the per-scan handling fee at the gate. |
| `trace_compose.py` | Whether VIP scans clear the $40 line on average, in typed steps. |
| `unfamiliar_snippet.py` | A sanity check on the feed's `scan_id`s. |
| `trace_report.md` | The template for what you hand in. Fill it in and upload it to Brightspace. |
| `pyproject.toml` | Declares the repo's one dependency (pandas) so `uv run python <file>` just works. |
| `uv.lock` | Pins the exact dependency versions `uv run` installs — everyone runs the same pandas. |
| `AGENTS.md` | The house rules a coding agent follows in this repo. |
| `tutor.md` | Instructions your own agent can read to tutor you for Quiz 2. |

## The data

- **Grain:** one row per gate scan — not one row per ticket sold, and not one row
  per show.
- **It is a raw feed.** Nothing has been cleaned, corrected, or totalled. The
  `amount` column is text as the scanner wrote it.
- **The season in the file:** seven performances between October and December
  2025 — Electric Pulse (twice), Latin Fire Night, Broadway Bites, Midnight
  Comedy Hour, Sunset Jazz Trio, Open Mic Underground.
