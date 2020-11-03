document.addEventListener('DOMContentLoaded', () =>{
    var socket = io();
    socket.on('connect', function() {
        socket.send('I\'m connected!');
    });

    socket.on('message', data =>{
        const p = document.createElement('p');
        const br = document.createElement('br');
        p.innerHTML = data;
        document.querySelector('#display-messages').append(p);
    });

    socket.on('some-event', data =>{
        console.log(data);
    });

    document.querySelector('#send-message').onclick =() => {
        socket.send(document.querySelector('#user-message').value);
    }
})