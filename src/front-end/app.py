
import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # a simple page that says hello
    app.config["BREAKFAST_URL"] = os.environ.get('BREAKFAST_URL')
    app.config["LUNCH_URL"] = os.environ.get('LUNCH_URL')
    app.config["DINNER_URL"] = os.environ.get('DINNER_URL')

    from . import recipes
    app.register_blueprint(recipes.bp)

    return app
