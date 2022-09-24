
from mongoengine import *
from flask import jsonify, request,Blueprint
from api.TokenDecorator import token_required
from odm.user import User
deleteuser = Blueprint("deleteuser",__name__)
#delete user --
@deleteuser.route("/deleteUser",methods=["DELETE"])
@token_required
def deleteUser(current_user):
    try:
        json_data=request.json
        id=json_data["id"]
        if(str(current_user[0].pk)==id):
            user=User(pk=id)
            if not user:
                return({"status":"user not exist"})
            user.delete()
            return({"status":"deleted successfully"})
        return({"status":"User not valid to perform this action"})    
    except Exception as e:
        return({"status":str(e)})