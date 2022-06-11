from db.run_sql import run_sql
from models.book import Book
from repositories import publisher_repository

def select_all():
    list_of_books = []

    sql = "SELECT * FROM books ORDER BY title"
    results = run_sql(sql)

    for book in results:
        title = book["title"]
        number_of_pages = book["number_of_pages"]
        genre = book["genre"]
        author = book["author"]
        stock = book["stock"]
        selling_price = book["selling_price"]
        id = book["id"]

        publisher = publisher_repository.select(book["publisher_id"])

        new_book = Book(title, number_of_pages, genre, author, stock, publisher, selling_price, id)

        list_of_books.append(new_book)

    return list_of_books


def add(new_book):
    sql = "INSERT INTO books (title, number_of_pages, genre, author, stock, selling_price, publisher_id) VALUES (%s, %s, %s, %s, %s, %s, %s) returning id"

    values = [new_book.title, new_book.number_of_pages, new_book.genre, new_book.author, new_book.stock, new_book.selling_price, new_book.publisher.id]

    result = run_sql(sql, values)

    id = result[0]["id"]

    new_book.id = id


def delete_all():
    sql = "DELETE FROM books *"
    run_sql(sql)


def select(id):
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    book = Book(result["title"], result["number_of_pages"], result["genre"], result["author"], result["stock"], result["publisher_id"], result["selling_price"], id)

    return book


def update(book):
    sql = "UPDATE books SET stock = %s WHERE id = %s"
    values = [book.stock, book.id]

    run_sql(sql, values)