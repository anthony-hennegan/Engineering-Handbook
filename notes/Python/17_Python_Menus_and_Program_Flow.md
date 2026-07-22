# Lesson 024 - Menus & Program Flow

## Objective

Learn how to organize a program around a main menu that lets the user choose what action to perform.

By the end of this lesson you should be able to:

- Display a menu of options.
- Let the user choose a feature.
- Execute only the selected feature.
- Return to the menu after each action.
- Exit the program when requested.

---

# Mental Model

Instead of the program deciding what happens next, the user decides.

Think of a librarian standing at the front desk.

The librarian asks:

```
How can I help you?
```

The customer chooses an option.

The librarian performs that task.

Then asks again.

This continues until the customer says they are finished.

---

# Program Flow

Before menus:

```
Start

↓

Greeting

↓

View Books

↓

Search

↓

Checkout

↓

Return

↓

Add

↓

Remove

↓

End
```

After menus:

```
Start

↓

Greeting

↓

Show Menu

↓

User chooses option

↓

Run selected feature

↓

Return to menu

↓

Repeat

↓

Exit
```

---

# Main Menu Loop

The application's main loop controls the entire program.

Conceptually:

```python
while True:

    show menu

    get user choice

    perform selected action

    repeat
```

The loop continues until the user selects Exit.

---

# Menu Responsibilities

## menus.py

Responsible for displaying the menu.

Example:

```python
show_main_menu(menu_options)
```

The menu function should only display information.

It should not:

- collect input
- run features
- modify program data

---

## main.py

Responsible for:

- asking for the user's choice
- deciding which feature to run
- calling the correct function

Example structure:

```python
if users_choice == "1":
    ...

elif users_choice == "2":
    ...

elif users_choice == "7":
    break
```

---

## catalog.py

Responsible for the library's behavior.

Examples:

- search books
- check out books
- return books
- add books
- remove books

It should not decide which menu option the user selected.

---

# Why Use Numbers?

The menu displays readable text:

```
1. View Books
2. Search Books
3. Check Out Book
```

The program uses the number to decide which feature to run.

Example:

```python
if users_choice == "1":
```

Using numbers is simpler than asking users to type the entire option name.

---

# break

The main loop ends only when the user chooses Exit.

Example:

```python
elif users_choice == "7":
    print("Thanks for stopping by!")
    break
```

`break` exits the menu loop and ends the program.

---

# Common Mistakes

### Comparing input to integers

Incorrect:

```python
if users_choice == 1:
```

`input()` returns a string.

Correct:

```python
if users_choice == "1":
```

---

### Ending the menu after one action

Incorrect:

```python
break
```

at the end of the loop.

The program should return to the menu after completing a feature.

Only Exit should end the loop.

---

### Putting feature logic inside the menu

The menu should decide **which** feature runs.

The feature functions should decide **how** that feature works.

Keep responsibilities separated.

---

# Project Application

The Library project now uses one main menu to access every feature.

Current features:

- View Books
- Search Books
- Check Out Book
- Return Book
- Add Book
- Remove Book
- Exit

Every feature returns to the main menu after completing.

---

# Best Practices

- One main loop controls the application.
- Menu functions display information only.
- Keep feature logic inside `catalog.py`.
- Use clear menu numbers.
- Only Exit should stop the application.

---

# Key Takeaways

- Menus let the user control program flow.
- The main loop keeps the application running.
- Each menu option calls one feature.
- Separate program control from business logic.
- Good programs are organized around small functions with one responsibility each.