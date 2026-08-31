"""Small pandas objects to predict, run, and inspect one cell at a time.

RUN THIS FILE IN INTERACTIVE MODE, NOT FROM THE TERMINAL.

Click inside a cell (a block under a `# %%` line) and press Shift+Enter, or
click the "Run Cell" link above the `# %%`. The result opens in the Python
Interactive window beside your code. Shift+Enter also moves to the next cell;
Ctrl+Enter runs the cell and stays put.

Predict the result, its type, and its shape on paper BEFORE you press.

The first time, VS Code asks which Python to use: choose the one inside this
folder, `02-trace/.venv`. If it is not offered, run `uv sync` here first.

Running this file from the terminal prints nothing, and that is expected: each
cell ends in a bare name, and bare names only display in interactive mode.
See README.md.
"""

# %% Starting table
import pandas as pd

BOOKINGS = {
    "booking_id": ["B14", "B08", "B21", "B05"],
    "nights": [2, 3, 1, 4],
    "nightly_rate": [180, 125, 250, 95],
}

stays = pd.DataFrame(BOOKINGS, index=[10, 2, 30, 4])
stays


# %% One column
one_column = stays["nights"]
one_column


# %% Labels and positions
by_label = stays.loc[2, "booking_id"]
by_position = stays.iloc[2, 0]
(by_label, by_position)


# %% Values down a column
room_revenue = stays["nights"] * stays["nightly_rate"]
room_revenue


# %% A comparison creates labeled True/False values
long_stay = stays["nights"] >= 2
long_stay


# %% Row selection keeps the labels marked True
eligible = stays[long_stay]
eligible


# %% Named steps
working = stays.copy()
working["room_revenue"] = room_revenue
eligible = working[long_stay]
ranked = eligible.sort_values("room_revenue", ascending=False)
result = ranked[["booking_id", "room_revenue"]]
result


# %% The same path as a chain
same_result = (
    working[working["nights"] >= 2]
    .sort_values("room_revenue", ascending=False)
    [["booking_id", "room_revenue"]]
)
same_result
