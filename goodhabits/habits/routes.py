from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint,jsonify)
from flask_login import current_user, login_required
from goodhabits import db
from goodhabits.models import HabitEvent, Habit
from goodhabits.habits.forms import HabitForm
from datetime import datetime, timedelta

habits = Blueprint('habits', __name__)

@habits.route('/habit_event/new', methods=["POST"])
# @login_required
def new_habit_event():
	request_data= request.get_json()
	day = datetime.strptime(request_data['date'],'%Y-%m-%d')
	previous_day = day - timedelta(1)

	existing_event = HabitEvent.query.filter_by(habit_id=request_data['habit'],date_occurred=day).first()
	previous_day_event = HabitEvent.query.filter_by(habit_id=request_data['habit'],date_occurred=previous_day).first()
	
	if existing_event:
		db.session.delete(existing_event)
		db.session.commit()
		return jsonify(age=0), 201
	else:
		habit = Habit.query.filter_by(id=request_data['habit']).first_or_404()
		age = previous_day_event.age + 1 if (previous_day_event and previous_day_event.age) else 1
		habit_event = HabitEvent(habit=habit, date_occurred=day, age=age)
		db.session.add(habit_event)
		db.session.commit()
		return jsonify(age=age), 201

@habits.route('/habit/delete', methods=['POST'])
def deleteHabit():
	request_data = request.get_json()

	habit = Habit.query.filter_by(id=request_data['habit_id']).first_or_404()
	habit_event = HabitEvent.query.filter_by(habit=habit).all()
	for h_e in habit_event:
		db.session.delete(h_e)
	db.session.delete(habit)
	db.session.commit()
	return 'Done', 201