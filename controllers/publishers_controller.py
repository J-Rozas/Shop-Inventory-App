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


@publishers_blueprint.route("/publishers/<id>/delete", methods=["POST"])
def delete(id):
    publisher_repository.delete(id)
    return redirect("/publishers")


@publishers_blueprint.route("/publishers/<id>/edit")
def edit(id):
    publisher = publisher_repository.select(id)
    return render_template("publishers/edit.html.jinja", publisher = publisher)


@publishers_blueprint.route("/publishers/<id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    country = request.form["country"]
    address = request.form["address"]

    publisher = Publisher(name, country, address, id)

    publisher_repository.update(publisher)

    return redirect("/publishers")