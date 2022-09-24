
from datetime import date
from mongoengine import *
from flask import jsonify, request,Blueprint
from api.TokenDecorator import token_required
from odm.user import User
from odm.blog import Blog, comment
updateblogdetails = Blueprint("updateblogdetails",__name__)

#to add comment -- {"id":"id of blog","user":"userid of commentator","comment":"_____"}
@updateblogdetails.route("/addcomment",methods=["POST"])
@token_required
def addcomments(current_user):
    json_data=request.json
    id=json_data["id"]
    commentedUser = current_user[0].pk
    username = User.objects.get(pk=commentedUser)
    comment = json_data["comment"]

    blog=Blog.objects(pk=id)
    commentlist=blog[0].comment
    commentlist=list(commentlist)
    commentDict = {"user":commentedUser,"username":str(username),"comment":comment}
    commentlist.append(commentDict)
    blog.update(comment=commentlist)
    return({"status":"success"})


#to delete a comment using index   -  {"id":"id of blog","user":"current user id for verification","index":1}
@updateblogdetails.route("/deletecomment",methods=["DELETE"])
@token_required
def deletecomments():
    json_data=request.json
    id=json_data["id"]
    user= json_data["user"]
    commentindex= json_data["index"]
    blog=Blog.objects(pk=id)
    useridfromcomment=blog[0].comment[commentindex].user
    if not blog:
        return({"status":"blog not exist"})
    commentlist=blog[0].comment
    commentlist=list(commentlist)
    if(len(commentlist)<commentindex):
        return({"status":"index mismatch"})   
    if(str(useridfromcomment.pk)==user) :        
        commentlist.pop(commentindex)
    blog.update(comment=commentlist)
    return({"status":"success"})

@updateblogdetails.route("/edittags",methods=["PUT"])
@token_required
def edittags(current_user):
    json_data=request.json
    id=json_data["id"]
    if(str(current_user[0].pk) !=id):
        return ({"status": "user has no access to this record"})
    tagList= json_data["taglist"]
    blog=Blog.objects(pk=id)
    if not blog:
        return({"status":"blog not exist"})

    blog.update(taglist=tagList,editeddate=date.today())
    return({"status":"success"})

@updateblogdetails.route("/editlikes",methods=["POST"])
@token_required
def editlikes(current_user):
    userid = current_user[0].pk
    postid= request.json["id"]
    blog=Blog.objects(pk=postid)
    val=list(blog[0].likes)
    val.append(userid)
    blog.update(likes=val)
    return({"status":"success"})



       
