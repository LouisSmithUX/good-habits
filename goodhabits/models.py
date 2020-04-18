from datetime import datetime
from goodhabits import db, login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model,UserMixin):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20),unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	habits = db.relationship('Habit', backref='owner', lazy=True)

	def get_reset_token(self, exprires_sec=1800):
		s = Serializer(current_app.config['SECRET_KEY'], exprires_sec)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			user_id = s.loads(token)['user_id']
		except:
			return None
		return User.query.get(user_id)

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"


class Habit(db.Model):
	__tablename__ = 'habits'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	date_created = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	events = db.relationship('HabitEvent', backref='habit', lazy=True)


	def __repr__(self):
		return f"Habit('{self.name}','{self.date_created}','{self.user_id}')"

class HabitEvent(db.Model):
	__tablename__ = 'habitevent'
	id = db.Column(db.Integer, primary_key=True)
	date_occurred = db.Column(db.Date, nullable= False)
	age = db.Column(db.Integer)
	habit_id = db.Column(db.Integer, db.ForeignKey('habits.id'), nullable=False)

	def __repr__(self):
		return f"HabitEvent('{self.date_occurred}','{self.habit_id}')"