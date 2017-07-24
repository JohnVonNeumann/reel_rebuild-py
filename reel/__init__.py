from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.path.abspath('config.py')


db = SQLAlchemy(app)
import reel.views
app.config.from_pyfile(os.path.abspath('config.py'))

