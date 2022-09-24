
from mongoengine import *
from odm.user import User
class BlogContent(EmbeddedDocument):
    title=StringField(Required=True)
    content=StringField(Required=True)
class comment(EmbeddedDocument):
    user=ReferenceField(User)
    username=StringField()
    comment=StringField()
class Blog(Document):
    user= ReferenceField(User)
    username=StringField()
    blog= EmbeddedDocumentField(BlogContent)
    comment=ListField(EmbeddedDocumentField(comment))
    likes=ListField()
    editedDate=DateField()
    postedDate=DateField()
    taglist=ListField(StringField())
