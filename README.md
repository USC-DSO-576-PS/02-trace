# Harbor House - front office

This Module 2 repo has one short pandas practice file and two inherited
front-office programs.

| File | Purpose | How to run it |
|---|---|---|
| `booking_basics.py` | Predict and inspect one `# %%` cell at a time. | Interactive |
| `arrival_board.py` / `booking_events.csv` | Arrival board traced together. | Terminal |
| `upgrade_offers.py` / `upgrade_candidates.csv` | Upgrade offers traced independently. | Terminal |
| `upgrade_policy_memo.md` | The one Brightspace deliverable. | You type in it |
| `AGENTS.md` / `tutor.md` | Guardrails and fresh practice for your agent. | Your agent reads them |

**Interactive** means: open the file in VS Code, click inside a cell (the block
under a `# %%` line), predict, then press **Shift + Enter**. The result appears
in the Interactive window beside your code. If VS Code asks which Python to use,
pick the one in this folder, `02-trace/.venv`.

**Terminal** means: open a terminal with **Terminal -> New Terminal** in VS
Code, or **Ctrl + `** (the backtick key above Tab - `Ctrl`, not `Cmd`, on a Mac
too). It opens in this folder, which is where these have to run:

```text
uv run python arrival_board.py
uv run python upgrade_offers.py
```

Using Mac Terminal or Windows PowerShell instead? `cd ~/dso576/02-trace` first,
or the program will not find its CSV. `pwd` prints where you are.

In `booking_events.csv`, `updated_at` is zero-padded `HH:MM` text from one day,
so sorting it as text is chronological.
