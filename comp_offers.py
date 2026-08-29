# Prints tonight's comp-upgrade offers: best members first, one offer per seat.

import pandas as pd


def comp_offers(candidates: pd.DataFrame, comp_seats: int) -> pd.DataFrame:
    ranked = candidates.sort_values(
        ["member_points", "arrived_at"],
        ascending=[False, True],
    )
    offers = ranked.loc[: comp_seats - 1]
    return offers[["guest", "member_points"]]


candidates = pd.read_csv("comp_candidates.csv", index_col="hold_id")

print(comp_offers(candidates, 3))
