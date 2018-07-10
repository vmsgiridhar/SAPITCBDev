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

  # FETCH THE CRYPTO NAME
  #crypto_name = data['conversation']['memory']['crypto']['raw']
  #crypto_name = data['conversation']['memory']['empid']['raw']
  #crypto_name = data['entities']['number']['raw']
  crypto_name = 'Testing'

  # FETCH BTC/USD/EUR PRICES
  #r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_name+"&tsyms=BTC,USD,EUR")
  #r = requests.get("https://giridev1c5232886trial.hanatrial.ondemand.com/ChatBot_DEV/Read.xsjs?EMPID="+crypto_name)
  r = requests.get("https://api.myjson.com/bins/l5rbi")

  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
	  'content': 'The Salary of %s is %f ' % (crypto_name, r.json()["SAL"])
    }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

#app.run(port=port)
app.run(port=port, host="0.0.0.0")
#https://giridev1c5232886trial.hanatrial.ondemand.com/ChatBot_DEV/Read.xsjs?EMPID=1002193
#crypto_name = data['conversation']['memory']['empid']['raw']
#'content': 'The price of %s is %f BTC and %f USD' % (crypto_name, r.json()['BTC'], r.json()['USD'])
#myjson.com
#'The Salary of %s is %f ' % (crypto_name, r.json()['SAL'])
