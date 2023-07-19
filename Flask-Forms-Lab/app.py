from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "siwarha"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]


@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method=='GET':
		return render_template('login.html')
	else:
		user=request.form['username']
		word=request.form['password']
		if username==user and password==word:
			return redirect(url_for('home'))

@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('home.html',facebook_friends=facebook_friends)

@app.route('/friend_exists/<string:name>')
def check(name):
	return render_template('friend_exists.html',st=name in facebook_friends)

  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True, port=5001
	)
