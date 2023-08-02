from flask import request,jsonify
from src.Controllers.roleController import getRoleAllController
def roleRoute (app):
    @app.route('/roles', methods = ['GET'])
    def role():
        if request.method == 'GET':
            response = getRoleAllController()
            return jsonify(
                response = response
            )