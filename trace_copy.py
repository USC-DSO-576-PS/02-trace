"""Open Mic Underground amounts, raw and cleaned side by side.

The numeric conversion runs on a working copy; both tables get printed.
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
