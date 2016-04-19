import os

class Production(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass

class Development(Production):
    # Statement for enabling the development environment
    DEBUG = True

    # Define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

    # Define the database - we are working with
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:techla@localhost/apollo'
    ROOT_DATABASE_URI = 'postgresql://postgres:@localhost/apollo'
    SQLALCHEMY_MIGRATE_REPO = BASE_DIR + "/migrations"
