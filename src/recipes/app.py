import os
from flask import Flask, request

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import recipes
    app.register_blueprint(recipes.bp)

    return app