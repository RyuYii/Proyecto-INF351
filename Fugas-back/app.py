from flask import Flask, session
from flask_restful import Api
from flask_session import Session
from flask_jwt_extended import JWTManager, create_access_token, exceptions, jwt_required, get_jwt_identity
from configuration import Configuration
from routes import Routes
from flask import jsonify
from flask_cors import CORS

from logging.handlers import RotatingFileHandler
import logging
import resources as resources
import traceback


# logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
LOG_FILENAME = 'aplication.log'
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(LOG_FILENAME, maxBytes=40000000, backupCount=40)
logger.addHandler(handler)

app = Flask(__name__)

CORS(app) # This will enable CORS for all routes
errors = {
  'InternalError': {
      'message': "Internal Error. Wait few Minutes or Contact the Administrator",
      'status': 500,
  },
  'NotFound': {
      'message': "Resource Not Found",
      'status': 404
  },
}
api = Api(app,errors=errors)

api.add_resource(resources.ObtenerOpciones, Routes.obtenerOpciones)
api.add_resource(resources.NextStep, Routes.nextStep)
api.add_resource(resources.Questions, Routes.questions)
api.add_resource(resources.Result, Routes.result)


# if __name__ == '__main__':
# 	# import os
app.run(host='127.0.0.1',port=9999,debug=True)