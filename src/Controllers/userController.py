from src.Models.userModel import postUser,getUser,getUserAll,getUserPasswordSecurity,putUser

def getUserController(code,password):
    response = getUser(code,password)
    if not (isinstance(response, list) and 'message' in response[0]):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta

def getUserPasswordSecurityController(code,securityResponse):
    response = getUserPasswordSecurity(code,securityResponse)
    if not (isinstance(response, list) and 'message' in response[0]):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta

def getUserAllController():
    response = getUserAll()
    if not (isinstance(response, list) and 'message' in response[0]):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta
    
def postUserController(code,password,idProfile):
    response = postUser(code,password,idProfile)
    if not (isinstance(response, list) and 'message' in response[0]):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta


def putUserController(idUser,idRole):
    response = putUser(idUser,idRole)
    if not (isinstance(response, list) and 'message' in response[0]):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta