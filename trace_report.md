# What this pipeline does — `ticket_scans.csv`

**To:** Operations Manager, The Marquee on Vine
**From:** <!-- your name -->
**Date:** <!-- today's date -->
**Re:** The inherited scan-cleaning script — what it actually does

---

## 1. The pipeline, step by step

The script we inherited is this:

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

<!-- Say where each traced value came from — which specimen you ran, or the
pipeline itself. The numbers have to be ones you saw. -->

### Two values worth pointing at

<!-- Pick two specific rows or numbers from the traced values above that a reader
would misread if nobody flagged them. State the value, and what it means. One or
two sentences each. -->

1. <!-- fill this in -->
2. <!-- fill this in -->

---

## 2. What the pipeline is for

<!-- Two or three sentences, in plain English, in YOUR words — not a restatement
of the code. What business question does `summary` answer, and who would use it?
Do not have an agent write this paragraph. -->

<!-- fill this in -->

---

## 3. One thing that would break it

<!-- Name ONE realistic change — to the data, the column names, or the thresholds
— that would make this pipeline give a wrong or misleading answer without
raising an error. Then say what you would see if it happened, and how you would
notice. -->

**What would break it.** <!-- fill this in -->

**What you would see.** <!-- fill this in -->

**How you would catch it.** <!-- fill this in -->

---

## 4. Confidence

<!-- One line. How much would you stake on `summary` being right today, and what
would you check before handing it to someone who will act on it? -->

<!-- fill this in -->
