from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = {
            "username": request.form['username'],
            "email": request.form['email'],
            "password": request.form['password'],
            "conform_password": request.form['conform_password']
        }
        user_exist = User.query.filter_by(email=user['email']).first()
        if len(user["username"]) < 4:
            flash('Username is longer than 4 cherater', category="error")
        elif len(user["email"]) < 4:
            flash('Email is longer than 4 cherater', category="error")
        elif len(user['password']) < 7:
            flash('Password is longer than 7 cherater', category="error")
        elif user['password'] != user['conform_password']:
            flash('Password not matched with confirm password', category="error")
        elif user_exist:
            flash('Email already exist', category="error")
        else:
            new_user = User(email=user['email'], username=user['username'], password = generate_password_hash(user['password'], method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account Created', category="success")
            return redirect(url_for('views.home'))
    return render_template('signup.html', user=current_user)
