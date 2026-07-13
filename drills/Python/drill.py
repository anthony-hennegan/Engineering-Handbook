reader_name = "Anthony henngan "

def format_name(name):
    return name.strip().title()

def greet_reader(name):
    print(f"Hello {name}")
    
reader_name = format_name(reader_name)
greet_reader(reader_name)

books = [
    {
        "title": "The Hobbit",
        "author": "Author 1",
        "checked_out": False
    },
    {
        "title": "The Book 2",
        "author": "Author 2",
        "checked_out": False
    },
    {
        "title": "The Book 3",
        "author": "Author 3",
        "checked_out": True
    }
]

def display_books(books_list):
    for book in books_list:
        print(f"{book["title"]} written by {book["author"]}")
        
def is_available(book):
    return not book["checked_out"]
for book in books:
    available = is_available(book)
    if available:
        print(f"{book['title']} is available.")
    else:
        print(f"{book['title']} is not available.")
        
# format_name returns a value because we need to use that value later.
# greet_reader prints instead of returns becuase we only want to display information to the user.
# is_available returns a boolean because we are accessing the checked_out key which is a boolean.
# One function one job means that each function should only perform a single action and not try to handle multiple.