from flask import Flask

from src.backend.app.routes import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app


app = create_app()
