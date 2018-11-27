# from flask import Flask, request, jsonify 
# from flask_socketio import send, emit    
# import json
# import requests
# import os
# app = Flask(__name__)
# #socketio = SocketIO(app)
# #port = '5000'
# port = int(os.environ["PORT"])

# @app.route('/', methods=['POST'])
# def index():
#   data = json.loads(request.get_data())
  
#   #Code for testing the Slack API
#   #challenge_var = data['challenge']
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


#Trying the brute force
from flask import Flask, request, jsonify 
from flask_socketio import send, emit
app = Flask(__name__)
port = int(os.environ["PORT"])
socketio = SocketIO(app)
def some_function():
    socketio.emit('some event', {'data': 42})
some_function()
app.run(port=port, host="0.0.0.0") 
