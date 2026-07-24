# Expected outputs — trace specimens

Trace each specimen **on paper first** (in the handout blanks), then run it and
check your prediction against the block below. Every output here was produced by
executing the committed file against the committed `ticket_scans.csv` — if your
run differs, you (or the data) changed something; re-run `python generate_scans.py`.

Do not read a specimen's block until you have written your own prediction. The
point of the module is knowing exactly what object you hold after each step; the
answer key only confirms it.

---

## `trace_filter.py` — filter (one step)

```text
scan_id ticket_type amount
  TS009         VIP     66
  TS010          GA     48
  TS011          GA     47
  TS012     presale     40
```

The mask keeps the four Broadway Bites scans and drops every other row. Same
grain (one row per scan), smaller population.

## `trace_derive.py` — clean, then derive a column (one step)

```text
scan_id ticket_type amount  paid  is_large_order
  TS009         VIP     66  66.0            True
  TS010          GA     48  48.0            True
  TS011          GA     47  47.0            True
  TS012     presale     40  40.0            True
  TS022        comp   comp   NaN           False
  TS023        comp    NaN   NaN           False
  TS024          GA     16  16.0           False
```

TS012 at exactly 40 is `True` (the `>= 40` boundary is inclusive). The two comp
scans (TS022 `"comp"`, TS023 blank) coerce to `NaN`, and `NaN >= 40` is `False`,
so they are not large orders. TS024 (16) is simply below the threshold.

## `trace_sort.py` — sort (one step)

```text
scan_id           show       scanned_at
  TS001 Electric Pulse 2025-11-14 19:39
  TS002 Electric Pulse 2025-11-14 19:41
  TS002 Electric Pulse 2025-11-14 19:41
  TS003 Electric Pulse 2025-11-14 19:49
  TS004 Electric Pulse 2025-11-14 19:54
  TS029 Electric Pulse 2025-11-14 20:11
  TS030 Electric Pulse 2025-11-14 23:58
  TS031 Electric Pulse 2025-11-15 00:04
```

The earliest eight scans are the whole 11-14 Electric Pulse night. TS002 shows
up twice — the duplicate gate scan — and the last two straddle midnight (23:58
on the show date, 00:04 the next calendar day). Sorting reordered rows; it
removed nothing.

## `trace_copy.py` — source vs independent copy

```text
SOURCE (unchanged — raw text amount, no is_free):
scan_id amount
  TS022   comp
  TS023    NaN
  TS024     16

WORKING (independent copy — cleaned amount, new is_free):
scan_id  amount  is_free
  TS022     NaN     True
  TS023     NaN     True
  TS024    16.0    False
```

`working = source.copy()` made a separate table. Cleaning `amount` and adding
`is_free` changed only `working`; `source` still has the original text `amount`
and no `is_free` column.

## `trace_chain.py` — two-step chain (filter → sort)

```text
scan_id                 show       scanned_at
  TS001       Electric Pulse 2025-11-14 19:39
  TS005     Latin Fire Night 2025-11-15 19:39
  TS009       Broadway Bites 2025-11-21 19:34
  TS013 Midnight Comedy Hour 2025-11-22 19:38
  TS017     Sunset Jazz Trio 2025-11-28 19:34
  TS025       Electric Pulse 2025-12-06 19:39
```

`step1` (the filter) is the six VIP scans; `step2` (the sort) orders them by
timestamp. The filter picked the population, the sort picked the order.

## `trace_function.py` — successive `if` statements

```text
gate_fee(30, False) -> 2
gate_fee(61, False) -> 7
gate_fee(61, True) -> 0
```

30 is not `> 30`, so the fee stays 2 (inclusive-looking boundary excludes it).
61 trips `> 30` (fee 4) and then `> 60` overwrites it to 7 — both `if`s run. The
comp flag resets the fee to 0 on the last line, whatever it had become.

## `trace_compose.py` — type-hinted composition

```text
mean VIP amount: 58.833333333333336
above 40.0? : True
```

`gate_amounts(vip)` returns the VIP amounts as a Series; `average` reduces it to
the float `58.833…`; `above(58.833…, 40.0)` returns `True`. DataFrame → Series →
float → bool, each boundary type-compatible.

## `unfamiliar_snippet.py` — an untaught construct (`value_counts`)

```text
ticket_type
GA         17
VIP         6
presale     6
comp        3
```

`value_counts()` returns a **Series** whose index is each distinct
`ticket_type` and whose values are how many scans have that type (grain: one row
per ticket type, sorted most-frequent first). It is a preview of the grouped
counting taught in Module 4.
