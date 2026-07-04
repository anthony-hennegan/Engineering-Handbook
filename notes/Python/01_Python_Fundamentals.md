# Lesson 003 - Python Fundamentals

## Purpose

A Python program is a set of instructions written in the Python programming language that tells the computer what to do.

Python executes statements one at a time from top to bottom unless directed otherwise.

---

## Key Concepts

### Statement

A statement is a single instruction that tells Python to perform an action.

Example:

```python
print("Hello")
```

```python
age = 34
```

---

### Variable

A variable is a name that refers to a value.

Example:

```python
name = "Anthony"
```

In this example, `name` is the variable.

---

### Value

A value is a piece of information used by a program.

Examples:

```python
"Anthony"
34
True
```

---

### Data Type

A data type is an attribute of a value that tells Python how to store, interpret, and operate on that value.

Examples:

| Value | Data Type |
|---|---|
| `"Anthony"` | `str` |
| `34` | `int` |
| `True` | `bool` |

---

## Mental Model

A variable is a name that refers to a value.

That value exists somewhere in the computer's memory while the program is running.

```text
name ─────────────▶ "Anthony"
variable name        value in memory
```

Another example:

```python
age = 34
```

Mental model:

```text
age ──────────────▶ 34
variable name       value in memory
```

The variable is not the value itself.

The variable is a name Python uses to find the value.

Every value also has a data type:

```text
"Anthony"  →  str
34         →  int
True       →  bool
```

So this line:

```python
age = 34
```

means:

```text
The variable name `age` refers to the value `34`.
The value `34` exists in memory while the program runs.
The value `34` has the data type `int`.
```

---

## Program Execution

Python runs one statement at a time from top to bottom.

Example:

```python
name = "Anthony"

print(name)

name = "Bob"

print(name)
```

Output:

```text
Anthony
Bob
```

The first `print(name)` displays `"Anthony"` because Python has not executed `name = "Bob"` yet.

A statement uses the value a variable refers to at the moment that statement runs.

---

## Variable Reassignment

A variable can be reassigned to refer to a different value.

Example:

```python
name = "Anthony"
name = "Bob"
```

After reassignment, `name` refers to `"Bob"`.

The old value is no longer accessed through that variable.

---

## `print()`

The `print()` function displays information in the terminal.

Example:

```python
print("Hello")
```

Output:

```text
Hello
```

By default, each `print()` call adds a newline character at the end.

That is why this:

```python
print("Hello")
print("World")
```

prints:

```text
Hello
World
```

A single `print()` call can display multiple values on one line:

```python
print("Anthony", 34)
```

Output:

```text
Anthony 34
```

---

## Application State

Application state is the information that represents the current condition of the application while it is running.

Examples from the Library project:

```python
library_name = "Bailey's Books and Bargains"
librarian_name = "Anthony"
book_count = 20
is_open = True
```

These variables describe the current state of the application.

---

## Stored vs. Derived Data

Before creating a variable, ask:

> Does this information need to be stored, or can it be derived from other information?

Stored data is information the program needs to remember.

Derived data is information that can be calculated from other data.

Example:

```python
library_name = "Bailey's Books and Bargains"
```

This should be stored.

But a welcome message can be created from the library name, so it does not necessarily need its own variable.

---

## Important Rules

- Python executes statements from top to bottom.
- A variable is a name that refers to a value.
- Values exist in memory while the program is running.
- Values have data types.
- Variables can be reassigned.
- A statement uses the current value of a variable when the statement runs.
- `print()` displays output in the terminal.
- `print()` adds a newline character by default.

---

## Best Practices

- Use clear and descriptive variable names.
- Use `snake_case` for variable names.
- Store only information the program needs to remember.
- Avoid creating variables for information that can be derived.
- Keep beginner programs simple and readable.
- Predict what the program will do before running it.

---

## Common Mistakes

- Confusing variables with values.
- Confusing values with data types.
- Forgetting that Python runs from top to bottom.
- Assuming a variable changes before reassignment happens.
- Creating unnecessary variables for derived information.
- Using vague variable names like `x`, `thing`, or `data`.

---

## Summary

A Python program is made of statements.

Python executes statements one at a time from top to bottom.

Variables are names that refer to values.

Values exist in memory while the program is running.

Values have data types.

Variables can be reassigned to refer to different values.

Understanding variables is one of the foundations of understanding Python.
