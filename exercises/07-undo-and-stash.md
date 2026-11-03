# Exercise 7: Undoing things (revert, reset, restore) and stash

**Goal:** pick the right "undo" for the situation.

```bash
git switch -c undo-practice main
```

## restore: discard uncommitted changes

```bash
echo "# scratch" >> pantry/cli.py
git status
git restore pantry/cli.py          # throw away working-tree changes

echo "# scratch" >> pantry/cli.py
git add pantry/cli.py
git restore --staged pantry/cli.py # unstage, keep the edit
git restore pantry/cli.py          # now discard it
```

## reset: move the branch pointer (rewrites local history)

```bash
git log --oneline -3
git reset --soft HEAD~1    # undo last commit, keep changes STAGED
git status
git commit -m "Recommit it"

git reset --mixed HEAD~1   # (default) undo commit, keep changes UNSTAGED
git status
git add -A && git commit -m "Recommit it again"

git reset --hard HEAD~1    # undo commit AND discard changes (reflog can save you)
```

| Mode | Branch pointer | Staging area | Working files |
|------|----------------|--------------|---------------|
| `--soft` | moved | kept | kept |
| `--mixed` | moved | reset | kept |
| `--hard` | moved | reset | **reset** |

## revert: undo a commit safely on a shared branch

`revert` does not rewrite history. It adds a new commit that is the inverse of an old one.

```bash
git reset --hard main        # start fresh
git log --oneline            # pick "Add demo CLI entry point"
git revert <hash>
git log --oneline -2
ls pantry/cli.py             # gone, via a new commit
git revert HEAD              # revert the revert: cli.py is back
```

**Rule of thumb:** pushed and shared? `revert`. Local only? `reset` is fine.

## stash: shelve work in progress

You're mid-change and need to switch branches *right now*:

```bash
echo "# half-done idea" >> pantry/reports.py
git stash push -m "report idea"
git status                   # clean
git switch release/1.0       # do something urgent...
git switch undo-practice
git stash list
git stash pop                # changes are back
```

More:

```bash
git stash -u                 # include untracked files
git stash show -p stash@{0}  # inspect a stash
git stash apply stash@{1}    # apply without removing from the list
git stash drop stash@{0}
git stash branch new-branch  # turn a stash into a branch
```

## Bonus: amend

```bash
git commit --amend           # fix the last commit's message or add forgotten files
```

Amend rewrites the last commit, so the same rules as rebase apply once it's pushed.
