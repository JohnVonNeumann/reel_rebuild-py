from reel import app
from flask import render_template


@app.route('/')
def home_welcome(page_title="Home"):
    return render_template("homepage.html", page_title = page_title)

@app.route('/signup')
def signup_welcome(page_title="Signup"):
    return render_template("signuppage.html", page_title = page_title)

@app.route('/login')
def login_welcome(page_title="Login"):
    return render_template("loginpage.html", page_title = page_title)

@app.route('/become_a_guide')
def guide_welcome(page_title="Become a Guide"):
    return render_template("guidepage.html", page_title = page_title)

@app.route('/help')
def help_welcome(page_title="Help"):
    return render_template("helppage.html", page_title = page_title)

