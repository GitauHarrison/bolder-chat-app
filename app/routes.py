from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import LoginForm
from app.models import User
from flask_login import login_user, current_user, logout_user

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember = form.remember_me.data)
        flash('You have successfully logged in!')
        return redirect(url_for('home'))
    return render_template('login.html', title = 'Login', form = form)
