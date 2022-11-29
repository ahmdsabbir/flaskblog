from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField, SearchField
from wtforms.validators import DataRequired, EqualTo
from flask_wtf.file import FileField
from flask_ckeditor import CKEditorField

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = CKEditorField('Content', validators=[DataRequired()])
    author = StringField('Author')
    slug = StringField('slug', validators=[DataRequired()])
    submit = SubmitField('Post')

class UserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo('password_hash_confirm', message='Passwords Must Match')])
    password_hash_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    favorite_color = StringField('Favorite Color')
    about_author = TextAreaField('About yourself')
    submit = SubmitField('Submit')

class NamerForm(FlaskForm):
    name = StringField('name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    searched = StringField('searched', validators=[DataRequired()])
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