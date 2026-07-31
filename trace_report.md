# What `door_report.py` does — and which door take to trust

**To:** Operations Manager, Marquee on Vine
**From:** <!-- your name -->
**Date:** <!-- today's date -->
**Re:** The inherited scan-cleaning script, and the $1,151 / $1,195 gap

<!-- This report is the one thing you hand in for Module 2. Fill in every
section, then upload this file to Brightspace before Quiz 2. Nothing is
submitted through GitHub. The wording has to be yours: write it yourself, and
use values you traced and confirmed by running the code rather than any you were
handed. -->

---

## 1. The pipeline, step by step

`door_report.py` is the script we inherited. Its pipeline is these six lines:

```python
raw       = pd.read_csv("ticket_scans.csv")
clean     = raw.copy()
clean["paid"] = pd.to_numeric(clean["amount"], errors="coerce")
paid_only = clean[clean["paid"].notna()].copy()
paid_only["is_large_order"] = paid_only["paid"] >= 40
summary   = paid_only.sort_values("paid", ascending=False)
```

One row per step. **Operation** = what kind of move it is (read, copy, derived
column, filter, sort). **Grain** = one row per *what* in the table that step
produces. **Traced values** = what you actually saw when you ran it — a row
count, the values in a column, the first rows of the result.

| # | Line | Operation | Object produced | Grain of that object | Traced values |
|---|---|---|---|---|---|
| 1 | `raw = pd.read_csv(...)` | <!-- fill this in --> | `raw` | <!-- fill this in --> | <!-- fill this in: how many rows? which columns? --> |
| 2 | `clean = raw.copy()` | <!-- fill this in --> | `clean` | <!-- fill this in --> | <!-- fill this in --> |
| 3 | `clean["paid"] = pd.to_numeric(...)` | <!-- fill this in --> | `clean` | <!-- fill this in --> | <!-- fill this in: which rows became NaN, and why? --> |
| 4 | `paid_only = clean[...notna()].copy()` | <!-- fill this in --> | `paid_only` | <!-- fill this in --> | <!-- fill this in: how many rows survived? how many were dropped? --> |
| 5 | `paid_only["is_large_order"] = ...` | <!-- fill this in --> | `paid_only` | <!-- fill this in --> | <!-- fill this in: how many True? what happens at exactly 40? --> |
| 6 | `summary = ...sort_values(...)` | <!-- fill this in --> | `summary` | <!-- fill this in --> | <!-- fill this in: the first three scan_ids and their paid values --> |

<!-- Say where each traced value came from — which file you ran, or the pipeline
itself. The numbers have to be ones you saw. -->

---

## 2. Which door take to trust

The script prints **$1,195** for the period. Finance closes the same period at
**$1,151**. This section is the reason the manager asked for the report at all,
so answer it plainly and in your own words.

**The figure the venue should quote.** <!-- Name ONE number, in one sentence. -->

**Why — what causes the gap.** <!-- What is it about the data or the pipeline
that makes the two figures differ? Name the specific rows or step involved, and
say how you found them: what you traced, what you ran, what it showed. Two to
four sentences. -->

**The check that settles it.** <!-- Give the one thing a reader could run or
look at that turns your explanation from plausible into proved. Say what it
shows. -->

**One more thing to flag.** <!-- `summary` has a row count. State plainly what
that count is a count *of* — and what it is not — so nobody downstream reads it
as something it isn't. One or two sentences. -->

---

## 3. What the pipeline is for

<!-- Two or three sentences, in plain English, in YOUR words — not a restatement
of the code. What business question does `summary` answer, and who would use it?
Do not have an agent write this paragraph. -->

<!-- fill this in -->

---

## 4. One thing that would break it

<!-- Name ONE realistic change — to the data, the column names, or the
thresholds — that would make this pipeline give a wrong or misleading answer
without raising an error. Then say what you would see if it happened, and how
you would notice. -->

**What would break it.** <!-- fill this in -->

**What you would see.** <!-- fill this in -->

**How you would catch it.** <!-- fill this in -->

---

## 5. Confidence

<!-- One line. How much would you stake on `summary` being right today, and what
would you check before handing it to someone who will act on it? -->

<!-- fill this in -->
