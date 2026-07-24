"""Generate ticket_scans.csv — the raw gate-scan feed for Marquee on Vine.

Module 1's `shows.csv` was the *show-level* table: one row per performance,
already cleaned and totalled. THIS file is what sits underneath it — the raw
feed from the door scanners: **one row per gate scan**, before anyone cleaned
it up. Aggregate these scans by show and you would rebuild the shows.csv world.

Run this to (re)create ticket_scans.csv. It is fully deterministic (fixed seed,
no external input), so every student's copy is byte-for-byte identical and every
frozen `trace_*.py` specimen prints the exact output recorded in
`expected_outputs.md`.

    python generate_scans.py

Standard library only (`csv`, `random`).

Grain: one row per gate scan.
Columns: scan_id, show, ticket_type, amount, scanned_at

The raw feed carries the mess the S3/S4 sessions need to trace through:
  * unparseable / blank `amount` values — comp tickets scanned as "comp", "n/a",
    or "" (blank). `pd.to_numeric(..., errors="coerce")` turns these into NaN,
    which is why the "clean amount" step comes before any numeric filter.
  * a duplicate row — one ticket scanned twice at the gate (same scan_id, every
    field identical). A raw feed is not deduplicated.
  * boundary values — a Broadway Bites presale at exactly 40 (the inclusive edge
    of an `amount >= 40` "large order" filter), and two Electric Pulse scans that
    straddle midnight (23:58 on the show date, 00:04 the next calendar day).
"""

import csv
import random

SEED = 576
OUT_PATH = "ticket_scans.csv"

# Base General-Admission price per show. VIP = GA + 20, presale = GA - 5,
# comp (complimentary) tickets carry no amount.
SHOWS = {
    "Electric Pulse": 42,
    "Latin Fire Night": 30,
    "Broadway Bites": 45,        # presale = 40 -> the amount>=40 boundary case
    "Midnight Comedy Hour": 35,
    "Sunset Jazz Trio": 28,
    "Open Mic Underground": 15,
}

# (date, show) — a handful of nights inside Module 1's Sep–Dec 2025 season.
PERFORMANCES = [
    ("2025-11-14", "Electric Pulse"),
    ("2025-11-15", "Latin Fire Night"),
    ("2025-11-21", "Broadway Bites"),
    ("2025-11-22", "Midnight Comedy Hour"),
    ("2025-11-28", "Sunset Jazz Trio"),
    ("2025-12-05", "Open Mic Underground"),
    ("2025-12-06", "Electric Pulse"),
]

# The ticket types scanned at each performance (order = scan order at the door).
# Every night has at least one VIP and one presale so the type-based specimens
# always have rows to work with.
TYPES_BY_SHOW = {
    "Open Mic Underground": ["comp", "comp", "GA"],
    "_default": ["VIP", "GA", "GA", "presale"],
}


def price(show, ttype):
    """The amount a scan of this type shows, as a string (raw-feed formatting)."""
    ga = SHOWS[show]
    if ttype == "VIP":
        return ga + 20
    if ttype == "presale":
        return ga - 5
    if ttype == "GA":
        return ga
    return None  # comp — no numeric amount


def main():
    rng = random.Random(SEED)
    rows = []
    counter = 0

    def next_id():
        nonlocal counter
        counter += 1
        return f"TS{counter:03d}"

    for date, show in PERFORMANCES:
        types = TYPES_BY_SHOW.get(show, TYPES_BY_SHOW["_default"])
        # A few nights draw one extra GA walk-up; deterministic via the seed.
        if rng.random() < 0.5:
            types = types + ["GA"]

        minute = 30  # doors at 19:30; each scan a few minutes after the last
        for ttype in types:
            minute += rng.randint(2, 9)
            hour = 19 + minute // 60
            mm = minute % 60
            scanned_at = f"{date} {hour:02d}:{mm:02d}"

            amt = price(show, ttype)
            if ttype == "comp":
                # comp tickets are logged inconsistently by the door staff
                amt_str = rng.choice(["", "comp"])
            else:
                # small ±jitter on paid amounts (never on the boundary presale)
                if not (show == "Broadway Bites" and ttype == "presale"):
                    amt = amt + rng.randint(0, 3)
                amt_str = str(amt)

            rows.append({
                "scan_id": next_id(),
                "show": show,
                "ticket_type": ttype,
                "amount": amt_str,
                "scanned_at": scanned_at,
            })

    # --- Planted rows the sessions trace through -----------------------------

    # (a) An "n/a" comp scan at the 11-14 Electric Pulse night: a third kind of
    #     unparseable amount alongside "" and "comp".
    rows.append({
        "scan_id": next_id(),
        "show": "Electric Pulse",
        "ticket_type": "comp",
        "amount": "n/a",
        "scanned_at": "2025-11-14 20:11",
    })

    # (b) Two Electric Pulse scans straddling midnight (boundary dates): the
    #     23:58 scan on the show date and a late 00:04 entry the next day.
    rows.append({
        "scan_id": next_id(),
        "show": "Electric Pulse",
        "ticket_type": "GA",
        "amount": "44",
        "scanned_at": "2025-11-14 23:58",
    })
    rows.append({
        "scan_id": next_id(),
        "show": "Electric Pulse",
        "ticket_type": "GA",
        "amount": "43",
        "scanned_at": "2025-11-15 00:04",
    })

    # (c) A duplicate scan — one ticket scanned twice at the gate. Same scan_id,
    #     every field identical. Insert the copy right after its original.
    original = next(r for r in rows if r["show"] == "Electric Pulse"
                    and r["ticket_type"] == "GA")
    dup = dict(original)
    rows.insert(rows.index(original) + 1, dup)

    with open(OUT_PATH, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["scan_id", "show", "ticket_type", "amount", "scanned_at"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} scan rows to {OUT_PATH}.")


if __name__ == "__main__":
    main()
