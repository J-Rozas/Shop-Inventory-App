from flask import Flask, render_template

from controllers.publishers_controller import publishers_blueprint
from controllers.books_controller import books_blueprint

app = Flask(__name__)

app.register_blueprint(publishers_blueprint)
app.register_blueprint(books_blueprint)

@app.route("/")
def main():
    return "hi"

if __name__ == "__main__":
    app.run()