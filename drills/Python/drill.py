user_name = input("What is your name? ")

cleaned_user_name = user_name.strip().title()
print(f"Hello {cleaned_user_name}")

view_book_selection = input("Would you like to view our book selection? ")
cleaned_selection_response = view_book_selection.strip().lower()

if cleaned_selection_response == "yes":
    print("The books will be shown")
elif cleaned_selection_response == "no":
    print("No worries. Have a nice day.")
else:
    print("Please type yes or no")

# String methods must be stored into a variable because they do not change the original string.
# They create a new string.
