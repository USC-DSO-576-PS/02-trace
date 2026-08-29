# Prints tonight's will-call board: confirmed holds for the show date.

import pandas as pd


def current_will_call(events: pd.DataFrame, show_date: str) -> pd.DataFrame:
    latest = (
        events
        .sort_values("updated_at")
        .drop_duplicates("hold_id")
    )
    on_date = latest.loc[latest["show_date"] == show_date].copy()
    confirmed = on_date.loc[
        on_date["status"] == "confirmed",
        ["hold_id", "guest", "status", "updated_at"],
    ]
    return confirmed.sort_values("guest")


events = pd.read_csv("hold_events.csv")

print(current_will_call(events, "2026-11-14"))
