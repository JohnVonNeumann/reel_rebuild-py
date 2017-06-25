from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def home_welcome():
    return 'Welcome to Reel!'

@app.route('/signup')
def signup_welcome():
    return 'Welcome to the signup page!'
