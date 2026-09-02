import pandas as pd


def arrival_list(bookings: pd.DataFrame, report_date: str) -> pd.DataFrame:
    on_date = bookings[bookings["arrival_date"] == report_date].copy()
    confirmed = on_date[on_date["status"] == "confirmed"]
    result = confirmed[
        ["booking_id", "guest_name", "room_type"]
    ]
    return result.sort_values("guest_name")
