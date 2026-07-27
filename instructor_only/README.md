<!-- INSTRUCTOR ONLY -->

# instructor_only/ — Module 2

Material that backs the trace exercise but must **never ship to students**. When
the public repo `USC-DSO-576-PS/02-trace` is built from `repo/`, this folder is
stripped. In particular, `expected_outputs.md` is the **solution key** — the whole
point of the module is that students trace on paper and confirm by *running* the
specimens (each one prints its own result), not by reading printed answers.

## Files
- `generate_scans.py` — the seeded, deterministic generator that produced
  `../ticket_scans.csv` (fixed seed, standard library only; reproduces the file
  byte-for-byte and encodes the planted mess: the duplicate scan, the
  `amount >= 40` boundary row, the two midnight-straddling scans, and the
  unparseable/blank comp amounts).
- `expected_outputs.md` — the exact printed output of every specimen. **Solution
  key; do not ship.** For the instructor's reference and for regenerating the
  handout answer blanks.

## Reproduce
```bash
cd ..            # run from the repo root so it writes ticket_scans.csv beside the specimens
python instructor_only/generate_scans.py
```
