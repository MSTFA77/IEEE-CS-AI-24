Books = {
    1: {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication_year": 1960
    },
    2: {
        "title": "1984",
        "author": "George Orwell",
        "publication_year": 1949
    },
    3: {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publication_year": 1813
    },
    4: {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_year": 1925
    },
    5: {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "publication_year": 1951
    },
}
#some of tests in the Dectionary
print(Books)


print(Books[1].get("title"))


for book_id in range(1, 6): 
    book = Books.get(book_id)
    if book: 
        print("Title:", book.get("title"))
        print("Author:", book.get("author"))
        print("Publication Year:", book.get("publication_year"))
        print()