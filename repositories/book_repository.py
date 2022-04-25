from db.run_sql import run_sql
from models.book import Book
from repositories import publisher_repository

def select_all():
    list_of_books = []

    sql = "SELECT * FROM books"
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