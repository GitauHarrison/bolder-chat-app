from app import app, socketio, send
from flask import render_template, url_for

@app.route('/')
def index():
    return render_template('home.html', title = 'Home')

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)