# Python Drill 017 - Error Handling

## Objective

Practice using `try` and `except` from memory with user input, type conversion, conditions, and multiple error types.

---

## Rules

* No handbook
* No flashcards
* No internet
* Run the program from the terminal
* Write the code from memory
* Do not copy the lesson exercises
* Test every required input

---

## Scenario - Delivery Cost Calculator

Build a program that calculates a delivery cost based on package weight and delivery distance.

## Requirements

* Ask the user for the package weight in pounds.
* Convert the weight to a `float`.
* Ask the user for the delivery distance in miles.
* Convert the distance to an `int`.
* Protect both conversions with error handling.
* If either conversion fails, catch `ValueError`.
* Print:

```text
Please enter valid numbers.
```

* If the weight is `0` or less, print:

```text
Weight must be greater than zero.
```

* If the distance is `0` or less, print:

```text
Distance must be greater than zero.
```

* Calculate the base delivery cost:

```python
delivery_cost = weight * 0.75 + distance * 0.25
```

* If the package weighs more than `50` pounds, add a `$15.00` heavy-package fee.
* Print the final cost with exactly two decimal places.

Example:

```text
Delivery cost: $24.50
```

## Test With

* Weight `10.5` and distance `20`
* Weight `60` and distance `10`
* Weight `0` and distance `10`
* Weight `10` and distance `-5`
* Weight `heavy` and distance `10`
* Weight `10` and distance `far`

---

## Reflection

Time to Complete:

Syntax I Forgot:

Concepts I Was Unsure About:

Mistakes I Made:

Questions I Have: