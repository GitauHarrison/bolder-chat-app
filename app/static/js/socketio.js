document.addEventListener('DOMContentLoaded', () =>{
    var socket = io();

    let room;

    // Display incoming messages
    socket.on('message', data =>{
        const p = document.createElement('p');
        const span_username = document.createElement('span');
        const span_timestamp = document.createElement('span');
        const br = document.createElement('br');
        span_username.innerHTML = data.username;
        span_timestamp.innerHTML = data.timestamp;
        p.innerHTML = span_username.outerHTML + br.outerHTML +  data.msg + br.outerHTML + span_timestamp.outerHTML;
        document.querySelector('#display-messages').append(p);
    });

    // Used for demonstration purposes
    // socket.on('some-event', data =>{
    //     console.log(data);
    // });

    // Send message    
    document.querySelector('#send-message').onclick =() => {
        socket.send({'msg': document.querySelector('#user-message').value, 'username': username});
    }

    // Room Selection
    document.querySelectorAll('select-rooms').forEach(p =>{
        p.onclick = () => {
            let newRoom = p.innerHTML;
            if (newRoom == room){
                msg = `You are already in ${room} room.`
                printSysMsg(msg);
            } else{
                leaveRoom(room);
                joinRoom(newRoom);
                room = newRoom;
            }
        }
    });



})