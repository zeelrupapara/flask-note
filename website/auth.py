from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = {
            "username": request.form['username'],
            "email": request.form['email'],
            "password": request.form['password'],
            "conform_password": request.form['conform_password']
        }
        print(user)
        if len(user["username"]) < 4:
            flash('Username is longer than 4 cherater', category="error")
        elif len(user["email"]) < 4:
            flash('Email is longer than 4 cherater', category="error")
        elif len(user['password']) < 7:
            flash('Password is longer than 7 cherater', category="error")
        elif user['password'] != user['conform_password']:
            flash('Password not matched with confirm password', category="error")
        else:
            flash('Account Created', category="success")
    return render_template('signup.html')
