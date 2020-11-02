from app import app
from flask import render_template, url_for

@app.route('/')
def index():
    return render_template('home.html', title = 'Home')

@app.route('login')
def login():
    return render_template('login.html', title = 'Login')

@app.route('/register')
def register():
    return render_template ('register.html', title = 'Register')