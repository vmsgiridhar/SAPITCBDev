from flask_socketio import send, emit

@socketio.on('message')
def handle_message(message):
    send(message)
handle_message("Hi")
