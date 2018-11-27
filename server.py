from flask import Flask, request, jsonify  
from flask_socketio import send, emit    
import json 
import requests
import os
app = Flask(__name__)
#port = '5000'
port = int(os.environ["PORT"])

@app.route('/', methods=['POST'])
def index():
  data = json.loads(request.get_data())
  
  #Code for testing the Slack API
  #challenge_var = data['challenge']
  test_message_channel = data['event']['text']
  print(test_message_channel)
  return jsonify(
        status=200,
        replies=[{
         'text': test_message_channel
        }]
      )

json = [{'Test':'Hi Test'}]
@socketio.on('json')
def handle_json(json):
  send(json, json=True)

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

#app.run(port=port)
app.run(port=port, host="0.0.0.0") 
