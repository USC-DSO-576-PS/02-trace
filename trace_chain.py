"""The season's VIP scans, earliest first.

The VIP list the house manager asks for after every run.
"""

import pandas as pd

scans = pd.read_csv("ticket_scans.csv")

result = scans[scans["ticket_type"] == "VIP"].sort_values("scanned_at")

print(result[["scan_id", "show", "scanned_at"]].to_string(index=False))
