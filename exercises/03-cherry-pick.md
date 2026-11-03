# Exercise 3: Cherry-pick

**Goal:** copy one specific commit from one branch onto another, without bringing anything else along.

## The situation

Version 1.0 shipped from `release/1.0` (also tagged `v1.0`). A customer reports the
inventory total is sometimes off by a cent.

Sam fixed it on `bugfix/rounding`, but that branch also contains a debug-print
commit and an unfinished experiment that must **not** go into a release:

```bash
git log --oneline main..bugfix/rounding
```

```
xxxxxxx Experimental: start moving prices to Decimal
xxxxxxx Fix total_value dropping a cent due to float truncation
xxxxxxx WIP: debug output while investigating totals
```

Merging the branch would bring all three. You only want the fix.

## Steps

See the bug first:

```bash
git switch -c release-practice release/1.0
python -c "from pantry.inventory import Inventory as I; i=I(); i.add('milk',1,1.15); print(i.total_value())"
# prints 1.14  (should be 1.15)
```

Find the fix commit's hash and cherry-pick it:

```bash
git log --oneline --grep="Fix total_value" bugfix/rounding
git cherry-pick -x <hash>
```

Verify:

```bash
git lg release-practice bugfix/rounding
git show --stat HEAD           # only inventory.py and its test changed
python -m unittest
```

The `-x` flag appends `(cherry picked from commit ...)` to the message, which is
a nice breadcrumb for whoever reads the release history later.

## Things to notice

- The new commit on `release-practice` has a **different hash** from the original.
  Same change, different parent, so a different commit.
- `pantry/money.py` and the `DEBUG` print are not on your branch.

## Variations to try

```bash
git cherry-pick A..B            # a range (excludes A, includes B)
git cherry-pick --no-commit <h> # apply the change but let you edit before committing
git cherry-pick --abort         # if it conflicts and you want out
```

## When to cherry-pick (and when not to)

Good for: backporting a fix to a release branch, rescuing one commit from an
abandoned branch.

Avoid as a habit for moving work between active branches. You end up with duplicate
commits that can cause confusing conflicts when the branches are merged later.

## Related: revert

`git revert <hash>` is cherry-pick's mirror image: it creates a new commit that
**undoes** a commit. See exercise 7.
