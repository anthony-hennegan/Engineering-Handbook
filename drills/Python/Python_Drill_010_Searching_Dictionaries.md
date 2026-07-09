# Python Drill 014 - Check Out a Book

## Objective

Practice finding a book dictionary, updating its `checked_out` value, and printing the updated library status.

---

## Rules

- No handbook
- No flashcards
- No internet
- Run the program from the terminal
- Write the code from memory
- Use your previous drill only after your first attempt

---

## Tasks

- [ ] Create a new Python file for the drill.
- [ ] Create a list named `books`.
- [ ] Add at least three dictionaries inside the `books` list.
- [ ] Each dictionary should represent one book.
- [ ] Each book dictionary should have:
  - `title`
  - `author`
  - `checked_out`
- [ ] Set at least one book’s `checked_out` value to `False`.
- [ ] Create a variable named `checkout_title`.
- [ ] Set `checkout_title` to the title of one book in the list.
- [ ] Create a variable named `found_book`.
- [ ] Set `found_book` to `False`.
- [ ] Use a `for` loop to loop through the `books` list.
- [ ] Inside the loop, check whether the current book’s title matches `checkout_title`.
- [ ] If the title matches, change `found_book` to `True`.
- [ ] If the title matches, check whether the book is already checked out.
- [ ] If the book is already checked out, print a message saying it is already checked out.
- [ ] If the book is not checked out, change its `checked_out` value to `True`.
- [ ] Print a message saying the book was checked out.
- [ ] After the loop, check whether `found_book` is still `False`.
- [ ] If `found_book` is still `False`, print `"Book not found."`
- [ ] After the checkout logic, print a heading named `"Library Status:"`.
- [ ] Use another `for` loop to print every book’s checkout status.
- [ ] Print one message for checked-out books.
- [ ] Print a different message for available books.
- [ ] Run the program once with a title that exists.
- [ ] Run the program again with a title that does not exist.
- [ ] Run the program again with a book that is already checked out.
- [ ] Add a comment explaining what changes the dictionary value.
- [ ] Add a comment explaining why we check whether the book is already checked out.
- [ ] Add a comment explaining why the final status loop shows the updated value.

---

## Reflection

Time to Complete:

Syntax I Forgot:

Concepts I Was Unsure About:

Mistakes I Made:

Questions I Have: