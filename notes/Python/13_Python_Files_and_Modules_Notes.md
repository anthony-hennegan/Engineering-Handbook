# Lesson 016 - Files and Modules

## Purpose

Files and modules let us split a growing Python program into smaller sections. This makes the program easier to read, organize, test, and maintain.

---

# Key Concepts

## Python Files

A Python file is a file ending in `.py`.

Example:

```text
main.py
catalog.py
menus.py
utils.py
```

Each file can contain Python code such as:

* variables
* functions
* conditionals
* loops
* imports

A larger program can be divided across several Python files instead of placing everything inside `main.py`.

---

## Modules

A Python file that can be imported into another Python file is called a module.

For example, `catalog.py` is a module when it is imported into `main.py`.

```text
library_project/
├── main.py
├── catalog.py
├── menus.py
└── utils.py
```

These files are separate modules, but they are still part of the same program.

---

## Importing a Function

A function must be imported before another module can use it.

Suppose `catalog.py` contains:

```python
def show_books(book_list):
    for book in book_list:
        print(book["title"])
```

`main.py` can import the function:

```python
from catalog import show_books
```

The function can then be called inside `main.py`:

```python
show_books(books)
```

The general syntax is:

```python
from module_name import function_name
```

Do not include `.py` in the module name.

Correct:

```python
from catalog import show_books
```

Incorrect:

```python
from catalog.py import show_books
```

---

## Importing Multiple Functions

Multiple functions can be imported from the same module.

Suppose `utils.py` contains:

```python
def format_name(name):
    return name.strip().title()


def format_response(response):
    return response.strip().lower()
```

Both functions can be imported:

```python
from utils import format_name, format_response
```

They can then be called normally:

```python
reader_name = format_name(input("Enter your name: "))
response = format_response(input("Would you like to view the books? "))
```

---

## Module Responsibilities

Each module should have one clear area of responsibility.

Example:

```text
main.py
catalog.py
menus.py
utils.py
```

Possible responsibilities:

### `main.py`

Starts the application and coordinates the program.

```python
from catalog import display_available_books
from utils import format_name

reader_name = format_name(input("Enter your name: "))
display_available_books(books)
```

### `catalog.py`

Contains functions related to books and the library catalog.

```python
def is_available(book):
    return not book["checked_out"]


def display_available_books(book_list):
    for book in book_list:
        if is_available(book):
            print(book["title"])
```

### `menus.py`

Contains functions that display menus or menu options.

```python
def display_main_menu():
    print("1. View available books")
    print("2. View checked-out books")
    print("3. Exit")
```

### `utils.py`

Contains small reusable helper functions.

```python
def format_name(name):
    return name.strip().title()


def format_response(response):
    return response.strip().lower()
```

---

## Import Order

Imports are normally placed at the top of a Python file.

Example:

```python
from catalog import display_available_books
from menus import display_main_menu
from utils import format_name

reader_name = format_name(input("Enter your name: "))

display_main_menu()
display_available_books(books)
```

Placing imports at the top makes it easier to see which modules the file depends on.

---

## Running a Multi-File Program

The program should normally be started by running `main.py`.

```bash
python main.py
```

Python reads the imports in `main.py` and loads the requested functions from the other modules.

You normally do not need to run each module separately.

For example, do not run all four files one at a time:

```bash
python catalog.py
python menus.py
python utils.py
python main.py
```

Instead, start the application through its main file:

```bash
python main.py
```

---

# Project Use

The Library CLI App can be divided into modules based on responsibility.

```text
001_library/
├── main.py
├── catalog.py
├── menus.py
└── utils.py
```

The book-related functions can be moved into `catalog.py`.

```python
def is_available(book):
    return not book["checked_out"]


def display_available_books(book_list):
    print("Available for Checkout")
    print("----------------------")

    for book in book_list:
        if is_available(book):
            print(f"{book['title']} by {book['author']}")


def display_checked_out_books(book_list):
    print("Currently Checked Out")
    print("---------------------")

    for book in book_list:
        if book["checked_out"]:
            print(f"{book['title']} by {book['author']}")
```

Formatting functions can be moved into `utils.py`.

```python
def format_name(name):
    return name.strip().title()


def format_response(response):
    return response.strip().lower()
```

Menu-related functions can be placed in `menus.py`.

```python
def display_main_menu():
    print("Library Menu")
    print("------------")
    print("1. View available books")
    print("2. View checked-out books")
    print("3. Exit")
```

`main.py` can import and coordinate the functions.

```python
from catalog import display_available_books
from menus import display_main_menu
from utils import format_name

reader_name = format_name(input("Enter your name: "))

print(f"Hello {reader_name}.")

display_main_menu()
display_available_books(books)
```

This keeps `main.py` focused on controlling the program instead of containing every function.

---

# Important Rules

* Every Python file ending in `.py` can be used as a module.
* A function must be imported before another module can use it.
* Use the module name without `.py` in an import statement.
* Place imports near the top of the file.
* Run the application through `main.py`.
* Give each module one clear responsibility.
* Keep related functions together.
* Moving a function does not change what the function does.
* After moving a function, update any file that needs to import it.

---

# Common Mistakes

## Including `.py` in the Import

Incorrect:

```python
from catalog.py import show_books
```

Correct:

```python
from catalog import show_books
```

---

## Calling a Function Without Importing It

Suppose `show_books()` is defined inside `catalog.py`.

Incorrect `main.py`:

```python
show_books(books)
```

This can raise a `NameError` because `main.py` does not know what `show_books` refers to.

Correct:

```python
from catalog import show_books

show_books(books)
```

---

## Importing the Wrong Function Name

Incorrect:

```python
from catalog import display_books
```

If the function is actually named:

```python
def display_available_books(book_list):
    pass
```

Correct:

```python
from catalog import display_available_books
```

The imported name must match the function definition.

---

## Running Every Module Separately

Incorrect workflow:

```bash
python catalog.py
python menus.py
python utils.py
python main.py
```

Correct workflow:

```bash
python main.py
```

`main.py` imports the functions it needs from the other modules.

---

## Putting Unrelated Functions Together

Poor organization:

```python
# catalog.py

def display_available_books(book_list):
    pass


def format_name(name):
    pass


def display_main_menu():
    pass
```

Better organization:

```python
# catalog.py

def display_available_books(book_list):
    pass
```

```python
# utils.py

def format_name(name):
    pass
```

```python
# menus.py

def display_main_menu():
    pass
```

Each module has a clearer responsibility.

---

## Creating Circular Imports

A circular import happens when two modules try to import from each other.

Example:

```python
# catalog.py
from menus import display_main_menu
```

```python
# menus.py
from catalog import display_available_books
```

This can make the program difficult to load and understand.

A better design is for `main.py` to import from both modules:

```python
from catalog import display_available_books
from menus import display_main_menu
```

The feature modules do not need to import each other.

---

# Summary

A Python program can be divided into multiple `.py` files called modules.

Functions can be moved into modules based on their responsibility and imported where they are needed.

The syntax:

```python
from catalog import show_books
```

allows one module to access a function defined in another module.

For the Library CLI App:

* `main.py` coordinates the application.
* `catalog.py` contains book-related functions.
* `menus.py` contains menu-related functions.
* `utils.py` contains reusable helper functions.

Splitting the application into modules keeps each file focused and makes the program easier to maintain.