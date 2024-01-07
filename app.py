from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


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


book_db = BookDatabase()


@app.route('/')
def index():
    all_books = book_db.read_books()
    return render_template('index.html', all_books=all_books)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publication_year = request.form['publication_year']
        book_db.create_book(title, author, publication_year)
        return redirect(url_for('index'))
    return render_template('add_book.html')


@app.route('/view_book/<title>')
def view_book(title):
    specific_book = book_db.read_book(title)
    return render_template('view_book.html', specific_book=specific_book)


@app.route('/update_book/<title>', methods=['GET', 'POST'])
def update_book(title):
    if request.method == 'POST':
        new_author = request.form['new_author']
        new_publication_year = request.form['new_publication_year']
        updated_book = book_db.update_book(
            title, new_author, new_publication_year)
        if updated_book:
            return redirect(url_for('index'))
    return render_template('update_book.html', title=title)


@app.route('/delete_book/<title>')
def delete_book(title):
    deleted = book_db.delete_book(title)
    if deleted:
        return redirect(url_for('index'))
    return render_template('book_not_found.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)
