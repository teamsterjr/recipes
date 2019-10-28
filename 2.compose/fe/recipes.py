from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort
import requests
import json

bp = Blueprint('recipes', __name__)
@bp.route('/')
def index():
    return render_template('recipe/index.html')

@bp.route('/breakfast')
def breakfast():
    r = requests.get(current_app.config["BREAKFAST_URL"])
    current_app.logger.info(r.text)
    return render_template('recipe/show.html', recipe=json.loads(r.text))

@bp.route('/lunch')
def lunch():
    r = requests.get(current_app.config["LUNCH_URL"])
    current_app.logger.info(r.text)
    return render_template('recipe/show.html', recipe=json.loads(r.text))

@bp.route('/dinner')
def dinner():
    r = requests.get(current_app.config["DINNER_URL"])
    current_app.logger.info(r.text)
    return render_template('recipe/show.html', recipe=json.loads(r.text))


