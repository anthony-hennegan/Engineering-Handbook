books = [
    {
        "title": "Book1",
        "author": "Author1",
        "checked_out": True
    },
    {
        "title": "Book2",
        "author": "Author2",
        "checked_out": False
    },
    {
        "title": "Book3",
        "author": "Author3",
        "checked_out": False
    }
]

checkout_title = "Book4"
found_book = False
for book in books:
    if book["title"] == checkout_title:
        found_book = True
        if book["checked_out"]:
            print(f"{book['title']} is not available.")
        else:
            book["checked_out"] = True
            print(f"{book["title"]} is now checked out.")
            
if not found_book:
    print(f"{checkout_title} was not found.")

print("Library Status:")
for book in books:
    if book["checked_out"]:
        print(f"{book['title']} is checked out")
    else: 
        print(f"{book['title']} is available.")
    

