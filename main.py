
from flask import Flask
from api.user.AddUser import adduser
from api.blog.AddBlog import blog
from api.user.Update import updateuser
from api.user.Delete import deleteuser
from api.blog.update import updateblogdetails
from api.blog.display import displayall
app = Flask(__name__)

app.register_blueprint(adduser)
app.register_blueprint(blog)
app.register_blueprint(updateuser)
app.register_blueprint(deleteuser)
app.register_blueprint(updateblogdetails)
app.register_blueprint(displayall)
if __name__=='__main__':
    app.run(debug=True)