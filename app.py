import json
from flask import Flask, Response ,jsonify, request
from Prospect import Prospect

app = Flask(__name__)


@app.route('/healthcheck')
def HealthCheck():
    return "WebServer is up and running!"

@app.route('/Predict', methods=['GET','POST'])
def prospectPredict():
    prospectObj = Prospect(0,'H','H','W','Dallas','Texas','654321','UA','10','N','01/01/2002','M', 0,0,0,0,0,'','',0,'','UA',1,'internet','2Bed',2)
    
    request_data = request.get_json()
    language = request_data['language']
    Details = {'id':2,'year':2019,'model':''}
    return prospectObj.__dict__

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')