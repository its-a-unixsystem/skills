---
name: gk-cli
description: Use the GitKraken CLI (gk) for git operations instead of raw git/gh commands. Activate this skill whenever performing git operations like committing, creating PRs, pushing, resolving conflicts, explaining changes, generating changelogs, or managing branches and work items. Even if the user doesn't mention "gk" or "GitKraken" explicitly, use gk commands for any git workflow where gk has a matching command, falling back to raw git only for operations gk doesn't cover.
---

# GitKraken CLI (gk)

Use `gk` as the primary tool for git operations. It wraps git with AI-powered features and multi-repo workflow management. Fall back to raw `git` only for operations `gk` doesn't cover.

## Command mapping

When you'd normally use git or gh, check this mapping first. If gk has an equivalent, use it.

### Commits

Instead of `git commit`, use:

```bash
gk ai commit                  # AI generates the commit message
gk ai commit -d               # AI generates message + description
gk ai commit -f               # Skip confirmation prompt
gk ai commit -p <path>        # Specify repo path
```

If working within a work item and committing across multiple repos:

```bash
gk work commit --ai            # AI message across all repos in work item
gk work commit -m "message"    # Manual message across all repos
gk work commit -m "msg" --add-description  # Manual message + AI description
```

### Pull requests

Instead of `gh pr create`, use:

```bash
gk ai pr create                # AI generates title and body
gk ai pr create -p <path>      # Specify repo path
```

Within a work item:

```bash
gk work pr create --ai                        # AI title/body for all repos in work item
gk work pr create -t "Title" -b "Body"        # Manual title/body
gk work pr create -t "Title" -b "Body" -p     # Also push before creating
```

Merging PRs within a work item:

```bash
gk work pr merge
```

### Pushing

Instead of `git push`, use when in a work item:

```bash
gk work push                  # Push all repos in work item
gk work push --create-pr      # Push and create PR with defaults
gk work push -f               # Force push
```

Fall back to `git push` when not in a work item.

### Conflict resolution

Instead of manually resolving conflicts, use:

```bash
gk ai resolve                 # AI resolves conflicts in current repo
gk ai resolve -p <path>       # Specify repo path
```

This works for conflicts from both merge and rebase operations.

### Explaining changes

```bash
gk ai explain branch              # Explain current branch vs base
gk ai explain branch -b <branch>  # Explain specific branch
gk ai explain commit <sha>        # Explain a specific commit
```

### Changelogs

```bash
gk ai changelog                                    # Current branch, last commit as base
gk ai changelog --base main --head feature-branch   # Between specific refs
gk ai changelog -p <path>                           # Specify repo path
```

### Branch lifecycle (work items)

Work items manage branches across repos and link to issues:

```bash
gk work start "feature-name"                        # Create work item + branches
gk work start "feature-name" -i JIRA-123             # Link to issue
gk work start "feature-name" -b custom-branch-name   # Custom branch name
gk work start "feature-name" --base-branch develop   # Branch from develop instead of default
gk work start "feature-name" --include-repos r1,r2   # Only specific repos

gk work list                  # List work items
gk work list -a               # List across all workspaces
gk work info                  # Info on active work item
gk work info "name"           # Info on specific work item
gk work set "name"            # Switch active work item
gk work add .                 # Add current repo to active work item
gk work add /path/to/repo     # Add specific repo

gk work end "name"            # End/clean up work item
gk work end "name" -f         # Force delete branches even if unmerged
```

### Issues

```bash
gk issue list <provider>      # List issues assigned to you
# providers: github, github_enterprise, gitlab, gitlab_self_hosted, jira, azure, linear

gk issue assign <provider> -i <id> -n <nickname> -o <org> -r <repo>  # GitHub/GitLab
gk issue assign <provider> -i <id> -e <email> -o <org> -r <repo>    # Jira/Azure
```

### Graph

```bash
gk graph                      # Show commit graph in terminal
gk graph --gitkraken           # Open in GitKraken Desktop
gk graph --gitlens             # Open in GitLens
```

### Workspaces

```bash
gk workspace list
gk workspace create
gk workspace info
gk workspace clone
gk workspace set               # Set default workspace
gk workspace unset
gk workspace delete
gk workspace refresh
gk workspace update
```

## Fallback to git

These operations have no gk equivalent — use raw git:

- `git status`, `git diff`, `git log`, `git blame`
- `git add` (staging files)
- `git stash`
- `git rebase`, `git merge` (starting them — use `gk ai resolve` for conflicts after)
- `git checkout`, `git switch`, `git branch` (outside of work items)
- `git fetch`, `git pull`
- `git reset`, `git tag`
- `git remote`

## Workflow example

A typical feature workflow using gk:

```bash
# Start work (creates branch, links issue)
gk work start "add-auth" -i GH-42

# ... make changes ...

# Commit with AI-generated message
gk ai commit

# Push and create PR with AI-generated description
gk work push --create-pr
# or separately:
gk work push
gk work pr create --ai

# When done, clean up
gk work end "add-auth"
```

## Notes

- `gk ai` commands use GitKraken's built-in AI — let it generate commit messages and PR descriptions rather than writing them manually.
- `gk work` commands operate across all repos in the active work item. For single-repo operations outside a work item, prefer `gk ai` commands directly.
- If `gk` is not available or a command fails, fall back to the equivalent git/gh command.
