# *******************************************************************
# Bottle Example API
# Authors/Maintainers: Rich Nason (rnason@awsdocs.com)
# *******************************************************************

# Required Modules:
# =================

# Install Requirements via PIP
from bottle import Bottle, HTTPResponse  # WebServer

# Bottle Parameters:
# ===================

VERSION = '0.0.1'     # API Version
BOTTLEIP = '0.0.0.0'  # The IP that Bottle will listen on to serve the API
BOTTLEPORT = '80'   # The TCP port that bottle will use to serve the API


# Setup the Bottle WebServer Instance:
# ====================================

APP = Bottle(__name__)


# Index Route
@APP.route('/', method=['OPTIONS', 'GET'])
def index():
    try:
        resp_msg = "All systems reporting go for launch!!"
        body = {'version': VERSION, 'message': resp_msg}
        response = HTTPResponse(status=200, body=body)
        return response
    except Exception as err:
        print(err)
        body = {'version': VERSION, 'message': err}
        response = HTTPResponse(status=400, body=body)
        return response


# Start the Web Server
# =====================

if __name__ == '__main__':
    try:
        SERVER = APP.run(host=BOTTLEIP, port=BOTTLEPORT, debug=True)
    except KeyboardInterrupt:
        pass
        print('exiting...')
        SERVER.stop()
