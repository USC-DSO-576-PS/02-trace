"""trace_sort.py — ONE step: sort (reorder rows, same population).

FROZEN specimen. Do not edit it. Trace it on paper first, then run to confirm.

`sort_values("scanned_at")` reorders every row by its scan timestamp, earliest
first. Sorting changes the ORDER of the rows, never which rows are present. The
first eight rows are the 11-14 Electric Pulse night — including the duplicate
scan (TS002 appears twice) and the two scans that straddle midnight: 23:58 on
the show date, then 00:04 logged the next calendar day.
"""

import pandas as pd

scans = pd.read_csv("ticket_scans.csv")

by_time = scans.sort_values("scanned_at")

print(by_time[["scan_id", "show", "scanned_at"]].head(8).to_string(index=False))
