# Logical Operators

## Purpose

Logical operators allow a program to combine or reverse conditions.

They are commonly used inside conditionals when more than one condition matters.

---

# Key Concepts

## `and`

`and` checks whether both conditions are true.

Example:

```python
is_open = True
requested_books = 2
checkout_limit = 3

if is_open and requested_books <= checkout_limit:
    print("Checkout approved.")
```

This condition is true only when:

```text
is_open is True
and
requested_books is less than or equal to checkout_limit
```

If either condition is false, the whole `and` condition is false.

---

## `or`

`or` checks whether at least one condition is true.

Example:

```python
answer = "yes"

if answer == "yes" or answer == "y":
    print("Showing books.")
```

This condition is true when:

```text
answer is "yes"
or
answer is "y"
```

Only one side needs to be true.

---

## `not`

`not` reverses a boolean condition.

Example:

```python
is_open = False

if not is_open:
    print("The library is closed.")
```

This means:

```text
If is_open is False
then print that the library is closed.
```

---

# Project Use

In the Library project, logical operators can be used to check multiple conditions before approving checkout.

Example:

```python
if is_open and requested_books <= checkout_limit:
    print("Checkout approved.")
else:
    print("Checkout is not available.")
```

This checks that:

```text
The library is open
and
the requested number of books is within the checkout limit
```

---

# Important Rules

- `and` requires both conditions to be true.
- `or` requires at least one condition to be true.
- `not` reverses a boolean value.
- Logical operators return a boolean result.
- Logical operators are commonly used with comparison operators.
- Use parentheses when combining several conditions to make the code easier to read.

---

# Summary

Logical operators let a program make decisions using more than one condition.

Use:

```python
and
```

when all conditions must be true.

Use:

```python
or
```

when at least one condition must be true.

Use:

```python
not
```

to reverse a condition.