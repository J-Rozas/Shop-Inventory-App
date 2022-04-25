from flask import Blueprint, redirect, render_template, request
from repositories import publisher_repository
from models.publisher import Publisher

publishers_blueprint = Blueprint("publishers", __name__)

@publishers_blueprint.route("/publishers")
def publishers():
    publishers = publisher_repository.select_all()
    return render_template("publishers/index.html.jinja", publishers = publishers)


@publishers_blueprint.route("/publishers/new")
def new():
    return render_template("publishers/new.html.jinja")

@publishers_blueprint.route("/publishers", methods=["POST"])
def create():
    name = request.form["name"]
    country = request.form["country"]
    address = request.form["address"]

    publisher_repository.add(Publisher(name, country, address))

    return redirect("/publishers")