# Lesson 014 - Functions

## Purpose

Functions allow a program to group code into reusable named actions.

They are useful when code needs to be reused, organized, or changed in one place.

In the Library CLI App, functions can help separate actions like greeting the reader, displaying books, and checking whether checkout is available.

---

# Key Concepts

## Function

A function is a reusable block of code with a name.

Example:

```python
def greet_reader():
    print("Hello reader.")
```

This defines a function named `greet_reader`.

The function does not run until it is called.

---

## Function Call

A function call tells Python to run the code inside a function.

Example:

```python
def greet_reader():
    print("Hello reader.")

greet_reader()
```

Output:

```text
Hello reader.
```

The function body ran because the function was called with parentheses.

---

## Function Body

The function body is the indented code inside the function.

Example:

```python
def show_message():
    print("Hello.")
    print("Welcome.")
```

Both `print()` lines belong to the function because they are indented.

Output:

```text
Hello.
Welcome.
```

---

## Parameters

A parameter allows a function to receive information.

Example:

```python
def greet_reader(name):
    print(f"Hello {name}.")
```

The parameter is:

```text
name
```

The parameter acts like a variable inside the function.

---

## Arguments

An argument is the actual value passed into a function call.

Example:

```python
def greet_reader(name):
    print(f"Hello {name}.")

greet_reader("Anthony")
```

Output:

```text
Hello Anthony.
```

The argument is:

```text
"Anthony"
```

Python uses the argument as the value for the parameter.

---

## Parameter vs Argument

A parameter is the placeholder in the function definition.

An argument is the actual value passed into the function call.

Example:

```python
def greet_reader(name):
    print(f"Hello {name}.")

greet_reader("Anthony")
```

The parameter is:

```text
name
```

The argument is:

```text
"Anthony"
```

Simple rule:

```text
parameter = placeholder
argument = actual value
```

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
# Project Use

In the Library CLI App, functions can organize actions that are currently written directly in `main.py`.

Example:

```python
def show_welcome_message():
    print("Welcome to Bailey's Books and Bargains.")

show_welcome_message()
```

A function can also receive project data.

Example:

```python
def greet_reader(name):
    print(f"Hello {name}.")

reader_name = "Anthony"
greet_reader(reader_name)
```

Functions can eventually help organize actions like:

```text
show_welcome_message
greet_reader
display_books
show_checkout_status
```

The goal is to turn one long script into smaller named actions.

---

# Important Rules

- Use `def` to define a function.
- A function body must be indented.
- A function does not run until it is called.
- Use parentheses to call a function.
- A parameter is a placeholder in the function definition.
- An argument is the actual value passed into the function call.
- Function names should describe the action being performed.
- Functions help reduce repeated code.
- Functions make code easier to organize and update.

---

# Common Mistakes

## Defining a Function but Not Calling It

Incorrect:

```python
def greet_reader():
    print("Hello reader.")
```

Nothing prints because the function was defined but never called.

Correct:

```python
def greet_reader():
    print("Hello reader.")

greet_reader()
```

---

## Forgetting Parentheses When Calling

Incorrect:

```python
def greet_reader():
    print("Hello reader.")

greet_reader
```

Correct:

```python
def greet_reader():
    print("Hello reader.")

greet_reader()
```

The parentheses tell Python to run the function.

---

## Forgetting Indentation

Incorrect:

```python
def greet_reader():
print("Hello reader.")
```

Correct:

```python
def greet_reader():
    print("Hello reader.")
```

The function body must be indented.

---

## Confusing Parameters and Arguments

Incorrect mental model:

```text
The argument is the variable in the function definition.
```

Correct mental model:

```text
The parameter is the variable in the function definition.
The argument is the value passed into the function call.
```

Example:

```python
def greet_reader(name):
    print(f"Hello {name}.")

greet_reader("Anthony")
```

`name` is the parameter.

`"Anthony"` is the argument.

---

# Summary

A function stores a reusable action under a name.

Functions are useful when code needs to be reused, organized, or changed in one place.

In the Library CLI App, functions will help turn one long script into smaller named actions.