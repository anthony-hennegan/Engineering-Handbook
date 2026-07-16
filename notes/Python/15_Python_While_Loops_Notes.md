# Lesson 018 - while Loops and Input Validation

## Purpose

`while` loops repeat code as long as a condition remains `True`.

They are useful when a program needs to keep asking for input until the user enters a valid response.

---

# Key Concepts

## while Loops

A `while` loop repeats its indented code while its condition is `True`.

Example:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

Output:

```text
1
2
3
```

The loop stops when:

```python
count <= 3
```

becomes `False`.

---

## Updating the Loop Condition

A `while` loop must usually change something that affects its condition.

Example:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

This line updates the value:

```python
count += 1
```

Without that update, `count` would stay at `1` and the loop would never stop.

---

## Infinite Loops

An infinite loop continues because its condition never becomes `False`.

Example:

```python
count = 1

while count <= 3:
    print(count)
```

The value of `count` never changes.

Output continues indefinitely:

```text
1
1
1
1
```

The program must be stopped manually.

---

## while True

The condition in this loop is always `True`:

```python
while True:
    print("Running")
```

Because the condition never becomes `False`, the loop continues until something inside the loop stops it.

`while True` is useful when the exit decision depends on input received inside the loop.

---

## break

`break` immediately exits the nearest loop.

Example:

```python
while True:
    response = input("Type yes: ")

    if response == "yes":
        break
```

If the user enters anything except `"yes"`, the loop repeats.

If the user enters `"yes"`, Python reaches:

```python
break
```

and exits the loop.

---

## Input Validation

Input validation checks whether the user's input follows the program's rules.

Example:

```python
while True:
    response = input("Enter yes or no: ")
    response = response.strip().lower()

    if response == "yes" or response == "no":
        break

    print("Please enter yes or no.")
```

The loop continues until the response is valid.

---

## Validating Integer Input

`while True`, `try`, `except`, and `break` can work together.

Example:

```python
while True:
    age_response = input("Enter your age: ")

    try:
        age = int(age_response)
        break
    except ValueError:
        print("Please enter a whole number.")
```

If the conversion fails, Python runs the `except` block.

Because Python does not reach `break`, the loop repeats.

If the conversion succeeds, Python reaches `break` and exits the loop.

---

## Validating More Than Type

A successful conversion does not always mean the value is acceptable.

Example:

```python
while True:
    quantity_response = input("Enter a quantity: ")

    try:
        quantity = int(quantity_response)

        if quantity > 0:
            break

        print("Quantity must be greater than zero.")

    except ValueError:
        print("Please enter a whole number.")
```

The input must satisfy two rules:

* It must convert to an integer.
* It must be greater than zero.

The loop exits only after both rules are satisfied.

---

## Code After the Loop

After `break` exits the loop, Python continues with the next unindented line.

Example:

```python
while True:
    number_response = input("Enter a number: ")

    try:
        number = int(number_response)
        break
    except ValueError:
        print("Please enter a whole number.")

print(f"You entered {number}.")
```

The final `print()` runs only after valid input has been received.

---

## Using a Boolean Loop Condition

A loop can also use a Boolean variable instead of `while True`.

Example:

```python
valid_input = False

while not valid_input:
    response = input("Enter yes or no: ")
    response = response.strip().lower()

    if response == "yes" or response == "no":
        valid_input = True
    else:
        print("Please enter yes or no.")
```

The loop stops when:

```python
valid_input = True
```

This works, but `while True` with `break` can be simpler when the exit condition is checked inside the loop.

---

# Project Use

The Library CLI App asks how many books the reader wants to check out.

Without a loop:

```python
requested_books = input(
    "How many books would you like to check out? "
)

try:
    requested_books = int(requested_books)
except ValueError:
    print("Please enter a whole number.")
```

The program prints an error once but does not ask again.

A loop can repeat the prompt until valid input is received:

```python
while True:
    requested_books_response = input(
        "How many books would you like to check out? "
    )

    try:
        requested_books = int(requested_books_response)

        if requested_books < 0:
            print("Please enter zero or a positive number.")
        else:
            break

    except ValueError:
        print("Please enter a whole number.")
```

After the loop:

```python
if 0 < requested_books <= checkout_limit and is_open:
    print("Perfect. Let's get you fixed up.")
elif requested_books == 0:
    print("No worries. Have a nice day.")
else:
    print("Checkout is not available.")
```

The checkout logic only runs after `requested_books` contains a valid integer.

---

## Validating Yes or No Input

The book-selection question can also repeat until the reader enters an accepted response.

```python
while True:
    view_selection_response = input(
        "Would you like to view our book selection? "
    )

    view_selection_response = format_response(
        view_selection_response
    )

    if (
        view_selection_response == "yes"
        or view_selection_response == "y"
        or view_selection_response == "no"
        or view_selection_response == "n"
    ):
        break

    print("Please type yes or no.")
```

After the loop, the response is known to be valid.

```python
if (
    view_selection_response == "yes"
    or view_selection_response == "y"
):
    display_available_books(books)
else:
    print("No worries. Have a nice day!")
```

---

# Important Rules

* A `while` loop repeats while its condition is `True`.
* Code inside the loop must be indented.
* The loop condition must eventually change unless `break` is used.
* `while True` creates a loop with no automatic ending.
* `break` immediately exits the nearest loop.
* Code after the loop runs after `break`.
* Invalid input should not reach `break`.
* Valid input should reach `break`.
* A successful type conversion does not guarantee the value follows all program rules.
* Validate both the data type and the allowed value.
* Be careful to avoid accidental infinite loops.

---

# Common Mistakes

## Forgetting to Update the Condition

Incorrect:

```python
count = 1

while count <= 3:
    print(count)
```

The loop never changes `count`.

Correct:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

---

## Forgetting break in while True

Incorrect:

```python
while True:
    response = input("Type yes: ")

    if response == "yes":
        print("Correct.")
```

Even after the user enters `"yes"`, the loop repeats.

Correct:

```python
while True:
    response = input("Type yes: ")

    if response == "yes":
        print("Correct.")
        break
```

---

## Breaking After Invalid Input

Incorrect:

```python
while True:
    age_response = input("Enter your age: ")

    try:
        age = int(age_response)
    except ValueError:
        print("Please enter a whole number.")

    break
```

The `break` runs whether the input is valid or invalid.

Correct:

```python
while True:
    age_response = input("Enter your age: ")

    try:
        age = int(age_response)
        break
    except ValueError:
        print("Please enter a whole number.")
```

---

## Using an Invalid Value After Conversion

Incorrect:

```python
while True:
    quantity = int(input("Enter a quantity: "))
    break
```

A negative number successfully converts to an integer, so the loop exits even if negative quantities are not allowed.

Correct:

```python
while True:
    quantity_response = input("Enter a quantity: ")

    try:
        quantity = int(quantity_response)

        if quantity > 0:
            break

        print("Quantity must be greater than zero.")

    except ValueError:
        print("Please enter a whole number.")
```

---

## Placing Dependent Code Before Validation Finishes

Incorrect:

```python
while True:
    requested_books_response = input(
        "How many books would you like? "
    )

    try:
        requested_books = int(requested_books_response)
    except ValueError:
        print("Please enter a whole number.")

    print(f"You requested {requested_books} books.")
```

If conversion fails, `requested_books` may not contain a valid integer.

Correct:

```python
while True:
    requested_books_response = input(
        "How many books would you like? "
    )

    try:
        requested_books = int(requested_books_response)
        break
    except ValueError:
        print("Please enter a whole number.")

print(f"You requested {requested_books} books.")
```

---

## Creating an Unnecessary Loop Variable

More complicated:

```python
keep_asking = True

while keep_asking:
    response = input("Type yes: ")

    if response == "yes":
        keep_asking = False
```

Simpler:

```python
while True:
    response = input("Type yes: ")

    if response == "yes":
        break
```

Both work, but `while True` with `break` is often clearer when the exit rule is inside the loop.

---

# Summary

A `while` loop repeats code while its condition remains `True`.

The pattern:

```python
while True:
    user_input = input("Enter a value: ")

    if input_is_valid:
        break
```

is useful for input validation.

When type conversion may fail, combine the loop with error handling:

```python
while True:
    response = input("Enter a whole number: ")

    try:
        number = int(response)
        break
    except ValueError:
        print("Please enter a whole number.")
```

Invalid input causes the loop to repeat. Valid input reaches `break`, exits the loop, and allows the rest of the program to continue.