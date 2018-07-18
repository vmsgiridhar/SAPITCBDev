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
  crypto_name_test = data['nlp']['entities']['number'][0]['raw']
  postdata = data['nlp']['entities']['number'][0]
  print(postdata)
  #crypto_name = "1002191"

  # FETCH BTC/USD/EUR PRICES
  #r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_name+"&tsyms=BTC,USD,EUR")
  r = requests.get("https://giridev1c5232886trial.hanatrial.ondemand.com/ChatBot_DEV/Read.xsjs?EMPID="+crypto_name_test)
  print(r.url)
  rp = requests.get("https://giridev1c5232886trial.hanatrial.ondemand.com/ChatBot_DEV/ReadGeneric.xsjs",params = postdata)
  print(rp.url)
  #r = requests.get("https://api.myjson.com/bins/13jh5m")
  if len(rp.json() != 0):
    derivedsalary = str(rp.json()[0]['SAL'])
  else:
    derivedsalary = "I don't see this employee in my records."
  return jsonify(
        status=200,
        replies=[{
          'type': 'text',
          'content': 'The Salary of %s is %s.' % (crypto_name_test, derivedsalary)
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

----
Python and oData accessing usingg
from pyslet.odata2.client import Client
class index:
    def GET(self):
    c=Client("http://services.odata.org/V2/Northwind/Northwind.svc/")
    products=c.feeds['Products'].OpenCollection()
    productNames = []
    for k,p in products.iteritems():
    productNames.append(p['ProductName'].value)
        web.header('Content-Type', 'text/html')
        return render_template('index.html', products = productNames)

'''
