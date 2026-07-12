# Lesson 015 - Function Design

## Purpose

Function design is the practice of deciding what a function should do and what it should not do.

Good function design makes code easier to read, test, reuse, and change.

In the Library CLI App, function design helps separate actions like formatting input, displaying books, greeting the reader, and checking checkout rules.

---

# Key Concepts

## One Clear Responsibility

A function should usually do one clear job.

Example:

```python
def greet_reader(name):
    print(f"Hello {name}.")
```

This function has one responsibility:

```text
Greet the reader.
```

The function name clearly describes what the function does.

---

## Too Many Responsibilities

A function becomes harder to understand when it does too many things.

Example:

```python
def handle_library():
    print("Welcome to the library.")
    name = input("What is your name? ")
    print(f"Hello {name}.")
    requested_books = int(input("How many books? "))
    print(requested_books)
```

This function handles several jobs:

```text
shows a welcome message
gets user input
greets the reader
converts input to an integer
prints checkout information
```

That makes the function harder to name, read, test, and change.

---

## Clear Function Names

A function name should describe the action the function performs.

Example:

```python
def display_books(book_list):
    for book in book_list:
        print(book)
```

The name `display_books` tells the reader that the function displays books.

A vague name is less useful.

Incorrect:

```python
def do_stuff(book_list):
    for book in book_list:
        print(book)
```

Correct:

```python
def display_books(book_list):
    for book in book_list:
        print(book)
```

---

## Function Input

A function should receive the information it needs through parameters.

Example:

```python
def greet_reader(name):
    print(f"Hello {name}.")
```

The function needs a name, so it receives `name` as a parameter.

Function call:

```python
greet_reader("Anthony")
```

Output:

```text
Hello Anthony.
```

---

## Function Output

Some functions display information with `print()`.

Example:

```python
def show_message():
    print("Hello.")
```

Output:

```text
Hello.
```

Other functions create a value and send it back with `return`.

Example:

```python
def format_name(name):
    return name.strip().title()
```

Function call:

```python
clean_name = format_name(" anthony ")
print(clean_name)
```

Output:

```text
Anthony
```

Use `print()` when the function's job is to display something.

Use `return` when the function's job is to produce a value the program needs later.

---

## Helper Function

A helper function is a small function that supports another part of the program.

Example:

```python
def format_response(response):
    return response.strip().lower()
```

This function has one clear helper job:

```text
Clean a user response.
```

Helper functions make the main program easier to read.

---

# Project Use

In the Library CLI App, function design helps organize the program into small named actions.

Example:

```python
def show_welcome_message(library_name):
    print(f"Welcome to {library_name}.")
```

This function only displays the welcome message.

Example:

```python
def format_name(name):
    return name.strip().title()
```

This function only formats a name.

Example:

```python
def display_books(book_list):
    for book in book_list:
        if book["checked_out"]:
            print(f"- {book['title']} by {book['author']} ---- Unavailable")
        else:
            print(f"- {book['title']} by {book['author']} ---- Available")
```

This function only displays the books.

The goal is not to create as many functions as possible.

The goal is to create useful functions with clear responsibilities.

---

# Important Rules

- A function should usually have one clear responsibility.
- A function name should describe the action being performed.
- A function should receive needed information through parameters.
- Use `print()` when the function only needs to display output.
- Use `return` when the function needs to send a value back.
- Avoid vague function names like `do_stuff`.
- Avoid functions that perform too many unrelated tasks.
- Small clear functions are easier to read, test, reuse, and change.

---

# Common Mistakes

## Making One Function Do Too Much

Incorrect:

```python
def handle_everything():
    print("Welcome.")
    name = input("Name: ")
    print(f"Hello {name}.")
    requested_books = int(input("How many books? "))
    print(requested_books)
```

Correct:

```python
def show_welcome_message():
    print("Welcome.")

def greet_reader(name):
    print(f"Hello {name}.")

def format_requested_books(amount):
    return int(amount.strip())
```

Each function has a clearer job.

---

## Using a Vague Function Name

Incorrect:

```python
def process(data):
    for item in data:
        print(item)
```

Correct:

```python
def display_items(items):
    for item in items:
        print(item)
```

The better name explains what the function does.

---

## Printing When the Program Needs a Value Back

Incorrect:

```python
def format_name(name):
    print(name.strip().title())

reader_name = format_name(" anthony ")
```

This prints the cleaned name, but it does not return the cleaned value.

Correct:

```python
def format_name(name):
    return name.strip().title()

reader_name = format_name(" anthony ")
```

The corrected function returns the value so the program can store and use it.

---

## Returning When the Function Only Needs to Display

Less useful:

```python
def show_message():
    return "Hello."

print(show_message())
```

Better:

```python
def show_message():
    print("Hello.")

show_message()
```

If the function's only job is to display text, `print()` is enough.

---

# Summary

Function design is about giving each function one clear responsibility.

A well-designed function has a clear name, receives the information it needs, and either displays output or returns a useful value.

In the Library CLI App, function design will help turn the program into smaller named actions that are easier to read, change, and reuse.