from flask import request,jsonify
from src.Controllers.recognitionController import getRecognitionAllController,getRecognitionUserController
def recognitionRoute (app):
    @app.route('/recognitions', methods = ['GET'])
    def recognition():
        if request.method == 'GET':
            if 'code' in request.args:
                code = request.args.get('code')
                response = getRecognitionUserController(code)
                return jsonify(
                        response = response
                    )
            else:
                response = getRecognitionAllController()
                return jsonify(
                        response = response
                    )