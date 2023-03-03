import os

db_host = os.getenv('DB_HOST', default="db")
db_port = os.getenv('DB_PORT', default="3306")
db_name = os.getenv('DB_NAME', default="note")
db_username = os.getenv('DB_USERNAME', default="note")
db_password = os.getenv('DB_PASSWORD', default="note")
database_url = "mysql+pymysql://{}:{}@{}:{}/{}".format(
    db_username, db_password, db_host, db_port, db_name)

SECRET_KEY = 'secret key'
SQLALCHEMY_DATABASE_URI = database_url
ENV = 'development'
DEBUG = True