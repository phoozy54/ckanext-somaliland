from flask import Blueprint


somaliland = Blueprint(
    "somaliland", __name__)


def page():
    return "Hello, somaliland!"


somaliland.add_url_rule(
    "/somaliland/page", view_func=page)


def get_blueprints():
    return [somaliland]
