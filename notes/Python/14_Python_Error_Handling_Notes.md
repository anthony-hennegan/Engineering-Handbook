# Lesson 017 - Error Handling

## Purpose

Error handling lets a Python program respond to expected problems without immediately crashing.

It is especially useful when working with user input because users may enter values that cannot be converted or processed correctly.

---

# Key Concepts

## Runtime Errors

A runtime error happens while the program is running.

Example:

```python
requested_books = int(input("How many books would you like? "))
```

If the user enters:

```text
two
```

Python cannot convert `"two"` into an integer.

The program raises:

```text
ValueError
```

Without error handling, the program stops.

---

## The try Block

The `try` block contains code that might raise an error.

Example:

```python
try:
    requested_books = int(input("How many books would you like? "))
```

Python attempts to run the code inside `try`.

If no error occurs, the program continues normally.

---

## The except Block

The `except` block runs when a matching error occurs inside the `try` block.

Example:

```python
try:
    requested_books = int(input("How many books would you like? "))
except ValueError:
    print("Please enter a whole number.")
```

If the user enters:

```text
3
```

The conversion succeeds.

If the user enters:

```text
three
```

Python raises a `ValueError` and runs the `except` block.

Output:

```text
Please enter a whole number.
```

---

## Matching the Error Type

The error named after `except` should match the error the program expects.

Example:

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter your age as a whole number.")
```

`ValueError` is appropriate because `int()` raises a `ValueError` when the string cannot be converted.

---

## Code After try and except

After Python finishes either the `try` block or the matching `except` block, execution continues below the error-handling structure.

Example:

```python
try:
    number = int(input("Enter a number: "))
    print(f"You entered {number}.")
except ValueError:
    print("That was not a valid whole number.")

print("Program finished.")
```

Valid input:

```text
Enter a number: 5
You entered 5.
Program finished.
```

Invalid input:

```text
Enter a number: five
That was not a valid whole number.
Program finished.
```

---

## Keeping the try Block Focused

Only place the code that may raise the expected error inside the `try` block.

Less focused:

```python
try:
    requested_books = int(input("How many books would you like? "))
    print("Processing request.")
    print("Checking inventory.")
    print("Preparing checkout.")
except ValueError:
    print("Please enter a whole number.")
```

More focused:

```python
try:
    requested_books = int(input("How many books would you like? "))
except ValueError:
    print("Please enter a whole number.")
```

A focused `try` block makes it clearer which operation may fail.

---

## Variables Created Inside try

A variable assigned inside `try` may not receive a value if an error happens.

Example:

```python
try:
    requested_books = int(input("How many books would you like? "))
except ValueError:
    print("Please enter a whole number.")

print(requested_books)
```

If the conversion fails, `requested_books` is never assigned.

Trying to use it afterward can raise another error.

A safer pattern is to use the value only when the conversion succeeds.

Example:

```python
try:
    requested_books = int(input("How many books would you like? "))
    print(f"You requested {requested_books} books.")
except ValueError:
    print("Please enter a whole number.")
```

---

# Project Use

The Library CLI App converts the requested checkout count into an integer.

Current code may look like:

```python
requested_books = input("How many books would you like to check out? ")
requested_books = int(format_response(requested_books))
```

This crashes if the reader enters something that is not a whole number.

The conversion can be protected with error handling:

```python
requested_books_response = input(
    "How many books would you like to check out? "
)

try:
    requested_books = int(format_response(requested_books_response))

    if requested_books <= checkout_limit and is_open:
        print("Perfect. Let's get you fixed up.")
    else:
        print("Checkout is not available.")
except ValueError:
    print("Please enter a whole number.")
```

The checkout logic is placed inside the `try` block because it should only run when `requested_books` was successfully created.

---

# Important Rules

* Put code that may raise an expected error inside `try`.
* Put the response to that error inside `except`.
* Name the specific error you expect.
* `int()` can raise a `ValueError`.
* If the `try` block succeeds, the `except` block is skipped.
* If the matching error occurs, Python runs the `except` block.
* Execution continues after the `try` and `except` structure.
* Keep the `try` block focused on the operation that may fail.
* Do not use a variable after `try` unless you know it was successfully assigned.

---

# Common Mistakes

## Placing the Risky Code Before try

Incorrect:

```python
requested_books = int(input("How many books would you like? "))

try:
    print(requested_books)
except ValueError:
    print("Please enter a whole number.")
```

The conversion happens before Python enters the `try` block, so the `ValueError` is not caught.

Correct:

```python
try:
    requested_books = int(input("How many books would you like? "))
except ValueError:
    print("Please enter a whole number.")
```

---

## Using the Wrong Error Type

Incorrect:

```python
try:
    requested_books = int(input("How many books would you like? "))
except IndexError:
    print("Please enter a whole number.")
```

`int()` does not raise an `IndexError` for invalid text.

Correct:

```python
try:
    requested_books = int(input("How many books would you like? "))
except ValueError:
    print("Please enter a whole number.")
```

---

## Using the Variable After a Failed Conversion

Incorrect:

```python
try:
    requested_books = int(input("How many books would you like? "))
except ValueError:
    print("Please enter a whole number.")

print(f"You requested {requested_books} books.")
```

If conversion fails, `requested_books` does not exist.

Correct:

```python
try:
    requested_books = int(input("How many books would you like? "))
    print(f"You requested {requested_books} books.")
except ValueError:
    print("Please enter a whole number.")
```

---

## Catching Every Error Without Naming One

Avoid:

```python
try:
    requested_books = int(input("How many books would you like? "))
except:
    print("Something went wrong.")
```

This hides which error the program expects.

Prefer:

```python
try:
    requested_books = int(input("How many books would you like? "))
except ValueError:
    print("Please enter a whole number.")
```

---

## Putting Too Much Code Inside try

Less clear:

```python
try:
    requested_books = int(input("How many books would you like? "))
    print("Checking the library.")
    print("Updating the display.")
    print("Preparing the checkout.")
except ValueError:
    print("Please enter a whole number.")
```

Clearer:

```python
try:
    requested_books = int(input("How many books would you like? "))
except ValueError:
    print("Please enter a whole number.")
```

Keep the protected section focused on the code likely to raise the expected error.

---

# Summary

Error handling allows a Python program to respond to expected runtime errors instead of crashing.

The basic structure is:

```python
try:
    risky_operation()
except ExpectedError:
    handle_the_error()
```

For user input converted with `int()`, the expected error is often `ValueError`.

The risky conversion must be inside the `try` block so Python can catch the error and run the matching `except` block.