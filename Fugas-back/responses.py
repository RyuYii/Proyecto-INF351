import copy
class clientResponses:
  index =  {"code":1 , "message": "Bienvenido al Portal de Usuarios"}



def messageToken(token, expires, nextRoute):
  msj = copy.deepcopy(clientResponses.accessToken)
  msj["token"]= token
  msj["expires"]= expires
  msj = addNextRoute(msj, nextRoute)
  return msj

def addNextRoute (msj, nextRoute):
  message = copy.deepcopy(msj)
  message["next"] = nextRoute
  return message

def addObject(msj, key,val):
  message=  copy.deepcopy(msj)
  message[key] =val 
  return message