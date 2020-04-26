from flask import render_template, request, Blueprint, flash,redirect, url_for, Flask, send_from_directory
from goodhabits.models import Habit
from goodhabits.habits.forms import HabitForm
from flask_login import current_user, login_required
from goodhabits import db
import itertools
from datetime import datetime, date, timedelta

main = Blueprint('main', __name__)


@main.route("/", methods=["GET","POST"])
@main.route("/home", methods=["GET","POST"])
def home():

	if (current_user.is_authenticated is False):
		return render_template('landing.html')

	month = request.args.get('month')
	month = month if month else datetime.today().strftime("%Y-%m")
	current_month = datetime.strptime(month, '%Y-%m')

	next_month = (current_month + timedelta(days=45)).replace(day=1)
	prev_month = (current_month - timedelta(days=15)).replace(day=1)
	months={'prev_month':prev_month,'current_month':current_month,'next_month':next_month}

	habits = Habit.query.filter_by(owner=current_user).all()

	calendar_query =\
"""SELECT 
dd::DATE as day_number,
h.id as habit,
h_e.age as habit_events
FROM generate_series
        ( (date_trunc('month', date '{month}') - INTERVAL '2 day')::timestamp 
        , (date_trunc('month', date '{month}') + INTERVAL '31 day')::timestamp
        , '1 day'::interval) dd
JOIN habits h ON h.user_id = {current_user_id}
LEFT JOIN habitevent h_E ON h_e.habit_id = h.id AND h_e.date_occurred::DATE = dd::DATE
ORDER BY dd::DATE ASC, habit ASC;"""\
.format(current_user_id=current_user.id,month=month+'-01');
	calendar = db.session.execute(calendar_query).fetchall()

	calendar = [{'date':key,'events':list(group)} for key,group in itertools.groupby(calendar, key=lambda x:x[0])]
	form = HabitForm()
	if form.validate_on_submit():
		habit = Habit(name=form.name.data, owner=current_user)
		db.session.add(habit)
		db.session.commit()
		flash('Your habit has been created!', 'success')
		return redirect(url_for('main.home'))

	return render_template('home.html', title='Home', form=form, habits=habits, calendar=calendar, today=date.today(),months=months)



@main.route("/landing")
def landing():
	return render_template('landing.html')


@main.route('/robots.txt')
@main.route('/sitemap.xml')
def static_from_root():
    return send_from_directory('static', request.path[1:])