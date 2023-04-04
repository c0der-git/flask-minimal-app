from flask import blueprints
view = blueprints.Blueprint("view", __name__)

@view.route("/")
def index():
    return "<p>Hello, World!</p>"

@view.route("/status")
def status():
    return "<p>STATUS page</p>"
