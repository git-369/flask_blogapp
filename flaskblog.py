from flask import Flask, render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '2cb5dbc2be7d290740d800c2aeac03ff'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username =db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120),unique=True, nullable=False)
	image_file = db.Column(db.String(20),nullable = False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	post = db.relationship('Post',backref='author',lazy=True)


	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
		id = db.Column(db.Integer, primary_key = True)
		title = db.Column(db.String(100), nullable = False)
		date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
		content = db.Column(db.Text, nullable=False)
		user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)


		def __repr__(self):
			return f"User('{self.title}','{self.date_posted}')"



posts = [
	{
	'title':'Blog 1',
	'author': 'Gitanjali M',
	'content': 'First Blog post content',
	'date_posted':'12 december 2023'
	},
	{
	'title':'Blog 2',
	'author': 'Gitanjali M',
	'content': 'Second Blog post content',
	'date_posted':'15 december 2023'
	}
]


@app.route("/")
def home():
	return render_template('home.html',posts=posts)

@app.route("/about")
def about():
	return render_template('about.html',title="About")

@app.route("/register", methods=['POST','GET'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account Created for {form.username.data}!','success')
		return redirect(url_for('home'))


	return render_template('register.html', title ="Sign Up", form=form)

@app.route("/login", methods=['POST','GET'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash(f'You have been logged in', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')


	return render_template('login.html', title="Login", form=form)

if __name__ == '__main__':
	app.run(debug=True)