from reel import app
from flask import render_template


@app.route('/')
def home_welcome():
    return render_template('index.html') 

@app.route('/signup')
def signup_welcome():
    return 'Welcome to the signup page!'

@app.route('/login')
def login_welcome():
    return 'Welcome to the login page!'

@app.route('/become_a_guide')
def guide_welcome():
    return 'Welcome to the guide page!'

@app.route('/help')
def help_welcome():
    return 'Welcome to the help page!'

