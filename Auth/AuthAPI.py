# Score API here
from flask import Blueprint, request, jsonify, current_app
import sys
from db import db, creds
import jwt
sys.path.append("../")

auth_api = Blueprint("auth", __name__)


@auth_api.route('/register', methods = ["POST"])
def reg():
    
    def regdetails(argsform):
        username = argsform.get('username')
        hashedPassword = argsform.get('passwordHash')

        if (username == '') or (hashedPassword == ''):
            return jsonify({"Status" : "Failed", "Message" : "Username or Password not available"})
        else:
            creds.append({"username" : username, "passwordHash" : hashedPassword})
            return jsonify({"Status" : "Success", "Message" : "Registered"})

    if request.args.get('username'):
        return regdetails(request.args)

    elif request.form.get('username'):
        return regdetails(request.form)
    
@auth_api.route('/login', methods = ["POST"])
def login():

    def logindetails(argsform):
        username = argsform.get('username')
        hashedPassword = argsform.get('passwordHash')
        return username, hashedPassword

    if request.args.get('username'):
        det = logindetails(request.args)

    elif request.form.get('username'):
        det = logindetails(request.form)

    username = det[0]
    hashedPassword = det[1]

    checkuser = {"username":username, "passwordHash":hashedPassword}
    if checkuser in creds: #if the details match with stored username and pw, then encode.
        token = jwt.encode({'userID': username,
                            'passwordHash': hashedPassword
                            }, current_app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'Status': 'Success', 'token': token})

    return jsonify({'Status': 'Failed', 'Message': 'Username or Password does not match'})




