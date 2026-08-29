"""Complimentary-upgrade offers for Harbor House."""

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
