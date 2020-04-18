from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class HabitForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	submit = SubmitField('Create habit')

