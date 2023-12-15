from flask import Flask, render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm

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