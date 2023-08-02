from src.Models.profileModel import getProfileEmail,getProfileUser,postProfile

def postProfileController(name,lastName,number,birthday,email,securityResponse):
    response = postProfile(name,lastName,number,birthday,email,securityResponse)
    if not (isinstance(response, list) and 'message' in response[0]):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta

def getProfileEmailController(email):
    response = getProfileEmail(email)
    if not (isinstance(response, list) and 'message' in response[0]):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta
    
def getProfileUserController(idUser):
    response = getProfileUser(idUser)
    if not (isinstance(response, list) and 'message' in response[0]):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta