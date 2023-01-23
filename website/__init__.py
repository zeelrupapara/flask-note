from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # config
    app.config.from_pyfile('config.py')

    # db
    db.init_app(app)

    # blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    
    # migrations
    
    migrate.init_app(app, db)

    # for user seesion management
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    # reload the user object from the user ID stored in the session
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
