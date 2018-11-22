# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:47:24 2018

@author: C5232886
"""

from flask import Flask, request, jsonify 
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
  challenge_var = data['challenge']
  
  return jsonify(
        status=200,
        replies=[{
         'challenge': challenge_var
        }]
      )
  test_message_channel = data['event']['channel']
  print(test_message_channel)

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

#app.run(port=port)
app.run(port=port, host="0.0.0.0") 
