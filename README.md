# Marquee on Vine — front of house

Marquee on Vine is a small live-events venue off Hollywood Boulevard. This is
the front-of-house working repo and the DSO-576 Module 2 repo.

Guests reserve seats as **ticket holds**. Before each show, the front of
house runs two inherited programs the last analyst left behind: one prints
the **will-call board** (who picks up tickets tonight), the other prints the
**comp-upgrade offers** (which members are offered tonight's spare premium
seats). Both run cleanly and print plausible tables. Your job this module is
to know exactly what object every step produces.

## Files

| File | What it is |
|---|---|
| `hold_basics.py` | Your ordered practice file: `# %%` cells with commented inspection lines. Predict, run, un-comment, check. |
| `will_call_board.py` | Inherited program: the will-call board for a show date. Traced together in class. |
| `hold_events.csv` | The hold-update log it reads: one row per update to a hold. |
| `comp_offers.py` | Inherited program: tonight's comp-upgrade offers. You trace this one yourself. |
| `comp_candidates.csv` | The member table it reads, keyed by hold number. |
| `comp_memo.md` | The one-file deliverable you complete and upload to Brightspace. |
| `AGENTS.md` | Standing rules for coding agents working in this repo. |
| `tutor.md` | Instructions for asking your own agent to tutor you. |
| `pyproject.toml`, `uv.lock` | The pandas environment used by `uv run`. |

## Run things

Open the whole folder in VS Code. In `hold_basics.py`, every `# %%` line
starts a cell: click in a cell and press **Shift+Enter** to run it. Work top
to bottom — predict, run, then un-comment one inspection line at a time and
check it against your prediction.

Run the two inherited programs from the terminal, after you have committed to
a paper trace:

```text
uv run python will_call_board.py
uv run python comp_offers.py
```

Timestamps in the data are zero-padded text (`2026-11-09 11:20`), so sorting
them as text puts them in time order.
