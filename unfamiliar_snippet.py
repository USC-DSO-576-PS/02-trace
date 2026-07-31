"""Sanity check on the gate feed: how many rows carry each scan_id.

Worth a look before anyone quotes a count off this file.
"""

import pandas as pd

scans = pd.read_csv("ticket_scans.csv")

counts = scans["scan_id"].value_counts()

print(counts.head().to_string())
