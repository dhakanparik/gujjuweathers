#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['GET'])
def webhook():

    if req.get("result").get("action") != "GyahooWeatherForecast":
        return {"parik"}
    r = make_response("parik dhakan")
    r.headers['Content-Type'] = 'application/json'
    # req = request.get_json(silent=True, force=True)

    # print("Request:")
    # print(json.dumps(req, indent=4))

    # res = processRequest(req)

    # res = json.dumps(res, indent=4)
    # # print(res)
    
    return r

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='101.101.101.101')
