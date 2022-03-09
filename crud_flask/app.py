from flask import Flask, render_template
from crud_flask.ext.site.main import bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app
