from flask import Flask, request, jsonify 
from flask_socketio import send, emit, SocketIO   
import json
import requests
import os
app = Flask(__name__)
socketio = SocketIO(app)
#port = '5000'
port = int(os.environ["PORT"])

#editing now
@socketio.on('json')
def handle_json(json):
    send(json, json=True)

@app.route('/', methods=['POST'])
def index():
  data = json.loads(request.get_data())
  
  #Code for testing the Slack API
  #challenge_var = data['challenge']
  test_message_channel = data['event']['text']
  #editing now
  test = [{'A':'a'}]
  handle_json(test)
  print(test)
  
  print(test_message_channel)
  return jsonify(
        status=200,
        replies=[{
         'text': test_message_channel
        }]
      )
    
@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

#app.run(port=port)
app.run(port=port, host="0.0.0.0") 


#Trying the brute force
# from flask import Flask, render_template
# from flask_socketio import SocketIO
# import requests
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)
# @app.route('/',methods=['POST'])
# def getData():
#   data = json.loads(request.get_data())
#   data = data['event']['text']
#   print(data)
# @socketio.on('json')
# def handle_json(json):
#     print('received json: ' + str(json))

# if __name__ == '__main__':
#     socketio.run(app)
