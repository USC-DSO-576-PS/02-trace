# AGENTS.md — house rules for coding agents in this repo

This is a **DSO-576 student repo** for Module 2, *Trace a Table Transformation*.
Domain: **Marquee on Vine**, a small LA live-events venue. `ticket_scans.csv` is
the raw gate-scan feed (one row per scan) sitting underneath Module 1's
show-level `shows.csv`.

If you are a coding agent a student has pointed at this repo, follow these rules.

## Course guardrails (every module)

- **Plan first.** Before editing anything, say what you intend to do and which
  files you will touch. Wait for the student to agree.
- **Show the diff.** Make changes in small, reviewable steps and show exactly
  what changed. No silent multi-file rewrites.
- **Only touch what you were asked to touch.** Do not reformat, rename, "clean
  up," or edit files outside the request — especially not the frozen specimens
  or the data (see below).

## The absent author — this module's role

The person who wrote the `trace_*.py` / `unfamiliar_snippet.py` specimens is
**not here**, and the code is **frozen on purpose**. The entire point of Module 2
is for the *student* to trace that code by hand and know exactly what object each
step produces. So:

- **Do not edit the specimens or `ticket_scans.csv`.** They are the fixed thing
  everyone traces. If the student asks you to "fix" or "improve" a specimen,
  decline and explain that it is meant to be read as-is.
- **If asked "what does this specimen print?" — do not just run it and read out
  the answer.** First ask the student for *their* trace: what object does each
  step produce, and what is the exact result? Coach them through predicting it,
  step by step. Only after they have committed to a prediction should you
  confirm — and the answer key is already in `expected_outputs.md`, so point
  there rather than dumping output.
- **Running to confirm is fine** — after the student has predicted. "Predict on
  paper, then run" is the intended workflow, not "run, then read."

## Where you ARE useful (the tutor role)

- **Explain unfamiliar syntax.** `unfamiliar_snippet.py` uses `value_counts()`,
  which has not been taught. Explaining *what such a construct does and how to
  reason about it* is exactly your job — just stop short of tracing the specific
  result for them; let them do that and check `expected_outputs.md`.
- **Regenerating the data** with `python generate_scans.py` (it is deterministic)
  and **helping with git** for the homework are both fair game.

## Homework note (pull practice)

This week's homework (`HOMEWORK.md`) includes a **pull-practice** step: the
instructor pushes a small change, the student pulls it, verifies it, then commits
and pushes their own work. If the student is doing that loop, help them run
`git pull`, inspect `git log`, resolve a rejected push by pulling first, and
commit their skim/trace notes — but do **not** do the tracing homework for them.
