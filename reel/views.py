from reel import app
from flask import render_template


@app.route('/')
def home_welcome():
    return render_template("homepage.html")

@app.route('/signup')
def signup_welcome():
    return render_template("signuppage.html")

@app.route('/login')
def login_welcome():
    return render_template("loginpage.html")

@app.route('/become_a_guide')
def guide_welcome():
    return render_template("guidepage.html")

@app.route('/help')
def help_welcome():
    return render_template("helppage.html")

