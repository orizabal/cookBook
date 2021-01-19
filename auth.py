from flask import Blueprint, request, render_template, redirect, url_for


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('index.html')
    return render_template('index.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return render_template('index.html')
    return render_template('index.html')


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        return redirect(url_for('main.index'))
    return render_template('index.html')
