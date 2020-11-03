from app import socketio
from flask_socketio import emit, send, join_room, leave_room

@socketio.on('message')
def message(data):
    print(f"\n\n{data}\n\n")
    send(data)
