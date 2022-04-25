from flask import Blueprint, redirect, render_template, request
from repositories import book_repository, publisher_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html.jinja", books = books)


@books_blueprint.route("/books/new")
def new():
    publishers = publisher_repository.select_all()
    return render_template("books/new.html.jinja", publishers = publishers)


@books_blueprint.route("/books", methods=["POST"])
def create():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    number_of_pages = request.form["number_of_pages"]
    selling_price = request.form["selling_price"]
    stock = request.form["stock"]
    publisher_id = request.form["publisher"]
    publisher = publisher_repository.select(publisher_id)

    book_repository.add(Book(title, number_of_pages, genre, author, stock, publisher, selling_price))

    return redirect("/books")