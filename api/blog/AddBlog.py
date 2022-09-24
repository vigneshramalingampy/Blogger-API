
from datetime import datetime,date
import datetime
from mongoengine import *
from odm.user import User
from flask import Blueprint, Flask,request
from api.TokenDecorator import token_required
from odm.blog import Blog, BlogContent
blog =Blueprint("blog",__name__)
#to add a blog -- {"title":"computer scinence","content":"vignesh is a good boy","taglist":["summa","code2"]}
@blog.route("/addblog",methods=["POST"])
@token_required
def addBlog(current_user):
    json_data=request.json
    id=current_user[0].pk
    title=json_data['title']
    content= json_data['content']
    tagList=json_data['taglist']
    try:
        blog=Blog(user=current_user[0].pk,blog=BlogContent(title=title,content=content),taglist=tagList)
        blog.likes=[]
        blog.postedDate=date.today()
        blog.editedDate=date.today()
        blog.save()
        return({"status":"success"})
    except Exception as e:
        return(str(e))

#to update the blog -- {"id":"6209bccdbcf63061a96a1293","title":"computer scinence","content":"vignesh is a good boy","taglist":["summa","code2"]}        
@blog.route("/editblog",methods=["PUT"])
@token_required
def editblog(current_user):
    json_data= request.json
    id=json_data["id"]
    title=json_data["title"]
    content=json_data["content"]   
    tagList=json_data["taglist"]
    blog=Blog.objects(pk=id)
    try:
        if(current_user[0].pk==blog[0].user.pk):
            blog=Blog(pk=id)
            blog.update(blog=BlogContent(title=title,content=content),taglist=tagList,editedDate=date.today())
            return({"status":'successful'})
        return({"status":"User not valid to perform this action"})    
    except Exception as e:
        return({"status":str(e)})