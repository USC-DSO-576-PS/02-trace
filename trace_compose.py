"""Do VIP scans clear the $40 large-order line on average?

Split into small typed helpers so the season report can reuse the pieces.
"""

import pandas as pd


def gate_amounts(t: pd.DataFrame) -> pd.Series:
    return pd.to_numeric(t["amount"], errors="coerce")


def average(s: pd.Series) -> float:
    return float(s.mean())


def above(x: float, y: float) -> bool:
    return bool(x >= y)


scans = pd.read_csv("ticket_scans.csv")
vip = scans[scans["ticket_type"] == "VIP"]

mean_vip = average(gate_amounts(vip))
answer = above(mean_vip, 40.0)

print("mean VIP amount:", mean_vip)
print("above 40.0? :", answer)
