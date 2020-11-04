document.addEventListener('DOMContentLoaded', () =>{
    // Connect to websocket
    var socket = io();

    // The default room
    let room = 'General';
    joinRoom('General');

    // Display incoming messages
    socket.on('message', data =>{
        if(data.msg){
            const p = document.createElement('p');
            const span_username = document.createElement('span');
            const span_timestamp = document.createElement('span');
            const br = document.createElement('br');
            // Display user's own message
            if (data.username == username){
                p.setAttribute('class', 'my-msg');

                // Username
                span_username.setAttribute('class', 'my-username');
                span_username.innerText = data.username;

                // Timestamp
                span_timestamp.setAttribute('class', 'timestamp');
                span_timestamp.innerText = data.timestamp;

                // HTML to append
                p.innerHTML = span_username.outerHTML + br.outerHTML +  data.msg + br.outerHTML + span_timestamp.outerHTML;
                //Append
                document.querySelector('#display-messages').append(p);
            }
            // Display other user's messages
            else if(typeof data.username !== 'undefined'){
                p.setAttribute('class', 'others-msg');

                // Username
                span_username.setAttribute('class', 'other-username');
                span_username.innerText = data.username;

                // Timestamp
                span_timestamp.setAttribute('class', 'timestamp');
                span_timestamp.innerText = data.timestamp;

                // HTML to append
                p.innerHTML += span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML + span_timestamp.outerHTML;
                // Append
                document.querySelector('#display-messages').append(p);
            }
            // Display system message
            else{
                printSysMsg(data.msg);
            }
        }
        scrollDownChatWindow();
    });

    // Used for demonstration purposes
    // socket.on('some-event', data =>{
    //     console.log(data);
    // });

    // Send message    
    document.querySelector('#send-message').onclick =() => {
        socket.send({'msg': document.querySelector('#user-message').value, 'username': username, 'room': room});
        // Clear input area
        document.querySelector('#user-message').value = '';
    }

    // Room Selection
    document.querySelectorAll('.select-room').forEach(p =>{
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

    // Leave room
    function leaveRoom(room){
        socket.emit('leave', {'username': username, 'room': room});
    }

    // Join room
    function joinRoom(room){
        socket.emit('join', { 'username': username, 'room': room });
        // Clear message area
        document.querySelector('#display-messages').innerHTML = '';
        // Autofocus on the textbox
        document.querySelector('#user-message').focus();
    }

    // Scroll chat window down
    function scrollDownChatWindow() {
        const chatWindow = document.querySelector("#display-messages");
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // Print system message
    function printSysMsg(msg){
        const p = document.createElement('p');
        p.innerHTML = msg;
        document.querySelector('#display-messages').append(p);
    }
})