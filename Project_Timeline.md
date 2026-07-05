# Project 001 - Library CLI App Timeline

## Purpose

This document tracks the lesson progression for completing the first Coding Dojo project:

**Project 001 - Library CLI App**

Each lesson should follow the standard workflow:

1. Introduce concept
2. Complete exercise
3. Complete drill
4. Apply to project
5. Create flashcards
6. Commit Knowledge repo
7. Commit Project repo

---

# Phase 0 - Setup and Workflow

## Lesson 001 - Git Fundamentals

### Project Use

Set up version control for the Library project.

### Example

```bash
git init
git add .
git commit -m "Create initial library project structure"
```

---

## Lesson 002 - Command Line Fundamentals

### Project Use

Navigate the project folder and manage files from the terminal.

### Example

```bash
cd CodingDojo/Projects/001_library
ls
touch main.py
```

---

# Phase 1 - Python Foundations

## Lesson 003 - Python Fundamentals

### Project Use

Create basic application state for the Library app.

### Example

```python
library_name = "Bailey's Books and Bargains"
librarian_name = "Anthony"
book_count = 20
is_open = True

print(library_name)
```

---

## Lesson 004 - User Input

### Project Use

Allow the user to enter information.

### Example

```python
reader_name = input("What is your name? ")

print(f"Hello {reader_name}.")
```

---

## Lesson 005 - Conditionals

### Project Use

Respond differently based on the user's answer.

### Example

```python
view_selection = input("Would you like to view our book selection? ")

if view_selection == "yes":
    print("Ok, here is what we have.")
elif view_selection == "no":
    print("No worries. Have a nice day!")
else:
    print("Please type yes or no.")
```

---

## Lesson 006 - String Methods

### Project Use

Clean up user input so `"Yes"`, `" yes"`, and `"YES"` can be handled correctly.

### Example

```python
view_selection = input("Would you like to view our book selection? ")
view_selection = view_selection.strip().lower()

if view_selection == "yes":
    print("Ok, here is what we have.")
elif view_selection == "no":
    print("No worries. Have a nice day!")
else:
    print("Please type yes or no.")
```

---

## Lesson 007 - Numbers and Type Conversion

### Project Use

Convert user input from a string into a number.

### Example

```python
book_count = input("How many books would you like to check out? ")
book_count = int(book_count)

print(f"You want to check out {book_count} books.")
```

---

## Lesson 008 - Comparison Operators

### Project Use

Check whether a number is within an allowed range.

### Example

```python
requested_books = int(input("How many books would you like to check out? "))

if requested_books > 3:
    print("You can only check out 3 books at a time.")
else:
    print("Checkout amount approved.")
```

---

## Lesson 009 - Logical Operators

### Project Use

Combine multiple conditions.

### Example

```python
is_open = True
has_books = True

if is_open and has_books:
    print("The library is open and books are available.")
else:
    print("Checkout is not available right now.")
```

---

## Lesson 010 - Lists

### Project Use

Store multiple book titles.

### Example

```python
books = ["The Hobbit", "The Alchemist", "Dune"]

print(books[0])
print(len(books))
```

---

## Lesson 011 - Loops

### Project Use

Display every book in the catalog.

### Example

```python
books = ["The Hobbit", "The Alchemist", "Dune"]

for book in books:
    print(book)
```

---

## Lesson 012 - Dictionaries

### Project Use

Store related information about one book.

### Example

```python
book = {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "is_checked_out": False
}

print(book["title"])
```

---

## Lesson 013 - Lists of Dictionaries

### Project Use

Store the full library catalog.

### Example

```python
books = [
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "is_checked_out": False
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "is_checked_out": False
    }
]

for book in books:
    print(book["title"])
```

---

# Phase 2 - Program Structure

## Lesson 014 - Functions

### Project Use

Move repeated logic into reusable functions.

### Example

```python
def greet_reader(name):
    print(f"Hello {name}.")

reader_name = input("What is your name? ")
greet_reader(reader_name)
```

---

## Lesson 015 - Function Design

### Project Use

Create functions with one clear responsibility.

### Example

```python
def show_books(books):
    for book in books:
        print(book["title"])
```

---

## Lesson 016 - Files and Modules

### Project Use

Split the project into multiple files.

### Example

```text
main.py
catalog.py
menus.py
utils.py
```

Example import:

```python
from catalog import show_books
```

---

## Lesson 017 - Error Handling

### Project Use

Prevent the program from crashing when the user enters bad input.

### Example

```python
try:
    requested_books = int(input("How many books? "))
except ValueError:
    print("Please enter a number.")
```

---

## Lesson 018 - Main Program Loop

### Project Use

Keep the app running until the user chooses to quit.

### Example

```python
while True:
    choice = input("Choose an option or type quit: ").strip().lower()

    if choice == "quit":
        break
    else:
        print("You chose:", choice)
```

---

# Phase 3 - Data Persistence

## Lesson 019 - Reading Files

### Project Use

Load saved book data from a file.

### Example

```python
with open("books.txt", "r") as file:
    contents = file.read()

print(contents)
```

---

## Lesson 020 - Writing Files

### Project Use

Save book data to a file.

### Example

```python
with open("books.txt", "w") as file:
    file.write("The Hobbit")
```

---

## Lesson 021 - JSON

### Project Use

Save and load structured book data.

### Example

```python
import json

with open("books.json", "w") as file:
    json.dump(books, file)
```

---

## Lesson 022 - Data Validation

### Project Use

Check that book records have required information.

### Example

```python
book = {
    "title": "",
    "author": "Unknown"
}

if book["title"] == "":
    print("Book title is required.")
```

---

# Phase 4 - Object-Oriented Programming

## Lesson 023 - Classes and Objects

### Project Use

Create a `Book` class.

### Example

```python
class Book:
    pass

book = Book()
```

---

## Lesson 024 - Constructors

### Project Use

Create book objects with title and author.

### Example

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("The Hobbit", "J.R.R. Tolkien")
```

---

## Lesson 025 - Methods

### Project Use

Add behavior to book objects.

### Example

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True
```

---

## Lesson 026 - Multiple Classes

### Project Use

Create a `Library` class that manages books.

### Example

```python
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
```

---

# Phase 5 - Testing and Quality

## Lesson 027 - Basic Testing

### Project Use

Use simple assertions to check logic.

### Example

```python
def is_available(book):
    return not book["is_checked_out"]

book = {"title": "Dune", "is_checked_out": False}

assert is_available(book) == True
```

---

## Lesson 028 - Pytest

### Project Use

Create test files for project functions.

### Example

```python
def test_book_is_available():
    book = {"title": "Dune", "is_checked_out": False}
    assert book["is_checked_out"] == False
```

---

## Lesson 029 - Refactoring

### Project Use

Improve code without changing behavior.

### Example

Before:

```python
print(book["title"])
print(book["author"])
```

After:

```python
def print_book(book):
    print(book["title"])
    print(book["author"])
```

---

## Lesson 030 - Debugging

### Project Use

Read errors and isolate problems.

### Example

```python
print("Debug:", book)
print("Debug title:", book["title"])
```

---

# Phase 6 - Final Release

## Lesson 031 - Requirements Review

### Project Use

Compare the finished app against `REQUIREMENTS.md`.

### Example

```text
Requirement: User can view available books.
Status: Complete.
```

---

## Lesson 032 - Command-Line Interface Polish

### Project Use

Make menus and messages easier to use.

### Example

```text
1. View books
2. Check out book
3. Return book
4. Quit
```

---

## Lesson 033 - Project Documentation

### Project Use

Update the README with setup and usage instructions.

### Example

```markdown
## How to Run

Run the project from the terminal:

```bash
python3 main.py
```
```

---

## Lesson 034 - Final Refactor

### Project Use

Clean up names, remove dead code, and simplify logic.

### Example

```python
# Unclear
x = input("Choice: ")

# Better
menu_choice = input("Choice: ")
```

---

## Lesson 035 - Final Project Release

### Project Use

Finish, commit, push, and write a final reflection.

### Example

```bash
git status
git add .
git commit -m "Complete library CLI app"
git push
```

---

# Final Outcome

By the end of Project 001, the Library CLI App should include:

- User input
- Conditionals
- Cleaned string input
- Lists
- Dictionaries
- Loops
- Functions
- File persistence
- JSON storage
- Error handling
- Tests
- Documentation
- Clean Git history