````markdown
# Lesson 025 — File Persistence with JSON

# What Problem Does File Persistence Solve?

So far, our Library Management System stores all books in a Python list.

Example:

```python
books = [
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "checked_out": False
    }
]
```

This list only exists while the program is running.

When Python exits:

- RAM is cleared.
- Variables disappear.
- The books list is lost.

Every time the program starts, it creates a brand new list.

---

# Memory vs Storage

Think of your computer as having two places for data.

```
             Computer

      RAM                     Disk
 (Temporary Memory)      (Permanent Storage)

     Very Fast               Slower

 Exists while program      Exists after program
      is running                exits
```

Variables live in RAM.

Files live on disk.

The program moves data between them.

---

# Program Flow

Without persistence:

```
Start Program
      │
      ▼
Create books list
      │
      ▼
User changes books
      │
      ▼
Exit
      │
      ▼
Everything disappears
```

With persistence:

```
Start Program
      │
      ▼
Load books.json
      │
      ▼
Create books list in RAM
      │
      ▼
User changes books
      │
      ▼
Save books.json
      │
      ▼
Exit
```

---

# Why JSON?

Python needs a way to store lists and dictionaries as text.

The most common format is JSON.

JSON stands for:

**JavaScript Object Notation**

Nearly every programming language supports it.

---

# JSON Looks Like Python

Python:

```python
books = [
    {
        "title": "Dune",
        "checked_out": False
    }
]
```

JSON:

```json
[
    {
        "title": "Dune",
        "checked_out": false
    }
]
```

Important differences:

Python:

- True
- False
- None

JSON:

- true
- false
- null

---

# The json Module

Import it with:

```python
import json
```

It translates between:

```
Python Objects
      │
      ▼
JSON Text
```

and

```
JSON Text
      │
      ▼
Python Objects
```

---

# Reading a JSON File

```python
import json

with open("books.json", "r", encoding="utf-8") as file:
    books = json.load(file)
```

Read this from the bottom upward:

1. Open the file.
2. Give the file to `json.load()`.
3. Convert JSON into Python objects.
4. Store the result in `books`.

After this:

```python
type(books)
```

returns

```python
list
```

The rest of your program works with a normal Python list.

---

# Writing a JSON File

```python
import json

with open("books.json", "w", encoding="utf-8") as file:
    json.dump(books, file, indent=4)
```

Read it as:

Take the Python list

↓

Convert it into JSON

↓

Write it to the file.

---

# Understanding `with open(...)`

Example:

```python
with open("books.json", encoding="utf-8") as file:
    books = json.load(file)
```

Break it apart:

```
with
│
├── open(...)
│      Opens the file.
│
├── as file
│      Stores the opened file in the variable named file.
│
└── :
       Everything inside the block uses the open file.
```

When the block ends:

- The file is automatically closed.
- The `books` variable still exists because it now lives in RAM.

The file closes.

The data does not.

---

# Why Open the File Twice?

Typical program flow:

```
Open file
      │
Read JSON
      │
Close file
      │
Modify books in RAM
      │
Open file again
      │
Write JSON
      │
Close file
```

We do not keep the file open because we only need it while reading or writing.

Good rule:

> Open a file late. Close it early.

---

# What Is a File Handle?

The variable:

```python
file
```

is **not** the file itself.

It is a file handle.

Think of it like a library checkout ticket.

```
books.json
      ▲
      │
 Operating System
      ▲
      │
File Handle
      ▲
      │
Python
```

Python talks to the operating system through the file handle.

---

# The Operating System's Role

Python does not read the hard drive directly.

Instead:

```
Python
    │
    ▼
Operating System
    │
    ▼
File System
    │
    ▼
Disk
```

When Python calls:

```python
open("books.json")
```

it asks the operating system for access to the file.

The operating system manages:

- permissions
- hardware
- open files
- file locations
- reading and writing

---

# Reading vs Writing Modes

```
"r"

Read an existing file.


"w"

Write to a file.

Creates a new file if needed.

Replaces existing contents.


"a"

Append to the end of a file.
```

Most projects primarily use:

- `"r"`
- `"w"`

---

# Functions Return Values

Every function returns something.

Some useful examples:

```python
name = input("Name: ")
```

returns a string.

```python
length = len(name)
```

returns an integer.

```python
books = load_books()
```

returns a list.

Even:

```python
print("Hello")
```

returns a value.

That value is:

```python
None
```

---

# Function vs Function Call

These are different.

```python
function
```

Refers to the function itself.

Nothing executes.

```python
function()
```

Calls the function.

Everything inside runs.

The returned value becomes the value of the expression.

---

# Functions as Expressions

Python evaluates function calls before continuing.

These two examples are equivalent.

```python
if checkout_book(title, books):
    save_books(books)
```

```python
result = checkout_book(title, books)

if result:
    save_books(books)
```

Execution order:

```
Call function

↓

Run its code

↓

Receive return value

↓

Evaluate the if statement
```

The function always runs.

The `if` uses its return value.

---

# Truthy and Falsy Values

Python converts values to `True` or `False` in conditions.

Falsy values:

```python
False
None
0
0.0
""
[]
{}
set()
```

Most other values are truthy.

Examples:

```python
23
-5
"Python"
[1, 2]
{"title": "Dune"}
```

Python effectively evaluates:

```python
bool(value)
```

inside an `if`.

---

# `return` vs `break`

`break`

- Stops the loop.
- Continues the function.

`return`

- Stops the loop.
- Ends the function immediately.
- Sends a value back to the caller.

Because `return` exits the function, a `break` after it is unnecessary.

---

# Separation of Responsibilities

The Library project is now organized into modules.

```
main.py
    │
    └── Coordinates the program

catalog.py
    │
    └── Book operations

storage.py
    │
    └── JSON file persistence

menus.py
    │
    └── User interface

utils.py
    │
    └── Shared helper functions
```

Each module has one primary responsibility.

This is called **Separation of Concerns**.

---

# Mental Model

```
Disk
     │
     ▼
Load JSON
     │
     ▼
Python List in RAM
     │
Modify books
     │
     ▼
Save JSON
     │
     ▼
Disk
```

Your program works with Python objects.

JSON is simply the translator between memory and storage.

---

# Common Mistakes

- Trying to read a file that does not exist.
- Forgetting to import `json`.
- Thinking the JSON file is the program's data instead of a storage format.
- Forgetting that `"w"` replaces the file contents.
- Leaving unnecessary `break` statements after `return`.
- Forgetting that `function` and `function()` mean different things.

---

# Rules to Remember

- Variables live in RAM.
- Files live on disk.
- JSON stores Python data as text.
- `json.load()` reads JSON into Python objects.
- `json.dump()` writes Python objects to JSON.
- Always use `with open(...)` for file operations.
- Every function returns a value.
- `function()` executes the function.
- `if function():` evaluates the function's return value.
- `return` exits the function immediately.
- Keep responsibilities separated between modules.
````
