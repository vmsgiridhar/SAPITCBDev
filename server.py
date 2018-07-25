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
  crypto_name_test = data['nlp']['entities']['number'][0]['raw'] #getting the numeric data
  skillgrab = data['conversation']['skill']
  postdata = data['nlp']['entities']['number'][0]
  print('Python Log: The number entered is:'+str(postdata))
  print('Python Log: The intent grabbed is:'+str(skillgrab))
  #crypto_name = "1002191"

  # FETCH BTC/USD/EUR PRICES
  #r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_name+"&tsyms=BTC,USD,EUR")
  #r = requests.get("https://giridev1c5232886trial.hanatrial.ondemand.com/ChatBot_DEV/Read.xsjs?EMPID="+crypto_name_test)
  if skillgrab == 'testsalary':
    r = requests.get("https://sitp2000481094trial.hanatrial.ondemand.com/sapit_test/read.xsjs?EMPID="+crypto_name_test)
    print(r.url)
    rp = requests.get("https://giridev1c5232886trial.hanatrial.ondemand.com/ChatBot_DEV/ReadGeneric.xsjs",params = postdata)
    print(rp.url)
  if skillgrab == 'testproduct':
    r = requests.get("https://sitp2000481094trial.hanatrial.ondemand.com/sapit_test/read_products.xsjs?PRDID="+crypto_name_test)
    print(r.url)
    rp = requests.get("https://giridev1c5232886trial.hanatrial.ondemand.com/ChatBot_DEV/ReadGeneric.xsjs",params = postdata)
    print(rp.url)
  #from TestData import datapartition_number
  #print(datapartition_number)
  #r = requests.get("https://api.myjson.com/bins/13jh5m")
  if len(r.json()) != 0 and skillgrab == 'testsalary':
    returnmessage = "The Salary of "+crypto_name_test+" who is "+str(r.json()[0]['EMPNAME'])+" is: "+str(r.json()[0]['SAL'])
  else:
    returnmessage = "I don't see the employee "+crypto_name_test+" in my records."
  if len(r.json()) != 0 and skillgrab == 'testproduct':
    returnmessage = "The cost of "+crypto_name_test+" which is a "+str(r.json()[0]['PRDNAME'])+" is: "+str(r.json()[0]['PRDCOST'])
  else:
    returnmessage = "I don't see the product "+crypto_name_test+" in my records."
  return jsonify(
        status=200,
        replies=[{
          'type': 'text',
          'content': returnmessage
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
Python and oData accessing using
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
New Service on my vmsgbtechgiet test account: https://sitp2000481094trial.hanatrial.ondemand.com/sapit_test/read.xsjs?EMPID=1002191
Made public too.
'''
