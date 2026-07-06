# Comparison Operators

## Purpose

Comparison operators allow a program to compare values.

A comparison produces a boolean result:

```python
True
```

or:

```python
False
```

Comparison operators are often used inside conditionals.

---

# Key Concepts

## Assignment vs Comparison

Assignment stores a value in a variable.

Example:

```python
book_limit = 3
```

This means:

```text
The variable book_limit refers to the value 3.
```

Comparison checks whether two values match a condition.

Example:

```python
book_limit == 3
```

This asks:

```text
Is book_limit equal to 3?
```

---

# Common Comparison Operators

## Equal To

```python
==
```

Checks whether two values are equal.

Example:

```python
3 == 3
```

Result:

```python
True
```

---

## Not Equal To

```python
!=
```

Checks whether two values are not equal.

Example:

```python
3 != 4
```

Result:

```python
True
```

---

## Greater Than

```python
>
```

Checks whether the left value is greater than the right value.

Example:

```python
5 > 3
```

Result:

```python
True
```

---

## Less Than

```python
<
```

Checks whether the left value is less than the right value.

Example:

```python
2 < 3
```

Result:

```python
True
```

---

## Greater Than or Equal To

```python
>=
```

Checks whether the left value is greater than or equal to the right value.

Example:

```python
3 >= 3
```

Result:

```python
True
```

---

## Less Than or Equal To

```python
<=
```

Checks whether the left value is less than or equal to the right value.

Example:

```python
3 <= 5
```

Result:

```python
True
```

---

# Project Use

In the Library project, comparison operators are used to check whether a requested number of books is allowed.

Example:

```python
requested_books = int(input("How many books would you like to check out? "))

if requested_books > 3:
    print("Sorry, you can check out no more than 3 books.")
else:
    print("Perfect. Let's get you fixed up.")
```

The comparison:

```python
requested_books > 3
```

asks:

```text
Is the requested number of books greater than 3?
```

---

# Important Rules

- `=` assigns a value.
- `==` compares two values.
- Comparisons return `True` or `False`.
- Comparison operators are commonly used in `if`, `elif`, and `else` logic.
- Numeric comparisons require numeric values.
- String comparisons are exact.

---

# Summary

Comparison operators let Python ask true-or-false questions.

They are the foundation of decision-making in conditionals.