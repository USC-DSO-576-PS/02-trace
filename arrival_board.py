"""Inherited arrival-board logic for Harbor House."""

import pandas as pd


def arrival_board(
    events: pd.DataFrame,
    report_date: str,
) -> pd.DataFrame:
    ordered = events.sort_values("updated_at")

    current = ordered.drop_duplicates("booking_id")

    on_date = current[current["arrival_date"] == report_date].copy()

    confirmed = on_date[on_date["status"] == "confirmed"]

    result = confirmed[
        ["booking_id", "guest_name", "room_type", "updated_at"]
    ]

    return result.sort_values("guest_name")


booking_events = pd.read_csv("booking_events.csv", index_col="event_index")
print(arrival_board(booking_events, "2026-09-12"))
