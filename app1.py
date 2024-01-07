class BookDatabase:
    def __init__(self):
        self.books = []

    def create_book(self, title, author, publication_year):
        book = {
            "title": title,
            "author": author,
            "publication_year": publication_year
        }
        self.books.append(book)
        return book

    def read_books(self):
        return self.books

    def read_book(self, title):
        for book in self.books:
            if book["title"] == title:
                return book
        return None

    def update_book(self, title, new_author=None, new_publication_year=None):
        for book in self.books:
            if book["title"] == title:
                if new_author:
                    book["author"] = new_author
                if new_publication_year:
                    book["publication_year"] = new_publication_year
                return book
        return None

    def delete_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                return True
        return False


# Example usage
book_db = BookDatabase()

# Create
book_db.create_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book_db.create_book("To Kill a Mockingbird", "Harper Lee", 1960)

# Read
all_books = book_db.read_books()
print("All Books:", all_books)

specific_book = book_db.read_book("The Great Gatsby")
print("Specific Book:", specific_book)

# Update
updated_book = book_db.update_book(
    "The Great Gatsby", new_author="Fitzgerald, F. Scott")
print("Updated Book:", updated_book)

# Delete
deleted = book_db.delete_book("To Kill a Mockingbird")
print("Book Deleted:", deleted)

all_books_after_deletion = book_db.read_books()
print("All Books After Deletion:", all_books_after_deletion)
