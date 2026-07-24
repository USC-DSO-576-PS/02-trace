"""trace_copy.py — a working table is INDEPENDENT of its source.

FROZEN specimen. Do not edit it. Trace it on paper first, then run to confirm.

`working = source.copy()` makes a separate DataFrame. Cleaning `amount` and
adding an `is_free` column on `working` changes ONLY `working`. `source` keeps
its original text `amount` and never gains `is_free`. Compare the two prints:
same rows, different columns and values — because they are two independent
objects, not two names for one table.
"""

import pandas as pd

scans = pd.read_csv("ticket_scans.csv")

source = scans[scans["show"] == "Open Mic Underground"][["scan_id", "amount"]].copy()
working = source.copy()

working["amount"] = pd.to_numeric(working["amount"], errors="coerce")
working["is_free"] = working["amount"].isna()

print("SOURCE (unchanged — raw text amount, no is_free):")
print(source.to_string(index=False))
print()
print("WORKING (independent copy — cleaned amount, new is_free):")
print(working.to_string(index=False))
