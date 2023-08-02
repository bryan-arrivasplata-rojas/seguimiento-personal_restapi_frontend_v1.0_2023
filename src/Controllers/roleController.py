from src.Models.roleModel import getRoleAll

def getRoleAllController():
    response = getRoleAll()
    if not (isinstance(response, list) and 'message' in response[0]):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta
