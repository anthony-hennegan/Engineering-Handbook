books = ['book1', 'book2', 'book3', 'book4']
print("Bailey's Book Selection")

for book in books:
    print(book)
print("Done")
print("----------------------------")
print("")

books.append("Dune")
for book in books:
    print(book)
print("----------------------------")
print("")

book_count = 0
for book in books:
    book_count += 1
print(book_count)
print("----------------------------")
print("")

for book in books:
    if book == "Dune":
        print("Found Dune.")
        
# A loop variable is a name that represents the current item the list being iterated through.
# The code block in the loop will run only using the current item, and then move on to the next item.

# If a condition is created inside a loop and has a false result the code block will be skipped.