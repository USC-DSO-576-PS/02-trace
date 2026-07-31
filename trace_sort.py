"""The season's earliest gate scans, by timestamp.

First eight rows — enough to see how opening night ran at the door.
"""

import pandas as pd

scans = pd.read_csv("ticket_scans.csv")

by_time = scans.sort_values("scanned_at")

print(by_time[["scan_id", "show", "scanned_at"]].head(8).to_string(index=False))
