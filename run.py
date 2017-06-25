from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def home_welcome():
    return 'Welcome to Reel!'

@app.route('/signup')
def signup_welcome():
    return 'Welcome to the signup page!'

@app.route('/login')
def login_welcome():
    return 'Welcome to the login page!'

@app.route('/become_a_guide')
def guide_welcome():
    return 'Welcome to the guide page!'
