# Harbor House — front office

Harbor House is a small waterfront hotel. This is its front-office repo, and the
DSO-576 Module 2 repo: one short pandas practice file and two inherited programs
you read, run, and explain.

**New this week: you run Python two different ways.** Some files you run *one
cell at a time* in VS Code's interactive window; others you run *whole* from the
terminal. The table below says which is which, and the sections after it show
exactly how to do each one.

## What's in this repo

| File | What it is | How you run it |
|---|---|---|
| `booking_basics.py` | Small pandas objects to predict and inspect | **Interactive** — one `# %%` cell at a time |
| `arrival_board.py` + `booking_events.csv` | The arrival board you trace together in class | **Terminal** — the whole file |
| `upgrade_offers.py` + `upgrade_candidates.csv` | The upgrade offers you trace on your own | **Terminal** — the whole file |
| `upgrade_policy_memo.md` | The one thing you hand in, to Brightspace | You type in it |
| `AGENTS.md` / `tutor.md` | Guardrails and quiz practice for your agent | Your agent reads them |

You clone this repo, work on your own machine, and never push. Nothing is handed
in through GitHub.

---

## Step 1 — Get the folder open in VS Code

Open a terminal — **Terminal** on Mac (press **Cmd + Space**, type `Terminal`,
press **Enter**) or **Windows PowerShell** on Windows (press the **Windows**
key, type `PowerShell`, press **Enter**) — and paste these lines one at a time:

```text
cd ~/dso576
git clone https://github.com/USC-DSO-576-PS/02-trace.git
cd 02-trace
code .
```

`~/dso576` is the course folder you made in Module 1. If the first line says it
does not exist, run `mkdir ~/dso576` and then `cd ~/dso576`. If `git clone` says
the folder already exists, you already have it — skip that line. If `code` is
not recognized, open VS Code yourself and use **File → Open Folder…** →
the `02-trace` folder → **Open**.

**Open the folder, not the file.** The folder you open is what VS Code, the
terminal, and your agent can all see.

## Step 2 — Build this folder's Python environment (once)

This repo has its **own** environment, separate from your `dso576` home base,
because it needs pandas.

With the `02-trace` folder open in VS Code, open a terminal **inside VS Code**:
menu **Terminal → New Terminal**, or press **Ctrl + `** (the backtick key, above
Tab — **Ctrl**, not Cmd, on a Mac too). A terminal panel opens at the bottom,
already in this folder. Run:

```text
uv sync
```

That creates a hidden `.venv` folder right here with pandas and the Jupyter
kernel in it. It takes a minute the first time and is instant afterwards. It is
always safe to run again.

Get used to that terminal: it is the one that is always in the right place, and
the next section explains why that matters so much this week.

---

## Where the terminal has to be

Almost every "it worked in class but not at home" problem this week is the same
problem: **the terminal is sitting in the wrong folder.**

`arrival_board.py` reads `booking_events.csv` **by name, with no path**. Python
looks for that name in the folder your terminal is *currently in*. If you are
one folder up, in `~/dso576`, there is no `booking_events.csv` there and the
program stops.

**The reliable way to be in the right folder: use VS Code's own terminal.**

1. Open the `02-trace` folder in VS Code (Step 1).
2. Menu: **Terminal → New Terminal** — or press **Ctrl + `** (the backtick key,
   above Tab, on Mac too).
3. A terminal panel opens at the bottom, **already in the folder you opened.**

If you would rather use Mac Terminal or Windows PowerShell directly, get
yourself there by hand first:

```text
cd ~/dso576/02-trace
```

**Lost? Type `pwd` and press Enter.** It prints the folder you are in, on Mac
and on Windows both. It should end in `02-trace`. If it doesn't, `cd` there
before you run anything.

---

## The two ways to run Python this week

### Interactive mode — one cell at a time (`booking_basics.py`)

Use this when you want to **look at one object** and check it against your
prediction. This is the whole point of `booking_basics.py`.

A line that reads exactly `# %%` starts a new **cell**. VS Code runs cells one
at a time and shows you the result of each.

1. In VS Code, open `booking_basics.py`.
2. Click anywhere inside the first cell (the block under the first `# %%`).
3. Press **Shift + Enter**. (Or click the small **Run Cell** link that appears
   just above the `# %%` line.)
4. **The first time only,** VS Code asks which Python to use. Choose the one
   whose path is inside *this* folder:
   - Mac: `~/dso576/02-trace/.venv/bin/python`
   - Windows: `...\dso576\02-trace\.venv\Scripts\python.exe`

   If that option is missing, you have not run `uv sync` yet — run it (Step 2),
   then click the refresh icon in the picker.
5. A pane called the **Python Interactive** window opens beside your code. The
   cell's result appears there — a DataFrame shows as a table.
6. **Shift + Enter** runs the cell and moves your cursor to the next one, so you
   can keep pressing it to walk down the file. **Ctrl + Enter** runs the cell and
   stays put, which is handy when you want to edit and re-run the same cell.

**Predict before you press.** Write down the result, its type, and its shape on
paper first, then run the cell and compare. The point of the exercise is the
gap between the two.

Each cell in `booking_basics.py` ends with a bare name — `stays`, `one_column`,
`result`. That is not a mistake and it is not a `print`: in interactive mode the
last expression of a cell is what gets displayed.

### Terminal mode — the whole file (`arrival_board.py`, `upgrade_offers.py`)

Use this when a file is a **finished program** that prints one answer. These two
files are inherited programs; you read them on paper first, and only then run
them to check your trace.

In a terminal that is in the `02-trace` folder (see above):

```text
uv run python arrival_board.py
```

```text
uv run python upgrade_offers.py
```

`uv run` is what makes pandas available: it uses **this folder's** environment,
the one `uv sync` built. You never have to "activate" anything — but you do have
to be in this folder, because `uv` looks in the folder you are in.

Do the paper trace first. The run is how you check the trace, not a substitute
for it.

### Which mode, and why

| File | Mode | Why |
|---|---|---|
| `booking_basics.py` | Interactive, cell by cell | You are inspecting one object per step |
| `arrival_board.py` | Terminal, whole file | It prints one finished board |
| `upgrade_offers.py` | Terminal, whole file | It prints one finished offer list |

Running `booking_basics.py` from the terminal is not an error, but it prints
**nothing** — bare names only display in the interactive window. If you got a
blank result, you are in the wrong mode for that file, not broken.

---

## If something goes wrong

| What you see | What it means | What to do |
|---|---|---|
| `FileNotFoundError: booking_events.csv` (or `No such file or directory`) | Your terminal is not in the `02-trace` folder | `cd ~/dso576/02-trace`, confirm with `pwd`, run again |
| `ModuleNotFoundError: No module named 'pandas'` | You ran plain `python`, not `uv run python` | Put `uv run` in front: `uv run python arrival_board.py` |
| VS Code says **Select Kernel** or **Select Interpreter** | It does not know which Python to run cells with | Pick the path containing `02-trace/.venv` (see Interactive mode, step 4) |
| The picker has no `02-trace/.venv` option | The environment is not built yet | Run `uv sync` in this folder, then hit refresh in the picker |
| Running `booking_basics.py` prints nothing | That file is for interactive mode | Open it and press **Shift + Enter** on a cell instead |
| `code` is not recognized | VS Code's `code` command is not on your PATH | Open VS Code and use **File → Open Folder…** instead |
| `git clone` says the folder already exists | You already cloned it | Skip the clone; just `cd 02-trace` |
| `uv` is not recognized | The terminal was open before `uv` was installed | Close the terminal window, open a new one, try again |

Still stuck? Ask your agent — it can read this repo. Say what you typed, which
folder you were in (`pwd`), and paste the exact message.

---

## One data note

In `booking_events.csv`, `updated_at` is zero-padded `HH:MM` text from a single
day, so sorting it as text is the same as sorting it by time.

## What you hand in

Complete `upgrade_policy_memo.md` — its five headings and comment prompts are
the instructions — and upload that one file to **Brightspace**. Leave every
comment prompt in place and write your response on the blank line beneath it.

To practice for the quiz, tell your agent: *"Read `tutor.md` and tutor me."*
