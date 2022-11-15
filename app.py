from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


# Flask instance
app = Flask(__name__)

app.config['SECRET_KEY'] = "my super secret key that no one else knows"
# # old sqllite db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# new mysql db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///usersname:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/our_users'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    favorite_color = db.Column(db.String(120))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Name {self.name}>'

class UserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo('password_hash_confirm', message='Passwords Must Match')])
    password_hash_confirm = PasswordField('Cnfirm Password', validators=[DataRequired()])
    favorite_color = StringField('Favorite Color')
    submit = SubmitField('Submit')

class NamerForm(FlaskForm):
    name = StringField('name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            hashed_password = generate_password_hash(form.password_hash.data, 'sha256')
            user = Users(name=form.name.data, email=form.email.data, password_hash=hashed_password, favorite_color=form.favorite_color.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        form.password_hash.data = ''
        form.favorite_color.data = ''
        flash('User added successfully')
    our_users = Users.query.order_by(Users.date_added)
    return render_template('add_user.html', form=form, our_users=our_users, name=name)


@app.route('/user/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UserForm()
    user_to_update = Users.query.get_or_404(id)
    if request.method == 'POST':
        user_to_update.name = request.form['name']
        user_to_update.email = request.form['email']
        user_to_update.favorite_color = request.form['favorite_color']
        try:
            db.session.commit()
            flash('updated')
            return render_template('update.html', form=form, user_to_update=user_to_update)
        except:
            flash('failed')
            return render_template('update.html', form=form, user_to_update=user_to_update)
    else:
        return render_template('update.html', form=form, user_to_update=user_to_update, id=id)

@app.route('/delete/<int:id>')
def delete(id):
    name = None
    form = UserForm()
    user_to_delete = Users.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash('user deleted')
        our_users = Users.query.order_by(Users.date_added)
        return render_template('add_user.html', form=form, our_users=our_users, name=name)
    except:
        flash('not deleted')
        return render_template('add_user.html', form=form, our_users=our_users, name=name)

# route decorator
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def profile(name):
    return render_template('user.html', name=name)

# custom error page

#invalid error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

# Name page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    #validate
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
        flash('Form submitted successfully')
    return render_template('name.html', name=name, form=form)


class PasswordForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password_hash = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')



@app.route('/test', methods=['GET', 'POST'])
def test_pwd():
    email = None
    password = None
    pw_to_check = None
    passed = None
    form = PasswordForm()
    #validate
    if form.validate_on_submit():
        email = form.email.data
        password = form.password_hash.data
        form.email.data=''
        form.password_hash.data=''
        pw_to_check = Users.query.filter_by(email=email).first()

        passed = check_password_hash(pw_to_check.password_hash, password)

    return render_template('test.html', email=email, password=password, form=form, pw_to_check=pw_to_check, passed=passed)



# initiate
if __name__ == "__main__":
    app.run(debug=True, port=8000)