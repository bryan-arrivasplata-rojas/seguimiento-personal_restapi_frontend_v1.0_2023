from flask import request,jsonify
from src.Controllers.historyController import postHistoryController,getHistoryController,getHistoryUserNowController

def historyRoute (app):
    @app.route('/histories', methods = [ 'POST', 'GET'])
    def history():
        if request.method == 'GET':
            if 'idUser' in request.args:
                idUser = request.args.get('idUser')
                response = getHistoryUserNowController(idUser)
                return jsonify(
                        response = response
                    )
            else:
                response = getHistoryController()
                return jsonify(
                        response = response
                    )
        if request.method == 'POST':
            idUser = request.form.get('idUser')
            idRecognition = request.form.get('idRecognition')
            response = postHistoryController(idUser,idRecognition)
            return jsonify(
                response = response
            )
        
        