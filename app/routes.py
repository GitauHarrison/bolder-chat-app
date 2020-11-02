from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You have successfully logged in!')
        return redirect(url_for('home'))
    return render_template('login.html', title = 'Login', form = form)

@app.route('/register')
def register():
    return render_template ('register.html', title = 'Register')