document.addEventListener('DOMContentLoaded', () =>{
    var socket = io();

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

    socket.on('some-event', data =>{
        console.log(data);
    });

    // Send message    
    document.querySelector('#send-message').onclick =() => {
        socket.send({'msg': document.querySelector('#user-message').value, 'username': username});
    }
})