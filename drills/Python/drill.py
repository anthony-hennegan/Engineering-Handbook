def show_message():
    print("Hello world.")
show_message()

def show_welcome_message():
    print("Welcome to Bailey's Books")
show_welcome_message()

def greet_reader(name):
    print(f"Hello {name}")
greet_reader("Anthony")
greet_reader("tony")

books = ["Book1", "Book2", "Book3"]

def display_books(book_list):
    for book in book_list:
        print(book)
display_books(books)

# A function is reusable block of code.
# A parameter is a placeholder in a fuction.
# An argument is the value used when calling the function.
# When a function is written it is only being defined. It must be called for the functions code block to execute.