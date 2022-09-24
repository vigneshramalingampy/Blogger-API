from datetime import datetime, timedelta
from flask import jsonify, make_response,request
from flask import Blueprint
import jwt
from mongoengine import *
from odm.user import User
from odm.blog import Blog
adduser = Blueprint("adduser",__name__)
secret_key = "secretkey"
connect(db='Blog_db',host='127.0.0.1',port=27017)
#create user -- 
@adduser.route('/addUser',methods=["POST"])
def addUser():
    json_data= request.json
    try:
        user=User()
        user.userid=json_data["userid"]
        user.password=json_data["password"]
        user.username=json_data["username"]
        user.Description=""
        user.rating=0

        user.save()
        return({"status":"successful"})
    except NotUniqueError:
            return({"status":"unsuccessful"})
    
#login user -- 
@adduser.route('/login',methods=["POST"])
def login():
    auth= request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify',401,{'WWW-Authenticate':'Basic realm ="Login required"'})
    user= User.objects(userid=auth.username)
    password=user[0].password
    id = user[0].pk

    if not user:
        return make_response('Could not verify',401,{'WWW-Authenticate':'Basic realm="Login required!"'})
    if (password == auth.password):
        token = jwt.encode({'userid':str(id),'exp':datetime.utcnow()+timedelta(hours=3)},secret_key,algorithm='HS256')       
        return jsonify({'token':str(token)})
    return make_response('Could not verify',401,{'WWW-Authenticate':'Basic realm="Login required!"'})
