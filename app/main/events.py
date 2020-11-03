from app import socketio
from flask_socketio import emit, send, join_room, leave_room
from flask_login import current_user
from time import localtime, strftime


@socketio.on('message')
def message(data):
    print(f"\n\n{data}\n\n")
    send({'msg': data['msg'], 'username': data['username'], 'timestamp': strftime('%d %b, %Y %I:%M %p', localtime()) })
    
    
@socketio.on('join')
def join(data):
    join_room(data['room'])
    send({'msg': data['username'] + 'has joined the ' + data['room'] + 'room.'}, room = data['room'])

@socketio.on('leave')
def leave(data):
    leave_room(data['room'])
    send({ 'msg': data['username'] + 'has left the ' + data['room'] + 'room.' }, room = data['room'])