# Author:       Trevor Strobel
# Date:         9/7/2022

from flask import Flask
from flask_sqlalchemy import SQLAlchemy





#create a flask instance
app = Flask(__name__)

# Configuration Parameters
app.config['SECRET_KEY'] = "e01e9bb75ed693f9c120d0d274092217"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create DB instance
db = SQLAlchemy(app)


from testapi import routes