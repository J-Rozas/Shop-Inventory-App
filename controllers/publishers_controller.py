from flask import Blueprint, render_template
from repositories import publisher_repository

publishers_blueprint = Blueprint("publishers", __name__)

@publishers_blueprint.route("/publishers")
def publishers():
    publishers = publisher_repository.select_all()
    return render_template("publishers/index.html.jinja", publishers = publishers)