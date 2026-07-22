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

- RAM is cleared
- Variables disappear
- The books list is lost

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

Your variables live in RAM.

Your files live on disk.

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
Create books list
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

Python needs a way to save lists and dictionaries into a text file.

The most common format is JSON.

JSON stands for:

JavaScript Object Notation

Even though it originated with JavaScript, nearly every programming language supports it.

---

# JSON Looks Very Similar to Python

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

Notice the differences:

Python:

- True
- False
- None

JSON:

- true
- false
- null

Everything else is nearly identical.

---

# The json Module

Python includes a built-in module named:

```python
import json
```

It converts between:

Python objects

↓

JSON text

and

JSON text

↓

Python objects

---

# Reading a JSON File

Basic pattern:

```python
import json

with open("books.json", "r") as file:
    books = json.load(file)
```

Read it from the bottom upward:

1. Open the file.
2. Give the file to json.load().
3. Convert JSON into Python objects.
4. Store the result in books.

After this:

```python
type(books)
```

returns

```python
list
```

The JSON file disappears from your thinking.

You simply have a normal Python list again.

---

# Writing a JSON File

Pattern:

```python
import json

with open("books.json", "w") as file:
    json.dump(books, file)
```

Read this as:

Take the Python list

↓

Convert it into JSON

↓

Write it into the file.

---

# The with Statement

Notice both examples use:

```python
with open(...) as file:
```

Why?

Without `with`, you must remember to close the file yourself.

```python
file = open("books.json")

...

file.close()
```

Using `with` automatically closes the file when the block ends.

This is safer and is the standard Python style.

---

# Reading vs Writing Modes

```
"r"

Read an existing file.


"w"

Write to a file.

Creates a new file if it doesn't exist.

Completely replaces existing contents.


"a"

Append to the end of a file.
```

For this project, we will mostly use:

- "r"
- "w"

---

# Mental Model

Think of JSON as a translator.

```
Python List
       │
       ▼
json.dump()
       │
       ▼
books.json
       │
       ▼
json.load()
       │
       ▼
Python List
```

Your program always works with Python objects.

JSON simply translates those objects to and from a file.

---

# Common Mistakes

Trying to read a file that does not exist.

Forgetting to import json.

Thinking the JSON file is the data.

Forgetting that "w" replaces the entire file.

Editing the JSON file by hand and breaking its formatting.

---

# Rules to Remember

Variables live in RAM.

Files live on disk.

JSON stores Python data as text.

json.load() reads JSON into Python objects.

json.dump() writes Python objects into JSON.

Always use `with open(...)` when working with files.

The program should work with Python objects—not directly with the file.