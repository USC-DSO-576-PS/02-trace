# Tonight's ticket holds at the box office.
# Every "# %%" line starts a cell: click in it and press Shift+Enter to run it.
# The commented lines are inspection lines. Work top to bottom: predict on
# paper, un-comment ONE line (remove its #), run the cell, check the value.
# This is how you look under the hood of any code you are handed.

import pandas as pd

# %% a list and a dictionary
seat_counts = [2, 3, 1, 4, 2]
one_hold = {"guest": "Okafor", "seats": 2, "seat_price": 180}
# seat_counts[0]
# one_hold["seats"]

# %% the holds table
holds = pd.DataFrame(
    {
        "guest": ["Okafor", "Reyes", "Lindqvist", "Duarte", "Whitfield"],
        "seats": [2, 3, 1, 4, 2],
        "seat_price": [180, 125, 250, 95, 175],
    },
    index=[41, 2, 19, 30, 12],
)
# holds
# type(holds)

# %% one column vs a list of columns
# holds["guest"]
# holds[["guest", "seats"]]
# type(holds["guest"])

# %% labels vs positions
# holds.loc[2, "seats"]
# holds.iloc[2, 1]
# holds.loc[:19]
# holds.iloc[:2]

# %% a derived column
holds["hold_value"] = holds["seats"] * holds["seat_price"]
# holds

# %% a mask, then a filter
# holds["seats"] >= 2
# holds.loc[holds["seats"] >= 2]

# %% the chain
top_value = (
    holds.loc[holds["seats"] >= 2]
    .sort_values("hold_value", ascending=False)
    ["hold_value"]
)
# top_value
# type(top_value)
