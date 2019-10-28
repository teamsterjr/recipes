import os
from settings import APP_STATIC
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    with open(os.path.join(APP_STATIC, 'recipe.json')) as f:
        response = app.response_class(
            response=f.read(),
            status=200,
            mimetype='application/json'
        )
        return response