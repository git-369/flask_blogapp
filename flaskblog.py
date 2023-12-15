from flask import Flask, render_template,url_for
from form import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '2cb5dbc2be7d290740d800c2aeac03ff'

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
def hello():
	return render_template('home.html',posts=posts)

@app.route("/about")
def about():
	return render_template('about.html',title="About")

@app.route("/register")
def register():
	form = RegistrationForm()

	return render_template('register.html', title ="Sign Up", form=form)

@app.route("/login")
def login():
	form = LoginForm()

	return render_template('login.html', title="Login", form=form)

if __name__ == '__main__':
	app.run(debug=True)