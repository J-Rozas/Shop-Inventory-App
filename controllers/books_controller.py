from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    return "The main books route is on!"