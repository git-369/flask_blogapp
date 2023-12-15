from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SECRET_KEY'] = '2cb5dbc2be7d290740d800c2aeac03ff'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db = SQLAlchemy(app)

from flaskblog import routes
