from mongoengine import *
from flask import request,Blueprint
from api.TokenDecorator import token_required
from odm.user import User
updateuser = Blueprint("updateuser",__name__)
#update description for user --
@updateuser.route("/updatedesc",methods=["PUT"])
@token_required
def updatedesc(current_user):
    json_data=request.json
    id=json_data["id"]
    desc=json_data["description"]
    try:
        if(str(current_user[0].pk)==id):
            user=User(pk=id)
            if not user:
                return({"status":"user not exist"})
            user.update(Description=desc)
            return({"status":"successful"})
    except Exception as e:
        return({"status":str(e)})    
