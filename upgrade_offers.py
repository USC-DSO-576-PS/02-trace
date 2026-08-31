"""Complimentary-upgrade offers for Harbor House.

RUN THIS FILE FROM THE TERMINAL, AS A WHOLE, AFTER YOUR PAPER TRACE:

    uv run python upgrade_offers.py

The terminal must be in the `02-trace` folder: this file reads
`upgrade_candidates.csv` by name, so Python looks for it in the folder you are
currently in. In VS Code, Terminal -> New Terminal opens there already.
Type `pwd` to check; it should end in `02-trace`. See README.md.
"""

import pandas as pd


def upgrade_offers(
    candidates: pd.DataFrame,
    rooms_available: int,
) -> pd.DataFrame:
    ranked = candidates.sort_values(
        "tier_points",
        ascending=False,
    )
    offers = ranked.loc[: rooms_available - 1]
    return offers[
        ["guest_id", "tier_points", "checked_in_at", "stay_nights"]
    ]


upgrade_candidates = pd.read_csv(
    "upgrade_candidates.csv",
    index_col="candidate_index",
)
print(upgrade_offers(upgrade_candidates, 2))
