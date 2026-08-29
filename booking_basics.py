"""Ordered practice for reading small pandas transformations.

For each cell: inspect the starting object, predict the next object on paper,
then run only that cell. Read from top to bottom.
"""

# %% 1 - values and types from Module 1
subtotal = 18 + 6 * 2
label = "room" + " revenue"
long_enough = subtotal >= 30

subtotal, type(subtotal)
label, type(label)
long_enough, type(long_enough)


# %% 2 - the two literal shapes pandas will use
booking_ids = ["B14", "B08", "B21", "B05"]
first_booking = booking_ids[0]

booking = {"booking_id": "B14", "nights": 2}
booking_nights = booking["nights"]

booking_ids
first_booking
booking
booking_nights


# %% 3 - one DataFrame, one row per booking
import pandas as pd

BOOKINGS = {
    "booking_id": ["B14", "B08", "B21", "B05"],
    "nights": [2, 3, 1, 4],
    "nightly_rate": [180, 125, 250, 95],
}

stays = pd.DataFrame(BOOKINGS, index=[10, 2, 30, 4])
stays
stays.shape
stays.index


# %% 4 - one column versus a list of columns
one_column = stays["nights"]
two_columns = stays[["booking_id", "nights"]]

one_column
two_columns


# %% 5 - labels versus positions
by_label = stays.loc[2, "booking_id"]
by_position = stays.iloc[2, 0]

by_label
by_position


# %% 6 - arithmetic down a column
room_revenue = stays["nights"] * stays["nightly_rate"]
room_revenue


# %% 7 - a comparison makes one boolean per row
long_stay = stays["nights"] >= 2
long_stay


# %% 8 - named steps: filter, derive, sort, select
working = stays.copy()
working["room_revenue"] = room_revenue

eligible = working.loc[long_stay]
ranked = eligible.sort_values("room_revenue", ascending=False)
result = ranked[["booking_id", "room_revenue"]]

eligible
ranked
result


# %% 9 - the same path as a short chain
same_result = (
    working.loc[working["nights"] >= 2]
    .sort_values("room_revenue", ascending=False)
    [["booking_id", "room_revenue"]]
)

same_result
