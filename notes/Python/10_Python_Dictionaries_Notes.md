# Lesson 012 - Dictionaries

## Purpose

Dictionaries allow a program to store related information together.

They are useful when one item has multiple pieces of data.

In the Library project, a dictionary can represent one book with a title, author, and checkout status.

---

# Key Concepts

## Dictionary

A dictionary is a collection of key-value pairs.

Example:

```python
book = {
    "title": "Dune",
    "author": "Frank Herbert",
    "is_checked_out": False
}
```

This dictionary represents one book.

---

# Key-Value Pair

A key-value pair connects a name to a value.

Example:

```python
"title": "Dune"
```

The key is:

```text
"title"
```

The value is:

```text
"Dune"
```

---

# Why Dictionaries Are Useful

This works, but the data is separated:

```python
book_title = "Dune"
book_author = "Frank Herbert"
book_is_checked_out = False
```

This is better:

```python
book = {
    "title": "Dune",
    "author": "Frank Herbert",
    "is_checked_out": False
}
```

The dictionary keeps all information about one book together.

---

# Accessing Values

Use the key inside square brackets to access a value.

Example:

```python
book = {
    "title": "Dune",
    "author": "Frank Herbert",
    "is_checked_out": False
}

print(book["title"])
```

Output:

```text
Dune
```

Another example:

```python
print(book["author"])
```

Output:

```text
Frank Herbert
```

---

# Updating Values

A dictionary value can be updated by assigning a new value to a key.

Example:

```python
book = {
    "title": "Dune",
    "author": "Frank Herbert",
    "is_checked_out": False
}

book["is_checked_out"] = True

print(book["is_checked_out"])
```

Output:

```text
True
```

---

# Adding New Key-Value Pairs

You can add a new key-value pair by assigning a value to a new key.

Example:

```python
book = {
    "title": "Dune",
    "author": "Frank Herbert"
}

book["is_checked_out"] = False

print(book)
```

---

# Dictionary Keys

Keys are used to look up values.

Example:

```python
book["title"]
```

The key must exist, or Python raises a `KeyError`.

Example:

```python
book["publisher"]
```

If `"publisher"` is not a key in the dictionary, Python raises a `KeyError`.

---

# Project Use

In the Library project, a dictionary can represent one book.

Example:

```python
book = {
    "title": "Dune",
    "author": "Frank Herbert",
    "is_checked_out": False
}
```

The program can access the title:

```python
print(book["title"])
```

The program can access the author:

```python
print(book["author"])
```

The program can update checkout status:

```python
book["is_checked_out"] = True
```

---

# Important Rules

- A dictionary stores key-value pairs.
- Keys are used to access values.
- Values can be strings, numbers, booleans, lists, or other dictionaries.
- Use curly braces to create a dictionary.
- Use square brackets and a key to access a value.
- Assigning to an existing key updates the value.
- Assigning to a new key adds a new key-value pair.
- Accessing a missing key causes a `KeyError`.

---

# Common Mistakes

## Forgetting Quotes Around String Keys

Incorrect:

```python
book[title]
```

Correct:

```python
book["title"]
```

---

## Accessing a Key That Does Not Exist

Problem:

```python
book = {
    "title": "Dune"
}

print(book["author"])
```

This causes a `KeyError` because `"author"` does not exist in the dictionary.

---

## Using Separate Variables Instead of One Dictionary

Less useful:

```python
book_title = "Dune"
book_author = "Frank Herbert"
book_is_checked_out = False
```

Better:

```python
book = {
    "title": "Dune",
    "author": "Frank Herbert",
    "is_checked_out": False
}
```

---

# Summary

A dictionary stores related information using key-value pairs.

Dictionaries are useful when one item has multiple pieces of data.

In the Library project, dictionaries let us represent a book as a structured record instead of only a title string.