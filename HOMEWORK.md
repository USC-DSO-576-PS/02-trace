# Module 2 homework

**Hand in one file: `trace_report.md`, uploaded to Brightspace before Quiz 2.**
Nothing is submitted through GitHub. Graded on completion and effort, not
correctness (see the syllabus).

`trace_report.md` is the explainer you send a manager who inherited the scan
pipeline and asked what it actually does. Start from the template in this repo.

## What to do

1. **Trace the specimens on paper first.** Work through `trace_filter.py`,
   `trace_derive.py`, `trace_sort.py`, `trace_copy.py`, `trace_chain.py`,
   `trace_function.py`, and `trace_compose.py` in the handout blanks — what object
   does each step produce, and what is the exact result?

2. **Run each one to confirm.** Every specimen prints its own result, so running
   it *is* the answer key. Where your trace and the run differ, find the step that
   diverged (the tutor helps you locate it — *"read tutor.md and tutor me"* — it
   will not hand you the corrected trace).

3. **Run the pipeline from handout §2.2** over `ticket_scans.csv` in a scratch
   file of your own, and record what you see: row counts, which rows became `NaN`,
   what happens at exactly 40, and the first rows of `summary`.

4. **Fill in `trace_report.md`:**
   - the per-step table — operation, object produced, grain, and the traced values
     you actually saw;
   - two values a reader would misread if nobody flagged them;
   - two or three sentences in your own words on what the pipeline is for;
   - one realistic thing that would break it, what you would see, and how you
     would catch it;
   - one line on what you would check before handing `summary` to someone who
     will act on it.

The traced values and the written paragraphs have to be yours. Everyone in the
section has the same data, so the numbers alone prove nothing — the reading of
them is the work.

## Working locally

```
git diff                                 # the exact lines you changed
git add .
git commit -m "Module 2 trace notes"
```

Clone → edit → diff → commit, all on your own machine. You never push.
