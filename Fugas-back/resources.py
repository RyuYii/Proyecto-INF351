import traceback
import json
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt, get_jti)
from flask import session, jsonify, current_app as app
from http import HTTPStatus
from configuration import Configuration
from responses import clientResponses as messages, messageToken, addNextRoute
from routes import Routes
from prolog import *
from multiprocessing import Lock
prologlock = Lock()

class Questions(Resource):
    def get(self):
        return questions()


parser = reqparse.RequestParser()
parser.add_argument('tipo', type=int, help = 'This field cannot be blank', required = True)
class ObtenerOpciones(Resource):
    def post(self):
        data = parser.parse_args()
        tipo = data['tipo']
        if tipo == 1 or tipo == 2:
            return {'texto': 'antiguedad instalacion', 'tipo': 1, 'siguiente': 1}

class NextStep(Resource):
    def post(self):
        data = parser.parse_args()
        tipo = data['tipo']
        print(tipo)
        if tipo == 1 or tipo == 2:
            return {'texto': 'material de la tuberia', 'tipo': 3, 'siguiente': 0}

parserR = reqparse.RequestParser()
parserR.add_argument('tipo', type=int, help = 'This field cannot be blank', required = True)
parserR.add_argument('answer', type=str, help = 'This field cannot be blank', required = True)
class Result(Resource):
    def post(self):
        data = parserR.parse_args()
        answer = data['answer']
        tipo = data['tipo']
        print(data)
        if tipo == 1:
            return {}
        if tipo == 2:
            return dos(answer)