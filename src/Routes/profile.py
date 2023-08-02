from flask import request,jsonify
from src.Controllers.profileController import postProfileController,getProfileEmailController,getProfileUserController

def profileRoute (app):
    @app.route('/profiles', methods = [ 'POST', 'GET'])
    def profile():
        if request.method == 'GET':
            if 'email' in request.args:
                email = request.args.get('email')
                response = getProfileEmailController(email)
                return jsonify(
                    response = response
                )
            else:
                idUser = request.args.get('idUser')
                response = getProfileUserController(idUser)
                return jsonify(
                    response = response
                )
        if request.method == 'POST':
            name = request.form.get('name')
            lastName = request.form.get('lastName')
            birthday = request.form.get('birthday')
            number = request.form.get('number')
            email = request.form.get('email')
            securityResponse = request.form.get('securityResponse')
            response = postProfileController(name,lastName,number,birthday,email,securityResponse)
            return jsonify(
                response = response
            )