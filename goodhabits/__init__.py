from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from goodhabits.config import Config
# from flask_mail import Mail
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


# mail = Mail()

migrate = Migrate()

def create_app(config_class=Config):
	app = Flask(__name__)

	app.config.from_object(Config)	

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	# mail.init_app(app)
	migrate.init_app(app, db)

	from goodhabits.users.routes import users
	app.register_blueprint(users)

	from goodhabits.habits.routes import habits
	app.register_blueprint(habits)

	from goodhabits.main.routes import main
	app.register_blueprint(main)

	from goodhabits.errors.handlers import errors
	app.register_blueprint(errors)

	return app

