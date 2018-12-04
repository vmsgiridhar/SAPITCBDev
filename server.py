# from flask import Flask, request, jsonify   
# from flask_socketio import send, emit, SocketIO   
# import json
# import requests
# import os
# app = Flask(__name__)
# #port = '5000'
# port = int(os.environ["PORT"])

# @app.route('/', methods=['POST'])
# def index():
#   data = json.loads(request.get_data())
#   test_message_channel = data['event']['text']
#   print(test_message_channel)
#   return jsonify(
#         status=200,
#         replies=[{
#          'text': test_message_channel
#         }]
#       )
    
# @app.route('/errors', methods=['POST'])
# def errors():
#   print(json.loads(request.get_data()))
#   return jsonify(status=200)

# #app.run(port=port)
# app.run(port=port, host="0.0.0.0") 

# Basic Flask Python Web App
from flask import Flask
from flask_socketio import SocketIO, send
import os #added
port = int(os.environ["PORT"]) #added
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='5a1b8a0f3c'
    APPLICATION_ROOT = 'sapitcbdev.herokuapp.com'
 )
#app.config['SERVER_NAME'] = '0.0.0.0:' + str(port)
socketio = SocketIO(app)

@socketio.on('message')
def messageHandler(msg):
   print('Message: '+ msg)
   send(msg, broadcast=True)

if __name__ == "__main__":
    socketio.run(app) 
