from flask import (
    Blueprint, render_template, request, current_app
)
import requests
import json

bp = Blueprint('recipes', __name__)
@bp.route('/')
def index():
    user = request.headers.get("x-test-user")
    return render_template('recipe/index.html', user=user)

@bp.route('/breakfast')
def breakfast():
    recipe = fetch_recipe(current_app.config["BREAKFAST_URL"])
    return render_template('recipe/show.html', recipe=recipe)

@bp.route('/lunch')
def lunch():
    recipe = fetch_recipe(current_app.config["LUNCH_URL"])
    return render_template('recipe/show.html', recipe=recipe)

@bp.route('/dinner')
def dinner():
    recipe = fetch_recipe(current_app.config["DINNER_URL"])
    return render_template('recipe/show.html', recipe=recipe)


def fetch_recipe(recipe_url):
    user = request.headers.get("x-test-user")
    headers = {}
    if user is not None:
        current_app.logger.info("setting user to %s", user)
        headers = {'x-test-user': user}
    r = requests.get(recipe_url, headers=headers)
    return json.loads(r.text)