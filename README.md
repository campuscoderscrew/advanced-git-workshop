# Advanced Git Workshop

Hands-on practice for the git commands that go beyond `add`, `commit` and `push`.
This repo contains a tiny Python project (**pantry**, an inventory tracker) and a
set of branches, each set up for one exercise.

You don't need to know Python. The code is there so the history means something,
and so tests can tell you when something is broken.

## Setup

```bash
git clone https://github.com/campuscoderscrew/advanced-git-workshop.git
cd advanced-git-workshop

# Fetch every exercise branch so they exist locally
git fetch --all

# Optional but recommended: a readable log alias
git config --global alias.lg "log --oneline --graph --decorate --all"

# Check the tests run (Python 3.8+)
python -m unittest        # use python3 on macOS/Linux if needed
```

Run `git lg` constantly. Watching the graph change is most of the learning.

## Exercises

| # | Topic | Branches used | Guide |
|---|-------|---------------|-------|
| 1 | Merge vs rebase | `feature/discount-codes`, `main` | [exercises/01-merge-vs-rebase.md](exercises/01-merge-vs-rebase.md) |
| 2 | Resolving merge conflicts | `conflict/units`, `conflict/currency` | [exercises/02-merge-conflicts.md](exercises/02-merge-conflicts.md) |
| 3 | Cherry-pick | `bugfix/rounding`, `release/1.0` | [exercises/03-cherry-pick.md](exercises/03-cherry-pick.md) |
| 4 | Interactive rebase (clean up history) | `feature/messy-history` | [exercises/04-interactive-rebase.md](exercises/04-interactive-rebase.md) |
| 5 | Bisect (find the commit that broke it) | `bisect/find-the-bug` | [exercises/05-bisect.md](exercises/05-bisect.md) |
| 6 | Reflog (recover "lost" work) | `reflog/lost-work` | [exercises/06-reflog-recovery.md](exercises/06-reflog-recovery.md) |
| 7 | Undoing things: revert, reset, restore, stash | `main` | [exercises/07-undo-and-stash.md](exercises/07-undo-and-stash.md) |

## Golden rule for this workshop

**Always do exercises on a practice branch you create yourself**, for example:

```bash
git switch -c my-rebase feature/discount-codes
```

That way the original exercise branches stay intact and you can repeat an exercise
as many times as you like.

## Messed up? Reset an exercise

```bash
git rebase --abort        # if you are mid-rebase
git merge --abort         # if you are mid-merge
git cherry-pick --abort   # if you are mid-cherry-pick
git bisect reset          # if you are mid-bisect

git switch main
git branch -D my-practice-branch     # delete your practice branch
git fetch origin
git switch -C feature/discount-codes origin/feature/discount-codes   # restore an exercise branch
```

## The project

```
pantry/
  inventory.py   Inventory model: add, remove, quantity, total_value
  reports.py     low-stock and stock reports
  cli.py         demo:  python -m pantry.cli
tests/           unittest tests:  python -m unittest
exercises/       step-by-step guides
```
