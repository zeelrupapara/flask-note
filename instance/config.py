import os

db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')
db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
database_url = "mysql+pymysql://${}:${}@${}:${}/${}".format(
    db_username, db_password, db_host, db_port, db_name)

SECRET_KEY = 'secret key'
SQLALCHEMY_DATABASE_URI = database_url
ENV = 'development'
DEBUG = True
