# Exercise 6: Reflog (recovering "lost" work)

**Goal:** learn that it is very hard to truly lose a commit in git, and how to get one back.

## What the reflog is

Every time `HEAD` or a branch tip moves (commit, checkout, reset, rebase, merge),
git writes an entry in the **reflog**. It's local to your machine and kept for
about 90 days by default. If a commit was ever on your machine, the reflog can
usually find it.

```bash
git reflog              # history of HEAD
git reflog show main    # history of a single branch
```

## Scenario A: "I ran reset --hard and lost two commits"

```bash
git switch -c lost-practice reflog/lost-work
git log --oneline -3          # note the two "CSV export" commits
git reset --hard HEAD~2       # oops
git log --oneline -3          # they're gone!
ls pantry/export.py           # file is gone too
```

Recover:

```bash
git reflog
# a1b2c3d HEAD@{0}: reset: moving to HEAD~2
# e4f5a6b HEAD@{1}: checkout: moving from main to lost-practice   <- the state before
git reset --hard HEAD@{1}     # or use the hash
git log --oneline -3          # back!
```

## Scenario B: "I deleted a branch that wasn't merged"

```bash
git switch main
git branch -D lost-practice
# Deleted branch lost-practice (was e4f5a6b).   <- git even tells you the hash
```

Recover it:

```bash
git reflog | grep lost-practice     # or just look for the hash git printed
git branch lost-practice <hash>
git lg
```

## Scenario C: "My interactive rebase went wrong"

Do exercise 4, finish the rebase, then:

```bash
git reflog
# look for the entry just before "rebase (start)"
git reset --hard HEAD@{n}
```

There's also `ORIG_HEAD`, which git sets before risky operations like reset, rebase
and merge. `git reset --hard ORIG_HEAD` often undoes the most recent one.

## Limits

- Reflog is **local**. A fresh clone has none of your history of moves.
- Changes you never committed (or stashed) aren't in it. Commit early and often.
- Entries expire (`gc.reflogExpire`, default 90 days; 30 for unreachable commits).
