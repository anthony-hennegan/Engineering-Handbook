# Lesson 010 - Lists

## Purpose

Lists allow a program to store multiple values in one variable.

They are useful when working with collections of related data.

In the Library project, a list can store multiple book titles.

---

# Key Concepts

## List

A list is a collection of values stored in one variable.

Example:

```python
books = ["The Hobbit", "Dune", "The Alchemist"]
```

The variable `books` refers to a list containing three string values.

---

## Why Lists Are Useful

This is hard to scale:

```python
book_1 = "The Hobbit"
book_2 = "Dune"
book_3 = "The Alchemist"
```

This is better:

```python
books = ["The Hobbit", "Dune", "The Alchemist"]
```

A list is easier to:

- count
- print
- search
- add to
- remove from
- loop through

---

# Indexes

Each item in a list has a position called an index.

Python list indexes start at `0`.

Example:

```python
books = ["The Hobbit", "Dune", "The Alchemist"]
```

Indexes:

```text
books[0] → "The Hobbit"
books[1] → "Dune"
books[2] → "The Alchemist"
```

Example:

```python
print(books[0])
```

Output:

```text
The Hobbit
```

---

# Common List Operations

## Print the Whole List

```python
books = ["The Hobbit", "Dune", "The Alchemist"]

print(books)
```

---

## Access One Item

```python
books = ["The Hobbit", "Dune", "The Alchemist"]

print(books[1])
```

Output:

```text
Dune
```

---

## Add an Item

Use `.append()` to add an item to the end of a list.

```python
books = ["The Hobbit", "Dune"]

books.append("The Alchemist")

print(books)
```

Output:

```text
['The Hobbit', 'Dune', 'The Alchemist']
```

---

## Count Items

Use `len()` to count how many items are in a list.

```python
books = ["The Hobbit", "Dune", "The Alchemist"]

print(len(books))
```

Output:

```text
3
```

---

## Remove an Item

Use `.remove()` to remove a specific item from a list.

```python
books = ["The Hobbit", "Dune", "The Alchemist"]

books.remove("Dune")

print(books)
```

Output:

```text
['The Hobbit', 'The Alchemist']
```

---

# Project Use

In the Library project, a list can store available book titles.

Example:

```python
books = ["The Hobbit", "Dune", "The Alchemist"]
```

The program can then show the list, count the books, add books, or remove books.

Example:

```python
print(f"We have {len(books)} books available.")
print(books)
```

---

# Important Rules

- A list stores multiple values in one variable.
- List items are ordered.
- List indexes start at `0`.
- Use square brackets to create a list.
- Use square brackets with an index to access one item.
- Use `.append()` to add an item.
- Use `.remove()` to remove an item.
- Use `len()` to count items.

---

# Common Mistakes

## Forgetting That Indexes Start at 0

```python
books = ["The Hobbit", "Dune", "The Alchemist"]

print(books[1])
```

This prints:

```text
Dune
```

not:

```text
The Hobbit
```

---

## Using Separate Variables Instead of a List

Less useful:

```python
book_1 = "The Hobbit"
book_2 = "Dune"
book_3 = "The Alchemist"
```

Better:

```python
books = ["The Hobbit", "Dune", "The Alchemist"]
```

---

# Summary

A list stores multiple values in one variable.

Lists are useful when a program needs to work with a collection of related values.

For the Library project, lists are the first step toward storing a real book catalog.