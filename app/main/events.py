from app import socketio
from flask_socketio import emit, send, join_room, leave_room
from flask_login import current_user
from time import localtime, strftime


@socketio.on('message')
def message(data):
    print(f"\n\n{data}\n\n")
    send({'msg': data['msg'], 'username': data['username'], 'timestamp': strftime('%d %b, %Y %I:%M %p', localtime()) })
    
    
