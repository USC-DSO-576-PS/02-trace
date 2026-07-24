"""trace_compose.py — compose type-hinted calls: DataFrame -> Series -> float -> bool.

FROZEN specimen. Do not edit it. Trace it inside-out on paper first, then run.

Read each signature as an intended interface and check the types fit at each
boundary:

    gate_amounts(vip)        DataFrame -> Series   (the VIP amounts, as numbers)
    average(<that Series>)   Series    -> float    (their mean, wrapped to float)
    above(<that float>, 40)  float     -> bool     (mean >= 40 ?)

`float(...)` and `bool(...)` make each pandas scalar match the declared return
type. The Series from `gate_amounts` fits `average`'s parameter; the float from
`average` fits `above`'s first parameter. Trace the compatible call to its exact
runtime value.
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
