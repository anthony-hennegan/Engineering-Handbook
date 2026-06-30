# Git Fundamentals
Last Updated: 2026-06-27
## Purpose
The command line (or terminal) is a text-based interface for interacting with the operating system.

Instead of using a graphical interface (GUI) with windows, icons, and menus, you interact with the computer by typing commands. This allows you to navigate files, manage projects, run programs, and automate tasks quickly and efficiently.

Many software development tools, including Git, Python, and package managers, are designed to be used from the command line.

## Key Concepts
### Directory
A directory is another name for a folder. Directories are used to organize files and other directories.

### Current Working Directory(CWD)
The Current Working Directory is the directory you are currently working in. Any command you run will operate relative to this location uless you specify a different path.

### Path
A path describes the location of a file or directory within the file system. It tells the computer how to find a specfic file or folder.

## Mental Model

The terminal always operates from your current location in the file system.

```text
Computer
│
└── Users
    └── anthonyhennegan
        └── CodingDojo
            ├── Knowledge
            └── Projects
                └── 001_library   ← Current Working Directory
```

Most terminal commands operate relative to your Current Working Directory (CWD). Before running commands, it is important to know where you are in the file system.


## Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `pwd` | Display the current working directory. | pwd |
| `ls` | List the files and directories in the current working directory. | ls |
| `cd` | Change the current working directory. | cd directory_name |
| `cd ..` | Go up one folder | cd .. |
| `cd ../..` | Go up two folders | cd ../.. |
| `mkdir` | Create a new directory. | mkdir directory_name |
| `touch` | Create a new empty file. | touch file.txt |
| `cp` | Copy files and renames it. | cp report.txt backup_report.txt |
| `cp` | Copy files into a folder. | cp report.txt /home/user/documents/|
| `mv` | Move files. | mv my_file.txt /path/to/destination/folder/
| `mv` | Rename files or directories. | mv my_file.txt /path/to/destination/folder/
| `rm` | Remove files | rm file1.txt|
| `rm -r` | Remove directory (no prompt) | rm -r directory_name|
| `rm -ri` | Remove directory with prompt | rm -ri directory_name -> y or n|


## Best Practices

- Always know your Current Working Directory before creating, moving, or deleting files.
- Use descriptive names for files and directories.
- Organize projects into logical directories.
- Double-check commands before using destructive operations such as `rm`.
- Use the terminal regularly to become comfortable navigating the file system.
- Learn the purpose of each command instead of memorizing syntax.

## Common Mistakes

- Forgetting to check the Current Working Directory before running commands.
- Accidentally creating files or folders in the wrong directory.
- Confusing similar commands such as `cp` (copy) and `mv` (move).
- Using `rm` without verifying the file or directory being deleted.
- Relying on the graphical interface instead of practicing terminal navigation.

## Summary

- The terminal is a text-based interface for interacting with the operating system.
- Most commands operate relative to the Current Working Directory.
- Directories organize files and folders within the file system.
- Learning a small set of core commands makes navigating and managing projects much more efficient.
- Regular practice builds speed and confidence when working from the command line.