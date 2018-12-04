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

# Working code
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send
import os #added
import json
import requests
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='5a1b8a0f3c'
 )

#Temp variable to catch return from Slack
Slack_ret = ''

# To listen code from Slack
@app.route('/', methods=['POST'])
def index():
  data = json.loads(request.get_data())
  test_message_channel = data['event']['text']
  Slack_ret = test_message_channel #added just now
  @socketio.on('message')
  def messageHandler(Slack_ret):
    print('Message: '+ Slack_ret)
    send(Slack_ret, broadcast=True)
  print(test_message_channel)
  return jsonify(
        status=200,
        replies=[{
         'text': test_message_channel
        }]
      )

socketio = SocketIO(app)
@socketio.on('message')
def messageHandler(msg):
   print('Message: '+ msg)
   send(msg, broadcast=True)

if __name__ == "__main__":
    port_1 = int(os.environ["PORT"]) #added
    socketio.run(app, host='0.0.0.0', port=port_1) 
