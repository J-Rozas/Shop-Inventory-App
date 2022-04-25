from flask import Blueprint

publishers_blueprint = Blueprint("publishers", __name__)

@publishers_blueprint.route("/publishers")
def publishers():
    return "The main publishers route works!"