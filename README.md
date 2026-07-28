# Module 2 — Trace a Table Transformation

This week's client is **Marquee on Vine**, a small live-events venue in LA.

Their reporting runs off a *show-level* table: one clean row per performance,
with tickets sold, price, and refunds already totalled. Someone — or some agent —
built that table. Your job starts one level **underneath** it, at
`ticket_scans.csv`: the **raw feed from the door scanners**, one row per gate
scan, before anyone cleaned it.

Your manager inherited a short script that cleans and ranks those scans, and
asked you a fair question: **what does it actually do?** Your job is not to write
the pipeline — it is to **trace** it, step by step, and know exactly what object
each step produces.

## What's in this repo

| File | What it is |
|---|---|
| `README.md` | This file — the setting and the steps. |
| `ticket_scans.csv` | The data: the raw gate-scan feed, one row per scan. Columns: `scan_id`, `show`, `ticket_type` (GA / VIP / presale / comp), `amount` (raw text), `scanned_at`. |
| `trace_filter.py` | ONE step — filter (a mask selects rows). |
| `trace_derive.py` | Clean `amount`, then ONE step — a derived column (`is_large_order`). |
| `trace_sort.py` | ONE step — sort (reorder rows, same population). |
| `trace_copy.py` | Source vs **independent** `.copy()` — mutating the copy leaves the source alone. |
| `trace_chain.py` | A two-step method chain (filter → sort), unpacked into named steps. |
| `trace_function.py` | A small function with **successive `if`** statements — check order is behavior. |
| `trace_compose.py` | Type-hinted composition: `DataFrame -> Series -> float -> bool`. |
| `unfamiliar_snippet.py` | ONE not-yet-taught construct (`value_counts`) for the ask-your-agent workflow. |
| `trace_report.md` | The template for what you hand in. Fill it in and upload it to Brightspace. |
| `AGENTS.md` | The house rules your coding agent follows in this repo. |
| `tutor.md` | Instructions your own agent can read to tutor you for Quiz 2. |

## The data (`ticket_scans.csv`)

- **Grain:** one row per gate scan.
- **It is a raw feed, so it is messy on purpose:** some `amount` values are
  unparseable or blank (comp tickets logged as `comp`, `n/a`, or nothing); one
  ticket was scanned twice (a duplicate `scan_id`); one presale sits exactly on
  the `amount >= 40` boundary; two scans straddle midnight.

`ticket_scans.csv` is committed and **frozen** — everyone traces the exact same
data. Don't edit it; if a run ever looks off, check out the committed file again
(`git checkout ticket_scans.csv`).

## The steps

### 1. Clone

You already have the `dso576` folder from Module 1 — go into it and clone this
module beside `01-onboard`.

**Mac** — open **Terminal**:

```
cd ~/dso576
git clone https://github.com/USC-DSO-576-PS/02-trace.git
cd 02-trace
```

**Windows** — open **Command Prompt**:

```
cd %USERPROFILE%\dso576
git clone https://github.com/USC-DSO-576-PS/02-trace.git
cd 02-trace
```

Lost? `pwd` (Mac) or `cd` with nothing after it (Windows) prints where you are.
Then open the `02-trace` folder in VS Code. You clone once, work locally, and
never push.

### 2. Trace on paper first, run to confirm

Every `trace_*.py` file is a **frozen** piece of agent-written code — nobody
generates it live, so the whole class traces the *same* code. For each one:

1. **Predict** — in the handout blanks, write what object each step produces and
   the exact result. Do not run it yet.
2. **Run to confirm** — `python trace_filter.py` (and so on). Each specimen
   **prints its own result**, so what it prints *is* the answer key. Compare it
   against your paper trace. A mismatch means your trace has a bug to find; that
   is the whole exercise.

There is no separate answers file: running is the self-check. When your run
differs from your trace and you can't see why, **work with the tutor** (*"read
tutor.md and tutor me."*) to locate the step that diverged — learning to learn
through an AI tutor is itself the skill.

### 3. Run the pipeline your report explains

The pipeline in the handout (§2.2) is the one your manager asked about:

```python
raw       = pd.read_csv("ticket_scans.csv")
clean     = raw.copy()
clean["paid"] = pd.to_numeric(clean["amount"], errors="coerce")
paid_only = clean[clean["paid"].notna()].copy()
paid_only["is_large_order"] = paid_only["paid"] >= 40
summary   = paid_only.sort_values("paid", ascending=False)
```

Run it over `ticket_scans.csv` yourself — in a scratch `.py` file of your own —
and record what you see at each step: the row counts, which rows became `NaN`,
what happens at exactly 40, and the first rows of `summary`. Those are the traced
values your report needs.

### 4. Diff and commit

```
git diff                                 # the exact lines you changed
git add .
git commit -m "Module 2 trace notes"
```

That is the weekly loop: **clone → edit → diff → commit**, all on your own
machine. `push` and `pull` send commits to and from a shared remote — worth
knowing as a professional, but this course never asks you to push.

## Homework

Fill in **`trace_report.md`** and **upload it to Brightspace before Quiz 2.** It
is the one thing you hand in for this module. Nothing is submitted through
GitHub.

The report is what you would send a manager who asked what the inherited script
does: one row per step with the operation, the grain of the table it produces,
and the traced values you saw; two or three sentences in your own words on what
the pipeline is for; and one thing that would break it. The traced values and the
plain-English paragraph have to be yours — don't have an agent write them.

To practice for the quiz, tell your agent: *"Read tutor.md and tutor me."*
