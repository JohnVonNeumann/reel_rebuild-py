from flask import Flask 
app = Flask(__name__) 
app.config.from_pyfile('/home/xibalba/code/reel/config.py') 
 
import reel.views

