# Module 2 homework

Graded on completion and effort, not correctness (see the syllabus). Push it
before Quiz 2 day.

## 1. Finish the in-class Try blocks

- **S3 — skim for the story.** For `ticket_scans.csv`, write one plain-English
  line per step of the `read_csv → clean amount → filter invalid rows → derive
  is_large_order → sort` pipeline: input object, action, output/grain, business
  role. No exact arithmetic — this is the story, not the numbers. Put your lines
  in a `skim.md` (or the handout).
- **S4 — trace `trace_function.py` by hand.** Before running it, write the exact
  return value of `gate_fee(30, False)`, `gate_fee(61, False)`, and
  `gate_fee(61, True)`, and one sentence on why swapping the two weight checks
  would change a result. Then run it and reconcile.

You are welcome to trace the other specimens too and check yourself against
`expected_outputs.md` — but the two above are the ones to hand in.

## 2. Pull practice (the named extra)

This is the one new mechanic this week: **pulling a teammate's change before you
push your own.** Keep it simple.

1. Sometime before the quiz, the instructor pushes a small change to your repo —
   a new frozen specimen (e.g. `trace_pull.py`) or a tweak to the data.
2. **Pull it down:**

   ```bash
   git pull
   ```

3. **Verify it landed:** `git log --oneline -3` should show the instructor's
   commit; run any new specimen and check it against its expected output.
4. **Do your own small work on top** — e.g. add your `skim.md` and your
   hand-trace — then commit and push:

   ```bash
   git add .
   git commit -m "S3 skim + S4 hand-trace; pulled instructor change"
   git push
   ```

That's the whole loop: **pull → verify → commit your work → push.** You named
`pull`/`sync` in Session 1; this is the hands-on version. If the push is
rejected because you had not pulled first, that rejection *is* the lesson — pull,
then push again.
