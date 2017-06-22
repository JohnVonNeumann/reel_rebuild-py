from flask import Flask
app = Flask(__name__)
app.config.from_envvar('SETTINGS')

@app.route('/')
def hello_world():
  return "Hello, World!"
