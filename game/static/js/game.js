// static/js/game.js
var connectionString = 'ws://' + window.location.host + '/ws';
var gameSocket = new WebSocket(connectionString);

function connect() {
    gameSocket.onopen = function open() {
        console.log('WebSockets connection created.');
        // on websocket open, send the START event.
        gameSocket.send(JSON.stringify({
            "event": "START",
            "message": "connect"
        }));
    };

    gameSocket.onclose = function (e) {
        console.log('Socket is closed. Reconnect will be attempted in 1 second.', e.reason);
        setTimeout(function () {
            connect();
        }, 1000);
    };
    gameSocket.onmessage = function (e) {
        // let data1 = JSON.parse(e.data);
        data = 'data:image/jpeg;base64,'+e.data+''
        document.getElementById("myid").src = data;
        console.log(e.data)
    };

    if (gameSocket.readyState == WebSocket.OPEN) {
        gameSocket.onopen();
    }
}

connect();