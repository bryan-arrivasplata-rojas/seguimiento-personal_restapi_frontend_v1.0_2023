from src.Models.recognitionModel import getRecognitionAll,getRecognitionUser

def getRecognitionAllController():
    response = getRecognitionAll()
    if not (isinstance(response, list) and 'message' in response[0]):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta

def getRecognitionUserController(code):
    response = getRecognitionUser(code)
    if not (isinstance(response, list) and 'message' in response[0]):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta