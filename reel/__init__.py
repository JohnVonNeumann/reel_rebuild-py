from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import reel.views

 
app = Flask(__name__) 
db = SQLAlchemy(app)
app.config.from_pyfile('/home/xibalba/code/reel/config.py') 
 

