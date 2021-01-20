from flask import Blueprint, request, render_template, redirect, url_for


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('main.index'))
    return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for('main.index'))
    return render_template('signup.html')


@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))
