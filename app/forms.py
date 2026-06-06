from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired

class Resgistration_form(FlaskForm):
    fullname = StringField('Full name ', validators=[DataRequired()])
    email = EmailField('Email Address ', validators=[DataRequired(), Email()])
    password = PasswordField('Create password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min= 6), EqualTo('password')])
    submit = SubmitField('Sign up',)

class Login_form(FlaskForm):
    email = EmailField('Email Address ', validators=[DataRequired(), Email()])
    password = PasswordField('Password ', validators=[DataRequired(), Length(min=6)])
    login = SubmitField("Login",)

class Task_form(FlaskForm):
    task = StringField('Task',validators=[DataRequired()])
    add = SubmitField('Add',)

class Task_update(FlaskForm):
    update_task = StringField('Update Task', validators=[DataRequired()])
    update = SubmitField('Update Task',)