# Exercise 4: Interactive rebase

**Goal:** turn a messy branch history into clean, reviewable commits before opening a pull request.

## The situation

`feature/messy-history` adds a search feature. The code works, but the history is
what real work looks like:

```bash
git log --oneline main..feature/messy-history
```

```
xxxxxxx fix typo again
xxxxxxx WIP please work
xxxxxxx oops forgot to add tests
xxxxxxx fix typo
xxxxxxx wip
xxxxxxx add search
```

Reviewers would rather see two commits:

1. `Add case-insensitive inventory search`
2. `Add tests for inventory search`

## Steps

```bash
git switch -c tidy-practice feature/messy-history
git rebase -i main
```

> Tip: if a terminal editor you don't know opens (vim), you can set a friendlier one first:
> `git config --global core.editor "code --wait"` (VS Code) or `"nano"`.

Git opens a todo list, **oldest commit first**:

```
pick aaaaaaa add search
pick bbbbbbb wip
pick ccccccc fix typo
pick ddddddd oops forgot to add tests
pick eeeeeee WIP please work
pick fffffff fix typo again
```

Edit it to this (reorder lines, change the verbs):

```
reword aaaaaaa add search
fixup  bbbbbbb wip
fixup  ccccccc fix typo
fixup  eeeeeee WIP please work
reword ddddddd oops forgot to add tests
fixup  fffffff fix typo again
```

Save and close. Git will stop twice to let you write the new messages for the
two `reword` commits.

| Verb | Meaning |
|------|---------|
| `pick` | keep the commit as is |
| `reword` | keep the change, edit the message |
| `squash` | meld into the previous commit, combine messages |
| `fixup` | meld into the previous commit, discard this message |
| `edit` | stop here so you can amend or split the commit |
| `drop` | delete the commit |

## Verify

```bash
git log --oneline main..tidy-practice     # 2 commits
python -m unittest
git diff feature/messy-history tidy-practice   # no output: same final code
```

That last command is the key insight: **interactive rebase changed the history,
not the result.**

## The fixup workflow (do this in real life)

Instead of making "fix typo" commits and cleaning up later, mark them as you go:

```bash
git commit --fixup=<hash-of-commit-being-fixed>
git rebase -i --autosquash main     # fixups are pre-arranged for you
```

## Safety

- Only rewrite commits that haven't been shared, or that only you work on.
- If you already pushed the branch, you need `git push --force-with-lease`
  (never plain `--force`; `--force-with-lease` refuses if someone else pushed meanwhile).
- Panic button: `git rebase --abort`. Already finished and regret it? See exercise 6 (reflog).
