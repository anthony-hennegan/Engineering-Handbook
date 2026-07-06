# Lesson 006 - String Methods

## Purpose

String methods allow a program to clean, format, or transform text.

They are useful for handling user input because users may type extra spaces or different capitalization.

---

# Key Concepts

## String Method

A string method is an action that can be called on a string value.

Example:

```python
"YES".lower()
```

Result:

```text
yes
```

String methods return a new string.

They do not automatically change the original string.

---

# Common String Methods

## `.lower()`

Converts a string to lowercase.

Example:

```python
answer = "YES"

print(answer.lower())
```

Output:

```text
yes
```

The original variable does not change unless the result is stored.

Example:

```python
answer = "YES"

answer.lower()

print(answer)
```

Output:

```text
YES
```

Correct version:

```python
answer = "YES"

answer = answer.lower()

print(answer)
```

Output:

```text
yes
```

---

## `.upper()`

Converts a string to uppercase.

Example:

```python
answer = "yes"

print(answer.upper())
```

Output:

```text
YES
```

This can be useful for formatting headings or emphasizing text.

---

## `.strip()`

Removes whitespace from the beginning and end of a string.

Example:

```python
answer = " yes "

print(answer.strip())
```

Output:

```text
yes
```

`.strip()` does not remove spaces from the middle of a string.

Example:

```python
answer = "yes or no"

print(answer.strip())
```

Output:

```text
yes or no
```

---

## `.title()`

Capitalizes the first letter of each word.

Example:

```python
reader_name = "anthony hennegan"

formatted_name = reader_name.title()

print(formatted_name)
```

Output:

```text
Anthony Hennegan
```

This is useful for formatting names or display text.

---

# Method Chaining

Method chaining means calling multiple methods one after another.

Example:

```python
answer = " YES "

clean_answer = answer.strip().lower()

print(clean_answer)
```

Output:

```text
yes
```

In this example:

1. `.strip()` runs first.
2. `.lower()` runs second.
3. The final cleaned value is stored in `clean_answer`.

---

# Normalizing Input

Normalizing input means converting user input into a consistent format before checking it.

Example:

```python
view_selection = input("Would you like to view our book selection? ")

cleaned_selection_response = view_selection.strip().lower()
```

This makes these inputs:

```text
yes
Yes
YES
 yes
yes 
```

all become:

```text
yes
```

That makes conditionals more reliable.

Example:

```python
view_selection = input("Would you like to view our book selection? ")

cleaned_selection_response = view_selection.strip().lower()

if cleaned_selection_response == "yes":
    print("Ok, here is what we have.")
elif cleaned_selection_response == "no":
    print("No worries. Have a nice day!")
else:
    print("Please type yes or no.")
```

---

# Project Use

In the Library project, string methods are used to clean the reader's name and normalize yes or no responses.

Example:

```python
reader_name = input("What is your name? ")
formatted_name = reader_name.strip().title()

print(f"Hello {formatted_name}.")

view_selection = input("Would you like to view our book selection? ")
cleaned_selection_response = view_selection.strip().lower()

if cleaned_selection_response == "yes":
    print("Ok, here is what we have.")
elif cleaned_selection_response == "no":
    print("No worries. Have a nice day!")
else:
    print("Please type yes or no.")
```

---

# Important Rules

- String methods return new strings.
- String methods do not automatically change the original variable.
- Store the result if you want to keep the changed value.
- `.lower()` converts text to lowercase.
- `.upper()` converts text to uppercase.
- `.strip()` removes whitespace from the beginning and end.
- `.title()` capitalizes the first letter of each word.
- Method chaining allows multiple methods to be applied in one statement.
- Normalizing input makes user responses easier to compare.

---

# Common Mistakes

## Forgetting to Store the Result

Incorrect:

```python
answer = " YES "

answer.strip().lower()

print(answer)
```

Output:

```text
 YES 
```

Correct:

```python
answer = " YES "

answer = answer.strip().lower()

print(answer)
```

Output:

```text
yes
```

---

## Comparing Uncleaned Input

Problem:

```python
answer = input("Continue? ")

if answer == "yes":
    print("Continuing.")
else:
    print("Please type yes or no.")
```

If the user types:

```text
Yes
```

the condition fails because:

```python
"Yes" == "yes"
```

is:

```python
False
```

Better:

```python
answer = input("Continue? ")
answer = answer.strip().lower()

if answer == "yes":
    print("Continuing.")
else:
    print("Please type yes or no.")
```

---

# Summary

String methods are tools for cleaning and formatting text.

They are especially useful when working with user input.

Because users may type extra spaces or different capitalization, programs should normalize input before comparing it.

The most important rule is:

```text
String methods return new strings. Store the result if you want to keep it.
```