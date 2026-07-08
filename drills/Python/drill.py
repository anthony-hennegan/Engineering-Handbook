books = ['Dune', 'Harry Potter', 'A walk to Remember', 'The Alchemist', 'The Hobbit']
print(books[0])
print(books[-1])
books.append('New book')
print(len(books))
books.remove('New book')
print(books)
first_book_response = input("Would you like to see the first book? ")
first_book_response = first_book_response.strip().lower()

if first_book_response == "yes" or first_book_response == "y":
    print(books[0])
elif first_book_response == "no" or first_book_response =="n":
    print("Goodbye")