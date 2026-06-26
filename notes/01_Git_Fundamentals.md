# Git Fundamentals

## Purpose
Git is a version control system that records the history of a project by creating snapshots called commits. It allows you to track changes, recover from mistakes, and collaborate with others. Git runs locally on your computer, while GitHub is a service that hosts Git repositories online.
---
## Key Concepts
### Repository
A project that is tracked by Git.

### Commit
A permanent snapshot of the staged changes in a project.

### Working Direcotry
The files you are currently editing.

### Staging Area
The area where changes are prepared before creating a commit.

### Branch
An independent line of development.

### Remote
A copy of your repository hosted on another server, such as GitHub.

## Mental Model
Git manages changes by moving them through three stages.

```text
Working Directory
    ↓
Staging Area
    ↓
Repository
```

### Working Directory
Where you actively edit your files.

### Staging Area
A holding area where you choose which changes will be included in the next commit.

### Repository
The permanent history of your project. Each commit creates a snapshot in the repository.

Remember:
- `git add` moves changes from the Working Directory to the Staging Area.
- `git commit` moves the staged changes into the Repository.

## Commands
| Command | Purpose |
|---------|---------|
| `git init` | Initialize a new Git repository. |
| `git status` | Show the current state of the repository. |
| `git add .` | Stage all modified and new files. |
| `git add <filename>` | Stage a specific file. |
| `git diff` | Show unstaged changes. |
| `git diff --staged` | Show staged changes. |
| `git commit -m "message"` | Create a commit from staged changes. |
| `git log --oneline` | Display a condensed commit history. |
| `git restore <filename>` | Discard uncommitted changes to a file. |
| `git restore --staged <filename>` | Remove a file from the staging area. |
| `git remote -v` | Display configured remote repositories. |
| `git push` | Upload commits to the remote repository. |
| `git pull` | Download and merge changes from the remote repository. |
| `git clone <url>` | Copy a remote repository to your local machine. |

## Best Practices
- Create one Git repository per project.
- Commit early and commit often.
- Each commit should represent one logical change.
- Write clear, descriptive commit messages.
- Review changes with `git diff` before committing.
- Check the repository status with `git status` frequently.
- Push your work to GitHub regularly to keep a backup.
- Keep documentation up to date as the project evolves.

## Common Mistakes
- Forgetting to stage files before committing.
- Thinking `git add` creates a commit.
- Forgetting to review changes before committing.
- Committing multiple unrelated changes together.
- Writing vague commit messages such as "update" or "fixed."
- Creating a single Git repository for multiple unrelated projects.
- Forgetting to push commits to GitHub after committing locally.

## Summary
Git records the history of a project by creating snapshots called commits.

Changes move through three stages:
1. Working Directory
2. Staging Area
3. Repository

The basic Git workflow is:

Edit → Review → Stage → Commit → Push

Git helps you work confidently by allowing you to track changes, recover from mistakes, and maintain a complete history of your project.