is_open = True
checkout_limit = 3

response_view_books = input("Would you like to view our books? ")
response_view_books = response_view_books.strip().lower()

if response_view_books == "yes" or response_view_books == "y":
    reponse_book_count = input("How many books would you like to check out? ")
    reponse_book_count = int(reponse_book_count.strip())
    if is_open and reponse_book_count <= checkout_limit:
        print("Checkout approved.")
    else: 
        print("Checkout is not available.")
elif response_view_books == "no" or response_view_books == "n":
    print("No worries. Hava a nice day.")
else:
    print("Please type yes or no.")
    
if not is_open:
    print("The library is closed.")
# and requires all conditions to be true.
# or allows multiple conditions to be true.
# not validates the reverse of a boolean value.