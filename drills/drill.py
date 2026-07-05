library_open = input("Is the library open? ")

if library_open == "yes":
    print("The library is Open!")
elif library_open == "no":
    print("The library is Closed.")
else:
    print("Please type yes or no")
    
view_books = input("Would you like to view our book selection? ")
if view_books == "yes":
    print("The books will be shown")
elif view_books == "no":
    print("No worries. Take care!")
else:
    print("Please type yes or no")
    
library_open = True

if library_open:
    print("The library is open")