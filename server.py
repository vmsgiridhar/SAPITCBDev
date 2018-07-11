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
  crypto_name_test = data['nlp']['entities']['number'][0]['scalar']
  #crypto_name = "1002191"

  # FETCH BTC/USD/EUR PRICES
  #r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_name+"&tsyms=BTC,USD,EUR")
  r = requests.get("https://giridev1c5232886trial.hanatrial.ondemand.com/ChatBot_DEV/Read.xsjs?EMPID="+crypto_name_test)
  #r = requests.get("https://api.myjson.com/bins/13jh5m")

  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
	  'content': 'The Salary of %s is %f and %s' % (crypto_name, r.json()[0]['SAL'], crypto_name_test)
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
# Make your xsjs public: https://archive.sap.com/discussions/thread/3656891
'''
UPDATE "_SYS_XS"."SQL_CONNECTIONS" SET username = 'SYSTEM' WHERE name = 'ChatBot_DEV::Anonymous';
SELECT * FROM "_SYS_XS"."SQL_CONNECTIONS"
UPDATE "CHATBOTDEV"."EMPLOYEE_DATA" SET SAL = '50000' WHERE EMPID = '1002191';
'''
