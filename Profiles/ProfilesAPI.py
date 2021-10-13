# Profile API here
from flask import Blueprint, request, jsonify
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route('/<int:id>/', methods = ["GET"])
def getid(id):
    if id > len(db)-1:
        return jsonify({"Status" : "Error", "Message" : "No such ID"})

    else: 
        det = db[id]
        return jsonify({"Status" : "Success", "Details" : det})

@profiles_api.route('/profiles', methods = ["POST"])
def postid():
    newprofile = {}
    newprofname = request.args.get('name')
    newprofile["name"] = newprofname

    db.append(newprofile)

    return jsonify({"Status" : "Success", "Details" : newprofile})


@profiles_api.route('/<int:id>/', methods = ["DELETE"])
def deleteid(id):
    if id > len(db)-1:
        return jsonify({"Status" : "Error", "Message" : "No such ID"})

    else:
        deleteddetails = db[id]
        del db[id]

        return jsonify({"Status" : "Success", "New db" : db, "Deleted profile" : deleteddetails})


@profiles_api.route('/<int:id>/score', methods = ["GET"])
def getabovemin(id):
    if id > len(db)-1:
        return jsonify({"Status" : "Error", "Message" : "No such ID"})

    minscore = request.args.get('minScore')
    scores = db[id]["scores"]

    if minscore == '':
        return jsonify({"Status" : "Success", "Details" : scores})
    
    abovemin = list(filter(lambda score: score > int(minscore), scores))
    

    return jsonify({"Status" : "Success", "Details" : abovemin})


    
