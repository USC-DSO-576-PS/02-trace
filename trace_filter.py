"""trace_filter.py — ONE step: filter (a boolean mask selects rows).

FROZEN specimen. Do not edit it. Trace it on paper first (what rows survive?),
then run `python trace_filter.py` to confirm against expected_outputs.md.

The mask `scans["show"] == "Broadway Bites"` is a per-row True/False test. The
filter keeps only the True rows. It changes WHICH rows remain; it does not
change the grain — the result is still one row per gate scan.
"""

import pandas as pd

scans = pd.read_csv("ticket_scans.csv")

broadway = scans[scans["show"] == "Broadway Bites"]

print(broadway[["scan_id", "ticket_type", "amount"]].to_string(index=False))
