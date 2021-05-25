from flask import Flask,jsonify,send_file,request,abort
import os
import sys
from flask_restful import Api
from resources.routes import initialize_routes

app=Flask(__name__,static_url_path='/static')
#CORS(app, support_credentials=True)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

api = Api(app)
initialize_routes(api)

  
app.run(threaded=True)
