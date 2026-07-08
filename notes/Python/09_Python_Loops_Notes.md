# Loops

## Purpose

Loops allow a program to repeat an action.

They are useful when working with collections like lists.

In the Library project, loops allow the program to print every book in the catalog without writing one `print()` statement for each book.

---

# Key Concepts

## Loop

A loop repeats a block of code.

Example:

```python
books = ["The Alchemist", "Dune", "The Hobbit"]

for book in books:
    print(book)
```

This means:

```text
For each book in the books list, print the book.
```

---

# `for` Loop

A `for` loop is used to repeat an action for each item in a collection.

Pattern:

```python
for item in collection:
    # use item here
```

Example:

```python
books = ["The Alchemist", "Dune", "The Hobbit"]

for book in books:
    print(book)
```

Output:

```text
The Alchemist
Dune
The Hobbit
```

---

# Loop Variable

The loop variable is a temporary variable that refers to the current item during each pass through the loop.

Example:

```python
for book in books:
    print(book)
```

In this example:

```text
book
```

is the loop variable.

The list is:

```text
books
```

Each time through the loop, `book` refers to the next item in the `books` list.

---

# Indentation

The indented code under a loop is the code that repeats.

Example:

```python
for book in books:
    print(book)
```

This repeats:

```python
print(book)
```

If a line is not indented under the loop, it does not repeat.

Example:

```python
for book in books:
    print(book)

print("Done")
```

This prints every book, then prints `"Done"` once.

---

# Why Loops Are Useful

Without a loop:

```python
print(books[0])
print(books[1])
print(books[2])
```

This only works if there are exactly three books.

With a loop:

```python
for book in books:
    print(book)
```

This works no matter how many books are in the list.

---

# Project Use

In the Library project, loops are used to display every book in the catalog.

Example:

```python
books = ["The Alchemist", "Dune", "The Hobbit"]

print("Available books:")

for book in books:
    print(book)
```

If a new book is added to the list, the loop prints it automatically.

---

# Important Rules

- A loop repeats a block of code.
- A `for` loop repeats once for each item in a collection.
- The loop variable is temporary.
- The loop variable refers to the current item.
- Indentation controls what code repeats.
- A loop makes code easier to update when working with lists.

---

# Common Mistakes

## Forgetting the Colon

Incorrect:

```python
for book in books
    print(book)
```

Correct:

```python
for book in books:
    print(book)
```

---

## Forgetting Indentation

Incorrect:

```python
for book in books:
print(book)
```

Correct:

```python
for book in books:
    print(book)
```

---

## Confusing the List and the Loop Variable

```python
for book in books:
    print(book)
```

`books` is the full list.

`book` is one item from the list during the current loop pass.

---

# Summary

Loops allow a program to repeat an action.

A `for` loop is especially useful for lists because it can run once for every item in the list.

In the Library project, a loop lets the program display every book without manually writing a `print()` statement for each one.