"""Interactive reading lab for Module 2.

Open this file in VS Code. For each cell: predict the printed value and type on
paper, then run only that cell with Shift+Enter. Read the cells in order.
"""

# %% 1 — values and types from Module 1
subtotal = 18 + 6 * 2
label = "door" + " take"
clears_line = subtotal >= 30

print(subtotal, type(subtotal))
print(label, type(label))
print(clears_line, type(clears_line))


# %% 2 — the two literal shapes pandas will use
columns = ["scan_id", "amount"]
ticket = {"scan_id": "A17", "amount": 27}

print(columns, type(columns))
print(columns[0], type(columns[0]))
print(ticket, type(ticket))
print(ticket["amount"], type(ticket["amount"]))


# %% 3 — Series is one-dimensional; DataFrame is two-dimensional
import pandas as pd

orders = pd.DataFrame(
    {
        "order_id": ["A17", "B04", "C22", "D09"],
        "channel": ["web", "door", "web", "door"],
        "amount": [27, 40, 18, 55],
    },
    index=["north", "south", "east", "west"],
)

one_column = orders["amount"]
two_columns = orders[["order_id", "amount"]]

print(type(one_column), one_column.ndim)
print(type(two_columns), two_columns.ndim)
print(two_columns)


# %% 4 — read the brackets from the inside out
chosen_columns = ["order_id", "amount"]
selected = orders[chosen_columns]

print(chosen_columns, type(chosen_columns))
print(selected, type(selected))


# %% 5 — loc uses labels; iloc uses integer positions
by_label = orders.loc["south", "amount"]
by_position = orders.iloc[1, 2]
two_rows = orders.loc[["north", "west"], ["order_id", "amount"]]

print(by_label, type(by_label))
print(by_position, type(by_position))
print(two_rows, type(two_rows))


# %% 6 — a comparison makes a boolean Series; brackets filter rows
door_mask = orders["channel"] == "door"
door_orders = orders.loc[door_mask, ["order_id", "amount"]]

print(door_mask, type(door_mask))
print(door_orders, type(door_orders))


# %% 7 — copy, then derive a column on the working table
working = orders.copy()
working["fee"] = working["amount"] * 0.05

print(orders)
print(working[["order_id", "amount", "fee"]])


# %% 8 — named steps before a chain
high = working[working["amount"] >= 27]
ranked = high.sort_values("amount", ascending=False)
result = ranked[["order_id", "amount", "fee"]]

print(result)


# %% 9 — the same short path as a chain
same_result = (
    working.loc[working["amount"] >= 27, ["order_id", "amount", "fee"]]
    .sort_values("amount", ascending=False)
)

print(same_result)
print(result.equals(same_result))


# %% 10 — type hints describe intended handoffs
def amount_column(table: pd.DataFrame) -> pd.Series:
    return table["amount"]


def average(values: pd.Series) -> float:
    return float(values.mean())


def at_least(value: float, threshold: float) -> bool:
    return bool(value >= threshold)


mean_amount = average(amount_column(orders))
answer = at_least(mean_amount, 35.0)

print(mean_amount, type(mean_amount))
print(answer, type(answer))


# %% 11 — every successive if is tested
def gate_fee(amount: float, complimentary: bool) -> int:
    fee = 2
    if amount > 30:
        fee = 4
    if amount > 60:
        fee = 7
    if complimentary:
        fee = 0
    return fee


print(gate_fee(30, False))
print(gate_fee(61, False))
print(gate_fee(61, True))
