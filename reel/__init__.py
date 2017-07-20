from flask import Flask
app = Flask(__name__)

import reel.views
app.config.from_pyfile(os.path.abspath('config.py')

