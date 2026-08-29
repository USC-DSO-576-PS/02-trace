# Tonight's ticket holds at the box office.
# Work top to bottom: add a # %% line above each block, predict, then run it.

import pandas as pd

seat_counts = [2, 3, 1, 4, 2]
seat_counts[0]

one_hold = {"guest": "Okafor", "seats": 2, "seat_price": 180}
one_hold["seats"]

HOLDS = {
    "guest": ["Okafor", "Reyes", "Lindqvist", "Duarte", "Whitfield"],
    "seats": [2, 3, 1, 4, 2],
    "seat_price": [180, 125, 250, 95, 175],
}

holds = pd.DataFrame(HOLDS, index=[41, 2, 19, 30, 12])
holds

holds["guest"]

holds[["guest", "seats"]]

holds.loc[2, "seats"]

holds.iloc[2, 1]

holds["hold_value"] = holds["seats"] * holds["seat_price"]
holds

holds["seats"] >= 2

holds.loc[holds["seats"] >= 2]

top_value = (
    holds.loc[holds["seats"] >= 2]
    .sort_values("hold_value", ascending=False)
    ["hold_value"]
)
top_value
