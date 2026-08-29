# Harbor House - front office

Harbor House is a small hotel. Each afternoon, the front-office manager needs
an accurate arrival board and a short list of guests to receive the available
complimentary upgrades.

The analyst who wrote the two functions is no longer available. Both programs
run and produce plausible tables. Your job is to predict each intermediate
object, confirm your trace, and explain the business rule the code implements.

## Files

| File | Purpose |
|---|---|
| `booking_basics.py` | Ordered Session 3 `# %%` practice. |
| `arrival_board.py` | Inherited function traced with the class. |
| `booking_events.csv` | Booking-update log, one row per update. |
| `upgrade_offers.py` | Independent function for the upgrade decision. |
| `upgrade_candidates.csv` | Eligible guests, one row per candidate. |
| `upgrade_policy_memo.md` | Manager-facing artifact uploaded to Brightspace. |
| `AGENTS.md` | Standing rules for coding agents in this repo. |
| `tutor.md` | Socratic practice instructions for your agent. |
| `pyproject.toml`, `uv.lock` | The pandas environment used by `uv run`. |

## Run the files

Open the whole folder in VS Code. In `booking_basics.py`, put the cursor in a
cell, write down your prediction, and press **Shift+Enter**. Read the cells from
top to bottom.

After you have committed to a paper trace, run the inherited files from the
terminal:

```text
uv run python arrival_board.py
uv run python upgrade_offers.py
```

The programs print final results as a self-check. The handout holds the trace
procedure and the complete artifact requirements.
