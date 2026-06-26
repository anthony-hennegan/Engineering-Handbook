# Git Fundamentals

## Purpose
Git is a version control system that records the history of a project by creating snapshots called commits. It allows you to track changes, recover from mistakes, and collaborate wiht others. Git runs locally on your computer, while GitHub is a service that hosts Git repositories online.
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
---
## Mental Model
Git manages changes by moving them through three stages.

Working Directory
    |
    v
Staging Area
    |
    v
Repository

### Wroking Directory
Where you actively edit your files.

### Staging Area
A holding area where you choose which changes will be included in the next commit.

### Repository
The permanent history of your project. Each commit creates a snapshot in the repository.

Remember:
- `git add` moves changes from the Working Direcotyr to the Staging Area.
- `git commit` moves the staged changes into the Repository.

## Commands

## Best Practices

## Common Mistakes

## Summary