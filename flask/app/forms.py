from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, PasswordField, FileField
from wtforms.validators import Email, DataRequired, EqualTo, InputRequired


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    age = IntegerField("Age", validators=[DataRequired()])
    button = SubmitField("Enter")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    button = SubmitField('Enter')


class File(FlaskForm):
    file = FileField('File')
    button = SubmitField("Enter")


class PostForm(FlaskForm):
    text = StringField('Text', validators=[DataRequired()])
    image = FileField('File', validators=[InputRequired()])
    button = SubmitField('Enter')