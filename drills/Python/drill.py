checkout_limit = 3
book_count = input("How many books would you like to check out? ")
book_count = int(book_count)

if book_count > checkout_limit:
    print("That exceeds the checkout limit.")
else:
    print("Checkout approved.")


user_name = input("What is your name? ")
user_name = user_name.strip().title()

if user_name:
    print(f"Hello {user_name}")
else:
    print("A name is required.")
    
# = assigns, and == compares.