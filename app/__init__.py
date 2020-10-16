from flask import Flask
from config import Config
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
socketio = SocketIO(app)

from app import routes