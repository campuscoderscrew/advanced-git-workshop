# Exercise 2: Resolving merge conflicts

**Goal:** trigger a real conflict, read the conflict markers, resolve it, and finish the merge.

## The situation

Two teammates changed the same line of `pantry/reports.py` (`format_line`) on
separate branches, and both updated the same tests:

- `conflict/units` makes lines read `apples: 6 units`
- `conflict/currency` makes lines read `apples: 6 @ $0.50`

The team wants **both**: `apples: 6 units @ $0.50`

## Steps

```bash
git switch -c conflict-practice conflict/units
git merge conflict/currency
```

Git stops with:

```
CONFLICT (content): Merge conflict in pantry/reports.py
CONFLICT (content): Merge conflict in tests/test_reports.py
Automatic merge failed; fix conflicts and then commit the result.
```

Look around before fixing anything:

```bash
git status            # "both modified" files are the conflicts
git diff              # combined diff of the conflicted hunks
```

Open `pantry/reports.py`. You'll see:

```
<<<<<<< HEAD
    return f"{name}: {data['qty']} units"
=======
    return f"{name}: {data['qty']} @ ${data['price']:.2f}"
>>>>>>> conflict/currency
```

- Between `<<<<<<< HEAD` and `=======` is **your** side (the branch you're on).
- Between `=======` and `>>>>>>>` is **their** side (the branch being merged in).

## Resolve it

1. Edit the line to combine both changes and delete all three marker lines:
   ```python
       return f"{name}: {data['qty']} units @ ${data['price']:.2f}"
   ```
2. Do the same in `tests/test_reports.py`: the expected strings become
   `"apples: 6 units @ $0.50"` (two places).
3. Check your work, then mark the files resolved and commit:
   ```bash
   python -m unittest
   git add pantry/reports.py tests/test_reports.py
   git commit            # git pre-fills a merge message
   git lg
   ```

## Useful tools

```bash
git merge --abort                     # bail out, back to before the merge
git checkout --ours   <file>          # take your side for a whole file
git checkout --theirs <file>          # take their side for a whole file
git config --global merge.conflictstyle zdiff3   # also show the original ("base") text
git mergetool                         # open a configured visual merge tool
```

Try it again with `merge.conflictstyle zdiff3` set. The extra `|||||||` section shows
what the line looked like *before* either change, which makes intent much clearer.

## Bonus: the same conflict during a rebase

```bash
git switch -c conflict-rebase conflict/currency
git rebase conflict/units
# resolve the same way, then:
git add pantry/reports.py tests/test_reports.py
git rebase --continue
```

During a rebase, "ours" and "theirs" are **swapped**: "ours" is the branch you're
rebasing onto, "theirs" is your commit being replayed.
