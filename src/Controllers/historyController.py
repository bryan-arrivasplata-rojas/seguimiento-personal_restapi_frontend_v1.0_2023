from src.Models.historyModel import postHistory, getHistory, getHistoryUserNow

def postHistoryController(idUser,idRecognition):
    response = postHistory(idUser,idRecognition)
    if not (isinstance(response, list) and 'message' in response[0]):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta

def getHistoryController():
    response = getHistory()
    if not (isinstance(response, list)):
        return response
    else:
        respuesta = ""
        if(len(response)==0):
            respuesta = {'message':'Sin elementos'}
        else:
            respuesta = {'error':str(response)}
        return respuesta

def getHistoryUserNowController(idUser):
    response = getHistoryUserNow(idUser)
    if not (isinstance(response, list)):
        return response
    else:
        respuesta = {'error':str(response)}
        return respuesta