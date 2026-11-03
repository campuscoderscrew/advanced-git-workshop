# Exercise 1: Merge vs rebase

**Goal:** integrate the same feature branch two ways and compare the history each one produces.

## The situation

`feature/discount-codes` was branched off `main` early (right after "Add total_value
calculation"). Since then, `main` gained reports, a CLI and these docs. The feature
branch has 3 commits that `main` doesn't have.

```bash
git lg main feature/discount-codes
```

You should see the two lines of history diverging.

## Part A: merge

```bash
git switch -c merge-practice main
git merge --no-ff feature/discount-codes -m "Merge discount codes feature"
git lg merge-practice
python -m unittest
```

**Notice:**
- A new **merge commit** with two parents ties the histories together.
- Every original commit keeps its original hash. Nothing was rewritten.
- `git log --first-parent merge-practice` shows only the "mainline" view.

## Part B: rebase

```bash
git switch -c rebase-practice feature/discount-codes
git rebase main
git lg rebase-practice
python -m unittest
```

**Notice:**
- The 3 feature commits now sit **on top of** `main`, in a straight line.
- They have **new hashes**. Compare `git log --oneline -3 rebase-practice` with
  `git log --oneline -3 feature/discount-codes`. Same messages, different commits.
- No merge commit.

Now land it on main with a fast-forward:

```bash
git switch -c ff-practice main
git merge --ff-only rebase-practice
git lg ff-practice
```

`--ff-only` succeeds because `ff-practice` is a direct ancestor of `rebase-practice`.
Try `git merge --ff-only feature/discount-codes` from a fresh branch off `main`. It fails. Why?

## Discussion

| | Merge | Rebase |
|---|---|---|
| History shape | Shows what actually happened (branches + merge commits) | Linear, as if work happened sequentially |
| Rewrites commits? | No | Yes (new hashes) |
| Safe on shared branches? | Yes | Only if nobody else has the old commits |
| Conflicts | Resolved once, in the merge commit | Possibly once per replayed commit |

**The golden rule of rebasing:** don't rebase commits that other people have already
pulled. Rebase your own local work; merge shared branches.

## Bonus

- `git pull --rebase` rebases your local commits onto the updated remote branch
  instead of creating a merge commit.
- `git rebase --onto main feature/discount-codes~2 rebase-practice` moves only the
  last 2 commits. Try it on a fresh practice branch and explain the result.
