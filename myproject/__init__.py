import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

### Database configuration ###
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///'+os.path.join(basedir,'data.sqlite')

db = SQLAlchemy(app)
Migrate(app,db)


### Creating Login Manager ###
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

### Blueprint configuration###
from myproject.core.views import core
from myproject.users.views import users
from myproject.blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
