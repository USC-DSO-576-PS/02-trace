"""Flag the large orders on the gate feed.

`amount` comes off the scanner as text, so it is converted to a number before
anything compares it to the $40 large-order line.
"""

import pandas as pd

scans = pd.read_csv("ticket_scans.csv")

scans["paid"] = pd.to_numeric(scans["amount"], errors="coerce")
scans["is_large_order"] = scans["paid"] >= 40

# Spot-check two nights.
look = scans[scans["show"].isin(["Broadway Bites", "Open Mic Underground"])]
print(look[["scan_id", "ticket_type", "amount", "paid", "is_large_order"]].to_string(index=False))
