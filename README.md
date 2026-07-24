# Module 2 — Trace a Table Transformation

Welcome back to **Marquee on Vine**, the small live-events venue from Module 1.

In Module 1 you read `shows.csv`: the *show-level* table, one clean row per
performance with tickets sold, price, and refunds already totalled. Someone —
or some agent — built that table. This week you look at what sits **underneath**
it: `ticket_scans.csv`, the **raw feed from the door scanners**, one row per
gate scan, before anyone cleaned it. Aggregate these scans by show and you would
rebuild the shows.csv world. Your job this module is not to write that pipeline —
it is to **trace** one, step by step, and always know exactly what object you
hold.

## The module's move

Track table state **one step at a time** — filter, derived column, sort,
independent copy — unpack a short **two-step method chain** into named steps,
compose type-hinted calls, and read a small function with **successive `if`
statements** for its exact behavior. (No `groupby` yet — that lands in Module 4.)

## How to work through it (S3 → S4)

**Trace on the handout FIRST, run to confirm SECOND.** Every specimen below is a
**frozen** piece of agent-written code — nobody generates it live, so the whole
class traces the *same* code. For each one:

1. **Predict on paper** — in the handout blanks, write what object each step
   produces and the exact result. Do not run it yet.
2. **Run to confirm** — `python trace_filter.py` (etc.), then check against
   [`expected_outputs.md`](expected_outputs.md). A mismatch means your trace has
   a bug to find — that is the whole exercise.

- **S3 — Skim a Pipeline:** read `raw → clean → summary` as named objects. Skim
  `ticket_scans.csv` and write one plain-English line per step (input object,
  action, output/grain, business role) — no exact arithmetic yet.
- **S4 — Trace a Pipeline:** now trace exact values, types, and grain through the
  specimens below.

## File map

| File | What it is |
|---|---|
| `ticket_scans.csv` | The raw gate-scan feed (one row per scan). The data every specimen reads. |
| `generate_scans.py` | Seeded, deterministic generator for the CSV. Re-run it to restore the exact data. |
| `trace_filter.py` | ONE step — filter (a mask selects rows). |
| `trace_derive.py` | Clean `amount`, then ONE step — a derived column (`is_large_order`). |
| `trace_sort.py` | ONE step — sort (reorder rows, same population). |
| `trace_copy.py` | Source vs **independent** `.copy()` — mutating the copy leaves the source alone. |
| `trace_chain.py` | A two-step method chain (filter → sort), unpacked into named steps. |
| `trace_function.py` | A small function with **successive `if`** statements — check order is behavior. |
| `trace_compose.py` | Type-hinted composition: `DataFrame -> Series -> float -> bool`. |
| `unfamiliar_snippet.py` | ONE not-yet-taught construct (`value_counts`) for the ask-your-agent workflow. |
| `expected_outputs.md` | Exact output of every specimen — your self-check key after tracing. |
| `HOMEWORK.md` | This week's homework: finish the Try blocks + the pull practice. |
| `AGENTS.md` | House rules for any coding agent you point at this repo. |
| `quiz-coach.md` | Drop-in instructions that turn your own agent into a Socratic Quiz 2 coach. |

## The data (`ticket_scans.csv`)

- **Grain:** one row per gate scan.
- **Columns:** `scan_id`, `show`, `ticket_type` (GA / VIP / presale / comp),
  `amount` (raw text), `scanned_at` (timestamp).
- **It is a raw feed, so it is messy on purpose:** some `amount` values are
  unparseable or blank (comp tickets logged as `comp`, `n/a`, or nothing); one
  ticket was scanned twice (a duplicate `scan_id`); one presale sits exactly on
  the `amount >= 40` boundary; two scans straddle midnight. The specimens trace
  through this mess — that is the skill.

Regenerate the data at any time with:

```bash
python generate_scans.py
```

It uses a fixed seed and the standard library only, so the file it writes is
identical every time.
