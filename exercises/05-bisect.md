# Exercise 5: Bisect

**Goal:** find the exact commit that introduced a bug using binary search.

## The situation

On `main`, all tests pass. On `bisect/find-the-bug`, 12 commits later, removing
**all** of an item's stock now raises an error:

```bash
git switch bisect/find-the-bug
python -m unittest
# FAIL / ERROR: test_remove_all_stock
```

Most of the 12 commits just add rows to a data file. One of them broke `remove()`.
You could check them one by one, or let git binary-search: about 4 steps for 12
commits, about 10 steps for 1,000.

## Part A: bisect by hand

```bash
git bisect start
git bisect bad                   # current commit is broken
git bisect good main             # main is known good
```

Git checks out a commit in the middle. Test it and report:

```bash
python -m unittest tests.test_inventory
git bisect good      # if tests pass
git bisect bad       # if tests fail
```

Repeat until git prints `<hash> is the first bad commit`. Then:

```bash
git show <hash>     # see exactly what changed
git bisect reset    # return to where you started
```

## Part B: let git do it (bisect run)

If you have a command that exits 0 for good and non-zero for bad, git can run the
whole search for you:

```bash
git bisect start bisect/find-the-bug main
git bisect run python -m unittest tests.test_inventory
git bisect reset
```

## Questions

1. Which commit was it? Does its message suggest a bug?
2. What exactly is wrong in the diff? (Hint: `>` vs `>=`.)
3. Fix it on a practice branch:
   ```bash
   git switch -c fix-bisect bisect/find-the-bug
   # edit pantry/inventory.py, then
   python -m unittest && git commit -am "Fix remove() rejecting removal of all stock"
   ```
   Or undo the bad commit entirely with `git revert <hash>`. What's the difference?

## Extra

- `git bisect skip` when a commit can't be tested (e.g. it doesn't build).
- `git bisect log` shows your decisions so far; `git bisect visualize` shows what's left.
- Bisect works best when every commit builds and passes tests on its own, one more
  reason to keep history clean (exercise 4).
