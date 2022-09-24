

from mongoengine import *
import json
from api.TokenDecorator import token_required
from flask import jsonify, request,Blueprint
from odm.blog import Blog
displayall = Blueprint("displayall",__name__)

@displayall.route("/allblog")
@token_required
def func(val):
    blog=Blog.objects()
    blogjsonstring=json.loads(blog.to_json())
    return({"status":"successful","data":blogjsonstring})