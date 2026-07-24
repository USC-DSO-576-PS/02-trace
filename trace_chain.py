"""trace_chain.py — unpack a two-step method chain into named steps.

FROZEN specimen. Do not edit it. Trace it on paper first, then run to confirm.

The one chained line

    result = scans[scans["ticket_type"] == "VIP"].sort_values("scanned_at")

is really two steps. Each call's result immediately becomes the object the next
call works on:

    step1 = scans[scans["ticket_type"] == "VIP"]   # filter  -> the VIP scans
    result = step1.sort_values("scanned_at")        # sort    -> earliest first

The filter chooses the population (every VIP scan); the sort only orders those
rows. Reading the chain = reading step1, then reading what step2 does TO step1.
"""

import pandas as pd

scans = pd.read_csv("ticket_scans.csv")

result = scans[scans["ticket_type"] == "VIP"].sort_values("scanned_at")

print(result[["scan_id", "show", "scanned_at"]].to_string(index=False))
