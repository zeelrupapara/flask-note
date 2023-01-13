from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import time
from flask_login import UserMixin
from sqlalchemy.sql import func

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    from .models import User, Note
    migrate.init_app(app, db)

    from .views import views
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    return app