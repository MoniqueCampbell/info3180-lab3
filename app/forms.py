#def ContactForm():
	# from flask_wtf import FlaskForm
	# from wtforms import StringField
	# from wtforms.validators import DataRequired
	# class MyForm(FlaskForm):
 # 	name = StringField('name',
	# validators=[DataRequired()])

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', render_kw={"rows": 5, "cols": 40}, validators=[DataRequired()])
