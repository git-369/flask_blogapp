from flask import Flask, render_template

app = Flask(__name__)

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



if __name__ == '__main__':
	app.run(debug=True)