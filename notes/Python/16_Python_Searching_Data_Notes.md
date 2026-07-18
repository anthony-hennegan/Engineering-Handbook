# Lesson 019 - Searching Data

## Objective

Learn how to search through a list of dictionaries to find a specific item.

By the end of this lesson you should be able to:

- Search for an item in a list.
- Compare values inside dictionaries.
- Stop searching once a match is found.
- Detect when no match exists.
- Apply searching to your Library project.

---

# Mental Model

Searching is checking one item at a time until you either:

- find what you're looking for, or
- reach the end of the list.

Think of it like looking for a specific book on a shelf.

You pick up one book.

Is this the one?

- Yes → stop searching.
- No → move to the next book.

Repeat until finished.

---

# Search Algorithm

```
Get search title

↓

Look at first book

↓

Does the title match?

↓

Yes
    Save the result
    Stop searching

No
    Continue to next book

↓

Loop ends

↓

Was a book found?

↓

Yes
    Display the book

No
    Print "Book not found."
```

---

# Basic Search Pattern

```python
found_book = False

for book in books:
    if book["title"].lower() == search_title:
        found_book = True
        print(book)
        break

if not found_book:
    print("Book not found.")
```

---

# Why Use a Flag?

A flag is a variable that remembers whether something happened.

Example:

```python
found_book = False
```

At the beginning of the search, assume nothing has been found.

If a matching book is discovered:

```python
found_book = True
```

After the loop:

```python
if not found_book:
    print("Book not found.")
```

The flag remembers what happened while the loop was running.

---

# Why "Book not found." Goes After the Loop

Incorrect:

```python
for book in books:
    if book["title"] == search_title:
        print(book)
    else:
        print("Book not found.")
```

Problem:

The message prints after checking only one book.

Correct:

Finish checking every book first.

Only after the search is complete can you know that no match exists.

---

# break

When the correct book is found:

```python
break
```

This immediately exits the loop.

There is no reason to continue searching because the job is complete.

---

# Common Mistakes

### Printing "Book not found" inside the loop

Incorrect:

```python
else:
    print("Book not found.")
```

Correct:

Print it after the loop.

---

### Forgetting the flag

Without a flag, the program cannot remember whether a book was found.

---

### Forgetting break

Without `break`, the loop keeps searching even after finding the correct book.

---

# Project Application

Search functionality belongs in the catalog.

Example structure:

```
main.py
    Ask the user for a title.
    Call the search function.

catalog.py
    Search the books.
    Display the matching book.
```

Current project search:

- Ask for a title.
- Search every book.
- Display title.
- Display author.
- Display availability.
- Print "Book not found." when necessary.

---

# Best Practices

- Compare lowercase strings for case-insensitive searching.
- Stop searching with `break` after a match.
- Use descriptive variable names like `found_book`.
- Keep searching logic inside `catalog.py`.
- Keep user interaction inside `main.py`.

---

# Key Takeaways

- Searching checks one item at a time.
- A flag remembers whether a match was found.
- `break` ends the search immediately after success.
- "Book not found." should only be printed after the entire search finishes.
- Separating search logic from user interaction makes the program easier to maintain.