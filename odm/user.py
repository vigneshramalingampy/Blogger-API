
from mongoengine import *

class User(Document):
    userid= EmailField(unique=True)
    password= StringField()
    username=StringField()
    Description=StringField()
    rating= IntField()