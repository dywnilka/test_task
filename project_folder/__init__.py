from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.getcwd()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///order.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.json.sort_keys = False

import views
