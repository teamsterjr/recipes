from flask import (
    Blueprint, current_app
)
bp = Blueprint('recipes', __name__)

@bp.route('/')
def health():
    return "OK"

@bp.route('/recipe.json')
def send_recipe():
    return current_app.send_static_file('recipe.json')