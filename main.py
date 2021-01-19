from flask import Blueprint, render_template


main = Blueprint('main', __name__)


# Landing page after sign in
# View meals s/a breakfast, lunch, dinner, etc
@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# View recipes from a meal
@main.route('/recipes', methods=['GET'])
def meals():
    return render_template('index.html')
