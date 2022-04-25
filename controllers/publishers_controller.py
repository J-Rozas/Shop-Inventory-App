from flask import Blueprint, render_template

publishers_blueprint = Blueprint("publishers", __name__)

@publishers_blueprint.route("/publishers")
def publishers():
    return render_template("publishers/index.html.jinja")