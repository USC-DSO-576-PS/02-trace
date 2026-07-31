"""Broadway Bites door list, pulled out of the gate feed.

One show's scans, so the box office can check that night against the printed
manifest.
"""

import pandas as pd

scans = pd.read_csv("ticket_scans.csv")

broadway = scans[scans["show"] == "Broadway Bites"]

print(broadway[["scan_id", "ticket_type", "amount"]].to_string(index=False))
