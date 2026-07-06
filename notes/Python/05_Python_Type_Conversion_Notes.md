# Lesson 007 - Numbers and Type Conversion

## Purpose

Type conversion allows a program to change a value from one data type into another data type.

This is important because `input()` always returns a string, even when the user types a number.

If the program needs to do math or numeric comparisons, the input must be converted first.

---

# Key Concepts

## Integer

An integer is a whole number.

Examples:

```python
1
3
20
-5
```

Integers are useful for counting things.

Library project examples:

```python
book_count = 20
requested_books = 3
checkout_limit = 3
```

---

## Float

A float is a decimal number.

Examples:

```python
3.5
10.0
0.25
1.50
```

Floats are useful when values may include decimals.

Examples:

```python
late_fee = 1.50
tax_rate = 0.0825
```

---

## String Number

A string number looks like a number but is stored as text.

Example:

```python
"3"
```

This is not the same as:

```python
3
```

Python treats these differently:

```python
"3"   # string
3     # integer
```

---

# `input()` Always Returns a String

When using `input()`, Python always returns a string.

Example:

```python
book_count = input("How many books do you own? ")

print(book_count)
print(type(book_count))
```

If the user types:

```text
20
```

Python stores it as:

```python
"20"
```

The type is:

```text
<class 'str'>
```

---

# Type Conversion Functions

## `int()`

`int()` converts a value into an integer.

Example:

```python
book_count = int("3")

print(book_count)
print(type(book_count))
```

Output:

```text
3
<class 'int'>
```

Use `int()` when you need a whole number.

---

## `float()`

`float()` converts a value into a decimal number.

Example:

```python
late_fee = float("1.50")

print(late_fee)
print(type(late_fee))
```

Output:

```text
1.5
<class 'float'>
```

Use `float()` when decimal values are allowed.

---

## `str()`

`str()` converts a value into a string.

Example:

```python
book_count = 20

book_count_text = str(book_count)

print(book_count_text)
print(type(book_count_text))
```

Output:

```text
20
<class 'str'>
```

Use `str()` when a value needs to be treated as text.

---

# Converting User Input

Because `input()` returns a string, numeric input must be converted before doing numeric comparisons or math.

Example:

```python
requested_books = input("How many books do you want to check out? ")
requested_books = int(requested_books)
```

Now `requested_books` can be used like a number.

---

# Numeric Comparisons

This does not work:

```python
requested_books = input("How many books? ")

if requested_books > 3:
    print("Too many books.")
```

The problem is that `requested_books` is a string, but `3` is an integer.

This works:

```python
requested_books = input("How many books? ")
requested_books = int(requested_books)

if requested_books > 3:
    print("Too many books.")
else:
    print("Checkout amount approved.")
```

---

# Conversion Errors

`int()` only works when the value can be converted into a whole number.

This works:

```python
int("5")
```

This fails:

```python
int("five")
```

This also fails:

```python
int("5.5")
```

`"five"` fails because it is word text.

`"5.5"` fails because it represents a decimal, not a whole number.

Invalid conversions raise a `ValueError`.

Error handling will be covered later.

---

# Function vs Method

`int()`, `float()`, and `str()` are functions.

They are called like this:

```python
int("5")
float("1.50")
str(20)
```

String methods are called on a string value.

Example:

```python
" YES ".strip()
```

---

# Project Use

In the Library project, type conversion is used to ask how many books the reader wants to check out.

Example:

```python
requested_books = input("How many books would you like to check out? ")
requested_books = int(requested_books)

if requested_books > 3:
    print("Sorry, you can check out no more than 3 books.")
else:
    print("Perfect. Let's get you fixed up.")
```

This logic should only run when the user says they want to view or check out books.

Example:

```python
if cleaned_selection_response == "yes":
    print("Ok, here is what we have.")

    requested_books = input("How many books would you like to check out? ")
    requested_books = int(requested_books)

    if requested_books > 3:
        print("Sorry, you can check out no more than 3 books.")
    else:
        print("Perfect. Let's get you fixed up.")

elif cleaned_selection_response == "no":
    print("No worries. Have a nice day!")
else:
    print("Please type yes or no.")
```

---

# Important Rules

- `input()` always returns a string.
- `int()` converts a value into an integer.
- `float()` converts a value into a decimal number.
- `str()` converts a value into a string.
- Numeric input must be converted before doing math.
- Numeric input must be converted before numeric comparisons.
- `int()` only works with values that represent whole numbers.
- Invalid conversions cause errors.
- `int()`, `float()`, and `str()` are functions, not methods.

---

# Common Mistakes

## Comparing a String to a Number

Incorrect:

```python
requested_books = input("How many books? ")

if requested_books > 3:
    print("Too many books.")
```

Correct:

```python
requested_books = input("How many books? ")
requested_books = int(requested_books)

if requested_books > 3:
    print("Too many books.")
```

---

## Forgetting That `input()` Returns Text

Problem:

```python
age = input("How old are you? ")

print(type(age))
```

Even if the user types:

```text
34
```

the type is:

```text
<class 'str'>
```

---

## Trying to Convert Invalid Input

This works:

```python
int("5")
```

This does not:

```python
int("five")
```

This does not:

```python
int("5.5")
```

Use `float()` for decimal numbers:

```python
float("5.5")
```

---

# Summary

`input()` always gives the program text.

When the program needs to treat that text as a number, convert it.

Use:

```python
int()
```

for whole numbers.

Use:

```python
float()
```

for decimal numbers.

Use:

```python
str()
```

to convert a value into text.

The most important rule is:

```text
Convert numeric input before doing math or numeric comparisons.
```