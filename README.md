# Harbor House - front office

This Module 2 repo has one short pandas practice file and two inherited
front-office programs.

| File | Purpose |
|---|---|
| `booking_basics.py` | Predict and inspect one `# %%` cell at a time. |
| `arrival_board.py` / `booking_events.csv` | Arrival board traced together. |
| `upgrade_offers.py` / `upgrade_candidates.csv` | Upgrade offers traced independently. |
| `upgrade_policy_memo.md` | The one Brightspace deliverable. |
| `AGENTS.md` / `tutor.md` | Guardrails and fresh practice for your agent. |

In `booking_events.csv`, `updated_at` is zero-padded `HH:MM` text from one day,
so sorting it as text is chronological.

For `booking_basics.py`, predict first and press **Shift+Enter** on one cell.
After the paper traces, run:

```text
uv run python arrival_board.py
uv run python upgrade_offers.py
```
