"""unfamiliar_snippet.py — one construct we have NOT taught yet.

FROZEN specimen. This is the S4-era workflow: you will hit code that uses
something you have not seen. Try to trace it from its name and the data; if you
cannot, ask your coding agent (its TUTOR role) to *explain what the construct
does* — not to hand you the answer — then confirm by running the file.

`value_counts()` is the unfamiliar piece here. Question to answer before you run:
what object does it return, what is its grain, and what do the numbers mean?
(It is a one-notch-up preview of the grouping/counting you will meet in Module 4.)
"""

import pandas as pd

scans = pd.read_csv("ticket_scans.csv")

counts = scans["ticket_type"].value_counts()

print(counts.to_string())
