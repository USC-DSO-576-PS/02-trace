"""Door take for the period, off the raw scanner feed.

Keeps the scans that carry a paid amount, flags the large orders, and ranks
everything high to low so the box office can read the top of the list at a
glance. Run it from the repo root:

    python door_report.py

Written for the fall season wrap, rerun each period since.  -- R. Salas
"""

import pandas as pd

raw       = pd.read_csv("ticket_scans.csv")
clean     = raw.copy()
clean["paid"] = pd.to_numeric(clean["amount"], errors="coerce")
paid_only = clean[clean["paid"].notna()].copy()
paid_only["is_large_order"] = paid_only["paid"] >= 40
summary   = paid_only.sort_values("paid", ascending=False)

# Top of the list is what the box office actually reads.
print(summary[["scan_id", "show", "ticket_type", "paid", "is_large_order"]]
      .head(10).to_string(index=False))
print()
print(f"{len(summary)} paid scans · ${summary['paid'].sum():.0f} door take · "
      f"{int(summary['is_large_order'].sum())} large orders")
