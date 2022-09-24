# from datetime import datetime, timedelta
# import jwt
# def generateToken(userid):
#     token = jwt.encode({"userid":userid,"exp":datetime.utcnow()+timedelta(seconds=40)},"summaSecret",algorithm='HS256') 
#     return (token)
# token=generateToken("620dadea79cb0ca0fc1739e4")
# print(token)

from functools import wraps
from textwrap import wrap

import jwt
from odm.user import User
from api.user import AddUser
from flask import jsonify, request


def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message':'Token is missing!'}),401
        try:
            data = jwt.decode(token,AddUser.secret_key,algorithms=['HS256'])
            current_user = User.objects(pk=data['userid'])
        except Exception as e:
            return jsonify({'message':'Token is Invalid! - except {}'.format(e)}),401
        return f(current_user,*args,**kwargs)         
    return decorated


