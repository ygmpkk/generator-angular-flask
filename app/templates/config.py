import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG   = False
    TESTING = False

class Development(Config):
    DEBUG   = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

class Production(Config):
    SQLALCHEMY_DATABASE_URI = '' #'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

class Testing(Config):
    DEBUG   = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

