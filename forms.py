from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length

class PostForm(FlaskForm):
    title = StringField('Ttle', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    slug = StringField('slug', validators=[DataRequired()])
    submit = SubmitField('Post')

class UserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo('password_hash_confirm', message='Passwords Must Match')])
    password_hash_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    favorite_color = StringField('Favorite Color')
    submit = SubmitField('Submit')

class NamerForm(FlaskForm):
    name = StringField('name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PasswordForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password_hash = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

# login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')