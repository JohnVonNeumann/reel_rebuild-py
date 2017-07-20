import os
basedir = os.path.abspath(os.path.dirname(__name__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQL_ALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    PRODUCTION = True

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    DEVELOPMENT = True
