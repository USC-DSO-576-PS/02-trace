"""trace_derive.py — clean the amount, then ONE step: a derived column.

FROZEN specimen. Do not edit it. Trace it on paper first, then run to confirm.

`amount` arrives as raw text: numbers like "48", but also "comp", "n/a", or a
blank for complimentary tickets. `pd.to_numeric(..., errors="coerce")` cleans it
to a real number, turning anything unparseable into NaN (a missing value).

The step this file is about is the LAST line — the derived column
`is_large_order`. It is a new field computed per row from an existing one.
Watch two edges:
  * 40 is a "large order": the test is `>= 40`, and the boundary is inclusive.
  * A NaN amount does not pass `>= 40` — a comparison against a missing value is
    False, so comp/blank scans are not large orders.
"""

import pandas as pd

scans = pd.read_csv("ticket_scans.csv")

scans["paid"] = pd.to_numeric(scans["amount"], errors="coerce")   # clean
scans["is_large_order"] = scans["paid"] >= 40                     # the derived column

# Show a readable slice: Broadway Bites (a 40 boundary) and Open Mic (NaN comps).
look = scans[scans["show"].isin(["Broadway Bites", "Open Mic Underground"])]
print(look[["scan_id", "ticket_type", "amount", "paid", "is_large_order"]].to_string(index=False))
